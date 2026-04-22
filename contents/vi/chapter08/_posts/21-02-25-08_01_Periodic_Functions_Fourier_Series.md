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

## Mục tiêu

Bài học này mở đầu chương Fourier bằng cách giúp sinh viên hiểu vì sao một hàm tuần hoàn có thể được xem như tổng của các dao động cơ bản. Sau bài học, sinh viên cần hiểu khái niệm hàm tuần hoàn, nhận ra vai trò của các mode $$ \sin(nx),\quad \cos(nx) $$, hiểu ý tưởng chuỗi Fourier như một phép chiếu lên hệ trực giao, và thấy được vì sao đây là ngôn ngữ nền tảng cho phương trình nhiệt, phương trình sóng và phân tích tín hiệu.

## Kiến thức nền

Sinh viên nên nắm tích phân xác định, trực giác về hàm lượng giác, và ý tưởng cơ sở trực giao từ đại số tuyến tính hoặc từ bài Sturm-Liouville trước đó. Nếu đã quen với khái niệm mode riêng, bài này sẽ trở nên đặc biệt tự nhiên.

## Dẫn nhập

Một tín hiệu âm thanh, một dao động cơ học, hay một nhiệt độ biên tuần hoàn theo thời gian thường trông rất phức tạp nếu chỉ nhìn trực tiếp trong miền không gian hoặc thời gian. Nhưng điều đáng ngạc nhiên là nhiều tín hiệu như vậy có thể được phân tách thành những dao động điều hòa đơn giản hơn nhiều. Chuỗi Fourier là công cụ cho phép ta làm điều đó một cách có hệ thống.

Về mặt sư phạm, đây là một trong những ý tưởng quan trọng nhất của toàn bộ học phần. Nó không chỉ giải thích cách phân tích tín hiệu thành tần số, mà còn chuẩn bị trực tiếp cho cách giải PDE bằng tách biến. Nói ngắn gọn, Fourier giúp ta biến một hình dạng phức tạp thành tổ hợp của các mode cơ bản mà hệ "hiểu" rất tốt.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy nghĩ đến một hợp âm trên đàn piano. Tai người nghe một âm thanh tổng hợp, nhưng thực ra nó là sự chồng chất của nhiều tần số riêng biệt. Chuỗi Fourier làm điều tương tự với hàm số: nó tách một tín hiệu tuần hoàn phức tạp thành những "nốt cơ bản" là sin và cos.

### Cách nhìn hình ảnh

Nếu ta vẽ một hàm tuần hoàn phức tạp, rồi lần lượt cộng thêm các mode $$\cos x,\quad \sin x,\quad \cos 2x,\quad \sin 2x,\ldots$$, ta sẽ thấy đồ thị được xây dựng dần từ thô đến tinh. Các mode tần số thấp tạo nên hình dáng lớn, còn các mode tần số cao tinh chỉnh các chi tiết nhỏ hơn. Đây là cách nhìn rất mạnh để giải thích tại sao Fourier vừa là công cụ hình học vừa là công cụ phổ.

### Cách nhìn hình thức

Một hàm $$ f $$ được gọi là tuần hoàn với chu kỳ $$ T>0 $$ nếu

$$ f(x+T)=f(x)
\qquad \text{với mọi } x. $$

Với hàm tuần hoàn chu kỳ $$ 2\pi $$, chuỗi Fourier có dạng

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$

Dấu $$ \sim $$ nhắc ta rằng đây là biểu diễn theo nghĩa hội tụ thích hợp, không phải lúc nào cũng là đẳng thức từng điểm mọi nơi.

## Những ngộ nhận thường gặp

- "Chuỗi Fourier chỉ dành cho hàm lượng giác." Sai. Nó dùng để biểu diễn nhiều hàm tuần hoàn rất khác nhau.
- "Nếu hàm không trơn thì Fourier vô dụng." Không đúng. Ngay cả hàm có bước nhảy vẫn có chuỗi Fourier rất hữu ích.
- "Sin và cos được chọn tùy ý." Sai. Chúng là hệ mode trực giao tự nhiên trên đoạn tuần hoàn.
- "Chuỗi Fourier luôn hội tụ đúng bằng hàm ở mọi điểm." Không phải; điều này còn phụ thuộc vào tính liên tục và loại hội tụ.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu hàm tuần hoàn

Sinh viên cần phân biệt rõ chu kỳ, chu kỳ cơ bản, và ý nghĩa đồ thị lặp lại.

### Bước 2: Nhìn sin-cos như các dao động cơ bản

Không nên xem chúng chỉ là hàm quen thuộc mà nên xem là các mode nền.

### Bước 3: Đưa ra chuỗi Fourier như một tổng các mode

Đây là lúc sinh viên hiểu "bài toán mô tả tín hiệu" được biến thành "bài toán tìm hệ số".

### Bước 4: Kết nối với trực giao

Ý tưởng chiếu là bản chất sâu nhất của bài.

### Các checkpoint

- Sinh viên có giải thích được bằng lời vì sao một hàm tuần hoàn có thể liên hệ với tần số hay không.
- Sinh viên có nhận ra vai trò khác nhau của mode thấp và mode cao hay không.
- Sinh viên có hiểu chuỗi Fourier là một phép chiếu chứ không phải mẹo đoán công thức hay không.

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

Ví dụ này rất quan trọng vì nó giúp sinh viên thấy mỗi mode cơ bản là một "tọa độ trục" trong không gian Fourier.

### Ví dụ 2: Hàm hằng là mode tần số 0

Với $$ f(x)=1 $$, ta có

$$ a_0=2,
\qquad
a_n=b_n=0 \text{ với } n\ge 1. $$

Điều này cho thấy chuỗi Fourier không chỉ chứa dao động mà còn chứa cả mức nền trung bình của hàm.

### Ví dụ 3: Hàm răng cưa

Xét

$$ f(x)=x,
\qquad
-\pi<x<\pi, $$

rồi mở rộng tuần hoàn. Vì hàm lẻ nên các hệ số cos đều bằng 0. Kết quả là

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này cho sinh viên thấy một đồ thị rất đơn giản về hình học vẫn có phổ Fourier vô hạn.

### Ví dụ 4: Sóng vuông

Xét hàm tuần hoàn nhận giá trị $$ 1 $$ trên nửa chu kỳ dương và $$ -1 $$ trên nửa chu kỳ âm. Chuỗi Fourier của nó chỉ chứa các mode sine bậc lẻ. Đây là ví dụ cực kỳ quan trọng để sinh viên thấy dạng phổ phản ánh trực tiếp cấu trúc đối xứng của dữ liệu.

## Câu hỏi khái niệm

1. Vì sao một hàm tuần hoàn lại có thể được nghiên cứu qua tần số thay vì chỉ qua đồ thị trực tiếp?
2. Chuỗi Fourier giống và khác ý tưởng khai triển theo hàm riêng ở chương Sturm-Liouville như thế nào?
3. Vì sao các mode tần số thấp thường mô tả hình dáng lớn, còn mode tần số cao mô tả chi tiết nhỏ?

## Bài toán ứng dụng

1. Trong âm học, vì sao một âm thanh tuần hoàn phức tạp có thể được phân tích thành các họa âm cơ bản?
2. Trong cơ học, vì sao dao động của dây đàn hoặc màng đàn thường được mô tả bằng các mode điều hòa?
3. Trong xử lý tín hiệu, vì sao việc biết tín hiệu chứa nhiều năng lượng ở tần số thấp hay cao lại quan trọng?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng cách phát hoặc mô tả một âm thanh tổng hợp và hỏi: "Liệu ta có thể tách nó thành những dao động đơn giản hơn không?"
- Vẽ cùng một hàm và các tổng riêng Fourier đầu tiên để sinh viên thấy quá trình "ghép mode" bằng mắt.
- Hỏi giữa giờ: "Nếu bỏ hết các mode cao, đồ thị sẽ mất điều gì?"
- Khuyến khích sinh viên liên hệ giữa Fourier và khái niệm mode riêng đã gặp ở chương trước.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên nhấn mạnh trực giác âm thanh và dao động trước, sau đó mới đi vào công thức. Với nhiều sinh viên, hình ảnh "hợp âm được tách thành nốt" dễ nhớ hơn nhiều so với chuỗi vô hạn ngay từ đầu.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi liên hệ chuỗi Fourier với cơ sở trực giao trong không gian $$ L^2 $$, hoặc giải thích vì sao Fourier là trường hợp đặc biệt của khai triển theo hàm riêng của một toán tử Sturm-Liouville.

## Tóm tắt dễ nhớ

Chuỗi Fourier biểu diễn một hàm tuần hoàn bằng tổng các mode sin và cos. Đó là cách chuyển từ miền hình dạng sang miền tần số. Ý tưởng cốt lõi không phải là công thức, mà là phép chiếu một hàm lên một hệ dao động cơ bản trực giao.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tín hiệu điện xoay chiều
- Bài toán: Dòng điện hoặc điện áp tuần hoàn thường không phải sin thuần, nhưng vẫn có thể được phân tích thành các họa âm.
- Mô hình:
$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$
- Giả thiết và giới hạn: Tín hiệu được xem là tuần hoàn và đủ khả tích trên một chu kỳ.
- Diễn giải: Chuỗi Fourier biến tín hiệu phức tạp thành tổ hợp các tần số đơn giản hơn.

#### Sóng và dao động cơ học lặp lại
- Bài toán: Một chuyển động lặp theo chu kỳ được đo thực nghiệm nhưng có dạng không trơn hoặc méo.
- Mô hình: Dùng chuỗi Fourier để biểu diễn profile tuần hoàn.
- Giả thiết và giới hạn: Biểu diễn là toàn cục theo chu kỳ; hội tụ điểm có thể tinh tế gần chỗ gián đoạn.
- Diễn giải: Mỗi mode sin-cos là một thành phần dao động riêng của tín hiệu.

### 2. Trực giác bổ sung và các kết nối

Chuỗi Fourier là bản mở rộng của ý tưởng khai triển theo hàm riêng, nhưng ở đây cơ sở sin-cos được chọn tự nhiên bởi tính tuần hoàn. Một bẫy phổ biến là nghĩ chuỗi Fourier chỉ là một "mẹo xấp xỉ"; thật ra nó là ngôn ngữ mode cho nhiều PDE và tín hiệu. Bài này nối trực tiếp với Chương 7, nơi ta đã học cách khai triển theo các hàm riêng thích hợp.

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
Vì $$ f $$ lẻ nên chỉ còn hệ số sin:
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

**Bậc đại học.** Nắm ý tưởng biểu diễn hàm tuần hoàn bằng sin-cos và tính vài hệ số cơ bản.

**Bậc sau đại học.** Nhấn mạnh không gian $$ L^2 $$, trực giao Hilbert và quan điểm phổ của toán tử đạo hàm bậc hai trên vòng tròn.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
