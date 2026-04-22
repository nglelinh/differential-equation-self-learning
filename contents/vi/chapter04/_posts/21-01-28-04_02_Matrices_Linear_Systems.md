---
layout: post
title: "04-02 Ma trận và Hệ Tuyến tính"
chapter: '04'
order: 2
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên viết hệ tuyến tính dưới dạng ma trận, hiểu vì sao ma trận là bản tóm tắt động học của hệ, và nắm khái niệm ma trận nghiệm cơ bản như phiên bản hệ của nghiệm tổng quát. Đây là cửa ngõ để đưa đại số tuyến tính vào giải ODE hệ thống.

## Kiến thức nền

Sinh viên cần nắm vector, ma trận, phép nhân ma trận với vector và ý tưởng độc lập tuyến tính. Việc hiểu ODE một ẩn tuyến tính cũng giúp sinh viên nhận ra cách nguyên lý chồng chập được mở rộng cho hệ.

## Dẫn nhập

![Ma trận điều khiển sự tiến hóa của hệ tuyến tính]({{ site.imgurl }}/chapter_img/chapter04/02_matrices_linear_systems.svg)

Khi ta viết một hệ gồm nhiều phương trình thành một biểu thức ma trận duy nhất, điều ta đạt được không chỉ là sự gọn gàng. Ta đạt được một bản đồ cấu trúc của tương tác. Mỗi hàng của ma trận cho biết tốc độ thay đổi của một biến trạng thái phụ thuộc thế nào vào toàn bộ trạng thái, còn mỗi cột cho biết một thành phần trạng thái ảnh hưởng ra sao lên cả hệ.

Đây là bước rất quan trọng về mặt nhận thức. Trước đó, sinh viên có thể nhìn hệ như một danh sách phương trình đặt cạnh nhau. Sau bài học này, hệ cần được nhìn như một thực thể tuyến tính duy nhất với một toán tử tiến hóa là ma trận $$ A $$.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Ma trận $$ A $$ giống như "bộ luật tương tác" của hệ. Nó cho biết nếu ta đang ở trạng thái hiện tại $$ \mathbf{x} $$ thì hệ bị kéo theo những hướng nào, mạnh hay yếu đến đâu.

### Cách nhìn hình ảnh

Trong hệ hai chiều
$$ \mathbf{x}'=A\mathbf{x}, $$
ma trận $$ A $$ gán cho mỗi điểm $$ \mathbf{x} $$ một vector tiếp tuyến $$ A\mathbf{x} $$. Vì vậy, ma trận sinh ra trường vector trên mặt phẳng trạng thái. Đó là cầu nối đầu tiên từ đại số tuyến tính sang hình học pha.

### Cách nhìn hình thức

Một hệ tuyến tính thuần nhất hệ số hằng được viết
$$ \mathbf{x}'=A\mathbf{x}, $$
trong đó $$ A $$ là ma trận hằng cỡ $$ n\times n $$. Nếu có nguồn ngoài, ta viết
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
Nếu $$ \mathbf{x}_1,\ldots,\mathbf{x}_n $$ là các nghiệm vector độc lập tuyến tính của hệ thuần nhất, thì ma trận
$$
\Phi(t)=
\begin{pmatrix}
\lvert  & & \rvert\\
\mathbf{x}_1(t) & \cdots & \mathbf{x}_n(t)\\
\lvert  & & \rvert
\end{pmatrix}
$$
được gọi là ma trận nghiệm cơ bản, và mọi nghiệm của hệ đều có dạng
$$ \mathbf{x}(t)=\Phi(t)\mathbf{c}. $$

## Những ngộ nhận thường gặp

- "Ma trận chỉ là ký hiệu viết tắt." Sai. Nó mã hóa cấu trúc tương tác của hệ.
- "Mỗi cột của ma trận nghiệm cơ bản chỉ là một nghiệm ngẫu nhiên." Sai. Cần các cột độc lập tuyến tính để sinh toàn bộ không gian nghiệm.
- "Nếu giải được từng phương trình thành phần thì không cần ma trận." Thường không đúng, vì các phương trình ghép chặt với nhau.
- "Ma trận $$ A $$ chỉ ảnh hưởng tốc độ, không ảnh hưởng hình học." Sai. Chính $$ A $$ quyết định trường vector và chân dung pha.

## Tiến trình học tập đề xuất

### Bước 1: Viết hệ dưới dạng vector-matrix

Chuyển từ danh sách phương trình sang một biểu thức duy nhất.

### Bước 2: Đọc ý nghĩa của từng hàng và từng cột

Làm cho ma trận bớt trừu tượng.

### Bước 3: Hiểu nguyên lý chồng chập cho hệ

Tổ hợp tuyến tính của các nghiệm vẫn là nghiệm.

### Bước 4: Xây ma trận nghiệm cơ bản

Đây là khái niệm sẽ quay lại nhiều lần trong chương.

### Các checkpoint

- Sinh viên có viết đúng hệ thành $$ \mathbf{x}'=A\mathbf{x} $$ hay không.
- Sinh viên có hiểu vì sao cần đủ $$ n $$ nghiệm độc lập cho hệ $$ n $$ chiều hay không.
- Sinh viên có diễn giải được $$ A\mathbf{x} $$ như một vector vận tốc trạng thái hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Viết hệ dưới dạng ma trận

Xét
$$
\begin{cases}
x_1'=2x_1-x_2,\\
x_2'=3x_1+4x_2.
\end{cases}
$$
Đặt
$$
\mathbf{x}=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
2 & -1\\
3 & 4
\end{pmatrix}.
$$
Khi đó hệ viết gọn là
$$ \mathbf{x}'=A\mathbf{x}. $$
Điểm sư phạm ở đây là sinh viên thấy ngay ma trận gom toàn bộ hệ lại thành một phép nhân duy nhất.

### Ví dụ 2: Hệ chéo

Với
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
$$
hệ trở thành
$$
\begin{cases}
x_1'=2x_1,\\
x_2'=-x_2.
\end{cases}
$$
Ta giải được
$$ x_1=c_1e^{2t},\qquad x_2=c_2e^{-t}. $$
Do đó
$$
\mathbf{x}(t)=
c_1e^{2t}
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^{-t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Ví dụ này cho thấy các trục tọa độ đóng vai trò như hai hướng động học độc lập.

### Ví dụ 3: Ma trận nghiệm cơ bản

Từ ví dụ trên, ta có thể chọn hai nghiệm độc lập:
$$
\mathbf{x}_1(t)=e^{2t}
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{x}_2(t)=e^{-t}
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Ma trận nghiệm cơ bản là
$$
\Phi(t)=
\begin{pmatrix}
e^{2t} & 0\\
0 & e^{-t}
\end{pmatrix}.
$$
Mọi nghiệm đều viết dưới dạng
$$ \mathbf{x}(t)=\Phi(t)\mathbf{c}. $$
Đây là phiên bản hệ của "nghiệm tổng quát" đã quen ở ODE một ẩn.

### Ví dụ 4: Đọc hàng và cột của ma trận

Nếu trong một hệ, phần tử $$ a_{21} $$ lớn dương, điều đó nói rằng biến thứ nhất tác động mạnh theo chiều tăng lên tốc độ thay đổi của biến thứ hai. Cách đọc này giúp ma trận trở thành một đối tượng có nghĩa, không chỉ là bảng số.

## Câu hỏi khái niệm

1. Vì sao viết hệ dưới dạng ma trận không chỉ là tiết kiệm ký hiệu?
2. Mỗi hàng và mỗi cột của ma trận $$ A $$ có thể được đọc theo những nghĩa nào?
3. Vì sao ma trận nghiệm cơ bản là khái niệm trung tâm cho hệ tuyến tính?

## Bài toán ứng dụng

1. Trong mô hình kinh tế hai ngành, một biến đại diện cho sản lượng và biến kia cho nhu cầu. Hãy giải thích vì sao ma trận là ngôn ngữ phù hợp để mã hóa tương tác.
2. Trong sinh học, hai quần thể tác động lẫn nhau. Hãy diễn giải ý nghĩa của các hệ số ngoài đường chéo của ma trận.
3. Trong cơ học nhiều bậc tự do, vì sao việc gom hệ vào ma trận giúp mở đường cho phân tích trị riêng?

## Chiến lược giảng dạy tương tác

- Cho sinh viên chuyển qua lại giữa dạng hệ thành phần và dạng ma trận.
- Yêu cầu lớp mô tả bằng lời ý nghĩa của từng hệ số trong một ma trận nhỏ.
- Cho sinh viên xây ma trận nghiệm cơ bản từ hai nghiệm đã biết để thấy khái niệm này không xa lạ.
- Dùng màu khác nhau cho các cột của $$ \Phi(t) $$ để nhấn mạnh chúng là các nghiệm cơ sở.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu làm việc với hệ 2 chiều trước, vì ở đó mọi thứ vẫn nhìn thấy được bằng hình và bằng công thức. Cần nhấn mạnh thật rõ rằng vector nghiệm là một hàm theo thời gian, không phải một vector cố định.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi chứng minh trực tiếp rằng nếu $$ \Phi(t) $$ là ma trận nghiệm cơ bản thì mọi nghiệm đều có dạng $$ \Phi(t)\mathbf{c} $$, hoặc phân tích mối liên hệ giữa định thức của $$ \Phi(t) $$ và tính độc lập tuyến tính.

## Tóm tắt dễ nhớ

Hệ tuyến tính viết dưới dạng
$$ \mathbf{x}'=A\mathbf{x} $$
để lộ ra toán tử động học của hệ. Ma trận $$ A $$ sinh trường vector, còn ma trận nghiệm cơ bản $$ \Phi(t) $$ sinh toàn bộ không gian nghiệm. Khi hiểu được hai đối tượng này, sinh viên đã có bộ khung đại số cho toàn bộ chương.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tương tác loài trong sinh học
- Bài toán: Mỗi quần thể chịu ảnh hưởng bởi bản thân nó và loài khác.
- Mô hình tuyến tính hóa:
$$ \mathbf{x}'=A\mathbf{x}. $$
- Giả thiết và giới hạn: Chỉ đúng gần điểm cân bằng, chưa phản ánh phi tuyến toàn cục.
- Diễn giải: Ma trận $$ A $$ là bản đồ gọn của mọi ảnh hưởng chéo trong hệ.

#### Mạng điện nhiều nút
- Bài toán: Điện áp hoặc dòng trên nhiều phần tử thay đổi đồng thời và phụ thuộc lẫn nhau.
- Mô hình:
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
- Giả thiết và giới hạn: Tuyến tính, thông số hằng, gần điểm làm việc.
- Diễn giải: Viết dưới dạng ma trận giúp nhìn ra ngay cấu trúc ghép nối của cả mạng.

#### Mô hình vốn - hàng tồn kho
- Bài toán: Một biến kinh tế có thể làm tăng hoặc giảm tốc độ biến kia.
- Mô hình:
$$
\begin{pmatrix}
x_1'\\
x_2'
\end{pmatrix}
=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix}.
$$
- Giả thiết và giới hạn: Chỉ là mô hình hóa tuyến tính cục bộ.
- Diễn giải: Hàng và cột của ma trận nói rõ ai tác động lên ai.

### 2. Trực giác bổ sung và các kết nối

Viết hệ dưới dạng ma trận không phải chỉ để rút gọn ký hiệu. Nó đổi hẳn cách đọc hệ: ma trận $$ A $$ vừa là bộ luật tương tác, vừa là máy sinh trường vector. Đây là điểm nối thẳng với đại số tuyến tính: cơ sở nghiệm, độc lập tuyến tính và ma trận nghiệm cơ bản đều là các ý tưởng quen thuộc nhưng giờ mang nghĩa động học.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, -1],
              [3,  4]])
x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
X, Y = np.meshgrid(x, y)
U = 2*X - Y
V = 3*X + 4*Y
N = np.sqrt(U**2 + V**2)

plt.quiver(X, Y, U / N, V / N, color="teal")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Trường vector của x' = Ax")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vector field matrix differential equation
- search: fundamental matrix intuition
- search: linear system state velocity visualization

### 5. Bài toán mẫu có bối cảnh thực

Cho hệ
$$
\begin{cases}
x_1'=2x_1-x_2,\\
x_2'=3x_1+4x_2.
\end{cases}
$$
Viết gọn:
$$
\mathbf{x}'=
\begin{pmatrix}
2 & -1\\
3 & 4
\end{pmatrix}\mathbf{x}.
$$
Ngay khi viết theo dạng này, ta đọc được:
- Hàng thứ nhất mô tả tốc độ của $$ x_1 $$ phụ thuộc vào chính $$ x_1 $$ và vào $$ x_2 $$.
- Hàng thứ hai làm điều tương tự cho $$ x_2 $$.
- Ma trận tạo một trường vector trên mặt phẳng trạng thái, từ đó chân dung pha sẽ được sinh ra.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo chuyển từ danh sách phương trình sang dạng $$ \mathbf{x}'=A\mathbf{x} $$.

**Bậc sau đại học.** Nhấn mạnh ma trận nghiệm cơ bản, không gian nghiệm và dòng chảy tuyến tính.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày rõ dạng ma trận và ma trận nghiệm cơ bản.
- Arnold, *Ordinary Differential Equations*: tốt cho trực giác hình học của toán tử $$ A $$.
