---
layout: post
title: "00-10 Giải tích Vector"
chapter: '00'
order: 10
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---


Nhiệt chảy từ nơi nóng sang nơi lạnh, chất lỏng xoáy quanh trụ cầu, còn điện trường tỏa ra từ điện tích—mọi định luật bảo toàn của vật lý đều được viết bằng ngôn ngữ của **giải tích vectơ**. Nắm vững bộ ba toán tử $\nabla$ (Gradient, Divergence, Curl) cùng hai định lý Gauss và Stokes chính là chiếc cầu trực tiếp biến định luật bảo toàn vật lý thành phương trình đạo hàm riêng (PDE) ở các chương cuối.

## Kiến thức cần nhớ: Bốn trụ cột của Giải tích Vectơ

1. **Bộ ba toán tử vi phân ($\nabla f$, $\nabla \cdot \mathbf{F}$, $\nabla \times \mathbf{F}$)**:
   Gradient đo độ dốc cực đại của trường vô hướng; Divergence đo mật độ "nguồn phát / hút" cục bộ của dòng chảy; Curl đo độ xoáy cục bộ quanh từng điểm.
2. **Toán tử Laplace ($\Delta u = \nabla \cdot (\nabla u) = u_{xx} + u_{yy} + u_{zz}$)**:
   Đo sự chênh lệch giữa giá trị của $u$ tại một điểm với trung bình xung quanh nó—xuất hiện ở tâm điểm của phương trình truyền nhiệt, phương trình sóng và phương trình Laplace.
3. **Định lý Phân kỳ Gauss ($\iiint_V (\nabla \cdot \mathbf{F})\,dV = \iint_{\partial V} \mathbf{F} \cdot \mathbf{n}\,dS$)**:
   Liên hệ tổng nguồn sinh ra bên trong thể tích $V$ với tổng thông lượng chảy qua mặt biên $\partial V$—cách chuẩn mực nhất để suy ra phương trình truyền nhiệt $u_t = \alpha \Delta u$.
4. **Định lý Green & Stokes ($\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$)**:
   Liên hệ độ xoáy trên mặt với lưu số dọc biên; khi $\nabla \times \mathbf{F} = \mathbf{0}$ trên miền đơn liên, trường vectơ là trường bảo toàn ($\mathbf{F} = \nabla \phi$)—tương ứng trực tiếp với phương trình vi phân toàn phần.

## Mục tiêu
Bài học này giúp sinh viên nắm vững ba phép toán vi phân cơ bản trên trường vô hướng và trường vector (gradient, divergence, curl), hiểu **ba định lý tích phân (Green, Stokes, Gauss)** cùng mối liên hệ giữa chúng, và vận dụng các công cụ này vào việc mô hình hóa các hiện tượng vật lý. Đây là nền tảng trực tiếp cho phương trình đạo hàm riêng (PDE) và các phương pháp giải PDE.

## Kiến thức nền
Sinh viên cần nắm vững đạo hàm riêng và gradient từ các bài trước, hiểu khái niệm tích phân đường, tích phân mặt, tích phân bội và có kiến thức cơ bản về hình học không gian (mặt phẳng, mặt cong).

## Dẫn nhập
Trong nhiều bài toán thực tế, ta không chỉ xét hàm một biến mà làm việc với các trường—những đại lượng phân bố trong không gian—như trường nhiệt độ $$ T(x,y,z) $$, trường vận tốc chất lưu $$ v(x,y,z) $$ hay điện trường $$ E(x,y,z) $$. Để mô tả và phân tích những trường này, ta cần các phép toán vi phân và tích phân trong không gian nhiều chiều.

Hãy hình dung một dòng sông. Gradient của độ cao mặt nước cho biết hướng dốc lớn nhất (nước chảy từ cao xuống thấp theo hướng ngược gradient); divergence của trường vận tốc cho biết tại một điểm có nguồn chảy ra hay bể hút vào; còn curl của trường vận tốc cho biết dòng chảy tại đó có xoáy hay không. Ba phép toán này mô tả đầy đủ các đặc trưng cục bộ của một trường trong không gian.

### Giải thích: Kiểm chứng định lý Phân kỳ Gauss bằng tay cho trường xuyên tâm $\mathbf{F}(x, y, z) = (x, y, z)$ trên hình cầu bán kính $R = 2$

1. **Vế trái (Tích phân thể tích của Divergence)**:
   $$\nabla \cdot \mathbf{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3.$$
   Tích phân trên hình cầu bán kính $R = 2$ (thể tích $V = \frac{4}{3}\pi R^3 = \frac{32\pi}{3}$):
   $$\iiint_V 3\,dV = 3 \cdot \frac{32\pi}{3} = \mathbf{32\pi}.$$
2. **Vế phải (Tích phân mặt thông lượng qua mặt cầu $x^2 + y^2 + z^2 = 4$)**:
   Pháp vectơ đơn vị hướng ra ngoài tại $(x, y, z)$ là $\mathbf{n} = \frac{(x, y, z)}{R} = \frac{(x, y, z)}{2}$.
   Tích vô hướng trên mặt cầu: $\mathbf{F} \cdot \mathbf{n} = \frac{x^2 + y^2 + z^2}{2} = \frac{4}{2} = 2$.
   Diện tích mặt cầu bán kính $R = 2$ là $4\pi R^2 = 16\pi$, nên:
   $$\iint_{\partial V} \mathbf{F} \cdot \mathbf{n}\,dS = 2 \cdot 16\pi = \mathbf{32\pi}.$$
   Hai vế khớp tuyệt đối $32\pi = 32\pi$!

## Khái niệm theo ba cách

### Cách nhìn trực quan
- **Gradient $$ \nabla f $$**: Tương tự la bàn chỉ hướng leo dốc nhanh nhất trên một sườn núi. Gradient cung cấp hai thông tin: **(1)** hướng tăng nhanh nhất của hàm vô hướng $$ f $$; **(2)** độ lớn $$ \|\nabla f\| $$ cho biết tốc độ tăng theo hướng đó. Vector gradient luôn vuông góc với đường đồng mức (level curves) hoặc mặt đồng mức.

- **Divergence $$ \nabla \cdot F $$**: Đo lưu lượng ròng chảy ra từ một điểm. Nếu divergence dương, điểm đó đóng vai trò như **nguồn** (source) có dòng chảy tỏa ra; nếu divergence âm, điểm đó đóng vai trò như **bể** (sink) có dòng chảy hội tụ vào. Trong điện từ học, divergence của điện trường $$ E $$ tỉ lệ với mật độ điện tích theo định luật Gauss: $$ \nabla \cdot E = \rho / \varepsilon_0 $$.

- **Curl $$ \nabla \times F $$**: Tương tự chuyển động quay của một chong chóng nhỏ đặt trong dòng chảy. Nếu dòng nước có xoáy, chong chóng sẽ quay: **(1)** phương của vector curl là trục quay (theo quy tắc bàn tay phải); **(2)** độ lớn của curl đo cường độ xoáy tại điểm đó. Khi curl khác vector không, trường có **xoáy** (circulation).

### Cách nhìn hình ảnh
Xét trường vector phẳng $$ F(x,y) = (-y, x) $$. Các mũi tên của trường tạo thành các vòng quay ngược chiều kim đồng hồ quanh gốc tọa độ. Tại mọi điểm, divergence bằng $$ 0 $$, còn curl (khi xem là trường trong không gian ba chiều $$ (-y,x,0) $$) bằng $$ \left(0,0,2\right) \neq 0 $$.

### Cách nhìn hình thức

Trước hết cần phân biệt hai loại trường:
- **$$ f(x,y,z) $$**: **Trường vô hướng** (scalar field) — gán cho mỗi điểm trong không gian một số thực, ví dụ nhiệt độ $$ T(x,y,z) $$, áp suất $$ p(x,y,z) $$ hoặc thế năng $$ V(x,y,z) $$.
- **$$ F(x,y,z) = (P,Q,R) $$**: **Trường vector** (vector field) — gán cho mỗi điểm trong không gian một vector, ví dụ vận tốc gió $$ v(x,y,z) $$, trường lực $$ F(x,y,z) $$ hoặc điện trường $$ E(x,y,z) $$.

Phép toán **gradient** tác động lên trường vô hướng $$ f $$ và cho ra một trường vector, còn **divergence** và **curl** tác động lên trường vector $$ F $$ để đo lần lượt độ phân kỳ (vô hướng) và độ xoáy (vector).

**Gradient**: Với trường vô hướng $$ f(x,y,z) $$, ta có $$\nabla f = \left(\partial f/\partial x, \partial f/\partial y, \partial f/\partial z\right)$$. Gradient chỉ hướng tăng nhanh nhất của $$ f $$.

![Gradient: hướng tăng nhanh nhất]({{ site.imgurl }}/chapter_img/chapter00/00_10_gradient.svg)

**Divergence**: Với trường vector $$ F = (P, Q, R) $$, ta có $$\nabla \cdot F = \partial P/\partial x + \partial Q/\partial y + \partial R/\partial z$$. Đây là đại lượng vô hướng đo mật độ lưu lượng tỏa ra tại mỗi điểm.

![Divergence: nguồn và bể]({{ site.imgurl }}/chapter_img/chapter00/00_10_divergence.svg)

**Curl**: Với trường vector $$ F = (P, Q, R) $$, ta có $$\nabla \times F = \left(\partial R/\partial y - \partial Q/\partial z,\partial P/\partial z - \partial R/\partial x,\partial Q/\partial x - \partial P/\partial y\right)$$. Đây là đại lượng vector đo mức độ xoáy của trường.

![Curl: hiện tượng xoáy]({{ site.imgurl }}/chapter_img/chapter00/00_10_curl.svg)

### Định lý Green

**Ý nghĩa**: Định lý Green liên hệ tích phân đường dọc theo đường cong kín $$ C $$ (biên 1D) với tích phân kép trên miền phẳng $$ D $$ (miền 2D bên trong):
$$\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA$$

![Định lý Green]({{ site.imgurl }}/chapter_img/chapter00/00_10_green_theorem.svg)

**Giải thích trực quan**: Nếu bạn đi một vòng quanh bờ hồ (đường cong kín $$ C $$), tổng lưu số (công) dọc theo đường biên bằng tổng độ xoáy tích lũy trên toàn bộ diện tích mặt hồ $$ D $$ bên trong.

**Điều kiện áp dụng**: Miền $$ D $$ bị chặn với biên $$ C $$ trơn từng khúc được định hướng dương (ngược chiều kim đồng hồ), và các hàm $$ P, Q $$ khả vi liên tục trên một miền mở chứa $$ D $$.

**Ví dụ**: Tính $$ \oint_C (y\,dx + x^2 y^2\,dy) $$ với $$ C $$ là đường tròn đơn vị định hướng dương. Đặt $$ P = y $$, $$ Q = x^2 y^2 $$, ta có:
$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2xy^2 - 1$$

Chuyển sang tọa độ cực $$ x = r\cos\theta $$, $$ y = r\sin\theta $$, $$ dA = r\,dr\,d\theta $$ trên đĩa đơn vị $$ 0 \leq r \leq 1 $$, $$ 0 \leq \theta \leq 2\pi $$:
$$\iint_D (2xy^2 - 1)\,dA = \int_0^{2\pi}\int_0^1 (2r^3\cos\theta\sin^2\theta - 1)r\,dr\,d\theta = -\pi$$

### Định lý Stokes

**Ý nghĩa**: Định lý Stokes liên hệ tích phân đường dọc theo biên kín $$ \partial S $$ (đường cong 1D) với tích phân mặt của curl trên mặt cong $$ S $$ (mặt 2D):
$$\oint_{\partial S} F\cdot dr = \iint_S (\nabla \times F)\cdot n\,dS$$

![Định lý Stokes]({{ site.imgurl }}/chapter_img/chapter00/00_10_stokes_theorem.svg)

**Giải thích trực quan**: Đây là dạng mở rộng của định lý Green trong không gian 3D. Hình dung một cánh buồm cong $$ S $$ căng trong luồng gió với trường lực $$ F $$: tổng công của trường dọc theo viền biên $$ \partial S $$ bằng thông lượng của vector xoáy $$ \nabla \times F $$ xuyên qua toàn bộ mặt $$ S $$.

**Điều kiện áp dụng**: Mặt $$ S $$ định hướng và trơn từng khúc có biên kín $$ \partial S $$ định hướng tương thích với vector pháp tuyến đơn vị $$ n $$ (theo quy tắc bàn tay phải), và $$ F $$ khả vi liên tục quanh $$ S $$.

**Ví dụ**: Tính $$ \oint_{\partial S} F\cdot dr $$ với $$ F = (-y, x, 0) $$ và $$ S $$ là nửa mặt cầu đơn vị phía trên $$ x^2+y^2+z^2=1 $$, $$ z \geq 0 $$ (pháp tuyến hướng ra ngoài). Ta có $$ \nabla \times F = (0, 0, 2) $$. Vì $$ (\nabla \times F)\cdot n = 2\cos\gamma $$ (với $$ \gamma $$ là góc giữa pháp tuyến $$ n $$ và trục $$ Oz $$), tích phân mặt trên nửa mặt cầu đơn vị bằng $$ 2 $$ lần diện tích hình chiếu xuống mặt phẳng $$ Oxy $$ (đĩa đơn vị diện tích $$ \pi $$), nên kết quả là $$ 2\pi $$.

### Định lý Gauss (Divergence)

**Định lý Gauss** liên hệ tích phân mặt trên mặt biên kín $$ \partial V $$ (mặt 2D) với tích phân bội ba trên miền khối $$ V $$ (miền 3D):
$$\iiint_V (\nabla \cdot F)\,dV = \iint_{\partial V} F\cdot n\,dS$$

![Định lý Gauss]({{ site.imgurl }}/chapter_img/chapter00/00_10_gauss_theorem.svg)

**Giải thích trực quan**: Nếu trong một khối chất lưu $$ V $$ có các nguồn phát và bể hút, tổng lưu lượng chảy ra qua mặt biên kín $$ \partial V $$ bằng tổng cường độ nguồn–bể (tích phân của divergence) bên trong toàn bộ thể tích $$ V $$.

**Điều kiện áp dụng**: Miền khối $$ V $$ bị chặn có mặt biên $$ \partial V $$ trơn từng khúc với pháp tuyến đơn vị $$ n $$ hướng ra ngoài, và trường $$ F $$ khả vi liên tục trên một miền mở chứa $$ V $$.

**Ví dụ**: Tính thông lượng của $$ F = (x, y, z) $$ ra khỏi mặt cầu đơn vị $$ x^2 + y^2 + z^2 = 1 $$. Tính trực tiếp: trên mặt cầu, pháp tuyến đơn vị hướng ra ngoài là $$ n = (x, y, z) $$, nên $$ F\cdot n = x^2 + y^2 + z^2 = 1 $$. Vì diện tích mặt cầu đơn vị là $$ 4\pi $$, ta có $$ \iint_{\partial V} F\cdot n\,dS = 4\pi $$.

Áp dụng định lý Gauss: $$ \nabla \cdot F = \partial x/\partial x + \partial y/\partial y + \partial z/\partial z = 3 $$. Thể tích khối cầu đơn vị là $$ 4\pi/3 $$, nên $$ \iiint_V 3\,dV = 3 \cdot (4\pi/3) = 4\pi $$. Hai cách tính cho cùng kết quả.

## Những ngộ nhận thường gặp
- "Gradient là một đại lượng vô hướng." Sai. Gradient tác động lên hàm vô hướng nhưng kết quả thu được là một trường vector.
- "Divergence và curl có bản chất giống nhau." Sai. Divergence là đại lượng vô hướng đo mức độ tỏa ra/hội tụ (nguồn/bể), còn curl là đại lượng vector đo mức độ xoáy.
- "Định lý Green chỉ áp dụng cho hình tròn." Sai. Định lý áp dụng cho mọi miền phẳng bị chặn $$ D $$ có biên $$ C $$ trơn từng khúc.
- "Nếu $$ \nabla \times F = 0 $$ thì $$ F $$ chắc chắn là trường thế." Chưa đủ nếu miền không đơn liên. Ví dụ trường $$ F = \left(-y/(x^2+y^2), x/(x^2+y^2)\right) $$ có curl bằng $$ 0 $$ nhưng không có hàm thế trên toàn bộ $$ \mathbb{R}^2 \setminus \{(0,0)\} $$.

## Tiến trình học tập đề xuất

### Bước 1: Nắm ý nghĩa vật lý của ba phép toán
Gắn từng phép toán với trực giác: gradient là hướng tăng nhanh nhất, divergence là nguồn/bể, curl là độ xoáy. Vẽ một số trường vector đơn giản để quan sát trực tiếp.

### Bước 2: Thành thạo công thức và kỹ năng tính
Ghi nhớ công thức tọa độ và luyện tính trên các trường đa thức đơn giản, chú ý đúng thứ tự lấy đạo hàm và dấu trong công thức curl.

### Bước 3: Kết nối ba định lý tích phân
Nhận thấy cả ba định lý đều nối tích phân trên biên với tích phân trên miền bên trong: Green nối biên một chiều với miền phẳng hai chiều; Stokes nối biên một chiều với mặt cong hai chiều; Gauss nối mặt biên hai chiều với khối ba chiều.

### Các checkpoint
- Bạn có tính đúng gradient, divergence và curl của các trường cơ bản không?
- Bạn có phát biểu chính xác và vận dụng được ba định lý Green, Stokes, Gauss không?
- Bạn có giải thích được ý nghĩa vật lý của từng phép toán không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tính gradient
Cho $$ f(x,y,z) = xyz^2 + x^2 z $$. Tính các đạo hàm riêng: $$ \partial f/\partial x = yz^2 + 2xz $$, $$ \partial f/\partial y = xz^2 $$, và $$ \partial f/\partial z = 2xyz + x^2 $$. Do đó

$$
\nabla f = \left(yz^2 + 2xz, xz^2, 2xyz + x^2\right).
$$

Tại điểm $$ \left(1,1,1\right) $$, ta thu được $$ \nabla f(1,1,1) = (3,1,3) $$.

### Ví dụ 2: Tính divergence và curl
Cho $$ F = (x^2 y, yz^2, zx^2) $$. Ta có

$$
\nabla \cdot F = \frac{\partial}{\partial x}(x^2 y) + \frac{\partial}{\partial y}(yz^2) + \frac{\partial}{\partial z}(zx^2) = 2xy + z^2 + x^2,
$$

và

$$
\nabla \times F =
\left(
\frac{\partial}{\partial y}(zx^2) - \frac{\partial}{\partial z}(yz^2),
\frac{\partial}{\partial z}(x^2 y) - \frac{\partial}{\partial x}(zx^2),
\frac{\partial}{\partial x}(yz^2) - \frac{\partial}{\partial y}(x^2 y)
\right)
= \left(-2yz,-2xz,-x^2\right).
$$

Tại $$ \left(1,1,1\right) $$, divergence bằng $$ 4 $$ và curl bằng $$ (-2,-2,-1) $$.

### Ví dụ 3: Áp dụng định lý Green
Tính $$ \oint_C \left(y\,dx + x^2 y^2\,dy\right) $$ với $$ C $$ là đường tròn đơn vị định hướng dương. Theo định lý Green,

$$
\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA.
$$

Với $$ P = y $$ và $$ Q = x^2 y^2 $$, ta có $$\partial Q/\partial x - \partial P/\partial y = 2xy^2 - 1$$. Đổi sang tọa độ cực trên đĩa đơn vị như đã thực hiện ở trên, thành phần $$ 2xy^2 $$ tích phân bằng $$ 0 $$ do tính đối xứng, còn lại tích phân của $$ -1 $$ trên đĩa bán kính $$ 1 $$, cho kết quả $$ -\pi $$.

### Ví dụ 4: Kiểm tra trường thế
Cho $$ F = (2xy + z^3, x^2, 3xz^2) $$. Tính trực tiếp cho thấy $$ \nabla \times F = (0,0,0) $$. Vì $$ F $$ xác định trên toàn $$ \mathbb{R}^3 $$ (miền đơn liên), nên $$ F $$ là trường thế. Tích phân $$ \partial f/\partial x = 2xy + z^3 $$ rồi đối chiếu với hai thành phần còn lại, ta tìm được hàm thế $$ f(x,y,z) = x^2 y + xz^3 + C $$.

### Ví dụ 5: Áp dụng trong PDE — phương trình Laplace
Hàm điều hòa thỏa mãn phương trình Laplace $$ \nabla^2 f = 0 $$, trong đó $$\nabla^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2 + \partial^2/\partial z^2$$ là toán tử Laplace. Với $$ f = x^2 - y^2 - z^2 $$, ta có $$ \nabla^2 f = 2 - 2 - 2 = -2 \neq 0 $$ nên hàm không điều hòa. Ngược lại, với $$ f = 1/\sqrt{x^2+y^2+z^2} $$, ta có $$ \nabla^2 f = 0 $$ trên $$ \mathbb{R}^3 \setminus \{0\} $$.

## Câu hỏi khái niệm
1. Vì sao gradient, divergence và curl giữ vai trò trung tâm trong vật lý toán? Hãy nêu ví dụ trong cơ học chất lưu hoặc điện từ học.
2. Ba định lý Green, Stokes và Gauss có cấu trúc chung nào, và vì sao chúng được gọi là các định lý liên hệ biên với miền?
3. Điều kiện cần và đủ để một trường vector khả vi liên tục là trường thế là gì? Vì sao tính đơn liên của miền lại quan trọng?

## Bài toán ứng dụng
1. **Vật lý — Điện trường**: Điện trường tĩnh liên hệ với điện thế $$ V $$ qua $$ E = -\nabla V $$. Nếu $$ V = k/r $$, hãy tính $$ E $$ và giải thích mối liên hệ giữa divergence của $$ E $$ với mật độ điện tích.
2. **Cơ học chất lưu**: Trường vận tốc của chất lưu không nén được có divergence bằng $$ 0 $$. Hãy giải thích ý nghĩa vật lý của điều kiện này.
3. **Truyền nhiệt**: Xét phương trình truyền nhiệt $$ \partial u/\partial t = \alpha \nabla^2 u $$. Vì sao toán tử $$ \nabla^2 u = \nabla \cdot (\nabla u) $$ xuất hiện, và từng số hạng mang ý nghĩa vật lý gì?

## Chiến lược giảng dạy tương tác
- **Hoạt động "Vẽ trường"**: Cho sinh viên phác họa hai trường vector $$ F = (y,-x) $$ và $$ F = (x,y) $$, sau đó tính và so sánh divergence, curl của từng trường.
- **Thảo luận nhóm**: Mỗi nhóm tính $$ \nabla \cdot F $$ và $$ \nabla \times F $$ cho một trường được giao rồi trình bày ý nghĩa vật lý tương ứng.
- **Câu hỏi nhanh**: "Trong ba trường $$ (x,y) $$, $$ (-y,x) $$ và $$ (x^2,y^2) $$, trường nào có divergence bằng $$ 0 $$ nhưng curl khác $$ 0 $$?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Bắt đầu từ ý nghĩa hình học và vật lý trước khi đi vào công thức tọa độ.
- Vẽ nhiều trường vector hai chiều đơn giản để rèn trực giác.
- Luyện tập tính toán trên các trường đa thức bậc thấp trước khi sang biểu thức phức tạp.

### Thử thách cho sinh viên khá giỏi
- Nghiên cứu chứng minh chi tiết một trong ba định lý Green, Stokes hoặc Gauss.
- Tìm hiểu toán tử Laplace–Beltrami và cách mở rộng giải tích vector lên đa tạp cong.
- Tìm hiểu phương trình Navier–Stokes và vai trò của divergence, curl trong cơ học chất lưu.

## Tóm tắt dễ nhớ
- **Gradient $$ \nabla f $$**: Vector chỉ hướng tăng nhanh nhất của hàm vô hướng, vuông góc với đường mức.
- **Divergence $$ \nabla \cdot F $$**: Đại lượng vô hướng đo nguồn hoặc bể.
- **Curl $$ \nabla \times F $$**: Vector đo độ xoáy của trường.
- **Green**: $$\oint_C P\,dx + Q\,dy = \iint_D \left(\partial Q/\partial x - \partial P/\partial y\right)\,dA$$.
- **Stokes**: $$\oint_{\partial S} F\cdot dr = \iint_S \left(\nabla \times F\right)\cdot n\,dS$$.
- **Gauss**: $$ \iiint_V (\nabla \cdot F)\,dV = \iint_{\partial V} F\cdot n\,dS $$.
- Cả ba định lý đều nối tích phân trên biên với tích phân của toán tử vi phân tương ứng (độ xoáy hoặc độ phân kỳ) trên miền bên trong.

## Video tham khảo

- Xem trước: [Div, Grad, and Curl: Vector Calculus Building Blocks for PDEs (Divergence, Gradient, and Curl)](https://www.youtube.com/watch?v=lKXW7DRyyro) — Steve Brunton, tiếng Anh. Trình bày gradient, divergence và curl như ba khối xây dựng cơ bản để thiết lập các phương trình PDE.
- [Divergence and curl:  The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) — 3Blue1Brown, tiếng Anh. Minh họa trực quan ý nghĩa của divergence và curl trong dòng chất lưu và trường điện từ.
- [Gauss's Divergence Theorem](https://www.youtube.com/watch?v=TORt20_HjMY) — Steve Brunton, tiếng Anh. Giải thích định lý divergence—công cụ chuyển từ bảo toàn thông lượng sang phương trình PDE.

## Tài liệu tham khảo
- Marsden & Tromba — *Vector Calculus*: giáo trình chuẩn về giải tích vector.
- Griffiths — *Introduction to Electrodynamics*: trình bày sâu các ứng dụng trong điện từ học.
- Strauss — *Partial Differential Equations*: kết nối trực tiếp giải tích vector với PDE.
