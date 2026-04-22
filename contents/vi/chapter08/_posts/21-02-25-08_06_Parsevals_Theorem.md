---
layout: post
title: "Định Lý Parseval"
chapter: '08'
order: 6
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---
![21 02 25 08 06 Parsevals Theorem]({{ site.imgurl }}/chapter_img/chapter08/06_parsevals_theorem.svg)

## Mục tiêu

Bài học này giúp sinh viên hiểu định lý Parseval như một định luật bảo toàn năng lượng cho chuỗi Fourier. Sau bài học, sinh viên cần biết phát biểu Parseval, hiểu ý nghĩa năng lượng của tổng bình phương các hệ số Fourier, biết dùng Parseval để ước lượng sai số hoặc tính một số tổng vô hạn cổ điển, và thấy được vì sao định lý này đặc biệt quan trọng trong PDE và phân tích tín hiệu.

## Kiến thức nền

Sinh viên nên nắm chuỗi Fourier, trực giao, và chuẩn $$ L^2 $$ ở mức trực giác. Bài này là một trong những nơi đẹp nhất mà công thức Fourier trở thành một phát biểu sâu về cấu trúc năng lượng.

## Dẫn nhập

Khi ta phân tách một hàm thành các mode Fourier, một câu hỏi tự nhiên xuất hiện: liệu "năng lượng" của hàm có bị thất thoát khi chuyển sang miền tần số hay không? Định lý Parseval trả lời rất đẹp: không. Năng lượng toàn phần trong miền không gian đúng bằng tổng năng lượng của từng mode Fourier.

Về mặt sư phạm, đây là bài rất quan trọng để sinh viên thấy Fourier không chỉ là cách viết lại hàm, mà là một phép phân rã bảo toàn lượng thông tin quan trọng. Trong cơ học, nhiệt, sóng và xử lý tín hiệu, đây là một ý tưởng cực kỳ trung tâm.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng một tín hiệu âm thanh được tách thành nhiều họa âm. Parseval nói rằng tổng năng lượng của âm thanh không biến mất sau phép tách ấy; nó chỉ được phân bố lại vào từng họa âm. Năng lượng không mất đi, chỉ đổi nơi "lưu trữ".

### Cách nhìn hình ảnh

Nếu ta vẽ phổ Fourier của một tín hiệu, các bình phương hệ số Fourier có thể được xem như các cột năng lượng nằm ở từng tần số. Parseval nói rằng diện tích năng lượng trong miền gốc bằng tổng các cột này. Đó là cách nhìn rất trực quan về mối liên hệ giữa miền thời gian hoặc không gian và miền tần số.

### Cách nhìn hình thức

Với $$ f\in L^2(-\pi,\pi) $$ có chuỗi Fourier

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr),
$$

định lý Parseval phát biểu:

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert f(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

Vế trái là năng lượng của hàm trong miền gốc, còn vế phải là tổng năng lượng của các mode Fourier.

## Những ngộ nhận thường gặp

- "Parseval chỉ là một công thức kỹ thuật." Sai. Nó là phát biểu nền tảng về bảo toàn năng lượng trong phép phân rã Fourier.
- "Nếu biết vài hệ số đầu thì có thể bỏ qua phần còn lại mà không lo." Cần cẩn thận; còn phải xét tổng bình phương của toàn bộ phần đuôi.
- "Chuỗi Fourier chỉ liên quan đến hình dạng, không liên quan năng lượng." Không đúng; Parseval cho thấy Fourier rất hợp với chuẩn năng lượng.
- "Định lý này chỉ dùng trong bài tính tổng đẹp." Sai; các ứng dụng trong PDE và sai số xấp xỉ còn quan trọng hơn nhiều.

## Tiến trình học tập đề xuất

### Bước 1: Ôn ý tưởng trực giao

Không có trực giao thì Parseval không thể xuất hiện đẹp như vậy.

### Bước 2: Hiểu năng lượng theo chuẩn

$$ L^2 $$

Giúp sinh viên thấy lý do vế trái có bình phương.

### Bước 3: Diễn giải vế phải như năng lượng phổ

Mỗi mode đóng góp qua bình phương hệ số.

### Bước 4: Ứng dụng vào sai số và tính tổng

Đây là lúc định lý trở nên sống động.

### Các checkpoint

- Sinh viên có phát biểu đúng Parseval hay không.
- Sinh viên có giải thích được tại sao phải bình phương hệ số hay không.
- Sinh viên có thấy mối liên hệ giữa Parseval và sai số cắt chuỗi hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dạng năng lượng của tổng riêng

Nếu

$$
S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr),
$$

thì do trực giao, ta có

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert S_N(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{N}(a_n^2+b_n^2).
$$

Ví dụ này là bước tiền Parseval rất quan trọng: trước hết hãy thấy điều đó đúng cho tổng hữu hạn.

### Ví dụ 2: Áp dụng cho

$$ f(x)=x $$

trên $$ (-\pi,\pi) $$ Ta biết chuỗi Fourier của $$ x $$ là

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Do đó

$$
a_0=0,\qquad a_n=0,\qquad b_n=\frac{2(-1)^{n+1}}{n}.
$$

Áp dụng Parseval:

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx
=
\sum_{n=1}^{\infty}\frac{4}{n^2}.
$$

Vế trái bằng

$$
\frac{1}{\pi}\cdot \frac{2\pi^3}{3}
=
\frac{2\pi^2}{3}.
$$

Suy ra

$$
\sum_{n=1}^{\infty}\frac{1}{n^2}
=
\frac{\pi^2}{6}.
$$

Đây là một trong những ví dụ đẹp nhất của Fourier trong toán cổ điển.

### Ví dụ 3: Sai số đuôi phổ

Từ Parseval, nếu cắt chuỗi tại $$ N $$, ta có

$$
\lVert f-S_N\rVert_{L^2}^2
=
\pi\sum_{n=N+1}^{\infty}(a_n^2+b_n^2).
$$

Ví dụ này cho thấy phần đuôi của phổ Fourier đo đúng năng lượng sai số. Đây là ý nghĩa thực dụng rất lớn trong xấp xỉ và số học tính toán.

## Câu hỏi khái niệm

1. Vì sao Parseval được xem như định luật bảo toàn năng lượng của Fourier series?
2. Tại sao chuẩn $$ L^2 $$ lại là chuẩn tự nhiên nhất cho Fourier?
3. Vì sao bình phương hệ số Fourier mới là đại lượng phù hợp để đo đóng góp của từng mode?

## Bài toán ứng dụng

1. Trong tín hiệu học, vì sao phổ năng lượng của tín hiệu thường được đọc từ bình phương biên độ các thành phần Fourier?
2. Trong phương trình nhiệt, vì sao mode cao thường đóng góp ít vào năng lượng tổng nếu hệ số Fourier giảm nhanh?
3. Trong tính toán số, vì sao Parseval giúp quyết định có thể cắt chuỗi ở đâu mà vẫn giữ sai số nhỏ?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Khi tách tín hiệu thành các tần số, năng lượng có bị chia nhỏ hay bị thất thoát?"
- Cho sinh viên kiểm tra Parseval trên một ví dụ hữu hạn rất ngắn trước khi phát biểu định lý tổng quát.
- Hỏi lớp: "Nếu các hệ số Fourier giảm nhanh, điều đó nói gì về năng lượng của đuôi phổ?"
- Tổ chức hoạt động dùng Parseval để tính một tổng vô hạn như

$$ \sum \frac{1}{n^2}. $$

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ chặt trực giác năng lượng và đồ thị cột phổ trước khi đi vào chứng minh. Với nhiều sinh viên, hiểu đúng ý nghĩa còn quan trọng hơn nhớ chính xác hằng số chuẩn hóa ở lần đầu.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi so sánh Parseval với định lý Pythagoras trong không gian vô hạn chiều, hoặc thảo luận dạng phức của Parseval như cầu nối sang biến đổi Fourier.

## Tóm tắt dễ nhớ

Định lý Parseval nói rằng năng lượng của hàm trong miền gốc bằng tổng năng lượng của các mode Fourier. Chuỗi Fourier không làm mất năng lượng; nó chỉ phân phối lại năng lượng vào các tần số. Vì vậy Parseval là chiếc cầu giữa phân tích phổ và chuẩn

$$ L^2. $$

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bảo toàn năng lượng của tín hiệu
- Bài toán: Muốn biết năng lượng của tín hiệu được phân bố thế nào giữa các họa âm.
- Mô hình Parseval:
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert f(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$
- Giả thiết và giới hạn: Hiểu theo chuẩn $$ L^2 $$; không phải mọi tín hiệu đều có hội tụ điểm đẹp.
- Diễn giải: Năng lượng toàn phần trong miền gốc bằng tổng năng lượng phổ.

#### Sai số cắt chuỗi trong mô phỏng số
- Bài toán: Cần biết mất bao nhiêu năng lượng khi bỏ các mode cao.
- Mô hình:
$$
\lVert f-S_N\rVert_{L^2}^2
=
\pi\sum_{n=N+1}^{\infty}(a_n^2+b_n^2).
$$
- Giả thiết và giới hạn: Sai số được đo trong chuẩn bình phương khả tích.
- Diễn giải: Đuôi phổ chính là năng lượng sai số còn lại.

### 2. Trực giác bổ sung và các kết nối

Parseval cho thấy Fourier không chỉ phân rã hình dạng, mà còn phân rã năng lượng. Một hiểu lầm phổ biến là xem bình phương hệ số như kỹ thuật hình thức; thật ra đó là lượng đóng góp năng lượng của từng mode. Bài này cũng là cầu nối quan trọng từ Fourier series sang Fourier transform.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 21)
energy = 4 / n**2

plt.bar(n, energy)
plt.xlabel("n")
plt.ylabel("mode energy")
plt.title("Nang luong mode cua f(x)=x")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Parseval theorem signal energy visualization
- search: Fourier mode energy spectrum
- search: truncation error Parseval Fourier series

### 5. Bài toán mẫu có bối cảnh thực

Với
$$ f(x)=x,\qquad -\pi<x<\pi, $$
ta có
$$ b_n=\frac{2(-1)^{n+1}}{n},\qquad a_n=0. $$
Áp dụng Parseval:
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx
=
\sum_{n=1}^{\infty}\frac{4}{n^2}.
$$
Từ đó suy ra
$$ \sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Phát biểu Parseval, dùng để tính tổng vô hạn và ước lượng sai số phổ.

**Bậc sau đại học.** Nhấn mạnh chuẩn $$ L^2 $$, đẳng cự của biến đổi Fourier và quan điểm Hilbert-space.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
