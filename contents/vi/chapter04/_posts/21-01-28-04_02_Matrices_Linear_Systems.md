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


Viết từng dòng $x_1' = a_{11}x_1 + a_{12}x_2 + \dots$ không chỉ dài dòng mà còn che lấp hoàn toàn cấu trúc hình học của hệ. Khi đưa vào ngôn ngữ **ma trận và ma trận cơ bản (fundamental matrix) $\Phi(t)$**, toàn bộ lý thuyết không gian nghiệm $n$ chiều, nguyên lý chồng chất, định thức Wronskian và công thức nghiệm cho mọi điều kiện đầu $\mathbf{x}(t) = \Phi(t)\Phi(t_0)^{-1}\mathbf{x}_0$ lập tức hiện ra trong suốt như pha lê!

## Kiến thức cần nhớ: Bốn trụ cột của Ma trận & Hệ Tuyến tính

1. **Nguyên lý Chồng chất cho Hệ thuần nhất $\mathbf{x}' = A(t)\mathbf{x}$**:
   Tập nghiệm tạo thành không gian vectơ đúng $n$ chiều; nếu $\mathbf{x}^{(1)}, \dots, \mathbf{x}^{(n)}$ là $n$ nghiệm độc lập tuyến tính thì mọi nghiệm đều viết được dưới dạng $\mathbf{x}(t) = \Phi(t)\mathbf{c}$.
2. **Ma trận Cơ bản $\Phi(t)$ & Wronskian Hệ ($W(t) = \det\Phi(t)$)**:
   Xếp $n$ nghiệm vectơ thành $n$ cột của ma trận $\Phi(t)$ cỡ $n \times n$; $\Phi(t)$ là ma trận cơ bản khi và chỉ khi $\det\Phi(t) \ne 0$.
3. **Định lý Liouville–Abel ($\det\Phi(t) = \det\Phi(t_0)\exp\int_{t_0}^t \operatorname{tr}A(s)\,ds$)**:
   Phiên bản nhiều chiều của định lý Abel: vết $\operatorname{tr}A(t)$ chính là **tốc độ giãn/nén thể tích** trong không gian pha! Nếu $\operatorname{tr}A \equiv 0$, dòng chảy bảo toàn thể tích!
4. **Cấu trúc nghiệm Hệ không thuần nhất ($\mathbf{x} = \mathbf{x}_h + \mathbf{x}_p$)**:
   Giống hệt PTVP vô hướng, nghiệm tổng quát của $\mathbf{x}' = A(t)\mathbf{x} + \mathbf{g}(t)$ là tổng của nghiệm thuần nhất $\Phi(t)\mathbf{c}$ và một nghiệm riêng $\mathbf{x}_p(t)$.

## Mục tiêu

Bài học này hướng dẫn cách viết hệ phương trình vi phân tuyến tính dưới dạng ma trận, hiểu ý nghĩa động học của ma trận hệ số và nắm khái niệm ma trận nghiệm cơ bản như phiên bản nhiều chiều của nghiệm tổng quát. Đây là bước chuẩn bị trực tiếp để vận dụng đại số tuyến tính vào giải hệ ODE.

## Kiến thức nền

Sinh viên cần nắm vector, ma trận, phép nhân ma trận với vector và khái niệm độc lập tuyến tính. Kiến thức về ODE tuyến tính một ẩn giúp dễ dàng mở rộng nguyên lý chồng chất sang hệ nhiều chiều.

## Dẫn nhập

![Ma trận điều khiển sự tiến hóa của hệ tuyến tính]({{ site.imgurl }}/chapter_img/chapter04/02_matrices_linear_systems.svg)

Viết một hệ phương trình thành một đẳng thức ma trận duy nhất không chỉ giúp rút gọn ký hiệu, mà còn thể hiện rõ cấu trúc tương tác của toàn hệ: mỗi hàng của ma trận cho biết tốc độ thay đổi của một biến trạng thái phụ thuộc vào toàn bộ các biến như thế nào, còn mỗi cột cho biết một thành phần trạng thái tác động ra sao lên cả hệ.

Từ đây, thay vì nhìn hệ như một danh sách phương trình rời rạc, ta nhìn hệ như một thực thể tuyến tính thống nhất với toán tử tiến hóa là ma trận $$ A $$.

### Giải thích: Kiểm chứng Ma trận cơ bản, định lý Liouville và giải nhanh IVP bằng $\Phi(t)\Phi(0)^{-1}\mathbf{x}_0$

Cho hệ $\mathbf{x}' = \begin{pmatrix} 1 & 0 \\ 0 & -2 \end{pmatrix}\mathbf{x}$ với hai nghiệm cột $\mathbf{x}^{(1)} = \begin{pmatrix} e^t \\ 0 \end{pmatrix}$, $\mathbf{x}^{(2)} = \begin{pmatrix} 0 \\ e^{-2t} \end{pmatrix}$:
1. **Lập ma trận cơ bản $\Phi(t)$**:
   $$\Phi(t) = \begin{pmatrix} e^t & 0 \\ 0 & e^{-2t} \end{pmatrix} \implies W(t) = \det\Phi(t) = \mathbf{e^{-t}} \ne 0.$$
2. **Kiểm chứng Định lý Liouville**:
   $\operatorname{tr} A = 1 + (-2) = -1$, và $W(0) = 1$, nên $W(0)\exp\left(\int_0^t (-1)\,ds\right) = \mathbf{e^{-t}}$—khớp tuyệt đối! Diện tích hình vuông đơn vị trong không gian pha bị co lại theo hệ số $e^{-t}$.
3. **Giải tức thì IVP với $\mathbf{x}(0) = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$**:
   Vì $\Phi(0) = I$, ta có ngay $\mathbf{x}(t) = \Phi(t)\mathbf{x}(0) = \begin{pmatrix} 3e^t \\ -4e^{-2t} \end{pmatrix}$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Ma trận $$ A $$ đóng vai trò "quy luật tương tác" của hệ: tại mỗi trạng thái $$ \mathbf{x} $$, tích $$ A\mathbf{x} $$ xác định hướng và độ lớn vận tốc biến đổi của trạng thái đó.

### Cách nhìn hình ảnh

Trong hệ hai chiều $$ \mathbf{x}'=A\mathbf{x} $$, ma trận $$ A $$ gán cho mỗi điểm $$ \mathbf{x} $$ trên mặt phẳng một vector tiếp tuyến $$ A\mathbf{x} $$, qua đó tạo nên trường vector trên mặt phẳng trạng thái. Đây là cầu nối trực tiếp từ đại số tuyến tính sang hình học pha.

### Cách nhìn hình thức

Một hệ tuyến tính thuần nhất hệ số hằng có dạng
$$ \mathbf{x}'=A\mathbf{x}, $$
với $$ A $$ là ma trận hằng cỡ $$ n\times n $$. Khi có tác động ngoài, hệ viết là
$$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t). $$
Nếu $$ \mathbf{x}_1,\ldots,\mathbf{x}_n $$ là $$ n $$ nghiệm vector độc lập tuyến tính của hệ thuần nhất, thì ma trận
$$
\Phi(t)=
\begin{pmatrix}
\lvert  & & \rvert\\
\mathbf{x}_1(t) & \cdots & \mathbf{x}_n(t)\\
\lvert  & & \rvert
\end{pmatrix}
$$
được gọi là ma trận nghiệm cơ bản, và nghiệm tổng quát của hệ thuần nhất có dạng $$ \mathbf{x}(t)=\Phi(t)\mathbf{c} $$.

## Những ngộ nhận thường gặp

- "Ma trận chỉ là cách viết tắt." Sai: ma trận mã hóa trực tiếp cấu trúc tương tác và hình học của hệ.
- "Các cột của ma trận nghiệm cơ bản là những nghiệm bất kỳ." Sai: các cột phải độc lập tuyến tính để sinh ra toàn bộ không gian nghiệm.
- "Có thể giải riêng từng phương trình thành phần mà không cần ma trận." Thường không thực hiện được khi các biến ghép nối chặt với nhau.
- "Ma trận $$ A $$ chỉ quyết định tốc độ, không quyết định hình học." Sai: chính $$ A $$ sinh ra trường vector và quyết định toàn bộ chân dung pha.

## Tiến trình học tập đề xuất

### Bước 1: Viết hệ dưới dạng ma trận – vector

Gom danh sách các phương trình thành phần thành một đẳng thức duy nhất.

### Bước 2: Đọc ý nghĩa của từng hàng và từng cột

Liên hệ từng phần tử $$ a_{ij} $$ với tác động giữa các biến trạng thái.

### Bước 3: Áp dụng nguyên lý chồng chất cho hệ

Tổ hợp tuyến tính của các nghiệm vector của hệ thuần nhất vẫn là nghiệm.

### Bước 4: Xây dựng ma trận nghiệm cơ bản

Chuẩn bị công cụ cốt lõi dùng xuyên suốt các bài sau của chương.

### Các checkpoint

- Sinh viên có chuyển chính xác hệ phương trình sang dạng $$ \mathbf{x}'=A\mathbf{x} $$ hay không.
- Sinh viên có hiểu vì sao hệ $$ n $$ chiều cần đúng $$ n $$ nghiệm độc lập tuyến tính hay không.
- Sinh viên có diễn giải được $$ A\mathbf{x} $$ như vector vận tốc trạng thái hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Biểu diễn hệ dưới dạng ma trận

Xét hệ
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
\end{pmatrix},
$$
hệ viết gọn thành $$ \mathbf{x}'=A\mathbf{x} $$. Toàn bộ quan hệ giữa hai biến được gói trong một phép nhân ma trận duy nhất.

### Ví dụ 2: Hệ có ma trận đường chéo

Với
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
$$
hệ tách thành hai phương trình độc lập $$ x_1'=2x_1 $$ và $$ x_2'=-x_2 $$, cho nghiệm $$ x_1=c_1e^{2t} $$ và $$ x_2=c_2e^{-t} $$. Viết dưới dạng vector:
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
Hai trục tọa độ đóng vai trò hai phương động học độc lập.

### Ví dụ 3: Xây dựng ma trận nghiệm cơ bản

Từ Ví dụ 2, chọn hai nghiệm độc lập
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
Ma trận nghiệm cơ bản tương ứng là
$$
\Phi(t)=
\begin{pmatrix}
e^{2t} & 0\\
0 & e^{-t}
\end{pmatrix},
$$
và mọi nghiệm của hệ thuần nhất đều viết dưới dạng $$ \mathbf{x}(t)=\Phi(t)\mathbf{c} $$.

### Ví dụ 4: Đọc ý nghĩa phần tử ma trận

Nếu phần tử $$ a_{21} $$ dương lớn, biến thứ nhất tác động mạnh theo chiều làm tăng tốc độ thay đổi của biến thứ hai. Cách đọc theo hàng và cột này gắn trực tiếp bảng số với cơ chế tương tác thực tế.

## Câu hỏi khái niệm

1. Vì sao biểu diễn ma trận mang lại giá trị vượt trên việc rút gọn ký hiệu?
2. Mỗi hàng và mỗi cột của ma trận $$ A $$ thể hiện thông tin gì?
3. Vì sao ma trận nghiệm cơ bản là khái niệm trung tâm của lý thuyết hệ tuyến tính?

## Bài toán ứng dụng

1. Trong mô hình kinh tế hai biến (sản lượng và nhu cầu), vì sao dạng ma trận thích hợp để mã hóa tác động qua lại giữa hai biến?
2. Trong sinh học, khi hai quần thể tương tác, các phần tử ngoài đường chéo của ma trận $$ A $$ biểu thị điều gì?
3. Trong cơ học nhiều bậc tự do, vì sao biểu diễn ma trận là bước đệm cần thiết cho phân tích trị riêng?

## Chiến lược giảng dạy tương tác

- Cho sinh viên chuyển đổi qua lại giữa dạng hệ thành phần và dạng ma trận.
- Yêu cầu lớp diễn đạt bằng lời ý nghĩa động học của từng hệ số trong một ma trận $$ 2\times 2 $$.
- Cho sinh viên tự ghép ma trận nghiệm cơ bản từ hai nghiệm vector đã biết.
- Dùng màu khác nhau phân biệt các cột của $$ \Phi(t) $$ để nhấn mạnh mỗi cột là một nghiệm cơ sở.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Bắt đầu với hệ hai chiều để sinh viên dễ đối chiếu đồng thời giữa công thức và hình vẽ, nhấn mạnh rõ vector nghiệm là một hàm theo thời gian chứ không phải vector hằng.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên chứng minh rằng nếu $$ \Phi(t) $$ là ma trận nghiệm cơ bản thì mọi nghiệm đều có dạng $$ \Phi(t)\mathbf{c} $$, và liên hệ định thức $$ \det\Phi(t) $$ với tính độc lập tuyến tính (định thức Wronskian của hệ).

## Tóm tắt dễ nhớ

Viết hệ tuyến tính dưới dạng $$ \mathbf{x}'=A\mathbf{x} $$ làm nổi bật toán tử động học của hệ: ma trận $$ A $$ sinh ra trường vector, còn ma trận nghiệm cơ bản $$ \Phi(t) $$ sinh ra toàn bộ không gian nghiệm qua biểu thức $$ \mathbf{x}(t)=\Phi(t)\mathbf{c} $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tương tác giữa các loài trong sinh học
- Bài toán: Tốc độ biến đổi của mỗi quần thể phụ thuộc vào chính nó và các loài khác.
- Mô hình tuyến tính hóa: $$ \mathbf{x}'=A\mathbf{x} $$.
- Giả thiết và giới hạn: Chỉ chính xác gần điểm cân bằng, chưa mô tả đầy đủ tính phi tuyến toàn cục.
- Diễn giải: Ma trận $$ A $$ tóm gọn toàn bộ các tác động chéo trong hệ sinh thái.

#### Mạng điện nhiều nút
- Bài toán: Điện áp hoặc dòng điện trên nhiều nhánh thay đổi đồng thời và phụ thuộc lẫn nhau.
- Mô hình: $$ \mathbf{x}'=A\mathbf{x}+\mathbf{g}(t) $$.
- Giả thiết và giới hạn: Mạch tuyến tính, tham số không đổi quanh điểm làm việc.
- Diễn giải: Dạng ma trận làm rõ ngay cấu trúc liên kết của mạng điện.

#### Mô hình vốn và hàng tồn kho
- Bài toán: Một biến kinh tế tác động trực tiếp lên tốc độ biến đổi của biến còn lại.
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
- Giả thiết và giới hạn: Xấp xỉ tuyến tính cục bộ.
- Diễn giải: Các phần tử theo hàng và cột chỉ rõ chiều và mức độ tác động giữa hai biến.

### 2. Trực giác bổ sung và các kết nối

Dạng ma trận thay đổi cách nhìn toàn diện về hệ: $$ A $$ vừa là quy luật tương tác giữa các biến, vừa là toán tử sinh trường vector trên không gian trạng thái. Các khái niệm đại số tuyến tính như cơ sở, độc lập tuyến tính và ma trận khả nghịch nay mang trực tiếp ý nghĩa động lực học.

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
Viết dưới dạng ma trận:
$$
\mathbf{x}'=
\begin{pmatrix}
2 & -1\\
3 & 4
\end{pmatrix}\mathbf{x}.
$$
Từ biểu diễn này ta đọc được trực tiếp:
- Hàng thứ nhất cho biết tốc độ thay đổi của $$ x_1 $$ phụ thuộc vào cả $$ x_1 $$ và $$ x_2 $$.
- Hàng thứ hai mô tả tương tự cho $$ x_2 $$.
- Ma trận $$ A $$ xác định trường vector trên mặt phẳng trạng thái, làm cơ sở dựng chân dung pha.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo chuyển hệ thành phần sang dạng $$ \mathbf{x}'=A\mathbf{x} $$ và dựng ma trận nghiệm cơ bản cho các trường hợp đơn giản.

**Bậc sau đại học.** Nhấn mạnh cấu trúc không gian nghiệm, ma trận nghiệm cơ bản chuẩn hóa và dòng chảy tuyến tính.

## Video tham khảo

- Xem trước: [Matrix Systems of Differential Equations](https://www.youtube.com/watch?v=Vtijyyo5fKI) — Steve Brunton, tiếng Anh. Trình bày hệ ma trận và lý do các cột của ma trận nghiệm cơ bản tạo thành cơ sở nghiệm.
- [Linear Systems of Equations | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=_Fo3Jq1blKk) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về hệ phương trình tuyến tính.
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, tiếng Anh. Minh họa trực quan vai trò hình học của vector riêng trong việc tách rời hệ ma trận.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày hệ thống về dạng ma trận và ma trận nghiệm cơ bản.
- Arnold, *Ordinary Differential Equations*: giàu trực giác hình học cho toán tử tuyến tính $$ A $$.
