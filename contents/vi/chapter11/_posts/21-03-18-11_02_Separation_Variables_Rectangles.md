---
layout: post
title: "Tách Biến Trong Hình Chữ Nhật"
chapter: '11'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---

![21 03 18 11 02 Separation Variables Rectangles]({{ site.imgurl }}/chapter_img/chapter11/02_separation_variables_rectangles.svg)

Tưởng tượng một tấm kim loại hình chữ nhật có ba cạnh áp vào nước đá $0^\circ\text{C}$, còn cạnh trên cùng được nung theo một phân bố nhiệt độ cho trước $f(x)$. Làm sao biết chính xác nhiệt độ tại tâm tấm kim loại? Bí quyết tách biến $u(x, y) = X(x)Y(y)$ tách bài toán 2D thành hai ODE 1D với một nét đối lập tuyệt đẹp: **một chiều dao động bằng $\sin/\cos$**, còn **chiều vuông góc còn lại bắt buộc phải tăng–giảm đơn điệu bằng $\sinh/\cosh$**!

## Bản đồ kiến thức nền: Bốn trụ cột của Tách biến trên Miền Chữ nhật

1. **Cặp dấu hằng số tách biến trái ngược**:
   Từ $X''/X = -Y''/Y = -\lambda$, nếu biên trên trục $x$ là thuần nhất ($u(0, y) = u(a, y) = 0$), ta buộc phải chọn $\lambda = (n\pi/a)^2 > 0$ để $X_n(x) = \sin(n\pi x/a)$ có nghiệm không tầm thường.
2. **Hàm Hyperbolic $\sinh$ và $\cosh$ theo chiều còn lại**:
   Với $\lambda > 0$, phương trình $Y'' - \lambda Y = 0$ cho nghiệm $A\cosh(\frac{n\pi y}{a}) + B\sinh(\frac{n\pi y}{a})$. Dùng dạng tổ hợp $\sinh\left(\frac{n\pi y}{a}\right)$ hoặc $\sinh\left(\frac{n\pi (b-y)}{a}\right)$ giúp thỏa mãn biên $0$ tại $y = 0$ hoặc $y = b$ ngay lập tức!
3. **Nguyên lý Chồng chất cho Bốn Cạnh Không Thuần nhất**:
   Khi cả 4 cạnh hình chữ nhật đều có nhiệt độ khác $0$, ta tách bài toán thành tổng 4 bài toán con $u = u_1 + u_2 + u_3 + u_4$, mỗi bài toán con chỉ có **đúng một cạnh khác $0$** và ba cạnh còn lại bằng $0$.
4. **Suy giảm theo hàm mũ vào sâu bên trong**:
   Tỷ số $\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)} \approx e^{-n\pi(b-y)/a}$ cho thấy các gợn sóng tần số cao $n$ lớn trên biên tắt rất nhanh khi đi vào trong—lý giải trực quan vì sao nghiệm Laplace luôn trơn vô hạn $C^\infty$ bên trong miền!

## Mục tiêu

Bài học này hướng dẫn giải phương trình Laplace trên miền hình chữ nhật bằng phương pháp tách biến, đồng thời làm rõ vì sao nghiệm có dạng hàm sin theo một phương và hàm hyperbolic theo phương còn lại. Sau bài học, sinh viên cần nắm quy trình tách biến cho bài toán Dirichlet chuẩn, hiểu vai trò của các mode riêng theo phương ngang, và thấy cách dữ liệu trên một cạnh biên được khai triển thành các hệ số Fourier rồi lan truyền vào bên trong miền.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace, bài toán trị riêng một chiều và chuỗi Fourier sin. Đây là bài toán mẫu nền tảng để luyện cách giải bài toán biên elliptic trên miền có hình học đơn giản.

## Dẫn nhập

Trên hình chữ nhật, phương pháp tách biến phát huy hiệu quả rõ rệt đối với phương trình Laplace. Dù dữ liệu biên có thể phức tạp, hình học đều đặn của miền cho phép phân tích bài toán thành các mode riêng một chiều. Mỗi mode theo phương này sẽ phát triển sang phương còn lại theo một hàm hyperbolic tương ứng.

Về mặt sư phạm, bài học này đánh dấu lần đầu sinh viên thấy trực tiếp một nghiệm elliptic được xây dựng từ dữ liệu biên thay vì dữ liệu ban đầu, từ đó hình thành trực giác khác biệt so với phương trình nhiệt và phương trình sóng.


### Khung giải thích (nên đọc chậm): Tính tay nhiệt độ chính xác tại tâm hình vuông $[0, \pi] \times [0, \pi]$

Xét $\Delta u = 0$ trên hình vuông $(0, \pi) \times (0, \pi)$ với $u = 0$ trên ba cạnh $x = 0$, $x = \pi$, $y = 0$, và cạnh trên có nhiệt độ $u(x, \pi) = \sin(x)$:
1. **Chọn dạng nghiệm tách biến**: Vì $u(0,y)=u(\pi,y)=0$ và $u(x,0)=0$, chỉ còn duy nhất mode $n = 1$:
   $$u(x, y) = B_1 \sin(x) \sinh(y).$$
2. **Áp điều kiện cạnh trên $y = \pi$**:
   $$u(x, \pi) = B_1 \sin(x) \sinh(\pi) = \sin(x) \implies B_1 = \frac{1}{\sinh(\pi)}.$$
   Vậy nghiệm chính xác là $u(x, y) = \frac{\sinh(y)}{\sinh(\pi)}\sin(x)$.
3. **Tính số tại đúng tâm hình vuông $\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$**:
   Dùng $\sinh(\pi) = 2\sinh(\frac{\pi}{2})\cosh(\frac{\pi}{2})$ và $\sin(\frac{\pi}{2}) = 1$:
   $$u\left(\frac{\pi}{2}, \frac{\pi}{2}\right) = \frac{1}{2\cosh(\pi/2)} \approx \frac{1}{2 \times 2{,}509} \approx \mathbf{0{,}1993}.$$
   Kiểm tra nhanh: trung bình giá trị của $u$ trên cả 4 cạnh là $\frac{1}{4}\left(0 + 0 + 0 + \frac{1}{\pi}\int_0^\pi \sin x\,dx\right) = \frac{1}{2\pi} \approx 0{,}159$, cùng bậc độ lớn với $0{,}1993$!
## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một cạnh của hình chữ nhật được đặt ở mức điện thế hoặc nhiệt độ không đồng đều, ảnh hưởng của dữ liệu đó sẽ thấm dần vào bên trong miền. Các dao động biên có bước sóng ngắn theo phương ngang sẽ suy giảm nhanh hơn theo phương dọc so với các dao động có bước sóng dài. Phương pháp tách biến cho phép theo dõi từng thành phần dao động đó một cách độc lập.

### Cách nhìn hình ảnh

Các mode $$ \sin\left(\frac{n\pi x}{a}\right) $$ biểu diễn dao động theo phương ngang. Khi đi vào bên trong miền theo phương $$ y $$, chúng được nhân với các hàm $$ \sinh $$ hoặc $$ \cosh $$. Như vậy, mỗi mode Fourier trên biên không biến mất mà lan vào trong miền với tốc độ suy giảm khác nhau tùy theo bậc $$ n $$.

### Cách nhìn hình thức

Xét phương trình $$ u_{xx}+u_{yy}=0 $$ trên $$ \Omega=(0,a)\times(0,b) $$. Đặt $$ u(x,y)=X(x)Y(y) $$ và thế vào PDE, ta được:

$$ \frac{X''}{X}=-\frac{Y''}{Y}=-\lambda. $$

Từ đó thu được hai phương trình vi phân thường:

$$ X''+\lambda X=0,
\qquad
Y''-\lambda Y=0. $$

Nếu điều kiện biên trên các cạnh $$ x=0,\ x=a,\ y=0 $$ đều bằng 0, còn trên cạnh $$ y=b $$ là $$ f(x) $$, thì $$ X $$ phải thỏa mãn bài toán trị riêng Dirichlet một chiều, suy ra:

$$
X_n(x)=\sin\left(\frac{n\pi x}{a}\right),
\qquad
\lambda_n=\left(\frac{n\pi}{a}\right)^2.
$$

## Những ngộ nhận thường gặp

- "Giải Laplace trong hình chữ nhật chỉ là viết lại chuỗi Fourier một chiều dài hơn." Không đúng; đây là bài toán biên hai chiều thực thụ.
- "Hàm hyperbolic xuất hiện một cách ngẫu nhiên." Sai; chúng là nghiệm tự nhiên của phương trình $$ Y''-\lambda Y=0. $$
- "Dữ liệu biên chỉ dùng ở bước cuối để tìm hằng số." Không đúng; toàn bộ cấu trúc nghiệm được xây dựng từ dữ liệu biên.
- "Mode bậc cao luôn ảnh hưởng ngang bằng mode bậc thấp ở sâu trong miền." Không đúng; các mode bậc cao suy giảm nhanh hơn khi đi vào bên trong miền.

## Tiến trình học tập đề xuất

### Bước 1: Viết đầy đủ bài toán biên

Xác định rõ cạnh nào có giá trị bằng 0 và cạnh nào mang dữ liệu biên khác 0.

### Bước 2: Giả sử nghiệm dạng tích

Đặt $$ u(x,y)=X(x)Y(y) $$ để tách PDE thành hai phương trình vi phân thường.

### Bước 3: Giải bài toán trị riêng cho $$ X $$

Bước này dẫn đến họ các mode sin.

### Bước 4: Giải phương trình cho $$ Y $$

Chọn tổ hợp hàm hyperbolic phù hợp với điều kiện biên trên các cạnh nằm ngang.

### Bước 5: Khớp dữ liệu biên bằng chuỗi Fourier sin

Vận dụng khai triển chuỗi Fourier để xác định các hệ số nghiệm.

### Các checkpoint

- Sinh viên có giải thích được vì sao phần $$ X $$ dẫn đến bài toán trị riêng Dirichlet hay không.
- Sinh viên có hiểu vì sao các hàm $$ \sinh $$ và $$ \cosh $$ xuất hiện ở phần $$ Y $$ hay không.
- Sinh viên có thấy cách dữ liệu trên một cạnh biên được chuyển thành các hệ số Fourier hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba cạnh bằng 0, cạnh trên bằng $$ f(x) $$

Xét bài toán với điều kiện biên:

$$ u(0,y)=u(a,y)=u(x,0)=0,
\qquad
u(x,b)=f(x). $$

Nghiệm có dạng chuỗi:

$$
u(x,y)=\sum_{n=1}^{\infty}c_n
\sinh\left(\frac{n\pi y}{a}\right)
\sin\left(\frac{n\pi x}{a}\right).
$$

Các hệ số $$ c_n $$ được xác định bằng cách khớp điều kiện biên trên cạnh $$ y=b $$. Đây là bài toán mẫu tiêu chuẩn của bài học.

### Ví dụ 2: Dữ liệu biên là một mode duy nhất

Nếu $$ f(x)=\sin\left(\frac{\pi x}{a}\right) $$, thì chỉ có mode $$ n=1 $$ xuất hiện, và nghiệm rút gọn thành:

$$
u(x,y)=C\,\sinh\left(\frac{\pi y}{a}\right)\sin\left(\frac{\pi x}{a}\right).
$$

Ví dụ này cho thấy khi dữ liệu biên chỉ gồm một mode riêng, nghiệm bên trong miền cũng bảo toàn đúng mode đó.

### Ví dụ 3: Dữ liệu biên hằng

Nếu $$ f(x)=1 $$ trên $$ (0,a) $$, ta phải khai triển hàm hằng thành chuỗi Fourier sin trên $$ [0,a] $$. Điều này cho thấy ngay cả dữ liệu biên đơn giản cũng có thể cần đến phổ Fourier vô hạn.

### Ví dụ 4: Sự suy giảm khi đi vào bên trong miền

Các mode bậc cao mang nhân tử $$ \sinh\left(\frac{n\pi y}{a}\right) $$ đã được chuẩn hóa theo cạnh biên trên. Khi đi từ cạnh biên vào sâu bên trong miền, các mode bậc cao suy giảm nhanh hơn nhiều so với mode bậc thấp. Đây là minh họa trực quan cho hiệu ứng lọc tần số của bài toán elliptic.

## Câu hỏi khái niệm

1. Vì sao trên hình chữ nhật, một phương của phương trình Laplace cho nghiệm sin còn phương kia cho nghiệm hyperbolic?
2. Vì sao dữ liệu biên đóng vai trò như phổ tần số trong nghiệm tách biến?
3. Điều gì khiến các mode bậc cao ít ảnh hưởng hơn khi đi sâu vào bên trong miền?

## Bài toán ứng dụng

1. Một cạnh của tấm kim loại được giữ theo một phân bố nhiệt độ không đều, còn ba cạnh kia giữ ở nhiệt độ 0. Vì sao nhiệt độ bên trong có thể biểu diễn qua các mode sin trên cạnh đó?
2. Trong tĩnh điện, vì sao điện thế bên trong hình chữ nhật có thể xem như phần mở rộng điều hòa của dữ liệu trên biên?
3. Nếu dữ liệu biên dao động rất nhanh theo phương ngang, vì sao ảnh hưởng của nó vào sâu trong miền lại suy yếu nhanh hơn?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu chỉ biết dữ liệu trên một cạnh biên, thông tin đó lan truyền vào toàn miền bằng cách nào?"
- Cho sinh viên thử trường hợp dữ liệu biên là một mode sin duy nhất để thấy dạng nghiệm gọn nhẹ trước khi xét chuỗi tổng quát.
- Hỏi cả lớp: "Tại sao phương trình theo $$ y $$ lại không cho nghiệm sin mà cho $$ \sinh,\cosh $$?"
- Khuyến khích sinh viên liên hệ với chương chuỗi Fourier để nhận ra ý nghĩa của phép khai triển dữ liệu biên.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám sát bài toán mẫu chuẩn với ba cạnh bằng 0 và một cạnh mang dữ liệu khác 0 để nắm chắc quy trình tách biến trên hình chữ nhật.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi khảo sát các cấu hình điều kiện biên khác, hoặc phân tích vì sao bài toán có dữ liệu khác 0 trên nhiều cạnh có thể giải bằng nguyên lý chồng chất từ nhiều nghiệm tách biến.

## Tóm tắt dễ nhớ

Trên hình chữ nhật, phương trình Laplace được giải bằng cách tách biến thành các mode sin theo một phương và các hàm hyperbolic theo phương còn lại. Dữ liệu biên được khai triển thành chuỗi Fourier, và mỗi mode lan truyền vào bên trong miền theo quy luật suy giảm đặc trưng của phương trình elliptic.

## Video tham khảo

- xem trước: [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, tiếng Anh. Trình bày phương pháp tách biến cho phương trình Laplace trên hình chữ nhật.
- [Laplace’s Equation: Separation of Variables](https://www.youtube.com/watch?v=8jOqXM8OFh8) — Professor Dave Explains, tiếng Anh. Hướng dẫn chi tiết phép tách biến trên miền hình chữ nhật.
- [Separation of Variables - Laplace Eq Part 1](https://www.youtube.com/watch?v=-FNkz01Ksvw) — Dr. Underwood's Physics YouTube Page, tiếng Anh. Giải bài toán Laplace trên hình chữ nhật với một cạnh không thuần nhất.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ ổn định trên tấm hình chữ nhật
- Bài toán: Tìm phân bố nhiệt độ bên trong một tấm kim loại chữ nhật khi biết nhiệt độ trên biên.
- Mô hình: $$ u_{xx}+u_{yy}=0 $$ trên hình chữ nhật với điều kiện biên Dirichlet.
- Giả thiết và giới hạn: Trạng thái dừng, vật liệu đồng nhất, miền hình chữ nhật lý tưởng.
- Diễn giải: Tách biến cho phép khảo sát riêng tác động của từng mode biên.

#### Điện thế trong miền dẫn điện hình chữ nhật
- Bài toán: Xác định điện thế giữa các cạnh dẫn điện mang điện thế khác nhau trong một miền chữ nhật.
- Mô hình: Phương trình Laplace với điều kiện biên cho trước về điện thế.
- Giả thiết và giới hạn: Điện trường tĩnh, không có điện tích bên trong miền.
- Diễn giải: Hình học chữ nhật tạo ra các mode kết hợp giữa hàm sin và hàm hyperbolic.

### 2. Trực giác bổ sung và các kết nối

Kỹ thuật tách biến ở đây tương tự như trong chương phương trình sóng và phương trình nhiệt, nhưng không còn biến thời gian; điều còn lại là sự cân bằng giữa các hướng không gian. Một ngộ nhận thường gặp là cho rằng các mode riêng chỉ có ý nghĩa trong bài toán tiến hóa, trong khi thực tế chúng cũng là ngôn ngữ tự nhiên cho bài toán elliptic.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

a, b = 1.0, 1.0
x = np.linspace(0, a, 160)
y = np.linspace(0, b, 160)
X, Y = np.meshgrid(x, y)
U = np.sin(np.pi * X / a) * np.sinh(np.pi * Y / a) / np.sinh(np.pi * b / a)

plt.contourf(X, Y, U, levels=20, cmap="inferno")
plt.colorbar(label="u")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Nghiem Laplace tren hinh chu nhat")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Laplace equation rectangle separation of variables
- search: steady state heat rectangle contour plot
- search: capacitor rectangle potential field

### 5. Bài toán mẫu có bối cảnh thực

Nếu trên hình chữ nhật $$ 0<x<a $$, $$ 0<y<b $$ ta đặt điều kiện biên
$$
u(0,y)=u(a,y)=u(x,0)=0, \qquad u(x,b)=\sin\!\left(\frac{\pi x}{a}\right),
$$
thì nghiệm là
$$
u(x,y)=\sin\!\left(\frac{\pi x}{a}\right)\frac{\sinh(\pi y/a)}{\sinh(\pi b/a)}.
$$
Kết quả này cho thấy ảnh hưởng của cạnh biên trên lan vào bên trong miền theo đúng một mode duy nhất.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập và giải bài toán trên hình chữ nhật bằng phương pháp tách biến.

**Bậc sau đại học.** Phân tích sự hội tụ của chuỗi nghiệm, tính đầy đủ của hệ hàm riêng và tính ổn định theo dữ liệu biên.
