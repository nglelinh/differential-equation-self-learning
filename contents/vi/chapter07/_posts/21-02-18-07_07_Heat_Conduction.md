---
layout: post
title: "07-07 Ứng dụng: Dẫn nhiệt"
chapter: '07'
order: 7
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

Khác với dây đàn rung giữ nguyên năng lượng và dao động mãi mãi, nhiệt năng trong một thanh kim loại luôn tự san phẳng mọi chênh lệch cho đến khi đạt trạng thái cân bằng. Dùng đúng một bộ hàm riêng Sturm–Liouville như bài dây rung, nhưng đạo hàm bậc nhất theo thời gian $u_t = \alpha u_{xx}$ thay đổi hoàn toàn định mệnh của nghiệm: mọi dao động biến thành **suy giảm hàm mũ cực nhanh**!

## Bản đồ kiến thức nền: Bốn trụ cột của Bài toán Dẫn nhiệt 1D

1. **Phương trình nhiệt 1D ($u_t = \alpha u_{xx}$)**:
   $\alpha = \frac{k}{\rho c_p} > 0$ là hệ số khuếch tán nhiệt; vùng có độ cong âm ($u_{xx} < 0$, đỉnh nóng) sẽ giảm nhiệt ($u_t < 0$) và vùng lõm lạnh ($u_{xx} > 0$) sẽ ấm lên.
2. **Hiệu ứng làm trơn tức thì (Smoothing Effect)**:
   Mỗi mode bậc $n$ suy giảm theo hệ số $e^{-\alpha (n\pi/L)^2 t}$. Do có **$n^2$ trên số mũ**, mode $n = 10$ tắt nhanh gấp **$100\times$** mode cơ bản $n = 1$!
3. **Biên Dirichlet vs. Biên Neumann (Cách nhiệt)**:
   - Biên giữ $0^\circ\text{C}$ ($u(0,t)=u(L,t)=0$): toàn bộ nhiệt thoát ra ngoài, $u(x,t) \to 0$.
   - Biên cách nhiệt ($u_x(0,t)=u_x(L,t)=0$): tổng nhiệt năng bảo toàn, thanh tiến dần về **nhiệt độ trung bình ban đầu** $a_0 = \frac{1}{L}\int_0^L f(x)\,dx$!
4. **Thời gian đặc trưng khuếch tán ($\tau \sim L^2 / \alpha$)**:
   Tăng gấp đôi chiều dài thanh làm thời gian truyền nhiệt tăng gấp **4 lần**!

## Mục tiêu

Bài học này vận dụng tư duy bài toán giá trị biên vào mô hình dẫn nhiệt ở trạng thái dừng. Sau bài học, sinh viên cần hiểu biên dạng nhiệt độ cân bằng như nghiệm của một BVP, biết diễn giải ý nghĩa vật lý của các điều kiện biên nhiệt học và thấy được cách hàm Green cùng khai triển theo hàm riêng hỗ trợ giải các bài toán dẫn nhiệt thực tế.

## Kiến thức nền

Sinh viên nên nắm vững BVP hai điểm, các điều kiện biên Dirichlet, Neumann, Robin cùng trực giác cơ bản về nhiệt độ và thông lượng nhiệt. Việc đã làm quen sơ bộ với phương trình nhiệt là lợi thế, dù bài này tập trung vào chế độ dừng.

## Dẫn nhập

![Dẫn nhiệt trạng thái dừng trong một thanh]({{ site.imgurl }}/chapter_img/chapter07/07_heat_conduction.svg)

Khi nhắc đến dẫn nhiệt, ta thường nghĩ ngay đến một quá trình phụ thuộc thời gian trong đó nhiệt lan truyền từ vùng nóng sang vùng lạnh. Tuy nhiên, khi hệ đạt đến trạng thái cân bằng ổn định sau thời gian đủ dài, biến thời gian biến mất và bài toán trở thành việc tìm phân bố nhiệt độ cố định theo không gian — tức là một bài toán giá trị biên.

Bài học này cho thấy BVP mô tả trực tiếp một hiện tượng vật lý quen thuộc, đồng thời làm bước đệm cho chương phương trình nhiệt sau này, nơi trạng thái dừng đóng vai trò nghiệm nền của quá trình tiến hóa theo thời gian.

### Khung giải thích (nên đọc chậm): Tính tay thời gian tắt dần của mode $n = 1$ so với mode $n = 3$ trên thanh dài $L = \pi$ ($\alpha = 1$)

Giả sử thanh có nhiệt độ ban đầu $u(x, 0) = 100\sin x + 100\sin(3x)$ với hai đầu giữ ở $0^\circ\text{C}$.
1. **Viết ngay nghiệm chính xác**:
   $$u(x, t) = 100 e^{-1^2 t}\sin x + 100 e^{-3^2 t}\sin(3x) = 100 e^{-t}\sin x + 100 e^{-9t}\sin(3x).$$
2. **Tính tay biên độ hai thành phần tại $t = 0{,}5\text{ s}$**:
   - Mode $n = 1$: $100 e^{-0{,}5} \approx 100 \times 0{,}6065 = \mathbf{60{,}65^\circ\text{C}}$.
   - Mode $n = 3$: $100 e^{-4{,}5} \approx 100 \times 0{,}0111 = \mathbf{1{,}11^\circ\text{C}}$ (đã gần như biến mất!).
3. **Kết luận trực giác**: Chỉ sau $0{,}5\text{ s}$, thành phần gồ ghề $\sin(3x)$ bị dập tắt mạnh hơn gần **$55\times$** so với sóng mượt $\sin x$—đó chính là lý do bản chất của khuếch tán luôn "là phẳng" mọi nếp nhăn sắc cạnh ngay lập tức!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Biên dạng nhiệt độ trạng thái dừng là phân bố nhiệt ổn định mà thanh đạt tới sau khi mọi biến đổi quá độ đã kết thúc. Dù không còn thay đổi theo thời gian, phân bố này vẫn có thể cong, dốc hoặc không đối xứng theo không gian tùy thuộc vào nguồn nhiệt bên trong và điều kiện ở hai đầu thanh.

### Cách nhìn hình ảnh

Khi hai đầu thanh được giữ ở nhiệt độ cố định, đồ thị nhiệt độ bị ghim chặt ở hai đầu mút (Dirichlet). Nếu một đầu được cách nhiệt hoàn toàn, tiếp tuyến của đồ thị tại đầu đó nằm ngang vì độ dốc bằng 0 (Neumann). Nếu đầu thanh trao đổi nhiệt đối lưu với môi trường, điều kiện Robin liên hệ trực tiếp cả giá trị lẫn độ dốc tại biên.

### Cách nhìn hình thức

Mô hình dẫn nhiệt trạng thái dừng một chiều tổng quát có dạng
$$ -(k(x)T')'=f(x), $$
trong đó $$ k(x) $$ là hệ số dẫn nhiệt và $$ f(x) $$ là mật độ nguồn nhiệt phân bố dọc theo thanh. Các điều kiện biên thường gặp gồm điều kiện nhiệt độ cố định
$$ T(0)=T_0,\qquad T(L)=T_L $$
hoặc điều kiện thông lượng nhiệt như
$$ T'(0)=0. $$
Đây là bài toán giá trị biên elliptic một chiều cổ điển.

## Những ngộ nhận thường gặp

- "Bài toán dẫn nhiệt lúc nào cũng là PDE phụ thuộc thời gian." Sai. Ở trạng thái dừng, phương trình rút gọn về một ODE dạng BVP.
- "Trạng thái dừng nghĩa là nhiệt độ bằng hằng số trên toàn thanh." Sai; trạng thái dừng chỉ có nghĩa là không đổi theo thời gian, còn theo không gian nhiệt độ vẫn có thể biến thiên.
- "Điều kiện biên nhiệt học chỉ có dạng cố định nhiệt độ." Sai; điều kiện cách nhiệt (thông lượng) và điều kiện đối lưu (Robin) đều rất phổ biến trong thực tế.
- "Bài toán này tách biệt với lý thuyết Sturm–Liouville." Sai. Nó chia sẻ cùng cấu trúc toán tử tự liên hợp và điều kiện biên của toàn chương.

## Tiến trình học tập đề xuất

### Bước 1: Diễn giải cấu hình vật lý

Phân biệt rõ vai trò của hệ số dẫn nhiệt $$ k(x) $$, nguồn nhiệt $$ f(x) $$ và điều kiện trao đổi nhiệt tại hai đầu thanh.

### Bước 2: Thiết lập BVP trạng thái dừng

Viết phương trình cân bằng nhiệt và chuyển các mô tả vật lý ở biên thành điều kiện biên toán học.

### Bước 3: Giải các trường hợp cơ bản

Luyện giải trực tiếp các bài toán không có nguồn hoặc có nguồn hằng để xây dựng trực giác vật lý.

### Bước 4: Kết nối với các công cụ tổng quát của chương

Liên hệ với hàm Green và khai triển theo hàm riêng cho các hàm nguồn hoặc hệ số dẫn nhiệt phức tạp hơn.

### Các điểm kiểm tra

- Sinh viên có phân biệt chính xác điều kiện nhiệt độ, điều kiện thông lượng và điều kiện đối lưu hay không.
- Sinh viên có giải thích được vì sao trạng thái dừng loại bỏ đạo hàm theo thời gian hay không.
- Sinh viên có diễn giải được ý nghĩa vật lý từ hình dạng đồ thị nhiệt độ thu được hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Thanh có nguồn nhiệt phân bố đều

Giải bài toán
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Tích phân hai lần liên tiếp:
$$ T''=-1, $$
$$ T'=-x+C_1, $$
$$ T=-\frac{x^2}{2}+C_1x+C_2. $$
Áp dụng hai điều kiện biên thu được
$$ C_2=0,\qquad C_1=\frac{1}{2}, $$
suy ra
$$ T(x)=\frac{x(1-x)}{2}. $$
Phân bố nhiệt độ có dạng parabol đạt cực đại tại chính giữa thanh, phản ánh nhiệt lượng sinh ra đều bên trong thanh và thoát ra ở cả hai đầu.

### Ví dụ 2: Đầu thanh cách nhiệt

Khi một đầu thanh được cách nhiệt hoàn toàn, dòng nhiệt đi qua biên triệt tiêu, tương ứng với điều kiện Neumann:
$$ T'(0)=0. $$
Điều kiện này không ấn định trực tiếp giá trị nhiệt độ tại biên mà ấn định độ dốc của biên dạng nhiệt độ bằng 0.

### Ví dụ 3: Điều kiện biên Robin

Điều kiện
$$ T'(L)+hT(L)=0 $$
mô tả sự trao đổi nhiệt đối lưu với môi trường bên ngoài theo định luật làm nguội Newton, cho thấy điều kiện biên phản ánh trực tiếp cơ chế vật lý tại ranh giới miền.

### Ví dụ 4: Biểu diễn nghiệm bằng hàm Green

Với nguồn nhiệt phân bố tổng quát $$ f(x) $$, nghiệm trạng thái dừng có thể viết gọn dưới dạng tích phân:
$$ T(x)=\int_0^L G(x,\xi)f(\xi)\,d\xi, $$
kết nối trực tiếp bài toán dẫn nhiệt với công cụ hàm Green đã học ở bài 07-05.

## Câu hỏi khái niệm

1. Vì sao bài toán dẫn nhiệt trạng thái dừng là một BVP thay vì một IVP?
2. Ý nghĩa vật lý của điều kiện biên Neumann và Robin trong bài toán dẫn nhiệt là gì?
3. Vì sao khi có nguồn nhiệt bên trong thì biên dạng nhiệt độ cân bằng có dạng cong thay vì đường thẳng?

## Bài toán ứng dụng

1. Trong thiết kế tường cách nhiệt hoặc thanh tản nhiệt, vì sao cần xác định toàn bộ biên dạng nhiệt độ cân bằng thay vì chỉ đo nhiệt độ tại một điểm?
2. Việc bọc thêm một lớp cách nhiệt ở một đầu thanh làm thay đổi điều kiện biên toán học như thế nào?
3. Trong tường ghép nhiều lớp vật liệu khác nhau, vì sao cần bảo đảm tính liên tục của cả nhiệt độ lẫn thông lượng nhiệt tại mặt phân cách?

## Chiến lược giảng dạy tương tác

- Cho sinh viên thực hành chuyển đổi các mô tả vật lý thành biểu thức điều kiện biên toán học.
- So sánh trực quan biên dạng nhiệt độ ứng với ba loại điều kiện biên Dirichlet, Neumann và Robin.
- Yêu cầu sinh viên dự đoán vị trí nóng nhất của thanh trước khi giải bài toán.
- Liên hệ với các đối tượng quen thuộc như tường nhà, thanh gia nhiệt và cánh tản nhiệt.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giải vững các ví dụ tích phân trực tiếp và rèn kỹ năng diễn giải ý nghĩa vật lý của từng loại điều kiện biên trước khi áp dụng hàm Green hoặc khai triển theo hàm riêng.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên xét thanh có hệ số dẫn nhiệt biến thiên $$ k(x) $$ hoặc bài toán truyền nhiệt qua tường nhiều lớp với điều kiện nối tại các mặt phân cách.

## Tóm tắt dễ nhớ

Dẫn nhiệt trạng thái dừng là ứng dụng trực quan và thiết thực của bài toán giá trị biên: nghiệm biểu diễn biên dạng nhiệt độ cân bằng theo không gian, còn điều kiện biên mô tả cách thanh tương tác nhiệt với môi trường ở hai đầu. Bài học này đồng thời mở đường trực tiếp sang chương phương trình nhiệt.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân bố nhiệt độ dừng trong thanh không đồng nhất
- Bài toán: Tìm biên dạng nhiệt độ cân bằng khi có nguồn nhiệt bên trong và hai đầu chịu ràng buộc nhiệt độ hoặc cách nhiệt.
- Mô hình:
$$ -(k(x)T')'=f(x), $$
kèm điều kiện biên Dirichlet, Neumann hoặc Robin.
- Giả thiết và giới hạn: Trạng thái dừng, dẫn nhiệt một chiều, không còn tích trữ nhiệt theo thời gian.
- Diễn giải: Đây là dạng BVP tiêu biểu có thể giải bằng hàm Green hoặc khai triển theo hàm riêng.

#### Truyền nhiệt qua tường nhiều lớp
- Bài toán: Xác định biên dạng nhiệt độ cân bằng qua tường ghép từ nhiều lớp vật liệu có độ dẫn nhiệt khác nhau.
- Mô hình:
$$ -(k(x)T')'=0 $$
trên từng lớp, kết hợp điều kiện liên tục nhiệt độ và thông lượng tại các mặt phân cách.
- Giả thiết và giới hạn: Mô hình một chiều, trạng thái ổn định theo thời gian.
- Diễn giải: Điều kiện biên cùng điều kiện nối xác định duy nhất phân bố nhiệt độ qua toàn bộ bức tường.

### 2. Trực giác bổ sung và các kết nối

Bài toán dẫn nhiệt trạng thái dừng làm rõ sự khác biệt giữa bài toán giá trị biên và bài toán tiến hóa: biến thời gian không còn xuất hiện, chỉ còn cấu hình không gian cân bằng. Cần phân biệt rõ biên dạng nhiệt độ dừng này với nghiệm phụ thuộc thời gian của phương trình nhiệt sẽ nghiên cứu tiếp ở Chương 9.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

def ode(x, y):
    return np.vstack((y[1], -10 * np.ones_like(x)))

def bc(ya, yb):
    return np.array([ya[0], yb[0] - 100])

x = np.linspace(0, 1, 200)
y_guess = np.zeros((2, x.size))
sol = solve_bvp(ode, bc, x, y_guess)

plt.plot(sol.x, sol.y[0], label="T(x)")
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("Phan bo nhiet do trang thai dung")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: steady state heat conduction boundary value problem
- search: rod temperature profile with heat source
- search: Dirichlet Neumann Robin heat boundary conditions

### 5. Bài toán mẫu có bối cảnh thực

Giải bài toán
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Tích phân hai lần liên tiếp:
$$
T''=-1,\qquad
T'=-x+C_1,\qquad
T=-\frac{x^2}{2}+C_1 x+C_2.
$$
Từ hai điều kiện biên suy ra
$$ C_2=0,\qquad C_1=\frac{1}{2}, $$
do đó
$$ T(x)=\frac{x(1-x)}{2}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Giải các bài toán tìm phân bố nhiệt độ dừng cơ bản và diễn giải ý nghĩa vật lý của từng loại điều kiện biên.

**Bậc sau đại học.** Kết nối với toán tử elliptic một chiều, nguyên lý cực đại và chuẩn bị cho lý thuyết PDE elliptic ở các chương sau.

## Video tham khảo

- Xem trước: [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, tiếng Anh. Xây dựng phương trình nhiệt từ định luật bảo toàn năng lượng.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Giải phương trình nhiệt bằng các chế độ Fourier.
- [The Heat Equation and the Steady State Heat Distribution via Laplace's Equation](https://www.youtube.com/watch?v=OoRwXVIXpL0) — Steve Brunton, tiếng Anh. Trạng thái dừng của phương trình nhiệt dẫn về phương trình Laplace — nền tảng cân bằng của bài học này.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10: các ví dụ BVP dẫn nhiệt trạng thái dừng.
- Haberman, Chương 5: phân tích chi tiết mô hình vật lý và các điều kiện biên nhiệt học.
