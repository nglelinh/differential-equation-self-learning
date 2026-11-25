---
layout: post
title: "00-02 Tính liên tục và Tính liên tục đều"
chapter: '00'
order: 2
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---


Cùng là hai hàm liên tục hoàn hảo trên $(0, 1)$, tại sao hàm $f(x) = x^2$ lại "ngoan ngoãn" để xấp xỉ số, còn $g(x) = 1/x$ lại khiến mọi lưới chia đều bước $h$ đều thất bại thảm hại khi tiến gần $0$? Ranh giới mỏng manh nhưng quyết định đó chính là **tính liên tục đều (uniform continuity)** và phiên bản mạnh hơn nữa của nó trong phương trình vi phân: **điều kiện Lipschitz**.

## Kiến thức cần nhớ: Bốn cấp độ "độ mượt" của hàm số

1. **Liên tục tại từng điểm (Pointwise Continuity)**:
   Độ rộng $\delta$ phụ thuộc vào **cả $\varepsilon$ lẫn vị trí $x_0$**; hàm có thể dốc đứng dần khi tiến ra biên miền mở.
2. **Liên tục đều (Uniform Continuity)**:
   Một giá trị $\delta(\varepsilon)$ duy nhất dùng chung cho **mọi điểm $x, y$** trên toàn miền; theo định lý Heine–Cantor, mọi hàm liên tục trên đoạn compact $[a, b]$ đều liên tục đều.
3. **Liên tục Lipschitz ($\vert f(x) - f(y)\vert \le L\vert x - y\vert$)**:
   Độ dốc cát tuyến bị chặn toàn cục bởi hằng số $L$—chính là điều kiện vàng đảm bảo nghiệm của $y' = f(t, y)$ là **duy nhất**!
4. **Cầu nối đến giải tích số**:
   Tính liên tục đều cho phép kiểm soát sai số toàn cục khi xấp xỉ tích phân Riemann hay rời rạc hóa phương trình vi phân trên lưới.

## Mục tiêu
Bài học này giúp sinh viên phân biệt tính liên tục điểm (cục bộ) với tính liên tục đều (toàn cục), hiểu mối liên hệ giữa tính compact và tính liên tục đều, đồng thời vận dụng các định lý liên quan khi khảo sát sự hội tụ của dãy hàm. Đây là kiến thức nền để tiếp cận các định lý tồn tại nghiệm trong lý thuyết phương trình vi phân.

## Kiến thức nền
Sinh viên cần nắm vững định nghĩa giới hạn và tính liên tục theo $$ \varepsilon $$–$$ \delta $$ từ bài trước, cùng các khái niệm cơ bản về tập mở, tập đóng và khoảng.

## Dẫn nhập
Ở bài trước, ta thấy tính liên tục trên một đoạn đóng đem lại nhiều kết quả thuận lợi. Tuy nhiên, trong nhiều bài toán ODE, ta phải làm việc trên các khoảng mở hoặc trên toàn bộ đường thẳng thực $$ \mathbb{R} $$. Khi đó, tính liên tục thông thường chưa đủ mà cần đến một điều kiện chặt hơn là tính liên tục đều.

Xét hàm $$ f(x) = x^2 $$ trên $$ \mathbb{R} $$. Đồ thị của hàm càng dốc khi $$ \lvert x \rvert $$ càng lớn: ở gần gốc tọa độ, đồ thị khá thoải, nhưng càng ra xa gốc, chỉ một bước dịch chuyển rất nhỏ theo phương ngang cũng làm giá trị hàm thay đổi lớn theo phương đứng. Do đó, với cùng một sai số $$ \varepsilon $$ cho trước, không tồn tại một giá trị $$ \delta $$ duy nhất dùng được tại mọi điểm $$ x \in \mathbb{R} $$. Đó chính là hiện tượng không liên tục đều.

### Giải thích: So sánh trực tiếp $\delta$ của $f(x) = x^2$ trên $[0, 1]$ và $g(x) = \frac{1}{x}$ trên $(0, 1)$ với $\varepsilon = 0{,}1$

1. **Với $f(x) = x^2$ trên $[0, 1]$ (Liên tục đều & Lipschitz)**:
   $$\vert x^2 - y^2\vert = \vert x + y\vert\,\vert x - y\vert \le 2\vert x - y\vert.$$
   Chọn duy nhất $\delta = \frac{\varepsilon}{2} = \mathbf{0{,}05}$ cho *mọi* điểm trên $[0, 1]$: hễ $\vert x - y\vert < 0{,}05$ thì chắc chắn $\vert x^2 - y^2\vert < 0{,}1$. Hằng số Lipschitz là $L = 2$.
2. **Với $g(x) = \frac{1}{x}$ trên $(0, 1)$ (Liên tục nhưng KHÔNG liên tục đều)**:
   Xét hai điểm rất gần nhau $x_n = \frac{1}{n}$ và $y_n = \frac{1}{n+1}$:
   - Khoảng cách đầu vào: $\vert x_n - y_n\vert = \frac{1}{n(n+1)} \to 0$ (ví dụ tại $n = 100$, khoảng cách chỉ là $0{,}000099$).
   - Khoảng cách đầu ra: $\left\vert \frac{1}{x_n} - \frac{1}{y_n}\right\vert = \vert n - (n+1)\vert = \mathbf{1} > 0{,}1$ với mọi $n$!
   Dù chọn $\delta$ bé đến đâu, gần $0$ luôn tồn tại cặp điểm lệch nhau $< \delta$ nhưng giá trị hàm nhảy vọt đúng $1$ đơn vị.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung bạn vẽ đồ thị trên giấy với một sai số cho phép $$ \varepsilon $$ theo chiều dọc. Với hàm liên tục đều, ta có thể chọn một độ rộng cố định $$ \delta $$ theo chiều ngang sao cho tại bất kỳ vị trí nào trên miền xác định, hai điểm cách nhau ít hơn $$ \delta $$ đều có giá trị hàm lệch nhau ít hơn $$ \varepsilon $$. Ngược lại, với hàm không liên tục đều như $$ x^2 $$, càng ra xa gốc tọa độ ta càng phải thu hẹp bước ngang $$ \delta $$ để giữ sai số dọc trong mức $$ \varepsilon $$.

### Cách nhìn hình ảnh
So sánh đồ thị của $$ f(x) = x^2 $$ trên $$ \mathbb{R} $$ (minh họa trên $$ [-3,3] $$) và $$ f(x) = \sqrt{x} $$ trên $$ [0,1] $$. Với $$ f(x) = x^2 $$, khi $$ \lvert x \rvert $$ tăng, đường cong ngày càng dựng đứng nên với $$ \varepsilon = 0.5 $$, không có một giá trị $$ \delta $$ cố định nào áp dụng được cho mọi $$ x \in \mathbb{R} $$. Với $$ f(x) = \sqrt{x} $$ trên $$ [0,1] $$, dù độ dốc lớn gần $$ x = 0 $$, ta vẫn có thể chọn một giá trị $$ \delta $$ duy nhất phụ thuộc vào $$ \varepsilon $$, cụ thể là $$ \delta = \varepsilon^2 $$, dùng được trên toàn bộ đoạn $$ [0,1] $$.

### Cách nhìn hình thức
**Liên tục tại điểm $$ x_0 $$**: Với mọi $$ \varepsilon > 0 $$, tồn tại $$ \delta > 0 $$ sao cho $$ \lvert x - x_0 \rvert < \delta $$ kéo theo $$ \lvert f(x) - f(x_0) \rvert < \varepsilon $$. Ở đây, $$ \delta $$ có thể phụ thuộc vào cả $$ \varepsilon $$ và $$ x_0 $$.

**Liên tục đều trên tập $$ A $$**: Với mọi $$ \varepsilon > 0 $$, tồn tại $$ \delta > 0 $$ chỉ phụ thuộc vào $$ \varepsilon $$ (không phụ thuộc vào vị trí điểm) sao cho với mọi $$ x, y \in A $$, điều kiện $$ \lvert x - y \rvert < \delta $$ kéo theo $$ \lvert f(x) - f(y) \rvert < \varepsilon $$.

**Định lý Heine–Cantor**: Nếu $$ f $$ liên tục trên tập compact $$ K $$, thì $$ f $$ liên tục đều trên $$ K $$.

## Những ngộ nhận thường gặp
- "Liên tục đều chỉ là cách nói nhấn mạnh của liên tục." Sai. Trên $$ \mathbb{R} $$, một hàm liên tục chưa chắc liên tục đều; đây là hai tính chất khác nhau về bản chất (cục bộ so với toàn cục).
- "Nếu $$ f $$ liên tục tại mọi điểm của miền thì $$ f $$ liên tục đều trên miền đó." Sai. Phản ví dụ quen thuộc là $$ f(x) = x^2 $$ trên $$ \mathbb{R} $$.
- "Chỉ cần chọn $$ \delta $$ đủ nhỏ tại từng điểm là đủ." Sai. Trong định nghĩa liên tục đều, một giá trị $$ \delta $$ duy nhất phải đúng đồng thời cho mọi cặp điểm $$ x, y $$ trong miền xác định.
- "Hàm liên tục đều thì đạo hàm phải bị chặn." Sai. Hàm $$ f(x) = \sqrt{x} $$ liên tục đều trên $$ [0,1] $$, nhưng đạo hàm $$ f'(x) = \frac{1}{2\sqrt{x}} $$ không bị chặn khi $$ x \to 0^+ $$.

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt hai định nghĩa
Đặt định nghĩa liên tục và liên tục đều cạnh nhau để so sánh thứ tự lượng từ. Trong định nghĩa liên tục đều, mệnh đề "tồn tại $$ \delta $$" đứng trước "với mọi $$ x, y \in A $$", nghĩa là cùng một $$ \delta $$ phải đáp ứng trên toàn bộ tập $$ A $$.

### Bước 2: Chứng minh không liên tục đều
Rèn luyện kỹ thuật phản chứng: giả sử hàm liên tục đều rồi chọn hai dãy $$ \left(x_n\right) $$ và $$ \left(y_n\right) $$ sao cho $$ \lvert x_n - y_n \rvert \to 0 $$ nhưng $$ \lvert f(x_n) - f(y_n) \rvert \not\to 0 $$. Đây là phương pháp tiêu chuẩn để bác bỏ tính liên tục đều.

### Bước 3: Áp dụng định lý Heine–Cantor
Hiểu vai trò của tính compact trong việc chuyển tính liên tục điểm thành tính liên tục đều. Trên tập compact, hàm không thể "chạy ra vô cực" hay có hành vi biến thiên đột ngột không kiểm soát như trên khoảng mở hoặc trên toàn $$ \mathbb{R} $$.

### Các checkpoint
- Bạn có phân biệt được tính liên tục và tính liên tục đều thông qua định nghĩa không?
- Bạn có chứng minh được $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$ không?
- Bạn có vận dụng được định lý Heine–Cantor vào các bài toán cụ thể không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Chứng minh $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$
Giả sử $$ f $$ liên tục đều trên $$ \mathbb{R} $$. Khi đó, với $$ \varepsilon = 1 $$, tồn tại $$ \delta > 0 $$ sao cho $$ \lvert x - y \rvert < \delta $$ kéo theo $$ \lvert x^2 - y^2 \rvert < 1 $$. Chọn $$ x = n + \delta/2 $$ và $$ y = n $$ với $$ n \in \mathbb{N} $$. Ta có $$ \lvert x - y \rvert = \delta/2 < \delta $$, nhưng

$$
\lvert x^2 - y^2 \rvert = \lvert (n + \delta/2)^2 - n^2 \rvert = \lvert n\delta + \delta^2/4 \rvert \to \infty
$$

khi $$ n \to \infty $$. Với $$ n $$ đủ lớn, ta có $$ \lvert x^2 - y^2 \rvert \ge 1 $$, mâu thuẫn với giả thiết. Vậy $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$.

### Ví dụ 2: $$ f(x) = \sqrt{x} $$ liên tục đều trên $$ [0,1] $$
Với mọi $$ x, y \in [0,1] $$, giả sử $$ x \le y $$. Ta có

$$
\lvert \sqrt{x} - \sqrt{y} \rvert = \frac{y - x}{\sqrt{x} + \sqrt{y}} \le \sqrt{\lvert x - y \rvert}.
$$

Do đó, với mọi $$ \varepsilon > 0 $$, chỉ cần chọn $$ \delta = \varepsilon^2 $$, thì $$ \lvert x - y \rvert < \delta $$ suy ra $$ \lvert \sqrt{x} - \sqrt{y} \rvert < \varepsilon $$. Vậy hàm liên tục đều trên $$ [0,1] $$.

### Ví dụ 3: $$ f(x) = 1/x $$ không liên tục đều trên $$ \left(0,1\right) $$
Giả sử $$ f $$ liên tục đều trên $$ \left(0,1\right) $$. Với $$ \varepsilon = 1 $$, tồn tại $$ \delta > 0 $$ thỏa định nghĩa; không mất tính tổng quát, giả sử $$ \delta < 1 $$. Chọn $$ x = \delta/2 $$ và $$ y = \delta/4 $$, cả hai đều thuộc $$ \left(0,1\right) $$. Khi đó $$ \lvert x - y \rvert = \delta/4 < \delta $$, nhưng

$$
\lvert 1/x - 1/y \rvert = \lvert 2/\delta - 4/\delta \rvert = 2/\delta > 1,
$$

dẫn đến mâu thuẫn. Vậy $$ f(x) = 1/x $$ không liên tục đều trên $$ \left(0,1\right) $$.

### Ví dụ 4: Dùng định lý Heine–Cantor
Hàm $$ f(x) = \sin(x^2) $$ liên tục trên đoạn $$ [-10,10] $$, là một tập compact. Theo định lý Heine–Cantor, $$ f $$ liên tục đều trên $$ [-10,10] $$. Đây là cách nhanh gọn để khẳng định tính liên tục đều mà không cần tìm $$ \delta $$ tường minh.

### Ví dụ 5: Áp dụng trong ODE
Xét phương trình $$ y' = f(y) $$ với $$ f $$ liên tục đều trên $$ \mathbb{R} $$. Tính liên tục đều giúp kiểm soát đồng đều độ biến thiên của vế phải trên toàn miền khi phân tích các dãy hàm xấp xỉ, là cơ sở gần gũi với các điều kiện chính quy (như điều kiện Lipschitz) trong định lý Picard–Lindelöf.

## Câu hỏi khái niệm
1. Vì sao trong định nghĩa liên tục đều, $$ \delta $$ không được phụ thuộc vào điểm $$ x_0 $$? Điều này đảm bảo tính chất gì cho hàm số?
2. Định lý Heine–Cantor khẳng định hàm liên tục trên tập compact thì liên tục đều. Về mặt hình học, vì sao tập compact ngăn cản hiện tượng độ dốc tăng không kiểm soát?
3. Trong lý thuyết ODE, vì sao tính liên tục đều thường hữu ích hơn so với tính liên tục đơn thuần?

## Bài toán ứng dụng
1. **Kỹ thuật**: Một cảm biến đo nhiệt độ có đầu ra tuyến tính $$ V = kT $$ ở vùng nhiệt độ thấp, nhưng độ nhạy giảm dần khi nhiệt độ cao. Hãy mô hình hóa bằng một hàm bão hòa và thảo luận tính liên tục đều trên dải đo.
2. **Tài chính**: Hàm giá cổ phiếu $$ S(t) $$ thường được mô hình hóa là liên tục theo thời gian, nhưng biến động mạnh quanh các thời điểm công bố tin tức có thể làm phá vỡ tính liên tục đều trên miền vô hạn. Hãy thảo luận ý nghĩa của nhận xét này.
3. **Sinh học**: Tốc độ phản ứng enzyme $$ E(c) $$ theo nồng độ cơ chất $$ c $$ tuân theo dạng bão hòa Michaelis–Menten. Hãy phân tích tính liên tục đều của hàm này trên $$ [0,\infty) $$.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Thử $$ \delta $$"**: Chiếu đồ thị hàm $$ f(x) = 1/x $$ và yêu cầu sinh viên tìm $$ \delta $$ ứng với $$ \varepsilon = 0.5 $$ tại các điểm $$ x_0 = 0.1, 0.01, 0.001 $$. Qua việc thấy $$ \delta $$ nhỏ dần về $$ 0 $$, sinh viên tự rút ra kết luận không tồn tại $$ \delta $$ dùng chung.
- **Thảo luận nhóm**: Giao cho mỗi nhóm một hàm số để chứng minh hoặc bác bỏ tính liên tục đều, sau đó trình bày để các nhóm khác phản biện.
- **Câu đố nhanh**: "Trong các hàm $$ x^3 $$, $$ 1/(1+x^2) $$ và $$ \sin(x^2) $$, hàm nào liên tục đều trên $$ \mathbb{R} $$?" Yêu cầu giải thích ngắn gọn trong 30 giây.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Minh họa bằng nhiều đồ thị trực quan trước khi chuyển sang lập luận $$ \varepsilon $$–$$ \delta $$.
- Dùng quy trình kiểm tra hai bước: (1) kiểm tra miền có compact không để áp dụng Heine–Cantor; (2) nếu không compact, thử dùng phản chứng bằng hai dãy để kiểm tra khả năng không liên tục đều.
- Luyện tập trước với các hàm quen thuộc như $$ x $$, $$ x^2 $$, $$ 1/x $$ trên các miền khác nhau.

### Thử thách cho sinh viên khá giỏi
- Chứng minh định lý Heine–Cantor bằng phương pháp phản chứng kết hợp định lý Bolzano–Weierstrass.
- Tìm hiểu khái niệm mô-đun liên tục (modulus of continuity) và ứng dụng trong lý thuyết xấp xỉ hàm.
- So sánh tính liên tục đều với điều kiện Lipschitz và phân tích vai trò của hai điều kiện này trong ODE.

## Tóm tắt dễ nhớ
- **Liên tục**: $$ \delta $$ phụ thuộc vào cả $$ \varepsilon $$ và điểm $$ x_0 $$.
- **Liên tục đều**: $$ \delta $$ chỉ phụ thuộc vào $$ \varepsilon $$, không phụ thuộc vào vị trí điểm.
- **Heine–Cantor**: Liên tục trên tập compact $$ \Rightarrow $$ liên tục đều.
- **Phản chứng**: Chọn hai dãy có $$ \lvert x_n - y_n \rvert \to 0 $$ nhưng $$ \lvert f(x_n) - f(y_n) \rvert \not\to 0 $$.
- Trong ODE, tính liên tục đều giúp kiểm soát đồng đều độ biến thiên của vế phải trên miền xét.

## Video tham khảo

- Xem trước: [This is the Epsilon Delta Definition of Continuity | Real Analysis](https://www.youtube.com/watch?v=O98eOlHyWmQ) — Wrath of Math, tiếng Anh. Trình bày một chứng minh $$ \varepsilon $$–$$ \delta $$ cho tính liên tục, đúng với định nghĩa được sử dụng trong bài.
- [Limits, L'Hôpital's rule, and epsilon delta definitions | Chapter 7, Essence of calculus](https://www.youtube.com/watch?v=kfF40MiS7zA) — 3Blue1Brown, tiếng Việt. Diễn giải giới hạn và tính liên tục như bài toán khống chế sai số bằng $$ \delta $$.
- [Metric Spaces 8: Cauchy Sequences](https://www.youtube.com/watch?v=UhEaX-uctnM) — Math at Andrews University, tiếng Anh. Trình bày dãy Cauchy trong không gian metric và cách khống chế khoảng cách liên quan mật thiết đến tính liên tục đều.

## Tài liệu tham khảo
- Rudin — *Principles of Mathematical Analysis*: chương 4 trình bày chi tiết về tính liên tục đều.
- Apostol — *Mathematical Analysis*: cung cấp nhiều ví dụ và bài tập luyện tập.
- Hirsch, Smale & Devaney — *Differential Equations, Dynamical Systems, and an Introduction to Chaos*: liên hệ trực tiếp với lý thuyết ODE.
