---
layout: post
title: "00-09 Lý thuyết Tích phân"
chapter: '00'
order: 9
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---

## Mục tiêu
Bài học này giúp sinh viên hiểu sâu sắc mối liên hệ giữa đạo hàm và tích phân qua định lý cơ bản của giải tích, nắm vững các tiêu chuẩn hội tụ của tích phân suy rộng, và vận dụng định lý Fubini trong việc tính tích phân nhiều lớp. Đây là nền tảng quan trọng để hiểu phương pháp biến đổi Laplace, phương trình đạo hàm riêng, và các công cụ giải tích nâng cao trong lý thuyết phương trình vi phân.

## Kiến thức nền
Sinh viên cần nắm vững tích phân Riemann cơ bản, các phương pháp tích phân (đổi biến, từng phần), và hiểu khái niệm hội tụ của chuỗi số. Kiến thức về giới hạn và liên tục từ các bài trước là cần thiết.

## Dẫn nhập
Khi giải phương trình vi phân, ta thường gặp tích phân không chỉ như một công cụ tính toán mà còn như một cách "ghi nhớ" toàn bộ lịch sử của hệ. Chẳng hạn, trong phương trình $$ y' = f(t) $$, nghiệm $$ y(t) = y(t_0) + \int_{t_0}^{t} f(s)\,ds $$ cho thấy giá trị hiện tại được tích lũy từ mọi quá khứ thông qua tích phân.

Hãy hình dung ta đổ nước vào một cái bình. Tốc độ dòng chảy vào tại mỗi thời điểm là f(t), và thể tích nước trong bình tại thời điểm t chính là tích phân của tốc độ đó từ lúc bắt đầu đến t. Tích phân không chỉ là phép cộng—nó là phép cộng có trí nhớ, nơi mọi khoảnh khắc đều được ghi lại và tổng hợp.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Tích phân xác định $$ \int_a^b f(x)\,dx $$ là diện tích "bao quanh" bởi đồ thị $$ f(x) $$, trục hoành, và các đường thẳng $$ x = a $$, $$ x = b $$. Nếu $$ f(x) \ge 0 $$, đó là diện tích thực. Nếu $$ f(x) $$ đổi dấu, ta cộng diện tích phần dương và trừ diện tích phần âm. Tích phân suy rộng cho phép $$ a = -\infty $$ hoặc $$ b = +\infty $$, hoặc $$ f $$ có điểm gián đoạn vô hạn.

### Cách nhìn hình ảnh
Vẽ đồ thị $$ f(x) = 1/\sqrt{x} $$ trên $$ \left(0,1\right] $$. Khi $$ x \to 0^+ $$, đồ thị dựng đứng, nhưng diện tích dưới đường cong vẫn hữu hạn, bằng $$ 2 $$. Ngược lại, với $$ f(x) = 1/x $$ trên $$ \left(0,1\right] $$, diện tích là vô hạn vì $$ \int_0^1 \frac{1}{x}\,dx = +\infty $$. Hai đồ thị trông tương tự nhưng tính khả tích hoàn toàn khác nhau tại $$ x = 0 $$.

### Cách nhìn hình thức
**Định lý cơ bản của giải tích (FTIC)**: Nếu $$ F $$ là một nguyên hàm của $$ f $$ trên $$ [a,b] $$, thì $$ \int_a^b f(x)\,dx = F(b) - F(a) $$. Đây là cầu nối giữa đạo hàm và tích phân.

**Tích phân suy rộng loại 1**: $$ \int_a^\infty f(x)\,dx $$ hội tụ nếu $$ \lim_{b \to \infty}\int_a^b f(x)\,dx $$ tồn tại hữu hạn.

**Tích phân suy rộng loại 2**: Nếu $$ f $$ có điểm kỳ dị tại $$ c \in (a,b) $$, thì $$ \int_a^b f(x)\,dx $$ hội tụ nếu cả $$ \int_a^c f(x)\,dx $$ và $$ \int_c^b f(x)\,dx $$ đều hội tụ.

**Tiêu chuẩn so sánh**: Nếu $$ 0 \le f(x) \le g(x) $$ và $$ \int g $$ hội tụ, thì $$ \int f $$ hội tụ. Nếu $$ \int g $$ phân kỳ và $$ f(x) \ge g(x) $$, thì $$ \int f $$ phân kỳ.

**Định lý Fubini**: $$\iint_R f(x,y)\,dA = \int_a^b \int_c^d f(x,y)\,dy\,dx = \int_c^d \int_a^b f(x,y)\,dx\,dy$$ nếu $$ f $$ khả tích trên hình chữ nhật $$ R $$.

## Những ngộ nhận thường gặp
- "Tích phân suy rộng chỉ cần tính là được." Không đúng. Phải kiểm tra hội tụ trước khi tính. Một số tích phân "tính" ra hữu hạn nhưng thực tế phân kỳ (do không hội tụ tuyệt đối).
- "$$ \int_0^\infty e^{-x}\,dx = 1/e $$." Sai. Thực ra $$ \int_0^\infty e^{-x}\,dx = 1 $$.
- "Đổi thứ tự tích phân luôn được." Không đúng. Chỉ khi hàm khả tích hoặc $$ f \ge 0 $$ mới được đổi thứ tự tùy ý.
- "Hàm bị chặn thì khả tích." Sai. Hàm Dirichlet (1 trên Q, 0 ngoài Q) bị chặn nhưng không khả tích Riemann vì không liên tục gần như mọi nơi.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại định lý cơ bản của giải tích
Hiểu rằng đạo hàm và tích phân là hai phép toán ngược nhau. $$ F'(x) = f(x) $$ có nghĩa là tốc độ thay đổi tức thời của $$ F $$ tại $$ x $$ bằng $$ f(x) $$, còn $$ \int_a^b f(x)\,dx = F(b) - F(a) $$ cho ta tổng cộng dồn của $$ f $$ trên đoạn.

### Bước 2: Phân loại và kiểm tra hội tụ tích phân suy rộng
Phân biệt giữa hai loại: khi cận vô hạn (loại 1) và khi hàm có điểm kỳ dị (loại 2). Học các tiêu chuẩn so sánh để xác định hội tụ hay phân kỳ.

### Bước 3: Mở rộng sang tích phân nhiều lớp
Dùng Fubini để đổi thứ tự tích phân. Hiểu rằng tích phân lặp là cách tính tích phân kép bằng cách "gọn gàng" từng lớp một.

### Các checkpoint
- Sinh viên có nhận biết được loại tích phân suy rộng và áp dụng tiêu chuẩn phù hợp không?
- Sinh viên có tính được các tích phân suy rộng cơ bản không?
- Sinh viên có vận dụng được Fubini trong các bài toán cụ thể không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tích phân suy rộng loại 1 - hội tụ
Tính $$ \int_1^\infty \frac{1}{x^2}\,dx $$. Nguyên hàm là $$ -1/x $$. Ta có $$\lim_{b \to \infty}\left[-1/x\right]_1^b = \lim_{b \to \infty}(-1/b + 1) = 1$$. Vậy tích phân hội tụ về $$ 1 $$.

### Ví dụ 2: Tích phân suy rộng loại 2 - phân kỳ
Tính $$ \int_0^1 \frac{1}{\sqrt{x}}\,dx $$. Tại $$ x = 0 $$ có điểm kỳ dị. Nguyên hàm là $$ 2\sqrt{x} $$. Khi đó $$\lim_{\varepsilon \to 0^+}\int_\varepsilon^1 \frac{1}{\sqrt{x}}\,dx = \lim_{\varepsilon \to 0^+}\left[2\sqrt{x}\right]_\varepsilon^1 = 2$$. Vậy tích phân hội tụ.

### Ví dụ 3: Tích phân suy rộng loại 2 - phân kỳ
Tính $$ \int_0^1 \frac{1}{x}\,dx $$. Nguyên hàm là $$ \ln\lvert x \rvert $$. Ta có $$\lim_{\varepsilon \to 0^+}\left[\ln\lvert x \rvert\right]_\varepsilon^1 = \lim_{\varepsilon \to 0^+}(0 - \ln \varepsilon) = +\infty$$. Vì vậy tích phân phân kỳ. Quy tắc chung là $$ \int_0^a x^p\,dx $$ hội tụ khi $$ p > -1 $$ và phân kỳ khi $$ p \le -1 $$.

### Ví dụ 4: Dùng Fubini tính tích phân kép
Tính $$ \iint_R (x + y)\,dA $$ với $$ R = [0,1]\times[0,2] $$. Theo Fubini,

$$
\int_0^2 \int_0^1 (x+y)\,dx\,dy
= \int_0^2 \left[\frac{x^2}{2} + xy\right]_0^1 dy
= \int_0^2 \left(\frac{1}{2} + y\right)dy
= 3.
$$

Đổi thứ tự tích phân cũng cho cùng kết quả.

### Ví dụ 5: Ứng dụng trong biến đổi Laplace
Biến đổi Laplace của $$ f(t) = 1 $$ là $$ \mathcal{L}\{1\} = \int_0^\infty e^{-st}\,dt $$. Đây là tích phân suy rộng loại 1. Ta có $$\int_0^\infty e^{-st}\,dt = \lim_{b \to \infty}\left[-e^{-st}/s\right]_0^b = 1/s$$ với $$ s > 0 $$. Vậy $$ \mathcal{L}\{1\} = 1/s $$ khi $$ \operatorname{Re}(s) > 0 $$.

## Câu hỏi khái niệm
1. Tại sao định lý cơ bản của giải tích được gọi là "cơ bản"? Nó kết nối hai khái niệm nào?
2. Tích phân suy rộng $$ \int_0^\infty f(x)\,dx $$ hội tụ khi nào? Tiêu chuẩn để xác định điều này là gì?
3. Định lý Fubini cho phép đổi thứ tự tích phân dựa trên điều kiện nào? Điều gì xảy ra nếu điều kiện không thỏa?

## Bài toán ứng dụng
1. **Vật lý**: Tính công cần thiết để đưa một vật khỏi trường hấp dẫn của Trái Đất. Công $$A = \int_R^\infty \frac{GMm}{r^2}\,dr = \frac{GMm}{R}$$.
2. **Xác suất**: Hàm mật độ xác suất $$ f(x) $$ trên $$ [0,\infty) $$ cần thỏa $$ \int_0^\infty f(x)\,dx = 1 $$. Kiểm tra xem $$ f(x) = e^{-x} $$ có phải là hàm mật độ không.
3. **Kỹ thuật**: Tính năng lượng tín hiệu $$ x(t) = e^{-\alpha t}\sin(\omega t) $$ trên $$ [0,\infty) $$. Khi đó $$ E = \int_0^\infty x^2(t)\,dt $$.

## Chiến lược giảng dạy tương tác
- **Hoạt động "So sánh hai đồ thị"**: Vẽ đồ thị $$ 1/x $$, $$ 1/x^2 $$, $$ 1/\sqrt{x} $$ gần $$ 0 $$. Yêu cầu sinh viên đoán tích phân trên $$ \left(0,1\right] $$ hội tụ hay phân kỳ, rồi kiểm tra bằng tính toán.
- **Thảo luận nhóm**: Cho mỗi nhóm một tích phân suy rộng và yêu cầu xác định loại, kiểm tra hội tụ, tính toán. Các nhóm trình bày kết quả.
- **Câu đố nhanh**: "$$ \int_0^1 x^{-0.5}\,dx $$ và $$ \int_0^1 x^{-1.5}\,dx $$ hội tụ hay phân kỳ?".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Cung cấp bảng tiêu chuẩn: "$$ \int_1^\infty x^{-p}\,dx $$ hội tụ khi $$ p > 1 $$" và "$$ \int_0^1 x^p\,dx $$ hội tụ khi $$ p > -1 $$".
- Luyện tập với các hàm đơn giản trước: đa thức, hàm mũ.
- Vẽ đồ thị để "thấy" tích phân như diện tích.

### Thử thách cho sinh viên khá giỏi
- Nghiên cứu và trình bày về tích phân hội tụ có điều kiện vs hội tụ tuyệt đối.
- Tìm hiểu về tiêu chuẩn Dirichlet và Abel trong việc kiểm tra hội tụ.
- Ứng dụng: chứng minh công thức Gamma và Beta.

## Tóm tắt dễ nhớ
**FTIC**: Đạo hàm và tích phân là hai phép toán ngược nhau.
**Suy rộng loại 1**: Cận vô hạn $$ \Rightarrow \int_1^\infty x^{-p}\,dx $$ hội tụ khi $$ p > 1 $$.
**Suy rộng loại 2**: Điểm kỳ dị $$ \Rightarrow \int_0^1 x^p\,dx $$ hội tụ khi $$ p > -1 $$.
**Fubini**: Tích phân kép = tích phân lặp nếu hàm khả tích.
Trong ODE, tích phân là "trí nhớ" của hệ—nó ghi lại toàn bộ lịch sử để xác định trạng thái hiện tại.

## Tài liệu tham khảo
- Bartle & Sherbert — *Introduction to Real Analysis*: chương 7 chi tiết về tích phân Riemann.
- Apostol — *Calculus, Vol. 1 & 2*: nhiều ví dụ về tích phân suy rộng.
- Churchill & Brown — *Operational Mathematics*: ứng dụng trong biến đổi Laplace.
