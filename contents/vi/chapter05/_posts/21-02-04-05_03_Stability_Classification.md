---
layout: post
title: "05-03 Phân loại Ổn định"
chapter: '05'
order: 3
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên phân biệt các khái niệm ổn định Lyapunov, ổn định tiệm cận và không ổn định, dùng trị riêng hoặc cặp trace-determinant để phân loại cân bằng của hệ phẳng, và hiểu rằng "ổn định" là một câu hỏi về phản ứng của hệ với nhiễu nhỏ chứ không chỉ là tên gọi hình học.

## Kiến thức nền

Sinh viên cần nắm tuyến tính hóa và trị riêng của Jacobian. Một mức quen thuộc với chân dung pha từ chương trước cũng rất hữu ích để liên hệ giữa ngôn ngữ đại số và hình học.

## Dẫn nhập

![Phân loại ổn định từ phổ của Jacobian]({{ site.imgurl }}/chapter_img/chapter05/03_stability_classification.svg)

Khi nói một hệ "ổn định", ta thường dùng ngôn ngữ đời thường rất mơ hồ. Trong động lực học, ổn định cần được hiểu rất chính xác. Nếu ta đẩy hệ lệch đi một chút khỏi cân bằng, nó có ở gần đó không, có quay về đó không, hay nó bỏ chạy ra xa? Ba câu hỏi này nghe giống nhau nhưng dẫn đến ba khái niệm khác nhau.

Bài học này quan trọng vì nó giúp sinh viên ngừng dùng ổn định như một nhãn cảm tính. Thay vào đó, các em học cách đọc nó từ cấu trúc phổ của Jacobian hoặc từ chân dung pha. Đây là bước để tư duy định tính trở nên thật sự chính xác.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một cái bát úp ngửa, một viên bi nằm dưới đáy bát và một viên bi nằm trên đỉnh đồi minh họa rất tốt các kiểu ổn định. Dưới đáy bát, viên bi bị lệch một chút vẫn ở gần và thường quay lại. Trên đỉnh đồi, lệch nhỏ cũng khiến nó rời xa. Đây là trực giác nền cho ổn định.

### Cách nhìn hình ảnh

Trong mặt phẳng pha, một cân bằng ổn định tiệm cận có các quỹ đạo lân cận tiến vào nó. Một cân bằng ổn định nhưng không tiệm cận có thể giữ quỹ đạo ở gần mà không hút vào, như tâm tuyến tính. Một cân bằng không ổn định có quỹ đạo rời xa với nhiễu nhỏ.

### Cách nhìn hình thức

Một điểm cân bằng là ổn định theo Lyapunov nếu mọi nghiệm bắt đầu đủ gần nó đều luôn ở gần nó. Nó ổn định tiệm cận nếu ngoài điều đó ra, nghiệm còn tiến về cân bằng khi $$ t\to\infty $$. Nó không ổn định nếu tồn tại các nhiễu nhỏ làm quỹ đạo rời xa khỏi lân cận đã chọn.

Với Jacobian $$ J $$ của hệ 2 chiều, đặt
$$ \tau=\operatorname{tr}(J),\qquad \Delta=\det(J). $$
Khi $$ \Delta<0 $$, cân bằng là yên ngựa nên không ổn định. Khi $$ \Delta>0 $$, ta xét tiếp dấu của $$ \tau $$ và của
$$ \tau^2-4\Delta. $$

## Những ngộ nhận thường gặp

- "Ổn định và ổn định tiệm cận là một." Sai. Có hệ giữ quỹ đạo ở gần nhưng không kéo về điểm cân bằng.
- "Nếu quỹ đạo quay quanh cân bằng thì cân bằng chắc chắn không ổn định." Không đúng; tâm là ví dụ quay mà vẫn ổn định Lyapunov.
- "Yên ngựa chỉ là một tên hình học, không liên quan đến ổn định." Sai. Nó là kiểu cân bằng điển hình của không ổn định.
- "Chỉ cần nhìn hình vẽ là đủ, không cần định nghĩa." Không nên. Định nghĩa giúp tránh nhầm giữa "ở gần" và "quay về".

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt các khái niệm ổn định

Rõ ràng bằng lời trước khi làm tính.

### Bước 2: Dùng Jacobian hoặc trace-determinant

Đọc loại phổ của cân bằng.

### Bước 3: Ghép phổ với chân dung pha

Đừng để đại số và hình học tách rời nhau.

### Bước 4: Kiểm tra ý nghĩa động học

Quỹ đạo ở gần, quay về hay bỏ chạy?

### Các checkpoint

- Sinh viên có phân biệt được ổn định và ổn định tiệm cận hay không.
- Sinh viên có dùng đúng $$ \tau,\Delta $$ để phân loại không.
- Sinh viên có ghép đúng kiểu phổ với kiểu chân dung pha hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Yên ngựa không ổn định

Nếu Jacobian có trị riêng
$$ \lambda_1>0,\qquad \lambda_2<0, $$
thì tồn tại một hướng đẩy và một hướng hút. Chỉ riêng điều này đã đủ để kết luận cân bằng không ổn định. Đây là lý do mọi yên ngựa đều là điểm không ổn định.

### Ví dụ 2: Nút hút

Nếu
$$ \lambda_1<0,\qquad \lambda_2<0, $$
thì các mode đều suy giảm. Cân bằng là ổn định tiệm cận. Quỹ đạo có thể không đi thẳng vào gốc, nhưng cuối cùng vẫn tiến về đó.

### Ví dụ 3: Tâm

Nếu Jacobian có trị riêng
$$ \pm i\beta, $$
thì hệ tuyến tính hóa cho tâm. Quỹ đạo quay quanh cân bằng với biên độ không đổi. Đây là ví dụ điển hình cho ổn định nhưng không tiệm cận trong hệ tuyến tính.

### Ví dụ 4: Dùng trace-determinant

Cho
$$
J=
\begin{pmatrix}
-2 & 1\\
-4 & -1
\end{pmatrix}.
$$
Ta có
$$ \tau=-3,\qquad \Delta=6. $$
Vì
$$ \tau^2-4\Delta=9-24<0, $$
trị riêng là phức với phần thực âm. Do đó cân bằng là tiêu điểm hút và ổn định tiệm cận.

## Câu hỏi khái niệm

1. Vì sao ổn định tiệm cận mạnh hơn ổn định Lyapunov?
2. Vì sao yên ngựa luôn không ổn định dù vẫn có một hướng hút?
3. Tâm và tiêu điểm hút khác nhau ở điểm cốt lõi nào về lâu dài?

## Bài toán ứng dụng

1. Trong một hệ điều khiển, vì sao "quay về trạng thái mong muốn" quan trọng hơn chỉ "không đi quá xa"?
2. Một mô hình sinh học có cân bằng kiểu tâm. Hãy giải thích vì sao nhiễu nhỏ không làm hệ nổ ra nhưng cũng không làm nó trở lại đúng điểm ban đầu.
3. Một hệ cơ học có Jacobian với một trị riêng dương rất nhỏ. Hãy thảo luận vì sao hệ vẫn không ổn định dù thoạt nhìn có vẻ "gần ổn định".

## Chiến lược giảng dạy tương tác

- Cho sinh viên mô tả bằng lời trước ba khái niệm: ổn định, tiệm cận, không ổn định.
- Làm bảng ghép cặp giữa loại trị riêng và loại cân bằng.
- Hỏi lớp: "Nếu chỉ lệch rất nhỏ mà vẫn không quay về, ta nên gọi hệ là gì?"
- Dùng ví dụ viên bi trong bát và trên đỉnh đồi để nhắc lại trực giác vật lý.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu học theo một sơ đồ quyết định rõ: trước hết nhìn dấu phần thực của trị riêng, sau đó mới phân biệt chi tiết hình học. Cách này giúp tránh lẫn lộn giữa nhiều tên gọi.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tìm ví dụ một hệ phi tuyến mà tuyến tính hóa cho tâm nhưng hệ thật không ổn định tiệm cận, để thấy giới hạn của kết luận phổ tuyến tính.

## Tóm tắt dễ nhớ

Ổn định là câu chuyện về phản ứng với nhiễu nhỏ. Ổn định tiệm cận nghĩa là ở gần và còn quay về. Yên ngựa luôn không ổn định, phần thực âm cho hút, phần thực dương cho đẩy, và phần thực bằng 0 là vùng phải cẩn thận.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ổn định của trạng thái bay
- Bài toán: Sau nhiễu nhỏ, máy bay có trở về cấu hình bay cân bằng hay lệch xa dần.
- Mô hình địa phương:
$$ \dot{\mathbf{u}}=J\mathbf{u}. $$
- Giả thiết và giới hạn: Chỉ là phân tích gần trạng thái trim, chưa phản ánh phi tuyến mạnh hay bão hòa điều khiển.
- Diễn giải: Node, saddle hay spiral tương ứng với các kiểu hồi phục hoặc mất ổn định khác nhau.

#### Vận hành lò phản ứng hóa học
- Bài toán: Một điểm vận hành có bền trước nhiễu nhiệt độ và nồng độ không.
- Mô hình:
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
phân loại qua Jacobian tại cân bằng.
- Giả thiết và giới hạn: Đúng gần điểm vận hành.
- Diễn giải: Saddle là cảnh báo mạnh vì có hướng nhiễu nhỏ sẽ bùng ra nhanh.

### 2. Trực giác bổ sung và các kết nối

Phân loại ổn định là ngôn ngữ hình học của phổ Jacobian. Phần thực âm kéo quỹ đạo vào, phần thực dương đẩy ra, còn phần ảo tạo quay. Một bẫy phổ biến là nghĩ "center" trong tuyến tính hóa luôn đồng nghĩa ổn định trong phi tuyến; điều đó không luôn đúng. Bài này kết nối chặt với Chapter 4 nhưng nay áp dụng cho Jacobian của hệ phi tuyến.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

cases = {
    "stable node": np.array([[-2, 0], [0, -1]]),
    "saddle": np.array([[1, 0], [0, -2]]),
    "spiral sink": np.array([[0, -1], [1, -1]])
}

x = np.linspace(-2, 2, 16)
y = np.linspace(-2, 2, 16)
X, Y = np.meshgrid(x, y)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, (name, A) in zip(axes, cases.items()):
    U = A[0, 0] * X + A[0, 1] * Y
    V = A[1, 0] * X + A[1, 1] * Y
    N = np.sqrt(U**2 + V**2) + 1e-9
    ax.quiver(X, Y, U / N, V / N)
    ax.set_title(name)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: stability classification phase portrait node saddle spiral
- search: trace determinant plane visualization
- search: nonlinear equilibrium classification Jacobian

### 5. Bài toán mẫu có bối cảnh thực

Với
$$
J=
\begin{pmatrix}
0 & 1\\
-2 & -3
\end{pmatrix},
$$
phương trình đặc trưng là
$$ \lambda^2+3\lambda+2=0 $$
nên có trị riêng $$ -1 $$ và $$ -2 $$. Vì cả hai đều âm, cân bằng là stable node. Trong ngữ cảnh kỹ thuật, nhiễu nhỏ sẽ tắt dần mà không tạo dao động kéo dài.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phân loại bằng trị riêng, vết và định thức.

**Bậc sau đại học.** Liên hệ với stable manifold, unstable manifold và sự bền vững cấu trúc của điểm hyperbolic.

## Tài liệu tham khảo

- Strogatz, Chương 5-6: rất tốt cho trực giác phân loại ổn định.
- Arnold, Chương 5: làm rõ ngôn ngữ ổn định trong động lực học.
