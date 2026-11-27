---
layout: post
title: "Nghiệm Yếu Của PDE"
chapter: '12'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: required
---

![Dạng yếu của PDE qua hàm thử và tích phân từng phần]({{ site.imgurl }}/chapter_img/chapter12/04_weak_solutions_pdes.svg)

Một tấm vật liệu ghép từ hai lớp đồng và sắt có hệ số dẫn nhiệt $a(x)$ nhảy bậc đột ngột tại mối nối: nghiệm nhiệt độ $u(x)$ bị gãy khúc đạo hàm ngay tại mối nối nên **không thể có đạo hàm bậc hai $u''$ theo nghĩa cổ điển**! Thế nhưng nhiệt độ ngoài đời thực vẫn tồn tại một cách hiển nhiên. **Công thức Nghiệm Yếu (Weak Formulation)** giải cứu hoàn toàn tình thế: nhân PDE với hàm thử $v$, tích phân từng phần một lần để chia đều gánh nặng đạo hàm bậc hai thành **hai đạo hàm bậc nhất** $\nabla u \cdot \nabla v$!

## Kiến thức cần nhớ: Bốn bước chuyển PDE sang Dạng Biến phân (Weak Form)

1. **Nhân với hàm thử $v$ và Tích phân từng phần (Công thức Green)**:
   Từ $-\nabla \cdot (a\nabla u) = f$, ta chuyển sang tìm $u \in V$ sao cho $\int_\Omega a\nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx$ với mọi $v \in V$. Bậc đạo hàm đòi hỏi trên $u$ giảm ngay từ $C^2$ xuống chỉ còn $H^1$!
2. **Phân biệt Điều kiện biên Thiết yếu (Essential) vs. Tự nhiên (Natural)**:
   - *Biên Dirichlet* ($u = 0$) được **ép cứng vào không gian hàm** $V = H_0^1(\Omega)$.
   - *Biên Neumann* ($a\partial_n u = g$) **tự động xuất hiện trong tích phân biên** $\int_{\partial\Omega} g v\,dS$ mà không cần ép lên không gian thử $V = H^1(\Omega)$!
3. **Dạng song tuyến tính $a(u, v) = \ell(v)$**:
   Mọi PDE elliptic tuyến tính bậc hai đều thu gọn về phương trình trừu tượng $a(u, v) = \ell(v)\; \forall v \in V$, chuẩn bị sẵn sàng cho định lý Lax–Milgram (Bài 12-05) và rời rạc hóa Galerkin/FEM (Chương 13).
4. **Tương đương giữa Nghiệm Cổ điển và Nghiệm Yếu**:
   Mọi nghiệm cổ điển $C^2$ đều là nghiệm yếu; ngược lại, nếu một nghiệm yếu tình cờ trơn $C^2$, tích phân từng phần ngược lại chứng minh nó thỏa mãn PDE theo đúng từng điểm!

## Mục tiêu

Bài học này hướng dẫn cách chuyển một PDE cổ điển sang dạng yếu, giải thích vì sao nghiệm yếu là khuôn khổ phù hợp cho nhiều bài toán elliptic, và làm rõ cầu nối trực tiếp tới các định lý tồn tại như Lax–Milgram. Sau bài học, sinh viên cần tự suy ra được dạng yếu cho các bài toán mẫu.

## Kiến thức nền

Sinh viên cần nắm đạo hàm yếu, các không gian $$ H^1 $$ và $$ H^1_0 $$, tích phân từng phần và trực giác về điều kiện biên Dirichlet. Cần lưu ý rằng dạng yếu không làm mất nội dung của PDE mà viết lại phương trình trong một khuôn khổ vững chắc hơn.

## Dẫn nhập

Một PDE cổ điển đòi hỏi nghiệm đủ trơn để mọi đạo hàm xuất hiện trong phương trình đều tồn tại tại từng điểm. Tuy nhiên, nghiệm tự nhiên của nhiều bài toán thực tế chỉ có đạo hàm yếu; nếu giữ nguyên yêu cầu cổ điển, các nghiệm quan trọng này sẽ bị loại bỏ.

Cách tiếp cận nghiệm yếu khắc phục điều này bằng cách nhân PDE với một hàm thử rồi tích phân từng phần để giảm bậc đạo hàm đặt lên nghiệm. Phương trình thu được đòi hỏi ít độ trơn hơn nhưng vẫn bảo toàn nguyên lý cân bằng hoặc bảo toàn của mô hình vật lý.


### Giải thích: Chuyển đổi và kiểm chứng trực tiếp nghiệm yếu của $-u'' = 2$ trên $(0, 1)$

Xét bài toán biên Dirichlet $-u''(x) = 2$ trên $(0, 1)$ với $u(0) = u(1) = 0$:
1. **Lập dạng yếu**: Nhân hai vế với hàm thử bất kỳ $v \in H_0^1(0, 1)$ (có $v(0) = v(1) = 0$) và tích phân từng phần:
   $$\int_0^1 (-u'') v\,dx = \Big[-u'(x)v(x)\Big]_0^1 + \int_0^1 u'(x)v'(x)\,dx = \int_0^1 u'(x)v'(x)\,dx.$$
   Vậy dạng yếu là: tìm $u \in H_0^1(0, 1)$ sao cho
   $$a(u, v) := \int_0^1 u'(x)v'(x)\,dx = \int_0^1 2v(x)\,dx =: \ell(v) \qquad \forall v \in H_0^1(0, 1).$$
2. **Kiểm chứng trực tiếp nghiệm $u(x) = x(1 - x)$**:
   Ta có $u(0) = u(1) = 0$ và $u'(x) = 1 - 2x$. Thay vào vế trái:
   $$\int_0^1 (1 - 2x)v'(x)\,dx = \Big[(1 - 2x)v(x)\Big]_0^1 - \int_0^1 (-2)v(x)\,dx = 0 + \int_0^1 2v(x)\,dx = \ell(v).$$
   Đẳng thức đúng với **mọi** hàm thử $v \in H_0^1(0,1)$—chứng tỏ $u(x) = x(1-x)$ là nghiệm yếu chính xác!
## Khái niệm theo ba cách

### Cách trực giác

Xét một tấm màng đàn hồi được cố định dọc theo biên. Dù bề mặt màng có thể không trơn tuyệt đối tại mọi điểm, hệ vẫn nằm ở trạng thái cân bằng năng lượng. Nghiệm yếu diễn đạt chính trạng thái cân bằng đó qua một điều kiện tích phân toàn cục thay vì đòi hỏi độ cong từng điểm.

### Cách hình ảnh

Có thể đặt hai biểu diễn song song để đối chiếu:

- Cột trái: PDE cổ điển với toán tử $$ -\Delta u=f $$.
- Cột phải: đẳng thức tích phân với hàm thử $$ \varphi $$.

Phép tích phân từng phần đóng vai trò mũi tên nối hai cột, cho thấy rõ bước chuyển một bậc đạo hàm từ nghiệm sang hàm thử.

### Cách hình thức

Xét bài toán Poisson:

$$
\begin{cases}
-\Delta u=f & \text{trong } \Omega,\\
u=0 & \text{trên } \partial\Omega.
\end{cases}
$$

Ta nói $$ u\in H^1_0(\Omega) $$ là nghiệm yếu của bài toán nếu:

$$
\int_\Omega \nabla u\cdot \nabla \varphi\,dx=\int_\Omega f\varphi\,dx
\qquad \forall \varphi\in H^1_0(\Omega).
$$

Khi $$ u $$ đủ trơn, đẳng thức này thu được trực tiếp bằng cách nhân PDE với $$ \varphi $$ rồi áp dụng công thức tích phân từng phần.

## Ngộ nhận thường gặp

### “Nghiệm yếu là nghiệm gần đúng”

Sai. Nghiệm yếu là khái niệm nghiệm chính xác được định nghĩa trên một không gian hàm rộng hơn.

### “Chuyển sang dạng yếu làm mất điều kiện biên”

Không đúng. Điều kiện biên được mã hóa vào không gian hàm (như $$ H^1_0(\Omega) $$ cho điều kiện Dirichlet thuần nhất) hoặc xuất hiện tường minh trong tích phân biên (như ở bài toán Neumann không thuần nhất).

### “Chỉ cần viết lại PDE dưới dạng tích phân là xong”

Chưa đủ. Cần chỉ rõ không gian cho nghiệm và không gian cho hàm thử để các tích phân đều có nghĩa và điều kiện biên được thực thi đúng.

### “Có nghiệm yếu thì tự động có nghiệm cổ điển”

Sai. Cần thêm các giả thiết và kết quả về tính chính quy (regularity) để khẳng định nghiệm yếu thực sự trơn hơn.

## Tiến trình học

### Bước 1: Bắt đầu từ một PDE cụ thể

Chọn bài toán Poisson làm ví dụ mẫu tiêu biểu.

### Bước 2: Nhân với hàm thử

Viết đẳng thức tích phân:

$$
\int_\Omega (-\Delta u)\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

### Bước 3: Áp dụng tích phân từng phần

Chuyển toán tử Laplace sang tích vô hướng của hai gradient:

$$
\int_\Omega \nabla u\cdot\nabla\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

### Bước 4: Xác định không gian nghiệm tự nhiên

Nhận thấy biểu thức cuối chỉ yêu cầu gradient yếu của $$ u $$ thuộc $$ L^2 $$, do đó không gian tự nhiên cho bài toán Dirichlet thuần nhất là $$ H^1_0(\Omega) $$.

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự suy ra được dạng yếu từ dạng cổ điển hay không?
- Sinh viên có giải thích được vai trò của hàm thử hay không?
- Sinh viên có chỉ ra được điều kiện biên được đưa vào vị trí nào trong dạng yếu hay không?

## Ví dụ có lời giải

### Ví dụ 1: Bài toán một chiều

Xét $$-u''=f \quad \text{trên } (0,1),\qquad u(0)=u(1)=0$$. Nhân hai vế với $$ \varphi\in H^1_0(0,1) $$ rồi tích phân:

$$ \int_0^1 (-u'')\varphi\,dx=\int_0^1 f\varphi\,dx. $$

Áp dụng tích phân từng phần (số hạng biên triệt tiêu vì $$ \varphi(0)=\varphi(1)=0 $$), ta thu được dạng yếu:

$$ \int_0^1 u'\varphi'\,dx=\int_0^1 f\varphi\,dx. $$

### Ví dụ 2: Tính tương thích với nghiệm cổ điển

Giả sử $$ u\in C^2(\Omega)\cap C(\overline{\Omega}) $$ là nghiệm cổ điển của bài toán Poisson với điều kiện biên bằng 0. Khi đó mọi bước tích phân từng phần đều hợp lệ, nên mọi nghiệm cổ điển đều là nghiệm yếu. Như vậy, nghiệm yếu là sự mở rộng nhất quán của nghiệm cổ điển.

### Ví dụ 3: Liên hệ với nguyên lý cực tiểu năng lượng

Xét phiếm hàm năng lượng:

$$
J(v)=\frac12\int_\Omega \lvert \nabla v\rvert^2\,dx-\int_\Omega fv\,dx
$$

trên $$ H^1_0(\Omega) $$. Nếu $$ u $$ là điểm cực tiểu của $$ J $$, đạo hàm theo hướng tại $$ u $$ phải bằng 0:

$$ \frac{d}{dt}J(u+t\varphi)\Big\vert_{t=0}=0. $$

Khai triển biểu thức này dẫn đến đúng dạng yếu:

$$
\int_\Omega \nabla u\cdot\nabla\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

Ví dụ này cho thấy dạng yếu tương đương với điều kiện dừng của năng lượng.

### Ví dụ 4: Điều kiện biên Neumann

Xét bài toán với điều kiện biên Neumann thuần nhất:

$$
-\Delta u=f \quad \text{trong } \Omega,\qquad \frac{\partial u}{\partial n}=0 \quad \text{trên } \partial\Omega.
$$

Ở đây, hàm thử $$ \varphi\in H^1(\Omega) $$ không bị ép bằng 0 trên biên như trong bài toán Dirichlet. Sau khi tích phân từng phần, số hạng biên $$ -\int_{\partial\Omega} \frac{\partial u}{\partial n}\varphi\,ds $$ triệt tiêu nhờ chính điều kiện $$ \frac{\partial u}{\partial n}=0 $$ (nếu điều kiện Neumann không thuần nhất $$ \frac{\partial u}{\partial n}=g $$, số hạng biên $$ \int_{\partial\Omega} g\varphi\,ds $$ sẽ xuất hiện tường minh trong dạng yếu). Điều này cho thấy cả không gian hàm thử lẫn biểu thức dạng yếu đều phụ thuộc trực tiếp vào loại điều kiện biên.

## Câu hỏi khái niệm

1. Vì sao dạng yếu của phương trình Poisson chỉ đòi hỏi đạo hàm yếu bậc một dù phương trình gốc có đạo hàm bậc hai?
2. Trong dạng yếu, điều kiện biên Dirichlet thuần nhất được thể hiện bằng cách nào?
3. Vì sao nghiệm yếu của nhiều bài toán elliptic gắn liền với một nguyên lý cực tiểu hóa năng lượng?

## Bài toán ứng dụng

1. Trong bài toán truyền nhiệt ổn định trên tấm kim loại, dạng yếu phản ánh ý nghĩa gì về cân bằng năng lượng toàn cục?
2. Trong phương pháp phần tử hữu hạn (FEM), vì sao người ta rời rạc hóa dạng yếu thay vì dạng cổ điển?
3. Trong cơ học kết cấu, vì sao trường chuyển vị thực tế thường phù hợp với khuôn khổ nghiệm yếu hơn nghiệm cổ điển?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu nghiệm không có đạo hàm bậc hai cổ điển, ta có cách nào vẫn giữ được ý nghĩa của PDE hay không?
- Hàm thử đóng vai trò kiểm định điều gì của nghiệm?
- Tại sao cùng một PDE nhưng dạng yếu và không gian hàm lại thay đổi khi đổi loại điều kiện biên?

### Hoạt động gợi ý

- Cho sinh viên thảo luận nhóm để tự suy ra dạng yếu cho bài toán một chiều.
- So sánh song song trên bảng ba biểu diễn: dạng cổ điển, dạng yếu và bài toán cực tiểu năng lượng.
- Mời từng nhóm tóm tắt trong một câu ý nghĩa vật lý của dạng yếu.

### Cách tăng tham gia

- Cho sinh viên điền từng bước biến đổi trong phép tích phân từng phần.
- Yêu cầu dự đoán không gian hàm tự nhiên trước khi viết định nghĩa chính thức.
- Mời sinh viên giải thích bằng lời lý do bậc đạo hàm giảm xuống sau khi tích phân từng phần.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm kỹ bài toán một chiều trước khi chuyển sang nhiều chiều.
- Viết rõ từng bước tích phân từng phần và xử lý số hạng biên.
- Minh họa vai trò của không gian $$ H^1_0 $$ qua điều kiện biên bằng 0.

### Thử thách cho sinh viên khá giỏi

- Tự suy ra dạng yếu cho toán tử phân kỳ $$ -\nabla\cdot(A\nabla u)=f $$.
- Liên hệ dạng yếu với phương trình Euler–Lagrange.
- So sánh vai trò của điều kiện biên cốt yếu (Dirichlet) và điều kiện biên tự nhiên (Neumann) trong khuôn khổ biến phân.

## Ghi nhớ nhanh

Nghiệm yếu viết lại PDE dưới dạng đẳng thức tích phân với hàm thử để bài toán vẫn có nghĩa khi nghiệm không đủ trơn. Đây là cầu nối trực tiếp tới không gian Sobolev, nguyên lý năng lượng và phương pháp phần tử hữu hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phương trình Poisson với nguồn không trơn
- Bài toán: Nguồn nhiệt, tải trọng hoặc mật độ điện tích thực tế thường chỉ thuộc $$ L^2 $$ chứ không trơn.
- Mô hình: Thay vì giải $$ -\Delta u=f $$ từng điểm, ta tìm $$ u $$ sao cho
$$
\int_\Omega \nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx
$$
với mọi hàm thử $$ v $$.
- Giả thiết và giới hạn: Miền và dữ liệu đảm bảo các tích phân hội tụ.
- Diễn giải: Khuôn khổ nghiệm yếu cho phép chứng minh tồn tại nghiệm ngay cả khi nghiệm cổ điển không xác định rõ.

#### Độ võng màng và đàn hồi tuyến tính
- Bài toán: Độ võng tĩnh của màng chịu tải phân bố thường được phát biểu trực tiếp từ nguyên lý cực tiểu năng lượng.
- Mô hình: Nghiệm yếu chính là nghiệm của phương trình biến phân tương ứng với cực tiểu năng lượng.
- Giả thiết và giới hạn: Mô hình tuyến tính cùng điều kiện biên thích hợp.
- Diễn giải: "Nghiệm yếu" không có nghĩa là kém chất lượng, mà là nghiệm thuộc đúng lớp hàm năng lượng của vật lý.

### 2. Trực giác bổ sung và các kết nối

Dạng yếu hình thành khi ta chuyển một bậc đạo hàm từ nghiệm sang hàm thử bằng tích phân từng phần. Nhờ giảm yêu cầu về độ trơn, phương trình áp dụng được cho lớp bài toán rộng hơn nhiều. Một nhầm lẫn phổ biến là coi nghiệm yếu chỉ là xấp xỉ số; thực chất đây là khái niệm nghiệm toán học chuẩn trong giải tích PDE hiện đại.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u = 0.5 * x * (1 - x)
f = np.ones_like(x)

plt.plot(x, u, label="nghiem yeu / co dien")
plt.plot(x, f, label="nguon f=1")
plt.legend()
plt.title("Bai toan -u''=1 tren (0,1) voi bien Dirichlet")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: weak solution Poisson equation finite element intuition
- search: variational formulation membrane deflection
- search: integration by parts weak form PDE

### 5. Bài toán mẫu có bối cảnh thực

Xét bài toán
$$
-u''=1 \quad \text{trên } (0,1), \qquad u(0)=u(1)=0.
$$
Dạng yếu là tìm $$ u \in H_0^1(0,1) $$ sao cho $$ \int_0^1 u'v'\,dx = \int_0^1 v\,dx $$ với mọi $$ v \in H_0^1(0,1) $$. Hàm $$ u(x)=\frac{x(1-x)}{2} $$ thỏa mãn đẳng thức này và chính là nghiệm yếu (đồng thời là nghiệm cổ điển) của bài toán.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm cách dùng tích phân từng phần để thiết lập dạng yếu của PDE.

**Bậc sau đại học.** Kết nối với phương pháp Galerkin, tính compact và sự tồn tại nghiệm yếu cho PDE phi tuyến.

## Video tham khảo

- xem trước: [Lax-Milgram, application to Poisson equation.](https://www.youtube.com/watch?v=s5P3e1FhpTk) — Learn Maths with Dr Alex, tiếng Anh. Áp dụng định lý Lax–Milgram cho phương trình Poisson để thu được nghiệm yếu.
- [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, tiếng Anh. Trình bày không gian Sobolev H^1 nơi nghiệm yếu tồn tại.
- [Lax-Milgram lemma](https://www.youtube.com/watch?v=w8QjyVug78M) — Numerical Analysis by Julian Roth, tiếng Anh. Trình bày chi tiết chứng minh bổ đề Lax–Milgram.
