---
layout: post
title: "Phương Pháp Đa Bước"
chapter: '13'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Trực giác về phương pháp đa bước và predictor-corrector]({{ site.imgurl }}/chapter_img/chapter13/03_multistep_methods.svg )

Phương pháp RK4 rất chính xác, nhưng ở mỗi bước nó phải đánh giá hàm vế phải $f(t, y)$ tới **4 lần** rồi ném bỏ toàn bộ kết quả sau khi bước sang $t_{n+1}$—một sự lãng phí lớn khi $f$ là một mô phỏng vật lý thiên văn hay khí quyển cực kỳ tốn CPU! **Phương pháp Đa bước Tuyến tính (Linear Multistep Methods)** như Adams–Bashforth, Adams–Moulton và BDF giải quyết bài toán ấy đầy thông minh: tận dụng lại lịch sử các giá trị $f_{n}, f_{n-1}, \dots, f_{n-k+1}$ đã tính sẵn để đạt bậc chính xác cao mà chỉ cần **đúng 1 lần gọi hàm $f$ mỗi bước**!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương pháp Đa bước (LMM)

1. **Họ Adams (Nội suy đa thức cho vế phải $f$)**:
   - *Adams–Bashforth (Hiện)*: nội suy $f$ qua các điểm quá khứ $t_n, t_{n-1}, \dots$ để ngoại suy sang $[t_n, t_{n+1}]$.
   - *Adams–Moulton (Ẩn)*: thêm cả điểm đích $f_{n+1}$ vào đa thức nội suy—tăng bậc chính xác và mở rộng đáng kể miền ổn định (thường ghép thành cặp Dự báo–Hiệu chỉnh PEC/PECE!).
2. **Họ BDF (Backward Differentiation Formulas — Khắc tinh của Bài toán Cứng)**:
   Thay vì tích phân $f$, BDF xấp xỉ đạo hàm $y'_{n+1}$ bằng đa thức đi qua $y_{n+1}, y_n, \dots, y_{n-k+1}$—tạo ra các sơ đồ ẩn siêu ổn định (BDF1 đến BDF6; BDF7 trở đi mất ổn định 0!).
3. **Định lý Tương đương Dahlquist (Ổn định 0 + Nhất quán $\iff$ Hội tụ)**:
   Đa thức đặc trưng thứ nhất $\rho(\zeta) = \sum \alpha_j \zeta^j$ phải thỏa mãn **điều kiện nghiệm** (mọi nghiệm có $|\zeta| \le 1$, và nghiệm trên đường tròn đơn vị phải là nghiệm đơn) để phương pháp không tự sinh nghiệm giả bùng nổ!
4. **Giai đoạn Khởi động (Starting Values)**:
   Vì sơ đồ $k$-bước cần $k$ giá trị ban đầu $y_0, y_1, \dots, y_{k-1}$ trong khi bài toán chỉ cho $y_0$, ta luôn dùng một phương pháp đơn bước (như RK4) để chạy $k - 1$ bước đầu tiên rồi mới bàn giao cho sơ đồ đa bước!

## Mục tiêu

Bài học này giới thiệu các phương pháp đa bước như Adams–Bashforth, Adams–Moulton và lược đồ dự đoán–hiệu chỉnh (predictor–corrector). Sau bài học, sinh viên cần hiểu lý do tận dụng lịch sử các bước trước, thiết lập được công thức đa bước cơ bản, nắm nhu cầu khởi động bằng phương pháp một bước, và nhận diện sự đánh đổi giữa hiệu quả tính toán, bộ nhớ và tính ổn định.

## Kiến thức nền

Sinh viên cần nắm phương pháp Euler, Runge–Kutta, phép tính tích phân gần đúng và dạng tích phân của ODE:

$$
y(t_{n+1})-y(t_n)=\int_{t_n}^{t_{n+1}} f(t,y(t))\,dt.
$$

Từ biểu thức này, mỗi phương pháp số có thể xem là một cách xấp xỉ tích phân ở vế phải.

## Dẫn nhập

Trong khi Runge–Kutta lấy nhiều mẫu độ dốc bên trong một bước, phương pháp đa bước chọn hướng tiếp cận khác: tái sử dụng các giá trị đạo hàm đã tính ở những bước trước để dự đoán bước tiếp theo.

Chiến lược này đặc biệt có lợi trong các mô phỏng dài hạn có hàm vế phải $$ f $$ tốn kém về mặt tính toán, vì số lần đánh giá $$ f $$ trên mỗi bước giảm đi đáng kể.


### Khung giải thích (nên đọc chậm): Tính tay 1 bước Adams–Bashforth bậc 2 (AB2) chỉ với 1 lần gọi hàm

Giải $y' = -y$, $y(0) = 1$ với $h = 0{,}1$ bằng công thức AB2: $y_{n+1} = y_n + \frac{h}{2}(3f_n - f_{n-1})$:
1. **Khởi động**: Ta có $y_0 = 1 \implies f_0 = -1$. Dùng giá trị khởi động chính xác $y_1 = e^{-0{,}1} \approx 0{,}904837 \implies f_1 = -0{,}904837$.
2. **Bước AB2 tính $y_2$ tại $t_2 = 0{,}2$**:
   $$y_2 = 0{,}904837 + \frac{0{,}1}{2}\big(3(-0{,}904837) - (-1)\big) = 0{,}904837 + 0{,}05(-1{,}714511) = \mathbf{0{,}819111}.$$
3. **Đối chiếu nghiệm đúng $e^{-0{,}2} \approx 0{,}818731$**:
   Sai số chỉ là $\mathbf{3{,}8 \times 10^{-4}}$—đạt bậc $O(h^2)$ mà chỉ tốn đúng **1 lần đánh giá $f$** ở mỗi bước mới (bằng một nửa chi phí của RK2)!
## Khái niệm theo ba cách

### Cách trực giác

Khi quan sát chuyển động của một vật trong vài giây gần nhất, ta có thể dự đoán vị trí kế tiếp không chỉ từ vận tốc tức thời mà còn từ xu hướng thay đổi trước đó. Phương pháp đa bước vận dụng đúng nguyên tắc này cho ODE: dùng thông tin lịch sử gần để ngoại suy xu hướng.

### Cách hình ảnh

Xét các mốc $$ t_{n-1},t_n,t_{n+1} $$ cùng các giá trị đã biết $$ f_{n-1},f_n $$. Ta dựng đa thức nội suy đi qua các giá trị $$ f $$ đã có rồi lấy tích phân đa thức đó trên đoạn $$ [t_n, t_{n+1}] $$. Hình ảnh này cho thấy Adams–Bashforth thực chất là một công thức cầu phương dựa trên lịch sử.

### Cách hình thức

Phương pháp Adams–Bashforth hai bước (tường minh) có dạng:

$$ y_{n+1}=y_n+\frac h2\left(3f_n-f_{n-1}\right), $$

trong đó $$ f_n=f(t_n,y_n) $$. Phương pháp Adams–Moulton một bước (còn gọi là quy tắc hình thang, dạng ẩn) có dạng:

$$ y_{n+1}=y_n+\frac h2\left(f_{n+1}+f_n\right). $$

Kết hợp một bước dự đoán tường minh với một bước hiệu chỉnh theo công thức ẩn tạo thành lược đồ dự đoán–hiệu chỉnh (predictor–corrector).

## Ngộ nhận thường gặp

### “Phương pháp đa bước luôn chính xác hơn Runge–Kutta”

Không hẳn. Lựa chọn tối ưu phụ thuộc vào chi phí đánh giá $$ f $$, độ trơn của nghiệm và yêu cầu về tính ổn định.

### “Dùng càng nhiều bước quá khứ thì càng tốt”

Sai. Số bước quá khứ càng nhiều thì miền ổn định thường càng thu hẹp và lược đồ càng nhạy với sai số lịch sử.

### “Phương pháp đa bước không cần bước khởi động”

Sai. Để áp dụng công thức hai bước hoặc nhiều bước, ta phải tính sẵn các giá trị đầu tiên bằng một phương pháp một bước.

### “Dự đoán–hiệu chỉnh là hai phương pháp tách biệt”

Không đúng. Đây là một quy trình kết hợp: dùng lược đồ tường minh để ước lượng trước rồi dùng lược đồ ẩn để hiệu chỉnh giá trị đó.

## Tiến trình học

### Bước 1: Viết ODE dưới dạng tích phân

Đặt nền tảng trực tiếp cho cách dẫn xuất họ phương pháp Adams.

### Bước 2: Nội suy $$ f $$ từ dữ liệu đã biết

Thấy rõ công thức đa bước xuất phát từ phép nội suy đa thức và lấy tích phân.

### Bước 3: Phân biệt tường minh và ẩn

Adams–Bashforth là họ tường minh, còn Adams–Moulton là họ ẩn.

### Bước 4: Xử lý bước khởi động và lưu trữ lịch sử

Dùng phương pháp một bước (như Euler hoặc Runge–Kutta) để sinh các điểm đầu tiên cần thiết.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao phương pháp đa bước cần dữ liệu quá khứ hay không?
- Sinh viên có hiểu vì sao phải khởi động bằng phương pháp một bước hay không?
- Sinh viên có phân biệt được vai trò của bước dự đoán và bước hiệu chỉnh hay không?

## Ví dụ có lời giải

### Ví dụ 1: Adams–Bashforth hai bước cho $$ y'=y $$

Vì $$ f_n=y_n $$, công thức trở thành:

$$ y_{n+1}=y_n+\frac h2\left(3y_n-y_{n-1}\right). $$

Đây là hệ thức truy hồi dùng hai giá trị gần nhất để tính giá trị kế tiếp.

### Ví dụ 2: Nhu cầu khởi động

Để tính $$ y_2 $$ bằng Adams–Bashforth hai bước, ta cần cả $$ y_0 $$ và $$ y_1 $$. Vì bài toán giá trị ban đầu chỉ cung cấp $$ y_0 $$, ta phải dùng phương pháp một bước như Euler hoặc RK4 để tính $$ y_1 $$ trước.

### Ví dụ 3: Lược đồ dự đoán–hiệu chỉnh

Từ $$ y_{n-1} $$ và $$ y_n $$, ta dự đoán bằng Adams–Bashforth:

$$ \widetilde y_{n+1}=y_n+\frac h2(3f_n-f_{n-1}), $$

sau đó hiệu chỉnh theo công thức Adams–Moulton:

$$
y_{n+1}=y_n+\frac h2\left(f(t_{n+1},\widetilde y_{n+1})+f_n\right).
$$

Cách kết hợp này tránh phải giải phương trình phi tuyến ẩn nhưng vẫn cải thiện độ chính xác và tính ổn định.

### Ví dụ 4: Lợi ích và rủi ro của việc dùng lịch sử

Nếu một bước nào đó phát sinh sai số lớn, sai số đó sẽ tiếp tục đi vào tính toán ở các bước kế tiếp do công thức sử dụng lại giá trị cũ. Điều này cho thấy việc khai thác lịch sử luôn đi kèm yêu cầu kiểm soát ổn định chặt chẽ.

## Câu hỏi khái niệm

1. Vì sao phương pháp đa bước có thể tiết kiệm chi phí tính toán hơn Runge–Kutta trong mô phỏng dài hạn?
2. Việc dùng dữ liệu quá khứ mang lại lợi ích gì và tiềm ẩn rủi ro gì?
3. Vì sao bước hiệu chỉnh trong lược đồ dự đoán–hiệu chỉnh thường cải thiện rõ chất lượng nghiệm?

## Bài toán ứng dụng

1. Trong mô phỏng thời tiết dài hạn, việc tái sử dụng giá trị vế phải từ các bước trước giúp tiết kiệm tài nguyên tính toán như thế nào?
2. Trong mô hình sinh học có vế phải $$ f $$ phức tạp, vì sao số lần đánh giá $$ f $$ mỗi bước là chỉ tiêu quan trọng?
3. Trong hệ điều khiển thời gian thực, yêu cầu lưu trữ lịch sử và thay đổi bước thời gian có thể gây khó khăn gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu đã có giá trị độ dốc ở hai bước gần nhất, ta có thể tận dụng chúng để dự đoán bước tiếp theo bằng cách nào?
- Vì sao việc tái sử dụng lịch sử giúp giảm số lần đánh giá hàm?
- Khi nào dữ liệu quá khứ lại trở thành bất lợi cho thuật toán?

### Hoạt động gợi ý

- Cho sinh viên tự nội suy tuyến tính $$ f $$ qua hai điểm và tích phân để suy ra Adams–Bashforth hai bước.
- So sánh số lần đánh giá hàm $$ f $$ trên mỗi bước giữa RK4 và Adams–Bashforth.
- Chia nhóm thực hành quy trình dự đoán–hiệu chỉnh từng bước trên một ODE đơn giản.

### Cách tăng tham gia

- Mở đầu bằng câu hỏi: "Tại sao lại bỏ phí các giá trị độ dốc đã tính ở bước trước?"
- Vẽ trục thời gian với mũi tên chỉ rõ các điểm quá khứ đóng góp vào $$ y_{n+1} $$.
- Liên hệ với các tình huống dự báo thực tế dựa trên xu hướng gần đây.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung trước vào công thức hai bước (AB2).
- Nhấn mạnh ý tưởng cốt lõi là tái sử dụng các độ dốc đã tính.
- Ưu tiên diễn giải hình học và quy trình tính trước khi đi sâu vào chứng minh bậc sai số.

### Thử thách cho sinh viên khá giỏi

- Tự suy ra công thức Adams–Bashforth ba bước.
- Phân tích tính ổn định tuyến tính của một phương pháp đa bước đơn giản.
- So sánh phương pháp đa bước với Runge–Kutta về chi phí tính toán và miền ổn định.

## Ghi nhớ nhanh

Phương pháp đa bước tận dụng thông tin đã tính từ các bước trước để giảm số lần đánh giá hàm trên mỗi bước, đặc biệt hiệu quả trong mô phỏng dài hạn; đổi lại, cần lưu ý bước khởi động, bộ nhớ lịch sử và điều kiện ổn định.

---

## Ứng dụng thực tế

### 1. Mô phỏng khí hậu và thời tiết dài hạn

Trong mô phỏng dài hạn, chi phí đánh giá vế phải của hệ rất lớn. Các phương pháp Adams–Bashforth hoặc dự đoán–hiệu chỉnh giúp giảm đáng kể số lần đánh giá $$ f $$ so với RK4 khi bài toán trơn và không quá cứng. Tuy nhiên, nếu hệ chứa nhiều thang thời gian chênh lệch hoặc nhiễu tích lũy mạnh, bộ nhớ dài có thể gây bất lợi về ổn định.

### 2. Động học hóa học và sinh học tính toán

Khi mỗi bước phải tính nhiều phản ứng tương tác phức tạp, việc giảm số lần gọi $$ f $$ mang lại lợi ích rõ rệt. Song nếu bài toán trở nên cứng, các phương pháp đa bước tường minh dễ mất ổn định và cần chuyển sang họ ẩn như BDF.

### 3. Tích phân quỹ đạo trong kỹ thuật

Trong mô phỏng cơ học hoặc mạch điện dài hạn, việc lưu trữ một vài bước lịch sử để đổi lấy ít phép tính hơn trên mỗi bước là lựa chọn phổ biến, thể hiện sự cân bằng thực tế giữa bộ nhớ, tốc độ và tính ổn định.

## Trực giác sâu hơn

Phương pháp đa bước cho thấy dữ liệu quá khứ không chỉ là kết quả lưu trữ mà còn là nguồn thông tin tính toán. Tuy vậy, thêm lịch sử không tự động đồng nghĩa với kết quả tốt hơn: ta đang đánh đổi giữa chi phí mỗi bước thấp hơn với yêu cầu khắt khe hơn về khởi động và tính ổn định.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

h = 0.2
t = np.arange(0, 2 + h, h)
y = np.zeros_like(t)
y[0] = 1.0
y[1] = np.exp(h)  # giả sử khởi động tốt

for n in range(1, len(t) - 1):
    f_n = y[n]
    f_nm1 = y[n - 1]
    y[n + 1] = y[n] + h * (3 * f_n - f_nm1) / 2

t_exact = np.linspace(0, 2, 400)
plt.plot(t_exact, np.exp(t_exact), 'k--', label='e^t')
plt.plot(t, y, 'o-', label='Adams-Bashforth 2 bước')
plt.title('Phương pháp đa bước dùng lịch sử gần')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để hiển thị trực tiếp các mũi tên từ $$ f_{n-1}, f_n $$ tới $$ y_{n+1} $$, minh họa trực quan cơ chế dùng lịch sử của phương pháp hai bước.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Adams Bashforth visualization`, `predictor corrector method animation`, hoặc `multistep methods stability`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Adams-Bashforth 2 bước" description="Quan sát cách phương pháp đa bước dùng cả slope hiện tại và slope từ bước trước để cập nhật nghiệm số." path="interactives/chapter13/multistep-methods-vi.html" height="620px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ý tưởng tái sử dụng độ dốc cũ, nhu cầu khởi động bằng phương pháp một bước và vai trò của dự đoán–hiệu chỉnh.

### Mức sau đại học (Graduate)

Đi sâu vào ổn định bậc không (zero-stability), điều kiện nghiệm đặc trưng (root condition), phân tích miền ổn định họ Adams và vai trò của phương pháp đa bước ẩn (BDF) cho bài toán cứng.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dự báo thời tiết số
- Bài toán: Các mô hình khí quyển lớn cần tái sử dụng thông tin từ các bước trước để giảm chi phí tính toán.
- Mô hình: Adams–Bashforth hoặc Adams–Moulton sử dụng dãy giá trị $$ f(t_n,y_n), f(t_{n-1},y_{n-1}), \dots $$ để cập nhật nghiệm.
- Giả thiết và giới hạn: Cần bước khởi tạo và kiểm soát chặt tính ổn định.
- Diễn giải: Sau giai đoạn khởi động, mỗi bước chỉ cần ít lần đánh giá hàm hơn.

#### Mô phỏng mạch điện dài hạn
- Bài toán: Với thời gian mô phỏng dài, chi phí nhiều tầng trên mỗi bước có thể quá cao.
- Mô hình: Sử dụng họ BDF hoặc họ Adams để cân bằng giữa ổn định và tốc độ.
- Giả thiết và giới hạn: BDF phù hợp với hệ cứng, còn Adams phù hợp với bài toán trơn không cứng.
- Diễn giải: Thông tin từ các bước trước trở thành tài nguyên tính toán để dự báo bước tiếp theo.

### 2. Trực giác bổ sung và các kết nối

Runge–Kutta lấy nhiều mẫu bên trong một bước, còn phương pháp đa bước lấy ít mẫu hơn nhưng tận dụng nhiều bước trước đó. Không nên xem phương pháp đa bước chỉ là "công thức dài hơn": điều kiện ổn định bậc không (zero-stability) là yếu tố sống còn quyết định sự hội tụ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
h = 0.25
N = 12
t = np.linspace(0, N * h, N + 1)
y = np.zeros(N + 1)
y[0] = 1.0
y[1] = np.exp(h)  # khoi tao tu nghiem dung de nhan manh cong thuc AB2

for n in range(1, N):
    y[n + 1] = y[n] + h * (1.5 * f(t[n], y[n]) - 0.5 * f(t[n - 1], y[n - 1]))

tt = np.linspace(0, t[-1], 300)
plt.plot(tt, np.exp(tt), label="nghiem dung")
plt.plot(t, y, "o-", label="Adams-Bashforth 2")
plt.legend()
plt.title("Mot vi du multistep")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Adams Bashforth Adams Moulton visualization
- search: multistep method zero stability intuition
- search: BDF method stiff ODE animation

### 5. Bài toán mẫu có bối cảnh thực

Phương pháp Adams–Bashforth bậc hai có dạng:
$$
y_{n+1}=y_n+h\left(\frac{3}{2}f_n-\frac{1}{2}f_{n-1}\right).
$$
Công thức này kết hợp độ dốc hiện tại và độ dốc bước trước để xấp xỉ tích phân trường vector trên một bước, nhờ đó tận dụng dữ liệu đã tính thay vì tính lại nhiều tầng như Runge–Kutta.

### 6. Phân tầng độ khó

**Bậc đại học.** Làm quen với Adams–Bashforth và Adams–Moulton qua các công thức bậc thấp.

**Bậc sau đại học.** Kết nối với điều kiện nghiệm đặc trưng (root condition), lý thuyết Dahlquist và họ phương pháp BDF.

## Video tham khảo

- xem trước: [Numerical methods for ODEs - Multistep methods - Adams Bashforth](https://www.youtube.com/watch?v=fp6n7x55tkQ) — The Math Guy, tiếng Anh. Dẫn xuất các phương pháp đa bước Adams–Bashforth.
- [Examples of Adams-Bashforth Methods](https://www.youtube.com/watch?v=JVKBe_vYdg0) — Melvin Leok, tiếng Anh. Giải các ví dụ cụ thể bằng phương pháp Adams–Bashforth.
- [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, tiếng Anh. Tổng quan về phương pháp một bước Runge–Kutta để đối chiếu với phương pháp đa bước.
