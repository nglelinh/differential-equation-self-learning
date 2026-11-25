---
layout: post
title: "Tính Chất Trung Bình và Cực Đại"
chapter: '11'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: required
---

![21 03 18 11 05 Mean Value Maximum Principle]({{ site.imgurl }}/chapter_img/chapter11/05_mean_value_maximum_principle.svg)

Không cần giải ra một công thức nghiệm nào, chỉ nhìn vào bốn ký tự $\Delta u = 0$ ta đã có thể tuyên bố chắc nịch hai định luật thép: nhiệt độ tại tâm bất kỳ hình cầu nào luôn bằng **đúng trung bình cộng** nhiệt độ trên mặt cầu bao quanh nó, và điểm nóng nhất hay lạnh nhất của cả căn phòng cân bằng nhiệt **chỉ có thể nằm trên tường biên** chứ không bao giờ lơ lửng giữa phòng! Hai tính chất tưởng giản dị ấy—Tính chất Trung bình và Nguyên lý Cực đại—lại là vũ khí sắc bén nhất để chứng minh tính duy nhất và ổn định nghiệm của PDE elliptic.

## Kiến thức cần nhớ: Bốn trụ cột của Tính chất Trung bình & Nguyên lý Cực đại

1. **Tính chất Giá trị Trung bình (Mean Value Property — MVP)**:
   Với mọi hình cầu $B(x_0, r) \subset \Omega$, hàm điều hòa $u$ thỏa mãn $u(x_0) = \frac{1}{|\partial B|}\int_{\partial B(x_0, r)} u\,dS = \frac{1}{|B|}\int_{B(x_0, r)} u\,dx$. Đáng kinh ngạc hơn: tính chất này là **điều kiện cần và đủ** để một hàm liên tục là hàm điều hòa!
2. **Nguyên lý Cực đại Yếu và Mạnh**:
   - *Yếu*: $\max_{\bar{\Omega}} u = \max_{\partial\Omega} u$ và $\min_{\bar{\Omega}} u = \min_{\partial\Omega} u$.
   - *Mạnh*: Nếu miền $\Omega$ liên thông và $u$ đạt cực đại (hoặc cực tiểu) tại một **điểm trong**, thì $u$ buộc phải là **hằng số trên toàn miền $\Omega$**.
3. **Hệ quả tức thì: Tính duy nhất và Phụ thuộc liên tục vào Dữ liệu biên**:
   Nếu $u_1, u_2$ có cùng dữ liệu biên thì $w = u_1 - u_2$ điều hòa với $w|_{\partial\Omega} = 0 \implies w \equiv 0$. Tổng quát hơn, $\|u_1 - u_2\|_{L^\infty(\Omega)} \le \|g_1 - g_2\|_{L^\infty(\partial\Omega)}$: sai số biên không bao giờ bị khuếch đại vào bên trong!
4. **Định lý Liouville và Bất đẳng thức Harnack**:
   Từ MVP suy ra ngay Định lý Liouville (mọi hàm điều hòa bị chặn trên toàn $\mathbb{R}^n$ đều là hằng số) và Bất đẳng thức Harnack (hàm điều hòa dương không thể dao động quá mạnh giữa hai điểm gần nhau).

## Mục tiêu

Bài học này trình bày hai tính chất định tính quan trọng của hàm điều hòa: tính chất giá trị trung bình và nguyên lý cực đại. Sau bài học, sinh viên cần hiểu vì sao giá trị của một hàm điều hòa tại một điểm bằng trung bình của nó xung quanh điểm đó, nắm được hệ quả rằng hàm điều hòa không thể có cực đại hay cực tiểu chặt bên trong miền trừ khi là hàm hằng, và biết dùng nguyên lý cực đại để chứng minh tính duy nhất của nghiệm bài toán Dirichlet.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace, trực giác về trạng thái cân bằng không nguồn và khái niệm bài toán biên. Đây là bài lý thuyết cốt lõi của chương vì nó mô tả hành vi đặc trưng của hàm điều hòa mà không cần đến công thức nghiệm tường minh.

## Dẫn nhập

Điều làm hàm điều hòa trở nên đặc biệt không chỉ là phương trình $$ \Delta u=0 $$, mà là những tính chất định tính chặt chẽ đi kèm. Một trong số đó là giá trị tại một điểm không tồn tại độc lập, mà bằng trung bình các giá trị xung quanh nó. Từ tính chất này suy ra ngay rằng nghiệm điều hòa khác hằng không thể tự tạo ra đỉnh cực đại hay đáy cực tiểu bên trong miền.

Tại đây, trực giác về trạng thái cân bằng trở thành phát biểu toán học chính xác. Khi không có nguồn bên trong miền, không có cơ chế nào để đẩy giá trị nghiệm lên cực đại cục bộ hay kéo xuống cực tiểu cục bộ bên trong; mọi giá trị bên trong đều bị ràng buộc bởi lân cận và cuối cùng bởi dữ liệu trên biên.


### Giải thích: Kiểm chứng trực tiếp cả MVP lẫn Nguyên lý Cực đại trên một đĩa đóng

Xét hàm điều hòa $u(x, y) = x^2 - y^2 + 3$ trên đĩa đóng $\bar{D}: x^2 + y^2 \le 4$ (bán kính $R = 2$):
1. **Kiểm tra Tính chất Trung bình trên đường tròn biên $r = 2$**:
   Thay $x = 2\cos\theta$, $y = 2\sin\theta$:
   $$u(2\cos\theta, 2\sin\theta) = 4(\cos^2\theta - \sin^2\theta) + 3 = 4\cos(2\theta) + 3.$$
   Lấy trung bình trên $[0, 2\pi]$:
   $$\frac{1}{2\pi}\int_0^{2\pi} \big(4\cos(2\theta) + 3\big)\,d\theta = 0 + 3 = \mathbf{3} = u(0, 0)!$$
2. **Tìm cực đại và cực tiểu toàn cục mà không cần giải hệ đạo hàm**:
   Theo Nguyên lý Cực đại, ta chỉ cần nhìn biểu thức trên biên $4\cos(2\theta) + 3$:
   - **Cực đại**: $4(1) + 3 = \mathbf{7}$, đạt tại hai điểm biên $(\pm 2, 0)$.
   - **Cực tiểu**: $4(-1) + 3 = \mathbf{-1}$, đạt tại hai điểm biên $(0, \pm 2)$.
   Mọi điểm bên trong đĩa đều có giá trị nằm chặt trong khoảng $(-1, 7)$!
## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi phân bố nhiệt độ đã đạt trạng thái ổn định không nguồn, nhiệt độ tại một điểm không thể cao hơn hẳn mọi điểm ngay xung quanh nó, vì nếu vậy nhiệt vẫn sẽ tiếp tục truyền đi và hệ chưa đạt cân bằng. Do đó, ở trạng thái điều hòa, giá trị tại mỗi điểm phải cân bằng với trung bình của vùng lân cận — đó là trực giác của tính chất giá trị trung bình.

### Cách nhìn hình ảnh

Hãy xét một màng đàn hồi mỏng được căng giữ theo đường biên. Nếu bề mặt có tính điều hòa, nó không thể tạo ra một đỉnh nhọn nằm hoàn toàn bên trong mà không có lực nâng từ phía dưới. Nếu tồn tại cực đại chặt bên trong miền, giá trị trung bình xung quanh điểm đó sẽ nhỏ hơn giá trị tại chính điểm đó, mâu thuẫn với tính chất giá trị trung bình. Lập luận này dẫn thẳng tới nguyên lý cực đại.

### Cách nhìn hình thức

Nếu $$ u $$ điều hòa trong miền $$ \Omega $$ và hình cầu $$ B_r(x_0)\subset \Omega $$, thì:

$$
u(x_0)=\frac{1}{\lvert B_r\rvert}\int_{B_r(x_0)}u(x)\,dx.
$$

Công thức tương tự cũng đúng với trung bình trên mặt cầu. Từ đó suy ra nguyên lý cực đại:

$$
\max_{\overline{\Omega}}u=\max_{\partial\Omega}u,
\qquad
\min_{\overline{\Omega}}u=\min_{\partial\Omega}u,
$$

với điều kiện $$ u $$ điều hòa trong $$ \Omega $$ và liên tục trên bao đóng $$ \overline{\Omega} $$ của miền bị chặn.

## Những ngộ nhận thường gặp

- "Tính chất giá trị trung bình chỉ là một kỹ thuật tính tích phân." Sai; nó phản ánh trực tiếp bản chất hình học của hàm điều hòa.
- "Nguyên lý cực đại có nghĩa là hàm điều hòa không thể nhận giá trị lớn." Không đúng; nguyên lý chỉ khẳng định cực trị phải đạt được trên biên nếu hàm không phải hàm hằng.
- "Nếu có cực đại bên trong miền thì chỉ là do hình dạng đặc biệt của đồ thị." Sai; cấu trúc của phương trình Laplace loại trừ khả năng này đối với hàm điều hòa khác hằng.
- "Tính duy nhất của bài toán Dirichlet phải chứng minh từ công thức nghiệm." Không cần thiết; nguyên lý cực đại cho phép chứng minh tính duy nhất một cách trực tiếp.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu tính chất giá trị trung bình

Nắm vững phát biểu nền tảng về giá trị tại tâm hình cầu hoặc mặt cầu.

### Bước 2: Suy ra nguyên lý cực đại

Nhìn nhận nguyên lý cực đại như hệ quả trực tiếp từ tính chất giá trị trung bình thay vì một định lý tách rời.

### Bước 3: Áp dụng chứng minh tính duy nhất

Sử dụng nguyên lý cực đại cho hiệu của hai nghiệm của bài toán Dirichlet.

### Các checkpoint

- Sinh viên có giải thích được bằng lời vì sao giá trị tại tâm bằng trung bình các giá trị xung quanh hay không.
- Sinh viên có hiểu vì sao cực đại chặt bên trong miền không thể tồn tại đối với hàm điều hòa khác hằng hay không.
- Sinh viên có vận dụng được nguyên lý cực đại để chứng minh tính duy nhất của nghiệm hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm hằng

Nếu $$ u(x)\equiv C $$, hiển nhiên giá trị tại mọi điểm đều bằng trung bình trên mọi hình cầu xung quanh. Đây là trường hợp đơn giản nhất minh họa tính chất giá trị trung bình.

### Ví dụ 2: Hàm tuyến tính trong một chiều

Trong một chiều, $$ u''=0 $$ cho $$ u(x)=ax+b $$. Giá trị tại trung điểm của một đoạn thẳng đúng bằng trung bình cộng của giá trị tại hai đầu mút. Đây là phiên bản một chiều trực quan của tính chất giá trị trung bình.

### Ví dụ 3: Tính duy nhất của bài toán Dirichlet

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán Dirichlet cho phương trình Laplace. Đặt $$ w=u_1-u_2 $$, khi đó:

$$
\Delta w=0,
\qquad
w=0 \text{ trên } \partial\Omega.
$$

Theo nguyên lý cực đại, $$ \max_{\overline{\Omega}}w=0 $$ và $$ \min_{\overline{\Omega}}w=0 $$, suy ra $$ w\equiv 0 $$. Đây là ứng dụng trọng tâm của bài học.

### Ví dụ 4: Kiểm tra tính hợp lý của nghiệm số

Nếu một nghiệm số của bài toán Laplace với dữ liệu biên không âm lại xuất hiện giá trị âm bên trong miền, ta biết ngay phép tính hoặc sơ đồ số có sai sót. Ví dụ này nối trực tiếp lý thuyết định tính với tính toán số.

## Câu hỏi khái niệm

1. Vì sao tính chất giá trị trung bình phản ánh trực tiếp giả thiết không có nguồn bên trong miền?
2. Tại sao sự tồn tại của một cực đại chặt bên trong miền lại mâu thuẫn với tính chất giá trị trung bình?
3. Vì sao nguyên lý cực đại kéo theo tính duy nhất của nghiệm bài toán Dirichlet?

## Bài toán ứng dụng

1. Trong truyền nhiệt ổn định không nguồn, vì sao nếu nhiệt độ trên biên nằm trong đoạn $$ [m,M] $$ thì nhiệt độ bên trong miền cũng phải nằm trong đoạn đó?
2. Trong tĩnh điện, vì sao điện thế trong vùng không có điện tích không thể đạt cực đại chặt bên trong miền?
3. Trong mô phỏng số phương trình Laplace, vì sao nguyên lý cực đại là một tiêu chí kiểm tra chất lượng nghiệm hữu hiệu?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu bên trong miền không có nguồn, điều gì ngăn trường nghiệm tạo ra một đỉnh cực đại mới?"
- Cho sinh viên thử phản chứng bằng cách giả sử tồn tại cực đại chặt bên trong rồi đối chiếu với tính chất giá trị trung bình.
- Hỏi cả lớp: "Nếu hai nghiệm có cùng giá trị trên biên, tại sao hiệu của chúng phải bằng 0 trên toàn miền?"
- Khuyến khích sinh viên diễn giải nguyên lý cực đại bằng ngôn ngữ vật lý bên cạnh công thức toán học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào trường hợp một chiều và tính chất trung bình trên đoạn thẳng trước. Khi ý tưởng này đã rõ ràng, công thức tích phân trên hình cầu và nguyên lý cực đại sẽ dễ tiếp cận hơn.

### Thử thách cho sinh viên khá giỏi

Có thể gợi ý sinh viên khá giỏi tìm hiểu nguyên lý cực đại mạnh, hoặc liên hệ tính chất giá trị trung bình với quá trình martingale và lý thuyết thế xác suất.

## Tóm tắt dễ nhớ

Hàm điều hòa có giá trị tại mỗi điểm bằng trung bình các giá trị xung quanh nó. Do đó, hàm điều hòa khác hằng không thể đạt cực trị chặt bên trong miền. Hệ quả trực tiếp là nghiệm bài toán Dirichlet cho phương trình Laplace có tính duy nhất và hoàn toàn bị chặn bởi dữ liệu biên.

## Video tham khảo

- xem trước: [Harmonic functions: Mean value theorem](https://www.youtube.com/watch?v=p60dU_62KcQ) — Dr Chris Tisdell, tiếng Anh. Chứng minh tính chất giá trị trung bình của hàm điều hòa.
- [Properties of harmonic functions part 2: the mean value property](https://www.youtube.com/watch?v=_bC91Xqirgs) — William Nesse, tiếng Anh. Phát biểu và áp dụng tính chất giá trị trung bình.
- [Qualitative Properties of Laplace's Equation - Partial Differential Equations | Lecture 12](https://www.youtube.com/watch?v=Mi25YqpsxlM) — Jason Bramburger, tiếng Anh. Trình bày các tính chất định tính của phương trình Laplace, bao gồm nguyên lý cực đại.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chuẩn về hàm điều hòa, phương trình Poisson và hàm Green.
- Haberman, *Applied Partial Differential Equations* — trình bày trực quan về tĩnh điện, dòng chảy thế và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kiểm tra cảm biến nhiệt
- Bài toán: Nếu nhiệt độ trên biên nằm trong một khoảng cho trước và không có nguồn bên trong, nhiệt độ bên trong miền không thể vượt ra ngoài khoảng đó.
- Mô hình: Suy ra từ nguyên lý cực đại cho $$ \Delta u=0 $$.
- Giả thiết và giới hạn: Miền liên thông, bị chặn; nghiệm điều hòa liên tục trên bao đóng miền.
- Diễn giải: Cực trị của nghiệm điều hòa đạt được trên biên chứ không ở bên trong miền.

#### Điện thế tĩnh không có cực trị bên trong
- Bài toán: Trong miền không có điện tích, điện thế không thể có điểm cực đại hoặc cực tiểu chặt bên trong.
- Mô hình: Tính chất giá trị trung bình và nguyên lý cực đại cho hàm điều hòa.
- Giả thiết và giới hạn: Không có nguồn điện tích bên trong, nghiệm đủ trơn.
- Diễn giải: Đây là ràng buộc định tính chặt chẽ, thường hữu ích ngay cả khi không có công thức nghiệm tường minh.

### 2. Trực giác bổ sung và các kết nối

Tính chất giá trị trung bình khẳng định giá trị tại một điểm bằng trung bình trên các đường tròn nhỏ bao quanh điểm đó. Nếu điểm ấy là cực đại chặt bên trong, giá trị trung bình xung quanh phải nhỏ hơn nó — dẫn đến mâu thuẫn. Đó chính là lập luận gốc của nguyên lý cực đại.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)
U = X**2 - Y**2

plt.contour(X, Y, U, levels=20)
plt.scatter([0], [0], color="red", label="u(0,0)=0 = trung binh dia phuong")
plt.axis("equal")
plt.legend()
plt.title("Duong muc cua mot ham dieu hoa")
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: maximum principle harmonic function visualization
- search: mean value property Laplace equation animation
- search: harmonic function no interior maxima

### 5. Bài toán mẫu có bối cảnh thực

Nếu $$ u $$ điều hòa trên một miền bị chặn, liên tục trên bao đóng và $$ u=0 $$ trên toàn bộ biên, thì theo nguyên lý cực đại cả giá trị lớn nhất lẫn nhỏ nhất trên miền đều bằng $$ 0 $$. Suy ra
$$ u\equiv 0. $$
Đây là cách ngắn gọn để chứng minh tính duy nhất mà không cần tìm công thức nghiệm.

### 6. Phân tầng độ khó

**Bậc đại học.** Vận dụng nguyên lý cực đại để suy ra chặn trên, chặn dưới và tính duy nhất của nghiệm.

**Bậc sau đại học.** Kết nối với bất đẳng thức Harnack, tính thác triển duy nhất (unique continuation) và nguyên lý cực đại yếu.
