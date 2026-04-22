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

## Mục tiêu

Bài học này giới thiệu dạng phức của chuỗi Fourier như một cách viết gọn và rất mạnh về mặt cấu trúc. Sau bài học, sinh viên cần biết công thức khai triển phức, hiểu liên hệ giữa hệ số phức $$ c_n $$ với các hệ số thực $$ a_n,\ b_n $$, thấy được vì sao dạng phức đặc biệt thuận tiện cho đạo hàm, tích chập và PDE, và nhận ra đây là cây cầu trực tiếp sang biến đổi Fourier.

## Kiến thức nền

Sinh viên nên nắm chuỗi Fourier dạng thực và công thức Euler $$ e^{inx}=\cos(nx)+i\sin(nx) $$. Nếu sinh viên còn chưa chắc về số phức, nên ôn lại ý nghĩa phần thực, phần ảo và liên hợp phức trước khi vào bài.

## Dẫn nhập

Ở dạng thực, chuỗi Fourier tách thành hai họ mode: sine và cosine. Điều đó rất rõ về mặt hình học, nhưng đôi khi khá cồng kềnh về mặt công thức. Dạng phức gom toàn bộ cấu trúc đó vào một biểu diễn duy nhất bằng các mũ phức $$ e^{inx} $$. Điều này không chỉ làm công thức gọn hơn mà còn làm nổi bật bản chất phổ của Fourier. Khi đó, mỗi chỉ số $$ n $$ đại diện cho một tần số, còn hệ số $$ c_n $$ là biên độ phức của tần số ấy.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu dạng thực giống như việc tách tín hiệu thành "thành phần cosine" và "thành phần sine", thì dạng phức giống như việc gói hai thông tin đó vào một vector quay duy nhất. Số phức giúp mô tả đồng thời biên độ và pha của mode.

### Cách nhìn hình ảnh

Hàm $$ e^{inx} $$ có thể được hình dung như một mũi tên quay đều trên mặt phẳng phức. Khi cộng nhiều mũi tên quay với tốc độ khác nhau, ta tạo nên tín hiệu ban đầu. Hình ảnh này đặc biệt hữu ích khi nói về pha và giao thoa của các mode.

### Cách nhìn hình thức

Chuỗi Fourier phức của một hàm chu kỳ $$ 2\pi $$ có dạng

$$ f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx}, $$

với

$$
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$

Liên hệ với dạng thực:

$$ c_0=\frac{a_0}{2}, $$

$$
c_n=\frac{a_n-ib_n}{2},
\qquad
c_{-n}=\frac{a_n+ib_n}{2}
\quad (n\ge 1).
$$

Nếu $$ f $$ là hàm thực, ta có đối xứng liên hợp

$$ c_{-n}=\overline{c_n}. $$

## Những ngộ nhận thường gặp

- "Dạng phức là một lý thuyết khác với dạng thực." Sai. Chúng hoàn toàn tương đương về nội dung.
- "Dùng số phức thì mất ý nghĩa hình học." Không đúng; thật ra dạng phức còn làm rõ biên độ và pha hơn.
- "Nếu hàm thực thì hệ số phức phải đều là số thực." Sai; điều đúng là chúng đối xứng liên hợp.
- "Dạng phức chỉ để viết gọn." Không chỉ vậy; nó làm đạo hàm, dịch pha và nhiều phép toán trở nên tự nhiên hơn rất nhiều.

## Tiến trình học tập đề xuất

### Bước 1: Ôn công thức Euler

Sinh viên cần thật thoải mái với việc chuyển qua lại giữa mũ phức và sin-cos.

### Bước 2: Viết lại chuỗi Fourier theo

$$ e^{inx} $$

Đây là bước chuyển hình thức.

### Bước 3: Hiểu hệ số phức

Chúng không chỉ là hệ số "lạ", mà là cách mã hóa biên độ và pha.

### Bước 4: Nhấn mạnh lợi ích thao tác

Đạo hàm, tích chập, dịch pha đều gọn hơn rõ rệt.

### Các checkpoint

- Sinh viên có chuyển qua lại được giữa dạng thực và dạng phức hay không.
- Sinh viên có hiểu vì sao hàm thực dẫn đến điều kiện

$$ c_{-n}=\overline{c_n} $$

hay không.
- Sinh viên có nhận ra ưu thế tính toán của dạng phức hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Một mode đơn

Với $$ f(x)=e^{i3x} $$, chuỗi Fourier phức chỉ có đúng một hệ số khác 0:

$$ c_3=1,
\qquad
c_n=0 \text{ nếu } n\ne 3. $$

Ví dụ này là bản phức của ví dụ "một mode duy nhất" trong dạng thực.

### Ví dụ 2: Liên hệ với cosine

Với $$ f(x)=\cos x $$, ta có

$$ \cos x=\frac{e^{ix}+e^{-ix}}{2}. $$

Do đó

$$ c_1=\frac{1}{2},
\qquad
c_{-1}=\frac{1}{2}, $$

và các hệ số khác bằng 0. Ví dụ này cho thấy một mode cosine thực thật ra là sự kết hợp của hai mode phức đối xứng.

### Ví dụ 3: Liên hệ với sine

Với

$$ \sin x=\frac{e^{ix}-e^{-ix}}{2i}, $$

ta có

$$ c_1=\frac{1}{2i},
\qquad
c_{-1}=-\frac{1}{2i}. $$

Ví dụ này giúp sinh viên thấy sự khác biệt pha giữa sine và cosine được mã hóa như thế nào trong hệ số phức.

### Ví dụ 4: Sóng vuông ở dạng phức

Với sóng vuông lẻ, ta có thể tính

$$
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$

Kết quả cho thấy các mode chẵn biến mất, chỉ còn các mode lẻ. Đây là phiên bản phức của điều đã thấy trong dạng thực, nhưng công thức gọn hơn và chuẩn bị tốt cho biến đổi Fourier.

## Câu hỏi khái niệm

1. Vì sao dạng phức không làm thay đổi nội dung của Fourier series mà chỉ thay đổi cách nhìn?
2. Hệ số phức mã hóa biên độ và pha tốt hơn dạng thực như thế nào?
3. Vì sao đạo hàm trong dạng phức trở nên đặc biệt đơn giản?

## Bài toán ứng dụng

1. Trong tín hiệu học, vì sao biểu diễn bằng biên độ và pha lại tự nhiên hơn chỉ bằng sine và cosine tách rời?
2. Trong PDE, vì sao mode $$ e^{inx} $$ là ngôn ngữ rất tiện cho việc lấy đạo hàm?
3. Trong dao động và sóng, vì sao hai mode $$ n $$ và $$ -n $$ lại nên được xem như một cặp liên hợp?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự viết lại

$$ \cos x,\ \sin x $$

theo mũ phức trước khi trình bày công thức tổng quát.
- Hỏi cả lớp: "Dạng phức giúp gì hơn dạng thực ngoài việc viết ngắn hơn?"
- Dùng hình ảnh mũi tên quay trên mặt phẳng phức để trực quan hóa

$$ e^{inx}. $$
- Tổ chức hoạt động chuyển đổi hai chiều giữa dạng thực và dạng phức để sinh viên thấy chúng thật sự tương đương.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên luôn gắn mỗi công thức phức với một công thức thực quen thuộc tương ứng. Khi các em thấy $$ e^{inx} $$ chỉ là cách gói $$ \cos(nx) $$ và $$ \sin(nx) $$, nỗi sợ số phức sẽ giảm rất nhanh.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận về dịch pha, tích chập, hoặc về vai trò của chuỗi Fourier phức trong cấu trúc của các nhóm tuần hoàn và giải tích điều hòa.

## Tóm tắt dễ nhớ

Chuỗi Fourier phức viết tín hiệu dưới dạng tổng của các mode $$ e^{inx} $$. Nó tương đương hoàn toàn với dạng thực nhưng gọn hơn, linh hoạt hơn, và làm nổi bật biên độ, pha, cũng như cấu trúc phổ của bài toán.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Điều chế và xử lý tín hiệu
- Bài toán: Biểu diễn tín hiệu tuần hoàn bằng một tổng mũ phức giúp việc dịch pha và tính toán đạo hàm dễ hơn.
- Mô hình:
$$
f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx},
\qquad
c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.
$$
- Giả thiết và giới hạn: Hàm tuần hoàn và khả tích theo nghĩa thích hợp.
- Diễn giải: Dạng phức gói sin-cos vào một công thức đối xứng hơn nhiều.

#### PDE tuyến tính với mode quay
- Bài toán: Khi toán tử tác động lên $$ e^{inx} $$, ta thu được nhân tử đại số đơn giản.
- Mô hình:
$$ \frac{d}{dx}e^{inx}=in e^{inx}. $$
- Giả thiết và giới hạn: Ưu thế đặc biệt rõ trong bài toán đạo hàm, tích chập và biến đổi.
- Diễn giải: Complex form là ngôn ngữ tự nhiên của phép vi phân và phổ.

### 2. Trực giác bổ sung và các kết nối

Chuỗi Fourier phức không thay đổi nội dung toán học; nó đổi ngôn ngữ sang dạng đối xứng và ngắn gọn hơn. Một bẫy phổ biến là xem số phức như làm bài toán "khó hơn", trong khi thực tế nó làm cấu trúc phổ trở nên trong suốt hơn.

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

Từ
$$
\cos(nx)=\frac{e^{inx}+e^{-inx}}{2},
\qquad
\sin(nx)=\frac{e^{inx}-e^{-inx}}{2i},
$$
ta gộp chuỗi Fourier thực thành
$$ f(x)\sim \sum_{n=-\infty}^{\infty}c_n e^{inx}. $$
Khi đó đạo hàm được viết gọn:
$$
f'(x)\sim \sum_{n=-\infty}^{\infty}in c_n e^{inx}.
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu mối liên hệ giữa hệ số thực và phức, dùng Euler để chuyển đổi qua lại.

**Bậc sau đại học.** Khai thác chuỗi phức trong PDE, tích chập, và chuẩn bị cho Fourier transform.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
