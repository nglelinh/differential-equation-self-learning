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

## Mục tiêu

Bài tùy chọn này nối phương trình nhiệt, nhân Gauss và nguyên lý cực đại với hai phát triển 2021–2024: bộ giải vật lý-thông tin và học toán tử cho khuếch tán, cùng mô hình sinh score mà quá trình thuận là SDE khuếch tán. Sinh viên cần nhận ra nhân nhiệt trong cả hai câu chuyện và giải thích vì sao nguyên lý cực đại là unit test cho trường nhiệt độ học được. Việc suy ra và phân tích Fourier của phương trình nhiệt vẫn là lý thuyết chính thức.

## Kiến thức nền

Sinh viên cần biết suy ra phương trình nhiệt, tách biến, nghiệm cơ bản trên đường thẳng, và nguyên lý cực đại. Bài phương pháp số tùy chọn của chương hữu ích nhưng không bắt buộc.

## Dẫn nhập

Phương trình nhiệt $$u_t=\alpha^2 u_{xx}$$ là mô hình liên tục của làm mượt. Nhân của nó là Gauss rộng dần theo thời gian, và nguyên lý cực đại cấm điểm nóng nội tại chưa có trên biên parabolic. Hai sự thật ấy nay là hạ tầng học máy.

Ở phía SciML, PINN, DeepONet và Fourier neural operator được huấn luyện như bộ giải khuếch tán và surrogate tham số cho dẫn nhiệt, dòng môi trường xốp, và các bài parabolic liên quan. Hao và cộng sự (*PINNacle*, NeurIPS 2024) gồm các bài dẫn nhiệt trong hơn hai mươi benchmark PDE. Li và cộng sự (PINO, [arXiv:2111.03794](https://arxiv.org/abs/2111.03794)) kết hợp học toán tử với phần dư vật lý để tập dữ liệu thô vẫn được tinh bằng chính toán tử nhiệt.

Ở phía mô hình sinh, Song, Sohl-Dickstein, Kingma, Kumar, Ermon và Poole (*Score-Based Generative Modeling through Stochastic Differential Equations*, ICLR 2021; [arXiv:2011.13456](https://arxiv.org/abs/2011.13456)) lấy một phân phối dữ liệu, tiến hóa nó bằng SDE khuếch tán mà luật thỏa phương trình Fokker–Planck, rồi đảo SDE để lấy mẫu. Quá trình thuận là dòng nhiệt trên mật độ. Hiểu nhân và nguyên lý cực đại vì thế không phải loại suy; đó là lý do quá trình ngược có thể đặt chỉnh sau khi học score $$\nabla\log p_t$$.

## Khái niệm then chốt

### Bộ giải học được cho phương trình nhiệt

PINN cho $$u_t-\alpha^2 u_{xx}=0$$ collocates điểm phần dư trong không-thời gian. Mô hình toán tử thay vào đó học ánh xạ từ dữ liệu đầu $$u(\cdot,0)$$, hoặc từ trường dẫn, tới $$u(\cdot,T)$$. Đối tượng thứ hai gần nhân nhiệt hơn: nó là toán tử Green xấp xỉ. Phép thử siêu phân giải, đánh giá mô hình trên lưới mịn hơn lưới huấn luyện, chỉ có nghĩa vì toán tử nhiệt thật là ánh xạ giữa không gian hàm, không phải giữa lưới pixel.

### Nhân như tích chập Gauss

Trên đường thẳng,

$$
u(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}\int_{\mathbb{R}}\exp\Bigl(-\frac{(x-y)^2}{4\alpha^2 t}\Bigr)u_0(y)\,dy.
$$

Mô hình score dùng tích chập họ hàng gần để biến luật dữ liệu phức tạp thành luật gần Gauss. SDE ngược rồi khử nhiễu. Sinh viên đã tính nhân này bằng biến đổi Fourier đang nhìn cùng Gauss, nay dùng như bộ sinh mẫu chứ không như công thức nhiệt độ.

### Nguyên lý cực đại như chẩn đoán

Nhiệt độ học được vượt cực đại đầu và biên không phải bộ giải hơi sai; đó là bộ giải đã rời định lý. Benchmark kiểu PINNacle vì thế nên báo vi phạm ràng buộc cũng như lỗi $$L^2$$. Cùng chẩn đoán áp cho khuếch tán sinh: quá trình ngược tập trung khối sắc hơn score ước lượng cho phép đang phá cấu trúc Fokker–Planck.

### Nhân quả theo thời gian

Wang, Sankaran và Perdikaris (CMAME 2024) cho thấy PINN xem thời gian như chỉ một tọa độ collocation khác có thể phá nhân quả parabolic và thất bại trên tiến hóa hỗn loạn hoặc turbulent. Với phương trình nhiệt vấn đề nhẹ hơn nhưng có thật: điểm phần dư lúc muộn không được phép “giải thích hết” trường sớm không nhất quán.

## Phương pháp và kỹ thuật

- **PINN / PINN nhân quả.** Tốt cho nhận dạng dẫn ngược và hình học không đều; mong manh trên chân trời dài và lớp nhiệt mỏng.
- **Neural operator (FNO, DeepONet, PINO).** Tốt cho họ dữ liệu đầu hoặc hệ số; phải kiểm ở độ phân giải mới và đối chiếu nhân trên đường thẳng.
- **Mô hình score / khuếch tán.** Tốt cho lấy mẫu từ luật dữ liệu chiều cao; mối liên hệ với chương này là cấu trúc Fokker–Planck / nhiệt, không phải tuyên bố chúng thay bộ giải PDE.

Sơ đồ sai phân hữu hạn từ bài số tùy chọn vẫn là nghiệm chuẩn huấn luyện và kiểm hai phương pháp đầu.

## Ví dụ

### Ví dụ 1: Kiểm nhân trên đường thẳng

Nếu mô hình toán tử được huấn luyện trên dữ liệu đầu giá compact trên khoảng lớn, đáp ứng của nó trước xấp xỉ delta phải gần Gauss phương sai $$2\alpha^2 T$$. Đo phương sai ấy là câu hỏi thi nhân nhiệt.

### Ví dụ 2: Phá nguyên lý cực đại

Huấn luyện PINN nhỏ trên $$u_t=u_{xx}$$ với $$u(0,t)=u(1,t)=0$$ và $$u(x,0)=x(1-x)$$, rồi soi $$\max u_\theta$$. Nếu cực đại vượt $$1/4$$, mô hình đã phá định lý và không bảng $$L^2$$ nào bào chữa được.

### Ví dụ 3: Bước nhiệt rời rạc và bước score

```python
import numpy as np

u = np.array([0.0, 0.2, 0.8, 0.2, 0.0])
u_next = u.copy()
u_next[1:-1] = u[1:-1] + 0.25 * (u[2:] - 2 * u[1:-1] + u[:-2])
print(u_next)
```

Bộ lấy mẫu khuếch tán nổ phương sai dùng trung bình địa phương tương tự, rồi thêm nhiễu. Phần tất định là phương trình nhiệt; nhiễu thuộc mối quan tâm của chương ngẫu nhiên.

## Ứng dụng

Bộ giải nhiệt học được xuất hiện trong thiết kế nhiệt, mô hình pin, và nhận dạng nguồn nhiệt y khoa. Mô hình thời tiết học toán tử xem khuếch tán và hòa trộn khí quyển như phần của surrogate Fourier lớn hơn. Mô hình score đã trở thành bộ sinh mặc định trong thị giác và, ngày càng, prior cho bài ngược ảnh y khoa (Song và cộng sự, ICLR 2022; Chung và cộng sự, *Diffusion Posterior Sampling*, ICLR 2023). Sinh học và tài chính, đã nêu ở bài ứng dụng khuếch tán tùy chọn, nay có lớp tính toán thứ hai: thay vì giải một Black–Scholes hoặc Fisher, ta có thể học một họ ánh xạ ấy, hoặc lấy mẫu từ khuếch tán huấn luyện trên quỹ đạo lịch sử.

## Thách thức và hướng mở rộng

Khuếch tán thời gian dài trên lưới mịn đắt để mô phỏng cho dữ liệu huấn luyện, nên mô hình toán tử có thể thừa hưởng độ đo thực nghiệm lệch. PINN khó với dẫn đa thang. Khuếch tán sinh đòi nhiều đánh giá hàm và khớp score cẩn thận; phương trình Fokker–Planck của chúng chiều cao và không thay thế một giải PDE đặt chỉnh. Khuếch tán dị hướng và suy biến phá bức tranh Gauss đơn giản. Mô hình có thể khớp marginal tại thời $$T$$ vẫn có nhân trung gian sai.

Nếu bộ giải nhiệt học được phá nguyên lý cực đại nhưng thắng benchmark, điều ấy nghĩa là gì về mặt vật lý? Nghĩa là benchmark đang đo đại lượng sai.

## Bài tập

1. **Phương sai của nhân.** Từ nghiệm cơ bản, chỉ ra khối delta tại gốc có phương sai $$2\alpha^2 t$$ tại thời $$t$$. Làm sao ước lượng $$\alpha$$ từ hàm Green học được?

2. **Nguyên lý cực đại như mất mát.** Đề xuất phạt hinge tính phí PINN mỗi khi $$u_\theta$$ vượt cực đại biên. Định lý nào bảo đảm nghiệm thật trả không gì?

3. **SDE thuận và nhiệt.** Với SDE $$dX=\sigma\,dW$$, viết phương trình Fokker–Planck cho mật độ và đồng nhất với phương trình nhiệt. $$\alpha$$ theo $$\sigma$$ là gì?

4. **Thí nghiệm tính toán.** Cài sơ đồ nhiệt hiện và mô hình toán tử nhỏ (thậm chí ánh xạ tuyến tính trên giá trị lưới) học một bước thời gian. So nhân của chúng bằng cách áp cả hai lên delta rời rạc.

5. **Khám phá mở.** Đọc Song và cộng sự (ICLR 2021) và một bài nhiệt PINNacle (2024). Viết một trang giải thích cách dùng khuếch tán nào — giải $$u_t=\alpha^2\Delta u$$, hay lấy mẫu bằng thêm nhiễu rồi khử nhiễu — gần nghiệm cơ bản của chương hơn.

## Tài liệu

- Evans, Chương 2; Haberman, Chương 1–2.
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Li, Z., và cộng sự. “Physics-informed neural operator.” [arXiv:2111.03794](https://arxiv.org/abs/2111.03794).
- Song, Y., và cộng sự. “Score-based generative modeling through stochastic differential equations.” *ICLR* 2021. [arXiv:2011.13456](https://arxiv.org/abs/2011.13456).
- Wang, S., Sankaran, S., và Perdikaris, P. “Respecting causality for training PINNs.” *CMAME* 421 (2024).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
