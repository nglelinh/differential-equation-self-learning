---
layout: post
title: "Phương Pháp Runge-Kutta"
chapter: '13'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Trực giác của Runge-Kutta bậc bốn]({{ site.imgurl }}/chapter_img/chapter13/02_runge_kutta_methods.svg )

## Mục tiêu

Bài này giới thiệu họ phương pháp Runge-Kutta như sự cải tiến có hệ thống của Euler. Sau bài học, sinh viên cần hiểu ý tưởng lấy nhiều mẫu độ dốc trong một bước, thiết lập được công thức RK4, giải thích được vì sao phương pháp này chính xác hơn Euler, và biết khi nào Runge-Kutta là lựa chọn phù hợp hay chưa phù hợp.

## Kiến thức nền

Sinh viên nên nắm phương pháp Euler, khai triển Taylor, khái niệm bậc chính xác, và bài toán giá trị ban đầu cho ODE. Nên nhớ rằng Euler dùng duy nhất một độ dốc tại đầu bước, còn Runge-Kutta tìm cách mô tả tốt hơn hình dạng cục bộ của nghiệm trong cả bước.

## Dẫn nhập

Nếu Euler giống như lái xe chỉ nhìn hướng tại điểm xuất phát của đoạn đường, thì Runge-Kutta giống như thò đầu quan sát thêm ở giữa đoạn và gần cuối đoạn trước khi quyết định bước đi. Ta không chỉ hỏi “độ dốc bây giờ là gì?” mà hỏi “độ dốc đại diện cho cả bước này nên là gì?”.

Ý tưởng ấy cực kỳ mạnh: chỉ bằng cách lấy vài mẫu thông minh trong một bước, ta có thể tăng độ chính xác rất nhiều mà không cần đạo hàm bậc cao của $$ f $$. Đó là lý do Runge-Kutta trở thành chuẩn thực hành trong rất nhiều bài toán ODE.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng đi bộ qua một con dốc quanh co. Nếu chỉ nhìn độ nghiêng tại điểm đầu, bạn dễ đi lệch. Nếu quan sát thêm giữa đường và gần cuối đoạn, bạn sẽ có ước lượng tốt hơn cho độ nghiêng trung bình của cả quãng. Runge-Kutta làm đúng điều đó với trường hướng của ODE.

### Cách hình ảnh

Giáo viên nên vẽ bốn điểm lấy mẫu trong một bước của RK4: đầu bước, hai điểm giữa bước, và cuối bước. Mỗi điểm cho một độ dốc $$ k_1,k_2,k_3,k_4 $$. Sau đó nhấn mạnh rằng nghiệm mới được tạo bởi trung bình có trọng số của bốn độ dốc ấy, chứ không đơn thuần lấy trung bình cộng.

### Cách hình thức

Với bài toán $$ y'=f(t,y) $$, RK4 được xác định bởi $$ k_1=f(t_n,y_n) $$, $$ k_2=f\!\left(t_n+\frac h2,y_n+\frac h2k_1\right), $$

$$ k_3=f\!\left(t_n+\frac h2,y_n+\frac h2k_2\right), $$ $$ k_4=f(t_n+h,y_n+hk_3) $$, và

$$
y_{n+1}=y_n+\frac h6\left(k_1+2k_2+2k_3+k_4\right).
$$

Phương pháp này có sai số toàn cục bậc bốn trong điều kiện trơn thích hợp.

## Ngộ nhận thường gặp

### “Runge-Kutta chỉ là Euler lặp nhiều lần”

Không đúng. Trọng số và vị trí lấy mẫu được chọn để khớp khai triển Taylor ở bậc cao.

### “Bậc cao hơn luôn tốt hơn”

Không hẳn. Nếu bài toán cứng hoặc mỗi lần tính $$ f $$ rất đắt, bậc cao chưa chắc là lựa chọn tối ưu.

### “RK4 chính xác vì dùng bốn điểm”

Chưa đủ. Điều quan trọng không chỉ là số điểm mà là cách chọn và cách trộn các độ dốc.

### “Một phương pháp chính xác cao thì tự động ổn định”

Sai. Độ chính xác và ổn định là hai câu chuyện khác nhau.

## Tiến trình học

### Bước 1: Nhìn lại Euler

Nhấn mạnh điểm yếu: chỉ lấy một độ dốc.

### Bước 2: Giới thiệu ý tưởng “nhiều slope trong một bước”

Cho sinh viên hiểu Runge-Kutta là cách ước lượng tốt hơn độ dốc trung bình trên khoảng $$ [t_n,t_{n+1}] $$.

### Bước 3: Học RK2 rồi lên RK4

Đi từ phương pháp trung điểm hoặc Heun để RK4 không xuất hiện như một công thức thần bí.

### Bước 4: So sánh chi phí với lợi ích

Một bước RK4 cần bốn lần tính $$ f $$, nhưng thường cho phép dùng bước lớn hơn nhiều so với Euler.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao cần nhiều độ dốc trong một bước không?
- Sinh viên có thiết lập đúng bốn hệ số $$ k_i $$ không?
- Sinh viên có phân biệt được bậc chính xác với số lần tính hàm không?

## Ví dụ có lời giải

### Ví dụ 1: RK2 cho bài toán đơn giản

Xét $$ y'=y,\qquad y(0)=1 $$. Với bước $$ h $$, phương pháp trung điểm cho

$$
k_1=y_n,
\qquad
k_2=y_n+\frac h2k_1=y_n\left(1+\frac h2\right).
$$

Suy ra

$$
y_{n+1}=y_n+hk_2=y_n\left(1+h+\frac{h^2}{2}\right).
$$

Đây đã tốt hơn Euler vì khớp thêm hạng bậc hai của $$ e^h $$.

### Ví dụ 2: Một bước RK4 cho $$ y'=y $$

Với $$ y_n=1 $$:

$$
k_1=1,
\qquad
k_2=1+\frac h2,
\qquad
k_3=1+\frac h2+\frac{h^2}{4},
\qquad
k_4=1+h+\frac{h^2}{2}+\frac{h^3}{4}.
$$

Thay vào công thức RK4 cho xấp xỉ gần với khai triển Taylor của $$ e^h $$ đến bậc bốn. Đây là lý do phương pháp rất chính xác cho bài toán trơn.

### Ví dụ 3: So sánh Euler và RK4

Với bước $$ h=0.5 $$ trên bài toán $$ y'=y $$, Euler sau một bước cho $$ y_1=1.5 $$, trong khi RK4 cho giá trị gần với $$ e^{0.5}\approx 1.6487 $$. Sự khác biệt thể hiện rõ ngay cả khi chỉ đi một bước tương đối lớn.

### Ví dụ 4: Khi RK4 chưa phải lựa chọn tốt

Xét bài toán cứng $$ y'=-1000y $$. Dù RK4 chính xác cao trong bài toán trơn không cứng, nó vẫn có thể bị ép dùng bước rất nhỏ vì ổn định. Ví dụ này nhắc sinh viên rằng bậc cao không giải quyết mọi vấn đề.

## Câu hỏi khái niệm

1. Vì sao Runge-Kutta không cần đạo hàm bậc cao của $$ f $$ mà vẫn đạt bậc chính xác cao?
2. Điều gì làm cho bốn độ dốc trong RK4 “đại diện” tốt cho cả một bước?
3. Khi nào nên ưu tiên phương pháp nhiều bậc hơn, và khi nào nên ưu tiên phương pháp ổn định hơn?

## Bài toán ứng dụng

1. Trong mô phỏng quỹ đạo hành tinh, vì sao một phương pháp như RK4 thường hữu ích hơn Euler?
2. Trong sinh học quần thể, nếu mỗi lần tính $$ f $$ tương đối rẻ, ta đánh đổi thế nào giữa số bước và độ chính xác?
3. Trong điều khiển robot thời gian thực, việc dùng RK4 có thể bị hạn chế bởi chi phí tính toán ra sao?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu Euler chỉ nhìn một điểm, em muốn nhìn thêm ở đâu để cải thiện dự đoán?
- Vì sao điểm giữa bước lại quan trọng?
- Em chọn bốn độ dốc rồi trộn chúng như thế nào để có ý nghĩa hình học?

### Hoạt động gợi ý

- Cho sinh viên tính thủ công RK2 và RK4 trên cùng một bài toán nhỏ.
- Dùng phần mềm so sánh sai số Euler, RK2, RK4 khi thay đổi $$ h $$.
- Chia nhóm: một nhóm bảo vệ Euler vì rẻ, một nhóm bảo vệ RK4 vì chính xác.

### Cách tăng tham gia

- Đi từ phương pháp trung điểm trước khi đưa RK4.
- Cho sinh viên đoán vai trò của các hệ số $$ 1,2,2,1 $$.
- Yêu cầu giải thích RK4 bằng lời không dùng công thức.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm quen bằng RK2 trước.
- Dùng sơ đồ khối chỉ ra luồng tạo $$ k_1,k_2,k_3,k_4 $$.

### Thử thách cho sinh viên khá giỏi

- Suy ra các điều kiện order conditions cơ bản cho RK2 và RK4.
- So sánh miền ổn định của RK4 với Euler tiến trên bài toán $$ y'=\lambda y $$.
- Phân tích khi nào embedded Runge-Kutta phù hợp cho adaptive step size.

## Ghi nhớ nhanh

Runge-Kutta cải tiến Euler bằng cách lấy nhiều mẫu độ dốc trong cùng một bước để ước lượng tốt hơn xu thế trung bình của nghiệm. RK4 đặc biệt phổ biến vì đạt độ chính xác cao cho nhiều bài toán trơn với chi phí vừa phải.

---

## Ứng dụng thực tế

### 1. Quỹ đạo hành tinh và vệ tinh

Trong cơ học thiên thể, hệ ODE thường có dạng

$$
\mathbf{x}'=\mathbf{v},
\qquad
\mathbf{v}'=\mathbf{a}(\mathbf{x}).
$$

RK4 thường cho quỹ đạo ngắn-trung hạn chính xác hơn nhiều so với Euler với cùng số bước. Mô hình giả định ta có thể tính gia tốc nhiều lần trong một bước mà chi phí vẫn chấp nhận được. Giới hạn là với tích phân rất dài hạn hay bài toán bảo toàn cấu trúc Hamilton, có thể cần các phương pháp cấu trúc-preserving khác.

### 2. Động học dịch bệnh và sinh học quần thể

Các mô hình SIR hay logistic mở rộng thường cần tính nhanh nhiều kịch bản tham số. Nếu mỗi lần đánh giá hàm $$ f $$ không quá đắt, RK4 là lựa chọn thực hành tốt vì giảm sai số mạnh với bước vừa phải. Giới hạn là bài toán cứng hoặc nhiều thang thời gian có thể khiến RK4 mất lợi thế ổn định.

### 3. Điều khiển robot và mô phỏng thời gian thực

Trong điều khiển robot, trạng thái hệ thường tuân theo ODE phi tuyến. RK4 cho mô phỏng quỹ đạo chính xác hơn Euler, nhưng bốn lần gọi hàm mỗi bước có thể là chi phí đáng kể trong vòng lặp thời gian thực. Đây là nơi sinh viên thấy rõ đánh đổi giữa độ chính xác và thời gian tính.

## Trực giác sâu hơn

Runge-Kutta là bài học về “thông tin nhiều hơn trong cùng một bước”. Thay vì giảm bước liên tục, ta hỏi liệu có thể hiểu tốt hơn hình dạng cục bộ của nghiệm trong chính bước đó không. Ngộ nhận phổ biến là nghĩ RK4 tốt chỉ vì nó có bốn công thức con; thực ra sức mạnh nằm ở việc các hệ số được chọn để khớp khai triển Taylor đến bậc cao.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

def euler_step(f, t, y, h):
    return y + h * f(t, y)

def rk4_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)
    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6

f = lambda t, y: y
h = 0.5
t = np.arange(0, 2 + h, h)
y_e = [1.0]
y_rk = [1.0]
for n in range(len(t) - 1):
    y_e.append(euler_step(f, t[n], y_e[-1], h))
    y_rk.append(rk4_step(f, t[n], y_rk[-1], h))

t_exact = np.linspace(0, 2, 400)
plt.plot(t_exact, np.exp(t_exact), 'k--', label='Nghiệm đúng')
plt.plot(t, y_e, 'o-', label='Euler')
plt.plot(t, y_rk, 's-', label='RK4')
plt.title('So sánh Euler và RK4 trên y\' = y')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để cho sinh viên bật/tắt các độ dốc $$ k_1,k_2,k_3,k_4 $$ trên cùng một bước và nhìn trực tiếp cách tổ hợp trọng số của chúng tạo ra cập nhật RK4.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `RK4 visualization`, `Runge Kutta slope sampling`, hoặc `adaptive Runge Kutta animation`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ý tưởng “lấy nhiều độ dốc trong một bước” và khả năng cải thiện đáng kể so với Euler trên các bài toán trơn không cứng.

### Mức sau đại học (Graduate)

Đi sâu vào order conditions, tableau Butcher, embedded methods, adaptive step size, và giới hạn ổn định của họ Runge-Kutta trên bài toán cứng.
- Tập trung vào ý tưởng “ước lượng độ dốc trung bình”.

### Thử thách cho sinh viên khá giỏi

- Tìm cách suy ra điều kiện bậc của Runge-Kutta.
- So sánh RK4 với Taylor bậc bốn.
- Tìm hiểu embedded Runge-Kutta và adaptive step size.

## Ghi nhớ nhanh

Runge-Kutta cải tiến Euler bằng cách lấy nhiều mẫu độ dốc trong cùng một bước để ước lượng tốt hơn độ dốc trung bình. RK4 là lựa chọn kinh điển vì cân bằng tốt giữa độ chính xác cao và chi phí tính toán vừa phải.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo tên lửa hoặc robot
- Bài toán: Cần mô phỏng hệ động lực với độ chính xác cao hơn Euler nhưng vẫn tránh giải implicit phức tạp.
- Mô hình: Dùng RK4
$$ y_{n+1}=y_n+\frac{h}{6}(k_1+2k_2+2k_3+k_4) $$
với các slope trung gian.
- Giả thiết và giới hạn: Mỗi bước cần nhiều lần đánh giá hàm hơn; không tự động giải quyết stiffness.
- Diễn giải: Runge-Kutta cải thiện độ chính xác bằng cách "thăm dò" độ dốc ở giữa bước.

#### Mô hình dịch bệnh
- Bài toán: Hệ SIR phi tuyến thường cần mô phỏng số với độ chính xác tốt trong ngắn và trung hạn.
- Mô hình: Áp RK2 hoặc RK4 cho hệ
$$
S'=-\beta SI,\quad I'=\beta SI-\gamma I,\quad R'=\gamma I.
$$
- Giả thiết và giới hạn: Độ chính xác phụ thuộc bước; bảo toàn không âm có thể cần bước nhỏ hoặc lược đồ chuyên biệt.
- Diễn giải: RK methods là lựa chọn mặc định trong nhiều mô phỏng khoa học trước khi đi sâu vào cấu trúc riêng của bài toán.

### 2. Trực giác bổ sung và các kết nối

Nếu Euler nhìn độ dốc tại một điểm, Runge-Kutta nhìn nhiều độ dốc bên trong một bước rồi trộn chúng lại có chủ ý. Ý tưởng này giống việc dùng thông tin cục bộ phong phú hơn để khớp khai triển Taylor mà không cần tính đạo hàm bậc cao. Một bẫy phổ biến là chỉ nhớ RK4 như công thức thuộc lòng mà quên cấu trúc stage và trọng số.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
h = 0.5
N = 8
t = np.linspace(0, N * h, N + 1)
y = np.zeros(N + 1)
y[0] = 1.0

for n in range(N):
    k1 = f(t[n], y[n])
    k2 = f(t[n] + h / 2, y[n] + h * k1 / 2)
    k3 = f(t[n] + h / 2, y[n] + h * k2 / 2)
    k4 = f(t[n] + h, y[n] + h * k3)
    y[n + 1] = y[n] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

tt = np.linspace(0, t[-1], 300)
plt.plot(tt, np.exp(tt), label="nghiem dung")
plt.plot(t, y, "o-", label="RK4")
plt.legend()
plt.title("Runge-Kutta bac 4 cho y' = y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Runge Kutta method stage visualization
- search: RK4 vs Euler comparison ODE
- search: Butcher tableau intuition animation

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="RK4 so với Euler" description="So sánh trực tiếp Euler và RK4 trên cùng một ODE để thấy lợi ích của nhiều stage trong một bước." path="interactives/chapter13/runge-kutta-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Cho
$$ y'=y,\qquad y(0)=1,\qquad h=0.5. $$
Một bước RK4 từ $$ t=0 $$ cho
$$
k_1=1,\quad k_2=1.25,\quad k_3=1.3125,\quad k_4=1.65625,
$$
nên
$$
y_1 = 1 + \frac{0.5}{6}(1+2(1.25)+2(1.3125)+1.65625)\approx 1.6484,
$$
rất gần $$ e^{0.5}\approx 1.6487 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** So sánh Euler, midpoint và RK4 trên cùng một ODE.

**Bậc sau đại học.** Kết nối với order conditions, Butcher tableaux và SSP methods.
