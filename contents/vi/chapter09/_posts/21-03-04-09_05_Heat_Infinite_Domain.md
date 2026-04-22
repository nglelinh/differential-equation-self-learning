---
layout: post
title: "Phương Trình Nhiệt Trên Miền Vô Hạn"
chapter: '09'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 05 Heat Infinite Domain]({{ site.imgurl }}/chapter_img/chapter09/05_heat_infinite_domain.svg)

## Mục tiêu

Bài học này trình bày phương trình nhiệt trên toàn trục thực, nơi tách biến theo chuỗi mode rời rạc không còn là công cụ tự nhiên nhất. Sau bài học, sinh viên cần hiểu vì sao biến đổi Fourier là lựa chọn đúng trên miền vô hạn, biết công thức nghiệm dưới dạng nhân nhiệt Gaussian, và thấy được mỗi tần số suy giảm theo hệ số $$ e^{-\alpha^2\xi^2 t} $$ nên các dao động cao tần bị dập tắt nhanh hơn.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt trên đoạn hữu hạn, chuỗi Fourier phức, và biến đổi Fourier ở mức giới thiệu. Bài này là nơi lý thuyết Fourier trên miền vô hạn thật sự đi vào PDE.

## Dẫn nhập

Trên đoạn hữu hạn, các mode riêng được đếm bằng số nguyên và bài toán được giải bằng chuỗi Fourier. Nhưng khi không còn biên, không còn điều kiện ở $$ x=0 $$ hay $$ x=L $$, thì tập mode phù hợp không còn là một dãy rời rạc nữa. Toàn trục thực đòi hỏi một phổ liên tục, và vì thế biến đổi Fourier trở thành công cụ tự nhiên.

Điểm đẹp của bài này là cùng một ý tưởng cũ vẫn sống tiếp: ta vẫn phân rã nghiệm thành các mode điều hòa, chỉ khác ở chỗ bây giờ tần số chạy liên tục. Đây là bước chuyển rất quan trọng từ Fourier series sang Fourier transform trong bối cảnh PDE.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu dữ liệu ban đầu là một đỉnh nhiệt cục bộ trên toàn trục, ta mong nhiệt lan ra cả hai phía mà không bị biên phản xạ hay chặn lại. Miền vô hạn vì thế là môi trường lý tưởng để quan sát khuếch tán "tự do". Nghiệm sẽ không còn là tổng của vài mode đếm được, mà là tổ hợp của vô số tần số liên tục.

### Cách nhìn hình ảnh

Trong miền tần số, mỗi dao động dạng $$ e^{i\xi x} $$ là một mode cơ bản. Theo thời gian, mode này bị nhân thêm bởi $$ e^{-\alpha^2\xi^2 t} $$. Vì $$ \xi^2 $$ lớn thì suy giảm nhanh, các chi tiết nhỏ của dữ liệu ban đầu biến mất trước. Trong miền không gian, điều đó xuất hiện như sự làm mượt và trải rộng của đồ thị.

### Cách nhìn hình thức

Xét bài toán

$$ u_t=\alpha^2u_{xx},
\qquad
x\in\mathbb R,\ t>0, $$

với điều kiện đầu $$ u(x,0)=f(x) $$. Lấy biến đổi Fourier theo $$ x $$: $$
\hat u(\xi,t)=\int_{-\infty}^{\infty}u(x,t)e^{-i\xi x}\,dx.
$$

Vì đạo hàm theo không gian trở thành phép nhân bởi $$ i\xi $$, ta có $$\partial_t\hat u(\xi,t)=-\alpha^2\xi^2\hat u(\xi,t)$$. Đây là ODE theo thời gian, nên $$ \hat u(\xi,t)=\hat f(\xi)e^{-\alpha^2\xi^2 t} $$. Lấy biến đổi ngược, ta được

$$
u(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\xi)e^{-\alpha^2\xi^2 t}e^{i\xi x}\,d\xi.
$$

## Những ngộ nhận thường gặp

- "Miền vô hạn chỉ là bản sao của miền hữu hạn khi cho

$$ L\to\infty. $$

" Không hẳn; phổ chuyển từ rời rạc sang liên tục.
- "Nếu không có biên thì bài toán đơn giản hơn theo mọi nghĩa." Không đúng; nó đẹp hơn theo Fourier transform nhưng cũng đòi hỏi trực giác mới.
- "Gaussian xuất hiện chỉ vì tính toán may mắn." Sai. Nó là hạt nhân tự nhiên của khuếch tán tự do.
- "Tần số thấp và cao đều suy giảm giống nhau." Không đúng; tần số càng cao càng bị triệt tiêu nhanh.

## Tiến trình học tập đề xuất

### Bước 1: Nhắc lại biến đổi Fourier

Sinh viên cần nhớ vai trò của phổ liên tục.

### Bước 2: Biến PDE thành ODE trong miền tần số

Đây là bước kỹ thuật quan trọng nhất.

### Bước 3: Lấy biến đổi ngược và nhận diện nhân nhiệt

Đây là lúc Gaussian xuất hiện.

### Bước 4: Diễn giải tính làm mượt bằng ngôn ngữ phổ

Đây là lợi ích khái niệm lớn nhất của bài.

### Các checkpoint

- Sinh viên có giải thích được vì sao miền vô hạn dẫn đến phổ liên tục hay không.
- Sinh viên có hiểu vì sao đạo hàm theo không gian trở thành phép nhân trong miền tần số hay không.
- Sinh viên có thấy mối liên hệ giữa

$$ e^{-\alpha^2\xi^2 t} $$

và sự triệt tiêu tần số cao hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Công thức phổ của nghiệm

Với dữ liệu ban đầu $$ f $$, ta có $$ \hat u(\xi,t)=\hat f(\xi)e^{-\alpha^2\xi^2 t} $$. Ví dụ này cho thấy nghiệm trong miền tần số cực kỳ đơn giản: mỗi tần số chỉ suy giảm theo một hệ số mũ.

### Ví dụ 2: Nhân nhiệt Gaussian

Ta có thể viết nghiệm dưới dạng chập:

$$ u(x,t)=\int_{-\infty}^{\infty}f(y)G(x-y,t)\,dy, $$

trong đó

$$
G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right).
$$

Đây là nhân nhiệt. Nó dương, có tổng khối lượng bằng 1, và làm vai trò của một hạt nhân trung bình có trọng số.

### Ví dụ 3: Dữ liệu xung hình chữ nhật

Nếu $$ f(x)=\mathbf 1_{\lvert x\rvert<a}(x) $$, thì nghiệm là một tích phân của Gaussian trên đoạn $$ [-a,a] $$, và có thể viết bằng hàm lỗi. Ví dụ này rất quan trọng vì nó cho thấy một biên sắc ban đầu sẽ được làm trơn ngay lập tức.

### Ví dụ 4: Dữ liệu rất nhấp nhô

Nếu dữ liệu ban đầu chứa nhiều thành phần cao tần, thì trong miền Fourier các thành phần này bị nhân bởi $$ e^{-\alpha^2\xi^2 t} $$ với $$ \xi $$ lớn, nên biến mất rất nhanh. Đây là cách giải thích phổ cho hiện tượng làm mượt mà không cần nhìn trực tiếp trong miền không gian.

## Câu hỏi khái niệm

1. Vì sao trên miền vô hạn ta nên nghĩ theo phổ liên tục thay vì các mode đếm được?
2. Điều gì trong công thức $$ e^{-\alpha^2\xi^2 t} $$ giải thích việc nhiệt làm mượt dữ liệu?
3. Vì sao nhân nhiệt Gaussian có thể được xem là một phép trung bình có trọng số?

## Bài toán ứng dụng

1. Một xung nhiệt cục bộ được đặt trên một thanh rất dài. Vì sao sau thời gian ngắn, hồ sơ nhiệt độ có dạng gần Gaussian?
2. Trong xử lý ảnh, vì sao lọc Gaussian lại có liên hệ chặt với phương trình nhiệt?
3. Trong xác suất, vì sao Gaussian xuất hiện tự nhiên khi mô tả sự lan tỏa của nhiều nhiễu nhỏ độc lập?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Khi không còn biên, mode riêng sẽ được đếm thế nào?"
- Cho sinh viên so sánh một bài toán trên đoạn hữu hạn với một bài toán trên toàn trục để thấy sự chuyển từ phổ rời rạc sang liên tục.
- Hỏi cả lớp: "Tần số nào sống lâu hơn dưới tác động của phương trình nhiệt?"
- Vẽ hoặc mô tả cách một xung hình chữ nhật được làm trơn dần thành dạng Gaussian.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên nhấn mạnh hai công thức cốt lõi: nghiệm phổ $$ \hat u=\hat f e^{-\alpha^2\xi^2 t} $$ và nghiệm chập với Gaussian. Khi hai công thức này đã quen, phần giải thích sâu hơn sẽ dễ tiếp nhận hơn.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi tự suy ra nhân nhiệt bằng cách lấy biến đổi ngược của $$ e^{-\alpha^2\xi^2 t} $$, hoặc liên hệ với chuyển động Brown và xác suất.

## Tóm tắt dễ nhớ

Trên miền vô hạn, phương trình nhiệt được giải tự nhiên bằng biến đổi Fourier. Mỗi tần số suy giảm theo $$ e^{-\alpha^2\xi^2 t} $$, nên tần số cao chết nhanh. Nghiệm trong miền không gian là chập của dữ liệu ban đầu với một Gaussian, vì thế nhiệt luôn có xu hướng làm mượt.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khuếch tán trên toàn trục số
- Bài toán: Chất lan truyền trên miền vô hạn, không còn biên hữu hạn để dùng chuỗi Fourier.
- Mô hình:
$$ u_t=\alpha^2 u_{xx},\qquad x\in \mathbb{R}. $$
- Giả thiết và giới hạn: Miền vô hạn và dữ liệu đủ giảm ở vô cực.
- Diễn giải: Phổ liên tục thay thế phổ rời rạc.

#### Nhiệt độ từ một đám nhiệt cục bộ
- Bài toán: Ban đầu nhiệt chỉ tập trung trong một vùng nhỏ rồi lan dần ra.
- Mô hình: Dùng biến đổi Fourier hoặc heat kernel.
- Giả thiết và giới hạn: Không có biên phản xạ hay điều kiện ngoại lực.
- Diễn giải: Profile ngày càng bè rộng và thấp đi nhưng tổng khối lượng nhiệt bảo toàn.

### 2. Trực giác bổ sung và các kết nối

Miền vô hạn phá vỡ cơ sở mode rời rạc sin-cos và đòi hỏi phổ liên tục. Một bẫy phổ biến là cố giữ nguyên trực giác chuỗi Fourier trên miền vô hạn; đúng hơn phải nghĩ theo biến đổi Fourier và hạt nhân nhiệt.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 800)
for t in [0.05, 0.2, 0.8]:
    G = (1 / np.sqrt(4 * np.pi * t)) * np.exp(-x**2 / (4 * t))
    plt.plot(x, G, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("G(x,t)")
plt.title("Heat kernel tren mien vo han")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: heat equation infinite domain Gaussian kernel
- search: diffusion on whole line animation
- search: Fourier transform heat equation solution

### 5. Bài toán mẫu có bối cảnh thực

Với dữ kiện đầu là delta tại gốc, nghiệm của phương trình nhiệt trên $$ \mathbb{R} $$ là
$$
G(x,t)=\frac{1}{\sqrt{4\pi \alpha^2 t}}\exp\left(-\frac{x^2}{4\alpha^2 t}\right).
$$
Đó là profile Gaussian cơ bản mô tả một xung nhiệt loãng dần theo thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu vì sao Gaussian xuất hiện và cách profile trải rộng theo thời gian.

**Bậc sau đại học.** Nhấn mạnh semigroup nhiệt trên $$ \mathbb{R}^n $$ và vai trò của biến đổi Fourier.
