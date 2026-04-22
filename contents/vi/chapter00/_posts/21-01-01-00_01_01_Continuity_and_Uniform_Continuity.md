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

## Mục tiêu
Bài học này giúp sinh viên phân biệt giữa liên tục cục bộ và liên tục đều toàn cục, hiểu sâu mối quan hệ giữa compactness và liên tục đều, và vận dụng các định lý trong việc khảo sát sự hội tụ của dãy hàm. Đây là nền tảng quan trọng để hiểu các định lý tồn tại trong lý thuyết phương trình vi phân.

## Kiến thức nền
Sinh viên cần nắm vững định nghĩa giới hạn và liên tục theo epsilon-delta từ bài trước. Kiến thức về tập mở, tập đóng, và khoảng cũng cần thiết. Nếu chưa vững, nên ôn lại trước khi tiếp tục.

## Dẫn nhập
Trong bài trước, ta đã thấy liên tục trên một đoạn đóng mang lại nhiều tính chất đẹp. Nhưng trong nhiều bài toán ODE, ta làm việc trên các khoảng mở hoặc trên toàn bộ đường thẳng thực. Khi đó, liên tục thông thường chưa đủ, ta cần phiên bản mạnh hơn: liên tục đều.

Hãy xem xét hàm $$ f(x) = x^2 $$ trên $$ \mathbb{R} $$. Đồ thị của nó càng dốc khi $$ x $$ càng lớn. Từ gốc tọa độ, ta có thể đi rất xa theo chiều ngang để đồ thị dâng lên một đơn vị theo chiều dọc. Điều này có nghĩa là không có một delta duy nhất nào hoạt động cho cùng một epsilon tại mọi điểm, đó là hiện tượng không liên tục đều.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy tưởng tượng ta đang vẽ đồ thị trên giấy với độ phóng đại cố định. Với hàm liên tục đều, ta có thể chọn một độ rộng đủ nhỏ, tức một $$ \delta $$, sao cho khi nén toàn bộ đồ thị theo chiều ngang với độ rộng đó, chiều cao của đồ thị cũng bị nén theo tương ứng, tức bởi $$ \varepsilon $$. Còn với hàm không liên tục đều như $$ x^2 $$, ở xa gốc, ta cần nén rất nhiều theo chiều ngang mới tạo ra một nén nhỏ theo chiều dọc.

### Cách nhìn hình ảnh
Vẽ đồ thị $$ f(x) = x^2 $$ trên $$ [-3,3] $$ và $$ f(x) = \sqrt{x} $$ trên $$ [0,1] $$. Với $$ f(x) = x^2 $$, khi $$ x $$ càng xa gốc, đường cong càng dựng đứng, nên ta không thể tìm được một $$ \delta $$ duy nhất cho cùng một giá trị $$ \varepsilon = 0.5 $$ mà hoạt động tại mọi $$ x $$. Ngược lại, với $$ f(x) = \sqrt{x} $$ trên $$ [0,1] $$, đường cong càng thoải khi $$ x $$ tăng, nên ta có thể chọn $$ \delta $$ cố định, chẳng hạn $$ \delta = \varepsilon^2 $$, và nó sẽ hoạt động trên toàn miền.

### Cách nhìn hình thức
**Liên tục tại điểm $$ x_0 $$**: Với mọi $$ \varepsilon > 0 $$, tồn tại $$ \delta > 0 $$ sao cho $$ \lvert x - x_0 \rvert < \delta $$ kéo theo $$ \lvert f(x) - f(x_0) \rvert < \varepsilon $$. Lưu ý: $$ \delta $$ phụ thuộc vào cả $$ \varepsilon $$ và $$ x_0 $$.

**Liên tục đều trên tập $$ A $$**: Với mọi $$ \varepsilon > 0 $$, tồn tại $$ \delta > 0 $$ chỉ phụ thuộc $$ \varepsilon $$, không phụ thuộc $$ x_0 $$, sao cho với mọi $$ x, y \in A $$, điều kiện $$ \lvert x - y \rvert < \delta $$ kéo theo $$ \lvert f(x) - f(y) \rvert < \varepsilon $$.

**Định lý Heine-Cantor**: Nếu f liên tục trên tập compact K, thì f liên tục đều trên K.

## Những ngộ nhận thường gặp
- "Liên tục đều chỉ là liên tục mạnh hơn một chút." Không đúng. Trên $$ \mathbb{R} $$, hàm liên tục chưa chắc đã liên tục đều. Đây là sự khác biệt về bản chất, không chỉ mức độ.
- "Nếu $$ f $$ liên tục tại mọi điểm thì $$ f $$ liên tục đều." Sai. Phản ví dụ: $$ f(x) = x^2 $$ trên $$ \mathbb{R} $$.
- "Delta chỉ cần đủ nhỏ là được." Không đúng. Với liên tục đều, delta phải hoạt động cho TẤT CẢ các cặp điểm trong miền, không chỉ cho một điểm cụ thể.
- "Hàm liên tục đều thì đạo hàm bị chặn." Không đúng. Hàm $$ f(x) = x^2 $$ liên tục đều trên $$ [0,1] $$ nhưng đạo hàm $$ 2x $$ không bị chặn bởi một hằng số cố định trên toàn $$ \mathbb{R} $$.

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt hai định nghĩa
So sánh trực tiếp định nghĩa liên tục và liên tục đều. Nhận xét: trong liên tục đều, vế "tồn tại $$ \delta $$" không có "với mọi $$ x_0 $$" ở đầu, tức là $$ \delta $$ phải đủ tốt cho toàn miền.

### Bước 2: Chứng minh không liên tục đều
Học kỹ thuật phản chứng: giả sử liên tục đều, chọn hai dãy $$ \left(x_n\right) $$, $$ \left(y_n\right) $$ với $$ \lvert x_n - y_n \rvert \to 0 $$ nhưng $$ \lvert f(x_n) - f(y_n) \rvert \not\to 0 $$. Đây là cách tiêu chuẩn để chứng minh một hàm không liên tục đều.

### Bước 3: Áp dụng định lý Heine-Cantor
Hiểu rằng compactness chính là "cơ chế" để biến liên tục thành liên tục đều. Tập compact "nén" mọi hướng vào, không cho phép "độ dốc tăng vô hạn" như trên $$ \mathbb{R} $$.

### Các checkpoint
- Sinh viên có phát biệt được liên tục và liên tục đều qua định nghĩa không?
- Sinh viên có chứng minh được $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$ không?
- Sinh viên có vận dụng được Heine-Cantor trong các bài toán cụ thể không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Chứng minh $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$
Giả sử $$ f $$ liên tục đều. Với $$ \varepsilon = 1 $$, tồn tại $$ \delta > 0 $$ sao cho $$ \lvert x - y \rvert < \delta $$ kéo theo $$ \lvert x^2 - y^2 \rvert < 1 $$. Chọn $$ x = n + \delta/2 $$, $$ y = n $$ với $$ n \in \mathbb{N} $$. Khi đó $$ \lvert x - y \rvert = \delta/2 < \delta $$, nhưng $$\lvert x^2 - y^2 \rvert = \lvert (n + \delta/2)^2 - n^2 \rvert = \lvert n\delta + \delta^2/4 \rvert \to \infty$$ khi $$ n \to \infty $$. Vậy với $$ n $$ đủ lớn, hiệu số sẽ lớn hơn $$ 1 $$, mâu thuẫn. Do đó $$ f(x) = x^2 $$ không liên tục đều trên $$ \mathbb{R} $$.

### Ví dụ 2: $$ f(x) = \sqrt{x} $$ liên tục đều trên $$ [0,1] $$
Với mọi $$ x, y \in [0,1] $$, giả sử $$ x \le y $$. Ta có

$$
\lvert \sqrt{x} - \sqrt{y} \rvert = \frac{y - x}{\sqrt{x} + \sqrt{y}} \le \sqrt{\lvert x - y \rvert}.
$$

Vậy với $$ \varepsilon > 0 $$, chọn $$ \delta = \varepsilon^2 $$, ta có $$ \lvert x - y \rvert < \delta $$ suy ra $$ \lvert \sqrt{x} - \sqrt{y} \rvert < \varepsilon $$. Do đó hàm liên tục đều trên $$ [0,1] $$.

### Ví dụ 3: $$ f(x) = 1/x $$ không liên tục đều trên $$ \left(0,1\right) $$
Giả sử liên tục đều. Với $$ \varepsilon = 1 $$, tồn tại $$ \delta > 0 $$. Chọn $$ x = \delta/2 $$, $$ y = \delta/4 $$ trong $$ \left(0,1\right) $$. Khi đó $$ \lvert x - y \rvert = \delta/4 < \delta $$, nhưng $$\lvert 1/x - 1/y \rvert = \lvert 2/\delta - 4/\delta \rvert = 2/\delta > 1$$ khi $$ \delta < 2 $$. Mâu thuẫn. Vậy hàm không liên tục đều trên $$ \left(0,1\right) $$.

### Ví dụ 4: Dùng Heine-Cantor
Hàm $$ f(x) = \sin(x^2) $$ liên tục trên $$ [-10,10] $$, là một tập compact. Theo Heine-Cantor, $$ f $$ liên tục đều trên $$ [-10,10] $$. Đây là cách hiệu quả để chứng minh liên tục đều mà không cần tìm delta trực tiếp.

### Ví dụ 5: Áp dụng trong ODE
Xét phương trình $$ y' = f(y) $$ với $$ f $$ liên tục đều trên $$ \mathbb{R} $$. Tính liên tục đều đảm bảo rằng khi ta dùng phương pháp xấp xỉ liên tiếp, các sai số không bị khuếch đại vô hạn. Đây là một trong các điều kiện trong định lý Picard-Lindelöf.

## Câu hỏi khái niệm
1. Tại sao trong định nghĩa liên tục đều, delta không được phụ thuộc vào điểm? Điều này đảm bảo tính chất gì cho hàm số?
2. Heine-Cantor nói rằng compact + liên tục = liên tục đều. Hãy giải thích ý nghĩa hình học: tại sao tập compact "ngăn cản" hiện tượng "độ dốc tăng vô hạn"?
3. Trong lý thuyết ODE, tại sao ta thường cần f liên tục đều hơn là chỉ liên tục?

## Bài toán ứng dụng
1. **Kỹ thuật**: Một cảm biến đo nhiệt độ với đầu ra $$ V = kT $$, nhưng ở nhiệt độ cao, độ nhạy giảm. Mô hình hóa bằng hàm bão hòa và thảo luận về liên tục đều trên dải đo.
2. **Tài chính**: Hàm giá cổ phiếu S(t) được mô hình là liên tục theo thời gian. Tuy nhiên, biến động mạnh gần thời điểm tin tức quan trọng có thể phá vỡ tính liên tục đều. Thảo luận ý nghĩa.
3. **Sinh học**: Nồng độ enzyme $$ E(c) $$ theo nồng độ $$ c $$ có dạng bão hòa Michaelis-Menten. Phân tích tính liên tục đều trên $$ [0,\infty) $$.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Thử delta"**: Chiếu đồ thị $$ f(x) = 1/x $$ và yêu cầu sinh viên tìm delta cho $$ \varepsilon = 0.5 $$ tại $$ x_0 = 0.1, 0.01, 0.001 $$. Quan sát delta phải nhỏ dần, từ đó nhận ra không có delta chung.
- **Thảo luận nhóm**: Cho mỗi nhóm một hàm và yêu cầu chứng minh hoặc bác bỏ liên tục đều. Các nhóm trình bày, các nhóm khác phản biện.
- **Câu đố nhanh**: "Hàm nào sau đây liên tục đều trên $$ \mathbb{R} $$: $$ x^3 $$, $$ 1/(1+x^2) $$, $$ \sin(x^2) $$?" Yêu cầu giải thích trong 30 giây.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Vẽ nhiều đồ thị trực quan hơn là chứng minh bằng epsilon-delta.
- Cung cấp checklist: "Bước 1: Kiểm tra miền có compact không $$ \Rightarrow $$ dùng Heine-Cantor. Bước 2: Nếu không compact $$ \Rightarrow $$ thử chứng minh không liên tục đều bằng phản chứng."
- Luyện tập với các hàm đơn giản trước: $$ x $$, $$ x^2 $$, $$ 1/x $$ trên các miền cụ thể.

### Thử thách cho sinh viên khá giỏi
- Chứng minh định lý Heine-Cortic (phiên bản yếu hơn của Heine-Cantor).
- Nghiên cứu và trình bày về modulus of continuity và ứng dụng trong lý thuyết hàm.
- So sánh liên tục đều với điều kiện Lipschitz, nhận xét mối quan hệ trong bối cảnh ODE.

## Tóm tắt dễ nhớ
**Liên tục**: Delta phụ thuộc $$ \varepsilon $$ và $$ x_0 $$.
**Liên tục đều**: Delta chỉ phụ thuộc $$ \varepsilon $$, không phụ thuộc $$ x_0 $$.
**Heine-Cantor**: Compact + liên tục $$ \Rightarrow $$ liên tục đều.
**Phản chứng**: Thường dùng hai dãy với $$ \lvert x_n - y_n \rvert \to 0 $$ nhưng $$ \lvert f(x_n) - f(y_n) \rvert \not\to 0 $$.
Trong ODE, liên tục đều giúp kiểm soát sai số không bị khuếch đại.

## Tài liệu tham khảo
- Rudin — *Principles of Mathematical Analysis*: chương 4 trình bày chi tiết về liên tục đều.
- Apostol — *Mathematical Analysis*: nhiều ví dụ và bài tập.
- Hirsch, Smale & Devaney — *Differential Equations, Dynamical Systems, and an Introduction to Chaos*: liên hệ với ODE.
