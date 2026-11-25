---
layout: post
title: "Các Hệ Số Fourier"
chapter: '08'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---

![21 02 25 08 02 Fourier Coefficients]({{ site.imgurl }}/chapter_img/chapter08/02_fourier_coefficients.svg)

Biết một tín hiệu phân tích được thành tổng các sóng sin/cosin là một chuyện; làm sao đo chính xác biên độ $a_n, b_n$ của từng tần số lại là chuyện khác. Nhờ tính trực giao của hệ lượng giác, ta có bộ **Công thức Euler–Fourier** cực kỳ trong sáng: muốn đo lượng tần số thứ $n$ chứa trong $f(x)$, chỉ cần nhân $f(x)$ với đúng sóng $\cos(n\pi x/L)$ hoặc $\sin(n\pi x/L)$ rồi lấy tích phân trung bình trên một chu kỳ!

## Kiến thức cần nhớ: Bốn kỹ năng tính Hệ số Fourier không sai dấu

1. **Bộ công thức Euler–Fourier trên $[-L, L]$**:
   $$a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx, \quad a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos\!\left(\frac{n\pi x}{L}\right)dx, \quad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx.$$
2. **Mẹo dấu vàng cần thuộc nằm lòng**:
   $\sin(n\pi) = 0$ với mọi $n \in \mathbb{Z}$, còn $\cos(n\pi) = (-1)^n$ (bằng $-1$ khi $n$ lẻ và $+1$ khi $n$ chẵn).
3. **Tích phân từng phần theo bảng (Tabular Integration)**:
   Khi $f(x)$ là đa thức ($x, x^2$) nhân $\sin(nx)$ hoặc $\cos(nx)$, dùng bảng dấu đan xen $(+, -, +)$ giúp tránh 90% lỗi dấu cơ học.
4. **Tính chất tối ưu bình phương tối thiểu (Best $L^2$ Approximation)**:
   Tổng riêng $S_N(x)$ dùng các hệ số Euler–Fourier chính là hàm lượng giác bậc $N$ có sai số bình phương trung bình $\int_{-L}^{L} [f(x) - T_N(x)]^2\,dx$ **nhỏ nhất có thể**!

## Mục tiêu

Bài học này tập trung vào cách tính và diễn giải các hệ số Fourier. Sau bài học, sinh viên cần hiểu vì sao công thức hệ số xuất phát từ tính trực giao, biết cách tính $$ a_n,\quad b_n $$ qua các ví dụ điển hình, nhìn nhận các hệ số như tọa độ của hàm trong cơ sở lượng giác và thấy được chúng đo lường mức đóng góp của từng tần số vào tín hiệu.

## Kiến thức nền

Sinh viên cần nắm vững khái niệm chuỗi Fourier cơ bản, tích phân xác định và tính trực giao của các hàm sin, cos trên một chu kỳ. Bài học này chuyển trực giác về phép chiếu thành kỹ thuật tính toán cụ thể.

## Dẫn nhập

Việc viết chuỗi Fourier sẽ không mang lại nhiều giá trị thực hành nếu ta không có cách xác định các hệ số. Điểm thuận lợi là ta không cần phải đoán: tương tự như trong đại số tuyến tính, khi có một cơ sở trực giao, các tọa độ của một vectơ được tách ra gọn gàng nhờ tích vô hướng. Các hệ số Fourier xuất hiện theo đúng nguyên lý đó.

Khi nắm chắc cơ chế này, sinh viên sẽ không phải học thuộc lòng các công thức tích phân một cách máy móc, mà hiểu chúng là hệ quả trực tiếp của tính trực giao. Nhờ vậy, các bài toán Fourier tiếp theo sẽ trở nên dễ tiếp cận hơn nhiều.

### Giải thích: Tính tay đầy đủ các hệ số Fourier của sóng răng cưa $f(x) = x$ trên $(-\pi, \pi)$

1. **Nhận xét tính chẵn/lẻ trước khi tích phân**: $f(x) = x$ là hàm **lẻ** trên đoạn đối xứng $(-\pi, \pi)$ ⇒ lập tức có **$a_0 = 0$** và **$a_n = 0$ với mọi $n \ge 1$**!
2. **Tính $b_n$ bằng tích phân từng phần** ($u = x \implies du = dx$; $dv = \sin(nx)\,dx \implies v = -\frac{\cos(nx)}{n}$):
   $$b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin(nx)\,dx = \frac{2}{\pi}\int_{0}^{\pi} x\sin(nx)\,dx = \frac{2}{\pi}\left[\left.-\frac{x\cos(nx)}{n}\right|_0^{\pi} + \frac{1}{n}\int_0^{\pi}\cos(nx)\,dx\right].$$
   Tích phân thứ hai bằng $\left.\frac{\sin(nx)}{n^2}\right|_0^\pi = 0$. Phần biên cho $-\frac{\pi\cos(n\pi)}{n} = -\frac{\pi(-1)^n}{n} = \frac{\pi(-1)^{n+1}}{n}$.
3. **Kết quả cuối cùng**:
   $$b_n = \frac{2(-1)^{n+1}}{n} \implies x \sim 2\left(\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \frac{\sin 4x}{4} + \dots\right).$$
   Kiểm tra tốc độ giảm hệ số: $\vert b_n \vert = \frac{2}{n}$ giảm chậm như $O(1/n)$ vì sóng răng cưa có bước nhảy đứt đoạn tại $x = \pm\pi$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Mỗi hệ số Fourier đóng vai trò như một nút điều chỉnh âm lượng cho một tần số riêng biệt. Hệ số lớn cho biết mode đó xuất hiện mạnh trong tín hiệu, còn hệ số nhỏ cho biết mode đó đóng góp ít. Toàn bộ phổ Fourier đóng vai trò như một bản đồ chỉ ra tín hiệu được cấu thành từ những tần số nào và với cường độ ra sao.

### Cách nhìn hình ảnh

Khi quan sát đồ thị tổng riêng Fourier, việc thay đổi một hệ số cụ thể sẽ làm tăng hoặc giảm biên độ của gợn sóng ứng với tần số đó. Do đó, các hệ số Fourier có thể được xem như "tọa độ phổ" của hàm, còn đồ thị gốc là sự chồng chất của các gợn dao động này.

### Cách nhìn hình thức

Với hàm tuần hoàn chu kỳ $$ 2\pi $$, ta viết

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$

Các hệ số được xác định bởi

$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,
\qquad n\ge 0,
$$

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx,
\qquad n\ge 1.
$$

Các công thức này xuất hiện vì họ hàm lượng giác là trực giao trên đoạn $$ [-\pi,\pi] $$.

## Những ngộ nhận thường gặp

- "Cần học thuộc công thức hệ số như những công thức độc lập." Không đúng; chúng được suy ra trực tiếp từ tính trực giao.
- "Hệ số Fourier lúc nào cũng khó tính." Không hẳn; tính đối xứng chẵn lẻ thường giúp triệt tiêu một nửa khối lượng tính toán.
- "Hệ số lớn nhất luôn là mode quan trọng nhất về mọi phương diện." Cần thận trọng; điều này còn tùy thuộc vào chuẩn đo và hiện tượng vật lý đang xét.
- "Nếu vài hệ số đầu nhỏ thì phần còn lại không đáng kể." Sai; năng lượng phổ có thể tập trung vào nhiều mode tần số cao.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại tính trực giao

Nếu sinh viên chưa vững về tính trực giao của các hàm sin và cos, cần củng cố lại trước khi đi tiếp.

### Bước 2: Suy ra công thức hệ số

Thay vì đưa công thức để học thuộc ngay, hãy dẫn dắt từ ý tưởng phép chiếu trực giao.

### Bước 3: Tính hệ số trên các ví dụ cơ bản

Hàm hằng, hàm lượng giác đơn, hàm lẻ và hàm chẵn là những ví dụ khởi đầu hiệu quả.

### Bước 4: Diễn giải hệ số theo góc nhìn phổ

Đây là bước chuyển từ tính toán thuần túy sang ý nghĩa vật lý và phân tích tín hiệu.

### Các điểm kiểm tra

- Sinh viên có tự giải thích được vì sao nhân hàm với một mode rồi lấy tích phân lại tách ra đúng hệ số tương ứng hay không.
- Sinh viên có tính đúng $$ a_n,\ b_n $$ trong các ví dụ cơ bản hay không.
- Sinh viên có hiểu hệ số Fourier như tọa độ trong một cơ sở trực giao hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm hằng

Với $$ f(x)=1 $$, ta có

$$ a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}1\,dx=2. $$

Với mọi $$ n\ge 1 $$,

$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}\cos(nx)\,dx=0,
\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}\sin(nx)\,dx=0.
$$

Như vậy, chuỗi Fourier chỉ còn lại chính hằng số ban đầu. Ví dụ này cho thấy $$ a_0 $$ gắn với thành phần trung bình của hàm.

### Ví dụ 2: Một mode lượng giác đơn

Với $$ f(x)=\cos(kx) $$, ta thu được $$ a_k=1 $$ và mọi hệ số khác đều bằng 0. Đây là phép kiểm tra trực giác hữu ích: một phần tử thuộc cơ sở trực giao phải có đúng một tọa độ khác 0.

### Ví dụ 3: Hàm răng cưa

Xét hàm số

$$ f(x)=x,
\qquad -\pi<x<\pi. $$

Vì $$ f $$ là hàm lẻ nên $$ a_n=0 $$ với mọi $$ n $$. Ta chỉ cần tính

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
=\frac{2}{\pi}\int_0^{\pi}x\sin(nx)\,dx.
$$

Áp dụng tích phân từng phần, ta được

$$ b_n=\frac{2(-1)^{n+1}}{n}. $$

Suy ra

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này cho thấy tính đối xứng lẻ giúp rút gọn đáng kể khối lượng tính toán.

### Ví dụ 4: Sóng vuông

Xét hàm số

$$
f(x)=
\begin{cases}
1, & 0<x<\pi,\\
-1, & -\pi<x<0.
\end{cases}
$$

Do hàm lẻ nên $$ a_n=0 $$. Ta tính được

$$
b_n=
\begin{cases}
\dfrac{4}{n\pi}, & n \text{ lẻ},\\
0, & n \text{ chẵn}.
\end{cases}
$$

Đây là ví dụ điển hình cho trường hợp phổ chỉ chứa các họa âm bậc lẻ.

## Câu hỏi khái niệm

1. Vì sao công thức hệ số Fourier bản chất là một phép chiếu chứ không phải mẹo tính toán?
2. Các hệ số Fourier cho biết điều gì về thành phần tần số có trong tín hiệu?
3. Vì sao tính đối xứng của hàm thường làm một số hệ số tự động bằng 0?

## Bài toán ứng dụng

1. Trong âm học, nếu một tín hiệu có biên độ lớn ở họa âm bậc ba và bậc năm, điều đó phản ánh gì về phổ Fourier của nó?
2. Trong truyền tín hiệu số, vì sao việc biết phổ Fourier giúp xác định dải tần mà nhiễu đang tập trung?
3. Trong dao động cơ học, nếu kích thích ban đầu có dạng gần đối xứng lẻ, vì sao ta kỳ vọng các mode sin chiếm ưu thế?

## Chiến lược giảng dạy tương tác

- Hướng dẫn sinh viên tự suy ra công thức hệ số từ tính trực giao thay vì cung cấp sẵn ngay từ đầu.
- Sử dụng các ví dụ ngắn như hàm hằng và một mode cos đơn để sinh viên tự kiểm chứng trực giác.
- Đặt câu hỏi cho cả lớp: "Hệ số nào đo thành phần trung bình của tín hiệu?"
- So sánh hai hàm có đồ thị khác nhau nhưng cùng một vài hệ số đầu để thảo luận về ý nghĩa của phổ tần số.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên luyện tập kỹ bốn mẫu cơ bản: hàm hằng, hàm cos đơn, hàm lẻ và hàm chẵn. Khi đã thành thạo bốn mẫu này, việc tính hệ số cho các hàm phức tạp hơn sẽ ít gây trở ngại hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên diễn giải các hệ số Fourier bằng ngôn ngữ tích vô hướng trong $$ L^2 $$, hoặc đối chiếu trực tiếp công thức hệ số Fourier với công thức tìm tọa độ trong đại số tuyến tính hữu hạn chiều.

## Tóm tắt dễ nhớ

Các hệ số Fourier là tọa độ của hàm số trong cơ sở lượng giác trực giao, được xác định thông qua phép chiếu tích phân. Biết các hệ số này đồng nghĩa với việc biết mức đóng góp của từng mode tần số trong tín hiệu.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân tích âm thanh
- Bài toán: Xác định năng lượng tín hiệu âm thanh phân bố ở từng họa âm.
- Mô hình:
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
$$
- Giả thiết và giới hạn: Dữ liệu được xem là một chu kỳ điển hình hoặc được mở rộng tuần hoàn.
- Diễn giải: Các hệ số Fourier đo mức độ tương quan giữa tín hiệu và từng mode chuẩn.

#### Dao động cưỡng bức có nhiều họa âm
- Bài toán: Phân tách một lực cưỡng bức tuần hoàn có dạng phức tạp thành các thành phần sin và cos.
- Mô hình: Sử dụng các hệ số Fourier để biểu diễn lực cưỡng bức dưới dạng tổng các mode.
- Giả thiết và giới hạn: Mô hình mang tính lý tưởng hóa; tín hiệu thực tế thường cần cắt cụt chuỗi hoặc lọc nhiễu.
- Diễn giải: Mode nào có hệ số lớn hơn thì tần số tương ứng đóng góp mạnh hơn vào kích thích.

### 2. Trực giác bổ sung và các kết nối

Các hệ số Fourier chính là tọa độ của hàm trong cơ sở trực giao sin-cos. Thay vì xem công thức hệ số là nội dung cần học thuộc, nên hiểu chúng xuất phát trực tiếp từ phép chiếu trực giao. Nội dung này liên kết chặt chẽ với khái niệm tính trực giao và hệ số khai triển trong lý thuyết Sturm-Liouville.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 2000)
f = x

bn = []
N = 12
for n in range(1, N + 1):
    coeff = (1 / np.pi) * np.trapz(f * np.sin(n * x), x)
    bn.append(coeff)

plt.stem(range(1, N + 1), bn)
plt.xlabel("n")
plt.ylabel("b_n")
plt.title("Pho Fourier cua f(x)=x tren (-pi,pi)")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Fourier coefficients spectrum visualization
- search: odd function sine coefficients example
- search: harmonic amplitudes bar chart signal processing

### 5. Bài toán mẫu có bối cảnh thực

Với hàm số
$$ f(x)=x,\qquad -\pi<x<\pi, $$
do $$ f $$ là hàm lẻ nên $$ a_n=0 $$. Khi đó
$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
=\frac{2(-1)^{n+1}}{n}.
$$
Vì vậy
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Tính thành thạo $$ a_n,b_n $$ cho các hàm chẵn, hàm lẻ và hàm xác định từng khúc đơn giản.

**Bậc sau đại học.** Diễn giải hệ số Fourier như phép chiếu trong không gian Hilbert và liên hệ với phổ năng lượng của tín hiệu.

## Video tham khảo

- Xem trước: [Computing Fourier Series | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=jzzpxqVohhI) — MIT OpenCourseWare, tiếng Anh. Hướng dẫn cách tính các hệ số Fourier từ công thức tích phân.
- [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Giải thích vì sao các tích phân hệ số chính là phép lấy tích vô hướng với sin và cos.
- [Manipulating Fourier Series | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=v4YcejwdQC0) — MIT OpenCourseWare, tiếng Anh. Trình bày cách biến đổi chuỗi Fourier khi đã biết các hệ số.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
