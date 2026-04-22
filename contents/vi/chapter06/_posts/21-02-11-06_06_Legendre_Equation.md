---
layout: post
title: "06-06 Phương trình Legendre"
chapter: '06'
order: 6
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

## Mục tiêu

Bài học này trình bày phương trình Legendre và đa thức Legendre như họ hàm riêng tự nhiên của các bài toán có đối xứng cầu. Sau bài học, sinh viên cần biết nhận dạng phương trình Legendre, hiểu vì sao khi tham số là số nguyên không âm thì nghiệm trở thành đa thức, biết vai trò của trực giao, và thấy mối liên hệ sâu giữa Legendre với tách biến trong tọa độ cầu.

## Kiến thức nền

Sinh viên nên nắm ý tưởng trị riêng, trực giao cơ bản, và các bước đầu của tách biến. Kiến thức về Bessel cũng hữu ích để so sánh: nếu Bessel là "họ hàm của bán kính tròn", thì Legendre là "họ hàm của góc cầu".

## Dẫn nhập

![Phương trình Legendre và đa thức Legendre]({{ site.imgurl }}/chapter_img/chapter06/06_legendre_equation.svg)

Nếu Bessel xuất hiện khi hình học có đối xứng trụ, thì Legendre xuất hiện khi bài toán mang đối xứng cầu. Trong điện thế hấp dẫn, điện thế tĩnh, trường ngoài một vật thể đối xứng trục, hay nhiều bài toán vật lý toán cổ điển khác, phần phụ thuộc góc dẫn đến phương trình Legendre. Điều này biến các đa thức Legendre thành một bộ "mode góc" tự nhiên.

Điều hay của bài này là sinh viên thấy một chuyển đổi rất đẹp: từ phương trình vi phân, ta thu được một họ đa thức có cấu trúc trực giao hoàn chỉnh. Đây là lúc ODE, đại số trực giao và vật lý hình học gặp nhau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng ta muốn mô tả một đại lượng trên bề mặt cầu nhưng chỉ phụ thuộc vào góc lệch so với trục thẳng đứng. Các mode đơn giản nhất sẽ là "đồng đều", rồi "nghiêng lên xuống", rồi "hai múi đối xứng", rồi các hình dạng dao động góc ngày càng phức tạp. Đa thức Legendre chính là các mode đó.

### Cách nhìn hình ảnh

Đồ thị của $$ P_0(x),\quad P_1(x),\quad P_2(x),\quad P_3(x) $$ cho thấy số điểm đổi dấu tăng dần giống cách các mode dao động tăng số nút. Trên đoạn $$ [-1,1] $$, các đa thức này vuông góc với nhau theo nghĩa tích phân, nên chúng hoạt động như một cơ sở Fourier nhưng được điều chỉnh cho hình học cầu.

### Cách nhìn hình thức

Phương trình Legendre có dạng $$ (1-x^2)y''-2xy'+n(n+1)y=0 $$. Khi $$ n $$ là số nguyên không âm, một nghiệm đặc biệt là đa thức Legendre bậc $$ n $$, ký hiệu là $$ P_n(x) $$. Ta có công thức Rodrigues:

$$ P_n(x)=\frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n. $$

Các đa thức này thỏa tính trực giao:

$$
\int_{-1}^{1}P_m(x)P_n(x)\,dx
=
\frac{2}{2n+1}\delta_{mn}.
$$

## Những ngộ nhận thường gặp

- "Legendre chỉ là một họ đa thức ngẫu nhiên." Sai. Chúng là nghiệm của một toán tử vi phân rất tự nhiên trong tọa độ cầu.
- "Nếu thấy đa thức thì bài toán chắc dễ." Không hẳn; điều đáng chú ý là cấu trúc trực giao và vai trò trị riêng của chúng.
- "Tính trực giao chỉ là kỹ thuật tính tích phân." Sai. Trực giao chính là lý do ta có thể khai triển hàm theo cơ sở Legendre.
- "Chỉ cần nhớ vài đa thức đầu." Chưa đủ; cần hiểu vì sao chúng xuất hiện và dùng ở đâu.

## Tiến trình học tập đề xuất

### Bước 1: Nhận ra dạng phương trình

Sinh viên cần nhìn thấy hệ số $$ 1-x^2 $$ và hạng $$ n(n+1) $$ như dấu hiệu đặc trưng của Legendre.

### Bước 2: Tạo các đa thức bậc thấp

Làm quen với

$$ P_0,\quad P_1,\quad P_2,\quad P_3. $$

### Bước 3: Hiểu trực giao

Không chỉ kiểm tra công thức mà phải hiểu trực giác về các mode độc lập.

### Bước 4: Liên hệ với đối xứng cầu

Đây là bước cho bài học có ý nghĩa vật lý rõ rệt.

### Các checkpoint

- Sinh viên có viết được vài đa thức Legendre đầu hay không.
- Sinh viên có giải thích được tính trực giao bằng ngôn ngữ hình học hoặc giải tích hay không.
- Sinh viên có thấy Legendre là họ mode góc của đối xứng cầu hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba đa thức đầu tiên

Từ công thức Rodrigues:

$$ P_0(x)=1, $$ $$ P_1(x)=x $$, $$ P_2(x)=\frac{1}{2}(3x^2-1). $$

Đây là ví dụ khởi động quan trọng vì nó giúp sinh viên thấy các đa thức Legendre không hề xa lạ; chúng là các đa thức rất cụ thể, chỉ khác ở chỗ được chuẩn hóa theo một cấu trúc sâu hơn.

### Ví dụ 2: Kiểm tra trực tiếp một nghiệm

Kiểm tra rằng

$$ y=\frac{1}{2}(3x^2-1) $$

là nghiệm của phương trình Legendre với $$ n=2 $$. Ta có

$$ y'=3x,
\qquad
y''=3. $$

Thế vào phương trình:

$$
(1-x^2)3-2x(3x)+2\cdot 3 \cdot \frac{1}{2}(3x^2-1).
$$

Rút gọn:

$$ 3-3x^2-6x^2+9x^2-3=0. $$

Ví dụ này giúp sinh viên kiểm tra trực tiếp mối liên hệ giữa đa thức và phương trình.

### Ví dụ 3: Tính trực giao đơn giản

Kiểm tra rằng $$ P_0 $$ và $$ P_1 $$ trực giao:

$$
\int_{-1}^{1}P_0(x)P_1(x)\,dx
=
\int_{-1}^{1}x\,dx
=0.
$$

Tương tự,

$$
\int_{-1}^{1}P_1(x)P_2(x)\,dx
=
\int_{-1}^{1}x\cdot \frac{1}{2}(3x^2-1)\,dx
=0
$$

vì tích phân của hàm lẻ trên đoạn đối xứng bằng 0. Đây là ví dụ tốt để nối trực giao với đối xứng.

### Ví dụ 4: Khai triển một đa thức theo cơ sở Legendre

Hãy viết $$ x^2 $$ theo $$ P_0 $$ và $$ P_2 $$. Vì

$$ P_2(x)=\frac{1}{2}(3x^2-1), $$

ta suy ra $$ 3x^2=2P_2(x)+1 $$. Do đó

$$ x^2=\frac{2}{3}P_2(x)+\frac{1}{3}P_0(x). $$

Ví dụ này cực kỳ hữu ích vì nó cho thấy các đa thức Legendre thật sự là một cơ sở để biểu diễn hàm.

### Ví dụ 5: Liên hệ với Laplace trong tọa độ cầu

Trong bài toán thế đối xứng trục, sau khi tách biến, phần góc thường dẫn tới phương trình

$$
\frac{d}{dx}\left[(1-x^2)\frac{dY}{dx}\right]+n(n+1)Y=0,
$$

chính là dạng Legendre. Điều này cho sinh viên một thông điệp quan trọng: các đa thức Legendre không xuất hiện vì ai đó chọn chúng, mà vì hình học cầu yêu cầu như vậy.

## Câu hỏi khái niệm

1. Vì sao các đa thức Legendre được xem như một phiên bản Fourier phù hợp với đối xứng cầu?
2. Tính trực giao giúp gì khi ta muốn biểu diễn một hàm theo các mode Legendre?
3. Vì sao chỉ với những giá trị $$ n $$ nguyên không âm ta mới nhận được các nghiệm đa thức đặc biệt đẹp?

## Bài toán ứng dụng

1. Trong điện thế tĩnh bên ngoài một vật có đối xứng trục, vì sao phần góc của nghiệm lại thường được khai triển theo Legendre?
2. Trong thiên văn học, khi mô tả trường hấp dẫn gần cầu nhưng có sai lệch nhỏ, vì sao các hạng Legendre bậc thấp rất quan trọng?
3. Trong đồ họa hoặc xử lý tín hiệu trên mặt cầu, vì sao cơ sở góc trực giao lại đặc biệt hữu ích?

## Chiến lược giảng dạy tương tác

- Vẽ cùng lúc các đồ thị

$$ P_0,\quad P_1,\quad P_2,\quad P_3 $$

và yêu cầu sinh viên mô tả bằng lời số nút, tính chẵn lẻ, và trực giác mode.
- Cho sinh viên tự tính một tích phân trực giao đơn giản để trực giác trở nên cụ thể.
- Hỏi lớp: "Nếu Fourier là ngôn ngữ của đoạn thẳng, vậy ngôn ngữ của mặt cầu là gì?"
- Tổ chức thảo luận nhóm ngắn về sự khác nhau giữa Bessel và Legendre theo góc nhìn hình học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho các em học chắc ba đa thức đầu, trực giác đối xứng chẵn lẻ, và ý nghĩa trực giao trước. Khi nền đó vững rồi, công thức Rodrigues sẽ ít gây áp lực hơn.

### Thử thách cho sinh viên khá giỏi

Có thể giao cho sinh viên khá giỏi chứng minh hệ thức truy hồi của Legendre hoặc dùng tính trực giao để tìm hệ số khai triển của một hàm đơn giản trên

$$ [-1,1]. $$

## Tóm tắt dễ nhớ

Phương trình Legendre tạo ra các đa thức Legendre, là các mode góc tự nhiên của đối xứng cầu. Chúng trực giao trên $$ [-1,1] $$ và đóng vai trò như cơ sở Fourier cho nhiều bài toán vật lý toán có đối xứng trục và cầu.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Điện thế hấp dẫn và điện tĩnh quanh mặt cầu
- Bài toán: Sau tách biến trong tọa độ cầu, phần góc thỏa phương trình Legendre.
- Mô hình:
$$ (1-x^2)y''-2x y'+n(n+1)y=0,\qquad x=\cos\theta. $$
- Giả thiết và giới hạn: Bài toán có đối xứng cầu và không phụ thuộc góc phương vị đơn giản.
- Diễn giải: Đa thức Legendre mô tả các multipole trường.

#### Cơ học lượng tử: mô men động lượng quỹ đạo
- Bài toán: Phần góc của hàm sóng hydrogen cho phương trình Legendre liên kết.
- Mô hình: Trường hợp $$ m=0 $$ quay về phương trình Legendre chuẩn.
- Giả thiết và giới hạn: Chỉ là lát cắt cơ bản của họ hàm cầu điều hòa.
- Diễn giải: Điều kiện hữu hạn trên $$ [-1,1] $$ buộc chỉ còn các bậc nguyên không âm.

### 2. Trực giác bổ sung và các kết nối

Legendre đóng vai trò tự nhiên trong hình học cầu. Khi tham số $$ \lambda $$ bằng $$ n(n+1) $$, nghiệm bounded trở thành đa thức và đó là dấu hiệu của lượng tử hóa mode góc. Bẫy phổ biến là quên rằng không phải mọi giá trị tham số đều cho đa thức, và không phải mọi nghiệm đều hữu hạn ở $$ x=\pm 1 $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 400)
for n in range(5):
    plt.plot(x, eval_legendre(n, x), label=f"P{n}")

plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.title("Da thuc Legendre dau tien")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Legendre polynomials spherical harmonics
- search: electrostatics multipole Legendre
- search: quantum angular equation Legendre

### 5. Bài toán mẫu có bối cảnh thực

Tìm nghiệm đa thức cho
$$ (1-x^2)y''-2xy'+6y=0. $$
Ta nhận ra $$ 6=2\cdot 3 $$ nên đây là trường hợp $$ n=2 $$. Do đó nghiệm bounded cơ bản là
$$ P_2(x)=\frac{1}{2}(3x^2-1). $$
Trong điện tĩnh, đó là mode quadrupole chuẩn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phương trình Legendre, công thức Rodrigues và vài đa thức đầu.

**Bậc sau đại học.** Nói về tính trực giao trên $$ [-1,1] $$, toán tử tự liên hợp và hàm cầu điều hòa.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: giới thiệu phương trình Legendre, truy hồi và các tính chất cơ bản.
- Haberman, Chương 7: cho thấy vai trò của Legendre trong bài toán vật lý có đối xứng cầu.
