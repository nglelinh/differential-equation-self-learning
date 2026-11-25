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

Một khi hệ hàm riêng $\{\phi_n(x)\}$ đã lập thành một "hệ trục tọa độ trực giao" cho không gian hàm, việc giải một phương trình vi phân biên **không thuần nhất** $L[y] - \mu w(x) y = f(x)$ trở nên dễ đến bất ngờ: chỉ cần chiếu cả nghiệm $y$ lẫn vế phải $f$ lên hệ trục $\{\phi_n\}$, phương trình vi phân lập tức tách rã thành vô hạn phương trình đại số 1 ẩn siêu đơn giản!

## Kiến thức cần nhớ: Bốn bước của Phương pháp Khai triển Hàm riêng

1. **Công thức hệ số Fourier tổng quát**:
   Vì $\langle \phi_m, \phi_n \rangle_w = 0$ khi $m \neq n$, ta chiếu hàm bất kỳ $f(x) = \sum_{n=1}^\infty c_n \phi_n(x)$ bằng công thức:
   $$c_n = \frac{\int_a^b f(x)\phi_n(x) w(x)\,dx}{\int_a^b [\phi_n(x)]^2 w(x)\,dx}.$$
2. **Chéo hóa toán tử vi phân $L$**:
   Vì $L[\phi_n] = \lambda_n w \phi_n$, phương trình $L[y] - \mu w y = f$ biến thành $(\lambda_n - \mu) a_n = b_n \implies a_n = \frac{b_n}{\lambda_n - \mu}$!
3. **Cộng hưởng & Điều kiện Fredholm Alternative**:
   Khi $\mu = \lambda_k$ (trùng trị riêng): nếu $b_k \neq 0$ → **vô nghiệm** (cộng hưởng phá hủy); nếu $b_k = 0$ (tức $f \perp \phi_k$) → **vô số nghiệm**!
4. **Cầu nối trực tiếp tới Chuỗi Fourier**:
   Chuỗi sin và cosin Fourier ở Chương 8 đơn giản chỉ là trường hợp riêng của khai triển hàm riêng với $L[y] = -y''$!

## Mục tiêu

Bài học này cho thấy giá trị thực tiễn của lý thuyết trị riêng và tính trực giao: cho phép biểu diễn một hàm bất kỳ theo hệ hàm riêng của bài toán. Sau bài học, sinh viên cần hiểu khai triển theo hàm riêng như sự tổng quát hóa của chuỗi Fourier, nắm công thức tính hệ số bằng phép chiếu có trọng số và biết cách dùng khai triển này để tách một bài toán phức tạp thành các chế độ độc lập.

## Kiến thức nền

Sinh viên nên nắm vững tính trực giao, hàm trọng số và khái niệm hàm riêng từ bài Sturm–Liouville. Kiến thức cơ bản về chuỗi Fourier là nền tảng trực tiếp vì khai triển theo hàm riêng chính là chuỗi Fourier viết trong cơ sở riêng của toán tử bài toán.

## Dẫn nhập

![Khai triển theo hàm riêng như Fourier tổng quát]({{ site.imgurl }}/chapter_img/chapter07/04_eigenfunction_expansions.svg)

Chuỗi Fourier cho thấy một hàm phức tạp có thể được phân tích thành tổng các sóng sin và cos cơ bản. Khai triển theo hàm riêng mở rộng trực tiếp ý tưởng đó: thay vì luôn cố định cơ sở lượng giác, ta sử dụng chính họ hàm riêng do toán tử vi phân và điều kiện biên của bài toán sinh ra.

Nhờ vậy, nhiều bài toán BVP không thuần nhất và PDE tách biến được giải gọn gàng: thay vì xử lý toàn bộ phương trình cùng lúc, ta chiếu dữ liệu lên từng chế độ riêng rồi giải từng phương trình độc lập.

### Giải thích: Giải làm từng bước BVP không thuần nhất $-y'' - 2y = 5\sin(3x),\; y(0) = y(\pi) = 0$

Bài toán trị riêng tương ứng $-y'' = \lambda y,\; y(0)=y(\pi)=0$ có trị riêng $\lambda_n = n^2$ và hàm riêng $\phi_n(x) = \sin(nx)$ ($n = 1, 2, 3, \dots$).
1. **Nhận diện vế phải trong cơ sở hàm riêng**: $f(x) = 5\sin(3x)$ chỉ có đúng **1 thành phần** ứng với $n = 3$ ($b_3 = 5$, mọi $b_n = 0$ với $n \neq 3$).
2. **Thay vào công thức chéo hóa** với $\mu = 2$ và $\lambda_3 = 3^2 = 9 \neq 2$:
   $$a_3 = \frac{b_3}{\lambda_3 - \mu} = \frac{5}{9 - 2} = \frac{5}{7}, \qquad a_n = 0 \; (n \neq 3).$$
3. **Nghiệm duy nhất**: $y(x) = \mathbf{\frac{5}{7}\sin(3x)}$.
4. **Kiểm tra ngược**: $-y'' - 2y = -\left(-\frac{45}{7}\sin(3x)\right) - \frac{10}{7}\sin(3x) = \frac{35}{7}\sin(3x) = 5\sin(3x)$ (đúng 100%!). Lưu ý: nếu đề bài đổi $\mu = 9$, mẫu số $9 - 9 = 0$ với $b_3 = 5 \neq 0$ → cộng hưởng vô nghiệm ngay lập tức!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Tương tự như một âm thanh phức tạp được phân tích thành các họa âm cơ bản, một phân bố nhiệt độ, hình dạng ban đầu của dây đàn hay hàm nguồn tác động đều có thể tách thành tổng các chế độ riêng mà hệ xử lý độc lập với nhau.

### Cách nhìn hình ảnh

Khi xấp xỉ một hàm trên đoạn bằng tổng hữu hạn các hàm riêng đầu tiên, đường cong tổng riêng ban đầu chỉ phản ánh dáng điệu tổng quát, rồi bám ngày càng sát hàm gốc khi bổ sung thêm các chế độ bậc cao — hoàn toàn tương tự chuỗi Fourier nhưng với họ hàm cơ sở tổng quát hơn.

### Cách nhìn hình thức

Nếu $$ \{\phi_n\} $$ là hệ hàm riêng trực giao theo hàm trọng số $$ w(x) $$ trên $$ [a,b] $$, ta khai triển hàm $$ f(x) $$ dưới dạng

$$ f(x)\sim \sum_{n=1}^{\infty} c_n\phi_n(x), $$

trong đó các hệ số khai triển được xác định bởi công thức chiếu có trọng số:

$$
c_n=
\frac{\int_a^b f(x)\phi_n(x)w(x)\,dx}
{\int_a^b \phi_n^2(x)w(x)\,dx}.
$$

Công thức này hoàn toàn tương tự phép chiếu một vector lên cơ sở trực giao trong đại số tuyến tính.

## Những ngộ nhận thường gặp

- "Khai triển theo hàm riêng chỉ là thay sin–cos bằng một họ hàm tùy chọn." Không đủ. Cơ sở phải được sinh ra từ chính toán tử và điều kiện biên của bài toán.
- "Chỉ cần biết các hàm trực giao, không cần quan tâm hàm trọng số." Sai. Trọng số $$ w(x) $$ là thành phần bắt buộc trong cả tử số và mẫu số của công thức chiếu.
- "Hệ số khai triển chỉ là kết quả tính tích phân thuần túy." Sai. Mỗi hệ số $$ c_n $$ đo trực tiếp biên độ đóng góp của chế độ thứ $$ n $$ trong dữ liệu.
- "Chỉ cần lấy vài chế độ đầu là không cần quan tâm điều kiện biên nữa." Sai. Hình dạng và ý nghĩa của các chế độ luôn gắn chặt với toán tử và điều kiện biên gốc.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại chuỗi Fourier

Xem lại công thức tính hệ số Fourier như một trường hợp đặc biệt với $$ w(x)=1 $$.

### Bước 2: Thay thế bằng hệ hàm riêng của bài toán

Chuyển sang cơ sở $$ \{\phi_n\} $$ tương ứng với toán tử Sturm–Liouville đang xét.

### Bước 3: Tính hệ số chiếu có trọng số

Luyện tính đúng tử số và mẫu số có kèm hàm trọng số $$ w(x) $$.

### Bước 4: Diễn giải ý nghĩa chế độ

Hiểu mỗi số hạng $$ c_n\phi_n(x) $$ như một thành phần dao động hoặc đáp ứng cơ bản.

### Bước 5: Vận dụng cho BVP không thuần nhất và PDE

Thay khai triển vào phương trình để đưa toán tử vi phân về phép nhân đại số theo từng trị riêng.

### Các điểm kiểm tra

- Sinh viên có viết đúng công thức hệ số chiếu có kèm trọng số $$ w(x) $$ hay không.
- Sinh viên có giải thích được vì sao các chế độ riêng tách rời nhau khi giải phương trình hay không.
- Sinh viên có nhận thấy chuỗi Fourier là trường hợp riêng của khai triển theo hàm riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khai triển Fourier sin cổ điển

Trên đoạn $$ [0,L] $$ với điều kiện biên Dirichlet thuần nhất, các hàm riêng là

$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right). $$

Khi đó

$$
f(x)\sim \sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$

với

$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

Đây là trường hợp quen thuộc nhất làm điểm tựa cho công thức tổng quát.

### Ví dụ 2: Khai triển hàm $$ f(x)=x $$ trên $$ [0,\pi] $$ theo sin

Trên đoạn $$ [0,\pi] $$, các hệ số khai triển là

$$ c_n=\frac{2}{\pi}\int_0^\pi x\sin(nx)\,dx. $$

Áp dụng tích phân từng phần thu được

$$ c_n=\frac{2(-1)^{n+1}}{n}. $$

Do đó

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này minh họa trọn vẹn quy trình tính hệ số chế độ từ hàm dữ liệu cho trước.

### Ví dụ 3: Khai triển với trọng số khác 1

Nếu hệ hàm riêng trực giao theo hàm trọng số $$ w(x)=x $$, công thức tính hệ số đúng phải là

$$
c_n=
\frac{\int_a^b f(x)\phi_n(x)x\,dx}
{\int_a^b \phi_n^2(x)x\,dx}.
$$

Cần luôn kiểm tra hàm trọng số của bài toán để tránh áp dụng máy móc công thức Fourier không trọng số.

### Ví dụ 4: Giải BVP không thuần nhất bằng khai triển hàm riêng

Xét bài toán

$$ -y''=f(x),
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Khai triển vế phải theo hệ hàm riêng $$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right) $$:

$$ f(x)=\sum_{n=1}^{\infty} b_n\phi_n(x), $$

và tìm nghiệm dưới dạng

$$ y(x)=\sum_{n=1}^{\infty} a_n\phi_n(x). $$

Thay vào phương trình và sử dụng $$ -\phi_n''=\lambda_n\phi_n $$, ta thu được $$ \lambda_n a_n=b_n $$, suy ra

$$ a_n=\frac{b_n}{\lambda_n}. $$

Nhờ khai triển theo hàm riêng, bài toán vi phân được chuyển thành dãy các phương trình đại số một ẩn độc lập.

## Câu hỏi khái niệm

1. Vì sao khai triển theo hàm riêng được xem là sự tổng quát hóa của chuỗi Fourier?
2. Mỗi hệ số khai triển $$ c_n $$ đo đại lượng gì trong mối quan hệ giữa hàm dữ liệu và chế độ riêng tương ứng?
3. Vì sao việc sử dụng đúng hệ hàm riêng của bài toán lại làm đơn giản hóa đáng kể quá trình giải BVP và PDE?

## Bài toán ứng dụng

1. Trong bài toán truyền nhiệt, vì sao phân bố nhiệt độ ban đầu có thể phân tích thành tổng các chế độ tắt dần độc lập theo thời gian?
2. Trong xử lý âm thanh, việc phân tích tín hiệu thành các thành phần tần số cơ bản tương đồng ra sao với khai triển theo hàm riêng?
3. Với một cơ hệ có nhiều chế độ dao động tự nhiên, vì sao một trạng thái kích thích ban đầu bất kỳ có thể biểu diễn dưới dạng chồng chất các chế độ đó?

## Chiến lược giảng dạy tương tác

- Đặt câu hỏi chuyển tiếp: nếu chuỗi Fourier phân tích hàm theo sóng sin–cos trên đoạn thẳng, thì trong một hình học hoặc bài toán biên khác ta nên dùng cơ sở nào?
- Cho sinh viên tự tính một số hệ số chiếu để nắm vững thao tác tích phân có trọng số.
- Vẽ so sánh tổng riêng 1, 2 và 5 chế độ để trực quan hóa quá trình hội tụ.
- Tổ chức trao đổi theo cặp: một sinh viên diễn giải bằng ngôn ngữ đại số tuyến tính, sinh viên kia diễn giải bằng ngôn ngữ vật lý về chế độ dao động.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên xuất phát từ chuỗi Fourier sin–cos quen thuộc rồi mới tổng quát hóa sang hệ hàm riêng và trọng số $$ w(x) $$ để dễ tiếp thu hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu thêm về tính đầy đủ (completeness) của hệ hàm riêng và đẳng thức Parseval như một dạng định luật bảo toàn năng lượng trong không gian hàm.

## Tóm tắt dễ nhớ

Khai triển theo hàm riêng là chuỗi Fourier tổng quát, biểu diễn hàm dữ liệu theo chính hệ chế độ riêng của bài toán. Các hệ số được tính bằng phép chiếu có trọng số, giúp tách nhiều BVP và PDE tuyến tính thành các phương trình độc lập theo từng chế độ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân bố nhiệt độ ban đầu trên thanh
- Bài toán: Phân tích phân bố nhiệt ban đầu bất kỳ thành tổng các chế độ không gian của bài toán truyền nhiệt.
- Mô hình:
$$ u(x,0)=\sum_{n=1}^{\infty} c_n \phi_n(x). $$
- Giả thiết và giới hạn: Bài toán Sturm–Liouville chính quy có hệ hàm riêng đầy đủ.
- Diễn giải: Khai triển theo hàm riêng là công cụ Fourier tổng quát tương thích với hình học và trọng số của bài toán.

#### Dao động dây với kích thích ban đầu bất kỳ
- Bài toán: Tách hình dạng ban đầu của dây đàn thành các chế độ dao động tự nhiên.
- Mô hình:
$$
f(x)=\sum_{n=1}^{\infty} c_n \phi_n(x),\qquad
c_n=\frac{\langle f,\phi_n\rangle_w}{\langle \phi_n,\phi_n\rangle_w}.
$$
- Giả thiết và giới hạn: Tốc độ và kiểu hội tụ phụ thuộc độ trơn của $$ f $$ và sự tương thích với điều kiện biên.
- Diễn giải: Bài toán phức tạp được tách thành chồng chất của các chế độ độc lập.

### 2. Trực giác bổ sung và các kết nối

Khai triển theo hàm riêng tổng quát hóa chuỗi Fourier bằng cách thay cơ sở lượng giác mặc định bằng cơ sở riêng sinh ra từ toán tử và điều kiện biên. Đây là ngôn ngữ nền tảng để giải hầu hết các PDE tuyến tính tách biến được.

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

Trên đoạn $$ [0,L] $$ với điều kiện biên Dirichlet thuần nhất, ta có
$$
f(x)=\sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right),
$$
với
$$
c_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$
Đây là trường hợp mẫu quen thuộc nhất để làm cơ sở mở rộng sang khai triển có trọng số tổng quát.

### 6. Phân tầng độ khó

**Bậc đại học.** Tính thành thạo hệ số khai triển và diễn giải chuỗi như chồng chất các chế độ riêng.

**Bậc sau đại học.** Nghiên cứu tính đầy đủ (completeness), sự hội tụ theo chuẩn $$ L^2_w $$ và lý thuyết phổ của toán tử tự liên hợp.

## Video tham khảo

- Xem trước: [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Giới thiệu chuỗi Fourier như khai triển theo hàm riêng tiêu biểu xuất phát từ phương trình nhiệt.
- [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, tiếng Anh. Giải thích vì sao hệ hàm riêng Sturm–Liouville lập thành cơ sở khai triển tự nhiên.
- [Computing Fourier Series | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=jzzpxqVohhI) — MIT OpenCourseWare, tiếng Anh. Tính hệ số Fourier làm mẫu cho hệ số khai triển suy rộng.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 11: xây dựng khai triển theo hàm riêng từ tính trực giao và bài toán giá trị biên.
- Haberman, Chương 5: trình bày cách khai triển hàm riêng chuyển bài toán PDE thành tổng các chế độ độc lập.
