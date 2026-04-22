---
layout: post
title: "Lý Thuyết Phổ"
chapter: '12'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: optional
---

![Phổ của toán tử elliptic và các mode riêng cơ bản]({{ site.imgurl }}/chapter_img/chapter12/07_spectral_theory.svg )

## Mục tiêu

Bài này giới thiệu lý thuyết phổ như cách nhìn toán tử vi phân qua các mode riêng. Sau bài học, sinh viên cần hiểu eigenvalue, eigenfunction, trực giao, và thấy vì sao toán tử tự liên hợp trong không gian Hilbert đóng vai trò tương tự ma trận đối xứng trong hữu hạn chiều. Đây là bài optional nhưng rất quan trọng để nối giải tích hàm với Fourier và PDE.

## Kiến thức nền

Sinh viên nên nắm không gian Hilbert, tích vô hướng, trực giao, bài toán Sturm-Liouville, và cơ sở Fourier. Kiến thức từ các chương về trị riêng của phương trình vi phân thường sẽ giúp bài này trở nên gần gũi hơn.

## Dẫn nhập

Khi một hệ dao động hay khuếch tán được tách thành các mode cơ bản, mỗi mode hành xử đơn giản hơn rất nhiều. Lý thuyết phổ là ngôn ngữ để làm điều đó một cách có hệ thống. Thay vì nhìn toàn bộ toán tử như một hộp đen, ta cố phân rã nó thành các hướng riêng mà trên đó tác động của toán tử chỉ là nhân với một số.

## Khái niệm theo ba cách

### Cách trực giác

Một cây đàn khi rung không rung theo một hình dạng ngẫu nhiên, mà theo các mode riêng. Mỗi mode có tần số riêng. Toán tử trong PDE cũng vậy: nó có những “hình dạng ưa thích” là các eigenfunction, và mỗi hình dạng đi kèm một eigenvalue mô tả mức độ đáp ứng.

### Cách hình ảnh

Rất nên vẽ vài mode của dây đàn cố định hai đầu:

- mode cơ bản có một bụng,
- mode thứ hai có hai bụng,
- mode thứ ba có ba bụng.

Sau đó nhắc rằng các hàm $$ \sin(n\pi x) $$ chính là eigenfunction của Laplacian một chiều với điều kiện Dirichlet.

### Cách hình thức

Cho toán tử tuyến tính $$ A $$ trên Hilbert space $$ H $$. Số $$ \lambda $$ là trị riêng nếu tồn tại $$ u\ne 0 $$ sao cho $$ Au=\lambda u $$. Khi $$ A $$ là tự liên hợp và có compact resolvent, ta thường thu được một họ eigenvalue rời rạc $$ \lambda_1\le \lambda_2\le \cdots \to \infty $$ và các eigenfunction tương ứng tạo thành một hệ trực giao hoàn chỉnh trong $$ H $$.

## Ngộ nhận thường gặp

### “Phổ chỉ là danh sách trị riêng”

Không hẳn. Trong nhiều bài toán vô hạn chiều, phổ có thể phức tạp hơn. Tuy nhiên, trong các ví dụ elliptic quen thuộc, phần phổ rời rạc là trung tâm.

### “Eigenfunction chỉ là công cụ kỹ thuật”

Sai. Chúng là ngôn ngữ tự nhiên để mô tả động lực và cấu trúc của nghiệm PDE.

### “Mọi toán tử đều có cơ sở eigenfunction đẹp”

Không. Cần giả thiết như tự liên hợp và compact resolvent.

### “Trực giao chỉ là tính toán thuận tiện”

Không. Nó là chìa khóa để phân rã nghiệm theo mode độc lập.

## Tiến trình học

### Bước 1: Bắt đầu từ ma trận đối xứng

Nhắc lại rằng ma trận đối xứng có trị riêng thực và vector riêng trực giao.

### Bước 2: Mở rộng sang toán tử

Giải thích rằng toán tử tự liên hợp trong Hilbert space đóng vai trò tương tự.

### Bước 3: Xem ví dụ Laplacian một chiều

Đây là nơi Fourier và phổ gặp nhau.

### Bước 4: Kết nối với PDE phụ thuộc thời gian

Các mode phổ giải thích vì sao heat equation và wave equation xử lý từng thành phần rất khác nhau.

### Các điểm kiểm tra hiểu bài

- Sinh viên có nhận ra mối liên hệ giữa eigenfunction và Fourier mode không?
- Sinh viên có giải thích được vì sao trị riêng khác nhau cho eigenfunction trực giao không?
- Sinh viên có thấy ý nghĩa động lực học của phổ trong heat và wave không?

## Ví dụ có lời giải

### Ví dụ 1: Laplacian một chiều với Dirichlet

Xét $$ -u''=\lambda u,\qquad u(0)=u(1)=0 $$. Nghiệm không tầm thường tồn tại khi

$$
\lambda_n=n^2\pi^2,\qquad u_n(x)=\sin(n\pi x),\qquad n=1,2,\dots
$$

Đây là ví dụ chuẩn của phổ rời rạc.

### Ví dụ 2: Trực giao

Với $$ m\ne n $$,

$$ \int_0^1 \sin(m\pi x)\sin(n\pi x)\,dx=0. $$

Điều này cho phép khai triển các hàm thích hợp thành tổng Fourier sine.

### Ví dụ 3: Ứng dụng vào phương trình nhiệt

Nếu $$ u_t-u_{xx}=0,\qquad u(0,t)=u(1,t)=0 $$, và dữ liệu đầu được khai triển theo $$ \sin(n\pi x) $$, thì từng mode suy giảm như $$ e^{-n^2\pi^2 t} $$. Mode cao tắt nhanh hơn, nên phổ giải thích hiệu ứng làm mượt của nhiệt.

### Ví dụ 4: Ứng dụng vào phương trình sóng

Trong phương trình sóng cùng biên, mỗi mode dao động với tần số $$ \sqrt{\lambda_n}=n\pi $$. So sánh với ví dụ nhiệt, sinh viên sẽ thấy cùng một phổ nhưng động lực học rất khác.

## Câu hỏi khái niệm

1. Vì sao toán tử tự liên hợp là đối tượng tự nhiên để làm phổ?
2. Điều gì làm cho eigenfunction trở thành “ngôn ngữ riêng” của một hệ PDE?
3. Tại sao phổ của Laplacian lại chi phối cả khuếch tán lẫn dao động?

## Bài toán ứng dụng

1. Trong âm học, các tần số cộng hưởng của một dây đàn liên hệ thế nào với eigenvalue?
2. Trong cơ học lượng tử, vì sao các mức năng lượng của hệ thường được đọc như phổ của một toán tử?
3. Trong phân tích dữ liệu và học máy, trực giao và phân rã theo mode có gợi liên hệ gì với PCA hay SVD?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Vì sao một hệ vật lý lại có các mode ưu tiên?
- Nếu hai mode có trị riêng khác nhau, tại sao chúng không “lẫn” vào nhau?
- Cùng một phổ, vì sao heat equation và wave equation cho hành vi thời gian khác nhau?

### Hoạt động gợi ý

- Vẽ vài mode riêng của dây đàn trên lớp.
- Cho nhóm sinh viên khai triển một hàm đơn giản theo basis sine.
- So sánh đáp ứng thời gian của từng mode trong nhiệt và sóng.

### Cách tăng tham gia

- Bắt đầu bằng một nhạc cụ hay dao động thực tế.
- Cho sinh viên đoán mode cơ bản trước khi giải phương trình.
- Khuyến khích sinh viên kể các ví dụ cộng hưởng trong đời sống.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám chặt vào ví dụ một chiều với $$ \sin(n\pi x) $$.
- Dùng ngôn ngữ “mode rung” thay cho mô tả quá trừu tượng.
- Tránh sa sâu vào định nghĩa phổ tổng quát trong lượt học đầu.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu compact resolvent.
- Chứng minh trực giao từ tính tự liên hợp.
- Liên hệ phổ với min-max principle ở mức trực giác.

## Ghi nhớ nhanh

Lý thuyết phổ cho phép ta nhìn toán tử như một hệ các mode riêng độc lập. Eigenvalue đo mức đáp ứng của từng mode, còn eigenfunction cung cấp cơ sở tự nhiên để phân rã và hiểu nghiệm PDE.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động riêng và cộng hưởng
- Bài toán: Dây đàn, màng rung và kết cấu cơ học đều có các mode riêng.
- Mô hình: Tìm $$ Au=\lambda u $$ cho toán tử tự liên hợp như Laplacian.
- Giả thiết và giới hạn: Miền và điều kiện biên quyết định phổ.
- Diễn giải: Phổ cho ta tần số riêng và cơ sở mode dao động.

#### Cơ học lượng tử
- Bài toán: Mức năng lượng của hệ lượng tử được mô tả bởi phổ của Hamiltonian.
- Mô hình: Ví dụ cổ điển là toán tử Schrödinger.
- Giả thiết và giới hạn: Tùy thế năng mà phổ có thể rời rạc hoặc liên tục.
- Diễn giải: Spectral theory biến bài toán động lực thành phân rã theo mode năng lượng.

### 2. Trực giác bổ sung và các kết nối

Spectral theory là phiên bản vô hạn chiều của chéo hóa ma trận. Với toán tử tự liên hợp tốt, ta hy vọng tách bài toán thành các mode trực giao. Bẫy phổ biến là nghĩ phổ chỉ gồm eigenvalue; trong không gian vô hạn chiều còn có phổ liên tục.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for n in [1, 2, 3, 4]:
    plt.plot(x, np.sin(n * np.pi * x), label=f"n={n}")

plt.legend()
plt.title("Cac eigenfunction dau cua -d^2/dx^2 tren [0,1]")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: spectral theory vibrating string eigenfunctions
- search: quantum well eigenstates visualization
- search: Laplacian spectrum rectangular domain

### 5. Bài toán mẫu có bối cảnh thực

Trên $$ 0<x<1 $$ với điều kiện Dirichlet, bài toán
$$ -u''=\lambda u, \qquad u(0)=u(1)=0 $$
có nghiệm không tầm thường khi
$$ \lambda_n=n^2\pi^2, \qquad u_n(x)=\sin(n\pi x). $$
Đây là mẫu chuẩn cho việc "phân rã theo mode" trong cơ học và PDE.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu spectral theory qua ví dụ eigenvalue quen thuộc.

**Bậc sau đại học.** Kết nối với toán tử compact, resolvent, phổ liên tục và functional calculus.
