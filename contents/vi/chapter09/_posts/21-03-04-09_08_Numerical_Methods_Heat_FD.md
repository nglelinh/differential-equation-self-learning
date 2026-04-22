---
layout: post
title: "Phương Pháp Số: Sai Phân Hữu Hạn"
chapter: '09'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: optional
---
![21 03 04 09 08 Numerical Methods Heat Fd]({{ site.imgurl }}/chapter_img/chapter09/08_numerical_methods_heat_fd.svg)

## Mục tiêu

Bài học này giới thiệu cách rời rạc hóa phương trình nhiệt bằng sai phân hữu hạn. Sau bài học, sinh viên cần hiểu cách xây dựng lưới không gian-thời gian, biết suy ra sơ đồ explicit, implicit và Crank-Nicolson, hiểu trực giác điều kiện ổn định

$$ r\le \frac12 $$

cho sơ đồ tường minh, và thấy được vì sao phân tích số không chỉ là tính gần đúng mà còn là bài học về ổn định và tôn trọng cấu trúc của PDE.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt liên tục, xấp xỉ sai phân của đạo hàm, và trực giác về ổn định từ ODE số nếu có. Đây là bài rất thích hợp để nối phân tích PDE với mô phỏng thực hành.

## Dẫn nhập

Ngay cả khi đã có nghiệm lý thuyết, trong nhiều bài toán thực tế ta vẫn cần mô phỏng số. Dữ liệu có thể quá phức tạp để khai triển tường minh, miền có thể khó, hoặc ta chỉ cần một xấp xỉ nhanh. Phương pháp sai phân hữu hạn là lựa chọn nhập môn tự nhiên nhất cho phương trình nhiệt.

Nhưng bài này không chỉ dạy cách thay đạo hàm bằng hiệu. Nó còn cho sinh viên thấy một thông điệp sâu hơn: một mô hình số tốt phải tôn trọng bản chất của phương trình gốc. Với phương trình nhiệt, điều đó có nghĩa là phải ổn định, làm mượt, và không tạo dao động phi vật lý khi lưới được chọn hợp lý.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Ta thay một thanh liên tục bằng một dãy các nút, và thay thời gian liên tục bằng các bước nhảy nhỏ. Nhiệt tại một nút ở thời điểm kế tiếp được tính từ nhiệt hiện tại của nút đó và hai nút lân cận. Điều này phản ánh đúng trực giác vật lý: nhiệt lan ra nhờ tương tác cục bộ với hàng xóm gần nhất.

### Cách nhìn hình ảnh

Trên lưới sai phân, sơ đồ explicit cập nhật giá trị mới từ tầng thời gian cũ, nên dễ hình dung như "nhảy tới" từng bước. Sơ đồ implicit thì buộc ta giải cả tầng mới cùng lúc, giống như tìm một cấu hình tự-consistent mới. Crank-Nicolson nằm ở giữa: nó cân bằng giữa chính xác và ổn định.

### Cách nhìn hình thức

Chia đoạn $$ [0,L] $$ thành các nút

$$ x_j=j\Delta x,
\qquad
\Delta x=\frac{L}{N}, $$

và thời gian thành $$ t^n=n\Delta t $$. Xấp xỉ

$$
u_t\approx \frac{u_j^{n+1}-u_j^n}{\Delta t},
\qquad
u_{xx}\approx \frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{(\Delta x)^2}.
$$

Với

$$ r=\frac{\alpha^2\Delta t}{(\Delta x)^2}, $$

sơ đồ explicit là

$$ u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n). $$

## Những ngộ nhận thường gặp

- "Sai phân chỉ là thay đạo hàm bằng hiệu nên luôn đáng tin." Sai; còn phải xét ổn định và hội tụ.
- "Explicit dễ hơn nên tốt hơn." Không nhất thiết; nó có điều kiện ổn định nghiêm ngặt.
- "Nếu nghiệm thật mượt thì nghiệm số tự động mượt." Không đúng; chọn lưới sai có thể tạo dao động phi vật lý.
- "Implicit luôn tốt hơn mọi mặt." Không hẳn; nó ổn định hơn nhưng đòi hỏi giải hệ tuyến tính mỗi bước.

## Tiến trình học tập đề xuất

### Bước 1: Dựng lưới

Sinh viên phải rõ biến liên tục được thay bằng những gì.

### Bước 2: Suy ra các xấp xỉ sai phân

Không nên học thuộc sơ đồ trước khi hiểu chúng từ đâu ra.

### Bước 3: So sánh explicit và implicit

Đây là bước quan trọng về mặt tư duy số.

### Bước 4: Phân tích ổn định cơ bản

Giúp sinh viên thấy vì sao PDE và mô phỏng số phải "khớp tính cách".

### Các checkpoint

- Sinh viên có viết đúng sơ đồ explicit từ xấp xỉ đạo hàm hay không.
- Sinh viên có hiểu ý nghĩa của tham số

$$ r $$

hay không.
- Sinh viên có phân biệt được ưu nhược của explicit, implicit, và Crank-Nicolson hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Sơ đồ explicit

Với $$ u_t=\alpha^2u_{xx} $$, ta thay các xấp xỉ sai phân và được

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\alpha^2\frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{(\Delta x)^2}.
$$

Suy ra $$ u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n) $$. Ví dụ này nên được dạy như khuôn mẫu đầu tiên của cả bài.

### Ví dụ 2: Điều kiện ổn định

Phân tích von Neumann cho sơ đồ explicit dẫn tới hệ số khuếch đại

$$ \xi=1-4r\sin^2\left(\frac{\theta}{2}\right). $$

Để $$ \lvert \xi\rvert\le 1 $$ với mọi $$ \theta $$, cần

$$ r\le \frac12. $$

Ví dụ này rất quan trọng vì nó cho thấy bước thời gian không được chọn tùy ý.

### Ví dụ 3: Sơ đồ implicit

Sơ đồ lùi Euler là

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\alpha^2\frac{u_{j+1}^{n+1}-2u_j^{n+1}+u_{j-1}^{n+1}}{(\Delta x)^2}.
$$

Sau khi thu gọn:

$$
-r u_{j-1}^{n+1}+(1+2r)u_j^{n+1}-r u_{j+1}^{n+1}=u_j^n.
$$

Ta phải giải một hệ tam đường chéo ở mỗi bước thời gian. Đổi lại, sơ đồ này ổn định hơn nhiều.

### Ví dụ 4: Crank-Nicolson

Crank-Nicolson lấy trung bình giữa explicit và implicit:

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\frac{\alpha^2}{2(\Delta x)^2}
\Bigl[(u_{j+1}^{n+1}-2u_j^{n+1}+u_{j-1}^{n+1})
+
(u_{j+1}^n-2u_j^n+u_{j-1}^n)\Bigr].
$$

Ví dụ này nên được dùng để nhấn mạnh sự đánh đổi giữa độ chính xác và độ phức tạp tính toán.

## Câu hỏi khái niệm

1. Vì sao sơ đồ explicit cho phương trình nhiệt cần điều kiện ổn định nghiêm ngặt?
2. Điều gì làm cho sơ đồ implicit đáng tin cậy hơn về ổn định?
3. Vì sao một mô phỏng số tốt nên phản ánh đúng bản chất làm mượt của phương trình nhiệt?

## Bài toán ứng dụng

1. Trong mô phỏng truyền nhiệt của một thanh dài, vì sao chọn $$ \Delta t $$ quá lớn có thể làm nghiệm số nổ dù nghiệm thật rất mượt?
2. Trong kỹ thuật tính toán, khi nào nên chấp nhận giải hệ tuyến tính mỗi bước để đổi lấy ổn định tốt hơn?
3. Trong đồ họa hoặc xử lý ảnh, vì sao khuếch tán số được xem như một phép lọc làm mượt và tại sao ổn định lại quan trọng?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự suy ra sơ đồ explicit từ xấp xỉ đạo hàm thay vì đưa công thức sẵn.
- Hỏi cả lớp: "Nếu nhiệt thật luôn làm mượt, vì sao nghiệm số lại có thể dao động?"
- Dùng một bảng so sánh explicit, implicit, Crank-Nicolson về chi phí, ổn định, và độ chính xác.
- Nếu có thể, cho sinh viên mô phỏng nhanh một trường hợp ổn định và một trường hợp không ổn định để trực giác trở nên rất rõ.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào sơ đồ explicit trước, vì nó cho cảm giác "cập nhật cục bộ" rất trực quan. Khi ý tưởng đó đã vững, mới chuyển sang implicit và Crank-Nicolson.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tự thực hiện phân tích von Neumann đầy đủ, hoặc so sánh tính ổn định năng lượng của các sơ đồ khác nhau.

## Tóm tắt dễ nhớ

Sai phân hữu hạn biến phương trình nhiệt thành bài toán lưới không gian-thời gian. Explicit dễ cài nhưng bị ràng buộc bởi

$$ r\le \frac12, $$

implicit ổn định hơn nhưng tốn công giải hệ, còn Crank-Nicolson cân bằng giữa ổn định và độ chính xác. Sơ đồ số tốt phải tôn trọng tính làm mượt của phương trình nhiệt.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mô phỏng nhiệt trên máy tính
- Bài toán: Cần tính gần đúng nghiệm khi không có công thức tường minh thuận tiện.
- Mô hình sai phân hiện:
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right).
$$
- Giả thiết và giới hạn: Lưới đều, miền một chiều, điều kiện ổn định kiểu CFL.
- Diễn giải: Sơ đồ số bắt chước tính làm phẳng của phương trình nhiệt.

#### Phương pháp implicit trong kỹ thuật
- Bài toán: Muốn bước thời gian lớn hơn mà vẫn ổn định.
- Mô hình: Backward Euler hoặc Crank-Nicolson cho phương trình nhiệt.
- Giả thiết và giới hạn: Phải giải hệ tuyến tính ở mỗi bước.
- Diễn giải: Đổi chi phí đại số để lấy ổn định tốt hơn.

### 2. Trực giác bổ sung và các kết nối

Phương pháp sai phân hữu hạn cho phương trình nhiệt cho thấy rõ mối quan hệ giữa PDE liên tục và mô hình lưới rời rạc. Một bẫy phổ biến là nghĩ chỉ cần rời rạc hóa xong là đúng; thật ra ổn định và hội tụ là điều phải kiểm tra cẩn thận.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

Nx = 80
dx = 1 / Nx
r = 0.45
dt = r * dx**2
x = np.linspace(0, 1, Nx + 1)
u = np.sin(np.pi * x)

snapshots = [u.copy()]
for _ in range(80):
    un = u.copy()
    u[1:-1] = un[1:-1] + r * (un[2:] - 2 * un[1:-1] + un[:-2])
    snapshots.append(u.copy())

for idx in [0, 10, 40, 80]:
    plt.plot(x, snapshots[idx], label=f"step {idx}")
plt.xlabel("x")
plt.ylabel("u")
plt.title("Sai phan huu han cho phuong trinh nhiet")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: finite difference heat equation stability animation
- search: explicit implicit heat equation comparison
- search: CFL condition heat equation visualization

### 5. Bài toán mẫu có bối cảnh thực

Với sơ đồ explicit,
$$ r=\frac{\alpha^2 \Delta t}{(\Delta x)^2}, $$
điều kiện ổn định cổ điển là
$$ r\le \frac{1}{2}. $$
Nếu chọn $$ r $$ quá lớn, nghiệm số có thể bùng nổ dù nghiệm thật rất trơn. Đây là ví dụ điển hình cho tầm quan trọng của phân tích ổn định.

### 6. Phân tầng độ khó

**Bậc đại học.** Cài đặt sơ đồ explicit cơ bản và hiểu điều kiện ổn định.

**Bậc sau đại học.** Phân tích Von Neumann, so sánh explicit/implicit, và bàn về consistency-stability-convergence.
