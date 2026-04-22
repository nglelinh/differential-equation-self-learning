---
layout: post
title: "02-04 Hạ bậc"
chapter: '02'
order: 4
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu cách tìm nghiệm thứ hai của phương trình tuyến tính cấp hai thuần nhất khi đã biết một nghiệm không tầm thường. Sinh viên sẽ học bản chất của phép đặt
$$ y_2=v(t)y_1(t), $$
biết khi nào nên dùng hạ bậc, và thấy rằng một nghiệm đã biết không chỉ là đáp số mà còn là chìa khóa mở ra toàn bộ không gian nghiệm.

## Kiến thức nền
Sinh viên nên nắm phương trình tuyến tính cấp hai, nguyên lý chồng chập, đạo hàm của tích và khái niệm độc lập tuyến tính. Việc hiểu vì sao cần hai nghiệm độc lập cho bài toán thuần nhất là nền tảng của toàn bộ bài học.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-04 Hạ bậc]({{ site.imgurl }}/chapter_img/chapter02/02_04_reduction_of_order.svg)

Trong một số bài toán, ta may mắn biết trước một nghiệm, có thể từ trực giác vật lý, từ đối xứng, hoặc từ cách đoán thông minh. Nhưng một nghiệm chưa đủ để viết nghiệm tổng quát của phương trình cấp hai thuần nhất. Câu hỏi tự nhiên là: có thể khai thác chính nghiệm đã biết để sinh nghiệm còn lại hay không?

Phương pháp hạ bậc trả lời đúng câu hỏi ấy. Thay vì tìm nghiệm mới từ con số 0, ta tìm nó dưới dạng một hệ số biến thiên nhân với nghiệm cũ. Ý tưởng này cực kỳ quan trọng về mặt tư duy: lời giải không phải là một danh sách mẹo rời rạc, mà là nghệ thuật khai thác cấu trúc có sẵn.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy xem nghiệm đã biết $$ y_1 $$ như một hướng chuyển động cơ bản của hệ. Nghiệm thứ hai được tìm bằng cách cho phép "cường độ" của hướng đó biến thiên theo thời gian thay vì giữ cố định. Hệ số biến thiên ấy chính là hàm $$ v(t) $$.

### Cách nhìn hình ảnh
Nếu $$ y_1 $$ là một đường cong nghiệm, thì nghiệm mới không đơn thuần là bản sao co giãn bằng hằng số. Ta cần một cách co giãn thay đổi theo thời gian để tạo ra một đường cong mới nhưng vẫn phù hợp với phương trình. Hạ bậc chính là cơ chế đó.

### Cách nhìn hình thức
Xét phương trình thuần nhất đã chuẩn hóa
$$ y''+p(t)y'+q(t)y=0. $$
Giả sử $$ y_1(t) $$ là một nghiệm không tầm thường. Ta tìm nghiệm thứ hai dưới dạng
$$ y_2=v(t)y_1(t). $$
Lấy đạo hàm:
$$ y_2'=v'y_1+vy_1', $$
$$ y_2''=v''y_1+2v'y_1'+vy_1''. $$
Thế vào phương trình và dùng việc $$ y_1 $$ đã là nghiệm, ta thu được một phương trình bậc thấp hơn cho $$ v' $$. Đây là lý do phương pháp có tên là hạ bậc.

## Những ngộ nhận thường gặp
- "Biết một nghiệm thì đoán nghiệm kia bằng cách thay hằng số khác." Sai. Ta cần nghiệm độc lập tuyến tính, không phải cùng một nghiệm nhân hằng số.
- "Hạ bậc luôn đơn giản." Không hẳn. Nó đúng về nguyên lý nhưng có thể dẫn đến tích phân không đẹp.
- "Nếu đã biết công thức tổng quát thì không cần hiểu hạ bậc." Sai. Hạ bậc là cầu nối tư duy rất quan trọng, đặc biệt khi hệ số không hằng.
- "Chỉ cần đặt $$ y_2=vy_1 $$ rồi thay trực tiếp là xong." Chưa đủ. Cần rút gọn cẩn thận để thu phương trình cho $$ v' $$.

## Tiến trình học tập đề xuất
### Bước 1: Chuẩn hóa phương trình
Viết về dạng
$$ y''+p(t)y'+q(t)y=0. $$

### Bước 2: Đặt $$ y_2=vy_1 $$
Đây là giả thiết cấu trúc trung tâm.

### Bước 3: Tính đạo hàm và thế vào
Phải làm chậm, rõ và có tổ chức.

### Bước 4: Giảm xuống phương trình cho $$ v' $$
Thường đặt
$$ u=v' $$
để giải dễ hơn.

### Bước 5: Kiểm tra độc lập tuyến tính
Nghiệm mới phải không phải là bội hằng của $$ y_1 $$.

### Các checkpoint
- Sinh viên có phân biệt được $$ v $$ là hàm chứ không phải hằng số hay không.
- Sinh viên có rút gọn đúng các số hạng dùng phương trình của $$ y_1 $$ hay không.
- Sinh viên có kiểm tra rằng nghiệm mới thực sự độc lập với nghiệm cũ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Một bài cổ điển
Xét
$$ y''-\frac{2}{t}y'+\frac{2}{t^2}y=0,\qquad t>0, $$
và biết một nghiệm là
$$ y_1=t. $$
Ta đặt
$$ y_2=vt. $$
Khi đó
$$ y_2'=v't+v, $$
$$ y_2''=v''t+2v'. $$
Thế vào phương trình:
$$
\left(v''t+2v'\right)-\frac{2}{t}\left(v't+v\right)+\frac{2}{t^2}(vt)=0.
$$
Rút gọn:
$$ v''t+2v'-2v'-\frac{2v}{t}+\frac{2v}{t}=0, $$
nên
$$ tv''=0. $$
Suy ra
$$ v''=0 \Rightarrow v'=C \Rightarrow v=Ct+D. $$
Chọn phần tạo nghiệm mới độc lập, lấy $$ v=t $$, ta được
$$ y_2=t^2. $$
Vậy nghiệm tổng quát là
$$ y=c_1t+c_2t^2. $$

### Ví dụ 2: Bài có logarit
Xét
$$ t^2y''-ty'+y=0,\qquad t>0, $$
và biết
$$ y_1=t. $$
Chia cho $$ t^2 $$:
$$ y''-\frac{1}{t}y'+\frac{1}{t^2}y=0. $$
Đặt
$$ y_2=vt. $$
Ta có
$$ y_2'=v't+v,\qquad y_2''=v''t+2v'. $$
Thế vào phương trình:
$$
\left(v''t+2v'\right)-\frac{1}{t}\left(v't+v\right)+\frac{1}{t^2}(vt)=0.
$$
Rút gọn:
$$ tv''+v'=0. $$
Đặt
$$ u=v', $$
ta được
$$ tu'+u=0. $$
Tách biến:
$$ \frac{u'}{u}=-\frac{1}{t}. $$
Suy ra
$$ u=\frac{C}{t}. $$
Vậy
$$ v=C\ln t + D. $$
Chọn phần độc lập:
$$ v=\ln t. $$
Do đó
$$ y_2=t\ln t. $$

### Ví dụ 3: Kiểm tra độc lập tuyến tính
Với hai nghiệm
$$ y_1=t,\qquad y_2=t\ln t, $$
ta thấy rõ $$ y_2 $$ không phải bội hằng của $$ y_1 $$ vì tỉ số
$$ \frac{y_2}{y_1}=\ln t $$
không phải hằng số. Đây là cách kiểm tra đơn giản nhưng giàu ý nghĩa.

### Ví dụ 4: Khi nào hạ bậc là lựa chọn tốt
Giả sử ta gặp một phương trình có hệ số biến thiên mà việc đoán đặc trưng không dùng được, nhưng nhờ quan sát ta biết một nghiệm đơn giản như $$ y_1=t $$ hoặc $$ y_1=e^t $$. Đây là tình huống lý tưởng của hạ bậc. Bài học ở đây là chọn phương pháp không theo thói quen, mà theo cấu trúc dữ kiện có sẵn.

## Câu hỏi khái niệm
1. Vì sao biết một nghiệm của phương trình cấp hai vẫn chưa đủ để xác định mọi nghiệm?
2. Ý nghĩa thật sự của phép đặt
$$ y_2=vy_1 $$
là gì?
3. Vì sao hạ bậc đặc biệt quan trọng khi hệ số không hằng?

## Bài toán ứng dụng
1. Trong một mô hình vật lý có đối xứng cho ta một nghiệm hiển nhiên, tại sao hạ bậc là bước tự nhiên để hoàn tất không gian nghiệm?
2. Một hệ cơ học có một mode đã biết do điều kiện biên đặc biệt. Hãy giải thích vì sao cần mode thứ hai để mô tả mọi trạng thái ban đầu.
3. Trong bài toán sóng hoặc dao động, việc thiếu một nghiệm độc lập sẽ làm mất khả năng mô tả loại chuyển động nào?

## Chiến lược giảng dạy tương tác
- Trước khi trình bày công thức, hỏi lớp: "Nếu đã biết một nghiệm, em sẽ tận dụng nó như thế nào thay vì bắt đầu lại từ đầu?"
- Cho sinh viên làm việc theo nhóm để thực hiện riêng từng bước đạo hàm và rút gọn, tránh tình trạng một bạn làm hết còn các bạn khác chỉ chép.
- Yêu cầu lớp xác định tại điểm nào việc dùng phương trình của $$ y_1 $$ làm bài toán nhẹ đi.
- Để sinh viên so sánh trực tiếp giữa bài hệ số hằng và bài hệ số biến thiên để thấy hạ bậc hữu ích ở đâu.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên chuẩn bị một mẫu rút gọn từng dòng và cho sinh viên điền vào chỗ trống các đạo hàm của $$ y_2=vy_1 $$. Đây là bài mà lỗi đại số dễ phá hỏng trực giác, nên cấu trúc từng bước rất quan trọng.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi suy ra công thức nghiệm thứ hai dạng tích phân
$$ y_2=y_1\int \frac{e^{-\int p(t)dt}}{y_1^2}dt $$
và giải thích vì sao công thức đó là phiên bản cô đọng của hạ bậc.

## Tóm tắt dễ nhớ
Hạ bậc là cách biến "biết một nghiệm" thành "biết cả không gian nghiệm". Ý tưởng trung tâm là đặt
$$ y_2=vy_1, $$
rồi để hàm $$ v $$ hấp thụ phần tự do còn thiếu. Đây không chỉ là kỹ thuật tính; nó là bài học về cách khai thác cấu trúc đã có.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phương trình Euler-Cauchy trong cơ học vật liệu
- Bài toán: Một số bài toán đàn hồi hoặc ổn định cho phương trình có hệ số biến thiên, trong đó ta đoán được một nghiệm cơ sở nhờ đối xứng tỷ lệ.
- Mô hình:
$$ y''+p(t)y'+q(t)y=0 $$
với một nghiệm đã biết $$ y_1(t) $$.
- Giả thiết và giới hạn: Biết trước một nghiệm là lợi thế lớn, nhưng không phải lúc nào cũng có sẵn từ trực giác.
- Diễn giải: Hạ bậc khai thác đúng thông tin đã có để sinh nghiệm còn lại thay vì bắt đầu lại từ đầu.

#### Bài toán hình học hoặc đối xứng
- Bài toán: Một nghiệm xuất hiện từ điều kiện đối xứng, bảo toàn, hoặc phép biến đổi tỉ lệ.
- Mô hình:
$$ y_2=v(t)y_1(t). $$
- Giả thiết và giới hạn: Phương pháp có thể cho tích phân khó, nên đúng về cấu trúc không có nghĩa luôn đẹp về tính toán.
- Diễn giải: Biến $$ v(t) $$ hấp thụ phần tự do còn thiếu để tạo ra hướng nghiệm độc lập.

#### Cầu nối tới lượng tử và Sturm-Liouville
- Bài toán: Nhiều bài toán giá trị riêng cho biết một nghiệm đặc biệt rồi cần dựng nghiệm thứ hai.
- Mô hình: Vẫn là hạ bậc cho ODE tuyến tính cấp hai.
- Giả thiết và giới hạn: Khi điều kiện biên hoặc điểm kỳ dị phức tạp, cần thêm lý thuyết sâu hơn.
- Diễn giải: Phương pháp này là bước đệm tự nhiên trước khi học Wronskian và biến thiên hằng số.

### 2. Trực giác bổ sung và các kết nối

Hạ bậc là một bài học về tái sử dụng cấu trúc. Thay vì hỏi "nghiệm thứ hai là gì", ta hỏi "khác nghiệm thứ nhất ở đâu". Câu trả lời là khác ở hệ số biến thiên theo thời gian. Đây là một trong những nơi tốt nhất để nhấn mạnh rằng độc lập tuyến tính không phải là hình thức phụ: ta cần một hướng nghiệm mới thật sự. Bài này nối thẳng sang Wronskian vì Wronskian sẽ kiểm tra đúng điều đó.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.2, 4, 500)
y1 = t
y2 = t**2

plt.plot(t, y1, label="y1 = t")
plt.plot(t, y2, label="y2 = t^2")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Hai nghiệm độc lập sau hạ bậc")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Trong ví dụ cổ điển của bài, hạ bậc từ $$ y_1=t $$ dẫn đến $$ y_2=t^2 $$. Hình giúp sinh viên thấy nghiệm mới không chỉ là bội hằng của nghiệm cũ.

### 4. Gợi ý tìm thêm mô phỏng

- search: reduction of order differential equations example
- search: second solution from known solution visualization
- search: Wronskian reduction of order connection

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$ y''-\frac{2}{t}y'+\frac{2}{t^2}y=0,\qquad t>0, $$
và biết một nghiệm là
$$ y_1=t. $$
Đặt
$$ y_2=v(t)t. $$
Thế vào, rút gọn được
$$ t v''=0. $$
Suy ra
$$ v''=0,\qquad v=At+B. $$
Bỏ phần tạo lại bội hằng của $$ y_1 $$, ta lấy thành phần mới và được
$$ y_2=t^2. $$
Kết luận:
$$ y(t)=c_1 t+c_2 t^2. $$
Ví dụ này rất tốt vì sinh viên thấy nghiệm thứ hai được "sinh ra" từ nghiệm thứ nhất một cách có hệ thống.

### 6. Phân tầng độ khó

**Bậc đại học.** Làm chậm phần đạo hàm và rút gọn để hiểu vì sao bậc phương trình cho $$ v $$ giảm xuống.

**Bậc sau đại học.** Dẫn ra công thức tích phân kín cho nghiệm thứ hai và liên hệ với Abel:
$$ y_2=y_1\int \frac{e^{-\int p(t)\,dt}}{y_1^2}\,dt. $$

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rất rõ hạ bậc trong các bài hệ số biến thiên.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập tốt để luyện đạo hàm và rút gọn.
- Ross — *Differential Equations*: hữu ích để ôn lại mục tiêu thực sự của phương pháp.
