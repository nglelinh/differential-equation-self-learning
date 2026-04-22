---
layout: post
title: "Sai Phân Hữu Hạn Cho PDEs"
chapter: '13'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Lưới sai phân cho PDE và xấp xỉ đạo hàm cục bộ]({{ site.imgurl }}/chapter_img/chapter13/05_finite_differences_pdes.svg )

## Mục tiêu

Bài học này giúp sinh viên hiểu phương pháp sai phân hữu hạn như bước rời rạc hóa cơ bản của PDE. Sau bài học, sinh viên cần xây dựng được các công thức sai phân trung tâm đơn giản, áp dụng được cho phương trình nhiệt, sóng, và Laplace, và hiểu cách một PDE liên tục biến thành hệ đại số trên lưới.

## Kiến thức nền

Sinh viên nên nắm đạo hàm riêng, Taylor, và trực giác về lưới không gian-thời gian. Từ các chương trước, sinh viên đã quen với PDE liên tục; bài này cho thấy cách đưa chúng lên máy tính.

## Dẫn nhập

Máy tính không làm việc trên cả một miền liên tục vô hạn điểm. Nó chỉ làm việc với hữu hạn nút lưới. Vì vậy, bước đầu tiên của tính toán PDE là thay miền liên tục bằng một mạng điểm và thay đạo hàm bằng hiệu giữa các giá trị lân cận. Sai phân hữu hạn chính là ngôn ngữ của bước thay thế đó.

Điểm đáng chú ý là đây không chỉ là thao tác cơ học. Cách chọn công thức sai phân quyết định độ chính xác, ổn định, và cả việc sơ đồ số có giữ được tính chất vật lý của PDE hay không.

## Khái niệm theo ba cách

### Cách trực giác

Nếu muốn đo độ dốc của một con đường nhưng chỉ biết độ cao tại vài cọc mốc, bạn sẽ lấy chênh lệch độ cao chia cho khoảng cách. Sai phân hữu hạn chính là ý tưởng đó: đạo hàm được xấp xỉ bằng chênh lệch cục bộ.

### Cách hình ảnh

Vẽ một lưới đều $$ x_i=ih $$ và các nút $$ u_{i-1},u_i,u_{i+1} $$. Từ ba nút liên tiếp ấy, sinh viên sẽ thấy $$ u_x $$ được xấp xỉ bằng chênh lệch lệch tâm, còn $$ u_{xx} $$ được xấp xỉ bằng việc đo độ cong cục bộ qua ba điểm.

### Cách hình thức

Trên lưới đều,

$$ u_x(x_i)\approx \frac{u_{i+1}-u_{i-1}}{2h}, $$

và

$$
u_{xx}(x_i)\approx \frac{u_{i+1}-2u_i+u_{i-1}}{h^2}.
$$

Áp dụng vào phương trình nhiệt $$ u_t=\alpha^2u_{xx} $$, ta thu được sơ đồ tường minh cơ bản

$$
\frac{u_i^{n+1}-u_i^n}{\Delta t}
=
\alpha^2\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{h^2}.
$$

## Ngộ nhận thường gặp

### “Chỉ cần thay đạo hàm bằng sai phân là xong”

Sai. Sau đó còn phải kiểm tra tính nhất quán, ổn định, điều kiện biên, và hội tụ.

### “Lưới càng dày thì luôn tốt”

Không hoàn toàn. Lưới dày hơn tăng chi phí tính toán và có thể đòi hỏi bước thời gian nhỏ hơn.

### “Sai phân hữu hạn chỉ phù hợp cho ODE”

Sai. Đây là một trong những công cụ cổ điển mạnh nhất cho PDE.

### “Công thức trung tâm luôn là lựa chọn tốt nhất trong mọi bài toán”

Không. Đối với bài toán đối lưu hay sóng, lựa chọn sai phân còn gắn với định hướng truyền thông tin và ổn định.

## Tiến trình học

### Bước 1: Xây công thức sai phân từ Taylor

Sinh viên cần thấy các công thức không được đoán mò.

### Bước 2: Lưới hóa miền

Giải thích rõ chỉ số không gian $$ i $$ và thời gian $$ n $$.

### Bước 3: Áp dụng vào PDE mẫu

Nên bắt đầu với nhiệt và Laplace trước.

### Bước 4: Dẫn sang ổn định

Ngay khi có sơ đồ, câu hỏi tiếp theo phải là: nó có đáng tin không?

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự suy ra được sai phân cho $$ u_x $$ và $$ u_{xx} $$ không?
- Sinh viên có đọc được ý nghĩa của chỉ số $$ u_i^n $$ không?
- Sinh viên có hiểu vì sao PDE sau rời rạc hóa trở thành hệ đại số không?

## Ví dụ có lời giải

### Ví dụ 1: Sai phân bậc nhất

Với hàm một biến, từ Taylor ta có $$ u(x+h)=u(x)+hu'(x)+O(h^2) $$. Suy ra

$$ u'(x)\approx \frac{u(x+h)-u(x)}{h}. $$

Đây là sai phân tiến bậc một.

### Ví dụ 2: Sai phân trung tâm cho đạo hàm bậc hai

Từ hai khai triển

$$ u(x+h)=u(x)+hu'(x)+\frac{h^2}{2}u''(x)+O(h^3), $$

$$ u(x-h)=u(x)-hu'(x)+\frac{h^2}{2}u''(x)+O(h^3), $$

cộng lại được

$$ u''(x)\approx \frac{u(x+h)-2u(x)+u(x-h)}{h^2}. $$

### Ví dụ 3: Laplace một chiều

Xét $$ -u''=f $$ trên lưới nội suy một chiều. Khi đó tại nút $$ i $$:

$$ -\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}=f_i. $$

Thu được hệ tuyến tính tam đường chéo, rất thuận lợi để giải.

### Ví dụ 4: Sơ đồ cho phương trình nhiệt

Với sơ đồ tường minh,

$$
u_i^{n+1}=u_i^n+r\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\right),
\qquad
r=\frac{\alpha^2\Delta t}{h^2}.
$$

Viết theo dạng cập nhật này, sinh viên dễ thấy giá trị mới là tổ hợp của các nút lân cận hiện tại.

## Câu hỏi khái niệm

1. Vì sao đạo hàm bậc hai lại gắn tự nhiên với công thức ba điểm?
2. Khi rời rạc hóa PDE, điều gì bị mất và điều gì được giữ lại?
3. Vì sao cùng một công thức sai phân nhưng cách dùng trong nhiệt và sóng lại dẫn tới hành vi số khác nhau?

## Bài toán ứng dụng

1. Trong mô hình truyền nhiệt trên một thanh, lưới hóa giúp chuyển PDE thành bài toán tính toán như thế nào?
2. Trong kỹ thuật kết cấu, vì sao hệ tam đường chéo là tin vui về mặt tính toán?
3. Trong mô phỏng ô nhiễm không khí, việc tinh chỉnh lưới ảnh hưởng thế nào tới chi phí và độ phân giải?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu chỉ biết giá trị tại vài nút, em sẽ đo độ dốc thế nào?
- Vì sao ba điểm là đủ để bắt độ cong cục bộ?
- Khi chia lưới dày hơn, em mong đợi điều gì thay đổi?

### Hoạt động gợi ý

- Cho sinh viên tự suy ra công thức sai phân từ Taylor theo nhóm.
- Dùng giấy ô vuông để biểu diễn lưới không gian-thời gian.
- So sánh trực tiếp nghiệm giải tích và nghiệm sai phân trên một ví dụ đơn giản.

### Cách tăng tham gia

- Bắt đầu bằng bài toán “đo độ dốc từ các cọc mốc”.
- Mời sinh viên lên bảng điền các nút lân cận vào công thức.
- Cho mỗi nhóm xử lý một PDE khác nhau: nhiệt, sóng, Laplace.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Chỉ làm một chiều trước.
- Tập trung vào công thức ba điểm.
- Dùng nhiều hình lưới hơn công thức dài.

### Thử thách cho sinh viên khá giỏi

- Suy ra sai số cắt cụt của các sai phân.
- Mở rộng sang lưới hai chiều cho Laplace.
- So sánh finite differences với finite elements về hình học và dạng yếu.

## Ghi nhớ nhanh

Sai phân hữu hạn thay đạo hàm bằng chênh lệch giữa các nút lưới, nhờ đó biến PDE thành hệ đại số. Đây là cầu nối cơ bản từ mô hình liên tục sang mô phỏng trên máy tính.

---

## Ứng dụng thực tế

### 1. Truyền nhiệt trong thanh và bản mỏng

Phương trình nhiệt $$ u_t=\alpha^2 u_{xx} $$ là mô hình cổ điển của dẫn nhiệt. Sai phân hữu hạn cho phép tính gần đúng nhiệt độ tại từng nút lưới theo thời gian. Mô hình giả định hệ số khuếch tán đồng nhất và hình học đơn giản. Diễn giải là: PDE liên tục được thay bằng quy tắc cập nhật cục bộ giữa các nút láng giềng.

### 2. Điện thế và bài toán Poisson/Laplace

Trong điện tĩnh hoặc cân bằng nhiệt, phương trình Poisson/Laplace sau khi rời rạc hóa tạo ra hệ tuyến tính thưa. Đây là lý do finite differences rất hấp dẫn cho miền hình chữ nhật hoặc hộp đơn giản. Giới hạn là miền cong hoặc lỗ phức tạp làm lưới đều kém linh hoạt.

### 3. Mô phỏng sóng và đối lưu

Với phương trình sóng hoặc đối lưu, việc chọn công thức sai phân không chỉ ảnh hưởng độ chính xác mà còn quyết định hướng lan truyền thông tin và ổn định. Đây là nơi sinh viên thấy finite differences gắn trực tiếp với vật lý truyền thông tin chứ không chỉ là đại số chênh lệch.

## Trực giác sâu hơn

Sai phân hữu hạn thành công vì nó thay bài toán vô hạn chiều bằng những tương tác cục bộ rất cụ thể: mỗi nút mới được quyết định bởi một mẫu lân cận nhỏ. Nhưng sự đơn giản đó cũng là giới hạn: lưới, điều kiện biên, và hình học có thể ảnh hưởng rất mạnh tới chất lượng mô phỏng. Ngộ nhận phổ biến là coi rời rạc hóa như thao tác máy móc; thực ra đây là bước mô hình hóa số đầy lựa chọn.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

nx = 80
nt = 200
L = 1.0
T = 0.08
alpha = 1.0
dx = L / (nx - 1)
dt = T / nt
r = alpha**2 * dt / dx**2

x = np.linspace(0, L, nx)
u = np.sin(np.pi * x)
snapshots = [u.copy()]

for n in range(nt):
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + r * (u[2:] - 2*u[1:-1] + u[:-2])
    u_new[0] = 0.0
    u_new[-1] = 0.0
    u = u_new
    if n in [0, 20, 80, 160]:
        snapshots.append(u.copy())

plt.figure(figsize=(9, 5))
for k, snap in enumerate(snapshots):
    plt.plot(x, snap, label=f'snapshot {k}')
plt.title('Sai phân hữu hạn cho phương trình nhiệt 1D')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để tạo heatmap thời gian-không gian của phương trình nhiệt hoặc sóng, giúp sinh viên nhìn trực tiếp sự lan truyền và làm mượt trên lưới.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `finite difference heat equation visualization`, `five point stencil animation`, hoặc `PDE grid discretization`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Sai phân hữu hạn cho phương trình nhiệt" description="Heatmap thời gian-không gian của sơ đồ nhiệt explicit, cho phép thay đổi hệ số r để quan sát sự chuyển từ làm mượt sang mất ổn định." path="interactives/chapter13/finite-differences-pde-vi.html" height="660px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào công thức ba điểm, lưới đều, và các PDE mẫu như nhiệt, sóng, Laplace trong một chiều hoặc hình chữ nhật đơn giản.

### Mức sau đại học (Graduate)

Đi sâu vào sai số cắt cụt, ma trận thưa, phân tích phổ của toán tử rời rạc, và mối liên hệ giữa stencil, consistency, stability, convergence.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phương trình nhiệt
- Bài toán: Xấp xỉ
$$ u_t=\alpha u_{xx} $$
trên lưới rời rạc để mô phỏng truyền nhiệt.
- Mô hình: Dùng sai phân trung tâm cho $$ u_{xx} $$ và Euler tiến/lùi theo thời gian.
- Giả thiết và giới hạn: Lưới đều; sai số và ổn định phụ thuộc vào $$ \Delta t $$ và $$ \Delta x $$.
- Diễn giải: PDE liên tục được biến thành hệ tuyến tính lớn theo thời gian.

#### Dao động hoặc sóng trên dây
- Bài toán: Theo dõi biên độ tại các nút lưới cho phương trình sóng.
- Mô hình: Dùng công thức sai phân hữu hạn cho đạo hàm thời gian và không gian.
- Giả thiết và giới hạn: Dễ sinh phản xạ số hoặc mất ổn định nếu lưới không phù hợp.
- Diễn giải: Finite differences là cầu nối trực tiếp nhất từ PDE sang thuật toán.

### 2. Trực giác bổ sung và các kết nối

Sai phân hữu hạn thay mọi đạo hàm bằng chênh lệch giữa các nút lưới gần nhau. Điều này tạo ra một phiên bản "vi mô rời rạc" của PDE. Một bẫy phổ biến là tin rằng công thức đúng cục bộ là đủ; với PDE, điều kiện biên và ổn định toàn cục mới quyết định chất lượng mô phỏng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

nx = 80
x = np.linspace(0, 1, nx)
dx = x[1] - x[0]
dt = 0.4 * dx**2
r = dt / dx**2
u = np.sin(np.pi * x)

for _ in range(120):
    un = u.copy()
    u[1:-1] = un[1:-1] + r * (un[2:] - 2 * un[1:-1] + un[:-2])
    u[0] = 0.0
    u[-1] = 0.0

plt.plot(x, np.sin(np.pi * x), label="ban dau")
plt.plot(x, u, label="sau nhieu buoc")
plt.legend()
plt.title("Sai phan huu han cho phuong trinh nhiet")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: finite difference heat equation animation
- search: wave equation finite difference grid visualization
- search: PDE stencil intuition

### 5. Bài toán mẫu có bối cảnh thực

Với lược đồ explicit cho phương trình nhiệt,
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right),
$$
trong đó
$$ r=\frac{\alpha \Delta t}{\Delta x^2}. $$
Ý nghĩa vật lý là nhiệt độ mới tại nút $$ j $$ bằng giá trị cũ cộng với hiệu ứng khuếch tán từ hai nút lân cận.

### 6. Phân tầng độ khó

**Bậc đại học.** Dựng stencil sai phân và lập trình lược đồ đơn giản.

**Bậc sau đại học.** Kết nối với consistency, matrix form và dispersion/dissipation số.
