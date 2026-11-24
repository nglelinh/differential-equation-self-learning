---
layout: post
title: "03-07 Định lý Tích chập"
chapter: '03'
order: 7
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---

Biến đổi Laplace bảo toàn phép cộng, nhưng **tuyệt đối không** bảo toàn phép nhân thông thường: $\mathcal{L}\{f \cdot g\} \ne F(s)G(s)$! Vậy phép toán nào trong miền thời gian tương ứng với phép nhân $F(s)G(s)$ trong miền Laplace? Câu trả lời là một phép toán trung tâm của toàn bộ giải tích, xử lý tín hiệu và mạng nơ-ron tích chập (CNN): **phép Tích chập (Convolution)** $(f * g)(t) = \int_0^t f(\tau)g(t - \tau)\,d\tau$!

## Bản đồ kiến thức nền: Bốn trụ cột của Định lý Tích chập

1. **Định nghĩa & Ý nghĩa vật lý ("Bộ nhớ của hệ")**:
   $(f * g)(t) = \int_0^t f(\tau)g(t - \tau)\,d\tau$ cộng dồn ảnh hưởng của mọi ngoại lực $g(\tau)$ trong quá khứ ($0 \le \tau \le t$), mỗi lực được nhân trọng số bởi đáp ứng xung $f(t - \tau)$ sau khoảng thời gian trôi qua $t - \tau$.
2. **Định lý Tích chập ($\mathcal{L}\{f * g\} = F(s)\cdot G(s)$)**:
   Chiều xuôi giúp tính nhanh biến đổi Laplace của tích phân tích chập; chiều ngược $\mathcal{L}^{-1}\{F(s)G(s)\} = (f * g)(t)$ giúp giải PTVP với **mọi** ngoại lực $g(t)$ kể cả khi không có công thức tường minh cho $G(s)$!
3. **Các tính chất đại số đẹp mắt**:
   Giao hoán ($f * g = g * f$), kết hợp và phân phối—và đặc biệt hàm xung Dirac $\delta(t)$ chính là **phần tử đơn vị**: $(f * \delta)(t) = f(t)$!
4. **Giải phương trình tích phân Volterra**:
   Phương trình dạng $y(t) + \int_0^t k(t - \tau)y(\tau)\,d\tau = g(t)$ lập tức trở thành phương trình đại số $Y(s) + K(s)Y(s) = G(s)$ trong miền Laplace!

## Mục tiêu
Bài học này giúp sinh viên hiểu tích chập như phép cộng dồn đáp ứng của một hệ tuyến tính đối với toàn bộ lịch sử đầu vào, nắm vững và vận dụng định lý $$ \mathcal{L}\{f*g\}=FG $$, đồng thời thấy vai trò cầu nối của tích chập giữa phương trình vi phân, đáp ứng xung và lý thuyết hệ thống.

## Kiến thức nền
Sinh viên cần nắm biến đổi Laplace, hàm delta, hàm bước Heaviside và ý tưởng đáp ứng xung. Kỹ năng đổi thứ tự tích phân hữu ích khi chứng minh, nhưng bài học có thể tiếp cận tự nhiên từ trực giác hệ thống trước rồi mới đi vào công thức.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-07 Định lý Tích chập]({{ site.imgurl }}/chapter_img/chapter03/03_07_convolution.svg)

Nếu biết một hệ phản ứng ra sao trước một xung tức thời, liệu ta có thể xây dựng đáp ứng của nó cho một tín hiệu đầu vào bất kỳ hay không? Đối với các hệ tuyến tính bất biến theo thời gian (LTI), câu trả lời là có: ta xem tín hiệu đầu vào như tổng liên tục của vô số xung nhỏ tại các thời điểm quá khứ rồi cộng dồn các đáp ứng tương ứng. Phép toán mô tả quá trình này chính là tích chập.

Với tích chập, biến đổi Laplace vượt ra khỏi vai trò công cụ giải từng phương trình riêng lẻ để trở thành ngôn ngữ thống nhất cho đầu vào, đầu ra, đáp ứng xung và bộ nhớ của hệ thống.

### Khung giải thích (nên đọc chậm): Tính $\mathcal{L}^{-1}\!\left\{\frac{1}{s(s^2 + 1)}\right\}$ bằng Định lý Tích chập và đối chiếu với tách phân thức

Chọn $F(s) = \frac{1}{s} \leftrightarrow f(t) = 1$ và $G(s) = \frac{1}{s^2 + 1} \leftrightarrow g(t) = \sin t$:
1. **Áp dụng Định lý Tích chập**:
   $$\mathcal{L}^{-1}\!\left\{\frac{1}{s}\cdot\frac{1}{s^2 + 1}\right\} = (1 * \sin)(t) = \int_0^t 1 \cdot \sin(t - \tau)\,d\tau.$$
2. **Tính tích phân** (đổi biến $u = t - \tau$, hoặc dùng giao hoán $\int_0^t \sin\tau\,d\tau$):
   $$\int_0^t \sin\tau\,d\tau = \big[-\cos\tau\big]_0^t = \mathbf{1 - \cos t}.$$
3. **Đối chiếu với tách phân thức**:
   $\frac{1}{s(s^2+1)} = \frac{1}{s} - \frac{s}{s^2+1} \implies \mathcal{L}^{-1} = \mathbf{1 - \cos t}$—khớp từng ký tự! Đặc biệt, nhân $G(s)$ với $\frac{1}{s}$ trong miền Laplace luôn tương đương với **lấy tích phân $\int_0^t g(\tau)\,d\tau$** trong miền thời gian!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Tích chập cho biết đầu ra tại thời điểm hiện tại không chỉ phụ thuộc vào đầu vào ngay lúc đó, mà là tổng tích lũy ảnh hưởng của toàn bộ đầu vào trong quá khứ, với trọng số xác định bởi cách hệ còn lưu giữ tác động sau mỗi khoảng trễ.

### Cách nhìn hình ảnh
Nếu $$ g(t) $$ là đáp ứng xung của hệ và $$ f(t) $$ là tín hiệu vào, thì để tính đầu ra tại thời điểm $$ t $$, ta xét từng thời điểm quá khứ $$ \tau \in [0,t] $$, lấy giá trị đầu vào $$ f(\tau) $$, nhân với mức đáp ứng còn lại sau khoảng trễ $$ t-\tau $$ là $$ g(t-\tau) $$, rồi tích phân từ $$ 0 $$ đến $$ t $$.

### Cách nhìn hình thức
Tích chập của hai hàm $$ f,g $$ xác định trên $$ t\ge 0 $$ được định nghĩa bởi
$$ (f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
Định lý tích chập phát biểu:
$$ \mathcal{L}\{f*g\}=F(s)G(s), $$
và theo chiều ngược lại:
$$ \mathcal{L}^{-1}\{F(s)G(s)\}=f*g. $$
Công thức này đặc biệt hữu ích khi cần biến đổi ngược một tích hai hàm trong miền $$ s $$.

## Những ngộ nhận thường gặp
- "Tích chập chỉ là một phép tính tích phân mới." Sai: nó biểu diễn trực tiếp cơ chế đáp ứng của hệ tuyến tính có bộ nhớ.
- "Vì $$ f*g = g*f $$ nên vai trò hai hàm luôn hoàn toàn giống nhau." Đúng về mặt đại số, nhưng trong ứng dụng ta thường phân biệt rõ một hàm là tín hiệu đầu vào và hàm kia là đáp ứng xung của hệ.
- "Có tích chập rồi thì không cần biến đổi Laplace." Không đúng: hai công cụ bổ trợ chặt chẽ cho nhau.
- "Dùng tích chập luôn tính nhanh hơn phân thức đơn." Không hẳn: đôi khi tích chập mạnh hơn ở khía cạnh biểu diễn tổng quát và diễn giải khái niệm.

## Tiến trình học tập đề xuất
### Bước 1: Nắm trực giác tích lũy theo quá khứ
Hiểu ý nghĩa của từng yếu tố trước khi đi vào công thức tích phân.

### Bước 2: Viết đúng công thức tích chập
Chú ý cận tích phân từ $$ 0 $$ đến $$ t $$ và đối số trễ $$ t-\tau $$.

### Bước 3: Kết nối với biến đổi Laplace
Phép tích chập trong miền thời gian tương ứng với phép nhân thông thường trong miền $$ s $$.

### Bước 4: Vận dụng giải bài toán cụ thể
Áp dụng cho cả bài toán biến đổi ngược và bài toán tìm đầu ra từ đáp ứng xung.

### Các checkpoint
- Sinh viên có giải thích được bằng lời ý nghĩa của thừa số $$ g(t-\tau) $$ hay không.
- Sinh viên có đặt đúng cận tích phân từ $$ 0 $$ đến $$ t $$ hay không.
- Sinh viên có hiểu vì sao tích chập mô tả tự nhiên hệ thống có bộ nhớ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Tính tích chập trực tiếp
Cho $$ f(t)=1 $$ và $$ g(t)=t $$. Theo định nghĩa:
$$ (f*g)(t)=\int_0^t 1\cdot (t-\tau)\,d\tau=\left[t\tau-\frac{\tau^2}{2}\right]_0^t=\frac{t^2}{2}. $$
Kiểm tra lại bằng biến đổi Laplace: $$ \mathcal{L}\{1\}=\frac{1}{s} $$ và $$ \mathcal{L}\{t\}=\frac{1}{s^2} $$, nên $$ F(s)G(s)=\frac{1}{s^3} $$, cho kết quả biến đổi ngược $$ \mathcal{L}^{-1}\left\{\frac{1}{s^3}\right\}=\frac{t^2}{2} $$, trùng khớp hoàn toàn.

### Ví dụ 2: Biến đổi ngược bằng định lý tích chập
Tính $$ \mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\} $$. Nhận thấy $$ \frac{1}{s(s+1)}=\frac{1}{s}\cdot \frac{1}{s+1} $$, ta có
$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1*e^{-t}=\int_0^t e^{-(t-\tau)}\,d\tau=1-e^{-t}.
$$

### Ví dụ 3: Đáp ứng của hệ với đầu vào tùy ý
Giả sử đáp ứng xung của hệ là $$ h(t)=e^{-t} $$ và đầu vào là $$ f(t) $$. Đầu ra tại thời điểm $$ t $$ là
$$ y(t)=\int_0^t f(\tau)e^{-(t-\tau)}\,d\tau. $$
Biểu thức này là tổng có trọng số của toàn bộ đầu vào quá khứ, trong đó các thời điểm càng xa hiện tại có trọng số suy giảm càng mạnh theo $$ e^{-(t-\tau)} $$.

### Ví dụ 4: Tích chập với hàm delta
Ta có $$ f*\delta=f $$, cho thấy $$ \delta $$ đóng vai trò phần tử đơn vị của phép tích chập. Về mặt hệ thống, đưa xung đơn vị vào sẽ trả lại đúng đáp ứng xung.

## Câu hỏi khái niệm
1. Vì sao tích chập mô tả tự nhiên đầu ra của một hệ có bộ nhớ?
2. Vì sao phép nhân trong miền $$ s $$ lại tương ứng với tích chập trong miền thời gian?
3. Dù tích chập có tính giao hoán, vì sao trong ứng dụng vẫn cần phân biệt hàm đầu vào và đáp ứng xung?

## Bài toán ứng dụng
1. Một cảm biến có phản ứng mờ dần theo thời gian sau mỗi kích thích nhỏ. Vì sao đầu ra tổng là tích chập giữa tín hiệu vào và hàm suy giảm của cảm biến?
2. Trong xử lý ảnh và tín hiệu, nhiều bộ lọc được biểu diễn bằng tích chập. Ý nghĩa trực quan của biểu diễn đó là gì?
3. Một hệ cơ học chịu chuỗi kích thích liên tục. Vì sao cộng dồn các đáp ứng xung là mô hình hợp lý khi hệ tuyến tính?

## Chiến lược giảng dạy tương tác
- Yêu cầu sinh viên diễn đạt bằng lời công thức tích chập trước khi tính tích phân.
- Minh họa miền tam giác $$ 0\le \tau\le t $$ để tránh nhầm lẫn cận tích phân.
- So sánh lời giải tính trực tiếp tích chập với lời giải qua biến đổi Laplace để củng cố niềm tin vào định lý.
- Đặt câu hỏi: "Nếu hệ lưu giữ tác động quá khứ rất lâu, hình dạng hàm đáp ứng xung sẽ như thế nào?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Bắt đầu từ các ví dụ ngắn như $$ 1*t $$ và $$ 1*e^{-t} $$ để làm quen phép tính trước khi mở rộng sang diễn giải hệ thống.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên chứng minh định lý tích chập bằng phép đổi thứ tự tích phân, hoặc so sánh tích chập liên tục với tích chập rời rạc trong xử lý tín hiệu số.

## Tóm tắt dễ nhớ
Tích chập cộng dồn ảnh hưởng của toàn bộ đầu vào quá khứ lên trạng thái hiện tại, và trong miền Laplace thỏa mãn $$ \mathcal{L}\{f*g\}=FG $$. Biết đáp ứng xung của hệ tuyến tính cho phép xây dựng đầu ra cho mọi đầu vào thông qua tích chập.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Xây dựng đầu ra từ đáp ứng xung
- Bài toán: Tính đầu ra cho đầu vào bất kỳ khi đã biết đáp ứng xung của hệ.
- Mô hình:
$$ y(t)=(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
- Giả thiết và giới hạn: Hệ tuyến tính bất biến theo thời gian với điều kiện đầu bằng 0.
- Diễn giải: Đầu ra hiện tại là tổng tích lũy của toàn bộ lịch sử đầu vào.

#### Dược động học và quá trình đào thải thuốc
- Bài toán: Nồng độ thuốc tại thời điểm hiện tại là tổng ảnh hưởng còn lại của các liều đã đưa vào trước đó.
- Mô hình: Đầu vào là tốc độ cấp thuốc, nhân tích chập là hàm suy giảm nồng độ của cơ thể.
- Giả thiết và giới hạn: Động học tuyến tính và thông số đào thải không đổi theo thời gian.
- Diễn giải: Tích chập thể hiện trực tiếp sự chồng chất của các liều dùng theo thời gian.

#### Cú sốc ngoại sinh trong kinh tế
- Bài toán: Một cú sốc chính sách không kết thúc tức thời mà để lại tác động suy giảm dần.
- Mô hình: Đáp ứng bằng tích chập giữa chuỗi cú sốc và nhân ghi nhớ của hệ.
- Giả thiết và giới hạn: Xấp xỉ tuyến tính cho một hệ kinh tế phức tạp hơn.
- Diễn giải: Tích chập là công cụ toán học mô tả tính quán tính và bộ nhớ của hệ.

### 2. Trực giác bổ sung và các kết nối

Định lý tích chập $$ \mathcal{L}\{f*g\}=FG $$ chuyển phép tích lũy theo quá khứ trong miền thời gian thành phép nhân đại số đơn giản trong miền $$ s $$. Nội dung này dẫn trực tiếp sang bài hàm truyền: biết hàm truyền nghĩa là biết đáp ứng xung, và từ đó tính được đầu ra qua tích chập.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 600)
dt = t[1] - t[0]
f = np.ones_like(t)
g = np.exp(-t)
y = np.convolve(f, g)[:len(t)] * dt

plt.plot(t, f, label="f(t)=1")
plt.plot(t, g, label="g(t)=e^{-t}")
plt.plot(t, y, label="(f*g)(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Tích chập như tích lũy ảnh hưởng quá khứ")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: convolution animation signal processing
- search: impulse response and convolution visualization
- search: moving overlap convolution intuition

### 5. Bài toán mẫu có bối cảnh thực

Cho $$ f(t)=1 $$ và $$ g(t)=e^{-t} $$. Tích chập tương ứng là
$$ (f*g)(t)=\int_0^t e^{-(t-\tau)}\,d\tau=1-e^{-t}. $$
Theo góc nhìn hệ thống, khi đầu vào là bước đơn vị và đáp ứng xung suy giảm theo hàm mũ, đầu ra không nhảy tức thời lên 1 mà tăng tiệm cận dần về 1.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo công thức tích chập, định lý tích chập và diễn giải ý nghĩa của $$ g(t-\tau) $$.

**Bậc sau đại học.** Chứng minh định lý bằng đổi thứ tự tích phân và liên hệ với lý thuyết hệ LTI tổng quát.

## Video tham khảo

- Xem trước: [Lec 21 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=3ejfkMHr_DE) — MIT OpenCourseWare, tiếng Anh. Bài giảng của giáo sư Mattuck về định lý tích chập trong biến đổi Laplace.
- [Laplace Transforms and Convolution](https://www.youtube.com/watch?v=WZMQdLW4COQ) — MIT OpenCourseWare, tiếng Anh. Trình bày mối liên hệ giữa biến đổi Laplace và phép tích chập.
- [Convolution and Green's Formula | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=IGk-7EKR35A) — MIT OpenCourseWare, tiếng Anh. Liên hệ tích chập với công thức Green cho bài toán giá trị đầu tuyến tính.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần tích chập trình bày rõ bước chuyển sang ngôn ngữ hệ thống.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ gắn tích chập với ngoại lực thực tế.
- Ross — *Differential Equations*: hữu ích để ôn ngắn gọn công thức và các ví dụ mẫu.
