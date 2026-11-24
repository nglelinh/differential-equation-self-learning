---
layout: post
title: "13-10 Ứng dụng hiện đại: Bộ giải khả vi và neural SDE"
chapter: '13'
order: 10
owner: Course Team
lang: vi
categories:
- chapter13
lesson_type: optional
---

Điều gì xảy ra khi ta đặt một bộ giải Runge–Kutta hay Euler–Maruyama *ngay bên trong* đồ thị tính toán của PyTorch/JAX để mạng nơ-ron học trực tiếp trường vector $f_\theta(y, t)$ của hệ động lực? Đó chính là cuộc cách mạng **Neural ODE, Neural SDE và Bộ giải Khả vi (Differentiable Solvers)**: thay vì lưu hàng nghìn bước trung gian làm tràn bộ nhớ GPU, ta giải ngược một **phương trình liên hợp (Adjoint ODE)** để tính gradient $\nabla_\theta \mathcal{L}$ với bộ nhớ $O(1)$!

## Bản đồ kiến thức nền: Bốn trụ cột của Bộ giải Khả vi & Neural SDE

1. **Neural ODE ($y'(t) = f_\theta(y(t), t)$) như giới hạn liên tục của ResNet**:
   Mỗi tầng mạng phần dư $y_{k+1} = y_k + h f_{\theta_k}(y_k)$ chính là một bước Euler; cho $h \to 0$ biến mạng sâu thành một ODE liên tục với bộ giải thích nghi bước thời gian!
2. **Hai chiến lược tính Gradient: Discretize-then-Optimize vs. Optimize-then-Discretize**:
   *Lan truyền ngược trực tiếp* qua từng bước RK cho gradient rời rạc chính xác nhưng tốn bộ nhớ $O(N)$; *Phương pháp Liên hợp liên tục (Adjoint Method)* giải ODE ngược thời gian $a'(t) = -a(t)^\top \frac{\partial f_\theta}{\partial y}$ với bộ nhớ $O(1)$!
3. **Neural SDE ($dY_t = \mu_\theta(Y_t, t)\,dt + \sigma_\theta(Y_t, t)\,dW_t$)**:
   Bổ sung thành phần nhiễu Brownian học được giúp mô hình hóa bất định, sinh chuỗi thời gian tài chính/y sinh và kết nối trực tiếp với **Mô hình Khuếch tán (Diffusion Models)** tạo ảnh hiện đại!
4. **Ổn định Số trong Huấn luyện (Stiffness & Gradient Exploding)**:
   Nếu mạng $f_\theta$ trở nên "cứng" trong lúc huấn luyện, bộ giải hiện sẽ phải băm nhỏ bước thời gian tới mức treo máy—đòi hỏi điều chuẩn Lipschitz hoặc bộ giải ẩn khả vi.

## Mục tiêu

Bài học tùy chọn này đặt các phương pháp Euler, Runge–Kutta, bài toán cứng, điều kiện CFL và lược đồ Euler–Maruyama làm nền tảng số của tính toán khoa học khả vi. Sinh viên cần giải thích được cách lấy đạo hàm lan truyền ngược (reverse-mode) qua một bộ giải, nắm vai trò của `torchdiffeq` và Diffrax, đồng thời kết nối neural SDE với các mô hình khuếch tán dựa trên score phổ biến trong giai đoạn 2021–2024. Lý thuyết nhất quán và ổn định cổ điển của chương vẫn giữ nguyên giá trị cốt lõi.

## Kiến thức nền

Sinh viên cần nắm phương pháp Euler tiến và Euler lùi, RK4, miền ổn định tuyến tính, điều kiện CFL và lược đồ Euler–Maruyama cho SDE. Bài 13.00 về rời rạc hóa và ổn định là phần chuẩn bị trực tiếp cho nội dung này.

## Dẫn nhập

Một phương pháp số thực chất là ánh xạ từ trường vector và bước lưới sang quỹ đạo rời rạc. Nếu ánh xạ đó khả vi, ta có thể đặt nó trực tiếp bên trong vòng lặp huấn luyện để tối ưu hóa tham số của trường vector, bộ điều khiển hoặc số hạng đóng (closure) bằng hạ gradient. Chen và cộng sự (NeurIPS 2018) đã phổ biến phương pháp liên hợp (adjoint) cho neural ODE. Luận án năm 2022 của Kidger ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) cùng thư viện Diffrax ([https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)) đã đưa toàn bộ hệ thống bộ giải của chương này — ODE hiện và ẩn, CDE, SDE, bước thích nghi — thành các thành phần tính toán gốc trong JAX; `torchdiffeq` ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) thực hiện mục tiêu tương tự trong PyTorch.

Ở nhánh ngẫu nhiên, Kidger, Foster, Li và Lyons (*Neural SDEs as Infinite-Dimensional GANs*, ICML 2021; *Efficient and Accurate Gradients for Neural SDEs*, NeurIPS 2021) chỉ ra cách lan truyền ngược qua bộ giải SDE. Song và cộng sự (ICLR 2021) sử dụng SDE khuếch tán làm mô hình sinh dữ liệu. Các vấn đề giải tích số cốt lõi vẫn giữ nguyên như trong chương: sai số mạnh so với sai số yếu, độ cứng và tính ổn định của lược đồ Euler–Maruyama.


### Khung giải thích (nên đọc chậm): Tính tay gradient bằng Phương pháp Liên hợp (Adjoint) mà không cần lưu lịch sử bước

Xét Neural ODE cực giản $y'(t) = \theta y(t)$, $y(0) = 1$ trên $[0, 1]$ với hàm mất mát $\mathcal{L} = \frac{1}{2}(y(1) - 2)^2$, cần tính $\frac{d\mathcal{L}}{d\theta}$ tại $\theta = 0$:
1. **Lượt xuôi (Forward)**: Tại $\theta = 0$, $y'(t) = 0 \implies y(t) \equiv 1$ trên toàn $[0, 1]$, nên $y(1) = 1$.
2. **Lượt ngược Liên hợp (Adjoint ODE)**:
   Điều kiện cuối $a(1) = \frac{\partial \mathcal{L}}{\partial y(1)} = y(1) - 2 = \mathbf{-1}$, và phương trình liên hợp $a'(t) = -\frac{\partial(\theta y)}{\partial y} a(t) = -0 \cdot a(t) = 0 \implies a(t) \equiv \mathbf{-1}$.
3. **Tích phân gradient theo tham số $\theta$**:
   $$\frac{d\mathcal{L}}{d\theta} = \int_0^1 a(t)\frac{\partial(\theta y)}{\partial \theta}\,dt = \int_0^1 (-1) \cdot 1\,dt = \mathbf{-1}.$$
   Kiểm tra bằng giải tích trực tiếp: $\mathcal{L}(\theta) = \frac{1}{2}(e^\theta - 2)^2 \implies \mathcal{L}'(0) = (e^0 - 2)e^0 = \mathbf{-1}$—khớp tuyệt đối!
## Khái niệm then chốt

### Lấy đạo hàm qua ánh xạ một bước

Lược đồ Euler tiến $$y_{n+1}=y_n+h f_\theta(y_n)$$ có ma trận Jacobian là $$I+h Df_\theta(y_n)$$. Phép vi phân tự động chế độ ngược (reverse-mode autodiff) nhân ngược các ma trận Jacobian này lại, tương ứng với phương pháp liên hợp rời rạc (discrete adjoint). Với Euler ẩn, mỗi bước đòi hỏi giải một hệ phương trình, và định lý hàm ẩn cung cấp biểu thức Jacobian tương ứng. Bài toán cứng đòi hỏi phương pháp liên hợp ẩn thay vì hiện, vì cùng lý do ổn định như ở chiều thuận.

### Phương pháp liên hợp liên tục và lưu mốc (checkpointing)

Phương pháp liên hợp liên tục của Chen và cộng sự tích phân ngược một ODE phụ để tiết kiệm bộ nhớ, nhưng phải đánh đổi bằng một sai số rời rạc hóa mới ở chiều ngược. Diffrax hỗ trợ cả hai cách tiếp cận *discretize-then-optimize* và *optimize-then-discretize*: lựa chọn giữa việc lấy gradient chính xác của lược đồ rời rạc hay xấp xỉ gradient của bài toán liên tục. Đây là hai đối tượng khác nhau, và phân tích sai số cục bộ trong chương áp dụng cho cả hai.

### Neural SDE và mô hình khuếch tán dựa trên score

Một neural SDE có dạng:

$$
dX_t = b_\theta(t,X_t)\,dt + \sigma_\theta(t,X_t)\,dW_t
$$

là một quá trình Itô có tham số học được. Việc huấn luyện đòi hỏi phương pháp liên hợp ngẫu nhiên và phải tái tạo chính xác cùng một quỹ đạo chuyển động Brown trên lượt ngược (Kidger và cộng sự, NeurIPS 2021). Trong khi đó, mô hình sinh dựa trên score sử dụng một SDE thuận cho trước và chỉ học hàm score xác định số hạng trôi ngược. Euler–Maruyama là bộ lấy mẫu cơ sở, còn các lược đồ SDE bậc cao hơn và dạng dự đoán–hiệu chỉnh (predictor–corrector) là những cải tiến giai đoạn 2021–2024; miền ổn định của lược đồ vẫn quyết định liệu bước thời gian ngược lớn có bị mất ổn định hay không.

### Điều kiện CFL và bộ bước thời gian PDE học được

Một bộ cập nhật thời gian học bằng mạng nơ-ron cho PDE vẫn có thể vi phạm điều kiện CFL ngay cả khi từng khung trạng thái trông mượt. Brandstetter, Worrall và Welling (*Message Passing Neural PDE Solvers*, ICLR 2022; [arXiv:2202.03376](https://arxiv.org/abs/2202.03376)) và bộ chuẩn PDEBench (Takamoto và cộng sự, NeurIPS 2022; [arXiv:2210.07182](https://arxiv.org/abs/2210.07182)) minh họa rõ hiện tượng này qua thực nghiệm. Việc dự báo ổn định trong 10 bước nhưng bùng nổ ở bước thứ 100 chính là bài toán ổn định số cổ điển, nay xuất hiện với thông lượng được tham số hóa bằng mạng nơ-ron.

## Phương pháp và kỹ thuật

1. Chọn lược đồ thuận có miền ổn định bao trùm phổ dự kiến (Runge–Kutta tường minh cho ODE không cứng, phương pháp ẩn hoặc hàm mũ cho ODE cứng, lược đồ thỏa điều kiện CFL cho PDE hyperbolic, Euler–Maruyama hoặc bậc cao hơn cho SDE).
2. Lựa chọn giữa vi phân tự động chính xác trên lược đồ rời rạc và phương pháp liên hợp liên tục.
3. Thiết lập dung sai đủ chặt để nhiễu từ bộ giải không làm lệch hướng gradient.
4. Với SDE, lưu trữ hoặc tái tạo chính xác cùng dãy gia số Brown trên lượt tính ngược.
5. Kiểm chứng bằng nghiệm tự tạo (manufactured solutions), phép thử ổn định tuyến tính và chạy dự báo nhiều bước (roll-out) dài hạn.

Tài liệu kỹ thuật của thư viện cũng là một phần quan trọng của quy trình: sinh viên nên tham khảo giao diện bộ giải của Diffrax và `odeint_adjoint` trong `torchdiffeq` trước khi tự xây dựng quy tắc lan truyền ngược.

## Ví dụ

### Ví dụ 1: Liên hợp cho Euler ẩn

Với bài toán thử $$y'=-\lambda y$$, lược đồ Euler ẩn cho $$y_{n+1}=y_n/(1+h\lambda)$$. Đạo hàm của $$y_{n+1}$$ theo $$\lambda$$ có thể tính trực tiếp bằng giải tích sơ cấp và phải khớp với kết quả từ vi phân tự động. Ngược lại, gradient của Euler tường minh khi $$h\lambda$$ lớn được tính dọc theo một quỹ đạo thuận đã mất ổn định nên không còn ý nghĩa.

### Ví dụ 2: Sai số mạnh của Euler–Maruyama

Lược đồ $$X_{n+1}=X_n+h b(X_n)+\sqrt{h}\,\sigma(X_n)\xi_n$$ nói chung chỉ có bậc hội tụ mạnh bằng $$1/2$$. Một neural SDE huấn luyện bằng hàm mất mát theo từng quỹ đạo không thể vượt qua giới hạn hội tụ này trừ khi nâng cấp lược đồ số. Ngược lại, hàm mất mát yếu (so sánh phân phối) cho phép dùng tiêu chuẩn hội tụ yếu hơn — đó là lý do các bộ lấy mẫu trong mô hình sinh thường chú trọng sai số yếu.

### Ví dụ 3: Minh họa bộ giải ODE làm chuẩn đối chiếu

```python
import numpy as np
from scipy.integrate import solve_ivp

def f(t, y, theta=0.8):
    return -theta * y

sol = solve_ivp(f, [0, 2], [1.0], rtol=1e-6, atol=1e-6)
print(sol.y[0, -1], np.exp(-0.8 * 2))
```

Một bộ giải khả vi thay `solve_ivp` bằng một toán tử vừa tính nghiệm thuận vừa trả về $$\partial y(T)/\partial\theta$$; tuy nhiên giá trị nghiệm thuận vẫn phải khớp với phép kiểm chứng chuẩn như trên.

## Ứng dụng

Bộ giải khả vi hiện là thành phần chuẩn trong neural ODE, phương trình vi phân phổ quát (Rackauckas và cộng sự, 2021, và hệ sinh thái SciML), nhận dạng hệ thống và điều khiển tối ưu. Neural SDE được dùng để mô hình hóa chuỗi thời gian tài chính lấy mẫu không đều, động học phân tử và các quá trình ngẫu nhiên ẩn. Các SDE dựa trên score được ứng dụng rộng rãi trong sinh ảnh, thiết kế phân tử và các bài toán ngược trong xử lý ảnh. PDEBench (2022) cùng các bộ dữ liệu chuẩn gần đây như The Well (Ohana và cộng sự, NeurIPS 2024) cung cấp bài kiểm tra dự báo nhiều bước công khai để đối chiếu bộ bước thời gian học được với các phương pháp số cổ điển của chương.

Trong kỹ thuật, bộ giải động lực học chất lưu (CFD) hoặc mạch điện khả vi cho phép tối ưu hóa hình học và tham số bằng cùng kỹ thuật liên hợp vốn đã quen thuộc hàng thập kỷ trong lý thuyết điều khiển tối ưu; điểm mới là phần dư phương trình có thể chứa trực tiếp một mạng nơ-ron.

## Thách thức và hướng mở rộng

Phương pháp liên hợp trên quỹ đạo hỗn loạn dài thường mất ổn định do độ nhạy theo điều kiện đầu; các kỹ thuật shadowing và least-squares shadowing vẫn đang là hướng nghiên cứu mở. Bộ giải ẩn làm tăng chi phí tính toán ở lượt ngược, còn liên hợp ngẫu nhiên đòi hỏi cơ chế tái tạo nhiễu chính xác. Bộ bước thời gian PDE học được dễ bị quá khớp trên khoảng thời gian dự báo ngắn, và các hệ lai rời rạc–liên tục làm hỏng phép vi phân tự động thông thường. Không một cải tiến học máy nào thay thế được tính A-ổn định hay điều kiện CFL; ngược lại, chúng làm nổi bật hơn nữa giá trị của các nguyên lý số cổ điển này.

Một câu hỏi thực tế quan trọng: nếu gradient từ liên hợp liên tục và liên hợp rời rạc lệch nhau $$10\%$$, ta nên tin kết quả nào cho quá trình tối ưu đang chạy? Theo quan điểm giải tích số của chương, nên dùng liên hợp rời rạc vì đó mới là gradient chính xác của thuật toán số thực sự đang được triển khai.

## Video tham khảo

- xem trước: [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, tiếng Anh. Giới thiệu neural ODE và bộ giải khả vi — chủ đề trọng tâm của bài.
- [Latent Stochastic Differential Equations for Irregularly-Sampled Time Series - David Duvenaud](https://www.youtube.com/watch?v=93wr5vhI0F4) — Institute for Advanced Study, tiếng Anh. Trình bày phương trình vi phân ngẫu nhiên ẩn cho dữ liệu chuỗi thời gian lấy mẫu không đều.
- [On Neural Differential Equations](https://www.youtube.com/watch?v=TGfGiBhDEi0) — Patrick Kidger, tiếng Anh. Bài giảng của Patrick Kidger về cơ sở toán học và kỹ thuật huấn luyện qua bộ giải phương trình vi phân.

## Bài tập

1. **Miền ổn định và bước thời gian học được.** Với $$y'=\lambda y$$, viết hệ số khuếch đại của RK4. Trong vùng giá trị nào của $$h\lambda$$ thì một bộ cập nhật phần dư nơ-ron có thể sử dụng RK4 làm lược đồ bên trong mà vẫn ổn định?

2. **Liên hợp rời rạc và liên hợp liên tục.** Với một bước Euler ẩn áp dụng cho $$y'=-\theta y$$, hãy tính cả gradient chính xác của ánh xạ số lẫn kết quả từ liên hợp liên tục đánh giá tại bước đó. Khi nào hai giá trị này khớp nhau?

3. **Sai số mạnh và sai số yếu.** Giải thích vì sao một bộ lấy mẫu theo mô hình score có thể chấp nhận lược đồ có bậc hội tụ mạnh thấp nếu tiêu chí đánh giá mục tiêu là khoảng cách giữa hai phân phối.

4. **Thí nghiệm tính toán.** Dùng `torchdiffeq` hoặc tự cài đặt ánh xạ Euler, ước lượng tham số $$\theta$$ trong $$y'=-\theta y$$ từ dữ liệu sinh bởi $$\theta=1$$. So sánh quá trình huấn luyện dùng liên hợp rời rạc với gradient sai phân hữu hạn.

5. **Khám phá mở.** Đọc tài liệu Diffrax hoặc chương về phương pháp số trong luận án của Kidger (2022), sau đó viết bản hướng dẫn ngắn một trang chỉ rõ nên chọn lớp bộ giải nào của chương này cho: (a) neural ODE không cứng, (b) mô hình động học hóa học cứng, và (c) neural SDE.

## Tài liệu

- Ascher và Petzold; Kloeden và Platen.
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435). Docs Diffrax: [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
- Kidger, P., Foster, J., Li, X., và Lyons, T. “Efficient and accurate gradients for neural SDEs.” *NeurIPS* 2021. [arXiv:2105.13493](https://arxiv.org/abs/2105.13493).
- Song, Y., và cộng sự. “Score-based generative modeling through SDEs.” *ICLR* 2021.
- Brandstetter, J., Worrall, D., và Welling, M. “Message passing neural PDE solvers.” *ICLR* 2022. [arXiv:2202.03376](https://arxiv.org/abs/2202.03376).
- Takamoto, M., và cộng sự. “PDEBench.” *NeurIPS* 2022. [arXiv:2210.07182](https://arxiv.org/abs/2210.07182).
- Chen, R. T. Q., và cộng sự. `torchdiffeq`. [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq).
