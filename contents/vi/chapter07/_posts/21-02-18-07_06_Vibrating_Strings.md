---
layout: post
title: "07-06 Ứng dụng: Dây rung"
chapter: '07'
order: 6
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

Khi bạn gảy một dây đàn guitar dài $L$ căng cố định ở hai đầu, sợi dây không dao động theo một hình sin đơn lẻ mà là bản giao hưởng chồng chất của vô hạn **sóng đứng (standing waves)** ở các tần số riêng $\omega_n = \frac{n\pi c}{L}$. Phương pháp tách biến nối thẳng Lý thuyết trị riêng Sturm–Liouville sang vật lý âm nhạc!

## Kiến thức cần nhớ: Bốn trụ cột của Bài toán Dây đàn rung

1. **Phương trình sóng 1D**:
   $u_{tt} = c^2 u_{xx}$ với tốc độ truyền sóng $c = \sqrt{T/\rho}$ ($T$: lực căng dây, $\rho$: khối lượng riêng dài).
2. **Tách biến $u(x, t) = X(x)T(t)$**:
   Tách thành bài toán trị riêng không gian $X'' + \lambda X = 0,\; X(0)=X(L)=0$ (cho $\phi_n = \sin(n\pi x/L)$) và dao động điều hòa thời gian $T_n(t) = A_n\cos(\omega_n t) + B_n\sin(\omega_n t)$.
3. **Âm cơ bản & Họa âm (Harmonics / Overtones)**:
   Tần số cơ bản $f_1 = \frac{c}{2L}$ quyết định cao độ nốt nhạc; tỷ lệ năng lượng giữa các họa âm $f_n = n f_1$ quyết định **âm sắc (timbre)** phân biệt đàn guitar với piano!
4. **Bảo toàn năng lượng cơ học**:
   Tổng động năng và thế năng đàn hồi $E(t) = \frac{1}{2}\int_0^L (u_t^2 + c^2 u_x^2)\,dx$ là hằng số không đổi theo thời gian.

## Mục tiêu

Bài học này kết nối toàn bộ nội dung chương với mô hình dây rung cổ điển. Sau bài học, sinh viên cần giải thích được vì sao điều kiện biên cố định hai đầu dẫn tới bài toán trị riêng không gian, diễn giải các hàm riêng như những chế độ sóng đứng và hiểu cách chồng chất các chế độ để mô tả dao động tổng quát của dây.

## Kiến thức nền

Sinh viên nên nắm vững BVP hai điểm, bài toán trị riêng, tính trực giao và khai triển theo hàm riêng. Một số trực giác vật lý cơ bản về sóng trên dây sẽ giúp tiếp thu bài học tự nhiên hơn.

## Dẫn nhập

![Các mode đứng của dây rung]({{ site.imgurl }}/chapter_img/chapter07/06_vibrating_strings.svg)

Dây rung là ví dụ vật lý tiêu biểu nhất minh họa trọn vẹn lý thuyết bài toán giá trị biên, trị riêng và khai triển theo hàm riêng. Một sợi dây cố định hai đầu chỉ duy trì được một họ rời rạc các hình dạng dao động tự nhiên, mỗi hình dạng gắn với một tần số riêng xác định.

Bài học này tổng hợp các khái niệm đã học thành một mạch logic thống nhất: BVP xác định toán tử không gian, bài toán trị riêng chọn ra các chế độ sóng đứng, còn tính trực giao cho phép khai triển điều kiện ban đầu thành tổng các chế độ đó.

### Giải thích: Tính tay dao động của dây đàn dài $L = \pi$ ($c = 2$) thả nhẹ từ hình dạng $u(x, 0) = 3\sin x - \sin(2x)$

Cho điều kiện ban đầu: $u(x, 0) = 3\sin x - \sin(2x)$ và vận tốc đầu $u_t(x, 0) = 0$ (thả không vận tốc đầu).
1. **Tìm tần số góc từng mode** ($\omega_n = \frac{n\pi c}{L} = \frac{n\pi \cdot 2}{\pi} = 2n$):
   - Mode $n = 1$: $\omega_1 = 2$.
   - Mode $n = 2$: $\omega_2 = 4$.
2. **Xác định hệ số $A_n, B_n$**:
   - Vì $u_t(x, 0) = 0 \implies$ mọi $B_n = 0$.
   - Khớp $u(x, 0) = \sum A_n \sin(nx) = 3\sin x - \sin(2x) \implies A_1 = 3,\; A_2 = -1$ (mọi $A_n$ khác bằng $0$).
3. **Nghiệm chính xác tại mọi $(x, t)$**:
   $$u(x, t) = 3\cos(2t)\sin x - \cos(4t)\sin(2x).$$
4. **Kiểm tra tại tâm dây $x = \pi/2$ vào lúc $t = \pi/4$**:
   $u(\pi/2, \pi/4) = 3\cos(\pi/2)\sin(\pi/2) - \cos(\pi)\sin(\pi) = 3(0)(1) - (-1)(0) = \mathbf{0}$ (dây đi ngang qua vị trí cân bằng!).

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một sợi dây đàn cố định hai đầu chỉ có thể rung tự nhiên theo các dạng sóng khớp chính xác với hai đầu ghim cố định: chế độ cơ bản gồm một bụng sóng, chế độ tiếp theo gồm hai bụng sóng, rồi ba bụng sóng và tiếp tục tăng dần. Mỗi dạng hình học đó là một chế độ sóng đứng.

### Cách nhìn hình ảnh

Quan sát đồ thị các chế độ dao động cho thấy số điểm nút bên trong dây tăng đều theo bậc $$ n $$. Chế độ bậc càng cao thì số nút càng nhiều và tần số dao động càng lớn, minh họa trực quan mối liên hệ giữa trị riêng (tần số) và hàm riêng (hình dạng không gian).

### Cách nhìn hình thức

Xét phương trình sóng một chiều
$$ u_{tt}=c^2u_{xx},
\qquad 0<x<L, $$
với điều kiện biên cố định hai đầu
$$ u(0,t)=u(L,t)=0. $$
Áp dụng phương pháp tách biến
$$ u(x,t)=X(x)T(t), $$
phần không gian dẫn đến bài toán trị riêng
$$ X''+\lambda X=0,
\qquad X(0)=X(L)=0, $$
cho hệ hàm riêng và trị riêng:
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
\lambda_n=\left(\frac{n\pi}{L}\right)^2.
$$

## Những ngộ nhận thường gặp

- "Mọi hình dạng ban đầu của dây đều là một chế độ riêng đơn lẻ." Sai. Hình dạng ban đầu tổng quát là chồng chất của nhiều chế độ riêng.
- "Các hàm sin chỉ là công thức lượng giác quen thuộc, không mang ý nghĩa vật lý đặc thù." Sai. Chúng chính là các chế độ sóng đứng của bài toán biên cố định hai đầu.
- "Điều kiện biên chỉ dùng để tìm hằng số tích phân." Sai. Chính điều kiện biên quyết định tập trị riêng rời rạc.
- "Thành phần thời gian mới quyết định cấu trúc phổ." Trong phép tách biến, chính bài toán biên theo không gian mới xác định phổ trị riêng.

## Tiến trình học tập đề xuất

### Bước 1: Thiết lập phương trình sóng và điều kiện biên

Xây dựng mô hình vật lý đầy đủ cho dây cố định hai đầu.

### Bước 2: Tách biến

Chuyển PDE thành hai ODE theo không gian và thời gian, làm rõ sự xuất hiện của bài toán trị riêng không gian.

### Bước 3: Xác định chế độ sóng đứng và tần số riêng

Tìm hệ hàm riêng $$ X_n(x) $$ và dãy tần số góc $$ \omega_n $$.

### Bước 4: Tổng hợp nghiệm tổng quát

Vận dụng khai triển theo hàm riêng để xác định các hệ số từ hình dạng và vận tốc ban đầu của dây.

### Các điểm kiểm tra

- Sinh viên có giải đúng bài toán trị riêng không gian của dây cố định hai đầu hay không.
- Sinh viên có diễn giải được ý nghĩa vật lý của các chế độ sóng đứng hay không.
- Sinh viên có giải thích được vì sao cần khai triển dữ kiện ban đầu theo hệ hàm riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba chế độ sóng đứng đầu tiên

Với dây chiều dài $$ L $$, ba chế độ đầu tiên là:
$$ X_1(x)=\sin\left(\frac{\pi x}{L}\right), $$
$$ X_2(x)=\sin\left(\frac{2\pi x}{L}\right), $$
$$ X_3(x)=\sin\left(\frac{3\pi x}{L}\right). $$
Chế độ thứ nhất có một bụng sóng, chế độ thứ hai có hai bụng sóng (một nút ở giữa dây) và chế độ thứ ba có ba bụng sóng (hai nút bên trong).

### Ví dụ 2: Dãy tần số riêng

Từ trị riêng
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2, $$
phương trình theo thời gian cho dãy tần số góc riêng:
$$ \omega_n=c\frac{n\pi}{L}. $$
Điều này giải thích vì sao các họa âm (harmonics) xuất hiện dưới dạng bội nguyên của tần số cơ bản $$ \omega_1 $$ khi dây được cố định hai đầu.

### Ví dụ 3: Nghiệm tổng quát

Chồng chất mọi chế độ riêng, nghiệm tổng quát của dây rung có dạng:
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)\sin\left(\frac{n\pi x}{L}\right).
$$
Các hệ số $$ A_n,B_n $$ được tính bằng khai triển Fourier sin từ li độ ban đầu $$ u(x,0) $$ và vận tốc ban đầu $$ u_t(x,0) $$.

### Ví dụ 4: Ý nghĩa của sự chồng chất chế độ

Khi gảy dây theo một hình dạng ban đầu không trùng với một chế độ đơn lẻ nào, chuyển động của dây được biểu diễn bằng tổ hợp tuyến tính của các chế độ sẵn có. Đây là ý nghĩa vật lý trực tiếp của tính đầy đủ của hệ hàm riêng.

## Câu hỏi khái niệm

1. Vì sao dây cố định hai đầu chỉ có một dãy rời rạc các tần số riêng?
2. Vì sao một trạng thái ban đầu tùy ý cần được biểu diễn như tổng của các chế độ riêng?
3. Điều kiện biên ảnh hưởng như thế nào đến hình dạng và phổ tần số của các chế độ sóng đứng?

## Bài toán ứng dụng

1. Trong nhạc cụ dây, vì sao âm thanh phát ra luôn gồm cả âm cơ bản lẫn các họa âm bậc cao?
2. Trong kỹ thuật cơ khí và kết cấu, vì sao việc xác định trước các tần số riêng là cần thiết để tránh hiện tượng cộng hưởng?
3. Nếu một đầu dây được thả tự do (điều kiện Neumann) thay vì cố định, phổ tần số riêng sẽ thay đổi ra sao?

## Chiến lược giảng dạy tương tác

- Cho sinh viên quan sát mô phỏng ba chế độ sóng đứng đầu tiên trước khi viết nghiệm chuỗi.
- Yêu cầu sinh viên mô tả bằng lời sự khác biệt về nút, bụng và tần số giữa chế độ cơ bản và các họa âm bậc cao.
- Minh họa một hình dạng gảy dây bất kỳ được tổng hợp từ vài chế độ sóng đứng đầu tiên.
- Liên hệ trực tiếp với âm học nhạc cụ và dao động kết cấu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung trước vào việc nhận diện ba chế độ đầu cùng các khái niệm nút, bụng và tần số riêng trước khi đi vào công thức tổng chuỗi đầy đủ.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên giải bài toán dây có một đầu cố định – một đầu tự do, hoặc tự suy ra công thức tích phân cho các hệ số $$ A_n, B_n $$ từ dữ kiện ban đầu.

## Tóm tắt dễ nhớ

Dây rung là ứng dụng tiêu biểu kết nối toàn bộ chương: điều kiện biên xác định phổ trị riêng, trị riêng sinh ra các chế độ sóng đứng và khai triển theo hàm riêng ghép các chế độ đó thành dao động tổng quát của dây.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dây đàn cố định hai đầu
- Bài toán: Xác định các chế độ dao động riêng và dãy tần số tự nhiên của dây đàn.
- Mô hình:
$$ u_{tt}=c^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
Sau phép tách biến:
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0. $$
- Giả thiết và giới hạn: Dây mảnh đồng nhất, lực căng không đổi, dao động biên độ nhỏ.
- Diễn giải: Hàm riêng dạng sin mô tả hình dạng sóng đứng, còn trị riêng quyết định phổ tần số.

#### Ống âm học và thanh đàn hồi một chiều
- Bài toán: Dao động dọc của cột khí trong ống hoặc thanh đàn hồi một chiều tạo ra các chế độ sóng đứng phụ thuộc điều kiện ở hai đầu.
- Mô hình: Cùng bài toán Sturm–Liouville một chiều với điều kiện biên Dirichlet, Neumann hoặc hỗn hợp.
- Giả thiết và giới hạn: Hình học một chiều, bỏ qua lực cản (damping).
- Diễn giải: Thay đổi điều kiện ở hai đầu ống làm thay đổi trực tiếp họ hàm riêng và các tần số cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Bài toán dây rung cho thấy mạch liên kết trọn vẹn của chương: bài toán biên sinh ra trị riêng, trị riêng tạo nên các chế độ đứng và nguyên lý chồng chất ghép chúng thành nghiệm tổng quát. Các hàm sin không xuất hiện một cách tình cờ mà chính là hệ hàm riêng của toán tử không gian ứng với điều kiện biên cố định.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 500)

fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, n in zip(axes, [1, 2, 3]):
    y = np.sin(n * np.pi * x / L)
    ax.plot(x, y)
    ax.set_title(f"Mode {n}")
    ax.set_ylim(-1.1, 1.1)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vibrating string standing wave modes
- search: fixed ends string eigenmodes animation
- search: boundary conditions standing waves

### 5. Bài toán mẫu có bối cảnh thực

Từ bài toán không gian
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
ta tìm được
$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$
Từ đó nghiệm tổng quát của dây rung là
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)X_n(x),
$$
với tần số góc
$$ \omega_n=c\frac{n\pi}{L}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững các chế độ sóng đứng, dãy tần số riêng và cách ghép chế độ khớp với điều kiện ban đầu.

**Bậc sau đại học.** Liên hệ với lý thuyết phổ của toán tử sóng, bảo toàn năng lượng và cơ sở trực giao trong không gian Hilbert.

## Video tham khảo

- Xem trước: [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, tiếng Anh. Giải phương trình sóng dây đàn bằng tách biến và diễn giải các chế độ riêng.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Xây dựng phương trình sóng một chiều từ cơ học dây căng.
- [D'Alembert Solution to the Wave Equation](https://www.youtube.com/watch?v=Sc21aPg2RyE) — Faculty of Khan, tiếng Anh. Công thức d'Alembert như một biểu diễn nghiệm đóng khác cho bài toán dây rung.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10–11: mô hình dây rung và các chế độ sóng đứng.
- Haberman, Chương 5: liên hệ chặt chẽ giữa BVP, bài toán trị riêng và phương trình sóng.
