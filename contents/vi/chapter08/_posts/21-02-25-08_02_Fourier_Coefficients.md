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

## Mục tiêu

Bài học này tập trung vào cách tính và diễn giải các hệ số Fourier. Sau bài học, sinh viên cần biết vì sao công thức hệ số xuất hiện từ trực giao, biết tính $$ a_n,\quad b_n $$ trong những ví dụ điển hình, hiểu các hệ số như tọa độ của hàm trong cơ sở lượng giác, và thấy được chúng đo "mức đóng góp" của từng tần số vào tín hiệu.

## Kiến thức nền

Sinh viên nên nắm chuỗi Fourier cơ bản, tích phân xác định, và trực giao của sin-cos trên một chu kỳ. Bài này là nơi trực giác "phép chiếu" phải được biến thành kỹ thuật tính toán chính xác.

## Dẫn nhập

Việc viết chuỗi Fourier sẽ không có nhiều ý nghĩa nếu ta không biết lấy các hệ số bằng cách nào. Nhưng điều hay ở đây là ta không phải đoán. Cũng như trong đại số tuyến tính, khi có một cơ sở trực giao, các tọa độ của một vector được tách ra rất sạch bằng tích vô hướng. Fourier coefficients xuất hiện chính xác theo tinh thần đó.

Nếu dạy tốt bài này, sinh viên sẽ bớt xem các công thức tích phân là thứ phải học thuộc. Thay vào đó, các em sẽ hiểu chúng là kết quả tất yếu của trực giao. Một khi điều đó được thông suốt, hầu như mọi bài toán Fourier sau này sẽ trở nên dễ thở hơn nhiều.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Mỗi hệ số Fourier giống như một núm điều chỉnh âm lượng cho một nốt nhạc riêng. Hệ số lớn nghĩa là mode đó xuất hiện mạnh trong tín hiệu; hệ số nhỏ nghĩa là mode đó góp ít. Toàn bộ phổ Fourier là bản đồ cho biết "tín hiệu này được ghép từ những tần số nào và mạnh yếu ra sao".

### Cách nhìn hình ảnh

Nếu nhìn đồ thị tổng riêng Fourier, việc thay đổi một hệ số cụ thể sẽ làm tăng hoặc giảm một gợn dao động tương ứng với tần số đó. Bởi vậy, hệ số Fourier có thể được hiểu như "tọa độ phổ" của hàm, còn đồ thị gốc là tổ hợp của các gợn này.

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

Chúng xuất hiện vì các hàm lượng giác là trực giao trên đoạn

$$ [-\pi,\pi]. $$

## Những ngộ nhận thường gặp

- "Cần nhớ công thức hệ số như công thức độc lập." Không đúng; chúng xuất phát trực tiếp từ trực giao.
- "Nếu hàm có chuỗi Fourier thì hệ số luôn khó tính." Không hẳn; đối xứng chẵn lẻ thường làm triệt tiêu một nửa công việc.
- "Hệ số lớn nhất luôn là mode quan trọng nhất về mọi mặt." Cần cẩn thận; còn phải xem bài toán đang đo bằng chuẩn nào và đang xét hiện tượng gì.
- "Nếu vài hệ số đầu nhỏ thì phần còn lại chắc không quan trọng." Sai; phổ có thể dồn năng lượng vào nhiều mode cao.

## Tiến trình học tập đề xuất

### Bước 1: Nhớ lại trực giao

Nếu sinh viên không còn cảm giác rõ về trực giao của sin-cos, nên ôn lại trước.

### Bước 2: Suy ra công thức hệ số

Không nên bắt đầu bằng học thuộc; nên bắt đầu bằng phép chiếu.

### Bước 3: Tính hệ số trên các ví dụ cơ bản

Hàm hằng, hàm lượng giác đơn, hàm lẻ, hàm chẵn là các ví dụ mở đường rất tốt.

### Bước 4: Diễn giải hệ số theo phổ

Đây là lúc công thức chuyển thành ý nghĩa vật lý và tín hiệu.

### Các checkpoint

- Sinh viên có tự giải thích được vì sao nhân với một mode rồi tích phân sẽ "tách" đúng hệ số hay không.
- Sinh viên có tính đúng

$$ a_n,\ b_n $$

ở các ví dụ ngắn hay không.
- Sinh viên có hiểu hệ số như tọa độ trong cơ sở trực giao hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm hằng

Với $$ f(x)=1 $$, ta có

$$ a_0=\frac{1}{\pi}\int_{-\pi}^{\pi}1\,dx=2. $$

Còn với mọi $$ n\ge 1 $$, $$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}\cos(nx)\,dx=0,
\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}\sin(nx)\,dx=0.
$$

Vậy chuỗi Fourier chỉ là chính hằng số đó. Ví dụ này giúp sinh viên thấy $$ a_0 $$ đại diện cho thành phần trung bình của hàm.

### Ví dụ 2: Một mode lượng giác đơn

Với $$ f(x)=\cos(kx) $$, ta được $$ a_k=1 $$, và mọi hệ số khác bằng 0. Đây là bài kiểm tra trực giác rất tốt: nếu cơ sở lượng giác là đúng, thì một phần tử của cơ sở phải có đúng một tọa độ khác 0.

### Ví dụ 3: Hàm răng cưa

Xét

$$ f(x)=x,
\qquad -\pi<x<\pi. $$

Vì $$ f $$ là hàm lẻ nên $$ a_n=0 $$ với mọi $$ n $$. Ta chỉ tính

$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
=\frac{2}{\pi}\int_0^{\pi}x\sin(nx)\,dx.
$$

Tích phân từng phần cho

$$ b_n=\frac{2(-1)^{n+1}}{n}. $$

Suy ra

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Ví dụ này cho thấy đối xứng lẻ giúp tiết kiệm đáng kể tính toán.

### Ví dụ 4: Sóng vuông

Xét

$$
f(x)=
\begin{cases}
1, & 0<x<\pi,\\
-1, & -\pi<x<0.
\end{cases}
$$

Hàm lẻ nên $$ a_n=0 $$. Ta tính được

$$
b_n=
\begin{cases}
\dfrac{4}{n\pi}, & n \text{ lẻ},\\
0, & n \text{ chẵn}.
\end{cases}
$$

Đây là ví dụ điển hình cho việc phổ chỉ chứa các harmonic lẻ.

## Câu hỏi khái niệm

1. Vì sao công thức hệ số Fourier là phép chiếu chứ không phải mẹo tính toán?
2. Hệ số Fourier nói gì về tần số xuất hiện trong tín hiệu?
3. Vì sao đối xứng của hàm thường làm một số hệ số tự động biến mất?

## Bài toán ứng dụng

1. Trong âm học, nếu một tín hiệu có biên độ mạnh ở harmonic thứ ba và thứ năm, điều đó gợi gì về phổ Fourier của nó?
2. Trong truyền tín hiệu số, vì sao biết phổ Fourier giúp ta hiểu nhiễu tập trung ở dải tần nào?
3. Trong dao động cơ học, nếu kích thích ban đầu có dạng gần đối xứng lẻ, vì sao ta kỳ vọng các mode sine chiếm ưu thế?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự suy ra công thức hệ số từ trực giao thay vì đưa công thức ngay từ đầu.
- Dùng các ví dụ rất ngắn như hàm hằng và một mode cos đơn để sinh viên tự kiểm tra trực giác.
- Hỏi cả lớp: "Hệ số nào đo thành phần trung bình của tín hiệu?"
- Tổ chức hoạt động so sánh hai hàm có đồ thị khác nhau nhưng cùng vài hệ số đầu để nói về ý nghĩa phổ.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để các em luyện thật chắc bốn mẫu cơ bản: hàm hằng, hàm cos, hàm lẻ, hàm chẵn. Nếu bốn mẫu này vững, việc tính hệ số cho các hàm phức tạp hơn sẽ bớt áp lực rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi diễn giải các hệ số Fourier dưới ngôn ngữ tích vô hướng trong $$ L^2 $$, hoặc so sánh trực tiếp công thức hệ số Fourier với công thức tọa độ trong đại số tuyến tính hữu hạn chiều.

## Tóm tắt dễ nhớ

Hệ số Fourier là tọa độ của một hàm trong cơ sở lượng giác trực giao. Chúng được lấy bằng phép chiếu tích phân. Biết hệ số nghĩa là biết tín hiệu chứa bao nhiêu của từng mode tần số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân tích âm thanh
- Bài toán: Muốn biết tín hiệu âm thanh chứa bao nhiêu năng lượng ở từng họa âm.
- Mô hình:
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,\qquad
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
$$
- Giả thiết và giới hạn: Dữ liệu được xem như một chu kỳ điển hình hoặc được tuần hoàn hóa.
- Diễn giải: Các hệ số Fourier đo "độ chồng" của tín hiệu với từng mode chuẩn.

#### Dao động cưỡng bức có nhiều họa âm
- Bài toán: Một lực lặp theo chu kỳ có dạng phức tạp có thể được tách thành các thành phần sin-cos.
- Mô hình: Dùng các hệ số Fourier để viết lực cưỡng bức thành tổng mode.
- Giả thiết và giới hạn: Tính toán lý tưởng hóa; tín hiệu thực có thể cần cắt ngắn hoặc lọc.
- Diễn giải: Hệ số lớn ở mode nào thì tần số đó đóng góp mạnh hơn.

### 2. Trực giác bổ sung và các kết nối

Hệ số Fourier là tọa độ của hàm trong cơ sở trực giao sin-cos. Một nhầm lẫn phổ biến là xem các công thức hệ số như phải học thuộc; tốt hơn là hiểu chúng đến từ phép chiếu trực giao. Bài này nối rất chặt với khái niệm trực giao và hệ số khai triển trong Sturm-Liouville.

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

Với
$$ f(x)=x,\qquad -\pi<x<\pi, $$
ta có hàm lẻ nên $$ a_n=0 $$. Khi đó
$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\sin(nx)\,dx
=\frac{2(-1)^{n+1}}{n}.
$$
Vì thế
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo tính $$ a_n,b_n $$ cho các hàm chẵn, lẻ và từng khúc đơn giản.

**Bậc sau đại học.** Diễn giải hệ số như phép chiếu trong không gian Hilbert và liên hệ với phổ năng lượng của tín hiệu.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
