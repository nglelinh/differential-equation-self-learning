---
layout: post
title: "Phương Trình Laplace: Giới Thiệu"
chapter: '11'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---
![21 03 18 11 01 Laplace Equation Introduction]({{ site.imgurl }}/chapter_img/chapter11/01_laplace_equation_introduction.svg)

## Mục tiêu

Bài học này mở đầu chương elliptic bằng cách giúp sinh viên hiểu phương trình Laplace là mô hình của trạng thái cân bằng không có nguồn nội tại. Sau bài học, sinh viên cần biết hàm điều hòa là gì, hiểu vì sao $$ \Delta u=0 $$ xuất hiện trong tĩnh điện, nhiệt ổn định và dòng chảy thế, nhận ra vai trò quyết định của dữ liệu biên, và thấy được sự khác biệt bản chất giữa phương trình Laplace với phương trình nhiệt và sóng.

## Kiến thức nền

Sinh viên nên nắm đạo hàm riêng, toán tử Laplace, ý tưởng về bài toán biên, và trực giác từ các chương trước về PDE theo thời gian. Bài này là một bước chuyển quan trọng: từ PDE tiến hóa sang PDE cân bằng.

## Dẫn nhập

Ở phương trình nhiệt, ta hỏi hệ tiến hóa theo thời gian thế nào. Ở phương trình sóng, ta hỏi nhiễu loạn truyền đi ra sao. Nhưng có rất nhiều bài toán vật lý mà trạng thái đã ổn định: không còn biến thiên theo thời gian, không còn quán tính, cũng không còn khuếch tán tiếp diễn. Khi ấy, điều ta tìm là một cấu hình cân bằng hoàn toàn do biên quyết định. Đó là thế giới của phương trình Laplace.

Điều rất đẹp ở đây là cùng một phương trình đơn giản $$ \Delta u=0 $$ lại xuất hiện trong nhiều bối cảnh: điện thế trong vùng không có điện tích, nhiệt độ ổn định không nguồn, và thế vận tốc của dòng chảy không nén được, không xoáy. Bài học này giúp sinh viên nhìn thấy sự thống nhất đó ngay từ đầu.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng một tấm kim loại đã đạt trạng thái nhiệt ổn định. Nhiệt độ bên trong không còn thay đổi theo thời gian. Nếu ở đâu đó trong tấm có nhiệt độ cao hơn rõ rệt so với xung quanh, thì cân bằng chưa thật sự đạt được vì nhiệt vẫn còn xu hướng chảy đi. Vì thế trong trạng thái cân bằng thật, giá trị tại một điểm phải được "cân bằng" bởi các giá trị xung quanh. Đó là trực giác cốt lõi của hàm điều hòa.

### Cách nhìn hình ảnh

Đồ thị của một hàm điều hòa không thể tạo ra một ngọn đỉnh nhọn hay một đáy hõm kín hoàn toàn trong nội thất nếu không phải hằng số. Thay vào đó, nó bị kéo bởi biên. Nếu vẽ các đường mức của điện thế hay nhiệt độ ổn định, ta sẽ thấy chúng được định hình bởi dữ liệu ở biên nhiều hơn là bởi một cơ chế nội tại nào bên trong miền.

### Cách nhìn hình thức

Trong hai chiều, phương trình Laplace có dạng $$ \Delta u=u_{xx}+u_{yy}=0 $$. Trong ba chiều:

$$ \Delta u=u_{xx}+u_{yy}+u_{zz}=0. $$

Một nghiệm của phương trình này được gọi là hàm điều hòa. Trong một chiều, phương trình trở thành $$ u''=0 $$, nên nghiệm chỉ là các hàm affine. Điều này gợi rằng phương trình Laplace mô tả cấu hình không có độ cong nội tại do nguồn bên trong sinh ra.

## Những ngộ nhận thường gặp

- "Laplace chỉ là Poisson với vế phải bằng 0 nên không có gì mới." Sai. Trường hợp không nguồn có cấu trúc định tính rất mạnh và riêng.
- "Nếu không có thời gian thì bài toán phải đơn giản hơn nhiều." Không hẳn; elliptic PDE có các tính chất hình học sâu và phụ thuộc mạnh vào biên.
- "Dữ liệu trong nội thất quyết định nghiệm." Với bài toán Laplace, chính biên mới đóng vai trò trung tâm.
- "Hàm điều hòa có thể có cực đại nội tại như các hàm số thông thường." Sai, trừ khi hàm là hằng.

## Tiến trình học tập đề xuất

### Bước 1: So sánh với nhiệt và sóng

Sinh viên cần thấy rõ đây là bài toán cân bằng chứ không phải bài toán tiến hóa.

### Bước 2: Hiểu hàm điều hòa là trạng thái không nguồn

Đây là câu ngắn gọn nên nhớ đầu tiên của chương.

### Bước 3: Nối với bài toán biên

Điểm quan trọng nhất là nghiệm bên trong bị điều khiển bởi biên.

### Bước 4: Dự đoán các tính chất định tính

Từ trực giác cân bằng, dự đoán nguyên lý cực đại và tính chất trung bình.

### Các checkpoint

- Sinh viên có giải thích được vì sao Laplace là mô hình của cân bằng hay không.
- Sinh viên có kể được ít nhất hai bối cảnh vật lý nơi

$$ \Delta u=0 $$

xuất hiện hay không.
- Sinh viên có thấy vì sao biên là nhân vật chính của bài toán elliptic hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Trường hợp một chiều

Trong một chiều, $$ u''=0 $$ nên $$ u(x)=ax+b $$. Nghiệm là một đường thẳng nối dữ liệu biên. Đây là hình ảnh đơn giản nhất của việc "bên trong được quyết định bởi biên".

### Ví dụ 2: Nhiệt ổn định

Nếu một thanh không có nguồn nhiệt bên trong và đã đạt trạng thái ổn định, nhiệt độ $$ T(x) $$ thỏa $$ T''=0 $$ trong một chiều, hay $$ \Delta T=0 $$ trong nhiều chiều. Điều này giúp nối rất tự nhiên với chương nhiệt vừa học xong.

### Ví dụ 3: Tĩnh điện

Trong miền không có điện tích, điện thế $$ V $$ thỏa $$ \Delta V=0 $$. Điện trường khi đó là $$ \mathbf E=-\nabla V $$. Ví dụ này cho thấy bài toán Laplace không chỉ là hình học của hàm, mà còn là mô hình trường vật lý thực sự.

### Ví dụ 4: Dòng chảy thế

Nếu $$ \mathbf v=\nabla \phi $$ và dòng chảy không nén được, thì $$ \nabla\cdot\mathbf v=0 $$ suy ra $$ \Delta \phi=0 $$. Ví dụ này rất tốt để sinh viên thấy cùng một PDE xuất hiện dưới những tên biến hoàn toàn khác.

## Câu hỏi khái niệm

1. Vì sao một trạng thái cân bằng không có nguồn bên trong lại dẫn đến phương trình Laplace?
2. Tại sao trong bài toán Laplace, biên quyết định mạnh hơn nội thất?
3. Điều gì làm cho phương trình Laplace khác căn bản với nhiệt và sóng dù đều là PDE cổ điển?

## Bài toán ứng dụng

1. Một tấm kim loại mỏng có nhiệt độ cố định trên biên và không có nguồn nhiệt bên trong. Vì sao nhiệt độ ổn định phải thỏa phương trình Laplace?
2. Trong tĩnh điện, vì sao vùng không có điện tích dẫn đến điện thế điều hòa?
3. Trong thủy động lực học, vì sao thế vận tốc của dòng chảy không nén được và không xoáy lại thỏa cùng một phương trình?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu hệ đã ở trạng thái cân bằng hoàn toàn, điều gì còn quyết định giá trị bên trong?"
- Cho sinh viên so sánh ba bối cảnh: nhiệt ổn định, điện thế, và dòng chảy thế để tìm cấu trúc chung.
- Hỏi cả lớp: "Một hàm điều hòa có thể tự tạo đỉnh ở nội thất không, và vì sao?"
- Khuyến khích sinh viên mô tả phương trình Laplace bằng ngôn ngữ vật lý trước khi dùng ký hiệu toán.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào phiên bản một chiều và trực giác "đường thẳng nối hai đầu" trước. Khi trực giác này đã chắc, việc chấp nhận $$ \Delta u=0 $$ trong nhiều chiều sẽ nhẹ hơn rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận quan hệ giữa phương trình Laplace và các bài toán cực tiểu năng lượng, hoặc dự đoán trước tính chất trung bình và nguyên lý cực đại từ trực giác cân bằng.

## Tóm tắt dễ nhớ

Phương trình Laplace là phương trình của cân bằng không nguồn. Hàm điều hòa không có động lực nội tại để tạo cực trị mới bên trong, nên nghiệm bị biên chi phối mạnh. Đây là mô hình nền của tĩnh điện, nhiệt ổn định và dòng chảy thế.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - khuôn khổ chuẩn cho hàm điều hòa, phương trình Poisson, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - trình bày trực quan về tĩnh điện, dòng chảy thế, và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ ổn định trong tấm vật liệu
- Bài toán: Tìm phân bố nhiệt khi hệ đã đạt trạng thái dừng.
- Mô hình:
$$ \Delta u=0. $$
- Giả thiết và giới hạn: Không còn phụ thuộc thời gian, không có nguồn nhiệt bên trong.
- Diễn giải: Hàm điều hòa mô tả trạng thái cân bằng không gian.

#### Điện thế tĩnh điện
- Bài toán: Trong miền không có điện tích, điện thế thỏa một phương trình elliptic.
- Mô hình: Với điện tích bằng không, thế điện $$ \phi $$ thỏa $$ \Delta \phi=0 $$.
- Giả thiết và giới hạn: Môi trường đồng nhất, tĩnh điện, bỏ qua hiệu ứng biên phức tạp.
- Diễn giải: Cùng một PDE mô tả cả cân bằng nhiệt lẫn cân bằng điện thế.

### 2. Trực giác bổ sung và các kết nối

Phương trình Laplace là phiên bản "cân bằng" của nhiều quá trình vật lý. Nếu phương trình nhiệt mô tả sự tiến dần về cân bằng, thì phương trình Laplace mô tả trạng thái đã cân bằng rồi. Một bẫy phổ biến là xem $$ \Delta u=0 $$ như một công thức trừu tượng; thật ra nó phát biểu rằng không còn mất cân bằng cục bộ nào trong miền.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 160)
y = np.linspace(-1, 1, 160)
X, Y = np.meshgrid(x, y)
U = X**2 - Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, U, cmap="coolwarm")
ax.set_title("Vi du mot ham dieu hoa: u = x^2 - y^2")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: harmonic function surface plot
- search: Laplace equation steady state temperature simulation
- search: electrostatic potential Laplace equation visualization

### 5. Bài toán mẫu có bối cảnh thực

Trong một thanh một chiều ở trạng thái dừng và không có nguồn nhiệt, ta có
$$ u''(x)=0. $$
Do đó
$$ u(x)=Ax+B. $$
Nếu $$ u(0)=T_0 $$ và $$ u(L)=T_L $$ thì nghiệm là nội suy tuyến tính giữa hai đầu. Đây là phiên bản đơn giản nhất của tư duy "trạng thái cân bằng không có nguồn".

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu phương trình Laplace như mô hình cân bằng không gian.

**Bậc sau đại học.** Kết nối với ellipticity, regularity và nguyên lý cực đại.
