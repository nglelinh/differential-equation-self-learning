---
layout: post
title: "04-12 Ứng dụng hiện đại: Latent ODE và hệ tuyến tính học được"
chapter: '04'
order: 12
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này nối hệ ma trận, trị riêng và ma trận cơ bản với latent neural ODE và các mô hình nhận dạng hệ hiện đại. Sinh viên cần đọc latent ODE như hệ ẩn tuyến tính hoặc phi tuyến, giải thích vì sao cấu trúc trị riêng vẫn chi phối hành vi dài hạn, và định vị các bài 2019–2022 đã biến mô hình không gian trạng thái liên tục thành công cụ deep learning chuẩn. Các phương pháp trị riêng của chương không bị thay thế.

## Kiến thức nền

Sinh viên cần biết viết hệ cấp một $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$, tính trị riêng và vector riêng, lập $$e^{At}$$, và đọc chân dung pha tuyến tính. Mô hình ngăn ở bài cuối chương là ví dụ chạy lý tưởng.

## Dẫn nhập

Hệ ODE là ngôn ngữ bản địa của các đại lượng tương tác: dao động tử liên kết, bồn nối tiếp, ngăn dịch tễ. Cùng ngôn ngữ ấy nay nằm trong mạng nơ-ron. Rubanova, Chen và Duvenaud (*Latent ODEs for Irregularly-Sampled Time Series*, NeurIPS 2019) mã hóa một dãy không đều thành trạng thái đầu ẩn, rồi sinh tương lai bằng cách tích phân neural ODE trong không gian ấy. Dãy quan sát là phần đọc ra của một hệ thời gian liên tục mà mạng không viết dạng đóng, nhưng vẫn có Jacobian, phổ, và chân dung pha.

Khảo sát 2022 của Kidger ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) và bài Neural CDE (Kidger, Morrill, Foster và Lyons, ICLR 2021) mở rộng ý tưởng từ trường ẩn tự trị sang hệ bị dẫn bởi một đường đầu vào. Cộng đồng SciML quanh Diffrax và DiffEqFlux xem hệ cơ chế và hệ nơ-ron như đối tượng hoán đổi được. Ma trận mũ của chương là nghiệm đúng của trường hợp tuyến tính, do đó là chẩn đoán đầu tiên cho mọi mô hình ấy.

## Khái niệm then chốt

### Không gian trạng thái ẩn

Latent ODE là hệ $$\mathbf{z}'=f_\theta(\mathbf{z})$$, $$\mathbf{x}(t)=g_\phi(\mathbf{z}(t))$$, với $$\mathbf{x}$$ quan sát và $$\mathbf{z}$$ ẩn. Nếu $$f_\theta(\mathbf{z})\approx A\mathbf{z}$$ gần cân bằng, phân loại đã chứng minh trong chương áp nguyên văn: trị riêng thực âm cho nút tắt, trị riêng phức phần thực âm cho xoắn ốc, trị riêng không báo đường cân bằng hoặc luật bảo toàn. Huấn luyện bỏ qua phổ ấy có thể khớp quan sát mà vẫn không ổn định bên trong.

### Ma trận cơ bản và tuyến tính hóa

Ma trận cơ bản $$\Phi(t)=e^{At}$$ ánh xạ điều kiện đầu thành trạng thái tại $$t$$. Trong mô hình ẩn tuyến tính, cùng đối tượng ấy là toán tử chuyển trạng thái học được. Với trường ẩn phi tuyến, ma trận cơ bản địa phương là ma trận chuyển của phương trình biến phân $$\mathbf{v}'=Df_\theta(\mathbf{z}(t))\mathbf{v}$$. Đó đúng tuyến tính hóa dùng để vẽ chân dung pha, nay được tính tự động bằng cách lấy đạo hàm bộ giải.

### Đầu vào, điều khiển, và Neural CDE

Hệ không thuần nhất $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$ là cách cổ điển thêm lực. Neural CDE thay $$\mathbf{g}(t)\,dt$$ bằng gia số điều khiển $$f_\theta(\mathbf{z})\,dX(t)$$, đúng mô hình khi đầu vào là đường đo được chứ không phải hàm thời gian cho sẵn. Biến thiên tham số vẫn là công thức nghiệm khái niệm: hệ thuần nhất vận chuyển hiệu ứng mỗi gia số về phía trước bằng $$\Phi(t)\Phi(s)^{-1}$$.

### Khả năng nhận dạng ngăn

Mô hình ngăn dược động học và dịch tễ chỉ nhận dạng được tới những đồng dạng nhất định. Sự mơ hồ ấy xuất hiện trong latent ODE: nếu $$P$$ khả nghịch, $$\mathbf{w}=P\mathbf{z}$$ cho hệ tương đương với ma trận $$PAP^{-1}$$. Trị riêng bất biến; vector riêng và nghĩa ngăn thì không.

## Phương pháp và kỹ thuật

1. Khớp latent ODE hoặc mô hình không gian trạng thái tuyến tính với dãy.
2. Tuyến tính hóa trường học được tại cân bằng hoặc điểm làm việc suy ra.
3. Tính trị riêng và so với các thang thời gian thấy trong dữ liệu.
4. Nếu ứng dụng là mô hình ngăn, kiểm tra phổ — không phải một cơ sở cụ thể — có ổn định qua các hạt giống ngẫu nhiên không.
5. Với hệ bị dẫn, so sánh đáp ứng học được với biến thiên tham số trên hệ tuyến tính hóa.

Phần mềm: `torchdiffeq` cho latent ODE PyTorch; Diffrax cho JAX, gồm CDE; hệ SciML trong Julia cho hệ lai cơ chế–nơ-ron.

## Ví dụ

### Ví dụ 1: Lấy lại hai bồn ẩn

Hai bồn pha trộn là hệ tuyến tính với trị riêng thực âm. Nếu chỉ quan sát nồng độ hạ lưu, latent ODE hai chiều ẩn nên lấy lại hai thang thời gian ấy, dù tọa độ học được là phép quay của các ngăn vật lý. Vẽ trị riêng qua các hạt giống huấn luyện giàu thông tin hơn vẽ quỹ đạo ẩn.

### Ví dụ 2: Dao động tử liên kết và mode riêng

Hai lò xo liên kết có một cặp cặp trị riêng ảo, tương ứng mode riêng. Mô hình ẩn huấn luyện trên tổng hai vị trí có thể lấy lại tần số và vẫn trộn hình dạng mode. Tính toán mode riêng của chương là chuẩn: tần số là bất biến phổ, hình dạng phụ thuộc cơ sở.

### Ví dụ 3: Latent ODE tuyến tính trong mã

```python
import torch
from torchdiffeq import odeint

A = torch.tensor([[-1.0, 1.0], [0.0, -2.0]])

def f(t, z):
    return z @ A.T

z0 = torch.tensor([1.0, 1.0])
t = torch.linspace(0.0, 4.0, 41)
zt = odeint(f, z0, t)
print(zt[-1])
```

Thay $$A$$ bằng một mạng nhỏ biến đoạn này thành latent ODE. Việc đầu tiên cần in sau huấn luyện vẫn là phổ của Jacobian tại cân bằng.

## Ứng dụng

Latent ODE được dùng trong hồ sơ sức khỏe điện tử, cảm biến đeo, chuỗi khí hậu và ghi quần thể thần kinh — mọi nơi mẫu không đều và trạng thái ẩn là hệ động lực chiều thấp. Trong kỹ thuật chúng ngồi cạnh lọc Kalman cổ điển và nhận dạng không gian con. Dịch tễ là phép thử đặc biệt trung thực. Một hệ ẩn kiểu SIR không nên được ca ngợi vì lỗi tái tạo thấp nếu Jacobian tại cân bằng không bệnh có dấu phổ sai, vì dấu ấy là số tái sản xuất cơ bản ở dạng tuyến tính hóa.

Các bài CDE và rough DE 2021–2022 thêm trục ứng dụng thứ hai: hệ bị dẫn bởi điều khiển, giao dịch hoặc kích thích không đều. Đó là phiên bản hiện đại của hệ tuyến tính không thuần nhất.

## Thách thức và hướng mở rộng

Chiều ẩn là siêu tham số không có analogue của dạng Jordan tính được: quá nhỏ thì mất mode, quá lớn thì trị riêng thừa không nhận dạng và thường không ổn định. Độ cứng xuất hiện ngay khi các thang thời gian tách, đúng như hệ tuyến tính stiff. Quan sát rời rạc để lại hệ liên tục dưới xác định. Trường phi tuyến học được có thể có hấp dẫn giả xa dữ liệu, nên ngoại suy là câu hỏi chân dung pha, không phải câu hỏi hàm mất mát.

Câu hỏi hữu ích: nếu hai hệ ẩn chia sẻ trị riêng nhưng không chia sẻ vector riêng, kết luận khoa học nào còn đúng? Câu trả lời của chương: những kết luận phụ thuộc lớp đồng dạng của $$A$$, không phụ thuộc một cơ sở ưa thích.

## Bài tập

1. **Bất biến đồng dạng.** Chỉ ra $$A$$ và $$PAP^{-1}$$ sinh quỹ đạo tương đương sau đổi tọa độ $$\mathbf{w}=P\mathbf{z}$$. Bài báo latent ODE nên báo những đại lượng nào?

2. **Hạng đầu ra quan sát.** Với $$\mathbf{x}'=A\mathbf{x}$$, $$y=c^\top\mathbf{x}$$, giải thích khi nào một đầu ra vô hướng vẫn lấy lại được phổ của $$A$$. Liên hệ với khả năng quan sát.

3. **Biến thiên tham số như bộ giải mã.** Viết nghiệm của $$\mathbf{z}'=A\mathbf{z}+B\mathbf{u}(t)$$ và diễn giải $$B\mathbf{u}(t)$$ như gia số Neural CDE. $$e^{A(t-s)}$$ đóng vai trò gì?

4. **Thí nghiệm tính toán.** Khớp latent ODE tuyến tính hai chiều với mẫu hệ hai bồn chỉ quan sát bồn thứ hai. So sánh trị riêng học được với trị riêng thật qua năm hạt giống.

5. **Khám phá mở.** Đọc Rubanova, Chen và Duvenaud (NeurIPS 2019) và phác sơ đồ encoder–decoder cạnh hình ngăn cổ điển. $$e^{At}$$ đang ẩn ở đâu?

## Tài liệu

- Boyce và DiPrima, Chương 7; Arnold, Chương 1–3.
- Rubanova, Y., Chen, R. T. Q., và Duvenaud, D. “Latent ordinary differential equations for irregularly-sampled time series.” *NeurIPS* 2019. [arXiv:1907.03907](https://arxiv.org/abs/1907.03907).
- Kidger, P., Morrill, J., Foster, J., và Lyons, T. “Neural controlled differential equations.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- `torchdiffeq` và Diffrax, như ở các bài hiện đại Chương 01 và 13.
