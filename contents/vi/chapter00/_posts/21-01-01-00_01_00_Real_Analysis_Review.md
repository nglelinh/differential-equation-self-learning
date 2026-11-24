---
layout: post
title: "00-01 Ôn tập Giải tích Thực"
chapter: '00'
order: 1
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---


Tại sao ta có thể yên tâm rằng phương trình vi phân $y' = f(t, y)$ thực sự có một nghiệm liên tục thay vì "rơi vào lỗ hổng" trên trục số? Câu trả lời nằm ở tính **đầy đủ (completeness)** của tập số thực $\mathbb{R}$—tính chất tinh tế ngăn không cho một dãy xấp xỉ hội tụ tiến tới một điểm... không tồn tại!

## Bản đồ kiến thức nền: Bốn trụ cột của Giải tích Thực cho PTVP

1. **Tiên đề Cận trên đúng (Supremum) & Tính đầy đủ của $\mathbb{R}$**:
   Mọi tập con khác rỗng bị chặn trên trong $\mathbb{R}$ đều có $\sup$, và mọi dãy Cauchy trong $\mathbb{R}$ đều hội tụ về một số thực—nền móng cho phép lặp Picard và phương pháp Euler.
2. **Dãy số & Tiêu chuẩn hội tụ**:
   Định lý hội tụ đơn điệu, định lý kẹp và định lý Bolzano–Weierstrass cho phép trích dãy con hội tụ từ các họ nghiệm xấp xỉ bị chặn.
3. **Hội tụ điểm vs. Hội tụ đều của dãy hàm**:
   Hội tụ đều bảo toàn tính liên tục và cho phép đưa giới hạn vào trong dấu tích phân $\lim \int f_n = \int \lim f_n$, điều kiện sống còn khi giải PTVP bằng chuỗi lũy thừa và lặp tích phân.
4. **Tính Compact (Định lý Heine–Borel)**:
   Trên đoạn đóng bị chặn $[a, b]$, mọi hàm liên tục đều đạt giá trị lớn nhất, nhỏ nhất—giúp chặn trên $\vert f(t, y) \vert \le M$ trong mọi chứng minh định lý tồn tại nghiệm.

## Mục tiêu
Bài học này giúp sinh viên củng cố nền tảng giải tích thực, nắm vững các khái niệm giới hạn, tính liên tục và tính compact, đồng thời hiểu vì sao các công cụ này đóng vai trò nền tảng trong việc phân tích phương trình vi phân. Sau bài học, sinh viên có thể vận dụng định lý giá trị trung gian, định lý Weierstrass và các tính chất hội tụ của dãy số trong bối cảnh phương trình vi phân thường (ODE).

## Kiến thức nền
Sinh viên cần nắm vững giới hạn dãy số, đạo hàm, tích phân cơ bản và các tính chất của hàm số thực. Kiến thức về tập hợp (hợp, giao, phần bù) cùng ký hiệu khoảng đóng và khoảng mở cũng cần thiết trước khi bắt đầu bài học này.

## Dẫn nhập
Khi khảo sát một phương trình vi phân, câu hỏi đầu tiên không chỉ là "nghiệm có dạng gì?" mà còn là "nghiệm có tồn tại không?" và "nếu tồn tại thì có duy nhất không?". Để trả lời những câu hỏi đó, ta cần kiểm soát hành vi của hàm số trên miền xác định. Đây chính là vai trò của giải tích thực.

Chẳng hạn, xét bài toán mô hình hóa phân bố nhiệt độ trên một thanh kim loại. Nếu hàm nhiệt độ bị gián đoạn tại một điểm, mô hình sẽ không phù hợp về mặt vật lý; nếu giá trị hàm tăng không bị chặn khi tiến tới một điểm, ta không thể dự đoán trạng thái của hệ. Giải tích thực cung cấp các điều kiện và định lý cần thiết để đảm bảo mô hình toán học có hành vi hợp lý.

### Khung giải thích (nên đọc chậm): Kiểm chứng dãy lặp Newton $x_{n+1} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$ là dãy Cauchy nhưng "lọt hố" trong $\mathbb{Q}$

Xuất phát từ $x_0 = 1 \in \mathbb{Q}$:
1. **Tính tay 4 số hạng đầu**:
   - $x_1 = \frac{1}{2}\left(1 + \frac{2}{1}\right) = \mathbf{1{,}5}$
   - $x_2 = \frac{1}{2}\left(1{,}5 + \frac{2}{1{,}5}\right) = \frac{17}{12} \approx \mathbf{1{,}416667}$
   - $x_3 = \frac{1}{2}\left(\frac{17}{12} + \frac{24}{17}\right) = \frac{577}{408} \approx \mathbf{1{,}4142157}$
2. **Quan sát khoảng cách giữa các số hạng**:
   - $\vert x_2 - x_1 \vert \approx 0{,}0833$
   - $\vert x_3 - x_2 \vert \approx 0{,}00245$
   - Sai số giảm theo bình phương: $\vert x_{n+1} - \sqrt{2}\vert = \frac{(x_n - \sqrt{2})^2}{2x_n}$, nên $(x_n)$ là dãy Cauchy cực nhanh.
3. **Điểm mấu chốt**: Mọi $x_n$ đều là **số hữu tỷ**, nhưng giới hạn $\sqrt{2} \notin \mathbb{Q}$. Nếu làm việc trên $\mathbb{Q}$, dãy xấp xỉ này không có đích đến; chỉ trong $\mathbb{R}$ đầy đủ thì giới hạn mới tồn tại.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung bạn đang đi trên một con đường núi. Định lý giá trị trung gian cho biết nếu bạn xuất phát ở độ cao 100 m và kết thúc ở độ cao 500 m, bạn buộc phải đi qua mọi độ cao nằm giữa hai mức đó—không thể nhảy từ 100 m lên 500 m mà bỏ qua các mức 200 m, 300 m hay 400 m. Trong khi đó, định lý Weierstrass khẳng định rằng trên một đoạn đường hữu hạn và đóng kín (tập compact), luôn tồn tại điểm cao nhất và điểm thấp nhất.

### Cách nhìn hình ảnh
Khi vẽ đồ thị của một hàm số liên tục trên đoạn $$ [a,b] $$, ta thu được một đường cong liền mạch. Định lý giá trị trung gian thể hiện ở chỗ đường cong này luôn cắt mọi đường thẳng nằm ngang ở mức giá trị nằm giữa $$ f(a) $$ và $$ f(b) $$. Định lý Weierstrass thể hiện ở chỗ đồ thị luôn có điểm đạt tung độ lớn nhất và điểm đạt tung độ nhỏ nhất trên đoạn đó.

### Cách nhìn hình thức
**Định lý Giá trị Trung gian (IVT)**: Nếu $$ f $$ liên tục trên $$ [a,b] $$ và $$ f(a)f(b) < 0 $$, thì tồn tại $$ c \in (a,b) $$ sao cho $$ f(c) = 0 $$.

**Định lý Weierstrass**: Nếu $$ f $$ liên tục trên tập compact $$ K $$, thì $$ f(K) $$ là tập compact. Đặc biệt, $$ f $$ đạt giá trị lớn nhất và giá trị nhỏ nhất trên $$ K $$.

**Dãy và Giới hạn**: Dãy $$ \left(x_n\right) $$ hội tụ đến $$ L $$ nếu với mọi $$ \varepsilon > 0 $$, tồn tại $$ N $$ sao cho với mọi $$ n > N $$, ta có $$ \lvert x_n - L \rvert < \varepsilon $$. Đây là cơ sở cho các phương pháp xấp xỉ liên tiếp trong lý thuyết giải ODE.

## Những ngộ nhận thường gặp
- "Hàm liên tục thì luôn trơn (có đạo hàm tại mọi điểm)." Sai. Có những hàm liên tục nhưng không khả vi tại một số điểm; ví dụ hàm giá trị tuyệt đối $$ \lvert x \rvert $$ liên tục trên $$ \mathbb{R} $$ nhưng có góc nhọn tại $$ x = 0 $$ nên không có đạo hàm tại đó.
- "Nếu $$ f $$ có giới hạn khi $$ x \to a $$ thì $$ f $$ liên tục tại $$ a $$." Sai. Giới hạn có thể tồn tại ngay cả khi hàm không xác định tại $$ a $$, hoặc xác định nhưng có giá trị khác với giới hạn đó.
- "Trên tập bị chặn thì hàm liên tục luôn đạt giá trị lớn nhất và nhỏ nhất." Sai. Tính bị chặn thôi chưa đủ; điều kiện đủ trong $$ \mathbb{R}^n $$ là tính compact (vừa đóng vừa bị chặn). Chẳng hạn, tập $$ \{1/n : n \in \mathbb{N}\} $$ bị chặn nhưng không đóng vì không chứa điểm giới hạn $$ 0 $$.
- "Định lý IVT chỉ dùng khi $$ f(a) $$ và $$ f(b) $$ trái dấu." Sai. Ở dạng tổng quát, với mọi giá trị $$ C $$ nằm giữa $$ f(a) $$ và $$ f(b) $$, đều tồn tại $$ c \in (a,b) $$ sao cho $$ f(c) = C $$.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại định nghĩa $$ \varepsilon $$–$$ \delta $$
Trước khi đi vào các định lý, sinh viên cần thành thạo định nghĩa giới hạn và tính liên tục theo ngôn ngữ $$ \varepsilon $$–$$ \delta $$. Đây là cách diễn đạt chặt chẽ ý tưởng "giá trị hàm tiến gần đến $$ L $$ khi $$ x $$ tiến gần đến $$ a $$".

### Bước 2: Phát biểu và hiểu các định lý cơ bản
Nắm vững phát biểu và ý nghĩa của định lý IVT và định lý Weierstrass, đặc biệt là vai trò của hai giả thiết "liên tục" và "tập compact"—nếu thiếu một trong hai điều kiện này, kết luận của định lý có thể không còn đúng.

### Bước 3: Vận dụng vào ODE
Liên hệ các định lý giải tích thực với bài toán tồn tại nghiệm của phương trình vi phân. Khi chứng minh một ODE có nghiệm, ta thường dùng các tính chất liên tục, bị chặn và hội tụ dãy để kiểm soát quỹ đạo nghiệm.

### Các checkpoint
- Bạn có thể phát biểu chính xác định lý IVT và định lý Weierstrass bằng lời không?
- Bạn có nhận diện được giả thiết quan trọng của từng định lý và đưa ra phản ví dụ khi thiếu giả thiết đó không?
- Bạn có giải thích được cách vận dụng các định lý này trong bối cảnh ODE không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Kiểm tra điều kiện IVT
Xét $$ f(x) = x^3 - x - 2 $$ trên đoạn $$ [1,2] $$. Ta có $$ f(1) = -2 $$ và $$ f(2) = 4 $$. Vì $$ f $$ liên tục trên $$ [1,2] $$ và $$ f(1)f(2) < 0 $$, theo định lý IVT tồn tại $$ c \in (1,2) $$ sao cho $$ f(c) = 0 $$. Điều này cho thấy phương trình $$ x^3 - x - 2 = 0 $$ có ít nhất một nghiệm thực thuộc khoảng $$ (1,2) $$.

### Ví dụ 2: Tìm giá trị lớn nhất và nhỏ nhất trên tập compact
Xét $$ f(x) = x^4 - 2x^2 + 1 $$ trên $$ [-2,2] $$. Đây là hàm liên tục trên tập compact $$ [-2,2] $$, nên theo định lý Weierstrass, $$ f $$ đạt giá trị lớn nhất và nhỏ nhất trên đoạn này. Tính đạo hàm: $$ f'(x) = 4x^3 - 4x = 4x(x^2 - 1) $$. Các điểm dừng là $$ x = 0 $$ và $$ x = \pm 1 $$. So sánh các giá trị $$ f(0) = 1 $$, $$ f(\pm 1) = 0 $$ và $$ f(\pm 2) = 9 $$, ta kết luận giá trị lớn nhất là $$ 9 $$ tại $$ x = \pm 2 $$ và giá trị nhỏ nhất là $$ 0 $$ tại $$ x = \pm 1 $$.

### Ví dụ 3: Dãy hội tụ trong ODE
Xét bài toán giá trị đầu $$ y' = y $$, $$ y(0) = 1 $$. Áp dụng phương pháp Euler trên đoạn $$ [0,1] $$ với bước $$ h = 1/n $$, ta thu được công thức truy hồi $$ x_{k+1} = x_k + \frac{1}{n}x_k $$, $$ x_0 = 1 $$. Tại $$ t = 1 $$, giá trị xấp xỉ là $$ x_n = \left(1 + \frac{1}{n}\right)^n $$, và dãy $$ \left(x_n\right) $$ hội tụ đến $$ e $$ khi $$ n \to \infty $$. Đây là minh họa cho việc dùng giới hạn dãy để xấp xỉ nghiệm ODE.

### Ví dụ 4: Phản ví dụ khi thiếu điều kiện
Xét $$ f(x) = 1/x $$ trên $$ \left(0,1\right] $$. Hàm này liên tục nhưng không bị chặn trên $$ \left(0,1\right] $$ và không đạt giá trị lớn nhất vì $$ f(x) \to +\infty $$ khi $$ x \to 0^+ $$. Phản ví dụ này cho thấy định lý Weierstrass không áp dụng được khi tập xác định $$ \left(0,1\right] $$ không phải là tập compact.

### Ví dụ 5: Áp dụng trong chứng minh tồn tại nghiệm
Xét bài toán $$ y' = \sqrt{1 - y^2} $$, $$ y(0) = 0 $$. Để chứng minh nghiệm tồn tại trên một khoảng chứa $$ t = 0 $$, ta cần hàm $$ f(t,y) = \sqrt{1 - y^2} $$ liên tục và bị chặn trong một miền đóng chứa điểm $$ \left(0,0\right) $$. Đây là ứng dụng trực tiếp của giải tích thực trong lý thuyết ODE.

## Câu hỏi khái niệm
1. Vì sao tính liên tục của vế phải $$ f(t,y) $$ lại quan trọng trong định lý tồn tại nghiệm ODE?
2. Tại sao khái niệm "tập compact" xuất hiện trong nhiều định lý giải tích? Nó đảm bảo tính chất gì?
3. Trong phương pháp xấp xỉ liên tiếp cho ODE, giới hạn dãy đóng vai trò gì?

## Bài toán ứng dụng
1. **Vật lý**: Một vật chuyển động có vận tốc thay đổi liên tục từ $$ -5\,\mathrm{m/s} $$ đến $$ 5\,\mathrm{m/s} $$. Chứng minh rằng tồn tại ít nhất một thời điểm mà vận tốc của vật bằng $$ 0 $$.
2. **Kinh tế**: Hàm cầu $$ Q(p) $$ liên tục theo giá $$ p $$. Nếu $$ Q(10) = 1000 $$ và $$ Q(20) = 500 $$, chứng minh rằng tồn tại mức giá $$ p_0 $$ nằm giữa $$ 10 $$ và $$ 20 $$ sao cho lượng cầu bằng $$ 750 $$.
3. **Sinh học**: Nồng độ thuốc trong máu $$ C(t) $$ là hàm liên tục theo thời gian $$ t $$. Nếu $$ C(0) = 0 $$ và $$ C(24) = 10\,\mathrm{mg/L} $$, chứng minh rằng tồn tại thời điểm $$ t_0 \in (0,24) $$ mà nồng độ đạt $$ 5\,\mathrm{mg/L} $$.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Tìm phản ví dụ"**: Cho sinh viên 5 phút để tìm các hàm vi phạm giả thiết của định lý (ví dụ: hàm liên tục nhưng không đạt giá trị lớn nhất trên một tập không compact).
- **Thảo luận nhóm**: Giao cho mỗi nhóm một mô hình vật lý đơn giản và yêu cầu xác định các đại lượng tương ứng với $$ f(a) $$, $$ f(b) $$ và điểm $$ c $$ trong định lý IVT.
- **Câu hỏi kiểm tra nhanh**: "Đúng hay sai? Nếu $$ f $$ liên tục trên $$ (0,1) $$ thì $$ f $$ đạt giá trị lớn nhất." Cho sinh viên suy nghĩ 30 giây rồi chọn đáp án và giải thích.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Sử dụng bảng hai cột gồm "Định lý" và "Điều kiện áp dụng" để hệ thống hóa các giả thiết cần thiết.
- Bổ sung các ví dụ minh họa bằng đồ thị trực quan bên cạnh cách viết ký hiệu hình thức.
- Vẽ đồ thị cho từng phản ví dụ để nhận ra rõ lý do định lý không còn đúng khi thiếu giả thiết.

### Thử thách cho sinh viên khá giỏi
- Chứng minh phiên bản mở rộng của định lý IVT cho hàm liên tục trên khoảng mở $$ (a,b) $$ có giới hạn một phía tại hai đầu mút trái dấu.
- So sánh định lý Arzelà–Ascoli (tính compact trong không gian hàm) với định lý Weierstrass và phân tích mối liên hệ giữa chúng.
- Đọc và trình bày lại định lý Picard–Lindelöf về sự tồn tại và duy nhất nghiệm, đồng thời nhận xét vai trò của điều kiện Lipschitz.

## Tóm tắt dễ nhớ
- **IVT**: Hàm liên tục trên một đoạn đóng sẽ nhận mọi giá trị trung gian giữa hai đầu mút.
- **Weierstrass**: Hàm liên tục trên tập compact luôn đạt giá trị lớn nhất và nhỏ nhất.
- **Tập compact** (trong $$ \mathbb{R}^n $$): Đóng và bị chặn.
- Giải tích thực cung cấp khung lý thuyết để chứng minh ODE có nghiệm và kiểm soát tính chất của nghiệm.

## Video tham khảo

- Xem trước: [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, tiếng Anh. Giới thiệu bức tranh tổng quan về đạo hàm và giới hạn trước khi dùng chúng làm ngôn ngữ mô tả sự biến thiên trong các chương ODE.
- [Limits, L'Hôpital's rule, and epsilon delta definitions | Chapter 7, Essence of calculus](https://www.youtube.com/watch?v=kfF40MiS7zA) — 3Blue1Brown, tiếng Việt. Phần $$ \varepsilon $$–$$ \delta $$ trình bày đúng ý nghĩa chặt chẽ của định nghĩa giới hạn được ôn tập trong bài.
- [Cauchy sequences and complete metric spaces, Real Analysis II](https://www.youtube.com/watch?v=m2iG0vR-7fM) — Dr. Bevin Maultsby, tiếng Anh. Trình bày về dãy Cauchy và tính đầy đủ trong không gian metric, làm nền tảng cho định lý ánh xạ co sau này.

## Tài liệu tham khảo
- Bartle & Sherbert — *Introduction to Real Analysis*: chương 2–3 trình bày chi tiết các định lý cơ bản.
- Ross — *Elementary Analysis*: hệ thống hóa nền tảng về giới hạn và tính liên tục.
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày ứng dụng của giải tích thực trong lý thuyết ODE.
