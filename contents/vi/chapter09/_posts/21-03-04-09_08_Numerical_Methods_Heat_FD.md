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

Khi thanh kim loại có độ dẫn nhiệt thay đổi theo vị trí $\alpha(x)$ hoặc hình dạng 2D/3D phức tạp, nghiệm chuỗi Fourier không còn viết nổi bằng tay nữa. Lúc này máy tính vào cuộc bằng **Phương pháp Sai phân Hữu hạn (Finite Difference Method)**: thay không gian liên tục bằng lưới điểm cách đều $\Delta x$, thay thời gian bằng bước $\Delta t$, và xấp xỉ đạo hàm bằng hiệu chia đơn giản—nhưng chỉ cần chọn bước thời gian $\Delta t$ hơi quá tay, nghiệm số sẽ **nổ tung thành dao động vô cùng**!

## Kiến thức cần nhớ: Bốn trụ cột của Sai phân Hữu hạn cho Phương trình Nhiệt

1. **Sơ đồ Hiện FTCS (Forward-Time Central-Space)**:
   $$u_j^{n+1} = u_j^n + r\,(u_{j+1}^n - 2u_j^n + u_{j-1}^n), \qquad r = \frac{\alpha \Delta t}{(\Delta x)^2}.$$
   Siêu dễ lập trình ($O(N)$ mỗi bước), nhưng chỉ ổn định khi thỏa **điều kiện CFL khuếch tán**: $\mathbf{r = \frac{\alpha \Delta t}{(\Delta x)^2} \le \frac{1}{2}}$!
2. **Sơ đồ Ẩn BTCS (Backward Euler) — Ổn định Vô điều kiện**:
   Đánh giá đạo hàm không gian ở bước $n+1$ tạo ra hệ ma trận **tam đường chéo (tridiagonal)** giải nhanh trong $O(N)$ bằng thuật toán Thomas; ổn định với **mọi $r > 0$**!
3. **Sơ đồ Crank–Nicolson (Trung bình Hiện + Ẩn)**:
   Vừa ổn định vô điều kiện, vừa đạt độ chính xác **bậc 2 theo cả thời gian lẫn không gian** $O(\Delta t^2 + \Delta x^2)$—chuẩn công nghiệp cho phương trình nhiệt và Black–Scholes!
4. **Định lý Tương đương Lax (Consistency + Stability $\iff$ Convergence)**:
   Một sơ đồ sai phân chỉ hội tụ về nghiệm thật khi nó vừa nhất quán (sai số cắt cụt $\to 0$) vừa ổn định (không khuếch đại sai số làm tròn).

## Mục tiêu

Bài học này giới thiệu cách rời rạc hóa phương trình nhiệt bằng phương pháp sai phân hữu hạn. Sau bài học, sinh viên cần nắm cách xây dựng lưới không gian–thời gian, biết thiết lập các sơ đồ tường minh (explicit), ẩn (implicit) và Crank-Nicolson, hiểu trực giác của điều kiện ổn định $$ r\le \frac12 $$ đối với sơ đồ tường minh, và thấy được vì sao phương pháp số cần tôn trọng cấu trúc định tính của PDE gốc.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt liên tục, công thức xấp xỉ đạo hàm bằng sai phân và khái niệm ổn định số cơ bản (từ phương trình vi phân thường nếu đã học). Bài học này kết nối lý thuyết PDE với mô phỏng tính toán thực hành.

## Dẫn nhập

Ngay cả khi đã nắm các phương pháp giải tích, nhiều bài toán thực tế vẫn đòi hỏi mô phỏng số do dữ liệu ban đầu phức tạp, miền hình học không chuẩn hoặc nhu cầu tính toán nhanh. Phương pháp sai phân hữu hạn là công cụ nhập môn trực tiếp nhất cho phương trình nhiệt.

Bài học này không chỉ dừng ở việc thay đạo hàm bằng tỉ số sai phân, mà nhấn mạnh một nguyên tắc quan trọng: một sơ đồ số đáng tin cậy phải phản ánh đúng bản chất vật lý của phương trình gốc. Với phương trình nhiệt, điều đó đòi hỏi sơ đồ phải ổn định, có tính làm mượt và không sinh ra dao động phi vật lý khi bước lưới được chọn hợp lý.

### Giải thích: Chạy tay 1 bước FTCS thấy tận mắt sự khác biệt giữa $r = 0{,}25$ (ổn định) và $r = 1{,}0$ (nổ dao động!)

Giả sử lưới gồm 5 điểm với biên $u_0 = u_4 = 0$ và trạng thái ban đầu có 1 đỉnh nóng ở giữa: $\mathbf{u}^0 = [0,\; 0,\; 100,\; 0,\; 0]$.
Áp dụng công thức FTCS $u_j^1 = (1 - 2r) u_j^0 + r(u_{j-1}^0 + u_{j+1}^0)$:
- **Khi $r = 0{,}25 \le 0{,}5$ (Ổn định)**:
  - $u_1^1 = 0{,}5(0) + 0{,}25(0 + 100) = \mathbf{25}$.
  - $u_2^1 = 0{,}5(100) + 0{,}25(0 + 0) = \mathbf{50}$.
  - $u_3^1 = \mathbf{25} \implies \mathbf{u}^1 = [0,\; 25,\; 50,\; 25,\; 0]$ (đỉnh hạ mượt, tổng nhiệt bảo toàn, thỏa Nguyên lý Cực đại $0 \le u \le 100$!).
- **Khi $r = 1{,}0 > 0{,}5$ (Mất ổn định!)**:
  - $u_1^1 = -1(0) + 1(0 + 100) = \mathbf{+100}$.
  - $u_2^1 = (1 - 2)(100) + 1(0 + 0) = \mathbf{-100}$ (tâm đang $100^\circ\text{C}$ bỗng rớt xuống **$-100^\circ\text{C}$** — vi phạm trắng trợn Nguyên lý Cực đại!).
  - Bước tiếp theo $u_2^2 = +300$, $u_2^3 = -900 \to \pm\infty$!

Lưu ý kỹ thuật: nếu giảm $\Delta x$ đi $2\times$ để lưới mịn hơn, điều kiện $\Delta t \le \frac{(\Delta x)^2}{2\alpha}$ ép bạn phải giảm $\Delta t$ đi **$4\times$**—đó là lý do lưới siêu mịn luôn chuyển sang Crank–Nicolson!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Ta thay thế thanh liên tục bằng một dãy các nút rời rạc và chia thời gian thành các bước nhỏ. Nhiệt độ tại một nút ở bước thời gian tiếp theo được cập nhật dựa trên nhiệt độ hiện tại của chính nút đó và hai nút kề cận. Cơ chế này phản ánh trực tiếp bản chất tương tác cục bộ của quá trình dẫn nhiệt.

### Cách nhìn hình ảnh

Trên lưới không gian–thời gian, sơ đồ tường minh (explicit) tính trực tiếp từng giá trị ở tầng thời gian mới từ tầng thời gian cũ. Sơ đồ ẩn (implicit) lại liên kết các ẩn số ở tầng mới thành một hệ phương trình giải đồng thời, tạo nên một cấu hình tự nhất quán. Sơ đồ Crank-Nicolson nằm ở giữa hai cách tiếp cận đó, cân bằng giữa độ chính xác và tính ổn định.

### Cách nhìn hình thức

Chia đoạn $$ [0,L] $$ thành các nút lưới

$$ x_j=j\Delta x,
\qquad
\Delta x=\frac{L}{N}, $$

và chia thời gian thành các mốc $$ t^n=n\Delta t $$. Xấp xỉ các đạo hàm bởi

$$
u_t\approx \frac{u_j^{n+1}-u_j^n}{\Delta t},
\qquad
u_{xx}\approx \frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{(\Delta x)^2}.
$$

Đặt tham số lưới

$$ r=\frac{\alpha^2\Delta t}{(\Delta x)^2}, $$

ta thu được sơ đồ tường minh

$$ u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n). $$

## Những ngộ nhận thường gặp

- "Phương pháp sai phân chỉ là thay đạo hàm bằng hiệu nên luôn hội tụ về nghiệm đúng." Sai; cần kiểm tra tính tương thích, tính ổn định và sự hội tụ.
- "Sơ đồ tường minh dễ cài đặt hơn nên luôn tốt hơn." Không hẳn; sơ đồ tường minh chịu điều kiện ổn định rất chặt về bước thời gian.
- "Nếu nghiệm chính xác trơn thì nghiệm số cũng tự động trơn." Không đúng; chọn bước lưới vi phạm điều kiện ổn định sẽ tạo ra dao động phi vật lý tăng nhanh.
- "Sơ đồ ẩn luôn vượt trội về mọi mặt." Không hoàn toàn; sơ đồ ẩn ổn định không điều kiện nhưng đòi hỏi giải hệ phương trình tuyến tính ở mỗi bước thời gian.

## Tiến trình học tập đề xuất

### Bước 1: Thiết lập lưới rời rạc

Xác định rõ biến liên tục và ẩn hàm được rời rạc hóa tại các nút lưới nào.

### Bước 2: Suy ra công thức xấp xỉ sai phân

Hiểu nguồn gốc của từng sơ đồ từ khai triển Taylor thay vì học thuộc công thức.

### Bước 3: So sánh sơ đồ tường minh và sơ đồ ẩn

Đánh giá sự đánh đổi giữa chi phí tính toán mỗi bước và giới hạn bước thời gian.

### Bước 4: Phân tích tính ổn định cơ bản

Làm rõ mối liên hệ giữa điều kiện ổn định số và tính chất khuếch tán của PDE.

### Các điểm kiểm tra

- Sinh viên có tự thiết lập được sơ đồ tường minh từ công thức xấp xỉ đạo hàm hay không.
- Sinh viên có hiểu vai trò của tham số không thứ nguyên $$ r $$ hay không.
- Sinh viên có phân biệt được ưu nhược điểm của sơ đồ tường minh, sơ đồ ẩn và Crank-Nicolson hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Sơ đồ tường minh (explicit)

Thay các xấp xỉ sai phân vào phương trình $$ u_t=\alpha^2u_{xx} $$, ta được

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\alpha^2\frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{(\Delta x)^2}.
$$

Suy ra $$ u_j^{n+1}=u_j^n+r(u_{j+1}^n-2u_j^n+u_{j-1}^n) $$. Đây là sơ đồ mẫu cơ bản nhất để bắt đầu tìm hiểu sai phân hữu hạn.

### Ví dụ 2: Điều kiện ổn định von Neumann

Phân tích ổn định von Neumann cho sơ đồ tường minh dẫn tới hệ số khuếch đại

$$ \xi=1-4r\sin^2\left(\frac{\theta}{2}\right). $$

Điều kiện ổn định $$ \lvert \xi\rvert\le 1 $$ với mọi $$ \theta $$ tương đương với

$$ r\le \frac12. $$

Kết quả này cho thấy bước thời gian $$ \Delta t $$ không thể chọn tùy ý mà phải giảm tỉ lệ với $$ (\Delta x)^2 $$ khi làm mịn lưới không gian.

### Ví dụ 3: Sơ đồ ẩn (implicit)

Sử dụng sai phân lùi theo thời gian (Backward Euler):

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\alpha^2\frac{u_{j+1}^{n+1}-2u_j^{n+1}+u_{j-1}^{n+1}}{(\Delta x)^2}.
$$

Thu gọn lại, ta được hệ phương trình

$$
-r u_{j-1}^{n+1}+(1+2r)u_j^{n+1}-r u_{j+1}^{n+1}=u_j^n.
$$

Ở mỗi bước thời gian ta phải giải một hệ tuyến tính tam đường chéo, đổi lại sơ đồ ổn định với mọi $$ r>0 $$.

### Ví dụ 4: Sơ đồ Crank-Nicolson

Crank-Nicolson lấy trung bình giữa sơ đồ tường minh và sơ đồ ẩn:

$$
\frac{u_j^{n+1}-u_j^n}{\Delta t}
=
\frac{\alpha^2}{2(\Delta x)^2}
\Bigl[(u_{j+1}^{n+1}-2u_j^{n+1}+u_{j-1}^{n+1})
+
(u_{j+1}^n-2u_j^n+u_{j-1}^n)\Bigr].
$$

Sơ đồ này vừa ổn định không điều kiện vừa đạt độ chính xác bậc hai theo cả không gian và thời gian, minh họa sự cân bằng giữa độ chính xác và chi phí tính toán.

## Câu hỏi khái niệm

1. Vì sao sơ đồ tường minh cho phương trình nhiệt đòi hỏi điều kiện ổn định chặt theo $$ (\Delta x)^2 $$?
2. Cơ chế nào giúp sơ đồ ẩn ổn định hơn sơ đồ tường minh?
3. Vì sao một sơ đồ số tốt cần phản ánh đúng tính chất làm mượt của phương trình nhiệt?

## Bài toán ứng dụng

1. Khi mô phỏng truyền nhiệt trên một thanh dài, vì sao chọn bước thời gian $$ \Delta t $$ quá lớn có thể khiến nghiệm số phân kỳ dù nghiệm chính xác rất trơn?
2. Trong thực hành tính toán kỹ thuật, khi nào nên chấp nhận giải hệ tuyến tính ở mỗi bước để đổi lấy bước thời gian lớn hơn?
3. Trong xử lý ảnh, vì sao khuếch tán số có thể đóng vai trò bộ lọc làm mịn và vì sao tính ổn định là yêu cầu bắt buộc?

## Chiến lược giảng dạy tương tác

- Hướng dẫn sinh viên tự thiết lập sơ đồ tường minh từ công thức sai phân thay vì đưa sẵn kết quả.
- Đặt câu hỏi: "Nếu nghiệm chính xác của phương trình nhiệt luôn trơn dần, vì sao nghiệm số lại có thể xuất hiện dao động tăng vọt?"
- Lập bảng so sánh ba sơ đồ tường minh, ẩn và Crank-Nicolson theo các tiêu chí: chi phí mỗi bước, điều kiện ổn định và bậc chính xác.
- Chạy minh họa nhanh một trường hợp ổn định ($$ r\le 1/2 $$) và một trường hợp bất ổn định ($$ r>1/2 $$) để sinh viên quan sát trực tiếp.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung nắm chắc sơ đồ tường minh trước vì cách cập nhật cục bộ dễ hình dung. Sau khi hiểu rõ công thức và vai trò của tham số $$ r $$, hãy chuyển sang sơ đồ ẩn và Crank-Nicolson.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên thực hiện đầy đủ phân tích ổn định von Neumann cho cả ba sơ đồ, hoặc khảo sát điều kiện để sơ đồ số thỏa mãn nguyên lý cực đại rời rạc.

## Tóm tắt dễ nhớ

Phương pháp sai phân hữu hạn chuyển phương trình nhiệt thành bài toán trên lưới không gian–thời gian. Sơ đồ tường minh dễ cài đặt nhưng bị ràng buộc bởi điều kiện ổn định $$ r\le \frac12 $$, sơ đồ ẩn ổn định không điều kiện nhưng cần giải hệ tuyến tính, còn Crank-Nicolson cân bằng giữa ổn định và độ chính xác bậc hai.

## Video tham khảo

- Xem trước: [PDE | Finite differences: introduction](https://www.youtube.com/watch?v=g3Xw1r7QGOE) — commutant, tiếng Anh. Giới thiệu tổng quan về phương pháp sai phân hữu hạn cho PDE.
- [Finite Difference Method for PDES: Solution of Heat Equation](https://www.youtube.com/watch?v=ACduEf-K9qk) — Easy Mathematics, tiếng Anh. Trình bày cụ thể cách thiết lập sơ đồ sai phân cho phương trình nhiệt.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, tiếng Anh. Giải thích phương pháp Euler thuận và Euler lùi, nền tảng cho bước rời rạc hóa theo thời gian.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mô phỏng truyền nhiệt trên máy tính
- Bài toán: Tính gần đúng phân bố nhiệt khi không có công thức nghiệm giải tích thuận tiện.
- Mô hình sai phân tường minh:
$$
u_j^{n+1}=u_j^n+r\left(u_{j+1}^n-2u_j^n+u_{j-1}^n\right).
$$
- Giả thiết và giới hạn: Lưới đều một chiều và thỏa mãn điều kiện ổn định số.
- Diễn giải: Sơ đồ sai phân tái hiện tính chất làm phẳng của phương trình nhiệt trên lưới rời rạc.

#### Sơ đồ ẩn trong mô phỏng kỹ thuật
- Bài toán: Cần sử dụng bước thời gian lớn hơn mà vẫn bảo toàn tính ổn định.
- Mô hình: Sơ đồ Backward Euler hoặc Crank-Nicolson cho phương trình nhiệt.
- Giả thiết và giới hạn: Đòi hỏi giải một hệ tuyến tính ở mỗi bước thời gian.
- Diễn giải: Đổi thêm chi phí đại số tuyến tính để đạt tính ổn định không điều kiện.

### 2. Trực giác bổ sung và các kết nối

Phương pháp sai phân hữu hạn cho phương trình nhiệt thể hiện rõ mối liên hệ giữa PDE liên tục và mô hình rời rạc trên lưới. Rời rạc hóa phương trình mới chỉ là bước đầu; tính ổn định và sự hội tụ luôn phải được kiểm tra chặt chẽ.

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

Với sơ đồ tường minh, tham số
$$ r=\frac{\alpha^2 \Delta t}{(\Delta x)^2} $$
phải thỏa mãn điều kiện ổn định cổ điển
$$ r\le \frac{1}{2}. $$
Nếu chọn $$ r $$ vượt ngưỡng này, nghiệm số sẽ phân kỳ nhanh dù nghiệm liên tục rất trơn. Đây là ví dụ tiêu biểu cho vai trò thiết yếu của phân tích ổn định số.

### 6. Phân tầng độ khó

**Bậc đại học.** Cài đặt sơ đồ tường minh cơ bản và hiểu điều kiện ổn định.

**Bậc sau đại học.** Thực hiện phân tích ổn định von Neumann, so sánh các sơ đồ tường minh và ẩn, cũng như vận dụng định lý tương đương Lax (tương thích và ổn định kéo theo hội tụ).
