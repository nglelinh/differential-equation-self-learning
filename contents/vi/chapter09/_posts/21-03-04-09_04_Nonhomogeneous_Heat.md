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

Ngoài đời thực, hiếm khi hai đầu thanh kim loại đều giữ đúng ở $0^\circ\text{C}$ và không có nguồn nhiệt bên trong. Một thanh đồng có thể có đầu trái nhúng nước sôi $100^\circ\text{C}$, đầu phải giữ $20^\circ\text{C}$, lại có dòng điện chạy qua tự sinh nhiệt $q(x)$! Khi đó ta không thể tách biến trực tiếp—mà dùng một phép tách cực kỳ thanh lịch: **Trạng thái Dừng $v(x)$ + Phần Quá độ $w(x, t)$**!

## Kiến thức cần nhớ: Bốn bước giải Bài toán Nhiệt Không Thuần nhất

1. **Phân tách $u(x, t) = v(x) + w(x, t)$**:
   Chọn **nghiệm dừng (steady-state)** $v(x)$ thỏa $0 = \alpha v''(x) + q(x)$ cùng **đúng điều kiện biên không thuần nhất** ($v(0)=T_1, v(L)=T_2$).
2. **Đưa phần quá độ $w(x, t) = u(x, t) - v(x)$ về bài toán thuần nhất**:
   Khi lấy hiệu, cả nguồn nhiệt $q(x)$ lẫn biên $T_1, T_2$ đều triệt tiêu sạch: $w_t = \alpha w_{xx}$, $w(0,t) = w(L,t) = 0$, với điều kiện đầu mới $w(x, 0) = f(x) - v(x)$!
3. **Khai triển hàm riêng cho nguồn phụ thuộc thời gian $q(x, t)$**:
   Nếu nguồn nhiệt hoặc biên thay đổi theo $t$, ta khai triển $u(x, t) = \sum c_n(t)\phi_n(x)$ và giải ODE bậc nhất cho từng $c_n'(t) + \alpha\lambda_n c_n(t) = q_n(t)$ bằng nhân tử tích phân (Nguyên lý Duhamel).
4. **Trực giác vật lý**:
   Khi $t \to \infty$, phần quá độ $w(x, t) \to 0$, nên nhiệt độ toàn thanh hội tụ về đúng đường cong dừng $v(x)$!

## Mục tiêu

Bài học này xử lý phương trình nhiệt khi điều kiện biên hoặc nguồn nhiệt không thuần nhất. Sau bài học, sinh viên cần nắm chiến lược đưa bài toán về điều kiện biên thuần nhất bằng một hàm phụ trợ, biết tách nghiệm thành phần cân bằng (dừng) và phần quá độ, đồng thời hiểu cách nguồn nhiệt kích thích từng mode riêng thông qua các phương trình vi phân thường có vế phải.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt với điều kiện biên thuần nhất, phương pháp tách biến và khai triển theo mode riêng. Đây là bước quan trọng vì phần lớn bài toán thực tế đều có biên hoặc nguồn không thuần nhất.

## Dẫn nhập

Trong thực tế, hai đầu thanh hiếm khi cùng giữ ở nhiệt độ 0 và nguồn nhiệt bên trong cũng thường khác 0. Tuy vậy, các công cụ của bài toán thuần nhất vẫn phát huy tác dụng: ta tách phần không thuần nhất vào một hàm phụ trợ đơn giản để phần còn lại quay về bài toán biên thuần nhất có thể giải bằng khai triển mode riêng.

Cách tiếp cận này mang tính chiến lược rõ ràng: thay vì xử lý toàn bộ bài toán cùng lúc, ta phân tách nghiệm thành phần cân bằng và phần quá độ. Phần cân bằng mô tả trạng thái dài hạn, còn phần quá độ cho biết hệ tiến dần về trạng thái đó như thế nào.

### Giải thích: Tìm nghiệm dừng $v(x)$ và thiết lập bài toán quá độ $w(x, t)$ cho thanh có biên $20^\circ\text{C}$ và $80^\circ\text{C}$

Xét $u_t = u_{xx}$ trên $[0, 10]$ với $u(0, t) = 20,\; u(10, t) = 80$ và nhiệt độ ban đầu $u(x, 0) = 50$.
1. **Tìm nghiệm dừng $v(x)$** ($v''(x) = 0 \implies v(x) = ax + b$):
   - $v(0) = 20 \implies b = 20$; $v(10) = 10a + 20 = 80 \implies a = 6$.
   - Vậy $v(x) = \mathbf{20 + 6x}$ (đường thẳng nối từ $20^\circ\text{C}$ đến $80^\circ\text{C}$!).
2. **Thiết lập bài toán cho $w(x, t) = u(x, t) - (20 + 6x)$**:
   - Phương trình: $w_t = w_{xx}$.
   - Điều kiện biên: $w(0, t) = 20 - 20 = \mathbf{0}$, $w(10, t) = 80 - 80 = \mathbf{0}$ (thuần nhất 100%!).
   - Điều kiện đầu mới: $w(x, 0) = 50 - (20 + 6x) = \mathbf{30 - 6x}$.
3. **Kiểm tra trạng thái cuối**: Khi $t \to \infty$, $w(x, t) \to 0$, nên tại điểm giữa thanh $x = 5$ nhiệt độ tiến về $v(5) = 20 + 6(5) = \mathbf{50^\circ\text{C}}$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi hai đầu thanh được giữ ở hai mức nhiệt độ cố định khác nhau, hệ sẽ tiến dần về một phân bố nhiệt độ cân bằng nối giữa hai đầu mút. Phần sai lệch so với trạng thái cân bằng mới là thành phần khuếch tán và tắt dần theo thời gian. Đó là ý nghĩa trực quan của phép tách $$ u=w+v $$.

### Cách nhìn hình ảnh

Đồ thị nghiệm có thể được hình dung như một đường nền cố định $$ w(x) $$ cộng thêm các gợn suy giảm $$ v(x,t) $$. Ở thời điểm ban đầu, các gợn này có thể lớn, nhưng theo thời gian chúng tắt dần, chỉ còn lại phân bố cân bằng $$ w(x) $$. Hình ảnh này phân biệt rõ bản chất của phần dừng và phần quá độ.

### Cách nhìn hình thức

Xét bài toán

$$
u_t=\alpha^2u_{xx},
\qquad
u(0,t)=T_1,\quad u(L,t)=T_2,
\qquad
u(x,0)=f(x).
$$

Ta tìm hàm dừng $$ w(x) $$ thỏa mãn

$$ w''=0,
\qquad
w(0)=T_1,\quad w(L)=T_2. $$

Nghiệm dừng là

$$ w(x)=T_1+\frac{T_2-T_1}{L}x. $$

Đặt $$ u(x,t)=w(x)+v(x,t) $$. Khi đó $$ v $$ thỏa mãn bài toán thuần nhất

$$
v_t=\alpha^2v_{xx},
\qquad
v(0,t)=v(L,t)=0,
\qquad
v(x,0)=f(x)-w(x).
$$

Nếu bài toán có thêm nguồn nhiệt $$ Q(x,t) $$, sau khi đưa về điều kiện biên thuần nhất, khai triển theo mode riêng dẫn đến hệ ODE:

$$ T_n'(t)+\alpha^2\lambda_nT_n(t)=Q_n(t). $$

## Những ngộ nhận thường gặp

- "Điều kiện biên không thuần nhất thì không thể dùng tách biến." Sai; chỉ cần thực hiện bước nâng hàm phụ trợ (lifting) để đưa về biên thuần nhất trước.
- "Hàm phụ trợ bắt buộc phải là nghiệm đầy đủ của PDE." Không nhất thiết; nhiều trường hợp chỉ cần hàm phụ trợ thỏa mãn điều kiện biên.
- "Phần dừng và phần quá độ là hai bài toán độc lập không liên quan." Sai; điều kiện ban đầu của phần quá độ phụ thuộc trực tiếp vào hàm dừng.
- "Khi có nguồn nhiệt, mỗi mode vẫn chỉ suy giảm thuần túy theo hàm mũ." Không đúng; nguồn nhiệt có thể liên tục bổ sung năng lượng vào từng mode.

## Tiến trình học tập đề xuất

### Bước 1: Xác định thành phần không thuần nhất

Kiểm tra xem yếu tố không thuần nhất nằm ở điều kiện biên, ở nguồn nhiệt hay ở cả hai.

### Bước 2: Chọn hàm phụ trợ phù hợp

Mục tiêu là khử phần không thuần nhất ở điều kiện biên.

### Bước 3: Thiết lập bài toán cho ẩn hàm mới

Chú ý cập nhật cả phương trình (nếu cần) lẫn điều kiện ban đầu trước khi khai triển mode.

### Bước 4: Giải ODE cho từng mode

Khi có vế phải nguồn nhiệt, giải bằng thừa số tích phân hoặc công thức Duhamel.

### Các điểm kiểm tra

- Sinh viên có xác định đúng cách chọn hàm $$ w $$ để xử lý biên hoặc nguồn trước hay không.
- Sinh viên có viết đúng điều kiện ban đầu mới cho $$ v $$ hay không.
- Sinh viên có hiểu rõ ý nghĩa vật lý của phần cân bằng và phần quá độ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Điều kiện biên Dirichlet không thuần nhất

Xét

$$
u_t=\alpha^2u_{xx},
\qquad
u(0,t)=T_1,\quad u(L,t)=T_2.
$$

Chọn hàm dừng

$$ w(x)=T_1+\frac{T_2-T_1}{L}x. $$

Đặt $$ u=w+v $$. Khi đó

$$ v_t=\alpha^2v_{xx},
\qquad
v(0,t)=v(L,t)=0. $$

Đây là khuôn mẫu cơ bản nhất cho kỹ thuật khử điều kiện biên không thuần nhất.

### Ví dụ 2: Điều kiện ban đầu lệch khỏi trạng thái cân bằng

Với $$ u(x,0)=f(x) $$, ta có $$ v(x,0)=f(x)-w(x) $$. Khai triển $$ f(x)-w(x) $$ theo chuỗi sin, ta thu được nghiệm đầy đủ

$$
u(x,t)=w(x)+\sum_{n=1}^{\infty}b_n e^{-\alpha^2(n\pi/L)^2t}\sin\left(\frac{n\pi x}{L}\right).
$$

Ví dụ này cho thấy điều kiện ban đầu mới chính là phần lệch của nhiệt độ ban đầu so với trạng thái cân bằng.

### Ví dụ 3: Bài toán có nguồn nhiệt theo thời gian

Xét $$ u_t=\alpha^2u_{xx}+Q(x,t) $$ với điều kiện biên thuần nhất. Khai triển nghiệm theo hệ hàm riêng

$$ u(x,t)=\sum_{n=1}^{\infty}T_n(t)X_n(x), $$

ta thu được $$ T_n'(t)+\alpha^2\lambda_n T_n(t)=Q_n(t) $$. Nghiệm của ODE này là

$$
T_n(t)=e^{-\alpha^2\lambda_n t}T_n(0)+\int_0^t e^{-\alpha^2\lambda_n(t-s)}Q_n(s)\,ds.
$$

Công thức này cho thấy mỗi mode hoạt động như một bộ lọc suy giảm mũ chịu tác động tích lũy của nguồn nhiệt.

### Ví dụ 4: Hành vi dài hạn của nghiệm

Nếu không có nguồn nhiệt phụ thuộc thời gian và điều kiện biên giữ cố định, thì $$ v(x,t)\to 0 $$ khi $$ t\to\infty $$, do đó $$ u(x,t)\to w(x) $$. Điều này giải thích lợi ích của việc tách riêng trạng thái cân bằng ngay từ đầu.

## Câu hỏi khái niệm

1. Vì sao phép tách $$ u=w+v $$ lại đặc biệt tự nhiên đối với bài toán nhiệt không thuần nhất?
2. Phần cân bằng và phần quá độ khác nhau như thế nào về mặt vật lý?
3. Khi có nguồn nhiệt, vì sao sự tiến hóa của mỗi mode không còn là hàm mũ suy giảm đơn thuần?

## Bài toán ứng dụng

1. Một thanh có hai đầu giữ ở hai mức nhiệt độ cố định khác nhau. Vì sao về lâu dài phân bố nhiệt độ tiến về dạng tuyến tính?
2. Nếu một nguồn nhiệt biến thiên tuần hoàn theo thời gian tác động lên thanh, các mode sẽ phản ứng như thế nào?
3. Trong kỹ thuật nhiệt, việc tách phần dừng và phần quá độ giúp phân tích hành vi dài hạn của hệ thuận lợi hơn ra sao?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Nếu hai đầu thanh được giữ ở hai nhiệt độ khác nhau, phân bố nhiệt độ sẽ tiến về dạng nào khi $$ t\to\infty $$?"
- Cho sinh viên tự tìm hàm cân bằng $$ w(x) $$ trước khi khái quát hóa thành kỹ thuật lifting.
- Đặt câu hỏi: "Sự có mặt của nguồn nhiệt làm thay đổi thành phần nào trong công thức từng mode?"
- Khuyến khích sinh viên diễn đạt bằng lời sự khác nhau giữa trạng thái cân bằng và phần quá độ tắt dần.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên rèn luyện một quy trình thao tác cố định: khử điều kiện biên không thuần nhất trước, đổi sang ẩn hàm mới, cập nhật điều kiện ban đầu, sau đó mới khai triển theo mode riêng. Quy trình nhất quán giúp giảm sai sót khi tính toán.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khảo sát trường hợp nguồn nhiệt phụ thuộc cả không gian lẫn thời gian, hoặc phân tích nguyên lý Duhamel như phiên bản liên tục của nguyên lý chồng chất theo thời gian.

## Tóm tắt dễ nhớ

Với bài toán nhiệt không thuần nhất, chiến lược chuẩn là tách nghiệm thành phần cân bằng và phần quá độ. Phần cân bằng hấp thụ điều kiện biên hoặc nguồn tĩnh, còn phần quá độ thỏa mãn biên thuần nhất và được giải bằng khai triển mode riêng.

## Video tham khảo

- Xem trước: [Solving PDEs with the Laplace Transform: The Heat Equation](https://www.youtube.com/watch?v=xuBJFSh6Bu4) — Steve Brunton, tiếng Anh. Trình bày cách giải bài toán nhiệt bằng biến đổi Laplace, một hướng tiếp cận khác cho dữ liệu không thuần nhất.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Ôn lại nghiệm bài toán thuần nhất làm nền cho bước hiệu chỉnh bằng trạng thái dừng hoặc khai triển hàm riêng.
- [The Heat Equation and the Steady State Heat Distribution via Laplace's Equation](https://www.youtube.com/watch?v=OoRwXVIXpL0) — Steve Brunton, tiếng Anh. Phân tích phân bố nhiệt dừng ứng với điều kiện biên không thuần nhất.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ biên thay đổi theo thời gian
- Bài toán: Hai đầu thanh chịu điều khiển bởi điều kiện nhiệt độ biên không thuần nhất.
- Mô hình: Tách nghiệm thành thành phần xử lý biên cộng phần biên thuần nhất:
$$ u(x,t)=v(x,t)+w(x,t). $$
- Giả thiết và giới hạn: Hàm phụ trợ $$ w $$ được chọn sao cho thỏa mãn điều kiện biên đã cho.
- Diễn giải: Phần phức tạp tại biên được hấp thụ vào hàm phụ trợ đơn giản hơn.

#### Nguồn nhiệt bên trong
- Bài toán: Hệ chịu tác động của một nguồn nhiệt cưỡng bức phân bố trong miền.
- Mô hình:
$$ u_t=\alpha^2 u_{xx}+f(x,t). $$
- Giả thiết và giới hạn: Hàm nguồn đủ trơn để áp dụng khai triển mode hoặc công thức Duhamel.
- Diễn giải: Nghiệm toàn phần gồm đáp ứng tự do và đáp ứng cưỡng bức.

### 2. Trực giác bổ sung và các kết nối

Bài toán không thuần nhất thường không đòi hỏi một phương pháp hoàn toàn mới; điểm chính là tách đúng phần xử lý biên hoặc nguồn. Một lỗi phổ biến là áp dụng trực tiếp cơ sở sin chuẩn cho bài toán biên không thuần nhất mà quên bước đổi biến trước.

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

Cho bài toán
$$ u_t=u_{xx},\qquad u(0,t)=0,\qquad u(1,t)=1. $$
Đặt
$$ w(x)=x,\qquad v(x,t)=u(x,t)-x. $$
Khi đó $$ v $$ thỏa mãn điều kiện biên thuần nhất
$$ v(0,t)=v(1,t)=0, $$
và phương trình cho $$ v $$ giải được trực tiếp bằng phương pháp tách biến chuẩn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phép tách nghiệm để đưa bài toán biên không thuần nhất về biên thuần nhất.

**Bậc sau đại học.** Liên hệ với nguyên lý Duhamel, nguyên lý chồng chất và lý thuyết nửa nhóm cho phương trình có vế phải.
