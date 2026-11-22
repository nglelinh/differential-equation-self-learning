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
Bài học này giúp sinh viên nắm vững mối liên hệ giữa đạo hàm và tích phân thông qua định lý cơ bản của giải tích, sử dụng thành thạo các tiêu chuẩn hội tụ cho tích phân suy rộng và vận dụng định lý Fubini khi tính tích phân bội. Đây là kiến thức nền để tiếp cận biến đổi Laplace, phương trình đạo hàm riêng và các công cụ giải tích nâng cao trong lý thuyết phương trình vi phân.

## Kiến thức nền
Sinh viên cần nắm vững tích phân Riemann cơ bản, các kỹ thuật tính tích phân (đổi biến, tích phân từng phần) cùng khái niệm hội tụ của chuỗi số, giới hạn và tính liên tục từ các bài trước.

## Dẫn nhập
Trong phương trình vi phân, tích phân không chỉ là phép tính kỹ thuật mà còn thể hiện sự tích lũy theo thời gian của hệ. Chẳng hạn, với phương trình $$ y' = f(t) $$, công thức nghiệm $$ y(t) = y(t_0) + \int_{t_0}^{t} f(s)\,ds $$ cho thấy trạng thái tại thời điểm $$ t $$ được tích lũy từ toàn bộ tốc độ biến thiên trong khoảng từ $$ t_0 $$ đến $$ t $$.

Hãy hình dung nước chảy vào một bình chứa với lưu lượng tại mỗi thời điểm là $$ f(t) $$. Thể tích nước tích tụ trong bình đến thời điểm $$ t $$ chính là tích phân của $$ f $$ từ lúc bắt đầu đến $$ t $$. Hiểu theo cách này, tích phân là phép cộng dồn liên tục mọi biến thiên theo thời gian.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Tích phân xác định $$ \int_a^b f(x)\,dx $$ biểu diễn diện tích đại số giới hạn bởi đồ thị hàm $$ f(x) $$, trục hoành và hai đường thẳng $$ x = a $$, $$ x = b $$: phần nằm phía trên trục hoành mang dấu dương, phần nằm phía dưới mang dấu âm. Tích phân suy rộng mở rộng khái niệm này cho trường hợp cận lấy tích phân tiến ra $$ \pm\infty $$ hoặc hàm $$ f $$ không bị chặn tại một điểm kỳ dị trong miền tích phân.

### Cách nhìn hình ảnh
Xét đồ thị hàm $$ f(x) = 1/\sqrt{x} $$ trên $$ \left(0,1\right] $$: khi $$ x \to 0^+ $$, đồ thị tiến thẳng lên vô cực, nhưng diện tích phần dưới đường cong vẫn hữu hạn và bằng $$ 2 $$. Ngược lại, với $$ f(x) = 1/x $$ trên $$ \left(0,1\right] $$, hình dạng đồ thị khá giống nhau nhưng diện tích lại vô hạn vì $$ \int_0^1 \frac{1}{x}\,dx = +\infty $$. Điều này cho thấy tốc độ tiến ra vô cực gần điểm kỳ dị quyết định tính hội tụ của tích phân.

### Cách nhìn hình thức
**Định lý cơ bản của giải tích (FTC)**: Nếu $$ F $$ là một nguyên hàm của $$ f $$ trên $$ [a,b] $$ (với $$ f $$ khả tích trên $$ [a,b] $$), thì $$ \int_a^b f(x)\,dx = F(b) - F(a) $$. Đây là cầu nối trực tiếp giữa phép lấy đạo hàm và phép lấy tích phân.

**Tích phân suy rộng loại 1**: $$ \int_a^\infty f(x)\,dx $$ hội tụ nếu giới hạn $$ \lim_{b \to \infty}\int_a^b f(x)\,dx $$ tồn tại hữu hạn.

**Tích phân suy rộng loại 2**: Nếu $$ f $$ có điểm kỳ dị tại $$ c \in (a,b) $$, thì $$ \int_a^b f(x)\,dx $$ hội tụ khi và chỉ khi cả hai tích phân $$ \int_a^c f(x)\,dx $$ và $$ \int_c^b f(x)\,dx $$ đều hội tụ.

**Tiêu chuẩn so sánh**: Nếu $$ 0 \le f(x) \le g(x) $$ và $$ \int g $$ hội tụ thì $$ \int f $$ cũng hội tụ. Ngược lại, nếu $$ 0 \le g(x) \le f(x) $$ và $$ \int g $$ phân kỳ thì $$ \int f $$ cũng phân kỳ.

**Định lý Fubini**: Nếu $$ f $$ khả tích tuyệt đối trên hình chữ nhật $$ R = [a,b]\times[c,d] $$, thì

$$
\iint_R f(x,y)\,dA = \int_a^b \int_c^d f(x,y)\,dy\,dx = \int_c^d \int_a^b f(x,y)\,dx\,dy.
$$

## Những ngộ nhận thường gặp
- "Tích phân suy rộng chỉ cần tìm nguyên hàm rồi thay cận là xong." Sai. Cần kiểm tra sự tồn tại của giới hạn và phát hiện các điểm kỳ dị bên trong đoạn tích phân; nếu bỏ qua điểm kỳ dị và áp dụng thẳng công thức Newton–Leibniz, ta có thể thu được một giá trị hữu hạn sai lệch dù tích phân thực chất phân kỳ.
- "$$ \int_0^\infty e^{-x}\,dx = 1/e $$." Sai. Kết quả đúng là $$ \int_0^\infty e^{-x}\,dx = 1 $$.
- "Lúc nào cũng có thể tùy ý đổi thứ tự tích phân." Sai. Chỉ được đổi thứ tự tích phân khi hàm khả tích tuyệt đối trên miền (định lý Fubini) hoặc không âm và đo được (định lý Tonelli).
- "Mọi hàm bị chặn trên đoạn đóng đều khả tích Riemann." Sai. Hàm Dirichlet (nhận giá trị $$ 1 $$ trên $$ \mathbb{Q} $$ và $$ 0 $$ ngoài $$ \mathbb{Q} $$) bị chặn nhưng không khả tích Riemann vì gián đoạn tại mọi điểm.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại định lý cơ bản của giải tích
Nắm rõ đạo hàm và tích phân là hai phép toán ngược nhau: $$ F'(x) = f(x) $$ mô tả tốc độ biến thiên tức thời, còn $$ \int_a^b f(x)\,dx = F(b) - F(a) $$ cho tổng biến thiên tích lũy trên đoạn $$ [a,b] $$.

### Bước 2: Phân loại và xét hội tụ tích phân suy rộng
Phân biệt rõ tích phân suy rộng loại 1 (cận vô hạn) và loại 2 (hàm có điểm kỳ dị), đồng thời thành thạo tiêu chuẩn so sánh để kết luận hội tụ hay phân kỳ.

### Bước 3: Mở rộng sang tích phân bội
Áp dụng định lý Fubini để chuyển tích phân kép thành tích phân lặp và biết khi nào được phép đổi thứ tự lấy tích phân.

### Các checkpoint
- Bạn có nhận diện đúng loại tích phân suy rộng và chọn tiêu chuẩn kiểm tra hội tụ phù hợp không?
- Bạn có tính được các tích phân suy rộng cơ bản không?
- Bạn có vận dụng được định lý Fubini để tính tích phân kép và đổi thứ tự tích phân không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tích phân suy rộng loại 1 — hội tụ
Tính $$ \int_1^\infty \frac{1}{x^2}\,dx $$. Một nguyên hàm là $$ -1/x $$, nên

$$
\lim_{b \to \infty}\left[-1/x\right]_1^b = \lim_{b \to \infty}(-1/b + 1) = 1.
$$

Vậy tích phân hội tụ về $$ 1 $$.

### Ví dụ 2: Tích phân suy rộng loại 2 — hội tụ
Tính $$ \int_0^1 \frac{1}{\sqrt{x}}\,dx $$. Hàm có điểm kỳ dị tại $$ x = 0 $$ và có nguyên hàm là $$ 2\sqrt{x} $$. Khi đó

$$
\lim_{\varepsilon \to 0^+}\int_\varepsilon^1 \frac{1}{\sqrt{x}}\,dx = \lim_{\varepsilon \to 0^+}\left[2\sqrt{x}\right]_\varepsilon^1 = 2.
$$

Vậy tích phân hội tụ và có giá trị bằng $$ 2 $$.

### Ví dụ 3: Tích phân suy rộng loại 2 — phân kỳ
Tính $$ \int_0^1 \frac{1}{x}\,dx $$. Nguyên hàm là $$ \ln\lvert x \rvert $$, nên

$$
\lim_{\varepsilon \to 0^+}\left[\ln\lvert x \rvert\right]_\varepsilon^1 = \lim_{\varepsilon \to 0^+}(0 - \ln \varepsilon) = +\infty.
$$

Vì vậy tích phân phân kỳ. Tổng quát, với $$ a > 0 $$, tích phân $$ \int_0^a x^p\,dx $$ hội tụ khi $$ p > -1 $$ và phân kỳ khi $$ p \le -1 $$.

### Ví dụ 4: Dùng định lý Fubini tính tích phân kép
Tính $$ \iint_R (x + y)\,dA $$ với $$ R = [0,1]\times[0,2] $$. Theo định lý Fubini,

$$
\int_0^2 \int_0^1 (x+y)\,dx\,dy
= \int_0^2 \left[\frac{x^2}{2} + xy\right]_0^1 dy
= \int_0^2 \left(\frac{1}{2} + y\right)dy
= 3.
$$

Đổi thứ tự lấy tích phân cũng cho cùng kết quả.

### Ví dụ 5: Ứng dụng trong biến đổi Laplace
Biến đổi Laplace của hàm hằng $$ f(t) = 1 $$ là $$ \mathcal{L}\{1\} = \int_0^\infty e^{-st}\,dt $$, một tích phân suy rộng loại 1. Với $$ s > 0 $$, ta có

$$
\int_0^\infty e^{-st}\,dt = \lim_{b \to \infty}\left[-e^{-st}/s\right]_0^b = 1/s.
$$

Tổng quát cho tham số phức, $$ \mathcal{L}\{1\} = 1/s $$ khi $$ \operatorname{Re}(s) > 0 $$.

## Câu hỏi khái niệm
1. Vì sao định lý cơ bản của giải tích được gọi là "cơ bản"? Nó kết nối hai khái niệm nào?
2. Tích phân suy rộng $$ \int_0^\infty f(x)\,dx $$ hội tụ khi nào, và có những tiêu chuẩn nào để kiểm tra?
3. Định lý Fubini đòi hỏi điều kiện gì để được phép đổi thứ tự tích phân, và điều gì có thể xảy ra nếu điều kiện đó không thỏa mãn?

## Bài toán ứng dụng
1. **Vật lý**: Tính công cần thiết để đưa một vật có khối lượng $$ m $$ thoát khỏi trường hấp dẫn của Trái Đất từ khoảng cách $$ R $$ ra vô cực: $$A = \int_R^\infty \frac{GMm}{r^2}\,dr = \frac{GMm}{R}$$.
2. **Xác suất**: Một hàm mật độ xác suất $$ f(x) $$ trên $$ [0,\infty) $$ cần không âm và thỏa mãn $$ \int_0^\infty f(x)\,dx = 1 $$. Hãy kiểm tra xem $$ f(x) = e^{-x} $$ có phải là hàm mật độ hợp lệ hay không.
3. **Kỹ thuật**: Xét tín hiệu $$ x(t) = e^{-\alpha t}\sin(\omega t) $$ trên $$ [0,\infty) $$ với $$ \alpha > 0 $$. Hãy thiết lập và tính năng lượng tín hiệu $$ E = \int_0^\infty x^2(t)\,dt $$.

## Chiến lược giảng dạy tương tác
- **Hoạt động "So sánh đồ thị"**: Vẽ đồ thị các hàm $$ 1/x $$, $$ 1/x^2 $$ và $$ 1/\sqrt{x} $$ gần $$ x = 0 $$, cho sinh viên dự đoán tích phân trên $$ \left(0,1\right] $$ hội tụ hay phân kỳ rồi kiểm chứng bằng tính toán.
- **Thảo luận nhóm**: Giao mỗi nhóm một tích phân suy rộng để phân loại, xét hội tụ và tính giá trị (nếu hội tụ), sau đó trình bày kết quả.
- **Câu hỏi nhanh**: "Hai tích phân $$ \int_0^1 x^{-0.5}\,dx $$ và $$ \int_0^1 x^{-1.5}\,dx $$ hội tụ hay phân kỳ?"

## Phân hóa học tập

### Hỗ trợ sinh viên gặp khó khăn
- Hệ thống hóa hai mốc so sánh chuẩn: $$ \int_1^\infty x^{-p}\,dx $$ hội tụ khi $$ p > 1 $$, và $$ \int_0^1 x^p\,dx $$ hội tụ khi $$ p > -1 $$.
- Luyện tập trước với các hàm sơ cấp như đa thức và hàm mũ.
- Vẽ đồ thị để gắn tích phân với trực giác diện tích.

### Thử thách cho sinh viên khá giỏi
- Phân biệt tích phân suy rộng hội tụ có điều kiện và hội tụ tuyệt đối.
- Tìm hiểu tiêu chuẩn Dirichlet và tiêu chuẩn Abel để xét sự hội tụ của tích phân suy rộng.
- Khảo sát miền hội tụ và các tính chất cơ bản của hàm Gamma và hàm Beta.

## Tóm tắt dễ nhớ
- **Định lý cơ bản (FTC)**: Đạo hàm và tích phân là hai phép toán ngược nhau.
- **Tích phân suy rộng loại 1**: Cận vô hạn; $$ \int_1^\infty x^{-p}\,dx $$ hội tụ khi $$ p > 1 $$.
- **Tích phân suy rộng loại 2**: Có điểm kỳ dị; $$ \int_0^1 x^p\,dx $$ hội tụ khi $$ p > -1 $$.
- **Định lý Fubini**: Tích phân kép bằng tích phân lặp khi hàm khả tích tuyệt đối.
- Trong ODE, tích phân đóng vai trò tổng hợp toàn bộ lịch sử biến thiên để xác định trạng thái hiện tại của hệ.

## Video tham khảo

- Xem trước: [Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus](https://www.youtube.com/watch?v=rfG8ce4nNh0) — 3Blue1Brown, tiếng Anh. Giải thích định lý cơ bản của giải tích—lý do bài toán $$ y'=f(t) $$ quy về phép lấy tích phân.
- [Numerical Integration: Discrete Riemann Integrals and Trapezoid Rule](https://www.youtube.com/watch?v=Xw6W3Ph3Wzc) — Steve Brunton, tiếng Anh. Trình bày tổng Riemann và quy tắc hình thang, cơ sở tích phân rời rạc của nhiều sơ đồ giải số ODE.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, tiếng Anh. Trực giác về diện tích và sự tích lũy như phép ngược của đạo hàm, hữu ích cho phương pháp biến thiên hằng số về sau.

## Tài liệu tham khảo
- Bartle & Sherbert — *Introduction to Real Analysis*: chương 7 trình bày chi tiết về tích phân Riemann.
- Apostol — *Calculus, Vol. 1 & 2*: cung cấp nhiều ví dụ về tích phân suy rộng.
- Churchill & Brown — *Operational Mathematics*: trình bày ứng dụng tích phân trong biến đổi Laplace.
