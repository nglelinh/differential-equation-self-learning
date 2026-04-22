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

## Mục tiêu

Bài học này giúp sinh viên giải phương trình Laplace trên hình chữ nhật bằng phương pháp tách biến, đồng thời hiểu vì sao nghiệm có dạng sine theo một chiều và hyperbolic theo chiều còn lại. Sau bài học, sinh viên cần biết quy trình tách biến cho bài toán Dirichlet chuẩn, hiểu vai trò của các mode riêng theo phương ngang, và thấy cách dữ liệu biên trên một cạnh được "phổ hóa" thành các hệ số Fourier rồi lan vào nội thất.

## Kiến thức nền

Sinh viên nên nắm phương trình Laplace, bài toán trị riêng một chiều và chuỗi Fourier sine. Đây là bài mẫu quan trọng nhất để học cách giải bài toán biên elliptic trên miền đơn giản.

## Dẫn nhập

Trên hình chữ nhật, phương trình Laplace là nơi phương pháp tách biến bộc lộ sức mạnh rất rõ. Dữ liệu biên có thể phức tạp, nhưng hình học miền lại rất đều, nên ta có thể bóc bài toán thành các mode riêng một chiều. Mỗi mode theo một phương sẽ lan sang phương còn lại theo một hàm hyperbolic phù hợp.

Về mặt sư phạm, bài này đặc biệt quan trọng vì nó là lần đầu sinh viên thấy rõ một nghiệm elliptic được xây dựng từ dữ liệu biên chứ không phải dữ liệu đầu. Điều này tạo nên một trực giác rất khác so với nhiệt và sóng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một cạnh của hình chữ nhật được áp đặt điện thế hoặc nhiệt độ không đều, ảnh hưởng của dữ liệu đó sẽ thấm dần vào bên trong miền. Các gợn biên "ngắn" theo phương ngang sẽ suy giảm theo phương dọc khác với các gợn "dài". Tách biến cho phép ta theo dõi từng gợn riêng lẻ.

### Cách nhìn hình ảnh

Các mode

$$ \sin\left(\frac{n\pi x}{a}\right) $$

diễn tả dao động theo chiều ngang. Khi đi vào trong miền theo chiều $$ y $$, chúng được nhân với các hàm $$ \sinh $$ hoặc $$ \cosh $$. Hình ảnh này rất hữu ích: một mode Fourier trên biên không biến mất, mà được "nâng vào trong miền" với tốc độ khác nhau theo bậc mode.

### Cách nhìn hình thức

Xét $$ u_{xx}+u_{yy}=0 $$ trên $$ \Omega=(0,a)\times(0,b) $$. Đặt $$ u(x,y)=X(x)Y(y) $$. Thế vào PDE:

$$ \frac{X''}{X}=-\frac{Y''}{Y}=-\lambda. $$

Ta nhận được

$$ X''+\lambda X=0,
\qquad
Y''-\lambda Y=0. $$

Nếu điều kiện biên trên $$ x=0,\ x=a,\ y=0 $$ là 0, còn trên $$ y=b $$ là $$ f(x) $$, thì phần $$ X $$ phải thỏa bài toán Dirichlet một chiều, nên

$$
X_n(x)=\sin\left(\frac{n\pi x}{a}\right),
\qquad
\lambda_n=\left(\frac{n\pi}{a}\right)^2.
$$

## Những ngộ nhận thường gặp

- "Laplace trong hình chữ nhật chỉ là Fourier một chiều viết dài hơn." Không đúng; đây là một bài toán biên hai chiều thật sự.
- "Hàm hyperbolic xuất hiện ngẫu nhiên." Sai. Chúng là nghiệm tự nhiên của phương trình

$$ Y''-\lambda Y=0. $$
- "Dữ liệu biên chỉ đóng vai trò cuối cùng để tìm hằng số." Không đúng; toàn bộ nghiệm được xây dựng từ dữ liệu biên.
- "Mode cao luôn quan trọng như mode thấp ở sâu trong miền." Không đúng; chúng thường suy giảm nhanh hơn khi đi vào trong.

## Tiến trình học tập đề xuất

### Bước 1: Viết bài toán biên đầy đủ

Sinh viên phải luôn rõ cạnh nào bằng 0, cạnh nào mang dữ liệu.

### Bước 2: Đặt dạng tích

Đây là bước mở khóa bài toán.

### Bước 3: Giải bài toán riêng cho

$$ X $$

Phần này dẫn đến sine modes.

### Bước 4: Giải phần

$$ Y $$

và chọn tổ hợp hyperbolic phù hợp.

### Bước 5: Ghép dữ liệu biên bằng Fourier sine

Đây là nơi chương Fourier quay lại một cách rất tự nhiên.

### Các checkpoint

- Sinh viên có hiểu vì sao phần

$$ X $$

là bài toán trị riêng Dirichlet hay không.
- Sinh viên có biết vì sao

$$ \sinh $$

và $$ \cosh $$ xuất hiện hay không.
- Sinh viên có thấy dữ liệu trên một cạnh được biến thành các hệ số Fourier như thế nào hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba cạnh bằng 0, cạnh trên bằng

$$ f(x) $$

Xét

$$ u(0,y)=u(a,y)=u(x,0)=0,
\qquad
u(x,b)=f(x). $$

Nghiệm có dạng

$$
u(x,y)=\sum_{n=1}^{\infty}c_n
\sinh\left(\frac{n\pi y}{a}\right)
\sin\left(\frac{n\pi x}{a}\right).
$$

Hệ số $$ c_n $$ được xác định bằng cách khớp điều kiện trên $$ y=b $$. Đây là ví dụ chuẩn nhất của bài.

### Ví dụ 2: Dữ liệu biên là một mode duy nhất

Nếu

$$ f(x)=\sin\left(\frac{\pi x}{a}\right), $$

thì chỉ mode $$ n=1 $$ xuất hiện. Nghiệm đơn giản thành

$$
u(x,y)=C\,\sinh\left(\frac{\pi y}{a}\right)\sin\left(\frac{\pi x}{a}\right).
$$

Ví dụ này rất mạnh vì nó cho thấy dữ liệu biên là một mode thì nghiệm bên trong giữ nguyên mode đó.

### Ví dụ 3: Dữ liệu biên hằng

Nếu $$ f(x)=1 $$ trên $$ (0,a) $$, ta phải khai triển hằng số thành sine series trên $$ [0,a] $$. Ví dụ này giúp sinh viên thấy ngay cả dữ liệu biên rất đơn giản cũng có thể yêu cầu phổ Fourier vô hạn.

### Ví dụ 4: Suy giảm vào nội thất

Các mode bậc cao mang hệ số

$$ \sinh\left(\frac{n\pi y}{a}\right) $$

chuẩn hóa theo biên trên. Khi nhìn từ biên vào sâu trong miền, các mode cao thường suy giảm nhanh hơn. Đây là ví dụ trực giác tốt về "lọc hình học" của bài toán elliptic.

## Câu hỏi khái niệm

1. Vì sao trên hình chữ nhật, một phương của Laplace dẫn đến sine còn phương kia dẫn đến hyperbolic?
2. Vì sao dữ liệu biên đóng vai trò tương tự dữ liệu phổ trong nghiệm tách biến?
3. Điều gì khiến mode cao ít ảnh hưởng hơn khi đi sâu vào trong miền?

## Bài toán ứng dụng

1. Một cạnh của tấm kim loại được giữ ở hồ sơ nhiệt độ không đều, ba cạnh còn lại giữ ở 0. Vì sao nhiệt độ bên trong có thể được xây dựng từ các sine modes trên cạnh đó?
2. Trong tĩnh điện, vì sao điện thế bên trong hình chữ nhật có thể được xem như "phần mở rộng điều hòa" của dữ liệu trên biên?
3. Nếu dữ liệu biên dao động rất gắt theo phương ngang, vì sao ảnh hưởng của nó vào sâu trong miền thường yếu nhanh hơn?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu chỉ biết dữ liệu trên một cạnh, làm sao thông tin đó lan vào cả miền?"
- Cho sinh viên thử một dữ liệu biên là một mode sine duy nhất để thấy nghiệm rất gọn.
- Hỏi cả lớp: "Tại sao phần theo

$$ y $$

lại không cho sine mà lại cho

$$ \sinh,\cosh? $$
"
- Khuyến khích sinh viên liên hệ với chương Fourier: dữ liệu biên ở đây đang được khai triển theo nghĩa nào?

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ một mẫu bài toán chuẩn với ba cạnh bằng 0 và một cạnh cho dữ liệu. Đây là khuôn mẫu tốt nhất để học chắc quy trình tách biến trong hình chữ nhật.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi khảo sát các cấu hình dữ liệu biên khác, hoặc thảo luận vì sao bài toán có dữ liệu trên nhiều cạnh dẫn đến việc ghép chồng nhiều nghiệm tách biến.

## Tóm tắt dễ nhớ

Trên hình chữ nhật, phương trình Laplace được giải bằng tách biến thành sine modes theo một chiều và hàm hyperbolic theo chiều kia. Dữ liệu biên được biến thành phổ Fourier, rồi mỗi mode được kéo vào trong miền theo quy luật elliptic tương ứng.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - khuôn khổ chuẩn cho hàm điều hòa, phương trình Poisson, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - trình bày trực quan về tĩnh điện, dòng chảy thế, và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ ổn định trên tấm hình chữ nhật
- Bài toán: Một tấm kim loại chữ nhật có nhiệt độ biên cho trước và ta cần phân bố nhiệt trong miền.
- Mô hình:
$$ u_{xx}+u_{yy}=0 $$
trên hình chữ nhật, với điều kiện Dirichlet.
- Giả thiết và giới hạn: Trạng thái dừng, vật liệu đồng nhất, hình chữ nhật lý tưởng.
- Diễn giải: Tách biến cho phép tách ảnh hưởng của từng mode biên.

#### Điện thế trong tụ bản phẳng hình chữ nhật
- Bài toán: Điện thế giữa các cạnh dẫn điện khác nhau trong một miền chữ nhật.
- Mô hình: Cùng phương trình Laplace với dữ liệu biên điện thế.
- Giả thiết và giới hạn: Điện trường tĩnh, không có điện tích trong miền.
- Diễn giải: Hình học chữ nhật làm xuất hiện các mode hyperbolic-sinus và sinus.

### 2. Trực giác bổ sung và các kết nối

Tách biến ở đây giống chương sóng và nhiệt, nhưng phần thời gian biến mất. Điều còn lại là cân bằng giữa các hướng không gian. Một ngộ nhận thường gặp là nghĩ các mode chỉ có ý nghĩa cho bài toán tiến hóa; thật ra chúng cũng là ngôn ngữ tự nhiên của bài toán elliptic.

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

Nếu trên hình chữ nhật $$ 0<x<a $$, $$ 0<y<b $$ ta đặt
$$
u(0,y)=u(a,y)=u(x,0)=0, \qquad u(x,b)=\sin\!\left(\frac{\pi x}{a}\right),
$$
thì nghiệm là
$$
u(x,y)=\sin\!\left(\frac{\pi x}{a}\right)\frac{\sinh(\pi y/a)}{\sinh(\pi b/a)}.
$$
Nghiệm cho thấy ảnh hưởng của biên trên lan vào miền theo một mode duy nhất.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập và giải bài toán chữ nhật bằng tách biến.

**Bậc sau đại học.** Phân tích hội tụ chuỗi, tính đầy đủ của eigenfunction và tính ổn định theo dữ liệu biên.
