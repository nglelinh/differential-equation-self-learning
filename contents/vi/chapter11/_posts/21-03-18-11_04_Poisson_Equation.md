---
layout: post
title: "Phương Trình Poisson"
chapter: '11'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---
![21 03 18 11 04 Poisson Equation]({{ site.imgurl }}/chapter_img/chapter11/04_poisson_equation.svg)

## Mục tiêu

Bài học này giới thiệu phương trình Poisson như phiên bản có nguồn của phương trình Laplace. Sau bài học, sinh viên cần hiểu vì sao $$ \Delta u=f $$ là mô hình của cân bằng có nguồn nội tại, biết diễn giải vai trò của dấu và độ lớn của $$ f $$, thấy mối liên hệ với điện tích và nguồn nhiệt, và hiểu ý tưởng biểu diễn nghiệm qua nghiệm cơ bản hoặc hàm Green.

## Kiến thức nền

Sinh viên nên nắm phương trình Laplace, khái niệm hàm điều hòa và trực giác về bài toán biên. Đây là bài giúp sinh viên chuyển từ "không nguồn" sang "có nguồn" trong elliptic PDE.

## Dẫn nhập

Nếu phương trình Laplace mô tả trạng thái cân bằng thuần khiết không có nguồn bên trong, thì Poisson là bước mở rộng tự nhiên khi trong miền có một cơ chế phát sinh hay tiêu hao nội tại. Một phân bố điện tích trong tĩnh điện, một nguồn nhiệt ổn định trong tấm kim loại, hay nhiều mô hình thế khác đều dẫn đến phương trình Poisson.

Điều rất nên nhấn mạnh là Poisson không phá vỡ câu chuyện elliptic, mà làm nó phong phú hơn. Laplace là Poisson với vế phải bằng 0, còn $$ f $$ chính là tác nhân uốn cong trường thế bên trong miền.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu Laplace là "cân bằng không nguồn", thì Poisson là "cân bằng có nguồn". Nơi $$ f>0 $$, nghiệm bị đẩy theo một phía nào đó; nơi $$ f<0 $$, nghiệm bị kéo theo phía ngược lại. Nguồn bên trong làm cho trường bên trong có độ cong nội tại thay vì chỉ phản ứng thụ động với biên.

### Cách nhìn hình ảnh

Với $$ \Delta u=0 $$, trường bên trong bị giữ bởi biên và không tự sinh đỉnh mới. Với $$ \Delta u=f $$, nguồn $$ f $$ giống như một lực "đẩy cong" đồ thị của $$ u $$. Nơi nguồn mạnh hơn, nghiệm cong mạnh hơn. Điều này giúp sinh viên liên hệ trực tiếp giữa dữ liệu nguồn và hình dạng nghiệm.

### Cách nhìn hình thức

Phương trình Poisson có dạng $$ \Delta u=f $$. Nếu $$ f=0 $$, ta quay về phương trình Laplace. Trong tĩnh điện:

$$ \Delta V=-\frac{\rho}{\varepsilon_0}, $$

với $$ \rho $$ là mật độ điện tích. Trong nhiệt ổn định:

$$ -k\Delta T=Q, $$

với $$ Q $$ là nguồn nhiệt thể tích. Trong toàn không gian, nếu có nghiệm cơ bản $$ \Phi $$, ta có thể hình dung nghiệm như một chập $$ u=\Phi*f $$ trong những điều kiện thích hợp.

## Những ngộ nhận thường gặp

- "Poisson chỉ khác Laplace ở việc thêm một vế phải, nên không cần học riêng." Sai. Vế phải chính là phần mang ý nghĩa vật lý của nguồn.
- "Dấu của

$$ f $$

không quan trọng." Sai; nó quyết định hướng cong của nghiệm.
- "Nếu có nguồn thì dữ liệu biên không còn quan trọng." Không đúng; elliptic PDE vẫn bị biên chi phối rất mạnh.
- "Chỉ cần biết

$$ f $$

là có thể bỏ qua miền và điều kiện biên." Sai; nguồn và biên cùng xác định nghiệm.

## Tiến trình học tập đề xuất

### Bước 1: So sánh Laplace và Poisson

Sinh viên nên thấy rõ mối liên hệ nền tảng giữa hai phương trình.

### Bước 2: Hiểu ý nghĩa của nguồn

Đây là phần bản chất nhất của bài.

### Bước 3: Nối với ứng dụng vật lý

Điện tích và nguồn nhiệt là hai ví dụ mạnh nhất.

### Bước 4: Giới thiệu biểu diễn nghiệm

Nghiệm cơ bản và hàm Green là ngôn ngữ tự nhiên tiếp theo.

### Các checkpoint

- Sinh viên có giải thích được vì sao Poisson là Laplace có nguồn hay không.
- Sinh viên có diễn giải được dấu của

$$ f $$

về mặt hình học hay không.
- Sinh viên có hiểu vì sao nguồn không thay thế vai trò của điều kiện biên hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Một chiều

Trong một chiều, $$ u''=f(x) $$. Nếu $$ f(x)=1 $$, thì nghiệm là một hàm bậc hai:

$$ u(x)=\frac{x^2}{2}+ax+b. $$

Ví dụ này rất hữu ích vì nó cho sinh viên thấy ngay "nguồn hằng" tạo ra độ cong đều.

### Ví dụ 2: Tĩnh điện

Nếu mật độ điện tích $$ \rho $$ khác 0 trong một vùng, điện thế $$ V $$ thỏa

$$ \Delta V=-\frac{\rho}{\varepsilon_0}. $$

Ví dụ này là cầu nối trực tiếp sang ứng dụng tĩnh điện ở cuối chương.

### Ví dụ 3: Nhiệt ổn định với nguồn

Nếu một tấm có nguồn nhiệt phân bố đều, nhiệt độ ổn định không còn điều hòa mà thỏa Poisson. Ví dụ này giúp sinh viên nối chương elliptic với chương nhiệt đã học trước đó.

### Ví dụ 4: Dạng tích chập trong toàn không gian

Trong toàn không gian, ta có thể viết $$ u=\Phi*f $$ khi điều kiện suy giảm phù hợp. Ví dụ này báo trước vai trò của nghiệm cơ bản và hàm Green ở bài kế tiếp.

## Câu hỏi khái niệm

1. Vì sao một nguồn nội tại làm bài toán chuyển từ Laplace sang Poisson?
2. Dấu của $$ f $$ ảnh hưởng đến độ cong của nghiệm như thế nào?
3. Vì sao bài toán Poisson vẫn là bài toán biên chứ không chỉ là bài toán nguồn?

## Bài toán ứng dụng

1. Trong tĩnh điện, vì sao một phân bố điện tích thể tích dẫn đến phương trình Poisson cho điện thế?
2. Trong truyền nhiệt ổn định, vì sao một nguồn nhiệt bên trong làm nhiệt độ không còn thỏa Laplace?
3. Nếu $$ f $$ chỉ khác 0 trong một vùng nhỏ, vì sao ảnh hưởng của nguồn vẫn lan ra toàn miền qua nghiệm của Poisson?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu trong miền có nguồn, cân bằng còn 'phẳng' như trước nữa không?"
- Cho sinh viên so sánh trực tiếp bài toán

$$ u''=0 $$

với $$ u''=1 $$ trong một chiều.
- Hỏi cả lớp: "Nguồn nội tại đang thay đổi điều gì trong cấu trúc của nghiệm?"
- Khuyến khích sinh viên kể bằng lời một ví dụ vật lý mà trong đó có nguồn bên trong miền.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào ví dụ một chiều trước để trực giác về độ cong trở nên rõ. Sau khi thấy $$ u''=f $$ trong một chiều, việc chấp nhận $$ \Delta u=f $$ trong nhiều chiều sẽ nhẹ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận vai trò của nghiệm cơ bản trong toàn không gian, hoặc so sánh Poisson với các bài toán cực tiểu năng lượng có thêm nguồn.

## Tóm tắt dễ nhớ

Phương trình Poisson là phương trình của cân bằng có nguồn. Laplace mô tả trường không nguồn, còn Poisson cho biết nguồn nội tại uốn cong nghiệm như thế nào. Dù có nguồn, bài toán vẫn bị biên chi phối mạnh và vẫn thuộc thế giới elliptic.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - khuôn khổ chuẩn cho hàm điều hòa, phương trình Poisson, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - trình bày trực quan về tĩnh điện, dòng chảy thế, và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tấm có nguồn nhiệt phân bố
- Bài toán: Một tấm mỏng được đốt nóng bên trong nên trạng thái dừng không còn là Laplace mà là Poisson.
- Mô hình:
$$ -\Delta u=f. $$
- Giả thiết và giới hạn: Nguồn $$ f $$ đã biết, vật liệu đồng nhất, trạng thái dừng.
- Diễn giải: Vế phải đo mức độ mất cân bằng nội tại do nguồn.

#### Võng của màng chịu tải
- Bài toán: Độ võng tĩnh của màng hay màng đàn hồi dưới tải phân bố.
- Mô hình: Một dạng Poisson với $$ f $$ là tải trọng.
- Giả thiết và giới hạn: Biến dạng nhỏ, tải đã biết.
- Diễn giải: So với Laplace, Poisson cho biết miền không còn "không nguồn".

### 2. Trực giác bổ sung và các kết nối

Nếu Laplace mô tả cân bằng thuần, thì Poisson mô tả cân bằng có cưỡng bức bên trong. Nguồn dương hay âm tạo độ cong trung bình trong nghiệm. Một lỗi phổ biến là quên ý nghĩa vật lý của dấu trừ hoặc quy ước dấu của nguồn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u = 0.5 * x * (1 - x)

plt.plot(x, u)
plt.xlabel("x")
plt.ylabel("u")
plt.title("Nghiem 1D cua -u'' = 1 voi u(0)=u(1)=0")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Poisson equation source term interpretation
- search: membrane deflection Poisson equation
- search: steady state heat equation with source

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ 0<x<1 $$, giải
$$ -u''=1, \qquad u(0)=u(1)=0. $$
Tích phân hai lần cho
$$ u(x)=\frac{1}{2}x(1-x). $$
Hàm nghiệm cong lên trên vì có nguồn dương phân bố đều. Đây là mô hình đơn giản cho nhiệt độ hay độ võng dưới tải đều.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ Laplace và Poisson qua vai trò của nguồn.

**Bậc sau đại học.** Kết nối với weak formulation, regularity elliptic và nguyên lý cực đại có nguồn.
