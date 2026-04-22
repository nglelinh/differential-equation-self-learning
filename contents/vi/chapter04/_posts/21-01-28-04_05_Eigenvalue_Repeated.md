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

## Mục tiêu

Bài học này giúp sinh viên xử lý trường hợp trị riêng lặp, phân biệt giữa "trị riêng lặp nhưng đủ vector riêng" và "trị riêng lặp thiếu vector riêng", hiểu vai trò của vector riêng suy rộng, và nhận ra vì sao các số hạng kiểu $$ te^{\lambda t} $$ xuất hiện trong nghiệm.

## Kiến thức nền

Sinh viên cần nắm trị riêng, vector riêng, nghiệm hệ với trị riêng thực phân biệt và một ít trực giác về độc lập tuyến tính. Đây là bài mà cấu trúc Jordan bắt đầu ló ra dưới dạng động học cụ thể.

## Dẫn nhập

![Trị riêng lặp và vector riêng tổng quát]({{ site.imgurl }}/chapter_img/chapter04/05_eigenvalue_repeated.svg)

Khi trị riêng bị lặp, nhiều sinh viên có xu hướng nghĩ rằng hệ chỉ đơn giản là trường hợp cũ nhưng ít số khác nhau hơn. Thực ra đây là một bước tinh tế hơn nhiều. Nếu ma trận vẫn có đủ vector riêng, mọi việc còn khá êm. Nhưng nếu không đủ vector riêng, hệ không thể chéo hóa, và động học xuất hiện một thành phần mới không còn là mũ thuần túy: đó là các số hạng có nhân thêm $$ t $$.

Đây là lúc sinh viên thấy rõ rằng đại số tuyến tính không chỉ cho phép giải bài, mà còn cho biết khi nào một hệ có cấu trúc thiếu "hướng riêng" và phải bổ sung bằng hướng suy rộng. Hình học của quỹ đạo khi đó cũng khác đi: có một hướng chính và một hiệu ứng trượt dọc theo hướng ấy.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu ở trường hợp đẹp, hệ có đủ các hướng động học độc lập, thì ở trường hợp lặp thiếu vector riêng, một hướng chính phải "gánh thêm" một hướng phụ gắn vào nó. Quỹ đạo không chỉ co giãn theo một mũ, mà còn trượt dọc theo hướng đó theo nhịp thời gian.

### Cách nhìn hình ảnh

Khi trị riêng lặp và ma trận không chéo hóa được, các quỹ đạo thường vẫn bị hút hoặc đẩy theo một hướng chủ đạo, nhưng không đối xứng đẹp như trường hợp chéo hóa được. Các số hạng $$ te^{\lambda t} $$ chính là dấu vết của sự thiếu hụt vector riêng này trong hình học.

### Cách nhìn hình thức

Nếu $$ \lambda $$ là trị riêng lặp và chỉ có một vector riêng $$ \mathbf{v} $$, ta tìm vector riêng suy rộng $$ \mathbf{w} $$ thỏa
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$
Khi đó hai nghiệm độc lập có thể chọn là
$$ e^{\lambda t}\mathbf{v}, $$
và
$$ e^{\lambda t}(t\mathbf{v}+\mathbf{w}). $$
Do đó nghiệm tổng quát là
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$

## Những ngộ nhận thường gặp

- "Trị riêng lặp luôn gây khó như nhau." Sai. Cần xem có đủ vector riêng hay không.
- "Nếu trị riêng lặp thì chỉ cần nhân thêm một hằng số khác." Sai. Khi thiếu vector riêng, phải có số hạng nhân thêm $$ t $$.
- "Vector riêng suy rộng chỉ là mẹo hình thức." Sai. Nó là cách bù cho hướng riêng còn thiếu.
- "Hai ma trận có cùng trị riêng lặp sẽ có cùng hình học." Không đúng. Số vector riêng quyết định sự khác biệt lớn.

## Tiến trình học tập đề xuất

### Bước 1: Tìm trị riêng lặp

Nhận ra đa thức đặc trưng có nghiệm lặp.

### Bước 2: Kiểm tra số vector riêng

Đây là bước phân nhánh quan trọng nhất.

### Bước 3: Nếu thiếu vector riêng, tìm vector suy rộng

Giải
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$

### Bước 4: Viết nghiệm tổng quát

Nhớ sự xuất hiện của $$ t\mathbf{v}+\mathbf{w} $$.

### Các checkpoint

- Sinh viên có phân biệt được lặp nhưng chéo hóa được với lặp không chéo hóa được hay không.
- Sinh viên có tìm đúng vector suy rộng hay không.
- Sinh viên có hiểu vì sao xuất hiện thừa số $$ t $$ hay không.

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
có trị riêng lặp $$ \lambda=2 $$, nhưng mọi vector khác 0 đều là vector riêng. Nghiệm tổng quát chỉ đơn giản là
$$ \mathbf{x}(t)=e^{2t}\mathbf{c}. $$
Đây là lời nhắc quan trọng: lặp trị riêng chưa chắc gây rắc rối.

### Ví dụ 2: Trị riêng lặp thiếu vector riêng

Xét
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
Trị riêng duy nhất là $$ \lambda=1 $$. Ta có
$$
A-I=
\begin{pmatrix}
0 & 1\\
0 & 0
\end{pmatrix}.
$$
Giải
$$ (A-I)\mathbf{v}=0 $$
cho vector riêng
$$
\mathbf{v}=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Tiếp theo tìm $$ \mathbf{w} $$ sao cho
$$ (A-I)\mathbf{w}=\mathbf{v}. $$
Viết
$$
\mathbf{w}=
\begin{pmatrix}
w_1\\
w_2
\end{pmatrix},
$$
ta cần
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
nên có thể lấy
$$
\mathbf{w}=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Nghiệm tổng quát:
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

Số hạng
$$ te^{\lambda t} $$
cho thấy ngoài co giãn mũ còn có một hiệu ứng trượt tuyến tính theo thời gian. Đây chính là dấu hiệu động học của khối Jordan.

### Ví dụ 4: So sánh hai hệ cùng trị riêng

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
đều có trị riêng lặp $$ 2 $$, nhưng hệ thứ nhất chéo hóa được còn hệ thứ hai không. So sánh này rất tốt để dạy rằng trị riêng thôi chưa kể hết câu chuyện.

## Câu hỏi khái niệm

1. Vì sao trị riêng lặp không tự động kéo theo khó khăn?
2. Vector riêng suy rộng đang bù cho điều gì còn thiếu trong cấu trúc nghiệm?
3. Vì sao số hạng $$ te^{\lambda t} $$ là dấu hiệu đặc trưng của trường hợp không chéo hóa được?

## Bài toán ứng dụng

1. Một hệ điều khiển có hai mode trùng tốc độ nhưng chỉ một hướng riêng. Điều này có thể ảnh hưởng thế nào đến hình dạng quỹ đạo?
2. Trong cơ học tuyến tính hóa, vì sao hai hệ có cùng trị riêng vẫn có thể cho quỹ đạo khác nhau?
3. Một mô hình số học lặp nhiều bước sinh ra ma trận gần Jordan. Hãy dự đoán khó khăn hình học có thể xuất hiện.

## Chiến lược giảng dạy tương tác

- So sánh trực tiếp hai ma trận có cùng trị riêng lặp nhưng khác số vector riêng.
- Để sinh viên tự tìm vector suy rộng theo nhóm, vì đây là bước dễ mắc lỗi đại số nhưng lại rất đáng để tự làm.
- Hỏi lớp: "Nếu thiếu một vector riêng, ta cần thêm thông tin kiểu gì để đủ cơ sở nghiệm?"
- Vẽ sơ bộ quỹ đạo của trường hợp chéo hóa được và không chéo hóa được để nhấn mạnh khác biệt hình học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu dùng một checklist rõ ràng: tìm trị riêng, tìm số vector riêng, nếu thiếu thì giải phương trình cho vector suy rộng, rồi mới viết nghiệm. Tránh để các em nhảy ngay vào công thức có $$ t $$ mà không hiểu lý do.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi liên hệ trực tiếp trường hợp này với dạng Jordan và ma trận mũ của một khối Jordan, để thấy công thức nghiệm xuất hiện rất tự nhiên từ
$$ e^{Jt}. $$

## Tóm tắt dễ nhớ

Trị riêng lặp chỉ thực sự khó khi thiếu vector riêng. Khi đó, ta cần vector suy rộng và nghiệm mới sẽ có dạng chứa
$$ te^{\lambda t}. $$
Muốn xử lý đúng, hãy luôn hỏi hai câu: trị riêng có lặp không, và số vector riêng có đủ không.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ thiếu hướng riêng
- Bài toán: Một ma trận có trị riêng lặp nhưng không đủ vector riêng, nên quỹ đạo có hiện tượng trượt dọc theo hướng chính.
- Mô hình:
$$ (A-\lambda I)\mathbf{w}=\mathbf{v}. $$
- Giả thiết và giới hạn: Ma trận không chéo hóa được.
- Diễn giải: Vector riêng suy rộng bổ sung hướng động học còn thiếu.

#### Hệ điều khiển Jordan bậc hai
- Bài toán: Một mode lặp trong hệ tuyến tính tạo ra nhân tử $$ t $$ trong đáp ứng.
- Mô hình:
$$
\mathbf{x}(t)=c_1e^{\lambda t}\mathbf{v}+c_2e^{\lambda t}(t\mathbf{v}+\mathbf{w}).
$$
- Giả thiết và giới hạn: Cấu trúc Jordan kích thước 2.
- Diễn giải: Nhân tử $$ t $$ là dấu vết động lực học của việc ma trận không đủ vector riêng.

#### Dao động hoặc suy giảm có trượt
- Bài toán: Dù chỉ có một trị riêng, hệ vẫn có hai hướng động học độc lập khi tính thêm vector suy rộng.
- Mô hình: Trị riêng lặp, thiếu vector riêng.
- Giả thiết và giới hạn: Chỉ là một dạng đặc biệt nhưng rất quan trọng.
- Diễn giải: Không thể chỉ "nhân thêm hằng số" như trường hợp đẹp.

### 2. Trực giác bổ sung và các kết nối

Bài học này là nơi cấu trúc Jordan hiện ra dưới dạng quỹ đạo thật. Sinh viên thường chỉ nhớ quy tắc thêm $$ t $$, nhưng điều quan trọng hơn là hiểu vì sao nó phải xuất hiện: hệ thiếu một hướng riêng thực sự. Đây cũng là bước chuẩn bị trực tiếp cho ma trận mũ và các khối Jordan.

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

Xét
$$
A=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$
Trị riêng duy nhất là
$$ \lambda=1. $$
Một vector riêng là
$$
\mathbf{v}=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Tìm vector suy rộng từ
$$ (A-I)\mathbf{w}=\mathbf{v} $$
cho ta có thể chọn
$$
\mathbf{w}=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$
Vì vậy nghiệm tổng quát là
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
Điều cốt lõi là sự xuất hiện tất yếu của nhân tử $$ t $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ trường hợp lặp nhưng đủ vector riêng với trường hợp thiếu vector riêng.

**Bậc sau đại học.** Liên hệ với khối Jordan, đa thức tối tiểu và động học của ma trận không chéo hóa được.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: phần trị riêng lặp và vector suy rộng rất phù hợp để học kỹ thuật.
- Arnold, *Ordinary Differential Equations*: tốt cho việc hiểu ý nghĩa hình học của cấu trúc Jordan.
