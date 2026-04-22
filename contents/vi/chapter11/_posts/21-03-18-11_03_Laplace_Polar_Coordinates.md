---
layout: post
title: "Phương Trình Laplace Trong Tọa Độ Cực"
chapter: '11'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---
![21 03 18 11 03 Laplace Polar Coordinates]({{ site.imgurl }}/chapter_img/chapter11/03_laplace_polar_coordinates.svg)

## Mục tiêu

Bài học này giúp sinh viên giải phương trình Laplace trên các miền tròn bằng tọa độ cực, đồng thời thấy các mode Fourier theo góc và các lũy thừa theo bán kính xuất hiện như thế nào. Sau bài học, sinh viên cần biết dạng Laplace trong tọa độ cực, tách biến thành phần góc và bán kính, hiểu vì sao điều kiện hữu hạn tại tâm loại các nghiệm kỳ dị, và biết xây dựng nghiệm trong đĩa từ dữ liệu biên theo góc.

## Kiến thức nền

Sinh viên nên nắm Laplace trong tọa độ Descartes, tách biến, chuỗi Fourier theo góc và phương trình Euler. Bài này là nơi hình học tròn làm cho tọa độ cực trở thành lựa chọn tự nhiên.

## Dẫn nhập

Nếu cố giải bài toán trên đĩa tròn bằng tọa độ Descartes, ta sẽ sớm cảm thấy hình học và công thức "lệch pha" với nhau. Tọa độ cực khớp với miền tròn một cách tự nhiên hơn rất nhiều. Khi dùng hệ tọa độ phù hợp, cấu trúc của nghiệm tự mở ra: Fourier theo góc, lũy thừa theo bán kính.

Đây cũng là một bài rất đẹp về mặt khái niệm. Nó cho sinh viên thấy rằng chọn hệ tọa độ đúng không chỉ giúp tính toán ngắn hơn, mà còn làm lộ rõ đối xứng của bài toán. Hình học tròn buộc nghiệm phải nói bằng ngôn ngữ của góc và bán kính.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu dữ liệu biên trên vòng tròn thay đổi theo góc như một sóng quanh tâm, thì ảnh hưởng của dữ liệu đó vào bên trong sẽ vừa phụ thuộc vào mode góc vừa phụ thuộc khoảng cách đến tâm. Càng gần tâm, những mode bậc cao thường yếu đi nhanh hơn. Đó là trực giác cốt lõi của lời giải trong đĩa.

### Cách nhìn hình ảnh

Các mode góc $$ \cos(n\theta),\ \sin(n\theta) $$ cho các hoa văn xoay quanh tâm. Phần bán kính $$ r^n $$ quyết định cường độ của mode khi đi từ biên vào tâm. Nếu mode góc có bậc cao, hoa văn sẽ có nhiều múi hơn và thường suy yếu nhanh hơn gần tâm.

### Cách nhìn hình thức

Trong tọa độ cực $$ (r,\theta) $$, phương trình Laplace là

$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$

Đặt $$ u(r,\theta)=R(r)\Theta(\theta) $$. Thế vào PDE:

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}=\lambda.
$$

Do tính tuần hoàn theo góc, ta được

$$ \Theta''+n^2\Theta=0,
\qquad n=0,1,2,\ldots $$

và phần bán kính thỏa

$$ r^2R''+rR'-n^2R=0. $$

## Những ngộ nhận thường gặp

- "Tọa độ cực chỉ là đổi ký hiệu, không đổi bản chất." Không đúng; nó làm cấu trúc đối xứng của bài toán lộ ra rõ ràng.
- "Nghiệm

$$ r^{-n} $$

và $$ \ln r $$ luôn chấp nhận được." Sai; trong đĩa có tâm, điều kiện hữu hạn tại $$ r=0 $$ thường loại chúng.
- "Các mode góc chỉ là Fourier quen thuộc nên phần bán kính chắc cũng đơn giản giống vậy." Không hẳn; phần bán kính phản ánh sâu hình học của miền.
- "Mode cao theo góc ảnh hưởng đều khắp miền." Không đúng; chúng thường yếu nhanh hơn khi vào gần tâm.

## Tiến trình học tập đề xuất

### Bước 1: Viết Laplace trong tọa độ cực

Sinh viên cần chấp nhận đây là hệ tọa độ đúng cho đĩa.

### Bước 2: Tách phần góc

Đây là chỗ Fourier quay lại tự nhiên nhất.

### Bước 3: Giải phần bán kính

Phương trình Euler này rất đáng được liên hệ với chương chuỗi đặc biệt.

### Bước 4: Áp điều kiện hữu hạn tại tâm

Đây là bước bản chất, không chỉ là chi tiết kỹ thuật.

### Các checkpoint

- Sinh viên có giải thích được vì sao phải dùng mode góc tuần hoàn hay không.
- Sinh viên có hiểu vì sao nghiệm kỳ dị bị loại trong đĩa có tâm hay không.
- Sinh viên có thấy dữ liệu trên biên vòng tròn được chuyển thành các hệ số Fourier theo góc hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dạng tổng quát trong đĩa

Nếu miền là đĩa bán kính $$ R $$ và nghiệm phải hữu hạn tại tâm, thì lời giải có dạng

$$
u(r,\theta)=a_0+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^n
\bigl(a_n\cos(n\theta)+b_n\sin(n\theta)\bigr),
$$

trong đó $$ a_n,\ b_n $$ là các hệ số Fourier của dữ liệu biên $$ f(\theta)=u(R,\theta) $$. Đây là công thức quan trọng nhất của bài.

### Ví dụ 2: Một mode duy nhất trên biên

Nếu $$ f(\theta)=V_0\cos\theta $$, thì chỉ mode $$ n=1 $$ xuất hiện, và nghiệm là

$$ u(r,\theta)=V_0\frac{r}{R}\cos\theta. $$

Ví dụ này nên được dùng thật kỹ vì nó cho thấy dữ liệu biên là một mode thì bên trong cũng là cùng mode đó.

### Ví dụ 3: Dữ liệu hằng

Nếu $$ f(\theta)=C $$, thì nghiệm bên trong chỉ là $$ u(r,\theta)=C $$. Ví dụ này giúp sinh viên thấy mode $$ n=0 $$ là thành phần trung bình của dữ liệu biên.

### Ví dụ 4: Vành khăn

Nếu miền là vành khăn thay vì đĩa, ta không còn cần loại nghiệm $$ r^{-n} $$ hay $$ \ln r $$. Ví dụ này rất tốt để nhấn mạnh rằng "hữu hạn tại tâm" là điều kiện hình học chứ không phải công thức mặc định.

## Câu hỏi khái niệm

1. Vì sao miền tròn khiến tọa độ cực trở thành lựa chọn tự nhiên?
2. Điều gì trong hình học của đĩa làm các nghiệm kỳ dị bị loại tại tâm?
3. Vì sao dữ liệu biên theo góc được xử lý bằng Fourier nhưng phần bán kính lại là lũy thừa?

## Bài toán ứng dụng

1. Trong tĩnh điện, nếu biên của đĩa được áp một điện thế thay đổi theo góc, vì sao điện thế bên trong có thể được xây dựng từ các mode Fourier góc?
2. Trong dòng chảy thế quanh tâm, vì sao đối xứng tròn làm cho lời giải tự nhiên phụ thuộc vào $$ r $$ và $$ \theta $$ thay vì

$$ x,y? $$
3. Trong một đĩa, vì sao các mode góc cao thường ít ảnh hưởng gần tâm hơn?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu miền là hình tròn, còn dùng

$$ x,y $$

thì có đang nói cùng ngôn ngữ với bài toán không?"
- Cho sinh viên nhìn vài mode

$$ \cos(n\theta),\ \sin(n\theta) $$

và mô tả hoa văn góc của chúng.
- Hỏi cả lớp: "Điều gì xảy ra với nghiệm

$$ r^{-n} $$

khi

$$ r\to 0? $$
"
- Khuyến khích sinh viên so sánh đĩa với vành khăn để thấy điều kiện hình học thay đổi nghiệm thế nào.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ trọng tâm ở công thức cho đĩa tròn và một vài mode đầu tiên. Khi trực giác góc-bán kính đã chắc, phần tổng quát sẽ ít đáng sợ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi suy ra công thức Poisson cho đĩa hoặc phân tích vai trò của mỗi mode như một bộ lọc tần số góc khi đi vào nội thất.

## Tóm tắt dễ nhớ

Trong miền tròn, Laplace nên được giải bằng tọa độ cực. Nghiệm được tách thành Fourier theo góc và lũy thừa theo bán kính. Dữ liệu biên trên vòng tròn quyết định các mode góc, còn điều kiện hữu hạn tại tâm loại các nghiệm kỳ dị.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - khuôn khổ chuẩn cho hàm điều hòa, phương trình Poisson, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - trình bày trực quan về tĩnh điện, dòng chảy thế, và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ quanh ống trụ
- Bài toán: Tính trường nhiệt độ ổn định quanh một ống tròn dài.
- Mô hình:
$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$
- Giả thiết và giới hạn: Đối xứng theo trục, trạng thái dừng, hình học tròn lý tưởng.
- Diễn giải: Tọa độ cực phù hợp với hình học và làm mô hình dễ hiểu hơn.

#### Điện thế quanh điện cực tròn
- Bài toán: Điện thế trong đĩa hoặc vành tròn thường thuận tiện nhất khi viết ở tọa độ cực.
- Mô hình: Phương trình Laplace trong tọa độ cực.
- Giả thiết và giới hạn: Không có điện tích trong miền.
- Diễn giải: Các mode góc $$ \cos(n\theta) $$ và $$ \sin(n\theta) $$ thể hiện đối xứng của dữ liệu biên.

### 2. Trực giác bổ sung và các kết nối

Đổi hệ tọa độ không thay đổi vật lý, nhưng có thể làm lộ rõ cấu trúc đối xứng. Một bẫy phổ biến là giữ tọa độ Descartes quá lâu và bỏ lỡ mô hình đơn giản hơn trong hình học tròn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 1, 160)
theta = np.linspace(0, 2 * np.pi, 240)
R, Theta = np.meshgrid(r, theta)
U = R * np.cos(Theta)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

plt.contourf(X, Y, U, levels=20, cmap="coolwarm")
plt.colorbar(label="u")
plt.axis("equal")
plt.title("Nghiem dieu hoa trong dia: u(r,theta)=r cos(theta)")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Laplace equation polar coordinates disk solution
- search: harmonic function disk boundary data animation
- search: electrostatic potential circular domain

### 5. Bài toán mẫu có bối cảnh thực

Trong đĩa đơn vị, nếu dữ liệu biên là
$$ u(1,\theta)=\cos\theta, $$
thì nghiệm điều hòa là
$$ u(r,\theta)=r\cos\theta. $$
Đây là ví dụ kinh điển cho thấy mode góc bậc một trên biên kéo vào trong miền bằng nhân tử $$ r $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận biết khi nào nên chuyển sang tọa độ cực.

**Bậc sau đại học.** Liên hệ với Poisson kernel trên đĩa và biểu diễn điều hòa theo chuỗi Fourier.
