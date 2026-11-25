---
layout: post
title: "03-08 Hàm Truyền và Hệ thống"
chapter: '03'
order: 8
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: optional
---

Kỹ sư hàng không hay kỹ sư âm thanh thiết kế một bộ lọc phức tạp như thế nào mà không bị chìm nghỉm trong rừng phương trình vi phân ghép nối? Họ đóng gói toàn bộ tính chất nội tại của hệ thống vào một phân thức duy nhất gọi là **Hàm truyền (Transfer Function)** $H(s) = \frac{Y(s)}{U(s)}$! Khi đã có $H(s)$, mọi hệ nối tiếp chỉ là phép nhân $H_1(s)H_2(s)$, hệ song song là phép cộng, còn vòng điều khiển phản hồi âm gọn đẹp thành $\frac{H}{1 + HK}$!

## Kiến thức cần nhớ: Bốn trụ cột của Hàm Truyền & Phân tích Hệ thống

1. **Định nghĩa Hàm truyền $H(s) = \frac{Y(s)}{U(s)}$ (với điều kiện đầu bằng $0$)**:
   $H(s)$ là biến đổi Laplace của đáp ứng xung $h(t)$, chỉ phụ thuộc vào cấu tạo bên trong của hệ ($m, c, k$ hay $R, L, C$), hoàn toàn độc lập với tín hiệu đầu vào $u(t)$.
2. **Ổn định BIBO (Bounded-Input Bounded-Output) & Vị trí các Cực**:
   Một hệ hữu tỷ hợp lệ ổn định BIBO (đầu vào bị chặn luôn cho đầu ra bị chặn) khi và chỉ khi **mọi cực của $H(s)$ đều có phần thực âm ngặt** ($\operatorname{Re}(p_k) < 0$).
3. **Đáp ứng tần số $H(i\omega)$ & Biểu đồ Bode**:
   Thay $s = i\omega$ vào hàm truyền ta thu được ngay **độ khuếch đại biên độ** $\vert H(i\omega)\vert$ và **độ lệch pha** $\arg H(i\omega)$ của hệ trước mọi sóng sin tần số $\omega$!
4. **Đại số Sơ đồ khối & Điều khiển Phản hồi (Feedback)**:
   Nối tiếp: $H_1 H_2$; song song: $H_1 + H_2$; phản hồi âm với bộ điều khiển $K(s)$: $H_{\text{cl}}(s) = \frac{H(s)}{1 + H(s)K(s)}$—cho phép dịch chuyển cực bất ổn sang nửa trái mặt phẳng phức!

## Mục tiêu
Bài học này giới thiệu hàm truyền như biểu diễn đại số đặc trưng cho một hệ tuyến tính bất biến theo thời gian (LTI), hướng dẫn cách suy ra hàm truyền từ ODE với điều kiện đầu bằng 0, và phân tích mối liên hệ giữa các cực, đáp ứng xung, tín hiệu vào và tín hiệu ra.

## Kiến thức nền
Sinh viên cần nắm giải IVP bằng Laplace, hàm bước Heaviside, hàm delta và định lý tích chập. Trực giác về đầu vào, đầu ra và đáp ứng xung sẽ được củng cố xuyên suốt bài học này.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-08 Hàm Truyền và Hệ thống]({{ site.imgurl }}/chapter_img/chapter03/03_08_transfer_functions.svg)

Khi một hệ vật lý phải chịu nhiều tín hiệu đầu vào khác nhau, việc giải lại phương trình vi phân từ đầu cho từng đầu vào là không hiệu quả. Ta cần một biểu diễn tóm gọn bản chất nội tại của hệ, tách rời khỏi từng đầu vào cụ thể — đó chính là hàm truyền.

Với điều kiện đầu bằng 0, một hệ LTI được mô tả hoàn toàn bởi tỉ số giữa ảnh Laplace của đầu ra và đầu vào. Từ biểu thức duy nhất này, ta có thể khảo sát tính ổn định, đáp ứng xung, đặc tính lọc tần số và hành vi dài hạn của hệ.

### Giải thích: Dùng bộ điều khiển phản hồi tỷ lệ $K$ để "cứu" một hệ bất ổn $H(s) = \frac{1}{s - 2}$ thành hệ ổn định!

1. **Hệ vòng hở (Open-loop)**:
   $H(s) = \frac{1}{s - 2}$ ứng với PTVP $y' - 2y = u(t)$. Cực nằm tại $s = +2 > 0$ (nửa phải) $\implies$ **bất ổn** (đáp ứng xung $e^{2t} \to \infty$)!
2. **Đóng vòng phản hồi âm với độ lợi $K > 0$**:
   $$H_{\text{cl}}(s) = \frac{H(s)}{1 + K H(s)} = \frac{\frac{1}{s - 2}}{1 + \frac{K}{s - 2}} = \mathbf{\frac{1}{s + (K - 2)}}.$$
3. **Đọc cực vòng kín mới**:
   Cực duy nhất dịch sang $s = 2 - K$.
   - Để hệ ổn định BIBO, chỉ cần $2 - K < 0 \iff \mathbf{K > 2}$!
   - Ví dụ chọn $K = 5$: cực nhảy về $s = -3$, hàm truyền thành $\frac{1}{s + 3}$, và độ khuếch đại tĩnh tại $\omega = 0$ là $H_{\text{cl}}(0) = \frac{1}{3}$. Phản hồi âm đã thuần hóa một hệ bùng nổ chỉ bằng một phép nhân đại số!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hàm truyền đóng vai trò "chữ ký động học" của hệ: nó mô tả cách hệ biến đổi mọi đầu vào mà không phụ thuộc vào một tín hiệu cụ thể nào. Khi có đầu vào mới, ta chỉ cần nhân ảnh Laplace của đầu vào với hàm truyền trong miền $$ s $$.

### Cách nhìn hình ảnh
Nếu xem hệ như một "hộp đen" biến đổi tín hiệu vào thành tín hiệu ra, hàm truyền chính là đặc trưng toán học của hộp đen đó. Các cực của hàm truyền cho biết hệ có xu hướng suy giảm, dao động hay mất ổn định, còn đáp ứng xung là biểu diễn tương ứng trong miền thời gian.

### Cách nhìn hình thức
Với hệ LTI có điều kiện đầu bằng 0, đặt $$ X(s)=\mathcal{L}\{x(t)\} $$ và $$ Y(s)=\mathcal{L}\{y(t)\} $$, hàm truyền được định nghĩa bởi
$$ H(s)=\frac{Y(s)}{X(s)}. $$
Nếu hệ được mô tả bởi ODE
$$
a_n y^{(n)}+\cdots+a_1 y'+a_0y=b_m x^{(m)}+\cdots+b_0x,
$$
thì sau khi lấy biến đổi Laplace với điều kiện đầu bằng 0, ta thu được
$$
H(s)=\frac{b_m s^m+\cdots+b_0}{a_n s^n+\cdots+a_0}.
$$

## Những ngộ nhận thường gặp
- "Hàm truyền chính là nghiệm của phương trình." Sai: hàm truyền là đặc trưng của hệ, không phải lời giải ứng với một đầu vào cụ thể.
- "Điều kiện đầu không liên quan đến định nghĩa hàm truyền." Sai: định nghĩa chuẩn yêu cầu điều kiện đầu bằng 0 để tách riêng đặc tính nội tại của hệ khỏi trạng thái ban đầu.
- "Biết hàm truyền là có ngay đồ thị đầu ra." Chưa đủ: cần nhân với ảnh Laplace của đầu vào cụ thể rồi biến đổi ngược về miền thời gian.
- "Vị trí cực chỉ là chi tiết đại số." Sai: vị trí cực quyết định trực tiếp các chế độ dao động và tính ổn định của hệ.

## Tiến trình học tập đề xuất
### Bước 1: Viết ODE đầu vào – đầu ra
Xác định rõ tín hiệu đầu vào $$ x(t) $$ và tín hiệu đầu ra $$ y(t) $$.

### Bước 2: Lấy biến đổi Laplace với điều kiện đầu bằng 0
Tách đặc tính nội tại của hệ khỏi trạng thái ban đầu.

### Bước 3: Lập tỉ số $$ H(s)=Y(s)/X(s) $$
Thu được hàm truyền dạng phân thức hữu tỉ.

### Bước 4: Đọc đáp ứng xung và vị trí cực
Liên hệ mẫu số hàm truyền với hành vi thời gian và tính ổn định.

### Các checkpoint
- Sinh viên có phân biệt rõ hàm truyền với nghiệm thời gian hay không.
- Sinh viên có giải thích được lý do cần điều kiện đầu bằng 0 hay không.
- Sinh viên có đọc được mối liên hệ giữa cực của hàm truyền và các thành phần nghiệm hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mạch RC đơn giản
Xét mạch RC với điện áp đầu vào $$ x(t) $$ và điện áp đầu ra trên tụ $$ y(t) $$:
$$ RC\,y'+y=x. $$
Lấy biến đổi Laplace với điều kiện đầu bằng 0: $$ RC\,sY+Y=X $$, suy ra
$$ H(s)=\frac{Y}{X}=\frac{1}{RC\,s+1}. $$
Đây là hàm truyền bậc nhất cơ bản của bộ lọc thông thấp RC.

### Ví dụ 2: Tìm đáp ứng xung từ hàm truyền
Với $$ H(s)=\frac{1}{s+1} $$, đáp ứng xung là
$$ h(t)=\mathcal{L}^{-1}\{H(s)\}=e^{-t}, $$
cho thấy ảnh hưởng của một xung tức thời suy giảm theo hàm mũ.

### Ví dụ 3: Tính đầu ra từ hàm truyền
Với $$ H(s)=\frac{1}{s+1} $$ và đầu vào bước đơn vị $$ x(t)=1 $$ (nên $$ X(s)=\frac{1}{s} $$), ta có
$$ Y(s)=H(s)X(s)=\frac{1}{s(s+1)}. $$
Lấy biến đổi Laplace ngược thu được $$ y(t)=1-e^{-t} $$. Có sẵn $$ H(s) $$ giúp tính nhanh đầu ra cho nhiều đầu vào khác nhau.

### Ví dụ 4: Cực của hàm truyền và tính ổn định
Với $$ H(s)=\frac{1}{(s+1)(s+3)} $$, hai cực tại $$ s=-1 $$ và $$ s=-3 $$ tương ứng với hai thành phần suy giảm $$ e^{-t} $$ và $$ e^{-3t} $$. Vì mọi cực đều có phần thực âm, đáp ứng tự do tắt dần về 0 và hệ ổn định.

## Câu hỏi khái niệm
1. Vì sao định nghĩa hàm truyền yêu cầu các điều kiện đầu bằng 0?
2. Vì sao biết hàm truyền giúp rút ngắn đáng kể việc tính đáp ứng cho nhiều đầu vào khác nhau?
3. Vị trí các cực của hàm truyền cho biết gì về tính ổn định và dạng dao động của hệ?

## Bài toán ứng dụng
1. Một bộ lọc điện tử cần làm suy giảm tín hiệu tần số cao. Vì sao hàm truyền là công cụ tự nhiên để mô tả đặc tính lọc đó?
2. Trong kỹ thuật điều khiển, vì sao việc kiểm tra vị trí cực trước khi mô phỏng theo thời gian có ý nghĩa quan trọng?
3. Một hệ đo lường phản ứng chậm trước tín hiệu đầu vào biến đổi nhanh. Hãy giải thích hiện tượng này bằng hàm truyền bậc nhất.

## Chiến lược giảng dạy tương tác
- Cho sinh viên tự suy ra hàm truyền từ ODE đầu vào – đầu ra trước khi tổng quát hóa công thức.
- Hỏi lớp: "Khi giữ nguyên hệ nhưng thay đổi tín hiệu đầu vào, phần nào của lời giải trong miền $$ s $$ không đổi?"
- Ghép cặp giữa một số hàm truyền đơn giản với đồ thị đáp ứng thời gian tương ứng.
- Thảo luận ý nghĩa ổn định và dao động của cực thực âm, cực thực dương và cặp cực phức.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Giữ quy trình ba bước ngắn gọn: viết ODE đầu vào – đầu ra, lấy Laplace với điều kiện đầu bằng 0 và rút tỉ số $$ Y(s)/X(s) $$.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên liên hệ hàm truyền với đáp ứng tần số $$ H(i\omega) $$, hoặc suy ra hàm truyền của mạch RLC rồi phân tích quỹ đạo các cực khi thay đổi điện trở $$ R $$.

## Tóm tắt dễ nhớ
Hàm truyền $$ H(s)=\frac{Y(s)}{X(s)} $$ (với điều kiện đầu bằng 0) mô tả gọn gàng đặc tính vào – ra của một hệ LTI trong miền Laplace. Các cực của hàm truyền tương ứng trực tiếp với các chế độ động học và tính ổn định của hệ trong miền thời gian.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bộ lọc thông thấp RC
- Bài toán: Mô tả đặc tính lọc của mạch RC độc lập với từng tín hiệu đầu vào.
- Mô hình:
$$
RC\,y'+y=x \quad\Rightarrow\quad H(s)=\frac{1}{RC\,s+1}.
$$
- Giả thiết và giới hạn: Điều kiện đầu bằng 0, hệ tuyến tính bất biến theo thời gian.
- Diễn giải: Hàm truyền cho biết mức suy giảm tín hiệu theo tần số.

#### Hệ cơ điện bậc hai
- Bài toán: Cảm biến hoặc cơ cấu chấp hành có quán tính, lực cản và độ cứng hồi phục.
- Mô hình: $$ m y''+c y'+k y=x(t) $$, cho hàm truyền $$ H(s)=\frac{1}{ms^2+cs+k} $$.
- Giả thiết và giới hạn: Tuyến tính hóa quanh điểm làm việc.
- Diễn giải: Vị trí các cực cho biết hệ dao động, tắt dần hay mất ổn định.

#### Mô hình hộp đen đầu vào – đầu ra trong kinh tế
- Bài toán: Quan tâm đến phản ứng tổng thể của hệ trước các cú sốc vào hơn là từng cơ chế vi mô bên trong.
- Mô hình: $$ H(s)=\frac{Y(s)}{X(s)} $$.
- Giả thiết và giới hạn: Điều kiện đầu bằng 0 và xấp xỉ tuyến tính bất biến theo thời gian.
- Diễn giải: Tách biệt đặc tính của hệ khỏi tín hiệu đầu vào.

### 2. Trực giác bổ sung và các kết nối

Hàm truyền đánh dấu bước chuyển từ giải ODE sang phân tích và thiết kế hệ thống. Cần phân biệt rõ: hàm truyền là thuộc tính của bản thân hệ ("hộp đen"), còn nghiệm thời gian chỉ xác định khi nhân hàm truyền với một đầu vào cụ thể rồi biến đổi ngược.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(0, 10, 600)
H = 1 / np.sqrt(1 + omega**2)

plt.plot(omega, H)
plt.xlabel(r"$\omega$")
plt.ylabel(r"$|H(i\omega)|$")
plt.title("Biên độ của hàm truyền H(s)=1/(s+1) trên trục tần số")
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy hệ bậc nhất này truyền tốt tín hiệu tần số thấp và làm suy giảm dần tín hiệu tần số cao.

### 4. Gợi ý tìm thêm mô phỏng

- search: transfer function intuition control systems
- search: RC low pass frequency response visualization
- search: poles and stability animation

### 5. Bài toán mẫu có bối cảnh thực

Xét mạch RC $$ RC\,y'+y=x $$. Lấy biến đổi Laplace với điều kiện đầu bằng 0 được $$ (RC\,s+1)Y=X $$, suy ra $$ H(s)=\frac{1}{RC\,s+1} $$. Khi đầu vào là bước đơn vị $$ x(t)=1 $$ ($$ X(s)=\frac{1}{s} $$), ta có
$$ Y(s)=\frac{1}{s(RC\,s+1)}, $$
và biến đổi ngược thu được $$ y(t)=1-e^{-t/(RC)} $$. Ví dụ minh họa rõ quy trình: hàm truyền đặc trưng cho mạch, còn đầu vào cụ thể quyết định đáp ứng cụ thể.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập đúng hàm truyền từ ODE đầu vào – đầu ra với điều kiện đầu bằng 0.

**Bậc sau đại học.** Mở rộng sang phân tích cực – điểm không, đáp ứng tần số (giản đồ Bode) và ổn định nội tại của hệ.

## Video tham khảo

- Xem trước: [Control Systems Lectures - Transfer Functions](https://www.youtube.com/watch?v=RJleGwXorUk) — Brian Douglas, tiếng Anh. Giới thiệu hàm truyền như ánh xạ vào – ra của một hệ tuyến tính.
- [Pole Diagrams | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=pUFSXhoazY8) — MIT OpenCourseWare, tiếng Anh. Giải thích cách các cực của hàm truyền quyết định tăng trưởng, tắt dần và dao động.
- [The Laplace Transform and the Important Role it Plays](https://www.youtube.com/watch?v=VJ9phDRys_I) — Brian Douglas, tiếng Anh. Phân tích vì sao biến đổi Laplace là ngôn ngữ tự nhiên cho hàm truyền.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần hàm truyền trình bày rõ cho người mới làm quen với lý thuyết hệ thống.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ gắn biến đổi Laplace với mạch điện và hệ thống.
- Ross — *Differential Equations*: ngắn gọn, thuận tiện để ôn ý tưởng cốt lõi của hàm truyền.
