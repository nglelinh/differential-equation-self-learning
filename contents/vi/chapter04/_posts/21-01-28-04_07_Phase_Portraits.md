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

## Mục tiêu

Bài học này giúp sinh viên đọc và phác họa chân dung pha của hệ tuyến tính phẳng, phân loại điểm cân bằng bằng trị riêng hoặc bằng vết-định thức, và hiểu vì sao hình học pha cho ta thông tin định tính rất mạnh ngay cả khi không viết nghiệm tường minh.

## Kiến thức nền

Sinh viên cần nắm trị riêng thực, trị riêng phức và các dạng nghiệm cơ bản của hệ tuyến tính 2 chiều. Trực giác về hướng trường vector và đường quỹ đạo từ chương phương trình tự trị sẽ là một nền rất tốt.

## Dẫn nhập

![Chân dung pha của hệ tuyến tính hai chiều]({{ site.imgurl }}/chapter_img/chapter04/07_phase_portraits.svg)

Một công thức nghiệm có thể rất chính xác, nhưng không phải lúc nào cũng nói cho ta bức tranh tổng thể dễ nhìn. Chân dung pha làm điều ngược lại: nó bỏ qua những chi tiết đại số để phóng to hình học của hệ. Ta nhìn thấy ngay quỹ đạo đi về đâu, trôi khỏi đâu, có xoắn hay không, có hướng bất biến nào nổi bật hay không.

Đây là bài học mà phương pháp định tính thật sự lên ngôi. Chỉ từ ma trận
$$ A, $$
ta có thể dự đoán gốc là yên ngựa, nút hút, nút đẩy, tâm hay tiêu điểm. Điều này rất quan trọng vì trong nhiều mô hình lớn hơn, chính trực giác pha mới là thứ giúp ta hiểu hệ trước khi đi sâu vào tính toán.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Chân dung pha giống như bản đồ gió của hệ. Tại mỗi điểm trong không gian trạng thái, ta biết trạng thái sẽ bị kéo theo hướng nào. Quỹ đạo là đường mà hệ thật sự đi khi thả từ một trạng thái ban đầu.

### Cách nhìn hình ảnh

Trong hệ hai chiều
$$ \mathbf{x}'=A\mathbf{x}, $$
gốc là điểm cân bằng. Nếu quỹ đạo chạy tới gốc từ mọi phía, ta có điểm hút. Nếu chúng rời gốc, ta có điểm đẩy. Nếu có một hướng vào và một hướng ra, ta có yên ngựa. Nếu quỹ đạo quay quanh gốc, ta nghĩ tới trị riêng phức.

### Cách nhìn hình thức

Với ma trận
$$
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
$$
ta đặt
$$
\tau=\operatorname{tr}(A)=a+d,
\qquad
\Delta=\det(A)=ad-bc.
$$
Đa thức đặc trưng là
$$ \lambda^2-\tau\lambda+\Delta=0. $$
Từ dấu của $$ \Delta $$ và của
$$ \tau^2-4\Delta $$
ta phân loại được kiểu điểm cân bằng.

## Những ngộ nhận thường gặp

- "Muốn vẽ chân dung pha phải giải nghiệm tường minh." Sai. Nhiều kết luận đi trực tiếp từ trị riêng.
- "Nếu quỹ đạo cong thì chắc chắn hệ phi tuyến." Sai. Hệ tuyến tính cũng cho quỹ đạo cong, xoắn hoặc hyperbol.
- "Tâm và tiêu điểm đều chỉ là quỹ đạo quay nên giống nhau." Sai. Tâm có biên độ không đổi, tiêu điểm thì hút hoặc đẩy.
- "Chỉ dấu của định thức là đủ để phân loại hoàn toàn." Không đúng. Cần thêm thông tin từ vết và biệt thức.

## Tiến trình học tập đề xuất

### Bước 1: Tìm trị riêng hoặc tính $$ \tau,\Delta $$

Đây là cổng vào nhanh nhất.

### Bước 2: Phân loại kiểu cân bằng

Yên ngựa, nút, tâm, tiêu điểm.

### Bước 3: Dùng vector riêng hoặc hướng quay để hoàn thiện hình

Đây là phần làm chân dung pha sống động.

### Bước 4: Kiểm tra độ hợp lý bằng vài vector trường

Không nên chỉ tin vào tên phân loại.

### Các checkpoint

- Sinh viên có phân biệt được nút, yên ngựa, tâm và tiêu điểm hay không.
- Sinh viên có dùng đúng $$ \tau,\Delta $$ hay không.
- Sinh viên có nhìn được hướng bất biến trong chân dung pha hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Yên ngựa

Xét
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$
Ta có
$$ \Delta=-2<0. $$
Do đó gốc là yên ngựa. Trục thứ nhất là hướng đẩy, trục thứ hai là hướng hút.

### Ví dụ 2: Nút hút

Xét
$$
A=
\begin{pmatrix}
-2 & 0\\
0 & -3
\end{pmatrix}.
$$
Hai trị riêng đều âm, nên gốc là nút ổn định. Mọi quỹ đạo không tầm thường tiến về gốc, thường bám theo hướng có tốc độ suy giảm chậm hơn khi $$ t $$ lớn.

### Ví dụ 3: Tiêu điểm hút

Xét
$$
A=
\begin{pmatrix}
-1 & -2\\
2 & -1
\end{pmatrix}.
$$
Ta có
$$ \tau=-2,\qquad \Delta=5. $$
Vì
$$ \tau^2-4\Delta=4-20<0, $$
trị riêng là phức, và vì $$ \tau<0 $$ nên phần thực âm. Do đó gốc là tiêu điểm ổn định: quỹ đạo xoắn vào.

### Ví dụ 4: Tâm

Với
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix},
$$
ta có
$$ \tau=0,\qquad \Delta=1,\qquad \tau^2-4\Delta<0. $$
Trị riêng là $$ \pm i $$, nên gốc là tâm. Quỹ đạo quay quanh gốc với biên độ không đổi.

## Câu hỏi khái niệm

1. Vì sao chân dung pha cho ta cái nhìn tổng quát nhanh hơn công thức nghiệm?
2. Vai trò của vết và định thức trong việc phân loại là gì?
3. Vì sao hai hệ đều có trị riêng phức nhưng một hệ là tâm còn hệ kia là tiêu điểm?

## Bài toán ứng dụng

1. Một mô hình cơ học tuyến tính hóa quanh cân bằng cho quỹ đạo yên ngựa. Hãy giải thích vì sao cân bằng đó rất khó duy trì.
2. Một hệ sinh học tuyến tính hóa quanh cân bằng cho tiêu điểm hút. Điều đó nói gì về dao động quanh mức cân bằng?
3. Một hệ điều khiển cần tránh cực dương để không bị nút đẩy hoặc tiêu điểm đẩy. Hãy diễn giải điều này bằng ngôn ngữ chân dung pha.

## Chiến lược giảng dạy tương tác

- Cho sinh viên đoán loại điểm cân bằng từ trị riêng trước khi vẽ.
- Dùng bảng phân loại nhỏ dựa trên $$ \Delta $$ và $$ \tau $$ để lớp luyện phản xạ.
- Cho các nhóm vẽ sơ bộ cùng một chân dung pha bằng hai cách: dùng trị riêng và dùng vết-định thức.
- Yêu cầu sinh viên kiểm tra bằng vài vector trường tại các điểm mẫu để tránh vẽ "theo tên gọi".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu bám vào bảng hai bước: trước hết nhìn dấu của $$ \Delta $$, sau đó nếu $$ \Delta>0 $$ thì xét tiếp biệt thức và dấu của $$ \tau $$. Việc có một sơ đồ quyết định rõ ràng giúp giảm nhầm lẫn rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi giải thích tại sao mode suy giảm chậm nhất chi phối hình dạng quỹ đạo gần gốc, hoặc nối chân dung pha với nghiệm explicit trong vài ví dụ đặc biệt.

## Tóm tắt dễ nhớ

Chân dung pha là bản đồ hình học của hệ tuyến tính. Với hệ 2 chiều, chỉ cần trị riêng hoặc cặp
$$ (\tau,\Delta) $$
là ta đọc được kiểu cân bằng. Đây là nơi đại số, hình học và trực giác động lực học gặp nhau rõ nhất.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tuyến tính hóa quanh cân bằng
- Bài toán: Gần điểm cân bằng, ta chỉ cần biết hệ là yên ngựa, nút, tâm hay tiêu điểm để đoán hành vi.
- Mô hình:
$$ \mathbf{x}'=A\mathbf{x}. $$
- Giả thiết và giới hạn: Chỉ đúng cục bộ nếu đến từ tuyến tính hóa hệ phi tuyến.
- Diễn giải: Chân dung pha cho thông tin định tính rất mạnh mà không cần nghiệm tường minh.

#### Điều khiển và ổn định
- Bài toán: Kỹ sư muốn biết hệ có bị đẩy ra khỏi gốc hay bị hút về gốc.
- Mô hình:
$$ \tau=\operatorname{tr}(A),\qquad \Delta=\det(A). $$
- Giả thiết và giới hạn: Hệ tuyến tính phẳng.
- Diễn giải: Chỉ từ dấu của $$ \Delta $$ và quan hệ giữa $$ \tau^2 $$ với $$ 4\Delta $$ đã phân loại được kiểu cân bằng.

#### Hóa học và sinh học
- Bài toán: Hai biến có thể tiến về cân bằng bằng cách xoắn, trượt hoặc lao thẳng.
- Mô hình: Chân dung pha của hệ 2 chiều.
- Giả thiết và giới hạn: Gần cân bằng, mô hình tuyến tính cục bộ.
- Diễn giải: Đây là ngôn ngữ hình học để đọc ổn định.

### 2. Trực giác bổ sung và các kết nối

Chân dung pha là nơi hình học thực sự lên ngôi. Nó tổng hợp mọi thứ từ trị riêng, vector riêng và trường vector thành một bức tranh duy nhất. Bài này cũng chuẩn bị cho chương phi tuyến, nơi ta không phải lúc nào cũng có công thức nghiệm nhưng vẫn cần hiểu quỹ đạo.

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

Xét
$$
A=
\begin{pmatrix}
2 & 0\\
0 & -1
\end{pmatrix}.
$$
Ta có
$$ \Delta=-2<0. $$
Vì định thức âm nên gốc là một yên ngựa. Trục thứ nhất là hướng đẩy, trục thứ hai là hướng hút. Không cần giải đầy đủ, ta đã biết đây là cân bằng rất không ổn định: chỉ một sai lệch nhỏ theo hướng đẩy sẽ làm hệ rời xa nhanh chóng.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân loại đúng các kiểu điểm cân bằng bằng trị riêng hoặc vết - định thức.

**Bậc sau đại học.** Nối với tuyến tính hóa hệ phi tuyến và ý nghĩa cục bộ của chân dung pha.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: rất tốt cho phân loại hệ phẳng.
- Strogatz, *Nonlinear Dynamics and Chaos*: trực giác xuất sắc về chân dung pha và điểm cân bằng.
