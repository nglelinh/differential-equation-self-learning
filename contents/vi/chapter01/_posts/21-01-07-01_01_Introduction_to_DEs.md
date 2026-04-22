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
## Mục tiêu
Bài học này giúp sinh viên hiểu phương trình vi phân như một quy luật mô tả sự biến thiên, biết phân loại ODE theo bậc, tuyến tính, tự trị và điều kiện đầu, đồng thời bắt đầu đọc nghiệm không chỉ như một công thức mà như quỹ đạo của một quá trình thực. Sau bài học, sinh viên cần thấy rõ vì sao phương trình vi phân xuất hiện tự nhiên trong khoa học, kỹ thuật, kinh tế và sinh học.

## Kiến thức nền
Sinh viên nên nắm vững đạo hàm, tích phân, ý nghĩa hình học của hệ số góc tiếp tuyến, cùng với các hàm sơ cấp như đa thức, mũ, logarit và lượng giác. Việc giải phương trình đại số đơn giản và đọc đồ thị hàm số cũng rất quan trọng, vì trong ODE ta thường chuyển qua lại giữa biểu thức đại số, đồ thị và diễn giải định tính.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-01 Giới thiệu Phương trình Vi phân]({{ site.imgurl }}/chapter_img/chapter01/01_01_introduction_to_des.svg)

Nếu một cốc cà phê đang nguội đi, điều ta quan sát không chỉ là nhiệt độ tại một thời điểm, mà là tốc độ nguội đi phụ thuộc vào chênh lệch nhiệt độ với môi trường. Nếu một quần thể vi khuẩn tăng trưởng, điều ta quan tâm không chỉ là số lượng hiện tại, mà là tốc độ sinh trưởng ở từng thời điểm. Nếu một tài khoản ngân hàng sinh lãi liên tục, điều quyết định quỹ đạo số dư là tốc độ tăng của nó so với chính nó. Những tình huống như vậy dẫn ta đến một câu hỏi chung: hàm số cần tìm thay đổi như thế nào?

Phương trình vi phân chính là ngôn ngữ toán học trả lời câu hỏi ấy. Thay vì cho ta giá trị trực tiếp của hàm, nó cho ta một ràng buộc giữa hàm và đạo hàm của nó. Vì thế, giải ODE không đơn thuần là thao tác ký hiệu; đó là quá trình tái dựng một chuyển động, một quá trình tích lũy, hay một cơ chế phản hồi từ thông tin về tốc độ biến thiên.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy hình dung bạn đang lái xe trên một con đường nhưng thay vì được cung cấp bản đồ đầy đủ, bạn chỉ được biết ở mỗi vị trí thì vô lăng nên nghiêng bao nhiêu. Nếu biết hướng đi tại mọi điểm và biết mình xuất phát ở đâu, về nguyên tắc ta có thể vẽ lại quỹ đạo. ODE làm đúng điều đó: nó cho ta "hướng chuyển động cục bộ" của nghiệm.

### Cách nhìn hình ảnh
Một cách hình dung rất mạnh là trường hướng hoặc slope field. Với phương trình
$$ \frac{dy}{dt}=f(t,y), $$
ta đặt tại mỗi điểm $$ \left(t,y\right) $$ một đoạn thẳng nhỏ có hệ số góc bằng $$ f(t,y) $$. Nghiệm của phương trình là những đường cong luôn tiếp xúc với các đoạn thẳng đó. Với $$ \frac{dy}{dt}=y $$, các đoạn dốc lên khi $$ y>0 $$, dốc xuống khi $$ y<0 $$, và nằm ngang trên trục $$ y=0 $$. Từ bức tranh đó, ta đoán được nghiệm dương sẽ tăng, nghiệm âm sẽ giảm về âm vô hạn, còn $$ y=0 $$ là nghiệm cân bằng.

### Cách nhìn hình thức
Một phương trình vi phân thường là phương trình chứa một hàm chưa biết và ít nhất một đạo hàm của nó. Trong chương này ta tập trung vào phương trình vi phân thường cấp một:
$$ \frac{dy}{dt}=f(t,y). $$
Nếu đạo hàm cao nhất là đạo hàm bậc nhất thì phương trình có bậc một. Nếu đạo hàm cao nhất là bậc hai, ta có phương trình bậc hai, v.v. Một nghiệm là một hàm khả vi $$ y(t) $$ thỏa phương trình trên một khoảng nào đó.

## Các ý niệm cốt lõi cần nhận biết
Một ODE thường được đọc qua bốn câu hỏi. Phương trình có bậc mấy. Nó tuyến tính hay phi tuyến. Nó tự trị hay phụ thuộc tường minh vào thời gian. Nó đi kèm điều kiện đầu hay không.

Phương trình
$$ \frac{dy}{dt}+p(t)y=q(t) $$
là tuyến tính cấp một vì $$ y $$ và $$ \frac{dy}{dt} $$ chỉ xuất hiện với lũy thừa một và không nhân với nhau. Trong khi đó,
$$ \frac{dy}{dt}=y^2-t $$
là phi tuyến vì có $$ y^2 $$. Phương trình
$$ \frac{dy}{dt}=f(y) $$
là tự trị vì vế phải không chứa trực tiếp biến thời gian.

Điều kiện đầu
$$ y(t_0)=y_0 $$
chọn ra một nghiệm cụ thể trong họ nghiệm tổng quát. Không có điều kiện đầu, ta thường chỉ mô tả được một họ quỹ đạo; có điều kiện đầu, ta gắn mô hình với một trạng thái ban đầu cụ thể của hệ thực.

## Những ngộ nhận thường gặp
- "Phương trình vi phân luôn phải giải ra công thức tường minh." Sai. Nhiều ODE quan trọng chỉ phân tích được định tính hoặc bằng số.
- "Đạo hàm chỉ là thao tác hình thức." Sai. Trong mô hình, đạo hàm là tốc độ thay đổi tức thời, thường mang ý nghĩa vật lý trực tiếp.
- "Chỉ cần tìm một hàm thỏa phương trình là xong." Chưa đủ. Ta còn phải xét miền xác định, điều kiện đầu, và liệu nghiệm có hợp lý theo bối cảnh ứng dụng hay không.
- "Hai nghiệm khác nhau có thể cắt nhau bất cứ lúc nào." Không đúng trong nhiều bài toán giá trị đầu có tính duy nhất; nếu duy nhất, hai nghiệm qua cùng một điểm không thể tách ra.

## Tiến trình học tập đề xuất
### Bước 1: Ôn lại đạo hàm như tốc độ biến thiên
Sinh viên cần nối lại trực giác từ giải tích: đạo hàm đo tốc độ thay đổi, còn tích phân gom góp sự thay đổi.

### Bước 2: Đọc phương trình như một luật tiến hóa
Thay vì hỏi "nghiệm là gì", ta hỏi "hệ biến đổi theo luật nào". Đây là chuyển dịch nhận thức quan trọng nhất trong đầu chương.

### Bước 3: Phân loại cấu trúc
Sinh viên tập nhìn nhanh xem phương trình thuộc loại nào để chuẩn bị phương pháp tương ứng ở các bài sau.

### Bước 4: Gắn với điều kiện đầu
Từ một họ nghiệm, ta chọn một nghiệm cụ thể bằng dữ kiện ban đầu.

### Các checkpoint
- Sinh viên có giải thích được bằng lời ý nghĩa của $$ \frac{dy}{dt}=f(t,y) $$ hay không.
- Sinh viên có phân biệt được tuyến tính với phi tuyến trong các ví dụ cơ bản hay không.
- Sinh viên có hiểu vì sao điều kiện đầu là một phần của mô hình chứ không phải chi tiết phụ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Kiểm tra một hàm có phải là nghiệm hay không
Xét phương trình
$$ \frac{dy}{dt}=2t $$
và hàm ứng viên
$$ y=t^2+3. $$
Ta có
$$ \frac{dy}{dt}=2t, $$
nên hàm này đúng là nghiệm. Nếu thêm điều kiện đầu $$ y(0)=3 $$ thì nghiệm trên thỏa. Nhưng nếu điều kiện đầu là $$ y(0)=1 $$ thì không thỏa, dù vẫn là nghiệm của ODE. Ví dụ này nhắc rằng một ODE và một bài toán giá trị đầu không phải là cùng một thứ.

### Ví dụ 2: Từ quy luật tăng trưởng đến họ nghiệm
Xét
$$ \frac{dy}{dt}=ky. $$
Ta biết từ giải tích rằng hàm mũ có tính chất đạo hàm tỉ lệ với chính nó, nên ta thử dạng
$$ y=Ce^{kt}. $$
Khi đạo hàm,
$$ \frac{dy}{dt}=kCe^{kt}=ky, $$
nên họ nghiệm là
$$ y(t)=Ce^{kt}. $$
Nếu $$ k>0 $$, nghiệm tăng theo thời gian; nếu $$ k<0 $$, nghiệm giảm dần về 0. Cùng một công thức nhưng hành vi định tính rất khác nhau tùy tham số.

### Ví dụ 3: Phân loại phương trình
Xét ba phương trình:
$$ \frac{dy}{dt}+3y=t, $$
$$ \frac{dy}{dt}=y(1-y), $$
$$ \frac{d^2x}{dt^2}+\omega^2 x=0. $$
Phương trình thứ nhất là tuyến tính cấp một, không tự trị. Phương trình thứ hai là phi tuyến cấp một, tự trị. Phương trình thứ ba là tuyến tính bậc hai. Chỉ riêng thao tác phân loại này đã giúp ta dự đoán công cụ sẽ học ở các bài sau.

### Ví dụ 4: Đọc trường hướng đơn giản
Với
$$ \frac{dy}{dt}=t-y, $$
tại điểm $$ \left(0,0\right) $$ hệ số góc bằng 0, tại $$ \left(1,0\right) $$ hệ số góc bằng 1, còn tại $$ \left(0,1\right) $$ hệ số góc bằng -1. Nghĩa là dưới đường thẳng $$ y=t $$ thì nghiệm có xu hướng đi lên, trên đường đó thì đi xuống. Trước cả khi giải chính xác, ta đã có bức tranh định tính về hành vi nghiệm.

## Câu hỏi khái niệm
1. Vì sao một phương trình vi phân cần được hiểu như quy luật biến thiên hơn là như một bài toán đại số?
2. Vì sao hai phương trình có hình thức gần giống nhau vẫn có thể cần phương pháp giải hoàn toàn khác?
3. Vì sao điều kiện đầu có thể thay đổi mạnh ý nghĩa thực tế của cùng một ODE?

## Bài toán ứng dụng
1. Nhiệt độ của một vật giảm với tốc độ tỉ lệ với chênh lệch nhiệt độ giữa vật và môi trường. Hãy mô tả bằng lời vì sao hiện tượng này nên dẫn đến một ODE cấp một.
2. Một tài khoản đầu tư tăng trưởng liên tục với lãi suất không đổi. Hãy giải thích vì sao mô hình hợp lý phải có dạng tốc độ tăng tỉ lệ với số dư hiện tại.
3. Một loài vi khuẩn được nuôi trong bình kín. Giai đoạn đầu tăng nhanh, về sau chậm lại. Hãy dự đoán vì sao mô hình tăng trưởng đơn giản $$ \frac{dP}{dt}=kP $$ rồi sẽ không đủ tốt.

## Chiến lược giảng dạy tương tác
- Bắt đầu lớp học bằng câu hỏi: "Nếu tôi chỉ cho các em biết vận tốc tại từng thời điểm, liệu ta có dựng lại chuyển động không?"
- Cho sinh viên làm việc theo cặp để phân loại 6 đến 8 phương trình thành các nhóm: tuyến tính, phi tuyến, tự trị, có điều kiện đầu.
- Chiếu một slope field đơn giản và yêu cầu lớp dự đoán nghiệm nào tăng, nghiệm nào giảm, nghiệm nào cân bằng trước khi giải.
- Khuyến khích sinh viên giải thích bằng lời ý nghĩa của từng thành phần trong phương trình thay vì chỉ đọc ký hiệu.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Giảng viên nên cho sinh viên yếu bắt đầu từ bảng hai cột: "ký hiệu" và "ý nghĩa". Ví dụ, $$ \frac{dy}{dt} $$ là tốc độ thay đổi, $$ y(0)=2 $$ là trạng thái ban đầu. Có thể dùng thêm các ví dụ đời sống quen thuộc như nhiệt độ, số dư tiền gửi, mực nước trong bể.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên khá giỏi so sánh cách hiểu "nghiệm là đồ thị" với "nghiệm là quỹ đạo trong trường hướng", hoặc phân tích vì sao phương trình không có nghiệm tường minh vẫn có thể rất có ích trong mô hình hóa. Có thể giao thêm bài đọc ngắn về mô phỏng số và lý do nó quan trọng.

## Tóm tắt dễ nhớ
Phương trình vi phân không cho ta giá trị trực tiếp của hệ, mà cho ta luật thay đổi của hệ. Muốn hiểu một ODE, hãy hỏi bốn điều: bậc mấy, tuyến tính hay phi tuyến, tự trị hay không, và có điều kiện đầu nào đi kèm. Nghiệm không chỉ là công thức; nó là câu chuyện tiến hóa của một trạng thái theo thời gian.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cảm biến nhiệt trong dây chuyền sản xuất
- Bài toán: Một đầu dò vừa được đưa từ phòng lạnh vào buồng nung, và kỹ sư muốn biết bao lâu thì số đo gần nhiệt độ thật của lò.
- Mô hình: Nếu $$ T(t) $$ là nhiệt độ đầu dò, thì một mô hình đầu tiên là
$$ \frac{dT}{dt}=-k\left(T-T_{\mathrm{env}}\right). $$
- Giả thiết và giới hạn: Ta giả sử môi trường có nhiệt độ đều, hệ số trao đổi nhiệt không đổi, và bản thân đầu dò có thể xem như một khối đồng nhất. Các hiệu ứng bức xạ mạnh hoặc trễ cảm biến phi tuyến chưa được tính tới.
- Diễn giải: Nghiệm mũ cho thấy cảm biến không nhảy ngay tới trạng thái cân bằng mà tiến gần dần, vì vậy người vận hành phải hiểu rõ độ trễ động học của phép đo.

#### Dược động học một ngăn
- Bài toán: Sau khi tiêm tĩnh mạch hoặc truyền thuốc, nồng độ thuốc trong máu thay đổi do vừa được đưa vào vừa bị đào thải.
- Mô hình:
$$ \frac{dC}{dt}=\frac{u(t)}{V}-kC, $$
trong đó $$ C(t) $$ là nồng độ, $$ u(t) $$ là tốc độ truyền thuốc, và $$ V $$ là thể tích phân bố hiệu dụng.
- Giả thiết và giới hạn: Mô hình một ngăn giả sử thuốc trộn đều tức thì trong cơ thể và tốc độ thải trừ tỉ lệ với nồng độ. Với thuốc có nhiều mô, chuyển hóa bão hòa, hoặc gắn protein mạnh, mô hình này còn quá thô.
- Diễn giải: Nghiệm cho thấy nồng độ là kết quả của cạnh tranh giữa cấp thuốc và thải trừ, từ đó giúp ta thiết kế liều nạp và liều duy trì.

#### Tài khoản đầu tư có nạp tiền đều
- Bài toán: Một người gửi tiết kiệm với lãi kép liên tục và nạp thêm tiền đều theo thời gian.
- Mô hình:
$$ \frac{dA}{dt}=rA+s, $$
trong đó $$ A(t) $$ là số dư, $$ r $$ là lãi suất liên tục, và $$ s $$ là tốc độ nạp thêm.
- Giả thiết và giới hạn: Ta giả sử lãi suất không đổi, không có thuế hay phí, và dòng tiền nạp là đều. Thị trường thực thường có biến động ngẫu nhiên và lãi suất thay đổi theo chu kỳ.
- Diễn giải: Nghiệm phân tách rõ phần tăng trưởng do vốn đang có và phần tăng trưởng do đóng góp đều, nhờ đó sinh viên thấy ngay ý nghĩa của các số hạng trong ODE.

#### Mạch RC như một bộ lọc thấp tần
- Bài toán: Một mạch cảm biến cần làm mượt tín hiệu vào có nhiễu cao tần.
- Mô hình:
$$
RC\frac{dV_{\mathrm{out}}}{dt}+V_{\mathrm{out}}=V_{\mathrm{in}}(t).
$$
- Giả thiết và giới hạn: Mô hình bỏ qua điện cảm ký sinh, tính phi tuyến của linh kiện, và giới hạn băng thông của cảm biến thật.
- Diễn giải: Dạng ODE này cho thấy mạch phản ứng tốt với tín hiệu chậm nhưng không thể bám ngay các thay đổi quá gấp.

### 2. Trực giác bổ sung và các kết nối

Phương trình vi phân nên được đọc như một luật tiến hóa cục bộ: tại trạng thái hiện tại, hệ được phép đổi nhanh đến mức nào. Ý tưởng này nối trực tiếp chương đầu với cả phần sau của khóa học. Phương trình tách biến là khi luật tiến hóa có thể phân rã thành ảnh hưởng theo thời gian và theo trạng thái. Phương trình tuyến tính cấp một là khi trạng thái xuất hiện theo cách cộng tính và có thể được "chuẩn hóa" bằng nhân tử tích phân. Phương trình tự trị là khi luật tiến hóa không nhìn đồng hồ tuyệt đối mà chỉ nhìn trạng thái hiện tại. Một ngộ nhận rất thường gặp là nghĩ rằng đồ thị nghiệm chính là trường hướng; thật ra trường hướng chỉ cho thông tin vi phân cục bộ, còn nghiệm là đường cong ghép các thông tin cục bộ ấy lại.

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

Đồ thị đầu cho cảm giác tăng trưởng hay suy giảm thuần túy. Đồ thị thứ hai cho thấy cơ chế kéo nghiệm về gần đường $$ y=t $$, rất phù hợp để nhấn mạnh khái niệm "trạng thái đích" và "phản hồi âm".

### 4. Gợi ý tìm thêm mô phỏng

- search: slope field first order differential equation
- search: Newton cooling interactive simulation
- search: RC circuit step response visualization

### 5. Bài toán mẫu có bối cảnh thực

Một tài khoản khởi đầu với 5000 đô la, nhận lãi liên tục 4 phần trăm mỗi năm và được nạp thêm đều 1200 đô la mỗi năm. Mô hình là
$$ \frac{dA}{dt}=0.04A+1200,\qquad A(0)=5000. $$
Ở mức đại học, ta giải được ngay
$$ A(t)=-30000+35000e^{0.04t}. $$
Nghiệm cho thấy về ngắn hạn, phần đóng góp đều thống trị; về dài hạn, thành phần mũ chi phối. Nếu dùng Euler với bước nửa năm, ta có một xấp xỉ số đủ tốt trong vài năm đầu nhưng sai số sẽ tích lũy dần, và đây là cơ hội sớm để nhấn mạnh sự khác nhau giữa nghiệm giải tích và mô phỏng số.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào việc đọc đúng biến trạng thái, phân loại đúng dạng phương trình, và hiểu rằng điều kiện đầu chọn ra một quỹ đạo riêng từ một họ nghiệm.

**Bậc sau đại học.** Nhấn mạnh khái niệm không gian trạng thái, tính đặt bài toán tốt, và sự khác nhau giữa mô hình xác định, mô hình có trễ, và mô hình ngẫu nhiên. Đây cũng là nơi thích hợp để gợi ý rằng không phải mọi động lực học đều được mô tả đủ tốt bằng một ODE cấp một.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giới thiệu rất tốt về ngôn ngữ mô hình và phân loại ODE.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ ngắn, phù hợp để luyện nhận dạng cấu trúc phương trình.
- Ross — *Differential Equations*: trình bày gọn, rõ và có nhiều bài tập khởi động đầu chương.
