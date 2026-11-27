---
layout: post
title: "Phương Trình Vi Phân Ngẫu Nhiên"
chapter: '13'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: optional
---

![Trực giác của phương trình vi phân ngẫu nhiên và đường đi Brownian]({{ site.imgurl }}/chapter_img/chapter13/08_stochastic_differential_equations.svg)

Một hạt phấn hoa lơ lửng trong cốc nước không bao giờ trượt theo đường cong trơn mà giật cục hỗn loạn dưới hàng tỷ cú va chạm phân tử; giá cổ phiếu trên sàn giao dịch cũng nhảy múa từng giây bởi tin tức bất ngờ. Để mô tả những hệ động lực chịu tác động của nhiễu ngẫu nhiên liên tục, ta bổ sung thêm số hạng chuyển động Brown $dW_t$ vào ODE để có **Phương trình Vi phân Ngẫu nhiên (SDE)**—nơi quy tắc đạo hàm cổ điển bị phá vỡ bởi một luật chơi kỳ diệu mang tên **Bổ đề Itô**: $(dW_t)^2 = dt$!

## Kiến thức cần nhớ: Bốn trụ cột của Phương trình Vi phân Ngẫu nhiên (SDE)

1. **Chuyển động Brown $W_t$ (Quá trình Wiener)**:
   Các số gia $W_{t+\Delta t} - W_t \sim \mathcal{N}(0, \Delta t)$ độc lập nhau, đường đi liên tục khắp nơi nhưng **không khả vi ở bất kỳ điểm nào**, và có bậc độ lớn $|\Delta W_t| \sim \sqrt{\Delta t} \gg \Delta t$!
2. **Bổ đề Itô (Quy tắc Chuỗi Ngẫu nhiên)**:
   Vì $(dW_t)^2 = dt$ không thể bỏ qua như $(dt)^2 = 0$, khai triển Taylor của $f(X_t)$ buộc phải giữ thêm số hạng đạo hàm bậc hai: $df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)\sigma^2\,dt$—sinh ra hệ số điều chỉnh độ trôi $-\frac{1}{2}\sigma^2$ nổi tiếng trong mô hình Black–Scholes!
3. **Sơ đồ Số Euler–Maruyama và Milstein**:
   Euler–Maruyama rời rạc hóa $dX_t = \mu\,dt + \sigma\,dW_t$ thành $X_{n+1} = X_n + \mu\Delta t + \sigma\sqrt{\Delta t}\,Z_n$ ($Z_n \sim \mathcal{N}(0,1)$), đạt bậc hội tụ **mạnh $0{,}5$** và **yếu $1{,}0$**. Thêm số hạng hiệu chỉnh bậc hai $\frac{1}{2}\sigma\sigma'(\Delta W_n^2 - \Delta t)$ cho ra sơ đồ Milstein nâng bậc hội tụ mạnh lên $1{,}0$!
4. **Cầu nối SDE $\leftrightarrow$ PDE (Phương trình Fokker–Planck / Kolmogorov)**:
   Trong khi mỗi đường đi $X_t$ là ngẫu nhiên, mật độ xác suất $p(x, t)$ của nó lại tiến hóa hoàn toàn tất định theo một phương trình khuếch tán–đối lưu (Fokker–Planck)!

## Mục tiêu

Bài học tùy chọn này giới thiệu phương trình vi phân ngẫu nhiên (SDE) như mô hình vi phân cho các hệ chịu tác động của nhiễu ngẫu nhiên. Sau bài học, sinh viên cần nắm vai trò của chuyển động Brown (Brownian motion), cấu trúc cơ bản của phương trình Itô, ý tưởng của lược đồ Euler–Maruyama, và sự khác biệt giữa nghiệm xác định của ODE với họ quỹ đạo ngẫu nhiên của SDE.

## Kiến thức nền

Sinh viên cần nắm ODE, phương pháp Euler, phân phối chuẩn và trực giác về nhiễu trong các hệ thực nghiệm. Bài học không yêu cầu sâu về lý thuyết xác suất độ đo, nhưng cần nắm bước chuyển tư duy rằng nghiệm nay là một quá trình ngẫu nhiên thay vì một hàm xác định duy nhất.

## Dẫn nhập

Nhiều hệ trong tự nhiên và tài chính không tiến hóa theo quy luật hoàn toàn xác định: giá tài sản dao động bất định, hạt phấn chịu va chạm liên tục từ các phân tử chất lỏng, kích thước quần thể chịu tác động của biến động môi trường. ODE chỉ mô tả xu hướng xác định; để đưa nhiễu nội tại vào phương trình, ta cần đến SDE.

SDE giữ lại thành phần xu hướng (drift) tương tự ODE và bổ sung thành phần nhiễu (diffusion). Sự xuất hiện của thành phần ngẫu nhiên làm thay đổi căn bản cách hiểu về nghiệm, quy tắc vi phân và cách xây dựng lược đồ số.


### Giải thích: Tính tay 1 bước Euler–Maruyama cho Chuyển động Brown Hình học (Giá cổ phiếu)

Xét SDE $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ với giá ban đầu $S_0 = 100$, lợi suất kỳ vọng $\mu = 0{,}10$, độ biến động $\sigma = 0{,}20$, bước thời gian $\Delta t = 0{,}25$ (1 quý), và mẫu ngẫu nhiên chuẩn $Z = +1{,}0$:
1. **Tính số gia Brown**: $\Delta W = \sqrt{\Delta t}\,Z = \sqrt{0{,}25} \times 1{,}0 = \mathbf{0{,}50}$.
2. **Bước Euler–Maruyama**:
   $$S_1^{\text{EM}} = S_0 + \mu S_0\Delta t + \sigma S_0\Delta W = 100 + 0{,}10(100)(0{,}25) + 0{,}20(100)(0{,}50) = 100 + 2{,}5 + 10 = \mathbf{112{,}50}.$$
3. **So với nghiệm Itô chính xác** $S_{\Delta t} = S_0\exp\!\big((\mu - \tfrac{1}{2}\sigma^2)\Delta t + \sigma\Delta W\big)$:
   $$S_{0{,}25}^{\text{exact}} = 100\exp\!\big((0{,}10 - 0{,}02)(0{,}25) + 0{,}20(0{,}50)\big) = 100\,e^{0{,}12} \approx \mathbf{112{,}75}.$$
   Lưu ý số hạng hiệu chỉnh Itô $-\frac{1}{2}\sigma^2 = -0{,}02$: chính biến động $\sigma$ làm giảm tốc độ tăng trưởng trung vị của tài sản!
## Khái niệm theo ba cách

### Cách trực giác

Hãy hình dung một chiếc lá trôi trên mặt sông: dòng chảy chính đẩy chiếc lá theo một hướng tổng thể, còn các xoáy nước nhỏ và dao động ngẫu nhiên làm quỹ đạo rung lắc liên tục. Trong SDE, thành phần drift tương ứng với dòng chảy chính, còn thành phần diffusion tương ứng với các nhiễu loạn ngẫu nhiên đó.

### Cách hình ảnh

Khi vẽ nhiều quỹ đạo mô phỏng cùng xuất phát từ một điều kiện đầu dưới cùng một SDE, ta thấy thay vì một đường cong duy nhất như ở ODE, nghiệm là cả một họ quỹ đạo phân nhánh ngẫu nhiên theo thời gian.

### Cách hình thức

Một SDE dạng Itô có biểu thức $$ dX_t=b(X_t,t)\,dt+\sigma(X_t,t)\,dW_t $$, trong đó $$ W_t $$ là chuyển động Brown chuẩn:

- Thành phần $$ b(X_t,t)\,dt $$ gọi là **drift**, mô tả xu hướng xác định.
- Thành phần $$ \sigma(X_t,t)\,dW_t $$ gọi là **diffusion**, mô tả cường độ nhiễu ngẫu nhiên.

Lược đồ số cơ bản **Euler–Maruyama** có dạng:

$$
X_{n+1}=X_n+b(X_n,t_n)\Delta t+\sigma(X_n,t_n)\Delta W_n,
$$

với các gia số độc lập $$ \Delta W_n\sim \mathcal{N}(0,\Delta t) $$.

## Ngộ nhận thường gặp

### “SDE chỉ là ODE cộng thêm nhiễu bên ngoài ở bước cuối”

Chưa đủ. Nhiễu ngẫu nhiên tác động liên tục vào động lực của hệ, làm thay đổi cả quy tắc giải tích (công thức Itô) lẫn cấu trúc nghiệm.

### “Chuyển động Brown là một hàm trơn dao động nhanh”

Sai. Quỹ đạo chuyển động Brown liên tục ở mọi nơi nhưng hầu chắc chắn không khả vi cổ điển tại bất kỳ điểm nào.

### “Chỉ cần chạy một quỹ đạo mô phỏng là nắm được hành vi của SDE”

Không đúng. Thường cần mô phỏng nhiều quỹ đạo để ước lượng phân phối, kỳ vọng, phương sai hoặc xác suất sự kiện.

### “Euler–Maruyama chỉ là phương pháp Euler đổi tên biến”

Không đúng. Gia số nhiễu có độ lệch chuẩn cỡ $$ \sqrt{\Delta t} $$ (phương sai tỷ lệ với $$ \Delta t $$), khiến tính chất hội tụ mạnh và hội tụ yếu khác hẳn ODE xác định.

## Tiến trình học

### Bước 1: Mở rộng từ ODE sang SDE

Xuất phát từ phương trình vi phân xác định rồi bổ sung thành phần nhiễu.

### Bước 2: Làm quen với chuyển động Brown

Nhấn mạnh hai tính chất cốt lõi: gia số độc lập và phân phối chuẩn $$ \mathcal{N}(0,\Delta t) $$.

### Bước 3: Thiết lập lược đồ Euler–Maruyama

Nhìn nhận đây là phần mở rộng tự nhiên của phương pháp Euler tiến sang môi trường ngẫu nhiên.

### Bước 4: Phân biệt quỹ đạo mẫu và đặc trưng thống kê

Làm rõ sự khác nhau giữa từng quỹ đạo riêng lẻ với kỳ vọng hay phân phối của tập quỹ đạo.

### Các điểm kiểm tra hiểu bài

- Sinh viên có phân biệt được vai trò của drift và diffusion hay không?
- Sinh viên có giải thích được vì sao gia số $$ \Delta W_n\sim \mathcal{N}(0,\Delta t) $$ hay không?
- Sinh viên có hiểu vì sao một SDE với cùng điều kiện đầu lại sinh ra nhiều quỹ đạo khác nhau hay không?

## Ví dụ có lời giải

### Ví dụ 1: Chuyển động Brown thuần túy

Xét $$ dX_t=dW_t $$, có nghiệm $$ X_t=X_0+W_t $$. Đây là mô hình cơ bản nhất của quá trình ngẫu nhiên không có thành phần drift.

### Ví dụ 2: Euler–Maruyama với drift và diffusion hằng

Xét $$ dX_t=\mu\,dt+\sigma\,dW_t $$. Lược đồ số là $$ X_{n+1}=X_n+\mu\Delta t+\sigma\Delta W_n $$, trong đó mỗi bước cập nhật gồm phần tịnh tiến xác định cộng thêm một gia số ngẫu nhiên chuẩn.

### Ví dụ 3: Chuyển động Brown hình học (Geometric Brownian motion)

Xét $$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t $$. Lược đồ Euler–Maruyama cho $$ X_{n+1}=X_n+\mu X_n\Delta t+\sigma X_n\Delta W_n $$. Đây là mô hình tiêu biểu trong tài chính định lượng, trong đó biên độ nhiễu tỷ lệ với trạng thái hiện tại.

### Ví dụ 4: Đối chiếu ODE và SDE

Khi đặt $$ \sigma=0 $$, phương trình rút về ODE $$ X'=\mu X $$ với một quỹ đạo xác định duy nhất từ mỗi điều kiện đầu. Khi $$ \sigma\ne 0 $$, các quỹ đạo cùng xuất phát từ $$ X_0 $$ sẽ phân tách ngẫu nhiên theo thời gian.

## Câu hỏi khái niệm

1. Vì sao nghiệm của SDE không thể xem là một đường cong trơn duy nhất?
2. Thành phần drift và thành phần diffusion đảm nhận hai vai trò khác nhau như thế nào?
3. Vì sao độ lớn điển hình của gia số chuyển động Brown có cỡ $$ \sqrt{\Delta t} $$ thay vì $$ \Delta t $$?

## Bài toán ứng dụng

1. Trong tài chính định lượng, vì sao diễn biến giá cổ phiếu thường được mô hình hóa bằng SDE thay vì ODE?
2. Trong sinh học tế bào, nhiễu nội tại của các phản ứng hóa sinh ít phân tử được thể hiện qua thành phần diffusion như thế nào?
3. Trong vật lý thống kê, chuyển động Brown của hạt lơ lửng trong chất lỏng liên hệ trực tiếp với SDE ra sao?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu cùng một điều kiện đầu nhưng các lần đo thực nghiệm cho nhiều quỹ đạo khác nhau, mô hình ODE thuần túy còn đủ không?
- Hiểu thế nào về việc nhiễu tích lũy theo căn bậc hai của thời gian?
- Khi mô phỏng SDE, khi nào ta quan tâm từng quỹ đạo cụ thể và khi nào quan tâm phân phối thống kê?

### Hoạt động gợi ý

- Chạy mô phỏng vài quỹ đạo Euler–Maruyama và so sánh với đường nghiệm ODE tương ứng (khi $$ \sigma=0 $$).
- Tính trung bình mẫu của nhiều quỹ đạo để đối chiếu với kỳ vọng lý thuyết.
- Thảo luận nhóm các hệ thực tế cần bổ sung yếu tố ngẫu nhiên.

### Cách tăng tham gia

- Mở đầu bằng biểu đồ giá tài sản hoặc chuyển động hạt bụi trong chất lỏng.
- Cho sinh viên tự sinh một vài bước số ngẫu nhiên chuẩn để cảm nhận sự phân nhánh của quỹ đạo.
- Yêu cầu phân biệt bằng lời giữa "sai số đo đạc" và "nhiễu động lực nội tại của hệ".

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung vào trực giác drift–diffusion và công thức Euler–Maruyama.
- Chưa đi sâu vào công thức Itô ở lần tiếp cận đầu tiên.
- Sử dụng nhiều đồ thị so sánh nhiều quỹ đạo mẫu.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu phân biệt giữa hội tụ mạnh (strong convergence) và hội tụ yếu (weak convergence).
- So sánh hai cách diễn giải tích phân ngẫu nhiên Itô và Stratonovich.
- Dẫn xuất nghiệm giải tích của chuyển động Brown hình học bằng công thức Itô.

## Ghi nhớ nhanh

SDE mở rộng ODE cho các hệ chịu nhiễu ngẫu nhiên nội tại: nghiệm không còn là một đường cong xác định mà là một quá trình ngẫu nhiên, và lược đồ Euler–Maruyama là phương pháp số cơ bản để mô phỏng các quỹ đạo đó.

---

## Ứng dụng thực tế

### 1. Giá tài sản và tài chính định lượng

Chuyển động Brown hình học $$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t $$ là mô hình cơ sở cho giá tài sản, với drift mô tả tỷ suất sinh lời kỳ vọng và diffusion mô tả độ biến động thị trường. Dù chưa nắm bắt được các bước nhảy giá hay độ biến động thay đổi theo thời gian, mô hình này là điểm khởi đầu chuẩn cho lý thuyết SDE.

### 2. Chuyển động Brown và vật lý thống kê

Hạt nhỏ lơ lửng trong chất lỏng chịu vô số va chạm phân tử ngẫu nhiên. SDE tách riêng lực cản/lực ngoài xác định (drift) khỏi tác động va chạm vi mô (diffusion) — một trong những động lực lịch sử quan trọng nhất của lý thuyết SDE.

### 3. Sinh học quần thể và hóa sinh tế bào

Với quần thể nhỏ hoặc phản ứng hóa sinh có số lượng phân tử ít, dao động ngẫu nhiên nội tại có thể ảnh hưởng mạnh tương đương xu hướng trung bình. SDE cho phép khảo sát các hiện tượng mà ODE bỏ sót, như sự thoát khỏi trạng thái cân bằng do nhiễu.

## Trực giác sâu hơn

Chuyển từ ODE sang SDE làm thay đổi câu hỏi trọng tâm: từ "tìm một hàm duy nhất" sang "khảo sát phân phối của tập quỹ đạo và các đại lượng thống kê như kỳ vọng, phương sai hay xác suất vượt ngưỡng".

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
T = 1.0
N = 500
dt = T / N
t = np.linspace(0, T, N + 1)
mu, sigma = 0.5, 0.7

plt.figure(figsize=(9, 5))
for _ in range(8):
    dW = np.sqrt(dt) * np.random.randn(N)
    X = np.zeros(N + 1)
    X[0] = 1.0
    for n in range(N):
        X[n + 1] = X[n] + mu * X[n] * dt + sigma * X[n] * dW[n]
    plt.plot(t, X, alpha=0.8)

plt.title('Nhiều quỹ đạo Euler-Maruyama cho geometric Brownian motion')
plt.xlabel('t')
plt.ylabel('X_t')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để sinh nhiều quỹ đạo mẫu từ cùng một điều kiện đầu và bật/tắt đường trung bình mẫu nhằm đối chiếu giữa từng quỹ đạo riêng lẻ với hành vi thống kê.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Euler Maruyama visualization`, `Brownian motion simulation`, hoặc `Ito vs Stratonovich intuition`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào khái niệm drift, diffusion, chuyển động Brown và lược đồ Euler–Maruyama.

### Mức sau đại học (Graduate)

Đi sâu vào hội tụ mạnh và hội tụ yếu, công thức Itô, phương trình Fokker–Planck, diễn giải Stratonovich và các lược đồ số bậc cao (như Milstein).

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thị trường tài chính
- Bài toán: Mô hình hóa giá tài sản vừa có xu hướng vừa chịu biến động ngẫu nhiên.
- Mô hình: $$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t $$.
- Giả thiết và giới hạn: Chuyển động Brown là mô hình lý tưởng hóa; dữ liệu thực tế có thể xuất hiện bước nhảy và độ biến động thay đổi theo thời gian.
- Diễn giải: SDE tích hợp trực tiếp nhiễu ngẫu nhiên vào phương trình động lực.

#### Chuyển động Brown và khuếch tán
- Bài toán: Mô phỏng hạt nhỏ chịu va chạm ngẫu nhiên liên tục trong chất lỏng.
- Mô hình: Các phương trình kiểu Langevin hoặc chuyển động Brown hình học.
- Giả thiết và giới hạn: Giả thiết nhiễu trắng Gaussian là xấp xỉ lý tưởng hóa.
- Diễn giải: SDE kết nối trực tiếp ODE với lý thuyết xác suất và phương trình Fokker–Planck.

### 2. Trực giác bổ sung và các kết nối

Vì quỹ đạo chuyển động Brown không khả vi cổ điển, giải tích Itô thay thế các quy tắc vi phân thông thường. Một sai sót phổ biến là thao tác với $$ dW_t $$ như vi phân cổ điển, bỏ qua số hạng bậc hai đặc trưng (số hạng Itô) xuất hiện từ $$ (dW_t)^2 \sim dt $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
T, N = 1.0, 800
dt = T / N
t = np.linspace(0, T, N + 1)
mu, sigma, X0 = 0.3, 0.6, 1.0
dW = np.sqrt(dt) * np.random.randn(N)
X = np.zeros(N + 1)
X[0] = X0

for n in range(N):
    X[n + 1] = X[n] + mu * X[n] * dt + sigma * X[n] * dW[n]

plt.plot(t, X)
plt.title("Mot quyd ao Euler-Maruyama")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Euler Maruyama simulation visualization
- search: geometric Brownian motion sample paths
- search: Ito calculus intuition Brownian motion

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Euler-Maruyama cho geometric Brownian motion" description="Sinh nhiều quỹ đạo mẫu để phân biệt trực giác nghiệm ngẫu nhiên với nghiệm xác định của ODE." path="interactives/chapter13/sde-euler-maruyama-vi.html" height="660px" %}

### 5. Bài toán mẫu có bối cảnh thực

Cho chuyển động Brown hình học $$ dX_t=\mu X_t\,dt+\sigma X_t\,dW_t $$. Lược đồ Euler–Maruyama được viết:
$$
X_{n+1}=X_n+\mu X_n \Delta t+\sigma X_n \Delta W_n,
$$
trong đó $$ \Delta W_n \sim \mathcal{N}(0,\Delta t) $$. Đây là phiên bản ngẫu nhiên trực tiếp của phương pháp Euler tiến.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm khái niệm quỹ đạo mẫu, nhiễu Brown và lược đồ Euler–Maruyama.

**Bậc sau đại học.** Kết nối với công thức Itô, hội tụ mạnh/yếu và phương trình Fokker–Planck.

## Video tham khảo

- xem trước: [21. Stochastic Differential Equations](https://www.youtube.com/watch?v=qdbkvD4N-us) — MIT OpenCourseWare, tiếng Anh. Bài giảng MIT 18.S096 giới thiệu phương trình vi phân ngẫu nhiên.
- [Lecture 24: Stochastic Calculus](https://www.youtube.com/watch?v=5cruqmIF6l0) — MIT OpenCourseWare, tiếng Anh. Giới thiệu giải tích ngẫu nhiên làm nền tảng cho SDE.
- [Latent Stochastic Differential Equations for Irregularly-Sampled Time Series - David Duvenaud](https://www.youtube.com/watch?v=93wr5vhI0F4) — Institute for Advanced Study, tiếng Anh. Trình bày ứng dụng SDE ẩn theo hướng dữ liệu cho chuỗi thời gian.
