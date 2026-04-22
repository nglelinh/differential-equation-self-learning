---
layout: post
title: "03-06 Hàm Xung và Phân phối Delta"
chapter: '03'
order: 6
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu Dirac delta như mô hình lý tưởng của một xung tác động tức thời, biết Laplace của delta, và diễn giải mối liên hệ giữa xung lực, bước nhảy của đạo hàm và đáp ứng của hệ tuyến tính. Đây là bài học chuyển mạnh từ tín hiệu gián đoạn sang tín hiệu tập trung tại một thời điểm.

## Kiến thức nền
Sinh viên cần nắm Heaviside, Laplace cơ bản và trực giác về tín hiệu có diện tích hoặc tác động hữu hạn. Một chút nền tảng vật lý về xung lực trong cơ học sẽ giúp bài học trở nên rất tự nhiên.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-06 Hàm Xung và Phân phối Delta]({{ site.imgurl }}/chapter_img/chapter03/03_06_impulse_functions.svg)

Một cú gõ búa lên vật, một xung điện cực ngắn, một cú hích tức thời vào hệ dao động: tất cả đều có thời lượng rất nhỏ nhưng vẫn truyền một lượng tác động hữu hạn. Nếu cố mô hình hóa những sự kiện đó bằng các hàm thông thường, ta phải làm việc với các xung ngày càng hẹp và cao hơn. Dirac delta xuất hiện như cách lý tưởng hóa hoàn hảo cho kiểu forcing ấy.

Bài học này rất quan trọng vì nó mở ra ngôn ngữ của đáp ứng xung. Trong lý thuyết hệ thống, nếu biết hệ phản ứng thế nào với một delta, ta gần như biết toàn bộ hệ. Vì vậy delta không chỉ là một vật thể lạ của giải tích; nó là hòn đá góc của phân tích hệ tuyến tính.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Dirac delta có thể được xem như một cú đánh "vô cùng ngắn nhưng hữu hạn tổng tác động". Nó không phải là một hàm bình thường với giá trị hữu hạn tại mọi điểm, mà là một phân phối tập trung toàn bộ khối lượng tại đúng một thời điểm.

### Cách nhìn hình ảnh
Ta hình dung một dãy xung ngày càng hẹp, ngày càng cao, nhưng luôn có diện tích bằng 1. Khi chiều rộng tiến về 0, dãy ấy tiến đến delta. Hình ảnh quan trọng không phải là chiều cao, mà là diện tích: đó là tổng tác động của xung.

### Cách nhìn hình thức
Dirac delta tại $$ t=a $$ được ký hiệu $$ \delta(t-a) $$ và thỏa tính chất sàng:
$$ \int_{-\infty}^{\infty} f(t)\delta(t-a)\,dt=f(a) $$
với giả thiết phù hợp. Trong Laplace, ta có
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
Đây là công thức cực đẹp vì nó cho thấy delta là "người anh em vi phân" của Heaviside theo nghĩa trực giác.

## Những ngộ nhận thường gặp
- "Delta là hàm nhận giá trị vô hạn tại một điểm và 0 ở nơi khác." Cách nói này chỉ mang tính trực giác, không phải định nghĩa chuẩn.
- "Delta không thực tế vì không tồn tại vật lý." Sai. Nó là mô hình lý tưởng rất hữu ích cho các xung rất ngắn.
- "Laplace của delta phức tạp vì bản thân delta lạ." Thực ra công thức Laplace của delta lại rất đơn giản.
- "Xung chỉ làm nghiệm nhảy." Cần cẩn thận: thường nghiệm vị trí liên tục, nhưng đạo hàm có thể nhảy.

## Tiến trình học tập đề xuất
### Bước 1: Hiểu delta như giới hạn của xung hẹp
Đây là điểm khởi động trực giác tốt nhất.

### Bước 2: Nắm tính chất sàng
Đây là công thức làm việc trung tâm.

### Bước 3: Học Laplace của delta
Liên hệ với Heaviside và độ trễ thời gian.

### Bước 4: Diễn giải bước nhảy của hệ
Kết nối trực tiếp với cơ học và hệ tuyến tính.

### Các checkpoint
- Sinh viên có phân biệt được "giá trị điểm" với "tác động tích phân" của delta hay không.
- Sinh viên có nhớ được
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as} $$
và hiểu lý do hay không.
- Sinh viên có diễn giải được xung làm thay đổi đại lượng nào trong hệ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Laplace của delta
Tính
$$ \mathcal{L}\{\delta(t-a)\}. $$
Theo định nghĩa Laplace:
$$
\mathcal{L}\{\delta(t-a)\}=\int_0^\infty e^{-st}\delta(t-a)\,dt.
$$
Áp dụng tính chất sàng:
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
Ví dụ này cho thấy delta chuyển thành một hệ số trễ rất gọn trong miền $$ s $$.

### Ví dụ 2: Bài toán dao động với xung
Giải
$$ y''+y=\delta(t-\pi),\qquad y(0)=0,\qquad y'(0)=0. $$
Áp Laplace:
$$ \left(s^2Y\right)+Y=e^{-\pi s}. $$
Suy ra
$$ Y=\frac{e^{-\pi s}}{s^2+1}. $$
Vì
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t,
$$
nên theo định lý dịch:
$$ y(t)=u(t-\pi)\sin (t-\pi). $$
Nghiệm cho thấy hệ đứng yên tới đúng thời điểm nhận xung, rồi bắt đầu dao động như một phản ứng tự do được kích hoạt tức thời.

### Ví dụ 3: Bước nhảy của đạo hàm
Với phương trình
$$ y''=\delta(t-a), $$
ta tích phân hai vế qua một lân cận rất nhỏ quanh $$ a $$:
$$
\int_{a^-}^{a^+} y''(t)\,dt=\int_{a^-}^{a^+}\delta(t-a)\,dt=1.
$$
Do đó
$$ y'(a^+)-y'(a^-)=1. $$
Điều này cho thấy xung tạo ra bước nhảy trong vận tốc, rất đúng với trực giác cơ học về xung lực.

### Ví dụ 4: Delta như đạo hàm của Heaviside
Ở mức trực giác, ta có thể xem
$$ \frac{d}{dt}u(t-a)=\delta(t-a). $$
Điều này giúp sinh viên kết nối bài Heaviside với bài delta: bước và xung không rời nhau, mà là hai cấp độ mô tả thay đổi đột ngột.

## Câu hỏi khái niệm
1. Vì sao diện tích của xung quan trọng hơn chiều cao cực đại trong trực giác về delta?
2. Vì sao xung thường làm đạo hàm nhảy chứ không nhất thiết làm chính nghiệm nhảy?
3. Trong lý thuyết hệ thống, vì sao biết đáp ứng với delta lại quan trọng đặc biệt?

## Bài toán ứng dụng
1. Một vật chịu một cú va chạm tức thời. Hãy giải thích vì sao vận tốc thay đổi đột ngột còn vị trí thường vẫn liên tục.
2. Một mạch điện nhận một xung điện rất ngắn. Hãy thảo luận vì sao mô hình delta là hợp lý.
3. Trong xử lý tín hiệu, vì sao một hệ tuyến tính thường được đặc trưng bởi đáp ứng xung?

## Chiến lược giảng dạy tương tác
- Dùng hình ảnh một chuỗi xung ngày càng hẹp nhưng cùng diện tích để xây trực giác trước khi viết ký hiệu delta.
- Hỏi lớp: "Một cú gõ búa làm thay đổi vị trí hay vận tốc ngay lập tức?"
- Cho sinh viên so sánh Heaviside và delta như hai dạng tín hiệu "bật" và "đập".
- Yêu cầu sinh viên giải thích bằng lời ý nghĩa của nghiệm
$$ u(t-\pi)\sin(t-\pi). $$

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên giữ bài học ở mức trực giác sàng và Laplace, tránh quá tải bằng ngôn ngữ phân phối trừu tượng. Khi sinh viên thấy ứng dụng cơ học rõ ràng, các em thường chấp nhận delta dễ hơn.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi liên hệ delta với đạo hàm yếu của Heaviside, hoặc dựng đáp ứng xung của một hệ cấp hai rồi so sánh với đáp ứng bước.

## Tóm tắt dễ nhớ
Dirac delta mô hình hóa một xung rất ngắn nhưng có tác động hữu hạn. Trong Laplace,
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
Xung thường làm đạo hàm của nghiệm nhảy. Nếu Heaviside là công tắc, thì delta là cú đánh tức thời.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Búa gõ vào hệ dao động
- Bài toán: Một cú gõ cực ngắn nhưng truyền xung lượng hữu hạn cho hệ.
- Mô hình:
$$ y''+\omega^2 y=\delta(t-a). $$
- Giả thiết và giới hạn: Xung được lý tưởng hóa là tức thời; lực thật luôn có độ rộng nhỏ nhưng hữu hạn.
- Diễn giải: Hệ đứng yên trước xung, rồi bắt đầu phản ứng ngay sau đó như một dao động tự do được kích hoạt.

#### Xung điện trong mạch
- Bài toán: Một mạch nhận một pulse rất ngắn có thể được xem là xung delta.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=\delta(t-a). $$
- Giả thiết và giới hạn: Xung đủ ngắn để bỏ qua cấu trúc chi tiết của nó.
- Diễn giải: Delta giúp nối cơ học, điện tử và lý thuyết hệ dưới cùng một ngôn ngữ.

#### Điều khiển kích xung
- Bài toán: Hệ được điều chỉnh bằng các cú hiệu chỉnh ngắn và mạnh.
- Mô hình:
$$ \delta(t-a) $$
hoặc tổng các delta ở nhiều thời điểm.
- Giả thiết và giới hạn: Đây là mô hình lý tưởng cho điều khiển xung hoặc lấy mẫu cực ngắn.
- Diễn giải: Đáp ứng xung gần như xác định toàn bộ hệ tuyến tính.

### 2. Trực giác bổ sung và các kết nối

Delta là bước tiến tự nhiên sau Heaviside: nếu Heaviside là bật công tắc, thì delta là cú gõ tức thời. Trong phân tích hiện đại, delta không phải hàm thông thường mà là phân phối. Tuy nhiên, ở mức khóa học này, trực giác về diện tích hữu hạn và tác động tích phân là đủ mạnh để làm việc hiệu quả.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 800)
eps_values = [0.25, 0.12, 0.06]

for eps in eps_values:
    pulse = np.exp(-(t / eps)**2) / (eps * np.sqrt(np.pi))
    plt.plot(t, pulse, label=f"eps={eps}")

plt.xlabel("t")
plt.ylabel("Pulse height")
plt.title("Các xung hẹp xấp xỉ delta")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Dirac delta intuition narrow pulse
- search: impulse response oscillator animation
- search: delta function Laplace transform visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$ y''+y=\delta(t-\pi),\qquad y(0)=0,\qquad y'(0)=0. $$
Áp Laplace:
$$
(s^2+1)Y=e^{-\pi s},
\qquad
Y=\frac{e^{-\pi s}}{s^2+1}.
$$
Vì
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t,
$$
nên
$$ y(t)=u(t-\pi)\sin(t-\pi). $$
Nghiệm thể hiện đúng trực giác vật lý: hệ không chuyển động trước thời điểm nhận xung, rồi bắt đầu dao động ngay sau đó.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm tính chất sàng, Laplace của delta và ý nghĩa bước nhảy của đạo hàm.

**Bậc sau đại học.** Liên hệ delta với đạo hàm yếu của Heaviside và với đáp ứng xung trong lý thuyết hệ thống.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giải thích delta theo tinh thần ứng dụng rất phù hợp.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ tốt về impulse response.
- Ross — *Differential Equations*: ngắn gọn nhưng rất hiệu quả cho trực giác cơ học của xung.
