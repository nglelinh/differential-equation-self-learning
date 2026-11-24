---
layout: post
title: "04-05 Phương pháp Trị riêng: Trùng"
chapter: '04'
order: 5
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---


Điều gì xảy ra khi ma trận $A$ cỡ $2\times 2$ có trị riêng kép $\lambda$, nhưng khi giải $(A - \lambda I)\mathbf{v} = \mathbf{0}$ ta chỉ tìm được **duy nhất một hướng vectơ riêng**? Ta đang thiếu mất một nghiệm để tạo đủ không gian nghiệm 2 chiều! Lời giải không phải là nhân $t$ đơn thuần vào $e^{\lambda t}\mathbf{v}$ (thử thay vào sẽ thấy sai ngay!), mà là xây dựng một **vectơ riêng suy rộng (generalized eigenvector)** $\mathbf{w}$ thỏa $(A - \lambda I)\mathbf{w} = \mathbf{v}$ để tạo ra cặp nghiệm hoàn hảo $(t\mathbf{v} + \mathbf{w})e^{\lambda t}$!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương pháp Trị riêng Trùng

1. **Bội đại số (AM) vs. Bội hình học (GM)**:
   - Nếu $\text{GM} = \text{AM}$ (ma trận đủ vectơ riêng, ví dụ $A = \lambda I$): vẫn đủ $n$ nghiệm dạng $e^{\lambda t}\mathbf{v}_k$—hình học là **nút sao (star node)**!
   - Nếu $\text{GM} < \text{AM}$ (ma trận thiếu hụt / defective): bắt buộc dùng chuỗi vectơ riêng suy rộng.
2. **Nghiệm thứ hai với Vectơ riêng suy rộng $\mathbf{w}$**:
   Tìm $\mathbf{v} \ne \mathbf{0}$ thỏa $(A - \lambda I)\mathbf{v} = \mathbf{0}$, rồi giải hệ không thuần nhất $(A - \lambda I)\mathbf{w} = \mathbf{v}$; khi đó:
   $$\mathbf{x}^{(2)}(t) = e^{\lambda t}(t\mathbf{v} + \mathbf{w}).$$
3. **Mẹo tính ngược cực nhanh cho cấp $2\times 2$**:
   Với ma trận $2\times 2$ thiếu hụt, $(A - \lambda I)^2 = 0$, nên bạn có thể chọn **bất kỳ vectơ $\mathbf{w}$ nào không phải vectơ riêng**, rồi đặt ngay $\mathbf{v} = (A - \lambda I)\mathbf{w}$—không cần giải hệ phương trình ngược!
4. **Hình học của Nút suy biến (Improper / Defective Node)**:
   Chỉ có đúng 1 đường thẳng bất biến dọc theo $\mathbf{v}$; mọi quỹ đạo khác uốn cong hình chữ S để tiếp xúc với hướng $\mathbf{v}$ khi tiến về gốc.

## Mục tiêu

Bài học này hướng dẫn cách giải hệ tuyến tính khi ma trận có trị riêng lặp, phân biệt rõ trường hợp "trị riêng lặp nhưng đủ vector riêng" với "trị riêng lặp nhưng thiếu vector riêng", hiểu vai trò của vector riêng suy rộng và lý do xuất hiện các số hạng dạng $$ te^{\lambda t} $$ trong nghiệm.

## Kiến thức nền

Sinh viên cần nắm khái niệm trị riêng, vector riêng, cách giải hệ có trị riêng thực phân biệt và tính độc lập tuyến tính. Đây là nơi cấu trúc khối Jordan xuất hiện cụ thể trong động lực học.

## Dẫn nhập

![Trị riêng lặp và vector riêng tổng quát]({{ site.imgurl }}/chapter_img/chapter04/05_eigenvalue_repeated.svg)

Khi đa thức đặc trưng có nghiệm lặp, cách xử lý phụ thuộc vào số vector riêng độc lập tuyến tính tìm được. Nếu ma trận vẫn có đủ vector riêng (chéo hóa được), nghiệm vẫn chỉ gồm các hàm mũ thuần túy. Ngược lại, nếu thiếu vector riêng, ma trận không chéo hóa được và nghiệm xuất hiện thêm thành phần nhân với $$ t $$.

Trường hợp này cho thấy đại số tuyến tính không chỉ hỗ trợ tính toán mà còn chỉ ra sự thiếu hụt phương bất biến, đòi hỏi bổ sung vector riêng suy rộng. Trên mặt phẳng pha, quỹ đạo khi đó có một phương chính kèm hiệu ứng trượt dọc theo phương đó.

### Khung giải thích (nên đọc chậm): Giải hệ thiếu hụt $\mathbf{x}' = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}\mathbf{x}$ bằng mẹo vectơ suy rộng cực gọn

1. **Tìm trị riêng**:
   $\tau = 3 + 1 = 4$, $\Delta = 3 - (-1) = 4 \implies \lambda^2 - 4\lambda + 4 = (\lambda - 2)^2 = 0 \implies \lambda = \mathbf{2}$ (bội 2).
2. **Tính ma trận $N = A - 2I$**:
   $$N = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \ne 0 \quad (\text{hạng } 1 \implies \text{GM} = 1 < 2).$$
3. **Áp dụng mẹo chọn $\mathbf{w}$ trước**:
   Chọn $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ (không nằm trong $\ker N$). Tính ngay vectơ riêng tương ứng:
   $$\mathbf{v} = N\mathbf{w} = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \mathbf{\begin{pmatrix} 1 \\ -1 \end{pmatrix}}.$$
   (Kiểm tra nhanh: $N\mathbf{v} = \begin{pmatrix} 1-1 \\ -1+1 \end{pmatrix} = \mathbf{0}$, đúng là vectơ riêng!).
4. **Nghiệm tổng quát**:
   $$\mathbf{x}(t) = c_1 e^{2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} + c_2 e^{2t}\left[t\begin{pmatrix} 1 \\ -1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right].$$

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi thiếu vector riêng, hệ không có đủ các phương độc lập chỉ co giãn thuần túy; thay vào đó, một phương chính phải kết hợp với một thành phần phụ tạo nên hiệu ứng trượt theo thời gian dọc theo phương chính đó.

### Cách nhìn hình ảnh

Với trị riêng lặp và ma trận không chéo hóa được, các quỹ đạo vẫn hút về hoặc đẩy ra theo một phương chủ đạo duy nhất, nhưng hình dạng bị uốn lệch thay vì đối xứng thẳng đều như trường hợp đủ vector riêng. Số hạng $$ te^{\lambda t} $$ phản ánh trực tiếp sự uốn lệch này.

### Cách nhìn hình thức

Nếu $$ \lambda $$ là trị riêng bội 2 của ma trận $$ 2\times 2 $$ nhưng chỉ có một vector riêng độc lập $$ \mathbf{v} $$, ta tìm một vector riêng suy rộng $$ \mathbf{w} $$ thỏa mãn
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$
Hai nghiệm độc lập tuyến tính khi đó là $$ e^{\lambda t}\mathbf{v} $$ và $$ e^{\lambda t}(t\mathbf{v}+\mathbf{w}) $$, nên nghiệm tổng quát có dạng
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$

## Những ngộ nhận thường gặp

- "Mọi trường hợp trị riêng lặp đều phải dùng vector riêng suy rộng." Sai: trước tiên phải kiểm tra xem ma trận có đủ vector riêng độc lập hay không.
- "Trị riêng lặp thiếu vector riêng chỉ cần nhân thêm hằng số." Sai: cần bổ sung thành phần chứa $$ t $$ gắn với vector riêng suy rộng.
- "Vector riêng suy rộng chỉ là mẹo biến đổi hình thức." Sai: nó bổ sung đúng chiều còn thiếu của không gian nghiệm.
- "Hai ma trận có cùng trị riêng lặp sẽ có cùng chân dung pha." Sai: số lượng vector riêng độc lập tạo ra sự khác biệt rõ rệt về hình học quỹ đạo.

## Tiến trình học tập đề xuất

### Bước 1: Tìm trị riêng lặp

Nhận diện nghiệm bội của đa thức đặc trưng.

### Bước 2: Kiểm tra số lượng vector riêng độc lập

Đây là bước phân nhánh quyết định cách viết nghiệm.

### Bước 3: Tìm vector riêng suy rộng nếu thiếu vector riêng

Giải hệ $$ (A-\lambda I)\mathbf{w}=\mathbf{v} $$.

### Bước 4: Viết nghiệm tổng quát

Kết hợp hai nghiệm độc lập với đầy đủ thành phần $$ t\mathbf{v}+\mathbf{w} $$.

### Các checkpoint

- Sinh viên có phân biệt đúng trường hợp chéo hóa được và không chéo hóa được hay không.
- Sinh viên có giải đúng vector riêng suy rộng $$ \mathbf{w} $$ hay không.
- Sinh viên có hiểu lý do xuất hiện thừa số $$ t $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Trị riêng lặp nhưng đủ vector riêng

Ma trận
$$
A=
\begin{pmatrix}
2 & 0\\
0 & 2
\end{pmatrix}
$$
có trị riêng lặp $$ \lambda=2 $$, nhưng mọi vector khác 0 đều là vector riêng. Nghiệm tổng quát đơn giản là $$ \mathbf{x}(t)=e^{2t}\mathbf{c} $$, cho thấy trị riêng lặp không tự động làm bài toán phức tạp hơn.

### Ví dụ 2: Trị riêng lặp thiếu vector riêng

Xét
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
Trị riêng duy nhất là $$ \lambda=1 $$, với
$$
A-I=
\begin{pmatrix}
0 & 1\\
0 & 0
\end{pmatrix}.
$$
Giải $$ (A-I)\mathbf{v}=0 $$ cho vector riêng $$ \mathbf{v}=\begin{pmatrix} 1\\ 0 \end{pmatrix} $$. Tiếp theo, giải $$ (A-I)\mathbf{w}=\mathbf{v} $$ với $$ \mathbf{w}=\begin{pmatrix} w_1\\ w_2 \end{pmatrix} $$:
$$
\begin{pmatrix}
w_2\\
0
\end{pmatrix}
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
nên có thể chọn $$ \mathbf{w}=\begin{pmatrix} 0\\ 1 \end{pmatrix} $$. Nghiệm tổng quát là
$$
\mathbf{x}(t)=c_1e^t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^t
\left(
t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
\begin{pmatrix}
0\\
1
\end{pmatrix}
\right)
=
e^t
\begin{pmatrix}
c_1+c_2t\\
c_2
\end{pmatrix}.
$$

### Ví dụ 3: Ý nghĩa của thừa số $$ t $$

Số hạng $$ te^{\lambda t} $$ thể hiện rằng ngoài sự co giãn theo hàm mũ còn có thành phần trượt tăng tuyến tính theo thời gian — dấu hiệu đặc trưng của khối Jordan không chéo hóa được.

### Ví dụ 4: So sánh hai hệ có cùng trị riêng

Hai ma trận
$$
\begin{pmatrix}
2 & 0\\
0 & 2
\end{pmatrix}
\qquad \text{và} \qquad
\begin{pmatrix}
2 & 1\\
0 & 2
\end{pmatrix}
$$
đều có trị riêng bội $$ \lambda=2 $$, nhưng ma trận thứ nhất chéo hóa được còn ma trận thứ hai không. Ví dụ này khẳng định rằng riêng trị riêng chưa đủ để mô tả trọn vẹn cấu trúc nghiệm.

## Câu hỏi khái niệm

1. Vì sao trị riêng lặp không phải lúc nào cũng dẫn tới thừa số $$ t $$?
2. Vector riêng suy rộng bổ sung điều gì cho không gian nghiệm?
3. Vì sao số hạng $$ te^{\lambda t} $$ là đặc trưng của ma trận không chéo hóa được?

## Bài toán ứng dụng

1. Một hệ điều khiển có hai thành phần trùng tốc độ nhưng chỉ có một phương riêng. Điều này ảnh hưởng thế nào đến hình dạng quỹ đạo?
2. Trong cơ học tuyến tính hóa, vì sao hai hệ có cùng tập trị riêng vẫn có thể cho chân dung pha khác nhau?
3. Một quá trình lặp có ma trận gần khối Jordan có thể gây khó khăn gì về mặt hình học và tính toán số?

## Chiến lược giảng dạy tương tác

- Đặt song song hai ma trận cùng trị riêng lặp nhưng khác số vector riêng để lớp so sánh trực tiếp.
- Cho sinh viên tự giải hệ tìm vector riêng suy rộng theo nhóm.
- Hỏi lớp: "Khi thiếu một vector riêng, ta cần điều kiện nào để tạo nghiệm độc lập thứ hai?"
- Vẽ so sánh chân dung pha nút sao (đủ vector riêng) và nút suy biến (thiếu vector riêng).

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Cho sinh viên tuân theo đúng trình tự bốn bước: tìm trị riêng, đếm số vector riêng độc lập, giải $$ (A-\lambda I)\mathbf{w}=\mathbf{v} $$ nếu thiếu, rồi lắp vào công thức nghiệm tổng quát.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên liên hệ trường hợp này với dạng chuẩn Jordan và tính trực tiếp hàm mũ ma trận $$ e^{Jt} $$ của một khối Jordan bậc hai.

## Tóm tắt dễ nhớ

Với trị riêng lặp, luôn kiểm tra xem ma trận có đủ vector riêng độc lập hay không. Nếu thiếu, ta tìm vector riêng suy rộng từ $$ (A-\lambda I)\mathbf{w}=\mathbf{v} $$ và thu được nghiệm chứa thừa số $$ te^{\lambda t} $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ thiếu phương riêng
- Bài toán: Ma trận có trị riêng lặp nhưng không đủ vector riêng, làm quỹ đạo trượt dọc theo phương chính duy nhất.
- Mô hình: $$ (A-\lambda I)\mathbf{w}=\mathbf{v} $$.
- Giả thiết và giới hạn: Ma trận không chéo hóa được.
- Diễn giải: Vector riêng suy rộng cung cấp phương độc lập còn thiếu để lập cơ sở nghiệm.

#### Khối Jordan bậc hai trong điều khiển
- Bài toán: Một cực lặp trong hệ tuyến tính tạo ra thừa số $$ t $$ trong đáp ứng quá độ.
- Mô hình:
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$
- Giả thiết và giới hạn: Cấu trúc khối Jordan kích thước 2.
- Diễn giải: Thừa số $$ t $$ có thể gây tăng trưởng tạm thời ngay cả khi $$ \lambda<0 $$.

#### Suy giảm có thành phần trượt
- Bài toán: Dù chỉ có một trị riêng duy nhất, hệ vẫn có hai nghiệm độc lập tuyến tính nhờ vector riêng suy rộng.
- Mô hình: Hệ tuyến tính có trị riêng lặp, thiếu vector riêng.
- Giả thiết và giới hạn: Trường hợp biên quan trọng giữa nút thực và xoắn ốc.
- Diễn giải: Không thể chỉ lấy hai bội hằng của cùng một vector riêng.

### 2. Trực giác bổ sung và các kết nối

Bài học này thể hiện trực tiếp cấu trúc Jordan trên mặt phẳng pha. Hiểu rằng thừa số $$ t $$ bắt nguồn từ việc thiếu vector riêng sẽ giúp sinh viên nắm chắc bước chuyển sang bài hàm mũ ma trận ở phần tiếp theo.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 400)
x1 = np.exp(t)
x2 = t * np.exp(t)

plt.plot(t, x1, label=r"$e^t$")
plt.plot(t, x2, label=r"$t e^t$")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Số hạng suy rộng khi trị riêng lặp")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Jordan block phase portrait visualization
- search: repeated eigenvalue generalized eigenvector intuition
- search: te^lambda t linear system explanation

### 5. Bài toán mẫu có bối cảnh thực

Xét lại ma trận
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
Với trị riêng $$ \lambda=1 $$, vector riêng $$ \mathbf{v}=\begin{pmatrix} 1\\ 0 \end{pmatrix} $$ và vector riêng suy rộng $$ \mathbf{w}=\begin{pmatrix} 0\\ 1 \end{pmatrix} $$ tìm từ $$ (A-I)\mathbf{w}=\mathbf{v} $$, nghiệm tổng quát là
$$
\mathbf{x}(t)=
c_1e^t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
c_2e^t
\left(
t
\begin{pmatrix}
1\\
0
\end{pmatrix}
+
\begin{pmatrix}
0\\
1
\end{pmatrix}
\right).
$$
Ví dụ minh họa trực tiếp sự xuất hiện tất yếu của thừa số $$ t $$ khi ma trận không chéo hóa được.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ trị riêng lặp đủ vector riêng và thiếu vector riêng; giải được trường hợp hệ $$ 2\times 2 $$.

**Bậc sau đại học.** Liên hệ với dạng chuẩn Jordan, đa thức tối tiểu và chuỗi vector riêng suy rộng kích thước bất kỳ.

## Video tham khảo

- Xem trước: [Repeated Eigenvalues and Secular Terms: Transient Growth in Non-Normal Systems](https://www.youtube.com/watch?v=9xWqNPXRl7o) — Steve Brunton, tiếng Anh. Phân tích trị riêng lặp, thừa số $$ t $$ và hiện tượng tăng trưởng tạm thời.
- [Lec 26 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=hEtWqTPPXuc) — MIT OpenCourseWare, tiếng Anh. Bài giảng của giáo sư Mattuck về trường hợp trị riêng lặp.
- [Systems of Differential Equations: Diagonalization and Jordan Canonical Form](https://www.youtube.com/watch?v=SsCiQym5yQU) — Steve Brunton, tiếng Anh. Trình bày dạng chuẩn Jordan khi thiếu vector riêng độc lập.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày rõ kỹ thuật giải trường hợp trị riêng lặp và vector riêng suy rộng.
- Arnold, *Ordinary Differential Equations*: giải thích sâu ý nghĩa hình học của cấu trúc Jordan.
