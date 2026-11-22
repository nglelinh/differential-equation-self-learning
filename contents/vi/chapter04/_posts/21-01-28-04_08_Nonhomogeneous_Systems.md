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

Bài học này hướng dẫn giải hệ tuyến tính không thuần nhất, trình bày công thức biến thiên hằng số cho hệ vector và làm rõ cách nguồn ngoài tác động lên quỹ đạo tự nhiên của hệ. Sinh viên cũng nắm được công thức tích phân Duhamel như biểu diễn tích lũy của đáp ứng cưỡng bức.

## Kiến thức nền

Sinh viên cần nắm cách giải hệ thuần nhất, ma trận nghiệm cơ bản, ma trận mũ và phép lấy tích phân hàm vector. Sự phân tách giữa phần tự do và phần cưỡng bức từ ODE một ẩn sẽ hỗ trợ trực tiếp cho bài này.

## Dẫn nhập

![Hệ tuyến tính không thuần nhất với lực cưỡng bức]({{ site.imgurl }}/chapter_img/chapter04/08_nonhomogeneous_systems.svg)

Các hệ thực tế hiếm khi tiến hóa hoàn toàn cô lập mà thường chịu tác động từ nguồn ngoài, dòng vào, tín hiệu điều khiển hoặc nhiễu. Khi đó, thay vì $$ \mathbf{x}'=A\mathbf{x} $$, ta có hệ không thuần nhất
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
Nghiệm của hệ không chỉ phụ thuộc vào các thành phần tự do mà còn tích lũy ảnh hưởng của toàn bộ lịch sử ngoại lực $$ \mathbf{g}(t) $$.

Cấu trúc của hệ thuần nhất vẫn đóng vai trò nền tảng: ta mở rộng phương pháp biến thiên hằng số sang dạng vector hoặc biểu diễn trực tiếp nghiệm bằng công thức tích phân qua ma trận mũ.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nghiệm của hệ không thuần nhất là tổng hợp của hai thành phần: diễn biến tự nhiên xuất phát từ trạng thái ban đầu khi không có tác động ngoài, và phần dịch chuyển tích lũy do ngoại lực kéo hệ đi theo thời gian.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, hệ thuần nhất xác định trường vector cố định $$ A\mathbf{x} $$. Khi cộng thêm $$ \mathbf{g}(t) $$, trường vector bị dịch chuyển hoặc biến đổi theo thời gian, khiến điểm cân bằng dời chỗ hoặc xuất hiện đáp ứng cưỡng bức ổn định.

### Cách nhìn hình thức

Với hệ $$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t) $$, nếu $$ \Phi(t) $$ là ma trận nghiệm cơ bản của hệ thuần nhất, thì công thức biến thiên hằng số cho nghiệm tổng quát:
$$
\mathbf{x}(t)=\Phi(t)\mathbf{c}+\Phi(t)\int \Phi(t)^{-1}\mathbf{g}(t)\,dt.
$$
Sử dụng ma trận mũ kèm điều kiện đầu $$ \mathbf{x}(t_0)=\mathbf{x}_0 $$, ta viết gọn dưới dạng công thức Duhamel:
$$
\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}_0+\int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$

## Những ngộ nhận thường gặp

- "Ngoại lực chỉ gây nhiễu nhỏ lên nghiệm thuần nhất." Sai: ngoại lực có thể làm thay đổi hoàn toàn trạng thái cân bằng và hành vi dài hạn.
- "Biến thiên hằng số cho hệ chỉ là viết dài hơn công thức một ẩn." Không chỉ vậy: dạng ma trận làm nổi bật cơ chế truyền tác động của ngoại lực qua toán tử tiến hóa.
- "Nếu $$ \mathbf{g}(t) $$ có biên độ nhỏ thì luôn bỏ qua được." Sai: một tác động nhỏ nhưng kéo dài (hoặc gần cộng hưởng) có thể tích lũy thành ảnh hưởng lớn.
- "Nghiệm riêng không liên quan đến hệ thuần nhất." Sai: ma trận nghiệm cơ bản $$ \Phi(t) $$ trực tiếp chi phối cấu trúc của nghiệm riêng.

## Tiến trình học tập đề xuất

### Bước 1: Giải hệ thuần nhất tương ứng

Tìm ma trận nghiệm cơ bản $$ \Phi(t) $$ hoặc ma trận mũ $$ e^{At} $$.

### Bước 2: Áp dụng biến thiên hằng số hoặc công thức Duhamel

Chọn biểu diễn thuận tiện nhất với dạng của $$ \mathbf{g}(t) $$ và điều kiện đầu.

### Bước 3: Tách phần quá độ và phần cưỡng bức

Phân biệt rõ đóng góp từ trạng thái ban đầu với đóng góp từ nguồn ngoài.

### Bước 4: Đánh giá hành vi dài hạn

Xem xét phần tự do có tắt dần hay không và phần cưỡng bức dẫn hệ về đâu.

### Các checkpoint

- Sinh viên có viết đúng công thức nghiệm tích phân với ma trận mũ hay không.
- Sinh viên có phân biệt rõ phần do điều kiện đầu và phần do ngoại lực hay không.
- Sinh viên có đọc được trạng thái dài hạn từ hai thành phần này hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Nguồn ngoài không đổi

Xét hệ
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
Nghiệm thuần nhất là
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
Tìm nghiệm riêng hằng $$ \mathbf{x}_p=\begin{pmatrix} a\\ b \end{pmatrix} $$, thay vào hệ được
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
\end{pmatrix}
\Rightarrow a=1,\quad b=0.
$$
Vậy nghiệm tổng quát là
$$
\mathbf{x}(t)=\mathbf{x}_h(t)+
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Khi $$ t\to\infty $$, phần thuần nhất tắt dần về 0 và hệ tiến về trạng thái cân bằng mới $$ (1,0)^T $$ do nguồn ngoài thiết lập.

### Ví dụ 2: Công thức Duhamel với điều kiện đầu tại $$ t=0 $$

Với $$ \mathbf{x}(0)=\mathbf{x}_0 $$, nghiệm duy nhất là
$$
\mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
Số hạng đầu là đáp ứng tự do do điều kiện đầu, số hạng tích phân là đáp ứng cưỡng bức do nguồn ngoài.

### Ví dụ 3: Ngoại lực dao động điều hòa

Khi $$ \mathbf{g}(t) $$ biến thiên điều hòa, nghiệm riêng thường dao động cùng tần số với biên độ và pha do ma trận $$ A $$ xác định — tương tự đáp ứng cưỡng bức và cộng hưởng ở phương trình một ẩn.

### Ví dụ 4: Ngoại lực và bộ nhớ của hệ

Trong tích phân $$ \int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds $$, tác động tại mỗi thời điểm quá khứ $$ s $$ được truyền tới thời điểm $$ t $$ thông qua toán tử tiến hóa $$ e^{A(t-s)} $$, thể hiện rõ tính tích lũy theo lịch sử của hệ.

## Câu hỏi khái niệm

1. Vì sao nghiệm riêng của hệ không thuần nhất vẫn phụ thuộc vào ma trận nghiệm cơ bản của hệ thuần nhất?
2. Hai số hạng trong công thức Duhamel mang ý nghĩa vật lý khác nhau như thế nào?
3. Vì sao ngoại lực có thể quyết định hoàn toàn trạng thái dài hạn ngay cả khi hệ thuần nhất suy giảm về 0?

## Bài toán ứng dụng

1. Một hệ điều khiển nhận tín hiệu đặt (tham chiếu) liên tục từ bên ngoài. Vì sao phần cưỡng bức quyết định trạng thái mong muốn ở chế độ xác lập?
2. Một hệ ngăn chứa có dòng cấp vào không đổi. Hãy diễn giải ý nghĩa của điểm cân bằng mới do dòng vào này tạo ra.
3. Một hệ dao động chịu lực tuần hoàn nhỏ nhưng duy trì lâu. Vì sao tác động tích lũy vẫn có thể đáng kể?

## Chiến lược giảng dạy tương tác

- Cho sinh viên phân tách nghiệm thành phần tự do và phần cưỡng bức bằng lời trước khi viết công thức.
- So sánh hệ thuần nhất với cùng hệ đó khi thêm nguồn hằng để thấy điểm cân bằng dịch chuyển thế nào.
- Hỏi lớp: "Nếu ngắt nguồn ngoài sau một thời gian dài, quỹ đạo sẽ tiếp tục tiến hóa ra sao?"
- Đánh dấu bằng hai màu khác nhau hai số hạng trong công thức Duhamel để phân rõ hai vai trò.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Bắt đầu từ trường hợp ngoại lực hằng hoặc đơn giản để sinh viên nắm chắc cấu trúc hai phần $$ \mathbf{x}_h+\mathbf{x}_p $$ trước khi tính các tích phân ma trận phức tạp.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên chứng minh công thức biến thiên hằng số và công thức Duhamel từ phép đặt $$ \mathbf{x}(t)=\Phi(t)\mathbf{u}(t) $$, hoặc khảo sát điều kiện cộng hưởng cho hệ hai chiều chịu lực tuần hoàn.

## Tóm tắt dễ nhớ

Nghiệm của hệ không thuần nhất $$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t) $$ gồm hai phần: phần tự do do điều kiện đầu và phần cưỡng bức tích lũy qua ma trận mũ theo công thức Duhamel.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ điều khiển tuyến tính có đầu vào
- Bài toán: Hệ trạng thái vừa có động lực nội tại vừa nhận tín hiệu điều khiển ngoài.
- Mô hình: $$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t) $$.
- Giả thiết và giới hạn: Hệ tuyến tính hệ số hằng.
- Diễn giải: Nghiệm là tổng đáp ứng trạng thái đầu và đáp ứng tích lũy theo đầu vào.

#### Mô hình ngăn có dòng cấp liên tục
- Bài toán: Hệ nhiều ngăn có thêm dòng vật chất bơm đều đặn từ bên ngoài.
- Mô hình:
$$
\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}_0+\int_{t_0}^t e^{A(t-s)}\mathbf{g}(s)\,ds.
$$
- Giả thiết và giới hạn: Lưu lượng trao đổi tuyến tính theo lượng chất trong từng ngăn.
- Diễn giải: Công thức Duhamel cho thấy cách dòng cấp tích lũy và lan truyền qua các ngăn.

#### Tác động nhỏ nhưng kéo dài
- Bài toán: Nguồn nhiễu biên độ nhỏ duy trì liên tục có thể làm lệch đáng kể trạng thái dài hạn.
- Mô hình: Hệ tuyến tính không thuần nhất.
- Giả thiết và giới hạn: Hệ tuyến tính với hàm nhiễu đã biết.
- Diễn giải: Biên độ tức thời nhỏ không đồng nghĩa ảnh hưởng tích lũy là không đáng kể.

### 2. Trực giác bổ sung và các kết nối

Hệ không thuần nhất là sự mở rộng trực tiếp của phương pháp biến thiên hằng số ở Chương 02, đồng thời nối liền với tích chập ở Chương 03 và phương pháp hàm Green cho phương trình đạo hàm riêng.

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

Xét lại hệ
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
Do phần thuần nhất suy giảm về 0, trạng thái cân bằng mới thỏa mãn $$ A\mathbf{x}_*=-\begin{pmatrix} 1\\ 0 \end{pmatrix} $$, cho $$ \mathbf{x}_*=\begin{pmatrix} 1\\ 0 \end{pmatrix} $$. Nguồn hằng đã dịch điểm hút của hệ từ gốc tọa độ sang điểm $$ (1,0)^T $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm cấu trúc nghiệm $$ \mathbf{x}_h+\mathbf{x}_p $$ và công thức biến thiên hằng số cho hệ tuyến tính.

**Bậc sau đại học.** Vận dụng công thức Duhamel, phân tích đáp ứng tần số nhiều chiều và ổn định vào – ra.

## Video tham khảo

- Xem trước: [Systems of Differential Equations with Forcing: Example in Control Theory](https://www.youtube.com/watch?v=vKgbYRw21xA) — Steve Brunton, tiếng Anh. Áp dụng biến thiên hằng số cho hệ tuyến tính có đầu vào kèm ví dụ điều khiển.
- [Linear Systems of Differential Equations with Forcing: Convolution and the Dirac Delta Function](https://www.youtube.com/watch?v=q1phVuNCuf0) — Steve Brunton, tiếng Anh. Trình bày tích chập với đáp ứng xung và hàm delta Dirac cho hệ tuyến tính.
- [Differential Equations with Forcing: Method of Variation of Parameters](https://www.youtube.com/watch?v=wCeDUbZQ_zA) — Steve Brunton, tiếng Anh. Ôn lại biến thiên hằng số vô hướng làm cơ sở cho mở rộng sang hệ.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày chuẩn mực hệ không thuần nhất và biến thiên hằng số.
- Arnold, *Ordinary Differential Equations*: hữu ích cho trực giác hình học về tác động của nguồn ngoài lên dòng chảy tuyến tính.
