---
layout: post
title: "01-01 Giới thiệu Phương trình Vi phân"
chapter: '01'
order: 1
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Tự nhiên hiếm khi nói thẳng cho ta biết vị trí của một hành tinh hay nhiệt độ của một tách cà phê tại mọi thời điểm; thay vào đó, tự nhiên chỉ tiết lộ **quy luật thay đổi** của chúng ngay tại khoảnh khắc hiện tại. Phương trình vi phân chính là ngôn ngữ dịch những quy luật thay đổi cục bộ đó thành dự đoán toàn cục theo thời gian!

## Kiến thức cần nhớ: Bốn viên gạch đầu tiên của Phương trình Vi phân

1. **Phân loại ODE vs. PDE**:
   Phương trình vi phân thường (ODE) chỉ có **một biến độc lập** (thường là thời gian $t$); phương trình đạo hàm riêng (PDE) có từ hai biến độc lập trở lên (như vị trí $x$ và thời gian $t$).
2. **Bậc (Order) & Tính tuyến tính (Linearity)**:
   Bậc là cấp đạo hàm cao nhất xuất hiện trong phương trình; phương trình tuyến tính chỉ chứa $y, y', y'', \dots$ ở bậc nhất và không nhân chúng với nhau—đây là đường ranh phân chia phương pháp giải.
3. **Nghiệm tổng quát, Nghiệm riêng & Bài toán giá trị đầu (IVP)**:
   PTVP cấp $n$ thường chứa $n$ hằng số tùy ý tạo thành một họ đường cong; gắn thêm $n$ điều kiện ban đầu (IVP) sẽ ghim chặt duy nhất một quỹ đạo vật lý.
4. **Trường hướng (Direction Field)**:
   Cho phép "nhìn thấy" hình dạng nghiệm trực tiếp từ phương trình $y' = f(t, y)$ ngay cả trước khi đặt bút giải.

## Mục tiêu
Bài học này giúp sinh viên hiểu phương trình vi phân như một quy luật mô tả sự biến thiên, biết phân loại phương trình vi phân thường (ODE) theo bậc, tính tuyến tính, tính tự trị và điều kiện đầu, đồng thời tập nhìn nghiệm không chỉ như một công thức đại số mà như quỹ đạo tiến hóa của một quá trình thực. Sau bài học, sinh viên sẽ thấy rõ vì sao phương trình vi phân xuất hiện tự nhiên trong khoa học, kỹ thuật, kinh tế và sinh học.

## Kiến thức nền
Sinh viên cần nắm vững đạo hàm, tích phân, ý nghĩa hình học của hệ số góc tiếp tuyến cùng các hàm sơ cấp (đa thức, hàm mũ, logarit, lượng giác). Kỹ năng giải phương trình đại số cơ bản và đọc đồ thị hàm số cũng rất cần thiết vì trong ODE ta thường xuyên chuyển đổi giữa biểu thức giải tích, đồ thị và diễn giải định tính.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-01 Giới thiệu Phương trình Vi phân]({{ site.imgurl }}/chapter_img/chapter01/01_01_introduction_to_des.svg)

Khi một cốc cà phê nguội dần, điều quyết định quá trình không chỉ là nhiệt độ tại một thời điểm mà là tốc độ nguội đi tỉ lệ với chênh lệch nhiệt độ so với môi trường. Khi một quần thể vi khuẩn sinh trưởng, ta quan tâm tốc độ tăng số lượng ở mỗi thời điểm. Khi một tài khoản ngân hàng sinh lãi liên tục, quỹ đạo số dư được chi phối bởi tốc độ tăng tỉ lệ với chính số dư hiện có. Các tình huống này đều dẫn đến một câu hỏi chung: đại lượng cần tìm biến thiên theo quy luật nào?

Phương trình vi phân là ngôn ngữ toán học trả lời câu hỏi đó. Thay vì cho trực tiếp giá trị của hàm số, nó đưa ra mối liên hệ giữa hàm số và đạo hàm của nó. Vì vậy, giải một ODE không chỉ là thao tác biến đổi ký hiệu mà là quá trình tái dựng quỹ đạo, sự tích lũy hoặc cơ chế phản hồi từ thông tin về tốc độ biến thiên.

### Giải thích: Kiểm chứng nghiệm và ghim hằng số cho bài toán làm nguội Newton $T'(t) = -0{,}2(T - 20),\; T(0) = 90$

Giả sử một tách cà phê $90^\circ\text{C}$ đặt trong phòng $20^\circ\text{C}$, và ta nghi ngờ nghiệm có dạng $T(t) = 20 + C e^{-0{,}2 t}$:
1. **Kiểm tra vế trái (đạo hàm)**: $T'(t) = -0{,}2 C e^{-0{,}2 t}$.
2. **Kiểm tra vế phải**: $-0{,}2(T(t) - 20) = -0{,}2(C e^{-0{,}2 t}) = -0{,}2 C e^{-0{,}2 t}$. Hai vế khớp nhau với mọi $C \in \mathbb{R}$!
3. **Áp dụng điều kiện đầu $T(0) = 90$**:
   $$20 + C e^0 = 90 \implies C = \mathbf{70}.$$
4. **Dự đoán thực tế**: Sau $t = 5$ phút, nhiệt độ tách cà phê là:
   $$T(5) = 20 + 70 e^{-1} \approx 20 + 70(0{,}3679) \approx \mathbf{45{,}75^\circ\text{C}}.$$

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung bạn đang lái xe trên một mặt phẳng nhưng không có sẵn bản đồ toàn tuyến, mà chỉ biết tại mỗi vị trí cần đánh lái theo hướng nào. Nếu biết hướng đi tại mọi điểm và biết điểm xuất phát, về nguyên tắc ta có thể dựng lại toàn bộ quỹ đạo. Phương trình vi phân cấp một cung cấp đúng thông tin về "hướng di chuyển cục bộ" đó của nghiệm.

### Cách nhìn hình ảnh
Một công cụ trực quan quan trọng là trường hướng (slope field). Với phương trình

$$
\frac{dy}{dt}=f(t,y),
$$

ta vẽ tại mỗi điểm $$ \left(t,y\right) $$ một đoạn thẳng nhỏ có hệ số góc bằng $$ f(t,y) $$. Các đường cong nghiệm luôn tiếp xúc với các đoạn thẳng này tại mọi điểm đi qua. Với phương trình $$ \frac{dy}{dt}=y $$, các đoạn hướng dốc lên khi $$ y>0 $$, dốc xuống khi $$ y<0 $$ và nằm ngang dọc theo đường $$ y=0 $$. Chỉ từ trường hướng, ta đã thấy ngay nghiệm dương tăng lên, nghiệm âm giảm về $$ -\infty $$, còn $$ y=0 $$ là nghiệm cân bằng.

### Cách nhìn hình thức
Phương trình vi phân thường (ODE) là phương trình liên hệ giữa một hàm ẩn một biến và ít nhất một đạo hàm của nó. Trong chương này, ta tập trung vào phương trình vi phân thường cấp một có dạng

$$
\frac{dy}{dt}=f(t,y).
$$

Bậc của phương trình là bậc của đạo hàm cao nhất xuất hiện trong phương trình (bậc một, bậc hai, v.v.). Một nghiệm của phương trình là một hàm khả vi $$ y(t) $$ thỏa mãn đẳng thức trên một khoảng xác định nào đó.

## Các ý niệm cốt lõi cần nhận biết
Khi phân tích một ODE, ta thường kiểm tra bốn đặc trưng cơ bản: phương trình có bậc mấy? Tuyến tính hay phi tuyến? Tự trị hay phụ thuộc tường minh vào biến độc lập? Có đi kèm điều kiện đầu hay không?

Phương trình $$ \frac{dy}{dt}+p(t)y=q(t) $$ là phương trình tuyến tính cấp một vì $$ y $$ và $$ \frac{dy}{dt} $$ chỉ xuất hiện ở bậc nhất và không nhân với nhau. Ngược lại, $$ \frac{dy}{dt}=y^2-t $$ là phương trình phi tuyến do có số hạng $$ y^2 $$. Phương trình $$ \frac{dy}{dt}=f(y) $$ được gọi là tự trị vì vế phải không phụ thuộc tường minh vào biến thời gian $$ t $$.

Điều kiện đầu $$ y(t_0)=y_0 $$ chọn ra một nghiệm cụ thể trong họ nghiệm tổng quát. Không có điều kiện đầu, ODE mô tả cả một họ quỹ đạo khả dĩ; khi gắn thêm điều kiện đầu, ta xác định quỹ đạo tương ứng với một trạng thái xuất phát cụ thể của hệ.

## Những ngộ nhận thường gặp
- "Mọi phương trình vi phân đều giải ra được công thức tường minh." Sai. Rất nhiều ODE quan trọng không có nghiệm sơ cấp dạng đóng mà phải phân tích định tính hoặc giải gần đúng bằng phương pháp số.
- "Đạo hàm trong ODE chỉ là ký hiệu hình thức." Sai. Trong mô hình hóa, đạo hàm biểu diễn tốc độ biến thiên tức thời và thường mang ý nghĩa vật lý trực tiếp.
- "Chỉ cần tìm được một công thức thỏa mãn phương trình là hoàn tất." Chưa đủ. Ta cần xem xét miền xác định, điều kiện đầu và tính hợp lý của nghiệm trong bối cảnh bài toán.
- "Hai đường cong nghiệm khác nhau có thể cắt nhau tại một điểm bất kỳ." Sai trong các bài toán giá trị đầu thỏa mãn điều kiện duy nhất nghiệm: khi đó qua mỗi điểm chỉ có đúng một đường cong nghiệm đi qua.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại ý nghĩa đạo hàm như tốc độ biến thiên
Kết nối trực giác từ giải tích: đạo hàm đo tốc độ thay đổi tức thời, còn tích phân đo lượng thay đổi tích lũy.

### Bước 2: Đọc phương trình như một quy luật tiến hóa
Thay vì vội hỏi "công thức nghiệm là gì?", hãy hỏi "hệ đang thay đổi theo quy luật nào?". Đây là bước chuyển tư duy quan trọng ở đầu chương.

### Bước 3: Phân loại cấu trúc phương trình
Luyện nhận diện nhanh bậc, tính tuyến tính và tính tự trị để định hướng phương pháp giải phù hợp ở các bài sau.

### Bước 4: Gắn điều kiện đầu
Từ họ nghiệm tổng quát, sử dụng dữ kiện ban đầu để xác định nghiệm riêng của bài toán.

### Các checkpoint
- Bạn có diễn giải được bằng lời ý nghĩa của phương trình $$ \frac{dy}{dt}=f(t,y) $$ không?
- Bạn có phân biệt được phương trình tuyến tính với phi tuyến qua các ví dụ cơ bản không?
- Bạn có giải thích được vì sao điều kiện đầu là thành phần thiết yếu của mô hình chứ không phải chi tiết phụ không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Kiểm tra một hàm có phải là nghiệm hay không
Xét phương trình $$ \frac{dy}{dt}=2t $$ và hàm thử $$ y=t^2+3 $$. Lấy đạo hàm ta được $$ \frac{dy}{dt}=2t $$, nên hàm này là một nghiệm của phương trình. Nếu đi kèm điều kiện đầu $$ y(0)=3 $$ thì nghiệm thỏa mãn; nhưng nếu điều kiện đầu là $$ y(0)=1 $$ thì không thỏa mãn, dù vẫn là nghiệm của ODE. Ví dụ này nhấn mạnh sự khác biệt giữa phương trình vi phân và bài toán giá trị đầu.

### Ví dụ 2: Từ quy luật tăng trưởng đến họ nghiệm
Xét phương trình $$ \frac{dy}{dt}=ky $$. Vì hàm mũ có đạo hàm tỉ lệ với chính nó, ta thử dạng $$ y=Ce^{kt} $$. Lấy đạo hàm ta thu được $$ \frac{dy}{dt}=kCe^{kt}=ky $$, nên họ nghiệm tổng quát là $$ y(t)=Ce^{kt} $$. Nếu $$ k>0 $$, nghiệm tăng theo hàm mũ; nếu $$ k<0 $$, nghiệm suy giảm dần về $$ 0 $$. Cùng một cấu trúc công thức nhưng dấu của tham số quyết định hành vi định tính hoàn toàn khác nhau.

### Ví dụ 3: Phân loại phương trình
Xét ba phương trình:

$$
\frac{dy}{dt}+3y=t, \qquad \frac{dy}{dt}=y(1-y), \qquad \frac{d^2x}{dt^2}+\omega^2 x=0.
$$

Phương trình thứ nhất là tuyến tính cấp một, không tự trị; phương trình thứ hai là phi tuyến cấp một, tự trị; phương trình thứ ba là tuyến tính cấp hai. Nhận diện đúng loại phương trình ngay từ đầu giúp chọn đúng kỹ thuật giải ở các bài tiếp theo.

### Ví dụ 4: Đọc trường hướng đơn giản
Với phương trình $$ \frac{dy}{dt}=t-y $$, hệ số góc tại $$ \left(0,0\right) $$ bằng $$ 0 $$, tại $$ \left(1,0\right) $$ bằng $$ 1 $$, còn tại $$ \left(0,1\right) $$ bằng $$ -1 $$. Do đó, ở phía dưới đường thẳng $$ y=t $$ (nơi $$ t-y>0 $$), đường cong nghiệm đi lên; ở phía trên đường thẳng $$ y=t $$ (nơi $$ t-y<0 $$), đường cong nghiệm đi xuống. Ngay cả khi chưa giải tường minh, ta đã nắm được xu hướng định tính của nghiệm.

## Câu hỏi khái niệm
1. Vì sao nên đọc một phương trình vi phân như một quy luật biến thiên thay vì một phương trình đại số thông thường?
2. Vì sao hai phương trình có hình thức gần giống nhau vẫn có thể đòi hỏi những phương pháp giải hoàn toàn khác nhau?
3. Điều kiện đầu ảnh hưởng như thế nào đến ý nghĩa thực tế của cùng một phương trình vi phân?

## Bài toán ứng dụng
1. Nhiệt độ của một vật giảm với tốc độ tỉ lệ với hiệu nhiệt độ giữa vật và môi trường. Hãy giải thích bằng lời vì sao hiện tượng này dẫn đến một ODE cấp một.
2. Một tài khoản đầu tư sinh lãi liên tục với lãi suất không đổi. Hãy giải thích vì sao tốc độ tăng số dư phải tỉ lệ với số dư hiện tại.
3. Một quần thể vi khuẩn nuôi trong bình kín ban đầu tăng nhanh nhưng về sau chậm dần. Hãy nhận xét vì sao mô hình $$ \frac{dP}{dt}=kP $$ không còn phù hợp ở giai đoạn sau.

## Chiến lược giảng dạy tương tác
- Mở đầu buổi học bằng câu hỏi: "Nếu chỉ biết vận tốc tại mọi thời điểm và vị trí xuất phát, ta có dựng lại được quỹ đạo chuyển động không?"
- Cho sinh viên làm việc theo cặp để phân loại 6–8 phương trình theo các tiêu chí: bậc, tuyến tính/phi tuyến, tự trị/không tự trị và có/không có điều kiện đầu.
- Chiếu một trường hướng đơn giản để cả lớp dự đoán nghiệm tăng, nghiệm giảm và nghiệm cân bằng trước khi giải đại số.
- Yêu cầu sinh viên diễn đạt bằng lời ý nghĩa từng số hạng trong phương trình thay vì chỉ đọc ký hiệu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng bảng hai cột gồm "ký hiệu" và "ý nghĩa thực tế" (chẳng hạn $$ \frac{dy}{dt} $$ là tốc độ thay đổi, $$ y(0)=2 $$ là trạng thái ban đầu), kết hợp với các ví dụ quen thuộc như nhiệt độ, số dư tiền gửi hoặc mực nước trong bể.

### Thử thách cho sinh viên khá giỏi
So sánh hai góc nhìn "nghiệm là đồ thị hàm số" và "nghiệm là quỹ đạo tiếp xúc với trường hướng", đồng thời phân tích vì sao một phương trình không có nghiệm dạng đóng vẫn hữu ích trong mô hình hóa khi kết hợp với phân tích định tính và mô phỏng số.

## Tóm tắt dễ nhớ
Phương trình vi phân không cho trực tiếp giá trị của đại lượng mà cho quy luật biến thiên của nó. Khi đọc một ODE, hãy kiểm tra bốn yếu tố: bậc, tính tuyến tính, tính tự trị và điều kiện đầu. Nghiệm của ODE chính là quỹ đạo tiến hóa theo thời gian của hệ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cảm biến nhiệt trong dây chuyền sản xuất
- Bài toán: Một đầu dò vừa được chuyển từ phòng lạnh vào buồng nung; kỹ sư cần ước lượng thời gian để số đo tiến gần nhiệt độ thực của lò.
- Mô hình: Gọi $$ T(t) $$ là nhiệt độ đầu dò, mô hình bậc nhất là

$$
\frac{dT}{dt}=-k\left(T-T_{\mathrm{env}}\right).
$$

- Giả thiết và giới hạn: Giả sử môi trường có nhiệt độ đồng đều, hệ số trao đổi nhiệt không đổi và đầu dò có nhiệt độ đồng nhất bên trong. Các hiệu ứng bức xạ mạnh hoặc độ trễ phi tuyến của cảm biến chưa được xét tới.
- Diễn giải: Nghiệm hàm mũ cho thấy số đo không nhảy ngay đến nhiệt độ lò mà tiệm cận dần, giúp người vận hành đánh giá độ trễ động học của phép đo.

#### Dược động học một ngăn
- Bài toán: Sau khi tiêm hoặc truyền tĩnh mạch, nồng độ thuốc trong máu biến đổi đồng thời do tốc độ truyền vào và tốc độ đào thải.
- Mô hình:

$$
\frac{dC}{dt}=\frac{u(t)}{V}-kC,
$$

trong đó $$ C(t) $$ là nồng độ thuốc, $$ u(t) $$ là tốc độ truyền và $$ V $$ là thể tích phân bố hiệu dụng.
- Giả thiết và giới hạn: Giả sử thuốc phân bố đều tức thì trong một ngăn duy nhất và tốc độ đào thải tỉ lệ bậc nhất với nồng độ. Với thuốc phân bố nhiều mô hoặc chuyển hóa bão hòa, cần mô hình nhiều ngăn hoặc phi tuyến.
- Diễn giải: Nghiệm phản ánh sự cân bằng giữa cấp thuốc và đào thải, làm cơ sở xác định liều nạp và liều duy trì.

#### Tài khoản đầu tư có nạp tiền đều
- Bài toán: Một tài khoản nhận lãi kép liên tục và được nạp thêm một khoản tiền đều theo thời gian.
- Mô hình:

$$
\frac{dA}{dt}=rA+s,
$$

trong đó $$ A(t) $$ là số dư, $$ r $$ là lãi suất liên tục và $$ s $$ là tốc độ nạp tiền.
- Giả thiết và giới hạn: Giả sử lãi suất không đổi, không tính thuế hay phí giao dịch và dòng tiền nạp hoàn toàn đều; thị trường thực tế có biến động lãi suất và yếu tố ngẫu nhiên.
- Diễn giải: Nghiệm tách bạch rõ phần đóng góp từ vốn tích lũy sẵn và phần đóng góp từ dòng tiền nạp đều.

#### Mạch RC như một bộ lọc thông thấp
- Bài toán: Một mạch đo cần làm mượt tín hiệu đầu vào chứa nhiễu tần số cao.
- Mô hình:

$$
RC\frac{dV_{\mathrm{out}}}{dt}+V_{\mathrm{out}}=V_{\mathrm{in}}(t).
$$

- Giả thiết và giới hạn: Bỏ qua điện cảm ký sinh, tính phi tuyến của linh kiện và giới hạn băng thông thực tế của cảm biến.
- Diễn giải: Phương trình cho thấy mạch bám tốt các biến đổi chậm nhưng làm suy giảm các dao động quá nhanh của tín hiệu vào.

### 2. Trực giác bổ sung và các kết nối

Phương trình vi phân có thể xem như một quy luật tiến hóa cục bộ xác định tốc độ thay đổi từ trạng thái hiện tại. Tư duy này kết nối xuyên suốt cả chương: phương trình tách biến là trường hợp luật tiến hóa phân rã thành tích của nhân tử phụ thuộc thời gian và nhân tử phụ thuộc trạng thái; phương trình tuyến tính cấp một có cấu trúc cộng tính xử lý được bằng nhân tử tích phân; phương trình tự trị có quy luật không phụ thuộc vào gốc thời gian mà chỉ phụ thuộc vào trạng thái. Cần tránh nhầm lẫn rằng đồ thị nghiệm chính là trường hướng: trường hướng chỉ biểu diễn thông tin đạo hàm cục bộ tại từng điểm, còn nghiệm là đường cong ghép nối liên tục các hướng cục bộ đó.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 21)
y = np.linspace(-2, 2, 21)
T, Y = np.meshgrid(t, y)

fields = [(Y, "y' = y"), (T - Y, "y' = t - y")]
fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharex=True, sharey=True)

for ax, F, title in zip(axes, [f[0] for f in fields], [f[1] for f in fields]):
    U = np.ones_like(F)
    V = F
    N = np.sqrt(U**2 + V**2)
    ax.quiver(T, Y, U / N, V / N, color="teal", pivot="mid")
    ax.set_title(title)
    ax.set_xlabel("t")
    ax.grid(alpha=0.2)

axes[0].set_ylabel("y")
plt.tight_layout()
plt.show()
```

Hình bên trái minh họa sự tăng trưởng và suy giảm thuần túy theo dấu của $$ y $$. Hình bên phải cho thấy các quỹ đạo có xu hướng bị kéo về gần đường thẳng $$ y=t $$, minh họa rõ cơ chế phản hồi âm.

### 4. Gợi ý tìm thêm mô phỏng

- search: slope field first order differential equation
- search: Newton cooling interactive simulation
- search: RC circuit step response visualization

### 5. Bài toán mẫu có bối cảnh thực

Một tài khoản bắt đầu với 5000 đô la, hưởng lãi suất liên tục 4%/năm và được nạp đều 1200 đô la mỗi năm. Mô hình tương ứng là

$$
\frac{dA}{dt}=0.04A+1200,\qquad A(0)=5000.
$$

Giải trực tiếp ta thu được

$$
A(t)=-30000+35000e^{0.04t}.
$$

Trong ngắn hạn, phần đóng góp đều tạo ra phần lớn sự gia tăng; về dài hạn, thành phần hàm mũ chiếm ưu thế. Nếu dùng phương pháp Euler với bước nửa năm, nghiệm xấp xỉ khớp khá sát trong vài năm đầu nhưng sai số tích lũy dần theo thời gian—cho thấy sự khác biệt giữa nghiệm giải tích và nghiệm số.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung xác định đúng biến trạng thái, phân loại chính xác dạng phương trình và hiểu vai trò của điều kiện đầu trong việc chọn một quỹ đạo riêng từ họ nghiệm.

**Bậc sau đại học.** Mở rộng sang khái niệm không gian trạng thái, tính đặt chỉnh (well-posedness) và sự phân biệt giữa mô hình xác định, mô hình có trễ và mô hình ngẫu nhiên.

## Video tham khảo

- Xem trước: [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, tiếng Anh. Giới thiệu tổng quan về ODE, từ bài toán vật rơi đến cách viết quy luật vật lý qua tốc độ biến thiên.
- [What is a DIFFERENTIAL EQUATION??   **Intro to my full ODE course**](https://www.youtube.com/watch?v=B5IjsTONKkw) — Dr. Trefor Bazett, tiếng Anh. Trình bày khái niệm bậc, nghiệm và điều kiện đầu tương ứng với phần phân loại mở đầu.
- [Lec 1 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=XDhJ8lVGbl8) — MIT OpenCourseWare, tiếng Anh. Bài giảng mở đầu của Mattuck về trường hướng trong trường hợp không có nghiệm dạng đóng.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ ngôn ngữ mô hình hóa và phân loại ODE.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ ngắn giúp rèn kỹ năng nhận diện cấu trúc phương trình.
- Ross — *Differential Equations*: trình bày gọn gàng với nhiều bài tập khởi động đầu chương.
