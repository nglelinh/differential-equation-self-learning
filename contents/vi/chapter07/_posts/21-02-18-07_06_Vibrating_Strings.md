---
layout: post
title: "07-06 Ứng dụng: Dây rung"
chapter: '07'
order: 6
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

## Mục tiêu

Bài học này nối toàn bộ chương với mô hình dây rung cổ điển. Sau bài học, sinh viên cần hiểu vì sao điều kiện biên cố định hai đầu sinh ra bài toán trị riêng không gian, biết diễn giải các hàm riêng như các mode đứng, và thấy cách ghép các mode để mô tả dao động tổng quát của dây.

## Kiến thức nền

Sinh viên nên nắm BVP hai điểm, bài toán trị riêng, trực giao của hàm riêng và khai triển theo hàm riêng. Một ít trực giác vật lý về sóng trên dây sẽ làm bài học trở nên rất tự nhiên.

## Dẫn nhập

![Các mode đứng của dây rung]({{ site.imgurl }}/chapter_img/chapter07/06_vibrating_strings.svg)

Nếu có một ví dụ vật lý duy nhất để minh họa toàn bộ lý thuyết giá trị biên, trị riêng và khai triển theo hàm riêng, thì đó chính là dây rung. Một sợi dây bị giữ cố định ở hai đầu không thể dao động theo mọi hình dạng tùy ý nếu ta xét các mode tự nhiên của nó. Nó chỉ cho phép một họ hình dạng đặc biệt, và mỗi hình dạng đi kèm một tần số riêng. Chính ở đây, những khái niệm tưởng như trừu tượng của chương bỗng trở nên nhìn thấy, nghe thấy và cảm được.

Điều quan trọng về mặt sư phạm là bài này hợp nhất nhiều lớp ý tưởng đã học. BVP xác định toán tử không gian. Bài toán trị riêng chọn ra các mode đứng. Tính trực giao cho phép tách dữ kiện ban đầu thành tổng các mode. Toàn bộ chương vì vậy hiện lên như một chuỗi logic thống nhất, không còn là các kỹ thuật rời rạc.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một dây đàn bị ghim ở hai đầu chỉ có thể rung tự nhiên theo những mẫu hình "vừa khít" với hai đầu cố định. Mẫu cơ bản có một bụng, mẫu tiếp theo có hai bụng, rồi ba bụng, và cứ thế tiếp tục. Mỗi mẫu là một mode đứng.

### Cách nhìn hình ảnh

Khi nhìn hình dạng của các mode, ta thấy ngay số nút bên trong dây tăng dần theo mode. Mode bậc cao dao động nhanh hơn và có hoa văn không gian phức tạp hơn. Chính hình ảnh này làm rõ ý nghĩa của trị riêng như tần số riêng và hàm riêng như hình dạng riêng.

### Cách nhìn hình thức

Với phương trình sóng một chiều
$$ u_{tt}=c^2u_{xx},
\qquad 0<x<L, $$
và điều kiện biên
$$ u(0,t)=u(L,t)=0, $$
tách biến
$$ u(x,t)=X(x)T(t) $$
cho bài toán không gian
$$ X''+\lambda X=0,
\qquad X(0)=X(L)=0. $$
Do đó
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
\lambda_n=\left(\frac{n\pi}{L}\right)^2.
$$

## Những ngộ nhận thường gặp

- "Một hình dạng ban đầu bất kỳ của dây chính là một mode riêng." Không đúng; thường đó là tổng của nhiều mode.
- "Các hàm sin chỉ là công thức quen thuộc chứ không có nội dung vật lý riêng." Sai. Chúng chính là các mode đứng của bài toán biên cố định.
- "Điều kiện biên chỉ dùng để tìm hằng số." Sai. Chúng quyết định toàn bộ phổ trị riêng.
- "Phần thời gian mới là phần quan trọng." Trong bài toán tách biến, phần không gian mới là nơi cấu trúc phổ được sinh ra.

## Tiến trình học tập đề xuất

### Bước 1: Viết phương trình sóng và điều kiện biên

Đây là bước mô hình hóa vật lý nền tảng.

### Bước 2: Tách biến

Sinh viên cần thấy rõ vì sao bài toán không gian trở thành bài toán trị riêng.

### Bước 3: Tìm mode đứng và tần số riêng

Đây là phần đẹp nhất của bài.

### Bước 4: Ghép mode để mô tả dao động tổng quát

Toàn bộ nội dung của khai triển theo hàm riêng được dùng ở đây.

### Các checkpoint

- Sinh viên có giải được bài toán trị riêng không gian của dây hay không.
- Sinh viên có diễn giải được mode đứng bằng ngôn ngữ vật lý hay không.
- Sinh viên có thấy vì sao dữ kiện ban đầu phải được khai triển theo mode hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ba mode đầu tiên

Với dây dài $$ L $$, ba mode đầu là
$$ X_1(x)=\sin\left(\frac{\pi x}{L}\right), $$
$$ X_2(x)=\sin\left(\frac{2\pi x}{L}\right), $$
$$ X_3(x)=\sin\left(\frac{3\pi x}{L}\right). $$
Mode thứ nhất có một bụng, mode thứ hai có hai bụng, và mode thứ ba có ba bụng.

### Ví dụ 2: Tần số riêng

Từ trị riêng
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2, $$
ta được tần số góc
$$ \omega_n=c\frac{n\pi}{L}. $$
Ví dụ này cho thấy các harmonics xuất hiện tự nhiên từ điều kiện biên cố định.

### Ví dụ 3: Nghiệm tổng quát

Nghiệm của dây rung có dạng
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)\sin\left(\frac{n\pi x}{L}\right).
$$
Các hệ số $$ A_n,B_n $$ được xác định từ hình dạng và vận tốc ban đầu. Đây chính là chỗ khai triển theo hàm riêng được sử dụng một cách trọn vẹn.

### Ví dụ 4: Ý nghĩa của mode chồng chập

Nếu kích thích dây theo hình dạng không trùng với một mode đơn, dây không "chọn một công thức mới", mà chỉ trộn các mode sẵn có. Đây là ý nghĩa vật lý sâu nhất của tính đầy đủ của họ hàm riêng.

## Câu hỏi khái niệm

1. Vì sao dây cố định hai đầu chỉ cho phép một phổ rời rạc các tần số riêng?
2. Tại sao một trạng thái ban đầu bất kỳ lại phải được viết như tổng các mode?
3. Điều kiện biên tác động thế nào đến hình dạng và phổ của các mode đứng?

## Bài toán ứng dụng

1. Trong nhạc cụ dây, vì sao âm thanh chứa cả họa âm chứ không chỉ một tần số?
2. Trong kỹ thuật cơ khí, vì sao biết trước các mode riêng lại quan trọng để tránh cộng hưởng nguy hiểm?
3. Nếu một đầu dây tự do thay vì cố định, phổ tần số sẽ thay đổi như thế nào?

## Chiến lược giảng dạy tương tác

- Cho sinh viên quan sát hoặc mô phỏng ba mode đầu trước khi viết công thức.
- Yêu cầu lớp mô tả bằng lời sự khác nhau giữa mode cơ bản và các mode bậc cao.
- So sánh hình dạng ban đầu bất kỳ với tổ hợp của các mode đứng để làm rõ ý tưởng khai triển.
- Liên hệ trực tiếp với âm nhạc hoặc dao động cơ học để tăng trực giác.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu tập trung trước vào việc nhận diện các mode đầu và hiểu ý nghĩa của nút, bụng, tần số riêng. Khi trực giác vững, công thức tổng quát sẽ bớt khó hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi so sánh các điều kiện biên khác nhau như cố định-tự do, hoặc tự suy ra cách tính hệ số từ dữ kiện ban đầu.

## Tóm tắt dễ nhớ

Dây rung là ví dụ vật lý mẫu của chương. Điều kiện biên chọn ra trị riêng, trị riêng sinh ra mode đứng, và khai triển theo hàm riêng cho phép ghép các mode thành dao động tổng quát. Đây là nơi toàn bộ chương hội tụ rất đẹp.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dây đàn cố định hai đầu
- Bài toán: Tìm các mode dao động riêng và tần số tự nhiên của dây đàn.
- Mô hình:
$$ u_{tt}=c^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
Sau tách biến:
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0. $$
- Giả thiết và giới hạn: Dây mảnh, lực căng đều, dao động nhỏ.
- Diễn giải: Mode riêng là sin, còn trị riêng quyết định phổ tần số.

#### Cột hay ống rung một chiều
- Bài toán: Ống âm học hoặc thanh đàn hồi một chiều có các mode đứng phụ thuộc biên.
- Mô hình: Cùng một bài toán Sturm-Liouville với điều kiện Dirichlet, Neumann hoặc hỗn hợp.
- Giả thiết và giới hạn: Hình học một chiều, chưa xét damping.
- Diễn giải: Điều kiện biên thay đổi trực tiếp họ hàm riêng và các cộng hưởng khả dĩ.

### 2. Trực giác bổ sung và các kết nối

Bài toán dây rung là ví dụ vật lý mẫu cho toàn bộ chương: BVP tạo trị riêng, trị riêng sinh mode, và các mode ghép lại thành nghiệm tổng quát. Một bẫy phổ biến là xem sin-cos như công thức quen thuộc riêng lẻ; thật ra chúng là hệ hàm riêng của toán tử không gian với biên cố định.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0
x = np.linspace(0, L, 500)

fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, n in zip(axes, [1, 2, 3]):
    y = np.sin(n * np.pi * x / L)
    ax.plot(x, y)
    ax.set_title(f"Mode {n}")
    ax.set_ylim(-1.1, 1.1)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vibrating string standing wave modes
- search: fixed ends string eigenmodes animation
- search: boundary conditions standing waves

### 5. Bài toán mẫu có bối cảnh thực

Từ
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
ta thu được
$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$
Do đó nghiệm tổng quát của dây rung có dạng
$$
u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cos(\omega_n t)+B_n\sin(\omega_n t)\right)X_n(x),
$$
với
$$ \omega_n=c\frac{n\pi}{L}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào mode đứng, tần số riêng và cách ghép mode để khớp dữ kiện đầu.

**Bậc sau đại học.** Liên hệ với lý thuyết phổ của toán tử sóng, năng lượng và cơ sở trực giao trong không gian Hilbert.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10-11: mô hình dây rung và mode đứng.
- Haberman, Chương 5: liên hệ rất tốt giữa BVP, trị riêng và phương trình sóng.
