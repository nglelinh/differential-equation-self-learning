---
layout: post
title: "02-08 Dao động Cơ học"
chapter: '02'
order: 8
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên chuyển toàn bộ kỹ thuật chương 02 vào mô hình vật lý trung tâm: hệ khối lượng - lò xo - giảm chấn. Sinh viên sẽ học cách lập phương trình, phân biệt dao động tự do và dao động cưỡng bức, đọc các chế độ quá tắt dần, tắt dần tới hạn, dưới tắt dần, và hiểu hiện tượng cộng hưởng dưới góc nhìn cơ học.

## Kiến thức nền
Sinh viên cần nắm phương trình tuyến tính cấp hai hệ số hằng, nghiệm thực, nghiệm phức và phương trình không thuần nhất. Kiến thức vật lý cần chỉ ở mức cơ bản: định luật Newton, lực đàn hồi Hooke và lực cản tuyến tính.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-08 Dao động Cơ học]({{ site.imgurl }}/chapter_img/chapter02/02_08_mechanical_vibrations.svg)

Dao động cơ học là một trong những ứng dụng đẹp nhất của ODE cấp hai vì mọi thành phần trong phương trình đều có ý nghĩa vật lý rõ ràng. Khối lượng $$ m $$ tạo quán tính, lò xo với hằng số $$ k $$ tạo lực hồi phục, và lực cản $$ c $$ hấp thụ năng lượng. Chỉ cần ba tham số này, ta đã có thể mô tả những hiện tượng rất phong phú: dao động thuần, tắt dần, quay về cân bằng nhanh nhất, hay rung mạnh dưới tác động tuần hoàn.

Đây cũng là bài học giúp sinh viên thấy sức mạnh của việc diễn giải nghiệm. Công thức không còn là kết quả trừu tượng. Mỗi dấu và mỗi tham số trả lời một câu hỏi cơ học: vật có rung hay không, rung bao lâu, trở về cân bằng như thế nào, và khi nào thì ngoại lực gây ra cộng hưởng nguy hiểm.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nếu kéo nhẹ một vật gắn lò xo rồi buông ra, lò xo kéo vật về vị trí cân bằng. Nếu không có ma sát, vật vượt qua cân bằng và tiếp tục dao động mãi. Nếu có lực cản, dao động yếu dần. Nếu có lực tác động tuần hoàn bên ngoài, vật có thể rung mạnh nếu tần số kích thích gần tần số riêng.

### Cách nhìn hình ảnh
Ba chế độ chính có thể được nhìn trực tiếp trên đồ thị:

- Quá tắt dần: vật trở về cân bằng không dao động, khá chậm.
- Tắt dần tới hạn: vật trở về cân bằng nhanh nhất mà không dao động.
- Dưới tắt dần: vật dao động với biên độ giảm dần.

Khi có cưỡng bức tuần hoàn, đồ thị còn thể hiện phần quá độ suy giảm và phần cưỡng bức ổn định theo tần số nguồn.

### Cách nhìn hình thức
Với chuyển vị $$ x(t) $$ quanh vị trí cân bằng, mô hình chuẩn là
$$ m x''+c x'+k x=F(t). $$
Nếu
$$ F(t)=0, $$
ta có dao động tự do. Nếu
$$ F(t)\neq 0, $$
ta có dao động cưỡng bức. Phương trình đặc trưng của phần thuần nhất là
$$ m r^2+c r+k=0. $$
Biệt thức
$$ \Delta=c^2-4mk $$
quyết định chế độ dao động.

## Những ngộ nhận thường gặp
- "Có lực cản thì vật không còn dao động." Sai. Nếu cản nhỏ, hệ vẫn dao động nhưng tắt dần.
- "Tắt dần tới hạn là cản lớn nhất." Sai. Đó là mức cản vừa đủ để trở về cân bằng nhanh nhất mà không dao động.
- "Cộng hưởng chỉ xảy ra khi không có cản." Sai. Cản làm giảm biên độ cộng hưởng nhưng không xóa bản chất hiện tượng.
- "Nghiệm tổng chỉ là phép cộng hình thức." Sai. Nó tách rõ phần quá độ và phần ổn định của hệ.

## Tiến trình học tập đề xuất
### Bước 1: Lập mô hình từ Newton
Viết tổng lực bằng $$ mx'' $$.

### Bước 2: Phân tích phần thuần nhất
Đọc chế độ từ biệt thức $$ c^2-4mk $$.

### Bước 3: Nếu có forcing, tìm nghiệm riêng
Thường là forcing tuần hoàn hoặc hằng.

### Bước 4: Diễn giải vật lý
Phân biệt rõ phần quá độ và phần cưỡng bức dài hạn.

### Các checkpoint
- Sinh viên có viết đúng dấu của lực đàn hồi và lực cản hay không.
- Sinh viên có đọc đúng ba chế độ tắt dần từ biệt thức hay không.
- Sinh viên có giải thích được ý nghĩa của cộng hưởng hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Không cản, không lực ngoài
Xét
$$ x''+9x=0. $$
Nghiệm là
$$ x(t)=c_1\cos 3t+c_2\sin 3t. $$
Đây là dao động điều hòa với tần số góc 3. Cơ năng được bảo toàn, nên biên độ không đổi.

### Ví dụ 2: Dưới tắt dần
Xét
$$ x''+2x'+10x=0. $$
Phương trình đặc trưng:
$$ r^2+2r+10=0, $$
cho
$$ r=-1\pm 3i. $$
Vậy
$$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right). $$
Hệ vẫn dao động nhưng biên độ giảm theo $$ e^{-t} $$.

### Ví dụ 3: Tắt dần tới hạn
Xét
$$ x''+6x'+9x=0. $$
Ta có
$$ r^2+6r+9=0=\left(r+3\right)^2. $$
Nghiệm là
$$ x(t)=\left(c_1+c_2t\right)e^{-3t}. $$
Hệ trở về cân bằng mà không dao động. Đây là mô hình tiêu biểu của tắt dần tới hạn.

### Ví dụ 4: Dao động cưỡng bức tuần hoàn
Xét
$$ x''+x=\cos t. $$
Nghiệm thuần nhất là
$$ x_h=c_1\cos t+c_2\sin t. $$
Vì forcing cộng hưởng với mode riêng, ta thử
$$ x_p=At\sin t. $$
Sau khi thế vào, ta được
$$ A=\frac{1}{2}, $$
nên
$$ x(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Ví dụ này rất quan trọng để trực giác hóa cộng hưởng: biên độ tăng theo thời gian do tần số kích thích trùng tần số riêng.

## Câu hỏi khái niệm
1. Vì sao cùng một hệ lò xo nhưng mức cản khác nhau lại tạo ra ba chế độ hành vi khác nhau?
2. Vì sao nghiệm cưỡng bức và nghiệm quá độ phải được phân biệt rõ về ý nghĩa vật lý?
3. Vì sao cộng hưởng là hiện tượng vừa toán học vừa kỹ thuật quan trọng?

## Bài toán ứng dụng
1. Hệ thống treo của xe máy nên gần với chế độ nào trong ba chế độ tắt dần, và vì sao?
2. Một tòa nhà cao tầng chịu rung do gió tuần hoàn. Hãy giải thích vì sao kỹ sư cần quan tâm đến tần số riêng của công trình.
3. Một dụng cụ đo rung được thiết kế để dập dao động nhanh nhất mà không vượt quá cân bằng. Hãy liên hệ với tắt dần tới hạn.

## Chiến lược giảng dạy tương tác
- Cho sinh viên xem ba đồ thị và đoán chế độ cản trước khi giải phương trình.
- Dùng mô hình lò xo hoặc video dao động để kết nối biểu thức với hiện tượng thật.
- Hỏi lớp: "Nếu tăng cản lên gấp đôi, em dự đoán hệ rung ít đi theo cách nào?"
- Tổ chức một cuộc thảo luận ngắn về cộng hưởng trong đời sống: cầu, nhà, nhạc cụ, máy móc.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên chuẩn bị bảng so sánh ba chế độ: điều kiện trên biệt thức, dạng nghiệm, dạng đồ thị, diễn giải cơ học. Sinh viên yếu thường tiến bộ nhanh khi bốn cột này được đặt cạnh nhau.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi tìm biên độ trạng thái ổn định của dao động cưỡng bức khi có cản, rồi khảo sát tần số nào làm biên độ lớn nhất.

## Tóm tắt dễ nhớ
Dao động cơ học được mô hình bởi
$$ mx''+cx'+kx=F(t). $$
Ba tham số $$ m,c,k $$ quyết định quán tính, cản và hồi phục. Phần thuần nhất cho biết cách hệ tự rung, phần forcing cho biết hệ bị kéo ra sao. Muốn hiểu bài toán, hãy hỏi: có cản không, cản mạnh đến mức nào, và forcing có gần tần số riêng hay không.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ treo ô tô
- Bài toán: Khung xe và bánh xe phản ứng trước mặt đường gồ ghề như một hệ lò xo - giảm chấn.
- Mô hình:
$$ m x''+c x'+k x=F(t). $$
- Giả thiết và giới hạn: Mô hình một bậc tự do là xấp xỉ; hệ treo thật có nhiều khối lượng và phi tuyến.
- Diễn giải: Phân biệt dưới tắt, quá tắt, tắt tới hạn có ý nghĩa trực tiếp với độ êm và độ bám đường.

#### Tòa nhà chịu kích thích tuần hoàn
- Bài toán: Gió hoặc nền rung kích thích công trình gần tần số riêng.
- Mô hình:
$$ m x''+c x'+k x=F_0\cos \omega t. $$
- Giả thiết và giới hạn: Mô hình tuyến tính và dao động nhỏ quanh cân bằng.
- Diễn giải: Cộng hưởng giải thích vì sao thiết kế phải tránh để tần số kích thích khớp với tần số riêng nguy hiểm.

#### Cảm biến MEMS và dao động nội tại
- Bài toán: Một đầu cảm biến cơ điện nhỏ có thể rung lâu nếu giảm chấn yếu.
- Mô hình: Cùng dạng khối lượng - lò xo - giảm chấn.
- Giả thiết và giới hạn: Cản tuyến tính, một mode chi phối.
- Diễn giải: Đáp ứng quá độ cho biết hệ ổn định nhanh hay tiếp tục "rung đuôi" quá lâu.

### 2. Trực giác bổ sung và các kết nối

Dao động cơ học là nơi toàn bộ chương 2 hội tụ: nghiệm thực cho quá tắt, nghiệm kép cho tắt tới hạn, nghiệm phức cho dưới tắt, nghiệm riêng cho forcing và cộng hưởng. Một sai lầm phổ biến là nghĩ tắt tới hạn là "nhiều cản nhất"; thực ra nó là mốc cản vừa đủ để quay về nhanh nhất mà không dao động.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
over = 2*np.exp(-t) - np.exp(-3*t)
critical = (1 + t) * np.exp(-2*t)
under = np.exp(-0.5*t) * np.cos(3*t)

plt.plot(t, over, label="Quá tắt dần")
plt.plot(t, critical, label="Tắt dần tới hạn")
plt.plot(t, under, label="Dưới tắt dần")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Ba chế độ dao động cơ học")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Hình này đặc biệt hữu ích trong giảng dạy vì nó đặt ba chế độ lên cùng một khung hình trực quan.

### 4. Gợi ý tìm thêm mô phỏng

- search: mass spring damper interactive
- search: critical damping animation
- search: mechanical resonance simulation

### 5. Bài toán mẫu có bối cảnh thực

Một hệ treo lý tưởng hóa được mô hình hóa bởi
$$ x''+2x'+10x=0,\qquad x(0)=0.05,\qquad x'(0)=0. $$
Nghiệm là
$$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right). $$
Áp điều kiện đầu được
$$
x(t)=0.05e^{-t}\left(\cos 3t+\frac{1}{3}\sin 3t\right).
$$
Hệ vẫn rung nhưng biên độ giảm dần. Về mặt cơ học, điều này mô tả phản ứng êm hơn so với cộng hưởng không cản nhưng vẫn có dao động đáng kể trước khi ổn định.

### 6. Phân tầng độ khó

**Bậc đại học.** Lập mô hình và phân biệt rõ ba chế độ từ biệt thức.

**Bậc sau đại học.** Đi sâu vào biên độ steady-state dưới forcing tuần hoàn, cộng hưởng có cản, và hàm truyền cơ học.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần dao động cơ học rất giàu trực giác.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều ví dụ cơ-lò-xo và cộng hưởng.
- Ross — *Differential Equations*: hữu ích để ôn nhanh các chế độ tắt dần.
