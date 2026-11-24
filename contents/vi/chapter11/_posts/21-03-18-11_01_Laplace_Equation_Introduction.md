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

Hãy nhúng một khung dây thép uốn cong bất kỳ vào chậu nước xà phòng rồi nhấc lên: màng xà phòng căng mịn hiện ra trong nháy mắt không có một đỉnh nhọn hay hố lõm nào bên trong. Ở trạng thái cân bằng, mọi điểm trên màng chỉ làm đúng một việc đơn giản: **trung bình hóa độ cao của các điểm lân cận quanh nó**. Khi viết sự cân bằng ấy thành ngôn ngữ vi phân, ta thu được **Phương trình Laplace** $\Delta u = u_{xx} + u_{yy} = 0$—trái tim của thế giới PDE elliptic!

## Bản đồ kiến thức nền: Bốn trực giác cốt lõi để làm chủ Phương trình Laplace

1. **Ý nghĩa hình học của Toán tử Laplace $\Delta u$**:
   Đạo hàm bậc hai $u_{xx}$ đo độ cong theo trục $x$, còn $u_{yy}$ đo độ cong theo trục $y$. Điều kiện $u_{xx} + u_{yy} = 0$ buộc mọi điểm bên trong phải có dạng **yên ngựa** (cong lên theo hướng này bao nhiêu thì phải cong xuống theo hướng vuông góc bấy nhiêu).
2. **Trạng thái dừng của Nhiệt và Sóng**:
   Khi nhiệt độ $u_t = \alpha \Delta u$ hoặc màng rung $u_{tt} = c^2 \Delta u$ ngừng biến đổi theo thời gian ($u_t = 0, u_{tt} = 0$), cả hai đều hội tụ về cùng một phương trình cân bằng $\Delta u = 0$.
3. **Bài toán Biên (BVP) thay vì Bài toán Giá trị Ban đầu (IVP)**:
   Phương trình Laplace không có biến thời gian: nghiệm tại mọi điểm bên trong miền $\Omega$ được quyết định đồng thời và tức thì bởi toàn bộ dữ liệu trên biên $\partial \Omega$ (Dirichlet cho $u$, Neumann cho $\partial u/\partial n$, hoặc Robin).
4. **Tính đặt chỉnh (Well-posedness) và Điều kiện tương thích**:
   Bài toán Dirichlet đặt chỉnh duy nhất; bài toán Neumann chỉ có nghiệm khi tổng thông lượng qua biên bằng $0$ ($\oint_{\partial\Omega} \frac{\partial u}{\partial n}\,ds = 0$) và nghiệm duy nhất sai khác một hằng số cộng.

## Mục tiêu

Bài học này mở đầu chương về phương trình elliptic, giúp sinh viên hiểu phương trình Laplace là mô hình của trạng thái cân bằng không có nguồn bên trong. Sau bài học, sinh viên cần nắm khái niệm hàm điều hòa, hiểu vì sao $$ \Delta u=0 $$ xuất hiện trong tĩnh điện, truyền nhiệt ổn định và dòng chảy thế, nhận ra vai trò quyết định của dữ liệu biên, và phân biệt được bản chất giữa phương trình Laplace với phương trình nhiệt và phương trình sóng.

## Kiến thức nền

Sinh viên cần nắm đạo hàm riêng, toán tử Laplace, khái niệm bài toán biên và trực giác từ các chương trước về PDE phụ thuộc thời gian. Bài học này đánh dấu bước chuyển quan trọng từ PDE tiến hóa sang PDE cân bằng.

## Dẫn nhập

Với phương trình nhiệt, ta khảo sát hệ tiến hóa theo thời gian như thế nào. Với phương trình sóng, ta quan tâm nhiễu loạn lan truyền ra sao. Tuy nhiên, trong nhiều bài toán vật lý, hệ đã đạt trạng thái ổn định: không còn biến thiên theo thời gian, không còn quán tính và cũng không còn quá trình khuếch tán tiếp diễn. Khi đó, ta cần tìm một cấu hình cân bằng hoàn toàn do điều kiện biên quyết định — đó là phạm vi của phương trình Laplace.

Đáng chú ý là cùng một phương trình $$ \Delta u=0 $$ lại xuất hiện trong nhiều lĩnh vực khác nhau: điện thế trong vùng không có điện tích, nhiệt độ ổn định khi không có nguồn nhiệt và thế vận tốc của dòng chảy không nén được, không xoáy. Bài học này giúp sinh viên nhận thấy sự thống nhất đó ngay từ đầu.


### Khung giải thích (nên đọc chậm): Kiểm tra bằng tay hàm nào là hàm điều hòa và hình dáng mặt yên ngựa

So sánh hai đa thức bậc hai rất giống nhau trên mặt phẳng $\mathbb{R}^2$:
1. **Hàm thứ nhất $u(x, y) = x^2 - y^2$**:
   - $u_{xx} = 2$, $u_{yy} = -2 \implies \Delta u = 2 + (-2) = \mathbf{0}$.
   - **Kết luận**: $u$ là **hàm điều hòa**! Tại gốc $(0, 0)$, đi dọc trục $x$ thì $u$ tăng lên (cong lên), đi dọc trục $y$ thì $u$ giảm xuống (cong xuống)—một mặt yên ngựa hoàn hảo, không có cực đại hay cực tiểu nội tại.
2. **Hàm thứ hai $v(x, y) = x^2 + y^2$**:
   - $v_{xx} = 2$, $v_{yy} = 2 \implies \Delta v = 2 + 2 = \mathbf{4} \neq 0$.
   - **Kết luận**: $v$ **không** điều hòa! Nó có một cực tiểu chặt $v(0,0) = 0$ ngay bên trong miền—điều mà một hàm điều hòa khác hằng không bao giờ có thể có.
## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy xét một tấm kim loại đã đạt trạng thái nhiệt ổn định, tức nhiệt độ bên trong không còn thay đổi theo thời gian. Nếu tại một điểm bên trong tấm, nhiệt độ cao hơn hẳn xung quanh, thì cân bằng chưa thực sự đạt được vì nhiệt vẫn tiếp tục truyền đi. Do đó, ở trạng thái cân bằng, giá trị tại mỗi điểm phải cân bằng với các giá trị xung quanh. Đó là trực giác cốt lõi của hàm điều hòa.

### Cách nhìn hình ảnh

Đồ thị của một hàm điều hòa khác hằng không thể tạo ra đỉnh nhọn hay đáy hõm cục bộ nằm hoàn toàn bên trong miền; thay vào đó, hình dạng của nó bị chi phối bởi giá trị trên biên. Khi vẽ các đường mức của điện thế hay nhiệt độ ổn định, ta thấy chúng được định hình chủ yếu bởi dữ liệu biên chứ không bởi một cơ chế phát sinh nào bên trong miền.

### Cách nhìn hình thức

Trong hai chiều, phương trình Laplace có dạng $$ \Delta u=u_{xx}+u_{yy}=0 $$. Trong ba chiều:

$$ \Delta u=u_{xx}+u_{yy}+u_{zz}=0. $$

Nghiệm của phương trình này được gọi là hàm điều hòa. Trong một chiều, phương trình rút gọn thành $$ u''=0 $$, nên nghiệm chỉ là các hàm tuyến tính (affine). Điều này cho thấy phương trình Laplace mô tả cấu hình không có độ cong nội tại do nguồn bên trong tạo ra.

## Những ngộ nhận thường gặp

- "Laplace chỉ là trường hợp riêng của Poisson khi vế phải bằng 0 nên không có gì mới." Sai; trường hợp không nguồn có cấu trúc định tính riêng và rất chặt chẽ.
- "Không có biến thời gian thì bài toán chắc chắn đơn giản hơn nhiều." Không hẳn; PDE elliptic có những tính chất hình học sâu sắc và phụ thuộc mạnh vào dữ liệu biên.
- "Dữ liệu bên trong miền quyết định nghiệm." Đối với bài toán Laplace, chính dữ liệu trên biên mới giữ vai trò trung tâm.
- "Hàm điều hòa có thể đạt cực đại bên trong miền như các hàm thông thường." Sai, trừ trường hợp hàm hằng.

## Tiến trình học tập đề xuất

### Bước 1: So sánh với phương trình nhiệt và phương trình sóng

Sinh viên cần phân biệt rõ đây là bài toán cân bằng, không phải bài toán tiến hóa.

### Bước 2: Hiểu hàm điều hòa là trạng thái không nguồn

Đây là nhận xét ngắn gọn cần ghi nhớ đầu tiên trong chương.

### Bước 3: Liên hệ với bài toán biên

Điểm cốt lõi là nghiệm bên trong miền bị điều khiển bởi điều kiện biên.

### Bước 4: Dự đoán các tính chất định tính

Từ trực giác cân bằng, dự đoán nguyên lý cực đại và tính chất giá trị trung bình.

### Các checkpoint

- Sinh viên có giải thích được vì sao phương trình Laplace mô tả trạng thái cân bằng hay không.
- Sinh viên có nêu được ít nhất hai bối cảnh vật lý trong đó $$ \Delta u=0 $$ xuất hiện hay không.
- Sinh viên có hiểu vì sao điều kiện biên giữ vai trò trung tâm trong bài toán elliptic hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Trường hợp một chiều

Trong một chiều, $$ u''=0 $$ nên $$ u(x)=ax+b $$. Nghiệm là một đường thẳng nối hai giá trị ở biên — hình ảnh đơn giản nhất cho việc giá trị bên trong được xác định hoàn toàn bởi biên.

### Ví dụ 2: Truyền nhiệt ổn định

Nếu một thanh không có nguồn nhiệt bên trong và đã đạt trạng thái dừng, nhiệt độ $$ T(x) $$ thỏa mãn $$ T''=0 $$ trong một chiều, hoặc $$ \Delta T=0 $$ trong nhiều chiều. Ví dụ này nối tiếp tự nhiên từ chương phương trình nhiệt.

### Ví dụ 3: Tĩnh điện

Trong miền không có điện tích, điện thế $$ V $$ thỏa mãn $$ \Delta V=0 $$, và điện trường tương ứng là $$ \mathbf E=-\nabla V $$. Điều này cho thấy bài toán Laplace không chỉ mang ý nghĩa hình học mà còn mô tả trực tiếp một trường vật lý.

### Ví dụ 4: Dòng chảy thế

Nếu vận tốc có dạng $$ \mathbf v=\nabla \phi $$ và dòng chảy không nén được, thì điều kiện $$ \nabla\cdot\mathbf v=0 $$ dẫn đến $$ \Delta \phi=0 $$. Ví dụ này minh họa rằng cùng một PDE có thể xuất hiện dưới nhiều tên biến và bối cảnh vật lý khác nhau.

## Câu hỏi khái niệm

1. Vì sao một trạng thái cân bằng không có nguồn bên trong lại dẫn đến phương trình Laplace?
2. Tại sao trong bài toán Laplace, điều kiện biên quyết định nghiệm thay vì dữ liệu bên trong miền?
3. Điều gì làm cho phương trình Laplace khác căn bản với phương trình nhiệt và phương trình sóng dù đều là các PDE cổ điển?

## Bài toán ứng dụng

1. Một tấm kim loại mỏng có nhiệt độ cố định trên biên và không có nguồn nhiệt bên trong. Vì sao phân bố nhiệt độ ổn định phải thỏa mãn phương trình Laplace?
2. Trong tĩnh điện, vì sao vùng không có điện tích dẫn đến điện thế là hàm điều hòa?
3. Trong cơ học chất lưu, vì sao thế vận tốc của dòng chảy không nén được và không xoáy lại thỏa mãn cùng phương trình này?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu hệ đã đạt trạng thái cân bằng hoàn toàn, yếu tố nào quyết định giá trị bên trong miền?"
- Cho sinh viên so sánh ba bối cảnh — nhiệt độ ổn định, điện thế và dòng chảy thế — để rút ra cấu trúc toán học chung.
- Hỏi cả lớp: "Một hàm điều hòa có thể tự tạo ra đỉnh cực đại bên trong miền không, và vì sao?"
- Khuyến khích sinh viên diễn đạt ý nghĩa của phương trình Laplace bằng ngôn ngữ vật lý trước khi viết ký hiệu toán học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu từ trường hợp một chiều với trực giác "đường thẳng nối hai đầu mút". Khi đã nắm chắc ý tưởng này, việc tiếp cận $$ \Delta u=0 $$ trong nhiều chiều sẽ thuận lợi hơn.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi tìm hiểu mối liên hệ giữa phương trình Laplace và bài toán cực tiểu hóa năng lượng, hoặc tự dự đoán tính chất giá trị trung bình và nguyên lý cực đại từ trực giác cân bằng.

## Tóm tắt dễ nhớ

Phương trình Laplace mô tả trạng thái cân bằng không có nguồn bên trong. Hàm điều hòa không tự tạo cực trị mới bên trong miền, nên nghiệm bị dữ liệu biên chi phối mạnh. Đây là mô hình nền tảng cho tĩnh điện, truyền nhiệt ổn định và dòng chảy thế.

## Video tham khảo

- xem trước: [Laplace's Equation and Poisson's Equation](https://www.youtube.com/watch?v=nmvs0vrBT18) — Steve Brunton, tiếng Anh. Trình bày và so sánh phương trình Laplace với phương trình Poisson.
- [Laplace's Equation and Potential Flow](https://www.youtube.com/watch?v=zN0zDrQimXU) — Steve Brunton, tiếng Anh. Giới thiệu phương trình Laplace dưới góc nhìn thế vận tốc của dòng chảy không nén được.
- [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, tiếng Anh. Giới thiệu phương pháp tách biến như cách giải đầu tiên cho phương trình Laplace.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ ổn định trong tấm vật liệu
- Bài toán: Tìm phân bố nhiệt độ khi hệ đã đạt trạng thái dừng.
- Mô hình:
$$ \Delta u=0. $$
- Giả thiết và giới hạn: Không còn phụ thuộc thời gian, không có nguồn nhiệt bên trong.
- Diễn giải: Hàm điều hòa mô tả trạng thái cân bằng không gian.

#### Điện thế tĩnh điện
- Bài toán: Tìm điện thế trong miền không có điện tích.
- Mô hình: Khi mật độ điện tích bằng không, điện thế $$ \phi $$ thỏa mãn $$ \Delta \phi=0 $$.
- Giả thiết và giới hạn: Môi trường đồng nhất, trường tĩnh điện, bỏ qua các hiệu ứng biên phức tạp.
- Diễn giải: Cùng một PDE mô tả cả cân bằng nhiệt lẫn cân bằng điện thế.

### 2. Trực giác bổ sung và các kết nối

Phương trình Laplace là phiên bản cân bằng của nhiều quá trình vật lý. Nếu phương trình nhiệt mô tả quá trình tiến dần về trạng thái cân bằng, thì phương trình Laplace mô tả chính trạng thái đã cân bằng đó. Một sai lầm phổ biến là chỉ xem $$ \Delta u=0 $$ như một công thức thuần túy ký hiệu; thực chất nó phát biểu rằng không còn sự mất cân bằng cục bộ nào bên trong miền.

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
Nếu $$ u(0)=T_0 $$ và $$ u(L)=T_L $$, nghiệm là hàm nội suy tuyến tính giữa hai đầu mút. Đây là biểu hiện đơn giản nhất của trạng thái cân bằng không nguồn.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu phương trình Laplace như mô hình cân bằng không gian.

**Bậc sau đại học.** Kết nối với tính elliptic, tính chính quy (regularity) và nguyên lý cực đại.
