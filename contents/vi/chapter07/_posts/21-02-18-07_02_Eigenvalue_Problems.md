---
layout: post
title: "07-02 Bài toán Trị riêng"
chapter: '07'
order: 2
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

## Mục tiêu

Bài học này giới thiệu bài toán trị riêng của ODE như bước chuyển quan trọng từ BVP thông thường sang lý thuyết phổ. Sau bài học, sinh viên cần hiểu trị riêng là gì, vì sao chỉ một số giá trị tham số đặc biệt mới cho nghiệm không tầm thường, biết giải bài toán mẫu trên đoạn hữu hạn, và thấy mối liên hệ trực tiếp giữa trị riêng, mode riêng và tần số tự nhiên của hệ vật lý.

## Kiến thức nền

Sinh viên nên nắm chắc BVP hai điểm, phương trình tuyến tính cấp hai hệ số hằng, và trực giác từ đại số tuyến tính về trị riêng của ma trận. Bài này đặc biệt hiệu quả nếu giảng viên liên tục đối chiếu với đại số tuyến tính để sinh viên thấy sự quen thuộc trong một bối cảnh vô hạn chiều.

## Dẫn nhập

![Bài toán trị riêng Sturm-Liouville]({{ site.imgurl }}/chapter_img/chapter07/02_eigenvalue_problems.svg)

Trong một BVP thông thường, dữ kiện ở vế phải và điều kiện biên thường được cho sẵn, và ta hỏi có nghiệm hay không. Nhưng đôi khi trong phương trình xuất hiện một tham số, và bài toán đổi thành: với những giá trị nào của tham số đó, ta mới có một nghiệm không tầm thường thỏa điều kiện biên? Khi ấy, ta bước vào thế giới của bài toán trị riêng.

Ý tưởng này rất đẹp vì nó hoàn toàn song song với đại số tuyến tính. Với ma trận $$ A $$, ta tìm $$ \lambda $$ để phương trình $$ A\mathbf{v}=\lambda \mathbf{v} $$ có vector riêng khác 0. Với toán tử vi phân, ta cũng làm điều tương tự: chỉ những giá trị tham số đặc biệt mới cho phép xuất hiện nghiệm khác không. Các nghiệm đó chính là hàm riêng, và trong vật lý chúng thường là các mode dao động hoặc trạng thái cộng hưởng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy nghĩ đến một dây đàn bị giữ cố định ở hai đầu. Không phải mọi tần số đều cho phép dây dao động tự nhiên. Chỉ một số tần số đặc biệt tạo ra hình dạng sóng khớp hoàn toàn với điều kiện ở hai đầu. Những tần số đó là trị riêng, còn hình dạng tương ứng là hàm riêng.

### Cách nhìn hình ảnh

Nếu vẽ các mode của dây rung, ta sẽ thấy mode cơ bản có một bụng, mode tiếp theo có hai bụng, rồi ba bụng, và cứ thế tăng dần. Mỗi mode có một "số nút" riêng và gắn với một trị riêng tăng dần. Hình ảnh này rất quan trọng vì nó cho thấy trị riêng không phải chỉ là con số; nó là nhãn cho một hoa văn dao động cụ thể.

### Cách nhìn hình thức

Một bài toán trị riêng vi phân điển hình có dạng $$ Ly=\lambda w(x)y $$, với điều kiện biên thích hợp. Ở đây $$ L $$ là toán tử vi phân và $$ w(x)>0 $$ là trọng số. Ta tìm những giá trị $$ \lambda $$ sao cho tồn tại nghiệm $$ y\not\equiv 0 $$ thỏa điều kiện biên. Những giá trị đó là trị riêng, còn nghiệm tương ứng là hàm riêng.

## Những ngộ nhận thường gặp

- "Trị riêng là bất kỳ giá trị nào làm bài toán có nghiệm." Chưa đủ. Ta cần nghiệm không tầm thường.
- "Hàm riêng chỉ khác nhau bởi một hệ số nên không quan trọng." Sai. Chính hình dạng của chúng mang ý nghĩa mode vật lý.
- "Nếu bài toán có tham số thì mọi giá trị tham số đều đáng như nhau." Không đúng. Bài toán trị riêng chính là sự chọn lọc các giá trị đặc biệt.
- "Khái niệm trị riêng ở ODE không liên quan đến đại số tuyến tính." Sai. Đây là cùng một ý tưởng được mở rộng sang toán tử trên không gian hàm.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại trị riêng ma trận

Điều này giúp sinh viên bớt cảm giác bài mới hoàn toàn xa lạ.

### Bước 2: Xem một BVP có tham số

Hiểu rằng tham số không còn là hằng số phụ mà là đối tượng cần tìm.

### Bước 3: Loại trừ các trường hợp tham số

Giải từng trường hợp

$$ \lambda<0,
\qquad
\lambda=0,
\qquad
\lambda>0 $$

để thấy trị riêng xuất hiện thế nào.

### Bước 4: Diễn giải hàm riêng như mode riêng

Đây là cầu nối quan trọng sang Sturm-Liouville.

### Các checkpoint

- Sinh viên có giải thích được vì sao ta cần nghiệm không tầm thường hay không.
- Sinh viên có giải được bài toán mẫu và tìm ra dãy trị riêng hay không.
- Sinh viên có hiểu hàm riêng là mode dao động hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dây đàn cố định hai đầu

Xét

$$ y''+\lambda y=0,
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Ta xét ba trường hợp.

Nếu $$ \lambda=-\mu^2<0 $$, thì nghiệm có dạng $$ y=Ae^{\mu x}+Be^{-\mu x} $$. Điều kiện biên buộc $$ A=B=0 $$, nên chỉ có nghiệm tầm thường.

Nếu $$ \lambda=0 $$, thì $$ y=Ax+B $$. Điều kiện biên lại buộc $$ A=B=0 $$. Nếu $$ \lambda=\mu^2>0 $$, thì $$ y=A\cos(\mu x)+B\sin(\mu x) $$. Điều kiện $$ y(0)=0 $$ cho $$ A=0 $$. Điều kiện $$ y(L)=0 $$ cho $$ B\sin(\mu L)=0 $$. Để có nghiệm không tầm thường, cần

$$
\sin(\mu L)=0
\quad \Longrightarrow \quad
\mu L=n\pi.
$$

Vậy

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
\phi_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
n=1,2,3,\ldots
$$

Đây là ví dụ nền tảng của cả chương.

### Ví dụ 2: Điều kiện Neumann

Xét

$$ y''+\lambda y=0,
\qquad
y'(0)=0,
\qquad
y'(L)=0. $$

Khi $$ \lambda=\mu^2>0 $$, nghiệm là $$ y=A\cos(\mu x)+B\sin(\mu x) $$. Ta có $$ y'=-A\mu\sin(\mu x)+B\mu\cos(\mu x) $$. Điều kiện $$ y'(0)=0 $$ cho $$ B=0 $$. Điều kiện $$ y'(L)=0 $$ cho $$ -A\mu\sin(\mu L)=0 $$. Do đó $$ \mu L=n\pi $$, và các hàm riêng là

$$ \phi_n(x)=\cos\left(\frac{n\pi x}{L}\right). $$

Ví dụ này cho thấy thay đổi điều kiện biên sẽ thay đổi cả họ hàm riêng.

### Ví dụ 3: Một bài toán có trị riêng bằng 0

Với điều kiện Neumann thuần nhất ở cả hai đầu, mode hằng $$ \phi_0(x)=1 $$ thường xuất hiện tương ứng với $$ \lambda_0=0 $$. Đây là một điểm nhiều sinh viên bỏ sót vì quá quen với dãy bắt đầu từ $$ n=1 $$. Ví dụ này rất đáng để nhấn mạnh: cấu trúc phổ phụ thuộc sâu vào điều kiện biên.

### Ví dụ 4: Từ trị riêng đến tần số

Với dây đàn, nghiệm theo thời gian thường có tần số tỉ lệ với $$ \sqrt{\lambda_n} $$. Điều này cho thấy trị riêng không chỉ là tham số toán học mà là đại lượng vật lý đo được. Ví dụ này nên được dùng để nối bài toán ODE với sóng và âm thanh.

## Câu hỏi khái niệm

1. Vì sao điều kiện $$ y\not\equiv 0 $$ lại là cốt lõi trong định nghĩa trị riêng?
2. Vì sao điều kiện biên thay đổi thì trị riêng và hàm riêng cũng thay đổi theo?
3. Trong mô hình vật lý, tại sao trị riêng thường được hiểu là các tần số tự nhiên hoặc mức năng lượng cho phép?

## Bài toán ứng dụng

1. Một dây đàn dài $$ L $$ bị giữ cố định ở hai đầu. Hãy giải thích vì sao chỉ một dãy rời rạc các tần số dao động mới được phép.
2. Một thanh cách nhiệt hoàn toàn ở hai đầu. Hãy thảo luận vì sao mode nhiệt hằng tương ứng với trị riêng bằng 0 lại xuất hiện tự nhiên.
3. Trong cơ học lượng tử, vì sao điều kiện biên trên miền hữu hạn thường dẫn đến các mức năng lượng rời rạc thay vì liên tục?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng cách hỏi: "Vì sao một dây đàn không phát ra mọi tần số cùng mức mạnh như nhau?"
- Cho sinh viên giải theo nhóm ba trường hợp dấu của

$$ \lambda $$

rồi ghép kết quả thành bức tranh hoàn chỉnh.
- Vẽ các mode đầu tiên của sin và cos để sinh viên gắn trị riêng với hình dạng thật.
- Khuyến khích sinh viên kể lại bằng lời mối liên hệ giữa trị riêng của ma trận và trị riêng của toán tử vi phân.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho các em lặp lại thật chắc ví dụ dây đàn cổ điển trước khi giới thiệu các biến thể điều kiện biên khác. Cấu trúc ba trường hợp của $$ \lambda $$ cần được luyện thành phản xạ.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi so sánh trực tiếp ma trận đối xứng hữu hạn chiều với toán tử Sturm-Liouville để thấy vì sao ta kỳ vọng trị riêng thực và hàm riêng trực giao trong bài sau.

## Tóm tắt dễ nhớ

Bài toán trị riêng hỏi: với những giá trị tham số nào, BVP có nghiệm không tầm thường. Các giá trị đó là trị riêng, còn các nghiệm tương ứng là hàm riêng. Trong vật lý, chúng chính là các mode và tần số tự nhiên mà hệ cho phép.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động tự nhiên của dây đàn
- Bài toán: Một dây giữ cố định hai đầu chỉ dao động ở một số tần số nhất định.
- Mô hình:
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
- Giả thiết và giới hạn: Dây mảnh, lực căng đều, dao động nhỏ.
- Diễn giải: Chỉ các giá trị
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2 $$
mới cho mode không tầm thường.

#### Mức năng lượng lượng tử trong hố thế
- Bài toán: Hạt trong giếng thế một chiều có các trạng thái dừng rời rạc.
- Mô hình: Sau chuẩn hóa, bài toán biên cho phương trình kiểu
$$ y''+\lambda y=0 $$
với điều kiện biên triệt tiêu ở thành giếng.
- Giả thiết và giới hạn: Mô hình hố thế vô hạn là lý tưởng hóa mạnh.
- Diễn giải: Trị riêng là mức năng lượng, hàm riêng là trạng thái sóng.

### 2. Trực giác bổ sung và các kết nối

Bài toán trị riêng của ODE là phiên bản vô hạn chiều của trị riêng ma trận. Điểm quan trọng nhất là: ta không tìm nghiệm cho mọi tham số, mà chỉ tìm những tham số đặc biệt cho phép nghiệm không tầm thường. Một bẫy phổ biến là quên loại nghiệm tầm thường hoặc không nhìn hàm riêng như mode vật lý.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 400)

for n in range(1, 4):
    y = np.sin(n * np.pi * x / L)
    plt.plot(x, y, label=f"n={n}")

plt.xlabel("x")
plt.ylabel("mode shape")
plt.title("Ba ham rieng dau tien cua bai toan day co dinh")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vibrating string eigenmodes boundary value problem
- search: eigenvalue problem ODE mode shapes
- search: quantum infinite well eigenfunctions

### 5. Bài toán mẫu có bối cảnh thực

Giải
$$ y''+\lambda y=0,\qquad y(0)=0,\qquad y(L)=0. $$
Nếu $$ \lambda=\mu^2>0 $$, nghiệm là
$$ y=A\cos(\mu x)+B\sin(\mu x). $$
Điều kiện ở $$ x=0 $$ cho $$ A=0 $$, còn ở $$ x=L $$ cho
$$ B\sin(\mu L)=0. $$
Muốn có nghiệm không tầm thường, cần
$$ \sin(\mu L)=0, $$
tức là
$$ \mu=\frac{n\pi}{L}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Giải bài toán mẫu và hiểu trị riêng, hàm riêng như tần số và mode.

**Bậc sau đại học.** Kết nối với lý thuyết phổ của toán tử tự liên hợp trên không gian hàm.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10: bài toán trị riêng và dây rung hai đầu.
- Haberman, Chương 5: liên hệ giữa trị riêng, mode riêng và điều kiện biên vật lý.
