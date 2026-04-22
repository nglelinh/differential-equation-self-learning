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

![Dạng yếu của PDE qua hàm thử và tích phân từng phần]({{ site.imgurl }}/chapter_img/chapter12/04_weak_solutions_pdes.svg )

## Mục tiêu

Bài này giúp sinh viên hiểu cách chuyển một PDE cổ điển sang dạng yếu, vì sao nghiệm yếu là khái niệm đúng cho nhiều bài toán elliptic, và vì sao đây là cầu nối trực tiếp tới các định lý tồn tại như Lax-Milgram. Sau bài học, sinh viên cần tự suy ra được dạng yếu cho một số bài toán mẫu.

## Kiến thức nền

Sinh viên nên nắm đạo hàm yếu, không gian $$ H^1 $$ và $$ H^1_0 $$, tích phân từng phần, cùng trực giác về điều kiện biên Dirichlet. Cần nhấn mạnh rằng ta đang không “bỏ bớt” nội dung của PDE mà đang viết nó lại theo cách bền hơn.

## Dẫn nhập

Một PDE cổ điển thường yêu cầu nghiệm đủ trơn để mọi đạo hàm trong phương trình đều có nghĩa từng điểm. Nhưng thực tế, nghiệm tự nhiên của bài toán có thể chỉ có đạo hàm yếu. Nếu cứ giữ tiêu chuẩn cổ điển, ta sẽ loại bỏ chính những nghiệm đáng quan tâm nhất.

Nghiệm yếu giải quyết điều đó bằng cách nhân PDE với một hàm thử rồi tích phân từng phần để chuyển đạo hàm sang phía hàm thử. Phương trình mới yếu hơn về mặt trơn, nhưng vẫn giữ nguyên nội dung cân bằng hay bảo toàn của mô hình.

## Khái niệm theo ba cách

### Cách trực giác

Hãy nghĩ đến một tấm màng đàn hồi gắn chặt ở biên. Dù bề mặt có thể không trơn hoàn hảo tại mọi điểm, nó vẫn ở trạng thái cân bằng năng lượng. Nghiệm yếu mô tả đúng trạng thái cân bằng ấy thông qua một nguyên lý tổng thể thay vì yêu cầu độ cong chính xác tại từng điểm.

### Cách hình ảnh

Trên bảng, giáo viên nên vẽ hai cột:

- Cột trái: PDE cổ điển với toán tử $$ -\Delta u=f $$.
- Cột phải: công thức tích phân với hàm thử $$ \varphi $$.

Mũi tên giữa hai cột chính là tích phân từng phần. Sinh viên sẽ nhìn thấy rất rõ quá trình “đẩy” đạo hàm khỏi nghiệm sang hàm thử.

### Cách hình thức

Xét bài toán Poisson

$$
\begin{cases}
-\Delta u=f & \text{trong } \Omega,\\
u=0 & \text{trên } \partial\Omega.
\end{cases}
$$

Ta gọi $$ u\in H^1_0(\Omega) $$ là nghiệm yếu nếu

$$
\int_\Omega \nabla u\cdot \nabla \varphi\,dx=\int_\Omega f\varphi\,dx
\qquad \forall \varphi\in H^1_0(\Omega).
$$

Nếu $$ u $$ đủ trơn, công thức này nhận được bằng cách nhân PDE với $$ \varphi $$ rồi tích phân từng phần.

## Ngộ nhận thường gặp

### “Nghiệm yếu là nghiệm gần đúng”

Sai. Nó là một khái niệm nghiệm chính xác trong một không gian hàm rộng hơn.

### “Dạng yếu làm mất điều kiện biên”

Không. Điều kiện biên được mã hóa trong việc chọn không gian thử, chẳng hạn $$ H^1_0(\Omega) $$ cho Dirichlet đồng nhất.

### “Chỉ cần thay PDE bằng một tích phân là xong”

Chưa đủ. Phải chọn đúng không gian cho nghiệm và hàm thử thì dạng yếu mới có ý nghĩa.

### “Nếu có nghiệm yếu thì tự động có nghiệm cổ điển”

Sai. Cần thêm giả thiết regularity để nâng nghiệm yếu lên nghiệm trơn hơn.

## Tiến trình học

### Bước 1: Bắt đầu từ PDE cụ thể

Chọn Poisson vì đây là ví dụ mẫu rõ nhất.

### Bước 2: Nhân với hàm thử

Viết

$$
\int_\Omega (-\Delta u)\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

### Bước 3: Tích phân từng phần

Chuyển Laplacian sang gradient:

$$
\int_\Omega \nabla u\cdot\nabla\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

### Bước 4: Mở rộng không gian của nghiệm

Nhận ra công thức sau chỉ đòi hỏi gradient yếu của $$ u $$ nằm trong $$ L^2 $$. Vì vậy không gian tự nhiên là $$ H^1_0(\Omega) $$.

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự suy ra được dạng yếu từ dạng cổ điển không?
- Sinh viên có giải thích được vai trò của hàm thử không?
- Sinh viên có biết điều kiện biên được gắn vào đâu trong dạng yếu không?

## Ví dụ có lời giải

### Ví dụ 1: Bài toán một chiều

Xét $$-u''=f \quad \text{trên } (0,1),\qquad u(0)=u(1)=0$$. Nhân với $$ \varphi\in H^1_0(0,1) $$ rồi tích phân:

$$ \int_0^1 (-u'')\varphi\,dx=\int_0^1 f\varphi\,dx. $$

Tích phân từng phần cho

$$ \int_0^1 u'\varphi'\,dx=\int_0^1 f\varphi\,dx. $$

Đó là dạng yếu.

### Ví dụ 2: Nếu nghiệm cổ điển tồn tại

Giả sử $$ u\in C^2(\Omega)\cap C(\overline{\Omega}) $$ nghiệm bài toán Poisson với biên bằng 0. Khi đó mọi bước tích phân từng phần đều hợp lệ, nên nghiệm cổ điển luôn là nghiệm yếu.

Ý nghĩa: nghiệm yếu mở rộng khái niệm cũ chứ không thay thế theo kiểu mâu thuẫn.

### Ví dụ 3: Từ nguyên lý năng lượng

Xét phiếm hàm

$$
J(v)=\frac12\int_\Omega \lvert \nabla v\rvert^2\,dx-\int_\Omega fv\,dx
$$

trên $$ H^1_0(\Omega) $$.

Nếu $$ u $$ là điểm cực tiểu của $$ J $$, thì đạo hàm theo hướng phải bằng 0:

$$ \frac{d}{dt}J(u+t\varphi)\Big\vert_{t=0}=0. $$

Từ đó suy ra

$$
\int_\Omega \nabla u\cdot\nabla\varphi\,dx=\int_\Omega f\varphi\,dx.
$$

Ví dụ này cho thấy dạng yếu cũng chính là điều kiện cân bằng năng lượng.

### Ví dụ 4: Điều kiện Neumann

Nếu bài toán là

$$
-\Delta u=f \quad \text{trong } \Omega,\qquad \frac{\partial u}{\partial n}=0 \quad \text{trên } \partial\Omega,
$$

thì sau tích phân từng phần, số hạng biên không mất đi vì hàm thử không bằng 0 trên biên. Điều này cho thấy dạng yếu phụ thuộc mạnh vào loại điều kiện biên.

## Câu hỏi khái niệm

1. Vì sao dạng yếu của Poisson chỉ cần đạo hàm bậc một yếu dù PDE gốc có đạo hàm bậc hai?
2. Trong dạng yếu, điều kiện biên Dirichlet được đưa vào bằng cách nào?
3. Tại sao nghiệm yếu thường gắn chặt với một nguyên lý cực tiểu năng lượng?

## Bài toán ứng dụng

1. Trong bài toán nhiệt ổn định của một tấm kim loại, dạng yếu diễn tả điều gì về cân bằng năng lượng toàn cục?
2. Trong phương pháp phần tử hữu hạn, vì sao người ta giải dạng yếu thay vì dạng cổ điển?
3. Trong cơ học kết cấu, tại sao các trường chuyển vị thực nghiệm thường phù hợp với mô hình nghiệm yếu hơn nghiệm cổ điển?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu nghiệm không có đạo hàm bậc hai cổ điển thì ta còn cách nào để giữ PDE không?
- Hàm thử đóng vai trò như “thiết bị đo” điều gì của nghiệm?
- Tại sao cùng một PDE nhưng dạng yếu thay đổi khi đổi điều kiện biên?

### Hoạt động gợi ý

- Cho sinh viên tự suy ra dạng yếu của bài toán một chiều theo nhóm.
- So sánh trên bảng ba mức: dạng cổ điển, dạng yếu, bài toán cực tiểu năng lượng.
- Để mỗi nhóm giải thích một câu “nội dung vật lý” của dạng yếu.

### Cách tăng tham gia

- Yêu cầu sinh viên điền chỗ trống trong phép tích phân từng phần.
- Cho dự đoán trước về không gian tự nhiên của nghiệm.
- Mời sinh viên nêu lại bằng lời tại sao bậc đạo hàm giảm đi.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm rất kỹ bài toán một chiều trước.
- Viết rõ từng bước tích phân từng phần.
- Nhấn mạnh vai trò của không gian $$ H^1_0 $$ bằng ví dụ biên bằng 0.

### Thử thách cho sinh viên khá giỏi

- Tự suy ra dạng yếu cho toán tử dạng

$$ -\nabla\cdot(A\nabla u)=f. $$

- Liên hệ dạng yếu với Euler-Lagrange.
- Phân tích sự khác nhau giữa Dirichlet và Neumann trong khuôn khổ biến phân.

## Ghi nhớ nhanh

Nghiệm yếu là cách viết lại PDE bằng công thức tích phân với hàm thử để bài toán vẫn có nghĩa khi nghiệm không đủ trơn. Đây là cánh cửa mở sang Sobolev space, nguyên lý năng lượng và phương pháp phần tử hữu hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Poisson với nguồn gồ ghề
- Bài toán: Nguồn nhiệt, tải trọng hay mật độ điện tích thực tế thường chỉ thuộc $$ L^2 $$ chứ không trơn.
- Mô hình: Thay vì giải $$ -\Delta u=f $$ theo nghĩa cổ điển, ta tìm $$ u $$ sao cho
$$
\int_\Omega \nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx
$$
với mọi test function $$ v $$.
- Giả thiết và giới hạn: Dữ liệu và miền đủ để các tích phân có nghĩa.
- Diễn giải: Nghiệm yếu cho phép tồn tại nghiệm trong các tình huống mà nghiệm cổ điển không rõ ràng.

#### Võng màng hoặc đàn hồi tuyến tính
- Bài toán: Độ võng của một màng dưới tải phân bố thường được mô tả tốt nhất qua nguyên lý năng lượng.
- Mô hình: Nghiệm yếu xuất hiện từ bài toán cực tiểu hóa năng lượng.
- Giả thiết và giới hạn: Mô hình tuyến tính và biên thích hợp.
- Diễn giải: "Yếu" ở đây không phải kém hơn, mà là đúng lớp hàm vật lý hơn.

### 2. Trực giác bổ sung và các kết nối

Nghiệm yếu xuất hiện khi ta chuyển đạo hàm từ nghiệm sang test function bằng tích phân từng phần. Cái giá phải trả là ta không còn đòi hỏi quá nhiều độ trơn, nhưng cái được là phạm vi áp dụng rộng hơn rất nhiều. Một ngộ nhận phổ biến là nghiệm yếu chỉ là xấp xỉ số; thật ra nó là khái niệm nghiệm chuẩn trong nhiều ngành.

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

Giải
$$
-u''=1 \quad \text{trên } (0,1), \qquad u(0)=u(1)=0.
$$
Dạng yếu là tìm $$ u \in H_0^1(0,1) $$ sao cho
$$ \int_0^1 u'v'\,dx = \int_0^1 v\,dx $$
với mọi $$ v \in H_0^1(0,1) $$. Hàm
$$ u(x)=\frac{x(1-x)}{2} $$
thỏa đẳng thức này, nên chính là nghiệm yếu.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu cách tích phân từng phần sinh ra dạng yếu.

**Bậc sau đại học.** Kết nối với Galerkin, compactness và tồn tại nghiệm cho PDE phi tuyến.
