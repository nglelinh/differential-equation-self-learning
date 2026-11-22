---
layout: post
title: "01-06 Định lý Tồn tại và Duy nhất"
chapter: '01'
order: 6
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---

## Mục tiêu
Bài học này giúp sinh viên nắm vững hai câu hỏi nền tảng đứng sau mọi kỹ thuật giải ODE: bài toán giá trị đầu có nghiệm hay không, và nếu có thì nghiệm đó có duy nhất hay không. Sinh viên cần phân biệt vai trò của tính liên tục với điều kiện Lipschitz, hiểu ý nghĩa của tính duy nhất đối với độ tin cậy của mô hình và phân tích được các phản ví dụ khi giả thiết bị vi phạm.

## Kiến thức nền
Sinh viên cần nắm dạng phương trình cấp một $$ y'=f(t,y) $$, ý nghĩa của bài toán giá trị đầu $$ y(t_0)=y_0 $$ và trực giác về trường hướng (slope field). Việc quen với giá trị tuyệt đối và khái niệm ánh xạ co sẽ giúp tiếp cận ý tưởng chứng minh Picard dễ hơn, nhưng nội dung cốt lõi vẫn hoàn toàn theo dõi được từ góc nhìn trực quan.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-06 Định lý Tồn tại và Duy nhất]({{ site.imgurl }}/chapter_img/chapter01/01_06_existence_uniqueness.svg)

Ở các bài trước, ta tập trung vào các kỹ thuật tìm nghiệm. Tuy nhiên, có một câu hỏi nền tảng hơn: liệu bài toán đã cho có chắc chắn tồn tại nghiệm không, và điều kiện đầu có xác định duy nhất một quỹ đạo không? Trong mô hình hóa, đây không phải chi tiết hình thức: nếu nghiệm không duy nhất, trạng thái ban đầu không thể dự báo tương lai một cách xác định.

Định lý tồn tại và duy nhất trả lời chính xác khi nào một bài toán giá trị đầu được đặt chỉnh (well-posed)—giúp ta biết trước khi giải rằng mô hình có cơ sở toán học nhất quán.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung mỗi điểm trong mặt phẳng $$ \left(t,y\right) $$ mang một mũi tên nhỏ chỉ hướng đi của nghiệm. Nếu các mũi tên biến đổi trơn tru và không đổi quá đột ngột theo phương thẳng đứng $$ y $$, từ mỗi điểm xuất phát ta kỳ vọng có duy nhất một đường cong tiếp xúc với trường hướng đó. Nếu trường hướng có sự thay đổi quá gắt theo $$ y $$, nhiều đường cong có thể cùng xuất phát từ một điểm.

### Cách nhìn hình ảnh
Trên trường hướng của một phương trình thỏa mãn tính duy nhất, hai đường cong nghiệm khác nhau không thể cắt nhau, vì tại giao điểm sẽ có hai nghiệm phân biệt cùng thỏa một điều kiện đầu. Ngược lại, với bài toán

$$
y'=y^{1/3},\qquad y(0)=0,
$$

có vô số quỹ đạo cùng đi qua gốc tọa độ: nghiệm hằng $$ y\equiv 0 $$, nghiệm rời khỏi gốc ngay lập tức, hoặc nghiệm nằm yên trên trục hoành một khoảng thời gian rồi mới tách lên.

### Cách nhìn hình thức
**Định lý Picard–Lindelöf**: Nếu hàm $$ f(t,y) $$ liên tục trên một hình chữ nhật đóng chứa điểm $$ \left(t_0,y_0\right) $$ ở phần trong và thỏa mãn điều kiện Lipschitz theo biến $$ y $$ trên hình chữ nhật đó, thì bài toán giá trị đầu

$$
\frac{dy}{dt}=f(t,y),\qquad y(t_0)=y_0
$$

có một nghiệm duy nhất trên một khoảng mở đủ nhỏ chứa $$ t_0 $$.

Điều kiện Lipschitz theo biến $$ y $$ nghĩa là tồn tại hằng số $$ L \ge 0 $$ sao cho

$$
\lvert f(t,y_1)-f(t,y_2)\rvert\leq L\lvert y_1-y_2\rvert
$$

với mọi $$ (t,y_1) $$, $$ (t,y_2) $$ trong miền xét. Điều kiện này chặt hơn tính liên tục theo $$ y $$ và là giả thiết then chốt bảo đảm tính duy nhất.

## Ý nghĩa toán học và mô hình hóa
Tính liên tục của $$ f $$ đủ để bảo đảm sự tồn tại nghiệm cục bộ (định lý Peano), vì trường hướng không bị đứt gãy. Tuy nhiên, để bảo đảm chỉ có duy nhất một quỹ đạo đi qua $$ (t_0,y_0) $$, ta cần kiểm soát tốc độ biến thiên của $$ f $$ theo trạng thái $$ y $$ thông qua điều kiện Lipschitz.

Về mặt ứng dụng, tính duy nhất bảo đảm tính quyết định cục bộ của mô hình: cùng một điều kiện đầu chỉ dẫn tới một diễn biến duy nhất. Trong tính toán số, tính duy nhất cũng là cơ sở để các thuật toán bước thời gian bám theo đúng quỹ đạo vật lý.

## Những ngộ nhận thường gặp
- "Tính liên tục của $$ f $$ là đủ để nghiệm duy nhất." Sai. Liên tục chỉ bảo đảm tồn tại cục bộ, không bảo đảm duy nhất.
- "Nếu $$ f $$ không Lipschitz thì nghiệm chắc chắn không duy nhất." Sai. Điều kiện Lipschitz là điều kiện đủ, không phải điều kiện cần.
- "Tìm được một công thức nghiệm nghĩa là nghiệm đó duy nhất." Sai. Có thể tồn tại nhiều nghiệm khác nhau cùng thỏa một điều kiện đầu.
- "Tính duy nhất chỉ là vấn đề lý thuyết thuần túy." Sai. Nó quyết định trực tiếp tính nhất quán và khả năng dự báo của mô hình.

## Tiến trình học tập đề xuất

### Bước 1: Nhắc lại bài toán giá trị đầu
Nắm rõ mục tiêu là khảo sát các đường cong nghiệm đi qua một điểm cho trước $$ (t_0,y_0) $$.

### Bước 2: Tách bạch câu hỏi tồn tại và câu hỏi duy nhất
Phân biệt rõ giả thiết nào đảm bảo có nghiệm và giả thiết nào đảm bảo nghiệm là duy nhất.

### Bước 3: Hiểu ý nghĩa của điều kiện Lipschitz
Xem điều kiện Lipschitz như giới hạn độ nhạy của vế phải $$ f(t,y) $$ theo biến trạng thái $$ y $$ (chẳng hạn $$ \partial f/\partial y $$ liên tục và bị chặn là điều kiện đủ dễ kiểm tra).

### Bước 4: Phân tích các phản ví dụ kinh điển
Khảo sát các bài toán không tồn tại, không duy nhất hoặc chỉ tồn tại cục bộ để hiểu giới hạn chính xác của định lý.

### Các checkpoint
- Bạn có phân biệt được tính liên tục với điều kiện Lipschitz không?
- Bạn có giải thích được vì sao hai đường cong nghiệm không thể cắt nhau khi tính duy nhất được thỏa mãn không?
- Bạn có phân biệt được nghiệm tồn tại cục bộ với nghiệm tồn tại toàn cục không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Bài toán có nghiệm duy nhất
Xét bài toán

$$
y'=t+y,\qquad y(0)=1.
$$

Hàm $$ f(t,y)=t+y $$ liên tục trên toàn $$ \mathbb{R}^2 $$ và thỏa điều kiện Lipschitz theo $$ y $$ với hằng số $$ L=1 $$, vì

$$
\lvert f(t,y_1)-f(t,y_2)\rvert=\lvert y_1-y_2\rvert.
$$

Do đó bài toán có nghiệm duy nhất cục bộ (và thực tế là toàn cục trên toàn $$ \mathbb{R} $$).

### Ví dụ 2: Liên tục nhưng không duy nhất
Xét bài toán

$$
y'=y^{1/3},\qquad y(0)=0.
$$

Hàm $$ f(y)=y^{1/3} $$ liên tục tại $$ y=0 $$ nhưng không Lipschitz trong mọi lân cận của $$ 0 $$, vì $$ f'(y)=\frac{1}{3}y^{-2/3} $$ không bị chặn khi $$ y\to 0 $$. Bên cạnh nghiệm tầm thường $$ y(t)=0 $$, tách biến với $$ y>0 $$ cho $$ \frac{dy}{y^{1/3}}=dt \implies \frac{3}{2}y^{2/3}=t+C $$. Từ đó, với mọi hằng số $$ a\geq 0 $$, hàm

$$
y(t)=
\begin{cases}
0, & t\leq a,\\
\left(\frac{2}{3}(t-a)\right)^{3/2}, & t>a
\end{cases}
$$

đều là nghiệm của bài toán giá trị đầu. Đây là phản ví dụ kinh điển cho thấy tính liên tục không đủ bảo đảm tính duy nhất.

### Ví dụ 3: Không tồn tại nghiệm tại điểm ban đầu
Xét bài toán

$$
y'=\frac{1}{t-1},\qquad y(1)=0.
$$

Vế phải không xác định và không liên tục tại $$ t=1 $$, nên định lý không áp dụng được; thực tế bài toán không có nghiệm nào khả vi đi qua điểm $$ (1,0) $$. Ví dụ này tách biệt rõ trường hợp "không tồn tại" với "không duy nhất".

### Ví dụ 4: Duy nhất cục bộ nhưng không tồn tại toàn cục
Xét bài toán

$$
y'=y^2,\qquad y(0)=1.
$$

Hàm $$ f(y)=y^2 $$ trơn và thỏa điều kiện Lipschitz cục bộ trên mọi miền bị chặn, nên tồn tại nghiệm duy nhất cục bộ. Giải trực tiếp cho $$ y(t)=\frac{1}{1-t} $$. Nghiệm là duy nhất nhưng chỉ tồn tại trên khoảng $$ (-\infty,1) $$—cho thấy tính duy nhất cục bộ không tự động kéo theo sự tồn tại trên toàn $$ \mathbb{R} $$.

## Câu hỏi khái niệm
1. Vì sao tính liên tục đủ để gợi ý sự tồn tại nghiệm nhưng lại chưa đủ để bảo đảm tính duy nhất?
2. Về mặt hình học, điều kiện Lipschitz ngăn cản hiện tượng gì xảy ra với trường hướng?
3. Vì sao một bài toán thỏa mãn định lý Picard–Lindelöf vẫn có thể có nghiệm chỉ tồn tại trên một khoảng thời gian hữu hạn?

## Bài toán ứng dụng
1. Nếu hàm phản hồi trong bộ điều khiển robot thay đổi quá gắt gần điểm cân bằng (vi phạm điều kiện Lipschitz), điều đó ảnh hưởng thế nào đến tính duy nhất của quỹ đạo?
2. Trong dự báo thời tiết hoặc mô hình dịch tễ, tính duy nhất của nghiệm có ý nghĩa gì?
3. Khi một mô hình sinh học cho nghiệm bùng nổ sau thời gian hữu hạn, đó là đặc điểm của tự nhiên hay là giới hạn của mô hình toán học?

## Chiến lược giảng dạy tương tác
- Trước khi phát biểu định lý, đặt câu hỏi: "Nếu biết hệ số góc tại mọi điểm, có chắc chỉ có đúng một đường cong đi qua một điểm cho trước không?"
- So sánh trực tiếp hai trường hướng: một ví dụ có nghiệm duy nhất và ví dụ $$ y'=y^{1/3} $$.
- Khuyến khích sinh viên tìm thêm hàm liên tục nhưng không Lipschitz tại $$ 0 $$.
- Thảo luận ngắn: trong thực tế, việc mất tính duy nhất phản ánh thiếu sót của mô hình hay bản chất vật lý?

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Phân tách bài học thành ba câu hỏi độc lập: tồn tại, duy nhất và toàn cục; dùng bảng so sánh các ví dụ theo ba cột này kèm minh họa trường hướng.

### Thử thách cho sinh viên khá giỏi
Phác thảo ý tưởng phép lặp Picard và nguyên lý ánh xạ co Banach, đồng thời chứng minh rằng nếu $$ f_y $$ liên tục và bị chặn trên một miền lồi theo $$ y $$ thì $$ f $$ thỏa điều kiện Lipschitz theo $$ y $$ trên miền đó.

## Tóm tắt dễ nhớ
Một bài toán giá trị đầu đáng tin cậy cần nghiệm tồn tại và duy nhất. Tính liên tục của $$ f $$ bảo đảm tồn tại cục bộ, còn điều kiện Lipschitz theo $$ y $$ bảo đảm tính duy nhất cục bộ; ngay cả khi duy nhất, nghiệm vẫn có thể chỉ tồn tại trên một khoảng hữu hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Điều khiển tự động và tính quyết định
- Bài toán: Bộ điều khiển lái cần bảo đảm rằng từ cùng một trạng thái ban đầu, hệ không thể rẽ sang hai quỹ đạo khác nhau.
- Mô hình:

$$
\frac{dx}{dt}=f(t,x),\qquad x(0)=x_0.
$$

- Giả thiết và giới hạn: Tính duy nhất yêu cầu luật phản hồi đủ trơn theo trạng thái; trong thực tế, bão hòa, va chạm hoặc điều khiển chuyển mạch rời rạc có thể phá vỡ tính trơn này.
- Diễn giải: Không có tính duy nhất, mô hình mất khả năng dự báo xác định.

#### Động học hóa học khi khởi động phản ứng
- Bài toán: Xác định xem từ nồng độ ban đầu cho trước, phản ứng có diễn biến theo một kịch bản duy nhất hay không.
- Mô hình:

$$
\frac{dc}{dt}=f(c,T).
$$

- Giả thiết và giới hạn: Mô hình ODE giả sử hỗn hợp khuấy đều và bỏ qua biến thiên theo không gian; khi có khuếch tán hoặc phân tầng nhiệt mạnh cần chuyển sang PDE.
- Diễn giải: Định lý tồn tại–duy nhất xác nhận tính nhất quán toán học của mô hình trước khi dùng để dự báo quá trình.

#### Dự báo dịch tễ ở giai đoạn đầu
- Bài toán: Kiểm tra xem cùng dữ liệu đầu vào có xác định một quỹ đạo số ca nhiễm duy nhất hay không.
- Mô hình cục bộ:

$$
\frac{dI}{dt}=f(t,I).
$$

- Giả thiết và giới hạn: ODE xác định bỏ qua yếu tố ngẫu nhiên và sai số đo; với quần thể nhỏ hoặc nhiễu lớn cần mô hình ngẫu nhiên.
- Diễn giải: Tồn tại và duy nhất không bảo đảm mô hình khớp hoàn hảo với thực tế, nhưng bảo đảm mô hình nhất quán về mặt toán học.

### 2. Trực giác bổ sung và các kết nối

Định lý tồn tại và duy nhất đánh dấu bước chuyển từ câu hỏi "giải thế nào?" sang "bài toán có đặt chỉnh không?". Tư duy này xuyên suốt phần còn lại của khóa học: tính tồn tại của dòng động lực học trong hệ ODE, tính đặt chỉnh (well-posedness) của bài toán biên–đầu trong PDE và sự hội tụ của phương pháp số về đúng nghiệm duy nhất. Điều kiện Lipschitz không phải ràng buộc hình thức mà là thước đo định lượng giúp trường hướng không biến đổi quá gắt theo phương đứng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 400)
solutions = [
    np.zeros_like(t),
    np.where(t <= 0.5, 0.0, ((2/3) * (t - 0.5))**1.5),
    np.where(t <= 1.0, 0.0, ((2/3) * (t - 1.0))**1.5),
]

for y in solutions:
    plt.plot(t, y)

plt.title("Nhiều nghiệm của y' = y^(1/3), y(0) = 0")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị minh họa trực quan hiện tượng nhiều quỹ đạo khác nhau cùng xuất phát từ điều kiện đầu $$ y(0)=0 $$ khi điều kiện Lipschitz bị vi phạm.

### 4. Gợi ý tìm thêm mô phỏng

- search: Picard Lindelof visual explanation
- search: nonunique solution y' = y^(1/3)
- search: slope field uniqueness differential equations

### 5. Bài toán mẫu có bối cảnh thực

Với bài toán $$ y'=t+y $$, $$ y(0)=1 $$, bên cạnh nhân tử tích phân ta có thể dựng dãy lặp Picard:

$$
y_{n+1}(t)=1+\int_0^t \left(s+y_n(s)\right)\,ds, \qquad y_0(t)=1.
$$

Hai xấp xỉ đầu tiên là

$$
y_1(t)=1+t+\frac{t^2}{2}, \qquad y_2(t)=1+t+t^2+\frac{t^3}{6}.
$$

Phép lặp này cho thấy định lý Picard–Lindelöf không chỉ khẳng định nghiệm tồn tại mà còn cung cấp một quy trình xây dựng dãy hàm hội tụ về nghiệm.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ ba câu hỏi: nghiệm có tồn tại không, có duy nhất không và có tồn tại toàn cục không.

**Bậc sau đại học.** Nghiên cứu nguyên lý ánh xạ co Banach, phép lặp Picard, điều kiện Carathéodory và các điều kiện yếu hơn Lipschitz vẫn bảo đảm tính duy nhất, làm nền cho tính đặt chỉnh (well-posedness) của PDE.

## Video tham khảo

- Xem trước: [The Big Theorem of Differential Equations: Existence & Uniqueness](https://www.youtube.com/watch?v=_WpncZ3RkTg) — Dr. Trefor Bazett, tiếng Anh. Trình bày định lý Picard–Lindelöf về tồn tại và duy nhất cục bộ khi $$ f $$ Lipschitz theo $$ y $$.
- [Picard Iteration: An Example](https://www.youtube.com/watch?v=00DTrCST-zA) — Mike, the Mathematician, tiếng Anh. Tính tường minh một ví dụ lặp Picard để cụ thể hóa ý tưởng ánh xạ co.
- [The Geometric Meaning of Differential Equations // Slope Fields, Integral Curves & Isoclines](https://www.youtube.com/watch?v=ccDMpj2UK_M) — Dr. Trefor Bazett, tiếng Anh. Minh họa trực giác hình học về trường hướng và tính duy nhất của đường cong tích phân.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày chuẩn xác định lý Picard–Lindelöf cùng các phản ví dụ kinh điển.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ cụ thể để rèn cách kiểm tra giả thiết định lý.
- Ross — *Differential Equations*: hữu ích để ôn tập sự phân biệt giữa tồn tại, duy nhất và khoảng tồn tại cực đại.
