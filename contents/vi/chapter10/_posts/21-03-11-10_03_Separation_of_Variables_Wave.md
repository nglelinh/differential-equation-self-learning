---
layout: post
title: "Phương Pháp Tách Biến Cho Sóng"
chapter: '10'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---

![21 03 11 10 03 Separation Of Variables Wave]({{ site.imgurl }}/chapter_img/chapter10/03_separation_of_variables_wave.svg)

Khi sợi dây có chiều dài hữu hạn $[0, L]$ bị kẹp chặt hai đầu, sóng chạy tới biên sẽ phản xạ qua lại liên tục. Lúc này **Phương pháp Tách biến** cho bức tranh trong sáng hơn hẳn d'Alembert: thay vì theo dõi vô số lần phản xạ, ta phân rã dao động thành chồng chất các **mode sóng đứng (normal modes)** $\sin(n\pi x/L)$ dao động điều hòa với hai bộ hệ số Fourier $A_n$ (từ vị trí đầu $f(x)$) và $B_n$ (từ vận tốc đầu $g(x)$)!

## Kiến thức cần nhớ: Bốn bước Tách biến cho Phương trình Sóng hữu hạn

1. **Nghiệm tổng quát trên $[0, L]$ với biên cố định $u(0, t) = u(L, t) = 0$**:
   $$u(x, t) = \sum_{n=1}^{\infty}\left[A_n\cos\!\left(\frac{n\pi c t}{L}\right) + B_n\sin\!\left(\frac{n\pi c t}{L}\right)\right]\sin\!\left(\frac{n\pi x}{L}\right).$$
2. **Hai công thức hệ số Fourier**:
   $$A_n = \frac{2}{L}\int_0^L f(x)\sin\!\left(\frac{n\pi x}{L}\right)dx, \qquad B_n = \frac{2}{n\pi c}\int_0^L g(x)\sin\!\left(\frac{n\pi x}{L}\right)dx.$$
   *(Đừng bao giờ quên hệ số chia $n\pi c$ khi tính $B_n$ do lấy đạo hàm $\frac{d}{dt}\sin(\frac{n\pi c t}{L})$!)*
3. **Tính tuần hoàn hoàn hảo với chu kỳ $T = \frac{2L}{c}$**:
   Mọi mode $\cos(n\pi c t/L)$ và $\sin(n\pi c t/L)$ đều lặp lại sau đúng $T = 2L/c$ (thời gian sóng đi hết chiều dài $L$ rồi phản xạ quay về!).
4. **Dây có hai đầu tự do (Neumann $u_x(0,t)=u_x(L,t)=0$)**:
   Chuyển sang cơ sở $\cos(n\pi x/L)$ và nhớ thêm mode $\lambda_0 = 0$: $T_0(t) = A_0 + B_0 t$ (dịch chuyển tịnh tiến tự do của cả sợi dây!).

## Mục tiêu

Bài học này trình bày phương pháp tách biến cho phương trình sóng trên đoạn hữu hạn, nơi điều kiện biên tạo ra các sóng dừng và các tần số riêng. Sau bài học, sinh viên cần biết cách đưa PDE về bài toán trị riêng không gian kết hợp với ODE theo thời gian, hiểu vì sao các mode riêng là sóng dừng và nắm cách khai triển điều kiện ban đầu theo các họa âm của dây.

## Kiến thức nền

Sinh viên cần nắm bài toán trị riêng Sturm-Liouville, khai triển chuỗi Fourier sin và dạng điều kiện ban đầu của phương trình sóng. Đây là nơi lý thuyết Fourier, trị riêng và vật lý dao động kết nối trực tiếp với nhau.

## Dẫn nhập

Trên toàn trục thực, nghiệm d'Alembert mô tả các sóng chạy tự do. Tuy nhiên, trên một đoạn hữu hạn có hai đầu cố định, sóng không thể truyền mãi mà liên tục phản xạ qua lại giữa hai biên. Sự giao thoa đó chọn lọc ra các dạng dao động đặc trưng tương thích với điều kiện biên: chúng không dịch chuyển tịnh tiến như sóng chạy đơn lẻ mà dao động tại chỗ, gọi là sóng dừng.

Như vậy, hình học miền và điều kiện biên chuyển bài toán truyền sóng thành một bài toán phổ. Âm thanh phát ra từ một sợi dây đàn chính là sự chồng chất của các mode sóng dừng này.

### Giải thích: Giải cầm tay bài toán dây đàn bị búa piano gõ (có vận tốc đầu $g(x)$, vị trí đầu $f(x) \equiv 0$)

Cho $u_{tt} = 9 u_{xx}$ ($c = 3$) trên $[0, \pi]$ với $u(0, t) = u(\pi, t) = 0$, $u(x, 0) = 0$ và vận tốc đầu $u_t(x, 0) = 6\sin x + 12\sin(2x)$.
1. Vì $f(x) \equiv 0 \implies$ mọi **$A_n = 0$**.
2. Tần số góc từng mode: $\omega_n = \frac{n\pi c}{L} = \frac{n\pi \cdot 3}{\pi} = 3n$.
3. Khớp đạo hàm thời gian tại $t = 0$: $u_t(x, 0) = \sum_{n=1}^{\infty} (3n B_n)\sin(nx) = 6\sin x + 12\sin(2x)$:
   - $n = 1$: $3(1) B_1 = 6 \implies B_1 = \mathbf{2}$.
   - $n = 2$: $3(2) B_2 = 12 \implies B_2 = \mathbf{2}$.
   - Mọi $B_n$ ($n \ge 3$) bằng $0$.
4. **Nghiệm chính xác**:
   $$u(x, t) = 2\sin(3t)\sin x + 2\sin(6t)\sin(2x).$$
   Kiểm tra lại $u_t(x, 0)$: $2(3)\cos(0)\sin x + 2(6)\cos(0)\sin(2x) = 6\sin x + 12\sin(2x)$ — khớp 100%!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một sợi dây đàn cố định hai đầu không thể duy trì ổn định mọi hình dạng dao động tùy ý. Chỉ những hình dạng triệt tiêu đúng tại hai đầu cố định mới tồn tại như các mode dao động tự nhiên. Phương pháp tách biến giúp tìm chính xác họ mode đó.

### Cách nhìn hình ảnh

Mode đầu tiên có một bụng sóng và không có điểm nút bên trong đoạn dây; mode thứ hai có hai bụng sóng và một điểm nút ở chính giữa; các mode bậc cao hơn có ngày càng nhiều nút. Mỗi mode giữ nguyên dáng không gian và chỉ thay đổi biên độ theo thời gian — đó chính là đặc trưng của sóng dừng.

### Cách nhìn hình thức

Xét phương trình

$$ u_{tt}=c^2u_{xx},
\qquad 0<x<L, $$

với điều kiện biên Dirichlet thuần nhất

$$ u(0,t)=u(L,t)=0. $$

Đặt $$ u(x,t)=X(x)T(t) $$ và thế vào PDE:

$$ X T''=c^2X''T. $$

Chia hai vế cho $$ c^2XT $$, ta thu được

$$ \frac{T''}{c^2T}=\frac{X''}{X}=-\lambda. $$

Từ đó tách ra hai phương trình vi phân thường:

$$ X''+\lambda X=0,
\qquad
T''+c^2\lambda T=0. $$

## Những ngộ nhận thường gặp

- "Tách biến cho phương trình sóng giống hệt phương trình nhiệt." Chỉ giống ở bài toán trị riêng không gian; phương trình theo thời gian khác hẳn vì đạo hàm thời gian có bậc hai.
- "Mỗi mode riêng là một sóng chạy." Không đúng; trên đoạn hữu hạn, các mode riêng chuẩn là sóng dừng.
- "Chỉ cần biết vị trí ban đầu là đủ xác định nghiệm." Sai; phương trình sóng đòi hỏi cả độ lệch ban đầu lẫn vận tốc ban đầu.
- "Các mode bậc cao chỉ là hiệu chỉnh nhỏ không quan trọng." Không đúng; chúng quyết định âm sắc và các chi tiết dao động của dây.

## Tiến trình học tập đề xuất

### Bước 1: Giả sử nghiệm dạng tích

Áp dụng bước khởi đầu quen thuộc $$ u(x,t)=X(x)T(t) $$.

### Bước 2: Giải bài toán trị riêng không gian

Sử dụng điều kiện biên để xác định họ hàm riêng và các trị riêng tương ứng.

### Bước 3: Giải ODE theo thời gian

Nhận diện nghiệm dao động điều hòa — điểm khác biệt rõ rệt nhất so với phương trình nhiệt.

### Bước 4: Áp đặt hai điều kiện ban đầu

Xác định hệ số khai triển từ độ lệch ban đầu $$ f $$ và vận tốc ban đầu $$ g $$.

### Các điểm kiểm tra

- Sinh viên có tách đúng bài toán không gian và bài toán thời gian hay không.
- Sinh viên có giải thích được vì sao phần thời gian dao động điều hòa thay vì suy giảm theo hàm mũ hay không.
- Sinh viên có mô tả được ý nghĩa vật lý của các mode sóng dừng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Điều kiện biên Dirichlet chuẩn

Với $$ u(0,t)=u(L,t)=0 $$, bài toán trị riêng không gian là

$$ X''+\lambda X=0,
\qquad
X(0)=X(L)=0. $$

Nghiệm không tầm thường tồn tại khi

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$

### Ví dụ 2: Nghiệm theo thời gian

Ứng với mỗi $$ \lambda_n $$, phương trình thời gian $$ T_n''+c^2\lambda_n T_n=0 $$ cho nghiệm

$$
T_n(t)=A_n\cos\left(\frac{n\pi ct}{L}\right)
+B_n\sin\left(\frac{n\pi ct}{L}\right).
$$

Kết quả này cho thấy phương trình sóng lý tưởng duy trì dao động liên tục thay vì dập tắt theo hàm mũ.

### Ví dụ 3: Nghiệm tổng quát

Chồng chất tất cả các mode riêng, ta có

$$
u(x,t)=\sum_{n=1}^{\infty}
\left[
A_n\cos\left(\frac{n\pi ct}{L}\right)
+B_n\sin\left(\frac{n\pi ct}{L}\right)
\right]
\sin\left(\frac{n\pi x}{L}\right).
$$

Trong đó, các hệ số $$ A_n $$ được xác định từ độ lệch ban đầu $$ f(x) $$, còn các hệ số $$ B_n $$ được xác định từ vận tốc ban đầu $$ g(x) $$.

### Ví dụ 4: Các họa âm của dây đàn

Tần số góc riêng của dây là

$$ \omega_n=\frac{n\pi c}{L}. $$

Mode $$ n=1 $$ là âm cơ bản, còn các mode $$ n\ge 2 $$ là các họa âm bậc cao. Đây là mối liên hệ trực tiếp giữa phổ trị riêng toán học và âm học nhạc cụ.

## Câu hỏi khái niệm

1. Vì sao trên đoạn hữu hạn có biên cố định, nghiệm lại tổ chức thành các mode sóng dừng?
2. Tại sao phần thời gian của phương trình sóng cho dao động điều hòa thay vì suy giảm mũ như phương trình nhiệt?
3. Vì sao cần cả độ lệch ban đầu và vận tốc ban đầu để xác định đầy đủ các hệ số trong nghiệm?

## Bài toán ứng dụng

1. Với một dây đàn cố định hai đầu, vì sao chỉ tồn tại một tập rời rạc các tần số dao động riêng?
2. Nếu hình dạng ban đầu của dây gần trùng với mode cơ bản, vì sao âm thanh nghe được chủ yếu mang tần số thấp nhất?
3. Trong thiết kế nhạc cụ dây, chiều dài $$ L $$ của dây ảnh hưởng như thế nào đến các tần số riêng?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Một sợi dây cố định hai đầu có thể dao động ổn định theo mọi hình dạng hay không?"
- Vẽ ba mode đầu tiên và yêu cầu sinh viên đếm số nút và số bụng của từng mode.
- Đặt câu hỏi: "Điểm khác biệt cốt lõi nhất giữa phương pháp tách biến cho phương trình nhiệt và cho phương trình sóng là gì?"
- Yêu cầu sinh viên xác định rõ mối liên hệ giữa điều kiện ban đầu với các hệ số $$ A_n $$ và $$ B_n $$.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên lấy bài toán dây cố định hai đầu làm khuôn mẫu chuẩn. Khi quy trình giải bài toán này đã vững, việc mở rộng sang điều kiện biên khác hoặc miền nhiều chiều sẽ thuận lợi hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên đối chiếu nghiệm d'Alembert (với mở rộng tuần hoàn lẻ) với khai triển sóng dừng trên đoạn hữu hạn, hoặc so sánh phổ mode của dây có biên Dirichlet và dây có biên Neumann.

## Tóm tắt dễ nhớ

Phương pháp tách biến cho phương trình sóng trên đoạn hữu hạn dẫn đến một bài toán trị riêng không gian và một ODE dao động điều hòa theo thời gian. Các mode không gian là sóng dừng ứng với các tần số riêng rời rạc, còn điều kiện ban đầu quyết định biên độ của từng họa âm.

## Video tham khảo

- Xem trước: [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, tiếng Anh. Giải phương trình sóng trên dây hữu hạn bằng tách biến và liên hệ với các họa âm của dây đàn.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Ôn lại quá trình thiết lập phương trình sóng trước khi áp dụng phương pháp tách biến.
- [But what is a Fourier series?  From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, tiếng Anh. Ôn lại chuỗi Fourier dùng để tổng hợp các mode không gian của dây.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tần số riêng của dây cố định hai đầu
- Bài toán: Xác định các mode dao động của dây đàn violin hoặc mô hình một chiều của dây cáp cầu treo.
- Mô hình:
$$ u_{tt}=c^2u_{xx}, \qquad u(0,t)=u(L,t)=0. $$
- Giả thiết và giới hạn: Hai đầu cố định hoàn toàn, dây lý tưởng, biên độ dao động nhỏ.
- Diễn giải: Tách biến cho ra tập rời rạc các mode sóng dừng.

#### Cộng hưởng trong kết cấu
- Bài toán: Một thanh hoặc dây cáp chịu kích thích gần tần số riêng sẽ dao động với biên độ lớn.
- Mô hình: Chồng chất các mode riêng tương ứng với điều kiện biên của kết cấu.
- Giả thiết và giới hạn: Hệ tuyến tính, bỏ qua phi tuyến hình học.
- Diễn giải: Phân tích phổ mode riêng là cơ sở để thiết kế kết cấu tránh hiện tượng cộng hưởng nguy hiểm.

### 2. Trực giác bổ sung và các kết nối

Tách biến chuyển PDE thành hai ODE liên kết qua cùng một trị riêng. Ý nghĩa vật lý là tìm các dạng dao động không gian có nhịp biến thiên điều hòa theo thời gian. Thông thường, một trạng thái ban đầu bất kỳ là sự chồng chất của nhiều mode chứ không chỉ một mode đơn lẻ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for n in [1, 2, 3]:
    plt.plot(x, np.sin(n * np.pi * x), label=f"mode {n}")

plt.xlabel("x")
plt.ylabel("shape")
plt.title("Ba mode rieng dau cua day co dinh hai dau")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: standing waves fixed string modes
- search: separation of variables wave equation string
- search: resonance normal modes string animation

### 5. Bài toán mẫu có bối cảnh thực

Nếu điều kiện ban đầu là
$$
u(x,0)=\sin\!\left(\frac{\pi x}{L}\right), \qquad u_t(x,0)=0,
$$
thì chỉ mode cơ bản được kích thích và nghiệm là
$$
u(x,t)=\cos\!\left(\frac{\pi c t}{L}\right)\sin\!\left(\frac{\pi x}{L}\right).
$$
Khi hình dạng ban đầu trùng đúng với một hàm riêng, dây sẽ dao động điều hòa mà giữ nguyên dạng hình học theo thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập bài toán tách biến, tính hệ số khai triển và xác định các tần số riêng.

**Bậc sau đại học.** Liên hệ với lý thuyết Sturm-Liouville, tính trực giao của hệ mode và sự hội tụ của khai triển theo hàm riêng.
