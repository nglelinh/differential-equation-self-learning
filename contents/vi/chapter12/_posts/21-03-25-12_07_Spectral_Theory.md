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

![Phổ của toán tử elliptic và các mode riêng cơ bản]({{ site.imgurl }}/chapter_img/chapter12/07_spectral_theory.svg)

Tại sao phương pháp tách biến ở các chương trước luôn "may mắn" tìm ra một họ hàm riêng $\{\sin(n\pi x/L)\}$ vừa trực giao, vừa đầy đủ để khai triển **mọi** hàm $L^2$ trên miền hình chữ nhật, hình tròn hay bất kỳ hình dạng méo mó nào? Bí mật nằm ở **Lý thuyết Phổ của Toán tử Compact Tự liên hợp**: nghịch đảo $T = (-\Delta)^{-1}$ là một toán tử compact đối xứng trên $L^2(\Omega)$, nên định lý phổ vô hạn chiều đảm bảo tồn tại một cơ sở trực chuẩn đầy đủ các hàm riêng—y hệt định lý chéo hóa ma trận đối xứng trong Đại số Tuyến tính!

## Kiến thức cần nhớ: Bốn trụ cột của Lý thuyết Phổ cho Toán tử PDE

1. **Từ Toán tử Không bị chặn $(-\Delta)$ sang Toán tử Compact $T = (-\Delta)^{-1}$**:
   Toán tử vi phân $-\Delta$ không bị chặn trên $L^2$, nhưng nhờ Lax–Milgram kết hợp Nhúng Compact Rellich–Kondrachov ($H_0^1(\Omega) \Subset L^2(\Omega)$), toán tử giải $T: f \mapsto u$ là toán tử **tuyến tính, compact và tự liên hợp** trên $L^2(\Omega)$!
2. **Định lý Phổ (Hilbert–Schmidt)**:
   Mọi toán tử compact tự liên hợp đều có cơ sở trực chuẩn các hàm riêng $\{\phi_k\}$ với giá trị riêng thực $\mu_k \to 0$. Đảo ngược lại cho $-\Delta$, ta thu được dãy giá trị riêng dương rời rạc $0 < \lambda_1 < \lambda_2 \le \lambda_3 \le \dots \to +\infty$!
3. **Thương số Rayleigh (Rayleigh Quotient) và Nguyên lý Min–Max**:
   Giá trị riêng cơ bản (tần số trầm nhất của mặt trống $\Omega$) được đặc trưng biến phân bởi $\lambda_1 = \min_{u \in H_0^1 \setminus \{0\}} \frac{\int_\Omega |\nabla u|^2\,dx}{\int_\Omega u^2\,dx}$—mở đường ước lượng tần số mà không cần giải PDE chính xác!
4. **Phổ Rời rạc (Miền Bị chặn) vs. Phổ Liên tục (Toàn Không gian $\mathbb{R}^n$)**:
   Trên miền bị chặn, tính compact làm phổ rời rạc (nốt nhạc rời rạc của dây đàn, mức năng lượng nguyên tử bị giam); trên toàn $\mathbb{R}^n$, tính compact biến mất nên phổ của $-\Delta$ trở thành nửa trục liên tục $[0, \infty)$!

## Mục tiêu

Bài học tùy chọn này giới thiệu lý thuyết phổ như phương pháp phân tích toán tử vi phân thông qua các mode riêng. Sau bài học, sinh viên cần nắm khái niệm trị riêng, hàm riêng, tính trực giao, và hiểu vì sao toán tử tự liên hợp trên không gian Hilbert giữ vai trò tương tự ma trận đối xứng trong không gian hữu hạn chiều. Nội dung này tạo cầu nối trực tiếp giữa giải tích hàm, chuỗi Fourier và PDE.

## Kiến thức nền

Sinh viên cần nắm không gian Hilbert, tích vô hướng, tính trực giao, bài toán Sturm–Liouville và cơ sở Fourier. Kiến thức về bài toán trị riêng của phương trình vi phân thường giúp tiếp cận bài học này thuận lợi hơn.

## Dẫn nhập

Khi một hệ dao động hoặc khuếch tán được phân tách thành các mode cơ bản, mỗi mode tiến hóa theo quy luật đơn giản hơn rất nhiều. Lý thuyết phổ hệ thống hóa ý tưởng này: thay vì xem toán tử như một khối phức tạp, ta phân rã nó theo các phương riêng mà trên đó tác động của toán tử chỉ quy về phép nhân với một hằng số.


### Giải thích: Đối chiếu trực tiếp phổ của $-\Delta$ và nghịch đảo compact $T = (-\Delta)^{-1}$ trên $(0, \pi)$

Xét bài toán giá trị riêng $-u'' = \lambda u$ trên $\Omega = (0, \pi)$ với $u(0) = u(\pi) = 0$:
1. **Dãy giá trị riêng và hàm riêng chuẩn hóa**:
   $$\lambda_n = n^2 \quad (1, 4, 9, 16, \dots \to +\infty), \qquad \phi_n(x) = \sqrt{\frac{2}{\pi}}\sin(nx).$$
2. **Phổ của toán tử nghịch đảo compact $T = (-\Delta)^{-1}$**:
   Vì $T\phi_n = \frac{1}{\lambda_n}\phi_n$, các giá trị riêng của $T$ là $\mu_n = \frac{1}{n^2} \in \{1, \tfrac{1}{4}, \tfrac{1}{9}, \tfrac{1}{16}, \dots\} \to \mathbf{0}$ (hội tụ về $0$ đúng như định lý phổ cho toán tử compact!).
3. **Kiểm tra trực chuẩn và thương số Rayleigh cho mode $n = 1$**:
   - $\|\phi_1\|_{L^2}^2 = \frac{2}{\pi}\int_0^\pi \sin^2(x)\,dx = \mathbf{1}$, và $\langle \phi_1, \phi_2 \rangle = \frac{2}{\pi}\int_0^\pi \sin(x)\sin(2x)\,dx = \mathbf{0}$.
   - Thương số Rayleigh: $R(\phi_1) = \frac{\int_0^\pi (\cos x)^2\,dx}{\int_0^\pi (\sin x)^2\,dx} = \frac{\pi/2}{\pi/2} = \mathbf{1} = \lambda_1$!
## Khái niệm theo ba cách

### Cách trực giác

Một dây đàn khi rung không dao động theo hình dạng tùy tiện mà là tổ hợp của các mode riêng, mỗi mode ứng với một tần số xác định. Toán tử trong PDE cũng có các "hình dạng đặc trưng" là các hàm riêng, và mỗi hàm riêng đi kèm một trị riêng biểu thị mức độ đáp ứng của toán tử.

### Cách hình ảnh

Có thể minh họa bằng các mode dao động của dây đàn cố định hai đầu:

- mode cơ bản có một bụng sóng,
- mode thứ hai có hai bụng sóng,
- mode thứ ba có ba bụng sóng.

Các hàm $$ \sin(n\pi x) $$ chính là các hàm riêng của toán tử Laplace một chiều với điều kiện biên Dirichlet thuần nhất.

### Cách hình thức

Cho toán tử tuyến tính $$ A $$ trên không gian Hilbert $$ H $$. Số $$ \lambda $$ là trị riêng nếu tồn tại $$ u\ne 0 $$ sao cho $$ Au=\lambda u $$. Khi $$ A $$ là toán tử tự liên hợp có toán tử giải (resolvent) compact, phổ của $$ A $$ gồm một dãy trị riêng rời rạc $$ \lambda_1\le \lambda_2\le \cdots \to \infty $$ và các hàm riêng tương ứng tạo thành một cơ sở trực giao đầy đủ trong $$ H $$.

## Ngộ nhận thường gặp

### “Phổ chỉ là tập hợp các trị riêng”

Không đầy đủ. Trong không gian vô hạn chiều, phổ còn có thể chứa phần phổ liên tục; tuy nhiên, đối với các bài toán elliptic trên miền bị chặn, phổ rời rạc giữ vai trò trung tâm.

### “Hàm riêng chỉ là công cụ tính toán phụ trợ”

Sai. Hàm riêng là cơ sở tự nhiên để phân tích cấu trúc và động lực của nghiệm PDE.

### “Mọi toán tử đều có cơ sở hàm riêng trực giao”

Không đúng. Kết quả này đòi hỏi các giả thiết như tính tự liên hợp và tính compact của toán tử giải.

### “Tính trực giao chỉ giúp tính tích phân nhanh hơn”

Không chỉ vậy; tính trực giao là điều kiện nền tảng cho phép tách bài toán thành các mode độc lập nhau.

## Tiến trình học

### Bước 1: Xuất phát từ ma trận đối xứng

Nhắc lại rằng ma trận đối xứng thực có các trị riêng thực và cơ sở vector riêng trực giao.

### Bước 2: Mở rộng sang toán tử trên không gian Hilbert

Chỉ ra rằng toán tử tự liên hợp đóng vai trò tương tự ma trận đối xứng trong không gian vô hạn chiều.

### Bước 3: Khảo sát toán tử Laplace một chiều

Nhận diện điểm giao nhau giữa lý thuyết phổ và khai triển chuỗi Fourier.

### Bước 4: Liên hệ với PDE phụ thuộc thời gian

Thấy cách cùng một phổ toán tử chi phối diễn biến rất khác nhau ở phương trình nhiệt và phương trình sóng.

### Các điểm kiểm tra hiểu bài

- Sinh viên có nhận ra mối liên hệ giữa hàm riêng và các mode Fourier hay không?
- Sinh viên có giải thích được vì sao các hàm riêng ứng với các trị riêng phân biệt thì trực giao hay không?
- Sinh viên có thấy ý nghĩa động lực học của phổ trong phương trình nhiệt và phương trình sóng hay không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử Laplace một chiều với điều kiện Dirichlet

Xét bài toán $$ -u''=\lambda u,\qquad u(0)=u(1)=0 $$. Nghiệm không tầm thường tồn tại khi và chỉ khi:

$$
\lambda_n=n^2\pi^2,\qquad u_n(x)=\sin(n\pi x),\qquad n=1,2,\dots
$$

Đây là ví dụ tiêu chuẩn của phổ rời rạc.

### Ví dụ 2: Tính trực giao

Với $$ m\ne n $$,

$$ \int_0^1 \sin(m\pi x)\sin(n\pi x)\,dx=0. $$

Tính chất này cho phép khai triển các hàm trong $$ L^2(0,1) $$ theo chuỗi Fourier sin.

### Ví dụ 3: Ứng dụng vào phương trình nhiệt

Với phương trình $$ u_t-u_{xx}=0,\qquad u(0,t)=u(1,t)=0 $$, khi khai triển dữ liệu ban đầu theo $$ \sin(n\pi x) $$, mỗi mode suy giảm theo hệ số $$ e^{-n^2\pi^2 t} $$. Các mode bậc cao tắt nhanh hơn nhiều, giải thích hiệu ứng làm trơn của quá trình truyền nhiệt.

### Ví dụ 4: Ứng dụng vào phương trình sóng

Với phương trình sóng cùng điều kiện biên, mỗi mode dao động với tần số góc $$ \sqrt{\lambda_n}=n\pi $$. So sánh với phương trình nhiệt cho thấy cùng một hệ phổ không gian nhưng cho ra hai dạng động lực thời gian hoàn toàn khác nhau.

## Câu hỏi khái niệm

1. Vì sao toán tử tự liên hợp là lớp toán tử tự nhiên cho lý thuyết phổ?
2. Điều gì khiến họ hàm riêng trở thành cơ sở đặc trưng của một bài toán PDE?
3. Vì sao phổ của toán tử Laplace đồng thời chi phối cả quá trình khuếch tán lẫn quá trình dao động?

## Bài toán ứng dụng

1. Trong âm học, các tần số cộng hưởng của dây đàn liên hệ như thế nào với các trị riêng?
2. Trong cơ học lượng tử, vì sao các mức năng lượng của hệ được xác định từ phổ của một toán tử?
3. Trong phân tích dữ liệu, sự phân rã theo các phương trực giao có điểm tương đồng nào với PCA hay SVD?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Vì sao một hệ vật lý lại có các mode dao động đặc trưng?
- Vì sao hai mode ứng với hai trị riêng khác nhau lại độc lập (trực giao) với nhau?
- Cùng một phổ toán tử không gian, vì sao phương trình nhiệt và phương trình sóng lại có hành vi theo thời gian khác nhau?

### Hoạt động gợi ý

- Vẽ các mode riêng đầu tiên của dây đàn cố định hai đầu.
- Cho nhóm sinh viên khai triển một hàm đơn giản theo cơ sở hàm sin.
- So sánh hệ số tiến hóa theo thời gian của từng mode trong phương trình nhiệt và phương trình sóng.

### Cách tăng tham gia

- Mở đầu bằng hình ảnh nhạc cụ hoặc dao động cơ học quen thuộc.
- Mời sinh viên dự đoán hình dạng mode cơ bản trước khi giải phương trình trị riêng.
- Khuyến khích sinh viên nêu các hiện tượng cộng hưởng gặp trong thực tế.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám sát ví dụ một chiều với họ hàm $$ \sin(n\pi x) $$.
- Dùng trực giác "mode dao động" trước khi chuyển sang phát biểu toán tử trừu tượng.
- Tránh đi quá sâu vào định nghĩa phổ tổng quát ở lần tiếp cận đầu tiên.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu khái niệm toán tử giải (resolvent) compact.
- Chứng minh tính trực giao của các hàm riêng từ tính tự liên hợp.
- Liên hệ các trị riêng với nguyên lý cực tiểu–cực đại (min–max principle).

## Ghi nhớ nhanh

Lý thuyết phổ phân tích toán tử thành hệ các mode riêng trực giao. Trị riêng đo mức đáp ứng của từng mode, còn hàm riêng tạo thành cơ sở tự nhiên để khai triển và nghiên cứu nghiệm PDE.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động riêng và cộng hưởng
- Bài toán: Dây đàn, màng rung và kết cấu cơ học đều có các mode dao động đặc trưng.
- Mô hình: Giải bài toán trị riêng $$ Au=\lambda u $$ cho toán tử tự liên hợp như toán tử Laplace.
- Giả thiết và giới hạn: Hình học miền và điều kiện biên quyết định trực tiếp phổ của toán tử.
- Diễn giải: Phổ cung cấp các tần số riêng và cơ sở mode dao động.

#### Cơ học lượng tử
- Bài toán: Các mức năng lượng của hệ lượng tử tương ứng với phổ của toán tử Hamilton.
- Mô hình: Ví dụ kinh điển là toán tử Schrödinger.
- Giả thiết và giới hạn: Tùy dạng thế năng mà phổ có thể rời rạc, liên tục hoặc hỗn hợp.
- Diễn giải: Lý thuyết phổ chuyển bài toán động lực lượng tử thành phân rã theo các trạng thái năng lượng riêng.

### 2. Trực giác bổ sung và các kết nối

Lý thuyết phổ là sự mở rộng vô hạn chiều của phép chéo hóa ma trận. Với toán tử tự liên hợp thích hợp, ta có thể tách bài toán thành các mode trực giao độc lập. Một nhầm lẫn thường gặp là đồng nhất phổ với tập trị riêng; trong không gian vô hạn chiều, phổ còn có thể bao gồm phổ liên tục.

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

Trên đoạn $$ 0<x<1 $$ với điều kiện Dirichlet thuần nhất, bài toán trị riêng
$$ -u''=\lambda u, \qquad u(0)=u(1)=0 $$
có nghiệm không tầm thường khi và chỉ khi
$$ \lambda_n=n^2\pi^2, \qquad u_n(x)=\sin(n\pi x). $$
Đây là mô hình chuẩn cho phương pháp phân rã theo mode trong cơ học và PDE.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm lý thuyết phổ thông qua các bài toán trị riêng một chiều quen thuộc.

**Bậc sau đại học.** Kết nối với toán tử compact, toán tử giải (resolvent), phổ liên tục và phép tính hàm cho toán tử (functional calculus).

## Video tham khảo

- xem trước: [Lecture 22: The Spectral Theorem for a Compact Self-Adjoint Operator](https://www.youtube.com/watch?v=-sfaHVFWBU8) — MIT OpenCourseWare, tiếng Anh. Bài giảng về định lý phổ cho toán tử compact tự liên hợp.
- [Lecture 20: Compact Operators and the Spectrum of a Bounded Linear Operator on a Hilbert Space](https://www.youtube.com/watch?v=SFDMFbzCsH0) — MIT OpenCourseWare, tiếng Anh. Trình bày toán tử compact và phổ của toán tử tuyến tính bị chặn trên không gian Hilbert.
- [Spectral Theorem For Dummies - 3Blue1Brown Summer of Math Exposition #SoME1](https://www.youtube.com/watch?v=4zD8Kd3HgJA) — Jacqueline Doan, tiếng Anh. Diễn giải trực quan định lý phổ dưới góc nhìn hình học.
