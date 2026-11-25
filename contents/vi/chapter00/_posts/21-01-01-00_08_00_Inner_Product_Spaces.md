---
layout: post
title: "00-08 Không Gian Tích Vô Hướng"
chapter: '00'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter00
lesson_type: optional
---


Trong không gian định chuẩn, ta đo được độ dài nhưng chưa có khái niệm "góc vuông". Chỉ khi trang bị thêm **tích vô hướng $\langle f, g\rangle$**, toàn bộ hình học Euclid—định lý Pythagoras, phép chiếu vuông góc và trực giao hóa Gram–Schmidt—mới bừng sáng trong không gian hàm vô hạn chiều, mở thẳng cánh cửa tới chuỗi Fourier, đa thức Legendre và lý thuyết Sturm–Liouville!

## Kiến thức cần nhớ: Bốn trụ cột của Không gian Tích vô hướng & Hilbert

1. **Tích vô hướng $\langle u, v\rangle$ & Bất đẳng thức Cauchy–Schwarz**:
   Trên $L^2([a, b])$, tích vô hướng là $\langle f, g\rangle = \int_a^b f(x)\overline{g(x)}\,dx$; bất đẳng thức $\vert\langle f, g\rangle\vert \le \|f\|\,\|g\|$ đảm bảo khái niệm "góc giữa hai hàm số" luôn hợp lệ.
2. **Tính trực giao ($\langle f, g\rangle = 0$) & Hệ trực chuẩn**:
   Hai hàm trực giao (như $\sin(nx)$ và $\sin(mx)$ với $n \ne m$) đóng vai trò như các trục tọa độ vuông góc—giúp phân tích một hàm phức tạp thành tổng các thành phần độc lập mà không bị nhiễu chéo.
3. **Phép chiếu trực giao & Xấp xỉ bình phương tối thiểu**:
   Hình chiếu $\sum \frac{\langle f, e_k\rangle}{\|e_k\|^2} e_k$ là xấp xỉ **tốt nhất duy nhất** của $f$ theo chuẩn $L^2$ trong không gian con sinh bởi $\{e_k\}$.
4. **Không gian Hilbert & Khai triển Fourier tổng quát**:
   Không gian tích vô hướng đầy đủ gọi là không gian Hilbert (như $L^2$), nơi mọi hàm bình phương khả tích đều khai triển được thành chuỗi trực giao và thỏa đẳng thức Parseval $\|f\|^2 = \sum \vert c_k\vert^2$.

## Mục tiêu

Bài học này giúp sinh viên hiểu không gian tích vô hướng như sự mở rộng hình học Euclid sang không gian hàm và không gian vô hạn chiều. Sau bài học, sinh viên có thể nắm định nghĩa tích vô hướng, hiểu mối liên hệ giữa tích vô hướng, chuẩn và góc, vận dụng bất đẳng thức Cauchy–Schwarz, nhận diện tính trực giao cùng phép chiếu trực giao, và thấy vai trò của chúng trong không gian Hilbert cũng như các khai triển trực giao cho phương trình vi phân.

## Kiến thức nền

Sinh viên cần nắm vững không gian vector, khái niệm chuẩn và trực giác hình học của tích vô hướng trên $$ \mathbb{R}^n $$. Kiến thức về tích phân xác định cũng rất cần thiết vì một ví dụ trung tâm của bài là tích vô hướng trên không gian hàm:

$$
\langle f,g\rangle=\int_a^b f(x)g(x)\,dx.
$$

## Dẫn nhập

Không gian định chuẩn cho phép đo độ lớn, nhưng chưa cung cấp khái niệm góc. Trong nhiều bài toán toán học và vật lý, ta không chỉ cần biết một vector hay một hàm lớn bao nhiêu mà còn cần biết hai đối tượng tương quan hay vuông góc với nhau ra sao. Tích vô hướng ra đời để đáp ứng đúng nhu cầu đó.

Trong ODE và PDE, khái niệm trực giao là chìa khóa của chuỗi Fourier, bài toán Sturm–Liouville, khai triển theo hàm riêng (eigenfunctions) và phương pháp bình phương tối thiểu. Bài học này đóng vai trò cầu nối từ hình học tuyến tính sơ cấp sang giải tích hàm và lý thuyết phổ.

### Giải thích: Trực giao hóa Gram–Schmidt cho $\{1, x, x^2\}$ trên $[-1, 1]$ để tự sinh ra đa thức Legendre!

Với tích vô hướng $\langle f, g\rangle = \int_{-1}^1 f(x)g(x)\,dx$:
1. **Chọn $p_0(x) = 1$**: $\|p_0\|^2 = \int_{-1}^1 1\,dx = 2$.
2. **Trực giao hóa $x$ với $p_0$**:
   $\langle x, 1\rangle = \int_{-1}^1 x\,dx = 0$ (hàm lẻ trên miền đối xứng). Vậy $p_1(x) = \mathbf{x}$, với $\|p_1\|^2 = \int_{-1}^1 x^2\,dx = \frac{2}{3}$.
3. **Trực giao hóa $x^2$ với $p_0$ và $p_1$**:
   - $\langle x^2, 1\rangle = \int_{-1}^1 x^2\,dx = \frac{2}{3}$.
   - $\langle x^2, x\rangle = \int_{-1}^1 x^3\,dx = 0$.
   - Suy ra:
     $$p_2(x) = x^2 - \frac{\langle x^2, 1\rangle}{\|1\|^2}\cdot 1 = x^2 - \frac{2/3}{2} = \mathbf{x^2 - \frac{1}{3}}.$$
4. **Chuẩn hóa sao cho $P_2(1) = 1$**: Nhân $p_2(x)$ với $\frac{3}{2}$, ta thu được ngay đa thức Legendre $P_2(x) = \frac{3x^2 - 1}{2}$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Có thể xem tích vô hướng như thước đo mức độ cùng phương giữa hai vector: tích vô hướng dương và lớn khi hai vector cùng hướng, bằng $$ 0 $$ khi vuông góc và âm khi ngược hướng. Khi mở rộng sang không gian hàm, trực giác này vẫn giữ nguyên: hai hàm được xem là trực giao nếu tích của chúng có phần dương và phần âm triệt tiêu nhau hoàn toàn khi lấy tích phân trên miền xét.

### Cách nhìn hình ảnh

Bắt đầu từ hai vector $$ u,v $$ trong mặt phẳng với công thức Euclid $$u\cdot v=\lVert u\rVert\,\lVert v\rVert\cos \theta$$. Sau đó đối chiếu với đồ thị của hai hàm $$ \sin x $$ và $$ \cos x $$ trên một chu kỳ đầy đủ $$ [0,2\pi] $$ để minh họa tính trực giao của hàm số. Sự đối chiếu này giúp thấy rõ khái niệm vuông góc không chỉ tồn tại trong hình học phẳng mà còn mở rộng tự nhiên sang không gian hàm.

### Cách nhìn hình thức

Một tích vô hướng trên không gian vector thực $$ X $$ là ánh xạ $$ \langle\cdot,\cdot\rangle:X\times X\to \mathbb{R} $$ thỏa mãn ba tính chất sau với mọi $$ x,y,z\in X $$ và mọi vô hướng $$ \alpha \in \mathbb{R} $$:

$$
\langle x,y\rangle=\langle y,x\rangle,
$$

$$
\langle \alpha x+y,z\rangle=\alpha\langle x,z\rangle+\langle y,z\rangle,
$$

$$
\langle x,x\rangle\ge 0,\qquad \langle x,x\rangle=0 \Leftrightarrow x=0.
$$

Từ tích vô hướng, ta luôn cảm sinh được một chuẩn: $$ \lVert x\rVert=\sqrt{\langle x,x\rangle} $$.

## Những ngộ nhận thường gặp

- "Mọi chuẩn đều sinh ra từ một tích vô hướng." Sai. Nhiều chuẩn (như $$ \lVert \cdot\rVert_1 $$ hay $$ \lVert \cdot\rVert_\infty $$ trên $$ \mathbb{R}^2 $$) không thể cảm sinh từ bất kỳ tích vô hướng nào.
- "Trực giao chỉ có nghĩa trong hình học hai chiều hoặc ba chiều." Sai. Trực giao định nghĩa hoàn toàn tự nhiên trong không gian hàm thông qua tích phân.
- "Hai hàm khác hẳn nhau thì không thể trực giao." Sai. $$ \sin x $$ và $$ \cos x $$ trên $$ [0,2\pi] $$ là ví dụ kinh điển của hai hàm khác nhau nhưng trực giao.
- "Bất đẳng thức Cauchy–Schwarz chỉ là một ước lượng kỹ thuật phụ." Sai. Đây là bất đẳng thức cốt lõi bảo đảm định nghĩa góc hợp lệ, đồng thời là nền tảng cho phép chiếu và các ước lượng năng lượng.

## Tiến trình học tập đề xuất

### Bước 1: Bắt đầu từ tích vô hướng Euclid

Ôn lại tích vô hướng thông thường (dot product) trong $$ \mathbb{R}^2 $$ và $$ \mathbb{R}^3 $$ để giữ trực giác hình học rõ ràng.

### Bước 2: Mở rộng sang không gian hàm

Làm quen với tích vô hướng tích phân và cách tính trên các hàm sơ cấp.

### Bước 3: Nắm vững Cauchy–Schwarz và tính trực giao

Sử dụng hai công cụ này làm trụ cột cho hình học trong không gian tích vô hướng.

### Bước 4: Tiếp cận phép chiếu trực giao và không gian Hilbert

Liên hệ phép chiếu trực giao với bài toán xấp xỉ tốt nhất và khai triển thành chuỗi trực giao.

### Các checkpoint

- Bạn có kiểm tra được một ánh xạ cho trước có phải là tích vô hướng hợp lệ không?
- Bạn có giải thích được ý nghĩa trực giao của hai hàm số không?
- Bạn có hiểu cách tích vô hướng cảm sinh chuẩn không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tích vô hướng Euclid

Với $$ u=(1,2) $$ và $$ v=(3,-1) $$, ta có $$ \langle u,v\rangle=1\cdot 3+2\cdot (-1)=1 $$. Vì tích vô hướng dương, góc giữa hai vector là góc nhọn.

### Ví dụ 2: Bất đẳng thức Cauchy–Schwarz

Với mọi $$ u,v $$ trong không gian tích vô hướng,

$$
\lvert\langle u,v\rangle\rvert\le \lVert u\rVert\,\lVert v\rVert.
$$

Áp dụng cho hai vector ở Ví dụ 1, ta có

$$
\lVert u\rVert=\sqrt{5},\qquad \lVert v\rVert=\sqrt{10},
$$

nên $$ \lvert\langle u,v\rangle\rvert=1\le \sqrt{50} $$, phù hợp với bất đẳng thức trên.

### Ví dụ 3: Tính trực giao của $$ \sin x $$ và $$ \cos x $$

Trên đoạn $$ [0,2\pi] $$, xét tích vô hướng

$$
\langle f,g\rangle=\int_0^{2\pi} f(x)g(x)\,dx.
$$

Khi đó

$$
\langle \sin x,\cos x\rangle=\int_0^{2\pi}\sin x\cos x\,dx=0.
$$

Vậy $$ \sin x $$ và $$ \cos x $$ trực giao với nhau trên $$ [0,2\pi] $$. Đây là nền tảng cho khai triển chuỗi Fourier.

### Ví dụ 4: Phép chiếu trực giao

Chiếu vector $$ u=(2,1) $$ lên phương của vector $$ v=(1,1) $$. Công thức phép chiếu trực giao là

$$
\operatorname{proj}_v u=\frac{\langle u,v\rangle}{\langle v,v\rangle}v.
$$

Vì $$ \langle u,v\rangle=3 $$ và $$ \langle v,v\rangle=2 $$, ta thu được

$$
\operatorname{proj}_v u=\frac32(1,1).
$$

Phép chiếu này cho xấp xỉ tốt nhất của $$ u $$ theo phương $$ v $$ tính theo chuẩn cảm sinh.

## Câu hỏi khái niệm

1. Vì sao cấu trúc tích vô hướng cung cấp nhiều thông tin hình học hơn so với cấu trúc chuẩn?
2. Vì sao khái niệm trực giao của hai hàm số vẫn hoàn toàn tự nhiên dù ta không thể vẽ trực tiếp góc giữa chúng như trong mặt phẳng?
3. Bất đẳng thức Cauchy–Schwarz đóng vai trò gì trong việc xây dựng hình học của không gian tích vô hướng?

## Bài toán ứng dụng

1. Trong chuỗi Fourier, vì sao tính trực giao của các hàm sin và cos giúp xác định từng hệ số khai triển một cách độc lập?
2. Trong phương pháp bình phương tối thiểu, phép chiếu trực giao giải thích như thế nào cho bài toán tìm xấp xỉ tốt nhất?
3. Trong cơ học lượng tử, vì sao không gian trạng thái thường là không gian Hilbert chứ không chỉ dừng ở không gian Banach?

## Chiến lược giảng dạy tương tác

### Câu hỏi nên hỏi trên lớp

- Hai hàm số có thể được xem là "vuông góc" với nhau theo nghĩa nào?
- Nếu chỉ có chuẩn mà không có tích vô hướng, ta có định nghĩa được góc và phép chiếu trực giao không?
- Tính trực giao trong chuỗi Fourier giống tính vuông góc trong hình học phẳng ở điểm nào?

### Hoạt động gợi ý

- Cho sinh viên tính tích vô hướng của một số cặp vector và cặp hàm đơn giản.
- Vẽ hình minh họa phép chiếu trực giao của một vector lên một đường thẳng trong mặt phẳng.
- Thảo luận nhóm về ý nghĩa "mức độ tương quan" giữa hai hàm thông qua tích vô hướng.

## Phân hóa học tập

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu hoàn toàn từ tích vô hướng Euclid (dot product) trong $$ \mathbb{R}^2 $$.
- Minh họa kỹ góc và phép chiếu trên hình vẽ trước khi chuyển sang không gian hàm.
- Luyện tập trên các cặp hàm sin–cos đơn giản trên những khoảng quen thuộc.

### Thử thách cho sinh viên khá giỏi

- Chứng minh bất đẳng thức Cauchy–Schwarz từ các tiên đề tích vô hướng.
- Sử dụng đẳng thức hình bình hành để phân biệt chuẩn cảm sinh từ tích vô hướng với chuẩn không cảm sinh từ tích vô hướng.
- Liên hệ phép chiếu trực giao với bài toán tối ưu khoảng cách đến một không gian con.

## Tóm tắt dễ nhớ

Không gian tích vô hướng mở rộng hình học Euclid sang các không gian tổng quát. Nhờ tích vô hướng, ta định nghĩa được chuẩn, góc, tính trực giao và phép chiếu trực giao—những công cụ nền cho chuỗi trực giao, xấp xỉ bình phương tối thiểu và không gian Hilbert trong giải tích hàm.

## Video tham khảo

- Xem trước: [Inner Products and Inner Product Spaces | Linear Algebra](https://www.youtube.com/watch?v=RWLhjq2rfcw) — Wrath of Math, tiếng Anh. Trình bày các tiên đề tích vô hướng và chuẩn cảm sinh từ tích vô hướng.
- [Proof of the Cauchy-Schwarz inequality | Vectors and spaces | Linear Algebra | Khan Academy](https://www.youtube.com/watch?v=r2PogGDl8_U) — Khan Academy, tiếng Anh. Chứng minh bất đẳng thức Cauchy–Schwarz, cơ sở của khái niệm góc và các ước lượng Fourier.
- [Dot products and duality | Chapter 9, Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0) — 3Blue1Brown, tiếng Anh. Cách nhìn hình học về tích vô hướng và tính đối ngẫu, hữu ích trước khi học tích vô hướng trừu tượng.

## Tài liệu tham khảo

- Kreyszig, *Introductory Functional Analysis with Applications*.
- Brezis, *Functional Analysis, Sobolev Spaces and PDEs*.
