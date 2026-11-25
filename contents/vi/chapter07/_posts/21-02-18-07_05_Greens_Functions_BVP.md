---
layout: post
title: "07-05 Hàm Green cho Bài toán Biên"
chapter: '07'
order: 5
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

Hãy hình dung bạn ấn nhẹ ngón tay vào một điểm duy nhất $\xi$ trên một cây cầu treo và ghi lại hình dáng độ võng $G(x, \xi)$ dọc toàn bộ cây cầu. Nhờ tính tuyến tính, khi có hàng trăm chiếc xe phân bố thành tải trọng bất kỳ $f(x)$ chạy qua, tổng độ võng chỉ đơn giản là **tích phân chồng chất** $y(x) = \int_a^b G(x, \xi) f(\xi)\,d\xi$! Hàm $G(x, \xi)$ kỳ diệu đó chính là **Hàm Green**—toán tử nghịch đảo $L^{-1}$ của toán tử vi phân!

## Kiến thức cần nhớ: Bốn tính chất đặc trưng của Hàm Green $G(x, \xi)$

1. **Nghiệm của phương trình với nguồn xung Dirac**:
   $L_x[G(x, \xi)] = \delta(x - \xi)$ kèm điều kiện biên thuần nhất tại $x = a$ và $x = b$.
2. **Bốn điều kiện xây dựng $G(x, \xi)$ (chia hai nhánh $x < \xi$ và $x > \xi$)**:
   - (i) Thỏa $L[G] = 0$ ở hai bên $x \neq \xi$;
   - (ii) Thỏa biên trái ở $x < \xi$ (tỷ lệ với $y_1(x)$) và biên phải ở $x > \xi$ (tỷ lệ với $y_2(x)$);
   - (iii) **Liên tục** tại $x = \xi$: $G(\xi^+, \xi) = G(\xi^-, \xi)$;
   - (iv) **Bước nhảy đạo hàm** tại $x = \xi$: $G_x(\xi^+, \xi) - G_x(\xi^-, \xi) = -\frac{1}{p(\xi)}$ (cho dạng $-(py')' + qy = \delta$).
3. **Công thức đóng qua Wronskian**:
   $G(x, \xi) = \frac{y_1(\min(x,\xi))\, y_2(\max(x,\xi))}{-p(\xi)\, W(y_1, y_2)(\xi)}$.
4. **Tính đối xứng vật lý (Định lý tương hỗ Maxwell–Betti)**:
   Với toán tử tự liên hợp, $G(x, \xi) = G(\xi, x)$: độ võng tại $x$ do lực đặt ở $\xi$ bằng đúng độ võng tại $\xi$ do lực đặt ở $x$!

## Mục tiêu

Bài học này giới thiệu hàm Green như một công cụ tổng quát và hiệu quả để giải bài toán giá trị biên tuyến tính không thuần nhất. Sau bài học, sinh viên cần hiểu hàm Green là đáp ứng của hệ đối với nguồn điểm, biết đọc và áp dụng công thức tích phân nghiệm, nắm được tính liên tục cùng bước nhảy đạo hàm tại vị trí nguồn và nhìn nhận hàm Green như hạt nhân của toán tử nghịch đảo.

## Kiến thức nền

Sinh viên nên nắm vững BVP tuyến tính, nguyên lý chồng chất và trực giác cơ bản về hàm delta Dirac. Kiến thức về hàm riêng và lý thuyết Sturm–Liouville cũng rất hữu ích vì hàm Green có thể biểu diễn dưới dạng tổng chuỗi theo các chế độ riêng.

## Dẫn nhập

![Hàm Green như đáp ứng xung của bài toán biên]({{ site.imgurl }}/chapter_img/chapter07/05_greens_functions_bvp.svg)

Nếu biết một hệ tuyến tính phản ứng ra sao trước một nguồn tập trung tại một điểm duy nhất, ta có thể chồng chất các đáp ứng điểm đó để tìm nghiệm cho bất kỳ nguồn phân bố nào. Đó chính là tư tưởng cốt lõi của **hàm Green**, chuyển việc phải giải lại bài toán cho từng hàm nguồn riêng biệt sang việc xác định một đáp ứng cơ bản duy nhất rồi tích phân.

Về mặt vật lý và kỹ thuật, hàm Green tương tự đáp ứng xung của hệ thống; về mặt toán học, nó là hạt nhân tích phân (kernel) của toán tử nghịch đảo.

### Giải thích: Xây dựng làm từng bước Hàm Green cho $-y'' = f(x),\; y(0) = y(1) = 0$ và kiểm tra lại độ võng dầm

1. **Tìm hai nghiệm thuần nhất ($y'' = 0$) thỏa từng đầu biên**:
   - Biên trái $y_1(0) = 0 \implies y_1(x) = x$.
   - Biên phải $y_2(1) = 0 \implies y_2(x) = 1 - x$.
2. **Tính Wronskian**: $W(y_1, y_2) = x(-1) - (1-x)(1) = -1$. Với $p(x) = 1$, ta có $-p W = -1 \cdot (-1) = +1$!
3. **Viết ngay Hàm Green**:
   $$G(x, \xi) = \begin{cases} x(1 - \xi), & 0 \le x \le \xi, \\ \xi(1 - x), & \xi \le x \le 1. \end{cases}$$
   Kiểm tra bước nhảy đạo hàm tại $x = \xi$: $G_x(\xi^+, \xi) - G_x(\xi^-, \xi) = (-\xi) - (1 - \xi) = \mathbf{-1} = -\frac{1}{p(\xi)}$ (khớp!).
4. **Áp dụng tìm nghiệm cho $f(x) = 1$** ($-y'' = 1$):
   $$y(x) = \int_0^x \xi(1 - x)\,d\xi + \int_x^1 x(1 - \xi)\,d\xi = (1 - x)\frac{x^2}{2} + x\frac{(1 - x)^2}{2} = \mathbf{\frac{x(1 - x)}{2}}.$$
   Kiểm tra: $-y'' = -\left(-1\right) = 1$ và $y(0) = y(1) = 0$ — khớp 100%!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy xét một sợi dây đàn hồi hoặc một thanh dẫn nhiệt. Khi tác động một lực tập trung hoặc đặt một nguồn nhiệt điểm tại vị trí $$ \xi $$, toàn bộ hệ phản ứng theo một hình dạng xác định được ghi lại bởi $$ G(x,\xi) $$. Với nguồn phân bố liên tục $$ f(\xi) $$, ta chỉ cần cộng dồn (tích phân) ảnh hưởng của mọi nguồn điểm dọc theo miền.

### Cách nhìn hình ảnh

Khi cố định vị trí nguồn $$ \xi $$, hàm $$ G(x,\xi) $$ theo biến $$ x $$ gồm hai nhánh ghép lại tại $$ x=\xi $$: một nhánh bên trái và một nhánh bên phải điểm nguồn. Hàm $$ G $$ liên tục tại $$ x=\xi $$, nhưng đạo hàm bậc nhất của nó có một bước nhảy xác định — tạo ra điểm gấp khúc phản ánh tác động tập trung của nguồn điểm.

### Cách nhìn hình thức

Với toán tử vi phân tuyến tính $$ L $$ kèm điều kiện biên thuần nhất, hàm Green $$ G(x,\xi) $$ thỏa mãn $$ L G(x,\xi)=\delta(x-\xi) $$ cùng các điều kiện biên theo biến $$ x $$. Khi đó nghiệm của bài toán không thuần nhất $$ L y=f $$ được biểu diễn dưới dạng tích phân:

$$ y(x)=\int_a^b G(x,\xi)f(\xi)\,d\xi. $$

Nếu toán tử $$ L $$ tự liên hợp cùng điều kiện biên thích hợp, hàm Green có tính đối xứng:

$$ G(x,\xi)=G(\xi,x). $$

## Những ngộ nhận thường gặp

- "Hàm Green chỉ là một thủ thuật tích phân." Sai. Nó là biểu diễn hạt nhân của toán tử nghịch đảo $$ L^{-1} $$.
- "Khái niệm nguồn điểm quá trừu tượng nên có thể bỏ qua." Không nên; trực giác đáp ứng xung là chìa khóa để hiểu bản chất hàm Green.
- "Hàm Green phải khả vi trơn tại mọi điểm." Sai. Chính bước nhảy của đạo hàm tại $$ x=\xi $$ mới thể hiện nguồn delta Dirac.
- "Hàm Green chỉ hữu ích để tính toán nghiệm số." Sai. Nó còn cho biết trực tiếp cơ chế lan truyền ảnh hưởng giữa các điểm trong miền.

## Tiến trình học tập đề xuất

### Bước 1: Ôn tập nguyên lý chồng chất

Khẳng định tính tuyến tính là nền tảng cho phép tổng hợp nghiệm từ các đáp ứng điểm.

### Bước 2: Hiểu mô hình nguồn điểm

Tiếp cận hàm delta Dirac như giới hạn lý tưởng hóa của một nguồn tập trung đơn vị.

### Bước 3: Xây dựng hàm Green hai nhánh

Luyện quy trình ghép hai nghiệm thuần nhất thỏa biên trái, biên phải, tính liên tục và điều kiện bước nhảy đạo hàm.

### Bước 4: Áp dụng công thức tích phân nghiệm

Diễn giải tích phân $$ \int_a^b G(x,\xi)f(\xi)\,d\xi $$ như sự chồng chất liên tục các đáp ứng xung.

### Bước 5: Liên hệ với tính đối xứng và tự liên hợp

Kết nối tính đối xứng $$ G(x,\xi)=G(\xi,x) $$ với cấu trúc toán tử tự liên hợp Sturm–Liouville.

### Các điểm kiểm tra

- Sinh viên có diễn đạt được ý nghĩa của hàm Green bằng lời mà không cần dùng công thức hay không.
- Sinh viên có nắm vững điều kiện liên tục và điều kiện bước nhảy đạo hàm tại $$ x=\xi $$ hay không.
- Sinh viên có hiểu hàm Green là biểu diễn nghịch đảo của toán tử vi phân hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm Green cho bài toán Dirichlet cơ bản

Xét bài toán

$$
-y''=f(x),
\qquad
0<x<1,
\qquad
y(0)=0,
\qquad
y(1)=0.
$$

Hàm Green thỏa mãn $$ -G_{xx}(x,\xi)=\delta(x-\xi) $$ và các điều kiện biên

$$ G(0,\xi)=0,
\qquad
G(1,\xi)=0. $$

Tìm $$ G $$ dưới dạng ghép hai nhánh tuyến tính:

$$
G(x,\xi)=
\begin{cases}
Ax+B, & 0\le x<\xi,\\
Cx+D, & \xi<x\le 1.
\end{cases}
$$

Áp dụng hai điều kiện biên, tính liên tục tại $$ x=\xi $$ và điều kiện bước nhảy đạo hàm $$ G_x(\xi^+,\xi)-G_x(\xi^-,\xi)=-1 $$, ta thu được:

$$
G(x,\xi)=
\begin{cases}
x(1-\xi), & x\le \xi,\\
\xi(1-x), & x\ge \xi.
\end{cases}
$$

Đây là ví dụ chuẩn mực nhất để nắm phương pháp xây dựng hàm Green một chiều.

### Ví dụ 2: Tính nghiệm bằng hàm Green

Sử dụng hàm Green vừa tìm được, nghiệm của bài toán là

$$ y(x)=\int_0^1 G(x,\xi)f(\xi)\,d\xi. $$

Với hàm nguồn hằng $$ f(\xi)=1 $$, ta tách tích phân tại $$ \xi=x $$:

$$
y(x)=\int_0^x \xi(1-x)\,d\xi+\int_x^1 x(1-\xi)\,d\xi
=\frac{x(1-x)}{2}.
$$

Ví dụ này cho thấy hàm Green sinh ra trực tiếp nghiệm tường minh cho mọi vế phải $$ f $$.

### Ví dụ 3: Ý nghĩa của bước nhảy đạo hàm

Trong Ví dụ 1, hàm $$ G(x,\xi) $$ liên tục tại $$ x=\xi $$ nhưng đạo hàm theo $$ x $$ nhảy một lượng đúng bằng $$ -1 $$ khi đi qua $$ x=\xi $$. Bước nhảy này phản ánh trực tiếp sự có mặt của nguồn xung $$ \delta(x-\xi) $$ (tương tự lực tập trung làm đổi đột ngột độ dốc dây căng).

### Ví dụ 4: Tính đối xứng

Kiểm tra trực tiếp công thức ở Ví dụ 1 cho thấy $$ G(x,\xi)=G(\xi,x) $$. Tính đối xứng này bắt nguồn từ tính tự liên hợp của toán tử và thể hiện nguyên lý tương hỗ vật lý: ảnh hưởng tại điểm $$ x $$ do nguồn đặt tại $$ \xi $$ bằng ảnh hưởng tại điểm $$ \xi $$ do nguồn đặt tại $$ x $$.

## Câu hỏi khái niệm

1. Vì sao biết đáp ứng của hệ tuyến tính với một nguồn điểm lại đủ để tìm nghiệm cho nguồn phân bố bất kỳ?
2. Vì sao hàm Green của bài toán cấp hai liên tục tại điểm nguồn nhưng đạo hàm bậc nhất lại có bước nhảy?
3. Tính đối xứng $$ G(x,\xi)=G(\xi,x) $$ phản ánh tính chất gì của toán tử vi phân và điều kiện biên?

## Bài toán ứng dụng

1. Trong bài toán dẫn nhiệt trạng thái dừng, vì sao hàm Green là công cụ tự nhiên khi xét một nguồn nhiệt đặt tập trung tại một điểm?
2. Trong cơ học kết cấu, vì sao việc biết độ võng của thanh hay dây dưới một lực điểm giúp tính biến dạng dưới tải phân bố tổng quát?
3. Trong điện tĩnh học, vì sao hàm Green được xem là điện thế sinh bởi một điện tích điểm đơn vị trong miền có biên nối đất?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: nếu biết phản ứng của hệ trước một tác động tập trung tại một điểm, làm thế nào suy ra phản ứng trước một tải phân bố liên tục?
- Vẽ đồ thị hai nhánh ghép tại $$ x=\xi $$ để làm nổi bật điểm liên tục và điểm gấp khúc đạo hàm.
- Cho sinh viên làm việc nhóm tự dựng hàm Green cho bài toán Dirichlet đơn giản trước khi đối chiếu công thức cuối cùng.
- Yêu cầu sinh viên diễn giải công thức tích phân nghiệm bằng ngôn ngữ chồng chất ảnh hưởng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung chắc vào ví dụ một chiều cơ bản và ghi nhớ ba điều kiện cấu tạo: thỏa điều kiện biên thuần nhất, liên tục tại $$ x=\xi $$ và có bước nhảy đạo hàm tương ứng với hàm delta.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên liên hệ hàm Green với khai triển song tuyến theo hệ hàm riêng Sturm–Liouville, hoặc đối chiếu hàm Green với các phần tử của ma trận nghịch đảo trong đại số tuyến tính.

## Tóm tắt dễ nhớ

Hàm Green là đáp ứng của BVP tuyến tính đối với một nguồn điểm đơn vị, đóng vai trò hạt nhân tích phân của toán tử nghịch đảo. Trong bài toán cấp hai một chiều, hàm Green thỏa điều kiện biên thuần nhất, liên tục tại vị trí nguồn và có bước nhảy xác định ở đạo hàm bậc nhất.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Độ võng của dây hoặc thanh dưới tải phân bố
- Bài toán: Tính biến dạng của hệ dưới nhiều dạng tải phân bố khác nhau mà không cần giải lại phương trình vi phân mỗi lần.
- Mô hình:
$$ Ly=f,\qquad y(x)=\int_a^b G(x,\xi)f(\xi)\,d\xi. $$
- Giả thiết và giới hạn: Hệ tuyến tính, điều kiện biên cố định và toán tử khả nghịch (hàm Green tồn tại).
- Diễn giải: Hàm Green biểu diễn đáp ứng với lực điểm, còn tích phân thực hiện chồng chất các đáp ứng điểm.

#### Điện thế do điện tích phân bố trong miền một chiều
- Bài toán: Xác định điện thế do mật độ điện tích phân bố trên đoạn có hai đầu nối đất.
- Mô hình:
$$ -u''=\rho(x),\qquad u(0)=u(L)=0. $$
- Giả thiết và giới hạn: Mô hình một chiều hóa để làm rõ cơ chế toán học.
- Diễn giải: Hàm Green đo mức độ ảnh hưởng từ mỗi vị trí điện tích nguồn tới mọi điểm quan sát.

### 2. Trực giác bổ sung và các kết nối

Hàm Green chuyển khái niệm trừu tượng "toán tử nghịch đảo" thành một "hạt nhân tích phân" cụ thể, tạo cầu nối chặt chẽ giữa ODE, PDE và lý thuyết toán tử. Không nên xem hàm Green chỉ là một công thức ghép nhánh đại số: tính liên tục và bước nhảy đạo hàm chính là dấu ấn trực tiếp của nguồn điểm delta.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
xi = 0.35
G = np.where(x <= xi, x * (1 - xi), xi * (1 - x))

plt.plot(x, G, label=f"G(x,{xi})")
plt.axvline(xi, color="gray", ls="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("G")
plt.title("Ham Green cho -y'' voi bien Dirichlet")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Green function boundary value problem visualization
- search: delta source response one dimensional Poisson
- search: impulse response differential operator

### 5. Bài toán mẫu có bối cảnh thực

Cho bài toán
$$ -y''=f(x),\qquad y(0)=y(1)=0. $$
Hàm Green tương ứng là
$$
G(x,\xi)=
\begin{cases}
x(1-\xi), & x\le \xi,\\
\xi(1-x), & x\ge \xi.
\end{cases}
$$
Do đó nghiệm có dạng
$$ y(x)=\int_0^1 G(x,\xi)f(\xi)\,d\xi. $$
Khi $$ f(\xi)=1 $$, ta thu được ngay
$$ y(x)=\frac{x(1-x)}{2}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Xây dựng hàm Green đơn giản trên đoạn hữu hạn và sử dụng để viết công thức tích phân nghiệm.

**Bậc sau đại học.** Khảo sát hàm Green như hạt nhân (kernel) của toán tử nghịch đảo, tính đối xứng và mối liên hệ với toán tử giải (resolvent).

## Video tham khảo

- Xem trước: [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, tiếng Anh. Trình bày trực quan hàm Green như đáp ứng của hệ với nguồn điểm.
- [Introducing Green's Functions for Partial Differential Equations (PDEs)](https://www.youtube.com/watch?v=xNqLZnM-PPY) — Faculty of Khan, tiếng Anh. Giới thiệu hàm Green cho PDE và bài toán giá trị biên.
- [Green's function for Sturm-Liouville problems](https://www.youtube.com/watch?v=8l4VsNSX_kw) — Nathan Kutz, tiếng Anh. Cách xây dựng hàm Green cho bài toán Sturm–Liouville.

## Tài liệu tham khảo

- Haberman, Chương 9: trình bày hàm Green cho bài toán giá trị biên một chiều và công thức biểu diễn nghiệm.
- Boyce & DiPrima, Chương 11: nền tảng về bài toán Sturm–Liouville và toán tử tự liên hợp.
