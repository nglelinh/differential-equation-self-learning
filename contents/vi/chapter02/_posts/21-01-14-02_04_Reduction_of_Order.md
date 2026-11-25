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

Với phương trình hệ số biến thiên $y'' + p(t)y' + q(t)y = 0$, phương trình đặc trưng không còn dùng được nữa—nhưng giả sử bằng trực giác hay quan sát vật lý bạn tìm được **một nghiệm $y_1(t)$**. Liệu có cách nào vắt kiệt thông tin từ $y_1$ để tự động sinh ra nghiệm độc lập thứ hai $y_2(t)$? Câu trả lời chính là **phương pháp Hạ bậc (Reduction of Order)**: đặt $y_2(t) = v(t)y_1(t)$ sẽ làm triệt tiêu sạch số hạng chứa $v$ và đưa bài toán về phương trình tách biến cấp một cho $w = v'$!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Hạ bậc

1. **Phép thế d'Alembert ($y_2(t) = v(t)\,y_1(t)$)**:
   Nếu $v$ là hằng số thì $v y_1$ phụ thuộc tuyến tính với $y_1$; để độc lập tuyến tính, ta cho $v(t)$ biến thiên không hằng!
2. **Cơ chế triệt tiêu số hạng $v$**:
   Khi thay $y_2 = v y_1$ vào $y'' + p y' + q y = 0$, hệ số của $v$ chính là $y_1'' + p y_1' + q y_1 = 0$, nên phương trình chỉ còn $y_1 v'' + (2y_1' + p y_1)v' = 0$.
3. **Công thức tích phân đóng qua Định lý Abel**:
   Đặt $w = v'$ và giải tách biến ta thu được ngay công thức vạn năng:
   $$y_2(t) = y_1(t)\int \frac{e^{-\int p(t)\,dt}}{[y_1(t)]^2}\,dt.$$
4. **Sức mạnh thống nhất**:
   Hạ bậc không chỉ giải thích nguồn gốc nghiệm $t e^{rt}$ (nghiệm kép) và $x^r \ln x$ (phương trình Euler), mà còn dùng được cho mọi phương trình hệ số biến thiên như Legendre hay Bessel!

## Mục tiêu
Bài học này giúp sinh viên hiểu cách tìm nghiệm thứ hai của phương trình tuyến tính cấp hai thuần nhất khi đã biết một nghiệm không tầm thường. Sinh viên sẽ nắm bản chất của phép đặt $$ y_2=v(t)y_1(t) $$, biết khi nào nên dùng phương pháp hạ bậc, và thấy rằng một nghiệm đã biết có thể dùng để xây dựng toàn bộ không gian nghiệm.

## Kiến thức nền
Sinh viên cần nắm phương trình tuyến tính cấp hai, nguyên lý chồng chất, quy tắc đạo hàm của tích và khái niệm độc lập tuyến tính. Hiểu rõ vì sao bài toán thuần nhất cấp hai cần hai nghiệm độc lập là cơ sở của toàn bộ bài học.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-04 Hạ bậc]({{ site.imgurl }}/chapter_img/chapter02/02_04_reduction_of_order.svg)

Trong một số bài toán, ta biết trước một nghiệm nhờ trực giác vật lý, tính đối xứng hoặc quan sát trực tiếp. Tuy nhiên, một nghiệm chưa đủ để viết nghiệm tổng quát của phương trình cấp hai thuần nhất. Câu hỏi đặt ra là liệu có thể tận dụng chính nghiệm đã biết để tìm nghiệm độc lập còn lại hay không.

Phương pháp hạ bậc giải quyết trực tiếp câu hỏi này. Thay vì tìm nghiệm mới từ đầu, ta tìm nó dưới dạng tích của một hàm biến thiên với nghiệm đã biết. Cách tiếp cận này thể hiện rõ tinh thần khai thác cấu trúc sẵn có của phương trình tuyến tính.

### Giải thích: Dùng Hạ bậc tìm nghiệm thứ hai của $t^2 y'' - 3t y' + 4y = 0$ ($t > 0$) khi biết sẵn $y_1(t) = t^2$

1. **Đưa về dạng chuẩn tắc**: Chia cho $t^2 > 0$:
   $$y'' - \frac{3}{t}y' + \frac{4}{t^2}y = 0 \implies p(t) = -\frac{3}{t}.$$
2. **Tính thừa số Abel $e^{-\int p(t)\,dt}$**:
   $$e^{-\int (-3/t)\,dt} = e^{3\ln t} = \mathbf{t^3}.$$
3. **Áp dụng công thức Hạ bậc** với $[y_1(t)]^2 = (t^2)^2 = t^4$:
   $$y_2(t) = t^2 \int \frac{t^3}{t^4}\,dt = t^2 \int \frac{1}{t}\,dt = \mathbf{t^2 \ln t}.$$
4. **Kiểm chứng trực tiếp**:
   $y_2' = 2t\ln t + t$, $\;y_2'' = 2\ln t + 3$. Thay vào vế trái:
   $t^2(2\ln t + 3) - 3t(2t\ln t + t) + 4(t^2\ln t) = (2 - 6 + 4)t^2\ln t + (3 - 3)t^2 = \mathbf{0}$!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Có thể xem nghiệm đã biết $$ y_1 $$ như một hướng chuyển động cơ bản của hệ. Để tạo ra nghiệm thứ hai độc lập, ta cho hệ số nhân của hướng đó biến thiên theo thời gian thay vì giữ cố định. Hệ số biến thiên này chính là hàm $$ v(t) $$.

### Cách nhìn hình ảnh
Nếu $$ y_1 $$ là một đường cong nghiệm, thì nghiệm thứ hai không thể chỉ là bản sao co giãn theo hằng số của $$ y_1 $$. Ta cần một hệ số co giãn thay đổi theo thời gian để tạo nên một đường cong mới độc lập nhưng vẫn thỏa mãn phương trình. Hạ bậc là cơ chế thực hiện điều đó.

### Cách nhìn hình thức
Xét phương trình thuần nhất ở dạng chuẩn hóa
$$ y''+p(t)y'+q(t)y=0. $$
Giả sử $$ y_1(t) $$ là một nghiệm không tầm thường. Ta tìm nghiệm thứ hai dưới dạng $$ y_2=v(t)y_1(t) $$. Lấy đạo hàm:
$$ y_2'=v'y_1+vy_1',\qquad y_2''=v''y_1+2v'y_1'+vy_1''. $$
Thế vào phương trình và sử dụng giả thiết $$ y_1 $$ là nghiệm, các số hạng chứa $$ v $$ sẽ triệt tiêu, để lại một phương trình bậc thấp hơn theo $$ v' $$. Đó là lý do phương pháp được gọi là hạ bậc.

## Những ngộ nhận thường gặp
- "Biết một nghiệm thì chỉ cần nhân với hằng số khác để được nghiệm thứ hai." Sai: ta cần một nghiệm độc lập tuyến tính, không phải bội hằng của nghiệm cũ.
- "Hạ bậc luôn cho phép tính đơn giản." Không hẳn: phương pháp đúng về mặt lý thuyết nhưng có thể dẫn tới tích phân khó tính bằng công thức sơ cấp.
- "Đã biết công thức tổng quát thì không cần hiểu hạ bậc." Sai: hạ bậc là công cụ quan trọng khi phương trình có hệ số biến thiên.
- "Chỉ cần đặt $$ y_2=vy_1 $$ rồi thay vào là xong." Chưa đủ: cần rút gọn cẩn thận nhờ phương trình của $$ y_1 $$ để thu được phương trình cấp một theo $$ v' $$.

## Tiến trình học tập đề xuất
### Bước 1: Chuẩn hóa phương trình
Đưa phương trình về dạng $$ y''+p(t)y'+q(t)y=0 $$.

### Bước 2: Đặt $$ y_2=vy_1 $$
Đây là giả thiết cấu trúc trung tâm của phương pháp.

### Bước 3: Tính đạo hàm và thay vào phương trình
Thực hiện cẩn thận, giữ rõ từng nhóm số hạng theo $$ v'' $$, $$ v' $$ và $$ v $$.

### Bước 4: Đưa về phương trình cấp một theo $$ v' $$
Đặt $$ u=v' $$ để giải phương trình cấp một thuận tiện hơn.

### Bước 5: Kiểm tra tính độc lập tuyến tính
Đảm bảo nghiệm mới không phải là bội hằng của $$ y_1 $$.

### Các checkpoint
- Sinh viên có phân biệt rõ $$ v $$ là hàm số chứ không phải hằng số hay không.
- Sinh viên có biết rút gọn nhóm số hạng chứa $$ v $$ bằng phương trình của $$ y_1 $$ hay không.
- Sinh viên có kiểm tra rằng nghiệm mới độc lập tuyến tính với nghiệm cũ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Phương trình hệ số biến thiên cơ bản
Xét phương trình
$$ y''-\frac{2}{t}y'+\frac{2}{t^2}y=0,\qquad t>0, $$
với một nghiệm đã biết là $$ y_1=t $$. Đặt $$ y_2=vt $$, ta có $$ y_2'=v't+v $$ và $$ y_2''=v''t+2v' $$. Thế vào phương trình:
$$
\left(v''t+2v'\right)-\frac{2}{t}\left(v't+v\right)+\frac{2}{t^2}(vt)=0.
$$
Rút gọn thu được $$ tv''=0 $$, suy ra $$ v''=0 \Rightarrow v'=C \Rightarrow v=Ct+D $$. Chọn phần tạo nghiệm độc lập mới bằng cách lấy $$ v=t $$, ta được $$ y_2=t^2 $$. Vậy nghiệm tổng quát là
$$ y=c_1t+c_2t^2. $$

### Ví dụ 2: Nghiệm chứa hàm logarit
Xét phương trình
$$ t^2y''-ty'+y=0,\qquad t>0, $$
với nghiệm đã biết $$ y_1=t $$. Chia hai vế cho $$ t^2 $$:
$$ y''-\frac{1}{t}y'+\frac{1}{t^2}y=0. $$
Đặt $$ y_2=vt $$, ta có $$ y_2'=v't+v $$ và $$ y_2''=v''t+2v' $$. Thế vào phương trình:
$$
\left(v''t+2v'\right)-\frac{1}{t}\left(v't+v\right)+\frac{1}{t^2}(vt)=0.
$$
Rút gọn được $$ tv''+v'=0 $$. Đặt $$ u=v' $$, ta có $$ tu'+u=0 $$. Tách biến:
$$ \frac{u'}{u}=-\frac{1}{t} \Rightarrow u=\frac{C}{t}. $$
Suy ra $$ v=C\ln t + D $$. Chọn phần độc lập $$ v=\ln t $$, ta nhận được
$$ y_2=t\ln t. $$

### Ví dụ 3: Kiểm tra độc lập tuyến tính
Với hai nghiệm $$ y_1=t $$ và $$ y_2=t\ln t $$, tỉ số
$$ \frac{y_2}{y_1}=\ln t $$
không phải hằng số, nên $$ y_2 $$ không phải bội hằng của $$ y_1 $$. Hai nghiệm này độc lập tuyến tính trên khoảng $$ t>0 $$.

### Ví dụ 4: Khi nào hạ bậc là lựa chọn phù hợp
Khi gặp phương trình có hệ số biến thiên không thể dùng phương trình đặc trưng, nhưng ta nhận ra trước một nghiệm đơn giản như $$ y_1=t $$ hay $$ y_1=e^t $$, hạ bậc là lựa chọn tự nhiên. Ví dụ này nhấn mạnh việc chọn phương pháp dựa trên thông tin sẵn có của bài toán.

## Câu hỏi khái niệm
1. Vì sao biết một nghiệm của phương trình cấp hai vẫn chưa đủ để xác định toàn bộ tập nghiệm?
2. Ý nghĩa của phép đặt $$ y_2=vy_1 $$ là gì?
3. Vì sao phương pháp hạ bậc đặc biệt hữu ích khi phương trình có hệ số biến thiên?

## Bài toán ứng dụng
1. Trong một mô hình vật lý có tính đối xứng cho sẵn một nghiệm hiển nhiên, vì sao hạ bậc là bước tự nhiên để hoàn thiện không gian nghiệm?
2. Một hệ cơ học có một thành phần nghiệm đã biết do điều kiện đặc biệt. Hãy giải thích vì sao vẫn cần nghiệm thứ hai để mô tả mọi trạng thái ban đầu.
3. Trong bài toán sóng hoặc dao động, việc thiếu một nghiệm độc lập sẽ làm mất khả năng mô tả loại chuyển động nào?

## Chiến lược giảng dạy tương tác
- Trước khi đưa công thức, hỏi lớp: "Nếu đã biết một nghiệm, ta có thể tận dụng nó thế nào thay vì giải lại từ đầu?"
- Cho sinh viên làm việc theo nhóm để thực hiện từng bước đạo hàm và rút gọn.
- Yêu cầu lớp chỉ rõ bước mà phương trình của $$ y_1 $$ giúp triệt tiêu các số hạng chứa $$ v $$.
- So sánh trực tiếp một bài hệ số hằng với một bài hệ số biến thiên để thấy phạm vi phát huy của hạ bậc.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên chuẩn bị khung rút gọn theo từng dòng để sinh viên điền các đạo hàm của $$ y_2=vy_1 $$. Vì lỗi biến đổi đại số dễ làm mất mạch tư duy, việc trình bày rõ từng bước rất có ích.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên chứng minh công thức tích phân cho nghiệm thứ hai
$$ y_2=y_1\int \frac{e^{-\int p(t)dt}}{y_1^2}dt $$
và giải thích vì sao đây là dạng rút gọn của phương pháp hạ bậc.

## Tóm tắt dễ nhớ
Hạ bậc chuyển thông tin từ một nghiệm đã biết thành toàn bộ không gian nghiệm. Phép đặt trung tâm là $$ y_2=vy_1 $$, để hàm $$ v $$ chứa phần tự do còn thiếu và đưa bài toán về phương trình cấp một theo $$ v' $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phương trình Euler-Cauchy trong cơ học vật liệu
- Bài toán: Một số bài toán đàn hồi hoặc ổn định dẫn tới phương trình hệ số biến thiên, trong đó có thể đoán được một nghiệm cơ sở nhờ tính đối xứng tỉ lệ.
- Mô hình: $$ y''+p(t)y'+q(t)y=0 $$ với một nghiệm đã biết $$ y_1(t) $$.
- Giả thiết và giới hạn: Cần biết trước một nghiệm không tầm thường, điều không phải lúc nào cũng tìm ra dễ dàng.
- Diễn giải: Hạ bậc tận dụng trực tiếp thông tin sẵn có để sinh ra nghiệm độc lập còn lại.

#### Bài toán hình học hoặc đối xứng
- Bài toán: Một nghiệm xuất hiện từ điều kiện đối xứng, định luật bảo toàn hoặc phép biến đổi tỉ lệ.
- Mô hình: $$ y_2=v(t)y_1(t) $$.
- Giả thiết và giới hạn: Phương pháp có thể dẫn tới tích phân phức tạp, nên đúng về cấu trúc không đồng nghĩa luôn có biểu thức sơ cấp gọn.
- Diễn giải: Hàm $$ v(t) $$ bù phần tự do còn thiếu để tạo ra hướng nghiệm độc lập thứ hai.

#### Cầu nối tới cơ học lượng tử và bài toán Sturm-Liouville
- Bài toán: Nhiều bài toán giá trị riêng cho trước một nghiệm đặc biệt và cần xây dựng nghiệm thứ hai.
- Mô hình: Phương pháp hạ bậc cho ODE tuyến tính cấp hai.
- Giả thiết và giới hạn: Khi điều kiện biên hoặc điểm kỳ dị phức tạp, cần bổ sung các công cụ lý thuyết sâu hơn.
- Diễn giải: Đây là bước đệm tự nhiên trước khi học định thức Wronskian và biến thiên hằng số.

### 2. Trực giác bổ sung và các kết nối

Hạ bậc cho thấy cách tái sử dụng cấu trúc đã biết: thay vì tìm nghiệm thứ hai độc lập hoàn toàn từ đầu, ta biểu diễn nó thông qua sự sai khác theo thời gian so với nghiệm thứ nhất. Phương pháp này cũng làm nổi bật vai trò thực chất của tính độc lập tuyến tính và nối thẳng sang định thức Wronskian — công cụ kiểm tra điều kiện độc lập đó.

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

Trong ví dụ của bài, hạ bậc từ $$ y_1=t $$ dẫn tới $$ y_2=t^2 $$. Đồ thị cho thấy nghiệm mới có dáng điệu khác hẳn chứ không chỉ là bội hằng của nghiệm cũ.

### 4. Gợi ý tìm thêm mô phỏng

- search: reduction of order differential equations example
- search: second solution from known solution visualization
- search: Wronskian reduction of order connection

### 5. Bài toán mẫu có bối cảnh thực

Xét lại phương trình
$$ y''-\frac{2}{t}y'+\frac{2}{t^2}y=0,\qquad t>0, $$
với nghiệm đã biết $$ y_1=t $$. Đặt $$ y_2=v(t)t $$, thay vào và rút gọn thu được $$ t v''=0 $$, suy ra $$ v''=0 $$ và $$ v=At+B $$. Loại bỏ phần hằng $$ B $$ (vốn chỉ tạo lại bội của $$ y_1 $$), ta chọn $$ y_2=t^2 $$ và thu được nghiệm tổng quát
$$ y(t)=c_1 t+c_2 t^2. $$
Quy trình này minh họa cách sinh nghiệm thứ hai một cách hệ thống từ một nghiệm sẵn có.

### 6. Phân tầng độ khó

**Bậc đại học.** Thực hiện cẩn thận bước lấy đạo hàm và rút gọn để hiểu vì sao bậc của phương trình theo $$ v $$ giảm đi một.

**Bậc sau đại học.** Chứng minh công thức tích phân kín cho nghiệm thứ hai và liên hệ với đồng nhất thức Abel:
$$ y_2=y_1\int \frac{e^{-\int p(t)\,dt}}{y_1^2}\,dt. $$

## Video tham khảo

- Xem trước: [❖ Reduction of Order: Basic Example in Differential Equations ❖](https://www.youtube.com/watch?v=oQSFW8BIrY0) — Patrick J, tiếng Anh. Ví dụ cơ bản về hạ bậc: tìm $$ y_2=v(x)y_1 $$ khi đã biết một nghiệm.
- [Reduction of orders, 2nd order differential equations with variable coefficients](https://www.youtube.com/watch?v=qw7lsWSkfGA) — blackpenredpen, tiếng Anh. Áp dụng hạ bậc cho phương trình cấp hai hệ số biến thiên.
- [Reduction of Order (Introduction)](https://www.youtube.com/watch?v=dtZjxolpzqM) — Houston Math Prep, tiếng Anh. Trình bày cách xây dựng phương pháp trước khi đi vào phần biến đổi đại số của ví dụ.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ phương pháp hạ bậc cho các bài hệ số biến thiên.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập rèn luyện kỹ năng đạo hàm và rút gọn.
- Ross — *Differential Equations*: hữu ích để ôn lại ý tưởng cốt lõi của phương pháp.
