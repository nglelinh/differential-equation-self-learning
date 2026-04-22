---
layout: post
title: "07-04 Khai triển theo Hàm riêng"
chapter: '07'
order: 4
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

## Mục tiêu

Bài học này cho thấy vì sao lý thuyết trị riêng và trực giao không chỉ đẹp về mặt lý thuyết mà còn cực kỳ hữu dụng: chúng cho phép biểu diễn một hàm theo hệ hàm riêng của bài toán. Sau bài học, sinh viên cần hiểu khai triển theo hàm riêng như một phiên bản tổng quát của chuỗi Fourier, biết công thức tính hệ số bằng phép chiếu có trọng số, và thấy được cách khai triển này tách một bài toán phức tạp thành các mode độc lập.

## Kiến thức nền

Sinh viên nên nắm chắc trực giao, trọng số, và khái niệm hàm riêng từ bài Sturm-Liouville. Trực giác từ chuỗi Fourier là nền tảng rất quan trọng, vì gần như mọi ý tưởng trong bài này đều là "Fourier nhưng trong cơ sở phù hợp với toán tử của bài toán".

## Dẫn nhập

![Khai triển theo hàm riêng như Fourier tổng quát]({{ site.imgurl }}/chapter_img/chapter07/04_eigenfunction_expansions.svg)

Chuỗi Fourier đã dạy ta một bài học lớn: một hàm phức tạp có thể được tách thành các dao động cơ bản đơn giản. Khai triển theo hàm riêng là sự mở rộng sâu hơn của ý tưởng đó. Thay vì chỉ dùng sin và cos, ta dùng chính các hàm riêng do bài toán và điều kiện biên sinh ra. Điều này làm cho cơ sở "ăn khớp" với cấu trúc vật lý của hệ hơn nhiều.

Đây là điểm bản lề của chương. Sau khi hiểu khai triển theo hàm riêng, sinh viên sẽ thấy cách giải nhiều BVP và PDE trở nên sáng sủa: thay vì xử lý cả bài toán trong một khối, ta chiếu dữ liệu lên từng mode rồi giải từng mode riêng biệt.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một bản nhạc phức tạp có thể được phân tích thành các họa âm đơn giản. Tương tự, một phân bố nhiệt, một hình dạng ban đầu của dây, hay một nguồn tác động có thể được tách thành các mode riêng. Mỗi mode là một thành phần cơ bản mà hệ "biết cách xử lý" rất tự nhiên.

### Cách nhìn hình ảnh

Nếu vẽ một hàm bất kỳ trên đoạn, ta có thể xấp xỉ nó bằng tổng hữu hạn các mode riêng đầu tiên. Ban đầu chỉ thấy hình dạng thô, nhưng khi thêm nhiều mode hơn, đồ thị dần bám sát hàm gốc. Hình ảnh này rất giống Fourier, chỉ khác là các mode cơ sở không còn phải là sin và cos.

### Cách nhìn hình thức

Nếu $$ \{\phi_n\} $$ là hệ hàm riêng trực giao với trọng số $$ w(x) $$, ta viết

$$ f(x)\sim \sum_{n=1}^{\infty} c_n\phi_n(x). $$

Các hệ số được tính bằng công thức chiếu:

$$
c_n=
\frac{\int_a^b f(x)\phi_n(x)w(x)\,dx}
{\int_a^b \phi_n^2(x)w(x)\,dx}.
$$

Đây là hoàn toàn tương tự với việc chiếu một vector lên cơ sở trực giao trong đại số tuyến tính.

## Những ngộ nhận thường gặp

- "Khai triển theo hàm riêng chỉ là thay sin-cos bằng một họ hàm khác." Chưa đủ. Điều cốt lõi là cơ sở được sinh ra từ chính toán tử của bài toán.
- "Trực giao là đủ, không cần quan tâm trọng số." Sai. Trọng số là một phần của tích vô hướng tự nhiên.
- "Hệ số khai triển chỉ là thủ tục tính toán." Không đúng. Chúng đo mức đóng góp của từng mode vào dữ liệu ban đầu hoặc nguồn tác động.
- "Nếu biết vài mode đầu thì không cần quan tâm bài toán gốc nữa." Sai. Ý nghĩa của mode luôn gắn với toán tử và điều kiện biên sinh ra nó.

## Tiến trình học tập đề xuất

### Bước 1: Nhớ lại Fourier

Xem lại công thức chiếu trong chuỗi Fourier như một tiền mẫu.

### Bước 2: Thay cơ sở Fourier bằng hàm riêng của bài toán

Đây là bước chuyển tư duy quan trọng.

### Bước 3: Tính hệ số có trọng số

Sinh viên cần rất chắc chỗ này.

### Bước 4: Diễn giải mode

Mỗi mode là một thành phần dao động hay đáp ứng cơ bản của hệ.

### Bước 5: Nối sang PDE và BVP không thuần nhất

Cho sinh viên thấy mục đích lớn của công cụ này.

### Các checkpoint

- Sinh viên có viết được công thức hệ số chiếu đúng trọng số hay không.
- Sinh viên có giải thích được tại sao các mode độc lập với nhau hay không.
- Sinh viên có thấy khai triển theo hàm riêng là Fourier tổng quát hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khai triển Fourier sin cổ điển

Trên đoạn $$ [0,L] $$, với điều kiện Dirichlet thuần nhất, các hàm riêng là

$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right). $$

Khi đó

$$
f(x)\sim \sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$

với

$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

Ví dụ này là điểm tựa tốt nhất vì sinh viên đã có thể quen từ chuỗi Fourier.

### Ví dụ 2: Khai triển hàm

$$ f(x)=x $$

trên $$ [0,\pi] $$ theo sin

Trên đoạn này, các hệ số là

$$ c_n=\frac{2}{\pi}\int_0^\pi x\sin(nx)\,dx. $$

Tích phân từng phần cho

$$ c_n=\frac{2(-1)^{n+1}}{n}. $$

Vì vậy

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này minh họa trọn vẹn quy trình từ dữ liệu đến hệ số mode.

### Ví dụ 3: Khai triển với trọng số khác 1

Giả sử hệ hàm riêng của một bài toán thỏa trực giao theo trọng số $$ w(x)=x $$. Khi đó hệ số đúng phải là

$$
c_n=
\frac{\int_a^b f(x)\phi_n(x)x\,dx}
{\int_a^b \phi_n^2(x)x\,dx}.
$$

Ví dụ khái niệm này rất cần thiết vì nhiều sinh viên mang công thức Fourier không trọng số vào mọi nơi rồi mắc lỗi.

### Ví dụ 4: Giải một BVP không thuần nhất bằng mode

Xét

$$ -y''=f(x),
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Nếu khai triển

$$ f(x)=\sum_{n=1}^{\infty} b_n\phi_n(x), $$

với

$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right), $$

thì ta tìm nghiệm dưới dạng

$$ y(x)=\sum_{n=1}^{\infty} a_n\phi_n(x). $$

Thế vào phương trình sẽ cho $$ \lambda_n a_n=b_n $$, nên

$$ a_n=\frac{b_n}{\lambda_n}. $$

Ví dụ này cho thấy toàn bộ sức mạnh của khai triển hàm riêng: bài toán vi phân biến thành vô số phương trình đại số một chiều.

## Câu hỏi khái niệm

1. Vì sao nói khai triển theo hàm riêng là phiên bản tổng quát của chuỗi Fourier?
2. Hệ số khai triển đo điều gì về mối quan hệ giữa dữ liệu và từng mode riêng?
3. Vì sao việc dùng đúng cơ sở hàm riêng của bài toán giúp lời giải PDE hoặc BVP sáng sủa hơn hẳn?

## Bài toán ứng dụng

1. Trong mô hình truyền nhiệt, vì sao phân bố nhiệt ban đầu có thể được tách thành các mode suy giảm độc lập theo thời gian?
2. Trong xử lý âm thanh, việc phân tích tín hiệu thành các mode cơ bản có ý nghĩa tương tự thế nào với khai triển hàm riêng?
3. Một hệ cơ học có nhiều mode dao động tự nhiên. Hãy giải thích vì sao tác động ban đầu bất kỳ có thể được xem như tổng của các mode đó.

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu Fourier là phân tích theo các sóng cơ bản, vậy trong một hình học khác ta sẽ phân tích theo cái gì?"
- Cho sinh viên tự tính một vài hệ số chiếu để cảm nhận được cơ chế "lấy thành phần theo mode".
- Vẽ gần đúng của một hàm bằng 1 mode, 2 mode, 5 mode để trực quan hóa sự hội tụ.
- Tổ chức hoạt động ghép đôi: một sinh viên giải thích bằng ngôn ngữ đại số tuyến tính, sinh viên kia giải thích bằng ngôn ngữ vật lý mode dao động.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên đi từ Fourier sin-cos quen thuộc trước rồi mới mở rộng sang hàm riêng tổng quát. Khi nền quen thuộc đã chắc, phần trọng số và cơ sở tổng quát sẽ bớt đáng sợ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi thảo luận về tính đầy đủ của hệ hàm riêng hoặc quan hệ Parseval như một phát biểu "bảo toàn năng lượng" trong không gian hàm.

## Tóm tắt dễ nhớ

Khai triển theo hàm riêng là Fourier tổng quát: ta biểu diễn một hàm bằng các mode riêng do bài toán sinh ra. Các hệ số được tính bằng phép chiếu có trọng số, và nhờ đó nhiều BVP và PDE phức tạp được tách thành các mode độc lập rất dễ xử lý.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân bố nhiệt trên thanh
- Bài toán: Nhiệt độ ban đầu bất kỳ trên thanh có thể được phân tích theo các mode riêng không gian.
- Mô hình:
$$ u(x,0)=\sum_{n=1}^{\infty} c_n \phi_n(x). $$
- Giả thiết và giới hạn: Cần một họ hàm riêng đầy đủ và bài toán chính quy.
- Diễn giải: Khai triển theo hàm riêng là Fourier tổng quát cho hình học và trọng số phù hợp.

#### Dao động dây với kích thích ban đầu bất kỳ
- Bài toán: Hình dạng ban đầu của dây cần được tách thành các mode dao động cơ bản.
- Mô hình:
$$
f(x)=\sum_{n=1}^{\infty} c_n \phi_n(x),\qquad
c_n=\frac{\langle f,\phi_n\rangle_w}{\langle \phi_n,\phi_n\rangle_w}.
$$
- Giả thiết và giới hạn: Sự hội tụ phụ thuộc lớp hàm và điều kiện biên.
- Diễn giải: Bài toán phức tạp được giảm thành tổng của các mode độc lập.

### 2. Trực giác bổ sung và các kết nối

Khai triển theo hàm riêng là bản nâng cấp của chuỗi Fourier: cơ sở không còn mặc định là sin-cos, mà là các mode riêng do toán tử và biên sinh ra. Một hiểu lầm phổ biến là xem đó chỉ là công cụ hình thức; thật ra nó là ngôn ngữ chuẩn để biểu diễn trạng thái trong hầu hết PDE tuyến tính tách biến được.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
f = x * (1 - x)

series = np.zeros_like(x)
for n in range(1, 6):
    cn = 2 * np.trapz(f * np.sin(n * np.pi * x), x)
    series += cn * np.sin(n * np.pi * x)

plt.plot(x, f, label="f(x)", color="black")
plt.plot(x, series, "--", label="5-mode expansion")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Khai trien theo ham rieng tren [0,1]")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: eigenfunction expansion generalized Fourier series
- search: vibrating string Fourier sine expansion
- search: Sturm Liouville completeness visualization

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ [0,L] $$ với điều kiện Dirichlet, ta có
$$
f(x)=\sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$
trong đó
$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$
Đây là ví dụ quen thuộc nhất của khai triển theo hàm riêng và là mẫu để hiểu trường hợp tổng quát có trọng số.

### 6. Phân tầng độ khó

**Bậc đại học.** Học cách tính hệ số và diễn giải khai triển như tổng mode.

**Bậc sau đại học.** Nói về completeness, hội tụ trong chuẩn $$ L^2_w $$ và lý thuyết phổ của toán tử tự liên hợp.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 11: xây dựng khai triển theo hàm riêng từ tính trực giao và bài toán biên.
- Haberman, Chương 5: nhấn mạnh cách khai triển này chuyển bài toán PDE thành chuỗi mode độc lập.
