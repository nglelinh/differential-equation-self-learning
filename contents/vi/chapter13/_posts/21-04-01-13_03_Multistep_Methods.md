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

## Mục tiêu

Bài học này giúp sinh viên hiểu các phương pháp đa bước như Adams-Bashforth, Adams-Moulton, và predictor-corrector. Sau bài học, sinh viên cần biết vì sao ta muốn tận dụng lịch sử các bước trước, biết thiết lập công thức đa bước cơ bản, hiểu nhu cầu khởi động, và nhận ra sự đánh đổi giữa hiệu quả, bộ nhớ, và ổn định.

## Kiến thức nền

Sinh viên nên nắm Euler, Runge-Kutta, tích phân gần đúng, và trực giác rằng nghiệm của ODE thỏa

$$
y(t_{n+1})-y(t_n)=\int_{t_n}^{t_{n+1}} f(t,y(t))\,dt.
$$

Từ góc nhìn này, mọi phương pháp số đều là cách xấp xỉ tích phân ở vế phải.

## Dẫn nhập

Runge-Kutta lấy nhiều mẫu trong cùng một bước. Phương pháp đa bước chọn chiến lược khác: dùng thông tin đã có từ các bước trước để tiết kiệm chi phí tính mới. Thay vì hỏi “trong bước này tôi sẽ lấy bao nhiêu slope?”, ta hỏi “từ lịch sử gần đây, tôi có thể dự đoán slope tiếp theo đến đâu?”.

Đây là một ý tưởng tự nhiên trong mô phỏng dài hạn: nếu mỗi lần tính $$ f $$ tốn kém, việc tái sử dụng dữ liệu cũ có thể tiết kiệm rất nhiều tài nguyên.

## Khái niệm theo ba cách

### Cách trực giác

Nếu theo dõi chuyển động của một xe đạp trong vài giây vừa qua, bạn có thể dự đoán vị trí sắp tới không chỉ từ vận tốc hiện tại mà còn từ xu hướng gần đây. Phương pháp đa bước làm điều tương tự với ODE: lịch sử gần có giá trị dự báo.

### Cách hình ảnh

Giáo viên nên vẽ các điểm $$ t_{n-1},t_n,t_{n+1} $$ và các giá trị $$ f_{n-1},f_n $$. Sau đó dùng một đa thức nội suy đơn giản để nối các giá trị $$ f $$ đã biết, rồi lấy diện tích dưới đa thức đó trên khoảng tiếp theo. Hình này rất mạnh vì cho thấy Adams-Bashforth thực ra là quy tắc tích phân dựa trên lịch sử.

### Cách hình thức

Phương pháp Adams-Bashforth hai bước:

$$ y_{n+1}=y_n+\frac h2\left(3f_n-f_{n-1}\right), $$

trong đó $$ f_n=f(t_n,y_n) $$. Phương pháp Adams-Moulton một bước có dạng

$$ y_{n+1}=y_n+\frac h2\left(f_{n+1}+f_n\right), $$

là phương pháp ngầm. Kết hợp một bước dự đoán tường minh với một bước sửa ngầm tạo nên predictor-corrector.

## Ngộ nhận thường gặp

### “Đa bước nghĩa là chính xác hơn Runge-Kutta”

Không phải lúc nào cũng vậy. Hiệu quả phụ thuộc vào bài toán và yêu cầu ổn định.

### “Dùng nhiều bước trước thì luôn tốt hơn”

Không. Phương pháp càng dài ký ức càng có thể nhạy với sai số lịch sử và khó ổn định hơn.

### “Phương pháp đa bước không cần khởi động”

Sai. Muốn dùng công thức hai bước hay nhiều bước, ta phải có đủ dữ liệu ban đầu.

### “Predictor-corrector là hai phương pháp tách rời”

Không. Đây là một chiến lược phối hợp: dự đoán trước bằng sơ đồ rẻ, rồi sửa lại bằng sơ đồ tốt hơn.

## Tiến trình học

### Bước 1: Viết ODE dưới dạng tích phân

Đây là cửa ngõ tự nhiên để hiểu Adams methods.

### Bước 2: Nội suy hàm $$ f $$ từ dữ liệu cũ

Cho sinh viên thấy công thức đa bước không rơi từ trời xuống mà đến từ nội suy và tích phân.

### Bước 3: Phân biệt explicit và implicit

Adams-Bashforth là tường minh, Adams-Moulton là ngầm.

### Bước 4: Bàn về khởi động và lưu lịch sử

Thường phải dùng Euler hay Runge-Kutta để lấy vài bước đầu.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao phương pháp đa bước cần dữ liệu quá khứ không?
- Sinh viên có biết vì sao phải khởi động bằng phương pháp khác không?
- Sinh viên có phân biệt được vai trò của predictor và corrector không?

## Ví dụ có lời giải

### Ví dụ 1: Adams-Bashforth hai bước cho $$ y'=y $$

Vì $$ f_n=y_n $$, công thức trở thành

$$ y_{n+1}=y_n+\frac h2\left(3y_n-y_{n-1}\right). $$

Đây là quan hệ truy hồi dùng hai giá trị cũ để tạo giá trị mới.

### Ví dụ 2: Vì sao cần khởi động

Để tính $$ y_2 $$ bằng Adams-Bashforth hai bước, ta cần cả $$ y_1 $$ và $$ y_0 $$. Nhưng ban đầu ta chỉ có $$ y_0 $$. Vì vậy phải dùng một phương pháp một bước như Euler hoặc RK4 để sinh ra $$ y_1 $$.

Ví dụ này giúp sinh viên nhớ rằng đa bước không thể bắt đầu từ khoảng không.

### Ví dụ 3: Predictor-corrector

Cho trước $$ y_{n-1} $$ và $$ y_n $$. Ta dự đoán

$$ \widetilde y_{n+1}=y_n+\frac h2(3f_n-f_{n-1}) $$

bằng Adams-Bashforth. Sau đó dùng

$$
y_{n+1}=y_n+\frac h2\left(f(t_{n+1},\widetilde y_{n+1})+f_n\right)
$$

để sửa theo Adams-Moulton. Cách này vừa tiết kiệm vừa cải thiện độ chính xác.

### Ví dụ 4: Lợi ích và rủi ro của ký ức

Nếu một bước nào đó có sai số lớn, sai số ấy có thể ảnh hưởng vài bước kế tiếp vì công thức vẫn dùng dữ liệu cũ. Ví dụ này nhắc sinh viên rằng ký ức là con dao hai lưỡi.

## Câu hỏi khái niệm

1. Vì sao phương pháp đa bước có thể rẻ hơn Runge-Kutta trên bài toán dài hạn?
2. Điều gì khiến ký ức quá khứ vừa hữu ích vừa nguy hiểm?
3. Tại sao bước sửa trong predictor-corrector thường cải thiện đáng kể chất lượng nghiệm?

## Bài toán ứng dụng

1. Trong mô phỏng thời tiết dài hạn, việc tái sử dụng dữ liệu từ các bước trước mang lại lợi ích tính toán gì?
2. Trong mô hình hóa sinh học có hàm $$ f $$ phức tạp, vì sao số lần đánh giá $$ f $$ là yếu tố quan trọng?
3. Trong hệ điều khiển theo thời gian thực, việc phải lưu lịch sử có thể tạo ra hạn chế nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu đã biết hai bước gần nhất, em có tận dụng chúng để dự đoán bước mới không?
- Tại sao lịch sử có thể giúp tiết kiệm tính toán?
- Khi nào lịch sử cũ lại trở thành gánh nặng?

### Hoạt động gợi ý

- Cho sinh viên nội suy tuyến tính $$ f $$ tại hai điểm rồi tự suy ra Adams-Bashforth hai bước.
- So sánh số lần tính $$ f $$ của RK4 và Adams-Bashforth.
- Làm hoạt động vai trò: một nhóm “dự đoán”, một nhóm “hiệu chỉnh”.

### Cách tăng tham gia

- Bắt đầu từ câu hỏi “ta có nên vứt bỏ dữ liệu cũ không?”.
- Dùng sơ đồ thời gian rõ ràng với các mũi tên từ quá khứ sang hiện tại.
- Cho sinh viên kể một ví dụ đời thường khi dự đoán dựa trên xu hướng gần đây.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Chỉ dùng công thức hai bước trước.
- Tập trung vào ý tưởng “dùng lại slope cũ”.
- Hạn chế chứng minh, ưu tiên hình học và quy trình tính.

### Thử thách cho sinh viên khá giỏi

- Tự suy ra Adams-Bashforth ba bước.
- Phân tích ổn định tuyến tính của một phương pháp đa bước đơn giản.
- So sánh multistep với Runge-Kutta theo chi phí và miền ổn định.

## Ghi nhớ nhanh

Phương pháp đa bước tận dụng lịch sử các bước trước để tạo bước mới, nhờ đó có thể giảm chi phí tính toán trên mô phỏng dài hạn. Điểm mạnh của chúng là hiệu quả, còn điểm cần chú ý là khởi động, lưu lịch sử, và ổn định.

---

## Ứng dụng thực tế

### 1. Mô phỏng khí hậu và thời tiết dài hạn

Trong mô phỏng dài hạn, số lần đánh giá hàm hoặc vế phải của hệ rất lớn. Các phương pháp Adams-Bashforth hay predictor-corrector hữu ích vì tái sử dụng lịch sử cũ thay vì tính nhiều slope mới như RK4. Mô hình này phù hợp khi hàm $$ f $$ đắt và bài toán không quá cứng. Giới hạn là khi hệ nhiều thang thời gian hoặc nhiễu số tích lũy mạnh, ký ức dài có thể gây bất lợi.

### 2. Động học hóa học và sinh học tính toán

Nếu mỗi bước phải giải nhiều tương tác phản ứng hay tín hiệu, việc giảm số lần gọi $$ f $$ có thể tiết kiệm đáng kể. Phương pháp đa bước cho lợi thế đó trong nhiều mô phỏng lớn. Tuy nhiên, khi stiffness xuất hiện, phương pháp đa bước tường minh có thể mất ổn định nhanh.

### 3. Tích phân quỹ đạo trong kỹ thuật

Trong mô phỏng cơ học hay điện mạch thời gian dài, người ta thường chấp nhận lưu vài bước lịch sử để đổi lấy hiệu quả tính toán tốt hơn. Điều này làm nổi bật đánh đổi thực hành giữa bộ nhớ, số phép tính, và độ bền ổn định.

## Trực giác sâu hơn

Phương pháp đa bước là bài học rằng dữ liệu quá khứ không chỉ để lưu trữ mà còn có thể trở thành tài nguyên tính toán. Nhưng “ký ức” không phải lúc nào cũng có lợi: một sai số cũ có thể tiếp tục được tái sử dụng nhiều bước sau. Ngộ nhận phổ biến là nghĩ thêm lịch sử luôn đồng nghĩa với thêm chính xác; thực ra ta đang đổi hiệu quả lấy sự nhạy cảm lớn hơn với ổn định và khởi động.

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

Có thể dùng `Plotly.js` để hiển thị các mũi tên từ $$ f_{n-1}, f_n $$ sang $$ y_{n+1} $$, giúp sinh viên nhìn thấy trực tiếp “ký ức” của phương pháp hai bước.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Adams Bashforth visualization`, `predictor corrector method animation`, hoặc `multistep methods stability`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Adams-Bashforth 2 bước" description="Quan sát cách phương pháp đa bước dùng cả slope hiện tại và slope từ bước trước để cập nhật nghiệm số." path="interactives/chapter13/multistep-methods-vi.html" height="620px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ý tưởng dùng lại slope cũ, nhu cầu khởi động, và sự khác nhau giữa dự đoán với hiệu chỉnh.

### Mức sau đại học (Graduate)

Đi sâu vào zero-stability, root condition, phân tích ổn định của họ Adams, và vai trò của phương pháp đa bước ngầm trong bài toán cứng.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dự báo thời tiết số
- Bài toán: Các mô hình khí quyển lớn muốn tái sử dụng thông tin từ nhiều bước trước để giảm chi phí tính toán.
- Mô hình: Adams-Bashforth hay Adams-Moulton dùng các giá trị
$$ f(t_n,y_n), f(t_{n-1},y_{n-1}), \dots $$
để cập nhật nghiệm.
- Giả thiết và giới hạn: Cần bước khởi tạo và có thể nhạy với ổn định.
- Diễn giải: Multistep methods tiết kiệm số lần đánh giá hàm trên mỗi bước sau khi đã "vào guồng".

#### Mô phỏng mạch điện dài hạn
- Bài toán: Khi chạy mô phỏng lâu, chi phí nhiều stage mỗi bước có thể lớn.
- Mô hình: Dùng BDF hoặc Adams để cân bằng giữa ổn định và hiệu quả.
- Giả thiết và giới hạn: BDF thích hợp hơn với hệ cứng; Adams thích hợp hơn với bài toán trơn không cứng.
- Diễn giải: Thông tin quá khứ trở thành tài nguyên số học để dự đoán tương lai.

### 2. Trực giác bổ sung và các kết nối

Runge-Kutta lấy nhiều mẫu trong một bước; multistep lấy ít mẫu hơn nhưng nhớ nhiều bước trước. Đó là hai triết lý khác nhau của phương pháp số. Một bẫy phổ biến là xem multistep chỉ như "công thức dài hơn"; thật ra zero-stability là điều kiện sống còn.

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

Phương pháp Adams-Bashforth bậc 2 có dạng
$$
y_{n+1}=y_n+h\left(\frac{3}{2}f_n-\frac{1}{2}f_{n-1}\right).
$$
Nó dùng slope hiện tại và slope trước đó để ước lượng tích phân của vector trường qua một bước. Ý nghĩa thực tế là ta tận dụng dữ liệu đã tính thay vì luôn bắt đầu lại từ đầu như RK.

### 6. Phân tầng độ khó

**Bậc đại học.** Làm quen với Adams-Bashforth và Adams-Moulton qua ví dụ bậc thấp.

**Bậc sau đại học.** Kết nối với root condition, Dahlquist theory và BDF families.
