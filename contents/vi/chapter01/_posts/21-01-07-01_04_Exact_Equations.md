---
layout: post
title: "01-04 Phương trình Toàn phần"
chapter: '01'
order: 4
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Hãy tưởng tượng bạn đang đi bộ trên một sườn núi có độ cao $F(x, y)$ sao cho độ cao không bao giờ đổi—nghĩa là bạn đang đi dọc theo một **đường đồng mức** $F(x, y) = C$. Khi lấy vi phân toàn phần $dF = F_x\,dx + F_y\,dy = 0$, ta thu được ngay một **phương trình vi phân toàn phần**! Giải phương trình toàn phần thực chất chính là bài toán ngược đầy thú vị: từ bản đồ độ dốc $(M, N)$, dựng lại địa hình $F(x, y)$ bị ẩn giấu.

## Bản đồ kiến thức nền: Bốn trụ cột của Phương trình Toàn phần

1. **Dạng vi phân $M(x, y)\,dx + N(x, y)\,dy = 0$**:
   Xem $x$ và $y$ bình đẳng nhau; nghiệm tổng quát là họ các đường mức $F(x, y) = C$ của một hàm thế $F$.
2. **Tiêu chuẩn toàn phần ($M_y = N_x$)**:
   Trên miền đơn liên, điều kiện cần và đủ để tồn tại hàm thế $F$ sao cho $F_x = M$ và $F_y = N$ chính là tính đối xứng đạo hàm hỗn hợp $M_y = N_x$ (định lý Clairaut–Schwarz).
3. **Quy trình dựng hàm thế $F(x, y)$**:
   Tích phân $M$ theo $x$ để được $F(x, y) = \int M\,dx + g(y)$, rồi lấy đạo hàm theo $y$ đối chiếu với $N(x, y)$ để tìm hàm "hằng số tích phân" $g(y)$.
4. **Thừa số tích phân đặc biệt $\mu(x)$ hoặc $\mu(y)$**:
   Khi $M_y \ne N_x$, nếu $\frac{M_y - N_x}{N}$ chỉ phụ thuộc $x$ (hoặc $\frac{N_x - M_y}{M}$ chỉ phụ thuộc $y$), ta nhân thêm thừa số tích phân để "chữa lành" phương trình thành toàn phần!

## Mục tiêu
Bài học này giúp sinh viên hiểu phương trình vi phân toàn phần (exact equation) như bài toán tìm một hàm thế ẩn phía sau biểu thức vi phân, nắm điều kiện kiểm tra tính toàn phần và giải được các ODE dạng

$$
M(t,y)dt+N(t,y)dy=0.
$$

Qua đó, sinh viên nhận ra mối liên hệ giữa phương trình toàn phần, vi phân toàn phần trong giải tích nhiều biến và các đại lượng bảo toàn trong mô hình vật lý.

## Kiến thức nền
Sinh viên cần nắm vững đạo hàm riêng, quy tắc vi phân toàn phần của hàm nhiều biến và khái niệm gradient. Ghi nhớ đẳng thức

$$
dF=F_tdt+F_y dy
$$

là chìa khóa để kết nối tự nhiên giữa giải tích nhiều biến và bài học này.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-04 Phương trình Toàn phần]({{ site.imgurl }}/chapter_img/chapter01/01_04_exact_equations.svg)

Trong cơ học, nhiều hệ bảo toàn có một đại lượng không đổi dọc theo quỹ đạo như cơ năng. Trong nhiệt động lực học, ta phân biệt rõ vi phân toàn phần của hàm trạng thái với vi phân phụ thuộc quá trình. Trong giải tích nhiều biến, câu hỏi liệu một trường vector có phải là gradient của một hàm thế hay không là một bài toán trung tâm. Phương trình vi phân toàn phần gắn kết tất cả những ý tưởng đó trong bối cảnh ODE cấp một.

Thay vì tìm cách giải trực tiếp $$ y(t) $$, ta đặt câu hỏi: biểu thức $$ M(t,y)dt+N(t,y)dy $$ có phải là vi phân toàn phần của một hàm vô hướng $$ F(t,y) $$ hay không? Nếu câu trả lời là có, phương trình lập tức quy về $$ dF=0 $$, tức là $$ F(t,y)=C $$.

### Khung giải thích (nên đọc chậm): Dựng hàm thế $F(x, y)$ bằng tay cho $(2xy + 3)\,dx + (x^2 - 1)\,dy = 0$

1. **Kiểm tra điều kiện toàn phần**:
   - $M(x, y) = 2xy + 3 \implies M_y = 2x$.
   - $N(x, y) = x^2 - 1 \implies N_x = 2x$.
   Vì $M_y = N_x = 2x$, phương trình là **toàn phần** trên toàn $\mathbb{R}^2$.
2. **Tích phân $M$ theo $x$** (coi $y$ là hằng số):
   $$F(x, y) = \int (2xy + 3)\,dx = x^2 y + 3x + g(y).$$
3. **Tìm $g(y)$ bằng cách đối chiếu $F_y = N$**:
   $$F_y(x, y) = x^2 + g'(y) \stackrel{!}{=} x^2 - 1 \implies g'(y) = -1 \implies g(y) = -y.$$
   (Lưu ý: mọi số hạng chứa $x$ phải triệt tiêu sạch khi tìm $g'(y)$—nếu còn sót $x$, chắc chắn có lỗi tính toán!).
4. **Nghiệm tổng quát**: $x^2 y + 3x - y = C$, hay giải tường minh $y(x) = \mathbf{\frac{C - 3x}{x^2 - 1}}$.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung bạn di chuyển trên một bề mặt địa hình có độ cao mô tả bởi hàm thế $$ F(t,y) $$. Nếu sự thay đổi vi phân dọc theo hướng đi luôn bằng $$ 0 $$, bạn đang đi dọc theo một đường đồng mức giữ nguyên độ cao. Phương trình toàn phần vận hành theo đúng nguyên tắc đó: mọi đường cong nghiệm đều là các đường mức của hàm thế $$ F $$.

### Cách nhìn hình ảnh
Nếu tồn tại hàm $$ F(t,y) $$ sao cho $$ F_t=M $$ và $$ F_y=N $$, thì họ nghiệm của ODE chính là họ đường đồng mức $$ F(t,y)=C $$ trên mặt phẳng $$ \left(t,y\right) $$. Cách nhìn hình học này giải thích vì sao nghiệm của phương trình toàn phần thường xuất hiện tự nhiên ở dạng ẩn.

### Cách nhìn hình thức
Phương trình

$$
M(t,y)dt+N(t,y)dy=0
$$

được gọi là phương trình toàn phần nếu tồn tại hàm khả vi $$ F(t,y) $$ sao cho

$$
dF=F_tdt+F_y dy=Mdt+Ndy,
$$

tức là $$ F_t=M $$ và $$ F_y=N $$. Khi đó nghiệm tổng quát được cho bởi $$ F(t,y)=C $$. Trên một miền đơn liên mà $$ M, N $$ có các đạo hàm riêng cấp một liên tục, điều kiện cần và đủ để phương trình toàn phần là

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial t}.
$$

## Ý tưởng toán học cốt lõi
Về bản chất, ta đang kiểm tra xem trường vector $$ \left(M,N\right) $$ có phải là trường gradient của một hàm thế vô hướng hay không. Nếu tồn tại hàm thế $$ F $$ khả vi liên tục cấp hai, định lý Schwarz về đạo hàm riêng hỗn hợp cho $$ F_{ty}=F_{yt} $$, dẫn trực tiếp tới điều kiện $$ M_y=N_t $$. Trên miền đơn liên, điều kiện này cũng là điều kiện đủ để tích phân đường không phụ thuộc đường đi và ta có thể dựng lại hàm thế $$ F(t,y) $$.

## Những ngộ nhận thường gặp
- "Cứ viết được dưới dạng $$ Mdt+Ndy=0 $$ thì là phương trình toàn phần." Sai. Mọi ODE cấp một đều có thể viết lại dưới dạng vi phân, nhưng chỉ những phương trình thỏa mãn tồn tại hàm thế mới là toàn phần.
- "Chỉ cần kiểm tra $$ M_y=N_t $$ là đủ trên mọi miền." Chưa chặt chẽ. Điều kiện đủ còn đòi hỏi tính đơn liên của miền xét.
- "Tích phân $$ M $$ theo $$ t $$ xong là tìm được $$ F(t,y) $$." Sai. Khi tích phân theo $$ t $$ (coi $$ y $$ như hằng số), phần hằng số tích phân thực chất có thể là một hàm $$ \phi(y) $$, cần xác định tiếp bằng điều kiện $$ F_y=N $$.
- "Nghiệm ở dạng ẩn $$ F(t,y)=C $$ là chưa giải xong." Sai. Với phương trình toàn phần, nghiệm ẩn theo đường mức chính là dạng chuẩn và tự nhiên nhất.

## Tiến trình học tập đề xuất

### Bước 1: Đưa về dạng vi phân
Viết phương trình đúng dạng chuẩn $$ M(t,y)dt+N(t,y)dy=0 $$ (chú ý dấu của $$ M $$ và $$ N $$).

### Bước 2: Kiểm tra điều kiện toàn phần
Tính $$ M_y $$ và $$ N_t $$ rồi so sánh hai biểu thức.

### Bước 3: Dựng hàm thế $$ F $$
Tích phân $$ M $$ theo $$ t $$ (thêm hàm phụ $$ \phi(y) $$), hoặc tích phân $$ N $$ theo $$ y $$ (thêm hàm phụ $$ \psi(t) $$).

### Bước 4: Khớp đạo hàm riêng còn lại
Lấy đạo hàm theo biến còn lại rồi đối chiếu với hệ số tương ứng để xác định hàm phụ.

### Bước 5: Viết họ nghiệm đường mức
Kết luận nghiệm tổng quát $$ F(t,y)=C $$ và áp dụng điều kiện đầu (nếu có) để tìm $$ C $$.

### Các checkpoint
- Bạn có giải thích được vì sao "hằng số tích phân" theo $$ t $$ lại có thể là một hàm theo $$ y $$ không?
- Bạn có phân biệt được "dạng vi phân" với "tính toàn phần" không?
- Bạn có nhận thức đúng rằng nghiệm ẩn $$ F(t,y)=C $$ là lời giải hoàn chỉnh của bài toán không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phương trình toàn phần cơ bản
Xét phương trình

$$
\left(2ty+y^2\right)dt+\left(t^2+2ty\right)dy=0.
$$

Với $$ M(t,y)=2ty+y^2 $$ và $$ N(t,y)=t^2+2ty $$, ta có

$$
M_y=2t+2y,\qquad N_t=2t+2y.
$$

Vì $$ M_y=N_t $$ trên toàn $$ \mathbb{R}^2 $$, phương trình là toàn phần. Tích phân $$ M $$ theo $$ t $$ ta được

$$
F(t,y)=\int \left(2ty+y^2\right)dt=t^2y+ty^2+\phi(y).
$$

Lấy đạo hàm riêng theo $$ y $$ cho $$ F_y=t^2+2ty+\phi'(y) $$. So sánh với $$ N=t^2+2ty $$ suy ra $$ \phi'(y)=0 $$, nên chọn $$ \phi(y)=0 $$. Vậy $$ F(t,y)=t^2y+ty^2 $$ và nghiệm tổng quát là

$$
t^2y+ty^2=C.
$$

### Ví dụ 2: Bài toán có điều kiện đầu
Giải bài toán

$$
\left(3t^2+2y\right)dt+\left(2t+4y^3\right)dy=0,\qquad y(0)=1.
$$

Ta có $$ M_y=2 $$ và $$ N_t=2 $$, nên phương trình là toàn phần. Tích phân $$ M $$ theo $$ t $$ thu được $$ F(t,y)=t^3+2ty+\phi(y) $$. Lấy đạo hàm theo $$ y $$ cho $$ F_y=2t+\phi'(y) $$; đối chiếu với $$ N=2t+4y^3 $$ ta có $$ \phi'(y)=4y^3 $$, suy ra $$ \phi(y)=y^4 $$. Do đó $$ F(t,y)=t^3+2ty+y^4 $$ và nghiệm tổng quát là

$$
t^3+2ty+y^4=C.
$$

Thay điều kiện đầu $$ t=0 $$, $$ y=1 $$ ta được $$ C=1 $$, vậy nghiệm riêng là

$$
t^3+2ty+y^4=1.
$$

### Ví dụ 3: Phương trình đơn giản nhưng toàn phần
Xét phương trình

$$
\left(y+t\right)dt+t\,dy=0.
$$

Tính đạo hàm riêng cho $$ M_y=1 $$ và $$ N_t=1 $$, nên phương trình là toàn phần. Tích phân $$ M $$ theo $$ t $$ cho $$ F=ty+\frac{t^2}{2}+\phi(y) $$, suy ra $$ F_y=t+\phi'(y) $$. Vì $$ N=t $$ nên $$ \phi'(y)=0 $$, và nghiệm tổng quát là

$$
ty+\frac{t^2}{2}=C.
$$

Ví dụ này nhắc rằng luôn cần kiểm tra tính toàn phần bằng đạo hàm riêng thay vì đoán cảm tính.

### Ví dụ 4: Phương trình không toàn phần
Xét phương trình

$$
\left(ty+y\right)dt+t\,dy=0.
$$

Ta có $$ M_y=t+1 $$ nhưng $$ N_t=1 $$. Vì $$ M_y\neq N_t $$, phương trình không toàn phần ở dạng hiện tại. Việc nhận ra phương trình không toàn phần giúp ta dừng đúng lúc và chuyển sang phương pháp khác (như tách biến hoặc tìm nhân tử tích phân) thay vì áp dụng nhầm quy trình.

## Câu hỏi khái niệm
1. Vì sao nghiệm của phương trình toàn phần thường biểu diễn dưới dạng đường mức của một hàm thế?
2. Vì sao sau khi tích phân $$ M(t,y) $$ theo $$ t $$, phần dư lại có thể là một hàm $$ \phi(y) $$ chứ không chỉ là một hằng số?
3. Trong mô hình hóa, sự tồn tại của hàm thế nói lên điều gì về tính bảo toàn của hệ?

## Bài toán ứng dụng
1. Trong cơ học, khi tổng năng lượng được bảo toàn, vì sao các quỹ đạo pha nằm trên các đường mức của hàm năng lượng?
2. Trong nhiệt động lực học, việc một biểu thức vi phân là vi phân toàn phần mang ý nghĩa vật lý gì đối với đại lượng trạng thái?
3. Nếu một trường lực không phải là gradient của thế năng, công của lực đó khi dịch chuyển giữa hai điểm có tính chất gì?

## Chiến lược giảng dạy tương tác
- Cho sinh viên dự đoán nhanh phương trình nào toàn phần trước khi tính $$ M_y $$ và $$ N_t $$ để kiểm chứng trực giác.
- Minh họa một số họ đường mức đơn giản như $$ F(t,y)=t^2+y^2 $$ để sinh viên quen với góc nhìn hình học của nghiệm ẩn.
- Cho các nhóm dựng hàm thế theo cả hai cách (tích phân $$ M $$ theo $$ t $$ hoặc tích phân $$ N $$ theo $$ y $$) rồi đối chiếu kết quả.
- Nhấn mạnh thường xuyên câu hỏi: "Phần thêm vào sau tích phân riêng là hằng số hay hàm của biến còn lại?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng mẫu quy trình cố định năm bước: xác định $$ M, N $$, tính $$ M_y, N_t $$, tích phân một thành phần, bổ sung hàm phụ và khớp lại bằng đạo hàm riêng còn lại.

### Thử thách cho sinh viên khá giỏi
Khảo sát điều kiện hình học của miền để $$ M_y=N_t $$ thực sự đủ cho tính toàn phần, và liên hệ với trường bảo toàn trong giải tích vector (xem phản ví dụ miền có lỗ thủng tại gốc tọa độ).

## Tóm tắt dễ nhớ
Phương trình toàn phần là bài toán tìm hàm thế ẩn $$ F(t,y) $$ sao cho $$ Mdt+Ndy=dF $$, từ đó thu ngay họ nghiệm đường mức $$ F(t,y)=C $$. Khi giải cần luôn kiểm tra $$ M_y=N_t $$, xác định cẩn thận hàm phụ $$ \phi(y) $$ (hoặc $$ \psi(t) $$) và xem nghiệm ẩn là dạng biểu diễn chuẩn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Đường đẳng thế trong cơ học bảo toàn
- Bài toán: Trong hệ cơ học không ma sát, quỹ đạo chuyển động bị ràng buộc bởi định luật bảo toàn năng lượng.
- Mô hình: Nếu $$ F(t,y) $$ là đại lượng bảo toàn, thì

$$
dF=F_t\,dt+F_y\,dy=0
$$

là một phương trình toàn phần.
- Giả thiết và giới hạn: Giả sử hệ bảo toàn năng lượng và không có lực ma sát hay ngoại lực không thế; sự có mặt của ma sát sẽ phá vỡ tính toàn phần này.
- Diễn giải: Quỹ đạo nghiệm nằm trên các đường mức $$ F(t,y)=C $$, gắn trực tiếp hình học nghiệm với hàm năng lượng.

#### Vi phân hàm trạng thái trong nhiệt động lực học
- Bài toán: Phân biệt đại lượng chỉ phụ thuộc trạng thái (như nội năng, entropy) với đại lượng phụ thuộc đường quá trình (như công, nhiệt).
- Mô hình: Biểu thức vi phân

$$
M(T,V)\,dT+N(T,V)\,dV
$$

nếu là vi phân toàn phần thì ứng với một hàm trạng thái.
- Giả thiết và giới hạn: Tính toàn phần phụ thuộc vào hệ biến trạng thái và miền cân bằng nhiệt động; trong quá trình không cân bằng, mô hình này không còn đủ.
- Diễn giải: Tính toàn phần cho biết khi nào độ biến thiên tích lũy chỉ phụ thuộc điểm đầu và điểm cuối chứ không phụ thuộc đường đi.

#### Đường đồng phí trong kinh tế học
- Bài toán: Khảo sát các tổ hợp hai yếu tố đầu vào cho cùng một mức tổng chi phí.
- Mô hình: Với hàm chi phí $$ C(x,y) $$, điều kiện chi phí không đổi viết là

$$
dC=C_x\,dx+C_y\,dy=0.
$$

- Giả thiết và giới hạn: Giả sử hàm chi phí trơn theo hai biến đầu vào liên tục, bỏ qua ràng buộc rời rạc hoặc biến động giá đột ngột.
- Diễn giải: Họ nghiệm của phương trình toàn phần tương ứng trực tiếp với các đường đồng mức của hàm chi phí.

### 2. Trực giác bổ sung và các kết nối

Phương trình toàn phần nối trực tiếp ODE với giải tích nhiều biến. Điều kiện $$ M_y=N_t $$ không chỉ là phép kiểm tra kỹ thuật mà bắt nguồn từ tính đối xứng của đạo hàm riêng hỗn hợp và tính độc lập đường đi của tích phân đường—những ý tưởng sau này mở rộng lên trường bảo toàn và vi phân ngoài.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
T, Y = np.meshgrid(t, y)
F = T**2 * Y + T * Y**2

plt.figure(figsize=(6, 5))
contours = plt.contour(T, Y, F, levels=12, cmap="viridis")
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Các đường mức của F(t, y) = t^2 y + t y^2")
plt.grid(alpha=0.2)
plt.show()
```

Mỗi đường mức trên hình tương ứng với một đường cong nghiệm của phương trình toàn phần $$ dF=0 $$, mang lại trực giác hình học rõ ràng cho nghiệm dạng ẩn.

### 4. Gợi ý tìm thêm mô phỏng

- search: exact differential equations contour plot
- search: conservative vector field potential function
- search: thermodynamics exact differential state function

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình

$$
\left(2ty+y^2\right)dt+\left(t^2+2ty\right)dy=0.
$$

Vì $$ M_y=N_t=2t+2y $$, phương trình là toàn phần với hàm thế $$ F(t,y)=t^2y+ty^2 $$, cho họ nghiệm đường mức $$ t^2y+ty^2=C $$. Trong ứng dụng, giá trị $$ C $$ xác định từ trạng thái ban đầu đóng vai trò như mức năng lượng hay đại lượng bảo toàn của quỹ đạo.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo kiểm tra tính toàn phần, dựng hàm thế và diễn giải nghiệm ẩn theo đường mức.

**Bậc sau đại học.** Kết nối với 1-dạng vi phân đóng và khớp (closed vs. exact 1-forms), miền đơn liên, tích phân đường và kỹ thuật tìm nhân tử tích phân cho phương trình chưa toàn phần.

## Video tham khảo

- Xem trước: [Giải tích 6.2 PTVP Cấp 1: Phương trình Vi phân Toàn phần - Phần 1](https://www.youtube.com/watch?v=KrJzMAG3wUU) — Eureka! Uni, tiếng Việt. Bài giảng tiếng Việt về phương trình vi phân toàn phần cấp một.
- [Exact equations intuition 1 (proofy) | First order differential equations | Khan Academy](https://www.youtube.com/watch?v=iEpqcdaJNTQ) — Khan Academy, tiếng Anh. Giải thích điều kiện toàn phần $$ \partial M/\partial y=\partial N/\partial x $$ và hàm thế đứng sau nó.
- [Exact equations example 1 | First order differential equations | Khan Academy](https://www.youtube.com/watch?v=Pb04ntcDJcQ) — Khan Academy, tiếng Anh. Ví dụ giải chi tiết một phương trình toàn phần kèm bước kiểm tra điều kiện.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần phương trình toàn phần trình bày rõ ràng, phù hợp cho buổi học đầu tiên.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện dựng hàm thế và áp dụng điều kiện đầu.
- Ross — *Differential Equations*: trình bày ngắn gọn, tiện so sánh phương trình toàn phần và không toàn phần.
