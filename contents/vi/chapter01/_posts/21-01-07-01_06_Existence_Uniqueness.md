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
Bài học này giúp sinh viên hiểu câu hỏi nền tảng phía sau mọi kỹ thuật giải ODE: liệu nghiệm có tồn tại hay không, và nếu tồn tại thì có duy nhất hay không. Sinh viên cần phân biệt vai trò của tính liên tục và điều kiện Lipschitz, hiểu ý nghĩa của tính duy nhất đối với độ tin cậy của mô hình, và biết phân tích những ví dụ phản trực giác khi giả thiết bị vi phạm.

## Kiến thức nền
Sinh viên nên nắm phương trình cấp một dạng
$$ y'=f(t,y), $$
ý nghĩa của bài toán giá trị đầu
$$ y(t_0)=y_0, $$
và trực giác về slope field. Một ít quen thuộc với chuẩn tuyệt đối và khái niệm co sẽ giúp việc tiếp cận ý tưởng chứng minh Picard trở nên dễ hiểu hơn, nhưng buổi học này vẫn có thể triển khai tốt ở mức trực giác.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-06 Định lý Tồn tại và Duy nhất]({{ site.imgurl }}/chapter_img/chapter01/01_06_existence_uniqueness.svg)

Trong các bài trước, ta đã học nhiều kỹ thuật để tìm nghiệm. Nhưng có một câu hỏi sâu hơn thường bị che khuất bởi thao tác tính toán: bài toán có thật sự có nghiệm không. Và nếu có, liệu dữ kiện đầu đã chọn ra đúng một quỹ đạo hay còn nhiều khả năng khác nhau. Trong mô hình hóa, đây không phải chi tiết phụ. Nếu mô hình không duy nhất, ta không thể nói trạng thái ban đầu quyết định tương lai một cách đáng tin cậy.

Định lý tồn tại và duy nhất vì thế là nền móng triết học lẫn kỹ thuật của chương. Nó nói cho ta biết khi nào ODE là một mô hình được đặt bài toán tốt. Nói cách khác, trước khi giải, ta cần biết mình có một bài toán đáng để giải hay không.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy tưởng tượng mỗi điểm trong mặt phẳng $$ \left(t,y\right) $$ được gắn với một mũi tên nhỏ chỉ hướng mà nghiệm phải đi. Nếu các mũi tên thay đổi "êm" và không quá nhọn theo biến $$ y $$, thì từ một điểm ban đầu ta mong đợi có đúng một đường cong đi theo các mũi tên ấy. Nếu trường hướng có một chỗ nhọn hoặc dựng đứng bất thường, nhiều đường cong có thể cùng phù hợp.

### Cách nhìn hình ảnh
Trên slope field của một phương trình có tính duy nhất, hai nghiệm khác nhau không thể cắt nhau, vì nếu chúng cắt nhau thì qua cùng một điểm sẽ có hai nghiệm khác nhau. Ngược lại, ở những ví dụ như
$$ y'=y^{1/3},\qquad y(0)=0, $$
ta có thể vẽ nhiều quỹ đạo cùng đi qua gốc: nghiệm hằng, nghiệm rời gốc ngay, hoặc nghiệm nằm yên một lúc rồi mới rời đi. Hình ảnh đó làm ý niệm "không duy nhất" trở nên rất sống động.

### Cách nhìn hình thức
Định lý Picard-Lindelof phát biểu rằng nếu $$ f(t,y) $$ liên tục trong một hình chữ nhật chứa $$ \left(t_0,y_0\right) $$ và Lipschitz theo biến $$ y $$ trên hình chữ nhật đó, thì bài toán giá trị đầu
$$ \frac{dy}{dt}=f(t,y),\qquad y(t_0)=y_0 $$
có một nghiệm duy nhất trên một khoảng thời gian đủ nhỏ quanh $$ t_0 $$.

Điều kiện Lipschitz theo $$ y $$ nghĩa là tồn tại hằng số $$ L $$ sao cho
$$
\lvert f(t,y_1)-f(t,y_2)\rvert\leq L\lvert y_1-y_2\rvert
$$
cho mọi $$ y_1,y_2 $$ trong miền xét. Điều kiện này mạnh hơn liên tục theo $$ y $$ và chính là chìa khóa cho tính duy nhất.

## Ý nghĩa toán học và mô hình hóa
Tính liên tục của $$ f $$ thường đủ để hứa hẹn sự tồn tại nghiệm cục bộ. Trực giác là trường hướng không bị "đứt gãy", nên ta có thể dựng được ít nhất một quỹ đạo. Nhưng để quỹ đạo ấy là duy nhất, ta cần một kiểm soát mạnh hơn về độ nhạy theo trạng thái, và đó là lý do điều kiện Lipschitz xuất hiện.

Trong mô hình hóa, tính duy nhất nói rằng trạng thái ban đầu xác định tương lai ít nhất ở mức cục bộ. Nếu không có duy nhất, mô hình thiếu sức tiên đoán. Trong mô phỏng số, điều này cũng cực kỳ quan trọng, vì thuật toán sẽ không biết mình nên bám theo quỹ đạo nào.

## Những ngộ nhận thường gặp
- "Liên tục là đủ cho duy nhất." Sai. Liên tục giúp tồn tại, nhưng không đảm bảo duy nhất.
- "Không Lipschitz thì chắc chắn không có duy nhất." Không đúng tuyệt đối. Lipschitz là điều kiện đủ rất mạnh, không phải lúc nào cũng là điều kiện cần.
- "Nếu có công thức nghiệm thì tự động có duy nhất." Không đúng. Có thể tồn tại nhiều công thức nghiệm cùng thỏa cùng điều kiện đầu.
- "Duy nhất chỉ là chi tiết lý thuyết." Sai. Nó quyết định mô hình có khả năng tiên đoán hay không.

## Tiến trình học tập đề xuất
### Bước 1: Nhắc lại bài toán giá trị đầu
Sinh viên cần hiểu ta đang hỏi về một nghiệm đi qua một điểm cụ thể.

### Bước 2: Phân biệt tồn tại và duy nhất
Đây là hai câu hỏi khác nhau và cần nhấn mạnh tách bạch.

### Bước 3: Hiểu điều kiện Lipschitz
Không cần quá hình thức lúc đầu; hãy xem nó như một ràng buộc tránh việc trường hướng thay đổi quá đột ngột theo $$ y $$.

### Bước 4: Xem phản ví dụ
Những ví dụ không duy nhất thường dạy nhiều hơn các ví dụ "đẹp".

### Các checkpoint
- Sinh viên có giải thích được sự khác nhau giữa liên tục và Lipschitz hay không.
- Sinh viên có hiểu vì sao hai nghiệm không thể cắt nhau trong trường hợp duy nhất hay không.
- Sinh viên có nhận ra rằng nghiệm có thể tồn tại cục bộ nhưng không tồn tại toàn cục hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Bài toán đẹp có nghiệm duy nhất
Xét
$$ y'=t+y,\qquad y(0)=1. $$
Hàm
$$ f(t,y)=t+y $$
liên tục mọi nơi và Lipschitz theo $$ y $$ với hằng số Lipschitz bằng 1, vì
$$
\lvert f(t,y_1)-f(t,y_2)\rvert=\lvert y_1-y_2\rvert.
$$
Do đó bài toán có nghiệm duy nhất cục bộ, và thực ra là toàn cục. Đây là ví dụ điển hình của một mô hình "lành tính".

### Ví dụ 2: Liên tục nhưng không duy nhất
Xét
$$ y'=y^{1/3},\qquad y(0)=0. $$
Hàm
$$ f(y)=y^{1/3} $$
liên tục tại 0 nhưng không Lipschitz gần 0. Thật vậy, đạo hàm
$$ f'(y)=\frac{1}{3}y^{-2/3} $$
không bị chặn gần 0. Ta có nghiệm
$$ y(t)=0. $$
Ngoài ra, nếu tách biến với $$ y>0 $$,
$$ \frac{dy}{y^{1/3}}=dt $$
cho
$$ \frac{3}{2}y^{2/3}=t+C. $$
Suy ra một họ nghiệm có thể đi qua gốc sau một thời gian chờ. Cụ thể, với mọi $$ a\geq 0 $$, hàm
$$
y(t)=
\begin{cases}
0, & t\leq a,\\
\left(\frac{2}{3}(t-a)\right)^{3/2}, & t>a
\end{cases}
$$
đều thỏa bài toán. Đây là ví dụ kinh điển cho thấy liên tục chưa đủ cho duy nhất.

### Ví dụ 3: Không tồn tại tại điểm ban đầu
Xét
$$ y'=\frac{1}{t-1},\qquad y(1)=0. $$
Hàm vế phải không liên tục tại $$ t=1 $$, nên định lý không áp dụng. Thật ra bài toán không có nghiệm đi qua $$ t=1 $$ vì đạo hàm bị buộc phải vô hạn ở đó. Ví dụ này tách biệt rõ câu hỏi "không duy nhất" với câu hỏi "không tồn tại".

### Ví dụ 4: Có duy nhất cục bộ nhưng không toàn cục
Xét
$$ y'=y^2,\qquad y(0)=1. $$
Hàm
$$ f(y)=y^2 $$
trơn và Lipschitz cục bộ, nên tồn tại nghiệm duy nhất cục bộ. Giải ra được
$$ y(t)=\frac{1}{1-t}. $$
Nghiệm là duy nhất, nhưng chỉ tồn tại đến trước $$ t=1 $$. Điều này giúp sinh viên hiểu rằng "có duy nhất" không đồng nghĩa với "tồn tại mãi mãi".

## Câu hỏi khái niệm
1. Vì sao tính liên tục có vẻ hợp lý cho tồn tại, nhưng chưa đủ cho duy nhất?
2. Trong ngôn ngữ hình học, điều kiện Lipschitz ngăn cản điều gì xảy ra với trường hướng?
3. Vì sao một mô hình có nghiệm duy nhất cục bộ vẫn có thể thất bại ở thời gian lớn?

## Bài toán ứng dụng
1. Một mô hình điều khiển robot cho tín hiệu phản hồi rất nhạy gần vị trí cân bằng. Nếu hàm phản hồi không đủ đều, điều này có thể ảnh hưởng thế nào đến tính duy nhất của quỹ đạo?
2. Trong mô phỏng thời tiết hoặc dịch tễ, tại sao tính duy nhất của nghiệm lại quan trọng đối với ý nghĩa dự báo?
3. Một mô hình sinh học cho nghiệm nổ sau thời gian hữu hạn. Hãy thảo luận xem đây là giới hạn của tự nhiên hay của chính mô hình toán học.

## Chiến lược giảng dạy tương tác
- Trước khi nêu định lý, hỏi lớp: "Nếu biết hướng đi tại mọi điểm, liệu có chắc chắn chỉ có một đường cong xuất phát từ một điểm không?"
- Dùng hai đồ thị hoặc slope field để so sánh một ví dụ duy nhất và một ví dụ không duy nhất.
- Yêu cầu sinh viên tự chế phản ví dụ bằng cách nghĩ đến một hàm liên tục nhưng có góc nhọn tại 0.
- Tổ chức thảo luận ngắn: trong ứng dụng, "không duy nhất" nghĩa là lỗi của mô hình hay là đặc trưng của hệ?

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên tách bài học thành ba nhãn rất rõ: tồn tại, duy nhất, toàn cục. Việc dùng bảng so sánh các ví dụ theo ba cột này giúp sinh viên bớt lẫn. Cũng nên ưu tiên hình ảnh slope field hơn là ngôn ngữ định lý quá sớm.

### Thử thách cho sinh viên khá giỏi
Có thể giao cho sinh viên khá giỏi phác thảo ý tưởng lặp Picard và nguyên lý ánh xạ co, hoặc yêu cầu chứng minh rằng nếu $$ f_y $$ liên tục và bị chặn trên một miền thì $$ f $$ Lipschitz theo $$ y $$ trên miền đó.

## Tóm tắt dễ nhớ
Muốn một bài toán giá trị đầu đáng tin, ta cần ít nhất biết nghiệm có tồn tại và tốt hơn nữa là duy nhất. Liên tục thường gắn với tồn tại, Lipschitz theo $$ y $$ gắn với duy nhất. Nhưng ngay cả khi có duy nhất, nghiệm vẫn có thể chỉ sống trong một khoảng thời gian hữu hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Điều khiển tự động và khả năng tiên đoán
- Bài toán: Một bộ điều khiển lái cần bảo đảm rằng từ cùng một trạng thái ban đầu, xe không thể "chọn" hai quỹ đạo khác nhau.
- Mô hình: Một dạng đơn giản là
$$ \frac{dx}{dt}=f(t,x),\qquad x(0)=x_0. $$
- Giả thiết và giới hạn: Tính duy nhất yêu cầu luật phản hồi đủ đều theo trạng thái. Trong thực tế, bão hòa, va chạm, hoặc luật điều khiển rời rạc có thể làm mô hình không còn trơn.
- Diễn giải: Nếu không có duy nhất, mô hình mất ý nghĩa dự báo và bộ điều khiển thiếu tính quyết định.

#### Động học hóa học khi khởi động phản ứng
- Bài toán: Một phản ứng được đưa vào vận hành từ nồng độ đầu xác định và kỹ sư cần biết hệ có đi theo một kịch bản duy nhất hay không.
- Mô hình:
$$ \frac{dc}{dt}=f(c,T). $$
- Giả thiết và giới hạn: Mô hình ODE thường giả sử trộn đều hoàn hảo và không gian không đóng vai trò độc lập. Khi có phân tầng nhiệt hoặc khuếch tán mạnh, phải dùng PDE.
- Diễn giải: Điều kiện tồn tại và duy nhất nói cho ta khi nào mô hình phòng thí nghiệm có thể được dùng cho dự báo quá trình.

#### Dự báo dịch tễ ở giai đoạn đầu
- Bài toán: Với cùng dữ liệu ban đầu, liệu mô hình có cho ra đúng một quỹ đạo số ca nhiễm hay không.
- Mô hình cục bộ:
$$ \frac{dI}{dt}=f(t,I). $$
- Giả thiết và giới hạn: ODE xác định bỏ qua ngẫu nhiên và bất định đo lường. Với quần thể nhỏ hoặc dữ liệu nhiễu mạnh, mô hình xác suất thích hợp hơn.
- Diễn giải: Tồn tại và duy nhất không làm mô hình đúng hơn, nhưng cho biết nó ít nhất là một cơ chế dự báo nhất quán về mặt toán học.

### 2. Trực giác bổ sung và các kết nối

Định lý tồn tại và duy nhất đánh dấu lần đầu tiên chương học chuyển từ "giải được như thế nào" sang "có đáng để giải hay không". Nó chuẩn bị tư duy cho toàn bộ phần sau của khóa học: ở hệ ODE, ta sẽ hỏi về dòng động lực học; ở PDE, ta sẽ hỏi về well-posedness của bài toán biên đầu; ở phương pháp số, ta sẽ hỏi sai số có hội tụ về đúng nghiệm duy nhất ấy hay không. Một hiểu lầm thường gặp là xem Lipschitz như điều kiện kỹ thuật vô hồn. Thực ra nó là cách định lượng việc trường hướng không đổi quá gắt theo phương đứng.

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

Hình này làm điều mà lời phát biểu định lý khó làm ngay: nó cho thấy cùng một điều kiện đầu có thể sinh ra nhiều nghiệm nếu điều kiện đủ cho duy nhất bị phá vỡ.

### 4. Gợi ý tìm thêm mô phỏng

- search: Picard Lindelof visual explanation
- search: nonunique solution y' = y^(1/3)
- search: slope field uniqueness differential equations

### 5. Bài toán mẫu có bối cảnh thực

Với bài toán
$$ y'=t+y,\qquad y(0)=1, $$
ta có thể không chỉ giải bằng nhân tử tích phân mà còn khảo sát lặp Picard:
$$
y_{n+1}(t)=1+\int_0^t \left(s+y_n(s)\right)\,ds,
\qquad y_0(t)=1.
$$
Các xấp xỉ đầu là
$$
y_1(t)=1+t+\frac{t^2}{2},
\qquad
y_2(t)=1+t+t^2+\frac{t^3}{6}.
$$
Điều này cho sinh viên cái nhìn rất cụ thể rằng định lý không chỉ nói "có nghiệm" mà còn gợi một quá trình xây dựng nghiệm.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ ba câu hỏi: có nghiệm không, có duy nhất không, và có tồn tại toàn cục không.

**Bậc sau đại học.** Đi vào ánh xạ co Banach, lặp Picard, điều kiện Caratheodory, và các phản ví dụ nơi duy nhất vẫn đúng dù không Lipschitz. Đây là nền cho tư duy well-posedness của PDE.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: có phần rất chuẩn về Picard-Lindelof và các phản ví dụ kinh điển.
- Zill — *Differential Equations with Boundary-Value Problems*: phù hợp để luyện phân tích giả thiết định lý qua các ví dụ cụ thể.
- Ross — *Differential Equations*: hữu ích cho việc ôn lại các phân biệt cơ bản giữa tồn tại, duy nhất và miền tồn tại.
