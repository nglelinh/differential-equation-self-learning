---
layout: post
title: "Toán Tử Dirac: Xuất Phát, Tính Chất, và Các Định Lý Cốt Lõi"
chapter: '15'
order: 10
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
---

![Toan tu Dirac va cac cau noi giua vat ly, hinh hoc, va topology]({{ site.imgurl }}/chapter_img/chapter15/10_dirac_operators.svg )

## Mục tiêu

Bài optional này đưa toán tử Dirac vào Chương 15 như một ví dụ trung tâm nơi PDE, hình học vi phân, cơ học lượng tử và topology chạm nhau. Sau bài học, sinh viên cần hiểu vì sao Dirac operator xuất hiện từ nhu cầu tìm một “căn bậc hai bậc nhất” của Laplacian hay Klein-Gordon operator, biết mô tả nó bằng ngôn ngữ Clifford multiplication và spinor bundle, nắm các tính chất cơ bản như tính elliptic, tự liên hợp hình thức và công thức bình phương, đồng thời nhận ra vai trò của các định lý kiểu Lichnerowicz, elliptic regularity và Atiyah-Singer index theorem.

## Kiến thức nền

Sinh viên nên nắm toán tử elliptic, principal symbol, regularity vi địa phương, Fourier transform, không gian Hilbert, và trực giác cơ bản về spinor hay ít nhất về differential forms. Nếu chưa học spin geometry một cách đầy đủ, sinh viên vẫn có thể theo bài này bằng cách xem Hodge-Dirac operator $$d+d^*$$ như mô hình cửa ngõ trước khi đi sang geometric Dirac operator trên spin manifold.

## Dẫn nhập

Trong nhiều chương trước, ta đã thấy các toán tử bậc hai như Laplacian, wave operator, và Schrödinger operator. Chúng là nhân vật chính của PDE cổ điển. Nhưng khi toán học và vật lý cùng tiến sâu hơn, một câu hỏi tự nhiên xuất hiện: có thể xây dựng một toán tử bậc nhất mà bình phương của nó tạo ra một toán tử kiểu Laplace hay không? Nếu làm được như vậy, ta sẽ có một đối tượng tinh hơn, nhạy hơn với hình học, và thường mang nhiều cấu trúc đối xứng hơn.

Đó chính là nơi toán tử Dirac xuất hiện. Trong vật lý, Dirac tìm kiếm một phương trình relativistic cho electron vừa bậc nhất theo thời gian, vừa bậc nhất theo không gian, thay vì dùng phương trình Klein-Gordon bậc hai. Trong hình học, người ta nhận ra rằng có cả một họ toán tử “kiểu Dirac” được xây trên Clifford algebra và connection tương thích, với tính chất bình phương của chúng tạo ra Laplace-type operator cộng thêm các số hạng cong. Từ đây, Dirac operator trở thành cây cầu đẹp hiếm có giữa giải tích, hình học và topology.

Với một khóa học về phương trình vi phân nâng cao, Dirac operator quan trọng không phải vì nó thêm một ví dụ lạ, mà vì nó cho thấy một bài học lớn hơn: những toán tử first-order elliptic mới là nơi cấu trúc hình học sâu thường lộ ra rõ nhất. Laplacian cho ta regularity và phổ; Dirac operator cho ta những thông tin ấy cùng với spin structure, curvature, index và đôi khi cả nội dung vật lý của spin-$$\frac12$$.

## Xuất phát của toán tử Dirac

Có hai con đường xuất phát rất đáng nhớ.

Con đường thứ nhất đến từ vật lý relativistic. Phương trình Klein-Gordon có dạng

$$
\left(\partial_t^2-\Delta_x+m^2\right)\psi=0,
$$

là mô hình relativistic bậc hai. Dirac muốn một phương trình bậc nhất theo cả thời gian lẫn không gian để diễn tả tốt hơn động học của electron và tự nhiên chứa spin. Ý tưởng then chốt là factor hóa biểu thức bậc hai bằng các ma trận thỏa quan hệ phản giao hoán. Chính quan hệ ấy mở cánh cửa vào Clifford algebra.

Con đường thứ hai đến từ hình học. Trên differential forms, toán tử

$$
D_{\mathrm{dR}}=d+d^*
$$

là một toán tử bậc nhất rất tự nhiên, và ta có

$$
D_{\mathrm{dR}}^2=\Delta_H,
$$

trong đó $$\Delta_H$$ là Hodge Laplacian. Đây là ví dụ đầu tiên cho trực giác “Dirac squared gives Laplace”. Khi spin geometry phát triển, mô hình này được tổng quát hóa sang spinor bundle với Clifford multiplication, tạo ra geometric Dirac operator quen thuộc của hình học vi phân hiện đại.

Vì thế, nếu nhìn từ góc độ PDE, toán tử Dirac không phải một phát minh tách biệt. Nó là câu trả lời cho nhu cầu factor hóa toán tử bậc hai, giữ lại ellipticity, và đưa thêm cấu trúc hình học vào chính toán tử vi phân.

## Khái niệm theo ba cách

### Cách trực giác

Hãy xem Laplacian như công cụ đo độ cong bậc hai của một trường, còn Dirac operator như công cụ “đạo hàm có định hướng và có spin”. Nó vừa là derivative, vừa nhớ được cách các thành phần của spinor xoay và tương tác với hình học xung quanh. Vì là toán tử bậc nhất, nó nhạy hơn với cấu trúc vi mô; vì bình phương của nó tạo ra một toán tử kiểu Laplace, nó vẫn thừa hưởng sức mạnh elliptic của PDE bậc hai.

### Cách hình ảnh

Một hình rất nên vẽ trên lớp là tam giác nối ba đỉnh: vật lý, hình học, topology. Ở đỉnh vật lý là “relativistic electron”; ở đỉnh hình học là “spin connection và Clifford multiplication”; ở đỉnh topology là “index”. Toán tử Dirac nằm ở giữa. Từ nó, một mũi tên đi xuống công thức $$D^2=\nabla^*\nabla+\text{curvature term}$$; một mũi tên khác đi sang định lý index, cho thấy dữ kiện phân tích của toán tử có thể phản ánh bất biến toàn cục của manifold.

### Cách hình thức

Cho một không gian Euclid với cơ sở trực chuẩn $$e_1,\dots,e_n$$. Một biểu diễn Clifford là một phép gán $$v\mapsto c(v)$$ sao cho

$$
c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{Id}.
$$

Nếu $$S$$ là spinor space hay spinor bundle, geometric Dirac operator có dạng

$$
D=\sum_{j=1}^n c(e_j)\nabla_{e_j},
$$

trong đó $$\nabla$$ là connection tương thích. Theo quy ước phân tích thường dùng, principal symbol của $$D$$ là

$$
\sigma_D(x,\xi)=i\,c(\xi).
$$

Vì quan hệ Clifford cho

$$
c(\xi)^2=-|\xi|^2\operatorname{Id},
$$

nên $$\sigma_D(x,\xi)$$ khả nghịch với mọi $$\xi\neq 0$$. Đó là lý do cốt lõi khiến Dirac operator elliptic. Trên không gian phẳng với coefficients hằng, bình phương của $$D$$ cho

$$
D^2=-\Delta \operatorname{Id},
$$

theo quy ước hình học.

## Tính chất cốt lõi

### Bậc nhất nhưng vẫn mang sức mạnh của toán tử bậc hai

Toán tử Dirac là bậc nhất, nên nó gần với động lực học và transport hơn so với Laplacian. Tuy nhiên, vì bình phương của nó là một toán tử kiểu Laplace, nó vẫn thuộc thế giới elliptic regularity. Điều này làm nó trở thành một đối tượng rất đặc biệt: nhạy với cấu trúc tinh nhưng vẫn đủ mạnh để kiểm soát regularity và phổ.

### Tính elliptic

Ellipticity không đến từ phép màu, mà đến trực tiếp từ Clifford relation. Khi $$\xi\neq 0$$, toán tử tuyến tính $$c(\xi)$$ bình phương thành một bội vô hướng của đồng nhất, nên nó phải khả nghịch. Hệ quả là Dirac operator có parametrix, kernel hữu hạn chiều trên compact manifold, và hưởng toàn bộ bộ công cụ của elliptic theory.

### Tự liên hợp hình thức

Với metric Hermitian thích hợp trên spinor bundle và connection tương thích, geometric Dirac operator là formally self-adjoint trên manifold đóng. Điều này rất quan trọng cho phổ: eigenvalues là thực, và ta có thể dùng spectral theory để hiểu nghiệm, dao động và trạng thái lượng tử.

### Cực kỳ nhạy với độ cong

Laplacian trên hàm nhớ hình học qua metric; Dirac operator nhớ thêm spin structure và connection. Điều đó làm cho bình phương của nó không chỉ là Laplacian thô mà còn kèm curvature term. Đây là điểm mở ra các định lý vanishing và index sâu.

## Các định lý trung tâm

### Định lý 1: Ellipticity của Dirac operator

Với một Dirac-type operator $$D$$, principal symbol $$\sigma_D(x,\xi)=i\,c(\xi)$$ khả nghịch với mọi $$\xi\neq 0$$. Vì vậy $$D$$ là elliptic.

Ý nghĩa của định lý này là toàn bộ lý thuyết elliptic regularity quay lại. Nếu $$Du=f$$ và $$f$$ trơn, thì $$u$$ trơn. Trên compact manifold, kernel của $$D$$ hữu hạn chiều, và nếu $$D$$ là self-adjoint thì phổ rời rạc với tích lũy duy nhất ở vô cùng.

### Định lý 2: Công thức Lichnerowicz

Trên spin manifold Riemann đóng,

$$
D^2=\nabla^*\nabla+\frac14\operatorname{Scal}.
$$

Đây là công thức đẹp nhất của chủ đề. Nó nói rằng bình phương của Dirac operator bằng rough Laplacian cộng đúng một phần tư scalar curvature. Công thức này khiến độ cong vô hướng bước thẳng vào giải tích của nghiệm.

Hệ quả nổi tiếng là vanishing theorem: nếu manifold đóng có $$\operatorname{Scal}>0$$ mọi nơi, thì mọi harmonic spinor đều bằng không. Thật ra chỉ cần lấy $$D\psi=0$$, nhân vô hướng và tích phân, ta được tổng của hai số hạng không âm bằng 0.

### Định lý 3: Elliptic regularity và Fredholmness

Nếu $$D$$ là Dirac-type operator trên compact manifold thì

$$
D:H^s(S)\to H^{s-1}(S)
$$

là toán tử Fredholm với mọi $$s$$ thích hợp. Điều này có nghĩa là nhân và đồng nhân hữu hạn chiều, còn lời giải tồn tại modulo một trở ngại hữu hạn chiều.

Ý nghĩa ở đây rất quan trọng cho PDE hiện đại: Dirac operator không chỉ là vật thể hình học đẹp mà còn là một operator analytic “ngoan”, cho phép ta nói nghiêm ngặt về phổ, chỉ số và stability của nghiệm.

### Định lý 4: Atiyah-Singer index theorem cho spin Dirac

Trên compact spin manifold chẵn chiều, spinor bundle tách thành $$S^+\oplus S^-$$ và Dirac operator tách thành

$$
D^+: \Gamma(S^+) \to \Gamma(S^-).
$$

Khi đó

$$
\operatorname{ind}(D^+)=\dim\ker D^+ - \dim\ker (D^+)^*
$$

được cho bởi một bất biến topology, trong trường hợp spin thuần túy là $$\widehat{A}(M)$$. Đây là một trong những khoảnh khắc vĩ đại của toán học thế kỷ XX: dữ kiện giải tích của một PDE first-order elliptic bằng đúng một số topological toàn cục.

## Định lý, bổ đề, và chứng minh trọng tâm

### Định lý: Ellipticity của Dirac operator
Với Dirac operator hình học $$ D $$, principal symbol có dạng
$$
\sigma_D(x,\xi)=i\,c(\xi),
$$
và khả nghịch với mọi $$ \xi\neq 0 $$. Vì thế $$ D $$ là một toán tử elliptic bậc nhất.

### Chứng minh
Quan hệ Clifford đọc trên covector $$\xi$$ là
$$
c(\xi)^2=-|\xi|^2\operatorname{Id}.
$$
Nếu $$\xi\neq 0$$ thì $$|\xi|^2\neq 0$$, nên $$c(\xi)$$ khả nghịch với nghịch đảo tường minh
$$
c(\xi)^{-1}=-\frac{c(\xi)}{|\xi|^2}.
$$
Principal symbol $$\sigma_D(x,\xi)=i\,c(\xi)$$ do đó cũng khả nghịch, với nghịch đảo $$-i\,c(\xi)/|\xi|^2$$. Symbol chính khả nghịch ngoài zero section đúng là định nghĩa ellipticity bậc $$1$$. Hệ quả: Dirac operator có parametrix trong $$\Psi^{-1}$$, và elliptic regularity (Bài 15.09) áp dụng: nếu $$Du$$ trơn thì $$u$$ trơn.

Công thức Lichnerowicz $$D^2=\nabla^*\nabla+\operatorname{Scal}/4$$ là đồng nhất thức của connection tương thích trên spinor bundle, không phải một chứng minh định lý chỉ số. Nó được kiểm bằng cách khai triển $$D^2$$ thành rough Laplacian cộng các số hạng cong Riemann, rồi dùng đồng nhất Bianchi để gom curvature thành $$\operatorname{Scal}/4$$. Định lý Atiyah–Singer không được chứng minh ở đây.

## Ví dụ có lời giải

### Ví dụ 1: Hodge-Dirac operator trên differential forms

Xét

$$
D_{\mathrm{dR}}=d+d^*.
$$

Khi bình phương, các số hạng chéo gộp lại thành

$$
D_{\mathrm{dR}}^2=dd^*+d^*d=\Delta_H.
$$

Ví dụ này là cửa ngõ tốt nhất cho người học chưa quen spinors. Nó cho thấy ý tưởng Dirac không bắt đầu từ những ma trận bí ẩn, mà từ một toán tử bậc nhất tự nhiên có bình phương là Laplacian. Hơn nữa, kernel của $$D_{\mathrm{dR}}$$ chính là các harmonic forms, liên hệ trực tiếp với de Rham cohomology.

### Ví dụ 2: Dirac phẳng trên $$\mathbb{R}^n$$

Trên không gian phẳng với Clifford matrices hằng,

$$
D=\sum_{j=1}^n c(e_j)\partial_{x_j}.
$$

Khi khai triển $$D^2$$, các đạo hàm chéo đi với hệ số

$$
c(e_j)c(e_k)+c(e_k)c(e_j),
$$

nên triệt tiêu khi $$j\neq k$$. Các số hạng đường chéo cho

$$
D^2=\sum_{j=1}^n c(e_j)^2\partial_{x_j}^2
=-\sum_{j=1}^n \partial_{x_j}^2 \operatorname{Id}
=-\Delta \operatorname{Id}.
$$

Đây là phép tính cơ bản nhất của chủ đề: phản giao hoán chính là lý do bình phương của toán tử bậc nhất trở về một đối tượng bậc hai vô hướng.

### Ví dụ 3: Hệ quả của độ cong dương

Giả sử $$M$$ là compact spin manifold và $$D\psi=0$$. Từ công thức Lichnerowicz,

$$
0=\langle D^2\psi,\psi\rangle
=\|\nabla\psi\|^2+\frac14\int_M \operatorname{Scal}\,|\psi|^2.
$$

Nếu $$\operatorname{Scal}>0$$ mọi nơi, cả hai số hạng ở vế phải đều không âm và tổng của chúng bằng 0, nên bắt buộc $$\psi=0$$. Bài toán này rất đáng nhớ vì nó cho thấy một định lý giải tích đơn giản có thể cấm sự tồn tại của một cấu trúc hình học nào đó.

### Ví dụ 4: Mode Fourier trên torus phẳng

Trên torus phẳng, lấy spinor mode

$$
\psi_k(x)=e^{i k\cdot x}u,
$$

với $$k\in \mathbb{Z}^n$$ và $$u$$ là spinor hằng. Khi đó

$$
D\psi_k = i\,c(k)e^{i k\cdot x}u.
$$

Vì eigenvalues của ma trận $$c(k)$$ có độ lớn bằng $$|k|$$, phổ của Dirac operator phản ánh trực tiếp cấu trúc tần số của manifold phẳng. Đây là một ví dụ tốt để nối Dirac operator với Fourier analysis và spectral asymptotics.

## Câu hỏi khái niệm

1. Vì sao trong nhiều bối cảnh toán tử bậc nhất như Dirac lại giàu thông tin hình học hơn toán tử bậc hai?
2. Tại sao quan hệ Clifford $$c(\xi)^2=-|\xi|^2\operatorname{Id}$$ là chìa khóa của ellipticity?
3. Vì sao việc bình phương Dirac operator tạo ra curvature term lại là tín hiệu rằng hình học đã đi thẳng vào giải tích?
4. Vì sao index theorem được xem là một cầu nối giữa PDE và topology hơn là chỉ một công thức đẹp?

## Bài toán ứng dụng

1. Hãy so sánh $$D_{\mathrm{dR}}=d+d^*$$ với Laplacian Hodge và giải thích vì sao bài toán harmonic forms vừa là bài toán PDE vừa là bài toán topology.
2. Trong mô hình electron relativistic, tại sao việc có phương trình bậc nhất lại quan trọng hơn chỉ biết bình phương của nó?
3. Nếu một compact spin manifold có scalar curvature dương mọi nơi, điều này nói gì về harmonic spinors và về chỉ số giải tích của $$D^+$$?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu em chỉ biết $$D^2$$ mà không biết $$D$$, em đã mất đi loại thông tin hình học nào?
- Tại sao một toán tử first-order lại có thể tạo ra cùng loại regularity mà ta hay gắn với Laplacian?
- Theo em, điều gì đáng ngạc nhiên hơn: công thức Lichnerowicz hay index theorem?

### Hoạt động gợi ý

- Cho sinh viên tự nhân $$D=\sum c(e_j)\partial_{x_j}$$ với chính nó để nhìn rõ các số hạng chéo biến mất ra sao.
- Chia lớp thành hai nhóm: một nhóm kể “câu chuyện vật lý” của Dirac, nhóm kia kể “câu chuyện hình học” của Hodge-Dirac và spinors.
- Vẽ sơ đồ kết nối $$D$$, $$D^2$$, curvature, kernel, và index rồi yêu cầu sinh viên diễn giải từng mũi tên bằng lời.

### Cách tăng tham gia

- Bắt đầu bằng câu hỏi “Làm sao lấy căn bậc hai của Laplacian mà vẫn giữ ý nghĩa hình học?”
- Cho sinh viên đoán trước xem tính elliptic đến từ đâu trước khi đưa ra Clifford relation.
- Khuyến khích sinh viên nối bài này với quantum mechanics, microlocal elliptic theory và spectral asymptotics.

## Ghi nhớ nhanh

Toán tử Dirac là toán tử first-order elliptic được xây từ Clifford multiplication và connection tương thích. Nó xuất phát vừa từ nhu cầu vật lý relativistic, vừa từ hình học của differential forms và spinors. Ellipticity đến từ quan hệ phản giao hoán, bình phương của nó tạo ra một toán tử kiểu Laplace cộng thêm curvature term, còn index của nó mở cánh cửa nối PDE với topology toàn cục.

---

## Ứng dụng thực tế

### 1. Cơ học lượng tử relativistic và hạt spin-$$\frac12$$

Dirac equation là mô hình nền cho electron relativistic. Trong ngôn ngữ hiện đại, điều quan trọng không chỉ là phương trình nghiệm, mà còn là cấu trúc operator: first-order, self-adjoint, và có phổ đối xứng theo những điều kiện nhất định. Mô hình giả định thang năng lượng relativistic và bỏ qua tương tác trường lượng tử đầy đủ. Diễn giải của bài học là: spin không phải một chi tiết thêm vào sau, mà nằm trong chính phép factor hóa của toán tử.

### 2. Hình học độ cong và câu hỏi scalar curvature

Lichnerowicz formula làm cho Dirac operator trở thành công cụ để chứng minh các định lý không tồn tại metric có scalar curvature dương trên một số manifold. Ở đây, PDE không chỉ giải một trường vật lý; nó đóng vai trò như một detector của hình học toàn cục. Giả thiết chính là manifold có spin structure và metric đủ trơn.

### 3. Vật liệu Dirac và nón phổ

Trong graphene hay một số topological materials, mô hình hiệu dụng gần điểm Dirac có dispersion relation tuyến tính thay vì bậc hai. Điều đó làm xuất hiện “Dirac cone” trong không gian xung lượng. Mô hình này không phải geometric Dirac operator đầy đủ trên manifold cong, nhưng nó chia sẻ cùng trực giác first-order, spinor-valued, và phổ tuyến tính ở tần số cao hay gần điểm đặc biệt.

## Trực giác sâu hơn

Một cách nghĩ rất hữu ích là: Laplacian đo “mức cong bậc hai” của trường, còn Dirac operator đo “đạo hàm có hướng và có spin”. Vì thế, khi bình phương Dirac operator, ta vừa lấy lại phần khuếch tán kiểu Laplace, vừa không đánh mất thông tin về connection và curvature. Đây là lý do nó được yêu thích trong hình học: nó đủ phân tích để dùng elliptic theory, nhưng đủ nhạy để nhìn thấy topology.

Một ngộ nhận phổ biến là tưởng rằng Dirac operator chỉ là một vật thể vật lý. Thật ra, trong toán học hiện đại, nó là mẫu chuẩn cho cả một lớp Dirac-type operators. Khi hiểu tốt ví dụ này, người học bắt đầu thấy vì sao nhiều định lý sâu của hình học vi phân có dạng “nếu curvature thế này thì kernel của một toán tử Dirac nào đó phải như thế kia”.

## Trực quan hóa bằng Python

Đoạn mã sau vẽ hai nhánh phổ của symbol Dirac phẳng hai chiều có khối lượng $$m$$:

```python
import numpy as np
import matplotlib.pyplot as plt

xi1 = np.linspace(-3, 3, 220)
xi2 = np.linspace(-3, 3, 220)
XI1, XI2 = np.meshgrid(xi1, xi2)
m = 1.0

E = np.sqrt(XI1**2 + XI2**2 + m**2)

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

ax1.plot_surface(XI1, XI2, E, cmap='viridis', linewidth=0, antialiased=True)
ax1.set_title("Nhanh duong: +sqrt(|xi|^2 + m^2)")
ax1.set_xlabel("xi1")
ax1.set_ylabel("xi2")

ax2.plot_surface(XI1, XI2, -E, cmap='plasma', linewidth=0, antialiased=True)
ax2.set_title("Nhanh am: -sqrt(|xi|^2 + m^2)")
ax2.set_xlabel("xi1")
ax2.set_ylabel("xi2")

plt.tight_layout()
plt.show()
```

Hình này giúp sinh viên thấy ngay vì sao người ta hay nói về “Dirac cone” hay “dispersion tuyến tính” khi $$m=0$$.

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để vẽ trực tiếp hai mặt $$\pm \sqrt{\xi_1^2+\xi_2^2+m^2}$$ và cho phép thay đổi thanh trượt của $$m$$. Khi $$m\to 0$$, khoảng hở phổ đóng lại tại gốc; khi $$m>0$$, nón mở thành hai mặt tách nhau bởi một gap.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Dirac operator intuition`, `Lichnerowicz formula visualization`, `Atiyah Singer Dirac operator introduction`, hoặc `graphene Dirac cone animation`.

## Bài tập

1. Từ $$c(\xi)^2=-|\xi|^2\operatorname{Id}$$, viết nghịch đảo tường minh của $$c(\xi)$$ khi $$\xi\neq 0$$, rồi của $$\sigma_D(x,\xi)=i\,c(\xi)$$. Kết luận ellipticity bậc $$1$$.
2. Trên $$\mathbb{R}^n$$ với ma trận Clifford hằng, khai triển $$D=\sum_j c(e_j)\partial_{x_j}$$ và kiểm $$D^2=-\Delta\operatorname{Id}$$ nhờ phản giao hoán.
3. Từ Lichnerowicz, nếu $$M$$ đóng, $$\operatorname{Scal}>0$$, và $$D\psi=0$$, suy $$\psi=0$$ bằng cách lấy tích vô hướng $$L^2$$. Đây là đồng nhất connection, không phải định lý chỉ số.
4. Hodge–Dirac $$D_{\mathrm{dR}}=d+d^*$$: kiểm $$D_{\mathrm{dR}}^2=\Delta_H$$ và giải thích ellipticity từ symbol của $$d+d^*$$.
5. Vì sao $$\sigma_D$$ thuần nhất bậc $$1$$? So sánh bậc của $$D^2$$ với Laplacian, và nêu hệ quả Weyl: $$N(\Lambda)\sim C\Lambda^{n}$$ cho $$|D|$$ (bậc $$1$$) chứ không phải $$\Lambda^{n/2}$$.

## Tài liệu tham khảo

- L. Hörmander, *The Analysis of Linear Partial Differential Operators III*: ellipticity, principal symbol, và regularity cho hệ bậc nhất kiểu Dirac.
- M. Taylor, *Pseudodifferential Operators and Nonlinear PDE*: symbol của toán tử bậc nhất trên bundle và parametrix elliptic, đủ để đọc $$D$$ như một hệ elliptic.

