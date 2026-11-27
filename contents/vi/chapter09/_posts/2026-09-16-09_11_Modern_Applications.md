---
layout: post
title: "09-11 Ứng dụng hiện đại: Bộ giải nơ-ron cho khuếch tán và mô hình score"
chapter: '09'
order: 11
owner: Course Team
lang: vi
categories:
- chapter09
lesson_type: optional
---

Làm sao các mô hình AI như Stable Diffusion, Midjourney hay Sora có thể biến một bức ảnh toàn nhiễu trắng ngẫu nhiên thành một bức tranh sắc nét như thật? Bí mật nằm ở đúng **Phương trình Nhiệt / Khuếch tán** Chương 9 chạy theo **hai chiều thời gian**: chiều xuôi làm nhòa dữ liệu ảnh thành nhiễu Gaussian thuần túy (phương trình Fokker–Planck), còn chiều ngược dùng mạng nơ-ron học **hàm điểm số (Score Function $\nabla_x \log p_t(x)$)** để đảo ngược quá trình khuếch tán!

## Kiến thức cần nhớ: Bốn trụ cột của Mô hình Khuếch tán & Score-Based AI

![Phương trình Truyền nhiệt & Mô hình Khuếch tán (Diffusion Models)]({{ site.imgurl }}/chapter_img/modern_apps/ma_09_heat_diffusion_ai.svg)

1. **Quá trình Khuếch tán Xuôi (Forward SDE / Heat Smoothing)**:
   Thêm dần nhiễu Gaussian qua $T$ bước $d\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,dt + g(t)\,d\mathbf{W}_t$; mật độ xác suất $p_t(\mathbf{x})$ tiến hóa theo phương trình Fokker–Planck (tổng quát hóa của phương trình nhiệt) về phân phối chuẩn $\mathcal{N}(\mathbf{0}, I)$.
2. **Phương trình Đảo ngược Thời gian (Anderson, 1982)**:
   Quá trình ngược cũng là một phương trình vi phân ngẫu nhiên, nhưng có thêm số hạng kéo về vùng dữ liệu thật nhờ **Score Function** $\mathbf{s}_\theta(\mathbf{x}, t) \approx \nabla_{\mathbf{x}} \log p_t(\mathbf{x})$!
3. **Dòng xác suất ODE (Probability Flow ODE)**:
   Song hành với SDE ngược là một **ODE xác định** có cùng mật độ biên $p_t(\mathbf{x})$, cho phép lấy mẫu siêu nhanh trong chỉ 10–20 bước (DDIM / DPM-Solver).
4. **Bộ giải Nơ-ron cho Khuếch tán Vật lý (Neural PDE Solvers)**:
   Bên cạnh AI tạo sinh, mạng nơ-ron còn học trực tiếp nhân Green khuếch tán để mô phỏng truyền nhiệt trong chip bán dẫn và pin xe điện nhanh gấp hàng trăm lần.

## Mục tiêu

Bài tùy chọn này kết nối phương trình nhiệt, nhân Gaussian và nguyên lý cực đại với hai hướng phát triển giai đoạn 2021–2024: các bộ giải mạng nơ-ron tích hợp vật lý (PINN) cùng học toán tử cho bài toán khuếch tán, và mô hình sinh dựa trên hàm score (score-based generative model) có quá trình thuận là phương trình vi phân ngẫu nhiên (SDE) khuếch tán. Sau bài học, sinh viên có thể nhận diện nhân nhiệt trong cả hai lĩnh vực và giải thích vì sao nguyên lý cực đại đóng vai trò tiêu chuẩn kiểm chứng cơ bản cho trường nhiệt độ học được. Việc thiết lập và phân tích Fourier cho phương trình nhiệt vẫn là nền tảng lý thuyết chính thức.

## Kiến thức nền

Sinh viên cần nắm cách thiết lập phương trình nhiệt, phương pháp tách biến, nghiệm cơ bản trên toàn trục thực và nguyên lý cực đại. Bài phương pháp sai phân hữu hạn tùy chọn của chương là tài liệu bổ trợ hữu ích nhưng không bắt buộc.

## Dẫn nhập

Phương trình nhiệt $$u_t=\alpha^2 u_{xx}$$ là mô hình liên tục điển hình của quá trình làm mượt: nhân tích phân của nó là hàm Gaussian trải rộng theo thời gian, còn nguyên lý cực đại loại trừ khả năng tự xuất hiện điểm nóng mới bên trong miền ngoài biên parabolic. Hai tính chất nền tảng này hiện đang đóng vai trò trụ cột trong nhiều phương pháp học máy khoa học.

Trong mảng học máy khoa học (SciML), PINN, DeepONet và Fourier neural operator được huấn luyện làm bộ giải khuếch tán và mô hình thay thế theo tham số cho bài toán dẫn nhiệt, dòng chảy trong môi trường xốp và các PDE parabolic liên quan. Hao và cộng sự (*PINNacle*, NeurIPS 2024) đưa các bài toán dẫn nhiệt vào bộ hơn hai mươi chuẩn đánh giá PDE. Li và cộng sự (PINO, [arXiv:2111.03794](https://arxiv.org/abs/2111.03794)) kết hợp học toán tử với phần dư phương trình vật lý để dữ liệu huấn luyện trên lưới thô vẫn được tinh chỉnh trực tiếp bởi toán tử nhiệt.

Trong mảng mô hình sinh, Song, Sohl-Dickstein, Kingma, Kumar, Ermon và Poole (*Score-Based Generative Modeling through Stochastic Differential Equations*, ICLR 2021; [arXiv:2011.13456](https://arxiv.org/abs/2011.13456)) lấy một phân bố dữ liệu, cho tiến hóa theo một SDE khuếch tán có mật độ xác suất thỏa mãn phương trình Fokker–Planck, rồi đảo ngược SDE theo thời gian để sinh mẫu mới. Quá trình thuận chính là một dòng khuếch tán trên hàm mật độ. Do đó, việc hiểu nhân nhiệt và nguyên lý cực đại không chỉ mang tính ví von, mà giải thích trực tiếp vì sao quá trình đảo ngược có thể đặt chỉnh sau khi học hàm score $$\nabla\log p_t$$.

### Giải thích: Tính tay Score Function $\nabla_x \log p_t(x)$ của một hạt khuếch tán Gaussian 1D

Giả sử dữ liệu gốc chỉ là 1 điểm duy nhất tại $x_0 = 5$. Sau thời gian khuếch tán $t$ (với phương sai nhiễu $\sigma_t^2 = 2t$), phân phối nhiễu tại thời điểm $t$ chính là nhân nhiệt Gaussian:
$$p_t(x) = \frac{1}{\sqrt{2\pi \sigma_t^2}} \exp\!\left(-\frac{(x - 5)^2}{2\sigma_t^2}\right).$$
1. Lấy logarit tự nhiên: $\log p_t(x) = -\frac{(x - 5)^2}{2\sigma_t^2} + \text{hằng số}$.
2. Lấy đạo hàm theo $x$ để tìm **Score Function**:
   $$s(x, t) = \frac{\partial}{\partial x}\log p_t(x) = \mathbf{-\frac{x - 5}{\sigma_t^2}}.$$
3. **Kiểm tra trực giác khử nhiễu**:
   - Nếu điểm nhiễu đang ở $x = 8$ (lệch phải): $s(8, t) = -\frac{3}{\sigma_t^2} < 0$ → **mũi tên đẩy sang trái** về $5$!
   - Nếu điểm nhiễu đang ở $x = 1$ (lệch trái): $s(1, t) = +\frac{4}{\sigma_t^2} > 0$ → **mũi tên kéo sang phải** về $5$!
   Mạng nơ-ron trong Stable Diffusion thực chất chỉ đang học trường vectơ mũi tên chỉ hướng ngược về vùng ảnh thật này!

## Khái niệm then chốt

### Bộ giải học được cho phương trình nhiệt

Mạng PINN giải phương trình $$u_t-\alpha^2 u_{xx}=0$$ bằng cách tối thiểu hóa phần dư PDE tại các điểm đặt (collocation points) trong miền không gian–thời gian. Ngược lại, các mô hình học toán tử trực tiếp học ánh xạ từ dữ liệu ban đầu $$u(\cdot,0)$$ hoặc từ trường hệ số dẫn nhiệt sang nghiệm $$u(\cdot,T)$$. Cách tiếp cận thứ hai gần với nhân nhiệt hơn vì nó xấp xỉ trực tiếp toán tử Green. Phép thử siêu phân giải (đánh giá mô hình trên lưới mịn hơn lưới huấn luyện) chỉ có ý nghĩa vì toán tử nhiệt thực chất là ánh xạ giữa các không gian hàm chứ không phụ thuộc vào một lưới điểm cố định.

### Nhân nhiệt như phép tích chập Gaussian

Trên toàn trục thực,

$$
u(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}\int_{\mathbb{R}}\exp\Bigl(-\frac{(x-y)^2}{4\alpha^2 t}\Bigr)u_0(y)\,dy.
$$

Các mô hình dựa trên score sử dụng một phép tích chập tương tự để biến phân bố dữ liệu phức tạp thành phân bố gần Gaussian, sau đó chạy SDE ngược để khử nhiễu và sinh mẫu. Khi đã tính nhân nhiệt này bằng biến đổi Fourier, sinh viên đang tiếp cận chính hàm Gaussian đó, chỉ khác là nó được dùng cho bài toán sinh mẫu thay vì tính phân bố nhiệt độ.

### Nguyên lý cực đại như công cụ chẩn đoán

Nếu một trường nhiệt độ do mạng dự đoán vượt quá cực đại của dữ liệu ban đầu và dữ liệu biên, đó không chỉ là sai số xấp xỉ nhỏ mà là dấu hiệu mô hình đã vi phạm trực tiếp định lý của bài toán. Vì vậy, các bộ chuẩn đánh giá như PINNacle cần báo cáo mức độ vi phạm ràng buộc vật lý song song với sai số $$L^2$$. Nguyên tắc chẩn đoán tương tự cũng áp dụng cho khuếch tán sinh: nếu quá trình ngược tập trung khối xác suất sắc hơn mức hàm score ước lượng cho phép, mô hình đang phá vỡ cấu trúc Fokker–Planck.

### Tính nhân quả theo thời gian

Wang, Sankaran và Perdikaris (*CMAME* 2024) chỉ ra rằng nếu PINN coi biến thời gian chỉ như một tọa độ đặt điểm thông thường, mô hình có thể vi phạm tính nhân quả của bài toán parabolic và thất bại trên các hệ hỗn loạn hoặc chảy rối. Đối với phương trình nhiệt, hiện tượng này nhẹ hơn nhưng vẫn hiện hữu: phần dư tại các thời điểm muộn không được phép bù đắp cho một trường nghiệm sai lệch ở các thời điểm sớm.

## Phương pháp và kỹ thuật

- **PINN và PINN bảo toàn nhân quả.** Phù hợp cho bài toán ngược nhận dạng hệ số dẫn nhiệt và miền hình học không đều, nhưng dễ kém ổn định trên khoảng thời gian dài hoặc khi xuất hiện lớp nhiệt mỏng.
- **Mạng toán tử (FNO, DeepONet, PINO).** Phù hợp cho họ dữ liệu ban đầu hoặc họ hệ số đa dạng; cần kiểm chứng trên độ phân giải mới và đối chiếu với nhân nhiệt trên trục thực.
- **Mô hình score / khuếch tán.** Phù hợp để lấy mẫu từ phân bố dữ liệu nhiều chiều; điểm giao với chương này nằm ở cấu trúc Fokker–Planck và phương trình nhiệt, không nhằm thay thế các bộ giải PDE truyền thống.

Các sơ đồ sai phân hữu hạn trong bài phương pháp số tùy chọn vẫn giữ vai trò bộ sinh nghiệm tham chiếu để huấn luyện và kiểm chứng hai nhóm phương pháp đầu tiên.

## Ví dụ

### Ví dụ 1: Kiểm chứng nhân nhiệt trên toàn trục thực

Nếu một mô hình toán tử được huấn luyện trên dữ liệu ban đầu có giá compact trong một khoảng đủ lớn, đáp ứng của nó trước một xung xấp xỉ hàm delta Dirac phải tiệm cận hàm Gaussian có phương sai $$2\alpha^2 T$$. Việc đo phương sai này là một phép kiểm chứng trực tiếp đối với nhân nhiệt học được.

### Ví dụ 2: Kiểm tra vi phạm nguyên lý cực đại

Huấn luyện một mạng PINN cỡ nhỏ cho phương trình $$u_t=u_{xx}$$ với điều kiện biên $$u(0,t)=u(1,t)=0$$ và điều kiện ban đầu $$u(x,0)=x(1-x)$$, sau đó kiểm tra giá trị $$\max u_\theta$$. Nếu cực đại vượt quá $$1/4$$, mô hình đã vi phạm nguyên lý cực đại dù sai số trung bình $$L^2$$ có thể vẫn nhỏ.

### Ví dụ 3: Bước cập nhật nhiệt rời rạc và bước khuếch tán

```python
import numpy as np

u = np.array([0.0, 0.2, 0.8, 0.2, 0.0])
u_next = u.copy()
u_next[1:-1] = u[1:-1] + 0.25 * (u[2:] - 2 * u[1:-1] + u[:-2])
print(u_next)
```

Bộ lấy mẫu khuếch tán tăng phương sai (variance-exploding) áp dụng một phép lấy trung bình cục bộ tương tự rồi cộng thêm nhiễu ngẫu nhiên. Phần tất định chính là bước tiến hóa của phương trình nhiệt, còn phần nhiễu gắn với mô hình ngẫu nhiên.

## Ứng dụng

Các bộ giải nhiệt dựa trên học máy được ứng dụng trong thiết kế quản lý nhiệt, mô hình hóa pin và nhận dạng nguồn nhiệt y sinh. Trong dự báo thời tiết bằng học toán tử, quá trình khuếch tán và hòa trộn khí quyển là một phần của mô hình thay thế Fourier quy mô lớn. Mô hình dựa trên score đã trở thành phương pháp sinh mẫu phổ biến trong thị giác máy tính và ngày càng được dùng làm phân bố tiên nghiệm (prior) cho bài toán ngược trong chẩn đoán hình ảnh y khoa (Song và cộng sự, ICLR 2022; Chung và cộng sự, *Diffusion Posterior Sampling*, ICLR 2023). Các bài toán sinh học và tài chính nêu ở bài ứng dụng khuếch tán cũng có thêm một lớp công cụ mới: thay vì chỉ giải từng phương trình Black–Scholes hoặc Fisher riêng lẻ, ta có thể học cả họ ánh xạ nghiệm hoặc lấy mẫu từ mô hình khuếch tán huấn luyện trên chuỗi dữ liệu lịch sử.

## Thách thức và hướng mở rộng

Mô phỏng khuếch tán trên khoảng thời gian dài với lưới mịn đòi hỏi chi phí tính toán lớn để tạo dữ liệu huấn luyện, khiến các mô hình toán tử dễ chịu ảnh hưởng của phân bố mẫu lệch. Mạng PINN gặp khó khăn với hệ số dẫn nhiệt đa thang đo. Các mô hình khuếch tán sinh đòi hỏi nhiều bước đánh giá hàm và ước lượng score chính xác; phương trình Fokker–Planck tương ứng có số chiều rất cao và không thay thế cho bộ giải PDE đặt chỉnh. Ngoài ra, khuếch tán dị hướng hoặc suy biến làm mất dạng Gaussian đơn giản, và một mô hình khớp tốt phân bố biên tại thời điểm cuối $$T$$ vẫn có thể học sai nhân chuyển tiếp ở các thời điểm trung gian.

Nếu một bộ giải nhiệt học được vi phạm nguyên lý cực đại nhưng đạt điểm cao trên bảng đánh giá, điều đó cho thấy tiêu chí đánh giá chưa phản ánh đúng yêu cầu vật lý của bài toán.

## Video tham khảo

- Xem trước: [Diffusion and Score-Based Generative Models](https://www.youtube.com/watch?v=wMmqCMwuM2Q) — MITCBMM, tiếng Anh. Giới thiệu khuếch tán và mô hình sinh dựa trên hàm score, chủ đề hiện đại trọng tâm của bài.
- [Physics Informed Neural Networks (PINNs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — Steve Brunton, tiếng Anh. Trình bày mạng nơ-ron tích hợp vật lý cho các bài toán PDE khuếch tán.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Ôn lại phương trình nhiệt cổ điển làm nền tảng cho các mô hình khuếch tán hiện đại.

## Bài tập

1. **Phương sai của nhân nhiệt.** Từ biểu thức nghiệm cơ bản, hãy chứng minh phân bố xuất phát từ khối delta tại gốc có phương sai $$2\alpha^2 t$$ tại thời điểm $$t$$. Làm thế nào ước lượng hệ số $$\alpha$$ từ hàm Green học được?

2. **Đưa nguyên lý cực đại vào hàm mất mát.** Đề xuất một số hạng phạt dạng hinge áp lên PINN mỗi khi $$u_\theta$$ vượt quá cực đại trên biên parabolic. Định lý nào bảo đảm nghiệm chính xác có giá trị phạt này bằng 0?

3. **SDE thuận và phương trình nhiệt.** Với SDE $$dX=\sigma\,dW$$, hãy viết phương trình Fokker–Planck cho hàm mật độ xác suất và đối chiếu với phương trình nhiệt. Hệ số $$\alpha$$ phụ thuộc vào $$\sigma$$ theo công thức nào?

4. **Thí nghiệm tính toán.** Cài đặt sơ đồ nhiệt tường minh và một mô hình toán tử đơn giản (chẳng hạn ánh xạ tuyến tính trên các giá trị lưới) để học một bước thời gian. So sánh nhân của hai phương pháp bằng cách tác động cả hai lên một xung delta rời rạc.

5. **Tìm hiểu mở rộng.** Đọc bài báo của Song và cộng sự (ICLR 2021) và một bài toán dẫn nhiệt trong bộ chuẩn PINNacle (2024). Viết một trang so sánh xem cách sử dụng khuếch tán nào — giải trực tiếp $$u_t=\alpha^2\Delta u$$ hay sinh mẫu bằng thêm nhiễu rồi khử nhiễu — gần với nghiệm cơ bản của chương hơn.

## Tài liệu

- Evans, Chương 2; Haberman, Chương 1–2.
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Li, Z., và cộng sự. “Physics-informed neural operator.” [arXiv:2111.03794](https://arxiv.org/abs/2111.03794).
- Song, Y., và cộng sự. “Score-based generative modeling through stochastic differential equations.” *ICLR* 2021. [arXiv:2011.13456](https://arxiv.org/abs/2011.13456).
- Wang, S., Sankaran, S., và Perdikaris, P. “Respecting causality for training PINNs.” *CMAME* 421 (2024).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
