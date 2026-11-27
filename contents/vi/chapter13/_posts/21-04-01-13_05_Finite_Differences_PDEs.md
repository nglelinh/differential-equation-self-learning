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

![Lưới sai phân cho PDE và xấp xỉ đạo hàm cục bộ]({{ site.imgurl }}/chapter_img/chapter13/05_finite_differences_pdes.svg)

Làm sao dạy máy tính giải phương trình Poisson $-\Delta u = f$ hay phương trình nhiệt $u_t = \alpha u_{xx}$ khi máy tính chỉ hiểu mảng số hữu hạn? **Phương pháp Sai phân Hữu hạn (Finite Difference Method — FDM)** phủ lên miền $\Omega$ một mạng lưới tọa độ bước $h$, thay mọi đạo hàm riêng bằng tổ hợp tuyến tính của vài nút lân cận (*stencil*), và biến PDE vô hạn chiều thành một **hệ phương trình đại số tuyến tính $A\mathbf{u} = \mathbf{b}$** có ma trận cực thưa!

## Kiến thức cần nhớ: Bốn trụ cột của Sai phân Hữu hạn cho PDE

1. **Xây dựng Stencil 3 điểm (1D) và 5 điểm (2D) cho Toán tử Laplace**:
   Thay $u_{xx} \approx \frac{u_{i-1} - 2u_i + u_{i+1}}{h^2}$ ở 1D và cộng thêm chiều $y$ cho stencil 5 điểm 2D đạt bậc chính xác $O(h^2)$.
2. **Cấu trúc Ma trận Thưa (Tam đường chéo / Khối tam đường chéo)**:
   Mỗi phương trình chỉ dính đến $3$ (ở 1D) hoặc $5$ (ở 2D) ẩn số! Nhờ tính thưa và đối xứng xác định dương (SPD), ta giải $A\mathbf{u} = \mathbf{b}$ siêu nhanh bằng thuật toán Thomas $O(N)$ ở 1D hoặc Conjugate Gradient / Multigrid ở 2D–3D.
3. **Ba sơ đồ kinh điển cho PDE Tiến hóa theo Thời gian**:
   - *FTCS (Hiện)*: dễ lập trình nhưng bị trói bởi điều kiện $r = \alpha\Delta t/\Delta x^2 \le 1/2$.
   - *BTCS (Ẩn)*: ổn định vô điều kiện, bậc $O(\Delta t + \Delta x^2)$.
   - *Crank–Nicolson*: lấy trung bình bước cũ và mới, vừa ổn định vô điều kiện vừa đạt bậc hai cả thời gian lẫn không gian $O(\Delta t^2 + \Delta x^2)$!
4. **Xử lý Điều kiện biên Dirichlet và Neumann (Nút Ảo — Ghost Nodes)**:
   Biên Dirichlet thay thẳng giá trị đã biết sang vế phải $\mathbf{b}$; biên Neumann $u_x(0) = g$ dùng nút ảo $u_{-1}$ với sai phân trung tâm $\frac{u_1 - u_{-1}}{2h} = g$ để giữ nguyên độ chính xác bậc $O(h^2)$!

## Mục tiêu

Bài học này giới thiệu phương pháp sai phân hữu hạn (finite difference method) như bước rời rạc hóa cơ bản cho PDE. Sau bài học, sinh viên cần xây dựng được các công thức sai phân trung tâm cơ bản, áp dụng cho phương trình nhiệt, phương trình sóng và phương trình Laplace, đồng thời hiểu cách một PDE liên tục chuyển thành hệ phương trình đại số trên lưới.

## Kiến thức nền

Sinh viên cần nắm đạo hàm riêng, khai triển Taylor và khái niệm lưới không gian–thời gian. Sau khi đã khảo sát PDE liên tục ở các chương trước, bài học này chỉ ra cách đưa chúng vào tính toán số.

## Dẫn nhập

Máy tính không xử lý trực tiếp miền liên tục vô hạn điểm mà chỉ tính toán trên hữu hạn nút lưới. Do đó, bước đầu tiên trong giải số PDE là thay miền liên tục bằng một lưới điểm và thay các đạo hàm bằng hiệu giữa giá trị tại các nút lân cận. Phương pháp sai phân hữu hạn cung cấp khung công thức trực tiếp cho bước chuyển đổi đó.

Việc lựa chọn công thức sai phân không chỉ là thao tác hình thức: nó quyết định bậc chính xác, tính ổn định và khả năng bảo toàn tính chất vật lý của PDE gốc.


### Giải thích: Giải tay trọn vẹn hệ ma trận sai phân 3 điểm cho $-u'' = 2$ trên $(0, 1)$

Chia đoạn $[0, 1]$ thành $3$ đoạn bằng nhau ($h = \frac{1}{3}$), có 2 nút trong $x_1 = \frac{1}{3}$, $x_2 = \frac{2}{3}$ và biên $u_0 = u_3 = 0$:
1. **Viết phương trình sai phân $\frac{-u_{i-1} + 2u_i - u_{i+1}}{h^2} = 2$** (với $1/h^2 = 9$):
   - Tại $i = 1$: $9(0 + 2u_1 - u_2) = 2 \implies 2u_1 - u_2 = \frac{2}{9}$.
   - Tại $i = 2$: $9(-u_1 + 2u_2 - 0) = 2 \implies -u_1 + 2u_2 = \frac{2}{9}$.
2. **Giải hệ $2 \times 2$ đối xứng**:
   Cộng hai phương trình: $u_1 + u_2 = \frac{4}{9}$. Do đối xứng $u_1 = u_2$, suy ra:
   $$u_1 = u_2 = \mathbf{\frac{2}{9}} \approx 0{,}2222.$$
3. **Kiểm chứng với nghiệm giải tích $u(x) = x(1 - x)$**:
   $u\left(\frac{1}{3}\right) = \frac{1}{3}\cdot\frac{2}{3} = \mathbf{\frac{2}{9}}$ và $u\left(\frac{2}{3}\right) = \mathbf{\frac{2}{9}}$—**sai số bằng $0$ tuyệt đối** vì sai phân trung tâm $O(h^2)$ có phần dư chứa $u^{(4)}$, mà $u^{(4)} \equiv 0$ cho đa thức bậc hai!
## Khái niệm theo ba cách

### Cách trực giác

Nếu muốn ước lượng độ dốc của một con đường khi chỉ biết độ cao tại các cọc mốc cách đều nhau, ta lấy hiệu độ cao chia cho khoảng cách giữa hai cọc. Sai phân hữu hạn áp dụng đúng ý tưởng đó: xấp xỉ đạo hàm bằng tỷ số chênh lệch cục bộ giữa các nút lưới.

### Cách hình ảnh

Trên lưới đều $$ x_i=ih $$ với ba nút liên tiếp $$ u_{i-1},u_i,u_{i+1} $$, đạo hàm bậc nhất $$ u_x $$ được xấp xỉ bằng sai phân trung tâm qua hai nút lân cận $$ u_{i-1} $$ và $$ u_{i+1} $$, còn đạo hàm bậc hai $$ u_{xx} $$ đo độ cong cục bộ dựa trên cả ba điểm.

### Cách hình thức

Trên lưới đều bước $$ h $$,

$$ u_x(x_i)\approx \frac{u_{i+1}-u_{i-1}}{2h}, $$

và

$$
u_{xx}(x_i)\approx \frac{u_{i+1}-2u_i+u_{i-1}}{h^2}.
$$

Áp dụng cho phương trình nhiệt $$ u_t=\alpha^2u_{xx} $$, ta thu được lược đồ tường minh cơ bản:

$$
\frac{u_i^{n+1}-u_i^n}{\Delta t}
=
\alpha^2\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{h^2}.
$$

## Ngộ nhận thường gặp

### “Chỉ cần thay đạo hàm bằng sai phân là giải xong bài toán”

Sai. Sau khi lập lược đồ, ta còn phải kiểm tra tính nhất quán, tính ổn định, xử lý điều kiện biên và sự hội tụ.

### “Chia lưới càng mịn thì kết quả luôn tốt hơn ngay lập tức”

Chưa hẳn. Lưới mịn hơn làm tăng chi phí tính toán và với lược đồ tường minh còn kéo theo yêu cầu bước thời gian $$ \Delta t $$ nhỏ hơn nhiều (thậm chí giảm theo $$ h^2 $$ ở phương trình nhiệt).

### “Sai phân hữu hạn chỉ dùng cho ODE”

Sai. Đây là một trong những phương pháp cổ điển phổ biến nhất để giải số PDE.

### “Sai phân trung tâm luôn là lựa chọn tối ưu cho mọi PDE”

Không đúng. Với bài toán đối lưu hoặc sóng, cần chọn sai phân phù hợp với hướng truyền thông tin (như lược đồ upwind) để đảm bảo ổn định.

## Tiến trình học

### Bước 1: Dẫn xuất công thức sai phân từ khai triển Taylor

Đảm bảo sinh viên hiểu nguồn gốc và sai số cắt cụt của từng công thức.

### Bước 2: Thiết lập lưới không gian–thời gian

Làm rõ ý nghĩa của chỉ số không gian $$ i $$ và chỉ số thời gian $$ n $$ trong ký hiệu $$ u_i^n $$.

### Bước 3: Áp dụng vào các PDE mẫu

Bắt đầu từ phương trình Laplace 1D và phương trình nhiệt 1D trước khi mở rộng.

### Bước 4: Dẫn sang bài toán ổn định

Đặt câu hỏi liệu lược đồ vừa lập có giữ được sai số trong tầm kiểm soát hay không.

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự dẫn xuất được công thức sai phân cho $$ u_x $$ và $$ u_{xx} $$ hay không?
- Sinh viên có đọc đúng ý nghĩa chỉ số của $$ u_i^n $$ hay không?
- Sinh viên có hiểu vì sao PDE sau khi rời rạc hóa trở thành một hệ phương trình đại số hay không?

## Ví dụ có lời giải

### Ví dụ 1: Sai phân tiến bậc nhất

Từ khai triển Taylor $$ u(x+h)=u(x)+hu'(x)+O(h^2) $$, ta suy ra:

$$ u'(x)\approx \frac{u(x+h)-u(x)}{h}. $$

Đây là công thức sai phân tiến có độ chính xác bậc một.

### Ví dụ 2: Sai phân trung tâm cho đạo hàm bậc hai

Từ hai khai triển:

$$ u(x+h)=u(x)+hu'(x)+\frac{h^2}{2}u''(x)+O(h^3), $$

$$ u(x-h)=u(x)-hu'(x)+\frac{h^2}{2}u''(x)+O(h^3), $$

cộng hai vế lại ta thu được công thức sai phân trung tâm cho đạo hàm bậc hai:

$$ u''(x)\approx \frac{u(x+h)-2u(x)+u(x-h)}{h^2}. $$

### Ví dụ 3: Phương trình Poisson một chiều

Xét $$ -u''=f $$ trên lưới đều một chiều. Tại mỗi nút trong $$ i $$:

$$ -\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}=f_i. $$

Hệ phương trình thu được có ma trận tam đường chéo, cho phép giải rất nhanh.

### Ví dụ 4: Lược đồ tường minh cho phương trình nhiệt

Viết lại lược đồ nhiệt dưới dạng cập nhật:

$$
u_i^{n+1}=u_i^n+r\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\right),
\qquad
r=\frac{\alpha^2\Delta t}{h^2}.
$$

Dạng này cho thấy trực tiếp giá trị tại bước thời gian mới là tổ hợp tuyến tính của nút hiện tại và hai nút lân cận.

## Câu hỏi khái niệm

1. Vì sao đạo hàm bậc hai gắn tự nhiên với mẫu sai phân ba điểm?
2. Khi rời rạc hóa PDE bằng sai phân hữu hạn, những thông tin nào được giữ lại và những gì bị xấp xỉ?
3. Vì sao cùng là công thức sai phân trung tâm nhưng áp dụng cho phương trình nhiệt và phương trình đối lưu lại cho tính chất ổn định khác nhau?

## Bài toán ứng dụng

1. Trong bài toán dẫn nhiệt trên một thanh, việc chia lưới chuyển PDE thành thuật toán cập nhật từng bước như thế nào?
2. Trong tính toán kết cấu, vì sao ma trận tam đường chéo (hoặc ma trận thưa có dải) lại mang lại lợi thế lớn về tốc độ giải?
3. Trong mô phỏng khuếch tán ô nhiễm không khí, việc làm mịn lưới ảnh hưởng ra sao đến độ phân giải và chi phí tính toán?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu chỉ biết giá trị hàm tại các nút lưới, làm sao ước lượng độ dốc và độ cong?
- Vì sao cần ít nhất ba điểm để xấp xỉ đạo hàm bậc hai?
- Khi giảm bước lưới $$ h $$ đi một nửa, điều gì thay đổi về độ chính xác và chi phí?

### Hoạt động gợi ý

- Cho sinh viên làm việc nhóm để tự suy ra sai phân trung tâm bậc một và bậc hai từ khai triển Taylor.
- Vẽ lưới không gian–thời gian để trực quan hóa mẫu sai phân (stencil) của phương trình nhiệt.
- Đối chiếu nghiệm giải tích và nghiệm sai phân trên một bài toán nhiệt 1D đơn giản.

### Cách tăng tham gia

- Mở đầu bằng hình ảnh ước lượng độ dốc con đường qua các cọc mốc.
- Mời sinh viên tự điền hệ số các nút lân cận vào mẫu sai phân trên bảng.
- Phân công mỗi nhóm lập sơ đồ rời rạc cho một PDE khác nhau: nhiệt, sóng hoặc Laplace.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm kỹ bài toán một chiều trước khi chuyển sang hai chiều.
- Tập trung nắm chắc mẫu sai phân ba điểm cho $$ u_{xx} $$.
- Sử dụng sơ đồ lưới minh họa trực quan song song với công thức.

### Thử thách cho sinh viên khá giỏi

- Tính chính xác sai số cắt cụt của các công thức sai phân tiến, lùi và trung tâm.
- Mở rộng sang mẫu năm điểm (five-point stencil) cho phương trình Laplace hai chiều.
- So sánh phương pháp sai phân hữu hạn với phương pháp phần tử hữu hạn về tính linh hoạt hình học và dạng yếu.

## Ghi nhớ nhanh

Phương pháp sai phân hữu hạn thay các đạo hàm riêng bằng hiệu giữa các giá trị tại nút lưới lân cận, biến PDE thành hệ phương trình đại số. Đây là bước chuyển trực tiếp từ mô hình PDE liên tục sang mô phỏng trên máy tính.

---

## Ứng dụng thực tế

### 1. Truyền nhiệt trong thanh và bản mỏng

Với phương trình nhiệt $$ u_t=\alpha^2 u_{xx} $$ trên hình học đơn giản và hệ số khuếch tán đồng nhất, sai phân hữu hạn chuyển PDE thành quy tắc cập nhật cục bộ giữa các nút lân cận theo thời gian.

### 2. Tĩnh điện và bài toán Poisson/Laplace

Rời rạc hóa phương trình Poisson/Laplace trên miền hình chữ nhật hoặc hình hộp tạo ra hệ tuyến tính thưa rất gọn. Hạn chế chính là khi miền có biên cong hoặc lỗ phức tạp, lưới đều kém linh hoạt hơn phương pháp phần tử hữu hạn.

### 3. Mô phỏng sóng và đối lưu

Trong các bài toán lan truyền sóng hoặc đối lưu, việc chọn sai phân không chỉ quyết định độ chính xác mà còn chi phối hướng truyền thông tin và tính ổn định — thể hiện rõ mối liên hệ giữa lược đồ số và vật lý của bài toán.

## Trực giác sâu hơn

Sai phân hữu hạn hiệu quả vì quy bài toán vô hạn chiều về tương tác cục bộ trên một mẫu nút nhỏ (stencil). Tuy nhiên, rời rạc hóa không phải thao tác máy móc: cách chọn lưới, công thức sai phân và xử lý điều kiện biên ảnh hưởng quyết định đến chất lượng nghiệm số.

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

Có thể dùng `Plotly.js` để dựng bản đồ nhiệt (heatmap) theo không gian và thời gian cho phương trình nhiệt hoặc sóng, giúp quan sát trực tiếp quá trình lan truyền và làm trơn trên lưới.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `finite difference heat equation visualization`, `five point stencil animation`, hoặc `PDE grid discretization`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Sai phân hữu hạn cho phương trình nhiệt" description="Heatmap thời gian-không gian của sơ đồ nhiệt explicit, cho phép thay đổi hệ số r để quan sát sự chuyển từ làm mượt sang mất ổn định." path="interactives/chapter13/finite-differences-pde-vi.html" height="660px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào mẫu sai phân ba điểm trên lưới đều và các PDE mẫu như nhiệt, sóng và Laplace trong một chiều hoặc trên hình chữ nhật.

### Mức sau đại học (Graduate)

Đi sâu vào phân tích sai số cắt cụt, cấu trúc ma trận thưa, phổ của toán tử sai phân rời rạc và mối liên hệ giữa stencil, tính nhất quán, ổn định và hội tụ.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phương trình nhiệt
- Bài toán: Xấp xỉ phương trình $$ u_t=\alpha u_{xx} $$ trên lưới rời rạc để mô phỏng truyền nhiệt.
- Mô hình: Dùng sai phân trung tâm cho $$ u_{xx} $$ kết hợp Euler tiến hoặc Euler lùi theo thời gian.
- Giả thiết và giới hạn: Lưới đều; sai số và tính ổn định phụ thuộc chặt vào $$ \Delta t $$ và $$ \Delta x $$.
- Diễn giải: PDE liên tục được chuyển thành hệ phương trình đại số theo từng bước thời gian.

#### Dao động và sóng trên dây
- Bài toán: Theo dõi biên độ dao động tại các nút lưới cho phương trình sóng.
- Mô hình: Rời rạc hóa cả đạo hàm thời gian và đạo hàm không gian bằng sai phân hữu hạn.
- Giả thiết và giới hạn: Dễ phát sinh phản xạ giả hoặc mất ổn định nếu lưới và điều kiện biên không tương thích.
- Diễn giải: Sai phân hữu hạn là con đường trực tiếp nhất từ PDE sang thuật toán tính toán.

### 2. Trực giác bổ sung và các kết nối

Sai phân hữu hạn tạo ra phiên bản rời rạc cục bộ của PDE bằng cách thay đạo hàm bằng hiệu giữa các nút lân cận. Cần tránh ngộ nhận rằng công thức đúng cục bộ là đủ: với PDE, xử lý điều kiện biên và điều kiện ổn định toàn cục mới quyết định độ tin cậy của mô phỏng.

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

Với lược đồ tường minh cho phương trình nhiệt $$ u_t = \alpha u_{xx} $$:
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right),
$$
trong đó $$ r=\frac{\alpha \Delta t}{\Delta x^2} $$. Về mặt vật lý, nhiệt độ mới tại nút $$ j $$ bằng giá trị cũ cộng với lượng khuếch tán trao đổi từ hai nút lân cận.

### 6. Phân tầng độ khó

**Bậc đại học.** Xây dựng mẫu sai phân (stencil) và lập trình các lược đồ cơ bản.

**Bậc sau đại học.** Kết nối với tính nhất quán, biểu diễn ma trận và phân tích tiêu tán/tán sắc số (numerical dissipation and dispersion).

## Video tham khảo

- xem trước: [PDE | Finite differences: introduction](https://www.youtube.com/watch?v=g3Xw1r7QGOE) — commutant, tiếng Anh. Giới thiệu cách thiết lập lưới sai phân hữu hạn cho PDE.
- [Finite Difference Method for PDES: Solution of Heat Equation](https://www.youtube.com/watch?v=ACduEf-K9qk) — Easy Mathematics, tiếng Anh. Rời rạc hóa phương trình nhiệt theo không gian và thời gian bằng sai phân hữu hạn.
- [Numerical Differentiation with Finite Difference Derivatives](https://www.youtube.com/watch?v=9fGaTU1-f-0) — Steve Brunton, tiếng Anh. Trình bày các công thức đạo hàm sai phân — nền tảng của lưới sai phân hữu hạn.
