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

Bài học này giới thiệu định lý Lax–Milgram như công cụ chứng minh tồn tại và duy nhất nền tảng cho các bài toán biến phân tuyến tính. Sau bài học, sinh viên cần nhận diện được hai điều kiện cốt lõi là tính liên tục (bị chặn) và tính cưỡng bức (coercive), hiểu ý nghĩa hình học của chúng, và áp dụng được định lý vào bài toán Poisson.

## Kiến thức nền

Sinh viên cần nắm không gian Hilbert, phiếm hàm tuyến tính liên tục, dạng song tuyến tính và dạng yếu của PDE. Ở hữu hạn chiều, giải hệ tuyến tính tương ứng với tìm nghịch đảo của một ma trận không suy biến; định lý Lax–Milgram là phiên bản vô hạn chiều của ý tưởng đó.

## Dẫn nhập

Sau khi chuyển PDE sang dạng yếu, ta không còn giải trực tiếp một phương trình vi phân từng điểm mà giải đẳng thức song tuyến tính $$ a(u,v)=F(v) $$. Ba câu hỏi đặt ra là: bài toán có nghiệm hay không, nghiệm có duy nhất hay không, và nghiệm có phụ thuộc liên tục vào dữ liệu hay không? Định lý Lax–Milgram trả lời đồng thời cả ba câu hỏi trong một khuôn khổ gọn gàng.

## Khái niệm theo ba cách

### Cách trực giác

Hãy hình dung một bề mặt năng lượng dạng lòng bát. Nếu đáy bát cong lên đủ mạnh theo mọi hướng, viên bi chỉ có đúng một vị trí cân bằng duy nhất và không thể trượt ra vô hạn. Tính cưỡng bức (coercive) tương ứng với độ cong dưới đủ mạnh đó, còn tính liên tục đảm bảo bề mặt không biến thiên quá đột ngột làm mất kiểm soát.

### Cách hình ảnh

Xét đồ thị của một phiếm hàm năng lượng bậc hai lồi chặt trong không gian hữu hạn chiều. Trong không gian Hilbert vô hạn chiều, định lý Lax–Milgram đảm bảo tính chất tương tự: bài toán biến phân có nghiệm cân bằng duy nhất khi dạng song tuyến tính thỏa mãn hai điều kiện liên tục và cưỡng bức.

### Cách hình thức

Cho $$ H $$ là không gian Hilbert thực. Giả sử $$ a:H\times H\to\mathbb{R} $$ là dạng song tuyến tính thỏa mãn điều kiện liên tục:

$$
\lvert a(u,v)\rvert\le M\lVert u\rVert_H\lVert v\rVert_H
$$

với mọi $$ u,v\in H $$, và điều kiện cưỡng bức $$ a(u,u)\ge \alpha \lVert u\rVert_H^2 $$ với một hằng số $$ \alpha>0 $$. Khi đó, với mọi phiếm hàm $$ F\in H^* $$, tồn tại duy nhất $$ u\in H $$ sao cho $$ a(u,v)=F(v)\qquad \forall v\in H $$. Hơn nữa, ta có ước lượng ổn định:

$$
\lVert u\rVert_H\le \frac{1}{\alpha}\lVert F\rVert_{H^*}.
$$

## Ngộ nhận thường gặp

### “Chỉ cần tính liên tục là đủ để có nghiệm”

Sai. Nếu thiếu tính cưỡng bức, bài toán có thể suy biến, vô nghiệm hoặc không duy nhất nghiệm.

### “Tính cưỡng bức đòi hỏi dạng song tuyến tính phải đối xứng”

Không đúng. Tính đối xứng giúp liên hệ trực tiếp với bài toán cực tiểu hóa năng lượng, nhưng không phải điều kiện bắt buộc trong định lý Lax–Milgram.

### “Lax–Milgram chỉ là một định lý trừu tượng”

Sai. Đây là công cụ trực tiếp dùng để chứng minh tồn tại và duy nhất nghiệm yếu cho lớp rộng các PDE elliptic.

### “Tính duy nhất đến từ dữ liệu vế phải”

Không đúng. Tính duy nhất xuất phát từ cấu trúc của dạng song tuyến tính, đặc biệt là điều kiện cưỡng bức.

## Tiến trình học

### Bước 1: Viết lại dạng yếu

Đưa bài toán về dạng chuẩn $$ a(u,v)=F(v) $$ để xác định rõ đối tượng áp dụng định lý.

### Bước 2: Phân tích hai điều kiện giả thiết

- Tính liên tục (bị chặn): kiểm soát chặn trên của dạng song tuyến tính.
- Tính cưỡng bức: tạo chặn dưới đủ mạnh để khóa nghiệm và đảm bảo tính duy nhất.

### Bước 3: Liên hệ với đại số tuyến tính

So sánh trực tiếp với ma trận xác định dương trong $$ \mathbb{R}^n $$.

### Bước 4: Áp dụng vào bài toán Poisson

Thực hành kiểm tra đầy đủ các giả thiết cho ví dụ mẫu quan trọng nhất của bài.

### Các điểm kiểm tra hiểu bài

- Sinh viên có phân biệt được tính liên tục và tính cưỡng bức hay không?
- Sinh viên có giải thích được vì sao tính cưỡng bức dẫn tới tính duy nhất của nghiệm hay không?
- Sinh viên có thiết lập được $$ a(u,v) $$ và $$ F(v) $$ cho bài toán Poisson hay không?

## Ví dụ có lời giải

### Ví dụ 1: Dạng tích vô hướng chuẩn

Trên không gian Hilbert $$ H $$, đặt $$ a(u,v)=\langle u,v\rangle $$. Khi đó $$\lvert a(u,v)\rvert\le \lVert u\rVert\,\lVert v\rVert$$ và $$ a(u,u)=\lVert u\rVert^2 $$, nên $$ a $$ vừa liên tục vừa cưỡng bức với $$ \alpha=1 $$. Theo định lý Lax–Milgram, với mọi $$ F\in H^* $$ tồn tại duy nhất $$ u\in H $$ sao cho $$ \langle u,v\rangle=F(v) $$. Đây chính là định lý biểu diễn Riesz.

### Ví dụ 2: Bài toán Poisson

Trên $$ H^1_0(\Omega) $$, đặt:

$$
a(u,v)=\int_\Omega \nabla u\cdot \nabla v\,dx,
\qquad
F(v)=\int_\Omega fv\,dx.
$$

Nhờ bất đẳng thức Cauchy–Schwarz và bất đẳng thức Poincaré, $$ a $$ thỏa mãn cả tính liên tục lẫn tính cưỡng bức. Do đó bài toán Poisson có nghiệm yếu duy nhất trong $$ H^1_0(\Omega) $$.

### Ví dụ 3: Bổ sung số hạng không chứa đạo hàm

Xét dạng song tuyến tính:

$$ a(u,v)=\int_0^1 u'v'\,dx+\int_0^1 uv\,dx. $$

Trên $$ H^1_0(0,1) $$ (và cả trên $$ H^1(0,1) $$), ta có:

$$
a(u,u)=\lVert u'\rVert_{L^2}^2+\lVert u\rVert_{L^2}^2=\lVert u\rVert_{H^1}^2,
$$

nên tính cưỡng bức được thỏa mãn trực tiếp với $$ \alpha=1 $$ mà không cần dùng bất đẳng thức Poincaré.

### Ví dụ 4: Một dạng không cưỡng bức

Xét

$$ a(u,v)=\int_0^1 u'v'\,dx $$

trên toàn bộ $$ H^1(0,1) $$ thay vì $$ H^1_0(0,1) $$. Với mọi hàm hằng khác không $$ u=c $$, ta có $$ a(u,u)=0 $$ dù $$ u\ne 0 $$, nên dạng này không cưỡng bức trên $$ H^1(0,1) $$. Ví dụ này cho thấy việc chọn đúng không gian hàm có vai trò quyết định.

## Câu hỏi khái niệm

1. Vì sao tính cưỡng bức là điều kiện thích hợp để chặn nghiệm trong không gian Hilbert?
2. Điều gì có thể xảy ra nếu dạng song tuyến tính chỉ liên tục mà không cưỡng bức?
3. Vì sao bất đẳng thức Poincaré thường được dùng khi áp dụng Lax–Milgram cho bài toán Poisson?

## Bài toán ứng dụng

1. Trong cơ học đàn hồi tuyến tính, dạng năng lượng biến dạng đóng vai trò gì so với dạng song tuyến tính $$ a(u,v) $$?
2. Trong truyền nhiệt ổn định, vì sao tính tồn tại và duy nhất của nghiệm yếu có ý nghĩa quan trọng về mặt vật lý?
3. Trong mô phỏng số, ước lượng ổn định $$ \lVert u\rVert_H\le C\lVert F\rVert_{H^*} $$ có vai trò gì đối với độ tin cậy của thuật toán?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu bề mặt năng lượng có một phương phẳng, điều gì xảy ra với tính duy nhất của nghiệm?
- Vì sao luôn phải kiểm tra các giả thiết của định lý trên một không gian cụ thể chứ không chỉ dựa vào công thức của $$ a(u,v) $$?
- Có thể xem định lý Lax–Milgram là phiên bản vô hạn chiều của việc giải hệ tuyến tính xác định dương không?

### Hoạt động gợi ý

- Cho sinh viên phân loại một số dạng song tuyến tính theo bốn nhóm: chỉ liên tục, chỉ cưỡng bức, thỏa cả hai, không thỏa điều kiện nào.
- Thảo luận nhóm về vai trò của bất đẳng thức Poincaré trong bài toán Poisson.
- Yêu cầu mỗi nhóm xây dựng một ví dụ thỏa mãn định lý và một ví dụ vi phạm giả thiết.

### Cách tăng tham gia

- Mở đầu bằng phản ví dụ không cưỡng bức để nhấn mạnh vai trò của không gian hàm.
- Dùng hình ảnh bề mặt năng lượng lồi để tạo trực giác trước khi phát biểu định lý.
- Cho sinh viên tự điền vào khung áp dụng định lý: chọn không gian $$ H $$, viết $$ a(u,v) $$ và $$ F(v) $$, rồi kiểm tra từng điều kiện.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Liên hệ trực tiếp với hệ tuyến tính có ma trận xác định dương trong đại số tuyến tính.
- Tập trung vào bài toán Poisson một chiều trước khi mở rộng sang nhiều chiều.
- Trình bày rõ từng bước kiểm tra tính liên tục và tính cưỡng bức.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu mối liên hệ giữa định lý Lax–Milgram và bài toán cực tiểu hóa phiếm hàm lồi.
- Phân tích trường hợp dạng song tuyến tính không đối xứng.
- Mở rộng sang toán tử elliptic tổng quát $$ -\nabla\cdot(A\nabla u)+cu=f $$.

## Ghi nhớ nhanh

Định lý Lax–Milgram khẳng định rằng nếu dạng song tuyến tính vừa liên tục vừa cưỡng bức trên một không gian Hilbert, thì bài toán biến phân tuyến tính có nghiệm duy nhất và phụ thuộc liên tục vào dữ liệu. Đây là công cụ chứng minh tồn tại nghiệm cơ bản của lý thuyết PDE elliptic.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dẫn nhiệt trong môi trường không đồng nhất
- Bài toán: Khảo sát truyền nhiệt qua vật liệu có hệ số dẫn nhiệt thay đổi theo vị trí.
- Mô hình: Tìm $$ u \in H_0^1(\Omega) $$ sao cho
$$
a(u,v)=\int_\Omega k(x)\nabla u \cdot \nabla v\,dx = \int_\Omega f v\,dx.
$$
- Giả thiết và giới hạn: Hệ số $$ k(x) $$ bị chặn trên và bị chặn dưới bởi các hằng số dương.
- Diễn giải: Định lý Lax–Milgram đảm bảo tồn tại duy nhất nghiệm yếu.

#### Phương pháp phần tử hữu hạn
- Bài toán: Rời rạc hóa PDE elliptic dẫn đến hệ phương trình tuyến tính xác định dương.
- Mô hình: Hệ rời rạc chính là phiên bản hữu hạn chiều của khuôn khổ Lax–Milgram.
- Giả thiết và giới hạn: Không gian xấp xỉ là không gian con hữu hạn chiều của không gian Hilbert.
- Diễn giải: Định lý chuyển bài toán chứng minh tính giải được thành kiểm tra tính bị chặn và tính cưỡng bức.

### 2. Trực giác bổ sung và các kết nối

Định lý Lax–Milgram nối trực tiếp giải tích hàm với mô hình năng lượng vật lý: khi dạng song tuyến tính bị chặn và cưỡng bức, bài toán có nghiệm duy nhất ổn định theo dữ liệu. Một lỗi phổ biến là cho rằng tính bị chặn đã đủ, trong khi chính tính cưỡng bức mới là điều kiện khóa nghiệm.

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

Trên $$ H_0^1(0,1) $$, xét:
$$
a(u,v)=\int_0^1 (u'v' + uv)\,dx, \qquad \ell(v)=\int_0^1 f v\,dx.
$$
Dạng $$ a $$ bị chặn và cưỡng bức theo chuẩn $$ H^1 $$. Do đó, với mọi $$ f \in L^2(0,1) $$, tồn tại duy nhất $$ u \in H_0^1(0,1) $$ sao cho $$ a(u,v)=\ell(v) $$ với mọi $$ v \in H_0^1(0,1) $$. Đây là khuôn mẫu tiêu chuẩn cho nhiều PDE elliptic tuyến tính.

### 6. Phân tầng độ khó

**Bậc đại học.** Liên hệ định lý Lax–Milgram với hệ phương trình tuyến tính đối xứng xác định dương.

**Bậc sau đại học.** Kết nối với định lý biểu diễn Riesz, bài toán điểm yên ngựa và điều kiện inf–sup.

## Video tham khảo

- xem trước: [Peter Lax - Lax-Milgram Theorem](https://www.youtube.com/watch?v=d6lx6kKV9-E) — Simons Foundation, tiếng Anh. Peter Lax chia sẻ trực tiếp về định lý Lax–Milgram trong buổi nói chuyện tại Simons Foundation.
- [Lax-Milgram lemma](https://www.youtube.com/watch?v=w8QjyVug78M) — Numerical Analysis by Julian Roth, tiếng Anh. Phát biểu và chứng minh bổ đề Lax–Milgram thông qua tính liên tục và tính cưỡng bức.
- [Lax-Milgram, application to Poisson equation.](https://www.youtube.com/watch?v=s5P3e1FhpTk) — Learn Maths with Dr Alex, tiếng Anh. Minh họa áp dụng định lý Lax–Milgram cho phương trình Poisson.
