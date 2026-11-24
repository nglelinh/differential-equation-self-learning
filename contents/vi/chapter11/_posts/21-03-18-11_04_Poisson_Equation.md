---
layout: post
title: "Phương Trình Poisson"
chapter: '11'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---

![21 03 18 11 04 Poisson Equation]({{ site.imgurl }}/chapter_img/chapter11/04_poisson_equation.svg)

Nếu phương trình Laplace $\Delta u = 0$ mô tả một căn phòng cân bằng nhiệt không có lò sưởi hay máy lạnh bên trong, thì **Phương trình Poisson** $-\Delta u = f$ là lúc ta bật nguồn nhiệt phân bố $f(x, y)$ ngay giữa phòng—hoặc đặt điện tích mật độ $\rho(x, y)$ vào không gian, hay đổ tải trọng $f$ lên màng đàn hồi. Nhờ tính tuyến tính, bài toán phức tạp này luôn tách gọn thành hai mảnh ghép rõ ràng: tìm một nghiệm riêng chịu trách nhiệm cho nguồn $f$, rồi cộng thêm nghiệm điều hòa để chỉnh đúng điều kiện biên!

## Bản đồ kiến thức nền: Bốn trụ cột giải Phương trình Poisson $-\Delta u = f$

1. **Tách nghiệm $u = u_p + u_h$ (Nghiệm riêng + Nghiệm điều hòa)**:
   Tìm một hàm $u_p$ bất kỳ thỏa mãn $-\Delta u_p = f$; khi đó hiệu $u_h = u - u_p$ thỏa mãn phương trình Laplace thuần nhất $\Delta u_h = 0$ với điều kiện biên mới $u_h|_{\partial\Omega} = g - u_p|_{\partial\Omega}$.
2. **Khai triển theo Hàm riêng của Toán tử Laplace**:
   Nếu $-\Delta \phi_k = \lambda_k \phi_k$ với biên thuần nhất, khai triển $f = \sum c_k \phi_k$ và $u = \sum u_k \phi_k$ biến PDE thành phép chia đại số đơn giản $u_k = c_k / \lambda_k$—cho thấy ngay mỗi mode nguồn bị làm trơn bởi hệ số $1/\lambda_k$.
3. **Nghiệm cơ bản và Tích phân Thế Newton**:
   Trên toàn không gian $\mathbb{R}^n$, nghiệm được viết qua tích chập với nghiệm cơ bản $\Phi$: ở 2D là $-\frac{1}{2\pi}\ln|x - y|$, ở 3D là $\frac{1}{4\pi|x - y|}$.
4. **Điều kiện Tương thích cho Biên Neumann**:
   Theo định lý Divergence, $\int_\Omega (-\Delta u)\,dx = -\oint_{\partial\Omega} \frac{\partial u}{\partial n}\,ds$, nên bài toán Poisson với biên Neumann $\partial_n u = h$ chỉ có nghiệm khi tổng nguồn sinh ra bên trong cân bằng chính xác với tổng thông lượng thoát ra qua biên: $\int_\Omega f\,dx + \oint_{\partial\Omega} h\,ds = 0$.

## Mục tiêu

Bài học này giới thiệu phương trình Poisson như dạng có nguồn của phương trình Laplace. Sau bài học, sinh viên cần hiểu vì sao $$ \Delta u=f $$ mô tả trạng thái cân bằng có nguồn bên trong, biết diễn giải ý nghĩa của dấu và độ lớn của $$ f $$, nắm mối liên hệ với mật độ điện tích và nguồn nhiệt, đồng thời hiểu ý tưởng biểu diễn nghiệm qua nghiệm cơ bản hoặc hàm Green.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace, khái niệm hàm điều hòa và trực giác về bài toán biên. Bài học này đánh dấu bước chuyển từ bài toán không nguồn sang bài toán có nguồn trong lớp PDE elliptic.

## Dẫn nhập

Nếu phương trình Laplace mô tả trạng thái cân bằng thuần túy không có nguồn bên trong, thì phương trình Poisson là bước mở rộng tự nhiên khi trong miền xuất hiện cơ chế phát sinh hoặc tiêu hao nội tại. Phân bố điện tích trong tĩnh điện, nguồn nhiệt ổn định trong tấm kim loại hay nhiều mô hình trường thế khác đều dẫn đến phương trình Poisson.

Cần lưu ý rằng phương trình Poisson vẫn nằm trọn trong khuôn khổ elliptic: phương trình Laplace là trường hợp riêng với vế phải bằng 0, còn số hạng nguồn $$ f $$ là tác nhân làm uốn cong trường thế bên trong miền.


### Khung giải thích (nên đọc chậm): Giải trọn vẹn bằng tay phương trình Poisson đối xứng tâm trên đĩa đơn vị

Xét tấm tròn bán kính $R = 1$ có nguồn nhiệt đều $f = 4$ và vành ngoài giữ ở $0^\circ\text{C}$:
$$-\Delta u = 4 \quad (r < 1), \qquad u(1) = 0.$$
1. **Viết theo bán kính $r$**: Do tính đối xứng tròn, $u = u(r)$ thỏa mãn:
   $$-\frac{1}{r}\frac{d}{dr}\left(r u'(r)\right) = 4 \implies \frac{d}{dr}\left(r u'(r)\right) = -4r.$$
2. **Tích phân lần thứ nhất**:
   $$r u'(r) = -2r^2 + C_1 \implies u'(r) = -2r + \frac{C_1}{r}.$$
   Để nhiệt độ bị chặn (không có kỳ dị $\ln r$) tại tâm $r = 0$, ta bắt buộc chọn $C_1 = 0$.
3. **Tích phân lần thứ hai và áp điều kiện biên $u(1) = 0$**:
   $$u(r) = -r^2 + C_2, \qquad u(1) = -1 + C_2 = 0 \implies C_2 = 1.$$
   Vậy nghiệm chính xác là $u(r) = \mathbf{1 - r^2} = 1 - x^2 - y^2$. Kiểm chứng nhanh: $-\Delta(1 - x^2 - y^2) = -(-2 - 2) = \mathbf{4}$, và đỉnh nóng nhất $u(0) = 1$ nằm ngay tại tâm—vượt trên biên $0$ vì nguồn $f = 4 > 0$!
## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu phương trình Laplace mô tả "cân bằng không nguồn", thì phương trình Poisson mô tả "cân bằng có nguồn". Tại nơi $$ f>0 $$, nghiệm bị uốn cong theo một chiều; tại nơi $$ f<0 $$, nghiệm bị uốn cong theo chiều ngược lại. Nguồn bên trong tạo ra độ cong nội tại cho trường nghiệm thay vì chỉ phụ thuộc thụ động vào biên.

### Cách nhìn hình ảnh

Với $$ \Delta u=0 $$, đồ thị nghiệm bên trong bị kéo căng bởi biên và không tự tạo đỉnh mới. Với $$ \Delta u=f $$, nguồn $$ f $$ đóng vai trò như lực làm cong đồ thị của $$ u $$; nơi nguồn mạnh hơn thì độ cong lớn hơn. Cách nhìn này giúp liên hệ trực tiếp giữa phân bố nguồn và hình dạng của nghiệm.

### Cách nhìn hình thức

Phương trình Poisson có dạng $$ \Delta u=f $$, và rút về phương trình Laplace khi $$ f=0 $$. Trong tĩnh điện:

$$ \Delta V=-\frac{\rho}{\varepsilon_0}, $$

với $$ \rho $$ là mật độ điện tích. Trong truyền nhiệt ổn định:

$$ -k\Delta T=Q, $$

với $$ Q $$ là nguồn nhiệt thể tích. Trên toàn không gian, khi có nghiệm cơ bản $$ \Phi $$ và điều kiện suy giảm thích hợp, nghiệm có thể biểu diễn dưới dạng tích chập $$ u=\Phi*f $$.

## Những ngộ nhận thường gặp

- "Poisson chỉ khác Laplace ở vế phải khác 0 nên không cần học riêng." Sai; vế phải mang trực tiếp ý nghĩa vật lý của phân bố nguồn.
- "Dấu của $$ f $$ không quan trọng." Sai; dấu của $$ f $$ quyết định chiều cong của nghiệm.
- "Khi đã có nguồn thì dữ liệu biên không còn quan trọng." Không đúng; PDE elliptic vẫn chịu sự chi phối mạnh của điều kiện biên.
- "Chỉ cần biết $$ f $$ là có thể bỏ qua hình học miền và điều kiện biên." Sai; cả nguồn bên trong lẫn điều kiện biên cùng xác định nghiệm.

## Tiến trình học tập đề xuất

### Bước 1: So sánh Laplace và Poisson

Làm rõ mối liên hệ cơ bản giữa trường hợp không nguồn và có nguồn.

### Bước 2: Hiểu ý nghĩa của số hạng nguồn

Diễn giải tác động của dấu và độ lớn của $$ f $$ lên hình dạng nghiệm.

### Bước 3: Liên hệ với ứng dụng vật lý

Phân tích hai mô hình điển hình là mật độ điện tích và nguồn nhiệt.

### Bước 4: Giới thiệu biểu diễn nghiệm

Đặt nền cho khái niệm nghiệm cơ bản và hàm Green ở bài tiếp theo.

### Các checkpoint

- Sinh viên có giải thích được vì sao phương trình Poisson là dạng có nguồn của phương trình Laplace hay không.
- Sinh viên có diễn giải được ý nghĩa hình học của dấu của $$ f $$ hay không.
- Sinh viên có hiểu vì sao sự có mặt của nguồn không thay thế vai trò của điều kiện biên hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Trường hợp một chiều

Trong một chiều, phương trình có dạng $$ u''=f(x) $$. Nếu $$ f(x)=1 $$, nghiệm là hàm bậc hai:

$$ u(x)=\frac{x^2}{2}+ax+b. $$

Ví dụ này minh họa trực tiếp rằng một nguồn hằng tạo ra độ cong không đổi.

### Ví dụ 2: Tĩnh điện

Khi mật độ điện tích $$ \rho $$ khác 0 trong một vùng, điện thế $$ V $$ thỏa mãn:

$$ \Delta V=-\frac{\rho}{\varepsilon_0}. $$

Đây là cầu nối trực tiếp tới phần ứng dụng tĩnh điện ở cuối chương.

### Ví dụ 3: Truyền nhiệt ổn định có nguồn

Nếu một tấm vật liệu có nguồn nhiệt phân bố đều, phân bố nhiệt độ ổn định không còn là hàm điều hòa mà thỏa mãn phương trình Poisson. Ví dụ này kết nối trực tiếp chương elliptic với chương phương trình nhiệt.

### Ví dụ 4: Biểu diễn tích chập trên toàn không gian

Trên toàn không gian, với điều kiện suy giảm thích hợp, nghiệm có thể viết dưới dạng $$ u=\Phi*f $$. Biểu diễn này mở đường cho khái niệm nghiệm cơ bản và hàm Green ở bài học kế tiếp.

## Câu hỏi khái niệm

1. Vì sao sự xuất hiện của nguồn bên trong khiến bài toán chuyển từ phương trình Laplace sang phương trình Poisson?
2. Dấu của $$ f $$ ảnh hưởng đến độ cong của nghiệm như thế nào?
3. Vì sao phương trình Poisson vẫn là một bài toán biên chứ không chỉ phụ thuộc vào nguồn?

## Bài toán ứng dụng

1. Trong tĩnh điện, vì sao một phân bố điện tích thể tích dẫn đến phương trình Poisson cho điện thế?
2. Trong truyền nhiệt ổn định, vì sao nguồn nhiệt bên trong làm nhiệt độ không còn thỏa mãn phương trình Laplace?
3. Nếu $$ f $$ chỉ khác 0 trong một vùng nhỏ, vì sao ảnh hưởng của nguồn vẫn lan ra toàn miền thông qua nghiệm của phương trình Poisson?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu trong miền có nguồn, trạng thái cân bằng có còn 'phẳng' như trường hợp không nguồn nữa không?"
- Cho sinh viên so sánh trực tiếp hai bài toán một chiều $$ u''=0 $$ và $$ u''=1 $$.
- Hỏi cả lớp: "Nguồn bên trong làm thay đổi điều gì trong cấu trúc của nghiệm?"
- Khuyến khích sinh viên nêu bằng lời một ví dụ vật lý có nguồn bên trong miền.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu từ ví dụ một chiều để làm rõ trực giác về độ cong. Khi đã quen với $$ u''=f $$, việc mở rộng sang $$ \Delta u=f $$ trong nhiều chiều sẽ tự nhiên hơn.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi tìm hiểu vai trò của nghiệm cơ bản trên toàn không gian, hoặc so sánh phương trình Poisson với bài toán cực tiểu hóa năng lượng có thêm số hạng nguồn.

## Tóm tắt dễ nhớ

Phương trình Poisson mô tả trạng thái cân bằng có nguồn. Nếu phương trình Laplace ứng với trường không nguồn, thì phương trình Poisson cho biết nguồn bên trong làm cong nghiệm như thế nào. Dù có nguồn, bài toán vẫn thuộc lớp elliptic và chịu sự chi phối mạnh của điều kiện biên.

## Video tham khảo

- xem trước: [mod08lec73 - The Poisson's Equation: Green's function solution](https://www.youtube.com/watch?v=hiHWwZb2AVU) — NPTEL-NOC IITM, tiếng Anh. Giải phương trình Poisson bằng hàm Green.
- [Laplace's Equation and Poisson's Equation](https://www.youtube.com/watch?v=nmvs0vrBT18) — Steve Brunton, tiếng Anh. So sánh sự khác biệt giữa phương trình Poisson và phương trình Laplace thông qua số hạng nguồn.
- [Lecture 4: Electrostatic potential, Poisson's Equation, Laplace's Equation, Green's functions](https://www.youtube.com/watch?v=Z0-AkSfMJYU) — rkingery, tiếng Anh. Trình bày tổng hợp về điện thế tĩnh điện, phương trình Poisson, Laplace và hàm Green.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tấm có nguồn nhiệt phân bố
- Bài toán: Tìm phân bố nhiệt độ dừng của một tấm mỏng có nguồn nhiệt bên trong.
- Mô hình:
$$ -\Delta u=f. $$
- Giả thiết và giới hạn: Nguồn $$ f $$ đã biết, vật liệu đồng nhất, trạng thái dừng.
- Diễn giải: Vế phải đo mức độ mất cân bằng cục bộ do nguồn tạo ra.

#### Độ võng của màng đàn hồi chịu tải
- Bài toán: Xác định độ võng tĩnh của một màng đàn hồi dưới tác dụng của tải phân bố.
- Mô hình: Phương trình Poisson với $$ f $$ biểu diễn mật độ tải trọng.
- Giả thiết và giới hạn: Biến dạng nhỏ, tải trọng đã biết.
- Diễn giải: So với phương trình Laplace, phương trình Poisson phản ánh sự có mặt của tác nhân tải trọng bên trong miền.

### 2. Trực giác bổ sung và các kết nối

Nếu phương trình Laplace mô tả cân bằng thuần túy, thì phương trình Poisson mô tả cân bằng có nguồn cưỡng bức bên trong; dấu của nguồn quyết định chiều độ cong trung bình của nghiệm. Một lỗi thường gặp là nhầm lẫn ý nghĩa vật lý của dấu trừ hoặc quy ước dấu của số hạng nguồn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u = 0.5 * x * (1 - x)

plt.plot(x, u)
plt.xlabel("x")
plt.ylabel("u")
plt.title("Nghiem 1D cua -u'' = 1 voi u(0)=u(1)=0")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Poisson equation source term interpretation
- search: membrane deflection Poisson equation
- search: steady state heat equation with source

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ 0<x<1 $$, xét bài toán
$$ -u''=1, \qquad u(0)=u(1)=0. $$
Tích phân hai lần thu được
$$ u(x)=\frac{1}{2}x(1-x). $$
Nghiệm cong lên trên do có nguồn dương phân bố đều. Đây là mô hình đơn giản cho phân bố nhiệt độ hoặc độ võng của dây/màng chịu tải đều.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ phương trình Laplace và phương trình Poisson qua vai trò của số hạng nguồn.

**Bậc sau đại học.** Liên hệ với dạng yếu (weak formulation), tính chính quy elliptic và nguyên lý cực đại cho bài toán có nguồn.
