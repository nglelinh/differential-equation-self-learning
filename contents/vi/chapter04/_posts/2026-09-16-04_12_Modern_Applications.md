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

Bài đọc tùy chọn này kết nối hệ ma trận, trị riêng và ma trận nghiệm cơ bản của Chương 04 với mô hình latent neural ODE và các phương pháp nhận dạng hệ hiện đại. Sinh viên sẽ nhìn nhận latent ODE như một hệ trạng thái ẩn (tuyến tính hoặc phi tuyến), giải thích vì sao cấu trúc trị riêng vẫn chi phối hành vi dài hạn, và hiểu vai trò của các công trình giai đoạn 2019–2022 trong việc đưa mô hình không gian trạng thái liên tục vào học sâu. Bài không thay thế các phương pháp trị riêng cổ điển của chương.

## Kiến thức nền

Sinh viên cần biết biểu diễn hệ bậc nhất $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$, tính trị riêng và vector riêng, xây dựng hàm mũ ma trận $$e^{At}$$ và đọc chân dung pha tuyến tính. Mô hình ngăn chứa ở cuối chương là ví dụ minh họa phù hợp nhất cho bài đọc này.

## Dẫn nhập

Hệ ODE là ngôn ngữ tự nhiên cho các đại lượng tương tác như bộ dao động ghép, bể pha trộn nối tiếp hay mô hình ngăn dịch tễ. Cách biểu diễn này hiện cũng được tích hợp trực tiếp vào mạng nơ-ron. Rubanova, Chen và Duvenaud (*Latent ODEs for Irregularly-Sampled Time Series*, NeurIPS 2019) mã hóa một chuỗi thời gian lấy mẫu không đều thành trạng thái khởi đầu trong không gian ẩn, rồi dự đoán tương lai bằng cách tích phân một neural ODE trong không gian ẩn đó. Chuỗi quan sát là đầu ra đọc từ một hệ thời gian liên tục mà mạng không viết ở dạng công thức đóng, nhưng vẫn có ma trận Jacobian, phổ trị riêng và chân dung pha.

Khảo sát năm 2022 của Kidger ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)) cùng bài báo về Neural CDE (Kidger, Morrill, Foster và Lyons, ICLR 2021) mở rộng hướng tiếp cận từ hệ ẩn tự trị sang hệ chịu dẫn dắt bởi một đường tín hiệu đầu vào. Cộng đồng học máy khoa học (SciML) xoay quanh các thư viện như Diffrax và DiffEqFlux xem hệ phương trình cơ chế và hệ nơ-ron là các thành phần có thể kết hợp hoặc thay thế lẫn nhau. Hàm mũ ma trận của Chương 04 chính là nghiệm giải tích đúng trong trường hợp tuyến tính, nên đóng vai trò công cụ kiểm chứng đầu tiên cho các mô hình này.

## Khái niệm then chốt

### Không gian trạng thái ẩn

Một mô hình latent ODE có dạng $$\mathbf{z}'=f_\theta(\mathbf{z})$$, $$\mathbf{x}(t)=g_\phi(\mathbf{z}(t))$$, trong đó $$\mathbf{x}$$ là biến quan sát và $$\mathbf{z}$$ là trạng thái ẩn. Nếu gần một điểm cân bằng ta có xấp xỉ tuyến tính $$f_\theta(\mathbf{z})\approx A\mathbf{z}$$, toàn bộ phân loại của Chương 04 vẫn giữ nguyên hiệu lực: trị riêng thực âm ứng với nút hút, trị riêng phức có phần thực âm ứng với xoắn ốc hút, còn trị riêng bằng 0 báo hiệu đường cân bằng hoặc đại lượng bảo toàn. Việc huấn luyện mà bỏ qua phổ trị riêng có thể khớp tốt dữ liệu quan sát nhưng vẫn ẩn chứa sự mất ổn định bên trong không gian ẩn.

### Ma trận nghiệm cơ bản và phép tuyến tính hóa

Ma trận nghiệm cơ bản $$\Phi(t)=e^{At}$$ ánh xạ trạng thái ban đầu sang trạng thái tại thời điểm $$t$$. Trong mô hình không gian trạng thái ẩn tuyến tính, đây chính là toán tử chuyển trạng thái được học từ dữ liệu. Với trường động lực ẩn phi tuyến, ma trận chuyển cục bộ tương ứng là nghiệm của phương trình biến phân $$\mathbf{v}'=Df_\theta(\mathbf{z}(t))\mathbf{v}$$ — chính là phép tuyến tính hóa dùng để phân tích chân dung pha, nay được tính tự động thông qua vi phân tự động qua bộ giải ODE.

### Đầu vào, điều khiển và Neural CDE

Hệ không thuần nhất $$\mathbf{x}'=A\mathbf{x}+\mathbf{g}(t)$$ là cách cổ điển để đưa tác động ngoài vào hệ. Neural CDE thay số hạng $$\mathbf{g}(t)\,dt$$ bằng gia số điều khiển $$f_\theta(\mathbf{z})\,dX(t)$$, phù hợp khi đầu vào là một chuỗi dữ liệu đo được liên tục theo thời gian thay vì một hàm giải tích cho trước. Về mặt khái niệm, công thức biến thiên hằng số vẫn giữ nguyên vai trò: hệ thuần nhất truyền tác động của từng gia số đầu vào theo thời gian thông qua toán tử $$\Phi(t)\Phi(s)^{-1}$$.

### Tính nhận dạng trong mô hình ngăn

Trong dược động học và dịch tễ, mô hình ngăn thường chỉ nhận dạng được sai khác một phép biến đổi tọa độ tương đương. Sự bất định tương tự xuất hiện ở latent ODE: với mọi ma trận khả nghịch $$P$$, phép đổi biến $$\mathbf{w}=P\mathbf{z}$$ tạo ra hệ tương đương với ma trận $$PAP^{-1}$$. Các trị riêng bất biến dưới phép đồng dạng này, còn vector riêng và ý nghĩa vật lý của từng ngăn thì thay đổi theo hệ cơ sở.

## Phương pháp và kỹ thuật

1. Huấn luyện một latent ODE hoặc mô hình không gian trạng thái tuyến tính trên chuỗi dữ liệu.
2. Tuyến tính hóa trường động lực học được tại điểm cân bằng hoặc điểm làm việc suy ra từ mô hình.
3. Tính các trị riêng của Jacobian và đối chiếu với các thang thời gian quan sát trong dữ liệu.
4. Với mô hình ngăn, kiểm tra xem phổ trị riêng — chứ không phải từng tọa độ riêng lẻ — có ổn định qua nhiều lần khởi tạo ngẫu nhiên khác nhau hay không.
5. Với hệ có đầu vào điều khiển, so sánh đáp ứng của mô hình với công thức biến thiên hằng số áp dụng lên hệ đã tuyến tính hóa.

Về công cụ phần mềm, `torchdiffeq` thường dùng cho latent ODE trên PyTorch, Diffrax dùng trên JAX (hỗ trợ cả CDE), còn hệ sinh thái SciML trên Julia thuận tiện cho các mô hình lai giữa cơ chế vật lý và mạng nơ-ron.

## Ví dụ

### Ví dụ 1: Khôi phục hệ hai bể pha trộn ẩn

Hệ hai bể pha trộn nối tiếp là hệ tuyến tính có hai trị riêng thực âm. Ngay cả khi chỉ quan sát nồng độ ở bể hạ lưu, một latent ODE hai chiều ẩn vẫn cần khôi phục được hai thang thời gian đặc trưng này, dù hệ tọa độ học được có thể là phép xoay của các ngăn vật lý ban đầu. Do đó, đối chiếu phổ trị riêng qua các lần chạy huấn luyện mang lại nhiều thông tin hơn so với việc chỉ vẽ trực tiếp các tọa độ ẩn.

### Ví dụ 2: Bộ dao động ghép và chế độ dao động riêng

Hệ hai lò xo ghép nối có hai cặp trị riêng thuần ảo tương ứng với hai tần số dao động riêng. Một mô hình ẩn huấn luyện chỉ trên tổng chuyển vị của hai vật có thể khôi phục chính xác hai tần số này nhưng vẫn trộn lẫn hình dạng của các chế độ riêng. Phân tích chế độ riêng của Chương 04 giải thích rõ điều đó: tần số là bất biến phổ, còn dạng dao động phụ thuộc vào hệ cơ sở được chọn.

### Ví dụ 3: Latent ODE tuyến tính bằng PyTorch

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

Thay ma trận hằng $$A$$ bằng một mạng nơ-ron nhỏ sẽ chuyển đoạn mã trên thành một latent ODE. Sau khi huấn luyện, đại lượng đầu tiên nên kiểm tra vẫn là phổ trị riêng của ma trận Jacobian tại điểm cân bằng.

## Ứng dụng

Latent ODE được ứng dụng trong phân tích hồ sơ sức khỏe điện tử, dữ liệu cảm biến đeo, chuỗi thời gian khí hậu và dữ liệu hoạt động quần thể thần kinh — những bài toán có tần suất lấy mẫu không đều và động lực ẩn chiều thấp. Trong kỹ thuật, chúng bổ sung cho bộ lọc Kalman cổ điển và phương pháp nhận dạng không gian con. Dịch tễ học là phép kiểm chứng rất rõ ràng: một mô hình ẩn dạng SIR không thể coi là đạt yêu cầu chỉ vì sai số tái tạo thấp nếu Jacobian tại cân bằng không bệnh mang dấu phổ sai, bởi dấu này liên hệ trực tiếp với hệ số lây nhiễm cơ bản trong xấp xỉ tuyến tính.

Các nghiên cứu về Neural CDE và phương trình vi phân thô (rough DE) giai đoạn 2021–2022 mở rộng sang lớp bài toán chịu dẫn dắt bởi tín hiệu điều khiển, dữ liệu giao dịch hoặc kích thích không đều — phiên bản hiện đại của hệ tuyến tính không thuần nhất.

## Thách thức và hướng mở rộng

Số chiều của không gian ẩn là siêu tham số không có cách xác định trực tiếp tương tự dạng chuẩn Jordan: chọn quá nhỏ sẽ bỏ sót chế độ động học, chọn quá lớn sẽ phát sinh trị riêng thừa khó nhận dạng và dễ mất ổn định. Tính cứng (stiffness) cũng xuất hiện ngay khi các thang thời gian chênh lệch lớn, giống như ở hệ tuyến tính cứng. Quan sát rời rạc khiến hệ liên tục bị thiếu xác định, và trường phi tuyến học được có thể sinh ra điểm hút giả nằm xa vùng dữ liệu huấn luyện; vì vậy, ngoại suy thực chất là bài toán phân tích chân dung pha chứ không chỉ là tối thiểu hóa hàm mất mát.

Một câu hỏi đáng suy nghĩ: nếu hai hệ ẩn có cùng phổ trị riêng nhưng khác vector riêng, những kết luận khoa học nào vẫn giữ nguyên giá trị? Theo lý thuyết Chương 04, đó là mọi kết luận phụ thuộc vào lớp đồng dạng của $$A$$ chứ không phụ thuộc vào một hệ cơ sở cụ thể.

## Video tham khảo

- Xem trước: [Latent Stochastic Differential Equations for Irregularly-Sampled Time Series - David Duvenaud](https://www.youtube.com/watch?v=93wr5vhI0F4) — Institute for Advanced Study, tiếng Anh. Bài giảng của David Duvenaud về phương trình vi phân ngẫu nhiên ẩn cho chuỗi thời gian lấy mẫu không đều.
- [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, tiếng Anh. Giới thiệu neural ODE — nền tảng động lực ẩn tất định của bài đọc này.
- [Solving Systems of Differential Equations with Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=Zwb5eiYcL8w) — Steve Brunton, tiếng Anh. Ôn lại hệ tuyến tính cổ điển mà các mô hình ẩn tuyến tính hướng tới khôi phục.

## Bài tập

1. **Bất biến đồng dạng.** Chứng minh rằng $$A$$ và $$PAP^{-1}$$ sinh ra các quỹ đạo tương đương qua phép đổi tọa độ $$\mathbf{w}=P\mathbf{z}$$. Từ đó, các nghiên cứu về latent ODE nên báo cáo những đại lượng nào?

2. **Khả năng quan sát từ đầu ra vô hướng.** Với hệ $$\mathbf{x}'=A\mathbf{x}$$ và đầu ra $$y=c^\top\mathbf{x}$$, giải thích điều kiện để một tín hiệu quan sát vô hướng vẫn khôi phục được phổ của $$A$$, và liên hệ với khái niệm tính quan sát được (observability).

3. **Biến thiên hằng số dưới góc nhìn giải mã.** Viết công thức nghiệm của $$\mathbf{z}'=A\mathbf{z}+B\mathbf{u}(t)$$ và đối chiếu số hạng $$B\mathbf{u}(t)$$ với gia số điều khiển trong Neural CDE. Toán tử $$e^{A(t-s)}$$ đóng vai trò gì?

4. **Thử nghiệm tính toán.** Huấn luyện một latent ODE tuyến tính hai chiều trên dữ liệu từ hệ hai bể pha trộn khi chỉ quan sát bể thứ hai. So sánh các trị riêng học được với trị riêng thực qua năm lần khởi tạo ngẫu nhiên khác nhau.

5. **Khám phá mở.** Đọc bài báo của Rubanova, Chen và Duvenaud (NeurIPS 2019) và vẽ sơ đồ encoder–decoder đặt cạnh mô hình ngăn cổ điển. Vai trò của $$e^{At}$$ tương ứng với bộ phận nào trong sơ đồ?

## Tài liệu

- Boyce và DiPrima, Chương 7; Arnold, Chương 1–3.
- Rubanova, Y., Chen, R. T. Q., và Duvenaud, D. “Latent ordinary differential equations for irregularly-sampled time series.” *NeurIPS* 2019. [arXiv:1907.03907](https://arxiv.org/abs/1907.03907).
- Kidger, P., Morrill, J., Foster, J., và Lyons, T. “Neural controlled differential equations.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- `torchdiffeq` và Diffrax, tương tự các bài ứng dụng hiện đại ở Chương 01 và Chương 13.
