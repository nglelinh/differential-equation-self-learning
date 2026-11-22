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

Bài học này trình bày phương trình Legendre và đa thức Legendre như họ hàm riêng tự nhiên của các bài toán có đối xứng cầu. Sau bài học, sinh viên cần nhận dạng được phương trình Legendre, hiểu vì sao khi tham số là số nguyên không âm thì xuất hiện nghiệm đa thức, nắm được vai trò của tính trực giao và thấy rõ mối liên hệ giữa đa thức Legendre với phương pháp tách biến trong tọa độ cầu.

## Kiến thức nền

Sinh viên nên nắm ý tưởng trị riêng, tính trực giao cơ bản và các bước tách biến. Việc đã học phương trình Bessel cũng rất hữu ích để đối chiếu: nếu hàm Bessel gắn với bán kính trong hình học tròn, thì đa thức Legendre gắn với góc trong hình học cầu.

## Dẫn nhập

![Phương trình Legendre và đa thức Legendre]({{ site.imgurl }}/chapter_img/chapter06/06_legendre_equation.svg)

Nếu hàm Bessel xuất hiện trong các bài toán có đối xứng trụ, thì đa thức Legendre xuất hiện khi bài toán có đối xứng cầu. Trong bài toán thế hấp dẫn, điện thế tĩnh, trường ngoài một vật thể đối xứng trục cùng nhiều bài toán vật lý toán cổ điển khác, thành phần phụ thuộc góc dẫn trực tiếp đến phương trình Legendre, biến các đa thức Legendre thành họ chế độ góc (angular modes) tự nhiên.

Từ một phương trình vi phân cấp hai, ta thu được một họ đa thức có đầy đủ cấu trúc trực giao trên đoạn $$ [-1,1] $$ — nơi giải tích vi phân, đại số trực giao và hình học vật lý kết nối chặt chẽ với nhau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy xét một đại lượng phân bố trên mặt cầu nhưng chỉ phụ thuộc vào góc cực tính từ trục thẳng đứng. Các chế độ cơ bản lần lượt là phân bố đồng đều, phân bố lưỡng cực (nghiêng hai cực), phân bố tứ cực (hai múi đối xứng) và các cấu trúc dao động góc bậc cao hơn. Đa thức Legendre chính là biểu diễn toán học của các chế độ đó.

### Cách nhìn hình ảnh

Đồ thị của $$ P_0(x),\ P_1(x),\ P_2(x),\ P_3(x) $$ cho thấy số điểm đổi dấu trên $$ (-1,1) $$ tăng đúng bằng bậc $$ n $$, tương tự sự gia tăng số nút của các chế độ dao động. Trên đoạn $$ [-1,1] $$, các đa thức này trực giao với nhau theo nghĩa tích phân, đóng vai trò như một hệ cơ sở Fourier dành riêng cho hình học cầu.

### Cách nhìn hình thức

Phương trình Legendre có dạng $$ (1-x^2)y''-2xy'+n(n+1)y=0 $$. Khi $$ n $$ là số nguyên không âm, nghiệm bị chặn tại hai đầu mút $$ x=\pm 1 $$ là đa thức Legendre bậc $$ n $$, ký hiệu $$ P_n(x) $$, xác định bởi công thức Rodrigues:

$$ P_n(x)=\frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n. $$

Các đa thức này thỏa mãn hệ thức trực giao:

$$
\int_{-1}^{1}P_m(x)P_n(x)\,dx
=
\frac{2}{2n+1}\delta_{mn}.
$$

## Những ngộ nhận thường gặp

- "Đa thức Legendre chỉ là một họ đa thức đặt tên tùy ý." Sai. Chúng là nghiệm riêng tự nhiên của một toán tử vi phân trong tọa độ cầu.
- "Vì là đa thức nên bài toán không có gì đặc biệt." Không đúng; giá trị cốt lõi nằm ở cấu trúc trực giao và vai trò hàm riêng của chúng.
- "Tính trực giao chỉ là một đẳng thức tích phân đẹp." Sai. Trực giao chính là cơ sở cho phép khai triển các hàm tùy ý theo đa thức Legendre.
- "Chỉ cần học thuộc vài đa thức bậc thấp là đủ." Chưa đủ; cần hiểu nguồn gốc hình học và cách vận dụng chúng trong khai triển nghiệm.

## Tiến trình học tập đề xuất

### Bước 1: Nhận dạng phương trình Legendre

Nhận biết hệ số đặc trưng $$ 1-x^2 $$ và tham số trị riêng $$ n(n+1) $$.

### Bước 2: Xây dựng các đa thức bậc thấp

Làm quen với các đa thức đầu tiên $$ P_0,\ P_1,\ P_2,\ P_3 $$ từ công thức Rodrigues hoặc hệ thức truy hồi.

### Bước 3: Nắm vững tính trực giao

Hiểu trực giao không chỉ qua tính tích phân mà còn như tính độc lập của các chế độ riêng.

### Bước 4: Liên hệ với đối xứng cầu

Kết nối phương trình Legendre với phép tách biến phương trình Laplace trong tọa độ cầu.

### Các điểm kiểm tra

- Sinh viên có viết chính xác vài đa thức Legendre đầu tiên hay không.
- Sinh viên có diễn giải được tính trực giao bằng ngôn ngữ hình học hoặc giải tích hay không.
- Sinh viên có hiểu vai trò của đa thức Legendre như họ chế độ góc trong đối xứng cầu hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba đa thức đầu tiên

Từ công thức Rodrigues, ta thu được $$ P_0(x)=1 $$, $$ P_1(x)=x $$ và $$ P_2(x)=\frac{1}{2}(3x^2-1) $$. Các đa thức Legendre thực chất rất quen thuộc, nhưng được chuẩn hóa theo một cấu trúc trực giao chặt chẽ trên $$ [-1,1] $$.

### Ví dụ 2: Kiểm tra trực tiếp một nghiệm

Kiểm tra rằng $$ y=\frac{1}{2}(3x^2-1) $$ là nghiệm của phương trình Legendre ứng với $$ n=2 $$. Ta có

$$ y'=3x,
\qquad
y''=3. $$

Thay vào vế trái của phương trình:

$$
(1-x^2)3-2x(3x)+2\cdot 3 \cdot \frac{1}{2}(3x^2-1)
= 3-3x^2-6x^2+9x^2-3=0.
$$

Phép kiểm tra trực tiếp này khẳng định mối liên hệ chặt chẽ giữa đa thức và phương trình vi phân.

### Ví dụ 3: Kiểm tra tính trực giao đơn giản

Kiểm tra $$ P_0 $$ và $$ P_1 $$ trực giao trên $$ [-1,1] $$:

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

vì tích phân của hàm lẻ trên đoạn đối xứng $$ [-1,1] $$ bằng 0. Ví dụ này gắn tính trực giao trực tiếp với tính chẵn–lẻ của đa thức.

### Ví dụ 4: Khai triển một đa thức theo cơ sở Legendre

Biểu diễn $$ x^2 $$ theo $$ P_0 $$ và $$ P_2 $$. Từ

$$ P_2(x)=\frac{1}{2}(3x^2-1), $$

suy ra $$ 3x^2=2P_2(x)+1 $$, do đó

$$ x^2=\frac{2}{3}P_2(x)+\frac{1}{3}P_0(x). $$

Ví dụ này cho thấy các đa thức Legendre thực sự đóng vai trò một cơ sở tuyến tính để khai triển hàm số.

### Ví dụ 5: Liên hệ với phương trình Laplace trong tọa độ cầu

Trong bài toán thế đối xứng trục, sau khi tách biến trong tọa độ cầu với $$ x=\cos\theta $$, phần phụ thuộc góc dẫn đến phương trình

$$
\frac{d}{dx}\left[(1-x^2)\frac{dY}{dx}\right]+n(n+1)Y=0,
$$

chính là dạng tự liên hợp của phương trình Legendre. Như vậy, đa thức Legendre xuất hiện một cách tất yếu từ hình học cầu.

## Câu hỏi khái niệm

1. Vì sao đa thức Legendre được xem như một phiên bản cơ sở Fourier cho các bài toán có đối xứng cầu?
2. Tính trực giao giúp đơn giản hóa việc tìm hệ số khai triển hàm theo đa thức Legendre như thế nào?
3. Vì sao chỉ các giá trị nguyên không âm của $$ n $$ mới tạo ra nghiệm đa thức bị chặn trên $$ [-1,1] $$?

## Bài toán ứng dụng

1. Trong điện tĩnh học bên ngoài một vật thể đối xứng trục, vì sao phần góc của điện thế thường được khai triển theo đa thức Legendre?
2. Trong thiên văn học, khi mô tả trường hấp dẫn của một hành tinh gần cầu, vì sao các số hạng Legendre bậc thấp lại đóng vai trò chủ đạo?
3. Trong đồ họa máy tính hoặc xử lý tín hiệu trên mặt cầu, vì sao một cơ sở góc trực giao lại đặc biệt hữu ích?

## Chiến lược giảng dạy tương tác

- Vẽ cùng lúc đồ thị các đa thức $$ P_0,\ P_1,\ P_2,\ P_3 $$ để sinh viên nhận xét số không điểm, tính chẵn–lẻ và ý nghĩa chế độ dao động.
- Cho sinh viên tự tính một vài tích phân trực giao cơ bản để củng cố trực giác.
- Đặt câu hỏi đối chiếu: nếu chuỗi Fourier là ngôn ngữ của đoạn thẳng, thì họ hàm nào đóng vai trò tương ứng trên mặt cầu?
- Tổ chức thảo luận ngắn so sánh Bessel và Legendre dưới góc độ hình học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giúp sinh viên nắm vững ba đa thức đầu tiên, tính chẵn–lẻ và ý nghĩa của tính trực giao trước khi đi vào công thức Rodrigues tổng quát.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên chứng minh hệ thức truy hồi ba số hạng của đa thức Legendre hoặc dùng tính trực giao để tính hệ số khai triển của một hàm đơn giản trên $$ [-1,1] $$.

## Tóm tắt dễ nhớ

Phương trình Legendre sinh ra các đa thức Legendre — họ chế độ góc tự nhiên của đối xứng cầu. Chúng trực giao trên đoạn $$ [-1,1] $$ và đóng vai trò như cơ sở khai triển phổ cho nhiều bài toán vật lý toán có đối xứng trục và đối xứng cầu.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thế hấp dẫn và điện thế tĩnh quanh mặt cầu
- Bài toán: Sau tách biến phương trình Laplace trong tọa độ cầu, thành phần phụ thuộc góc thỏa phương trình Legendre.
- Mô hình:
$$ (1-x^2)y''-2x y'+n(n+1)y=0,\qquad x=\cos\theta. $$
- Giả thiết và giới hạn: Bài toán có đối xứng trục, không phụ thuộc góc phương vị.
- Diễn giải: Các đa thức Legendre mô tả các thành phần đa cực (multipole) của trường.

#### Cơ học lượng tử: mô men động lượng quỹ đạo
- Bài toán: Phần góc của hàm sóng nguyên tử hydro dẫn đến phương trình Legendre liên kết.
- Mô hình: Trường hợp số lượng tử từ $$ m=0 $$ quy về phương trình Legendre chuẩn.
- Giả thiết và giới hạn: Là lát cắt cơ bản của họ hàm cầu điều hòa.
- Diễn giải: Điều kiện hữu hạn trên $$ [-1,1] $$ lượng tử hóa chỉ số góc về các số nguyên không âm.

### 2. Trực giác bổ sung và các kết nối

Đa thức Legendre là họ hàm tự nhiên của hình học cầu. Khi tham số $$ \lambda $$ nhận giá trị đặc biệt $$ n(n+1) $$, nghiệm bị chặn trở thành đa thức — biểu hiện rõ nét của sự lượng tử hóa chế độ góc. Cần tránh nhầm rằng mọi giá trị tham số đều cho nghiệm đa thức hoặc mọi nghiệm đều hữu hạn tại hai điểm kỳ dị biên $$ x=\pm 1 $$.

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

Tìm nghiệm đa thức của phương trình
$$ (1-x^2)y''-2xy'+6y=0. $$
Nhận thấy $$ 6=2\cdot 3 $$, đây là phương trình Legendre ứng với $$ n=2 $$. Do đó nghiệm bị chặn cơ bản là
$$ P_2(x)=\frac{1}{2}(3x^2-1), $$
tương ứng với thành phần tứ cực (quadrupole) chuẩn trong điện tĩnh học.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện phương trình Legendre, vận dụng công thức Rodrigues và tính vài đa thức bậc đầu.

**Bậc sau đại học.** Phân tích tính trực giao trên $$ [-1,1] $$, cấu trúc toán tử tự liên hợp và mở rộng sang hàm cầu điều hòa.

## Video tham khảo

- Xem trước: [Intro to Legendre Polynomials](https://www.youtube.com/watch?v=djlUmwbPw20) — Physics and Math Lectures, tiếng Anh. Giới thiệu đa thức Legendre và lý do phương trình cho nghiệm đa thức tại các bậc nguyên.
- [Lecture 42 part 3 (Orthogonality of Legendre Polynomials)](https://www.youtube.com/watch?v=gwTmJN8mucE) — Daniel Maxin, tiếng Anh. Chứng minh và phân tích tính trực giao của đa thức Legendre trên $$ [-1,1] $$.
- [Legendre Polynomial | Orthogonal Properties of Legendre Polynomial](https://www.youtube.com/watch?v=RDU7FTqgx7s) — Dr.Gajendra Purohit, tiếng Anh. Trình bày các hệ thức trực giao phục vụ khai triển hàm số.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: giới thiệu phương trình Legendre, hệ thức truy hồi và các tính chất cơ bản.
- Haberman, Chương 7: phân tích vai trò của đa thức Legendre trong các bài toán vật lý có đối xứng cầu.
