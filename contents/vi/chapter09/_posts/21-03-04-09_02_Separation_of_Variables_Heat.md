---
layout: post
title: "Phương Pháp Tách Biến Cho Phương Trình Nhiệt"
chapter: '09'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---

![21 03 04 09 02 Separation Of Variables Heat]({{ site.imgurl }}/chapter_img/chapter09/02_separation_of_variables_heat.svg)

Đứng trước một phương trình đạo hàm riêng $u_t = \alpha u_{xx}$ nơi hai biến $x$ và $t$ quyện chặt vào nhau, **Phương pháp Tách biến (Separation of Variables)** của Fourier thực hiện một nước đi táo bạo: thử tìm các nghiệm cơ sở có dạng tích $u(x, t) = X(x)T(t)$, tách một PDE khó thành **hai ODE dễ giải**, rồi cộng chồng chất vô hạn chúng lại bằng Chuỗi Fourier để khớp điều kiện ban đầu!

## Bản đồ kiến thức nền: Bốn bước chuẩn mực của Phương pháp Tách biến

1. **Tách hằng số phân ly $-\lambda$**:
   Thế $u = X(x)T(t)$ vào $u_t = \alpha u_{xx}$ và chia cho $\alpha X T$:
   $$\frac{T'(t)}{\alpha T(t)} = \frac{X''(x)}{X(x)} = -\lambda \quad (\text{hằng số độc lập cả } x \text{ lẫn } t!).$$
2. **Giải Bài toán Trị riêng cho $X(x)$**:
   $X'' + \lambda X = 0$ kết hợp điều kiện biên thuần nhất ở $x = 0, L$ cho các cặp $(\lambda_n, X_n(x))$.
3. **Giải ODE bậc nhất cho $T_n(t)$**:
   $T_n'(t) = -\alpha \lambda_n T_n(t) \implies T_n(t) = e^{-\alpha \lambda_n t}$.
4. **Nguyên lý Chồng chất & Khớp điều kiện ban đầu $u(x, 0) = f(x)$**:
   Viết $u(x, t) = \sum c_n X_n(x) e^{-\alpha \lambda_n t}$ và tìm $c_n$ bằng đúng công thức hệ số Fourier của $f(x)$!

## Mục tiêu

Bài học này trình bày phương pháp tách biến cho phương trình nhiệt trên đoạn hữu hạn. Sau bài học, sinh viên cần hiểu vì sao giả thiết $$ u(x,t)=X(x)T(t) $$ phù hợp với bài toán tuyến tính có điều kiện biên đơn giản, biết cách tách PDE thành hai ODE, hiểu vai trò của bài toán trị riêng không gian và thấy được mỗi mode nhiệt suy giảm độc lập theo thời gian theo quy luật hàm mũ.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt, chuỗi Fourier, bài toán trị riêng Sturm-Liouville và điều kiện biên thuần nhất. Đây là bài học cầu nối trực tiếp giữa chương chuỗi Fourier và chương phương trình nhiệt.

## Dẫn nhập

Phương pháp tách biến là một kỹ thuật nền tảng của lý thuyết PDE cổ điển. Giả thiết mở đầu tưởng như rất hạn chế: tìm nghiệm có dạng tích của hai hàm một biến, một hàm chỉ phụ thuộc không gian và một hàm chỉ phụ thuộc thời gian. Tuy nhiên, trong các bài toán tuyến tính có miền và điều kiện biên phù hợp, giả thiết này sinh ra một họ mode riêng đủ để tổng hợp nghiệm tổng quát.

Với phương trình nhiệt, kết quả thu được mang ý nghĩa vật lý rõ nét: mỗi mode không gian đại diện cho một dạng phân bố nhiệt cơ bản, còn thừa số thời gian quyết định tốc độ tắt dần của mode đó. Các mode tần số cao tắt nhanh hơn, còn các mode tần số thấp tồn tại lâu hơn — đây là cách diễn đạt định lượng cho hiệu ứng làm mượt của quá trình khuếch tán.

### Khung giải thích (nên đọc chậm): Giải trọn vẹn bài toán thanh nhiệt $u_t = 2 u_{xx}$ trên $[0, \pi]$ với $u(0,t)=u(\pi,t)=0$ và $u(x,0) = 1$

1. **Tách biến với $L = \pi, \alpha = 2$**:
   Biên Dirichlet $X(0) = X(\pi) = 0 \implies \lambda_n = n^2,\; X_n(x) = \sin(nx)$ và $T_n(t) = e^{-2n^2 t}$.
2. **Nghiệm chuỗi chồng chất**: $u(x, t) = \sum_{n=1}^{\infty} b_n \sin(nx)\, e^{-2n^2 t}$.
3. **Khớp điều kiện đầu $u(x, 0) = 1$** (khai triển Sin nửa khoảng của $f(x) = 1$):
   $$b_n = \frac{2}{\pi}\int_0^{\pi} 1\cdot\sin(nx)\,dx = \frac{2(1 - (-1)^n)}{n\pi} = \begin{cases} \frac{4}{n\pi}, & n \text{ lẻ}, \\ 0, & n \text{ chẵn}. \end{cases}$$
4. **Nghiệm chính xác**:
   $$u(x, t) = \frac{4}{\pi}\left(e^{-2t}\sin x + \frac{1}{3}e^{-18t}\sin(3x) + \frac{1}{5}e^{-50t}\sin(5x) + \dots\right).$$
   Kiểm tra nhiệt độ tại tâm thanh $x = \pi/2$ lúc $t = 0{,}5\text{ s}$: số hạng $n = 3$ chỉ còn $\frac{1}{3}e^{-9} \approx 0{,}00004$ (bỏ qua được!), nên $u(\pi/2, 0{,}5) \approx \frac{4}{\pi}e^{-1} \approx \mathbf{0{,}468}$ — chỉ một số hạng đầu đã chính xác tới 4 chữ số!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung phân bố nhiệt độ ban đầu của một thanh là tổng của nhiều gợn sóng không gian. Các gợn này không suy giảm với cùng một tốc độ: những gợn có bước sóng ngắn, dao động gắt sẽ tắt đi rất nhanh, trong khi những gợn dài, biến thiên chậm sẽ tồn tại lâu hơn. Phương pháp tách biến cho phép theo dõi sự tiến hóa của từng gợn như một mode độc lập.

### Cách nhìn hình ảnh

Khi quan sát các mode $$ \sin\left(\frac{n\pi x}{L}\right) $$, mode thứ nhất gồm một nửa chu kỳ sóng, mode thứ hai gồm một chu kỳ đầy đủ, và các mode bậc cao hơn có ngày càng nhiều nút dao động. Khi nhân từng mode với thừa số $$ e^{-\alpha^2\lambda_n t} $$, mode có nhiều nút hơn sẽ suy giảm nhanh hơn nhiều, giải thích trực quan vì sao đồ thị nhiệt độ ngày càng trơn phẳng theo thời gian.

### Cách nhìn hình thức

Xét bài toán

$$ u_t=\alpha^2u_{xx},
\qquad 0<x<L,\ t>0, $$

với điều kiện biên Dirichlet thuần nhất $$ u(0,t)=u(L,t)=0 $$. Đặt $$ u(x,t)=X(x)T(t) $$ và thế vào PDE:

$$ X(x)T'(t)=\alpha^2X''(x)T(t). $$

Chia hai vế cho $$ \alpha^2X(x)T(t) $$, ta thu được

$$ \frac{T'}{\alpha^2T}=\frac{X''}{X}=-\lambda. $$

Vì vế trái chỉ phụ thuộc $$ t $$ còn vế phải chỉ phụ thuộc $$ x $$, cả hai vế phải cùng bằng một hằng số. Từ đó ta tách được thành hai phương trình vi phân thường:

$$ X''+\lambda X=0, $$

$$ T'+\alpha^2\lambda T=0. $$

## Những ngộ nhận thường gặp

- "Phương pháp tách biến áp dụng được cho mọi bài toán PDE." Không đúng; phương pháp này đòi hỏi tính tuyến tính, hình học miền và điều kiện biên tương thích.
- "Một nghiệm dạng tích đơn lẻ đã là nghiệm tổng quát." Sai; dạng tích chỉ cho từng mode riêng, và ta cần chồng chất chúng thành chuỗi để thỏa mãn điều kiện đầu.
- "Tách biến chỉ là một mẹo đại số." Không đúng; nó bộc lộ trực tiếp cấu trúc phổ của toán tử vi phân theo không gian.
- "Phần thời gian và phần không gian hoàn toàn độc lập." Không chính xác; hai phần liên kết chặt chẽ với nhau thông qua cùng một trị riêng $$ \lambda $$.

## Tiến trình học tập đề xuất

### Bước 1: Viết đầy đủ bài toán biên–đầu

Nhìn nhận PDE, điều kiện biên và điều kiện đầu như một hệ thống thống nhất.

### Bước 2: Giả sử nghiệm có dạng tích

Đây là bước khởi đầu của phương pháp tách biến.

### Bước 3: Tách thành hai ODE theo không gian và thời gian

Sinh viên cần giải thích rõ vì sao xuất hiện hằng số tách biến.

### Bước 4: Giải bài toán trị riêng không gian

Đây là nơi kiến thức về chuỗi Fourier và lý thuyết Sturm-Liouville được vận dụng trực tiếp.

### Bước 5: Chồng chất các mode và áp đặt điều kiện đầu

Điều kiện ban đầu xác định hệ số khai triển của từng mode.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao hai vế sau khi chia phải bằng một hằng số hay không.
- Sinh viên có thiết lập và giải đúng bài toán trị riêng không gian hay không.
- Sinh viên có hiểu vì sao nghiệm tổng quát là chuỗi tổng các mode chứ không phải một mode đơn lẻ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bài toán Dirichlet chuẩn

Xét

$$ u_t=\alpha^2u_{xx},
\qquad
u(0,t)=u(L,t)=0. $$

Sau khi tách biến, bài toán không gian là

$$ X''+\lambda X=0,
\qquad
X(0)=X(L)=0. $$

Nghiệm không tầm thường chỉ tồn tại khi

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$

Từ phương trình theo thời gian, ta có

$$ T_n(t)=e^{-\alpha^2\lambda_n t}. $$

Do đó mỗi mode cơ bản có dạng

$$
u_n(x,t)=e^{-\alpha^2(n\pi/L)^2 t}\sin\left(\frac{n\pi x}{L}\right).
$$

### Ví dụ 2: Ghép điều kiện ban đầu

Với điều kiện ban đầu $$ u(x,0)=f(x) $$, ta khai triển

$$
f(x)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right),
$$

trong đó

$$
b_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

Từ đó thu được nghiệm đầy đủ

$$
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\alpha^2(n\pi/L)^2 t}\sin\left(\frac{n\pi x}{L}\right).
$$

Đây là công thức nghiệm trung tâm của toàn chương.

### Ví dụ 3: Dữ liệu ban đầu là hàm hằng

Nếu $$ f(x)=1 $$ trên $$ [0,L] $$, ta tính được

$$
b_n=\frac{2}{L}\int_0^L \sin\left(\frac{n\pi x}{L}\right)\,dx
=\frac{2}{n\pi}\bigl(1-(-1)^n\bigr).
$$

Chỉ các mode bậc lẻ xuất hiện:

$$
u(x,t)=\frac{4}{\pi}\sum_{n=1,3,5,\ldots}^{\infty}\frac{1}{n}
e^{-\alpha^2(n\pi/L)^2 t}
\sin\left(\frac{n\pi x}{L}\right).
$$

Ví dụ này minh họa rõ sự kết hợp giữa khai triển Fourier và phương pháp tách biến.

### Ví dụ 4: So sánh tốc độ suy giảm của các mode

Mode $$ n=1 $$ suy giảm theo thừa số $$ e^{-\alpha^2(\pi/L)^2 t} $$, trong khi mode $$ n=5 $$ suy giảm theo thừa số $$ e^{-25\alpha^2(\pi/L)^2 t} $$. Tốc độ suy giảm tăng theo bình phương bậc mode, cung cấp lời giải thích định lượng cho tính chất làm mượt của phương trình nhiệt.

## Câu hỏi khái niệm

1. Vì sao trong phương trình nhiệt, các mode không gian tần số cao lại suy giảm nhanh hơn các mode tần số thấp?
2. Yếu tố nào khiến bài toán trị riêng không gian xuất hiện một cách tự nhiên trong quá trình tách biến?
3. Vì sao một mode riêng đơn lẻ không đủ để thỏa mãn điều kiện ban đầu tổng quát?

## Bài toán ứng dụng

1. Một thanh có phân bố nhiệt độ ban đầu dao động mạnh ở quy mô nhỏ. Hãy giải thích vì sao chỉ sau một thời gian ngắn, các gợn nhỏ biến mất nhanh hơn dáng điệu tổng thể.
2. Trong xử lý ảnh, vì sao quá trình khuếch tán nhiệt có thể được xem như một bộ lọc làm mịn?
3. Nếu phân bố nhiệt độ ban đầu gần với mode cơ bản, vì sao nghiệm ở thời gian dài chủ yếu bị chi phối bởi mode này?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Nếu phân tích dữ liệu ban đầu thành các gợn sóng khác nhau, gợn nào sẽ tồn tại lâu hơn?"
- Cung cấp khung lời giải tách biến còn khuyết một số bước để sinh viên tự hoàn thiện.
- Vẽ vài mode đầu tiên và yêu cầu cả lớp dự đoán mode nào suy giảm nhanh nhất.
- Thảo luận ngắn: tách biến là một kỹ thuật đại số đơn thuần hay là một phương pháp phân tích phổ?

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên lấy bài toán Dirichlet thuần nhất làm mẫu chuẩn trong lần đầu học và lặp lại quy trình năm bước rõ ràng: đặt dạng tích, tách hằng số, giải bài toán trị riêng không gian, giải ODE thời gian và áp đặt điều kiện đầu.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên đối chiếu phương pháp tách biến cho phương trình nhiệt với phương trình sóng, nhằm làm rõ vì sao một bên cho nghiệm suy giảm theo hàm mũ còn bên kia cho nghiệm dao động điều hòa theo thời gian.

## Tóm tắt dễ nhớ

Phương pháp tách biến chuyển phương trình nhiệt thành một bài toán trị riêng theo không gian và một ODE theo thời gian. Mỗi mode không gian suy giảm theo quy luật hàm mũ, và nghiệm tổng quát là chuỗi chồng chất các mode với hệ số xác định từ khai triển Fourier của điều kiện đầu.

## Video tham khảo

- Xem trước: [(PT đạo hàm riêng) Bài 2: Phương Trình Truyền Nhiệt](https://www.youtube.com/watch?v=fFyhBMbUhLQ) — Học Toán Cùng Hải Sơn, tiếng Việt. Giới thiệu phương trình truyền nhiệt và cách giải cơ bản bằng tiếng Việt.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Trình bày phương pháp tách biến và minh họa sự suy giảm của các mode Fourier theo thời gian.
- [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, tiếng Anh. Trình bày tổng quan phương pháp tách biến, có thể áp dụng tương tự cho phương trình nhiệt.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thanh có biên giữ cố định nhiệt độ
- Bài toán: Xác định sự biến thiên nhiệt độ theo thời gian khi hai đầu thanh được giữ ở nhiệt độ không đổi.
- Mô hình:
$$ u_t=\alpha^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
- Giả thiết và giới hạn: Điều kiện biên thuần nhất và hình học một chiều.
- Diễn giải: Tách biến tạo ra các mode không gian dạng sin cùng hệ số suy giảm hàm mũ theo thời gian.

#### Sự suy giảm của các mode nhiệt
- Bài toán: Phân rã một phân bố nhiệt độ ban đầu bất kỳ theo hệ các mode riêng.
- Mô hình:
$$
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\alpha^2 \lambda_n t}\phi_n(x).
$$
- Giả thiết và giới hạn: Hàm ban đầu khai triển được theo hệ hàm riêng tương ứng.
- Diễn giải: Các mode bậc cao suy giảm nhanh hơn do có trị riêng lớn hơn.

### 2. Trực giác bổ sung và các kết nối

Phương pháp tách biến cho phương trình nhiệt ứng dụng trực tiếp lý thuyết Sturm-Liouville: mỗi mode riêng không gian suy giảm theo tốc độ mũ xác định bởi trị riêng của nó. Nghiệm tách biến không phải là kỹ thuật tình cờ, mà chính là biểu diễn phổ của bài toán tiến hóa.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for t in [0.0, 0.02, 0.08]:
    u = np.sin(np.pi * x) * np.exp(-np.pi**2 * t) + 0.4 * np.sin(3 * np.pi * x) * np.exp(-9 * np.pi**2 * t)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Suy giam mode trong phuong trinh nhiet")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: separation of variables heat equation animation
- search: eigenmode decay heat equation
- search: Fourier sine series heat equation

### 5. Bài toán mẫu có bối cảnh thực

Đặt
$$ u(x,t)=X(x)T(t). $$
Khi đó
$$ \frac{T'}{\alpha^2 T}=\frac{X''}{X}=-\lambda. $$
Ta thu được bài toán trị riêng
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
cho nghiệm
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
T_n(t)=e^{-\alpha^2 (n\pi/L)^2 t}.
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo quy trình tách biến và thiết lập nghiệm dưới dạng chuỗi mode.

**Bậc sau đại học.** Diễn giải nghiệm theo lý thuyết nửa nhóm (semigroup) và toán tử sinh của quá trình tiến hóa nhiệt.
