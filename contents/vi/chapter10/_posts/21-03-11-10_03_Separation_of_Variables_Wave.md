---
layout: post
title: "Phương Pháp Tách Biến Cho Sóng"
chapter: '10'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 03 Separation Of Variables Wave]({{ site.imgurl }}/chapter_img/chapter10/03_separation_of_variables_wave.svg)

## Mục tiêu

Bài học này trình bày phương pháp tách biến cho phương trình sóng trên đoạn hữu hạn, nơi điều kiện biên tạo ra các sóng dừng và các tần số riêng. Sau bài học, sinh viên cần biết cách chuyển PDE thành bài toán trị riêng không gian cùng ODE thời gian, hiểu vì sao các mode riêng là sóng dừng, và thấy được cách dữ liệu đầu được khai triển theo các họa âm của dây.

## Kiến thức nền

Sinh viên nên nắm bài toán trị riêng Sturm-Liouville, khai triển Fourier sine và điều kiện đầu của phương trình sóng. Bài này là nơi Fourier, giá trị riêng và vật lý sóng gặp nhau rõ nhất.

## Dẫn nhập

Trên toàn trục, nghiệm d'Alembert cho ta sóng chạy. Nhưng trên một đoạn hữu hạn, nhất là với hai đầu dây bị cố định, sóng không thể cứ chạy mãi mà không phản xạ. Hệ bắt đầu chọn ra những mode đặc biệt tương thích với biên. Những mode đó không dịch chuyển như sóng chạy đơn lẻ, mà dao động tại chỗ. Chúng được gọi là sóng dừng.

Vì vậy bài này rất quan trọng: nó chỉ ra cách hình học của miền và điều kiện biên biến bài toán sóng thành một bài toán phổ. Âm thanh của dây đàn chính là tổng của các mode dừng này.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một dây đàn bị kẹp ở hai đầu không thể rung với hình dạng bất kỳ. Chỉ những hình dạng vừa khít với hai đầu cố định mới tồn tại lâu dài như các mode dao động tự nhiên. Tách biến là cách toán học để tìm chính các mode "vừa khít" đó.

### Cách nhìn hình ảnh

Mode đầu tiên có một bụng và không có nút trong nội thất, mode thứ hai có hai bụng và một nút giữa, mode thứ ba có nhiều nút hơn. Mỗi mode dao động theo thời gian nhưng giữ nguyên hình dạng không gian. Hình ảnh này giải thích thế nào là sóng dừng.

### Cách nhìn hình thức

Xét

$$ u_{tt}=c^2u_{xx},
\qquad 0<x<L, $$

với điều kiện biên Dirichlet:

$$ u(0,t)=u(L,t)=0. $$

Đặt $$ u(x,t)=X(x)T(t) $$. Thế vào PDE:

$$ X T''=c^2X''T. $$

Chia cho $$ c^2XT $$, ta được

$$ \frac{T''}{c^2T}=\frac{X''}{X}=-\lambda. $$

Từ đó:

$$ X''+\lambda X=0,
\qquad
T''+c^2\lambda T=0. $$

## Những ngộ nhận thường gặp

- "Tách biến cho sóng giống hệt tách biến cho nhiệt." Chỉ giống ở phần không gian; phần thời gian hoàn toàn khác vì bậc thời gian là hai.
- "Mỗi mode riêng là một sóng chạy." Không đúng; trên đoạn hữu hạn các mode riêng điển hình là sóng dừng.
- "Chỉ cần điều kiện đầu về vị trí." Sai; phương trình sóng cần cả vận tốc đầu.
- "Mode cao chỉ là chi tiết kỹ thuật." Không đúng; chúng tạo nên âm sắc và chi tiết dao động.

## Tiến trình học tập đề xuất

### Bước 1: Đặt nghiệm dạng tích

Đây là bước khởi đầu quen thuộc.

### Bước 2: Giải bài toán trị riêng không gian

Điều kiện biên quyết định họ hàm riêng.

### Bước 3: Giải ODE thời gian

Đây là nơi sóng khác nhiệt rõ nhất.

### Bước 4: Ghép điều kiện đầu

Vai trò của $$ f $$ và $$ g $$ phải được thấy rõ.

### Các checkpoint

- Sinh viên có phân biệt được phần không gian và phần thời gian sau tách biến hay không.
- Sinh viên có hiểu vì sao phần thời gian dao động điều hòa thay vì suy giảm mũ hay không.
- Sinh viên có giải thích được ý nghĩa vật lý của các mode dừng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Điều kiện Dirichlet chuẩn

Với $$ u(0,t)=u(L,t)=0 $$, ta có bài toán không gian

$$ X''+\lambda X=0,
\qquad
X(0)=X(L)=0. $$

Nghiệm không tầm thường xuất hiện khi

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$

### Ví dụ 2: Phần thời gian

Với mỗi $$ \lambda_n $$, ta được $$ T_n''+c^2\lambda_n T_n=0 $$. Nghiệm là

$$
T_n(t)=A_n\cos\left(\frac{n\pi ct}{L}\right)
+B_n\sin\left(\frac{n\pi ct}{L}\right).
$$

Ví dụ này nên được dùng để nhấn mạnh: phương trình sóng bảo toàn dao động thay vì dập nó đi.

### Ví dụ 3: Nghiệm tổng quát

Ghép lại:

$$
u(x,t)=\sum_{n=1}^{\infty}
\left[
A_n\cos\left(\frac{n\pi ct}{L}\right)
+B_n\sin\left(\frac{n\pi ct}{L}\right)
\right]
\sin\left(\frac{n\pi x}{L}\right).
$$

Hệ số $$ A_n $$ đến từ dữ liệu vị trí đầu $$ f(x) $$, còn $$ B_n $$ đến từ dữ liệu vận tốc đầu

$$ g(x). $$

### Ví dụ 4: Họa âm của dây đàn

Tần số riêng là

$$ \omega_n=\frac{n\pi c}{L}. $$

Mode thứ nhất là họa âm cơ bản, các mode cao hơn là họa âm bậc cao. Ví dụ này là cầu nối rất mạnh giữa toán học và âm học.

## Câu hỏi khái niệm

1. Vì sao trên đoạn hữu hạn, sóng chạy dẫn đến các mode dừng sau khi xét điều kiện biên?
2. Tại sao phần thời gian của phương trình sóng cho dao động điều hòa thay vì suy giảm mũ như phương trình nhiệt?
3. Vì sao cần cả dữ liệu vị trí và vận tốc đầu để xác định nghiệm?

## Bài toán ứng dụng

1. Một dây đàn bị kẹp hai đầu. Vì sao chỉ một họ rời rạc các tần số mới được phép tồn tại bền vững?
2. Nếu dữ liệu đầu gần với mode cơ bản, vì sao âm thanh nghe được chủ yếu gần với tần số thấp nhất?
3. Trong thiết kế nhạc cụ, vì sao chiều dài $$ L $$ ảnh hưởng trực tiếp đến các tần số riêng?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Một dây bị kẹp hai đầu có thể rung theo mọi hình dạng hay không?"
- Vẽ ba mode đầu tiên và yêu cầu sinh viên đếm số nút, số bụng.
- Hỏi cả lớp: "Điểm khác lớn nhất giữa bài tách biến cho nhiệt và cho sóng là gì?"
- Cho sinh viên ghép dữ liệu đầu với vai trò của

$$ A_n $$

và

$$ B_n. $$

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào bài toán dây hai đầu cố định như mẫu chuẩn. Khi các em hiểu thật chắc trường hợp này, việc mở rộng sang biên khác hoặc hình học khác sẽ dễ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi so sánh nghiệm d'Alembert với khai triển sóng dừng trên đoạn hữu hạn, hoặc phân tích sự khác nhau giữa mode riêng của Dirichlet và Neumann cho dây rung.

## Tóm tắt dễ nhớ

Tách biến cho phương trình sóng trên đoạn hữu hạn sinh ra một bài toán trị riêng không gian và một ODE dao động theo thời gian. Các mode không gian là sóng dừng, còn tần số của chúng là các tần số riêng của hệ. Dữ liệu đầu quyết định cách pha trộn các họa âm đó.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tần số riêng của dây cố định hai đầu
- Bài toán: Xác định các mode dao động của dây violin hay dây cầu treo mô hình hóa một chiều.
- Mô hình:
$$ u_{tt}=c^2u_{xx}, \qquad u(0,t)=u(L,t)=0. $$
- Giả thiết và giới hạn: Biên cố định hoàn toàn, dây lý tưởng, dao động nhỏ.
- Diễn giải: Tách biến dẫn đến các mode đứng rời rạc.

#### Cộng hưởng trong cấu kiện
- Bài toán: Một thanh hay cáp bị kích thích gần tần số riêng sẽ cho đáp ứng lớn.
- Mô hình: Tổng các mode riêng theo điều kiện biên tương ứng.
- Giả thiết và giới hạn: Hệ tuyến tính, không xét phi tuyến hình học.
- Diễn giải: Phân tích mode là nền tảng của thiết kế tránh cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Tách biến biến PDE thành hai ODE được ghép bởi cùng một hằng số tách. Ý nghĩa vật lý là ta đang tìm các hình dạng không gian dao động với nhịp thời gian riêng. Một ngộ nhận hay gặp là mọi điều kiện ban đầu đều là một mode đơn; thật ra chúng thường là tổ hợp của nhiều mode.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for n in [1, 2, 3]:
    plt.plot(x, np.sin(n * np.pi * x), label=f"mode {n}")

plt.xlabel("x")
plt.ylabel("shape")
plt.title("Ba mode rieng dau cua day co dinh hai dau")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: standing waves fixed string modes
- search: separation of variables wave equation string
- search: resonance normal modes string animation

### 5. Bài toán mẫu có bối cảnh thực

Nếu
$$
u(x,0)=\sin\!\left(\frac{\pi x}{L}\right), \qquad u_t(x,0)=0,
$$
thì chỉ mode cơ bản được kích hoạt và nghiệm là
$$
u(x,t)=\cos\!\left(\frac{\pi c t}{L}\right)\sin\!\left(\frac{\pi x}{L}\right).
$$
Điều này cho thấy một hình dạng ban đầu trùng với eigenfunction sẽ dao động mà không đổi hình.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập bài toán tách biến và nhận diện tần số riêng.

**Bậc sau đại học.** Kết nối với Sturm-Liouville, tính trực giao của mode và hội tụ của khai triển eigenfunction.
