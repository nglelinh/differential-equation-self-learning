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

Trong không gian Euclid 3 chiều, định lý Pythagoras nói rằng bình phương độ dài vectơ bằng tổng bình phương ba tọa độ trực giao: $\|\mathbf{v}\|^2 = v_x^2 + v_y^2 + v_z^2$. **Định lý Parseval** chính là **Định lý Pythagoras trong không gian hàm vô hạn chiều**: tổng năng lượng trung bình của tín hiệu trong miền thời gian bằng **đúng** tổng năng lượng các thành phần tần số trong miền Fourier!

## Bản đồ kiến thức nền: Bốn ý nghĩa sâu sắc của Định lý Parseval

1. **Đẳng thức Bảo toàn Năng lượng trên $[-L, L]$**:
   $$\frac{1}{L}\int_{-L}^{L} [f(x)]^2\,dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty}(a_n^2 + b_n^2).$$
   (Với chuỗi Fourier phức $c_n$: $\frac{1}{2L}\int_{-L}^{L} \vert f(x) \vert^2\,dx = \sum_{n=-\infty}^{\infty} \vert c_n \vert^2$).
2. **Bất đẳng thức Bessel & Tính đầy đủ**:
   Tổng hữu hạn $\frac{a_0^2}{2} + \sum_{n=1}^{N}(a_n^2 + b_n^2) \le \frac{1}{L}\int_{-L}^L f^2\,dx$ luôn bị chặn trên (Bessel); dấu bằng khi $N \to \infty$ (Parseval) khẳng định hệ lượng giác là **đầy đủ** (không bị thiếu chiều nào!).
3. **Đo tỷ lệ năng lượng giữ lại khi nén tín hiệu (MP3 / JPEG)**:
   Tính tỷ số $\frac{E_N}{E_{\text{tổng}}}$ cho biết giữ lại $N$ tần số đầu bảo toàn bao nhiêu phần trăm năng lượng gốc.
4. **Vũ khí tính các tổng chuỗi số kinh điển**:
   Áp dụng Parseval cho những hàm đơn giản như $f(x) = x$ hay $f(x) = x^2$ lập tức tính ra $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$ và $\sum \frac{1}{n^4} = \frac{\pi^4}{90}$!

## Mục tiêu

Bài học này giúp sinh viên hiểu định lý Parseval như một định luật bảo toàn năng lượng cho chuỗi Fourier. Sau bài học, sinh viên cần nắm phát biểu định lý Parseval, hiểu ý nghĩa năng lượng của tổng bình phương các hệ số Fourier, vận dụng được định lý để ước lượng sai số cắt chuỗi hoặc tính một số tổng vô hạn cổ điển, và nhận ra vai trò của nó trong PDE cũng như phân tích tín hiệu.

## Kiến thức nền

Sinh viên cần nắm chuỗi Fourier, tính trực giao và khái niệm chuẩn $$ L^2 $$ ở mức trực giác. Đây là nội dung tiêu biểu cho thấy công thức Fourier gắn liền với cấu trúc năng lượng của hệ.

## Dẫn nhập

Khi phân tách một hàm thành các mode Fourier, một câu hỏi tự nhiên đặt ra: liệu "năng lượng" của hàm có bị thay đổi khi chuyển từ miền không gian sang miền tần số hay không? Định lý Parseval cho câu trả lời rõ ràng: không. Năng lượng toàn phần trong miền không gian bằng đúng tổng năng lượng đóng góp bởi từng mode Fourier.

Từ góc độ ứng dụng, kết quả này cho thấy chuỗi Fourier không chỉ là một cách viết lại hàm, mà là một phép phân rã bảo toàn năng lượng. Trong cơ học, truyền nhiệt, truyền sóng và xử lý tín hiệu, đây là nguyên lý nền tảng.

### Khung giải thích (nên đọc chậm): Chứng minh Bài toán Basel $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$ chỉ trong 3 dòng bằng Parseval

Ta đã biết ở bài 08-02: với $f(x) = x$ trên $(-\pi, \pi)$ ($L = \pi$), ta có $a_0 = a_n = 0$ và $b_n = \frac{2(-1)^{n+1}}{n}$.
1. **Tính vế trái của Parseval (Năng lượng miền không gian)**:
   $$\frac{1}{\pi}\int_{-\pi}^{\pi} x^2\,dx = \frac{2}{\pi}\left[\frac{x^3}{3}\right]_0^{\pi} = \mathbf{\frac{2\pi^2}{3}}.$$
2. **Tính vế phải của Parseval (Năng lượng miền tần số)**:
   $$\sum_{n=1}^{\infty} b_n^2 = \sum_{n=1}^{\infty} \frac{4}{n^2} = 4\sum_{n=1}^{\infty} \frac{1}{n^2}.$$
3. **Cho hai vế bằng nhau**:
   $$4\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{2\pi^2}{3} \implies \sum_{n=1}^{\infty} \frac{1}{n^2} = \mathbf{\frac{\pi^2}{6}} \approx 1{,}64493!$$
Kiểm tra tỷ lệ năng lượng của chỉ 3 số hạng đầu: $1 + \frac{1}{4} + \frac{1}{9} = 1{,}3611 \implies \frac{1{,}3611}{1{,}6449} \approx \mathbf{82{,}7\%}$ toàn bộ năng lượng sóng răng cưa đã nằm gọn trong 3 tần số đầu tiên!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một tín hiệu âm thanh được tách thành nhiều họa âm. Định lý Parseval khẳng định rằng tổng năng lượng của âm thanh không thay đổi sau phép phân tách; nó chỉ được phân bố lại vào từng họa âm riêng lẻ.

### Cách nhìn hình ảnh

Khi biểu diễn phổ Fourier của một tín hiệu, bình phương các hệ số Fourier có thể được xem như các cột năng lượng đặt tại từng tần số. Định lý Parseval cho biết tổng năng lượng tích phân trong miền gốc bằng tổng chiều cao các cột năng lượng này, tạo liên hệ trực quan giữa miền không gian (hoặc thời gian) và miền tần số.

### Cách nhìn hình thức

Với $$ f\in L^2(-\pi,\pi) $$ có chuỗi Fourier

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr),
$$

định lý Parseval phát biểu rằng

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert f(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$

Vế trái biểu thị năng lượng của hàm trong miền gốc, còn vế phải là tổng năng lượng của các mode Fourier.

## Những ngộ nhận thường gặp

- "Định lý Parseval chỉ là một đẳng thức kỹ thuật." Sai; đây là phát biểu nền tảng về sự bảo toàn năng lượng trong phép phân rã Fourier.
- "Chỉ cần biết vài hệ số đầu là đủ, có thể bỏ qua phần còn lại." Cần thận trọng; sai số còn phụ thuộc vào tổng bình phương của toàn bộ phần đuôi chuỗi.
- "Chuỗi Fourier chỉ mô tả hình dạng, không liên quan đến năng lượng." Không đúng; định lý Parseval cho thấy cơ sở Fourier tương thích tự nhiên với chuẩn năng lượng.
- "Định lý này chỉ dùng để tính các tổng số học." Sai; ứng dụng trong PDE và đánh giá sai số xấp xỉ còn quan trọng hơn nhiều.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại tính trực giao

Tính trực giao của hệ hàm lượng giác là cơ sở trực tiếp dẫn đến đẳng thức Parseval.

### Bước 2: Hiểu năng lượng theo chuẩn $$ L^2 $$

Bước này giải thích lý do xuất hiện bình phương hàm ở vế trái.

### Bước 3: Diễn giải vế phải như năng lượng phổ

Mỗi mode đóng góp vào tổng năng lượng thông qua bình phương hệ số của nó.

### Bước 4: Ứng dụng vào ước lượng sai số và tính tổng

Các ví dụ cụ thể giúp làm rõ giá trị thực hành của định lý.

### Các điểm kiểm tra

- Sinh viên có phát biểu đúng định lý Parseval hay không.
- Sinh viên có giải thích được vì sao phải lấy bình phương các hệ số hay không.
- Sinh viên có nắm được mối liên hệ giữa định lý Parseval và sai số cắt chuỗi hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dạng năng lượng của tổng riêng

Nếu

$$
S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr),
$$

thì nhờ tính trực giao, ta có

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert S_N(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{N}(a_n^2+b_n^2).
$$

Đây là bước chuẩn bị quan trọng: kiểm chứng đẳng thức năng lượng trên tổng hữu hạn trước khi chuyển qua giới hạn vô hạn.

### Ví dụ 2: Áp dụng cho $$ f(x)=x $$ trên $$ (-\pi,\pi) $$

Ta đã biết chuỗi Fourier của $$ x $$ là

$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$

Do đó

$$
a_0=0,\qquad a_n=0,\qquad b_n=\frac{2(-1)^{n+1}}{n}.
$$

Áp dụng định lý Parseval:

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

Đây là một ứng dụng kinh điển của giải tích Fourier trong việc tính tổng chuỗi số.

### Ví dụ 3: Sai số đuôi phổ

Từ định lý Parseval, nếu cắt cụt chuỗi tại bậc $$ N $$, sai số trong chuẩn $$ L^2 $$ thỏa mãn

$$
\lVert f-S_N\rVert_{L^2}^2
=
\pi\sum_{n=N+1}^{\infty}(a_n^2+b_n^2).
$$

Kết quả này cho thấy phần đuôi của phổ Fourier đo chính xác năng lượng sai số còn lại, mang ý nghĩa thực tế trong xấp xỉ hàm và tính toán số.

## Câu hỏi khái niệm

1. Vì sao định lý Parseval được xem là định luật bảo toàn năng lượng của chuỗi Fourier?
2. Tại sao chuẩn $$ L^2 $$ lại là chuẩn tự nhiên nhất đối với khai triển Fourier?
3. Vì sao bình phương hệ số Fourier mới là đại lượng phù hợp để đo mức đóng góp năng lượng của từng mode?

## Bài toán ứng dụng

1. Trong xử lý tín hiệu, vì sao phổ năng lượng của tín hiệu thường được đọc từ bình phương biên độ các thành phần Fourier?
2. Trong phương trình nhiệt, vì sao các mode tần số cao đóng góp ít vào tổng năng lượng nếu các hệ số Fourier suy giảm nhanh?
3. Trong tính toán số, định lý Parseval hỗ trợ như thế nào trong việc chọn bậc cắt chuỗi để giữ sai số trong ngưỡng cho phép?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Khi tách tín hiệu thành các tần số, tổng năng lượng có bị thay đổi hay không?"
- Cho sinh viên kiểm tra đẳng thức Parseval trên một tổng hữu hạn ngắn trước khi phát biểu dạng tổng quát.
- Đặt câu hỏi cho cả lớp: "Nếu các hệ số Fourier giảm nhanh, điều đó nói gì về năng lượng của phần đuôi phổ?"
- Tổ chức hoạt động vận dụng định lý Parseval để tính một tổng vô hạn như $$ \sum \frac{1}{n^2} $$.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên nhấn mạnh trực giác năng lượng và biểu đồ cột phổ trước khi đi vào chứng minh. Hiểu rõ ý nghĩa vật lý của đẳng thức thường quan trọng hơn việc ghi nhớ ngay hằng số chuẩn hóa ở lần học đầu tiên.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên đối chiếu định lý Parseval với định lý Pythagoras trong không gian vô hạn chiều, hoặc tìm hiểu dạng phức của Parseval làm bước đệm sang biến đổi Fourier.

## Tóm tắt dễ nhớ

Định lý Parseval khẳng định rằng năng lượng của hàm trong miền gốc bằng tổng năng lượng của các mode Fourier. Phép khai triển Fourier không làm mất năng lượng mà chỉ phân bố lại năng lượng theo từng tần số, tạo cầu nối trực tiếp giữa phân tích phổ và chuẩn $$ L^2 $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bảo toàn năng lượng của tín hiệu
- Bài toán: Xác định cách năng lượng của tín hiệu được phân bố giữa các họa âm.
- Mô hình Parseval:
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}\lvert f(x)\rvert^2\,dx
=
\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
$$
- Giả thiết và giới hạn: Đẳng thức hiểu theo chuẩn $$ L^2 $$; không đòi hỏi tín hiệu phải hội tụ từng điểm ở mọi nơi.
- Diễn giải: Năng lượng toàn phần trong miền gốc bằng đúng tổng năng lượng phổ.

#### Sai số cắt chuỗi trong mô phỏng số
- Bài toán: Đánh giá phần năng lượng bị mất khi bỏ qua các mode tần số cao.
- Mô hình:
$$
\lVert f-S_N\rVert_{L^2}^2
=
\pi\sum_{n=N+1}^{\infty}(a_n^2+b_n^2).
$$
- Giả thiết và giới hạn: Sai số được đo trong chuẩn bình phương khả tích.
- Diễn giải: Đuôi phổ biểu thị trực tiếp năng lượng sai số còn lại.

### 2. Trực giác bổ sung và các kết nối

Định lý Parseval cho thấy chuỗi Fourier không chỉ phân rã hình dạng mà còn phân rã năng lượng. Bình phương mỗi hệ số không phải là phép biến đổi hình thức, mà biểu thị đúng phần đóng góp năng lượng của mode tương ứng. Nội dung này đồng thời là cầu nối sang biến đổi Fourier.

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

Với hàm số
$$ f(x)=x,\qquad -\pi<x<\pi, $$
ta có
$$ b_n=\frac{2(-1)^{n+1}}{n},\qquad a_n=0. $$
Áp dụng định lý Parseval:
$$
\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx
=
\sum_{n=1}^{\infty}\frac{4}{n^2}.
$$
Từ đó suy ra
$$ \sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Phát biểu định lý Parseval, vận dụng để tính tổng vô hạn và ước lượng sai số phổ.

**Bậc sau đại học.** Nhấn mạnh chuẩn $$ L^2 $$, tính đẳng cự của ánh xạ Fourier và góc nhìn không gian Hilbert.

## Video tham khảo

- Xem trước: [Parseval's Theorem](https://www.youtube.com/watch?v=ML0eYMyhqOs) — Steve Brunton, tiếng Anh. Trình bày định lý Parseval và ý nghĩa năng lượng chứa trong các hệ số Fourier.
- [Parseval's Identity, Fourier Series, and Solving this Classic Pi Formula](https://www.youtube.com/watch?v=WPeU34jndSw) — Dr. Trefor Bazett, tiếng Anh. Vận dụng đẳng thức Parseval để tính một tổng chuỗi cổ điển liên quan đến số $$ \pi $$.
- [Parseval's Theorem (Fourier series engineering mathematics)](https://www.youtube.com/watch?v=1qkqCTwYoqU) — blackpenredpen, tiếng Anh. Thực hành tính toán trực tiếp đẳng thức Parseval cho một chuỗi Fourier.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
