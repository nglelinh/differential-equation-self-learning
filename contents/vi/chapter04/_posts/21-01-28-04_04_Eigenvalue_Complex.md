---
layout: post
title: "04-04 Phương pháp Trị riêng: Phức"
chapter: '04'
order: 4
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên xử lý hệ tuyến tính khi ma trận có cặp trị riêng phức liên hợp, chuyển nghiệm phức thành nghiệm thực, và đọc được hiện tượng quay, xoắn ốc hút vào hay xoắn ốc đẩy ra từ phần thực và phần ảo của trị riêng.

## Kiến thức nền

Sinh viên cần nắm số phức cơ bản, công thức Euler và trường hợp trị riêng thực phân biệt. Đây là nơi trực giác hình học trở nên đặc biệt mạnh, nên việc liên hệ với dao động điều hòa từ chương trước rất hữu ích.

## Dẫn nhập

![Quỹ đạo xoắn khi trị riêng là phức liên hợp]({{ site.imgurl }}/chapter_img/chapter04/04_eigenvalue_complex.svg)

Trong hệ một ẩn, nghiệm phức thường báo hiệu dao động. Điều đó tiếp tục đúng với hệ tuyến tính, nhưng bây giờ ý nghĩa hình học còn rõ hơn. Khi trị riêng là phức, quỹ đạo không chỉ tăng hoặc giảm trên một đường thẳng, mà quay quanh gốc. Nếu đồng thời có co lại hay giãn ra, quỹ đạo sẽ thành xoắn ốc.

Đây là bài học rất giàu trực giác. Chỉ từ cặp số
$$ \alpha\pm i\beta, $$
ta có thể đọc ngay ba thông tin: có quay hay không, quay nhanh hay chậm, và biên độ co hay giãn. Không nhiều nơi trong toán học mà đại số và hình học nói chuyện trực tiếp với nhau rõ đến như vậy.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Có thể hình dung hệ như một chuyển động quay trong mặt phẳng. Phần ảo của trị riêng tạo ra nhịp quay, còn phần thực giống như việc mỗi vòng quay đồng thời bị co lại hoặc bị kéo phình ra.

### Cách nhìn hình ảnh

Nếu
$$ \alpha<0, $$
quỹ đạo xoắn vào gốc. Nếu
$$ \alpha>0, $$
quỹ đạo xoắn ra. Nếu
$$ \alpha=0, $$
quỹ đạo chỉ quay quanh gốc mà không co giãn, tạo nên tâm lý tưởng trong mô hình tuyến tính. Phần ảo $$ \beta $$ quyết định tốc độ góc.

### Cách nhìn hình thức

Giả sử $$ A $$ có trị riêng
$$ \lambda=\alpha\pm i\beta,\qquad \beta\neq 0, $$
và vector riêng phức
$$ \mathbf{v}=\mathbf{a}+i\mathbf{b}. $$
Một nghiệm phức là
$$
\mathbf{x}(t)=e^{(\alpha+i\beta)t}(\mathbf{a}+i\mathbf{b}).
$$
Dùng công thức Euler, ta tách được hai nghiệm thực độc lập:
$$
\mathbf{x}_1(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t-\mathbf{b}\sin \beta t\right),
$$
$$
\mathbf{x}_2(t)=e^{\alpha t}\left(\mathbf{a}\sin \beta t+\mathbf{b}\cos \beta t\right).
$$

## Những ngộ nhận thường gặp

- "Trị riêng phức khiến nghiệm không còn ý nghĩa thực." Sai. Ta luôn tách được hai nghiệm thực độc lập.
- "Chỉ cần có phần ảo là quỹ đạo luôn là đường tròn." Sai. Còn phụ thuộc phần thực có bằng 0 hay không.
- "Nếu quỹ đạo quay thì hệ chắc chắn ổn định." Không đúng. Có thể quay và đồng thời đi ra xa.
- "Phần thực và phần ảo của trị riêng có vai trò như nhau." Sai. Chúng mã hóa hai loại hành vi hoàn toàn khác.

## Tiến trình học tập đề xuất

### Bước 1: Tìm trị riêng phức

Nhận ra trường hợp biệt thức âm.

### Bước 2: Tìm vector riêng phức

Làm chậm và cẩn thận với số phức.

### Bước 3: Tách phần thực và phần ảo

Đây là bước chuyển về thế giới nghiệm thực.

### Bước 4: Diễn giải hình học

Hỏi ngay quỹ đạo quay, hút hay đẩy.

### Các checkpoint

- Sinh viên có tách đúng nghiệm phức sang hai nghiệm thực hay không.
- Sinh viên có giải thích được vai trò của $$ \alpha $$ và $$ \beta $$ hay không.
- Sinh viên có phân biệt được tâm, xoắn ốc hút và xoắn ốc đẩy hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Chuyển động quay thuần

Xét
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix}.
$$
Ta có trị riêng
$$ \lambda=\pm i. $$
Nghiệm thực là tổ hợp của sin-cos. Các quỹ đạo là đường tròn quanh gốc. Đây là mô hình hệ bậc nhất của dao động điều hòa không tắt.

### Ví dụ 2: Xoắn ốc hút vào

Xét
$$
A=
\begin{pmatrix}
-1 & -2\\
2 & -1
\end{pmatrix}.
$$
Trị riêng là
$$ -1\pm 2i. $$
Vì phần thực âm, quỹ đạo quay và đồng thời co về gốc. Do đó gốc là một tiêu điểm ổn định.

### Ví dụ 3: Xoắn ốc đẩy ra

Nếu thay ma trận trên bằng
$$
A=
\begin{pmatrix}
1 & -2\\
2 & 1
\end{pmatrix},
$$
thì trị riêng là
$$ 1\pm 2i. $$
Quỹ đạo vẫn quay với tốc độ góc 2 nhưng biên độ tăng theo $$ e^t $$. Đây là mô hình điển hình của xoắn ốc không ổn định.

### Ví dụ 4: Tách giải thích từ trị riêng

Từ trị riêng
$$ \lambda=-3\pm 4i, $$
ta có thể đọc ngay: hệ quay, tốc độ quay liên quan đến 4, và biên độ giảm như $$ e^{-3t} $$. Sinh viên nên tập phản xạ đọc trực tiếp ý nghĩa này mà không cần giải đầy đủ.

## Câu hỏi khái niệm

1. Vì sao trị riêng phức lại gắn với chuyển động quay trong mặt phẳng?
2. Phần thực và phần ảo của trị riêng đóng vai trò động học nào?
3. Vì sao cùng có phần ảo nhưng có hệ quay tròn, có hệ xoắn vào, có hệ xoắn ra?

## Bài toán ứng dụng

1. Một hệ điều khiển có đáp ứng dao động rồi tắt dần. Hãy liên hệ với trị riêng phức có phần thực âm.
2. Một mô hình quần thể hai biến cho quỹ đạo xoắn ra khỏi cân bằng. Điều này gợi ý gì về ổn định?
3. Một mạch điện dao động điều hòa lý tưởng không mất năng lượng. Hãy diễn giải vì sao phần thực của trị riêng phải bằng 0.

## Chiến lược giảng dạy tương tác

- Cho sinh viên đoán dạng quỹ đạo chỉ từ trị riêng trước khi vẽ hình.
- Tổ chức bài tập ghép cặp giữa các trị riêng và các chân dung pha tương ứng.
- Yêu cầu lớp diễn giải bằng lời cụm
$$ \alpha\pm i\beta $$
thành "quay, hút/đẩy, nhanh/chậm".
- So sánh trực tiếp với dao động điều hòa ở chương trước để tạo cầu nối.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu bám vào một bảng ngắn: $$ \alpha<0 $$ là hút, $$ \alpha>0 $$ là đẩy, $$ \beta\neq 0 $$ là quay. Sơ đồ hóa đơn giản này giúp các em không bị chìm trong số phức.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi viết nghiệm dưới dạng ma trận quay kết hợp co giãn, để thấy cấu trúc
$$ e^{\alpha t}R_{\beta t} $$
ẩn sau cặp trị riêng phức.

## Tóm tắt dễ nhớ

Trị riêng phức không làm hệ "mất thực", mà làm hệ bắt đầu quay. Phần ảo tạo dao động quay, phần thực tạo co hoặc giãn. Muốn đọc nhanh hệ 2 chiều, hãy nhìn
$$ \alpha\pm i\beta $$
như mã hóa của quay cộng co/giãn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mô hình quay và xoắn trong cơ học
- Bài toán: Một hệ phẳng vừa quay vừa co hoặc giãn.
- Mô hình:
$$ \lambda=\alpha\pm i\beta. $$
- Giả thiết và giới hạn: Hệ tuyến tính hai chiều.
- Diễn giải: Phần ảo sinh quay, phần thực sinh co hoặc giãn.

#### Điện tử và dao động tắt dần
- Bài toán: Một mạch điện hoặc bộ lọc có đáp ứng dao động tắt dần quanh cân bằng.
- Mô hình:
$$
\mathbf{x}(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t+\mathbf{b}\sin \beta t\right).
$$
- Giả thiết và giới hạn: Tính tuyến tính gần điểm làm việc.
- Diễn giải: Trị riêng phức là ngôn ngữ tự nhiên của dao động có quay trong không gian trạng thái.

#### Mô hình dòng chảy quay trong sinh học hoặc hóa học
- Bài toán: Hai biến có thể quay quanh cân bằng thay vì tiến thẳng vào hoặc ra.
- Mô hình:
$$
\alpha<0 \Rightarrow \text{spiral sink},\qquad
\alpha>0 \Rightarrow \text{spiral source}.
$$
- Giả thiết và giới hạn: Chỉ là phân loại tuyến tính cục bộ.
- Diễn giải: Chỉ từ trị riêng đã đọc được kiểu quỹ đạo.

### 2. Trực giác bổ sung và các kết nối

Nếu trị riêng thực nói về giãn co dọc các hướng riêng, thì trị riêng phức nói về giãn co kết hợp quay. Bài này nối rất chặt với chương dao động điều hòa: nghiệm phức không phải đối tượng "ảo" mà là cách mã hóa tự nhiên của dao động và xoắn ốc.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12, 800)
for alpha, label in [(-0.15, "Spiral sink"), (0.0, "Center"), (0.12, "Spiral source")]:
    x = np.exp(alpha * t) * np.cos(2 * t)
    y = np.exp(alpha * t) * np.sin(2 * t)
    plt.plot(x, y, label=label)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Ảnh hưởng của phần thực lên quỹ đạo quay")
plt.legend()
plt.axis("equal")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: spiral sink spiral source phase portrait
- search: complex eigenvalues linear system visualization
- search: center vs spiral phase portrait animation

### 5. Bài toán mẫu có bối cảnh thực

Cho
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix}.
$$
Các trị riêng là
$$ \lambda=\pm i. $$
Nghiệm có dạng quay thuần:
$$
\mathbf{x}(t)=
c_1
\begin{pmatrix}
\cos t\\
\sin t
\end{pmatrix}
+
c_2
\begin{pmatrix}
-\sin t\\
\cos t
\end{pmatrix}.
$$
Quỹ đạo là các đường tròn quanh gốc. Đây là ví dụ nền tảng để thấy trị riêng phức tạo ra quay chứ không phải chỉ "tính toán phức".

### 6. Phân tầng độ khó

**Bậc đại học.** Học tách nghiệm phức thành hai nghiệm thực và đọc vai trò của $$ \alpha,\beta $$.

**Bậc sau đại học.** Nối với dạng chuẩn quay - co giãn và các tiêu điểm trong phân loại điểm cân bằng.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày rất rõ cách chuyển nghiệm phức sang nghiệm thực.
- Arnold, *Ordinary Differential Equations*: đặc biệt mạnh về trực giác hình học của quỹ đạo quay.
