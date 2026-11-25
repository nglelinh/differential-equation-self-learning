---
layout: post
title: "Sự Hội Tụ của Chuỗi Fourier"
chapter: '08'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---

![21 02 25 08 03 Convergence Fourier Series]({{ site.imgurl }}/chapter_img/chapter08/03_convergence_fourier_series.svg)

Tính xong công thức chuỗi Fourier mới là bước một; câu hỏi quyết định trong giải tích là: **chuỗi vô hạn đó có thực sự hội tụ về đúng $f(x)$ không, hội tụ nhanh cỡ nào, và chuyện gì xảy ra ngay tại điểm đứt đoạn?** Định lý Dirichlet và Hiện tượng Gibbs trả lời trọn vẹn mọi hành vi tinh tế đó!

## Kiến thức cần nhớ: Bốn quy luật vàng về Sự Hội tụ của Chuỗi Fourier

1. **Định lý Hội tụ Từng điểm của Dirichlet**:
   Nếu $f$ trơn từng khúc trên $[-L, L]$, thì chuỗi Fourier hội tụ tại **mọi điểm $x$** về đúng trung bình cộng hai giới hạn trái–phải:
   $$S(x) = \frac{f(x^+) + f(x^-)}{2}.$$
   (Tại điểm liên tục thì $S(x) = f(x)$; tại điểm nhảy thì $S(x)$ rơi đúng vào **trung điểm** của bước nhảy!).
2. **Độ trơn của $f$ quyết định tốc độ suy giảm của hệ số $a_n, b_n$**:
   - $f$ có bước nhảy gián đoạn → hệ số giảm chậm $O(1/n)$ (hội tụ không đều).
   - $f$ liên tục tuần hoàn nhưng có góc gãy ($f'$ gián đoạn, như sóng tam giác) → hệ số giảm nhanh $O(1/n^2)$ (hội tụ đều tuyệt đối!).
   - $f \in C^k$ tuần hoàn → hệ số giảm $O(1/n^{k+1})$.
3. **Hiện tượng Gibbs (Vọt lố $\approx 8{,}95\%$ tại bước nhảy)**:
   Gần điểm gián đoạn, tổng riêng $S_N(x)$ luôn có một đỉnh nhọn vượt quá chiều cao bước nhảy một lượng tiến về $\frac{1}{\pi}\int_0^\pi \frac{\sin t}{t}\,dt - \frac{1}{2} \approx \mathbf{8{,}95\%}$ của độ cao bước nhảy—không bao giờ biến mất dù $N \to \infty$ (chỉ co hẹp bề ngang về 0)!
4. **Hội tụ trong $L^2$ (Bình phương trung bình)**:
   Với mọi hàm năng lượng hữu hạn ($\int \vert f \vert^2 < \infty$), sai số năng lượng $\int \vert f - S_N \vert^2 \to 0$ ngay cả khi tồn tại điểm gián đoạn.

## Mục tiêu

Bài học này trả lời câu hỏi trọng tâm sau khi đã xây dựng được chuỗi Fourier: chuỗi đó hội tụ theo nghĩa nào, trong điều kiện nào và hội tụ về giá trị nào. Sau bài học, sinh viên cần nắm phát biểu và trực giác của định lý Dirichlet, phân biệt được hội tụ từng điểm, hội tụ đều và hội tụ trong $$ L^2 $$, hiểu hiện tượng Gibbs và nhận ra vì sao trong PDE người ta đặc biệt quan tâm đến hội tụ theo năng lượng.

## Kiến thức nền

Sinh viên cần nắm chuỗi Fourier, cách tính hệ số Fourier và các khái niệm hội tụ cơ bản của chuỗi hàm ở mức trực giác. Vì đây là bài học giàu tính khái niệm, việc kết hợp hình ảnh minh họa và ví dụ cụ thể sẽ giúp giảm bớt cảm giác trừu tượng.

## Dẫn nhập

Khi viết

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr),
$$

một câu hỏi tự nhiên được đặt ra: tổng vô hạn này có thực sự hội tụ về hàm ban đầu hay không, và nếu có thì theo nghĩa nào — từng điểm, đều hay theo năng lượng? Đây không chỉ là vấn đề kỹ thuật thuần túy, mà quyết định khi nào chuỗi Fourier là một biểu diễn chính xác của tín hiệu và khi nào cần hiểu nó như một phép xấp xỉ theo một chuẩn thích hợp.

Bài học này giúp sinh viên hình thành tư duy chặt chẽ hơn về biểu diễn hàm. Không phải mọi chuỗi vô hạn đều hội tụ theo cùng một cách, và trong lý thuyết Fourier, mỗi kiểu hội tụ phản ánh một tính chất khác nhau của hàm.

### Giải thích: Áp dụng Định lý Dirichlet tại 3 điểm đặc biệt của hàm bậc thang

Xét hàm tuần hoàn chu kỳ $2\pi$ xác định trên $(-\pi, \pi]$ bởi $f(x) = \begin{cases} 0, & -\pi < x < 0, \\ 4, & 0 \le x \le \pi. \end{cases}$
Hãy dùng Định lý Dirichlet dự đoán **chính xác** giá trị hội tụ $S(x)$ mà không cần tính một tích phân nào:
- **Tại $x = \pi/2$** (điểm liên tục): $S(\pi/2) = f(\pi/2) = \mathbf{4}$.
- **Tại $x = 0$** (điểm nhảy nội): $f(0^-) = 0$, $f(0^+) = 4 \implies S(0) = \frac{0 + 4}{2} = \mathbf{2}$ (dù đề định nghĩa $f(0) = 4$!).
- **Tại $x = \pi$** (điểm biên tuần hoàn!): Bên trái $f(\pi^-) = 4$; bên phải nhờ tính tuần hoàn $f(\pi^+) = f(-\pi^+) = 0 \implies S(\pi) = \frac{4 + 0}{2} = \mathbf{2}$!
- **Đỉnh Gibbs dự kiến** sát $x = 0^+$: độ cao bước nhảy là $4 - 0 = 4$, nên đỉnh vọt lố sẽ đạt khoảng $4 + 0{,}0895 \times 4 \approx \mathbf{4{,}36}$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi sử dụng ngày càng nhiều mode để tái tạo hàm gốc, ta kỳ vọng tổng riêng sẽ ngày càng gần với hàm hơn. Tuy nhiên, "gần hơn" có thể được hiểu theo nhiều nghĩa. Có trường hợp đồ thị gần như trùng khớp ở hầu hết mọi điểm nhưng vẫn dao động mạnh tại chỗ có bước nhảy; có trường hợp sai số tại một số điểm không giảm đều nhưng năng lượng sai số tổng thể lại tiến về 0. Nghiên cứu sự hội tụ Fourier là việc phân biệt rạch ròi các kiểu tiệm cận này.

### Cách nhìn hình ảnh

Với một hàm liên tục và trơn, các tổng riêng Fourier bám sát đồ thị gốc khá đều. Ngược lại, với hàm có bước nhảy, các tổng riêng sẽ dao động mạnh quanh điểm gián đoạn. Biên độ vượt quá của dao động này không triệt tiêu khi số hạng tăng lên mà chỉ co hẹp dần về sát điểm nhảy. Đây chính là hiện tượng Gibbs, minh họa rõ ràng sự khác biệt giữa hội tụ từng điểm và hội tụ theo năng lượng.

### Cách nhìn hình thức

Gọi $$ S_N(x) $$ là tổng riêng Fourier bậc $$ N $$. Ta đặt ba câu hỏi khác nhau:

- Liệu $$ S_N(x)\to f(x) $$ tại từng điểm hay không?
- Liệu $$ \sup_x \lvert S_N(x)-f(x)\rvert\to 0 $$ hay không?
- Liệu $$ \lVert S_N-f\rVert_{L^2}\to 0 $$ hay không?

Ba kiểu hội tụ này không tương đương nhau.

## Những ngộ nhận thường gặp

- "Nếu chuỗi Fourier tồn tại thì nó phải hội tụ đúng về giá trị hàm tại mọi điểm." Sai; tại điểm gián đoạn, chuỗi thường hội tụ về trung bình cộng hai giới hạn một phía.
- "Dao động Gibbs chứng tỏ chuỗi Fourier không hiệu quả." Không đúng; chuỗi Fourier vẫn hội tụ chính xác theo nhiều nghĩa quan trọng, đặc biệt là hội tụ trong $$ L^2 $$.
- "Hội tụ từng điểm luôn là tiêu chuẩn quan trọng nhất." Không hẳn; trong PDE và cơ học, hội tụ trong $$ L^2 $$ thường phù hợp hơn với đại lượng năng lượng.
- "Càng lấy nhiều số hạng thì vùng gần điểm nhảy càng hết dao động." Sai; độ vượt quá cực đại không tiến về 0 mà chỉ co hẹp vào một lân cận nhỏ hơn quanh điểm nhảy.

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt các kiểu hội tụ

Sinh viên cần nhận thức rằng khái niệm "hội tụ" không chỉ có một nghĩa duy nhất.

### Bước 2: Tìm hiểu định lý Dirichlet

Đây là kết quả định hướng cơ bản cho sự hội tụ từng điểm của chuỗi Fourier.

### Bước 3: Quan sát hiện tượng Gibbs

Đây là nội dung mang tính trực quan rõ nét nhất của bài học.

### Bước 4: Liên hệ với hội tụ $$ L^2 $$ và năng lượng

Bước này giúp sinh viên hiểu vì sao chuỗi Fourier vẫn hữu ích trong PDE ngay cả khi xuất hiện dao động cục bộ.

### Các điểm kiểm tra

- Sinh viên có phân biệt được hội tụ từng điểm và hội tụ trong $$ L^2 $$ hay không.
- Sinh viên có biết chuỗi Fourier hội tụ về giá trị nào tại điểm gián đoạn hay không.
- Sinh viên có giải thích được hiện tượng Gibbs bằng lời hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Định lý Dirichlet cho hàm bước

Xét hàm tuần hoàn xác định trên $$ (-\pi,\pi) $$ bởi

$$
f(x)=
\begin{cases}
0, & x<0,\\
1, & x>0.
\end{cases}
$$

Tại $$ x=0 $$, chuỗi Fourier hội tụ về

$$
\frac{f(0^-)+f(0^+)}{2}
=
\frac{0+1}{2}
=
\frac{1}{2}.
$$

Ví dụ này minh họa quy tắc lấy trung bình hai phía của chuỗi Fourier tại điểm gián đoạn.

### Ví dụ 2: Hàm liên tục và trơn

Nếu

$$ f(x)=\cos x + \frac{1}{2}\sin 2x, $$

thì chuỗi Fourier của hàm là một tổng hữu hạn ngay từ đầu, do đó hội tụ đúng về $$ f(x) $$ tại mọi điểm. Ví dụ này nhấn mạnh rằng các hiện tượng phức tạp về hội tụ chủ yếu phát sinh khi hàm không trơn hoặc có điểm gián đoạn.

### Ví dụ 3: Hàm trị tuyệt đối

Với $$ f(x)=\lvert x\rvert $$ trên $$ (-\pi,\pi) $$, hàm liên tục nhưng không khả vi tại $$ x=0 $$. Chuỗi Fourier vẫn hội tụ từng điểm về $$ \lvert x\rvert $$, nhưng các hệ số giảm chậm hơn so với các hàm có bậc trơn cao hơn. Ví dụ này cho thấy mối liên hệ trực tiếp giữa độ trơn của hàm và tốc độ suy giảm của hệ số Fourier.

### Ví dụ 4: Hiện tượng Gibbs

Xét lại hàm sóng vuông. Khi vẽ các tổng riêng đầu tiên, ta thấy xuất hiện các đỉnh vượt quá gần điểm nhảy. Khi tăng số hạng, vùng dao động co hẹp lại nhưng biên độ vượt quá không tiến về 0. Đây là minh họa trực quan cho thấy hội tụ từng điểm gần điểm gián đoạn có những đặc điểm riêng biệt.

## Câu hỏi khái niệm

1. Vì sao tại điểm gián đoạn, chuỗi Fourier lại hội tụ về trung bình hai phía thay vì chọn giá trị bên trái hoặc bên phải?
2. Vì sao một chuỗi có thể hội tụ tốt trong $$ L^2 $$ nhưng vẫn có dao động cục bộ đáng kể tại một số điểm?
3. Độ trơn của hàm ảnh hưởng như thế nào đến tốc độ suy giảm của các hệ số Fourier?

## Bài toán ứng dụng

1. Trong xử lý tín hiệu số, vì sao việc tái tạo một tín hiệu có cạnh sắc thường tạo ra dao động quanh cạnh?
2. Trong PDE, vì sao hội tụ theo năng lượng thường được ưu tiên hơn hội tụ từng điểm?
3. Trong bài toán truyền nhiệt với nhiệt độ ban đầu có bước nhảy, vì sao chuỗi Fourier vẫn là công cụ phù hợp dù có hiện tượng Gibbs tại thời điểm đầu?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Nếu hàm có bước nhảy, chuỗi Fourier sẽ nhận giá trị nào ngay tại điểm nhảy?"
- Vẽ hoặc mô tả lần lượt các tổng riêng của sóng vuông để sinh viên quan sát hiện tượng Gibbs.
- Cho lớp phân loại một số phát biểu thành hội tụ từng điểm, hội tụ đều hoặc hội tụ $$ L^2 $$.
- Khuyến khích sinh viên diễn đạt bằng lời: chuỗi Fourier chính xác theo nghĩa nào và có hạn chế ở nghĩa nào.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên ưu tiên trực giác đồ thị và ví dụ hàm bước trước khi giới thiệu phát biểu định lý Dirichlet. Hình ảnh hình học của hiện tượng Gibbs thường là điểm tựa dễ nhớ để hiểu phần lý thuyết.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu vai trò của hạt nhân Dirichlet hoặc phân tích định lượng mối liên hệ giữa độ trơn của hàm và tốc độ suy giảm của hệ số Fourier, qua đó mở hướng sang giải tích điều hòa.

## Tóm tắt dễ nhớ

Chuỗi Fourier có nhiều kiểu hội tụ khác nhau. Tại điểm liên tục, chuỗi thường hội tụ về đúng giá trị của hàm; tại điểm nhảy, chuỗi hội tụ về trung bình cộng hai giới hạn một phía. Trong nhiều bài toán PDE, hội tụ trong $$ L^2 $$ và cấu trúc năng lượng là tiêu chí trọng tâm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tái tạo tín hiệu không trơn
- Bài toán: Xấp xỉ một tín hiệu tuần hoàn có góc nhọn hoặc điểm gián đoạn bằng tổng hữu hạn các mode.
- Mô hình:
$$
S_N(x)=\frac{a_0}{2}+\sum_{n=1}^{N}\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$
- Giả thiết và giới hạn: Sự hội tụ từng điểm phụ thuộc vào độ trơn và bản chất điểm gián đoạn của hàm.
- Diễn giải: Chuỗi Fourier có thể hội tụ tốt theo chuẩn năng lượng ngay cả khi hội tụ từng điểm diễn ra chậm.

#### Xử lý ảnh và tín hiệu
- Bài toán: Giải thích nguyên nhân vùng biên hoặc cạnh sắc sinh ra hiện tượng rung phổ khi cắt cụt chuỗi.
- Mô hình: Phân tích sự hội tụ và hiện tượng Gibbs đối với tín hiệu có bước nhảy.
- Giả thiết và giới hạn: Mô hình một chiều là phiên bản đơn giản hóa của bài toán nhiều chiều.
- Diễn giải: Hiện tượng Gibbs cho thấy các mode tần số cao đóng vai trò cần thiết quanh điểm gián đoạn.

### 2. Trực giác bổ sung và các kết nối

Nghiên cứu hội tụ Fourier không chỉ là kiểm tra xem chuỗi có tiến về hàm gốc hay không, mà còn phải xác định hội tụ theo chuẩn nào: từng điểm, đều hay $$ L^2 $$. Một nhầm lẫn thường gặp là cho rằng hàm liên tục thì chuỗi Fourier luôn hội tụ đều; điều này không đúng nếu hàm không đủ trơn. Bài học này chuẩn bị nền tảng cho định lý Parseval và biến đổi Fourier bằng cách làm rõ ý nghĩa hội tụ trong không gian hàm.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 2000)
f = np.sign(x)

def partial_sum(x, N):
    s = np.zeros_like(x)
    for k in range(1, N + 1, 2):
        s += (4 / (np.pi * k)) * np.sin(k * x)
    return s

plt.plot(x, f, color="black", label="target")
for N in [3, 9, 25]:
    plt.plot(x, partial_sum(x, N), label=f"N={N}")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hien tuong Gibbs gan diem gian doan")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Gibbs phenomenon Fourier series
- search: pointwise vs L2 convergence Fourier
- search: Dirichlet theorem Fourier series visualization

### 5. Bài toán mẫu có bối cảnh thực

Với sóng vuông ở bài trước, chuỗi Fourier hội tụ về
$$ \frac{f(x^-)+f(x^+)}{2} $$
tại điểm gián đoạn $$ x=0 $$, nên giá trị giới hạn là $$ 0 $$ thay vì $$ \pm 1 $$. Đây là ví dụ tiêu chuẩn cho định lý Dirichlet, giúp sinh viên thấy rõ sự hội tụ của chuỗi Fourier khác với hội tụ từng điểm đơn giản.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm định lý Dirichlet cơ bản, hiểu sự hội tụ tại điểm liên tục và quy tắc trung bình hai phía tại điểm gián đoạn.

**Bậc sau đại học.** Tìm hiểu sâu về hội tụ trong $$ L^2 $$, định lý Carleson và mối liên hệ giữa độ trơn của hàm với tốc độ suy giảm của hệ số Fourier.

## Video tham khảo

- Xem trước: [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Minh họa các tổng riêng và dao động Gibbs, cung cấp bức tranh trực quan về sự hội tụ.
- [Lec 16 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=xWa5_OXI6VM) — MIT OpenCourseWare, tiếng Anh. Arthur Mattuck mở rộng chuỗi Fourier cho chu kỳ tổng quát và thảo luận các vấn đề hội tụ.
- [Lec 15 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=EWWw0jryj1A) — MIT OpenCourseWare, tiếng Anh. Bài giảng MIT giới thiệu cấu trúc chuỗi Fourier làm nền cho việc xét hội tụ.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
