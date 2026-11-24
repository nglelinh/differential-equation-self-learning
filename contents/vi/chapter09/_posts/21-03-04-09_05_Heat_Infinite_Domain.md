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

Điều gì xảy ra nếu thanh kim loại dài vô hạn trên cả trục thực $(-\infty, +\infty)$? Không còn biên hai đầu để tạo ra các tần số rời rạc $n\pi/L$ nữa—thay vào Chuỗi Fourier, ta dùng **Biến đổi Fourier** và thu được một công thức nghiệm tích phân tuyệt đẹp: **Tích chập giữa nhiệt độ ban đầu $f(x)$ với Nhân Nhiệt Gaussian (Heat Kernel)**!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương trình Nhiệt trên $\mathbb{R}$

1. **Giải nhanh trong miền tần số Fourier**:
   Áp dụng $\mathcal{F}_x$ vào $u_t = \alpha u_{xx}$ cho $\hat{u}_t(\omega, t) = -\alpha \omega^2 \hat{u}(\omega, t) \implies \hat{u}(\omega, t) = \hat{f}(\omega)\, e^{-\alpha\omega^2 t}$.
2. **Nhân Nhiệt Gaussian (Heat Kernel $\Phi(x, t)$)**:
   Biến đổi Fourier ngược của $e^{-\alpha\omega^2 t}$ chính là hàm chuông Gaussian:
   $$\Phi(x, t) = \frac{1}{\sqrt{4\pi\alpha t}}\exp\!\left(-\frac{x^2}{4\alpha t}\right) \qquad (t > 0).$$
3. **Công thức tích chập nghiệm**:
   $$u(x, t) = (\Phi(\cdot, t) * f)(x) = \frac{1}{\sqrt{4\pi\alpha t}}\int_{-\infty}^{\infty} f(y)\exp\!\left(-\frac{(x - y)^2}{4\alpha t}\right)dy.$$
   Nhiệt độ tại $(x, t)$ chính là **trung bình có trọng số Gaussian** của nhiệt độ ban đầu quanh $x$ với bán kính lan truyền $\sigma = \sqrt{2\alpha t}$!
4. **Tốc độ lan truyền vô hạn (Nghịch lý lý thuyết)**:
   Vì $\Phi(x, t) > 0$ tại mọi $x$ ngay cả với $t = 10^{-9}\text{ s}$, một nguồn nhiệt dương ở gốc tạo ra $u(x, t) > 0$ tức thì ở khoảng cách 1 triệu km (dù cực nhỏ đến mức không đo được!).

## Mục tiêu

Bài học này trình bày phương trình nhiệt trên toàn trục thực, nơi phương pháp tách biến theo chuỗi mode rời rạc không còn phù hợp. Sau bài học, sinh viên cần hiểu vì sao biến đổi Fourier là công cụ tự nhiên trên miền vô hạn, nắm công thức nghiệm tích chập với nhân nhiệt Gaussian và thấy được mỗi thành phần tần số suy giảm theo hệ số $$ e^{-\alpha^2\xi^2 t} $$, khiến các dao động tần số cao bị triệt tiêu nhanh hơn.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt trên đoạn hữu hạn, chuỗi Fourier phức và biến đổi Fourier ở mức nhập môn. Bài học này đưa lý thuyết biến đổi Fourier trực tiếp vào việc giải PDE trên miền không bị chặn.

## Dẫn nhập

Trên đoạn hữu hạn, điều kiện biên tạo ra một dãy mode riêng đếm được và bài toán được giải bằng chuỗi Fourier. Khi không còn biên tại $$ x=0 $$ hay $$ x=L $$, phổ tần số không còn rời rạc mà trở thành liên tục trên toàn trục thực. Do đó, biến đổi Fourier thay thế chuỗi Fourier một cách tự nhiên.

Ý tưởng cốt lõi vẫn không đổi: nghiệm vẫn được phân rã thành các mode điều hòa, chỉ khác là chỉ số tần số giờ đây biến thiên liên tục. Đây là bước chuyển quan trọng từ chuỗi Fourier sang biến đổi Fourier trong lý thuyết PDE.

### Khung giải thích (nên đọc chậm): Tính tay nghiệm bằng hàm sai số $\operatorname{erf}$ khi nửa thanh phải nóng $100^\circ\text{C}$ và nửa trái $0^\circ\text{C}$

Cho $u_t = \alpha u_{xx}$ trên $\mathbb{R}$ với $f(y) = 100$ khi $y > 0$ và $f(y) = 0$ khi $y < 0$.
1. Thay vào công thức tích chập (chỉ tích phân trên $y \in (0, +\infty)$):
   $$u(x, t) = \frac{100}{\sqrt{4\pi\alpha t}}\int_0^{\infty} \exp\!\left(-\frac{(x - y)^2}{4\alpha t}\right)dy.$$
2. Đổi biến $z = \frac{y - x}{\sqrt{4\alpha t}} \implies dy = \sqrt{4\alpha t}\,dz$ (khi $y = 0 \implies z = -\frac{x}{\sqrt{4\alpha t}}$):
   $$u(x, t) = \frac{100}{\sqrt{\pi}}\int_{-x/\sqrt{4\alpha t}}^{\infty} e^{-z^2}\,dz = \mathbf{50\left[1 + \operatorname{erf}\!\left(\frac{x}{\sqrt{4\alpha t}}\right)\right]}.$$
3. **Kiểm tra ngay 3 điểm đặc biệt**:
   - Tại điểm tiếp giáp $x = 0$ với mọi $t > 0$: $\operatorname{erf}(0) = 0 \implies u(0, t) = \mathbf{50^\circ\text{C}}$ (đúng trung bình cộng $0$ và $100$ ngay lập tức!).
   - Khi $x \to +\infty$: $\operatorname{erf}(+\infty) = 1 \implies u \to 100^\circ\text{C}$.
   - Khi $x \to -\infty$: $\operatorname{erf}(-\infty) = -1 \implies u \to 0^\circ\text{C}$.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu phân bố nhiệt ban đầu là một đỉnh cục bộ trên toàn trục thực, nhiệt sẽ lan tỏa đều ra cả hai phía mà không chịu phản xạ hay ràng buộc từ biên. Miền vô hạn vì thế là mô hình lý tưởng để quan sát quá trình khuếch tán tự do, nơi nghiệm là sự chồng chất của một phổ tần số liên tục.

### Cách nhìn hình ảnh

Trong miền tần số, mỗi dao động cơ bản có dạng $$ e^{i\xi x} $$. Theo thời gian, biên độ của mode này được nhân thêm thừa số suy giảm $$ e^{-\alpha^2\xi^2 t} $$. Khi $$ \lvert\xi\rvert $$ lớn, thừa số này giảm rất nhanh nên các chi tiết nhỏ, biến thiên gắt của dữ liệu ban đầu sớm biến mất. Trong miền không gian, quá trình đó biểu hiện qua việc đồ thị nhiệt độ ngày càng phẳng và trải rộng ra.

### Cách nhìn hình thức

Xét bài toán

$$ u_t=\alpha^2u_{xx},
\qquad
x\in\mathbb R,\ t>0, $$

với điều kiện ban đầu $$ u(x,0)=f(x) $$. Lấy biến đổi Fourier theo biến không gian $$ x $$:

$$
\hat u(\xi,t)=\int_{-\infty}^{\infty}u(x,t)e^{-i\xi x}\,dx.
$$

Vì phép lấy đạo hàm theo không gian chuyển thành phép nhân với $$ i\xi $$, ta thu được $$\partial_t\hat u(\xi,t)=-\alpha^2\xi^2\hat u(\xi,t)$$. Giải ODE theo thời gian này cho $$ \hat u(\xi,t)=\hat f(\xi)e^{-\alpha^2\xi^2 t} $$. Áp dụng biến đổi Fourier ngược, ta có

$$
u(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\xi)e^{-\alpha^2\xi^2 t}e^{i\xi x}\,d\xi.
$$

## Những ngộ nhận thường gặp

- "Miền vô hạn chỉ đơn giản là trường hợp miền hữu hạn khi cho $$ L\to\infty $$." Không hoàn toàn như vậy; khi lấy giới hạn này, phổ chuyển từ rời rạc sang liên tục.
- "Không có biên thì bài toán đơn giản hơn về mọi mặt." Không đúng; bài toán thuận tiện hơn cho biến đổi Fourier nhưng đòi hỏi trực giác mới về tích phân phổ và điều kiện ở vô cực.
- "Hàm Gaussian xuất hiện chỉ nhờ sự trùng hợp trong tính toán." Sai; đây là hạt nhân tự nhiên của quá trình khuếch tán tự do.
- "Tần số thấp và tần số cao suy giảm với tốc độ như nhau." Không đúng; tần số càng cao càng bị triệt tiêu nhanh theo bậc hai của $$ \xi $$.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại biến đổi Fourier

Củng cố khái niệm phổ liên tục và các tính chất cơ bản của biến đổi Fourier.

### Bước 2: Chuyển PDE thành ODE trong miền tần số

Đây là bước biến đổi kỹ thuật trọng tâm của bài.

### Bước 3: Biến đổi ngược và nhận diện nhân nhiệt

Đưa nghiệm từ miền tần số trở về miền không gian để thấy sự xuất hiện của hàm Gaussian.

### Bước 4: Diễn giải hiệu ứng làm mượt qua phổ

Liên hệ sự suy giảm nhanh ở tần số cao với độ trơn của nghiệm theo thời gian.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao miền vô hạn dẫn đến phổ liên tục hay không.
- Sinh viên có hiểu vì sao đạo hàm theo không gian chuyển thành phép nhân trong miền tần số hay không.
- Sinh viên có thấy mối liên hệ giữa thừa số $$ e^{-\alpha^2\xi^2 t} $$ và sự triệt tiêu các thành phần tần số cao hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Công thức nghiệm trong miền phổ

Với điều kiện ban đầu $$ f $$, ta có $$ \hat u(\xi,t)=\hat f(\xi)e^{-\alpha^2\xi^2 t} $$. Biểu diễn trong miền tần số đặc biệt gọn: mỗi thành phần tần số chỉ suy giảm độc lập theo một thừa số mũ.

### Ví dụ 2: Nhân nhiệt Gaussian

Áp dụng định lý tích chập, nghiệm có thể viết dưới dạng

$$ u(x,t)=\int_{-\infty}^{\infty}f(y)G(x-y,t)\,dy, $$

trong đó

$$
G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right).
$$

Hàm $$ G(x,t) $$ được gọi là nhân nhiệt (heat kernel). Nhân nhiệt luôn dương, có tích phân toàn miền bằng 1 và đóng vai trò như một hàm trọng số lấy trung bình.

### Ví dụ 3: Dữ liệu ban đầu dạng xung chữ nhật

Nếu $$ f(x)=\mathbf 1_{\lvert x\rvert<a}(x) $$, nghiệm là tích phân của hàm Gaussian trên đoạn $$ [-a,a] $$ và có thể biểu diễn qua hàm lỗi (error function). Ví dụ này cho thấy một bước nhảy sắc nét ban đầu sẽ được làm trơn ngay lập tức khi $$ t>0 $$.

### Ví dụ 4: Dữ liệu ban đầu dao động mạnh

Nếu dữ liệu ban đầu chứa nhiều thành phần tần số cao, trong miền Fourier các thành phần này bị nhân với $$ e^{-\alpha^2\xi^2 t} $$ (với $$ \lvert\xi\rvert $$ lớn) nên tắt rất nhanh. Đây là lời giải thích theo ngôn ngữ phổ cho hiệu ứng làm mượt của phương trình nhiệt.

## Câu hỏi khái niệm

1. Vì sao trên miền vô hạn ta sử dụng phổ liên tục thay vì các mode rời rạc đếm được?
2. Yếu tố nào trong biểu thức $$ e^{-\alpha^2\xi^2 t} $$ giải thích cơ chế làm mượt dữ liệu của phương trình nhiệt?
3. Vì sao nhân nhiệt Gaussian có thể được hiểu như một phép lấy trung bình có trọng số?

## Bài toán ứng dụng

1. Một xung nhiệt cục bộ được tạo ra trên một thanh rất dài. Vì sao sau một thời gian ngắn, phân bố nhiệt độ có dạng gần với đường cong Gaussian?
2. Trong xử lý ảnh, vì sao bộ lọc làm mờ Gaussian có liên hệ mật thiết với phương trình nhiệt?
3. Trong lý thuyết xác suất, vì sao phân bố Gaussian xuất hiện tự nhiên khi tổng hợp tác động lan tỏa của nhiều nhiễu nhỏ độc lập?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Khi không còn biên hữu hạn, các mode riêng sẽ được phân bố như thế nào?"
- Đối chiếu một bài toán trên đoạn hữu hạn với một bài toán trên toàn trục thực để làm nổi bật bước chuyển từ phổ rời rạc sang phổ liên tục.
- Đặt câu hỏi: "Thành phần tần số nào tồn tại lâu hơn dưới sự tiến hóa của phương trình nhiệt?"
- Minh họa quá trình một xung chữ nhật được làm trơn dần thành dạng gần Gaussian.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào hai công thức cốt lõi: nghiệm trong miền phổ $$ \hat u=\hat f e^{-\alpha^2\xi^2 t} $$ và nghiệm tích chập với nhân Gaussian. Khi đã quen với hai công thức này, phần diễn giải chi tiết sẽ dễ tiếp thu hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự tính biến đổi Fourier ngược của $$ e^{-\alpha^2\xi^2 t} $$ để suy ra nhân nhiệt, hoặc tìm hiểu mối liên hệ với chuyển động Brown trong lý thuyết xác suất.

## Tóm tắt dễ nhớ

Trên miền vô hạn, phương trình nhiệt được giải tự nhiên bằng biến đổi Fourier. Mỗi tần số suy giảm theo thừa số $$ e^{-\alpha^2\xi^2 t} $$ nên các tần số cao tắt nhanh hơn. Trong miền không gian, nghiệm là tích chập của dữ liệu ban đầu với nhân nhiệt Gaussian, qua đó làm mượt phân bố nhiệt theo thời gian.

## Video tham khảo

- Xem trước: [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, tiếng Anh. Trình bày cách dùng biến đổi Fourier để giải phương trình nhiệt trên toàn trục thực.
- [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Minh họa cơ chế suy giảm theo tần số, đối chiếu giữa miền hữu hạn và miền vô hạn.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, tiếng Anh. Giới thiệu trực quan biến đổi Fourier như phép đổi hệ tọa độ sang miền tần số.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khuếch tán trên toàn trục thực
- Bài toán: Chất hòa tan hoặc nhiệt lan truyền trên miền vô hạn, không có biên hữu hạn để dùng chuỗi Fourier.
- Mô hình:
$$ u_t=\alpha^2 u_{xx},\qquad x\in \mathbb{R}. $$
- Giả thiết và giới hạn: Miền vô hạn và dữ liệu suy giảm đủ nhanh ở vô cực.
- Diễn giải: Phổ tần số liên tục thay thế cho phổ rời rạc.

#### Phân bố nhiệt từ một nguồn cục bộ
- Bài toán: Ban đầu nhiệt tập trung trong một vùng hẹp rồi khuếch tán dần ra xung quanh.
- Mô hình: Sử dụng biến đổi Fourier hoặc tích chập với nhân nhiệt.
- Giả thiết và giới hạn: Không có biên phản xạ hay nguồn nhiệt ngoài.
- Diễn giải: Đồ thị nhiệt độ ngày càng trải rộng và hạ thấp đỉnh, trong khi tổng nhiệt lượng được bảo toàn.

### 2. Trực giác bổ sung và các kết nối

Trên miền vô hạn, cơ sở mode rời rạc sin-cos không còn phù hợp và cần chuyển sang phổ liên tục. Thay vì giữ trực giác của chuỗi Fourier, cần tiếp cận bài toán bằng biến đổi Fourier và nhân nhiệt.

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

Với điều kiện ban đầu là hàm delta Dirac tại gốc tọa độ, nghiệm của phương trình nhiệt trên $$ \mathbb{R} $$ là
$$
G(x,t)=\frac{1}{\sqrt{4\pi \alpha^2 t}}\exp\left(-\frac{x^2}{4\alpha^2 t}\right).
$$
Đây là dạng Gaussian cơ bản mô tả sự khuếch tán dần của một xung nhiệt điểm theo thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu nguồn gốc của hàm Gaussian và cách phân bố nhiệt trải rộng theo thời gian.

**Bậc sau đại học.** Tìm hiểu nửa nhóm nhiệt (heat semigroup) trên $$ \mathbb{R}^n $$ và vai trò của biến đổi Fourier trong phân tích nghiệm.
