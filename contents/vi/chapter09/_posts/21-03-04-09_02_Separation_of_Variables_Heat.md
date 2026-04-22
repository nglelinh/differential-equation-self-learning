---
layout: post
title: "Phương Pháp Tách Biến Cho Phương Trình Nhiệt"
chapter: '09'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 02 Separation Of Variables Heat]({{ site.imgurl }}/chapter_img/chapter09/02_separation_of_variables_heat.svg)

## Mục tiêu

Bài học này trình bày phương pháp tách biến cho phương trình nhiệt trên đoạn hữu hạn. Sau bài học, sinh viên cần hiểu vì sao giả thiết $$ u(x,t)=X(x)T(t) $$ là tự nhiên trong bài toán tuyến tính có điều kiện biên đơn giản, biết cách tách PDE thành hai ODE, hiểu vai trò của bài toán trị riêng không gian, এবং thấy mỗi mode nhiệt suy giảm độc lập theo thời gian với hệ số mũ.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt, chuỗi Fourier, bài toán trị riêng Sturm-Liouville và điều kiện biên thuần nhất. Đây là bài then chốt nối chương Fourier với chương PDE.

## Dẫn nhập

Phương pháp tách biến là một trong những thủ pháp đẹp nhất của PDE cổ điển. Ý tưởng ban đầu có vẻ liều lĩnh: giả sử nghiệm không phải một hàm phức tạp của cả $$ x $$ và $$ t $$, mà là tích của hai hàm đơn giản hơn, một hàm chỉ phụ thuộc không gian và một hàm chỉ phụ thuộc thời gian. Điều bất ngờ là trong các bài toán có cấu trúc đẹp, giả thiết này mở ra cả một hệ mode riêng đủ để ghép lại nghiệm tổng quát.

Đối với phương trình nhiệt, kết quả thu được có ý nghĩa vật lý rất sâu. Mỗi mode không gian là một "hình dạng nhiệt" riêng, còn phần thời gian cho biết mode đó tắt dần nhanh hay chậm. Mode cao tần chết nhanh hơn, mode thấp tần sống lâu hơn. Đây chính là cách toán học diễn đạt hiện tượng làm mượt của khuếch tán.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng nhiệt độ ban đầu của một thanh là tổng của nhiều gợn sóng không gian. Mỗi gợn không biến mất cùng tốc độ. Các gợn ngắn, nhấp nhô mạnh sẽ tắt rất nhanh; các gợn dài, biến thiên chậm sẽ tồn tại lâu hơn. Tách biến cho phép ta nhìn từng gợn như một mode độc lập.

### Cách nhìn hình ảnh

Nếu vẽ các mode

$$ \sin\left(\frac{n\pi x}{L}\right), $$

ta sẽ thấy mode thứ nhất là một nửa sóng, mode thứ hai là một sóng đầy đủ, mode thứ ba nhiều nút hơn. Khi nhân mỗi mode với $$ e^{-\alpha^2\lambda_n t} $$, ta thấy rõ mode có nhiều nút hơn tắt nhanh hơn. Hình ảnh này giải thích vì sao đồ thị nhiệt độ ngày càng mượt.

### Cách nhìn hình thức

Xét bài toán

$$ u_t=\alpha^2u_{xx},
\qquad 0<x<L,\ t>0, $$

với điều kiện biên Dirichlet thuần nhất $$ u(0,t)=u(L,t)=0 $$. Đặt $$ u(x,t)=X(x)T(t) $$. Thế vào PDE:

$$ X(x)T'(t)=\alpha^2X''(x)T(t). $$

Chia cho $$ \alpha^2X(x)T(t) $$, ta được

$$ \frac{T'}{\alpha^2T}=\frac{X''}{X}=-\lambda. $$

Vì vế trái chỉ phụ thuộc $$ t $$ và vế phải chỉ phụ thuộc $$ x $$, cả hai phải bằng cùng một hằng số. Từ đó xuất hiện hai ODE:

$$ X''+\lambda X=0, $$

$$ T'+\alpha^2\lambda T=0. $$

## Những ngộ nhận thường gặp

- "Tách biến luôn cho mọi bài toán." Không đúng; nó cần hình học và điều kiện biên đủ phù hợp.
- "Giả thiết tích là toàn bộ nghiệm." Sai. Nó chỉ tạo ra các mode riêng, rồi ta phải cộng chồng chúng.
- "Tách biến chỉ là mẹo đại số." Không đúng; nó làm lộ rõ cấu trúc phổ của toán tử không gian.
- "Phần thời gian và phần không gian độc lập hoàn toàn." Chúng liên kết với nhau qua cùng một trị riêng

$$ \lambda. $$

## Tiến trình học tập đề xuất

### Bước 1: Viết bài toán đầy đủ

PDE, điều kiện biên, điều kiện đầu phải được nhìn như một hệ thống hoàn chỉnh.

### Bước 2: Đặt nghiệm dạng tích

Đây là điểm khởi đầu của phương pháp.

### Bước 3: Tách thành ODE không gian và thời gian

Sinh viên cần hiểu vì sao xuất hiện hằng số tách biến.

### Bước 4: Giải bài toán trị riêng không gian

Đây là chỗ Fourier và Sturm-Liouville quay lại.

### Bước 5: Ghép tổng các mode

Điều kiện đầu quyết định hệ số của từng mode.

### Các checkpoint

- Sinh viên có giải thích được vì sao hai vế sau khi chia phải bằng một hằng số hay không.
- Sinh viên có tìm đúng bài toán trị riêng không gian hay không.
- Sinh viên có hiểu vì sao nghiệm tổng quát là tổng của các mode, không chỉ một mode duy nhất, hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bài toán Dirichlet chuẩn

Xét

$$ u_t=\alpha^2u_{xx},
\qquad
u(0,t)=u(L,t)=0. $$

Sau tách biến, bài toán không gian là

$$ X''+\lambda X=0,
\qquad
X(0)=X(L)=0. $$

Nghiệm không tầm thường chỉ xuất hiện khi

$$
\lambda_n=\left(\frac{n\pi}{L}\right)^2,
\qquad
X_n(x)=\sin\left(\frac{n\pi x}{L}\right).
$$

Từ phương trình thời gian:

$$ T_n(t)=e^{-\alpha^2\lambda_n t}. $$

Nên mỗi mode có dạng

$$
u_n(x,t)=e^{-\alpha^2(n\pi/L)^2 t}\sin\left(\frac{n\pi x}{L}\right).
$$

### Ví dụ 2: Ghép điều kiện đầu

Nếu $$ u(x,0)=f(x) $$, ta viết

$$
f(x)=\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right),
$$

với

$$
b_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

Do đó

$$
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\alpha^2(n\pi/L)^2 t}\sin\left(\frac{n\pi x}{L}\right).
$$

Ví dụ này là công thức trung tâm của toàn chương.

### Ví dụ 3: Dữ liệu ban đầu hằng

Nếu $$ f(x)=1 $$ trên $$ [0,L] $$, thì

$$
b_n=\frac{2}{L}\int_0^L \sin\left(\frac{n\pi x}{L}\right)\,dx
=\frac{2}{n\pi}\bigl(1-(-1)^n\bigr).
$$

Chỉ các mode lẻ xuất hiện:

$$
u(x,t)=\frac{4}{\pi}\sum_{n=1,3,5,\ldots}^{\infty}\frac{1}{n}
e^{-\alpha^2(n\pi/L)^2 t}
\sin\left(\frac{n\pi x}{L}\right).
$$

Ví dụ này giúp sinh viên thấy rõ cách Fourier và tách biến ghép lại.

### Ví dụ 4: So sánh tốc độ tắt mode

Mode $$ n=1 $$ suy giảm theo $$ e^{-\alpha^2(\pi/L)^2 t} $$, còn mode $$ n=5 $$ suy giảm theo $$ e^{-25\alpha^2(\pi/L)^2 t} $$. Điều này cho thấy mode bậc cao chết cực nhanh. Đây là lời giải thích định lượng cho hiện tượng làm mượt.

## Câu hỏi khái niệm

1. Vì sao trong phương trình nhiệt, các mode không gian cao tần lại tắt nhanh hơn mode thấp tần?
2. Điều gì khiến bài toán trị riêng không gian xuất hiện một cách tự nhiên khi ta tách biến?
3. Vì sao một mode riêng riêng lẻ không đủ mô tả dữ liệu ban đầu tổng quát?

## Bài toán ứng dụng

1. Một thanh có phân bố nhiệt độ ban đầu nhấp nhô mạnh. Hãy giải thích vì sao sau một thời gian ngắn, các nhấp nhô nhỏ biến mất nhanh hơn hình dạng lớn.
2. Trong xử lý ảnh, vì sao khuếch tán nhiệt có thể được xem như một phép lọc làm mịn?
3. Nếu dữ liệu ban đầu gần giống mode cơ bản, vì sao nghiệm về sau thường bị chi phối chủ yếu bởi mode này?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu ta tách dữ liệu ban đầu thành các gợn sóng, gợn nào sẽ sống lâu hơn?"
- Cho sinh viên tự điền các bước tách biến còn khuyết vào một khung lời giải để tránh bị ngợp.
- Vẽ một vài mode đầu tiên và yêu cầu lớp dự đoán mode nào tắt nhanh nhất.
- Tổ chức thảo luận ngắn: "Tách biến là mẹo đại số hay là cách nhìn phổ?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ bài toán Dirichlet chuẩn làm mẫu duy nhất trong lần đầu, rồi lặp đi lặp lại quy trình năm bước: đặt dạng tích, tách hằng số, giải bài toán không gian, giải ODE thời gian, ghép điều kiện đầu.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi so sánh tách biến của phương trình nhiệt với phương trình sóng, để thấy vì sao một bên cho suy giảm mũ còn bên kia cho dao động điều hòa theo thời gian.

## Tóm tắt dễ nhớ

Tách biến biến phương trình nhiệt thành một bài toán trị riêng theo không gian và một ODE theo thời gian. Mỗi mode không gian tắt theo hàm mũ, và nghiệm tổng quát là tổng của các mode với hệ số lấy từ khai triển Fourier của dữ liệu ban đầu.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thanh có biên cố định nhiệt độ
- Bài toán: Tìm nghiệm theo thời gian của nhiệt độ khi hai đầu thanh giữ ở nhiệt độ không đổi.
- Mô hình:
$$ u_t=\alpha^2 u_{xx},\qquad u(0,t)=u(L,t)=0. $$
- Giả thiết và giới hạn: Điều kiện biên thuần nhất và hình học một chiều.
- Diễn giải: Tách biến sinh ra các mode không gian sin và các hệ số suy giảm theo thời gian.

#### Sự tắt dần của các mode nhiệt
- Bài toán: Một profile đầu bất kỳ phân rã theo tổng các mode riêng.
- Mô hình:
$$
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\alpha^2 \lambda_n t}\phi_n(x).
$$
- Giả thiết và giới hạn: Cần khai triển theo hàm riêng thích hợp.
- Diễn giải: Mode cao suy giảm nhanh hơn do trị riêng lớn hơn.

### 2. Trực giác bổ sung và các kết nối

Tách biến cho phương trình nhiệt là nơi lý thuyết Sturm-Liouville quay lại một cách sống động. Mỗi mode riêng không gian tự tắt theo một tốc độ mũ riêng. Một bẫy phổ biến là xem nghiệm tách biến như kỹ thuật ngẫu nhiên; thật ra đó là biểu diễn phổ của bài toán.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
for t in [0.0, 0.02, 0.08]:
    u = np.sin(np.pi * x) * np.exp(-np.pi**2 * t) + 0.4 * np.sin(3 * np.pi * x) * np.exp(-9 * np.pi**2 * t)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Suy giam mode trong phuong trinh nhiet")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: separation of variables heat equation animation
- search: eigenmode decay heat equation
- search: Fourier sine series heat equation

### 5. Bài toán mẫu có bối cảnh thực

Đặt
$$ u(x,t)=X(x)T(t). $$
Khi đó
$$ \frac{T'}{\alpha^2 T}=\frac{X''}{X}=-\lambda. $$
Ta nhận được
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0, $$
nên
$$
X_n(x)=\sin\left(\frac{n\pi x}{L}\right),
\qquad
T_n(t)=e^{-\alpha^2 (n\pi/L)^2 t}.
$$

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo tách biến và viết nghiệm chuỗi mode.

**Bậc sau đại học.** Diễn giải bằng semigroup và toán tử sinh của tiến hóa nhiệt.
