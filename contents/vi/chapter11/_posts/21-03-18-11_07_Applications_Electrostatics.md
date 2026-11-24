---
layout: post
title: "Ứng Dụng: Tĩnh Điện Học"
chapter: '11'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---

![21 03 18 11 07 Applications Electrostatics]({{ site.imgurl }}/chapter_img/chapter11/07_applications_electrostatics.svg)

Mỗi chiếc tụ điện trên bo mạch chủ, lồng Faraday chống sét cho máy bay hay ống cáp đồng trục dẫn tín hiệu Internet đều được thiết kế bằng chính những công cụ bạn vừa học trong Chương 11. Khi điện tích đứng yên, trường tĩnh điện $\mathbf{E}$ hoàn toàn không xoáy ($\nabla \times \mathbf{E} = \mathbf{0}$), nên mọi thông tin của trường vector 3 chiều thu gọn vào một hàm thế vô hướng duy nhất $\varphi$ thỏa mãn phương trình Poisson $-\Delta \varphi = \rho / \varepsilon_0$!

## Bản đồ kiến thức nền: Bốn trụ cột kết nối PDE Elliptic với Tĩnh điện học

1. **Từ Định luật Gauss đến Phương trình Poisson & Laplace**:
   Kết hợp $\mathbf{E} = -\nabla \varphi$ với $\nabla \cdot \mathbf{E} = \rho / \varepsilon_0$ cho ra $-\Delta \varphi = \rho / \varepsilon_0$ (Poisson) trong vùng có điện tích và $\Delta \varphi = 0$ (Laplace) trong không gian điện môi trống.
2. **Vật dẫn ở Cân bằng = Điều kiện biên Dirichlet hằng số**:
   Trên bề mặt kim loại dẫn điện, điện thế $\varphi = V_0$ là hằng số (mặt đẳng thế), điện trường luôn vuông góc với bề mặt và mật độ điện tích cảm ứng tỷ lệ với đạo hàm pháp tuyến $\sigma = -\varepsilon_0 \frac{\partial \varphi}{\partial n}$.
3. **Nguyên lý Cực đại & Hiện tượng Che chắn Lồng Faraday**:
   Bên trong một khoang rỗng hoàn toàn bao bọc bởi vật dẫn ở thế $V_0$ không chứa điện tích, $\Delta \varphi = 0$ và $\varphi|_{\partial\Omega} = V_0 \implies \varphi \equiv V_0$ mọi nơi bên trong, suy ra $\mathbf{E} = -\nabla \varphi = \mathbf{0}$—bất kể ngoài lồng có điện trường mạnh cỡ nào!
4. **Năng lượng Tĩnh điện và Nguyên lý Dirichlet**:
   Năng lượng trường điện $W = \frac{\varepsilon_0}{2}\int_\Omega |\nabla \varphi|^2\,dx$ đạt giá trị **nhỏ nhất có thể** tại đúng nghiệm của phương trình Laplace—tự nhiên luôn chọn cấu hình thế tiết kiệm năng lượng nhất.

## Mục tiêu

Bài học này đặt phương trình Laplace và phương trình Poisson vào bối cảnh tĩnh điện học — một ứng dụng kinh điển của PDE elliptic. Sau bài học, sinh viên cần nắm mối liên hệ giữa điện thế và điện trường, hiểu vì sao điện thế thỏa mãn phương trình Laplace hay phương trình Poisson tùy theo sự có mặt của điện tích, nhận ra vai trò của điều kiện biên trên bề mặt vật dẫn, và thấy cách năng lượng điện trường kết nối vật lý với phân tích toán học.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace, phương trình Poisson, toán tử gradient và ý niệm hàm Green ở mức trực giác. Bài học này cho thấy các nội dung toán học của chương gắn kết trực tiếp với các mô hình vật lý.

## Dẫn nhập

Trong tĩnh điện học, ta không quan sát trực tiếp điện trường bằng mắt thường, nhưng tác dụng của nó thể hiện rõ qua lực tương tác, điện thế và năng lượng tích trữ trong phân bố điện tích. Toàn bộ cấu trúc đó được mô tả gọn bằng một PDE elliptic: trong vùng không có điện tích, điện thế là hàm điều hòa; trong vùng có điện tích, điện thế thỏa mãn phương trình Poisson.

Bài học này cho thấy PDE không chỉ là công cụ giải tích mà còn là ngôn ngữ mô tả trực tiếp trường vật lý: điện thế, điện trường, năng lượng và điều kiện biên của vật dẫn đều liên kết trong cùng một cấu trúc toán học.


### Khung giải thích (nên đọc chậm): Tính tay phân bố điện thế và cường độ điện trường trong cáp đồng trục

Xét một đoạn cáp đồng trục dài có lõi trong bán kính $a = 1\text{ cm}$ giữ ở hiệu điện thế $V(a) = 100\text{ V}$ và vỏ ngoài nối đất bán kính $b = e \approx 2{,}718\text{ cm}$ với $V(b) = 0\text{ V}$:
1. **Giải phương trình Laplace đối xứng trụ** $\frac{1}{r}\frac{d}{dr}(r V'(r)) = 0$:
   $$r V'(r) = A \implies V(r) = A\ln r + B.$$
2. **Xác định hằng số từ hai biên Dirichlet**:
   - $V(1) = A\ln 1 + B = 100 \implies B = 100$.
   - $V(e) = A\ln e + 100 = 0 \implies A = -100$.
   Vậy điện thế giữa hai lớp là $V(r) = \mathbf{100(1 - \ln r)}\text{ V}$.
3. **Tính cường độ điện trường $E(r) = -V'(r) = \frac{100}{r}\text{ V/cm}$**:
   - Tại sát lõi trong ($r = 1\text{ cm}$): $E(1) = \mathbf{100\text{ V/cm}}$ (cực đại—đây là nơi lớp cách điện dễ bị đánh thủng nhất!).
   - Tại sát vỏ ngoài ($r = e\text{ cm}$): $E(e) \approx \mathbf{36{,}8\text{ V/cm}}$.
## Khái niệm theo ba cách

### Cách nhìn trực quan

Điện thế có thể hình dung như một bề mặt thế năng, trong đó điện tích thử có xu hướng di chuyển theo chiều dốc xuống của bề mặt. Khi không có điện tích bên trong vùng xét, bề mặt thế năng chỉ chịu sự chi phối của biên; khi có nguồn điện tích, bề mặt bị uốn cong ngay từ bên trong. Đó là trực giác của phương trình Laplace và phương trình Poisson trong tĩnh điện.

### Cách nhìn hình ảnh

Các đường đẳng thế tương tự như các đường đồng mức trên bản đồ địa hình, còn điện trường vuông góc với các đường đẳng thế và hướng theo chiều giảm nhanh nhất của điện thế. Gần điện tích điểm, các đường đẳng thế nằm sát nhau hơn, biểu thị điện trường mạnh hơn. Đối với vật dẫn, bề mặt vật dẫn áp đặt giá trị điện thế trên biên và buộc trường bên trong sắp xếp tương thích.

### Cách nhìn hình thức

Điện thế $$ V $$ thỏa mãn phương trình:

$$ \Delta V=-\frac{\rho}{\varepsilon_0}, $$

trong đó $$ \rho $$ là mật độ điện tích. Khi $$ \rho=0 $$, ta thu được $$ \Delta V=0 $$. Điện trường được tính bằng $$ \mathbf E=-\nabla V $$, và năng lượng điện trường có dạng:

$$
W=\frac{\varepsilon_0}{2}\int \lvert \nabla V\rvert^2\,dx.
$$

## Những ngộ nhận thường gặp

- "Điện thế và điện trường là hai đại lượng độc lập." Không đúng; điện trường được xác định trực tiếp từ gradient của điện thế.
- "Vùng không có điện tích thì không có gì đáng khảo sát." Sai; chính vùng không nguồn là nơi lý thuyết hàm điều hòa thể hiện đầy đủ vai trò.
- "Điều kiện biên của vật dẫn chỉ là dữ kiện kỹ thuật phụ." Không đúng; chúng phản ánh trực tiếp cấu hình vật lý và quyết định trường điện trong miền.
- "Năng lượng điện trường chỉ là khái niệm phụ trợ." Sai; biểu thức năng lượng kết nối trực tiếp với các nguyên lý biến phân và giải tích PDE.

## Tiến trình học tập đề xuất

### Bước 1: Xem điện thế là đại lượng trung tâm

Từ phân bố điện thế có thể suy ra ngay điện trường.

### Bước 2: Phân biệt vùng có điện tích và vùng không có điện tích

Đây là ranh giới phân tách giữa phương trình Laplace và phương trình Poisson.

### Bước 3: Hiểu vai trò của vật dẫn và điều kiện biên

Nhận diện cách bề mặt vật dẫn áp đặt điều kiện biên vật lý lên bài toán.

### Bước 4: Liên hệ với năng lượng điện trường và hàm Green

Hoàn thiện bức tranh liên kết giữa vật lý và công cụ giải tích.

### Các checkpoint

- Sinh viên có giải thích được vì sao vùng không có điện tích dẫn đến phương trình Laplace hay không.
- Sinh viên có biết cách suy ra điện trường từ điện thế hay không.
- Sinh viên có hiểu điều kiện biên của vật dẫn chi phối cấu trúc trường như thế nào hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Điện tích điểm

Trong không gian ba chiều, điện thế do một điện tích điểm $$ q $$ đặt tại gốc tọa độ tạo ra là:

$$ V(x)=\frac{q}{4\pi\varepsilon_0\lvert x\rvert}. $$

Đây là nghiệm cơ bản vật lý tiêu biểu của chương.

### Ví dụ 2: Vùng không có điện tích

Khi $$ \rho=0 $$ trong một miền, ta có $$ \Delta V=0 $$, nên điện thế bên trong miền hoàn toàn bị chi phối bởi giá trị trên biên. Ví dụ này nhấn mạnh vai trò của hàm điều hòa trong tĩnh điện học.

### Ví dụ 3: Hai bản cực song song

Giữa hai bản cực phẳng song song lý tưởng, điện thế biến thiên tuyến tính theo phương vuông góc với hai bản. Đây là ví dụ một chiều trực quan cho bài toán Dirichlet của phương trình Laplace.

### Ví dụ 4: Phương pháp ảnh

Một điện tích điểm đặt gần mặt phẳng dẫn điện có thể được khảo sát bằng cách thay mặt dẫn bằng một điện tích ảnh đối xứng. Ví dụ này kết nối trực tiếp ứng dụng tĩnh điện với kỹ thuật xây dựng hàm Green.

## Câu hỏi khái niệm

1. Vì sao giải phương trình cho điện thế thường thuận tiện hơn giải trực tiếp cho điện trường?
2. Tại sao vật dẫn và điều kiện biên trên bề mặt của nó lại giữ vai trò quyết định trong tĩnh điện học?
3. Vì sao năng lượng điện trường có thể biểu diễn qua tích phân $$ \int \lvert \nabla V\rvert^2 $$?

## Bài toán ứng dụng

1. Trong một vùng không có điện tích nhưng có các vật dẫn áp đặt điện thế trên biên, vì sao phân bố điện trường bên trong vẫn có thể rất phức tạp?
2. Vì sao điện trường mạnh hơn tại những vùng có các đường đẳng thế xếp dày đặc hơn?
3. Trong thiết kế tụ điện, vì sao hình học của các bản cực ảnh hưởng trực tiếp đến phân bố điện trường và năng lượng tích trữ?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu đã biết điện thế trên toàn miền, ta cần thực hiện phép toán nào để suy ra điện trường?"
- Cho sinh viên so sánh hai vùng — một có điện tích và một không có điện tích — rồi xác định PDE tương ứng cho từng vùng.
- Hỏi cả lớp: "Tại sao một điện tích ảnh lại có thể thay thế cho cả một mặt phẳng dẫn điện trong một số bài toán?"
- Khuyến khích sinh viên liên hệ đường đẳng thế và chiều điện trường với hình ảnh đường đồng mức địa hình.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào ba công thức cốt lõi:

$$
\Delta V=-\rho/\varepsilon_0,\qquad \mathbf E=-\nabla V,
\qquad
W=\frac{\varepsilon_0}{2}\int \lvert \nabla V\rvert^2.
$$

Khi đã nắm vững ba biểu thức này, việc liên kết các nội dung còn lại sẽ thuận lợi hơn.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi tìm hiểu sâu hơn về phương pháp ảnh, hoặc phân tích cách nguyên lý cực tiểu hóa năng lượng dẫn đến bài toán Dirichlet trong tĩnh điện học.

## Tóm tắt dễ nhớ

Tĩnh điện học là ứng dụng tiêu biểu của phương trình Laplace và phương trình Poisson. Điện thế thỏa mãn PDE elliptic, điện trường bằng âm gradient của điện thế, và năng lượng trường tỷ lệ với tích phân bình phương độ lớn gradient. Điều kiện biên trên vật dẫn cùng phân bố điện tích xác định toàn bộ cấu trúc trường.

## Video tham khảo

- xem trước: [Lecture 4: Electrostatic potential, Poisson's Equation, Laplace's Equation, Green's functions](https://www.youtube.com/watch?v=Z0-AkSfMJYU) — rkingery, tiếng Anh. Trình bày điện thế tĩnh điện như nghiệm của phương trình Poisson và Laplace.
- [Divergence and curl:  The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) — 3Blue1Brown, tiếng Anh. Minh họa trực quan cấu trúc trường không xoáy và khái niệm thế trong điện từ học Maxwell.
- [Laplace's Equation and Poisson's Equation](https://www.youtube.com/watch?v=nmvs0vrBT18) — Steve Brunton, tiếng Anh. Phân biệt phương trình Laplace và phương trình Poisson theo sự có mặt của điện tích.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Trường điện quanh dây dẫn
- Bài toán: Tính điện thế và điện trường xung quanh các điện cực ở trạng thái tĩnh.
- Mô hình: $$ \Delta \phi=0 $$ trong vùng không có điện tích, hoặc $$ -\Delta \phi=\rho/\varepsilon $$ khi có nguồn điện tích.
- Giả thiết và giới hạn: Trường tĩnh điện, môi trường đồng nhất.
- Diễn giải: Các đường đẳng thế và đường sức điện phản ánh hình học của nghiệm elliptic.

#### Cáp đồng trục
- Bài toán: Xác định điện thế giữa hai hình trụ đồng tâm để tính điện trường và điện dung hiệu dụng.
- Mô hình: Trong tọa độ trụ, nghiệm chỉ phụ thuộc vào bán kính.
- Giả thiết và giới hạn: Đối xứng trụ lý tưởng, bỏ qua hiệu ứng đầu mút.
- Diễn giải: Một bài toán kỹ thuật quen thuộc có nghiệm dạng logarit đặc trưng.

### 2. Trực giác bổ sung và các kết nối

Điện thế điều hòa là ví dụ chuẩn của hàm trơn bị ràng buộc chặt bởi dữ liệu biên. Các kết quả định tính như nguyên lý cực đại và tính chất giá trị trung bình đều mang ý nghĩa vật lý rõ ràng trong điện từ học.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 220)
y = np.linspace(-2, 2, 220)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) + 1e-6
Phi = np.log(R)

plt.contour(X, Y, Phi, levels=20)
plt.axis("equal")
plt.title("Duong dang the xung quanh nguon doi xung tron")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: electrostatic potential contour plot Laplace equation
- search: coaxial cable Laplace equation solution
- search: equipotential lines electric field visualization

### 5. Bài toán mẫu có bối cảnh thực

Cho hai bán kính $$ a<b $$, nghiệm điện thế trong cáp đồng trục với điều kiện $$ \phi(a)=V_0 $$ và $$ \phi(b)=0 $$ là:
$$ \phi(r)=V_0\frac{\ln(b/r)}{\ln(b/a)}. $$
Thành phần điện trường hướng tâm được tính bởi $$ E_r=-\phi_r $$. Dạng hàm logarit là đặc trưng của bài toán có đối xứng trụ.

### 6. Phân tầng độ khó

**Bậc đại học.** Giải thích vì sao phân bố điện thế bị quyết định bởi điều kiện biên.

**Bậc sau đại học.** Kết nối với khái niệm điện dung, điều kiện biên hỗn hợp và bài toán ngược trong đo điện trở suất.
