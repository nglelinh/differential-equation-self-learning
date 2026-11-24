---
layout: post
title: "Hàm Tuần Hoàn và Chuỗi Fourier"
chapter: '08'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---

![21 02 25 08 01 Periodic Functions Fourier Series]({{ site.imgurl }}/chapter_img/chapter08/01_periodic_functions_fourier_series.svg)

Mọi tín hiệu lặp lại theo chu kỳ—từ sóng điện xoay chiều 50 Hz, nhịp tim điện tâm đồ ECG đến âm thanh một phím đàn—đều là **hàm tuần hoàn** thỏa $f(x + T) = f(x)$. Ý tưởng trung tâm của **Chuỗi Fourier** giống hệt lăng kính tách ánh sáng trắng thành cầu vồng: phân rã một sóng tuần hoàn phức tạp bất kỳ thành tổng các sóng sin và cosin tinh khiết ở các tần số bội nguyên $\frac{n\pi}{L}$!

## Bản đồ kiến thức nền: Bốn viên gạch đầu tiên của Chuỗi Fourier

1. **Chu kỳ cơ bản $T = 2L$ & Tần số góc cơ bản $\omega_0 = \frac{2\pi}{T} = \frac{\pi}{L}$**:
   Nếu $f(x + T) = f(x)$ với mọi $x$, tích phân trên bất kỳ đoạn độ dài $T$ nào (như $[-L, L]$ hay $[0, 2L]$) đều có giá trị y hệt nhau.
2. **Dạng chuẩn chuỗi Fourier trên $[-L, L]$**:
   $$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n\cos\!\left(\frac{n\pi x}{L}\right) + b_n\sin\!\left(\frac{n\pi x}{L}\right)\right].$$
   Số hạng $\frac{a_0}{2}$ chính là **giá trị trung bình (thành phần DC)** của tín hiệu trên một chu kỳ!
3. **Tính trực giao của hệ lượng giác $\{1, \cos(n\pi x/L), \sin(n\pi x/L)\}$**:
   Tích phân trên $[-L, L]$ của tích hai hàm bất kỳ *khác nhau* trong hệ đều bằng **$0$**, còn tích phân bình phương mỗi hàm $\cos^2$ hoặc $\sin^2$ đều bằng đúng **$L$**!
4. **Dấu $\sim$ thay vì dấu $=$**:
   Ta viết $f(x) \sim \dots$ trước khi kiểm chứng điều kiện hội tụ vì tại các điểm gián đoạn, chuỗi Fourier có thể hội tụ về giá trị khác $f(x)$.

## Mục tiêu

Bài học này mở đầu chương về chuỗi Fourier bằng cách giải thích vì sao một hàm tuần hoàn có thể được biểu diễn thành tổng của các dao động điều hòa cơ bản. Sau bài học, sinh viên cần nắm vững khái niệm hàm tuần hoàn, nhận ra vai trò của các mode $$ \sin(nx),\quad \cos(nx) $$, hiểu chuỗi Fourier như một phép chiếu lên hệ trực giao và thấy được vì sao đây là công cụ nền tảng cho phương trình nhiệt, phương trình sóng cũng như phân tích tín hiệu.

## Kiến thức nền

Sinh viên cần nắm vững tích phân xác định, các tính chất cơ bản của hàm lượng giác và ý tưởng cơ sở trực giao từ đại số tuyến tính hoặc từ bài Sturm-Liouville trước đó. Khi đã quen với khái niệm mode riêng, việc tiếp cận chuỗi Fourier sẽ trở nên tự nhiên hơn.

## Dẫn nhập

Một tín hiệu âm thanh, một dao động cơ học hay một nhiệt độ biên biến thiên tuần hoàn theo thời gian thường có dạng phức tạp nếu chỉ quan sát trực tiếp trong miền không gian hoặc thời gian. Tuy nhiên, nhiều tín hiệu như vậy có thể được phân tách thành tổng của những dao động điều hòa đơn giản hơn. Chuỗi Fourier là công cụ giúp thực hiện phép phân tách này một cách có hệ thống.

Đây là một trong những ý tưởng trọng tâm của toàn bộ học phần. Chuỗi Fourier không chỉ giải thích cách phân tích tín hiệu theo tần số mà còn chuẩn bị trực tiếp cho phương pháp tách biến khi giải phương trình đạo hàm riêng (PDE). Nói ngắn gọn, khai triển Fourier chuyển một hàm có hình dạng phức tạp thành tổ hợp của các mode cơ bản dễ phân tích hơn.

### Khung giải thích (nên đọc chậm): Kiểm chứng trực tiếp bằng tay tính trực giao $\int_{-\pi}^{\pi} \cos(2x)\cos(3x)\,dx = 0$

Dùng công thức tích thành tổng $\cos A \cos B = \frac{1}{2}[\cos(A - B) + \cos(A + B)]$:
$$\int_{-\pi}^{\pi} \cos(2x)\cos(3x)\,dx = \frac{1}{2}\int_{-\pi}^{\pi} [\cos(-x) + \cos(5x)]\,dx = \frac{1}{2}\left[\sin x + \frac{\sin 5x}{5}\right]_{-\pi}^{\pi} = \frac{1}{2}(0 - 0) = \mathbf{0}!$$
Còn khi $m = n = 2$:
$$\int_{-\pi}^{\pi} \cos^2(2x)\,dx = \frac{1}{2}\int_{-\pi}^{\pi} [1 + \cos(4x)]\,dx = \frac{1}{2}\left[x + \frac{\sin 4x}{4}\right]_{-\pi}^{\pi} = \frac{1}{2}(2\pi) = \mathbf{\pi} = L!$$
Chính sự triệt tiêu tuyệt đối khi $m \neq n$ giúp ta "lọc" riêng từng hệ số $a_n, b_n$ độc lập nhau mà không cần giải hệ phương trình!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy nghĩ đến một hợp âm trên đàn piano. Tai người nghe một âm thanh tổng hợp, nhưng thực chất đó là sự chồng chất của nhiều tần số riêng biệt. Chuỗi Fourier thực hiện điều tương tự với hàm số: tách một tín hiệu tuần hoàn phức tạp thành những thành phần cơ bản là các hàm sin và cos.

### Cách nhìn hình ảnh

Khi vẽ một hàm tuần hoàn phức tạp rồi lần lượt cộng thêm các mode $$\cos x,\quad \sin x,\quad \cos 2x,\quad \sin 2x,\ldots$$, đồ thị của tổng riêng sẽ dần tái hiện hình dạng ban đầu từ thô đến tinh. Các mode tần số thấp định hình dáng tổng thể, còn các mode tần số cao tinh chỉnh các chi tiết nhỏ hơn. Cách nhìn này cho thấy Fourier vừa mang ý nghĩa hình học vừa mang ý nghĩa phổ tần số.

### Cách nhìn hình thức

Một hàm $$ f $$ được gọi là tuần hoàn với chu kỳ $$ T>0 $$ nếu

$$ f(x+T)=f(x)
\qquad \text{với mọi } x. $$

Với hàm tuần hoàn chu kỳ $$ 2\pi $$, chuỗi Fourier có dạng

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$

Ký hiệu $$ \sim $$ nhấn mạnh rằng đây là sự biểu diễn theo một nghĩa hội tụ thích hợp, chứ không nhất thiết là đẳng thức từng điểm tại mọi vị trí.

## Những ngộ nhận thường gặp

- "Chuỗi Fourier chỉ dành cho hàm lượng giác." Sai; chuỗi Fourier biểu diễn được nhiều lớp hàm tuần hoàn rất khác nhau.
- "Nếu hàm không trơn thì chuỗi Fourier vô dụng." Không đúng; ngay cả những hàm có bước nhảy vẫn có chuỗi Fourier hữu ích.
- "Các hàm sin và cos được chọn một cách tùy ý." Sai; chúng tạo thành hệ mode trực giao tự nhiên trên đoạn tuần hoàn.
- "Chuỗi Fourier luôn hội tụ đúng bằng giá trị của hàm tại mọi điểm." Không đúng; tính hội tụ còn phụ thuộc vào tính liên tục của hàm và loại hội tụ đang xét.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu hàm tuần hoàn

Sinh viên cần phân biệt rõ chu kỳ, chu kỳ cơ bản và ý nghĩa lặp lại của đồ thị.

### Bước 2: Xem sin và cos như các dao động cơ bản

Thay vì chỉ coi sin và cos là các hàm lượng giác quen thuộc, hãy nhìn chúng như các mode nền tảng.

### Bước 3: Biểu diễn chuỗi Fourier như tổng các mode

Ở bước này, bài toán mô tả tín hiệu được chuyển thành bài toán xác định các hệ số khai triển.

### Bước 4: Kết nối với tính trực giao

Ý tưởng phép chiếu trực giao là bản chất cốt lõi của bài học.

### Các điểm kiểm tra

- Sinh viên có giải thích được bằng lời vì sao một hàm tuần hoàn có thể gắn với các thành phần tần số hay không.
- Sinh viên có nhận ra vai trò khác nhau giữa mode tần số thấp và mode tần số cao hay không.
- Sinh viên có hiểu chuỗi Fourier là một phép chiếu trực giao chứ không phải mẹo đoán công thức hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm lượng giác cơ bản tự biểu diễn chính nó

Với $$ f(x)=\cos(3x) $$, chuỗi Fourier của hàm chỉ có đúng một mode khác 0:

$$
a_3=1,
\qquad
a_n=0 \text{ nếu } n\ne 3,
\qquad
b_n=0 \text{ với mọi } n.
$$

Ví dụ này cho thấy mỗi mode cơ bản đóng vai trò như một trục tọa độ trong không gian Fourier.

### Ví dụ 2: Hàm hằng là mode tần số 0

Với $$ f(x)=1 $$, ta có

$$ a_0=2,
\qquad
a_n=b_n=0 \text{ với } n\ge 1. $$

Kết quả này cho thấy chuỗi Fourier không chỉ chứa các thành phần dao động mà còn bao gồm cả mức trung bình của hàm.

### Ví dụ 3: Hàm răng cưa

Xét hàm số

$$ f(x)=x,
\qquad
-\pi<x<\pi, $$

rồi mở rộng tuần hoàn với chu kỳ $$ 2\pi $$. Vì hàm lẻ nên mọi hệ số cos đều bằng 0. Kết quả khai triển là

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này minh họa rằng một hàm có đồ thị hình học đơn giản vẫn có thể sở hữu phổ Fourier vô hạn.

### Ví dụ 4: Sóng vuông

Xét hàm tuần hoàn nhận giá trị $$ 1 $$ trên nửa chu kỳ dương và $$ -1 $$ trên nửa chu kỳ âm. Chuỗi Fourier của nó chỉ chứa các mode sin bậc lẻ. Ví dụ này cho thấy dạng phổ phản ánh trực tiếp cấu trúc đối xứng của hàm ban đầu.

## Câu hỏi khái niệm

1. Vì sao một hàm tuần hoàn có thể được nghiên cứu thông qua tần số thay vì chỉ quan sát trực tiếp đồ thị?
2. Chuỗi Fourier giống và khác ý tưởng khai triển theo hàm riêng ở chương Sturm-Liouville ở điểm nào?
3. Vì sao các mode tần số thấp thường mô tả hình dáng tổng thể, còn các mode tần số cao mô tả các chi tiết nhỏ?

## Bài toán ứng dụng

1. Trong âm học, vì sao một âm thanh tuần hoàn phức tạp có thể được phân tích thành các họa âm cơ bản?
2. Trong cơ học, vì sao dao động của dây đàn hoặc màng đàn thường được mô tả bằng các mode điều hòa?
3. Trong xử lý tín hiệu, vì sao việc biết tín hiệu tập trung nhiều năng lượng ở tần số thấp hay tần số cao lại có ý nghĩa quan trọng?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng cách phát hoặc mô tả một âm thanh tổng hợp và đặt câu hỏi: "Liệu ta có thể tách nó thành những dao động đơn giản hơn không?"
- Vẽ cùng một hàm và các tổng riêng Fourier đầu tiên để sinh viên quan sát trực tiếp quá trình ghép mode.
- Đặt câu hỏi giữa giờ: "Nếu loại bỏ toàn bộ các mode tần số cao, đồ thị sẽ mất đi đặc điểm gì?"
- Khuyến khích sinh viên liên hệ chuỗi Fourier với khái niệm mode riêng đã học ở chương trước.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên nhấn mạnh trực giác về âm thanh và dao động trước khi đi vào công thức. Với nhiều sinh viên, hình ảnh tách một hợp âm thành từng nốt cơ bản dễ tiếp cận hơn so với việc đối mặt ngay với một chuỗi vô hạn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên liên hệ chuỗi Fourier với cơ sở trực giao trong không gian $$ L^2 $$, hoặc giải thích vì sao chuỗi Fourier là trường hợp đặc biệt của khai triển theo hàm riêng của một toán tử Sturm-Liouville.

## Tóm tắt dễ nhớ

Chuỗi Fourier biểu diễn một hàm tuần hoàn dưới dạng tổng các mode sin và cos, giúp chuyển góc nhìn từ miền hình dạng sang miền tần số. Ý tưởng cốt lõi không nằm ở việc ghi nhớ công thức, mà ở phép chiếu một hàm lên hệ dao động cơ bản trực giao.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tín hiệu điện xoay chiều
- Bài toán: Dòng điện hoặc điện áp tuần hoàn trong thực tế thường không phải dạng sin thuần túy, nhưng vẫn có thể phân tích thành các họa âm.
- Mô hình:
$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$
- Giả thiết và giới hạn: Tín hiệu được xem là tuần hoàn và đủ điều kiện khả tích trên một chu kỳ.
- Diễn giải: Chuỗi Fourier phân tách tín hiệu phức tạp thành tổ hợp các thành phần tần số đơn giản hơn.

#### Sóng và dao động cơ học lặp lại
- Bài toán: Một chuyển động lặp theo chu kỳ đo được từ thực nghiệm nhưng có dạng không trơn hoặc bị méo.
- Mô hình: Sử dụng chuỗi Fourier để biểu diễn dạng hàm tuần hoàn.
- Giả thiết và giới hạn: Biểu diễn mang tính toàn cục trên cả chu kỳ; sự hội tụ từng điểm có thể trở nên tinh tế gần các điểm gián đoạn.
- Diễn giải: Mỗi mode sin-cos tương ứng với một thành phần dao động riêng của tín hiệu.

### 2. Trực giác bổ sung và các kết nối

Chuỗi Fourier là sự mở rộng tự nhiên của ý tưởng khai triển theo hàm riêng, trong đó cơ sở sin-cos xuất hiện trực tiếp từ tính tuần hoàn. Một ngộ nhận phổ biến là coi chuỗi Fourier chỉ là một kỹ thuật xấp xỉ; thực tế, đây là ngôn ngữ mode nền tảng cho nhiều bài toán PDE và xử lý tín hiệu. Bài học này nối tiếp trực tiếp Chương 7, nơi ta đã làm quen với việc khai triển hàm theo các hàm riêng phù hợp.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)
f = np.sign(x)

S = np.zeros_like(x)
for k in range(1, 10, 2):
    S += (4 / (np.pi * k)) * np.sin(k * x)

plt.plot(x, f, label="wave vuong", color="black")
plt.plot(x, S, "--", label="tong Fourier 5 mode le")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Chuoi Fourier cua song vuong")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Fourier series square wave animation
- search: harmonic decomposition periodic signal
- search: Gibbs phenomenon introductory visualization

### 5. Bài toán mẫu có bối cảnh thực

Cho sóng vuông tuần hoàn lẻ
$$
f(x)=
\begin{cases}
1, & 0<x<\pi,\\
-1, & -\pi<x<0.
\end{cases}
$$
Vì $$ f $$ là hàm lẻ nên chỉ còn các hệ số sin:
$$
b_n=\frac{2}{\pi}\int_0^{\pi}\sin(nx)\,dx
=
\begin{cases}
\frac{4}{n\pi}, & n\ \text{lẻ},\\
0, & n\ \text{chẵn}.
\end{cases}
$$
Do đó
$$
f(x)\sim \frac{4}{\pi}\left(\sin x+\frac{1}{3}\sin 3x+\frac{1}{5}\sin 5x+\cdots\right).
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm ý tưởng biểu diễn hàm tuần hoàn bằng các hàm sin, cos và tính được một số hệ số cơ bản.

**Bậc sau đại học.** Nhấn mạnh cấu trúc không gian $$ L^2 $$, tính trực giao trong không gian Hilbert và quan điểm phổ của toán tử đạo hàm bậc hai trên đường tròn.

## Video tham khảo

- Xem trước: [TTV: Chuỗi Fourier - Chuỗi có thể vẽ bất kỳ hình dạng gì mà bạn muốn](https://www.youtube.com/watch?v=Ya-feoX0Qkk) — Toán Thú Vị, tiếng Việt. Minh họa trực quan cách chuỗi Fourier có thể tái tạo các hình vẽ phức tạp.
- [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Giải thích bản chất chuỗi Fourier từ bài toán truyền nhiệt đến việc vẽ đường cong bằng các vòng tròn quay.
- [Intro to FOURIER SERIES: The Big Idea](https://www.youtube.com/watch?v=wmCIrpLBFds) — Dr. Trefor Bazett, tiếng Anh. Trình bày ý tưởng cốt lõi của chuỗi Fourier trước khi đi vào các công thức tính hệ số.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
