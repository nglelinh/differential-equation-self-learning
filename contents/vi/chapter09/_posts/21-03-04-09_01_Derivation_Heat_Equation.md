---
layout: post
title: "Suy Ra Phương Trình Nhiệt"
chapter: '09'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 01 Derivation Heat Equation]({{ site.imgurl }}/chapter_img/chapter09/01_derivation_heat_equation.svg)

## Mục tiêu

Bài học này giúp sinh viên hiểu phương trình nhiệt không phải là công thức xuất hiện từ hư không, mà là hệ quả trực tiếp của hai ý tưởng vật lý rất cơ bản: bảo toàn năng lượng và định luật dẫn nhiệt Fourier. Sau bài học, sinh viên cần hiểu được quá trình suy ra phương trình nhiệt trong một chiều và nhiều chiều ở mức khái niệm, nhận ra ý nghĩa của các hệ số vật lý, và thấy vì sao phương trình nhiệt có bản chất khuếch tán, làm mượt dữ liệu theo thời gian.

## Kiến thức nền

Sinh viên nên nắm đạo hàm riêng, đạo hàm bậc hai, tích phân trên đoạn hoặc trên miền, và trực giác vật lý cơ bản về nhiệt độ, dòng nhiệt, năng lượng. Kiến thức về bảo toàn khối lượng hoặc bảo toàn năng lượng trong cơ học chất lưu cũng rất hữu ích vì logic lập mô hình ở đây rất tương đồng.

## Dẫn nhập

Trong nhiều giáo trình, phương trình nhiệt được viết ngay dưới dạng $$ u_t=\alpha^2u_{xx} $$ hoặc $$ u_t=\alpha^2\Delta u $$, rồi đi thẳng vào nghiệm. Nhưng nếu học như vậy, sinh viên rất dễ nhớ công thức mà không hiểu tại sao đạo hàm theo thời gian lại liên hệ với đạo hàm bậc hai theo không gian. Bài này giải quyết đúng điểm đó.

Ta sẽ thấy ý tưởng cốt lõi rất tự nhiên: nhiệt lượng trong một phần vật thể chỉ thay đổi nếu có dòng nhiệt đi qua biên hoặc có nguồn nhiệt sinh ra bên trong. Khi dòng nhiệt tỉ lệ với độ dốc nhiệt độ, việc cân bằng năng lượng sẽ tự động sinh ra đạo hàm bậc hai theo không gian. Chính đạo hàm bậc hai này là dấu hiệu toán học của khuếch tán.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một điểm trên thanh kim loại nóng hơn vùng xung quanh, nhiệt sẽ chảy ra khỏi vùng đó về hai phía. Ngược lại, nếu một điểm lạnh hơn xung quanh, nhiệt sẽ chảy vào. Vì vậy tốc độ thay đổi nhiệt độ tại một điểm không phụ thuộc vào nhiệt độ riêng tại điểm đó, mà phụ thuộc vào việc điểm đó cao hay thấp hơn mức trung bình lân cận. Đó chính là trực giác của đạo hàm bậc hai.

### Cách nhìn hình ảnh

Hãy tưởng tượng đồ thị nhiệt độ dọc theo một thanh. Nếu đồ thị có một đỉnh nhọn, nhiệt sẽ thoát khỏi đỉnh đó và làm đỉnh hạ xuống. Nếu có một hõm sâu, nhiệt từ hai phía chảy vào và làm hõm đầy lên. Vì thế phương trình nhiệt luôn có xu hướng làm phẳng đồ thị. Đỉnh bị hạ, hõm bị lấp, các dao động cao tần bị dập tắt nhanh hơn các biến thiên chậm.

### Cách nhìn hình thức

Gọi $$ u(x,t) $$ là nhiệt độ. Định luật Fourier cho mật độ dòng nhiệt $$ q=-k u_x $$ trong một chiều, hoặc $$ \mathbf q=-k\nabla u $$ trong nhiều chiều. Dấu trừ cho biết nhiệt chảy từ nơi nóng sang nơi lạnh.

Bảo toàn năng lượng trên đoạn $$ [x,x+\Delta x] $$ cho ta:

$$
\frac{d}{dt}\int_x^{x+\Delta x}\rho c\,u(\xi,t)\,d\xi
=
q(x,t)-q(x+\Delta x,t)+\int_x^{x+\Delta x}Q(\xi,t)\,d\xi.
$$

Chia cho $$ \Delta x $$ và cho $$ \Delta x\to 0 $$, ta được $$ \rho c\,u_t=-q_x+Q $$. Thay $$ q=-ku_x $$, suy ra $$ \rho c\,u_t=(k u_x)_x+Q $$. Nếu $$ k $$ là hằng số, thì

$$
u_t=\alpha^2u_{xx}+\frac{Q}{\rho c},
\qquad
\alpha^2=\frac{k}{\rho c}.
$$

## Những ngộ nhận thường gặp

- "Phương trình nhiệt chỉ đúng cho nhiệt độ." Sai. Nó còn mô tả nhiều quá trình khuếch tán khác.
- "Định luật Fourier là hệ quả toán học hiển nhiên." Không đúng; nó là định luật thực nghiệm được đưa vào mô hình.
- "Đạo hàm bậc hai chỉ xuất hiện vì tính toán." Sai. Nó phản ánh sự chênh lệch giữa giá trị tại một điểm và mức trung bình lân cận.
- "Nếu có nguồn nhiệt thì chỉ cần cộng thêm một hằng số." Không đúng; nguồn có thể phụ thuộc cả vị trí lẫn thời gian.

## Tiến trình học tập đề xuất

### Bước 1: Xác định đại lượng cần theo dõi

Nhiệt độ là đại lượng trường theo không gian và thời gian.

### Bước 2: Viết dòng nhiệt theo gradient

Đây là nơi vật lý đi vào mô hình.

### Bước 3: Viết cân bằng năng lượng trên một đoạn nhỏ

Không nên nhảy thẳng đến PDE nếu chưa hiểu bước tích phân này.

### Bước 4: Chuyển từ mô tả tích phân sang mô tả vi phân

Đây là cầu nối để PDE xuất hiện.

### Bước 5: Diễn giải bản chất khuếch tán

Sinh viên nên tự giải thích bằng lời vì sao nghiệm có xu hướng làm mượt dữ liệu.

### Các checkpoint

- Sinh viên có giải thích được vì sao dấu trừ xuất hiện trong định luật Fourier hay không.
- Sinh viên có hiểu vì sao cân bằng năng lượng sinh ra đạo hàm theo thời gian hay không.
- Sinh viên có diễn giải được ý nghĩa của

$$ u_{xx} $$

như một "độ lệch khỏi trung bình lân cận" hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Thanh một chiều không có nguồn

Giả sử $$ Q=0 $$ và $$ k,\rho,c $$ là hằng số. Khi đó:

$$ \rho c\,u_t=k u_{xx}. $$

Chia hai vế cho $$ \rho c $$, ta được phương trình nhiệt chuẩn $$ u_t=\alpha^2u_{xx} $$. Ví dụ này là trường hợp cơ bản nhất và nên được học thật chắc trước khi thêm nguồn hoặc hệ số biến thiên.

### Ví dụ 2: Có nguồn nhiệt đều

Nếu thanh có nguồn nhiệt không đổi $$ Q=Q_0 $$, thì phương trình trở thành

$$ u_t=\alpha^2u_{xx}+\frac{Q_0}{\rho c}. $$

Ý nghĩa vật lý rất rõ: ngoài khuếch tán, hệ còn được bơm nhiệt đều khắp miền.

### Ví dụ 3: Hệ số dẫn nhiệt biến thiên

Nếu vật liệu không đồng nhất, ta không được viết đơn giản là $$ k u_{xx} $$. Thay vào đó phải giữ dạng $$ \rho c\,u_t=(k(x)u_x)_x+Q $$. Ví dụ này rất quan trọng để sinh viên thấy mô hình PDE nhạy với cấu trúc vật liệu như thế nào.

### Ví dụ 4: Ý nghĩa làm mượt

Giả sử dữ liệu ban đầu có một đỉnh nhiệt cục bộ. Tại vùng đỉnh, $$ u_{xx}<0 $$, nên nếu không có nguồn thì $$ u_t<0 $$. Điều đó nghĩa là đỉnh giảm xuống theo thời gian. Tương tự, tại một hõm, $$ u_{xx}>0 $$ nên nhiệt độ tăng lên. Đây là ví dụ ngắn nhưng cực kỳ mạnh để nối công thức với trực giác.

## Câu hỏi khái niệm

1. Vì sao tốc độ thay đổi nhiệt độ tại một điểm lại liên hệ với độ cong của đồ thị nhiệt độ chứ không chỉ với giá trị nhiệt độ tại chính điểm đó?
2. Dấu trừ trong định luật Fourier phản ánh điều gì về dòng nhiệt?
3. Vì sao phương trình nhiệt làm mượt dữ liệu ban đầu thay vì tạo ra các đỉnh mới?

## Bài toán ứng dụng

1. Một thanh kim loại được nung nóng cục bộ ở giữa. Hãy giải thích bằng lời vì sao vùng nóng sẽ lan ra và đồng thời hạ đỉnh nhiệt độ.
2. Trong sinh học, nếu $$ u $$ là nồng độ một chất khuếch tán, định luật tương tự Fourier sẽ có nghĩa vật lý gì?
3. Trong vật liệu không đồng nhất, vì sao hệ số dẫn nhiệt biến thiên theo vị trí làm phương trình phải đổi sang dạng $$ (k(x)u_x)_x $$ thay vì

$$ k u_{xx}? $$

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu một điểm nóng hơn hàng xóm của nó, nhiệt sẽ đi theo hướng nào?"
- Cho sinh viên mô tả bằng lời hình dạng đồ thị nào làm cho nhiệt độ giảm và hình dạng nào làm nhiệt độ tăng.
- Tổ chức hoạt động nhóm nhỏ: một nhóm trình bày định luật Fourier, nhóm khác trình bày bảo toàn năng lượng, rồi ghép hai ý tưởng lại để tạo PDE.
- Dùng đồ thị có đỉnh và hõm để yêu cầu lớp dự đoán dấu của

$$ u_t $$

trước khi viết phương trình.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên dạy thật chậm bằng phiên bản một chiều trước, với một đoạn nhỏ của thanh. Khi trực giác và công thức một chiều đã chắc, việc hiểu dạng nhiều chiều sẽ nhẹ hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tự suy ra dạng nhiều chiều bằng định lý divergence, hoặc thảo luận vì sao mô hình khuếch tán khác căn bản với mô hình sóng ở tốc độ lan truyền thông tin.

## Tóm tắt dễ nhớ

Phương trình nhiệt xuất phát từ bảo toàn năng lượng cộng với định luật Fourier. Dòng nhiệt đi từ nóng sang lạnh, nên tốc độ thay đổi nhiệt độ tại một điểm được quyết định bởi độ cong không gian của nhiệt độ. Vì vậy phương trình nhiệt có bản chất khuếch tán và làm mượt dữ liệu theo thời gian.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dẫn nhiệt trong thanh kim loại
- Bài toán: Nhiệt lan truyền từ vùng nóng sang vùng lạnh trong một thanh dài.
- Mô hình:
$$ u_t=\alpha^2 u_{xx}. $$
- Giả thiết và giới hạn: Dẫn nhiệt một chiều, vật liệu đồng nhất, bỏ qua nguồn ngoài.
- Diễn giải: Đạo hàm thời gian đo tốc độ đổi nhiệt, còn đạo hàm không gian bậc hai đo độ cong của profile nhiệt.

#### Khuếch tán chất hòa tan
- Bài toán: Nồng độ muối hay thuốc nhuộm lan dần trong môi trường lỏng.
- Mô hình: Cùng phương trình nhiệt với $$ u $$ là nồng độ.
- Giả thiết và giới hạn: Hệ số khuếch tán hằng, môi trường đồng nhất.
- Diễn giải: Phương trình nhiệt là mô hình chuẩn cho mọi quá trình làm "phẳng" chênh lệch nồng độ.

### 2. Trực giác bổ sung và các kết nối

Phương trình nhiệt là mô hình điển hình của khuếch tán: nơi nào profile cong nhiều thì thời gian sẽ kéo nó phẳng lại. Một bẫy phổ biến là nghĩ đạo hàm bậc hai chỉ là kỹ thuật tính toán; thật ra nó đo độ lệch khỏi cân bằng cục bộ. Bài này nối tự nhiên từ trạng thái dừng ở Chương 7 sang tiến hóa theo thời gian.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u0 = np.where(x < 0.5, 1.0, 0.0)

plt.plot(x, u0, label="t = 0")
for t, sigma in [(0.002, 0.03), (0.01, 0.07), (0.03, 0.12)]:
    kernel = np.exp(-((x[:, None] - x[None, :])**2) / (4 * sigma**2))
    kernel /= kernel.sum(axis=1, keepdims=True)
    ut = kernel @ u0
    plt.plot(x, ut, label=f"t ~ {t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Lam phang profile nhiet theo thoi gian")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: heat equation diffusion animation
- search: derivation Fourier law conservation energy heat equation
- search: smoothing effect heat equation

### 5. Bài toán mẫu có bối cảnh thực

Từ định luật Fourier
$$ q=-k u_x $$
và bảo toàn năng lượng trên một đoạn nhỏ, ta suy ra
$$ u_t=\alpha^2 u_{xx}. $$
Thông điệp vật lý cốt lõi là: thông lượng nhiệt đi theo hướng giảm nhiệt độ, và tốc độ đổi nhiệt tại một điểm được quyết định bởi chênh lệch thông lượng hai phía.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu suy ra phương trình từ bảo toàn năng lượng và định luật Fourier.

**Bậc sau đại học.** Nhấn mạnh bản chất parabolic, tính làm trơn tức thời và đối chiếu với phương trình sóng/hàm điều hòa.
