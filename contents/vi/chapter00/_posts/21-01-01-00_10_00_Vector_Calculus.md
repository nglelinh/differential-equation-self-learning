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

## Mục tiêu
Bài học này giúp sinh viên nắm vững ba phép toán cơ bản trên trường vector (gradient, divergence, curl), hiểu sâu sắc **ba định lý tích phân (Green, Stokes, Gauss)** và mối liên hệ giữa chúng, đồng thời vận dụng được trong việc mô hình hóa các hiện tượng vật lý. Đây là công cụ không thể thiếu để học phương trình đạo hàm riêng và các phương pháp giải PDE như phân tách biến.

## Kiến thức nền
Sinh viên cần nắm vững đạo hàm riêng, gradient từ bài trước, hiểu khái niệm tích phân đường và tích phân mặt, biết cơ bản về hình học không gian (mặt phẳng, mặt cong). Kiến thức về tích phân nhiều lớp cũng hữu ích.

## Dẫn nhập
Trong nhiều bài toán thực tế, ta không chỉ làm việc với hàm một biến mà với các trường, tức các đại lượng phân bố trong không gian. Chẳng hạn có trường nhiệt độ $$ T(x,y,z) $$, trường vận tốc chất lỏng $$ v(x,y,z) $$, hay trường điện $$ E(x,y,z) $$. Để mô tả những trường này, ta cần các phép toán vi phân và tích phân trên không gian nhiều chiều.

Hãy hình dung một dòng sông. Gradient của độ cao mặt nước cho biết nước chảy theo hướng nào (từ cao xuống thấp). Divergence của trường vận tốc cho biết tại một điểm có "nguồn" hay "bể" nước (nước chảy ra hay chảy vào). Curl của trường vận tốc cho biết dòng nước có xoáy hay không. Ba phép toán này cho ta "bức tranh" đầy đủ về hành vi của trường.

## Khái niệm theo ba cách

### Cách nhìn trực quan
- **Gradient $$ \nabla f $$**: Như la bàn chỉ hướng leo dốc nhất trên một ngọn núi. Gradient cho biết hai điều: **(1)** hướng nào leo dốc nhanh nhất — nếu bạn đứng ở một điểm trên sườn núi và muốn lên đỉnh nhanh nhất, bạn phải đi theo hướng của gradient; **(2)** dốc có bao nhiêu — độ lớn $$ \|\nabla f\| $$ cho biết sườn núi tại điểm đó dốc đến mức nào. Gradient luôn vuông góc với đường đồng mức (level curves), tức các vòng tròn đường bao quanh đỉnh núi trên bản đồ địa hình.

- **Divergence $$ \nabla \cdot F $$**: Như lượng nước "chảy ra" khỏi một cái vòi. Tại mỗi điểm, divergence đo xem có bao nhiêu "chất lỏng" (theo nghĩa vật lý hoặc tượng trưng) được tạo ra hoặc bị hút vào tại điểm đó. Nếu divergence dương, điểm đó hoạt động như **nguồn** (source) — có dòng chảy ra; nếu divergence âm, điểm đó hoạt động như **bể** (sink) — có dòng chảy vào. Trong vật lý, divergence dương của trường điện $$ E $$ tương ứng với sự hiện diện của điện tích (định lý Gauss: $$ \nabla \cdot E = \rho / \varepsilon_0 $$).

- **Curl $$ \nabla \times F $$**: Như cách quay của cái chong chóng đặt trong dòng nước. Nếu bạn thả một cái chong chóng nhỏ vào dòng sông, nó sẽ quay nếu dòng nước có "xoáy". Curl đo chính xác điều này: **(1)** hướng của trục quay — trục của chong chóng sẽ chỉ theo vector curl (quy tắc bàn tay phải); **(2)** tốc độ quay — độ lớn của curl cho biết chong chóng quay nhanh như thế nào. Curl khác vector-không nghĩa là trường có **xoáy** (circulation), tức một vòng kín trong trường sẽ đẩy vật thể quay.

### Cách nhìn hình ảnh
Vẽ trường vector $$ F(x,y) = (-y, x) $$ trên mặt phẳng. Đây là trường quay theo chiều ngược kim đồng hồ. Tại mọi điểm, divergence bằng $$ 0 $$, còn curl bằng $$ \left(0,0,2\right) \neq 0 $$. Nếu vẽ các mũi tên, ta sẽ thấy chúng tạo thành các vòng tròn quanh gốc.

### Cách nhìn hình thức

Trước khi đi vào công thức, cần phân biệt hai loại đại lượng:
- **$$ f(x,y,z) $$**: **Hàm vô hướng** (scalar field) — mỗi điểm trong không gian cho một con số. Ví dụ: nhiệt độ $$ T(x,y,z) $$, áp suất $$ p(x,y,z) $$, thế năng $$ V(x,y,z) $$.
- **$$ F(x,y,z) = (P,Q,R) $$**: **Trường vector** (vector field) — mỗi điểm trong không gian cho một vector (có cả hướng và độ lớn). Ví dụ: vận tốc gió $$ v(x,y,z) $$, lực $$ F(x,y,z) $$, điện trường $$ E(x,y,z) $$.

Với $$ f $$ (vô hướng), ta dùng **gradient** vì gradient biến một số thành một vector chỉ hướng. Với $$ F $$ (vector), ta dùng **divergence** và **curl** vì chúng đo "hành vi" của vector.

**Gradient**: Cho $$ f(x,y,z) $$ (vô hướng), ta có $$\nabla f = \left(\partial f/\partial x, \partial f/\partial y, \partial f/\partial z\right)$$. Gradient là vector chỉ hướng tăng nhanh nhất của $$ f $$.

![Gradient: hướng tăng nhanh nhất]({{ site.imgurl }}/chapter_img/chapter00/00_10_gradient.svg)

**Divergence**: Cho $$ F = (P, Q, R) $$ (vector), ta có $$\nabla \cdot F = \partial P/\partial x + \partial Q/\partial y + \partial R/\partial z$$. Divergence là đại lượng vô hướng đo "lưu lượng ra" tại một điểm.

![Divergence: nguồn và bể]({{ site.imgurl }}/chapter_img/chapter00/00_10_divergence.svg)

**Curl**: Cho $$ F = (P, Q, R) $$ (vector), ta có $$\nabla \times F = \left(\partial R/\partial y - \partial Q/\partial z,\partial P/\partial z - \partial R/\partial x,\partial Q/\partial x - \partial P/\partial y\right)$$. Curl là vector đo mức độ xoay của trường.

![Curl: hiện tượng xoáy]({{ site.imgurl }}/chapter_img/chapter00/00_10_curl.svg)

### Định lý Green

**Ý nghĩa**: Định lý Green nối tích phân đường dọc theo đường cong kín $$ C $$ (biên 1D) với tích phân kép trên miền $$ D $$ (miền 2D bên trong). Công thức:
$$\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA$$

![Định lý Green]({{ site.imgurl }}/chapter_img/chapter00/00_10_green_theorem.svg)

**Giải thích trực quan**: Hãy tưởng tượng bạn đi bộ dọc theo bờ hồ (đường cong kín $$ C $$) và muốn tính tổng công sức bạn bỏ ra. Thay vì đi từng bước một quanh bờ, bạn có thể đo diện tích hồ $$ D $$ rồi tính "độ xoắn" của nước tại mỗi điểm trong hồ. Định lý Green nói: **Tổng công trên đường biên = Tích phân độ xoắn trên toàn miền**.

**Điều kiện áp dụng**: Miền $$ D $$ có biên $$ C $$ trơn từng khúc, đường cong đi theo một chiều (ngược kim đồng hồ).

**Ví dụ**: Tính $$ \oint_C (y\,dx + x^2 y^2\,dy) $$ với $$ C $$ là đường tròn đơn vị theo chiều dương. Áp dụng Green với $$ P = y $$, $$ Q = x^2 y^2 $$, ta có:
$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2xy^2 - 1$$

Dùng tọa độ cực: $$ x = r\cos\theta, y = r\sin\theta, dA = r\,dr\,d\theta $$, tích phân trên đĩa đơn vị $$ 0 \leq r \leq 1, 0 \leq \theta \leq 2\pi $$:
$$\iint_D (2xy^2 - 1)\,dA = \int_0^{2\pi}\int_0^1 (2r^2\cos\theta\sin^2\theta - 1)r\,dr\,d\theta = -\pi$$

### Định lý Stokes

**Ý nghĩa**: Định lý Stokes nối tích phân đường dọc theo đường cong kín $$ \partial S $$ (biên 1D của mặt) với tích phân mặt của curl trên mặt $$ S $$ (mặt 2D). Công thức:
$$\oint_{\partial S} F\cdot dr = \iint_S (\nabla \times F)\cdot n\,dS$$

![Định lý Stokes]({{ site.imgurl }}/chapter_img/chapter00/00_10_stokes_theorem.svg)

**Giải thích trực quan**: Giống như Green nhưng trong không gian 3D. Hãy tưởng tượng một cánh buồm (mặt cong $$ S $$) căng trên cột. Gió thổi qua cánh buồm tạo ra lực $$ F $$. Công của gió dọc theo cạnh cánh buồm (đường cong kín $$ \partial S $$) bằng tổng lượng xoáy (curl) của gió xuyên qua toàn bộ cánh buồm. Định lý Stokes: **Tổng công trên đường biên = Tích phân curl xuyên qua mặt**.

**Điều kiện áp dụng**: Mặt $$ S $$ trơn hoặc trơn từng khúc, có biên $$ \partial S $$ trơn, vector pháp $$ n $$ nhất quán.

**Ví dụ**: Tính $$ \oint_{\partial S} F\cdot dr $$ với $$ F = (-y, x, 0) $$ và $$ S $$ là nửa mặt cầu trên $$ z \geq 0 $$. Ta có $$ \nabla \times F = (0, 0, 2) $$. Vì $$ n \cdot (0,0,2) = 2\cos\gamma $$ (với $$ \gamma $$ là góc giữa pháp vector và trục $$ z $$), tích phân mặt trên nửa mặt cầu cho kết quả $$ 4\pi $$.

### Định lý Gauss (Divergence)

**Ðịnh lý Gauss** nối tích phân mặt trên biên $$ \partial S $$ (mặt 2D) với tích phân ba lớp trên miền $$ V $$ (miền 3D). Công thức:
$$\iiint_V (\nabla \cdot F)\,dV = \iint_{\partial S} F\cdot n\,dS$$

![Định lý Gauss]({{ site.imgurl }}/chapter_img/chapter00/00_10_gauss_theorem.svg)

**Giải thích trực quan**: Hãy tưởng tượng bạn có một nguồn nước phun ra trong một cái hồ chứa (miền $$ V $$). Tổng lượng nước chảy ra khỏi toàn bộ mặt bao quanh hồ (biên $$ \partial S $$) bằng tổng "cường độ nguồn" tại mọi điểm bên trong hồ. Định lý Gauss: **Tổng lượng chảy qua mặt biên = Tích phân divergence bên trong thể tích**.

**Điều kiện áp dụng**: Miền $$ V $$ có biên $$ \partial S $$ trơn từng khúc, trường $$ F $$ liên tục có đạo hàm liên tục trên $$ V $$.

**Ví dụ**: Tính thông lượng của $$ F = (x, y, z) $$ qua mặt cầu đơn vị $$ x^2 + y^2 + z^2 = 1 $$. Phương pháp trực tiếp: trên mặt cầu, $$ n = (x, y, z) $$, nên $$ F\cdot n = x^2 + y^2 + z^2 = 1 $$. Diện tích mặt cầu đơn vị là $$ 4\pi $$, nên $$ \iint_{\partial S} F\cdot n\,dS = 4\pi $$.

Dùng Gauss: $$ \nabla \cdot F = \partial x/\partial x + \partial y/\partial y + \partial z/\partial z = 3 $$. Thể tích quả cầu đơn vị là $$ 4\pi/3 $$, nên $$ \iiint_V 3\,dV = 3 \cdot (4\pi/3) = 4\pi $$. Hai cách cho kết quả giống nhau.

## Những ngộ nhận thường gặp
- "Gradient là số." Không đúng. Gradient là vector có hướng, không chỉ là độ lớn.
- "Divergence và curl giống nhau." Không đúng. Divergence là vô hướng, cho biết có nguồn/bể không. Curl là vector, cho biết có xoáy không.
- "Định lý Green chỉ áp dụng cho đường tròn." Sai. Định lý Green áp dụng cho mọi miền D có biên C trơn từng khúc, không nhất thiết là hình tròn.
- "Curl $$ F = 0 $$ thì $$ F $$ là trường thế." Điều này chưa đủ nếu thiếu điều kiện miền đơn liên. Ví dụ $$ F = \left(-y/(x^2+y^2), x/(x^2+y^2)\right) $$ có curl bằng $$ 0 $$ nhưng không có thế trên toàn mặt phẳng trừ gốc.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu ba phép toán qua ý nghĩa vật lý
Gradient: hướng tăng nhanh nhất. Divergence: nguồn/bể. Curl: xoáy. Vẽ nhiều trường vector để "thấy" ý nghĩa.

### Bước 2: Học công thức và cách tính
Ghi nhớ công thức và luyện tập với các trường vector cụ thể. Chú ý thứ tự đạo hàm trong công thức curl.

### Bước 3: Hiểu ba định lý tích phân
Nhận ra ba định lý đều nối tích phân trên "biên" với tích phân trên "miền". Green: biên một chiều $$ \Rightarrow $$ miền hai chiều. Stokes: biên hai chiều $$ \Rightarrow $$ mặt hai chiều. Gauss: biên hai chiều $$ \Rightarrow $$ miền ba chiều.

### Các checkpoint
- Sinh viên có tính được gradient, divergence, curl của các trường cơ bản không?
- Sinh viên có phát biểu và vận dụng được ba định lý không?
- Sinh viên có hiểu ý nghĩa vật lý của mỗi phép toán không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tính gradient
Cho $$ f(x,y,z) = xyz^2 + x^2 z $$. Khi đó $$ \partial f/\partial x = yz^2 + 2xz $$, $$ \partial f/\partial y = xz^2 $$, $$ \partial f/\partial z = xy^2 + x^2 $$. Vậy

$$
\nabla f = \left(yz^2 + 2xz, xz^2, xy^2 + x^2\right).
$$

Tại điểm $$ \left(1,1,1\right) $$, ta được $$ \nabla f = (3,1,2) $$.

### Ví dụ 2: Tính divergence và curl
Cho $$ F = (x^2 y, yz^2, zx^2) $$. Khi đó

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
= \left(-y^2,-x^2,-x^2\right).
$$

Tại $$ \left(1,1,1\right) $$, divergence bằng $$ 4 $$ và curl bằng $$ (-1,-1,-1) $$.

### Ví dụ 3: Áp dụng định lý Green
Tính $$ \oint_C \left(y\,dx + x^2 y^2\,dy\right) $$ với $$ C $$ là đường tròn đơn vị theo chiều dương. Theo Green,

$$
\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dA.
$$

Ở đây $$ P = y $$, $$ Q = x^2 y^2 $$, nên $$\partial Q/\partial x - \partial P/\partial y = 2xy^2 - 1$$. Dùng tọa độ cực trên đĩa đơn vị, ta thu được giá trị cuối cùng là $$ -\pi $$.

### Ví dụ 4: Kiểm tra trường thế
Cho $$ F = (2xy + z^3, x^2, 3xz^2) $$. Ta tính được $$ \nabla \times F = (0,0,0) $$. Vì miền đang xét là toàn $$ \mathbb{R}^3 $$, một miền đơn liên, nên $$ F $$ là trường thế. Từ $$ \partial f/\partial x = 2xy + z^3 $$, ta suy ra một thế là $$ f = x^2 y + xz^3 + C $$.

### Ví dụ 5: Áp dụng trong PDE - phương trình Laplace
Hàm điều hòa thỏa mãn $$ \nabla^2 f = 0 $$, với $$\nabla^2 = \partial^2/\partial x^2 + \partial^2/\partial y^2 + \partial^2/\partial z^2$$ là toán tử Laplace. Nếu $$ f = x^2 - y^2 - z^2 $$, thì $$ \nabla^2 f = 2 - 2 - 2 = -2 \neq 0 $$, nên không điều hòa. Nếu $$ f = 1/\sqrt{x^2+y^2+z^2} $$, thì $$ \nabla^2 f = 0 $$ trên $$ \mathbb{R}^3 \setminus \{0\} $$.

## Câu hỏi khái niệm
1. Tại sao gradient, divergence, và curl lại quan trọng trong vật lý toán? Cho ví dụ về ứng dụng trong cơ học chất lỏng hoặc điện từ học.
2. Ba định lý Green, Stokes, Gauss có điểm gì chung? Tại sao chúng được gọi là các định lý "biên-miền"?
3. Điều kiện để một trường vector có thế là gì? Tại sao cần thêm điều kiện về miền?

## Bài toán ứng dụng
1. **Vật lý - Điện trường**: Trường điện $$ E = -\nabla V $$ với $$ V $$ là thế điện. Nếu $$ V = k/r $$, tính $$ E $$. Tại sao divergence của $$ E $$ liên quan đến mật độ điện tích?
2. **Cơ học chất lỏng**: Trường vận tốc của chất lỏng không nén được có divergence bằng $$ 0 $$. Giải thích ý nghĩa vật lý.
3. **Nhiệt học**: Phương trình truyền nhiệt $$ \partial u/\partial t = \alpha \nabla^2 u $$. Tại sao $$ \nabla^2 u $$ xuất hiện? Ý nghĩa của mỗi số hạng là gì?

## Chiến lược giảng dạy tương tác
- **Hoạt động "Vẽ trường"**: Cho sinh viên vẽ trường vector $$ F = (y,-x) $$ và $$ F = (x,y) $$. So sánh divergence và curl của mỗi trường.
- **Thảo luận nhóm**: Mỗi nhóm tính $$ \nabla \cdot F $$ và $$ \nabla \times F $$ cho một trường cho trước, rồi giải thích ý nghĩa vật lý.
- **Câu đố nhanh**: "Trường nào có divergence bằng $$ 0 $$ nhưng curl khác $$ 0 $$: $$ (x,y) $$, $$ (-y,x) $$, hay $$ (x^2,y^2) $$?".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Tập trung vào ý nghĩa hình học và vật lý trước, công thức sau.
- Vẽ nhiều trường vector để trực quan hóa.
- Luyện tập với các trường đơn giản trước.

### Thử thách cho sinh viên khá giỏi
- Nghiên cứu và chứng minh một trong ba định lý.
- Tìm hiểu về toán tử Laplace-Beltrami và mở rộng lên đa tạp.
- Ứng dụng: phương trình Navier-Stokes và vai trò của divergence, curl.

## Tóm tắt dễ nhớ
**Gradient $$ \nabla f $$**: Vector chỉ hướng tăng nhanh nhất, vuông góc với đường mức.
**Divergence $$ \nabla \cdot F $$**: Vô hướng đo nguồn hoặc bể.
**Curl $$ \nabla \times F $$**: Vector đo xoáy.
**Green**: $$\oint_C = \iint_D \left(\partial Q/\partial x - \partial P/\partial y\right)$$.
**Stokes**: $$\oint_{\partial S} = \iint_S \left(\nabla \times F\right)\cdot n$$.
**Gauss**: $$ \iiint_V = \iint_{\partial S} F\cdot n $$.
Ba định lý nối biên với miền: "Tổng trên biên = tích phân bên trong nhân với độ cong."

## Tài liệu tham khảo
- Marsden & Tromba — *Vector Calculus*: giáo trình chuẩn về giải tích vector.
- Griffiths — *Introduction to Electrodynamics*: ứng dụng điện từ học.
- Strauss — *Partial Differential Equations*: liên hệ trực tiếp với PDE.
