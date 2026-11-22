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

Bài học này hướng dẫn cách dùng trị riêng và vector riêng để giải hệ tuyến tính khi ma trận có các trị riêng thực phân biệt, hiểu ý nghĩa của từng thành phần nghiệm riêng như một phương động học bất biến, và nhận diện hành vi hút, đẩy hay yên ngựa từ dấu của các trị riêng.

## Kiến thức nền

Sinh viên cần nắm phương trình đặc trưng của ODE hệ số hằng, khái niệm trị riêng, vector riêng và ma trận. Đây là bài đưa đại số tuyến tính vào trung tâm quá trình giải hệ ODE, nên trực giác về không gian vector rất quan trọng.

## Dẫn nhập

![Nghiệm theo hai trị riêng thực phân biệt]({{ site.imgurl }}/chapter_img/chapter04/03_eigenvalue_real_distinct.svg)

Với hệ tuyến tính $$ \mathbf{x}'=A\mathbf{x} $$, một câu hỏi tự nhiên là: tồn tại những phương nào mà khi hệ xuất phát dọc theo đó, quỹ đạo không bị bẻ lệch sang phương khác? Câu trả lời chính là các vector riêng của $$ A $$. Dọc theo những phương bất biến này, động lực học trở nên đơn giản nhất: trạng thái chỉ co lại hoặc giãn ra theo một hàm mũ.

Khi ma trận có đủ các trị riêng thực phân biệt, toàn bộ hệ tách thành các thành phần nghiệm độc lập rõ ràng. Mỗi thành phần có tốc độ tiến hóa riêng, và nghiệm tổng quát là tổ hợp tuyến tính của chúng. Qua đó, trị riêng và vector riêng trở thành công cụ trực tiếp để đọc hành vi động học của hệ.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Vector riêng là phương mà toán tử $$ A $$ không làm đổi hướng, chỉ làm thay đổi độ dài theo thời gian. Xuất phát trên phương đó, quỹ đạo chỉ đi thẳng vào gốc hoặc đi thẳng ra xa gốc.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, hai vector riêng xác định hai đường thẳng bất biến đi qua gốc. Các quỹ đạo khác thường uốn cong để tiệm cận một trong hai đường thẳng này khi thời gian tăng. Nếu một trị riêng dương và một trị riêng âm, gốc tọa độ là điểm yên ngựa: một phương hút về gốc và một phương đẩy ra xa.

### Cách nhìn hình thức

Thử nghiệm dạng $$ \mathbf{x}(t)=\mathbf{v}e^{\lambda t} $$ vào hệ $$ \mathbf{x}'=A\mathbf{x} $$, ta được
$$
\lambda \mathbf{v}e^{\lambda t}=A\mathbf{v}e^{\lambda t} \Rightarrow A\mathbf{v}=\lambda \mathbf{v}.
$$
Như vậy $$ \lambda $$ là trị riêng và $$ \mathbf{v} $$ là vector riêng của $$ A $$. Nếu $$ A $$ có hai trị riêng thực phân biệt $$ \lambda_1,\lambda_2 $$ ứng với hai vector riêng độc lập $$ \mathbf{v}_1,\mathbf{v}_2 $$, thì nghiệm tổng quát là
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$

## Những ngộ nhận thường gặp

- "Trị riêng chỉ dùng để tính nghiệm, không giúp hiểu động học." Sai: dấu của trị riêng quyết định trực tiếp tính ổn định của điểm cân bằng.
- "Vector riêng chỉ là bước trung gian đại số." Sai: chúng xác định các phương bất biến thực sự của trường vector.
- "Hai trị riêng cùng âm thì mọi quỹ đạo đi vào gốc giống hệt nhau." Không đúng: tốc độ hút dọc theo hai phương riêng khác nhau, nên quỹ đạo cong và tiệm cận phương suy giảm chậm hơn.
- "Thành phần có hệ số ban đầu lớn hơn sẽ luôn chi phối lâu dài." Sai: khi $$ t\to\infty $$, thành phần ứng với trị riêng lớn hơn mới chi phối hành vi dài hạn.

## Tiến trình học tập đề xuất

### Bước 1: Tìm các trị riêng

Giải phương trình đặc trưng $$ \det(A-\lambda I)=0 $$.

### Bước 2: Tìm các vector riêng tương ứng

Giải hệ thuần nhất $$ (A-\lambda I)\mathbf{v}=0 $$ cho từng trị riêng.

### Bước 3: Lập các nghiệm riêng dạng hàm mũ

Mỗi cặp $$ (\lambda_i, \mathbf{v}_i) $$ sinh ra một thành phần nghiệm $$ \mathbf{v}_ie^{\lambda_i t} $$.

### Bước 4: Viết nghiệm tổng quát và diễn giải động học

Đọc hướng hút, hướng đẩy và thành phần chi phối dài hạn từ dấu và độ lớn của các trị riêng.

### Các checkpoint

- Sinh viên có tính đúng trị riêng và vector riêng hay không.
- Sinh viên có viết chính xác dạng nghiệm $$ \mathbf{v}e^{\lambda t} $$ hay không.
- Sinh viên có xác định được phương hút và phương đẩy từ dấu của trị riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ chéo

Xét ma trận
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
Các trị riêng là $$ \lambda_1=3 $$ và $$ \lambda_2=-2 $$, với các vector riêng tương ứng
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
Nghiệm tổng quát là
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
Hệ có một phương đẩy và một phương hút, nên gốc tọa độ là điểm yên ngựa.

### Ví dụ 2: Ma trận không chéo có trị riêng thực phân biệt

Xét
$$
A=
\begin{pmatrix}
4 & 1\\
2 & 3
\end{pmatrix}.
$$
Phương trình đặc trưng là
$$
\det(A-\lambda I)=
\begin{vmatrix}
4-\lambda & 1\\
2 & 3-\lambda
\end{vmatrix}
=(4-\lambda)(3-\lambda)-2=\lambda^2-7\lambda+10=0,
$$
cho hai trị riêng $$ \lambda_1=5 $$ và $$ \lambda_2=2 $$. Vì cả hai trị riêng đều dương, mọi quỹ đạo không tầm thường đều đi ra xa gốc theo hai tốc độ khác nhau.

### Ví dụ 3: Xác định thành phần chi phối dài hạn

Với nghiệm $$ \mathbf{x}(t)=c_1\mathbf{v}_1e^{2t}+c_2\mathbf{v}_2e^{-t} $$, khi $$ t\to\infty $$, thành phần $$ e^{2t} $$ chi phối hoàn toàn nếu $$ c_1\neq 0 $$. Điều này cho thấy các thành phần nghiệm không đóng góp ngang nhau trong hành vi dài hạn.

### Ví dụ 4: Điều kiện đầu chọn tổ hợp các thành phần riêng

Khi cho điều kiện đầu $$ \mathbf{x}(0)=\mathbf{x}_0 $$, ta giải hệ tuyến tính $$ \mathbf{x}_0=c_1\mathbf{v}_1+c_2\mathbf{v}_2 $$ để tìm $$ c_1,c_2 $$. Điều kiện đầu thực chất là phép khai triển trạng thái ban đầu theo cơ sở vector riêng.

## Câu hỏi khái niệm

1. Vì sao các vector riêng là những phương bất biến đặc biệt của dòng chảy động lực học?
2. Vì sao dấu của trị riêng quyết định tính ổn định cục bộ của gốc tọa độ trong hệ tuyến tính?
3. Vì sao một thành phần nghiệm có thể chi phối toàn bộ hành vi dài hạn của hệ?

## Bài toán ứng dụng

1. Một mô hình kinh tế có một hướng tăng trưởng và một hướng suy thoái. Hãy diễn giải hiện tượng đó bằng cặp trị riêng trái dấu.
2. Một hệ sinh học có hai quá trình thư giãn với tốc độ khác nhau. Vì sao thành phần suy giảm chậm hơn thường quan sát được lâu hơn?
3. Một hệ cơ học tuyến tính hóa quanh điểm cân bằng có hai trị riêng dương. Kết quả này nói lên điều gì về tính ổn định của cân bằng đó?

## Chiến lược giảng dạy tương tác

- Cho sinh viên dự đoán hình thái quỹ đạo chỉ từ dấu của hai trị riêng trước khi giải chi tiết.
- Xét một ma trận chéo trước rồi chuyển sang ma trận không chéo để thấy cách đọc động học từ trị riêng hoàn toàn thống nhất.
- Hỏi lớp: "Nếu xuất phát đúng trên một vector riêng, quỹ đạo sẽ di chuyển ra sao?"
- Yêu cầu sinh viên vẽ hai đường thẳng bất biến trước khi viết công thức nghiệm tổng quát.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Luyện kỹ hệ hai chiều với ma trận hệ số nhỏ để sinh viên quan sát đồng thời trị riêng, vector riêng và chân dung pha, nhấn mạnh $$ \mathbf{v}e^{\lambda t} $$ là một hàm vector theo thời gian.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên chứng minh rằng các vector riêng ứng với các trị riêng phân biệt luôn độc lập tuyến tính, từ đó suy ra chúng tạo thành một cơ sở nghiệm đầy đủ cho hệ.

## Tóm tắt dễ nhớ

Khi ma trận có đủ trị riêng thực phân biệt, nghiệm tổng quát của hệ tuyến tính là tổ hợp các thành phần hàm mũ độc lập:
$$
\mathbf{x}(t)=\sum c_i\mathbf{v}_ie^{\lambda_i t}.
$$
Trị riêng quyết định tốc độ và dấu ổn định, còn vector riêng xác định phương chuyển động bất biến.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tương tác cạnh tranh hoặc hợp tác gần điểm cân bằng
- Bài toán: Quanh trạng thái cân bằng, hai biến quần thể biến đổi theo hai phương độc lập.
- Mô hình: $$ \mathbf{x}'=A\mathbf{x} $$ với $$ A $$ có hai trị riêng thực phân biệt.
- Giả thiết và giới hạn: Xấp xỉ tuyến tính cục bộ gần điểm cân bằng.
- Diễn giải: Mỗi vector riêng chỉ một phương bất biến và trị riêng tương ứng cho tốc độ tiến hóa dọc phương đó.

#### Hệ cơ học tại điểm yên ngựa
- Bài toán: Một phương ổn định và một phương bất ổn cùng tồn tại quanh điểm cân bằng.
- Mô hình: $$ \lambda_1>0 $$ và $$ \lambda_2<0 $$.
- Giả thiết và giới hạn: Hệ tuyến tính hoặc tuyến tính hóa gần cân bằng.
- Diễn giải: Điểm yên ngựa không ổn định nhưng có đường phân cách hút về gốc dọc theo phương trị riêng âm.

#### Đáp ứng quá độ hai thang thời gian
- Bài toán: Một hệ kỹ thuật có hai hằng số thời gian suy giảm khác nhau.
- Mô hình:
$$
\mathbf{x}(t)=c_1\mathbf{v}_1e^{\lambda_1 t}+c_2\mathbf{v}_2e^{\lambda_2 t}.
$$
- Giả thiết và giới hạn: Hai vector riêng độc lập tuyến tính.
- Diễn giải: Thành phần ứng với trị riêng lớn hơn (ít âm hơn) chi phối hành vi dài hạn.

### 2. Trực giác bổ sung và các kết nối

Phương pháp trị riêng cho hệ tuyến tính là phiên bản nhiều chiều của phương trình đặc trưng ở Chương 02: mỗi trị riêng tương ứng một tốc độ mũ và mỗi vector riêng xác định một phương bất biến, kết nối trực tiếp đại số tuyến tính với động lực học.

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

Xét ma trận
$$
A=
\begin{pmatrix}
3 & 0\\
0 & -2
\end{pmatrix}.
$$
Hai trị riêng $$ \lambda_1=3 $$ và $$ \lambda_2=-2 $$ có các vector riêng là hai trục tọa độ. Nghiệm tổng quát là
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
Trục $$ x_1 $$ là phương đẩy ra xa gốc, còn trục $$ x_2 $$ là phương hút về gốc — hình ảnh điển hình của điểm yên ngựa.

### 6. Phân tầng độ khó

**Bậc đại học.** Tính đúng trị riêng, vector riêng và lập nghiệm tổng quát.

**Bậc sau đại học.** Đọc nhanh thành phần chi phối, tính ổn định và cấu trúc yên ngựa trực tiếp từ phổ của ma trận.

## Video tham khảo

- Xem trước: [Phương trình vi phân - Phương pháp giá trị riêng giải hệ phương trình vi phân tuyến thuần nhất](https://www.youtube.com/watch?v=LVbsb6mAFZ4) — MATH KEY, tiếng Việt. Hướng dẫn phương pháp trị riêng cho hệ tuyến tính thuần nhất.
- [Solving Systems of Differential Equations with Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=Zwb5eiYcL8w) — Steve Brunton, tiếng Anh. Xây dựng nghiệm tổng quát từ các cặp trị riêng và vector riêng thực phân biệt.
- [2x2 Systems of ODEs: Sources and Sinks](https://www.youtube.com/watch?v=NaNdkCPLftc) — Steve Brunton, tiếng Anh. Phân tích điểm nguồn và điểm hút dựa trên dấu của hai trị riêng thực.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày chuẩn mực phương pháp trị riêng thực.
- Arnold, *Ordinary Differential Equations*: giàu trực giác hình học về phương bất biến và điểm yên ngựa.
