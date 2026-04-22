---
layout: post
title: "04-01 Giới thiệu Hệ Phương trình"
chapter: '04'
order: 1
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này mở đầu chương về hệ phương trình vi phân, giúp sinh viên hiểu vì sao nhiều hiện tượng không thể mô tả đầy đủ bằng một ẩn duy nhất, biết cách viết trạng thái dưới dạng vector, và thấy được mối liên hệ giữa phương trình bậc cao và hệ bậc nhất. Sau bài học, sinh viên cần chuyển từ tư duy "một hàm theo thời gian" sang tư duy "toàn bộ trạng thái của hệ tiến hóa theo thời gian".

## Kiến thức nền

Sinh viên nên nắm ODE cấp một, ODE cấp hai, khái niệm điều kiện đầu và một ít đại số tuyến tính cơ bản như vector và ma trận. Trực giác vật lý về vị trí, vận tốc, dòng chảy hoặc nhiều quần thể tương tác cũng rất hữu ích, vì hệ phương trình thường xuất hiện khi một đại lượng không đủ để kể hết câu chuyện động học.

## Dẫn nhập

![Sơ đồ chuyển từ phương trình bậc cao sang hệ trạng thái]({{ site.imgurl }}/chapter_img/chapter04/01_introduction_systems.svg)

Trong các chương trước, ta thường giải một phương trình cho một hàm chưa biết. Nhưng thực tế hiếm khi gói gọn trong một biến duy nhất. Một vật dao động cần cả vị trí lẫn vận tốc. Một mạch điện cần điện tích và dòng điện. Một mô hình sinh thái có thể cần theo dõi nhiều loài cùng lúc. Khi nhiều đại lượng cùng tiến hóa và ảnh hưởng lẫn nhau, cách nhìn tự nhiên nhất không còn là một phương trình, mà là một hệ.

Ý tưởng trung tâm của chương là: hệ phương trình không phải là phiên bản dài dòng hơn của ODE một ẩn, mà là ngôn ngữ đúng cho các mô hình nhiều trạng thái. Một khi ta chấp nhận nhìn trạng thái như một vector, rất nhiều công cụ mạnh xuất hiện: ma trận, trị riêng, chân dung pha, ma trận mũ và cuối cùng là cách đọc hình học của động lực học.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một hệ phương trình giống như một đội nhiều người đang cùng di chuyển, trong đó mỗi người không chỉ phụ thuộc vào bản thân mình mà còn phụ thuộc vào vị trí và chuyển động của những người khác. Ta không thể hiểu đội hình bằng cách theo dõi riêng từng người mà phải theo dõi toàn bộ cấu hình.

### Cách nhìn hình ảnh

Nếu một ODE một ẩn cho quỹ đạo trên mặt phẳng $$ \left(t,y\right) $$, thì hệ hai ẩn cho quỹ đạo trong mặt phẳng trạng thái $$ \left(x_1,x_2\right) $$, hệ ba ẩn cho quỹ đạo trong không gian ba chiều, và nói chung là trong không gian trạng thái $$ \mathbb{R}^n $$. Khi đó nghiệm không chỉ là đồ thị theo thời gian, mà là một đường cong trạng thái cho thấy hệ đi qua những cấu hình nào.

### Cách nhìn hình thức

Một hệ vi phân cấp một tổng quát có dạng
$$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}), $$
trong đó
$$
\mathbf{x}(t)=
\begin{pmatrix}
x_1(t)\\
x_2(t)\\
\vdots\\
x_n(t)
\end{pmatrix}.
$$
Nếu phương trình bậc $$ n $$
$$ y^{(n)}=F\left(t,y,y',\ldots,y^{(n-1)}\right) $$
được đặt với
$$
x_1=y,\quad x_2=y',\quad \ldots,\quad x_n=y^{(n-1)},
$$
thì nó trở thành hệ bậc nhất:
$$
\begin{cases}
x_1'=x_2,\\
x_2'=x_3,\\
\vdots\\
x_{n-1}'=x_n,\\
x_n'=F(t,x_1,\ldots,x_n).
\end{cases}
$$

## Những ngộ nhận thường gặp

- "Hệ phương trình chỉ là cách viết khác của ODE bậc cao." Sai. Chúng tương đương về dữ liệu, nhưng hệ làm lộ ra cấu trúc trạng thái và tương tác tốt hơn nhiều.
- "Mỗi phương trình trong hệ có thể được hiểu riêng rẽ." Không đúng. Ý nghĩa thực sự nằm ở sự ghép nối giữa các thành phần.
- "Trạng thái chỉ là giá trị của biến chính." Sai. Trạng thái gồm toàn bộ thông tin cần để dự đoán tương lai, thường là nhiều biến cùng lúc.
- "Chỉ hệ phi tuyến mới thú vị." Sai. Ngay cả hệ tuyến tính đã cho ta hình học và động lực học rất phong phú.

## Tiến trình học tập đề xuất

### Bước 1: Nhận ra biến trạng thái

Hỏi xem cần biết những đại lượng nào để dự đoán tương lai của hệ.

### Bước 2: Viết trạng thái dưới dạng vector

Tập cho sinh viên quen với ký hiệu gọn mà giàu ý nghĩa này.

### Bước 3: Từ phương trình bậc cao sang hệ bậc nhất

Đây là cầu nối kỹ thuật quan trọng nhất đầu chương.

### Bước 4: Chuyển từ đồ thị theo thời gian sang quỹ đạo trạng thái

Đây là bước đổi tư duy quan trọng nhất.

### Các checkpoint

- Sinh viên có giải thích được vì sao một hệ cần nhiều biến trạng thái hay không.
- Sinh viên có chuyển đúng một ODE bậc cao về hệ bậc nhất hay không.
- Sinh viên có hiểu quỹ đạo trong không gian trạng thái khác gì đồ thị theo thời gian hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Từ dao động bậc hai sang hệ

Xét phương trình
$$ y''+2y'+5y=0. $$
Đặt
$$ x_1=y,\qquad x_2=y'. $$
Khi đó
$$ x_1'=x_2, $$
và từ phương trình gốc,
$$ x_2'=-2x_2-5x_1. $$
Ta thu được hệ
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
Ví dụ này rất quan trọng vì nó cho sinh viên thấy rõ một ODE bậc hai thật ra là một hệ hai biến trạng thái.

### Ví dụ 2: Mô hình hai quần thể

Giả sử $$ x(t) $$ và $$ y(t) $$ là hai quần thể có tương tác tuyến tính sơ bộ:
$$
\begin{cases}
x'=2x-y,\\
y'=x+3y.
\end{cases}
$$
Ở đây, tốc độ thay đổi của mỗi quần thể phụ thuộc vào cả hai quần thể. Không có cách hợp lý nào để nén bức tranh này vào một ẩn duy nhất mà vẫn giữ trực giác mô hình ban đầu. Đây là ví dụ rất tốt để nhấn mạnh vì sao hệ là ngôn ngữ tự nhiên.

### Ví dụ 3: Trạng thái trong mạch điện

Một mạch LC đơn giản có thể viết thành phương trình bậc hai cho điện tích. Nhưng nếu đặt
$$ x_1=q,\qquad x_2=q', $$
ta có ngay hệ hai chiều, trong đó $$ x_1 $$ là điện tích còn $$ x_2 $$ là dòng điện. Điều này có ý nghĩa vật lý rất mạnh: ta không chỉ biết "mạch đang chứa bao nhiêu điện tích", mà còn biết "điện tích đang thay đổi theo hướng nào".

### Ví dụ 4: Ý nghĩa của điều kiện đầu

Với hệ
$$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}), $$
điều kiện đầu có dạng
$$ \mathbf{x}(t_0)=\mathbf{x}_0. $$
Nghĩa là ta không chỉ biết một số, mà biết toàn bộ cấu hình khởi đầu của hệ. Đây là bản tổng quát hóa rất tự nhiên của bài toán giá trị đầu đã học ở chương trước.

## Câu hỏi khái niệm

1. Vì sao nhiều mô hình vật lý hoặc sinh học buộc phải được viết dưới dạng hệ chứ không thể chỉ bằng một ODE một ẩn?
2. Khi viết một ODE bậc hai thành hệ bậc nhất, điều gì được "lộ ra" về mặt trạng thái?
3. Vì sao quỹ đạo trong không gian trạng thái thường cho trực giác tốt hơn chỉ nhìn đồ thị theo thời gian?

## Bài toán ứng dụng

1. Một xe tự hành cần được mô tả bởi vị trí và vận tốc. Hãy giải thích vì sao chỉ biết vị trí tại một thời điểm là chưa đủ để dự đoán chuyển động tiếp theo.
2. Một mô hình dịch tễ có ba nhóm dân số: nhạy cảm, nhiễm và hồi phục. Hãy giải thích vì sao hệ phương trình là ngôn ngữ đúng.
3. Một mạch điện có điện tích và dòng điện thay đổi theo thời gian. Hãy diễn giải chúng như hai thành phần của một vector trạng thái.

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Muốn dự đoán hoàn toàn tương lai của một vật dao động, chỉ biết vị trí hiện tại có đủ không?"
- Cho sinh viên làm việc theo cặp để chuyển 2 đến 3 ODE bậc hai thành hệ bậc nhất.
- Vẽ đồng thời đồ thị $$ y(t) $$ và quỹ đạo trong mặt phẳng $$ \left(y,y'\right) $$ để lớp thấy sự khác biệt giữa hai cách nhìn.
- Khuyến khích sinh viên giải thích bằng lời ý nghĩa của từng thành phần trong vector trạng thái.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu dùng một mẫu cố định: đặt trạng thái, viết các đạo hàm thấp trước, rồi dùng phương trình gốc cho đạo hàm cuối cùng. Việc lặp đúng khuôn mẫu này sẽ giúp các em bớt sợ ký hiệu vector.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi suy nghĩ xem một hệ bậc nhất hai chiều có thể được nén lại thành một ODE bậc hai trong trường hợp nào, và khi nào việc đó làm mất trực giác mô hình.

## Tóm tắt dễ nhớ

Hệ phương trình là ngôn ngữ của trạng thái nhiều thành phần. Một ODE bậc cao có thể viết thành hệ bậc nhất, nhưng lợi ích lớn hơn là ta nhìn thấy toàn bộ cấu trúc tương tác của hệ. Muốn hiểu một hệ, hãy hỏi: trạng thái gồm những gì, các thành phần ảnh hưởng nhau ra sao, và quỹ đạo trạng thái trông như thế nào.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo của vật bay
- Bài toán: Muốn mô tả một vật trong mặt phẳng, ta không thể chỉ theo dõi một biến; cần cả vị trí và vận tốc theo nhiều hướng.
- Mô hình:
$$
\mathbf{x}(t)=
\begin{pmatrix}
x\\
y\\
v_x\\
v_y
\end{pmatrix},
\qquad
\mathbf{x}'=\mathbf{f}(t,\mathbf{x}).
$$
- Giả thiết và giới hạn: Bỏ qua nhiều chi tiết như lực cản phi tuyến hoặc quay của vật.
- Diễn giải: Hệ phương trình là ngôn ngữ tự nhiên vì trạng thái thật sự có nhiều thành phần gắn kết.

#### Mô hình dịch tễ nhiều ngăn
- Bài toán: Số người nhạy cảm, nhiễm và hồi phục cùng tiến hóa theo thời gian.
- Mô hình:
$$
\frac{dS}{dt}=f_1(S,I,R),\qquad
\frac{dI}{dt}=f_2(S,I,R),\qquad
\frac{dR}{dt}=f_3(S,I,R).
$$
- Giả thiết và giới hạn: Hệ đồng nhất, tham số không đổi, chưa xét cấu trúc tuổi hay không gian.
- Diễn giải: Hệ cho phép đọc tương tác giữa nhiều biến mà một ODE đơn lẻ không thể kể hết.

#### Chuyển ODE bậc cao sang trạng thái
- Bài toán: Một dao động cơ học bậc hai cần được viết lại để dùng công cụ ma trận và hình học pha.
- Mô hình:
$$
y''+2y'+5y=0
\quad\Longrightarrow\quad
\begin{cases}
x_1'=x_2,\\
x_2'=-2x_2-5x_1.
\end{cases}
$$
- Giả thiết và giới hạn: Chỉ thay đổi ngôn ngữ mô tả, không thay đổi nội dung động học.
- Diễn giải: Dạng hệ bậc nhất là cánh cửa vào toàn bộ chương hệ ODE.

### 2. Trực giác bổ sung và các kết nối

Hệ phương trình là bước chuyển từ "một đại lượng biến thiên" sang "một trạng thái nhiều chiều". Đây là thay đổi tư duy quan trọng hơn chính kỹ thuật biến đổi. Bài học này nối trực tiếp với chương trước vì mọi ODE bậc cao đều có thể được xem như hệ bậc nhất, và nó cũng chuẩn bị cho hình học của chân dung pha cùng phổ ma trận ở các bài sau. Một bẫy phổ biến là cố đọc từng phương trình thành phần như các bài toán riêng; ý nghĩa thật sự nằm ở sự ghép nối của toàn bộ hệ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, X):
    x1, x2 = X
    return [x2, -2*x2 - 5*x1]

t = np.linspace(0, 12, 600)
for x10, x20 in [(1, 0), (0, 1), (1, -1)]:
    sol = solve_ivp(system, [0, 12], [x10, x20], t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f"IC=({x10},{x20})")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Quỹ đạo trạng thái của hệ bậc nhất tương đương")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: state space intuition differential equations
- search: converting second order ODE to first order system
- search: phase trajectory system of ODEs visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét dao động
$$ y''+2y'+5y=0. $$
Đặt
$$ x_1=y,\qquad x_2=y', $$
ta được hệ
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
Trạng thái ban đầu
$$ y(0)=1,\qquad y'(0)=0 $$
tương ứng với
$$
\mathbf{x}(0)=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Ví dụ này cho thấy một ODE bậc hai không mất đi nội dung khi chuyển về hệ; trái lại, nó trở nên minh bạch hơn về mặt trạng thái.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào việc chọn đúng biến trạng thái và chuyển ODE bậc cao thành hệ bậc nhất.

**Bậc sau đại học.** Nhấn mạnh không gian trạng thái, dòng chảy động lực học và quan điểm hệ như một toán tử tiến hóa trên $$ \mathbb{R}^n $$.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: phần mở đầu rất tốt cho việc chuyển từ ODE bậc cao sang hệ trạng thái.
- Arnold, *Ordinary Differential Equations*: cho trực giác hình học sâu về hệ và không gian trạng thái.
