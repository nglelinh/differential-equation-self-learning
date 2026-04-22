---
layout: post
title: "02-06 Biến thiên Hằng số"
chapter: '02'
order: 6
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu phương pháp biến thiên hằng số như một công cụ tổng quát để tìm nghiệm riêng cho phương trình không thuần nhất, đặc biệt khi vế phải không phù hợp với hệ số bất định. Sinh viên sẽ học cách thay hằng số bằng hàm, thiết lập hệ phương trình cho các hàm đó, và diễn giải vai trò của Wronskian trong toàn bộ quy trình.

## Kiến thức nền
Sinh viên nên nắm nghiệm thuần nhất của phương trình tuyến tính cấp hai, nguyên lý chồng chập, kỹ thuật hạ bậc và kỹ năng giải hệ hai phương trình tuyến tính. Một mức quen thuộc với Wronskian sẽ rất hữu ích, nhưng bài học này cũng có thể dùng như nơi tạo động lực để thấy vì sao Wronskian quan trọng.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-06 Biến thiên Hằng số]({{ site.imgurl }}/chapter_img/chapter02/02_06_variation_of_parameters.svg)

Phương pháp hệ số bất định rất đẹp nhưng có phạm vi áp dụng giới hạn. Nếu forcing là $$ \ln t $$, $$ \tan t $$ hay một hàm không thuộc họ đóng dưới đạo hàm, ta cần một công cụ tổng quát hơn. Biến thiên hằng số là câu trả lời. Ý tưởng của nó rất thanh lịch: nghiệm thuần nhất đã có dạng
$$ c_1y_1+c_2y_2. $$
Vậy khi có ngoại lực, thay vì giữ $$ c_1,c_2 $$ là hằng, ta cho chúng được phép biến thiên theo thời gian.

Đây là một trong những bài mà sinh viên dễ cảm thấy phương pháp "tự nhiên" khi hiểu đúng. Ta không hề đoán mò nghiệm riêng từ bên ngoài; ta dùng chính cơ sở nghiệm của hệ thuần nhất để dựng phản ứng cưỡng bức. Vì vậy, biến thiên hằng số không chỉ là một kỹ thuật. Nó là sự tiếp tục hợp lý của nguyên lý chồng chập.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy tưởng tượng nghiệm thuần nhất cung cấp hai mode chuyển động cơ bản của hệ. Khi không có ngoại lực, trọng số của hai mode này là hằng số. Khi có ngoại lực, hệ vẫn chuyển động trong cùng không gian hai chiều ấy, nhưng trọng số của các mode được "lái" theo thời gian. Các trọng số mới chính là các hàm $$ u_1(t) $$ và $$ u_2(t) $$.

### Cách nhìn hình ảnh
Nếu nghiệm thuần nhất tạo nên một họ quỹ đạo cơ sở, nghiệm không thuần nhất có thể được xem là một quỹ đạo liên tục đổi cách pha trộn giữa hai hướng cơ sở ấy để thích nghi với forcing. Hình ảnh này giúp sinh viên tránh cảm giác công thức là điều gì xa lạ.

### Cách nhìn hình thức
Xét phương trình đã chuẩn hóa:
$$ y''+p(t)y'+q(t)y=g(t). $$
Giả sử $$ y_1,y_2 $$ là hai nghiệm độc lập của phương trình thuần nhất. Ta tìm nghiệm riêng dưới dạng
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
Để đơn giản hóa đạo hàm, ta áp thêm điều kiện phụ
$$ u_1'y_1+u_2'y_2=0. $$
Khi đó ta có hệ
$$ u_1'y_1+u_2'y_2=0, $$
$$ u_1'y_1'+u_2'y_2'=g(t). $$
Giải hệ này cho $$ u_1',u_2' $$ sẽ dẫn đến công thức có Wronskian.

## Những ngộ nhận thường gặp
- "Biến thiên hằng số chỉ là hệ số bất định viết phức tạp hơn." Sai. Đây là phương pháp tổng quát hơn nhiều.
- "Hai hàm $$ u_1,u_2 $$ được chọn tùy ý." Sai. Chúng bị ràng buộc bởi hệ phương trình sinh ra từ việc thế vào ODE.
- "Điều kiện phụ
$$ u_1'y_1+u_2'y_2=0 $$
là mẹo không có lý do." Sai. Nó được chọn để giảm bậc và làm phép tính khả thi.
- "Nếu tích phân xấu thì phương pháp không đúng." Không đúng. Phương pháp vẫn đúng dù kết quả không đẹp.

## Tiến trình học tập đề xuất
### Bước 1: Giải bài toán thuần nhất
Tìm $$ y_1,y_2 $$ trước. Không có bước này thì không thể làm tiếp.

### Bước 2: Đặt nghiệm riêng dạng biến thiên hằng số
Viết
$$ y_p=u_1y_1+u_2y_2. $$

### Bước 3: Áp điều kiện phụ
Đây là bước chiến lược để tránh đạo hàm bậc hai của $$ u_1,u_2 $$.

### Bước 4: Giải hệ cho $$ u_1',u_2' $$
Thường dùng Wronskian.

### Bước 5: Tích phân và dựng $$ y_p $$
Sau đó ghép với $$ y_h $$ để có nghiệm tổng.

### Các checkpoint
- Sinh viên có nhớ rằng $$ u_1,u_2 $$ là hàm chứ không phải hằng số hay không.
- Sinh viên có lập đúng hệ hai phương trình cho $$ u_1',u_2' $$ hay không.
- Sinh viên có hiểu vì sao Wronskian phải khác 0 hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Một forcing không tiện cho hệ số bất định
Giải
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
Nghiệm thuần nhất là
$$ y_h=c_1\cos t+c_2\sin t. $$
Lấy
$$ y_1=\cos t,\qquad y_2=\sin t. $$
Wronskian là
$$ W=y_1y_2'-y_1'y_2=\cos^2 t+\sin^2 t=1. $$
Theo công thức biến thiên hằng số:
$$
u_1'=-\frac{y_2g}{W}=-\sin t\tan t=-\frac{\sin^2 t}{\cos t},
$$
$$ u_2'=\frac{y_1g}{W}=\cos t\tan t=\sin t. $$
Do đó
$$ u_2=-\cos t. $$
Còn
$$ u_1'=-\frac{1-\cos^2 t}{\cos t}=-\sec t+\cos t, $$
nên
$$ u_1=-\ln \lvert \sec t+\tan t\rvert+\sin t. $$
Vì vậy
$$ y_p=u_1\cos t+u_2\sin t. $$
Ở đây điều quan trọng là thấy phương pháp vẫn hoạt động dù forcing không "đẹp".

### Ví dụ 2: Forcing đa thức nhưng dùng phương pháp tổng quát
Giải
$$ y''+y=t. $$
Nghiệm thuần nhất:
$$ y_h=c_1\cos t+c_2\sin t. $$
Với $$ W=1 $$, ta có
$$ u_1'=-t\sin t,\qquad u_2'=t\cos t. $$
Tích phân từng phần:
$$ u_1=t\cos t-\sin t, $$
$$ u_2=t\sin t+\cos t. $$
Suy ra
$$
y_p=\left(t\cos t-\sin t\right)\cos t+\left(t\sin t+\cos t\right)\sin t=t.
$$
Vậy
$$ y=c_1\cos t+c_2\sin t+t. $$
Ví dụ này cho thấy biến thiên hằng số có thể cho kết quả rất gọn ngay cả khi ta dùng một "dao lớn" cho bài toán đơn giản.

### Ví dụ 3: Vai trò của Wronskian
Nếu $$ W=0 $$, hai nghiệm $$ y_1,y_2 $$ không độc lập tuyến tính, nên hệ để tìm $$ u_1',u_2' $$ suy biến. Điều đó phản ánh đúng trực giác: nếu cơ sở nghiệm thuần nhất chưa đủ hai hướng độc lập, ta không thể biểu diễn mọi phản ứng cưỡng bức bằng nó.

### Ví dụ 4: Khi nào nên dùng biến thiên hằng số
Nếu forcing là đa thức hay mũ đơn giản, hệ số bất định thường nhanh hơn. Nhưng nếu forcing là
$$ \ln t,\qquad \tan t,\qquad \sec t, $$
hay một hàm không thuộc họ đóng dưới đạo hàm, biến thiên hằng số thường là lựa chọn tự nhiên hơn. Đây là kỹ năng ra quyết định phương pháp mà sinh viên cần luyện.

## Câu hỏi khái niệm
1. Vì sao biến thiên hằng số là sự mở rộng tự nhiên của nghiệm thuần nhất?
2. Vai trò thật sự của điều kiện phụ
$$ u_1'y_1+u_2'y_2=0 $$
là gì?
3. Vì sao Wronskian xuất hiện một cách tự nhiên trong phương pháp này?

## Bài toán ứng dụng
1. Một hệ dao động nhận forcing không chuẩn như $$ \ln t $$. Hãy giải thích vì sao hệ số bất định không phù hợp nhưng biến thiên hằng số vẫn dùng được.
2. Một hệ điều khiển tuyến tính có hai mode cơ bản đã biết. Hãy diễn giải vật lý của việc cho các "trọng số mode" biến thiên theo thời gian.
3. Trong mô hình sóng cưỡng bức, vì sao một cơ sở nghiệm độc lập của hệ thuần nhất là điều kiện thiết yếu để dựng đáp ứng đầy đủ?

## Chiến lược giảng dạy tương tác
- Trước khi đưa công thức, hỏi lớp: "Nếu ngoại lực làm thay đổi cách hệ pha trộn hai mode cơ bản, em sẽ sửa dạng nghiệm thuần nhất như thế nào?"
- Cho sinh viên thực hiện riêng từng bước: một nhóm tìm $$ y_h $$, một nhóm lập hệ cho $$ u_1',u_2' $$, một nhóm tính Wronskian.
- So sánh cùng một bài giải bằng hệ số bất định và biến thiên hằng số để thấy rõ sự đánh đổi giữa tính tổng quát và độ gọn.
- Khuyến khích sinh viên nói bằng lời khi nào không nên dùng phương pháp này, dù về nguyên tắc vẫn dùng được.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp cho sinh viên yếu một khung mẫu cố định gồm năm bước nói trên. Các em thường bối rối không phải vì tích phân, mà vì mất cấu trúc giữa quá nhiều ký hiệu.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi suy ra công thức Cramer cho $$ u_1',u_2' $$ trực tiếp từ hệ hai phương trình, hoặc so sánh biến thiên hằng số với phương pháp Green trong bài toán tuyến tính.

## Tóm tắt dễ nhớ
Biến thiên hằng số là cách cho các hằng số trong nghiệm thuần nhất trở thành hàm thời gian để hấp thụ forcing. Phương pháp này tổng quát, mạnh, và dựa trực tiếp trên cơ sở nghiệm của hệ thuần nhất. Hãy nhớ: tìm $$ y_1,y_2 $$ trước, lập hệ cho $$ u_1',u_2' $$ sau.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Forcing không chuẩn trong cơ học
- Bài toán: Hệ dao động bị kích bởi tín hiệu như $$ \tan t $$, $$ \ln t $$, hoặc một hàm được đo thực nghiệm.
- Mô hình:
$$ y''+p(t)y'+q(t)y=g(t). $$
- Giả thiết và giới hạn: Cần biết trước cơ sở nghiệm thuần nhất và Wronskian không bằng 0.
- Diễn giải: Biến thiên hằng số tổng quát hơn hệ số bất định vì không cần forcing thuộc họ đóng dưới đạo hàm.

#### Điều khiển tuyến tính với hai mode cơ bản
- Bài toán: Hệ có hai mode riêng và ngoại lực làm hệ thay đổi cách trộn hai mode đó theo thời gian.
- Mô hình:
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
- Giả thiết và giới hạn: Phương pháp vẫn có thể cho tích phân khó, nhưng về nguyên lý luôn áp dụng cho phương trình tuyến tính cấp hai.
- Diễn giải: Các "hằng số" của nghiệm thuần nhất trở thành trọng số phụ thuộc thời gian.

#### Truyền nhiệt hay dao động với nguồn phức tạp
- Bài toán: Một hệ bị kích bởi nguồn không tuần hoàn đơn giản và không thể dùng bảng forcing tiêu chuẩn.
- Mô hình: Vẫn là ODE tuyến tính cấp hai không thuần nhất.
- Giả thiết và giới hạn: Phương pháp đòi hỏi giải tích phân, đôi khi chỉ đánh giá số được.
- Diễn giải: Đây là nơi sinh viên thấy tính tổng quát thường đi kèm giá thành tính toán cao hơn.

### 2. Trực giác bổ sung và các kết nối

Biến thiên hằng số là phiên bản tinh tế của ý tưởng chồng chập. Khi không có forcing, các trọng số của hai mode là hằng số; khi có forcing, các trọng số ấy bị "lái" bởi nguồn ngoài. Bài học này rất gần với công thức Duhamel, Green function, và cả phương pháp nghiệm cơ bản cho PDE sau này. Một sai lầm thường gặp là xem điều kiện phụ
$$ u_1'y_1+u_2'y_2=0 $$
là tùy tiện; thực ra nó là lựa chọn chiến lược để tránh xuất hiện đạo hàm bậc hai của $$ u_1,u_2 $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t = np.linspace(0.05, 1.2, 400)
g = np.tan(t)
y1 = np.cos(t)
y2 = np.sin(t)
u1p = -y2 * g
u2p = y1 * g
u1 = np.concatenate(([0], cumulative_trapezoid(u1p, t)))
u2 = np.concatenate(([0], cumulative_trapezoid(u2p, t)))
yp = u1 * y1 + u2 * y2

plt.plot(t, yp, label="y_p from variation of parameters")
plt.xlabel("t")
plt.ylabel("y_p(t)")
plt.title("Nghiệm riêng cho y'' + y = tan(t)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Hình này cho sinh viên cảm giác rất trực tiếp rằng nghiệm riêng thực sự được dựng từ việc trộn hai mode cơ bản với trọng số thay đổi theo thời gian.

### 4. Gợi ý tìm thêm mô phỏng

- search: variation of parameters visualization
- search: Wronskian Cramer rule animation
- search: Green function second order ODE intuition

### 5. Bài toán mẫu có bối cảnh thực

Giải
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
Nghiệm thuần nhất:
$$ y_h=c_1\cos t+c_2\sin t. $$
Lấy
$$ y_1=\cos t,\qquad y_2=\sin t,\qquad W=1. $$
Khi đó
$$
u_1'=-y_2g=-\sin t\tan t,\qquad u_2'=y_1g=\cos t\tan t=\sin t.
$$
Từ đây
$$ u_2=-\cos t $$
và $$ u_1 $$ nhận được qua tích phân. Dù tích phân của $$ u_1 $$ không đẹp bằng bài forcing chuẩn, phương pháp vẫn hoàn toàn nhất quán và cho nghiệm riêng đúng.

### 6. Phân tầng độ khó

**Bậc đại học.** Học quy trình 5 bước rõ ràng và biết khi nào nên dùng biến thiên hằng số thay cho hệ số bất định.

**Bậc sau đại học.** Kết nối với công thức Cramer, Green function, và biểu diễn tích phân của toán tử nghịch đảo.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rất rõ công thức và động lực của phương pháp.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài forcing không chuẩn để luyện biến thiên hằng số.
- Ross — *Differential Equations*: hữu ích để ôn ý tưởng tổng quát khi so với hệ số bất định.
