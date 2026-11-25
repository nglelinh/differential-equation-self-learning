---
layout: post
title: "Chuỗi Fourier Phức"
chapter: '08'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---

![21 02 25 08 07 Complex Fourier Series]({{ site.imgurl }}/chapter_img/chapter08/07_complex_fourier_series.svg)

Ghi nhớ cùng lúc ba công thức tách rời cho $a_0, a_n, b_n$ cùng các công thức tích lượng giác rườm rà sẽ trở nên hoàn toàn thừa thãi ngay khi bạn dùng **Công thức Euler** $e^{i\theta} = \cos\theta + i\sin\theta$. **Chuỗi Fourier Phức** hợp nhất toàn bộ $a_0, a_n, b_n$ vào **một công thức duy nhất siêu gọn**—và là cây cầu trực tiếp dẫn sang Biến đổi Fourier và FFT!

## Kiến thức cần nhớ: Bốn trụ cột của Chuỗi Fourier Phức

1. **Một công thức duy nhất cho mọi $n \in \mathbb{Z}$ (từ $-\infty$ đến $+\infty$)**:
   $$f(x) \sim \sum_{n=-\infty}^{\infty} c_n e^{i n\pi x / L}, \qquad c_n = \frac{1}{2L}\int_{-L}^{L} f(x)\, e^{-i n\pi x / L}\,dx.$$
2. **Ánh xạ chính xác giữa $c_n$ và $(a_n, b_n)$**:
   $c_0 = \frac{a_0}{2}$; với $n \ge 1$: $c_n = \frac{a_n - i b_n}{2}$ và $c_{-n} = \frac{a_n + i b_n}{2}$.
3. **Đối xứng liên hợp cho tín hiệu thực**:
   Khi $f(x)$ là hàm **thực**, ta luôn có $c_{-n} = \overline{c_n}$ (phổ biên độ $\vert c_n \vert$ đối xứng chẵn, phổ pha $\arg(c_n)$ đối xứng lẻ).
4. **Sức mạnh đại số của hàm mũ $e^{inx}$**:
   Tích phân hàm mũ nhân hàm mũ chỉ đơn giản là cộng số mũ, và đạo hàm chỉ là nhân với $i\frac{n\pi}{L}$—nhanh gấp đôi so với lượng giác!

## Mục tiêu

Bài học này giới thiệu dạng phức của chuỗi Fourier như một cách biểu diễn gọn gàng và có cấu trúc chặt chẽ. Sau bài học, sinh viên cần nắm công thức khai triển phức, hiểu mối liên hệ giữa hệ số phức $$ c_n $$ với các hệ số thực $$ a_n,\ b_n $$, nhận ra lợi thế của dạng phức khi thực hiện đạo hàm, tích chập và giải PDE, đồng thời thấy được đây là bước đệm trực tiếp sang biến đổi Fourier.

## Kiến thức nền

Sinh viên cần nắm chuỗi Fourier dạng thực và công thức Euler $$ e^{inx}=\cos(nx)+i\sin(nx) $$. Nếu chưa vững về số phức, nên ôn lại khái niệm phần thực, phần ảo và số phức liên hợp trước khi học bài này.

## Dẫn nhập

Ở dạng thực, chuỗi Fourier tách thành hai họ mode là sin và cos. Cách viết này rõ ràng về mặt hình học nhưng đôi khi dài dòng khi thao tác đại số. Dạng phức hợp nhất toàn bộ cấu trúc đó vào một biểu thức duy nhất theo các hàm mũ phức $$ e^{inx} $$. Cách biểu diễn này vừa rút gọn công thức vừa làm nổi bật bản chất phổ của chuỗi Fourier: mỗi chỉ số nguyên $$ n $$ ứng với một tần số, còn hệ số $$ c_n $$ là biên độ phức của tần số đó.

### Giải thích: Tính tay Chuỗi Fourier Phức của $f(x) = e^{x}$ trên $(-\pi, \pi)$ chỉ bằng 1 tích phân

Với $L = \pi$, thay trực tiếp $f(x) = e^x$ vào công thức $c_n$ (không cần tách $a_n, b_n$!):
$$c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{x} e^{-inx}\,dx = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{(1 - in)x}\,dx = \frac{1}{2\pi}\left[\frac{e^{(1-in)x}}{1 - in}\right]_{-\pi}^{\pi}.$$
Nhớ rằng $e^{-in\pi} = e^{in\pi} = (-1)^n$ và $\frac{e^{\pi} - e^{-\pi}}{2} = \sinh\pi$:
$$c_n = \frac{(-1)^n (e^{\pi} - e^{-\pi})}{2\pi(1 - in)} = \frac{(-1)^n \sinh\pi}{\pi(1 - in)} = \mathbf{\frac{(-1)^n \sinh\pi}{\pi}\cdot\frac{1 + in}{1 + n^2}}.$$
Kiểm tra nhanh đối xứng liên hợp cho hàm thực $e^x$: thay $n \to -n$ ta được $c_{-n} = \frac{(-1)^n\sinh\pi}{\pi}\cdot\frac{1 - in}{1 + n^2} = \overline{c_n}$ — chính xác tuyệt đối!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu dạng thực tách tín hiệu thành thành phần cos và thành phần sin riêng rẽ, thì dạng phức gộp cả hai thông tin đó vào một vectơ quay duy nhất. Số phức cho phép biểu diễn đồng thời cả biên độ và pha của từng mode.

### Cách nhìn hình ảnh

Hàm $$ e^{inx} $$ có thể được hình dung như một vectơ quay đều trên mặt phẳng phức. Khi cộng nhiều vectơ quay với các tốc độ góc khác nhau, ta tái tạo lại tín hiệu ban đầu. Hình ảnh này hỗ trợ trực tiếp cho việc hiểu pha và sự giao thoa giữa các mode.

### Cách nhìn hình thức

Chuỗi Fourier phức của một hàm tuần hoàn chu kỳ $$ 2\pi $$ có dạng

$$ f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx}, $$

với

$$
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$

Mối liên hệ với dạng thực là

$$ c_0=\frac{a_0}{2}, $$

$$
c_n=\frac{a_n-ib_n}{2},
\qquad
c_{-n}=\frac{a_n+ib_n}{2}
\quad (n\ge 1).
$$

Nếu $$ f $$ là hàm thực, các hệ số thỏa mãn tính đối xứng liên hợp

$$ c_{-n}=\overline{c_n}. $$

## Những ngộ nhận thường gặp

- "Dạng phức là một lý thuyết khác với dạng thực." Sai; hai dạng hoàn toàn tương đương về nội dung toán học.
- "Dùng số phức sẽ làm mất ý nghĩa hình học." Không đúng; thực tế dạng phức thể hiện biên độ và pha rõ ràng hơn.
- "Nếu hàm là hàm thực thì mọi hệ số phức đều phải là số thực." Sai; điều kiện đúng là chúng đối xứng liên hợp ($$ c_{-n}=\overline{c_n} $$).
- "Dạng phức chỉ có tác dụng viết ngắn gọn hơn." Không chỉ vậy; dạng phức giúp các phép toán như đạo hàm, dịch pha và tích chập trở nên đơn giản hơn nhiều.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại công thức Euler

Sinh viên cần chuyển đổi thành thạo giữa hàm mũ phức và các hàm sin, cos.

### Bước 2: Viết lại chuỗi Fourier theo $$ e^{inx} $$

Đây là bước chuyển đổi hình thức từ dạng thực sang dạng phức.

### Bước 3: Diễn giải ý nghĩa hệ số phức

Các hệ số $$ c_n $$ mã hóa đồng thời biên độ và pha của mỗi mode tần số.

### Bước 4: Khai thác lợi thế tính toán

Quan sát cách đạo hàm, tích chập và dịch pha trở nên gọn hơn rõ rệt trong dạng phức.

### Các điểm kiểm tra

- Sinh viên có chuyển đổi qua lại giữa dạng thực và dạng phức hay không.
- Sinh viên có giải thích được vì sao hàm thực dẫn đến điều kiện $$ c_{-n}=\overline{c_n} $$ hay không.
- Sinh viên có nhận ra ưu thế thao tác của dạng phức hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Một mode đơn

Với $$ f(x)=e^{i3x} $$, chuỗi Fourier phức chỉ có đúng một hệ số khác 0:

$$ c_3=1,
\qquad
c_n=0 \text{ nếu } n\ne 3. $$

Đây là phiên bản phức của ví dụ "một mode duy nhất" ở dạng thực.

### Ví dụ 2: Liên hệ với hàm cos

Với $$ f(x)=\cos x $$, ta có

$$ \cos x=\frac{e^{ix}+e^{-ix}}{2}. $$

Do đó

$$ c_1=\frac{1}{2},
\qquad
c_{-1}=\frac{1}{2}, $$

và mọi hệ số khác bằng 0. Kết quả này cho thấy một mode cos thực chất là sự kết hợp của hai mode phức đối xứng.

### Ví dụ 3: Liên hệ với hàm sin

Với

$$ \sin x=\frac{e^{ix}-e^{-ix}}{2i}, $$

ta thu được

$$ c_1=\frac{1}{2i},
\qquad
c_{-1}=-\frac{1}{2i}. $$

Ví dụ này minh họa cách sự lệch pha giữa sin và cos được mã hóa trong hệ số phức.

### Ví dụ 4: Sóng vuông ở dạng phức

Với sóng vuông lẻ, ta tính

$$
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$

Kết quả cho thấy các mode chẵn đều triệt tiêu, chỉ còn lại các mode lẻ. Đây là biểu diễn phức tương ứng với kết quả đã biết ở dạng thực, với cấu trúc gọn hơn và thuận tiện để chuyển tiếp sang biến đổi Fourier.

## Câu hỏi khái niệm

1. Vì sao dạng phức không làm thay đổi nội dung toán học của chuỗi Fourier mà chỉ thay đổi cách biểu diễn?
2. Hệ số phức mã hóa biên độ và pha hiệu quả hơn dạng thực ở điểm nào?
3. Vì sao phép lấy đạo hàm trong dạng phức lại đơn giản hơn đáng kể?

## Bài toán ứng dụng

1. Trong xử lý tín hiệu, vì sao biểu diễn theo biên độ và pha tự nhiên hơn so với việc tách riêng sin và cos?
2. Trong PDE, vì sao họ hàm $$ e^{inx} $$ đặc biệt thuận tiện cho phép lấy đạo hàm?
3. Trong nghiên cứu dao động và sóng, vì sao hai mode ứng với $$ n $$ và $$ -n $$ thường được xét như một cặp liên hợp?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự viết lại $$ \cos x,\ \sin x $$ theo hàm mũ phức trước khi trình bày công thức tổng quát.
- Đặt câu hỏi cho cả lớp: "Ngoài việc viết ngắn gọn hơn, dạng phức mang lại lợi thế nào so với dạng thực?"
- Sử dụng hình ảnh vectơ quay trên mặt phẳng phức để minh họa hàm $$ e^{inx} $$.
- Tổ chức bài tập chuyển đổi hai chiều giữa dạng thực và dạng phức để sinh viên kiểm chứng tính tương đương.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên luôn đặt mỗi công thức phức bên cạnh công thức thực tương ứng. Khi nhận ra $$ e^{inx} $$ đơn giản là cách gộp $$ \cos(nx) $$ và $$ \sin(nx) $$, sinh viên sẽ bớt e ngại khi làm việc với số phức.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên phân tích phép dịch pha, phép tích chập hoặc vai trò của chuỗi Fourier phức trong cấu trúc nhóm tuần hoàn và giải tích điều hòa.

## Tóm tắt dễ nhớ

Chuỗi Fourier phức biểu diễn tín hiệu dưới dạng tổng các mode $$ e^{inx} $$. Cách viết này hoàn toàn tương đương với dạng thực nhưng gọn gàng, linh hoạt hơn và thể hiện trực tiếp biên độ, pha cũng như cấu trúc phổ của bài toán.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Điều chế và xử lý tín hiệu
- Bài toán: Biểu diễn tín hiệu tuần hoàn bằng một tổng hàm mũ phức giúp phép dịch pha và lấy đạo hàm trở nên thuận tiện hơn.
- Mô hình:
$$
f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx},
\qquad
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$
- Giả thiết và giới hạn: Hàm tuần hoàn và khả tích theo nghĩa thích hợp.
- Diễn giải: Dạng phức gộp sin và cos vào một biểu thức có cấu trúc đối xứng hơn.

#### PDE tuyến tính với mode quay
- Bài toán: Khi toán tử vi phân tác động lên $$ e^{inx} $$, ta thu được nhân tử đại số đơn giản.
- Mô hình:
$$ \frac{d}{dx}e^{inx}=in e^{inx}. $$
- Giả thiết và giới hạn: Lợi thế thể hiện rõ nhất trong các phép toán vi phân, tích chập và biến đổi tuyến tính.
- Diễn giải: Dạng phức là ngôn ngữ tự nhiên cho phép vi phân và phân tích phổ.

### 2. Trực giác bổ sung và các kết nối

Chuỗi Fourier phức không làm thay đổi bản chất toán học của bài toán mà chuyển sang một ký hiệu đối xứng và súc tích hơn. Thay vì gây khó khăn thêm, việc dùng số phức giúp cấu trúc phổ trở nên rõ ràng hơn nhiều.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 500)
z = np.exp(1j * 3 * t)

plt.plot(z.real, z.imag)
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Quy dao cua e^{i 3 t} tren mat phang phuc")
plt.axis("equal")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: complex Fourier series geometric interpretation
- search: Euler formula rotating phasor animation
- search: Fourier basis complex exponentials

### 5. Bài toán mẫu có bối cảnh thực

Từ các đồng nhất thức
$$
\cos(nx)=\frac{e^{inx}+e^{-inx}}{2},
\qquad
\sin(nx)=\frac{e^{inx}-e^{-inx}}{2i},
$$
ta gộp chuỗi Fourier thực thành
$$ f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx}. $$
Khi đó đạo hàm được viết gọn thành
$$
f'(x)\sim \sum_{n=-\infty}^{\infty}in c_n e^{inx}.
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm mối liên hệ giữa hệ số thực và hệ số phức, sử dụng công thức Euler để chuyển đổi hai chiều.

**Bậc sau đại học.** Vận dụng chuỗi Fourier phức trong PDE, tích chập và làm bước chuyển tiếp sang biến đổi Fourier.

## Video tham khảo

- Xem trước: [Complex Fourier Series](https://www.youtube.com/watch?v=4cfctnaHyFM) — Steve Brunton, tiếng Anh. Trình bày cách suy ra dạng phức $$ c_n e^{in t} $$ của chuỗi Fourier.
- [Complex Fourier Series (fourier series engineering mathematics)](https://www.youtube.com/watch?v=aC0j8CW58AM) — blackpenredpen, tiếng Anh. Minh họa chi tiết phép tính một chuỗi Fourier phức.
- [MM41: Complex Fourier series](https://www.youtube.com/watch?v=3n36uTz0Qso) — Learn Physics with Dr. Viv!, tiếng Anh. Đối chiếu trực tiếp các hệ số phức với dạng sin và cos thực.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
