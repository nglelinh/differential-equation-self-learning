---
layout: post
title: "02-05 Phương trình Không thuần nhất: Hệ số Bất định"
chapter: '02'
order: 5
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên giải các phương trình tuyến tính cấp hai không thuần nhất bằng phương pháp hệ số bất định, biết chọn đúng dạng nghiệm riêng thử, xử lý hiện tượng cộng hưởng bằng cách nhân thêm lũy thừa của $$ t $$, và hiểu vì sao phương pháp này chỉ phù hợp với những họ hàm đóng dưới phép đạo hàm.

## Kiến thức nền
Sinh viên cần nắm nghiệm thuần nhất của phương trình hệ số hằng, nguyên lý chồng chập và kỹ năng lấy đạo hàm các hàm đa thức, mũ, sin-cos. Đây là bài mà tư duy nhận dạng dạng forcing quan trọng không kém kỹ thuật thay thế vào phương trình.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-05 Phương trình Không thuần nhất: Hệ số Bất định]({{ site.imgurl }}/chapter_img/chapter02/02_05_undetermined_coefficients.svg)

Khi vế phải của phương trình không bằng 0, ta cần tìm một nghiệm riêng mô tả phản ứng của hệ trước ngoại lực. Nếu forcing có dạng đẹp như đa thức, mũ, sin-cos hoặc tích của chúng, ta không cần dùng công cụ tổng quát nặng nề. Ta có thể thử một nghiệm cùng họ rồi điều chỉnh các hệ số chưa biết. Đây chính là phương pháp hệ số bất định.

Sự tinh tế của phương pháp nằm ở chỗ không phải cứ nhìn thấy forcing là chép lại y hệt. Nếu dạng thử trùng với một phần của nghiệm thuần nhất, ta phải nhân thêm $$ t $$, đôi khi là $$ t^2 $$, để tạo ra một hàm độc lập tuyến tính. Đây là nơi hiện tượng cộng hưởng xuất hiện dưới ngôn ngữ đại số.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hệ giống như một nhạc cụ bị gõ bởi một kiểu tín hiệu đặc biệt. Nếu tín hiệu đó thuộc một họ "ổn định dưới đạo hàm", thì ta mong phản ứng cưỡng bức cũng thuộc họ đó. Nhưng nếu âm kích thích trùng với mode tự nhiên của hệ, biên độ phản ứng phải thay đổi kiểu khác, và đó là lý do cần nhân thêm $$ t $$.

### Cách nhìn hình ảnh
Nếu forcing là hằng hoặc đa thức, nghiệm riêng thường cong theo đa thức. Nếu forcing là $$ e^{at} $$, nghiệm riêng thường mang cùng dạng mũ. Nếu forcing là $$ \sin bt $$ hoặc $$ \cos bt $$, nghiệm riêng thường là tổ hợp sin-cos. Khi cộng hưởng xảy ra, đồ thị thường xuất hiện số hạng tăng theo $$ t $$ nhân với mode vốn có của hệ.

### Cách nhìn hình thức
Với phương trình
$$ ay''+by'+cy=g(t), $$
ta viết nghiệm tổng dưới dạng
$$ y=y_h+y_p. $$
Phương pháp hệ số bất định tìm $$ y_p $$ bằng cách đoán một dạng thuộc cùng họ với $$ g(t) $$. Nếu dạng đoán trùng với thành phần của $$ y_h $$, ta nhân thêm $$ t^s $$, trong đó $$ s $$ là bội số cần thiết để đạt độc lập tuyến tính.

## Những ngộ nhận thường gặp
- "Chỉ cần chép y nguyên forcing làm nghiệm riêng thử." Sai. Cần xét cả đạo hàm của forcing và khả năng trùng với nghiệm thuần nhất.
- "Nếu dạng thử không đúng thì phương pháp thất bại hoàn toàn." Không đúng. Phần lớn sai sót là do thiếu hạng hoặc thiếu nhân thêm $$ t $$.
- "Mọi forcing đều dùng được hệ số bất định." Sai. Phương pháp chỉ phù hợp với các họ đóng dưới đạo hàm.
- "Cộng hưởng chỉ là khái niệm vật lý." Sai. Nó xuất hiện rất cụ thể khi dạng thử đụng vào nghiệm thuần nhất.

## Tiến trình học tập đề xuất
### Bước 1: Giải phương trình thuần nhất
Không bao giờ bỏ qua bước này, vì nó quyết định việc có cộng hưởng hay không.

### Bước 2: Nhìn forcing và chọn họ hàm phù hợp
Liệt kê toàn bộ các hạng có thể sinh ra sau đạo hàm.

### Bước 3: Kiểm tra trùng với nghiệm thuần nhất
Nếu trùng, nhân thêm $$ t $$ hoặc bậc cao hơn.

### Bước 4: Thế vào để tìm hệ số
Đây là phần đại số cần gọn gàng và có tổ chức.

### Các checkpoint
- Sinh viên có chọn đủ họ hàm thử hay không.
- Sinh viên có phát hiện cộng hưởng hay không.
- Sinh viên có phân biệt nghiệm riêng và nghiệm tổng quát hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Forcing đa thức
Giải
$$ y''-3y'+2y=t. $$
Nghiệm thuần nhất:
$$ y_h=c_1e^t+c_2e^{2t}. $$
Vì forcing là đa thức bậc một, ta thử
$$ y_p=At+B. $$
Khi đó
$$ y_p'=A,\qquad y_p''=0. $$
Thế vào:
$$ 0-3A+2(At+B)=t. $$
So sánh hệ số:
$$ 2A=1 \Rightarrow A=\frac{1}{2}, $$
$$
-3A+2B=0 \Rightarrow -\frac{3}{2}+2B=0 \Rightarrow B=\frac{3}{4}.
$$
Vậy
$$ y(t)=c_1e^t+c_2e^{2t}+\frac{1}{2}t+\frac{3}{4}. $$

### Ví dụ 2: Forcing mũ không cộng hưởng
Giải
$$ y''+y=e^t. $$
Nghiệm thuần nhất:
$$ y_h=c_1\cos t+c_2\sin t. $$
Ta thử
$$ y_p=Ae^t. $$
Thế vào:
$$
Ae^t+Ae^t=e^t \Rightarrow 2A=1 \Rightarrow A=\frac{1}{2}.
$$
Do đó
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}e^t. $$

### Ví dụ 3: Forcing mũ có cộng hưởng
Giải
$$ y''-y=e^t. $$
Nghiệm thuần nhất là
$$ y_h=c_1e^t+c_2e^{-t}. $$
Nếu thử $$ Ae^t $$ thì sẽ trùng với $$ y_h $$, nên phải thử
$$ y_p=Ate^t. $$
Tính đạo hàm:
$$ y_p'=Ae^t+Ate^t, $$
$$ y_p''=2Ae^t+Ate^t. $$
Thế vào:
$$ \left(2Ae^t+Ate^t\right)-Ate^t=e^t. $$
Suy ra
$$ 2A=1 \Rightarrow A=\frac{1}{2}. $$
Vậy
$$ y(t)=c_1e^t+c_2e^{-t}+\frac{1}{2}te^t. $$
Đây là ví dụ cộng hưởng đại số điển hình.

### Ví dụ 4: Forcing lượng giác
Giải
$$ y''+4y=\cos t. $$
Nghiệm thuần nhất:
$$ y_h=c_1\cos 2t+c_2\sin 2t. $$
Vì forcing là $$ \cos t $$, ta thử
$$ y_p=A\cos t+B\sin t. $$
Khi đó
$$ y_p''=-A\cos t-B\sin t. $$
Thế vào:
$$ 3A\cos t+3B\sin t=\cos t. $$
Suy ra
$$ A=\frac{1}{3},\qquad B=0. $$
Vậy
$$ y(t)=c_1\cos 2t+c_2\sin 2t+\frac{1}{3}\cos t. $$

## Câu hỏi khái niệm
1. Vì sao phương pháp hệ số bất định chỉ phù hợp với một số loại forcing nhất định?
2. Vì sao khi forcing trùng với nghiệm thuần nhất ta phải nhân thêm $$ t $$?
3. Trong diễn giải vật lý, hiện tượng cộng hưởng đại số gợi nhắc điều gì?

## Bài toán ứng dụng
1. Một hệ cơ học bị kích thích bởi lực tuần hoàn. Hãy giải thích vì sao forcing lượng giác dẫn đến nghiệm riêng lượng giác.
2. Một mạch điện nhận tín hiệu mũ do nguồn bật lên theo kiểu hàm mũ. Hãy giải thích vì sao nghiệm cưỡng bức thường cùng họ hàm.
3. Một hệ rung được kích bởi tín hiệu đúng mode tự nhiên. Hãy thảo luận vì sao phản ứng có thể xuất hiện số hạng nhân thêm bởi $$ t $$.

## Chiến lược giảng dạy tương tác
- Cho sinh viên tham gia trò chơi "đoán dạng nghiệm riêng" trước khi tính chi tiết.
- Viết lên bảng nhiều forcing khác nhau và yêu cầu lớp chỉ ra bài nào có nguy cơ cộng hưởng.
- Dừng trước bước nhân thêm $$ t $$ và hỏi: "Nếu ta thử dạng cũ thì điều gì xảy ra?"
- Khuyến khích sinh viên giải thích bằng lời vì sao phải bổ sung cả sin lẫn cos khi forcing chỉ có một trong hai.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên yếu dùng bảng quy chiếu giữa loại forcing và dạng thử tương ứng. Việc luyện phân biệt "đa thức", "mũ", "lượng giác", "tích của các họ" sẽ giúp các em bớt sợ phần chọn ansatz.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi giải thích bằng ngôn ngữ không gian vector vì sao các họ forcing phù hợp phải đóng dưới phép đạo hàm, hoặc yêu cầu xử lý forcing dạng $$ te^t $$ hay $$ e^t\cos t $$.

## Tóm tắt dễ nhớ
Hệ số bất định hoạt động khi forcing thuộc một họ đẹp dưới phép đạo hàm. Muốn dùng đúng phương pháp, hãy làm bốn việc: giải phần thuần nhất, chọn đúng họ thử, kiểm tra cộng hưởng, rồi mới tìm hệ số. Nếu dạng thử trùng nghiệm thuần nhất, hãy nhân thêm $$ t $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động cưỡng bức trong cơ học
- Bài toán: Một hệ lò xo bị kích bởi ngoại lực tuần hoàn hoặc hằng.
- Mô hình:
$$ m x''+c x'+k x=F_0\cos \omega t $$
hoặc
$$ m x''+c x'+k x=P_0. $$
- Giả thiết và giới hạn: Hệ số hằng và forcing thuộc họ đóng dưới phép đạo hàm.
- Diễn giải: Nghiệm riêng nên được đoán cùng họ với forcing, trừ khi gặp cộng hưởng.

#### Tín hiệu vào mạch điện
- Bài toán: Nguồn vào là đa thức, mũ, sin-cos hoặc tích của các dạng đó.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Giả thiết và giới hạn: Phương pháp hệ số bất định chỉ hợp khi đạo hàm không đưa ta ra khỏi họ hàm đang xét.
- Diễn giải: Đây là lý do các forcing như $$ \ln t $$ hay $$ \tan t $$ không phù hợp với phương pháp này.

#### Kích thích điều hòa gần tần số riêng
- Bài toán: Hệ bị ép đúng gần mode tự nhiên nên biên độ cưỡng bức tăng mạnh.
- Mô hình:
$$ y''+\omega_0^2 y=\cos \omega_0 t. $$
- Giả thiết và giới hạn: Không có cản hoặc cản rất nhỏ.
- Diễn giải: Nhân thêm $$ t $$ trong ansatz là dấu hiệu đại số của cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Phương pháp hệ số bất định hoạt động vì một số họ hàm đóng dưới phép đạo hàm tạo thành không gian hữu hạn chiều. Điều này làm cho bài toán tìm nghiệm riêng trở thành bài toán tìm hệ số. Đây là một ý tưởng đại số đẹp ẩn dưới kỹ thuật giải. Một lỗi rất thường gặp là chỉ chép nguyên forcing sang nghiệm thử mà quên rằng đạo hàm của nó sinh thêm các thành phần cùng họ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 1000)
y_res = 0.5 * t * np.sin(t)
y_nonres = 0.75 * np.cos(2*t)

plt.plot(t, y_res, label="Cộng hưởng: y_p ~ t sin(t)")
plt.plot(t, y_nonres, label="Không cộng hưởng: y_p ~ cos(2t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("So sánh nghiệm riêng khi có và không có cộng hưởng")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cộng hưởng cho thấy biên độ tăng theo thời gian thay vì giữ bị chặn như trường hợp không cộng hưởng.

### 4. Gợi ý tìm thêm mô phỏng

- search: undetermined coefficients resonance animation
- search: forced oscillator particular solution visualization
- search: resonance t sin t explanation

### 5. Bài toán mẫu có bối cảnh thực

Xét hệ dao động
$$ y''+y=\cos t. $$
Phần thuần nhất có nghiệm
$$ y_h=c_1\cos t+c_2\sin t. $$
Nếu thử trực tiếp $$ A\cos t+B\sin t $$ thì sẽ trùng với nghiệm thuần nhất. Vì vậy phải nhân thêm $$ t $$ và đặt
$$ y_p=t\left(A\cos t+B\sin t\right). $$
Tính ra một nghiệm riêng là
$$ y_p=\frac{1}{2}t\sin t. $$
Do đó
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Hệ số $$ t $$ là dấu hiệu rất quan trọng: lực kích đúng tần số riêng làm hệ hút năng lượng tích lũy.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo bảng chọn ansatz, kiểm tra cộng hưởng, và tính hệ số.

**Bậc sau đại học.** Giải thích phương pháp bằng ngôn ngữ không gian bất biến dưới phép đạo hàm và liên hệ với toán tử annihilator.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: rất mạnh ở phương pháp hệ số bất định và cộng hưởng.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài luyện chọn ansatz.
- Ross — *Differential Equations*: trình bày gọn, tốt cho việc ôn bảng dạng forcing.
