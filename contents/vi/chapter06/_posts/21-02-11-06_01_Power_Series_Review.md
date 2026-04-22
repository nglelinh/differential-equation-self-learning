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

## Mục tiêu

Bài học này ôn lại chuỗi lũy thừa theo đúng tinh thần cần cho chương nghiệm chuỗi: không chỉ nhớ công thức, mà phải hiểu chuỗi lũy thừa như một ngôn ngữ mô tả hành vi cục bộ của hàm số. Sau bài học, sinh viên cần biết nhận dạng một chuỗi lũy thừa, xác định bán kính hội tụ, thao tác với đạo hàm và tích phân từng số hạng, đồng thời hiểu vì sao các hệ số chuỗi trở thành ẩn số trung tâm khi giải phương trình vi phân.

## Kiến thức nền

Sinh viên nên nắm giới hạn, chuỗi số, đạo hàm, tích phân và công thức Taylor cơ bản. Nếu còn yếu ở phần chuỗi hình học hoặc kiểm tra hội tụ bằng tỉ số, nên ôn lại trước, vì hầu như mọi phép biến đổi trong chương này đều dựa trên các kỹ năng đó.

## Dẫn nhập

![Chuỗi lũy thừa và miền hội tụ]({{ site.imgurl }}/chapter_img/chapter06/01_power_series_review.svg)

Khi quan sát một hàm số gần một điểm, ta thường muốn có một mô tả vừa đơn giản vừa đủ chính xác. Chuỗi lũy thừa làm đúng việc đó: nó thay một hàm có thể rất phức tạp bằng tổng vô hạn của những khối quen thuộc là các lũy thừa. Điều đặc biệt là trong nhiều trường hợp, đây không chỉ là xấp xỉ, mà là cách viết chính xác của hàm trong cả một lân cận.

Trong chương này, ta sẽ không đoán nghiệm bằng các hàm sơ cấp quen thuộc như sin, cos hay hàm mũ. Thay vào đó, ta giả sử nghiệm có dạng chuỗi rồi để chính phương trình vi phân chỉ ra các hệ số. Vì vậy, ôn tập chuỗi lũy thừa không phải là phần phụ trợ, mà là bước đặt nền cho toàn bộ chương.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng bạn đang phóng to bản đồ quanh một vị trí cụ thể. Ở mức phóng đại nhỏ, bề mặt cong phức tạp có thể được mô tả bằng một số đặc điểm đơn giản: độ cao hiện tại, độ dốc, độ cong, rồi các hiệu chỉnh tinh hơn. Chuỗi Taylor và chuỗi lũy thừa làm đúng việc đó với hàm số. Mỗi hệ số là một mảnh thông tin cục bộ: giá trị, tốc độ thay đổi, mức độ cong, và các hiệu ứng bậc cao.

### Cách nhìn hình ảnh

Về mặt đồ họa, chuỗi lũy thừa quanh điểm $$ x_0 $$ là một họ các đường cong xấp xỉ ngày càng tốt khi lấy thêm nhiều số hạng. Đồ thị của đa thức bậc 1 cho ta tiếp tuyến, bậc 2 cho ta một parabol ôm sát hơn, bậc 3 và cao hơn cho ta hình dạng cục bộ ngày càng giống hàm gốc. Bán kính hội tụ cho biết ta có thể tin vào bức tranh đó xa đến đâu trước khi chuỗi “mất hiệu lực”.

### Cách nhìn hình thức

Một chuỗi lũy thừa quanh điểm $$ x_0 $$ có dạng

$$ \sum_{n=0}^{\infty} a_n (x-x_0)^n. $$

Tồn tại một số thực không âm $$ R $$, gọi là bán kính hội tụ, sao cho chuỗi hội tụ tuyệt đối với mọi $$ \lvert x-x_0\rvert<R $$ và phân kỳ với mọi $$ \lvert x-x_0\rvert>R $$. Trong miền hội tụ, ta được phép đạo hàm và tích phân từng số hạng:

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

Nếu một hàm bằng chuỗi Taylor của chính nó trong một lân cận, ta gọi hàm đó là giải tích tại điểm đang xét.

## Những ngộ nhận thường gặp

- "Chuỗi lũy thừa chỉ là công cụ xấp xỉ gần đúng." Không hẳn. Trong miền hội tụ, chuỗi có thể biểu diễn chính xác hàm.
- "Chỉ cần biết vài số hạng đầu là hiểu hoàn toàn chuỗi." Sai. Hành vi ở biên hội tụ và bán kính hội tụ vẫn rất quan trọng.
- "Nếu chuỗi hội tụ tại một điểm thì phải hội tụ mọi điểm gần đó." Không luôn đúng. Miền hội tụ được quyết định bởi khoảng cách đến điểm kỳ dị gần nhất trong mặt phẳng phức, không chỉ bởi trực giác trên trục thực.
- "Đạo hàm chuỗi luôn được." Sai nếu đứng ngoài miền hội tụ; quy tắc đạo hàm từng số hạng chỉ an toàn bên trong bán kính hội tụ.

## Tiến trình học tập đề xuất

### Bước 1: Ôn chuỗi hình học

Nắm thật chắc khai triển

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty} x^n, \qquad \lvert x\rvert<1.
$$

Đây là "mẹ" của rất nhiều khai triển khác.

### Bước 2: Hiểu bán kính hội tụ

Sinh viên cần biết dùng kiểm tra tỉ số hoặc nghiệm để xác định miền chuỗi có ý nghĩa.

### Bước 3: Luyện thao tác đại số

Đạo hàm, tích phân, đổi chỉ số, nhân với $$ x $$, cộng trừ các chuỗi là các thao tác xuất hiện liên tục trong bài toán ODE.

### Bước 4: Liên hệ với Taylor

Hiểu rằng các hệ số chuỗi không phải các con số ngẫu nhiên; chúng phản ánh cấu trúc đạo hàm của hàm tại điểm khai triển.

### Các checkpoint

- Sinh viên có viết đúng chuỗi lũy thừa quanh một điểm bất kỳ, không chỉ quanh 0, hay không.
- Sinh viên có tìm được bán kính hội tụ bằng kiểm tra tỉ số hay không.
- Sinh viên có đổi chỉ số thuần thục khi đạo hàm và so khớp lũy thừa hay không.
- Sinh viên có giải thích được vì sao chuỗi là công cụ tự nhiên cho nghiệm ODE hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Chuỗi hình học cơ bản

Xét hàm

$$ f(x)=\frac{1}{1-x}. $$

Ta biết

$$
f(x)=1+x+x^2+x^3+\cdots=\sum_{n=0}^{\infty}x^n,
\qquad \lvert x\rvert<1.
$$

Từ đây, bán kính hội tụ là $$ R=1 $$. Ý nghĩa sư phạm của ví dụ này là rất lớn: chỉ từ một chuỗi đơn giản, ta có thể sinh ra vô số chuỗi khác bằng đạo hàm, tích phân, thay biến và nhân chia phù hợp.

### Ví dụ 2: Đạo hàm từng số hạng

Từ ví dụ trên,

$$ \frac{1}{1-x}=\sum_{n=0}^{\infty}x^n. $$

Lấy đạo hàm hai vế,

$$ \frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}n x^{n-1}. $$

Nhân thêm $$ x $$,

$$ \frac{x}{(1-x)^2}=\sum_{n=1}^{\infty}n x^n. $$

Ví dụ này cho sinh viên thấy chuỗi không tĩnh. Ta có thể thao tác trên chuỗi để tạo biểu diễn cho các hàm mới mà không cần khởi động lại từ đầu.

### Ví dụ 3: Tìm bán kính hội tụ

Xét chuỗi

$$ \sum_{n=0}^{\infty} \frac{n+1}{3^n} x^n. $$

Áp dụng kiểm tra tỉ số:

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

Vậy bán kính hội tụ là $$ R=3 $$. Đây là ví dụ tốt để tách bạch hai việc: tìm bán kính hội tụ trước, rồi mới xét kỹ các đầu mút nếu cần.

### Ví dụ 4: Chuỗi Taylor của hàm mũ

Từ công thức Taylor quanh 0,

$$ e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}. $$

Dùng kiểm tra tỉ số:

$$
\lim_{n\to\infty}
\left\vert
\frac{x^{n+1}/(n+1)!}{x^n/n!}
\right\vert
=
\lim_{n\to\infty}\frac{\lvert x\rvert}{n+1}=0.
$$

Chuỗi hội tụ với mọi $$ x $$, nên $$ R=\infty $$. Ví dụ này giúp sinh viên nhận ra rằng không phải mọi chuỗi đều có miền hội tụ hữu hạn.

### Ví dụ 5: Chuỗi như bước chuẩn bị cho ODE

Giả sử ta muốn chuẩn bị cho bài toán $$ y''-y=0 $$. Nếu đặt

$$ y=\sum_{n=0}^{\infty}a_n x^n, $$

thì

$$ y''=\sum_{n=2}^{\infty}n(n-1)a_n x^{n-2}. $$

Đổi chỉ số để có cùng lũy thừa:

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n. $$

Thế vào phương trình:

$$
\sum_{n=0}^{\infty}
\left[(n+2)(n+1)a_{n+2}-a_n\right]x^n=0.
$$

Suy ra truy hồi

$$ a_{n+2}=\frac{a_n}{(n+2)(n+1)}. $$

Đây chính là khoảnh khắc sinh viên thấy rõ vai trò của ôn tập chuỗi: ta đã biến một phương trình vi phân thành một quy tắc đại số cho các hệ số.

## Câu hỏi khái niệm

1. Vì sao bán kính hội tụ quan trọng hơn việc chỉ viết ra vài số hạng đầu của chuỗi?
2. Vì sao được phép đạo hàm từng số hạng bên trong miền hội tụ lại là chìa khóa cho phương pháp nghiệm chuỗi?
3. Chuỗi Taylor cho biết điều gì về mối liên hệ giữa đạo hàm tại một điểm và hình dạng cục bộ của hàm?

## Bài toán ứng dụng

1. Trong kỹ thuật, cảm biến thường chỉ đo được tín hiệu gần một trạng thái cân bằng. Hãy giải thích vì sao chuỗi Taylor là công cụ phù hợp để mô tả tín hiệu quanh trạng thái đó.
2. Trong cơ học, thế năng gần vị trí cân bằng thường được xấp xỉ bởi đa thức bậc hai. Hãy liên hệ điều này với tư tưởng chuỗi lũy thừa.
3. Trong tính toán số, vì sao người ta hay dùng chuỗi để xấp xỉ các hàm như sin, cos, hàm mũ trên máy tính?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu chỉ biết giá trị và độ dốc của hàm tại một điểm, ta đoán được đồ thị gần đó đến mức nào?"
- Cho sinh viên làm nhanh bài tập nhóm: từ chuỗi hình học, tự suy ra chuỗi của $$ \frac{1}{(1-x)^2} $$ và $$ \ln(1+x) $$.
- Yêu cầu một nhóm trình bày quy trình đổi chỉ số thật chậm, vì đây là chỗ nhiều sinh viên mất tự tin.
- Vẽ cùng lúc đồ thị hàm gốc và các đa thức cắt ngắn để lớp thấy chuỗi không chỉ là ký hiệu mà là một quá trình "ôm sát" đồ thị.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho các em một bảng quy trình cố định: viết chuỗi, tìm bán kính hội tụ, đạo hàm từng số hạng, đổi chỉ số, so khớp hệ số. Mẫu thao tác nhất quán giúp giảm tải nhận thức đáng kể.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận vì sao hàm

$$ \frac{1}{1+x^2} $$

có chuỗi lũy thừa quanh 0 với bán kính hội tụ bằng 1 dù trên trục thực không có điểm kỳ dị tại $$ x=\pm 1 $$. Điều này mở cánh cửa đến vai trò của các điểm kỳ dị phức trong việc quyết định bán kính hội tụ.

## Tóm tắt dễ nhớ

Chuỗi lũy thừa là cách mô tả hàm bằng các lũy thừa quanh một điểm. Bên trong bán kính hội tụ, ta được phép cộng, đạo hàm và tích phân từng số hạng. Vì vậy khi giải ODE bằng chuỗi, ta biến bài toán tìm hàm thành bài toán tìm các hệ số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động góc nhỏ trong cơ học
- Bài toán: Với con lắc phi tuyến
$$ \theta''+\frac{g}{L}\sin\theta=0, $$
ta muốn xấp xỉ hệ khi $$ \theta $$ nhỏ.
- Mô hình chuỗi:
$$
\sin\theta=\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots
$$
và do đó
$$ \theta''+\frac{g}{L}\theta\approx 0 $$
ở bậc đầu.
- Giả thiết và giới hạn: Chỉ đúng khi góc nhỏ; ra xa cân bằng thì các hạng bậc cao quan trọng.
- Diễn giải: Chuỗi lũy thừa là cầu nối giữa mô hình phi tuyến và mô hình tuyến tính quen thuộc.

#### Xấp xỉ đáp ứng sớm của hệ kỹ thuật
- Bài toán: Một hệ tuyến tính với kích thích giải tích gần $$ t=0 $$ có thể được xấp xỉ bởi vài hạng đầu của chuỗi.
- Mô hình:
$$
y''+y=e^t,\qquad
e^t=\sum_{n=0}^{\infty}\frac{t^n}{n!}.
$$
- Giả thiết và giới hạn: Phù hợp khi chỉ cần mô tả địa phương gần thời điểm đầu.
- Diễn giải: Chuỗi cho ta một mô tả ngắn gọn của đáp ứng mà chưa cần lời giải kín hoàn chỉnh.

### 2. Trực giác bổ sung và các kết nối

Chuỗi lũy thừa là "đa thức vô hạn" lưu giữ thông tin địa phương của hàm. Trong chương này, mỗi đạo hàm của ODE sẽ biến thành quan hệ giữa các hệ số chuỗi. Một bẫy phổ biến là quên rằng bán kính hội tụ không phải vô hạn mặc định; một bẫy khác là thao tác đạo hàm hay đổi chỉ số sai lệch một bậc.

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

Từ
$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n,\qquad \lvert x\rvert<1,
$$
ta đạo hàm được
$$ \frac{1}{(1-x)^2}=\sum_{n=1}^{\infty}n x^{n-1}. $$
Trong ngôn ngữ mô hình hóa, đây là ví dụ cơ bản cho thấy các phép đạo hàm và tích phân có thể được đẩy xuống mức hệ số chuỗi miễn là ta ở trong miền hội tụ.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo bán kính hội tụ, đổi chỉ số, đạo hàm và tích phân từng hạng.

**Bậc sau đại học.** Nhấn mạnh tính giải tích, miền hội tụ trong mặt phức và vai trò của điểm kỳ dị trong việc quyết định $$ R $$.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: ôn tập chuỗi lũy thừa và chuỗi Taylor trong bối cảnh phương trình vi phân.
- Ross, Chương 6: trình bày gọn, rõ các thao tác chuỗi thường gặp trong tính nghiệm.
