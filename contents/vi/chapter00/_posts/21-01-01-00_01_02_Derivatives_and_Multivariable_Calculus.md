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


Trong không gian một chiều, đạo hàm chỉ là độ dốc của một đường tiếp tuyến; nhưng thế giới thực của phương trình vi phân là không gian nhiều biến—nơi nhiệt độ thay đổi theo cả vị trí lẫn thời gian, và hệ động lực có hàng chục trạng thái tương tác lẫn nhau. Khi bước lên nhiều chiều, đạo hàm biến hóa thành **ma trận Jacobi**, **vectơ gradient** và **vi phân toàn phần**—chiếc kính hiển vi tuyến tính hóa cục bộ mọi hiện tượng phi tuyến.

## Kiến thức cần nhớ: Bốn công cụ cốt lõi của Giải tích Đa biến

1. **Đạo hàm riêng & Gradient ($\nabla f$)**:
   Đạo hàm riêng đo tốc độ biến thiên dọc từng trục tọa độ; vectơ $\nabla f$ chỉ hướng tăng nhanh nhất của hàm vô hướng và vuông góc với mọi đường mức $f(x, y) = C$.
2. **Vi phân toàn phần & Xấp xỉ tuyến tính ($df = \nabla f \cdot d\mathbf{x}$)**:
   Thay mặt cong phức tạp quanh một điểm bằng mặt phẳng tiếp xúc—chìa khóa để nhận diện phương trình vi phân toàn phần ở Chương 01.
3. **Ma trận Jacobi ($J_{\mathbf{F}}$) & Quy tắc dây chuyền đa biến**:
   Với ánh xạ vectơ $\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m$, ma trận Jacobi gom toàn bộ đạo hàm riêng cấp một và quyết định tính ổn định cục bộ của hệ phi tuyến ở Chương 05.
4. **Định lý Clairaut–Schwarz ($f_{xy} = f_{yx}$)**:
   Khi đạo hàm riêng cấp hai liên tục, thứ tự lấy đạo hàm giao hoán—đây chính là tiêu chuẩn kiểm tra $M_y = N_x$ cho phương trình vi phân toàn phần và điều kiện trường bảo toàn.

## Mục tiêu
Bài học này giúp sinh viên hiểu đạo hàm theo nghĩa phép tuyến tính hóa cục bộ, nắm vững các công cụ của giải tích đa biến (gradient, ma trận Jacobi, ma trận Hessian), đồng thời vận dụng quy tắc dây chuyền và định lý hàm ẩn khi biến đổi hoặc giải phương trình vi phân. Đây là bước chuyển từ giải tích một biến sang không gian nhiều chiều của hệ ODE.

## Kiến thức nền
Sinh viên cần thành thạo đạo hàm và vi phân cơ bản của hàm một biến, hiểu khái niệm hàm số và đồ thị, cũng như biết áp dụng quy tắc dây chuyền một biến. Kiến thức cơ bản về ma trận và vector sẽ hỗ trợ tốt nhưng chưa bắt buộc ở mức sâu.

## Dẫn nhập
Ở các bài trước, ta chủ yếu xét hàm một biến $$ y = f(t) $$. Tuy nhiên, các mô hình thực tế thường phụ thuộc vào nhiều biến cùng lúc: nhiệt độ thay đổi theo cả vị trí và thời gian $$ u(x,t) $$, hệ sinh thái gồm nhiều quần thể tương tác $$ P(t) $$, $$ Q(t) $$, hay mạch điện có nhiều dòng điện nhánh $$ I_1(t) $$, $$ I_2(t) $$. Vì vậy, ta cần mở rộng khái niệm đạo hàm sang không gian nhiều chiều.

Hãy hình dung bạn đang đứng trên một sườn núi mô tả bởi mặt $$ z = f(x,y) $$. Độ dốc theo phương đông–tây là $$ \partial z/\partial x $$, còn theo phương bắc–nam là $$ \partial z/\partial y $$. Vector gradient $$ \left(\partial z/\partial x, \partial z/\partial y\right) $$ chỉ hướng leo dốc nhanh nhất. Nhờ gradient, ta xác định được ngay hướng tăng nhanh nhất và hướng giảm nhanh nhất của hàm số—thông tin rất hữu ích trong tối ưu hóa và phân tích ODE.

### Giải thích: Tính tay Gradient, Ma trận Jacobi và kiểm tra định lý Clairaut cho $f(x, y) = x^2 y + \sin(xy)$ tại $(1, 0)$

1. **Tính các đạo hàm riêng cấp một**:
   - $f_x(x, y) = 2xy + y\cos(xy)$
   - $f_y(x, y) = x^2 + x\cos(xy)$
   Tại điểm $(1, 0)$: $\nabla f(1, 0) = (0,\; 1 + 1) = \mathbf{(0, 2)}$.
2. **Xấp xỉ tuyến tính gần $(1, 0)$** tại $(1{,}02,\; 0{,}05)$:
   $$f(1{,}02, 0{,}05) \approx f(1, 0) + 0\cdot(0{,}02) + 2\cdot(0{,}05) = 0 + \mathbf{0{,}10}.$$
   (Giá trị thật: $(1{,}02)^2(0{,}05) + \sin(0{,}051) \approx 0{,}05202 + 0{,}05098 = 0{,}1030$, sai số chỉ $0{,}003$!)
3. **Kiểm tra đối xứng đạo hàm hỗn hợp ($f_{xy} = f_{yx}$)**:
   - $f_{xy} = \frac{\partial}{\partial y}(2xy + y\cos(xy)) = 2x + \cos(xy) - xy\sin(xy)$.
   - $f_{yx} = \frac{\partial}{\partial x}(x^2 + x\cos(xy)) = 2x + \cos(xy) - xy\sin(xy)$.
   Hai biểu thức khớp hoàn toàn từng số hạng—đúng như định lý Clairaut–Schwarz khẳng định.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Đạo hàm một biến $$ f'(a) $$ là hệ số góc của tiếp tuyến tại điểm $$ \left(a, f(a)\right) $$, cho xấp xỉ tuyến tính $$ f(a + h) \approx f(a) + f'(a)h $$. Với hàm hai biến, đạo hàm riêng $$ \partial f/\partial x(a,b) $$ là hệ số góc khi cố định $$ y = b $$ và chỉ thay đổi $$ x $$. Kết hợp các đạo hàm riêng lại, ta thu được vector gradient $$ \nabla f $$, từ đó xây dựng được mặt phẳng tiếp xúc của đồ thị tại điểm đang xét.

### Cách nhìn hình ảnh
Xét mặt paraboloid $$ z = x^2 + y^2 $$. Tại điểm $$ \left(1,1,2\right) $$, gradient trong mặt phẳng $$ Oxy $$ là $$ \nabla f(1,1) = (2x, 2y)\big|_{(1,1)} = (2,2) $$, hướng theo đường phân giác góc $$ 45^\circ $$ và vuông góc với đường mức $$ x^2 + y^2 = 2 $$. Mặt phẳng tiếp xúc với mặt cong tại điểm này có phương trình $$ z = 2 + 2(x-1) + 2(y-1) $$, với vector pháp tuyến là $$ (2, 2, -1) $$; mọi vector tiếp tuyến với mặt cong tại $$ (1,1,2) $$ đều nằm trong mặt phẳng này.

### Cách nhìn hình thức
**Đạo hàm riêng**: $$\frac{\partial f}{\partial x}(a,b) = \lim_{h \to 0} \frac{f(a+h,b) - f(a,b)}{h}$$, trong đó các biến khác được giữ cố định.

**Gradient**: $$\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right)$$. Vector gradient chỉ hướng tăng nhanh nhất của hàm và vuông góc với các đường mức (hoặc mặt mức).

**Ma trận Jacobi (Jacobian)**: Với ánh xạ $$ F:\mathbb{R}^n \to \mathbb{R}^m $$, ma trận Jacobi $$ DF $$ có các phần tử $$ \left(DF\right)_{ij} = \partial f_i/\partial x_j $$. Đây là ánh xạ tuyến tính xấp xỉ tốt nhất cho $$ F $$ trong lân cận mỗi điểm.

**Quy tắc dây chuyền**: Nếu $$ x = x(t) $$, $$ y = y(t) $$ và $$ z = f(x(t), y(t)) $$, thì

$$
\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}.
$$

**Định lý hàm ẩn**: Nếu $$ F(x,y) = 0 $$ và $$ \partial F/\partial y \neq 0 $$ tại $$ \left(a,b\right) $$ (với $$ F $$ khả vi liên tục quanh $$ (a,b) $$), thì tồn tại hàm $$ y = f(x) $$ xác định bởi $$ F(x,f(x)) = 0 $$ trong một lân cận của $$ a $$, thỏa mãn

$$
f'(a) = -\frac{\partial F/\partial x(a,b)}{\partial F/\partial y(a,b)}.
$$

## Những ngộ nhận thường gặp
- "Đạo hàm riêng $$ \partial f/\partial x $$ và $$ \partial f/\partial y $$ là hai đại lượng tách rời nhau." Không chính xác. Chúng là hai thành phần của cùng một vector gradient và cùng xác định mặt phẳng tiếp xúc của đồ thị tại điểm đang xét (khi hàm khả vi).
- "Gradient chỉ mang thông tin về hướng tăng nhanh nhất." Chưa đủ. Hướng của gradient là hướng tăng nhanh nhất, còn độ dài $$ \lVert \nabla f \rVert $$ chính là tốc độ tăng cực đại theo hướng đó.
- "Nếu $$ \partial f/\partial x = 0 $$ và $$ \partial f/\partial y = 0 $$ thì điểm đó chắc chắn là cực trị." Sai. Điều kiện đó chỉ cho biết điểm dừng; nó có thể là điểm yên ngựa (chẳng hạn $$ f(x,y) = x^2 - y^2 $$ tại $$ (0,0) $$), tương tự như điểm uốn nằm ngang của $$ y = x^3 $$ tại $$ x = 0 $$ trong trường hợp một biến.
- "Quy tắc dây chuyền chỉ dùng cho hàm hợp một biến." Sai. Quy tắc này mở rộng tự nhiên cho nhiều biến dưới dạng tích vô hướng: $$ dz/dt = \nabla f \cdot r'(t) $$, với $$ r'(t) $$ là vector vận tốc của đường cong $$ r(t) $$.

## Tiến trình học tập đề xuất

### Bước 1: Từ đạo hàm một biến đến đạo hàm riêng
Xem đạo hàm riêng như đạo hàm một biến thông thường khi ta chỉ cho một tọa độ thay đổi và giữ cố định các tọa độ còn lại. Quan sát đồ thị mặt cong để thấy ý nghĩa hình học của từng lát cắt.

### Bước 2: Hiểu gradient như một vector
Nhìn nhận gradient không chỉ là danh sách các đạo hàm riêng mà là một đối tượng hình học: nó chỉ hướng tăng nhanh nhất, vuông góc với đường mức, và điều kiện $$ \nabla f = 0 $$ xác định các điểm dừng (có thể là cực trị hoặc điểm yên ngựa).

### Bước 3: Quy tắc dây chuyền và định lý hàm ẩn
Nắm vững hai công cụ trung tâm này: quy tắc dây chuyền cho phép tính đạo hàm dọc theo đường cong (hoặc quỹ đạo nghiệm ODE), còn định lý hàm ẩn cho phép tính đạo hàm của hàm xác định bởi phương trình ẩn mà không cần giải tường minh $$ y $$ theo $$ x $$.

### Các checkpoint
- Bạn có tính được gradient và giải thích ý nghĩa hình học của nó không?
- Bạn có vận dụng đúng quy tắc dây chuyền trong các trường hợp nhiều biến không?
- Bạn có xác định được khi nào định lý hàm ẩn áp dụng được không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tính gradient và phương trình tiếp tuyến đường mức
Cho $$ f(x,y) = x^2 + xy + y^2 $$. Ta có $$ \partial f/\partial x = 2x + y $$ và $$ \partial f/\partial y = x + 2y $$. Tại điểm $$ \left(1,2\right) $$, gradient là $$ \nabla f(1,2) = (4,5) $$, chỉ hướng tăng nhanh nhất của hàm số. Đường mức $$ f(x,y) = 7 $$ đi qua $$ \left(1,2\right) $$ có vector pháp tuyến là $$ \left(4,5\right) $$, nên tiếp tuyến của đường mức tại điểm này có phương trình $$ 4(x-1) + 5(y-2) = 0 $$.

### Ví dụ 2: Quy tắc dây chuyền
Cho $$ z = f(x,y) = x^2 + y^2 $$ với $$ x = t^3 $$ và $$ y = t^2 $$. Theo quy tắc dây chuyền,

$$
\frac{dz}{dt}
= \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}
= (2x)(3t^2) + (2y)(2t)
= 6t^5 + 4t^3.
$$

Kiểm tra bằng cách thay trực tiếp: $$ z = (t^3)^2 + (t^2)^2 = t^6 + t^4 $$, suy ra $$ dz/dt = 6t^5 + 4t^3 $$.

### Ví dụ 3: Định lý hàm ẩn
Từ phương trình $$ x^2 + y^2 = 1 $$, đặt $$ F(x,y) = x^2 + y^2 - 1 $$. Ta có $$ \partial F/\partial y = 2y $$. Tại điểm $$ \left(0,1\right) $$, $$ \partial F/\partial y = 2 \neq 0 $$, nên tồn tại hàm $$ y = f(x) $$ thỏa mãn $$ x^2 + f(x)^2 = 1 $$ trong lân cận của $$ x = 0 $$. Đạo hàm của hàm ẩn là

$$
f'(x) = -\frac{\partial F/\partial x}{\partial F/\partial y} = -\frac{2x}{2y} = -\frac{x}{y}.
$$

Tại $$ x = 0 $$, $$ y = 1 $$, ta thu được $$ f'(0) = 0 $$.

### Ví dụ 4: Ma trận Jacobi cho ánh xạ hai biến
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

Tại $$ \left(1,1\right) $$, ma trận Jacobi là $$\begin{pmatrix}2 & 1 \\ 1 & 1\end{pmatrix}$$, biểu diễn ánh xạ tuyến tính xấp xỉ $$ F $$ gần điểm đó.

### Ví dụ 5: Áp dụng trong ODE — phương trình tách biến và nghiệm ẩn
Xét phương trình $$ \frac{dy}{dx} = g(x)h(y) $$ với $$ h(y) \neq 0 $$. Khi tách biến thành $$ \frac{1}{h(y)}\,dy = g(x)\,dx $$ và lấy nguyên hàm hai vế, ta thu được nghiệm ở dạng ẩn $$ H(y) - G(x) = C $$, trong đó $$ H'(y) = 1/h(y) $$ và $$ G'(x) = g(x) $$. Đặt $$ F(x,y) = H(y) - G(x) - C $$; theo quy tắc dây chuyền và định lý hàm ẩn, điều kiện $$ \frac{\partial F}{\partial x} + \frac{\partial F}{\partial y}\frac{dy}{dx} = 0 $$ khôi phục đúng phương trình vi phân ban đầu.

## Câu hỏi khái niệm
1. Vì sao gradient luôn vuông góc với đường mức? Ý nghĩa hình học của tính chất này là gì?
2. Định lý hàm ẩn đảm bảo điều gì, và vì sao điều kiện $$ \partial F/\partial y \neq 0 $$ lại cần thiết?
3. Ma trận Jacobi tổng quát hóa đạo hàm một biến như thế nào, và nó đóng vai trò gì trong nghiên cứu hệ ODE?

## Bài toán ứng dụng
1. **Vật lý**: Cho trường nhiệt độ $$ T(x,y,z,t) $$. Vector $$ -\nabla T $$ tỉ lệ với dòng nhiệt. Hãy giải thích ý nghĩa vật lý của dấu trừ và từng thành phần của vector này.
2. **Kinh tế**: Xét hàm sản xuất Cobb–Douglas $$ Y(L,K) = AL^\alpha K^\beta $$. Hãy tính $$ \partial Y/\partial L $$, $$ \partial Y/\partial K $$ và giải thích ý nghĩa kinh tế của chúng.
3. **Sinh học**: Xét mô hình Lotka–Volterra $$ dP/dt = \alpha P - \beta PQ $$, $$ dQ/dt = \delta PQ - \gamma Q $$. Hãy viết hệ dưới dạng vector và tính ma trận Jacobi tại các điểm cân bằng.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Vẽ gradient"**: Cho sinh viên vẽ đường mức của các hàm hai biến đơn giản như $$ x^2+y^2 $$, $$ xy $$, $$ x^2-y^2 $$ rồi vẽ vector gradient tại một số điểm.
- **Thảo luận nhóm**: Giao cho mỗi nhóm một phương trình ẩn $$ F(x,y)=0 $$ để kiểm tra điều kiện áp dụng định lý hàm ẩn và tính $$ f'(x) $$, sau đó trình bày trước lớp.
- **Câu hỏi nhanh**: "Gradient của $$ f(x,y) = x^2 - y^2 $$ tại $$ \left(1,1\right) $$ hướng về đâu, và tại $$ \left(0,0\right) $$ đó là loại điểm gì?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Bắt đầu từ đạo hàm một biến quen thuộc trước khi mở rộng sang hàm hai biến.
- Sử dụng hình vẽ hoặc phần mềm vẽ đồ thị 3D và đường mức để tạo trực giác hình học.
- Luyện tập trên các hàm đơn giản như $$ x+y $$, $$ xy $$, $$ x^2+y^2 $$ trước khi sang các biểu thức phức tạp hơn.

### Thử thách cho sinh viên khá giỏi
- Tìm hiểu và trình bày định lý hàm ngược cùng các ứng dụng liên quan.
- So sánh phương pháp hạ gradient (gradient descent) trong tối ưu hóa với phương pháp Euler trong giải số ODE.
- Tìm hiểu ma trận Hessian và vai trò của nó trong phân loại cực trị cũng như phân tích ổn định của hệ ODE.

## Tóm tắt dễ nhớ
- **Gradient $$ \nabla f $$**: Chỉ hướng tăng nhanh nhất và vuông góc với đường mức.
- **Quy tắc dây chuyền**: $$ dz/dt = \nabla f \cdot r'(t) $$.
- **Định lý hàm ẩn**: $$ f'(x) = -F_x/F_y $$ khi $$ F_y \neq 0 $$.
- **Ma trận Jacobi**: Tổng quát hóa khái niệm đạo hàm cho ánh xạ nhiều biến.
- Trong hệ ODE nhiều chiều, gradient và ma trận Jacobi cung cấp xấp xỉ tuyến tính cục bộ cho trường vector.

## Video tham khảo

- Xem trước: [Visualizing the chain rule and product rule | Chapter 4, Essence of calculus](https://www.youtube.com/watch?v=YG15m2VwSjA) — 3Blue1Brown, tiếng Anh. Minh họa trực quan quy tắc dây chuyền, công cụ thiết yếu khi vế phải ODE phụ thuộc nhiều biến.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, tiếng Anh. Giới thiệu đạo hàm như tốc độ biến thiên tức thời, đúng với ý nghĩa của $$ y' $$ trong các mô hình vi phân.
- [Calculus Review: The Derivative (and the Power Law and Chain Rule)](https://www.youtube.com/watch?v=-NhgElcA3K8) — Steve Brunton, tiếng Anh. Ôn nhanh các quy tắc đạo hàm thường dùng khi kiểm tra nghiệm của ODE.

## Tài liệu tham khảo
- Marsden & Tromba — *Vector Calculus*: giáo trình chuẩn về giải tích đa biến.
- Apostol — *Calculus, Vol. 2*: trình bày chi tiết về đạo hàm riêng và ứng dụng.
- Hirsch, Smale & Devaney — *Differential Equations*: kết nối trực tiếp giải tích đa biến với hệ ODE.
