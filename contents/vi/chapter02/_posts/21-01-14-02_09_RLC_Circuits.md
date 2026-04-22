---
layout: post
title: "02-09 Mạch điện RLC"
chapter: '02'
order: 9
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên thấy cách phương trình cấp hai xuất hiện trong mạch điện RLC, hiểu sự tương đồng cấu trúc giữa mạch điện và dao động cơ học, giải được các bài toán tự do và cưỡng bức cơ bản, đồng thời diễn giải được các tham số điện trở, điện cảm và điện dung dưới ngôn ngữ động học.

## Kiến thức nền
Sinh viên nên nắm ODE tuyến tính cấp hai hệ số hằng, dao động cơ học và định luật Kirchhoff. Không cần nền điện tử sâu; điều quan trọng hơn là biết điện tích $$ q(t) $$, dòng điện $$ i(t)=q'(t) $$ và điện áp trên từng phần tử.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-09 Mạch điện RLC]({{ site.imgurl }}/chapter_img/chapter02/02_09_rlc_circuits.svg)

Mạch RLC là một trong những ví dụ đẹp nhất cho sự thống nhất của toán học ứng dụng. Một bên là khối lượng - lò xo - giảm chấn trong cơ học. Bên kia là điện cảm - tụ điện - điện trở trong mạch điện. Dù bản chất vật lý khác nhau, cả hai đều dẫn đến cùng một cấu trúc ODE cấp hai. Điều này giúp sinh viên thấy rằng toán học không chỉ giải bài, mà còn chỉ ra các hiện tượng khác ngành có cùng xương sống.

Trong mạch RLC, điện cảm đóng vai trò quán tính, điện trở đóng vai trò cản, còn tụ điện tạo cơ chế hồi phục. Vì vậy, các chế độ quá tắt, tắt tới hạn, dưới tắt và cộng hưởng điện học đều có thể đọc bằng chính ngôn ngữ đã học ở dao động cơ học.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nếu cơ học là "vật không muốn thay đổi vận tốc ngay", thì điện cảm là "dòng điện không muốn thay đổi ngay". Nếu lò xo lưu năng lượng đàn hồi, tụ điện lưu năng lượng điện trường. Điện trở tiêu tán năng lượng như ma sát.

### Cách nhìn hình ảnh
Điện tích hoặc dòng điện trong mạch RLC có thể dao động, tắt dần hoặc về cân bằng không dao động tùy tham số. Đồ thị tín hiệu theo thời gian rất giống đồ thị dao động cơ học: có thể là sin-cos tắt dần, mũ kép suy giảm hoặc hồi đáp cộng hưởng.

### Cách nhìn hình thức
Theo định luật Kirchhoff cho mạch nối tiếp RLC:
$$
L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac{1}{C}q=E(t),
$$
trong đó $$ q(t) $$ là điện tích trên tụ và $$ i(t)=q'(t) $$ là dòng điện. Nếu
$$ E(t)=0, $$
ta có đáp ứng tự do. Nếu $$ E(t)\neq 0 $$, ta có đáp ứng cưỡng bức.

## Những ngộ nhận thường gặp
- "Mạch điện chỉ dẫn đến phương trình cấp một." Sai. Mạch RLC nối tiếp tự nhiên dẫn đến ODE cấp hai.
- "Điện trở càng lớn thì hệ càng về cân bằng nhanh hơn." Không hẳn. Quá lớn có thể làm hệ quay về chậm hơn so với tắt dần tới hạn.
- "Nếu có dao động thì chắc chắn mạch không có điện trở." Sai. Dao động tắt dần xuất hiện khi điện trở có nhưng chưa quá lớn.
- "Cộng hưởng chỉ là khái niệm cơ học." Sai. Nó rất quan trọng trong điện tử và xử lý tín hiệu.

## Tiến trình học tập đề xuất
### Bước 1: Viết định luật Kirchhoff
Tổng điện áp trên cuộn cảm, điện trở và tụ bằng nguồn ngoài.

### Bước 2: Chọn biến trạng thái
Thường là điện tích $$ q(t) $$, rồi dòng điện suy ra bằng $$ q'(t) $$.

### Bước 3: Phân tích phần thuần nhất
Đọc chế độ từ phương trình đặc trưng.

### Bước 4: Nếu có nguồn, tìm nghiệm cưỡng bức
Phân biệt phần quá độ và phần ổn định.

### Các checkpoint
- Sinh viên có viết đúng phương trình cho $$ q(t) $$ hay không.
- Sinh viên có thấy sự tương đồng giữa RLC và dao động cơ học hay không.
- Sinh viên có diễn giải được tín hiệu dài hạn trong mạch hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mạch không nguồn
Xét
$$ q''+4q'+5q=0. $$
Phương trình đặc trưng:
$$ r^2+4r+5=0, $$
cho
$$ r=-2\pm i. $$
Vậy
$$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right). $$
Điện tích dao động tắt dần về 0. Dòng điện $$ i=q' $$ cũng tắt dần.

### Ví dụ 2: Tắt dần tới hạn trong mạch
Xét
$$ q''+6q'+9q=0. $$
Ta có nghiệm kép $$ r=-3 $$, nên
$$ q(t)=\left(c_1+c_2t\right)e^{-3t}. $$
Đây là đáp ứng không dao động nhưng về 0 nhanh nhất trong lớp không dao động.

### Ví dụ 3: Mạch có nguồn không đổi
Xét
$$ q''+3q'+2q=10. $$
Nghiệm thuần nhất:
$$ q_h=c_1e^{-t}+c_2e^{-2t}. $$
Thử nghiệm riêng hằng $$ q_p=A $$:
$$ 2A=10 \Rightarrow A=5. $$
Vậy
$$ q(t)=c_1e^{-t}+c_2e^{-2t}+5. $$
Điều này cho thấy mạch tiến dần tới trạng thái điện tích ổn định bằng 5.

### Ví dụ 4: Nguồn tuần hoàn và cộng hưởng
Xét
$$ q''+q=\cos t. $$
Đây là mô hình lý tưởng không cản, và forcing trùng với tần số riêng. Nghiệm riêng có dạng cộng hưởng:
$$ q_p=\frac{1}{2}t\sin t. $$
Do đó
$$ q(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Biên độ tăng theo thời gian, cho thấy cộng hưởng điện học rõ rệt.

## Câu hỏi khái niệm
1. Vì sao mạch RLC và hệ cơ học lại có cùng cấu trúc phương trình?
2. Điện trở ảnh hưởng đến tín hiệu theo cách tương tự lực cản cơ học như thế nào?
3. Trong mạch có nguồn tuần hoàn, vì sao phần quá độ và phần ổn định cần được tách ra?

## Bài toán ứng dụng
1. Một mạch lọc tín hiệu cần loại bỏ dao động quá độ nhanh. Hãy giải thích vai trò của điện trở trong thiết kế.
2. Một mạch cộng hưởng vô tuyến cần nhạy với một tần số nhất định. Hãy liên hệ điều này với tần số riêng của mạch.
3. Một cảm biến điện tử có tín hiệu dao động rung trước khi ổn định. Hãy giải thích hiện tượng đó bằng ngôn ngữ RLC.

## Chiến lược giảng dạy tương tác
- Yêu cầu sinh viên ghép cặp các đại lượng cơ học và điện học: khối lượng với điện cảm, ma sát với điện trở, lò xo với tụ điện.
- Cho lớp so sánh trực tiếp hai phương trình: một của lò xo, một của mạch RLC, rồi thảo luận xem điều gì giống và khác.
- Hỏi sinh viên: "Nếu tăng điện trở, em dự đoán tín hiệu sẽ bớt dao động theo nghĩa nào?"
- Có thể dùng mô phỏng mạch đơn giản hoặc hình ảnh đáp ứng bước để tăng trực giác.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên dùng bảng song song giữa cơ học và điện học để sinh viên không thấy phần điện quá xa lạ. Khi thấy cấu trúc ODE giống nhau, các em thường tự tin hơn nhiều.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi tính hàm truyền của mạch RLC đơn giản hoặc khảo sát biên độ trạng thái ổn định dưới forcing tuần hoàn theo tần số nguồn.

## Tóm tắt dễ nhớ
Mạch RLC là phiên bản điện học của dao động cơ học. Phương trình
$$ Lq''+Rq'+\frac{1}{C}q=E(t) $$
cho ta toàn bộ câu chuyện: điện cảm như quán tính, điện trở như cản, tụ điện như hồi phục. Khi hiểu điều này, nhiều hiện tượng điện học trở nên quen thuộc như những bài lò xo.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bộ lọc điện tử bậc hai
- Bài toán: Mạch RLC được dùng để lọc hoặc chọn tần trong xử lý tín hiệu.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Giả thiết và giới hạn: Linh kiện lý tưởng và tuyến tính.
- Diễn giải: Hệ có thể dao động, tắt dần hoặc cộng hưởng điện học tùy thông số và nguồn vào.

#### Bộ chỉnh lưu và đáp ứng quá độ
- Bài toán: Sau khi đóng mạch, dòng và điện tích không đạt trạng thái ổn định ngay mà đi qua quá độ.
- Mô hình: Vẫn là phương trình RLC cấp hai.
- Giả thiết và giới hạn: Không xét chuyển mạch phi tuyến của diode hay transistor.
- Diễn giải: Thành phần thuần nhất mô tả quá độ, còn nghiệm riêng mô tả trạng thái vận hành do nguồn cưỡng bức.

#### Cảm biến cộng hưởng điện cơ
- Bài toán: Thiết bị phát hiện tín hiệu mạnh nhất quanh một dải tần riêng.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E_0\cos \omega t. $$
- Giả thiết và giới hạn: Một mode chi phối và nguồn điều hòa thuần.
- Diễn giải: Cộng hưởng điện học là phiên bản mạch điện của cộng hưởng cơ học.

### 2. Trực giác bổ sung và các kết nối

Mạch RLC là bài học thống nhất hóa: điện cảm tương ứng quán tính, điện trở tương ứng cản, điện dung tương ứng lực hồi phục. Khi sinh viên thực sự thấy sự tương đương này, rất nhiều công thức không còn rời rạc nữa. Một ngộ nhận hay gặp là tưởng điện trở càng lớn thì đáp ứng càng "tốt"; thực ra cản quá lớn có thể làm hệ quay về chậm hơn trạng thái tới hạn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
q = np.exp(-2*t) * (np.cos(t) + 0.5*np.sin(t))
i = np.gradient(q, t)

plt.plot(t, q, label="Điện tích q(t)")
plt.plot(t, i, label="Dòng điện i(t)=q'(t)")
plt.xlabel("t")
plt.ylabel("Biên độ")
plt.title("Đáp ứng tắt dần của mạch RLC")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đặt điện tích và dòng điện trên cùng đồ thị giúp sinh viên thấy rõ hơn ý nghĩa của việc chọn biến trạng thái là $$ q(t) $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: RLC circuit resonance interactive
- search: transient response RLC animation
- search: circuit mechanical analogy visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét mạch không nguồn
$$ q''+4q'+5q=0,\qquad q(0)=1,\qquad q'(0)=0. $$
Nghiệm có dạng
$$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right). $$
Áp điều kiện đầu:
$$ q(t)=e^{-2t}\left(\cos t+2\sin t\right). $$
Từ đây
$$ i(t)=q'(t) $$
cũng tắt dần về 0. Về mặt kỹ thuật, đây là một đáp ứng quá độ suy giảm có dao động do năng lượng qua lại giữa cuộn cảm và tụ điện.

### 6. Phân tầng độ khó

**Bậc đại học.** Lập đúng phương trình RLC, giải phần thuần nhất và đọc tương đồng với dao động cơ học.

**Bậc sau đại học.** Nối với hàm truyền, đáp ứng tần số, và thiết kế chọn lọc băng thông.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần mạch RLC rất phù hợp để thấy sự tương đồng với cơ học.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài luyện về đáp ứng quá độ và cưỡng bức.
- Ross — *Differential Equations*: gọn và tốt để ôn lại cấu trúc mô hình.
