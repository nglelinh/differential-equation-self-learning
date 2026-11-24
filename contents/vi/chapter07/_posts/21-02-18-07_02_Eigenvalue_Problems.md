---
layout: post
title: "07-02 Bài toán Trị riêng"
chapter: '07'
order: 2
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

Tại sao một sợi dây đàn guitar chiều dài $L$ chỉ phát ra đúng những nốt nhạc rời rạc (âm cơ bản và các họa âm bậc $2, 3, \dots$) chứ không rung ở bất kỳ tần số nào tùy thích? Tại sao một cây cột mảnh chỉ bị oằn gãy đột ngột ở đúng những mức tải trọng tới hạn nhất định (tải trọng Euler)? Câu trả lời toán học chung cho mọi hiện tượng cộng hưởng và lượng tử hóa trong tự nhiên chính là **Bài toán Trị riêng (Eigenvalue Problem)** cho toán tử vi phân!

## Bản đồ kiến thức nền: Bốn trụ cột của Bài toán Trị riêng Vi phân

1. **Nghiệm không tầm thường ($y \not\equiv 0$)**:
   Với bài toán biên thuần nhất $y'' + \lambda y = 0$, $y \equiv 0$ luôn là nghiệm tầm thường. Giá trị $\lambda$ làm xuất hiện nghiệm **khác không** gọi là **trị riêng (eigenvalue)**, và nghiệm tương ứng gọi là **hàm riêng (eigenfunction)**.
2. **Xét đầy đủ 3 miền dấu của $\lambda$ ($\lambda < 0,\; \lambda = 0,\; \lambda > 0$)**:
   Quy trình bắt buộc khi giải bài toán trị riêng: không bao giờ bỏ sót $\lambda = 0$ (ví dụ với biên Neumann $y'(0) = y'(L) = 0$, $\lambda_0 = 0$ với hàm hằng $y_0 = 1$ **là** một trị riêng quan trọng!).
3. **Biên tổng quát & Phương trình siêu việt**:
   Với biên Robin ($y(0) = 0,\; y'(L) + h y(L) = 0$), trị riêng không còn công thức đóng mà là nghiệm của phương trình siêu việt $\tan(\mu L) = -\mu / h$ tìm được bằng giao điểm đồ thị.
4. **Ý nghĩa vật lý của phổ rời rạc**:
   Biên hữu hạn $[0, L]$ biến phổ liên tục thành **phổ rời rạc đếm được** $\lambda_1 < \lambda_2 < \lambda_3 < \dots \to +\infty$.

## Mục tiêu

Bài học này giới thiệu bài toán trị riêng cho phương trình vi phân thường như bước chuyển tiếp từ BVP thông thường sang lý thuyết phổ. Sau bài học, sinh viên cần hiểu khái niệm trị riêng và hàm riêng, giải thích được vì sao chỉ một số giá trị tham số đặc biệt mới cho nghiệm không tầm thường, giải thành thạo bài toán mẫu trên đoạn hữu hạn và nhận ra mối liên hệ giữa trị riêng, chế độ riêng và tần số tự nhiên trong vật lý.

## Kiến thức nền

Sinh viên cần nắm vững BVP hai điểm, phương trình vi phân tuyến tính cấp hai hệ số hằng và khái niệm trị riêng, vector riêng của ma trận trong đại số tuyến tính. Việc đối chiếu thường xuyên với đại số tuyến tính sẽ giúp khái niệm toán tử trên không gian hàm trở nên gần gũi hơn.

## Dẫn nhập

![Bài toán trị riêng Sturm-Liouville]({{ site.imgurl }}/chapter_img/chapter07/02_eigenvalue_problems.svg)

Trong một BVP thông thường, phương trình và điều kiện biên được cho trước để tìm nghiệm. Khi phương trình thuần nhất chứa một tham số chưa biết $$ \lambda $$, bài toán chuyển thành câu hỏi mới: với những giá trị nào của $$ \lambda $$ thì bài toán tồn tại nghiệm không tầm thường thỏa mãn điều kiện biên? Đó là **bài toán trị riêng**.

Cấu trúc này hoàn toàn song song với đại số tuyến tính: thay vì tìm $$ \lambda $$ để phương trình ma trận $$ A\mathbf{v}=\lambda \mathbf{v} $$ có vector riêng khác 0, ở đây ta tìm các giá trị $$ \lambda $$ để toán tử vi phân có nghiệm khác không thỏa điều kiện biên. Các nghiệm đó là **hàm riêng**, và trong vật lý chúng tương ứng với các chế độ dao động tự nhiên hoặc trạng thái dừng.

### Khung giải thích (nên đọc chậm): Giải đầy đủ 3 trường hợp dấu của $\lambda$ cho $y'' + \lambda y = 0,\; y(0) = 0,\; y'(L) = 0$ (biên hỗn hợp Dirichlet–Neumann)

1. **Trường hợp 1 ($\lambda = -\mu^2 < 0$, $\mu > 0$)**:
   $y = c_1 \cosh(\mu x) + c_2 \sinh(\mu x)$. Từ $y(0) = c_1 = 0 \implies y = c_2\sinh(\mu x) \implies y'(L) = c_2 \mu \cosh(\mu L) = 0$. Vì $\cosh(\mu L) \ge 1 > 0 \implies c_2 = 0$ (chỉ có nghiệm tầm thường → **loại**).
2. **Trường hợp 2 ($\lambda = 0$)**:
   $y = c_1 + c_2 x$. Từ $y(0) = 0 \implies c_1 = 0$; $y'(L) = c_2 = 0$ → **loại**.
3. **Trường hợp 3 ($\lambda = \mu^2 > 0$, $\mu > 0$)**:
   $y = c_1\cos(\mu x) + c_2\sin(\mu x)$. Từ $y(0) = 0 \implies c_1 = 0$. Điều kiện $y'(L) = c_2 \mu \cos(\mu L) = 0$. Để $c_2 \neq 0$, ta cần:
   $$\cos(\mu L) = 0 \implies \mu_n L = \left(n - \frac{1}{2}\right)\pi \implies \lambda_n = \left(\frac{(2n-1)\pi}{2L}\right)^2, \quad y_n(x) = \sin\!\left(\frac{(2n-1)\pi x}{2L}\right)$$
   với $n = 1, 2, 3, \dots$ (chính là các họa âm lẻ $1:3:5$ của ống sáo kín một đầu!).

## Khái niệm theo ba cách

### Cách nhìn trực quan

Xét một sợi dây đàn cố định hai đầu. Dây không thể dao động tự nhiên ở mọi tần số tùy ý; chỉ một dãy rời rạc các tần số đặc biệt mới tạo ra sóng dừng khớp với hai đầu cố định. Các tần số đó gắn với trị riêng, còn hình dạng sóng tương ứng là hàm riêng.

### Cách nhìn hình ảnh

Khi vẽ các chế độ dao động của dây rung, chế độ cơ bản có một bụng sóng, chế độ thứ hai có hai bụng sóng (một nút ở giữa), chế độ thứ ba có ba bụng sóng, và số nút tăng dần theo bậc. Mỗi trị riêng vì thế gắn với một hình dạng không gian và một số nút xác định.

### Cách nhìn hình thức

Một bài toán trị riêng vi phân điển hình có dạng $$ Ly=\lambda w(x)y $$ kèm các điều kiện biên thuần nhất, trong đó $$ L $$ là toán tử vi phân và $$ w(x)>0 $$ là hàm trọng số. Những giá trị $$ \lambda $$ mà tại đó tồn tại nghiệm không tầm thường $$ y\not\equiv 0 $$ gọi là **trị riêng** (eigenvalue), và các nghiệm tương ứng gọi là **hàm riêng** (eigenfunction).

## Những ngộ nhận thường gặp

- "Trị riêng là bất kỳ giá trị nào giúp bài toán có nghiệm." Sai. Nghiệm tầm thường $$ y\equiv 0 $$ luôn thỏa bài toán thuần nhất; trị riêng đòi hỏi phải có nghiệm không tầm thường.
- "Hàm riêng chỉ xác định sai khác một hằng số nhân nên không quan trọng." Sai. Hình dạng không gian và vị trí các nút của hàm riêng mang ý nghĩa vật lý trực tiếp.
- "Mọi giá trị tham số trong phương trình đều có vai trò như nhau." Sai. Điều kiện biên chọn lọc ra một tập rời rạc các giá trị đặc biệt.
- "Trị riêng của ODE không liên quan đến trị riêng ma trận." Sai. Đây là sự mở rộng trực tiếp của cùng một khái niệm từ hữu hạn chiều sang không gian hàm vô hạn chiều.

## Tiến trình học tập đề xuất

### Bước 1: Liên hệ với trị riêng ma trận

Nhắc lại khái niệm $$ A\mathbf{v}=\lambda\mathbf{v} $$ với $$ \mathbf{v}\neq \mathbf{0} $$ làm điểm tựa trực giác.

### Bước 2: Phân tích BVP thuần nhất có tham số

Nhận diện vai trò của tham số $$ \lambda $$ cần xác định thay vì một hằng số đã biết.

### Bước 3: Xét đầy đủ các trường hợp dấu của tham số

Khảo sát lần lượt ba trường hợp $$ \lambda<0 $$, $$ \lambda=0 $$ và $$ \lambda>0 $$ để không bỏ sót trị riêng nào.

### Bước 4: Diễn giải hàm riêng dưới góc độ chế độ dao động

Gắn kết kết quả giải tích với hình dạng sóng và chuẩn bị chuyển sang lý thuyết Sturm–Liouville.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao định nghĩa trị riêng yêu cầu $$ y\not\equiv 0 $$ hay không.
- Sinh viên có giải đầy đủ ba trường hợp dấu của $$ \lambda $$ cho bài toán mẫu hay không.
- Sinh viên có liên hệ được hàm riêng với chế độ dao động vật lý hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dây đàn cố định hai đầu

Xét bài toán

$$ y''+\lambda y=0,
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Ta xét ba trường hợp của $$ \lambda $$:

- Nếu $$ \lambda=-\mu^2<0 $$ ($$ \mu>0 $$): nghiệm tổng quát là $$ y=Ae^{\mu x}+Be^{-\mu x} $$. Điều kiện biên buộc $$ A=B=0 $$, chỉ cho nghiệm tầm thường.
- Nếu $$ \lambda=0 $$: nghiệm là $$ y=Ax+B $$, điều kiện biên cũng buộc $$ A=B=0 $$.
- Nếu $$ \lambda=\mu^2>0 $$ ($$ \mu>0 $$): nghiệm là $$ y=A\cos(\mu x)+B\sin(\mu x) $$. Điều kiện $$ y(0)=0 $$ cho $$ A=0 $$; điều kiện $$ y(L)=0 $$ cho $$ B\sin(\mu L)=0 $$. Để có nghiệm không tầm thường ($$ B\neq 0 $$), cần

$$
\sin(\mu L)=0
\quad \Longrightarrow \quad
\mu L=n\pi.
$$

Vậy dãy trị riêng và hàm riêng tương ứng là:

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
\phi_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
n=1,2,3,\ldots
$$

Đây là bài toán trị riêng mẫu mực của toàn chương.

### Ví dụ 2: Điều kiện biên Neumann

Xét bài toán

$$ y''+\lambda y=0,
\qquad
y'(0)=0,
\qquad
y'(L)=0. $$

Với $$ \lambda=\mu^2>0 $$, nghiệm là $$ y=A\cos(\mu x)+B\sin(\mu x) $$ nên $$ y'=-A\mu\sin(\mu x)+B\mu\cos(\mu x) $$. Điều kiện $$ y'(0)=0 $$ cho $$ B=0 $$; điều kiện $$ y'(L)=0 $$ cho $$ -A\mu\sin(\mu L)=0 $$, suy ra $$ \mu L=n\pi $$ và các hàm riêng là

$$ \phi_n(x)=\cos\left(\frac{n\pi x}{L}\right). $$

Ví dụ này cho thấy việc thay đổi điều kiện biên làm thay đổi trực tiếp họ hàm riêng.

### Ví dụ 3: Trường hợp có trị riêng bằng 0

Trong bài toán điều kiện biên Neumann thuần nhất ở hai đầu (Ví dụ 2), khi xét $$ \lambda=0 $$ ta thu được nghiệm $$ y=Ax+B $$. Điều kiện $$ y'(0)=y'(L)=0 $$ chỉ buộc $$ A=0 $$ còn $$ B $$ tùy ý, nên tồn tại trị riêng $$ \lambda_0=0 $$ ứng với hàm riêng hằng $$ \phi_0(x)=1 $$. Đây là trường hợp dễ bị bỏ sót nếu chỉ quen dãy bắt đầu từ $$ n=1 $$.

### Ví dụ 4: Từ trị riêng đến tần số tự nhiên

Trong mô hình dây đàn, tần số dao động theo thời gian tỉ lệ thuận với $$ \sqrt{\lambda_n} $$. Do đó trị riêng không chỉ là đại lượng toán học trừu tượng mà gắn trực tiếp với các tần số cộng hưởng đo được trong thực nghiệm.

## Câu hỏi khái niệm

1. Vì sao yêu cầu $$ y\not\equiv 0 $$ là điều kiện không thể thiếu trong định nghĩa trị riêng?
2. Vì sao khi thay đổi điều kiện biên thì phổ trị riêng và họ hàm riêng đều thay đổi theo?
3. Trong vật lý, vì sao trị riêng thường tương ứng với tần số tự nhiên hoặc mức năng lượng rời rạc?

## Bài toán ứng dụng

1. Với một dây đàn chiều dài $$ L $$ cố định hai đầu, hãy giải thích vì sao dây chỉ dao động tự nhiên ở một dãy tần số rời rạc.
2. Với một thanh cách nhiệt hoàn toàn ở hai đầu, hãy giải thích ý nghĩa vật lý của chế độ nhiệt hằng tương ứng với trị riêng $$ \lambda_0=0 $$.
3. Trong cơ học lượng tử, vì sao ràng buộc biên trên miền hữu hạn thường dẫn đến phổ năng lượng rời rạc thay vì liên tục?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi thực tế: vì sao dây đàn chỉ phát ra các họa âm rời rạc thay vì mọi tần số tùy ý?
- Phân nhóm sinh viên xử lý ba trường hợp dấu của $$ \lambda $$ rồi tổng hợp kết quả chung.
- Vẽ các hàm riêng sin và cos bậc thấp để sinh viên gắn trị riêng với số nút và hình dạng sóng.
- Yêu cầu sinh viên so sánh bằng lời cấu trúc bài toán trị riêng của ma trận và của toán tử vi phân.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên thực hành thuần thục bài toán dây cố định hai đầu cùng quy trình xét đủ ba trường hợp dấu của $$ \lambda $$ trước khi chuyển sang các điều kiện biên khác.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên đối chiếu tính chất của ma trận đối xứng thực (trị riêng thực, vector riêng trực giao) với kỳ vọng tương tự cho toán tử Sturm–Liouville ở bài học tiếp theo.

## Tóm tắt dễ nhớ

Bài toán trị riêng tìm những giá trị tham số $$ \lambda $$ sao cho một BVP thuần nhất có nghiệm không tầm thường. Các giá trị đó là trị riêng, còn các nghiệm tương ứng là hàm riêng — biểu diễn toán học của các tần số và chế độ tự nhiên mà hệ vật lý cho phép.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động tự nhiên của dây đàn
- Bài toán: Dây đàn cố định hai đầu chỉ duy trì dao động đứng ở một dãy tần số riêng rời rạc.
- Mô hình:
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
- Giả thiết và giới hạn: Dây mảnh, lực căng không đổi, biên độ dao động nhỏ.
- Diễn giải: Chỉ các giá trị
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2 $$
mới cho chế độ dao động không tầm thường.

#### Mức năng lượng lượng tử trong hố thế vô hạn
- Bài toán: Hạt vi mô chuyển động trong giếng thế một chiều có các trạng thái dừng rời rạc.
- Mô hình: Sau khi chuẩn hóa, phương trình Schrödinger dừng có dạng
$$ y''+\lambda y=0 $$
với hàm sóng triệt tiêu tại hai thành giếng.
- Giả thiết và giới hạn: Hố thế sâu vô hạn là mô hình lý tưởng hóa.
- Diễn giải: Trị riêng tương ứng với mức năng lượng cho phép, còn hàm riêng là hàm sóng trạng thái dừng.

### 2. Trực giác bổ sung và các kết nối

Bài toán trị riêng của ODE là phiên bản vô hạn chiều của bài toán trị riêng ma trận. Điểm cốt lõi là ta không giải với mọi tham số tùy ý mà tìm tập tham số đặc biệt cho nghiệm không tầm thường. Cần tránh hai lỗi phổ biến: quên kiểm tra trường hợp $$ \lambda=0 $$ và tách rời hàm riêng khỏi ý nghĩa chế độ vật lý.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 400)

for n in range(1, 4):
    y = np.sin(n * np.pi * x / L)
    plt.plot(x, y, label=f"n={n}")

plt.xlabel("x")
plt.ylabel("mode shape")
plt.title("Ba ham rieng dau tien cua bai toan day co dinh")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vibrating string eigenmodes boundary value problem
- search: eigenvalue problem ODE mode shapes
- search: quantum infinite well eigenfunctions

### 5. Bài toán mẫu có bối cảnh thực

Giải bài toán trị riêng
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
Với $$ \lambda=\mu^2>0 $$, nghiệm có dạng
$$ y=A\cos(\mu x)+B\sin(\mu x). $$
Điều kiện tại $$ x=0 $$ cho $$ A=0 $$; điều kiện tại $$ x=L $$ cho
$$ B\sin(\mu L)=0. $$
Để có nghiệm không tầm thường, phải có
$$ \sin(\mu L)=0, $$
suy ra
$$ \mu=\frac{n\pi}{L}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Giải thành thạo bài toán trị riêng cơ bản và diễn giải trị riêng, hàm riêng như tần số và chế độ dao động.

**Bậc sau đại học.** Kết nối với lý thuyết phổ của toán tử tự liên hợp trên không gian hàm.

## Video tham khảo

- Xem trước: [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, tiếng Anh. Giới thiệu trị riêng và hàm riêng của toán tử vi phân kèm điều kiện biên.
- [Sturm-Liouville Theorem and Proof](https://www.youtube.com/watch?v=_F0ck1JncLE) — Faculty of Khan, tiếng Anh. Phát biểu và chứng minh định lý Sturm–Liouville.
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, tiếng Anh. Trực giác hình học về trị riêng hữu hạn chiều mà bài toán vi phân mở rộng.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10: bài toán trị riêng và dây rung cố định hai đầu.
- Haberman, Chương 5: mối liên hệ giữa trị riêng, chế độ riêng và điều kiện biên vật lý.
