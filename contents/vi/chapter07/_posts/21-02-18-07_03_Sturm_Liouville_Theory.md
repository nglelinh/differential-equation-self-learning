---
layout: post
title: "07-03 Lý thuyết Sturm-Liouville"
chapter: '07'
order: 3
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

Trong đại số tuyến tính, ma trận đối xứng thực $A = A^T$ sở hữu những tính chất đẹp như mơ: mọi trị riêng đều thực, các vectơ riêng ứng với trị riêng khác nhau thì vuông góc với nhau, và chúng lập thành cơ sở cho toàn không gian. **Lý thuyết Sturm–Liouville** nâng toàn bộ định lý phổ tuyệt đẹp đó lên **không gian hàm vô hạn chiều** cho toán tử vi phân tự liên hợp $L[y] = -\frac{d}{dx}[p(x)y'] + q(x)y = \lambda w(x)y$!

## Bản đồ kiến thức nền: Bốn định lý vàng của Lý thuyết Sturm–Liouville Chính quy

1. **Tính tự liên hợp (Self-Adjointness) & Đồng nhất thức Lagrange**:
   Tích phân từng phần hai lần cho $\int_a^b (u L[v] - v L[u])\,dx = -\big[p(x)(u v' - v u')\big]_a^b$. Với điều kiện biên tách rời chuẩn, vế biên triệt tiêu $\implies \langle u, L[v]\rangle = \langle L[u], v\rangle$!
2. **Trị riêng thực, đơn và sắp thứ tự tăng dần**:
   Mọi trị riêng của bài toán Sturm–Liouville chính quy ($p(x) > 0, w(x) > 0$ trên $[a, b]$) đều là **số thực**, mỗi trị riêng chỉ có 1 hàm riêng độc lập (bội 1), và $\lambda_1 < \lambda_2 < \lambda_3 < \dots \to +\infty$.
3. **Tính trực giao theo hàm trọng số $w(x)$**:
   Nếu $\lambda_m \neq \lambda_n$, thì $\langle \phi_m, \phi_n \rangle_w = \int_a^b \phi_m(x)\phi_n(x) w(x)\,dx = 0$!
4. **Tính đầy đủ (Completeness) & Thương số Rayleigh**:
   Hệ hàm riêng $\{\phi_n\}$ lập thành cơ sở trực giao của $L^2_w(a, b)$, và trị riêng nhỏ nhất thỏa nguyên lý biến phân $\lambda_1 = \min_{y \not\equiv 0} \frac{\int_a^b (p y'^2 + q y^2)\,dx}{\int_a^b w y^2\,dx}$!

## Mục tiêu

Bài học này trình bày lý thuyết Sturm–Liouville như khuôn khổ thống nhất của bài toán trị riêng vi phân. Sau bài học, sinh viên cần nhận diện được dạng Sturm–Liouville chuẩn, hiểu ý nghĩa của tính tự liên hợp, giải thích được vì sao các trị riêng là số thực và các hàm riêng ứng với trị riêng khác nhau trực giao theo trọng số, đồng thời thấy rõ cầu nối giữa ODE, chuỗi Fourier tổng quát và các PDE tách biến.

## Kiến thức nền

Sinh viên nên nắm vững bài toán trị riêng cơ bản, kỹ thuật tích phân từng phần và trực giác về cơ sở trực giao từ đại số tuyến tính hoặc chuỗi Fourier. Nếu bài 07-02 đóng vai trò một ví dụ điển hình, thì bài này tổng quát hóa và giải thích cấu trúc toán học đứng sau ví dụ đó.

## Dẫn nhập

![Cấu trúc tự liên hợp của bài toán Sturm-Liouville]({{ site.imgurl }}/chapter_img/chapter07/03_sturm_liouville_theory.svg)

Đằng sau nhiều bài toán trị riêng có tham số trong vật lý toán tồn tại một cấu trúc chung rất chặt chẽ: một toán tử vi phân tự liên hợp, một hàm trọng số dương, một phổ trị riêng thực và một hệ hàm riêng trực giao. Lý thuyết mô tả cấu trúc tổng quát đó gọi là **lý thuyết Sturm–Liouville**.

Nhờ lý thuyết này, các kết quả về hàm Bessel, đa thức Legendre, chuỗi Fourier tổng quát và khai triển theo hàm riêng được đặt vào cùng một hệ thống thống nhất thay vì tách rời từng công thức.

### Khung giải thích (nên đọc chậm): Dùng Thương số Rayleigh ước lượng cực nhanh trị riêng nhỏ nhất $\lambda_1$ bằng một đa thức đơn giản

Xét bài toán $-y'' = \lambda y$ trên $[0, 1]$ với $y(0) = y(1) = 0$. Ta biết giá trị chính xác là $\lambda_1 = \pi^2 \approx \mathbf{9{,}8696}$.
Thử dùng một hàm thử đa thức cực đơn giản thỏa đúng điều kiện biên: $u(x) = x(1 - x) = x - x^2$ (thì $u'(x) = 1 - 2x$).
1. **Tính tử số**:
   $$\int_0^1 [u'(x)]^2\,dx = \int_0^1 (1 - 4x + 4x^2)\,dx = 1 - 2 + \frac{4}{3} = \frac{1}{3}.$$
2. **Tính mẫu số**:
   $$\int_0^1 [u(x)]^2\,dx = \int_0^1 (x^2 - 2x^3 + x^4)\,dx = \frac{1}{3} - \frac{1}{2} + \frac{1}{5} = \frac{1}{30}.$$
3. **Thương số Rayleigh**:
   $$R[u] = \frac{1/3}{1/30} = \mathbf{10{,}000} \ge \lambda_1 = 9{,}8696!$$
Chỉ bằng một đa thức bậc 2 đơn giản tính trong 30 giây, ta đã ước lượng cận trên của $\pi^2$ với sai số chỉ **$1{,}3\%$**—đây chính là nền tảng của phương pháp Phần tử hữu hạn (FEM) và cơ học lượng tử biến phân!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Trong đại số tuyến tính, ma trận đối xứng thực có cấu trúc phổ rất đẹp: mọi trị riêng đều thực, các vector riêng ứng với trị riêng khác nhau trực giao và lập thành cơ sở trực giao. Lý thuyết Sturm–Liouville là phiên bản vô hạn chiều của kết quả đó, trong đó toán tử vi phân tự liên hợp đóng vai trò ma trận đối xứng và các hàm riêng đóng vai trò vector riêng.

### Cách nhìn hình ảnh

Khi vẽ các hàm riêng đầu tiên của một bài toán Sturm–Liouville, số không điểm (nút) bên trong miền tăng dần theo bậc trị riêng và các chế độ này không giao thoa lẫn nhau theo nghĩa tích phân có trọng số. Tích phân có trọng số của hai chế độ khác nhau triệt tiêu hoàn toàn, thể hiện tính độc lập hình học giữa các chế độ.

### Cách nhìn hình thức

Bài toán Sturm–Liouville dạng chuẩn có phương trình

$$ -(p(x)y')'+q(x)y=\lambda w(x)y,
\qquad a<x<b, $$

với $$ p(x)>0 $$, $$ w(x)>0 $$ cùng các điều kiện biên thuần nhất tách biệt thích hợp. Do tính tự liên hợp của toán tử, bài toán Sturm–Liouville chính quy có các tính chất nền tảng sau:

- Mọi trị riêng đều là số thực và lập thành một dãy tăng dần ra vô cực.
- Các hàm riêng ứng với các trị riêng khác nhau trực giao theo hàm trọng số $$ w(x) $$.
- Hệ các hàm riêng tạo thành một cơ sở đầy đủ để khai triển hàm trong không gian $$ L^2_w(a,b) $$.

## Những ngộ nhận thường gặp

- "Dạng Sturm–Liouville chỉ là cách viết lại hình thức." Sai. Dạng viết này làm lộ rõ tính tự liên hợp — yếu tố quyết định toàn bộ tính chất phổ.
- "Hàm trọng số $$ w(x) $$ chỉ là hệ số phụ." Sai. Nó xác định trực tiếp tích vô hướng tự nhiên của bài toán.
- "Tính trực giao chỉ là kết quả tính toán tình cờ." Sai. Nó là hệ quả trực tiếp của tính tự liên hợp và điều kiện biên.
- "Lý thuyết này quá trừu tượng, ít gắn với vật lý." Sai. Hầu hết các bài toán chế độ riêng trong cơ học, nhiệt học và cơ học lượng tử đều thuộc khung Sturm–Liouville.

## Tiến trình học tập đề xuất

### Bước 1: Nhìn lại bài toán trị riêng cơ bản

Xuất phát từ bài toán dây đàn để tìm hiểu cơ chế tạo nên tính thực của trị riêng và tính trực giao của hàm sin.

### Bước 2: Đưa phương trình về dạng tự liên hợp

Luyện cách biến đổi phương trình vi phân cấp hai về dạng chuẩn $$ -(py')'+qy=\lambda wy $$ (nhân thừa số tích phân nếu cần).

### Bước 3: Nắm khái niệm tích vô hướng có trọng số

Liên hệ tích phân có trọng số $$ w(x) $$ với tích vô hướng trong đại số tuyến tính.

### Bước 4: Chứng minh tính trực giao bằng tích phân từng phần

Thực hiện cẩn thận phép tích phân từng phần (đồng nhất thức Lagrange) và thấy vai trò của điều kiện biên trong việc triệt tiêu các số hạng biên.

### Bước 5: Diễn giải các hệ quả phổ

Ghi nhớ bộ tính chất cốt lõi: trị riêng thực, hàm riêng trực giao và thứ tự tăng dần của số nút.

### Các điểm kiểm tra

- Sinh viên có xác định đúng hàm trọng số $$ w(x) $$ của bài toán hay không.
- Sinh viên có giải thích được sự tương đồng giữa toán tử tự liên hợp và ma trận đối xứng thực hay không.
- Sinh viên có tự trình bày được chứng minh tính trực giao của hai hàm riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bài toán sin cổ điển dưới dạng Sturm–Liouville

Xét bài toán

$$ y''+\lambda y=0,
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Viết lại dưới dạng chuẩn:

$$ -y''=\lambda y, $$

tương ứng với $$ p(x)=1 $$, $$ q(x)=0 $$ và $$ w(x)=1 $$. Đây là trường hợp Sturm–Liouville đơn giản nhất, khẳng định rằng chuỗi Fourier sin là một trường hợp riêng của lý thuyết tổng quát.

### Ví dụ 2: Chứng minh tính trực giao của hai hàm riêng

Giả sử $$ \phi_m $$ và $$ \phi_n $$ lần lượt là hàm riêng ứng với hai trị riêng $$ \lambda_m $$ và $$ \lambda_n $$:

$$ -(p\phi_m')'+q\phi_m=\lambda_m w\phi_m,\qquad -(p\phi_n')'+q\phi_n=\lambda_n w\phi_n. $$

Nhân phương trình thứ nhất với $$ \phi_n $$, phương trình thứ hai với $$ \phi_m $$, trừ vế theo vế rồi lấy tích phân trên $$ [a,b] $$. Áp dụng tích phân từng phần, các số hạng tại biên triệt tiêu nhờ điều kiện biên, thu được:

$$
(\lambda_m-\lambda_n)\int_a^b \phi_m(x)\phi_n(x)w(x)\,dx=0.
$$

Khi $$ \lambda_m\ne \lambda_n $$, suy ra ngay:

$$ \int_a^b \phi_m(x)\phi_n(x)w(x)\,dx=0. $$

Phép chứng minh ngắn gọn này là hạt nhân lý thuyết của cả chương.

### Ví dụ 3: Vai trò của hàm trọng số

Xét bài toán có dạng

$$ -(xy')'=\lambda x y,
\qquad 0<x<1. $$

Ở đây hàm trọng số là $$ w(x)=x $$, nên điều kiện trực giao đúng phải là

$$ \int_0^1 \phi_m(x)\phi_n(x)x\,dx=0, $$

chứ không phải tích phân không có trọng số. Ví dụ này giúp tránh sai sót phổ biến khi bỏ quên trọng số trong khai triển hàm riêng.

### Ví dụ 4: Liên hệ với phương trình Bessel và Legendre

Sau khi đưa về dạng tự liên hợp, phương trình Legendre, phương trình Bessel và nhiều phương trình đặc biệt ở Chương 06 đều nằm gọn trong khuôn khổ Sturm–Liouville. Điều này gắn kết Chương 06 và Chương 07 thành một hệ thống thống nhất.

## Câu hỏi khái niệm

1. Tính tự liên hợp của toán tử vi phân tương ứng như thế nào với tính đối xứng của ma trận trong đại số tuyến tính?
2. Vì sao tính trực giao giữa các hàm riêng ứng với trị riêng phân biệt lại có giá trị thực tiễn lớn?
3. Hàm trọng số $$ w(x) $$ đóng vai trò gì trong cấu trúc của bài toán Sturm–Liouville?

## Bài toán ứng dụng

1. Trong bài toán truyền nhiệt hoặc dao động, vì sao việc sở hữu một họ chế độ trực giao giúp giải bài toán thuận lợi hơn nhiều?
2. Khi một mô hình vật lý dẫn tới phương trình có hệ số biến thiên, việc viết lại phương trình dưới dạng Sturm–Liouville mang lại lợi ích gì?
3. Trong các hệ dao động cơ học, vì sao các chế độ riêng khác nhau được xem là độc lập về mặt năng lượng?

## Chiến lược giảng dạy tương tác

- Đặt câu hỏi mở đầu: ma trận đối xứng thực có những tính chất phổ nổi bật nào, và điều gì được bảo toàn khi chuyển sang toán tử vi phân?
- Cho sinh viên lập bảng đối chiếu giữa đại số tuyến tính và Sturm–Liouville: vector riêng – hàm riêng, tích vô hướng – tích phân có trọng số, tính đối xứng – tính tự liên hợp.
- Phân tích chậm bước tích phân từng phần trong chứng minh trực giao để làm rõ vai trò triệt tiêu số hạng biên của điều kiện biên.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên duy trì sự đối chiếu liên tục với đại số tuyến tính và chuỗi Fourier quen thuộc để giảm cảm giác trừu tượng khi làm việc trong không gian hàm.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu thêm về tính đầy đủ của hệ hàm riêng hoặc nguyên lý cực trị Rayleigh–Ritz cho trị riêng nhỏ nhất — bước chuẩn bị tốt cho giải tích hàm và PDE.

## Tóm tắt dễ nhớ

Lý thuyết Sturm–Liouville là phiên bản vô hạn chiều của lý thuyết phổ cho ma trận đối xứng thực. Dạng tự liên hợp kết hợp điều kiện biên thích hợp bảo đảm các trị riêng thực, các hàm riêng trực giao theo hàm trọng số $$ w(x) $$ và mở đường cho khai triển hàm theo hệ hàm riêng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động dây không đồng nhất
- Bài toán: Dây có mật độ khối lượng thay đổi theo vị trí dẫn đến bài toán chế độ riêng có hàm trọng số.
- Mô hình:
$$ -(p(x)y')'+q(x)y=\lambda w(x)y. $$
- Giả thiết và giới hạn: Hệ tuyến tính, điều kiện biên chính quy, $$ p(x)>0 $$ và $$ w(x)>0 $$.
- Diễn giải: Lý thuyết Sturm–Liouville bảo đảm trị riêng thực và các chế độ dao động trực giao theo trọng số mật độ.

#### Truyền nhiệt hoặc khuếch tán trong môi trường không đồng nhất
- Bài toán: Tách biến phương trình nhiệt với hệ số dẫn nhiệt phụ thuộc vị trí dẫn tới toán tử tự liên hợp.
- Mô hình:
$$
\frac{d}{dx}\left(p(x)\frac{dy}{dx}\right)+(\lambda w(x)-q(x))y=0.
$$
- Giả thiết và giới hạn: Bài toán tách biến được với điều kiện biên thích hợp.
- Diễn giải: Tính tự liên hợp bảo đảm phổ thực và tính trực giao của các chế độ truyền nhiệt.

### 2. Trực giác bổ sung và các kết nối

Lý thuyết Sturm–Liouville đặt các bài toán trị riêng vào một khung toán tử có cấu trúc chặt chẽ. Thay vì học thuộc danh sách các tính chất rời rạc, cần nắm rõ nguồn gốc chung của chúng: phép tích phân từng phần kết hợp với điều kiện biên thuần nhất.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
y1 = np.sin(np.pi * x)
y2 = np.sin(2 * np.pi * x)

plt.plot(x, y1, label="phi1")
plt.plot(x, y2, label="phi2")
plt.fill_between(x, y1 * y2, alpha=0.3, color="orange", label="phi1 * phi2")
plt.xlabel("x")
plt.ylabel("value")
plt.title("Truc giao cua cac ham rieng co dinh bien")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Sturm Liouville orthogonality visualization
- search: self adjoint operator boundary value problem
- search: weighted orthogonality eigenfunctions

### 5. Bài toán mẫu có bối cảnh thực

Với bài toán trị riêng cơ bản
$$ y''+\lambda y=0,\qquad y(0)=y(L)=0, $$
các hàm riêng là
$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right) $$
thỏa mãn tính trực giao
$$ \int_0^L \phi_m(x)\phi_n(x)\,dx=0\qquad (m\ne n). $$
Đây là minh họa trực quan nhất cho cơ chế trực giao trong lý thuyết Sturm–Liouville.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm dạng chuẩn Sturm–Liouville, tính thực của trị riêng và tính trực giao có trọng số của hàm riêng.

**Bậc sau đại học.** Nghiên cứu toán tử tự liên hợp, không gian Hilbert có trọng số $$ L^2_w $$ và định lý phổ.

## Video tham khảo

- Xem trước: [Sturm-Liouville Theorem and Proof](https://www.youtube.com/watch?v=_F0ck1JncLE) — Faculty of Khan, tiếng Anh. Trình bày dạng tự liên hợp, trị riêng thực và tính trực giao của hàm riêng.
- [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, tiếng Anh. Phát triển đầy đủ lý thuyết Sturm–Liouville từ toán tử vi phân.
- [Sturm-Liouville Theory](https://www.youtube.com/watch?v=12d15vI52b8) — Nathan Kutz, tiếng Anh. Tổng quan lý thuyết và tính toán về Sturm–Liouville.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 11: trình bày khuôn khổ Sturm–Liouville, trọng số và tính trực giao hàm riêng.
- Haberman, Chương 5: giải thích trực giác về toán tử tự liên hợp trong các bài toán vật lý cổ điển.
