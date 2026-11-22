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

Bài học này hướng dẫn cách giải hệ tuyến tính khi ma trận có cặp trị riêng phức liên hợp, chuyển nghiệm phức về hai nghiệm thực độc lập và đọc trực tiếp chuyển động quay, xoắn ốc hút hay xoắn ốc đẩy từ phần thực và phần ảo của trị riêng.

## Kiến thức nền

Sinh viên cần nắm kiến thức cơ bản về số phức, công thức Euler và phương pháp trị riêng cho trường hợp trị riêng thực phân biệt. Liên hệ với bài nghiệm phức của ODE cấp hai ở Chương 02 sẽ giúp nắm bài nhanh hơn.

## Dẫn nhập

![Quỹ đạo xoắn khi trị riêng là phức liên hợp]({{ site.imgurl }}/chapter_img/chapter04/04_eigenvalue_complex.svg)

Ở phương trình một ẩn, nghiệm đặc trưng phức dẫn đến dao động. Trong hệ tuyến tính, ý nghĩa hình học còn trực quan hơn: khi ma trận có cặp trị riêng phức liên hợp, quỹ đạo trên mặt phẳng pha quay quanh gốc tọa độ; nếu phần thực khác 0, quỹ đạo vừa quay vừa co lại hoặc giãn ra tạo thành đường xoắn ốc.

Chỉ từ cặp trị riêng $$ \alpha\pm i\beta $$, ta xác định được ngay ba đặc tính: hệ có quay quanh gốc, tần số góc tỉ lệ với $$ \beta $$, và biên độ co lại hay giãn ra tùy dấu của $$ \alpha $$.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hệ có thể hình dung như một chuyển động quay trong mặt phẳng: phần ảo tạo ra chuyển động quay, còn phần thực làm bán kính quay thu hẹp dần hoặc mở rộng dần theo thời gian.

### Cách nhìn hình ảnh

Nếu $$ \alpha<0 $$, quỹ đạo xoắn vào gốc (xoắn ốc hút); nếu $$ \alpha>0 $$, quỹ đạo xoắn ra xa gốc (xoắn ốc đẩy); nếu $$ \alpha=0 $$, quỹ đạo khép kín quanh gốc tạo thành điểm tâm (center) trong mô hình tuyến tính. Phần ảo $$ \beta $$ quyết định tốc độ quay góc.

### Cách nhìn hình thức

Giả sử $$ A $$ có cặp trị riêng phức liên hợp $$ \lambda=\alpha\pm i\beta $$ ($$ \beta\neq 0 $$) và vector riêng phức $$ \mathbf{v}=\mathbf{a}+i\mathbf{b} $$ ứng với $$ \alpha+i\beta $$. Một nghiệm phức của hệ là
$$
\mathbf{x}(t)=e^{(\alpha+i\beta)t}(\mathbf{a}+i\mathbf{b}).
$$
Áp dụng công thức Euler rồi tách phần thực và phần ảo, ta thu được hai nghiệm thực độc lập tuyến tính:
$$
\mathbf{x}_1(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t-\mathbf{b}\sin \beta t\right),
$$
$$
\mathbf{x}_2(t)=e^{\alpha t}\left(\mathbf{a}\sin \beta t+\mathbf{b}\cos \beta t\right).
$$

## Những ngộ nhận thường gặp

- "Trị riêng phức nghĩa là hệ không có nghiệm thực." Sai: phần thực và phần ảo của một nghiệm phức luôn cho hai nghiệm thực độc lập tuyến tính.
- "Có phần ảo thì quỹ đạo luôn là đường tròn." Sai: quỹ đạo chỉ khép kín khi $$ \alpha=0 $$ (và thường là elip hơn là đường tròn chuẩn).
- "Quỹ đạo quay nghĩa là hệ ổn định." Không đúng: nếu $$ \alpha>0 $$, quỹ đạo vừa quay vừa xoắn ra xa vô hạn.
- "Phần thực và phần ảo có vai trò giống nhau." Sai: phần thực quyết định co/giãn biên độ, còn phần ảo quyết định tần số quay.

## Tiến trình học tập đề xuất

### Bước 1: Tìm cặp trị riêng phức liên hợp

Xác định trường hợp biệt thức âm từ đa thức đặc trưng.

### Bước 2: Tìm một vector riêng phức

Chỉ cần tìm một vector riêng $$ \mathbf{v}=\mathbf{a}+i\mathbf{b} $$ ứng với $$ \lambda=\alpha+i\beta $$.

### Bước 3: Tách phần thực và phần ảo

Sử dụng công thức Euler để viết hai nghiệm thực độc lập tuyến tính.

### Bước 4: Đọc hình học quỹ đạo

Xác định ngay dạng tâm, xoắn ốc hút hay xoắn ốc đẩy từ dấu của $$ \alpha $$.

### Các checkpoint

- Sinh viên có tách chính xác nghiệm phức thành hai nghiệm thực hay không.
- Sinh viên có giải thích rõ vai trò của $$ \alpha $$ và $$ \beta $$ hay không.
- Sinh viên có phân biệt được điểm tâm, xoắn ốc hút và xoắn ốc đẩy hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Chuyển động quay thuần

Xét ma trận
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix},
$$
có cặp trị riêng $$ \lambda=\pm i $$. Nghiệm thực là tổ hợp của sin và cos, và các quỹ đạo là các đường tròn đồng tâm quanh gốc — biểu diễn hệ bậc nhất của dao động điều hòa không cản.

### Ví dụ 2: Xoắn ốc hút

Xét
$$
A=
\begin{pmatrix}
-1 & -2\\
2 & -1
\end{pmatrix},
$$
có trị riêng $$ \lambda=-1\pm 2i $$. Vì phần thực $$ \alpha=-1<0 $$, quỹ đạo vừa quay vừa co về gốc, tạo thành tiêu điểm (xoắn ốc) ổn định.

### Ví dụ 3: Xoắn ốc đẩy

Với ma trận
$$
A=
\begin{pmatrix}
1 & -2\\
2 & 1
\end{pmatrix},
$$
trị riêng là $$ \lambda=1\pm 2i $$. Quỹ đạo quay với tốc độ góc bằng 2 nhưng biên độ tăng theo $$ e^t $$, tạo thành xoắn ốc không ổn định.

### Ví dụ 4: Đọc nhanh đặc tính động học từ trị riêng

Từ cặp trị riêng $$ \lambda=-3\pm 4i $$, ta kết luận ngay: hệ quay quanh gốc với tần số góc 4 và biên độ suy giảm theo $$ e^{-3t} $$. Sinh viên nên rèn kỹ năng đọc nhanh này trước khi giải chi tiết.

## Câu hỏi khái niệm

1. Vì sao cặp trị riêng phức liên hợp gắn liền với chuyển động quay trên mặt phẳng pha?
2. Phần thực và phần ảo của trị riêng đóng vai trò động học nào?
3. Vì sao cùng có phần ảo khác 0 nhưng có hệ tạo quỹ đạo khép kín, có hệ xoắn vào và có hệ xoắn ra?

## Bài toán ứng dụng

1. Một hệ điều khiển có đáp ứng dao động tắt dần. Hãy liên hệ hiện tượng này với cặp trị riêng phức có phần thực âm.
2. Một mô hình hai quần thể có quỹ đạo xoắn ra xa điểm cân bằng. Điều đó cho biết gì về tính ổn định?
3. Một mạch LC lý tưởng không tiêu hao năng lượng dao động điều hòa mãi. Vì sao phần thực của trị riêng phải bằng 0?

## Chiến lược giảng dạy tương tác

- Cho sinh viên dự đoán dạng chân dung pha chỉ từ cặp trị riêng trước khi vẽ hình.
- Tổ chức bài tập ghép cặp giữa các giá trị $$ \alpha\pm i\beta $$ và các dạng chân dung pha tương ứng.
- Yêu cầu lớp diễn đạt nhanh cặp $$ \alpha\pm i\beta $$ thành mô tả định tính: quay, hút/đẩy, nhanh/chậm.
- Đối chiếu trực tiếp với bài nghiệm phức của Chương 02 để củng cố sự liên kết kiến thức.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Tóm gọn quy tắc bằng bảng ngắn: $$ \alpha<0 $$ là hút, $$ \alpha>0 $$ là đẩy, $$ \alpha=0 $$ là quay khép kín, còn $$ \beta\neq 0 $$ tạo chuyển động quay.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên biểu diễn nghiệm bằng phép quay kết hợp co giãn dạng $$ e^{\alpha t}R_{\beta t} $$ để thấy rõ bản chất hình học ẩn sau cặp trị riêng phức.

## Tóm tắt dễ nhớ

Trị riêng phức liên hợp $$ \alpha\pm i\beta $$ mã hóa chuyển động quay kết hợp co giãn: phần ảo $$ \beta $$ tạo nhịp quay, còn phần thực $$ \alpha $$ quyết định biên độ thu nhỏ ($$ \alpha<0 $$), giữ nguyên ($$ \alpha=0 $$) hay mở rộng ($$ \alpha>0 $$).

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chuyển động quay và xoắn trong cơ học
- Bài toán: Hệ hai chiều vừa quay quanh cân bằng vừa tiêu tán hoặc nhận năng lượng.
- Mô hình: $$ \lambda=\alpha\pm i\beta $$.
- Giả thiết và giới hạn: Hệ tuyến tính hai chiều.
- Diễn giải: Phần ảo tạo chuyển động quay, phần thực tạo sự co hoặc giãn bán kính.

#### Dao động tắt dần trong mạch điện tử
- Bài toán: Mạch điện hoặc bộ lọc có đáp ứng dao động tắt dần về cân bằng.
- Mô hình:
$$
\mathbf{x}(t)=e^{\alpha t}\left(\mathbf{a}\cos \beta t+\mathbf{b}\sin \beta t\right).
$$
- Giả thiết và giới hạn: Tuyến tính hóa quanh điểm làm việc.
- Diễn giải: Cặp trị riêng phức là biểu diễn chuẩn của dao động trong không gian trạng thái.

#### Dòng chảy xoắn trong sinh học và hóa học
- Bài toán: Hai đại lượng biến đổi lệch pha và quay quanh cân bằng thay vì tiến thẳng vào hoặc ra.
- Mô hình: $$ \alpha<0 \Rightarrow \text{spiral sink} $$, $$ \alpha>0 \Rightarrow \text{spiral source} $$.
- Giả thiết và giới hạn: Phân loại tuyến tính cục bộ quanh điểm cân bằng.
- Diễn giải: Chỉ cần xác định trị riêng là đọc được hình thái quỹ đạo lân cận cân bằng.

### 2. Trực giác bổ sung và các kết nối

Nếu trị riêng thực tương ứng với co giãn dọc các phương riêng, thì trị riêng phức tương ứng với co giãn kết hợp phép quay. Nội dung này nối thẳng với bài nghiệm phức của Chương 02: số phức là công cụ đại số gọn gàng để mô tả dao động và xoắn ốc.

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

Cho ma trận
$$
A=
\begin{pmatrix}
0 & -1\\
1 & 0
\end{pmatrix},
$$
có các trị riêng $$ \lambda=\pm i $$. Nghiệm tổng quát thực là
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
Các quỹ đạo là đường tròn quanh gốc, minh họa trực tiếp việc cặp trị riêng thuần ảo sinh ra chuyển động quay tuần hoàn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo tách nghiệm phức thành hai nghiệm thực độc lập và đọc vai trò của $$ \alpha,\beta $$.

**Bậc sau đại học.** Liên hệ với dạng chuẩn quay – co giãn và phân loại điểm cân bằng tiêu điểm/tâm.

## Video tham khảo

- Xem trước: [2x2 Systems of ODEs: Imaginary Eigenvalues and Center Fixed Points](https://www.youtube.com/watch?v=b7389fIVey0) — Steve Brunton, tiếng Anh. Phân tích cặp trị riêng thuần ảo và điểm tâm trên mặt phẳng pha.
- [Linear Systems: Complex Roots | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=TRVS5Wo9LoM) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về hệ tuyến tính có trị riêng phức.
- [MAE5790-5 Two dimensional linear systems](https://www.youtube.com/watch?v=QrHRaA93Nrg) — Cornell MAE, tiếng Anh. Giáo sư Strogatz phân loại hệ tuyến tính hai chiều, bao gồm các trường hợp xoắn ốc.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: trình bày rõ kỹ thuật chuyển nghiệm phức sang nghiệm thực.
- Arnold, *Ordinary Differential Equations*: giải thích sâu trực giác hình học của chuyển động quay.
