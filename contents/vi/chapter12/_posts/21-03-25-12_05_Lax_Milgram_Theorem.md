---
layout: post
title: "Định Lý Lax-Milgram"
chapter: '12'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: required
---

![Trực giác về coercivity trong định lý Lax-Milgram]({{ site.imgurl }}/chapter_img/chapter12/05_lax_milgram_theorem.svg )

## Mục tiêu

Bài này giúp sinh viên hiểu định lý Lax-Milgram như công cụ tồn tại và duy nhất nền tảng cho bài toán biến phân tuyến tính. Sau bài học, sinh viên cần nhận diện được hai điều kiện cốt lõi là tính liên tục và coercive, hiểu ý nghĩa hình học của chúng, và áp dụng được định lý vào bài toán Poisson.

## Kiến thức nền

Sinh viên nên nắm không gian Hilbert, phiếm hàm tuyến tính liên tục, dạng song tuyến tính, và dạng yếu của PDE. Cũng nên nhớ rằng ở hữu hạn chiều, giải hệ tuyến tính chính là tìm nghiệm của một toán tử khả nghịch; Lax-Milgram là phiên bản vô hạn chiều của ý tưởng đó.

## Dẫn nhập

Sau khi viết PDE về dạng yếu, ta không còn giải trực tiếp một phương trình vi phân nữa mà giải một đẳng thức song tuyến tính $$ a(u,v)=F(v) $$. Câu hỏi lớn là: bài toán này có nghiệm không, nghiệm có duy nhất không, và dữ liệu thay đổi nhỏ thì nghiệm có ổn định không? Lax-Milgram trả lời cả ba câu hỏi trong cùng một khuôn khổ rất đẹp.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một bát năng lượng. Nếu đáy bát cong đủ mạnh, viên bi sẽ chỉ có một vị trí cân bằng duy nhất và không thể trôi đi vô hạn. Tính coercive chính là “đáy bát cong đủ mạnh”, còn tính liên tục nói rằng bề mặt không quá dữ dội để ta mất kiểm soát.

### Cách hình ảnh

Vẽ đồ thị của một năng lượng bậc hai lồi mạnh trong không gian hữu hạn chiều. Sau đó nói với sinh viên rằng trong Hilbert space, Lax-Milgram bảo đảm điều tương tự: có một điểm cân bằng duy nhất khi năng lượng đủ tốt.

### Cách hình thức

Cho $$ H $$ là không gian Hilbert thực. Giả sử $$ a:H\times H\to\mathbb{R} $$ là dạng song tuyến tính thỏa

$$
\lvert a(u,v)\rvert\le M\lVert u\rVert_H\lVert v\rVert_H
$$

với mọi $$ u,v\in H $$, và $$ a(u,u)\ge \alpha \lVert u\rVert_H^2 $$ với một hằng số $$ \alpha>0 $$. Khi đó với mọi $$ F\in H^* $$, tồn tại duy nhất $$ u\in H $$ sao cho $$ a(u,v)=F(v)\qquad \forall v\in H $$. Hơn nữa,

$$
\lVert u\rVert_H\le \frac{1}{\alpha}\lVert F\rVert_{H^*}.
$$

## Ngộ nhận thường gặp

### “Liên tục là đủ để có nghiệm”

Sai. Nếu không coercive, bài toán có thể suy biến hoặc không duy nhất.

### “Coercive nghĩa là ma trận hay toán tử phải đối xứng”

Không nhất thiết. Đối xứng hữu ích nhưng không phải là điều kiện bắt buộc trong phát biểu cơ bản.

### “Lax-Milgram chỉ là định lý trừu tượng”

Sai. Đây là công cụ trực tiếp để chứng minh tồn tại nghiệm yếu của nhiều PDE elliptic.

### “Tính duy nhất đến từ dữ liệu”

Không. Tính duy nhất đến từ cấu trúc của dạng song tuyến tính, đặc biệt là coercive.

## Tiến trình học

### Bước 1: Nhìn lại dạng yếu

Viết lại bài toán dưới dạng $$ a(u,v)=F(v) $$ để sinh viên thấy định lý được áp dụng ở đâu.

### Bước 2: Phân tích hai điều kiện

- Liên tục: không gian không bị “nổ”.
- Coercive: có chặn dưới đủ mạnh để khóa nghiệm lại.

### Bước 3: Liên hệ với đại số tuyến tính

So sánh với ma trận xác định dương trong $$ \mathbb{R}^n $$.

### Bước 4: Áp dụng vào Poisson

Đây là ví dụ mẫu quan trọng nhất của bài.

### Các điểm kiểm tra hiểu bài

- Sinh viên có phân biệt được liên tục và coercive không?
- Sinh viên có giải thích được vì sao coercive liên quan đến tính duy nhất không?
- Sinh viên có thiết lập được $$ a(u,v) $$ và $$ F(v) $$ cho Poisson không?

## Ví dụ có lời giải

### Ví dụ 1: Dạng tích vô hướng chuẩn

Trên một Hilbert space $$ H $$, đặt $$ a(u,v)=\langle u,v\rangle $$. Khi đó $$\lvert a(u,v)\rvert\le \lVert u\rVert\,\lVert v\rVert$$ và $$ a(u,u)=\lVert u\rVert^2 $$. Vậy $$ a $$ vừa liên tục vừa coercive với $$ \alpha=1 $$. Lax-Milgram cho biết với mọi $$ F\in H^* $$ có duy nhất $$ u\in H $$ sao cho $$ \langle u,v\rangle=F(v) $$. Đây chính là định lý Riesz dưới một cách nhìn khác.

### Ví dụ 2: Bài toán Poisson

Trên $$ H^1_0(\Omega) $$, đặt

$$
a(u,v)=\int_\Omega \nabla u\cdot \nabla v\,dx,
\qquad
F(v)=\int_\Omega fv\,dx.
$$

Nhờ Cauchy-Schwarz và Poincare, ta có liên tục và coercive. Vì vậy bài toán Poisson có nghiệm yếu duy nhất.

### Ví dụ 3: Thêm hạng không đạo hàm

Xét

$$ a(u,v)=\int_0^1 u'v'\,dx+\int_0^1 uv\,dx. $$

Trên $$ H^1_0(0,1) $$, dạng này còn mạnh hơn ví dụ Poisson vì

$$
a(u,u)=\lVert u'\rVert_{L^2}^2+\lVert u\rVert_{L^2}^2=\lVert u\rVert_{H^1}^2.
$$

Do đó coercive hiển nhiên.

### Ví dụ 4: Một dạng không coercive

Xét

$$ a(u,v)=\int_0^1 u'v'\,dx $$

trên $$ H^1(0,1) $$ thay vì $$ H^1_0(0,1) $$. Với các hàm hằng $$ u=c $$, ta có $$ a(u,u)=0 $$ dù $$ u\ne 0 $$. Vậy dạng này không coercive trên toàn bộ $$ H^1(0,1) $$.

Ví dụ này giúp sinh viên thấy chọn đúng không gian là điều sống còn.

## Câu hỏi khái niệm

1. Vì sao coercive là điều kiện đúng để chặn nghiệm trong Hilbert space?
2. Điều gì có thể sai nếu dạng song tuyến tính chỉ liên tục mà không coercive?
3. Vì sao bất đẳng thức Poincare thường xuất hiện khi áp dụng Lax-Milgram cho Poisson?

## Bài toán ứng dụng

1. Trong cơ học đàn hồi tuyến tính, dạng năng lượng toàn phần đóng vai trò gì so với dạng $$ a(u,v) $$?
2. Trong truyền nhiệt ổn định, vì sao tồn tại nghiệm yếu duy nhất lại quan trọng về mặt vật lý?
3. Trong mô phỏng số, việc có ước lượng $$ \lVert u\rVert_H\le C\lVert F\rVert_{H^*} $$ giúp gì cho tính ổn định của thuật toán?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu bề mặt năng lượng có một hướng phẳng, điều gì xảy ra với tính duy nhất?
- Vì sao phải kiểm tra định lý trên một không gian cụ thể chứ không chỉ trên công thức?
- Có thể nhìn Lax-Milgram như một định lý “giải hệ tuyến tính vô hạn chiều” không?

### Hoạt động gợi ý

- Cho sinh viên phân loại một số dạng song tuyến tính thành “liên tục”, “coercive”, “cả hai”, “không cái nào”.
- Thảo luận nhóm về vai trò của Poincare trong Poisson.
- Yêu cầu mỗi nhóm tự viết một ví dụ thỏa điều kiện và một ví dụ vi phạm điều kiện.

### Cách tăng tham gia

- Bắt đầu bằng một phản ví dụ không coercive.
- Dùng hình ảnh bát năng lượng để gợi trực giác trước khi phát biểu định lý.
- Cho sinh viên tự điền vào khung áp dụng định lý: không gian, dạng song tuyến tính, phiếm hàm.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Liên hệ chặt với ma trận xác định dương trong đại số tuyến tính.
- Tập trung vào ví dụ Poisson một chiều.
- Viết rõ kiểm tra liên tục và coercive từng bước.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu mối liên hệ giữa Lax-Milgram và minimization của phiếm hàm lồi.
- Phân tích trường hợp dạng song tuyến tính không đối xứng.
- Mở rộng sang bài toán dạng

$$ -\nabla\cdot(A\nabla u)+cu=f. $$

## Ghi nhớ nhanh

Lax-Milgram nói rằng nếu dạng song tuyến tính đủ ổn định và đủ chặn dưới, thì bài toán biến phân tuyến tính có nghiệm duy nhất và nghiệm phụ thuộc liên tục vào dữ liệu. Đây là chiếc máy phát tồn tại cơ bản của lý thuyết PDE elliptic.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dẫn nhiệt không đồng nhất
- Bài toán: Nhiệt truyền qua vật liệu có hệ số khuếch tán thay đổi theo vị trí.
- Mô hình: Tìm $$ u \in H_0^1(\Omega) $$ sao cho
$$
a(u,v)=\int_\Omega k(x)\nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx.
$$
- Giả thiết và giới hạn: $$ k(x) $$ bị chặn trên và dưới bởi hằng dương.
- Diễn giải: Lax-Milgram đảm bảo tồn tại và duy nhất nghiệm yếu.

#### Phương pháp phần tử hữu hạn
- Bài toán: Sau khi rời rạc hóa PDE elliptic, ta thường nhận được hệ tuyến tính đối xứng xác định dương.
- Mô hình: Đây là phiên bản hữu hạn chiều của Lax-Milgram.
- Giả thiết và giới hạn: Không gian xấp xỉ là Hilbert hoặc con hữu hạn chiều của nó.
- Diễn giải: Định lý biến điều kiện giải được thành kiểm tra boundedness và coercivity.

### 2. Trực giác bổ sung và các kết nối

Lax-Milgram là cầu nối giữa giải tích hàm và mô hình vật lý năng lượng. Nếu dạng song tuyến tính bị chặn và coercive, năng lượng có một cực tiểu duy nhất và do đó bài toán có một nghiệm duy nhất. Một bẫy phổ biến là nghĩ tính bị chặn là đủ; thật ra coercivity mới là chìa khóa.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([1.0, 1.5])

x1 = np.linspace(-1, 1.5, 150)
x2 = np.linspace(-1, 1.5, 150)
X1, X2 = np.meshgrid(x1, x2)
J = 0.5 * (A[0,0] * X1**2 + 2 * A[0,1] * X1 * X2 + A[1,1] * X2**2) - b[0] * X1 - b[1] * X2

plt.contour(X1, X2, J, levels=20)
sol = np.linalg.solve(A, b)
plt.scatter([sol[0]], [sol[1]], color="red", label="nghiem duy nhat")
plt.legend()
plt.title("The nang luong lồi sinh nghiem duy nhat")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Lax Milgram theorem energy minimization visualization
- search: coercive bilinear form finite element intuition
- search: symmetric positive definite system geometry

### 5. Bài toán mẫu có bối cảnh thực

Trên $$ H_0^1(0,1) $$, xét
$$
a(u,v)=\int_0^1 (u'v' + uv)\,dx, \qquad \ell(v)=\int_0^1 f v\,dx.
$$
Dạng $$ a $$ bị chặn và coercive theo chuẩn $$ H^1 $$. Vì thế với mọi $$ f \in L^2(0,1) $$, tồn tại duy nhất $$ u \in H_0^1(0,1) $$ sao cho
$$ a(u,v)=\ell(v) $$
với mọi $$ v $$. Đây là khuôn mẫu chuẩn cho nhiều PDE elliptic tuyến tính.

### 6. Phân tầng độ khó

**Bậc đại học.** So sánh với hệ tuyến tính đối xứng xác định dương.

**Bậc sau đại học.** Kết nối với Riesz representation, bài toán yên ngựa và điều kiện inf-sup.
