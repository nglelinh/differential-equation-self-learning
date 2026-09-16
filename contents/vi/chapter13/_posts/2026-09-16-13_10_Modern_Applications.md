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

## Mục tiêu

Bài tùy chọn này xem Euler, Runge–Kutta, độ cứng, CFL và Euler–Maruyama như xương sống số của tính toán khoa học khả vi. Sinh viên cần giải thích đạo hàm reverse-mode qua một bộ giải, định vị `torchdiffeq` và Diffrax, và nối neural SDE với các mô hình khuếch tán score thống trị mô hình sinh 2021–2024. Lý thuyết nhất quán và ổn định cổ điển của chương không bị thay thế.

## Kiến thức nền

Sinh viên cần biết Euler tiến và lùi, RK4, miền ổn định tuyến tính, CFL, và sơ đồ Euler–Maruyama cho SDE. Bài ôn chuẩn bị về lỗi rời rạc hóa là khởi động đúng.

## Dẫn nhập

Phương pháp số là ánh xạ từ trường vector và bước lưới tới quỹ đạo rời rạc. Nếu ánh xạ ấy khả vi, nó có thể ngồi trong vòng học: tham số của trường, của bộ điều khiển, hoặc của closure có thể được huấn luyện bằng gradient descent. Chen và cộng sự (NeurIPS 2018) phổ biến phương pháp liên hợp cho neural ODE. Luận án 2022 của Kidger ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) và thư viện Diffrax ([https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)) biến toàn bộ catalog của chương này — bộ giải ODE hiện và ẩn, CDE, SDE, bước thích nghi — thành nguyên thủy JAX. `torchdiffeq` ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) làm điều tương tự trong PyTorch.

Ở phía ngẫu nhiên, Kidger, Foster, Li và Lyons (*Neural SDEs as Infinite-Dimensional GANs*, ICML 2021; *Efficient and Accurate Gradients for Neural SDEs*, NeurIPS 2021) cho thấy cách lan truyền ngược qua bộ giải SDE. Song và cộng sự (ICLR 2021) dùng SDE khuếch tán như mô hình sinh. Các câu hỏi số là những câu đã học ở đây: lỗi mạnh versus yếu, độ cứng, và ổn định của Euler–Maruyama.

## Khái niệm then chốt

### Lấy đạo hàm ánh xạ một bước

Euler tiến $$y_{n+1}=y_n+h f_\theta(y_n)$$ có Jacobian $$I+h Df_\theta(y_n)$$. Autodiff reverse-mode nhân các Jacobian ấy ngược, tức lan truyền liên hợp rời rạc. Euler ẩn đòi giải tuyến tính mỗi bước; định lý hàm ẩn cung cấp Jacobian. Bài stiff đòi liên hợp ẩn, không hiện, vì cùng lý do chúng đòi giải thuận ẩn.

### Liên hợp liên tục và checkpoint

Liên hợp liên tục của Chen và cộng sự tích phân một ODE thêm ngược và tiết kiệm bộ nhớ, với giá một lỗi rời rạc hóa mới. Diffrax mở cả hai lựa chọn discretize-then-optimize và optimize-then-discretize, tức cách nói thời 2022: chọn liệu gradient là gradient đúng của phương pháp số hay xấp xỉ gradient của bài liên tục. Đó là hai đối tượng khác nhau, và phân tích lỗi địa phương của chương áp cho cả hai.

### Neural SDE và SDE score

Neural SDE

$$
dX_t = b_\theta(t,X_t)\,dt + \sigma_\theta(t,X_t)\,dW_t
$$

là quá trình Itô học được. Huấn luyện nó đòi liên hợp ngẫu nhiên và đường Brownian nhất quán trên lượt ngược (Kidger và cộng sự, NeurIPS 2021). Mô hình sinh score dùng SDE thuận cho sẵn và chỉ học score định nghĩa drift ngược. Euler–Maruyama là bộ lấy mẫu mặc định; sơ đồ SDE bậc cao hơn và predictor–corrector là tinh chỉnh 2021–2024. Miền ổn định của sơ đồ vẫn quyết định bước ngược lớn có nổ hay không.

### CFL và stepper PDE học được

Stepper thời gian học được cho PDE có thể phá CFL dù mỗi ảnh chụp trông trơn. Brandstetter, Worrall và Welling (*Message Passing Neural PDE Solvers*, ICLR 2022; [arXiv:2202.03376](https://arxiv.org/abs/2202.03376)) và bộ PDEBench (Takamoto và cộng sự, NeurIPS 2022; [arXiv:2210.07182](https://arxiv.org/abs/2210.07182)) làm điều ấy thực nghiệm. Roll-out ổn định mười bước rồi nổ ở một trăm là câu chuyện ổn định cổ điển, nay với thông lượng nơ-ron.

## Phương pháp và kỹ thuật

1. Chọn sơ đồ thuận có miền ổn định chứa phổ kỳ vọng (RK hiện cho ODE không stiff, phương pháp ẩn hoặc mũ cho ODE stiff, sơ đồ tôn CFL cho PDE hyperbolic, Euler–Maruyama hoặc tốt hơn cho SDE).
2. Quyết định giữa autodiff đúng của sơ đồ rời rạc và liên hợp liên tục.
3. Đặt dung sai sao cho gradient không bị nhiễu bộ giải át.
4. Với SDE, lưu hoặc tái tạo cùng gia số Brownian trên lượt ngược.
5. Kiểm chứng bằng nghiệm chế tạo, phép thử ổn định tuyến tính, và roll-out dài.

Tài liệu phần mềm là một phần của phương pháp. API bộ giải Diffrax và `odeint_adjoint` của `torchdiffeq` là tài liệu sinh viên nên mở trước khi bịa quy tắc backprop mới.

## Ví dụ

### Ví dụ 1: Liên hợp Euler ẩn

Với $$y'=-\lambda y$$, Euler ẩn là $$y_{n+1}=y_n/(1+h\lambda)$$. Đạo hàm theo $$\lambda$$ sơ cấp và phải khớp autodiff. Gradient của Euler hiện, ngược lại, được lấy qua thuận không ổn định khi $$h\lambda$$ lớn, và do đó vô nghĩa.

### Ví dụ 2: Lỗi mạnh Euler–Maruyama

Sơ đồ $$X_{n+1}=X_n+h b(X_n)+\sqrt{h}\,\sigma(X_n)\xi_n$$ có bậc mạnh $$1/2$$ nói chung. Neural SDE huấn luyện với mất mát từng đường không thể thắng bậc ấy trừ khi nâng sơ đồ. Mất mát yếu (phân phối) có thể dùng sơ đồ yếu hơn, vì thế bộ lấy mẫu mô hình sinh thường quan tâm lỗi yếu.

### Ví dụ 3: Giải ODE kiểu Diffrax về tinh thần

```python
import numpy as np
from scipy.integrate import solve_ivp

def f(t, y, theta=0.8):
    return -theta * y

sol = solve_ivp(f, [0, 2], [1.0], rtol=1e-6, atol=1e-6)
print(sol.y[0, -1], np.exp(-0.8 * 2))
```

Bộ giải khả vi thay `solve_ivp` bằng đối tượng cũng trả $$\partial y(T)/\partial\theta$$. Các số thuận vẫn phải khớp phép thử này.

## Ứng dụng

Bộ giải khả vi nay là chuẩn trong neural ODE, phương trình vi phân phổ quát (Rackauckas và cộng sự, 2021, và hệ SciML), nhận dạng hệ, và điều khiển tối ưu. Neural SDE mô hình chuỗi tài chính không đều, động học phân tử, và động lực ngẫu nhiên ẩn. SDE score sinh ảnh, phân tử, và ngày càng ứng viên cho bài ngược ảnh hóa. PDEBench (2022) và các bộ sau như The Well (Ohana và cộng sự, NeurIPS 2024) cung cấp phép thử roll-out cộng đồng để stepper học được so với các phương pháp cổ điển của chương trên bài công khai.

Trong kỹ thuật, bộ giải CFD hoặc mạch khả vi cho phép nhà thiết kế tối ưu hình học hoặc tham số với cùng công nghệ liên hợp mà lý thuyết điều khiển tối ưu đã dùng hàng thập kỷ. Nguyên liệu mới là chính phần dư có thể chứa một mạng.

## Thách thức và hướng mở rộng

Liên hợp của quỹ đạo hỗn loạn dài không ổn định; shadowing và least-squares shadowing là chủ đề nghiên cứu, không phải công cụ đã giải. Bộ giải ẩn làm lượt ngược đắt. Liên hợp ngẫu nhiên cần tái tạo nhiễu cẩn thận. Stepper PDE học được overfitting chân trời ngắn. Hệ lai rời rạc–liên tục phá autodiff ngây thơ. Không vấn đề nào bãi bỏ A-ổn định hoặc CFL; chúng làm các ý niệm cổ điển ấy quý hơn.

Câu hỏi: nếu liên hợp liên tục và liên hợp rời rạc lệch $$10\%$$, cái nào bạn nên tin cho tối ưu bạn thực sự đang chạy? Câu trả lời của chương là liên hợp rời rạc, vì đó là gradient của phương pháp bạn đã triển khai.

## Bài tập

1. **Miền ổn định và bước học được.** Với $$y'=\lambda y$$, viết hệ số khuếch đại của RK4. Với $$h\lambda$$ nào stepper phần dư nơ-ron được phép dùng RK4 làm sơ đồ trong?

2. **Liên hợp rời rạc versus liên tục.** Với một bước Euler ẩn của $$y'=-\theta y$$, tính cả gradient đúng của ánh xạ số lẫn liên hợp liên tục đánh giá tại bước ấy. Khi nào chúng khớp?

3. **Mạnh versus yếu.** Giải thích vì sao bộ lấy mẫu score có thể chịu sơ đồ bậc mạnh kém nếu metric mục tiêu là khoảng cách phân phối.

4. **Thí nghiệm tính toán.** Dùng `torchdiffeq` hoặc ánh xạ Euler tự viết, khớp $$\theta$$ trong $$y'=-\theta y$$ với dữ liệu sinh bởi $$\theta=1$$. So huấn luyện bằng liên hợp rời rạc và gradient sai phân hữu hạn.

5. **Khám phá mở.** Đọc tài liệu Diffrax hoặc Kidger (2022), chương số, và viết hướng dẫn một trang: lớp bộ giải nào của chương này người dùng nên chọn cho (a) neural ODE không stiff, (b) closure hóa học stiff, (c) neural SDE?

## Tài liệu

- Ascher và Petzold; Kloeden và Platen.
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435). Docs Diffrax: [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
- Kidger, P., Foster, J., Li, X., và Lyons, T. “Efficient and accurate gradients for neural SDEs.” *NeurIPS* 2021. [arXiv:2105.13493](https://arxiv.org/abs/2105.13493).
- Song, Y., và cộng sự. “Score-based generative modeling through SDEs.” *ICLR* 2021.
- Brandstetter, J., Worrall, D., và Welling, M. “Message passing neural PDE solvers.” *ICLR* 2022. [arXiv:2202.03376](https://arxiv.org/abs/2202.03376).
- Takamoto, M., và cộng sự. “PDEBench.” *NeurIPS* 2022. [arXiv:2210.07182](https://arxiv.org/abs/2210.07182).
- Chen, R. T. Q., và cộng sự. `torchdiffeq`. [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq).
