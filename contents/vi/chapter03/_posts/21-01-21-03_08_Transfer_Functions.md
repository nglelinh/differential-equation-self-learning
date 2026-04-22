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
## Mục tiêu
Bài học này giúp sinh viên hiểu hàm truyền như mô tả đại số của một hệ tuyến tính bất biến theo thời gian, biết cách suy ra hàm truyền từ ODE với điều kiện đầu bằng 0, và diễn giải mối quan hệ giữa cực, đáp ứng xung, đầu vào và đầu ra. Đây là bước mở rộng từ Laplace như công cụ giải bài toán sang Laplace như ngôn ngữ của điều khiển và xử lý tín hiệu.

## Kiến thức nền
Sinh viên cần nắm giải IVP bằng Laplace, Heaviside, delta và tích chập. Một chút trực giác về đầu vào, đầu ra và đáp ứng xung sẽ rất hữu ích, nhưng bài học này có thể đóng vai trò chính để tạo ra trực giác ấy.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-08 Hàm Truyền và Hệ thống]({{ site.imgurl }}/chapter_img/chapter03/03_08_transfer_functions.svg)

Trong các bài trước, ta thường bắt đầu từ một ODE cụ thể rồi giải để tìm nghiệm. Nhưng nếu cùng một hệ phải chịu nhiều đầu vào khác nhau, việc giải lại từ đầu mỗi lần là không hiệu quả. Ta cần một cách tóm gọn bản thân hệ, tách nó khỏi tín hiệu vào cụ thể. Hàm truyền chính là công cụ đó.

Khi điều kiện đầu bằng 0, một hệ tuyến tính bất biến theo thời gian có thể được mô tả bằng tỉ số giữa đầu ra và đầu vào trong miền Laplace. Từ đó, ta có thể nghiên cứu ổn định, đáp ứng xung, lọc tần số và hành vi dài hạn bằng một biểu thức duy nhất. Đây là nơi ODE gặp lý thuyết hệ thống.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hàm truyền giống như "chữ ký động" của hệ. Nó cho biết hệ sẽ biến đổi đầu vào như thế nào mà không cần biết đầu vào cụ thể là gì. Khi có đầu vào mới, ta chỉ cần nhân với hàm truyền trong miền $$ s $$.

### Cách nhìn hình ảnh
Nếu coi đầu vào là thứ đi qua một "hộp đen", thì hàm truyền mô tả chính hộp đen ấy. Các cực của hàm truyền cho biết hệ có xu hướng rung, suy giảm hay cộng hưởng ra sao. Đáp ứng xung là hình ảnh thời gian của cùng một thông tin.

### Cách nhìn hình thức
Với hệ LTI và điều kiện đầu bằng 0, nếu
$$
X(s)=\mathcal{L}\{x(t)\},\qquad Y(s)=\mathcal{L}\{y(t)\},
$$
thì hàm truyền được định nghĩa bởi
$$ H(s)=\frac{Y(s)}{X(s)}. $$
Nếu hệ được mô tả bởi ODE
$$
a_n y^{(n)}+\cdots+a_1 y'+a_0y=b_m x^{(m)}+\cdots+b_0x,
$$
thì sau Laplace với điều kiện đầu bằng 0, ta có
$$
H(s)=\frac{b_m s^m+\cdots+b_0}{a_n s^n+\cdots+a_0}.
$$

## Những ngộ nhận thường gặp
- "Hàm truyền là cùng một thứ với nghiệm." Sai. Nó là đặc trưng của hệ, không phải lời giải cho một đầu vào cụ thể.
- "Điều kiện đầu không quan trọng khi nói về hàm truyền." Sai. Định nghĩa chuẩn dùng điều kiện đầu bằng 0 để tách riêng bản thân hệ khỏi trạng thái ban đầu.
- "Biết hàm truyền là đủ để biết mọi thứ ngay lập tức." Chưa đủ; còn cần hiểu đầu vào và cách quay về miền thời gian.
- "Cực chỉ là thông tin đại số." Sai. Chúng liên hệ trực tiếp với mode động học và ổn định.

## Tiến trình học tập đề xuất
### Bước 1: Xuất phát từ một ODE đầu vào-đầu ra
Viết rõ tín hiệu vào và ra.

### Bước 2: Áp Laplace với điều kiện đầu bằng 0
Đây là bước tách hệ khỏi trạng thái đầu.

### Bước 3: Giải tỉ số $$ Y/X $$
Ta thu được hàm truyền.

### Bước 4: Kết nối với đáp ứng xung và cực
Hiểu được ý nghĩa hệ thống của công thức.

### Các checkpoint
- Sinh viên có phân biệt được hàm truyền với nghiệm thời gian hay không.
- Sinh viên có hiểu tại sao cần điều kiện đầu bằng 0 trong định nghĩa hay không.
- Sinh viên có đọc được cực của hàm truyền gắn với mode hệ như thế nào hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mạch RC đơn giản
Xét mạch RC với điện áp đầu vào $$ x(t) $$ và điện áp đầu ra trên tụ là $$ y(t) $$:
$$ RC\,y'+y=x. $$
Áp Laplace với điều kiện đầu bằng 0:
$$ RC\,sY+Y=X. $$
Suy ra
$$ H(s)=\frac{Y}{X}=\frac{1}{RC\,s+1}. $$
Đây là hàm truyền bậc nhất rất quan trọng trong lý thuyết mạch và lọc tín hiệu.

### Ví dụ 2: Đáp ứng xung từ hàm truyền
Với
$$ H(s)=\frac{1}{s+1}, $$
đáp ứng xung là
$$ h(t)=\mathcal{L}^{-1}\{H(s)\}=e^{-t}. $$
Điều này cho thấy hệ "ghi nhớ" đầu vào quá khứ theo một hàm suy giảm mũ.

### Ví dụ 3: Từ hàm truyền đến đầu ra
Nếu
$$ H(s)=\frac{1}{s+1} $$
và đầu vào là bước đơn vị
$$ x(t)=1, $$
thì
$$ X(s)=\frac{1}{s}. $$
Do đó
$$ Y(s)=H(s)X(s)=\frac{1}{s(s+1)}. $$
Lấy Laplace ngược:
$$ y(t)=1-e^{-t}. $$
Ví dụ này cho thấy hàm truyền thực sự giúp ta giải nhiều bài với cùng một hệ rất nhanh.

### Ví dụ 4: Cực và ổn định
Nếu
$$ H(s)=\frac{1}{(s+1)(s+3)}, $$
thì các cực ở $$ s=-1 $$ và $$ s=-3 $$ cho ta hai mode suy giảm
$$ e^{-t},\qquad e^{-3t}. $$
Vì cả hai cực đều có phần thực âm, hệ ổn định theo nghĩa đáp ứng tự do suy giảm. Đây là cầu nối rất đẹp giữa đại số miền $$ s $$ và động học miền thời gian.

## Câu hỏi khái niệm
1. Vì sao hàm truyền được định nghĩa với điều kiện đầu bằng 0?
2. Vì sao biết hàm truyền cho phép giải nhanh nhiều bài với cùng một hệ?
3. Cực của hàm truyền nói gì về ổn định và mode của hệ?

## Bài toán ứng dụng
1. Một bộ lọc điện tử cần làm mượt tín hiệu cao tần. Hãy giải thích vì sao hàm truyền là công cụ tự nhiên để mô tả chức năng của bộ lọc.
2. Trong điều khiển tự động, vì sao việc biết cực của hệ trước khi mô phỏng thời gian lại rất có giá trị?
3. Một hệ đo lường có đầu ra chậm phản ứng với đầu vào thay đổi nhanh. Hãy giải thích hiện tượng này dưới ngôn ngữ hàm truyền bậc nhất.

## Chiến lược giảng dạy tương tác
- Cho sinh viên nhìn ODE đầu vào-đầu ra rồi tự suy ra hàm truyền trước khi giáo viên chốt công thức.
- Hỏi lớp: "Nếu giữ nguyên hệ nhưng thay đầu vào, phần nào của phép tính được giữ lại?"
- Cho sinh viên ghép các hàm truyền đơn giản với dạng đáp ứng thời gian tương ứng.
- Khuyến khích lớp diễn giải bằng lời cực âm, cực dương, cực phức dưới góc nhìn ổn định và dao động.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên để sinh viên yếu bám vào chuỗi đơn giản: ODE đầu vào-đầu ra, Laplace với điều kiện đầu bằng 0, rút $$ Y/X $$. Khi thấy quy trình lặp lại, hàm truyền sẽ bớt trừu tượng.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi nối hàm truyền với đáp ứng tần số sơ cấp, hoặc suy ra hàm truyền của một hệ bậc hai như RLC rồi phân tích các cực.

## Tóm tắt dễ nhớ
Hàm truyền là bản mô tả gọn của hệ trong miền Laplace:
$$ H(s)=\frac{Y(s)}{X(s)} $$
khi điều kiện đầu bằng 0. Biết hàm truyền là biết cách hệ biến đổi mọi đầu vào. Các cực của nó chính là dấu vết đại số của các mode thời gian.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bộ lọc RC
- Bài toán: Mạch RC đầu vào - đầu ra cần được mô tả độc lập với từng tín hiệu cụ thể.
- Mô hình:
$$
RC\,y'+y=x
\quad\Rightarrow\quad
H(s)=\frac{1}{RC\,s+1}.
$$
- Giả thiết và giới hạn: Điều kiện đầu bằng 0, hệ tuyến tính và bất biến theo thời gian.
- Diễn giải: Hàm truyền là "chữ ký động" của hệ và cho biết nó lọc tín hiệu như thế nào.

#### Hệ cơ điện bậc hai
- Bài toán: Một cảm biến hoặc bộ truyền động có quán tính, cản và hồi phục.
- Mô hình:
$$ m y''+c y'+k y=x(t). $$
- Giả thiết và giới hạn: Tuyến tính hóa quanh điểm làm việc.
- Diễn giải: Các cực của
$$ H(s)=\frac{1}{ms^2+cs+k} $$
cho biết hệ dao động, tắt dần hay mất ổn định.

#### Kinh tế và hộp đen đầu vào - đầu ra
- Bài toán: Ta quan tâm hệ phản ứng với các cú sốc vào như thế nào hơn là từng chi tiết vi mô bên trong.
- Mô hình:
$$ H(s)=\frac{Y(s)}{X(s)}. $$
- Giả thiết và giới hạn: Điều kiện đầu bằng 0 và hệ mang tính LTI.
- Diễn giải: Hàm truyền cho phép tách "hệ" khỏi "đầu vào".

### 2. Trực giác bổ sung và các kết nối

Hàm truyền là điểm chương Laplace chuyển hẳn sang tư duy hệ thống. Từ đây, giải ODE không còn là mục tiêu duy nhất; ta còn muốn mô tả, so sánh và thiết kế hệ. Một hiểu lầm phổ biến là nghĩ hàm truyền chính là nghiệm. Không phải vậy: nó là đặc trưng của hộp đen, còn nghiệm thời gian chỉ xuất hiện khi ghép nó với một đầu vào cụ thể.

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

Đây là một trực quan rất tốt để thấy mạch bậc nhất điển hình phản ứng mạnh với tần số thấp và yếu dần với tần số cao.

### 4. Gợi ý tìm thêm mô phỏng

- search: transfer function intuition control systems
- search: RC low pass frequency response visualization
- search: poles and stability animation

### 5. Bài toán mẫu có bối cảnh thực

Xét mạch RC:
$$ RC\,y'+y=x. $$
Áp Laplace với điều kiện đầu bằng 0:
$$ (RC\,s+1)Y=X. $$
Suy ra
$$ H(s)=\frac{Y}{X}=\frac{1}{RC\,s+1}. $$
Nếu đầu vào là bước đơn vị
$$ x(t)=1,\qquad X(s)=\frac{1}{s}, $$
thì
$$ Y(s)=\frac{1}{s(RC\,s+1)}. $$
Lấy ngược được
$$ y(t)=1-e^{-t/(RC)}. $$
Ví dụ này cho thấy rất rõ luồng tư duy: hàm truyền mô tả hộp đen, đầu vào cụ thể tạo ra đầu ra cụ thể.

### 6. Phân tầng độ khó

**Bậc đại học.** Dẫn xuất đúng hàm truyền từ ODE đầu vào - đầu ra với điều kiện đầu bằng 0.

**Bậc sau đại học.** Đi tiếp sang cực, zero, đáp ứng tần số và ổn định nội tại của hệ.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần hàm truyền rất phù hợp cho sinh viên lần đầu gặp ngôn ngữ hệ thống.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều ví dụ nối Laplace với mạch điện và hệ thống.
- Ross — *Differential Equations*: ngắn gọn và hữu ích để ôn ý tưởng cốt lõi của transfer function.
