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
Bài học này giúp sinh viên hiểu hàm delta Dirac như mô hình lý tưởng của một xung tác động tức thời, nắm công thức biến đổi Laplace của delta, và diễn giải mối liên hệ giữa xung lực, bước nhảy của đạo hàm và đáp ứng xung của hệ tuyến tính.

## Kiến thức nền
Sinh viên cần nắm hàm bước Heaviside, biến đổi Laplace cơ bản và trực giác về tín hiệu có tổng tác động (diện tích dưới đường cong) hữu hạn. Kiến thức cơ học cơ bản về xung lượng sẽ giúp bài học dễ hình dung hơn.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-06 Hàm Xung và Phân phối Delta]({{ site.imgurl }}/chapter_img/chapter03/03_06_impulse_functions.svg)

Một cú gõ búa, một xung điện cực ngắn hay một cú va chạm tức thời đều diễn ra trong khoảng thời gian rất ngắn nhưng truyền một tổng tác động hữu hạn. Nếu mô tả bằng các hàm thông thường, ta phải xét dãy xung ngày càng hẹp và cao. Hàm delta Dirac cung cấp một mô hình lý tưởng hóa gọn gàng cho loại tác động này.

Bài học đồng thời mở ra khái niệm đáp ứng xung: trong lý thuyết hệ tuyến tính, khi biết đáp ứng của hệ trước một xung đơn vị delta, ta có thể xác định đáp ứng của hệ trước mọi đầu vào tổng quát.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Delta Dirac đại diện cho một tác động diễn ra trong thời gian vô cùng ngắn nhưng có tổng xung lượng bằng 1. Đây không phải hàm số thông thường có giá trị hữu hạn tại mọi điểm, mà là một phân bố (hàm suy rộng) tập trung toàn bộ trọng số tại một thời điểm duy nhất.

### Cách nhìn hình ảnh
Có thể hình dung một dãy xung có độ rộng tiến về 0 và chiều cao tăng lên tương ứng sao cho diện tích dưới mỗi xung luôn bằng 1. Đại lượng mang ý nghĩa vật lý không phải chiều cao cực đại mà là diện tích bằng 1 — tổng tác động của xung.

### Cách nhìn hình thức
Delta Dirac tại $$ t=a $$ được ký hiệu là $$ \delta(t-a) $$ và thỏa mãn tính chất sàng (lấy mẫu):
$$ \int_{-\infty}^{\infty} f(t)\delta(t-a)\,dt=f(a) $$
với mọi hàm $$ f $$ liên tục tại $$ a $$. Trong biến đổi Laplace (với $$ a\ge 0 $$), ta có
$$ \mathcal{L}\{\delta(t-a)\}=e^{-as}. $$
Về mặt trực giác và đạo hàm suy rộng, delta là đạo hàm của hàm bước Heaviside.

## Những ngộ nhận thường gặp
- "Delta là hàm bằng vô cực tại một điểm và bằng 0 ở mọi nơi khác." Đây chỉ là hình ảnh trực giác, không phải định nghĩa toán học chặt chẽ.
- "Delta không có ý nghĩa thực tế vì không tồn tại xung vô hạn ngắn." Sai: đây là phép xấp xỉ rất hiệu quả khi thời lượng xung nhỏ hơn nhiều so với thang thời gian của hệ.
- "Biến đổi Laplace của delta rất phức tạp." Thực tế công thức Laplace của delta lại đơn giản bậc nhất trong bảng.
- "Xung lực luôn làm nghiệm vị trí nhảy bậc." Cần chú ý: trong phương trình cấp hai, nghiệm vị trí thường vẫn liên tục, còn đạo hàm bậc nhất (vận tốc) mới xuất hiện bước nhảy.

## Tiến trình học tập đề xuất
### Bước 1: Hình dung delta như giới hạn của dãy xung hẹp
Tạo trực giác về diện tích không đổi bằng 1.

### Bước 2: Nắm tính chất sàng
Sử dụng trực tiếp trong tích phân và biến đổi Laplace.

### Bước 3: Áp dụng công thức Laplace của delta
Liên hệ với nhân tử trễ $$ e^{-as} $$ của hàm bước Heaviside.

### Bước 4: Diễn giải bước nhảy của đạo hàm
Kết nối trực tiếp với xung lượng và biến thiên vận tốc trong cơ học.

### Các checkpoint
- Sinh viên có phân biệt được "giá trị tại một điểm" với "tác động tích phân" của delta hay không.
- Sinh viên có nhớ công thức $$ \mathcal{L}\{\delta(t-a)\}=e^{-as} $$ và giải thích được nguồn gốc của nó hay không.
- Sinh viên có xác định đúng đại lượng nào của hệ bị nhảy bậc khi chịu tác động xung hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Biến đổi Laplace của delta
Tính $$ \mathcal{L}\{\delta(t-a)\} $$ với $$ a\ge 0 $$. Theo định nghĩa và tính chất sàng:
$$
\mathcal{L}\{\delta(t-a)\}=\int_0^\infty e^{-st}\delta(t-a)\,dt=e^{-as}.
$$
Xung tại thời điểm $$ a $$ chuyển thành nhân tử trễ $$ e^{-as} $$ trong miền $$ s $$.

### Ví dụ 2: Hệ dao động chịu xung lực
Giải bài toán $$ y''+y=\delta(t-\pi) $$ với $$ y(0)=0 $$, $$ y'(0)=0 $$. Lấy biến đổi Laplace hai vế:
$$ s^2Y+Y=e^{-\pi s} \Rightarrow Y=\frac{e^{-\pi s}}{s^2+1}. $$
Vì $$ \mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t $$, theo định lý dịch thời gian ta được
$$ y(t)=u(t-\pi)\sin (t-\pi). $$
Hệ đứng yên cho đến đúng thời điểm $$ t=\pi $$, rồi bắt đầu dao động tự do ngay sau khi nhận xung.

### Ví dụ 3: Bước nhảy của đạo hàm bậc nhất
Với phương trình $$ y''=\delta(t-a) $$, tích phân hai vế trên một lân cận rất nhỏ quanh $$ a $$:
$$
\int_{a^-}^{a^+} y''(t)\,dt=\int_{a^-}^{a^+}\delta(t-a)\,dt=1 \Rightarrow y'(a^+)-y'(a^-)=1.
$$
Xung lực đơn vị tạo ra bước nhảy bằng 1 trong vận tốc $$ y' $$, phù hợp trực tiếp với định lý xung lượng trong cơ học.

### Ví dụ 4: Liên hệ giữa delta và Heaviside
Theo nghĩa đạo hàm suy rộng, ta viết
$$ \frac{d}{dt}u(t-a)=\delta(t-a). $$
Quan hệ này kết nối hai bài học: hàm bước mô tả sự thay đổi trạng thái kiểu công tắc, còn hàm delta mô tả tác động xung tức thời.

## Câu hỏi khái niệm
1. Vì sao diện tích dưới xung quan trọng hơn chiều cao cực đại khi hình dung delta Dirac?
2. Vì sao trong hệ cấp hai, xung lực thường làm nhảy vận tốc chứ không làm nhảy vị trí?
3. Trong lý thuyết hệ thống, vì sao đáp ứng xung lại giữ vai trò đặc trưng cho toàn bộ hệ tuyến tính?

## Bài toán ứng dụng
1. Một vật chịu va chạm tức thời. Hãy giải thích vì sao vận tốc thay đổi đột ngột trong khi vị trí vẫn liên tục.
2. Một mạch điện nhận xung điện áp rất ngắn. Khi nào mô hình hóa bằng hàm delta là hợp lý?
3. Trong xử lý tín hiệu, vì sao hệ tuyến tính bất biến theo thời gian thường được đặc trưng bởi đáp ứng xung?

## Chiến lược giảng dạy tương tác
- Vẽ dãy xung ngày càng hẹp nhưng cùng diện tích bằng 1 trước khi đưa ký hiệu $$ \delta $$.
- Hỏi lớp: "Một cú gõ búa tức thời làm thay đổi ngay vị trí hay vận tốc của vật?"
- Đặt hàm Heaviside và hàm delta cạnh nhau như hai mô hình cơ bản: "bật công tắc" và "tác động tức thời".
- Yêu cầu sinh viên diễn giải bằng lời nghiệm $$ u(t-\pi)\sin(t-\pi) $$.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Giữ trọng tâm ở tính chất sàng, công thức Laplace và trực giác xung lượng cơ học; tránh đi quá sâu vào lý thuyết phân bố trừu tượng ở bước đầu.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên liên hệ delta với đạo hàm yếu của hàm Heaviside, hoặc tính cả đáp ứng xung lẫn đáp ứng bước của một hệ cấp hai rồi so sánh quan hệ đạo hàm giữa chúng.

## Tóm tắt dễ nhớ
Delta Dirac mô hình hóa một xung rất ngắn có tổng tác động bằng 1, với biến đổi Laplace $$ \mathcal{L}\{\delta(t-a)\}=e^{-as} $$ ($$ a\ge 0 $$). Trong phương trình cấp hai, xung làm đạo hàm bậc nhất xuất hiện bước nhảy. Nếu Heaviside là công tắc bật/tắt, thì delta là cú tác động tức thời.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cú gõ búa vào hệ dao động
- Bài toán: Tác động cơ học rất ngắn nhưng truyền một xung lượng hữu hạn cho hệ.
- Mô hình:
$$ y''+\omega^2 y=\delta(t-a). $$
- Giả thiết và giới hạn: Lý tưởng hóa xung là tức thời; lực thực tế luôn có độ rộng nhỏ nhưng hữu hạn.
- Diễn giải: Hệ đứng yên trước thời điểm $$ a $$, rồi dao động tự do ngay sau khi nhận xung.

#### Xung điện ngắn trong mạch RLC
- Bài toán: Mạch điện nhận một xung điện áp rất ngắn có thể xấp xỉ bằng delta.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=\delta(t-a). $$
- Giả thiết và giới hạn: Độ rộng xung nhỏ hơn rất nhiều so với hằng số thời gian của mạch.
- Diễn giải: Hàm delta thống nhất cách phân tích xung trong cơ học, điện tử và lý thuyết hệ thống.

#### Điều khiển bằng xung hiệu chỉnh
- Bài toán: Hệ được điều chỉnh bằng các tác động ngắn và mạnh tại những thời điểm rời rạc.
- Mô hình: $$ \delta(t-a) $$ hoặc tổng các xung delta tại nhiều thời điểm.
- Giả thiết và giới hạn: Là mô hình lý tưởng hóa cho điều khiển xung hoặc lấy mẫu tức thời.
- Diễn giải: Đáp ứng xung cung cấp thông tin đặc trưng để dự đoán đáp ứng của hệ tuyến tính.

### 2. Trực giác bổ sung và các kết nối

Delta là bước nối tiếp tự nhiên sau hàm bước Heaviside. Trong giải tích hiện đại, delta được định nghĩa chặt chẽ trong lý thuyết phân bố; ở phạm vi khóa học này, trực giác về diện tích bằng 1 và tính chất sàng là đủ để áp dụng chính xác.

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

Xét lại bài toán $$ y''+y=\delta(t-\pi) $$, $$ y(0)=0 $$, $$ y'(0)=0 $$. Áp dụng biến đổi Laplace:
$$
(s^2+1)Y=e^{-\pi s},\qquad Y=\frac{e^{-\pi s}}{s^2+1}.
$$
Vì $$ \mathcal{L}^{-1}\left\{\frac{1}{s^2+1}\right\}=\sin t $$, ta thu được $$ y(t)=u(t-\pi)\sin(t-\pi) $$. Nghiệm phản ánh đúng trực giác vật lý: vật đứng yên trước khi nhận xung và bắt đầu dao động điều hòa ngay sau thời điểm $$ t=\pi $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm tính chất sàng, công thức Laplace của delta và bước nhảy của đạo hàm.

**Bậc sau đại học.** Liên hệ delta với đạo hàm yếu của Heaviside và vai trò của đáp ứng xung trong lý thuyết hệ LTI.

## Video tham khảo

- Xem trước: [Step and Delta Functions | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=q0PxCQWG3ic) — MIT OpenCourseWare, tiếng Anh. Giới thiệu xung delta như đạo hàm suy rộng của hàm bước cùng biến đổi Laplace tương ứng.
- [Unit Step and Impulse Response | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=LjqUV6vqwkg) — MIT OpenCourseWare, tiếng Anh. So sánh trực tiếp đáp ứng xung và đáp ứng bước.
- [Dirac Delta: Not a Function but a Distribution](https://www.youtube.com/watch?v=XZKf1G5ATkM) — Scintropy, tiếng Anh. Giải thích bản chất phân bố (hàm suy rộng) của delta Dirac.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày delta theo hướng ứng dụng rõ ràng.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập tốt về đáp ứng xung.
- Ross — *Differential Equations*: ngắn gọn, giúp nắm nhanh trực giác cơ học của xung lực.
