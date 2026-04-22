---
layout: post
title: "Không Gian Sobolev"
chapter: '12'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: required
---

![Trực giác về Sobolev space và gradient yếu]({{ site.imgurl }}/chapter_img/chapter12/03_sobolev_spaces.svg )

## Mục tiêu

Bài này xây dựng không gian Sobolev như nơi ta đo đồng thời bản thân hàm và các đạo hàm yếu của nó. Sau bài học, sinh viên cần hiểu định nghĩa $$ W^{k,p} $$, ý nghĩa đặc biệt của $$ H^k=W^{k,2} $$, vai trò của $$ H^1_0 $$ trong bài toán biên, và trực giác vì sao nhúng Sobolev tạo cầu nối giữa năng lượng và tính trơn.

## Kiến thức nền

Sinh viên cần nắm không gian $$ L^p $$, đạo hàm yếu, chuẩn, tích vô hướng, và trực giác cơ bản về bài toán biên Dirichlet. Cũng nên nhớ rằng trong PDE, “trơn” không phải lúc nào cũng là yêu cầu ban đầu mà thường là điều phải suy ra sau.

## Dẫn nhập

Khi giải PDE, chỉ biết một hàm có tích phân hữu hạn thường chưa đủ. Ta còn cần kiểm soát độ dốc, độ cong, hay các đạo hàm cao hơn. Nhưng nếu cứ đòi đạo hàm cổ điển, ta sẽ loại bỏ quá nhiều nghiệm quan trọng. Không gian Sobolev ra đời để giải quyết đúng chỗ căng đó: đủ rộng để chứa nghiệm yếu, nhưng đủ chặt để còn mang cấu trúc hình học và năng lượng.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một tấm vải căng. Để biết nó “êm” hay “nhăn”, không chỉ cần nhìn độ cao của vải mà còn cần nhìn độ dốc thay đổi thế nào. Chuẩn Sobolev đo cả hai thứ đó cùng lúc: mức độ lớn của hàm và mức độ lớn của các đạo hàm yếu.

### Cách hình ảnh

Một đồ thị có thể liên tục nhưng gợn sóng rất mạnh, hoặc ngược lại có giá trị lớn nhưng thay đổi rất chậm. Không gian Sobolev phân biệt được hai trường hợp đó vì nó nhìn cả chiều cao lẫn gradient. Trong lớp học, nên vẽ hai hàm có cùng chuẩn $$ L^2 $$ nhưng gradient rất khác nhau để sinh viên thấy chỉ dùng $$ L^2 $$ là chưa đủ.

### Cách hình thức

Với $$ k\in\mathbb{N} $$ và $$ 1\le p\le\infty $$, ta định nghĩa

$$
W^{k,p}(\Omega)=\left\{u\in L^p(\Omega):D^\alpha u\in L^p(\Omega)\ \text{với mọi }\lvert \alpha\rvert\le k\right\},
$$

trong đó các đạo hàm hiểu theo nghĩa yếu.

Khi $$ p=2 $$, ta viết $$ H^k(\Omega)=W^{k,2}(\Omega) $$. Đặc biệt,

$$
\lVert u\rVert_{H^1}^2=\lVert u\rVert_{L^2}^2+\lVert \nabla u\rVert_{L^2}^2.
$$

Không gian $$ H^1_0(\Omega) $$ là bao đóng của $$ C_c^\infty(\Omega) $$ trong chuẩn $$ H^1 $$ và thường diễn tả điều kiện biên Dirichlet đồng nhất.

## Ngộ nhận thường gặp

### “Sobolev space chỉ là $$ L^p $$ của đạo hàm”

Chưa đủ. Ta cần cả hàm và mọi đạo hàm yếu đến bậc yêu cầu đều nằm trong $$ L^p $$.

### “Nếu hàm không trơn thì không thể thuộc Sobolev”

Sai. Rất nhiều hàm có góc nhọn, như $$ \lvert x\rvert $$ trên khoảng hữu hạn, vẫn thuộc $$ H^1 $$.

### “$$ H^1_0 $$ nghĩa là hàm bằng 0 tại mọi điểm biên theo nghĩa cổ điển”

Không nhất thiết. Điều kiện biên trong Sobolev được hiểu qua trace hoặc qua phép đóng của các hàm trơn hỗ compact.

### “Nhúng Sobolev luôn cho tính liên tục”

Sai. Kết quả nhúng phụ thuộc mạnh vào bậc đạo hàm, số chiều và chỉ số $$ p $$.

## Tiến trình học

### Bước 1: Bắt đầu từ đạo hàm yếu

Nhắc lại rằng đạo hàm yếu cho phép nói về vi phân dù hàm không trơn. Sobolev space chỉ đơn giản là tập hợp những hàm có đủ đạo hàm yếu khả tích.

### Bước 2: Tập trung vào $$ H^1 $$

Đây là không gian xuất hiện thường xuyên nhất trong PDE elliptic. Sinh viên nên thật quen với

$$
\lVert u\rVert_{H^1}^2=\lVert u\rVert_{L^2}^2+\lVert \nabla u\rVert_{L^2}^2.
$$

### Bước 3: Giới thiệu $$ H^1_0 $$

Giải thích đây là “ngôi nhà tự nhiên” của nhiều bài toán Dirichlet đồng nhất.

### Bước 4: Nêu trực giác về nhúng Sobolev

Kiểm soát đủ nhiều đạo hàm yếu thì hàm sẽ bớt hoang dã hơn. Đây là cầu nối giữa năng lượng và tính trơn.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao $$ \lvert x\rvert $$ thuộc $$ H^1(-1,1) $$ không?
- Sinh viên có phân biệt được $$ H^1 $$ và $$ H^1_0 $$ không?
- Sinh viên có thấy vì sao số chiều ảnh hưởng đến nhúng Sobolev không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm tuyến tính trên khoảng

Xét $$ u(x)=x $$ trên $$ (0,1) $$. Ta có $$ u\in L^2(0,1) $$ và đạo hàm yếu $$ u'=1\in L^2(0,1) $$. Vì vậy $$ u\in H^1(0,1) $$. Tuy nhiên, vì $$ u(0)\ne 0 $$ và $$ u(1)\ne 0 $$ nên $$ u\notin H^1_0(0,1) $$.

### Ví dụ 2: Hàm giá trị tuyệt đối

Xét $$ u(x)=\lvert x\rvert $$ trên $$ (-1,1) $$.

- Hàm thuộc $$ L^2(-1,1) $$.
- Đạo hàm yếu là hàm bằng $$ -1 $$ bên trái và $$ 1 $$ bên phải, thuộc $$ L^2(-1,1) $$.

Vậy $$ \lvert x\rvert\in H^1(-1,1) $$.

### Ví dụ 3: Hàm có singularity mạnh

Xét $$ u(x)=x^{-1/2} $$ trên $$ (0,1) $$.

Ta đã biết $$ u\notin L^2(0,1) $$, nên chắc chắn $$ u\notin H^1(0,1) $$.

Ví dụ này nhấn mạnh rằng muốn thuộc Sobolev, trước hết chính hàm phải đủ khả tích.

### Ví dụ 4: Hàm thử trơn hỗ compact

Nếu $$ u\in C_c^\infty(\Omega) $$ thì mọi đạo hàm của $$ u $$ đều trơn và có hỗ compact, nên thuộc mọi $$ L^p $$ trên miền bị chặn. Do đó $$ u\in W^{k,p}(\Omega) $$ với mọi $$ k $$ và mọi $$ p $$ hữu hạn. Đây là lớp hàm mẫu để xây dựng các không gian Sobolev bằng phép đóng.

## Câu hỏi khái niệm

1. Vì sao $$ H^1 $$ là không gian tự nhiên hơn $$ C^1 $$ trong nhiều bài toán PDE?
2. Tại sao chuẩn $$ H^1 $$ phải gồm cả phần $$ L^2 $$ của chính hàm lẫn của gradient?
3. Điều gì khiến kết quả nhúng Sobolev phụ thuộc vào số chiều không gian?

## Bài toán ứng dụng

1. Trong bài toán màng đàn hồi, vì sao năng lượng biến dạng thường liên quan trực tiếp đến $$ \lVert \nabla u\rVert_{L^2} $$?
2. Trong xử lý ảnh, việc phạt gradient trong các mô hình làm mượt ảnh liên hệ thế nào với chuẩn Sobolev?
3. Trong cơ học chất rắn, tại sao trường dịch chuyển có năng lượng hữu hạn thường được đặt trong một không gian Sobolev thay vì không gian hàm trơn?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một hàm có góc nhọn, em có nghĩ nó vẫn có “năng lượng” hữu hạn không?
- Tại sao bài toán biên lại cần một không gian như $$ H^1_0 $$ thay vì chỉ $$ H^1 $$?
- Một chuẩn chỉ đo bản thân hàm có đủ để kiểm soát hành vi vi phân không?

### Hoạt động gợi ý

- Cho sinh viên phân loại các hàm mẫu vào $$ L^2 $$, $$ H^1 $$, $$ H^1_0 $$.
- So sánh hai hàm có cùng chuẩn $$ L^2 $$ nhưng gradient khác nhau trên đồ thị.
- Tổ chức thảo luận nhóm về ý nghĩa vật lý của gradient trong năng lượng.

### Cách tăng tham gia

- Yêu cầu sinh viên diễn đạt định nghĩa $$ H^1 $$ bằng lời không dùng ký hiệu.
- Cho dự đoán trước khi tính xem một hàm có thuộc $$ H^1 $$ hay không.
- Để mỗi nhóm tự tạo một ví dụ “thuộc $$ H^1 $$ nhưng không trơn”.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm việc chủ yếu trong một chiều trước khi lên nhiều chiều.
- Dùng các ví dụ quen thuộc như $$ x $$, $$ \lvert x\rvert $$, $$ x^2 $$.
- Nhấn mạnh “Sobolev = hàm + đạo hàm yếu khả tích”.

### Thử thách cho sinh viên khá giỏi

- Chứng minh $$ H^1(\Omega) $$ là Hilbert.
- Tìm hiểu ý tưởng trace cho $$ H^1 $$.
- Phân tích trường hợp nhúng Sobolev tới $$ L^q $$ trong các số chiều khác nhau.

## Ghi nhớ nhanh

Không gian Sobolev là nơi ta kiểm soát cả giá trị của hàm và độ lớn của các đạo hàm yếu. Nó là khung làm việc tự nhiên cho nghiệm yếu, năng lượng và bài toán biên trong PDE hiện đại.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chuyển vị đàn hồi hữu hạn năng lượng
- Bài toán: Trong cơ học liên tục, điều quan trọng thường là biến dạng có bình phương khả tích chứ không nhất thiết trơn cổ điển.
- Mô hình: Không gian $$ H^1(\Omega) $$ gom các hàm và gradient yếu đều thuộc $$ L^2 $$.
- Giả thiết và giới hạn: Mô hình tuyến tính, năng lượng biến dạng bậc hai.
- Diễn giải: Sobolev spaces là ngôn ngữ tự nhiên của năng lượng đàn hồi.

#### Dẫn nhiệt và dòng thấm
- Bài toán: Nhiệt độ hoặc áp suất trong môi trường gồ ghề có thể không trơn nhưng vẫn có gradient bình phương khả tích.
- Mô hình: Tìm nghiệm trong $$ H^1 $$ thay vì trong lớp hàm cổ điển.
- Giả thiết và giới hạn: Miền và hệ số có thể không đủ mượt.
- Diễn giải: Sobolev spaces cho phép PDE sống tốt trên miền thực tế hơn.

### 2. Trực giác bổ sung và các kết nối

Không gian Sobolev đo đồng thời kích thước của hàm và kích thước của đạo hàm yếu. Vì vậy nó nằm giữa thế giới "quá thô" của $$ L^2 $$ và thế giới "quá mượt" của $$ C^1 $$. Một bẫy phổ biến là đồng nhất $$ H^1 $$ với hàm khả vi cổ điển; thật ra rất nhiều hàm chỉ có đạo hàm theo nghĩa yếu.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
u = np.abs(x - 0.5)
v = x * (1 - x)

du = np.gradient(u, x)
dv = np.gradient(v, x)

print("Approx H1 seminorm of u:", np.sqrt(np.trapz(du**2, x)))
print("Approx H1 seminorm of v:", np.sqrt(np.trapz(dv**2, x)))

plt.plot(x, u, label="u=|x-1/2|")
plt.plot(x, v, label="v=x(1-x)")
plt.legend()
plt.title("Hai ham khong tron giong nhau nhung van nam trong H1(0,1)")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Sobolev space intuition H1 finite energy
- search: weak gradient visualization Sobolev spaces
- search: finite element Sobolev space motivation

### 5. Bài toán mẫu có bối cảnh thực

Hàm
$$ u(x)=\lvert x-\tfrac12\rvert $$
trên $$ [0,1] $$ không khả vi cổ điển tại $$ x=\tfrac12 $$, nhưng đạo hàm yếu của nó bằng $$ -1 $$ ở bên trái và $$ 1 $$ ở bên phải, nên thuộc $$ L^2(0,1) $$. Do đó
$$ u \in H^1(0,1). $$
Đây là ví dụ điển hình cho việc Sobolev spaces chấp nhận các nghiệm có góc nhọn nhưng vẫn hữu hạn năng lượng.

### 6. Phân tầng độ khó

**Bậc đại học.** Làm quen với $$ H^1 $$ như không gian hàm hữu hạn năng lượng.

**Bậc sau đại học.** Kết nối với trace theorem, compact embeddings và Rellich-Kondrachov.
