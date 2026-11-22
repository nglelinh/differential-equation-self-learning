---
layout: post
title: "04-06 Ma trận Mũ"
chapter: '04'
order: 6
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này giới thiệu ma trận mũ (hàm mũ ma trận) $$ e^{At} $$ như toán tử tiến hóa trung tâm của hệ tuyến tính hệ số hằng, trình bày định nghĩa bằng chuỗi lũy thừa, cách tính trong trường hợp chéo hóa được và khối Jordan, đồng thời cho thấy $$ e^{At} $$ thống nhất toàn bộ các trường hợp trị riêng đã học trong chương.

## Kiến thức nền

Sinh viên cần nắm chuỗi Taylor của hàm mũ thông thường, trị riêng, vector riêng cùng các trường hợp trị riêng phức và trị riêng lặp. Trực giác về toán tử đưa trạng thái từ thời điểm ban đầu đến thời điểm $$ t $$ sẽ giúp nắm bài dễ dàng hơn.

## Dẫn nhập

![Ma trận mũ như dòng chảy của hệ tuyến tính]({{ site.imgurl }}/chapter_img/chapter04/06_matrix_exponentials.svg)

Trong ODE một ẩn, hàm mũ $$ e^{at} $$ là nghiệm cơ bản vì đạo hàm của nó tỉ lệ với chính nó. Với hệ tuyến tính $$ \mathbf{x}'=A\mathbf{x} $$, đối tượng tương ứng là ma trận mũ $$ e^{At} $$, cho phép viết nghiệm của mọi bài toán giá trị đầu hệ số hằng trong một công thức duy nhất.

Giá trị lớn nhất của ma trận mũ là tính thống nhất: trị riêng thực phân biệt, trị riêng phức, trị riêng lặp và vector riêng suy rộng đều có thể xem là các phương pháp khác nhau để tính hoặc diễn giải cùng một đối tượng $$ e^{At} $$.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Ma trận mũ đóng vai trò toán tử tiến hóa theo thời gian: khi biết trạng thái ban đầu $$ \mathbf{x}_0 $$, phép nhân $$ e^{At}\mathbf{x}_0 $$ cho trực tiếp trạng thái của hệ tại thời điểm $$ t $$.

### Cách nhìn hình ảnh

Nếu ma trận $$ A $$ sinh ra trường vector vận tốc trên không gian trạng thái, thì $$ e^{At} $$ mô tả dòng chảy của trường vector đó sau khoảng thời gian $$ t $$, ánh xạ mọi điểm xuất phát sang vị trí mới dọc theo quỹ đạo.

### Cách nhìn hình thức

Ma trận mũ được định nghĩa bằng chuỗi lũy thừa hội tụ với mọi ma trận vuông $$ A $$:
$$
e^{At}=I+At+\frac{(At)^2}{2!}+\frac{(At)^3}{3!}+\cdots.
$$
Từ định nghĩa này suy ra $$ \frac{d}{dt}e^{At}=Ae^{At} $$ và $$ e^{A\cdot 0}=I $$. Do đó, nghiệm duy nhất của bài toán giá trị đầu
$$
\mathbf{x}'=A\mathbf{x},\qquad \mathbf{x}(0)=\mathbf{x}_0
$$
là $$ \mathbf{x}(t)=e^{At}\mathbf{x}_0 $$.

## Những ngộ nhận thường gặp

- "Ma trận mũ chỉ là cách ký hiệu cho gọn." Sai: đây là toán tử tiến hóa xác định chặt chẽ bằng chuỗi và có nhiều tính chất đại số quan trọng.
- "Muốn tính $$ e^{At} $$ phải cộng trực tiếp chuỗi vô hạn." Thường không cần: ta thường tính thông qua chéo hóa, dạng Jordan hoặc biến đổi Laplace.
- "Biết trị riêng rồi thì không cần ma trận mũ." Sai: ma trận mũ gộp toàn bộ các thành phần nghiệm vào một ma trận nghiệm cơ bản chuẩn hóa tại $$ t=0 $$.
- "Ma trận mũ luôn dễ tính bằng tay." Không hẳn, nhưng ý nghĩa lý thuyết và ứng dụng tính toán số của nó vẫn rất quan trọng.

## Tiến trình học tập đề xuất

### Bước 1: Nắm định nghĩa bằng chuỗi lũy thừa

Hiểu nguồn gốc của tính chất đạo hàm $$ \frac{d}{dt}e^{At}=Ae^{At} $$.

### Bước 2: Kiểm chứng vai trò giải bài toán giá trị đầu

Thấy rõ $$ \mathbf{x}(t)=e^{At}\mathbf{x}_0 $$ thỏa cả phương trình lẫn điều kiện đầu.

### Bước 3: Tính qua phép chéo hóa

Luyện thành thạo công thức $$ e^{At}=Pe^{Dt}P^{-1} $$.

### Bước 4: Tính cho khối Jordan

Thấy trực tiếp nguồn gốc đại số của các số hạng $$ te^{\lambda t} $$.

### Các checkpoint

- Sinh viên có hiểu vì sao $$ e^{At} $$ là ma trận nghiệm cơ bản thỏa $$ \Phi(0)=I $$ hay không.
- Sinh viên có biết áp dụng phép chéo hóa để tính $$ e^{At} $$ hay không.
- Sinh viên có liên hệ được $$ e^{At} $$ với các dạng nghiệm đã học ở các bài trước hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ma trận đường chéo

Nếu
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
$$
thì
$$
e^{At}=
\begin{pmatrix}
e^{2t} & 0\\
0 & e^{-t}
\end{pmatrix}.
$$
Đây là trường hợp đơn giản nhất, minh họa trực tiếp việc hàm mũ tác động độc lập lên từng phần tử đường chéo.

### Ví dụ 2: Ma trận chéo hóa được

Giả sử $$ A=PDP^{-1} $$ với $$ D=\begin{pmatrix} \lambda_1 & 0\\ 0 & \lambda_2 \end{pmatrix} $$. Khi đó
$$
e^{At}=Pe^{Dt}P^{-1}
=
P
\begin{pmatrix}
e^{\lambda_1 t} & 0\\
0 & e^{\lambda_2 t}
\end{pmatrix}
P^{-1},
$$
nối trực tiếp phép chéo hóa với công thức nghiệm của hệ.

### Ví dụ 3: Khối Jordan bậc hai

Với
$$
A=
\begin{pmatrix}
\lambda & 1\\
0 & \lambda
\end{pmatrix},
$$
ta tách $$ A=\lambda I+N $$, trong đó
$$
N=
\begin{pmatrix}
0 & 1\\
0 & 0
\end{pmatrix},
\qquad N^2=0.
$$
Vì $$ \lambda I $$ và $$ N $$ giao hoán với nhau, ta có
$$
e^{At}=e^{\lambda t}e^{Nt}
=e^{\lambda t}\left(I+tN\right)
=e^{\lambda t}
\begin{pmatrix}
1 & t\\
0 & 1
\end{pmatrix}.
$$
Đây chính là nguồn gốc ma trận của thừa số $$ te^{\lambda t} $$.

### Ví dụ 4: Giải bài toán giá trị đầu bằng ma trận mũ

Nếu đã có $$ e^{At} $$ và điều kiện đầu $$ \mathbf{x}(0)=\begin{pmatrix} 1\\ 2 \end{pmatrix} $$, ta chỉ cần thực hiện phép nhân $$ \mathbf{x}(t)=e^{At}\mathbf{x}(0) $$. Toàn bộ điều kiện đầu được áp dụng trong một phép nhân ma trận – vector duy nhất.

## Câu hỏi khái niệm

1. Vì sao biết $$ e^{At} $$ tương đương với việc nắm trọn vẹn động học của hệ tuyến tính thuần nhất?
2. Vì sao phép chéo hóa rút ngắn đáng kể việc tính ma trận mũ?
3. Vì sao khối Jordan bậc hai lại sinh ra thừa số $$ t $$ trong $$ e^{At} $$?

## Bài toán ứng dụng

1. Trong mô phỏng số, vì sao công thức tiến hóa trực tiếp $$ \mathbf{x}(t)=e^{At}\mathbf{x}_0 $$ có giá trị thực tiễn cao?
2. Một hệ điều khiển tuyến tính cần dự báo trạng thái sau bước thời gian $$ h $$. Ma trận mũ đóng vai trò gì trong bước rời rạc hóa này?
3. Với một hệ dao động ghép nhiều thành phần, vì sao ma trận mũ giúp gộp mọi chế độ vào một biểu thức duy nhất?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự tính $$ e^{At} $$ từ chuỗi định nghĩa trên ma trận đường chéo trước để tạo trực giác.
- Hỏi lớp: "Nếu hàm mũ thường giải ODE vô hướng $$ x'=ax $$, công cụ tương ứng cho hệ $$ \mathbf{x}'=A\mathbf{x} $$ là gì?"
- Đặt cạnh nhau hai ví dụ chéo hóa và khối Jordan để tổng hợp lại các bài trước.
- Nhấn mạnh cách đọc $$ e^{At} $$ như một toán tử dòng chảy thay vì chỉ là công thức tính.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Luyện vững các ví dụ ma trận đường chéo và ma trận chéo hóa được trước, tập trung hiểu ý nghĩa toán tử tiến hóa của $$ e^{At} $$.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên chứng minh tính chất nhóm một tham số $$ e^{A(t+s)}=e^{At}e^{As} $$, đồng thời kiểm tra lý do công thức $$ e^{(A+B)t}=e^{At}e^{Bt} $$ chỉ đúng khi $$ AB=BA $$.

## Tóm tắt dễ nhớ

Ma trận mũ $$ e^{At} $$ là toán tử tiến hóa đưa trạng thái ban đầu $$ \mathbf{x}_0 $$ sang trạng thái $$ \mathbf{x}(t)=e^{At}\mathbf{x}_0 $$. Chéo hóa và khối Jordan là các cách tính cụ thể của cùng một công cụ thống nhất cho hệ tuyến tính hệ số hằng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dự báo trạng thái trực tiếp
- Bài toán: Xác định trạng thái của hệ tuyến tính sau thời gian $$ t $$ từ trạng thái ban đầu.
- Mô hình: $$ \mathbf{x}(t)=e^{At}\mathbf{x}_0 $$.
- Giả thiết và giới hạn: Hệ tuyến tính hệ số hằng.
- Diễn giải: Ma trận mũ ánh xạ trực tiếp trạng thái đầu sang trạng thái tại thời điểm bất kỳ.

#### Rời rạc hóa trong mô phỏng số và điều khiển
- Bài toán: Cập nhật trạng thái hệ liên tục theo bước thời gian rời rạc $$ h $$.
- Mô hình: $$ \mathbf{x}(t+h)=e^{Ah}\mathbf{x}(t) $$.
- Giả thiết và giới hạn: Hệ thuần nhất (hoặc phần ngoại lực được xử lý riêng).
- Diễn giải: Công thức chuẩn để rời rạc hóa chính xác hệ tuyến tính trong điều khiển số.

#### Công thức thống nhất mọi trường hợp trị riêng
- Bài toán: Biểu diễn nghiệm mà không cần tách rời từng trường hợp thực, phức hay lặp.
- Mô hình: $$ e^{At}=I+At+\frac{(At)^2}{2!}+\cdots $$.
- Giả thiết và giới hạn: Luôn xác định với mọi ma trận vuông $$ A $$.
- Diễn giải: Bao trùm toàn bộ các kỹ thuật giải hệ thuần nhất hệ số hằng trong chương.

### 2. Trực giác bổ sung và các kết nối

Nếu $$ e^{rt} $$ giải phương trình vô hướng hệ số hằng, thì $$ e^{At} $$ giải hệ tuyến tính hệ số hằng. Mọi trường hợp đã học trước đó (trị riêng thực, phức, lặp) đều quy về việc tính hoặc phân tích cùng một đối tượng $$ e^{At} $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

A = np.array([[2, 0],
              [0, -1]], dtype=float)
t_values = [0.0, 0.5, 1.0, 1.5]
x0 = np.array([1.0, 1.0])

for t in t_values:
    xt = expm(A * t) @ x0
    plt.scatter(xt[0], xt[1], label=f"t={t}")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Trạng thái thu được qua ma trận mũ")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: matrix exponential intuition linear systems
- search: expm state transition visualization
- search: flow generated by matrix A animation

### 5. Bài toán mẫu có bối cảnh thực

Với
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix},
\qquad
e^{At}=
\begin{pmatrix}
e^{2t} & 0\\
0 & e^{-t}
\end{pmatrix},
$$
và điều kiện đầu $$ \mathbf{x}(0)=\begin{pmatrix} 1\\ 3 \end{pmatrix} $$, ta thu được ngay
$$
\mathbf{x}(t)=
\begin{pmatrix}
e^{2t}\\
3e^{-t}
\end{pmatrix}.
$$
Công thức ma trận mũ vừa giữ rõ cấu trúc các thành phần nghiệm vừa cho phép tính trực tiếp trạng thái tại mọi thời điểm.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vai trò của $$ e^{At} $$ và tính được cho ma trận đường chéo, chéo hóa được và khối Jordan bậc hai.

**Bậc sau đại học.** Chứng minh các tính chất toán tử và liên hệ với nửa nhóm (semigroup) tiến hóa của hệ tuyến tính.

## Video tham khảo

- Xem trước: [How (and why) to raise e to the power of a matrix | DE6](https://www.youtube.com/watch?v=O85OWBJ2ayo) — 3Blue1Brown, tiếng Anh. Giải thích vì sao $$ e^{At} $$ giải hệ $$ \mathbf{x}'=A\mathbf{x} $$ và cách tính hàm mũ ma trận.
- [Matrix Exponentials | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=qbyeQum8qTE) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về hàm mũ ma trận.
- [Lec 29 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=zreI4HllD80) — MIT OpenCourseWare, tiếng Anh. Bài giảng đầy đủ của giáo sư Mattuck xây dựng công thức hàm mũ ma trận.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày rõ ràng ứng dụng của ma trận mũ trong giải hệ tuyến tính.
- Arnold, *Ordinary Differential Equations*: nhấn mạnh trực giác dòng chảy và toán tử tiến hóa.
