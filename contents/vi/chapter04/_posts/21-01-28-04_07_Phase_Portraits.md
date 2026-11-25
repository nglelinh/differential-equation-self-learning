---
layout: post
title: "04-07 Chân dung Pha cho Hệ Tuyến tính"
chapter: '04'
order: 7
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---


Đứng trước một hệ hai phương trình vi phân tuyến tính $\mathbf{x}' = A\mathbf{x}$, bạn không cần máy tính hay hàng trang giấy tính toán để biết toàn bộ bức tranh vận động của nó. Chỉ cần liếc qua hai con số—vết $\tau = a + d$ và định thức $\Delta = ad - bc$—kèm hướng của hai vectơ riêng (nếu thực), bạn có thể phác thảo bằng tay **chân dung pha (phase portrait)** chính xác gần như tuyệt đối trong vòng một phút!

## Kiến thức cần nhớ: Bốn chìa khóa đọc & vẽ Chân dung Pha 2D

1. **Bản đồ phân loại theo $(\tau, \Delta)$ và biệt thức $D = \tau^2 - 4\Delta$**:
   - $\Delta < 0$: **Điểm yên ngựa** (luôn bất ổn).
   - $\Delta > 0,\; D > 0$: **Nút** (hút nếu $\tau < 0$, đẩy nếu $\tau > 0$).
   - $\Delta > 0,\; D < 0$: **Xoáy ốc** (hút nếu $\tau < 0$, đẩy nếu $\tau > 0$) hoặc **Tâm** (nếu $\tau = 0$).
   - $\Delta > 0,\; D = 0$: **Nút sao** hoặc **Nút suy biến**.
2. **Quy tắc tiếp tuyến tại gốc của Nút (Fast vs. Slow Eigendirection)**:
   Với nút hút $\lambda_1 < \lambda_2 < 0$, thành phần $e^{\lambda_1 t}$ tắt nhanh hơn $e^{\lambda_2 t}$ nên mọi quỹ đạo (trừ đường thẳng dọc $\mathbf{v}_1$) đều **tiếp xúc với trục chậm $\mathbf{v}_2$** khi tiến về $(0, 0)$!
3. **Tính nhạy cảm cấu trúc (Structural Stability)**:
   Nút, yên ngựa và xoáy ốc là bền vững cấu trúc; ngược lại **Tâm ($\tau = 0$)** và **Nút suy biến ($D = 0$)** nằm đúng trên đường ranh giới—chỉ cần nhiễu cực nhỏ $10^{-6}$ là Tâm biến thành Xoáy ốc!
4. **Cầu nối trực tiếp sang Hệ phi tuyến Chương 05**:
   Theo định lý Hartman–Grobman, chân dung pha của hệ phi tuyến quanh điểm cân bằng hyperbol giống hệt chân dung pha tuyến tính của ma trận Jacobi tại điểm đó!

## Mục tiêu

Bài học này hướng dẫn cách đọc và phác họa chân dung pha của hệ tuyến tính hai chiều, phân loại điểm cân bằng bằng trị riêng hoặc bằng cặp vết – định thức, và cho thấy sức mạnh của phân tích định tính ngay cả khi không viết công thức nghiệm tường minh.

## Kiến thức nền

Sinh viên cần nắm trị riêng thực, trị riêng phức và các dạng nghiệm cơ bản của hệ tuyến tính hai chiều. Trực giác về trường vector và đường quỹ đạo từ chương phương trình tự trị là nền tảng rất hữu ích.

## Dẫn nhập

![Chân dung pha của hệ tuyến tính hai chiều]({{ site.imgurl }}/chapter_img/chapter04/07_phase_portraits.svg)

Một công thức nghiệm tường minh cho giá trị chính xác tại từng thời điểm nhưng không phải lúc nào cũng giúp hình dung nhanh bức tranh tổng thể. Chân dung pha làm điều ngược lại: bỏ qua chi tiết đại số để thể hiện trực tiếp hình học của chuyển động — quỹ đạo đi về đâu, rời khỏi đâu, có xoắn hay không và có những phương bất biến nào.

Chỉ từ ma trận $$ A $$, ta đã có thể phân loại gốc tọa độ thành điểm yên ngựa, nút hút, nút đẩy, tâm hay tiêu điểm. Kỹ năng định tính này rất cần thiết vì trong nhiều mô hình phức tạp, việc đọc cấu trúc pha là bước mở đầu trước khi tính toán chi tiết.

### Giải thích: Phác thảo bằng tay chân dung pha cho hệ nút hút $\mathbf{x}' = \begin{pmatrix} -4 & 0 \\ 0 & -1 \end{pmatrix}\mathbf{x}$ và kiểm tra độ cong

Hệ đã chéo sẵn: $\lambda_1 = -4$ (trục nhanh $\mathbf{v}_1 = (1, 0)^\top$ là trục $Ox$), $\lambda_2 = -1$ (trục chậm $\mathbf{v}_2 = (0, 1)^\top$ là trục $Oy$).
1. **Nghiệm tường minh**: $x_1(t) = c_1 e^{-4t},\; x_2(t) = c_2 e^{-t}$.
2. **Khử $t$ để tìm phương trình quỹ đạo**:
   Vì $e^{-t} = x_2/c_2$, thay vào $x_1$ ta được:
   $$x_1 = c_1\left(\frac{x_2}{c_2}\right)^4 = \mathbf{k\,x_2^4}!$$
3. **Đọc dáng hình học tại gốc $(0, 0)$**:
   Đường cong $x_1 = k x_2^4$ (ví dụ $x_1 = x_2^4$) khi tiến về $(0, 0)$ có $\frac{dx_1}{dx_2} = 4kx_2^3 \to 0$, tức là **ép sát và tiếp tuyến thẳng đứng với trục chậm $Oy$**! Ngược lại khi $t \to -\infty$, $x_1$ phình nhanh hơn $x_2$ rất nhiều nên quỹ đạo vươn gần như nằm ngang song song với trục nhanh $Ox$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Chân dung pha giống như bản đồ dòng chảy của hệ: tại mỗi điểm trong mặt phẳng trạng thái, ta thấy ngay chiều dịch chuyển của trạng thái, còn mỗi quỹ đạo là con đường hệ đi qua khi xuất phát từ một điều kiện đầu cụ thể.

### Cách nhìn hình ảnh

Trong hệ hai chiều $$ \mathbf{x}'=A\mathbf{x} $$, gốc tọa độ luôn là một điểm cân bằng. Nếu mọi quỹ đạo hội tụ về gốc, đó là điểm hút; nếu rời xa gốc, đó là điểm đẩy; nếu có một phương hút và một phương đẩy, đó là điểm yên ngựa; nếu quỹ đạo quay quanh gốc, hệ có cặp trị riêng phức.

### Cách nhìn hình thức

Với ma trận
$$
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
$$
đặt vết và định thức là
$$
\tau=\operatorname{tr}(A)=a+d,\qquad \Delta=\det(A)=ad-bc.
$$
Đa thức đặc trưng có dạng $$ \lambda^2-\tau\lambda+\Delta=0 $$. Dấu của $$ \Delta $$, dấu của $$ \tau $$ và dấu của biệt thức $$ \tau^2-4\Delta $$ xác định đầy đủ kiểu điểm cân bằng tại gốc.

## Những ngộ nhận thường gặp

- "Muốn vẽ chân dung pha phải giải nghiệm tường minh trước." Sai: phần lớn thông tin hình học rút ra trực tiếp từ trị riêng, vector riêng và cặp $$ (\tau,\Delta) $$.
- "Quỹ đạo cong đồng nghĩa với hệ phi tuyến." Sai: hệ tuyến tính vẫn tạo ra quỹ đạo cong dạng hyperbol, parabol hoặc xoắn ốc.
- "Tâm và tiêu điểm đều quay quanh gốc nên giống nhau." Sai: quanh tâm các quỹ đạo khép kín với biên độ không đổi, còn quanh tiêu điểm quỹ đạo xoắn vào hoặc xoắn ra.
- "Chỉ cần biết dấu của định thức là phân loại được hoàn toàn." Không đủ: khi $$ \Delta>0 $$, cần xét thêm dấu của $$ \tau $$ và $$ \tau^2-4\Delta $$.

## Tiến trình học tập đề xuất

### Bước 1: Tính trị riêng hoặc cặp $$ (\tau,\Delta) $$

Đây là bước xác định nhanh kiểu cân bằng.

### Bước 2: Phân loại điểm cân bằng

Xác định gốc là yên ngựa, nút, tâm hay tiêu điểm.

### Bước 3: Xác định phương bất biến và chiều quay

Dùng vector riêng (khi trị riêng thực) hoặc kiểm tra chiều quay tại một điểm mẫu (khi trị riêng phức).

### Bước 4: Kiểm chứng bằng vài vector của trường

Tính $$ A\mathbf{x} $$ tại một vài điểm để chắc chắn chiều mũi tên trên hình vẽ là chính xác.

### Các checkpoint

- Sinh viên có phân biệt rõ nút, yên ngựa, tâm và tiêu điểm hay không.
- Sinh viên có vận dụng chính xác tiêu chuẩn vết – định thức $$ (\tau,\Delta) $$ hay không.
- Sinh viên có xác định được các phương bất biến trên chân dung pha hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Điểm yên ngựa

Xét ma trận
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
$$
có $$ \Delta=-2<0 $$. Do định thức âm, gốc tọa độ là điểm yên ngựa với trục thứ nhất là phương đẩy và trục thứ hai là phương hút.

### Ví dụ 2: Nút hút

Xét
$$
A=
\begin{pmatrix}
-2 & 0\\
0 & -3
\end{pmatrix}.
$$
Hai trị riêng đều âm, nên gốc là nút ổn định (nút hút). Mọi quỹ đạo không tầm thường đều tiến về gốc và tiệm cận theo phương ứng với trị riêng suy giảm chậm hơn ($$ \lambda=-2 $$) khi $$ t\to\infty $$.

### Ví dụ 3: Tiêu điểm hút

Xét
$$
A=
\begin{pmatrix}
-1 & -2\\
2 & -1
\end{pmatrix},
$$
có $$ \tau=-2 $$ và $$ \Delta=5 $$. Vì $$ \tau^2-4\Delta=4-20<0 $$ nên trị riêng là phức, và vì $$ \tau<0 $$ nên phần thực âm. Gốc tọa độ là tiêu điểm ổn định (xoắn ốc hút).

### Ví dụ 4: Điểm tâm

Với
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix},
$$
ta có $$ \tau=0 $$, $$ \Delta=1 $$ và $$ \tau^2-4\Delta<0 $$. Trị riêng là $$ \pm i $$, nên gốc là điểm tâm với các quỹ đạo quay khép kín quanh gốc.

## Câu hỏi khái niệm

1. Vì sao chân dung pha mang lại cái nhìn tổng thể nhanh hơn công thức nghiệm tường minh?
2. Vết $$ \tau $$ và định thức $$ \Delta $$ đóng vai trò gì trong phân loại điểm cân bằng?
3. Vì sao cùng có cặp trị riêng phức nhưng có hệ cho điểm tâm, còn hệ khác cho tiêu điểm?

## Bài toán ứng dụng

1. Một mô hình cơ học tuyến tính hóa quanh điểm cân bằng cho chân dung pha dạng yên ngựa. Vì sao trạng thái cân bằng này rất khó duy trì trong thực tế?
2. Một hệ sinh học tuyến tính hóa quanh cân bằng cho tiêu điểm hút. Điều đó cho biết gì về cách quần thể quay về mức cân bằng?
3. Trong điều khiển tự động, vì sao cần tránh cực có phần thực dương để không xuất hiện nút đẩy hay tiêu điểm đẩy?

## Chiến lược giảng dạy tương tác

- Cho sinh viên dự đoán loại điểm cân bằng từ trị riêng trước khi phác họa.
- Sử dụng bảng phân loại theo mặt phẳng $$ (\tau,\Delta) $$ để luyện phản xạ nhận diện.
- Cho các nhóm phác họa cùng một chân dung pha theo hai cách: dùng trị riêng và dùng vết – định thức.
- Yêu cầu sinh viên kiểm tra chiều mũi tên bằng cách tính trực tiếp $$ A\mathbf{x} $$ tại một vài điểm mẫu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Áp dụng quy trình hai bước: kiểm tra dấu của $$ \Delta $$ trước ($$ \Delta<0 $$ là yên ngựa); nếu $$ \Delta>0 $$, xét tiếp dấu của $$ \tau^2-4\Delta $$ (nút hay xoắn ốc) và dấu của $$ \tau $$ (hút, đẩy hay tâm).

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên chứng minh vì sao các quỹ đạo tiến về nút hút lại tiếp xúc với phương của trị riêng suy giảm chậm hơn gần gốc, và đối chiếu chân dung pha với nghiệm tường minh.

## Tóm tắt dễ nhớ

Chân dung pha là bản đồ hình học của hệ tuyến tính. Với hệ hai chiều, cặp vết – định thức $$ (\tau,\Delta) $$ hoặc các trị riêng cho phép phân loại nhanh điểm cân bằng tại gốc thành yên ngựa, nút, tâm hay tiêu điểm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tuyến tính hóa quanh điểm cân bằng
- Bài toán: Dự đoán hành vi cục bộ quanh cân bằng của hệ phi tuyến thông qua dạng yên ngựa, nút, tâm hay tiêu điểm.
- Mô hình: $$ \mathbf{x}'=A\mathbf{x} $$.
- Giả thiết và giới hạn: Chỉ có hiệu lực cục bộ gần điểm cân bằng khi xuất phát từ tuyến tính hóa.
- Diễn giải: Chân dung pha cung cấp thông tin định tính mạnh mà không cần giải nghiệm đóng.

#### Phân tích ổn định trong điều khiển
- Bài toán: Xác định xem trạng thái có hội tụ về gốc hay phân kỳ khỏi gốc.
- Mô hình: $$ \tau=\operatorname{tr}(A) $$ và $$ \Delta=\det(A) $$.
- Giả thiết và giới hạn: Hệ tuyến tính hai chiều.
- Diễn giải: Điều kiện ổn định tiệm cận tương đương $$ \tau<0 $$ và $$ \Delta>0 $$.

#### Động học hai biến trong hóa học và sinh học
- Bài toán: Xác định hai đại lượng tiến về cân bằng theo đường xoắn, đường trượt hay tiến thẳng.
- Mô hình: Chân dung pha của hệ hai chiều.
- Giả thiết và giới hạn: Xấp xỉ tuyến tính quanh điểm cân bằng.
- Diễn giải: Cung cấp trực giác hình học rõ ràng về độ ổn định.

### 2. Trực giác bổ sung và các kết nối

Chân dung pha tổng hợp trị riêng, vector riêng và trường vector vào một biểu diễn hình học thống nhất, đồng thời là cầu nối trực tiếp sang nghiên cứu hệ phi tuyến ở các chương sau — nơi nghiệm giải tích thường không tồn tại nhưng phân tích pha vẫn phát huy hiệu quả.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2],
              [-3, -4]], dtype=float)
x = np.linspace(-2, 2, 17)
y = np.linspace(-2, 2, 17)
X, Y = np.meshgrid(x, y)
U = A[0,0] * X + A[0,1] * Y
V = A[1,0] * X + A[1,1] * Y
N = np.sqrt(U**2 + V**2)

plt.quiver(X, Y, U / N, V / N, color="darkgreen")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Chân dung pha tuyến tính từ ma trận A")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: trace determinant plane interactive
- search: linear system phase portrait applet
- search: saddle node spiral source sink visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét ma trận
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$
Vì $$ \Delta=-2<0 $$, gốc là điểm yên ngựa với trục $$ x_1 $$ là phương đẩy và trục $$ x_2 $$ là phương hút. Không cần giải chi tiết, ta thấy ngay điểm cân bằng này không ổn định vì chỉ một nhiễu nhỏ dọc phương đẩy sẽ kéo hệ rời xa gốc nhanh chóng.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân loại chính xác các dạng điểm cân bằng bằng trị riêng hoặc cặp vết – định thức.

**Bậc sau đại học.** Liên hệ với định lý Hartman–Grobman về tuyến tính hóa hệ phi tuyến và tính bền vững cấu trúc của chân dung pha.

## Video tham khảo

- Xem trước: [Phase Portraits | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=zmzyW1rP-hk) — MIT OpenCourseWare, tiếng Anh. Giới thiệu các dạng chân dung pha tuyến tính cơ bản.
- [Trace-Determinant Diagram | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=oEskbXrhkkk) — MIT OpenCourseWare, tiếng Anh. Phân loại chân dung pha trên mặt phẳng vết – định thức.
- [MAE5790-5 Two dimensional linear systems](https://www.youtube.com/watch?v=QrHRaA93Nrg) — Cornell MAE, tiếng Anh. Giáo sư Strogatz trình bày phân loại hệ tuyến tính hai chiều từ trị riêng.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày hệ thống phân loại hệ tuyến tính phẳng.
- Strogatz, *Nonlinear Dynamics and Chaos*: giàu trực giác hình học về chân dung pha và phân loại điểm cân bằng.
