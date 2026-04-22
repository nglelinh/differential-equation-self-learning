---
layout: post
title: "04-03 Phương pháp Trị riêng: Thực Phân biệt"
chapter: '04'
order: 3
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên dùng trị riêng và vector riêng để giải hệ tuyến tính khi ma trận có các trị riêng thực phân biệt, hiểu ý nghĩa của mỗi mode riêng như một hướng động học bất biến, và đọc được hành vi tăng, giảm hay yên ngựa của hệ từ dấu của các trị riêng.

## Kiến thức nền

Sinh viên cần nắm phương trình đặc trưng của ODE hệ số hằng, vector riêng và ma trận. Đây là bài mà đại số tuyến tính bước vào trung tâm của giải ODE, nên trực giác về không gian vector rất quan trọng.

## Dẫn nhập

![Nghiệm theo hai trị riêng thực phân biệt]({{ site.imgurl }}/chapter_img/chapter04/03_eigenvalue_real_distinct.svg)

Nếu hệ tuyến tính được viết thành
$$ \mathbf{x}'=A\mathbf{x}, $$
thì câu hỏi tự nhiên là: có những hướng nào mà nếu hệ bắt đầu di chuyển đúng trên đó, nó sẽ không bị bẻ sang hướng khác? Câu trả lời chính là các vector riêng. Trên những hướng đặc biệt này, động lực học trở nên đơn giản nhất có thể: hệ chỉ bị co lại hoặc kéo giãn theo một hàm mũ.

Đây là trường hợp đẹp nhất của chương. Khi ma trận có đủ các trị riêng thực phân biệt, toàn bộ hệ tách thành các mode độc lập rõ ràng. Mỗi mode có một tốc độ riêng, và nghiệm tổng là sự chồng chập của các mode ấy. Từ đây, sinh viên có thể thấy trực tiếp vì sao trị riêng không chỉ là công cụ đại số, mà là ngôn ngữ đọc động lực học.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một vector riêng là một hướng mà hệ không làm đổi hướng, chỉ làm đổi độ dài theo thời gian. Nếu đi dọc hướng ấy, quỹ đạo không bị bẻ cong mà chỉ tiến thẳng ra xa hoặc co thẳng về gốc.

### Cách nhìn hình ảnh

Trong mặt phẳng pha, hai vector riêng tạo ra hai đường thẳng bất biến. Các quỹ đạo khác thường cong để bám gần một trong hai hướng đó khi thời gian lớn. Nếu một trị riêng dương và một trị riêng âm, ta nhìn thấy hình yên ngựa: một hướng hút, một hướng đẩy.

### Cách nhìn hình thức

Ta thử nghiệm dạng
$$ \mathbf{x}(t)=\mathbf{v}e^{\lambda t}. $$
Thế vào hệ:
$$
\lambda \mathbf{v}e^{\lambda t}=A\mathbf{v}e^{\lambda t}.
$$
Suy ra
$$ A\mathbf{v}=\lambda \mathbf{v}. $$
Vậy $$ \lambda $$ là trị riêng và $$ \mathbf{v} $$ là vector riêng. Nếu $$ A $$ có hai trị riêng thực phân biệt $$ \lambda_1,\lambda_2 $$ với các vector riêng độc lập $$ \mathbf{v}_1,\mathbf{v}_2 $$, thì nghiệm tổng quát là
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$

## Những ngộ nhận thường gặp

- "Trị riêng chỉ giúp giải hệ, không giúp hiểu hệ." Sai. Dấu của trị riêng quyết định trực tiếp ổn định.
- "Vector riêng chỉ là công cụ kỹ thuật." Sai. Chúng là các hướng bất biến thật sự của trường vector.
- "Nếu hai trị riêng đều âm thì mọi quỹ đạo giống hệt nhau." Không đúng. Chúng đều hút về gốc, nhưng theo những tốc độ và hướng khác nhau.
- "Mode có hệ số đầu lớn hơn sẽ luôn chi phối lâu dài." Sai. Thường mode có trị riêng lớn hơn mới chi phối khi $$ t\to\infty $$.

## Tiến trình học tập đề xuất

### Bước 1: Tìm trị riêng

Giải phương trình
$$ \det(A-\lambda I)=0. $$

### Bước 2: Tìm vector riêng

Giải
$$ (A-\lambda I)\mathbf{v}=0. $$

### Bước 3: Viết các mode mũ

Mỗi trị riêng sinh ra một mode.

### Bước 4: Ghép thành nghiệm tổng quát và đọc động học

Đây là bước quan trọng nhất về ý nghĩa.

### Các checkpoint

- Sinh viên có giải đúng trị riêng và vector riêng hay không.
- Sinh viên có viết đúng nghiệm dạng $$ \mathbf{v}e^{\lambda t} $$ hay không.
- Sinh viên có đọc được hướng hút và đẩy từ dấu của trị riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ chéo

Xét
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
Các trị riêng là
$$ \lambda_1=3,\qquad \lambda_2=-2, $$
với vector riêng tương ứng
$$
\mathbf{v}_1=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{v}_2=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Nghiệm tổng quát:
$$
\mathbf{x}(t)=
c_1e^{3t}
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
Hệ có một hướng đẩy và một hướng hút, nên gốc là một yên ngựa.

### Ví dụ 2: Ma trận không chéo nhưng có trị riêng thực phân biệt

Xét
$$
A=
\begin{pmatrix}
4 & 1\\
2 & 3
\end{pmatrix}.
$$
Ta có
$$
\det(A-\lambda I)=
\begin{vmatrix}
4-\lambda & 1\\
2 & 3-\lambda
\end{vmatrix}
=(4-\lambda)(3-\lambda)-2.
$$
Suy ra
$$ \lambda^2-7\lambda+10=0, $$
nên
$$ \lambda_1=5,\qquad \lambda_2=2. $$
Hai trị riêng đều dương, nên mọi quỹ đạo không tầm thường đều đi ra xa gốc, dù theo hai tốc độ khác nhau.

### Ví dụ 3: Đọc mode chi phối

Nếu nghiệm có dạng
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{2t}+c_2\mathbf{v}_2e^{-t},
$$
thì khi $$ t\to\infty $$, mode $$ e^{2t} $$ chi phối nếu $$ c_1\neq 0 $$. Điều này cho thấy hành vi dài hạn không do mọi mode quyết định như nhau.

### Ví dụ 4: Điều kiện đầu chọn quỹ đạo

Khi cho
$$ \mathbf{x}(0)=\mathbf{x}_0, $$
ta giải hệ
$$ \mathbf{x}_0=c_1\mathbf{v}_1+c_2\mathbf{v}_2 $$
để tìm $$ c_1,c_2 $$. Vì vậy điều kiện đầu đơn giản là cách chọn cách pha trộn các mode riêng.

## Câu hỏi khái niệm

1. Vì sao vector riêng là những hướng đặc biệt của dòng chảy?
2. Vì sao dấu của trị riêng quyết định ổn định cục bộ của gốc đối với hệ tuyến tính?
3. Vì sao một mode có thể chi phối toàn bộ hành vi dài hạn của hệ?

## Bài toán ứng dụng

1. Một mô hình kinh tế có một hướng tăng trưởng và một hướng suy thoái. Hãy diễn giải điều đó bằng trị riêng trái dấu.
2. Một hệ sinh học có hai mode thư giãn với tốc độ khác nhau. Hãy giải thích vì sao mode chậm hơn thường được quan sát lâu hơn.
3. Một hệ cơ học tuyến tính hóa quanh cân bằng có hai trị riêng dương. Điều đó nói gì về khả năng giữ ổn định của hệ?

## Chiến lược giảng dạy tương tác

- Cho sinh viên dự đoán hình học quỹ đạo chỉ từ dấu của hai trị riêng.
- Dùng một ma trận chéo trước, rồi một ma trận không chéo để sinh viên thấy trị riêng vẫn đọc động học như nhau.
- Hỏi lớp: "Nếu ta khởi đầu đúng trên vector riêng, quỹ đạo sẽ trông thế nào?"
- Cho sinh viên vẽ sơ bộ hai đường bất biến trước khi viết nghiệm tổng quát.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu làm thật chắc hệ 2 chiều với ma trận nhỏ, vì ở đó trị riêng, vector riêng và chân dung pha vẫn nhìn được cùng lúc. Cần nhấn mạnh nhiều lần rằng $$ \mathbf{v}e^{\lambda t} $$ là một nghiệm vector.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi giải thích tại sao các vector riêng ứng với trị riêng phân biệt luôn độc lập tuyến tính, và liên hệ điều này với việc tồn tại cơ sở nghiệm.

## Tóm tắt dễ nhớ

Khi ma trận có các trị riêng thực phân biệt, hệ tuyến tính tách thành các mode mũ độc lập:
$$
\mathbf{x}(t)=\sum c_i\mathbf{v}_ie^{\lambda_i t}.
$$
Trị riêng cho tốc độ và dấu ổn định, vector riêng cho hướng chuyển động. Đây là trường hợp đơn giản nhất nhưng cũng là nền tảng nhất của chương.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cạnh tranh hoặc hợp tác loài gần cân bằng
- Bài toán: Gần trạng thái cân bằng, hai biến có thể tăng giảm theo hai mode độc lập.
- Mô hình:
$$ \mathbf{x}'=A\mathbf{x} $$
với $$ A $$ có hai trị riêng thực phân biệt.
- Giả thiết và giới hạn: Tuyến tính hóa cục bộ quanh cân bằng.
- Diễn giải: Mỗi vector riêng là một hướng bất biến và mỗi trị riêng là tốc độ tiến hóa dọc hướng đó.

#### Hệ cơ học yên ngựa
- Bài toán: Một mode ổn định và một mode bất ổn cùng tồn tại trong cùng hệ.
- Mô hình:
$$ \lambda_1>0,\qquad \lambda_2<0. $$
- Giả thiết và giới hạn: Hệ tuyến tính hoặc tuyến tính hóa gần cân bằng.
- Diễn giải: Yên ngựa là cấu trúc cực kỳ quan trọng vì nó vừa hút vừa đẩy tùy hướng.

#### Tín hiệu quá độ hai tốc độ
- Bài toán: Một hệ kỹ thuật có hai time scale suy giảm khác nhau.
- Mô hình:
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$
- Giả thiết và giới hạn: Hai vector riêng độc lập.
- Diễn giải: Mode với trị riêng lớn hơn chi phối dài hạn.

### 2. Trực giác bổ sung và các kết nối

Phương pháp trị riêng cho hệ là phiên bản nhiều chiều của phương trình đặc trưng ở các chương trước. Mỗi trị riêng cho một mode, mỗi vector riêng cho một hướng. Đây là một trong những nơi đẹp nhất để sinh viên thấy đại số tuyến tính và động lực học là cùng một câu chuyện bằng hai ngôn ngữ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

A = np.array([[3, 0],
              [0, -2]])

def system(t, X):
    return A @ X

t = np.linspace(0, 2.5, 400)
for x0 in [(1, 1), (0.5, -1), (-1, 0.5)]:
    sol = solve_ivp(system, [0, 2.5], x0, t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f"IC={x0}")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Chân dung pha của một hệ có hai trị riêng thực phân biệt")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: saddle point phase portrait eigenvalues
- search: eigenvectors invariant directions visualization
- search: linear system real eigenvalues dynamics

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
Hai trị riêng:
$$ \lambda_1=3,\qquad \lambda_2=-2, $$
với vector riêng tương ứng là các trục tọa độ. Nghiệm tổng quát:
$$
\mathbf{x}(t)=
c_1
\begin{pmatrix}
1\\
0
\end{pmatrix}
e^{3t}
+
c_2
\begin{pmatrix}
0\\
1
\end{pmatrix}
e^{-2t}.
$$
Hướng $$ x_1 $$ là hướng đẩy, còn hướng $$ x_2 $$ là hướng hút. Đây là yên ngựa điển hình.

### 6. Phân tầng độ khó

**Bậc đại học.** Tìm đúng trị riêng, vector riêng và ghép nghiệm tổng quát.

**Bậc sau đại học.** Đọc mode trội, ổn định và cấu trúc yên ngựa trực tiếp từ phổ của ma trận.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày chuẩn về phương pháp trị riêng thực.
- Arnold, *Ordinary Differential Equations*: rất tốt cho trực giác về hướng bất biến và yên ngựa.
