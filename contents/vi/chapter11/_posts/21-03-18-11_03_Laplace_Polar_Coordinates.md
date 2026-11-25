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

Trên một đĩa tròn hay hình vành khăn, hệ tọa độ Descartes $(x, y)$ trở nên vụng về vì biên cong không khớp với lưới vuông góc. Chuyển sang tọa độ cực $(r, \theta)$ làm hình học trở nên gọn gàng ngay lập tức, nhưng đổi lại xuất hiện một "người khách quen" đầy thú vị từ Chương 6: phương trình hướng kính biến thành **phương trình Cauchy–Euler** $r^2 R'' + r R' - n^2 R = 0$, kéo theo công thức tích phân Poisson tuyệt đẹp cho giá trị tại mọi điểm bên trong hình tròn!

## Kiến thức cần nhớ: Bốn trụ cột của Phương trình Laplace trong Tọa độ Cực

1. **Biến đổi Toán tử Laplace sang $(r, \theta)$**:
   $$\Delta u = u_{rr} + \frac{1}{r} u_r + \frac{1}{r^2} u_{\theta\theta} = 0.$$
   Tính tuần hoàn góc $u(r, \theta + 2\pi) = u(r, \theta)$ tự động đóng vai trò "điều kiện biên" theo $\theta$, ép hằng số tách biến phải là số nguyên bình phương $\lambda = n^2$ ($n = 0, 1, 2, \dots$).
2. **Nghiệm Cauchy–Euler và Chọn nhánh theo Hình học Miền**:
   Với $n = 0$: $R_0(r) = A_0 + B_0 \ln r$; với $n \ge 1$: $R_n(r) = A_n r^n + B_n r^{-n}$.
   - **Trong đĩa tròn $r < R$**: đòi hỏi bị chặn tại $r = 0$ nên loại bỏ $\ln r$ và $r^{-n}$.
   - **Ngoài đĩa tròn $r > R$**: đòi hỏi bị chặn khi $r \to \infty$ nên loại bỏ $\ln r$ và $r^n$.
   - **Hình vành khăn $R_1 < r < R_2$**: giữ nguyên cả hai nhánh!
3. **Chuỗi Fourier trên Đường tròn Biên**:
   Nghiệm tổng quát trong đĩa bán kính $R$ có dạng $u(r, \theta) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(\frac{r}{R}\right)^n (a_n \cos n\theta + b_n \sin n\theta)$, trong đó $a_n, b_n$ chính là hệ số Fourier của dữ liệu biên $f(\theta)$.
4. **Công thức Tích phân Poisson (Poisson Kernel)**:
   Cộng đóng chuỗi hình học $\sum (r/R)^n \cos(n(\theta - \phi))$ thu được biểu thức tích phân trực tiếp $u(r, \theta) = \frac{1}{2\pi}\int_0^{2\pi} \frac{R^2 - r^2}{R^2 - 2Rr\cos(\theta-\phi) + r^2} f(\phi)\,d\phi$—chứng minh tức thì Tính chất Trung bình tại tâm $r = 0$!

## Mục tiêu

Bài học này hướng dẫn giải phương trình Laplace trên các miền tròn bằng tọa độ cực, đồng thời làm rõ cách các mode Fourier theo góc và các lũy thừa theo bán kính xuất hiện. Sau bài học, sinh viên cần nắm dạng phương trình Laplace trong tọa độ cực, biết tách biến thành phần góc và phần bán kính, hiểu vì sao điều kiện hữu hạn tại tâm giúp loại bỏ các nghiệm kỳ dị, và biết xây dựng nghiệm trong đĩa tròn từ dữ liệu biên theo góc.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace trong tọa độ Descartes, phương pháp tách biến, chuỗi Fourier theo góc và phương trình Euler. Khi miền có dạng hình tròn, tọa độ cực trở thành lựa chọn phù hợp nhất.

## Dẫn nhập

Nếu giải bài toán trên đĩa tròn bằng tọa độ Descartes, công thức và hình học của miền sẽ không khớp nhau, khiến việc áp đặt điều kiện biên trở nên cồng kềnh. Ngược lại, tọa độ cực khớp tự nhiên với miền tròn và làm lộ rõ cấu trúc nghiệm: chuỗi Fourier theo góc kết hợp với lũy thừa theo bán kính.

Về mặt khái niệm, bài học này cho thấy việc chọn đúng hệ tọa độ không chỉ rút gọn phép tính mà còn làm nổi bật tính đối xứng của bài toán. Hình học tròn khiến nghiệm biểu diễn tự nhiên nhất theo góc và bán kính.


### Giải thích: Giải nhanh bằng tay bài toán Dirichlet trên đĩa tròn bán kính $R = 2$

Tìm nghiệm điều hòa $\Delta u = 0$ trong đĩa $r < 2$ biết nhiệt độ trên vành tròn $r = 2$ là:
$$u(2, \theta) = 10 + 4\cos\theta - 8\sin(2\theta).$$
1. **Khớp từng mode điều hòa (không cần tính tích phân!)**:
   Vì dữ liệu biên đã là một đa thức lượng giác hữu hạn, ta chỉ cần nhân mỗi mode bậc $n$ với thừa số suy giảm $\left(\frac{r}{R}\right)^n = \left(\frac{r}{2}\right)^n$:
   $$u(r, \theta) = 10 + 4\left(\frac{r}{2}\right)\cos\theta - 8\left(\frac{r}{2}\right)^2\sin(2\theta) = \mathbf{10 + 2r\cos\theta - 2r^2\sin(2\theta)}.$$
2. **Kiểm tra tại tâm $r = 0$**: $u(0, \theta) = \mathbf{10}$—đúng bằng giá trị trung bình của $u(2, \theta)$ trên cả đường tròn!
3. **Tính tại điểm $(r = 1, \theta = \pi/4)$**:
   $$u\left(1, \frac{\pi}{4}\right) = 10 + 2(1)\frac{\sqrt{2}}{2} - 2(1)^2(1) = 8 + \sqrt{2} \approx \mathbf{9{,}414}.$$
## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu dữ liệu trên đường tròn biên biến thiên theo góc như một dạng sóng quanh tâm, thì ảnh hưởng của nó vào bên trong miền sẽ phụ thuộc đồng thời vào bậc mode góc và khoảng cách tới tâm. Càng gần tâm, các mode bậc cao suy yếu càng nhanh — đó là trực giác cốt lõi của nghiệm điều hòa trong đĩa tròn.

### Cách nhìn hình ảnh

Các mode góc $$ \cos(n\theta),\ \sin(n\theta) $$ tạo ra các dạng phân bố tuần hoàn quanh tâm, còn nhân tử bán kính $$ r^n $$ quyết định biên độ của mode khi đi từ biên vào tâm. Mode có bậc $$ n $$ càng cao thì càng có nhiều thùy dao động theo góc và suy giảm càng nhanh gần tâm.

### Cách nhìn hình thức

Trong tọa độ cực $$ (r,\theta) $$, phương trình Laplace có dạng:

$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$

Đặt $$ u(r,\theta)=R(r)\Theta(\theta) $$ và thế vào PDE, ta thu được:

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}=\lambda.
$$

Do tính tuần hoàn $$ 2\pi $$ theo góc, ta có phương trình phần góc:

$$ \Theta''+n^2\Theta=0,
\qquad n=0,1,2,\ldots $$

và phương trình Euler cho phần bán kính:

$$ r^2R''+rR'-n^2R=0. $$

## Những ngộ nhận thường gặp

- "Chuyển sang tọa độ cực chỉ là đổi ký hiệu chứ không thay đổi cách hiểu bài toán." Không đúng; hệ tọa độ cực giúp cấu trúc đối xứng của bài toán hiện ra trực tiếp.
- "Các nghiệm $$ r^{-n} $$ và $$ \ln r $$ luôn dùng được." Sai; trong đĩa tròn chứa tâm, điều kiện hữu hạn tại $$ r=0 $$ loại bỏ các nghiệm kỳ dị này.
- "Phần góc là chuỗi Fourier quen thuộc nên phần bán kính cũng có dạng lượng giác tương tự." Không đúng; phần bán kính là nghiệm của phương trình Euler và phản ánh trực tiếp hình học hướng tâm của miền.
- "Mode góc bậc cao có ảnh hưởng đồng đều khắp miền." Không đúng; chúng suy giảm nhanh hơn khi tiến về gần tâm.

## Tiến trình học tập đề xuất

### Bước 1: Viết phương trình Laplace trong tọa độ cực

Nhận diện đây là hệ tọa độ phù hợp nhất cho bài toán trên đĩa tròn.

### Bước 2: Tách phần góc

Áp dụng tính tuần hoàn theo góc để thu được chuỗi Fourier.

### Bước 3: Giải phần bán kính

Giải phương trình Euler tương ứng với từng giá trị $$ n $$.

### Bước 4: Áp đặt điều kiện hữu hạn tại tâm

Loại bỏ các nghiệm kỳ dị tại $$ r=0 $$ — đây là bước mang ý nghĩa hình học bản chất chứ không chỉ là thao tác kỹ thuật.

### Các checkpoint

- Sinh viên có giải thích được vì sao phải chọn các mode góc tuần hoàn hay không.
- Sinh viên có hiểu vì sao các nghiệm kỳ dị bị loại trong đĩa tròn chứa tâm hay không.
- Sinh viên có thấy cách dữ liệu trên đường tròn biên được chuyển thành các hệ số Fourier theo góc hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Nghiệm tổng quát trong đĩa tròn

Nếu miền là đĩa tròn bán kính $$ R $$ và nghiệm hữu hạn tại tâm, lời giải có dạng:

$$
u(r,\theta)=a_0+\sum_{n=1}^{\infty}\left(\frac{r}{R}\right)^n
\bigl(a_n\cos(n\theta)+b_n\sin(n\theta)\bigr),
$$

trong đó $$ a_n,\ b_n $$ là các hệ số Fourier của dữ liệu biên $$ f(\theta)=u(R,\theta) $$. Đây là công thức trọng tâm của bài học.

### Ví dụ 2: Dữ liệu biên là một mode duy nhất

Nếu $$ f(\theta)=V_0\cos\theta $$, thì chỉ mode $$ n=1 $$ xuất hiện, và nghiệm là:

$$ u(r,\theta)=V_0\frac{r}{R}\cos\theta. $$

Ví dụ này cho thấy khi dữ liệu biên chỉ gồm một mode góc, nghiệm bên trong cũng giữ nguyên đúng mode đó.

### Ví dụ 3: Dữ liệu biên hằng

Nếu $$ f(\theta)=C $$, thì nghiệm bên trong miền là $$ u(r,\theta)=C $$. Điều này minh họa rằng mode $$ n=0 $$ chính là thành phần trung bình của dữ liệu biên.

### Ví dụ 4: Miền vành khăn

Nếu miền là hình vành khăn (không chứa tâm $$ r=0 $$), ta không còn loại bỏ các nghiệm $$ r^{-n} $$ hay $$ \ln r $$. Ví dụ này nhấn mạnh rằng điều kiện hữu hạn tại tâm bắt nguồn từ hình học miền chứ không phải quy tắc áp dụng mặc định cho mọi bài toán.

## Câu hỏi khái niệm

1. Vì sao miền hình tròn khiến tọa độ cực trở thành lựa chọn tự nhiên?
2. Yếu tố hình học nào của đĩa tròn dẫn đến việc loại bỏ các nghiệm kỳ dị tại tâm?
3. Vì sao dữ liệu biên theo góc dẫn đến chuỗi Fourier trong khi phần bán kính lại có dạng lũy thừa?

## Bài toán ứng dụng

1. Trong tĩnh điện, nếu biên của một đĩa tròn được đặt ở điện thế biến thiên theo góc, vì sao điện thế bên trong có thể biểu diễn bằng các mode Fourier theo góc?
2. Trong dòng chảy thế quanh tâm, vì sao tính đối xứng tròn làm cho lời giải phụ thuộc tự nhiên vào $$ r $$ và $$ \theta $$ thay vì $$ x,y $$?
3. Trong một đĩa tròn, vì sao các mode góc bậc cao thường ảnh hưởng rất yếu ở gần tâm?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu miền là hình tròn, việc giữ nguyên tọa độ $$ x,y $$ có phù hợp với hình học của bài toán không?"
- Cho sinh viên quan sát một vài mode $$ \cos(n\theta),\ \sin(n\theta) $$ và mô tả dạng phân bố theo góc của chúng.
- Hỏi cả lớp: "Điều gì xảy ra với nghiệm $$ r^{-n} $$ khi $$ r\to 0 $$?"
- So sánh bài toán trên đĩa tròn và trên hình vành khăn để làm rõ cách hình học miền quyết định việc giữ hay loại nghiệm.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung trước vào công thức nghiệm trên đĩa tròn và một vài mode bậc thấp. Khi đã nắm chắc trực giác về phần góc và phần bán kính, biểu thức chuỗi tổng quát sẽ dễ tiếp cận hơn.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi suy ra công thức tích phân Poisson cho đĩa tròn, hoặc phân tích vai trò của từng mode như một bộ lọc tần số góc khi đi vào bên trong miền.

## Tóm tắt dễ nhớ

Trên miền tròn, phương trình Laplace được giải thuận tiện nhất trong tọa độ cực. Nghiệm tách thành chuỗi Fourier theo góc và các lũy thừa theo bán kính: dữ liệu trên đường tròn biên quyết định các hệ số Fourier, còn điều kiện hữu hạn tại tâm loại bỏ các nghiệm kỳ dị.

## Video tham khảo

- xem trước: [Laplace PDE on circular domain solved in polar coordinates](https://www.youtube.com/watch?v=Yybsq8qiK9I) — Daniel An, tiếng Anh. Giải phương trình Laplace trên đĩa tròn bằng tọa độ cực.
- [10.1 General solution to Laplace's equation in polar coordinates](https://www.youtube.com/watch?v=fNSMMy9Q8Ls) — Daniel Nino, tiếng Anh. Trình bày nghiệm tổng quát trong tọa độ cực, bao gồm cả số hạng logarit.
- [The Laplacian in Polar Coordinates](https://www.youtube.com/watch?v=wlbZxa66ncg) — Mike, the Mathematician, tiếng Anh. Biểu diễn toán tử Laplace trong tọa độ cực trước khi thực hiện tách biến.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ ổn định quanh ống trụ
- Bài toán: Tính phân bố nhiệt độ ổn định quanh một ống trụ tròn dài.
- Mô hình:
$$
u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}=0.
$$
- Giả thiết và giới hạn: Đối xứng dọc trục, trạng thái dừng, hình học tròn lý tưởng.
- Diễn giải: Tọa độ cực khớp trực tiếp với hình học miền và giúp mô hình gọn rõ hơn.

#### Điện thế quanh điện cực tròn
- Bài toán: Xác định điện thế trong đĩa tròn hoặc hình vành khăn.
- Mô hình: Phương trình Laplace viết trong tọa độ cực.
- Giả thiết và giới hạn: Không có điện tích bên trong miền.
- Diễn giải: Các mode góc $$ \cos(n\theta) $$ và $$ \sin(n\theta) $$ phản ánh tính đối xứng của dữ liệu biên.

### 2. Trực giác bổ sung và các kết nối

Đổi hệ tọa độ không làm thay đổi bản chất vật lý nhưng có thể làm lộ rõ cấu trúc đối xứng của bài toán. Một sai sót phổ biến là giữ tọa độ Descartes quá lâu trên miền tròn, bỏ lỡ cách biểu diễn đơn giản hơn trong tọa độ cực.

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

Trên đĩa đơn vị, nếu dữ liệu biên là $$ u(1,\theta)=\cos\theta $$, thì nghiệm điều hòa tương ứng là $$ u(r,\theta)=r\cos\theta $$. Ví dụ kinh điển này cho thấy mode góc bậc một trên biên lan vào bên trong miền với nhân tử $$ r $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận biết khi nào cần chuyển sang tọa độ cực và thực hiện tách biến trên đĩa tròn.

**Bậc sau đại học.** Liên hệ với nhân Poisson trên đĩa tròn và biểu diễn hàm điều hòa bằng chuỗi Fourier.
