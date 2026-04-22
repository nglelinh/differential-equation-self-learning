---
layout: post
title: "Phương Trình Sóng Trong Chiều Cao Hơn"
chapter: '10'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 04 Wave Higher Dimensions]({{ site.imgurl }}/chapter_img/chapter10/04_wave_higher_dimensions.svg)

## Mục tiêu

Bài học này mở rộng trực giác sóng từ một chiều sang hai và ba chiều, nơi hình học của miền bắt đầu xuất hiện rõ ràng trong nghiệm. Sau bài học, sinh viên cần hiểu dạng nhiều chiều của phương trình sóng, biết vì sao hình học miền quyết định các mode riêng, nhận ra vai trò của các hệ tọa độ phù hợp như Descartes, cực, cầu, và thấy các hàm đặc biệt Bessel cùng các hàm cầu quay trở lại một cách tự nhiên.

## Kiến thức nền

Sinh viên nên nắm phương trình sóng một chiều, tách biến, Laplace operator và các hàm đặc biệt như Bessel, Legendre ở mức đã học trước đó. Bài này là nơi các chương trước bắt đầu thực sự liên kết với nhau.

## Dẫn nhập

Trong một chiều, sóng là chuyện của dây. Nhưng trong hai và ba chiều, ta gặp màng trống, mặt nước, sóng âm trong phòng, và trường điện từ trong không gian. Lúc đó, sóng không còn lan dọc theo một đường thẳng, mà lan theo mặt sóng. Hình học của miền trở thành nhân vật chính.

Đây là bài cực kỳ quan trọng để sinh viên thấy rằng PDE không chỉ là phương trình cộng với điều kiện biên, mà là phương trình cộng với hình học. Cùng một phương trình sóng, nhưng trên hình chữ nhật, đĩa tròn, hay quả cầu, hệ mode riêng sẽ hoàn toàn khác nhau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu gảy một dây đàn, ta nghe họa âm của một chiều. Nếu gõ một mặt trống tròn, các mode rung sẽ là những hoa văn với vòng tròn đồng tâm và cánh góc. Nếu nói trong một căn phòng, sóng âm phản xạ theo hình học ba chiều của phòng. Cùng là sóng, nhưng hình học miền quyết định cách năng lượng phân bố vào các mode.

### Cách nhìn hình ảnh

Trên hình chữ nhật, các mode là mạng nút dạng lưới. Trên đĩa tròn, các nút có thể là các vòng tròn và các tia góc. Trên quả cầu, các mode có cấu trúc múi và vành. Hình ảnh này rất quan trọng vì nó cho thấy nghiệm riêng không chỉ là công thức, mà là hình dạng dao động của toàn miền.

### Cách nhìn hình thức

Trong nhiều chiều, phương trình sóng có dạng $$ u_{tt}=c^2\Delta u $$. Với miền hình chữ nhật hai chiều, đặt $$ u(x,y,t)=X(x)Y(y)T(t) $$, ta được

$$
\frac{T''}{c^2T}=\frac{X''}{X}+\frac{Y''}{Y}=-\lambda.
$$

Sau đó ta tiếp tục tách $$ \lambda=\lambda_x+\lambda_y $$ và nhận được hai bài toán trị riêng một chiều cho $$ X $$ và $$ Y $$. Với miền tròn, trong tọa độ cực:

$$
u_{tt}=c^2\left(u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}\right),
$$

và phần bán kính dẫn đến phương trình Bessel.

## Những ngộ nhận thường gặp

- "Sóng nhiều chiều chỉ là sóng một chiều viết dài hơn." Sai. Hình học miền thay đổi hoàn toàn cấu trúc mode.
- "Dùng tọa độ nào cũng như nhau." Không đúng; chọn hệ tọa độ phù hợp với đối xứng giúp bài toán lộ ra cấu trúc tự nhiên.
- "Hàm Bessel và các hàm cầu là công cụ ngoại lai." Sai. Chúng xuất hiện đúng vì hình học tròn và cầu yêu cầu như vậy.
- "Mode nhiều chiều chỉ là sản phẩm cơ học của các mode một chiều." Chỉ đúng trong vài miền rất đặc biệt như hình chữ nhật.

## Tiến trình học tập đề xuất

### Bước 1: Viết dạng nhiều chiều của PDE

Sinh viên cần thấy toán tử Laplace là nhân vật chính mới.

### Bước 2: Chọn hệ tọa độ phù hợp

Hình chữ nhật đi với Descartes, đĩa tròn đi với cực, quả cầu đi với cầu.

### Bước 3: Tách biến và nhận diện bài toán riêng

Đây là nơi các hàm đặc biệt quay lại.

### Bước 4: Diễn giải mode như hoa văn dao động

Đừng để bài học chỉ dừng ở công thức.

### Các checkpoint

- Sinh viên có giải thích được vì sao hình học miền ảnh hưởng trực tiếp đến mode riêng hay không.
- Sinh viên có nhận ra vì sao đĩa tròn dẫn đến Bessel hay không.
- Sinh viên có hiểu rằng trong nhiều chiều, mode là hoa văn không gian chứ không chỉ là hàm số hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hình chữ nhật hai chiều

Trên miền $$ 0<x<a,\qquad 0<y<b $$, với biên cố định, các mode riêng có dạng

$$
X_m(x)=\sin\left(\frac{m\pi x}{a}\right),
\qquad
Y_n(y)=\sin\left(\frac{n\pi y}{b}\right).
$$

Do đó nghiệm riêng có dạng

$$
u_{mn}(x,y,t)=
\sin\left(\frac{m\pi x}{a}\right)
\sin\left(\frac{n\pi y}{b}\right)
T_{mn}(t),
$$

với tần số riêng phụ thuộc vào

$$ m,\ n. $$

### Ví dụ 2: Màng tròn

Với màng tròn, đặt $$ u(r,\theta,t)=R(r)\Theta(\theta)T(t) $$. Phần góc cho $$ \Theta(\theta)=\cos(m\theta),\ \sin(m\theta) $$, còn phần bán kính thỏa phương trình Bessel. Nghiệm hữu hạn tại tâm là $$ R(r)=J_m(\lambda r) $$. Ví dụ này là minh họa trực tiếp cho việc hình học tròn dẫn đến Bessel.

### Ví dụ 3: Đối xứng cầu

Trong đối xứng cầu, phương trình sóng có thể dẫn đến biểu diễn

$$ u(r,t)=\frac{1}{r}\bigl(F(r-ct)+G(r+ct)\bigr) $$

cho sóng xuyên tâm trong ba chiều. Ví dụ này cho sinh viên thấy cùng là sóng chạy, nhưng hình học không gian đã đưa thêm hệ số

$$ \frac{1}{r} $$

vào biên độ.

### Ví dụ 4: Ý nghĩa của hình học

Một mặt trống tròn và một mặt trống hình chữ nhật có cùng diện tích nhưng phổ dao động khác hẳn nhau. Đây là ví dụ rất mạnh để sinh viên thấy hình học quan trọng không kém phương trình.

## Câu hỏi khái niệm

1. Vì sao cùng một phương trình sóng nhưng miền khác nhau lại có phổ dao động khác nhau?
2. Vì sao tọa độ cực tự nhiên dẫn đến hàm Bessel?
3. Mode nhiều chiều nên được hiểu như công thức hay như hoa văn không gian?

## Bài toán ứng dụng

1. Vì sao âm thanh của trống tròn khác âm thanh của màng rung hình chữ nhật?
2. Trong âm học phòng, vì sao hình học căn phòng ảnh hưởng mạnh đến cộng hưởng?
3. Trong điện từ học, vì sao hình dạng ống dẫn sóng quyết định các mode cho phép?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu đổi dây đàn thành mặt trống, điều gì trong toán học phải thay đổi?"
- Cho sinh viên xem hoặc mô tả các hoa văn mode trên màng tròn và hình chữ nhật.
- Hỏi cả lớp: "Khi nào ta nên đổi hệ tọa độ trước khi giải PDE?"
- Khuyến khích sinh viên liên hệ bài này với Bessel và Legendre đã học trước đó.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám trước vào miền hình chữ nhật, vì ở đó mode còn là tích của các sin quen thuộc. Sau khi mẫu này vững, mới mở rộng sang đĩa tròn và tọa độ cực.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận các mode suy biến, vai trò của đối xứng nhóm trong đa bội trị riêng, hoặc phân tích sâu hơn các mode của màng tròn.

## Tóm tắt dễ nhớ

Trong nhiều chiều, phương trình sóng vẫn giữ cùng dạng nhưng hình học miền quyết định hệ mode riêng. Hình chữ nhật dẫn đến tích các sin, đĩa tròn dẫn đến Bessel, còn quả cầu dẫn đến các mode cầu. Cùng một PDE nhưng hình học khác thì sóng cũng khác về bản chất.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mặt trống rung
- Bài toán: Dao động của màng hai chiều tạo nên âm sắc của trống.
- Mô hình:
$$ u_{tt}=c^2\Delta u. $$
- Giả thiết và giới hạn: Màng mỏng, lực căng đều, dao động nhỏ.
- Diễn giải: Trong hai chiều, độ cong tổng quát được đo bởi Laplace.

#### Sóng âm trong phòng
- Bài toán: Áp suất âm trong một phòng phản xạ tạo các mode không gian.
- Mô hình: Dạng sóng nhiều chiều với điều kiện biên phụ thuộc tường cứng hay hấp thụ.
- Giả thiết và giới hạn: Môi trường tuyến tính, đồng nhất, hình học lý tưởng hóa.
- Diễn giải: Cấu trúc hình học của miền quyết định tần số cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Ở nhiều chiều, nhiễu loạn không chỉ đi trái và phải mà lan trên nhiều hướng. Vì thế hình học của miền bắt đầu đóng vai trò quan trọng. Đây là cầu nối tự nhiên sang phân tích phổ của miền và các bài toán trị riêng cho Laplace.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 120)
y = np.linspace(0, 1, 120)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi * X) * np.sin(2 * np.pi * Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("Mot mode rung cua mang hinh chu nhat")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: drumhead mode animation wave equation
- search: 2D wave equation membrane simulation
- search: room acoustics standing modes visualization

### 5. Bài toán mẫu có bối cảnh thực

Trên hình chữ nhật $$ 0<x<a $$, $$ 0<y<b $$, một mode có dạng
$$
u(x,y,t)=\sin\!\left(\frac{m\pi x}{a}\right)\sin\!\left(\frac{n\pi y}{b}\right)\cos(\omega_{mn} t),
$$
với
$$
\omega_{mn}=c\pi\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}.
$$
Chỉ số mode và kích thước miền cùng nhau quyết định tần số.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện Laplace như toán tử cong không gian trong nhiều chiều.

**Bậc sau đại học.** Kết nối với hình học phổ, hàm riêng của Laplacian và ảnh hưởng của miền lên phổ.
