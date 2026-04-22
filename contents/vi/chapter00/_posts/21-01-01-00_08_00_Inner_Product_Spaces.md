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

## Mục tiêu

Bài học này giúp sinh viên hiểu không gian tích vô hướng như nơi hình học Euclid được mở rộng sang không gian hàm và không gian vô hạn chiều. Sau bài học, sinh viên cần nắm định nghĩa tích vô hướng, hiểu mối liên hệ giữa tích vô hướng, norm và góc, vận dụng bất đẳng thức Cauchy-Schwarz, nhận diện trực giao và phép chiếu trực giao, và thấy vì sao đây là nền tảng của không gian Hilbert và khai triển trực giao trong phương trình vi phân.

## Kiến thức nền

Sinh viên cần nắm không gian vector, chuẩn, và trực giác hình học của tích vô hướng trên $$ \mathbb{R}^n $$. Kiến thức về tích phân cũng rất hữu ích vì một trong những ví dụ quan trọng nhất của bài là tích vô hướng trên không gian hàm

$$ \langle f,g\rangle=\int_a^b f(x)g(x)\,dx. $$

## Dẫn nhập

Không gian chuẩn cho ta độ lớn, nhưng chưa cho ta góc. Trong nhiều bài toán toán học và vật lý, ta không chỉ muốn biết một vector hay một hàm lớn đến đâu, mà còn muốn biết hai đối tượng đó “giống nhau” hay “vuông góc” đến mức nào. Đó là lúc tích vô hướng xuất hiện.

Trong ODE và PDE, ý tưởng trực giao là chìa khóa cho chuỗi Fourier, bài toán Sturm-Liouville, khai triển theo eigenfunctions, và cả nguyên lý bình phương tối thiểu. Vì vậy, bài này là cửa mở từ hình học tuyến tính cơ bản sang giải tích hàm và phổ toán tử.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy nghĩ tích vô hướng như thước đo mức độ cùng hướng của hai vector. Nếu hai vector cùng hướng, tích vô hướng dương và lớn. Nếu vuông góc, tích vô hướng bằng 0. Nếu ngược hướng, tích vô hướng âm. Khi chuyển sang không gian hàm, ý tưởng ấy vẫn còn: hai hàm có thể được xem là “trực giao” nếu dao động của chúng triệt tiêu nhau khi lấy tích phân.

### Cách nhìn hình ảnh

Giáo viên nên vẽ hai vector $$ u,v $$ trong mặt phẳng và nhắc công thức Euclid $$u\cdot v=\lVert u\rVert\,\lVert v\rVert\cos \theta$$.

Sau đó chuyển sang đồ thị hai hàm sin và cos trên một khoảng đầy đủ chu kỳ để minh họa trực giao của hàm. Hình này rất hữu ích vì nó cho thấy “vuông góc” không chỉ tồn tại trong hình học phẳng mà còn trong không gian hàm.

### Cách nhìn hình thức

Một tích vô hướng trên không gian vector thực $$ X $$ là một ánh xạ $$ \langle\cdot,\cdot\rangle:X\times X\to \mathbb{R} $$ thỏa với mọi $$ x,y,z\in X $$ và vô hướng $$ \alpha $$:

$$ \langle x,y\rangle=\langle y,x\rangle, $$

$$
\langle \alpha x+y,z\rangle=\alpha\langle x,z\rangle+\langle y,z\rangle,
$$

$$
\langle x,x\rangle\ge 0,\qquad \langle x,x\rangle=0 \Leftrightarrow x=0.
$$

Từ tích vô hướng, ta sinh ra norm: $$ \lVert x\rVert=\sqrt{\langle x,x\rangle} $$.

## Những ngộ nhận thường gặp

- “Mọi norm đều đến từ một tích vô hướng.” Sai. Có nhiều norm không thể sinh từ tích vô hướng.
- “Trực giao chỉ có nghĩa trong hình học 2D hay 3D.” Sai. Trực giao là khái niệm rất tự nhiên trong không gian hàm.
- “Nếu hai hàm không giống nhau thì không thể trực giao.” Sai. Sin và cos là ví dụ kinh điển của hai hàm khác nhau nhưng trực giao.
- “Cauchy-Schwarz chỉ là bất đẳng thức kỹ thuật.” Không. Nó là định lý cốt lõi làm cho khái niệm góc, chiếu, và ước lượng năng lượng hoạt động.

## Tiến trình học tập đề xuất

### Bước 1: Bắt đầu từ Euclid

Nhắc lại dot product quen thuộc để sinh viên không thấy khái niệm quá đột ngột.

### Bước 2: Tổng quát hóa sang không gian hàm

Đây là bước quan trọng nhất của bài.

### Bước 3: Học Cauchy-Schwarz và trực giao

Hai công cụ này là xương sống của hình học trong không gian tích vô hướng.

### Bước 4: Đi tới phép chiếu và Hilbert space

Cho sinh viên thấy ứng dụng trong xấp xỉ và chuỗi trực giao.

### Các checkpoint

- Sinh viên có kiểm tra được một tích vô hướng hợp lệ không?
- Sinh viên có giải thích được trực giao của hai hàm không?
- Sinh viên có hiểu vì sao tích vô hướng sinh ra norm không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tích vô hướng Euclid

Với $$ u=(1,2),\qquad v=(3,-1) $$, ta có $$ \langle u,v\rangle=1\cdot 3+2\cdot (-1)=1 $$. Vì tích vô hướng dương, góc giữa hai vector là góc nhọn. Đây là ví dụ đơn giản nhất cho ý nghĩa hình học của inner product.

### Ví dụ 2: Cauchy-Schwarz

Với mọi $$ u,v $$ trong không gian tích vô hướng,

$$
\lvert\langle u,v\rangle\rvert\le \lVert u\rVert\,\lVert v\rVert.
$$

Trong ví dụ trên,

$$
\lVert u\rVert=\sqrt{5},\qquad \lVert v\rVert=\sqrt{10},
$$

nên $$ \lvert\langle u,v\rangle\rvert=1\le \sqrt{50} $$. Ví dụ số học này giúp sinh viên kiểm tra trực tiếp bất đẳng thức.

### Ví dụ 3: Trực giao của sin và cos

Trên khoảng $$ [0,2\pi] $$, đặt

$$ \langle f,g\rangle=\int_0^{2\pi} f(x)g(x)\,dx. $$

Khi đó

$$
\langle \sin x,\cos x\rangle=\int_0^{2\pi}\sin x\cos x\,dx=0.
$$

Vậy $$ \sin x $$ và $$ \cos x $$ trực giao. Đây là nền cho khai triển Fourier.

### Ví dụ 4: Phép chiếu trực giao

Chiếu vector $$ u=(2,1) $$ lên hướng của $$ v=(1,1) $$. Ta có

$$
\operatorname{proj}_v u=\frac{\langle u,v\rangle}{\langle v,v\rangle}v.
$$

Vì $$ \langle u,v\rangle=3,\qquad \langle v,v\rangle=2 $$, nên

$$ \operatorname{proj}_v u=\frac32(1,1). $$

Ví dụ này cho thấy tích vô hướng dẫn trực tiếp tới xấp xỉ tốt nhất theo một hướng.

## Câu hỏi khái niệm

1. Vì sao tích vô hướng mạnh hơn norm về mặt thông tin hình học?
2. Tại sao trực giao của hai hàm là khái niệm tự nhiên dù ta không thể “vẽ góc” giữa chúng như trong mặt phẳng?
3. Điều gì làm cho Cauchy-Schwarz trở thành định lý nền của không gian tích vô hướng?

## Bài toán ứng dụng

1. Trong chuỗi Fourier, vì sao trực giao của các mode sin-cos giúp tính hệ số khai triển dễ dàng?
2. Trong bình phương tối thiểu, phép chiếu trực giao giải thích thế nào việc tìm xấp xỉ tốt nhất?
3. Trong cơ học lượng tử, vì sao không gian trạng thái tự nhiên thường là Hilbert space chứ không chỉ là Banach space?

## Chiến lược giảng dạy tương tác

### Câu hỏi nên hỏi trên lớp

- Hai hàm có thể “vuông góc” theo nghĩa nào?
- Nếu không có tích vô hướng, ta còn định nghĩa góc và phép chiếu được không?
- Em thấy trực giao trong Fourier giống trực giao trong hình học phẳng ở điểm nào?

### Hoạt động gợi ý

- Cho sinh viên tính tích vô hướng của vài cặp vector và vài cặp hàm đơn giản.
- Vẽ phép chiếu trực giao của một vector lên một đường trong mặt phẳng.
- Thảo luận nhóm về ý nghĩa “mức độ giống nhau” của hai hàm qua tích vô hướng.

## Phân hóa học tập

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu hoàn toàn từ dot product trong $$ \mathbb{R}^2 $$.
- Dùng hình vẽ góc và phép chiếu trước khi chuyển sang không gian hàm.
- Cho nhiều ví dụ sin-cos trên khoảng đơn giản.

### Thử thách cho sinh viên khá giỏi

- Chứng minh bất đẳng thức Cauchy-Schwarz.
- Phân biệt chuẩn nào sinh từ tích vô hướng và chuẩn nào không.
- Liên hệ phép chiếu trực giao với bài toán tối ưu lồi đơn giản.

## Tóm tắt dễ nhớ

Không gian tích vô hướng mở rộng hình học Euclid sang không gian tổng quát. Nhờ inner product, ta có thể nói về góc, trực giao, phép chiếu, và từ đó xây dựng chuỗi trực giao, xấp xỉ tốt nhất, và không gian Hilbert cho giải tích hàm.

## Tài liệu tham khảo

- Kreyszig, *Introductory Functional Analysis with Applications*.
- Brezis, *Functional Analysis, Sobolev Spaces and PDEs*.
