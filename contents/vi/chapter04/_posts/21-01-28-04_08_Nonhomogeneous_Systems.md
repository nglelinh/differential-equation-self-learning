---
layout: post
title: "04-08 Hệ Không thuần nhất"
chapter: '04'
order: 8
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên giải hệ tuyến tính không thuần nhất, hiểu công thức biến thiên hằng số cho hệ, và thấy rõ cách ngoại lực hoặc nguồn ngoài làm biến dạng quỹ đạo tự nhiên của hệ. Sinh viên cũng sẽ hiểu công thức tích phân kiểu Duhamel như phiên bản hệ của đáp ứng cưỡng bức.

## Kiến thức nền

Sinh viên cần nắm hệ thuần nhất, ma trận nghiệm cơ bản, ma trận mũ và tích phân của hàm vector. Trực giác về "phần tự do" và "phần cưỡng bức" từ ODE một ẩn sẽ giúp bài học này bớt lạ.

## Dẫn nhập

![Hệ tuyến tính không thuần nhất với lực cưỡng bức]({{ site.imgurl }}/chapter_img/chapter04/08_nonhomogeneous_systems.svg)

Một hệ thực hiếm khi tự tiến hóa hoàn toàn cô lập. Nó thường bị thúc bởi nguồn ngoài, lực ngoài, dòng vào, tín hiệu điều khiển hoặc nhiễu. Khi đó, thay vì
$$ \mathbf{x}'=A\mathbf{x}, $$
ta có
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
Nghiệm không còn chỉ là sự pha trộn của các mode riêng tự do, mà còn chứa dấu vết của toàn bộ lịch sử forcing.

Điểm hay của bài học này là ngoại lực không phá hỏng hoàn toàn cấu trúc đã học. Ngược lại, toàn bộ lý thuyết thuần nhất vẫn là khung xương. Phần mới chỉ là cách cho các hằng số trong nghiệm thuần nhất biến thiên theo thời gian hoặc, tương đương, cách tích lũy ảnh hưởng forcing qua ma trận mũ.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nghiệm của hệ không thuần nhất là tổng của hai câu chuyện: hệ tự muốn đi đâu nếu không ai tác động, và hệ bị đẩy lệch đi ra sao bởi lực ngoài. Ngoại lực không chỉ tác động tức thời; nó để lại dấu vết tích lũy theo thời gian.

### Cách nhìn hình ảnh

Trong mặt phẳng pha, hệ thuần nhất cho ta một trường vector cố định bởi $$ A\mathbf{x} $$. Khi thêm $$ \mathbf{g}(t) $$, trường vector bị dời hoặc bẻ theo thời gian. Quỹ đạo vì thế không còn chỉ xoắn vào hay ra quanh gốc, mà có thể bị kéo lệch, dịch cân bằng hoặc có thành phần cưỡng bức ổn định.

### Cách nhìn hình thức

Với
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t), $$
nếu $$ \Phi(t) $$ là ma trận nghiệm cơ bản của hệ thuần nhất, thì nghiệm tổng quát có dạng
$$
\mathbf{x}(t)=\Phi(t)\mathbf{c}+\Phi(t)\int \Phi(t)^{-1}\mathbf{g}(t)\,dt.
$$
Nếu dùng ma trận mũ và điều kiện đầu tại $$ t_0 $$, ta có công thức thuận tiện:
$$
\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}_0+\int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$

## Những ngộ nhận thường gặp

- "Ngoại lực chỉ cộng thêm một chút vào nghiệm thuần nhất." Sai. Nó có thể thay đổi hoàn toàn hành vi dài hạn.
- "Biến thiên hằng số cho hệ chỉ là phiên bản dài dòng của công thức một ẩn." Một phần đúng, nhưng điểm quan trọng là nó cho thấy mọi forcing được truyền qua ma trận tiến hóa.
- "Nếu $$ \mathbf{g}(t) $$ nhỏ thì có thể bỏ qua." Không nhất thiết, đặc biệt về hành vi dài hạn.
- "Nghiệm riêng là thứ hoàn toàn tách rời cấu trúc của hệ thuần nhất." Sai. Chính ma trận nghiệm cơ bản chi phối nó.

## Tiến trình học tập đề xuất

### Bước 1: Giải hoặc hiểu phần thuần nhất

Không có khung xương này thì forcing khó đọc đúng.

### Bước 2: Dùng biến thiên hằng số hoặc công thức Duhamel

Chọn dạng phù hợp nhất với dữ kiện.

### Bước 3: Tách phần quá độ và phần cưỡng bức

Đây là bước diễn giải trọng tâm.

### Bước 4: Xét hành vi dài hạn

Hỏi forcing thắng hay phần tự do thắng.

### Các checkpoint

- Sinh viên có nhớ công thức nghiệm với tích phân ma trận mũ hay không.
- Sinh viên có phân biệt phần do điều kiện đầu và phần do forcing hay không.
- Sinh viên có đọc đúng hành vi dài hạn từ hai phần này hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Nguồn hằng

Xét
$$
\mathbf{x}'=
\begin{pmatrix}
-1 & 0\\
0 & -2
\end{pmatrix}\mathbf{x}
+
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Phần thuần nhất có nghiệm
$$
\mathbf{x}_h(t)=
c_1e^{-t}
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^{-2t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Ta tìm nghiệm riêng hằng
$$
\mathbf{x}_p=
\begin{pmatrix}
a\\
b
\end{pmatrix}.
$$
Thay vào:
$$
0=
\begin{pmatrix}
-a\\
-2b
\end{pmatrix}
+
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
nên
$$ a=1,\qquad b=0. $$
Vậy nghiệm tổng quát là
$$
\mathbf{x}(t)=\mathbf{x}_h(t)+
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Hệ tiến về trạng thái cân bằng mới do forcing thiết lập.

### Ví dụ 2: Công thức Duhamel

Nếu
$$ \mathbf{x}(0)=\mathbf{x}_0, $$
thì
$$
\mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
Hạng đầu là phần tự do, hạng tích phân là phần cưỡng bức. Công thức này đáng để sinh viên nhớ vì nó làm lộ ý nghĩa hệ thống rất rõ.

### Ví dụ 3: Forcing dao động

Nếu $$ \mathbf{g}(t) $$ dao động điều hòa, nghiệm riêng thường mang cùng tần số nhưng có biên độ và pha do ma trận $$ A $$ quyết định. Đây là phiên bản hệ của cộng hưởng cưỡng bức đã gặp ở ODE một ẩn.

### Ví dụ 4: Ngoại lực và lịch sử

Trong tích phân
$$ \int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds, $$
mọi thời điểm quá khứ $$ s $$ đều đóng góp vào hiện tại. Điều này giúp sinh viên thấy hệ không thuần nhất là hệ có "trí nhớ cưỡng bức" thông qua toán tử tiến hóa.

## Câu hỏi khái niệm

1. Vì sao nghiệm của hệ không thuần nhất vẫn phải dựa trên ma trận nghiệm cơ bản của hệ thuần nhất?
2. Hai phần trong công thức Duhamel mang hai ý nghĩa vật lý nào?
3. Vì sao forcing có thể thay đổi hoàn toàn trạng thái dài hạn dù phần tự do tự nó suy giảm?

## Bài toán ứng dụng

1. Một hệ điều khiển liên tục bị bơm tín hiệu tham chiếu từ bên ngoài. Hãy giải thích vì sao phần cưỡng bức là thứ quyết định trạng thái mong muốn.
2. Một mô hình ngăn có dòng vào đều đặn. Hãy diễn giải ý nghĩa của trạng thái cân bằng mới do nguồn ngoài sinh ra.
3. Một hệ dao động chịu lực tuần hoàn nhỏ nhưng kéo dài. Hãy thảo luận vì sao tác động tích lũy có thể đáng kể.

## Chiến lược giảng dạy tương tác

- Cho sinh viên tách một nghiệm thành phần tự do và phần cưỡng bức bằng lời trước khi viết công thức.
- So sánh trực tiếp một hệ không nguồn và cùng hệ đó có nguồn hằng để thấy trạng thái dài hạn thay đổi ra sao.
- Hỏi lớp: "Nếu tắt forcing sau một thời gian dài, hệ sẽ còn lại điều gì?"
- Dùng màu khác nhau cho hai hạng trong công thức Duhamel để nhấn mạnh hai vai trò.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu làm trước với forcing hằng hoặc forcing rất đơn giản, vì mục tiêu chính là hiểu cấu trúc hai phần chứ không phải kỹ thuật tích phân nặng.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi suy ra công thức Duhamel từ phép đặt
$$ \mathbf{x}(t)=\Phi(t)\mathbf{u}(t), $$
hoặc phân tích trường hợp forcing tuần hoàn và cộng hưởng trong hệ 2 chiều.

## Tóm tắt dễ nhớ

Hệ không thuần nhất vẫn dựa trên bộ khung của hệ thuần nhất. Nghiệm gồm phần do điều kiện đầu và phần do forcing tích lũy qua ma trận mũ. Muốn hiểu hệ chịu ngoại lực, hãy luôn hỏi: hệ tự nó làm gì, ngoại lực kéo nó đi đâu, và phần nào thắng về lâu dài.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ điều khiển có forcing
- Bài toán: Một hệ trạng thái vừa có động lực nội tại vừa nhận tín hiệu điều khiển bên ngoài.
- Mô hình:
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
- Giả thiết và giới hạn: Tuyến tính, hệ số hằng.
- Diễn giải: Nghiệm gồm phần do trạng thái đầu và phần do forcing tích lũy theo thời gian.

#### Dòng vào đều trong mô hình ngăn
- Bài toán: Một hệ nhiều ngăn có thêm nguồn cấp đều đặn từ ngoài.
- Mô hình:
$$
\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}_0+\int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
- Giả thiết và giới hạn: Hệ tuyến tính hóa của dòng vào - dòng ra.
- Diễn giải: Công thức Duhamel mô tả rõ forcing đi qua "bộ nhớ" của hệ như thế nào.

#### Nhiễu nhỏ nhưng kéo dài
- Bài toán: Một forcing nhỏ nhưng duy trì lâu có thể quyết định trạng thái dài hạn.
- Mô hình: Cùng hệ không thuần nhất.
- Giả thiết và giới hạn: Tuyến tính và forcing đã biết.
- Diễn giải: "Nhỏ" về biên độ không đồng nghĩa "không quan trọng" về lâu dài.

### 2. Trực giác bổ sung và các kết nối

Hệ không thuần nhất là nơi sinh viên thấy rõ hơn bao giờ hết cấu trúc "tự do + cưỡng bức". Đây cũng là phiên bản hệ của biến thiên hằng số ở chương 2 và là tiền đề cho công thức Duhamel, Green function và convolution trong các chương sau.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = np.array([[-1, 0],
              [ 0, -2]], dtype=float)

def forcing(t):
    return np.array([1.0, 0.0])

def system(t, X):
    return A @ X + forcing(t)

t = np.linspace(0, 8, 500)
sol = solve_ivp(system, [0, 8], [0, 0], t_eval=t)

plt.plot(sol.t, sol.y[0], label="x1(t)")
plt.plot(sol.t, sol.y[1], label="x2(t)")
plt.xlabel("t")
plt.ylabel("State")
plt.title("Hệ không thuần nhất với nguồn hằng")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: variation of constants for linear systems visualization
- search: Duhamel formula intuition ODE system
- search: forced linear system state response

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$
\mathbf{x}'=
\begin{pmatrix}
-1 & 0\\
0 & -2
\end{pmatrix}\mathbf{x}
+
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Phần thuần nhất suy giảm về 0. Với forcing hằng, ta tìm trạng thái cân bằng mới từ
$$
A\mathbf{x}_*=-
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
suy ra
$$
\mathbf{x}_*=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Điều này cho thấy forcing đã dời điểm hút từ gốc sang một trạng thái mới.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung hiểu công thức nghiệm và tách phần tự do với phần cưỡng bức.

**Bậc sau đại học.** Kết nối với công thức Duhamel, đáp ứng hệ thống và tác động dài hạn của forcing.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: phần hệ không thuần nhất và biến thiên hằng số rất nền tảng.
- Arnold, *Ordinary Differential Equations*: tốt cho trực giác về việc forcing biến dạng dòng chảy tuyến tính.
