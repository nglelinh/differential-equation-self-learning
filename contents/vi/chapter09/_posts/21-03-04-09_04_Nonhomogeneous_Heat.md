---
layout: post
title: "Bài Toán Nhiệt Non-Thuần Nhất"
chapter: '09'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 04 Nonhomogeneous Heat]({{ site.imgurl }}/chapter_img/chapter09/04_nonhomogeneous_heat.svg)

## Mục tiêu

Bài học này xử lý phương trình nhiệt khi điều kiện biên hoặc nguồn nhiệt không còn thuần nhất. Sau bài học, sinh viên cần hiểu chiến lược chuẩn là đưa bài toán về biên thuần nhất bằng một hàm phụ trợ, biết tách nghiệm thành phần cân bằng và phần quá độ, và hiểu cách nguồn nhiệt kích thích từng mode riêng qua các ODE có vế phải.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt với biên thuần nhất, tách biến và khai triển theo mode riêng. Bài này là bước rất quan trọng vì hầu hết các bài toán thực tế đều không "đẹp" như trường hợp thuần nhất hoàn toàn.

## Dẫn nhập

Trong thực tế, hai đầu thanh hiếm khi đều được giữ ở 0, và nguồn nhiệt hiếm khi biến mất hoàn toàn. Nhưng điều đó không có nghĩa là các công cụ của bài toán thuần nhất trở nên vô dụng. Ý tưởng then chốt là tách cái "phiền" của dữ liệu không thuần nhất ra thành một hàm phụ trợ đơn giản, để phần còn lại quay về một bài toán có thể giải bằng mode riêng.

Đây là một bài rất tốt để rèn tư duy chiến lược. Thay vì đối đầu trực tiếp với toàn bộ bài toán, ta tách nó thành phần cân bằng và phần động. Phần cân bằng giải thích trạng thái dài hạn, còn phần động cho biết hệ tiến về trạng thái ấy như thế nào.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu hai đầu thanh bị giữ ở hai nhiệt độ khác nhau, hệ sẽ tiến dần về một hồ sơ nhiệt độ cân bằng nối hai đầu đó. Phần "lệch khỏi cân bằng" mới là thứ thực sự khuếch tán và tắt dần theo thời gian. Đây là trực giác cốt lõi của việc viết

$$ u=w+v. $$

### Cách nhìn hình ảnh

Đồ thị nghiệm tổng quát có thể được hình dung như một đường nền cố định $$ w(x) $$ cộng với các gợn suy giảm $$ v(x,t) $$. Ban đầu gợn có thể lớn, nhưng theo thời gian chúng tắt dần, để lại đường nền cân bằng. Hình ảnh này giúp sinh viên hiểu phần quá độ và phần dừng là hai thành phần khác bản chất.

### Cách nhìn hình thức

Xét

$$
u_t=\alpha^2u_{xx},
\qquad
u(0,t)=T_1,\quad u(L,t)=T_2,
\qquad
u(x,0)=f(x).
$$

Ta tìm hàm dừng $$ w(x) $$ thỏa

$$ w''=0,
\qquad
w(0)=T_1,\quad w(L)=T_2. $$

Kết quả là

$$ w(x)=T_1+\frac{T_2-T_1}{L}x. $$

Đặt $$ u(x,t)=w(x)+v(x,t) $$. Khi đó

$$
v_t=\alpha^2v_{xx},
\qquad
v(0,t)=v(L,t)=0,
\qquad
v(x,0)=f(x)-w(x).
$$

Nếu có nguồn $$ Q(x,t) $$, thì sau khi đưa về biên thuần nhất, ta nhận được ODE mode:

$$ T_n'(t)+\alpha^2\lambda_nT_n(t)=Q_n(t). $$

## Những ngộ nhận thường gặp

- "Biên không thuần nhất thì không dùng được tách biến." Sai. Ta chỉ cần lifting trước.
- "Hàm phụ trợ phải là nghiệm đầy đủ của PDE." Không nhất thiết; thường chỉ cần nó xử lý đúng phần biên.
- "Phần dừng và phần động là hai lời giải tách biệt không liên quan." Sai; chúng ghép lại thành nghiệm thực của bài toán.
- "Nếu có nguồn nhiệt thì mỗi mode vẫn chỉ suy giảm thuần túy." Không đúng; nguồn có thể bơm năng lượng liên tục vào mode.

## Tiến trình học tập đề xuất

### Bước 1: Nhìn xem cái gì không thuần nhất

Biên, nguồn, hay cả hai.

### Bước 2: Chọn hàm phụ trợ

Mục tiêu là biến điều kiện biên thành thuần nhất.

### Bước 3: Viết phương trình cho phần còn lại

Phần này mới là đối tượng của khai triển mode.

### Bước 4: Giải ODE theo từng mode

Nếu có nguồn, ta dùng nhân tích phân hoặc Duhamel.

### Các checkpoint

- Sinh viên có nhận ra nên chọn

$$ w $$

để xử lý biên hay nguồn trước hay không.
- Sinh viên có viết đúng điều kiện đầu mới cho

$$ v $$

hay không.
- Sinh viên có hiểu ý nghĩa vật lý của phần cân bằng và phần quá độ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Biên Dirichlet không thuần nhất

Xét

$$
u_t=\alpha^2u_{xx},
\qquad
u(0,t)=T_1,\quad u(L,t)=T_2.
$$

Chọn

$$ w(x)=T_1+\frac{T_2-T_1}{L}x. $$

Đặt $$ u=w+v $$. Khi đó

$$ v_t=\alpha^2v_{xx},
\qquad
v(0,t)=v(L,t)=0. $$

Ví dụ này là khuôn mẫu cơ bản nhất cho mọi bài lifting.

### Ví dụ 2: Điều kiện đầu lệch khỏi cân bằng

Nếu $$ u(x,0)=f(x) $$, thì $$ v(x,0)=f(x)-w(x) $$. Ta khai triển $$ f(x)-w(x) $$ theo sine series, rồi thu được nghiệm đầy đủ:

$$
u(x,t)=w(x)+\sum_{n=1}^{\infty}b_n e^{-\alpha^2(n\pi/L)^2t}\sin\left(\frac{n\pi x}{L}\right).
$$

Ví dụ này giúp sinh viên thấy điều kiện đầu mới chính là "phần lệch khỏi cân bằng".

### Ví dụ 3: Có nguồn theo thời gian

Xét $$ u_t=\alpha^2u_{xx}+Q(x,t) $$, với biên thuần nhất. Khi khai triển

$$ u(x,t)=\sum_{n=1}^{\infty}T_n(t)X_n(x), $$

ta được $$ T_n'(t)+\alpha^2\lambda_n T_n(t)=Q_n(t) $$. Nghiệm là

$$
T_n(t)=e^{-\alpha^2\lambda_n t}T_n(0)+\int_0^t e^{-\alpha^2\lambda_n(t-s)}Q_n(s)\,ds.
$$

Đây là công thức rất quan trọng: mỗi mode phản ứng như một bộ lọc mũ bị kích bởi nguồn.

### Ví dụ 4: Ý nghĩa dài hạn

Nếu không còn nguồn theo thời gian và biên giữ cố định, thì $$ v(x,t)\to 0 $$ khi $$ t\to\infty $$. Vì vậy $$ u(x,t)\to w(x) $$. Đây là ví dụ giúp sinh viên hiểu tại sao trạng thái cân bằng đáng được tách riêng ngay từ đầu.

## Câu hỏi khái niệm

1. Vì sao chiến lược $$ u=w+v $$ lại đặc biệt tự nhiên trong bài toán nhiệt không thuần nhất?
2. Phần cân bằng và phần quá độ khác nhau thế nào về mặt vật lý?
3. Khi có nguồn nhiệt, vì sao mỗi mode không còn đơn giản chỉ là một hàm mũ suy giảm?

## Bài toán ứng dụng

1. Một thanh có hai đầu giữ ở hai nhiệt độ khác nhau. Vì sao về lâu dài nhiệt độ tiến về một hồ sơ gần tuyến tính?
2. Nếu một nguồn nhiệt tuần hoàn theo thời gian tác động lên hệ, ta mong các mode phản ứng ra sao?
3. Trong kỹ thuật nhiệt, vì sao việc tách phần dừng và phần quá độ giúp đọc hành vi dài hạn của hệ dễ hơn nhiều?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu hai đầu thanh bị giữ ở hai nhiệt độ khác nhau, hệ sẽ tiến về cái gì khi

$$ t\to\infty? $$
"
- Cho sinh viên tự tìm hàm cân bằng

$$ w(x) $$

trước khi giới thiệu lifting như một kỹ thuật tổng quát.
- Hỏi cả lớp: "Nguồn nhiệt sẽ làm thay đổi phần nào của công thức mode?"
- Khuyến khích sinh viên giải thích bằng lời sự khác nhau giữa trạng thái cân bằng và phần tắt dần.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ một mẫu thao tác cố định: xử lý biên trước, viết biến mới, tìm điều kiện đầu mới, rồi mới khai triển mode. Khi có quy trình ổn định, các em sẽ đỡ rối hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi khảo sát trường hợp nguồn không gian-thời gian phức tạp hơn hoặc thảo luận Duhamel như phiên bản liên tục của nguyên lý chồng chất theo thời gian.

## Tóm tắt dễ nhớ

Với bài toán nhiệt không thuần nhất, ta thường tách nghiệm thành phần cân bằng và phần quá độ. Phần cân bằng xử lý biên hoặc nguồn tĩnh, còn phần quá độ quay về biên thuần nhất và được giải bằng các mode riêng. Đây là chiến lược chuẩn cho hầu hết các bài toán nhiệt thực tế.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ biên thay đổi theo thời gian
- Bài toán: Hai đầu thanh bị điều khiển bởi profile nhiệt độ không thuần nhất.
- Mô hình: Tách nghiệm thành phần dừng cộng phần thuần nhất:
$$ u(x,t)=v(x,t)+w(x,t). $$
- Giả thiết và giới hạn: Chọn $$ w $$ sao cho xử lý được biên không thuần nhất.
- Diễn giải: Phần khó của biên được "hấp thụ" vào nghiệm phụ đơn giản hơn.

#### Nguồn nhiệt bên trong
- Bài toán: Hệ có nguồn cưỡng bức trong miền.
- Mô hình:
$$ u_t=\alpha^2 u_{xx}+f(x,t). $$
- Giả thiết và giới hạn: Nguồn đủ trơn để áp dụng khai triển mode hoặc Duhamel.
- Diễn giải: Nghiệm gồm phần tự do cộng phần cưỡng bức.

### 2. Trực giác bổ sung và các kết nối

Bài toán không thuần nhất thường không cần phương pháp hoàn toàn mới; điều cốt lõi là tách đúng phần xử lý biên hay nguồn. Một bẫy phổ biến là cố nhét trực tiếp điều kiện biên không thuần nhất vào cơ sở sin chuẩn mà không đổi biến trước.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 300)
t = 0.05
steady = x
transient = 0.3 * np.sin(np.pi * x) * np.exp(-np.pi**2 * t)
u = steady + transient

plt.plot(x, steady, label="phan bien")
plt.plot(x, u, label="tong nghiem")
plt.xlabel("x")
plt.ylabel("u")
plt.title("Tach thanh phan dung va thanh phan tan dan")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: nonhomogeneous heat equation steady state decomposition
- search: Duhamel principle heat equation
- search: heat equation with source term visualization

### 5. Bài toán mẫu có bối cảnh thực

Cho
$$ u_t=u_{xx},\qquad u(0,t)=0,\qquad u(1,t)=1. $$
Đặt
$$ w(x)=x,\qquad v(x,t)=u(x,t)-x. $$
Khi đó $$ v $$ thỏa biên thuần nhất:
$$ v(0,t)=v(1,t)=0, $$
và phương trình cho $$ v $$ có thể giải bằng tách biến chuẩn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phép tách nghiệm để đưa biên không thuần nhất về thuần nhất.

**Bậc sau đại học.** Liên hệ với Duhamel, nguyên lý chồng chất và semigroup có nguồn.
