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

Khi bước từ sợi dây 1D sang mặt trống 2D ($u_{tt} = c^2(u_{xx} + u_{yy})$) và không gian âm thanh/ánh sáng 3D ($u_{tt} = c^2 \nabla^2 u$), một hiện tượng vật lý ngoạn mục xuất hiện: **Nguyên lý Huygens**! Tại sao ta có thể nói chuyện rõ ràng trong không gian 3D (tiếng vỗ tay đi qua là dứt hẳn, không kéo đuôi), nhưng nếu sống trong thế giới phẳng 2D (như mặt ao nước), mọi âm thanh đều để lại một "cái đuôi vang" mờ ảo kéo dài vô tận?

## Kiến thức cần nhớ: Bốn trụ cột của Phương trình Sóng 2D & 3D

1. **Màng chữ nhật 2D ($[0, a] \times [0, b]$)**:
   Tách biến $u = X(x)Y(y)T(t)$ cho các mode $\sin\!\left(\frac{m\pi x}{a}\right)\sin\!\left(\frac{n\pi y}{b}\right)$ với tần số góc $\omega_{mn} = c\pi\sqrt{\frac{m^2}{a^2} + \frac{n^2}{b^2}}$. Khi $a = b$ (màng vuông), xuất hiện hiện tượng **suy biến (degeneracy)**: $(m, n) = (1, 2)$ và $(2, 1)$ có cùng tần số, tạo nên các họa tiết cát **Chladni** tuyệt đẹp!
2. **Màng tròn 2D (Tọa độ cực)**:
   Nghiệm tách thành $J_m(k r)\cos(m\theta)$ — kết nối trực tiếp với Hàm Bessel ở Chương 6.
3. **Công thức Kirchhoff trong 3D & Nguyên lý Huygens Mạnh**:
   Trong 3D, $u(\mathbf{x}, t)$ chỉ phụ thuộc vào dữ liệu ban đầu nằm **đúng trên mặt cầu rỗng** $\vert \mathbf{y} - \mathbf{x} \vert = ct$ (không phụ thuộc phần ruột bên trong!). Vì thế xung ánh sáng hay âm thanh có mặt đầu VÀ mặt đuôi sắc nét!
4. **Công thức Poisson trong 2D (Phương pháp Hạ chiều Hadamard)**:
   Trong 2D, $u(\mathbf{x}, t)$ phụ thuộc vào **toàn bộ đĩa đặc** $\vert \mathbf{y} - \mathbf{x} \vert \le ct$ — nên sóng 2D luôn để lại đuôi dư chấn kéo dài!

## Mục tiêu

Bài học này mở rộng phương trình sóng từ một chiều sang hai và ba chiều, nơi hình học của miền ảnh hưởng trực tiếp đến cấu trúc nghiệm. Sau bài học, sinh viên cần nắm dạng nhiều chiều của phương trình sóng, hiểu vì sao hình học miền quyết định hệ mode riêng, biết lựa chọn hệ tọa độ phù hợp (Descartes, cực, cầu) và thấy các hàm đặc biệt như hàm Bessel và hàm điều hòa cầu xuất hiện tự nhiên trong quá trình giải.

## Kiến thức nền

Sinh viên cần nắm phương trình sóng một chiều, phương pháp tách biến, toán tử Laplace và các hàm đặc biệt (Bessel, Legendre) đã học ở các chương trước. Bài học này kết nối trực tiếp nhiều kiến thức đã tích lũy.

## Dẫn nhập

Trong một chiều, sóng gắn với dao động của sợi dây. Sang hai và ba chiều, ta gặp mặt trống rung, sóng trên mặt nước, sóng âm trong phòng và sóng điện từ trong không gian. Khi đó, nhiễu loạn không còn truyền theo một đường thẳng mà lan theo các mặt sóng, và hình học của miền đóng vai trò quyết định.

Bài học này nhấn mạnh rằng một bài toán PDE không chỉ gồm phương trình và điều kiện biên mà còn phụ thuộc chặt chẽ vào hình học miền: cùng một phương trình sóng, nhưng trên hình chữ nhật, đĩa tròn hay hình cầu, hệ mode riêng và phổ tần số sẽ khác hẳn nhau.

### Giải thích: Tính tay các tần số suy biến đầu tiên của màng vuông $[0, \pi] \times [0, \pi]$ ($c = 1$)

Với $a = b = \pi$ và $c = 1$, công thức tần số rút gọn cực đẹp: $\omega_{mn} = \sqrt{m^2 + n^2}$ ($m, n \ge 1$):

| Mode $(m, n)$ | $m^2 + n^2$ | Tần số $\omega_{mn}$ | Bậc suy biến (số mode cùng tần số) |
| :---: | :---: | :---: | :---: |
| $(1, 1)$ | $2$ | $\sqrt{2} \approx 1{,}414$ | 1 (không suy biến) |
| $(1, 2)$ và $(2, 1)$ | $5$ | $\sqrt{5} \approx 2{,}236$ | **2 (suy biến!)** |
| $(2, 2)$ | $8$ | $\sqrt{8} \approx 2{,}828$ | 1 |
| $(1, 3)$ và $(3, 1)$ | $10$ | $\sqrt{10} \approx 3{,}162$ | **2 (suy biến!)** |

Vì $(1, 2)$ và $(2, 1)$ có cùng tần số $\sqrt{5}$, mọi tổ hợp $A\sin(x)\sin(2y) + B\sin(2x)\sin(y)$ đều là sóng đứng ở đúng tần số $\sqrt{5}$—chính là nguồn gốc các đường nút đối xứng hình học kỳ ảo khi rắc cát lên tấm kim loại rung (Chladni figures)!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Gảy một dây đàn tạo ra các họa âm một chiều; gõ một mặt trống tròn sinh ra các hoa văn dao động gồm các đường tròn đồng tâm và các đường kính nút; còn nói trong một căn phòng tạo ra sóng âm phản xạ theo hình dạng ba chiều của không gian. Cùng một quy luật truyền sóng, nhưng hình học miền quy định cách năng lượng phân bố vào các mode.

### Cách nhìn hình ảnh

Trên màng hình chữ nhật, các đường nút tạo thành mạng lưới vuông góc. Trên màng đĩa tròn, các đường nút là các vòng tròn đồng tâm và các tia xuyên tâm. Trên mặt cầu, các mode tổ chức thành các vùng phân chia theo kinh tuyến và vĩ tuyến. Cách nhìn này cho thấy mỗi mode riêng trong nhiều chiều là một hoa văn dao động đặc trưng của toàn miền.

### Cách nhìn hình thức

Trong nhiều chiều, phương trình sóng có dạng $$ u_{tt}=c^2\Delta u $$. Trên miền hình chữ nhật hai chiều, đặt $$ u(x,y,t)=X(x)Y(y)T(t) $$, ta thu được

$$
\frac{T''}{c^2T}=\frac{X''}{X}+\frac{Y''}{Y}=-\lambda.
$$

Tiếp tục tách $$ \lambda=\lambda_x+\lambda_y $$ dẫn đến hai bài toán trị riêng một chiều cho $$ X $$ và $$ Y $$. Trên miền đĩa tròn trong tọa độ cực, phương trình có dạng

$$
u_{tt}=c^2\left(u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}\right),
$$

và phần phụ thuộc bán kính sau tách biến dẫn đến phương trình Bessel.

## Những ngộ nhận thường gặp

- "Sóng nhiều chiều chỉ là sóng một chiều viết thêm biến." Sai; hình học miền làm thay đổi căn bản cấu trúc mode và phân bố tần số riêng.
- "Chọn hệ tọa độ nào để giải cũng như nhau." Không đúng; chọn hệ tọa độ tương thích với đối xứng của miền giúp tách biến thành công và làm lộ cấu trúc tự nhiên.
- "Hàm Bessel và hàm điều hòa cầu là các công cụ áp đặt từ bên ngoài." Sai; chúng xuất hiện tất yếu từ toán tử Laplace trên miền tròn và miền cầu.
- "Mode nhiều chiều luôn là tích đơn giản của các mode một chiều." Chỉ đúng với một số miền đặc biệt như hình chữ nhật hoặc hình hộp chữ nhật.

## Tiến trình học tập đề xuất

### Bước 1: Viết phương trình sóng nhiều chiều

Nhận diện vai trò trung tâm của toán tử Laplace $$ \Delta u $$.

### Bước 2: Lựa chọn hệ tọa độ phù hợp với hình học miền

Hình chữ nhật dùng tọa độ Descartes, đĩa tròn dùng tọa độ cực, hình cầu dùng tọa độ cầu.

### Bước 3: Tách biến và giải bài toán trị riêng

Quan sát cách các hàm đặc biệt (Bessel, hàm điều hòa cầu) xuất hiện tự nhiên.

### Bước 4: Diễn giải mode như các hoa văn dao động

Gắn công thức giải tích với hình ảnh đường nút và bụng sóng trên miền.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao hình học miền tác động trực tiếp đến hệ mode riêng hay không.
- Sinh viên có nêu được lý do miền tròn dẫn đến hàm Bessel hay không.
- Sinh viên có hình dung được các mode hai chiều như hoa văn nút–bụng trên bề mặt hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Màng hình chữ nhật hai chiều

Trên miền $$ 0<x<a,\qquad 0<y<b $$ với biên cố định, các hàm riêng theo từng trục là

$$
X_m(x)=\sin\left(\frac{m\pi x}{a}\right),
\qquad
Y_n(y)=\sin\left(\frac{n\pi y}{b}\right).
$$

Do đó mỗi mode riêng có dạng

$$
u_{mn}(x,y,t)=
\sin\left(\frac{m\pi x}{a}\right)
\sin\left(\frac{n\pi y}{b}\right)
T_{mn}(t),
$$

với tần số riêng phụ thuộc vào cặp chỉ số $$ m,\ n $$.

### Ví dụ 2: Màng đĩa tròn

Đặt $$ u(r,\theta,t)=R(r)\Theta(\theta)T(t) $$. Phần góc cho $$ \Theta(\theta)=\cos(m\theta),\ \sin(m\theta) $$, còn phần bán kính thỏa mãn phương trình Bessel. Điều kiện hữu hạn tại tâm chọn ra nghiệm $$ R(r)=J_m(\lambda r) $$. Đây là minh họa trực tiếp cho việc hình học tròn sinh ra hàm Bessel.

### Ví dụ 3: Sóng xuyên tâm có đối xứng cầu

Trong ba chiều với đối xứng cầu, phương trình sóng cho nghiệm dạng

$$ u(r,t)=\frac{1}{r}\bigl(F(r-ct)+G(r+ct)\bigr). $$

So với sóng một chiều, hình học không gian ba chiều làm xuất hiện thêm thừa số suy giảm biên độ $$ \frac{1}{r} $$ khi sóng lan ra xa nguồn.

### Ví dụ 4: Ảnh hưởng của hình học lên phổ tần số

Một mặt trống tròn và một màng hình chữ nhật có cùng diện tích nhưng có phổ tần số riêng khác hẳn nhau (chẳng hạn các tần số riêng của trống tròn không phải bội nguyên của âm cơ bản). Điều này cho thấy hình học miền quan trọng ngang với bản thân phương trình.

## Câu hỏi khái niệm

1. Vì sao cùng một phương trình sóng nhưng trên các miền khác nhau lại cho phổ dao động khác nhau?
2. Vì sao bài toán trên đĩa tròn trong tọa độ cực lại dẫn trực tiếp đến phương trình Bessel?
3. Nên hiểu các mode trong nhiều chiều dưới góc độ hình ảnh không gian như thế nào?

## Bài toán ứng dụng

1. Vì sao âm sắc của trống mặt tròn khác với âm sắc của một màng rung hình chữ nhật?
2. Trong âm học kiến trúc, vì sao hình dạng căn phòng ảnh hưởng mạnh đến các tần số cộng hưởng?
3. Trong kỹ thuật điện từ, vì sao tiết diện của ống dẫn sóng quyết định các mode truyền sóng được phép tồn tại?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Khi chuyển từ dây đàn một chiều sang mặt trống hai chiều, yếu tố toán học nào phải thay đổi?"
- Minh họa hoặc mô tả các đường nút (hình Chladni) trên màng tròn và màng hình chữ nhật.
- Đặt câu hỏi: "Khi nào cần đổi hệ tọa độ trước khi thực hiện tách biến cho PDE?"
- Khuyến khích sinh viên liên hệ lại kiến thức về hàm Bessel và hàm Legendre ở các chương trước.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu từ miền hình chữ nhật, nơi các mode vẫn là tích của các hàm sin quen thuộc, rồi mới mở rộng sang đĩa tròn và tọa độ cực.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên phân tích hiện tượng suy biến tần số (nhiều mode khác nhau có cùng tần số riêng trên miền vuông hoặc miền tròn), vai trò của tính đối xứng hình học trong độ bội trị riêng, hoặc khảo sát sâu hơn các không điểm của hàm Bessel.

## Tóm tắt dễ nhớ

Trong hai và ba chiều, phương trình sóng có dạng $$ u_{tt}=c^2\Delta u $$ và hình học miền quyết định trực tiếp hệ mode riêng: hình chữ nhật dẫn đến tích các hàm sin, đĩa tròn dẫn đến hàm Bessel, còn hình cầu dẫn đến các mode cầu và thừa số $$ 1/r $$ đối với sóng xuyên tâm.

## Video tham khảo

- Xem trước: [Vibrating Circular Membranes - Partial Differential Equations | Lecture 31](https://www.youtube.com/watch?v=DeG6dq4vlO4) — Jason Bramburger, tiếng Anh. Giải bài toán màng tròn dao động và chỉ rõ vai trò của hàm Bessel trong bài toán trị riêng theo bán kính.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Ôn lại cách thiết lập phương trình sóng một chiều trước khi mở rộng sang nhiều chiều.
- [Deriving the Heat Equation in 2D & 3D (& in N Dimensions!) with Control Volumes and Vector Calculus](https://www.youtube.com/watch?v=lBZIxv1bZDo) — Steve Brunton, tiếng Anh. Minh họa kỹ thuật thể tích kiểm soát trong 2D và 3D, tương đồng với cách thiết lập PDE ở chiều cao hơn.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mặt trống dao động
- Bài toán: Dao động của màng đàn hồi hai chiều tạo nên âm sắc đặc trưng của trống.
- Mô hình:
$$ u_{tt}=c^2\Delta u. $$
- Giả thiết và giới hạn: Màng mỏng, lực căng đồng đều, biên độ dao động nhỏ.
- Diễn giải: Trong hai chiều, độ cong bề mặt tổng quát được đo bởi toán tử Laplace.

#### Sóng âm trong phòng
- Bài toán: Trường áp suất âm phản xạ qua lại giữa các bức tường tạo thành các mode không gian.
- Mô hình: Phương trình sóng ba chiều kèm điều kiện biên phụ thuộc tính chất tường cứng hay hấp thụ âm.
- Giả thiết và giới hạn: Môi trường tuyến tính, đồng nhất, hình học phòng lý tưởng hóa.
- Diễn giải: Hình học của căn phòng quyết định trực tiếp các tần số cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Trong không gian nhiều chiều, nhiễu loạn lan truyền theo mọi hướng nên hình học miền ảnh hưởng trực tiếp tới phổ dao động. Nội dung này mở sang bài toán trị riêng của toán tử Laplace và hình học phổ.

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

Trên miền hình chữ nhật $$ 0<x<a $$, $$ 0<y<b $$, một mode dao động có dạng
$$
u(x,y,t)=\sin\!\left(\frac{m\pi x}{a}\right)\sin\!\left(\frac{n\pi y}{b}\right)\cos(\omega_{mn} t),
$$
với tần số góc riêng
$$
\omega_{mn}=c\pi\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}.
$$
Cặp chỉ số mode cùng kích thước miền xác định trực tiếp tần số dao động.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu toán tử Laplace như thước đo độ cong không gian nhiều chiều và giải được bài toán trên miền cơ bản.

**Bậc sau đại học.** Tìm hiểu hình học phổ, tính chất hàm riêng của toán tử Laplace và mối liên hệ giữa hình học miền với phân bố phổ.
