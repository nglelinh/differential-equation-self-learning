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
## Mục tiêu
Bài học này giúp sinh viên hiểu tích chập như phép mô tả đầu ra của một hệ tuyến tính dựa trên việc cộng dồn phản ứng với các đầu vào quá khứ, biết phát biểu và sử dụng định lý
$$ \mathcal{L}\{f*g\}=FG, $$
và thấy rằng tích chập chính là cầu nối giữa ODE, đáp ứng xung và quan điểm hệ thống.

## Kiến thức nền
Sinh viên cần nắm Laplace, delta, Heaviside và ý tưởng đáp ứng xung cơ bản. Kỹ năng đổi thứ tự tích phân hữu ích, nhưng bài học này có thể được tiếp cận rất tốt bằng trực giác hệ thống trước rồi mới viết công thức.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-07 Định lý Tích chập]({{ site.imgurl }}/chapter_img/chapter03/03_07_convolution.svg)

Nếu ta biết một hệ phản ứng thế nào với một xung rất ngắn, liệu có thể dựng phản ứng của nó với một tín hiệu bất kỳ hay không? Trong các hệ tuyến tính bất biến theo thời gian, câu trả lời là có. Ta xem tín hiệu vào như tổng liên tục của vô số xung nhỏ, rồi cộng các phản ứng tương ứng. Toán học của ý tưởng này chính là tích chập.

Đây là một bài có ý nghĩa khái niệm rất lớn. Trước đó, Laplace mới chủ yếu là công cụ giải phương trình. Với tích chập, Laplace trở thành ngôn ngữ của hệ thống: đầu vào, đầu ra, đáp ứng xung và bộ nhớ của hệ đều đi vào cùng một khung thống nhất.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Tích chập nói rằng đầu ra hiện tại của hệ không chỉ phụ thuộc vào đầu vào hiện tại, mà là tổng ảnh hưởng của toàn bộ đầu vào quá khứ, mỗi phần được cân theo cách hệ phản ứng sau một khoảng trễ nhất định.

### Cách nhìn hình ảnh
Nếu $$ g(t) $$ là đáp ứng xung của hệ, còn $$ f(t) $$ là đầu vào, thì để tính đầu ra tại thời điểm $$ t $$, ta xem từng thời điểm quá khứ $$ \tau $$, lấy lượng đầu vào $$ f(\tau) $$, rồi nhân với phản ứng mà hệ còn "ghi nhớ" sau thời gian $$ t-\tau $$, tức là $$ g(t-\tau) $$. Sau đó cộng hết từ $$ 0 $$ đến $$ t $$.

### Cách nhìn hình thức
Tích chập của hai hàm $$ f,g $$ trên $$ t\ge 0 $$ được định nghĩa bởi
$$ (f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
Định lý tích chập phát biểu:
$$ \mathcal{L}\{f*g\}=F(s)G(s). $$
Ngược lại,
$$ \mathcal{L}^{-1}\{F(s)G(s)\}=f*g. $$
Đây là công cụ cực mạnh khi việc lấy Laplace ngược trực tiếp khó khăn.

## Những ngộ nhận thường gặp
- "Tích chập chỉ là một kỹ thuật tích phân mới." Sai. Nó mang nghĩa hệ thống rất sâu.
- "Công thức đối xứng trong $$ f $$ và $$ g $$ nên vai trò của chúng hoàn toàn như nhau." Về đại số thì đúng, nhưng trong ứng dụng ta thường gán một hàm là đầu vào, một hàm là đáp ứng xung.
- "Nếu đã có tích chập thì không cần Laplace." Không đúng. Hai công cụ bổ sung cho nhau rất mạnh.
- "Tích chập luôn làm bài toán dễ hơn." Không hẳn. Đôi khi nó là cách hiểu khái niệm tốt hơn là cách tính ngắn hơn.

## Tiến trình học tập đề xuất
### Bước 1: Hiểu bằng lời ý nghĩa tích lũy theo quá khứ
Đây là linh hồn của bài học.

### Bước 2: Viết công thức tích chập
Nhận ra miền tam giác $$ 0\le \tau\le t $$.

### Bước 3: Kết nối với Laplace
Tích chập trong thời gian thành phép nhân trong miền $$ s $$.

### Bước 4: Dùng để giải bài toán cụ thể
Đặc biệt khi biết đáp ứng xung.

### Các checkpoint
- Sinh viên có diễn giải được $$ g(t-\tau) $$ bằng lời hay không.
- Sinh viên có nhớ cận tích phân từ 0 đến $$ t $$ hay không.
- Sinh viên có hiểu vì sao tích chập phù hợp tự nhiên với hệ có bộ nhớ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Tính tích chập trực tiếp
Cho
$$ f(t)=1,\qquad g(t)=t. $$
Khi đó
$$ (f*g)(t)=\int_0^t 1\cdot (t-\tau)\,d\tau. $$
Tính được
$$
(f*g)(t)=\left[t\tau-\frac{\tau^2}{2}\right]_0^t=\frac{t^2}{2}.
$$
Ta có thể kiểm tra bằng Laplace:
$$
\mathcal{L}\{1\}=\frac{1}{s},\qquad \mathcal{L}\{t\}=\frac{1}{s^2},
$$
nên
$$ F(s)G(s)=\frac{1}{s^3}. $$
Lấy ngược:
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^3}\right\}=\frac{t^2}{2},
$$
khớp hoàn toàn.

### Ví dụ 2: Từ miền $$ s $$ sang tích chập
Tính
$$ \mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}. $$
Ta nhận ra
$$ \frac{1}{s(s+1)}=\frac{1}{s}\cdot \frac{1}{s+1}. $$
Vậy
$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1*e^{-t}.
$$
Do đó
$$
(1*e^{-t})(t)=\int_0^t e^{-(t-\tau)}\,d\tau=1-e^{-t}.
$$
Đây là một ví dụ rất tốt vì vừa ngắn vừa cho thấy ý nghĩa trực tiếp.

### Ví dụ 3: Đáp ứng của hệ với đầu vào tùy ý
Giả sử đáp ứng xung của một hệ là
$$ h(t)=e^{-t}, $$
còn đầu vào là $$ f(t) $$. Khi đó đầu ra là
$$ y(t)=\int_0^t f(\tau)e^{-(t-\tau)}\,d\tau. $$
Đây là trung bình có trọng số của toàn bộ đầu vào quá khứ, với trọng số suy giảm theo độ cũ của tín hiệu. Ý nghĩa "bộ nhớ ngắn dần" của hệ lộ ra rất rõ.

### Ví dụ 4: Tích chập với delta
Ta có
$$ f*\delta=f. $$
Điều này phản ánh đúng vai trò của delta như phần tử đơn vị của tích chập. Về mặt hệ thống, đầu vào là delta sẽ trả lại đúng đáp ứng xung.

## Câu hỏi khái niệm
1. Vì sao tích chập mô tả tự nhiên đầu ra của một hệ có bộ nhớ?
2. Vì sao phép nhân trong miền $$ s $$ lại tương ứng với tích chập trong miền thời gian?
3. Trong ứng dụng, khác biệt giữa "đầu vào" và "đáp ứng xung" quan trọng ở đâu dù tích chập là đối xứng?

## Bài toán ứng dụng
1. Một cảm biến có phản ứng mờ dần theo thời gian với mỗi kích thích nhỏ. Hãy giải thích vì sao đầu ra tổng là tích chập giữa đầu vào và hàm ghi nhớ của cảm biến.
2. Trong xử lý ảnh và tín hiệu, nhiều bộ lọc được mô tả bằng tích chập. Hãy nêu ý nghĩa trực giác của điều đó.
3. Một hệ cơ học nhận nhiều cú kích thích nhỏ liên tục. Hãy giải thích vì sao cộng dồn đáp ứng xung là mô hình hợp lý.

## Chiến lược giảng dạy tương tác
- Cho sinh viên mô tả bằng lời công thức tích chập trước khi tính toán.
- Dùng hình vẽ miền tam giác tích phân để giúp các em không bị lẫn cận.
- So sánh bài tính trực tiếp tích chập với bài tính qua Laplace để thấy hai cách nhìn khớp nhau.
- Tổ chức hoạt động hỏi đáp: "Nếu hệ ghi nhớ quá khứ rất lâu thì hàm đáp ứng xung sẽ trông như thế nào?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên để sinh viên yếu bắt đầu từ các ví dụ cực đơn giản như $$ 1*t $$, $$ 1*e^{-t} $$ trước khi nói về hệ thống. Khi đã quen với công thức, phần ý nghĩa sẽ dễ hấp thụ hơn.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi chứng minh định lý tích chập bằng cách đổi thứ tự tích phân, hoặc so sánh tích chập liên tục với phiên bản rời rạc trong xử lý tín hiệu số.

## Tóm tắt dễ nhớ
Tích chập là phép cộng dồn ảnh hưởng của toàn bộ quá khứ lên hiện tại. Với Laplace,
$$ \mathcal{L}\{f*g\}=FG. $$
Muốn hiểu hệ tuyến tính, hãy nhớ: biết đáp ứng xung gần như là biết toàn bộ hệ, và tích chập chính là công thức dựng đầu ra từ đáp ứng ấy.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Đầu ra của hệ từ đáp ứng xung
- Bài toán: Nếu biết hệ phản ứng với delta như thế nào, ta muốn dựng đầu ra cho một tín hiệu vào bất kỳ.
- Mô hình:
$$ y(t)=(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau. $$
- Giả thiết và giới hạn: Hệ tuyến tính và bất biến theo thời gian.
- Diễn giải: Đầu ra hiện tại là tích lũy ảnh hưởng của toàn bộ quá khứ.

#### Dược động học và bộ nhớ của cơ thể
- Bài toán: Nồng độ thuốc hiện tại phản ánh tổng ảnh hưởng của các liều đã được đưa vào trước đó.
- Mô hình: Input là liều dùng, kernel là đáp ứng suy giảm của cơ thể.
- Giả thiết và giới hạn: Hệ tuyến tính hóa và không đổi theo thời gian.
- Diễn giải: Tích chập mang nghĩa rất tự nhiên như "tổng chồng ảnh hưởng của quá khứ".

#### Kinh tế và hệ có quán tính
- Bài toán: Một cú sốc chính sách không biến mất ngay mà để lại ảnh hưởng suy giảm theo thời gian.
- Mô hình: Response = shock * memory kernel.
- Giả thiết và giới hạn: Chỉ là xấp xỉ tuyến tính của một hệ phức tạp hơn.
- Diễn giải: Convolution là ngôn ngữ toán học của bộ nhớ hệ thống.

### 2. Trực giác bổ sung và các kết nối

Định lý tích chập
$$ \mathcal{L}\{f*g\}=FG $$
là một trong những công thức đẹp nhất của chương vì nó biến tích lũy theo quá khứ ở miền thời gian thành phép nhân đơn giản trong miền $$ s $$. Bài này nối trực tiếp với hàm truyền: nếu biết hàm truyền, ta biết đáp ứng xung, và từ đó biết đầu ra qua tích chập.

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

Cho
$$ f(t)=1,\qquad g(t)=e^{-t}. $$
Khi đó
$$ (f*g)(t)=\int_0^t e^{-(t-\tau)}\,d\tau. $$
Tính được
$$ (f*g)(t)=1-e^{-t}. $$
Từ góc nhìn hệ thống, nếu đầu vào là bước đơn vị và kernel suy giảm mũ là "bộ nhớ" của hệ, thì đầu ra tăng dần về 1 thay vì nhảy tức thì lên 1.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo công thức tích chập và hiểu bằng lời ý nghĩa của $$ g(t-\tau) $$.

**Bậc sau đại học.** Chứng minh định lý bằng đổi thứ tự tích phân, rồi nối với đáp ứng xung và hệ LTI tổng quát.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần tích chập rất phù hợp cho bước chuyển sang ngôn ngữ hệ thống.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ kết nối tích chập với forcing thực tế.
- Ross — *Differential Equations*: hữu ích để ôn lại công thức và vài ví dụ mẫu ngắn.
