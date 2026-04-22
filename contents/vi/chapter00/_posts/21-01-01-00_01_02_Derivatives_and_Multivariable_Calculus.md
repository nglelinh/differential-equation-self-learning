---
layout: post
title: "00-03 Đạo hàm và Giải tích đa biến"
chapter: '00'
order: 3
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---

## Mục tiêu
Bài học này giúp sinh viên hiểu sâu sắc đạo hàm như phép tuyến tính hóa cục bộ, nắm vững các công cụ giải tích đa biến (gradient, Jacobian, Hessian), và vận dụng quy tắc dây chuyền, định lý hàm ẩn trong việc chuyển đổi và giải các phương trình vi phân. Đây là cầu nối từ giải tích một biến sang không gian nhiều chiều của hệ ODE.

## Kiến thức nền
Sinh viên cần thành thạo đạo hàm và vi phân cơ bản một biến, hiểu khái niệm hàm số và đồ thị, biết vận dụng quy tắc dây chuyền đơn giản. Kiến thức về ma trận và vector sẽ giúp ích nhưng không bắt buộc ở mức đầu.

## Dẫn nhập
Trong các bài trước, ta làm việc với hàm một biến $$ y = f(t) $$. Nhưng thế giới thực phong phú hơn nhiều: nhiệt độ phụ thuộc vào cả vị trí và thời gian $$ u(x,t) $$, hệ sinh thái có nhiều loài tương tác $$ P(t) $$, $$ Q(t) $$, hay mạch điện có nhiều dòng chảy $$ I_1(t) $$, $$ I_2(t) $$. Khi đó, ta cần "đạo hàm nhiều chiều."

Hãy hình dung ta đang đứng trên một ngọn núi. Độ dốc theo hướng đông-tây là $$ \partial z/\partial x $$, theo hướng bắc-nam là $$ \partial z/\partial y $$. Vector gradient $$\left(\partial z/\partial x,\partial z/\partial y\right)$$ chỉ hướng leo dốc nhất. Từ gradient, ta biết ngay lập tức hướng nào đi lên nhanh nhất, hướng nào đi xuống. Đây là thông tin quan trọng trong nhiều bài toán tối ưu và điều khiển ODE.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Đạo hàm một biến $$ f'(a) $$ là hệ số góc của tiếp tuyến tại $$ \left(a, f(a)\right) $$. Nó cho ta xấp xỉ tuyến tính $$ f(a + h) \approx f(a) + f'(a)h $$. Với hàm hai biến, đạo hàm riêng $$ \partial f/\partial x(a,b) $$ là hệ số góc khi ta cố định $$ y = b $$ và chỉ di chuyển theo hướng $$ x $$. Còn gradient $$ \nabla f $$ là vector tổng hợp cả hai hướng, cho ta mặt phẳng tiếp xúc tại điểm.

### Cách nhìn hình ảnh
Vẽ mặt $$ z = x^2 + y^2 $$, một paraboloid. Tại điểm $$ \left(1,1,2\right) $$, gradient là $$ \nabla f = (2x, 2y) = (2,2) $$, hướng lên trên theo đường chéo $$ 45^\circ $$. Mặt phẳng tiếp xúc tại đó có phương trình $$ z = 2 + 2(x-1) + 2(y-1) $$. Mọi vector tiếp tuyến đều nằm trong mặt phẳng này, và gradient là vector vuông góc với mặt phẳng đó.

### Cách nhìn hình thức
**Đạo hàm riêng**: $$\frac{\partial f}{\partial x}(a,b) = \lim_{h \to 0} \frac{f(a+h,b) - f(a,b)}{h}$$, với các biến khác được giữ nguyên.

**Gradient**: $$\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right)$$. Gradient chỉ hướng tăng nhanh nhất và vuông góc với các đường mức.

**Jacobian**: Với $$ F:\mathbb{R}^n \to \mathbb{R}^m $$, ma trận Jacobi $$ DF $$ có các phần tử $$ \left(DF\right)_{ij} = \partial f_i/\partial x_j $$. Nó là ánh xạ tuyến tính xấp xỉ $$ F $$ tại mỗi điểm.

**Quy tắc dây chuyền**: Nếu $$ x = x(t) $$ và $$ y = y(t) $$, với $$ z = f(x(t), y(t)) $$, thì

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.
$$

**Định lý hàm ẩn**: Nếu $$ F(x,y) = 0 $$ và $$ \partial F/\partial y \neq 0 $$ tại $$ \left(a,b\right) $$, thì tồn tại hàm $$ y = f(x) $$ định bởi $$ F(x,f(x)) = 0 $$ trong lân cận của $$ a $$, với

$$
f'(a) = -\frac{\partial F/\partial x(a,b)}{\partial F/\partial y(a,b)}.
$$

## Những ngộ nhận thường gặp
- "Đạo hàm riêng $$ \partial f/\partial x $$ và $$ \partial f/\partial y $$ là hai đạo hàm độc lập." Không đúng. Chúng là hai thành phần của cùng một vector gradient, và tại mỗi điểm, chúng xác định hoàn toàn mặt phẳng tiếp xúc.
- "Gradient luôn chỉ hướng tăng nhanh nhất." Đúng về hướng, nhưng giá trị (độ dài) của gradient cho biết tốc độ tăng. Vector đơn vị gradient mới chỉ hướng.
- "Nếu $$ \partial f/\partial x = 0 $$ và $$ \partial f/\partial y = 0 $$ thì đó là điểm cực trị." Sai. Điểm của đồ thị $$ y = x^3 $$ tại gốc cho ta ví dụ về điểm dừng không phải cực trị.
- "Quy tắc dây chuyền chỉ áp dụng cho hàm hợp một biến." Sai. Nó tổng quát cho nhiều biến: $$ dz/dt = \nabla f \cdot r'(t) $$, trong đó $$ r'(t) $$ là vector đạo hàm của đường cong.

## Tiến trình học tập đề xuất

### Bước 1: Từ đạo hàm một biến đến đạo hàm riêng
Hiểu rằng đạo hàm riêch là "bóng" của đạo hàm thông thường khi ta chỉ di chuyển theo một hướng. Quan sát đồ thị để thấy ý nghĩa hình học.

### Bước 2: Hiểu gradient như vector
Gradient không chỉ là ký hiệu toán mà mang ý nghĩa hình học rõ ràng: hướng tăng nhanh nhất, và gradient = 0 là điểm dừng (có thể là cực trị hoặc điểm yên ngựa).

### Bước 3: Quy tắc dây chuyền và hàm ẩn
Đây là hai công cụ trung tâm. Quy tắc dây chuyền cho phép tính đạo hàm của hàm hợp. Định lý hàm ẩn cho phép ta "giải" một phương trình để được hàm ẩn và tính đạo hàm của nó mà không cần tìm công thức tường minh.

### Các checkpoint
- Sinh viên có tính được gradient và hiểu ý nghĩa hình học không?
- Sinh viên có vận dụng đúng quy tắc dây chuyền trong các tình huống khác nhau không?
- Sinh viên có biết khi nào định lý hàm ẩn áp dụng được không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tính gradient và hiểu ý nghĩa
Cho $$ f(x,y) = x^2 + xy + y^2 $$. Ta có $$ \partial f/\partial x = 2x + y $$, $$ \partial f/\partial y = x + 2y $$. Tại điểm $$ \left(1,2\right) $$, gradient là $$ \nabla f(1,2) = (4,5) $$. Vector này chỉ hướng tăng nhanh nhất. Đường mức $$ f(x,y) = 7 $$ đi qua $$ \left(1,2\right) $$ có pháp vector $$ \left(4,5\right) $$, nên đường tiếp tuyến tại đó có phương trình $$ 4(x-1) + 5(y-2) = 0 $$.

### Ví dụ 2: Quy tắc dây chuyền
Cho $$ z = f(x,y) = x^2 + y^2 $$, với $$ x = t^3 $$, $$ y = t^2 $$. Theo quy tắc dây chuyền,

$$
\frac{dz}{dt}
= \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}
= (2x)(3t^2) + (2y)(2t)
= 6t^5 + 4t^3.
$$

Kiểm tra bằng cách thay trực tiếp: $$ z = (t^3)^2 + (t^2)^2 = t^6 + t^4 $$, nên $$ dz/dt = 6t^5 + 4t^3 $$.

### Ví dụ 3: Định lý hàm ẩn
Từ phương trình $$ x^2 + y^2 = 1 $$, ta có $$ F(x,y) = x^2 + y^2 - 1 $$. Tính $$ \partial F/\partial y = 2y $$. Tại điểm $$ \left(0,1\right) $$, giá trị này khác $$ 0 $$, nên tồn tại hàm $$ y = f(x) $$ định bởi $$ x^2 + f(x)^2 = 1 $$ trong lân cận $$ x = 0 $$. Đạo hàm là

$$
f'(x) = -\frac{\partial F/\partial x}{\partial F/\partial y} = -\frac{2x}{2y} = -\frac{x}{y}.
$$

Tại $$ x = 0 $$, $$ y = 1 $$, ta có $$ f'(0) = 0 $$.

### Ví dụ 4: Ma trận Jacobian cho hệ
Cho $$ F(x,y) = (u(x,y), v(x,y)) = (x^2 + y, xy) $$. Khi đó

$$
DF =
\begin{pmatrix}
\partial u/\partial x & \partial u/\partial y \\
\partial v/\partial x & \partial v/\partial y
\end{pmatrix}
=
\begin{pmatrix}
2x & 1 \\
y & x
\end{pmatrix}.
$$

Tại $$ \left(1,1\right) $$, Jacobian là $$\begin{pmatrix}2 & 1 \\ 1 & 1\end{pmatrix}$$. Đây là ánh xạ tuyến tính xấp xỉ $$ F $$ gần điểm đó.

### Ví dụ 5: Áp dụng trong ODE - phương trình phân ly
Xét phương trình dy/dx = g(x)h(y). Viết F(x,y) = g(x)h(y) - y'. Để tìm nghiệm, ta "tách biến": 1/h(y) dy = g(x) dx. Đây là ứng dụng của tích phân riêng: ta tích phân theo từng biến riêng biệt. Đạo hàm riêng cho ta cách "tách" ảnh hưởng của x và y.

## Câu hỏi khái niệm
1. Tại sao gradient vuông góc với đường mức? Ý nghĩa hình học của điều này là gì?
2. Định lý hàm ẩn đảm bảo điều gì? Tại sao điều kiện $$ \partial F/\partial y \neq 0 $$ lại quan trọng?
3. Jacobian tổng quát hóa đạo hàm một biến như thế nào? Khi nào nó đặc biệt quan trọng trong ODE?

## Bài toán ứng dụng
1. **Vật lý**: Trường nhiệt độ $$ T(x,y,z,t) $$. Gradient $$ -\nabla T $$ là vector dòng nhiệt. Giải thích ý nghĩa vật lý của mỗi thành phần.
2. **Kinh tế**: Hàm sản xuất Cobb-Douglas $$ Y(L,K) = AL^\alpha K^\beta $$. Tính $$ \partial Y/\partial L $$ và $$ \partial Y/\partial K $$. Giải thích ý nghĩa kinh tế.
3. **Sinh học**: Mô hình Lotka-Volterra $$ dP/dt = \alpha P - \beta PQ $$, $$ dQ/dt = \delta PQ - \gamma Q $$. Viết dưới dạng vector và nhận xét về Jacobian tại điểm cân bằng.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Vẽ gradient"**: Cho sinh viên vẽ đồ thị một số hàm hai biến đơn giản như $$ x^2+y^2 $$, $$ xy $$, $$ x^2-y^2 $$ và đánh dấu gradient tại nhiều điểm.
- **Thảo luận nhóm**: Cho mỗi nhóm một hàm ẩn F(x,y)=0 và yêu cầu xác định xem có thể giải được y=f(x) hay không, tính f'(x). Các nhóm trình bày kết quả.
- **Câu hỏi nhanh**: "Gradient của $$ f(x,y) = x^2 - y^2 $$ tại $$ \left(1,1\right) $$ chỉ hướng nào? Đây là điểm gì?".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Bắt đầu từ đạo hàm một biến quen thuộc, sau đó mới thêm biến thứ hai.
- Vẽ nhiều đồ thị 3D trực quan (có thể dùng phần mềm hoặc hình vẽ).
- Luyện tập với các hàm đơn giản trước: $$ x+y $$, $$ xy $$, $$ x^2+y^2 $$.

### Thử thách cho sinh viên khá giỏi
- Nghiên cứu và trình bày về định lý hàm ngược và ứng dụng.
- So sánh gradient descent trong tối ưu hóa với phương pháp Euler trong ODE.
- Tìm hiểu về ma trận Hessian và ứng dụng trong phân tích ổn định của hệ ODE.

## Tóm tắt dễ nhớ
**Gradient $$ \nabla f $$**: Vector chỉ hướng tăng nhanh nhất, vuông góc với đường mức.
**Quy tắc dây chuyền**: $$ dz/dt = \nabla f \cdot r'(t) $$.
**Hàm ẩn**: $$ f'(x) = -F_x/F_y $$ khi $$ F_y \neq 0 $$.
**Jacobian**: Ma trận tổng quát hóa đạo hàm cho ánh xạ nhiều biến.
Trong ODE nhiều chiều, gradient và Jacobian cho ta "bản đồ" cục bộ của trường vector.

## Tài liệu tham khảo
- Marsden & Tromba — *Vector Calculus*: giáo trình chuẩn về giải tích đa biến.
- Apostol — *Calculus, Vol. 2*: chi tiết về đạo hàm riêng và ứng dụng.
- Hirsch, Smale & Devaney — *Differential Equations*: liên hệ trực tiếp với hệ ODE.
