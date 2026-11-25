---
layout: post
title: "06-01 Ôn tập Chuỗi Lũy thừa"
chapter: '06'
order: 1
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

Trước khi giải phương trình vi phân bằng chuỗi vô hạn, bạn cần sử dụng thành thạo "bộ cờ lê đại số" của **chuỗi lũy thừa** $\sum_{n=0}^{\infty} a_n (x - x_0)^n$: tìm bán kính hội tụ để biết nghiệm có nghĩa ở đâu, lấy đạo hàm từng số hạng, và đặc biệt là kỹ thuật **dịch chỉ số (index shifting)** để cộng gộp các tổng có lũy thừa lệch nhau về cùng một mẫu $x^k$.

## Kiến thức cần nhớ: Bốn thao tác xương sống với Chuỗi Lũy thừa

1. **Bán kính hội tụ $R$ (Tiêu chuẩn D'Alembert / Cauchy)**:
   $R = \lim_{n\to\infty} \left\vert \frac{a_n}{a_{n+1}} \right\vert$. Chuỗi hội tụ tuyệt đối khi $\vert x - x_0 \vert < R$ và phân kỳ khi $\vert x - x_0 \vert > R$.
2. **Đạo hàm và Tích phân từng số hạng bên trong khoảng hội tụ**:
   $y'(x) = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1}$ và $y''(x) = \sum_{n=2}^{\infty} n(n-1) a_n (x - x_0)^{n-2}$ đều giữ nguyên **đúng bán kính hội tụ $R$**.
3. **Kỹ thuật dịch chỉ số (Index Shifting)**:
   Đặt $k = n - 2$ (suy ra $n = k + 2$) để biến $\sum_{n=2}^{\infty} n(n-1) a_n x^{n-2}$ thành $\sum_{k=0}^{\infty} (k+2)(k+1) a_{k+2} x^k$—giúp mọi tổng cùng bắt đầu từ $x^k$ để đồng nhất hệ số!
4. **Định lý đồng nhất hệ số (Identity Theorem)**:
   Nếu $\sum_{k=0}^{\infty} c_k (x - x_0)^k = 0$ trên một khoảng mở quanh $x_0$, thì **mọi hệ số $c_k = 0$ với mọi $k \ge 0$**!

## Mục tiêu

Bài học này ôn tập chuỗi lũy thừa theo đúng định hướng của chương nghiệm chuỗi: không chỉ ghi nhớ công thức mà hiểu chuỗi lũy thừa như một ngôn ngữ mô tả hành vi cục bộ của hàm số. Sau bài học, sinh viên cần biết nhận dạng chuỗi lũy thừa, xác định bán kính hội tụ, thực hiện đạo hàm và tích phân từng số hạng, đồng thời hiểu vì sao dãy hệ số chuỗi trở thành ẩn số trung tâm khi giải phương trình vi phân.

## Kiến thức nền

Sinh viên nên nắm vững giới hạn, chuỗi số, đạo hàm, tích phân và khai triển Taylor cơ bản. Nếu chưa thành thạo chuỗi hình học hoặc tiêu chuẩn tỉ số, cần ôn lại trước vì hầu hết phép biến đổi trong chương này đều dựa trên các công cụ đó.

## Dẫn nhập

![Chuỗi lũy thừa và miền hội tụ]({{ site.imgurl }}/chapter_img/chapter06/01_power_series_review.svg)

Khi khảo sát một hàm số quanh một điểm, ta thường muốn có một biểu diễn vừa gọn gàng vừa chính xác. Chuỗi lũy thừa đáp ứng yêu cầu đó bằng cách thay một hàm phức tạp bằng tổng vô hạn của các lũy thừa cơ bản. Đáng chú ý là trong nhiều trường hợp, đây không chỉ là phép xấp xỉ mà là biểu diễn chính xác của hàm trong cả một lân cận.

Trong chương này, thay vì tìm nghiệm dưới dạng tổ hợp các hàm sơ cấp quen thuộc như sin, cos hay hàm mũ, ta giả sử nghiệm có dạng chuỗi lũy thừa rồi dùng chính phương trình vi phân để xác định các hệ số. Vì vậy, ôn tập chuỗi lũy thừa là nền tảng trực tiếp cho toàn bộ chương.

### Giải thích: Thực hành dịch chỉ số và gộp 2 tổng thành 1 tổng duy nhất

Cần viết biểu thức $S(x) = \sum_{n=2}^{\infty} n(n-1) a_n x^{n-2} + \sum_{n=0}^{\infty} a_n x^n$ thành một chuỗi duy nhất theo $x^k$:
1. **Tổng thứ nhất**: Đặt $k = n - 2 \implies n = k + 2$. Khi $n = 2$ thì $k = 0$:
   $$\sum_{n=2}^{\infty} n(n-1) a_n x^{n-2} = \sum_{k=0}^{\infty} (k+2)(k+1) a_{k+2} x^k.$$
2. **Tổng thứ hai**: Chỉ cần đổi tên biến giả $n \to k$: $\sum_{k=0}^{\infty} a_k x^k$.
3. **Gộp chung vì cả hai đã cùng bắt đầu từ $k = 0$ và cùng lũy thừa $x^k$**:
   $$S(x) = \sum_{k=0}^{\infty} \big[(k+2)(k+1) a_{k+2} + a_k\big] x^k.$$
4. **Áp dụng ngay**: Nếu $S(x) = 0$ (chính là phương trình $y'' + y = 0$!), định lý đồng nhất hệ số lập tức cho hệ thức truy hồi:
   $$a_{k+2} = -\frac{a_k}{(k+2)(k+1)} \qquad (k = 0, 1, 2, \dots).$$

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung việc phóng to bề mặt địa hình quanh một điểm. Ở lân cận gần, bề mặt cong phức tạp có thể được mô tả lần lượt qua độ cao hiện tại, độ dốc, độ cong và các hiệu chỉnh bậc cao hơn. Chuỗi Taylor và chuỗi lũy thừa mô tả hàm số theo đúng cơ chế đó: mỗi hệ số lưu giữ một phần thông tin cục bộ về giá trị, tốc độ biến thiên, độ cong và các đạo hàm bậc cao.

### Cách nhìn hình ảnh

Về mặt đồ thị, chuỗi lũy thừa quanh điểm $$ x_0 $$ tạo ra một dãy đa thức xấp xỉ ngày càng sát hàm gốc khi tăng số hạng. Đa thức bậc 1 cho đường tiếp tuyến, bậc 2 cho parabol bám sát độ cong, còn các bậc cao hơn mô tả hình dạng cục bộ ngày càng chính xác. Bán kính hội tụ cho biết khoảng cách tối đa quanh $$ x_0 $$ mà biểu diễn chuỗi này còn có hiệu lực.

### Cách nhìn hình thức

Một chuỗi lũy thừa khai triển quanh điểm $$ x_0 $$ có dạng

$$ \sum_{n=0}^{\infty} a_n (x-x_0)^n. $$

Tồn tại một số thực không âm $$ R $$ (hoặc $$ R=\infty $$), gọi là **bán kính hội tụ**, sao cho chuỗi hội tụ tuyệt đối với mọi $$ \lvert x-x_0\rvert<R $$ và phân kỳ với mọi $$ \lvert x-x_0\rvert>R $$. Bên trong khoảng hội tụ, ta được phép đạo hàm và tích phân từng số hạng:

$$
\frac{d}{dx}\sum_{n=0}^{\infty} a_n (x-x_0)^n
=
\sum_{n=1}^{\infty} n a_n (x-x_0)^{n-1},
$$

$$
\int \sum_{n=0}^{\infty} a_n (x-x_0)^n \, dx
=
C+\sum_{n=0}^{\infty} \frac{a_n}{n+1}(x-x_0)^{n+1}.
$$

Nếu một hàm bằng đúng tổng chuỗi Taylor của chính nó trong một lân cận của $$ x_0 $$, ta gọi hàm đó là **hàm giải tích** tại $$ x_0 $$.

## Những ngộ nhận thường gặp

- "Chuỗi lũy thừa chỉ là phép xấp xỉ gần đúng." Không hẳn. Bên trong miền hội tụ của một hàm giải tích, chuỗi biểu diễn chính xác hàm đó.
- "Chỉ cần viết vài số hạng đầu là đủ để hiểu chuỗi." Sai. Bán kính hội tụ và hành vi tại biên khoảng hội tụ vẫn rất quan trọng.
- "Nếu chuỗi hội tụ tại một điểm thì luôn hội tụ quanh mọi điểm lân cận tùy ý." Không đúng. Bán kính hội tụ bị giới hạn bởi khoảng cách từ tâm khai triển đến điểm kỳ dị gần nhất trong mặt phẳng phức, chứ không chỉ nhìn trên trục thực.
- "Lúc nào cũng có thể đạo hàm từng số hạng của chuỗi." Sai nếu đứng ngoài khoảng hội tụ; quy tắc đạo hàm từng số hạng chỉ đảm bảo hợp lệ bên trong bán kính hội tụ.

## Tiến trình học tập đề xuất

### Bước 1: Ôn tập chuỗi hình học

Nắm chắc khai triển

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty} x^n, \qquad \lvert x\rvert<1.
$$

Đây là khai triển nền tảng để suy ra nhiều chuỗi lũy thừa khác.

### Bước 2: Xác định bán kính hội tụ

Thành thạo tiêu chuẩn tỉ số hoặc tiêu chuẩn căn để tìm khoảng hội tụ của chuỗi.

### Bước 3: Luyện tập thao tác đại số trên chuỗi

Thực hành đạo hàm, tích phân, đổi chỉ số tổng, nhân với $$ x $$ và cộng trừ các chuỗi — những bước lặp lại thường xuyên khi giải ODE.

### Bước 4: Liên hệ với khai triển Taylor

Hiểu rằng các hệ số chuỗi không tùy ý mà phản ánh trực tiếp các đạo hàm của hàm tại tâm khai triển.

### Các điểm kiểm tra

- Sinh viên có viết đúng dạng chuỗi lũy thừa quanh một điểm $$ x_0 $$ bất kỳ (không chỉ $$ x_0=0 $$) hay không.
- Sinh viên có xác định được bán kính hội tụ bằng tiêu chuẩn tỉ số hay không.
- Sinh viên có đổi chỉ số tổng chính xác khi đạo hàm và đồng nhất bậc lũy thừa hay không.
- Sinh viên có giải thích được vì sao chuỗi lũy thừa là công cụ tự nhiên để tìm nghiệm ODE hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Chuỗi hình học cơ bản

Xét hàm

$$ f(x)=\frac{1}{1-x}. $$

Ta có khai triển

$$
f(x)=1+x+x^2+x^3+\cdots=\sum_{n=0}^{\infty}x^n,
\qquad \lvert x\rvert<1.
$$

Bán kính hội tụ là $$ R=1 $$. Chỉ từ chuỗi cơ bản này, ta có thể sinh ra nhiều khai triển khác thông qua đạo hàm, tích phân, đổi biến và nhân đại số.

### Ví dụ 2: Đạo hàm từng số hạng

Xuất phát từ

$$ \frac{1}{1-x}=\sum_{n=0}^{\infty}x^n, $$

lấy đạo hàm hai vế theo $$ x $$:

$$ \frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}n x^{n-1}. $$

Nhân hai vế với $$ x $$:

$$ \frac{x}{(1-x)^2}=\sum_{n=1}^{\infty}n x^n. $$

Ví dụ này cho thấy ta có thể biến đổi trực tiếp trên chuỗi sẵn có để biểu diễn các hàm mới mà không cần tính lại từ định nghĩa Taylor.

### Ví dụ 3: Tìm bán kính hội tụ

Xét chuỗi

$$ \sum_{n=0}^{\infty} \frac{n+1}{3^n} x^n. $$

Áp dụng tiêu chuẩn tỉ số:

$$
\lim_{n\to\infty}
\left\vert
\frac{\frac{n+2}{3^{n+1}}x^{n+1}}{\frac{n+1}{3^n}x^n}
\right\vert
=
\lim_{n\to\infty}\frac{n+2}{n+1}\frac{\lvert x\rvert}{3}
=
\frac{\lvert x\rvert}{3}.
$$

Chuỗi hội tụ khi

$$
\frac{\lvert x\rvert}{3}<1
\quad \Longleftrightarrow \quad
\lvert x\rvert<3.
$$

Vậy bán kính hội tụ là $$ R=3 $$. Ta tách bạch hai bước: xác định bán kính hội tụ trước, sau đó mới xét riêng hai đầu mút nếu cần.

### Ví dụ 4: Chuỗi Taylor của hàm mũ

Từ công thức Taylor quanh $$ 0 $$:

$$ e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}. $$

Áp dụng tiêu chuẩn tỉ số:

$$
\lim_{n\to\infty}
\left\vert
\frac{x^{n+1}/(n+1)!}{x^n/n!}
\right\vert
=
\lim_{n\to\infty}\frac{\lvert x\rvert}{n+1}=0.
$$

Chuỗi hội tụ với mọi $$ x\in\mathbb{R} $$, do đó $$ R=\infty $$. Ví dụ này cho thấy bán kính hội tụ có thể là vô hạn.

### Ví dụ 5: Dùng chuỗi lũy thừa cho ODE

Xét bài toán $$ y''-y=0 $$. Đặt

$$ y=\sum_{n=0}^{\infty}a_n x^n, $$

khi đó

$$ y''=\sum_{n=2}^{\infty}n(n-1)a_n x^{n-2}. $$

Đổi chỉ số tổng để đưa về cùng lũy thừa $$ x^n $$:

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n. $$

Thay vào phương trình ban đầu:

$$
\sum_{n=0}^{\infty}
\left[(n+2)(n+1)a_{n+2}-a_n\right]x^n=0.
$$

Đồng nhất hệ số bằng 0, ta thu được hệ thức truy hồi:

$$ a_{n+2}=\frac{a_n}{(n+2)(n+1)}. $$

Qua đó, phương trình vi phân đã được chuyển thành một quy tắc đại số xác định các hệ số chuỗi.

## Câu hỏi khái niệm

1. Vì sao bán kính hội tụ quan trọng hơn việc chỉ viết vài số hạng đầu của chuỗi?
2. Vì sao tính chất được phép đạo hàm từng số hạng trong khoảng hội tụ là nền tảng của phương pháp nghiệm chuỗi?
3. Chuỗi Taylor thể hiện mối liên hệ nào giữa các đạo hàm tại một điểm và hình dạng cục bộ của hàm số?

## Bài toán ứng dụng

1. Trong kỹ thuật, cảm biến thường đo tín hiệu xung quanh một trạng thái cân bằng. Hãy giải thích vì sao chuỗi Taylor phù hợp để mô hình hóa tín hiệu trong vùng lân cận đó.
2. Trong cơ học, thế năng gần vị trí cân bằng thường được xấp xỉ bằng đa thức bậc hai. Hãy liên hệ cách làm này với tư tưởng chuỗi lũy thừa.
3. Trong tính toán số, vì sao các hàm sơ cấp như sin, cos hay hàm mũ thường được tính xấp xỉ bằng đa thức cắt cụt từ chuỗi?

## Chiến lược giảng dạy tương tác

- Đặt câu hỏi mở đầu: nếu chỉ biết giá trị và độ dốc của hàm tại một điểm, ta có thể dự đoán đồ thị ở lân cận chính xác đến mức nào?
- Cho sinh viên làm việc nhóm nhanh: từ chuỗi hình học, tự suy ra khai triển của $$ \frac{1}{(1-x)^2} $$ và $$ \ln(1+x) $$.
- Mời một nhóm trình bày từng bước quy trình đổi chỉ số tổng vì đây là thao tác dễ gây nhầm lẫn nhất.
- Vẽ chồng đồ thị hàm gốc và các đa thức tổng riêng để sinh viên thấy trực quan quá trình chuỗi bám sát hàm gốc.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cung cấp một quy trình thao tác chuẩn: viết dạng chuỗi, tìm bán kính hội tụ, đạo hàm từng số hạng, đổi chỉ số tổng rồi đồng nhất hệ số. Quy trình nhất quán giúp giảm sai sót kỹ thuật.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên giải thích vì sao hàm

$$ \frac{1}{1+x^2} $$

có chuỗi lũy thừa quanh 0 với bán kính hội tụ $$ R=1 $$ dù hàm hoàn toàn trơn trên toàn trục thực. Điều này dẫn tới vai trò của các điểm kỳ dị phức ($$ x=\pm i $$) trong việc xác định bán kính hội tụ.

## Tóm tắt dễ nhớ

Chuỗi lũy thừa biểu diễn hàm số dưới dạng tổng vô hạn các lũy thừa quanh một điểm. Bên trong bán kính hội tụ, ta được phép cộng, đạo hàm và tích phân từng số hạng; nhờ đó, bài toán giải phương trình vi phân được chuyển thành bài toán tìm dãy hệ số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động góc nhỏ trong cơ học
- Bài toán: Với con lắc phi tuyến
$$ \theta''+\frac{g}{L}\sin\theta=0, $$
cần xấp xỉ phương trình khi góc lệch $$ \theta $$ nhỏ.
- Mô hình chuỗi:
$$
\sin\theta=\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots
$$
nên ở bậc xấp xỉ đầu tiên ta có
$$ \theta''+\frac{g}{L}\theta\approx 0. $$
- Giả thiết và giới hạn: Chỉ chính xác khi góc lệch nhỏ; khi góc lớn, các số hạng bậc cao đóng vai trò đáng kể.
- Diễn giải: Chuỗi lũy thừa là cầu nối tự nhiên giữa mô hình phi tuyến và mô hình tuyến tính quen thuộc.

#### Xấp xỉ đáp ứng sớm của hệ kỹ thuật
- Bài toán: Xấp xỉ đáp ứng gần $$ t=0 $$ của một hệ tuyến tính chịu kích thích giải tích bằng vài số hạng đầu của chuỗi.
- Mô hình:
$$
y''+y=e^t,\qquad
e^t=\sum_{n=0}^{\infty}\frac{t^n}{n!}.
$$
- Giả thiết và giới hạn: Phù hợp khi chỉ cần phân tích hành vi cục bộ gần thời điểm ban đầu.
- Diễn giải: Chuỗi lũy thừa cung cấp biểu diễn gọn cho đáp ứng ngắn hạn mà chưa cần nghiệm đóng toàn cục.

### 2. Trực giác bổ sung và các kết nối

Chuỗi lũy thừa có thể xem như "đa thức bậc vô hạn" lưu giữ thông tin cục bộ của hàm số. Trong chương này, mỗi đạo hàm trong ODE đều chuyển hóa thành mối liên hệ đại số giữa các hệ số. Hai lỗi phổ biến cần tránh là mặc định bán kính hội tụ luôn bằng vô hạn và làm lệch một bậc khi đạo hàm hoặc đổi chỉ số tổng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.2, 1.2, 500)
partial_1 = 1 + x
partial_3 = 1 + x + x**2 + x**3
partial_8 = sum(x**k for k in range(9))
exact = 1 / (1 - x)

plt.plot(x, exact, label="1/(1-x)", color="black")
plt.plot(x, partial_1, "--", label="bac 1")
plt.plot(x, partial_3, "--", label="bac 3")
plt.plot(x, partial_8, "--", label="bac 8")
plt.ylim(-4, 8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Tong rieng cua chuoi hinh hoc")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: power series radius of convergence visualization
- search: geometric series partial sums plot
- search: small angle approximation pendulum series

### 5. Bài toán mẫu có bối cảnh thực

Từ khai triển
$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n,\qquad \lvert x\rvert<1,
$$
đạo hàm hai vế cho
$$ \frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}n x^{n-1}. $$
Ví dụ này minh họa nguyên lý cơ bản của chương: trong miền hội tụ, các phép đạo hàm và tích phân được chuyển trực tiếp thành thao tác trên hệ số chuỗi.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo tìm bán kính hội tụ, đổi chỉ số tổng, đạo hàm và tích phân từng số hạng.

**Bậc sau đại học.** Nhấn mạnh khái niệm hàm giải tích, miền hội tụ trên mặt phẳng phức và vai trò của các điểm kỳ dị trong việc xác định $$ R $$.

## Video tham khảo

- Xem trước: [Taylor series | Chapter 11, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — 3Blue1Brown, tiếng Anh. Chuỗi Taylor làm nền tảng trực quan cho việc xây dựng nghiệm chuỗi cục bộ.
- [Taylor Series and Power Series Made Easy (with Pictures): Review of Calculus](https://www.youtube.com/watch?v=ebfOSDj4j3I) — Steve Brunton, tiếng Anh. Ôn tập trực quan chuỗi Taylor và chuỗi lũy thừa trước khi áp dụng cho ODE.
- [Taylor Series of the Exponential Function and Euler's Formula!](https://www.youtube.com/watch?v=H0Zbg_CqMCs) — Steve Brunton, tiếng Anh. Chuỗi hàm mũ — ví dụ chuẩn thường dùng để đối chiếu với các hệ thức truy hồi về sau.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: ôn tập chuỗi lũy thừa và chuỗi Taylor trong bối cảnh phương trình vi phân.
- Ross, Chương 6: trình bày gọn gàng các thao tác chuỗi thường dùng khi giải ODE.
