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

## Mục tiêu

Bài học này trình bày hai tính chất định tính quan trọng nhất của hàm điều hòa: tính chất trung bình và nguyên lý cực đại. Sau bài học, sinh viên cần hiểu vì sao giá trị của một hàm điều hòa tại một điểm bằng trung bình của nó xung quanh điểm đó, biết hệ quả rằng hàm điều hòa không thể có cực đại hay cực tiểu nội tại nghiêm ngặt trừ khi là hằng, và dùng nguyên lý cực đại để giải thích tính duy nhất của bài toán Dirichlet.

## Kiến thức nền

Sinh viên nên nắm phương trình Laplace, trực giác về trạng thái cân bằng không nguồn, và khái niệm bài toán biên. Đây là bài lý thuyết cốt lõi của chương vì nó mô tả "tính cách" của hàm điều hòa mà không cần công thức nghiệm cụ thể.

## Dẫn nhập

Điều gì làm hàm điều hòa trở nên đặc biệt? Không chỉ là việc nó thỏa $$ \Delta u=0 $$, mà là những tính chất định tính rất mạnh đi kèm. Một trong những tính chất đẹp nhất là: giá trị tại một điểm không được quyết định bởi điểm đó, mà bởi trung bình xung quanh. Từ đó suy ra ngay rằng nghiệm không thể tự mọc ra một đỉnh mới hay một đáy mới trong nội thất.

Đây là chỗ mà trực giác "cân bằng" trở nên chính xác. Nếu bên trong miền không có nguồn, thì không có cơ chế nào để đẩy trường lên một cực đại nội tại hay kéo nó xuống một cực tiểu nội tại. Mọi giá trị bên trong đều bị ràng buộc bởi lân cận và cuối cùng bởi biên.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu nhiệt độ đã ở trạng thái ổn định không nguồn, giá trị tại một điểm không thể khác biệt quá mạnh so với môi trường rất gần quanh nó. Nếu điểm đó nóng hơn hẳn mọi điểm xung quanh, hệ chưa thật sự cân bằng. Vì thế trong trạng thái điều hòa, điểm trung tâm phải "bình quân" với vùng lân cận. Đó là trực giác của tính chất trung bình.

### Cách nhìn hình ảnh

Hãy tưởng tượng một bề mặt đàn hồi mỏng được giữ bởi biên. Nếu bề mặt là điều hòa, nó không thể có một chóp nhọn hoàn toàn bên trong mà không có lực nâng từ dưới. Nếu có một cực đại nội tại nghiêm ngặt, trung bình quanh điểm đó sẽ thấp hơn, mâu thuẫn với tính chất trung bình. Hình ảnh này rất tốt để dẫn tới nguyên lý cực đại.

### Cách nhìn hình thức

Nếu $$ u $$ điều hòa trong miền $$ \Omega $$ và quả cầu $$ B_r(x_0)\subset \Omega $$, thì

$$
u(x_0)=\frac{1}{\lvert B_r\rvert}\int_{B_r(x_0)}u(x)\,dx.
$$

Một công thức tương tự đúng với trung bình trên mặt cầu. Từ đó suy ra nguyên lý cực đại:

$$
\max_{\overline{\Omega}}u=\max_{\partial\Omega}u,
\qquad
\min_{\overline{\Omega}}u=\min_{\partial\Omega}u,
$$

nếu $$ u $$ điều hòa và liên tục trên đóng của miền.

## Những ngộ nhận thường gặp

- "Tính chất trung bình chỉ là mẹo tích phân." Sai. Nó là bản chất hình học của hàm điều hòa.
- "Nguyên lý cực đại nói rằng hàm điều hòa không thể lớn." Không đúng; nó nói cực trị phải nằm ở biên nếu hàm không hằng.
- "Nếu có cực đại nội tại thì chắc chỉ do đồ thị đặc biệt." Sai; điều đó bị cấu trúc Laplace cấm.
- "Tính duy nhất của bài toán Dirichlet phải đến từ công thức nghiệm." Không nhất thiết; nguyên lý cực đại cho tính duy nhất rất trực tiếp.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu tính chất trung bình

Đây là phát biểu nền tảng nhất.

### Bước 2: Suy ra nguyên lý cực đại

Sinh viên nên thấy nó như một hệ quả tự nhiên chứ không phải định lý rời rạc.

### Bước 3: Áp dụng cho tính duy nhất

Đây là ứng dụng quan trọng nhất của bài.

### Các checkpoint

- Sinh viên có giải thích được bằng lời vì sao giá trị tại tâm phải bằng trung bình xung quanh hay không.
- Sinh viên có hiểu vì sao cực đại nội tại nghiêm ngặt là không thể hay không.
- Sinh viên có dùng nguyên lý cực đại để chứng minh tính duy nhất được hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Trường hợp hằng

Nếu $$ u(x)\equiv C $$, thì rõ ràng giá trị tại mọi điểm bằng trung bình trên mọi quả cầu xung quanh. Đây là ví dụ đơn giản nhất cho tính chất trung bình.

### Ví dụ 2: Hàm affine trong một chiều

Trong một chiều, $$ u''=0 $$ cho $$ u(x)=ax+b $$. Giá trị tại điểm giữa đoạn đúng bằng trung bình của hai đầu đoạn. Đây là phiên bản một chiều rất trực giác của tính chất trung bình.

### Ví dụ 3: Tính duy nhất của bài toán Dirichlet

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán Dirichlet cho Laplace. Đặt $$ w=u_1-u_2 $$. Khi đó

$$
\Delta w=0,
\qquad
w=0 \text{ trên } \partial\Omega.
$$

Theo nguyên lý cực đại, $$ \max_{\overline{\Omega}}w=0 $$ và $$ \min_{\overline{\Omega}}w=0 $$. Suy ra $$ w\equiv 0 $$. Đây là ví dụ quan trọng nhất của bài.

### Ví dụ 4: Kiểm tra trực giác của nghiệm số

Nếu một nghiệm số cho bài toán Laplace với dữ liệu biên không âm lại tạo ra một đỉnh âm bên trong miền, ta biết ngay có gì đó sai. Ví dụ này giúp nối lý thuyết với tính toán số.

## Câu hỏi khái niệm

1. Vì sao tính chất trung bình phản ánh trực tiếp ý tưởng "không có nguồn bên trong"?
2. Tại sao cực đại nội tại nghiêm ngặt mâu thuẫn với tính chất trung bình?
3. Vì sao nguyên lý cực đại kéo theo tính duy nhất của bài toán Dirichlet?

## Bài toán ứng dụng

1. Trong nhiệt ổn định, vì sao nếu biên luôn nằm trong khoảng $$ [m,M] $$, nhiệt độ bên trong cũng phải nằm trong khoảng đó?
2. Trong tĩnh điện, vì sao điện thế trong vùng không có điện tích không thể có một đỉnh nội tại nghiêm ngặt?
3. Trong mô phỏng số Laplace, vì sao nguyên lý cực đại là một kiểm tra chất lượng rất mạnh?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu bên trong miền không có nguồn, điều gì ngăn trường tạo ra một đỉnh mới?"
- Cho sinh viên thử phản biện bằng cách giả sử tồn tại cực đại nội tại rồi đối chiếu với tính chất trung bình.
- Hỏi cả lớp: "Nếu hai nghiệm có cùng biên, tại sao hiệu của chúng phải bằng 0?"
- Khuyến khích sinh viên diễn giải nguyên lý cực đại bằng ngôn ngữ vật lý, không chỉ bằng ký hiệu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào phiên bản một chiều và trực giác trung bình trên đoạn trước. Khi ý tưởng đó rõ, công thức quả cầu và nguyên lý cực đại sẽ bớt trừu tượng hơn.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận nguyên lý cực đại mạnh hoặc liên hệ tính chất trung bình với các quá trình martingale và xác suất thế vị.

## Tóm tắt dễ nhớ

Hàm điều hòa có giá trị tại một điểm bằng trung bình của nó xung quanh điểm đó. Vì thế nó không thể có cực trị nội tại nghiêm ngặt trừ khi là hằng. Đây là lý do bài toán Dirichlet cho Laplace có tính duy nhất rất mạnh và nghiệm bị biên kiểm soát hoàn toàn.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - khuôn khổ chuẩn cho hàm điều hòa, phương trình Poisson, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - trình bày trực quan về tĩnh điện, dòng chảy thế, và phương pháp ảnh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kiểm tra cảm biến nhiệt
- Bài toán: Nếu dữ liệu biên nằm trong một khoảng cho trước, nhiệt độ bên trong không thể vượt quá khoảng đó khi không có nguồn.
- Mô hình: Tính chất này đến từ nguyên lý cực đại cho $$ \Delta u=0 $$.
- Giả thiết và giới hạn: Miền liên thông, nghiệm điều hòa đủ trơn.
- Diễn giải: Cực trị của nghiệm điều hòa nằm ở biên, không ở bên trong.

#### Điện thế tĩnh không có cực trị nội bộ
- Bài toán: Trong miền không có điện tích, điện thế không thể có điểm cực đại hoặc cực tiểu chặt bên trong.
- Mô hình: Mean value property và maximum principle cho hàm điều hòa.
- Giả thiết và giới hạn: Không có nguồn nội bộ, nghiệm đủ trơn.
- Diễn giải: Đây là ràng buộc định tính rất mạnh, thường hữu ích hơn công thức nghiệm tường minh.

### 2. Trực giác bổ sung và các kết nối

Tính chất trung bình nói rằng giá trị tại một điểm bằng trung bình trên các vòng tròn nhỏ xung quanh nó. Nếu một điểm thật sự là cực đại nội bộ, trung bình xung quanh sẽ nhỏ hơn nó, điều này mâu thuẫn. Đây là trực giác gốc của nguyên lý cực đại.

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

Nếu $$ u $$ điều hòa trên một miền đóng bị chặn và $$ u=0 $$ trên toàn bộ biên, thì theo nguyên lý cực đại cả cực đại lẫn cực tiểu đều bằng $$ 0 $$. Do đó
$$ u\equiv 0. $$
Đây là cách rất nhanh để chứng minh tính duy nhất mà không cần viết nghiệm ra.

### 6. Phân tầng độ khó

**Bậc đại học.** Dùng nguyên lý cực đại để suy ra chặn trên, chặn dưới và tính duy nhất.

**Bậc sau đại học.** Kết nối với Harnack inequality, unique continuation và weak maximum principle.
