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

Bài học này giới thiệu họ phương pháp Runge–Kutta như sự cải tiến có hệ thống của phương pháp Euler. Sau bài học, sinh viên cần hiểu ý tưởng lấy nhiều mẫu độ dốc trong cùng một bước, thiết lập được công thức RK4, giải thích vì sao RK4 chính xác hơn Euler đáng kể, và nhận biết khi nào Runge–Kutta là lựa chọn thích hợp hay chưa phù hợp.

## Kiến thức nền

Sinh viên cần nắm phương pháp Euler, khai triển Taylor, khái niệm bậc chính xác và bài toán giá trị ban đầu cho ODE. Trong khi Euler chỉ dùng một độ dốc tại đầu bước, Runge–Kutta sử dụng nhiều mẫu độ dốc để nắm bắt chính xác hơn hình dạng cục bộ của nghiệm trên toàn bước.

## Dẫn nhập

Nếu phương pháp Euler chỉ dựa vào hướng đi tại điểm xuất phát của mỗi đoạn đường, thì phương pháp Runge–Kutta quan sát thêm độ dốc ở giữa đoạn và cuối đoạn trước khi quyết định bước cập nhật. Thay vì chỉ dùng độ dốc đầu bước, ta tìm một độ dốc đại diện tốt hơn cho cả khoảng $$ [t_n, t_{n+1}] $$.

Chỉ bằng cách lấy một vài mẫu độ dốc có chọn lọc trong mỗi bước, Runge–Kutta nâng cao bậc chính xác đáng kể mà không cần tính đạo hàm bậc cao của $$ f $$. Nhờ ưu điểm này, họ Runge–Kutta trở thành công cụ tiêu chuẩn cho nhiều bài toán ODE không cứng.

## Khái niệm theo ba cách

### Cách trực giác

Khi đi qua một đoạn dốc uốn lượn, nếu chỉ đo độ nghiêng tại điểm đầu thì dự đoán vị trí cuối đoạn dễ bị lệch. Nếu đo thêm độ nghiêng ở giữa đoạn và gần cuối đoạn rồi kết hợp lại, ta thu được ước lượng sát hơn nhiều cho độ dốc trung bình của cả quãng. Runge–Kutta thực hiện đúng nguyên tắc đó trên trường hướng của ODE.

### Cách hình ảnh

Trong một bước của RK4, ta lấy bốn mẫu độ dốc $$ k_1,k_2,k_3,k_4 $$ tại đầu bước, hai vị trí giữa bước và cuối bước. Giá trị mới $$ y_{n+1} $$ được tính theo trung bình có trọng số của bốn độ dốc đó (với trọng số $$ 1, 2, 2, 1 $$ chia cho 6), ưu tiên thông tin ở giữa bước.

### Cách hình thức

Với bài toán $$ y'=f(t,y) $$, phương pháp Runge–Kutta bậc bốn cổ điển (RK4) được xác định bởi:

$$
k_1=f(t_n,y_n), \qquad k_2=f\!\left(t_n+\frac h2,y_n+\frac h2k_1\right),
$$

$$
k_3=f\!\left(t_n+\frac h2,y_n+\frac h2k_2\right), \qquad k_4=f(t_n+h,y_n+hk_3),
$$

và

$$
y_{n+1}=y_n+\frac h6\left(k_1+2k_2+2k_3+k_4\right).
$$

Trong điều kiện nghiệm đủ trơn, phương pháp này có sai số toàn cục bậc bốn, tức $$ O(h^4) $$.

## Ngộ nhận thường gặp

### “Runge–Kutta chỉ là lặp phương pháp Euler nhiều lần”

Không đúng. Các điểm lấy mẫu và trọng số trong Runge–Kutta được thiết kế đặc biệt để triệt tiêu các số hạng sai số và khớp khai triển Taylor đến bậc cao.

### “Phương pháp bậc cao hơn luôn tốt hơn”

Không hẳn. Khi bài toán cứng hoặc mỗi lần đánh giá hàm $$ f $$ rất tốn kém, phương pháp bậc cao tường minh chưa chắc là lựa chọn tối ưu.

### “RK4 chính xác đơn thuần vì dùng bốn điểm”

Chưa đủ. Yếu tố quyết định không chỉ là số tầng (stage) mà là cách chọn vị trí lấy mẫu và bộ trọng số sao cho khớp với khai triển Taylor bậc bốn.

### “Phương pháp có bậc chính xác cao thì tự động ổn định”

Sai. Bậc chính xác và tính ổn định là hai tính chất độc lập nhau.

## Tiến trình học

### Bước 1: Nhìn lại hạn chế của phương pháp Euler

Nhấn mạnh nguyên nhân sai số bậc thấp: chỉ sử dụng duy nhất độ dốc tại đầu bước.

### Bước 2: Giới thiệu ý tưởng lấy nhiều độ dốc trong một bước

Xem Runge–Kutta như cách ước lượng chính xác hơn độ dốc trung bình trên đoạn $$ [t_n,t_{n+1}] $$.

### Bước 3: Đi từ RK2 lên RK4

Bắt đầu từ phương pháp trung điểm hoặc Heun (RK2) trước khi giới thiệu RK4 để công thức không xuất hiện đột ngột.

### Bước 4: Cân nhắc chi phí và hiệu quả

Mỗi bước RK4 cần bốn lần đánh giá $$ f $$, nhưng thường cho phép dùng bước $$ h $$ lớn hơn nhiều so với Euler để đạt cùng mức sai số.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao lấy nhiều mẫu độ dốc trong một bước lại giảm sai số hay không?
- Sinh viên có viết và tính đúng bốn hệ số $$ k_1,k_2,k_3,k_4 $$ hay không?
- Sinh viên có phân biệt được bậc chính xác của phương pháp với số lần đánh giá hàm trong một bước hay không?

## Ví dụ có lời giải

### Ví dụ 1: RK2 cho bài toán đơn giản

Xét $$ y'=y,\qquad y(0)=1 $$. Với bước $$ h $$, phương pháp trung điểm (RK2) cho:

$$
k_1=y_n,
\qquad
k_2=y_n+\frac h2k_1=y_n\left(1+\frac h2\right),
$$

suy ra

$$
y_{n+1}=y_n+hk_2=y_n\left(1+h+\frac{h^2}{2}\right).
$$

Kết quả này chính xác hơn Euler vì đã khớp thêm số hạng bậc hai của khai triển $$ e^h $$.

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

Thay vào công thức RK4 cho biểu thức khớp hoàn toàn với khai triển Taylor của $$ e^h $$ đến bậc bốn. Đây là lý do RK4 đạt độ chính xác cao trên các bài toán trơn.

### Ví dụ 3: So sánh Euler và RK4

Với bước $$ h=0.5 $$ trên bài toán $$ y'=y $$, sau một bước Euler cho $$ y_1=1.5 $$, trong khi RK4 cho giá trị rất sát với $$ e^{0.5}\approx 1.6487 $$. Sự chênh lệch thể hiện rõ ngay cả trên một bước khá lớn.

### Ví dụ 4: Khi RK4 chưa phải lựa chọn tốt

Xét bài toán cứng $$ y'=-1000y $$. Dù có bậc chính xác cao trên bài toán trơn, RK4 là phương pháp tường minh nên vẫn bị ràng buộc bởi miền ổn định hữu hạn và buộc phải dùng bước $$ h $$ rất nhỏ. Ví dụ này nhắc lại rằng bậc cao không tự động giải quyết tính cứng.

## Câu hỏi khái niệm

1. Vì sao phương pháp Runge–Kutta đạt bậc chính xác cao mà không cần tính đạo hàm bậc cao của $$ f $$?
2. Vì sao bốn độ dốc trong RK4 phản ánh tốt hành vi trung bình của nghiệm trên cả bước $$ [t_n,t_{n+1}] $$?
3. Trong trường hợp nào nên ưu tiên phương pháp bậc cao, và khi nào nên ưu tiên phương pháp có miền ổn định rộng hơn?

## Bài toán ứng dụng

1. Trong mô phỏng quỹ đạo hành tinh, vì sao RK4 thường vượt trội hơn phương pháp Euler?
2. Trong mô hình sinh học quần thể, khi chi phí mỗi lần tính $$ f $$ thấp, ta cân đối giữa kích thước bước và độ chính xác như thế nào?
3. Trong điều khiển robot thời gian thực, chi phí bốn lần đánh giá $$ f $$ mỗi bước của RK4 có thể đặt ra hạn chế gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu Euler chỉ lấy độ dốc tại đầu bước, ta nên lấy mẫu thêm ở vị trí nào trong đoạn $$ [t_n,t_{n+1}] $$?
- Vì sao thông tin tại điểm giữa bước lại được gán trọng số lớn hơn trong RK4?
- Tại sao bốn độ dốc cần được tổ hợp có trọng số thay vì lấy trung bình đều?

### Hoạt động gợi ý

- Cho sinh viên tính tay một bước RK2 và RK4 trên cùng một bài toán đơn giản.
- Chạy mã so sánh đồ thị sai số của Euler, RK2 và RK4 theo bước $$ h $$ trên thang log–log.
- Thảo luận nhóm so sánh lợi thế của Euler (chi phí mỗi bước thấp) và RK4 (độ chính xác cao).

### Cách tăng tham gia

- Trình bày phương pháp trung điểm (RK2) trước khi đưa ra công thức RK4.
- Mời sinh viên dự đoán ý nghĩa của bộ trọng số $$ 1,2,2,1 $$ (gợi liên hệ với quy tắc Simpson).
- Yêu cầu giải thích ý tưởng RK4 bằng lời trước khi viết công thức.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm quen từ RK2 trước khi chuyển sang RK4.
- Dùng sơ đồ luồng minh họa thứ tự tính $$ k_1 \to k_2 \to k_3 \to k_4 $$.
- Tập trung vào ý tưởng "ước lượng độ dốc trung bình trên cả bước".

### Thử thách cho sinh viên khá giỏi

- Suy ra các điều kiện bậc (order conditions) cơ bản cho RK2 và RK4.
- So sánh miền ổn định của RK4 với Euler tiến trên bài toán $$ y'=\lambda y $$.
- Tìm hiểu cặp phương pháp Runge–Kutta lồng nhau (embedded Runge–Kutta) dùng để điều chỉnh bước thích nghi.

## Ghi nhớ nhanh

Runge–Kutta cải tiến phương pháp Euler bằng cách lấy nhiều mẫu độ dốc trong cùng một bước để ước lượng chính xác hơn xu thế trung bình của nghiệm. RK4 được dùng rộng rãi vì cân bằng tốt giữa độ chính xác bậc bốn và chi phí tính toán hợp lý trên các bài toán trơn không cứng.

---

## Ứng dụng thực tế

### 1. Quỹ đạo hành tinh và vệ tinh

Trong cơ học thiên thể, hệ phương trình chuyển động thường có dạng:

$$
\mathbf{x}'=\mathbf{v},
\qquad
\mathbf{v}'=\mathbf{a}(\mathbf{x}).
$$

Trên khoảng thời gian ngắn đến trung hạn, RK4 cho quỹ đạo chính xác hơn nhiều so với Euler với cùng số bước (khi chi phí tính gia tốc chấp nhận được). Tuy nhiên, với mô phỏng rất dài hạn cần bảo toàn năng lượng hoặc cấu trúc Hamilton, cần các phương pháp bảo toàn cấu trúc (như tích phân symplectic).

### 2. Động học dịch bệnh và sinh học quần thể

Các mô hình như SIR hay logistic mở rộng thường cần chạy nhanh nhiều kịch bản tham số. Khi mỗi lần đánh giá $$ f $$ không quá tốn kém, RK4 giảm mạnh sai số với bước thời gian vừa phải; giới hạn chỉ xuất hiện khi hệ có tính cứng hoặc nhiều thang thời gian chênh lệch lớn.

### 3. Điều khiển robot và mô phỏng thời gian thực

Trạng thái robot tuân theo các hệ ODE phi tuyến. RK4 cho độ chính xác quỹ đạo cao hơn Euler, nhưng bốn lần gọi hàm mỗi bước có thể tạo áp lực lên chu kỳ tính toán thời gian thực — thể hiện rõ sự đánh đổi giữa độ chính xác và tốc độ.

## Trực giác sâu hơn

Runge–Kutta dựa trên ý tưởng khai thác nhiều thông tin hơn trong cùng một bước thay vì chỉ chia nhỏ bước liên tục. Sức mạnh của RK4 không nằm ở việc có bốn công thức con, mà ở việc vị trí các tầng và bộ trọng số được chọn chính xác để khớp khai triển Taylor đến bậc bốn.

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

Có thể dùng `Plotly.js` cho phép bật/tắt từng độ dốc $$ k_1,k_2,k_3,k_4 $$ trên cùng một bước để quan sát trực tiếp cách tổ hợp trọng số của chúng tạo ra bước cập nhật RK4.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `RK4 visualization`, `Runge Kutta slope sampling`, hoặc `adaptive Runge Kutta animation`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ý tưởng lấy nhiều mẫu độ dốc trong một bước và ưu thế độ chính xác của RK4 so với Euler trên các bài toán trơn không cứng.

### Mức sau đại học (Graduate)

Đi sâu vào điều kiện bậc (order conditions), bảng Butcher, phương pháp lồng nhau (embedded methods), điều khiển bước thích nghi và giới hạn ổn định của họ Runge–Kutta trên bài toán cứng.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo tên lửa hoặc robot
- Bài toán: Mô phỏng hệ động lực với độ chính xác cao hơn Euler nhưng vẫn tránh giải hệ ẩn phức tạp.
- Mô hình: Sử dụng RK4 với công thức $$ y_{n+1}=y_n+\frac{h}{6}(k_1+2k_2+2k_3+k_4) $$ cùng bốn độ dốc trung gian.
- Giả thiết và giới hạn: Cần bốn lần đánh giá hàm mỗi bước và không tự động xử lý được tính cứng.
- Diễn giải: Cải thiện độ chính xác nhờ thăm dò độ dốc tại các điểm bên trong bước.

#### Mô hình dịch bệnh
- Bài toán: Mô phỏng hệ SIR phi tuyến với độ chính xác tốt trên khoảng thời gian ngắn và trung hạn.
- Mô hình: Áp dụng RK2 hoặc RK4 cho hệ:
$$
S'=-\beta SI,\quad I'=\beta SI-\gamma I,\quad R'=\gamma I.
$$
- Giả thiết và giới hạn: Độ chính xác phụ thuộc kích thước bước; việc bảo toàn tính không âm có thể cần bước nhỏ hoặc lược đồ chuyên biệt.
- Diễn giải: Họ Runge–Kutta thường là lựa chọn khởi đầu tiêu chuẩn trước khi thiết kế các lược đồ chuyên biệt cho cấu trúc riêng của bài toán.

### 2. Trực giác bổ sung và các kết nối

Nếu Euler chỉ dựa vào độ dốc tại một điểm, thì Runge–Kutta kết hợp nhiều độ dốc bên trong một bước để khớp khai triển Taylor bậc cao mà không phải tính đạo hàm bậc cao của $$ f $$. Nên nắm vững cấu trúc các tầng (stages) và trọng số thay vì chỉ học thuộc công thức RK4 một cách máy móc.

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

Cho $$ y'=y,\qquad y(0)=1,\qquad h=0.5 $$. Một bước RK4 từ $$ t=0 $$ cho:
$$
k_1=1,\quad k_2=1.25,\quad k_3=1.3125,\quad k_4=1.65625,
$$
suy ra
$$
y_1 = 1 + \frac{0.5}{6}(1+2(1.25)+2(1.3125)+1.65625)\approx 1.6484,
$$
rất sát với nghiệm chính xác $$ e^{0.5}\approx 1.6487 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** So sánh trực tiếp Euler, phương pháp trung điểm và RK4 trên cùng một ODE.

**Bậc sau đại học.** Kết nối với điều kiện bậc, bảng Butcher và các phương pháp SSP (strong stability preserving).

## Video tham khảo

- xem trước: [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, tiếng Anh. Tổng quan về phương pháp Runge–Kutta như bộ tích phân một bước đa dụng.
- [Coding a Fourth-Order Runge-Kutta Integrator in Python and Matlab](https://www.youtube.com/watch?v=vNoFdtcPFdk) — Steve Brunton, tiếng Anh. Hướng dẫn cài đặt phương pháp Runge–Kutta bậc bốn trong Python và MATLAB.
- [Understanding Runge-Kutta](https://www.youtube.com/watch?v=t48a2M27kjM) — ThatMathThing, tiếng Anh. Giải thích trực quan nguồn gốc các tầng trong phương pháp Runge–Kutta.
