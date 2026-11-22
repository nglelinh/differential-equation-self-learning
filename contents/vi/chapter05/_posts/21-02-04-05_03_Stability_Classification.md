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

Bài học này giúp sinh viên phân biệt các khái niệm ổn định Lyapunov, ổn định tiệm cận và không ổn định, sử dụng trị riêng hoặc cặp vết–định thức (trace–determinant) để phân loại điểm cân bằng của hệ phẳng, đồng thời hiểu rằng tính ổn định phản ánh phản ứng của hệ trước nhiễu nhỏ chứ không chỉ là tên gọi hình học.

## Kiến thức nền

Sinh viên cần nắm vững phép tuyến tính hóa và trị riêng của ma trận Jacobian. Việc quen thuộc với chân dung pha từ chương trước cũng giúp liên kết chặt chẽ giữa đại số và hình học.

## Dẫn nhập

![Phân loại ổn định từ phổ của Jacobian]({{ site.imgurl }}/chapter_img/chapter05/03_stability_classification.svg)

Trong ngôn ngữ đời thường, từ "ổn định" thường được dùng khá mơ hồ. Tuy nhiên, trong động lực học, khái niệm này cần được định nghĩa chặt chẽ. Khi tác động một nhiễu nhỏ làm hệ lệch khỏi vị trí cân bằng, hệ sẽ duy trì gần vị trí đó, quay trở về đúng vị trí đó, hay rời xa dần? Ba tình huống này tuy gần nhau về trực giác nhưng tương ứng với ba khái niệm toán học khác biệt.

Bài học này giúp sinh viên chuyển từ cách hiểu cảm tính sang phân tích chính xác tính ổn định thông qua phổ trị riêng của ma trận Jacobian và hình dạng chân dung pha.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hình ảnh một viên bi nằm dưới đáy bát và một viên bi đặt trên đỉnh đồi minh họa rõ các kiểu ổn định. Ở đáy bát, nếu bị đẩy lệch nhẹ, viên bi vẫn ở gần đáy và thường quay lại vị trí ban đầu. Trên đỉnh đồi, chỉ một xê dịch rất nhỏ cũng khiến viên bi lăn ra xa.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, quanh một điểm cân bằng ổn định tiệm cận, các quỹ đạo lân cận đều tiến về điểm đó. Với điểm cân bằng ổn định nhưng không tiệm cận (như tâm tuyến tính), quỹ đạo giữ nguyên khoảng cách lân cận mà không tiến sát vào điểm cân bằng. Ngược lại, quanh điểm cân bằng không ổn định, tồn tại các nhiễu nhỏ khiến quỹ đạo rời xa dần.

### Cách nhìn hình thức

Một điểm cân bằng là **ổn định theo Lyapunov** nếu mọi quỹ đạo xuất phát đủ gần điểm cân bằng đều luôn ở gần điểm đó theo thời gian. Điểm cân bằng là **ổn định tiệm cận** nếu ngoài tính ổn định Lyapunov, các quỹ đạo đủ gần còn hội tụ về điểm cân bằng khi $$ t\to\infty $$. Nó là **không ổn định** nếu tồn tại các nhiễu tùy ý nhỏ khiến quỹ đạo thoát ra khỏi lân cận đã chọn.

Với ma trận Jacobian $$ J $$ của hệ hai chiều, đặt
$$ \tau=\operatorname{tr}(J),\qquad \Delta=\det(J). $$
Khi $$ \Delta<0 $$, điểm cân bằng là điểm yên ngựa nên không ổn định. Khi $$ \Delta>0 $$, ta xét tiếp dấu của $$ \tau $$ và biệt thức
$$ \tau^2-4\Delta $$
để xác định dạng nút, tiêu điểm xoắn hay tâm.

## Những ngộ nhận thường gặp

- "Ổn định và ổn định tiệm cận là giống nhau." Sai. Có những hệ giữ quỹ đạo ở gần điểm cân bằng nhưng không kéo chúng quay về đó.
- "Nếu quỹ đạo quay quanh điểm cân bằng thì điểm cân bằng không ổn định." Không đúng; tâm tuyến tính có quỹ đạo quay quanh nhưng vẫn ổn định theo Lyapunov.
- "Yên ngựa chỉ là tên gọi hình học, không liên quan đến tính ổn định." Sai. Điểm yên ngựa luôn là điểm cân bằng không ổn định.
- "Chỉ cần quan sát hình vẽ là đủ, không cần định nghĩa hình thức." Không nên. Định nghĩa chính xác giúp tránh nhầm lẫn giữa việc quỹ đạo "ở gần" và việc quỹ đạo "hội tụ về".

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt các khái niệm ổn định

Diễn đạt rành mạch sự khác nhau giữa ổn định Lyapunov, ổn định tiệm cận và không ổn định trước khi tính toán.

### Bước 2: Dùng Jacobian hoặc cặp vết–định thức

Xác định phổ trị riêng của ma trận Jacobian tại điểm cân bằng.

### Bước 3: Liên kết phổ trị riêng với chân dung pha

Kết hợp kết quả đại số với hình dạng quỹ đạo trên mặt phẳng pha.

### Bước 4: Diễn giải ý nghĩa động học

Xác định rõ quỹ đạo sẽ duy trì gần cân bằng, hội tụ về cân bằng hay phân kỳ ra xa.

### Các điểm kiểm tra

- Sinh viên có phân biệt được ổn định Lyapunov và ổn định tiệm cận hay không.
- Sinh viên có áp dụng đúng tiêu chuẩn $$ \tau,\Delta $$ để phân loại điểm cân bằng hay không.
- Sinh viên có gắn đúng từng dạng phổ trị riêng với chân dung pha tương ứng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Yên ngựa không ổn định

Nếu ma trận Jacobian có hai trị riêng thực trái dấu
$$ \lambda_1>0,\qquad \lambda_2<0, $$
thì tồn tại một phương đẩy ra và một phương hút vào. Chỉ riêng sự tồn tại của phương đẩy đã đủ để kết luận điểm cân bằng không ổn định. Vì vậy, mọi điểm yên ngựa đều không ổn định.

### Ví dụ 2: Nút hút

Nếu
$$ \lambda_1<0,\qquad \lambda_2<0, $$
thì cả hai chế độ riêng đều tắt dần theo thời gian. Điểm cân bằng là ổn định tiệm cận: các quỹ đạo lân cận có thể không đi theo đường thẳng vào gốc, nhưng cuối cùng đều hội tụ về điểm cân bằng.

### Ví dụ 3: Tâm

Nếu ma trận Jacobian có cặp trị riêng thuần ảo
$$ \pm i\beta, $$
hệ tuyến tính hóa cho chân dung pha dạng tâm, với các quỹ đạo khép kín quay quanh điểm cân bằng có biên độ không đổi. Đây là ví dụ điển hình của điểm cân bằng ổn định Lyapunov nhưng không ổn định tiệm cận trong hệ tuyến tính.

### Ví dụ 4: Phân loại bằng vết và định thức

Cho ma trận
$$
J=
\begin{pmatrix}
-2 & 1\\
-4 & -1
\end{pmatrix}.
$$
Ta tính được
$$ \tau=-3,\qquad \Delta=6. $$
Vì
$$ \tau^2-4\Delta=9-24<0, $$
ma trận có cặp trị riêng phức liên hợp với phần thực âm. Do đó điểm cân bằng là tiêu điểm hút và ổn định tiệm cận.

## Câu hỏi khái niệm

1. Vì sao ổn định tiệm cận là điều kiện chặt hơn ổn định Lyapunov?
2. Vì sao điểm yên ngựa luôn không ổn định mặc dù vẫn có một hướng hút?
3. Điểm khác biệt cốt lõi về hành vi dài hạn giữa tâm và tiêu điểm hút là gì?

## Bài toán ứng dụng

1. Trong một hệ điều khiển, vì sao yêu cầu "quay về trạng thái mong muốn" thường quan trọng hơn việc chỉ "không đi quá xa"?
2. Một mô hình sinh học có điểm cân bằng dạng tâm. Hãy giải thích vì sao nhiễu nhỏ không làm hệ phân kỳ nhưng cũng không đưa hệ trở lại đúng trạng thái ban đầu.
3. Một hệ cơ học có ma trận Jacobian chứa một trị riêng dương rất nhỏ. Hãy thảo luận vì sao hệ vẫn không ổn định dù thoạt nhìn có vẻ gần như ổn định.

## Chiến lược giảng dạy tương tác

- Yêu cầu sinh viên diễn đạt bằng lời ba khái niệm: ổn định, ổn định tiệm cận và không ổn định.
- Lập bảng đối chiếu giữa dạng trị riêng và kiểu điểm cân bằng.
- Đặt câu hỏi thảo luận: nếu hệ chỉ lệch rất nhỏ nhưng không quay về vị trí cân bằng, ta xếp nó vào loại ổn định nào?
- Sử dụng hình ảnh viên bi ở đáy bát và trên đỉnh đồi để củng cố trực giác vật lý.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên hướng dẫn sinh viên áp dụng sơ đồ phân loại theo thứ tự rõ ràng: trước hết xét dấu phần thực của các trị riêng, sau đó mới phân biệt các dạng hình học chi tiết để tránh nhầm lẫn tên gọi.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm một hệ phi tuyến mà phép tuyến tính hóa cho dạng tâm nhưng hệ gốc lại không ổn định tiệm cận, nhằm minh họa giới hạn của phân tích phổ tuyến tính.

## Tóm tắt dễ nhớ

Ổn định mô tả phản ứng của hệ trước nhiễu nhỏ: ổn định Lyapunov giữ quỹ đạo ở gần, còn ổn định tiệm cận kéo quỹ đạo quay về điểm cân bằng. Điểm yên ngựa luôn không ổn định; phần thực âm tạo tính hút, phần thực dương tạo tính đẩy, và trường hợp phần thực bằng 0 cần được kiểm tra cẩn trọng bằng phương pháp phi tuyến.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ổn định trạng thái bay
- Bài toán: Xác định xem sau một nhiễu nhỏ, máy bay sẽ quay lại cấu hình bay cân bằng hay lệch xa dần.
- Mô hình cục bộ:
$$ \dot{\mathbf{u}}=J\mathbf{u}. $$
- Giả thiết và giới hạn: Chỉ áp dụng gần trạng thái bay cân bằng (trim), chưa xét các hiệu ứng phi tuyến mạnh hay bão hòa điều khiển.
- Diễn giải: Các dạng nút (node), yên ngựa (saddle) hay tiêu điểm xoắn (spiral) tương ứng với những kiểu hồi phục hoặc mất ổn định khác nhau.

#### Vận hành lò phản ứng hóa học
- Bài toán: Đánh giá xem một điểm vận hành có bền vững trước nhiễu nhiệt độ và nồng độ hay không.
- Mô hình:
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
được phân loại thông qua ma trận Jacobian tại điểm cân bằng.
- Giả thiết và giới hạn: Chỉ có hiệu lực trong lân cận điểm vận hành.
- Diễn giải: Điểm yên ngựa là dấu hiệu cảnh báo vì tồn tại phương mà nhiễu nhỏ sẽ khuếch đại nhanh chóng.

### 2. Trực giác bổ sung và các kết nối

Phân loại ổn định là cách diễn đạt hình học của phổ ma trận Jacobian: phần thực âm kéo quỹ đạo về điểm cân bằng, phần thực dương đẩy quỹ đạo ra xa và phần ảo tạo chuyển động quay. Một sai lầm thường gặp là cho rằng dạng tâm (center) của hệ tuyến tính hóa luôn bảo đảm ổn định cho hệ phi tuyến gốc. Bài học này kế thừa trực tiếp Chương 4 nhưng áp dụng vào ma trận Jacobian của hệ phi tuyến.

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

Với ma trận
$$
J=
\begin{pmatrix}
0 & 1\\
-2 & -3
\end{pmatrix},
$$
phương trình đặc trưng là
$$ \lambda^2+3\lambda+2=0, $$
cho hai trị riêng $$ -1 $$ và $$ -2 $$. Do cả hai đều âm, điểm cân bằng là nút hút (stable node). Trong bối cảnh kỹ thuật, điều này cho thấy nhiễu nhỏ sẽ tắt dần mà không sinh ra dao động kéo dài.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo việc phân loại điểm cân bằng bằng trị riêng, vết và định thức.

**Bậc sau đại học.** Liên hệ với đa tạp ổn định (stable manifold), đa tạp không ổn định (unstable manifold) và tính bền vững cấu trúc của điểm cân bằng hyperbolic.

## Video tham khảo

- Xem trước: [Stability and Eigenvalues: What does it mean to be a "stable" eigenvalue?](https://www.youtube.com/watch?v=XXjoh8L1HkE) — Steve Brunton, tiếng Anh. Giải thích ý nghĩa của trị riêng ổn định đối với hành vi dài hạn của quỹ đạo.
- [Trace-Determinant Diagram | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=oEskbXrhkkk) — MIT OpenCourseWare, tiếng Anh. Phân loại nút, yên ngựa, tiêu điểm xoắn và tâm trên giản đồ vết–định thức.
- [MAE5790-5 Two dimensional linear systems](https://www.youtube.com/watch?v=QrHRaA93Nrg) — Cornell MAE, tiếng Anh. Bài giảng phân loại hệ tuyến tính phẳng của Strogatz.

## Tài liệu tham khảo

- Strogatz, Chương 5–6: trình bày trực quan về phân loại tính ổn định.
- Arnold, Chương 5: làm rõ ngôn ngữ và cấu trúc ổn định trong động lực học.
