---
layout: post
title: "Các Lớp Symbol"
chapter: '14'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter14
lesson_type: required
---

![Các lớp symbol và kiểm soát tăng trưởng theo tần số]({{ site.imgurl }}/chapter_img/chapter14/03_symbol_classes.svg)

Nếu ta cho phép $p(x, \xi)$ là một hàm tùy ý thì tích phân Fourier $\int e^{ix\xi} p(x, \xi)\widehat{u}(\xi)\,d\xi$ có thể phân kỳ, và hợp thành hai toán tử sẽ mất sạch cấu trúc đại số! Lars Hörmander đã tìm ra đúng "điều kiện tăng trưởng vàng" để mọi phép tính vi tích phân, hợp thành và đánh giá Sobolev chạy mượt như nhung: **lớp ký hiệu $S^m(\mathbb{R}^n \times \mathbb{R}^n)$**—nơi mỗi lần lấy đạo hàm theo $\xi$, bậc tăng trưởng phải **rơi xuống đúng 1 nấc**!

## Kiến thức cần nhớ: Bốn trụ cột của Các lớp Ký hiệu Hörmander $S^m_{\rho,\delta}$

1. **Ước lượng Định nghĩa của Lớp chuẩn $S^m = S^m_{1,0}$**:
   Hàm trơn $p \in C^\infty(\mathbb{R}^n \times \mathbb{R}^n)$ thuộc $S^m$ nếu với mọi đa chỉ số $\alpha, \beta$:
   $$\big|\partial_x^\beta \partial_\xi^\alpha p(x, \xi)\big| \le C_{\alpha, \beta} \langle\xi\rangle^{m - |\alpha|}, \qquad \langle\xi\rangle = (1 + |\xi|^2)^{1/2}.$$
   Đạo hàm theo $x$ **giữ nguyên bậc $m$**, còn mỗi đạo hàm theo $\xi$ **giảm bậc đi $1$** (y hệt như khi lấy đạo hàm một đa thức bậc $m$ theo $\xi$!).
2. **Thang bậc Phân tầng và Lớp Làm trơn $S^{-\infty}$**:
   Ta có chuỗi lồng nhau $S^{-\infty} = \bigcap_m S^m \subset \dots \subset S^{-1} \subset S^0 \subset S^1 \subset \dots$. Các ký hiệu thuộc $S^{-\infty}$ tắt nhanh hơn mọi lũy thừa $\langle\xi\rangle^{-N}$—chúng sinh ra các **toán tử làm trơn** biến mọi phân phối thành hàm $C^\infty$!
3. **Ký hiệu Cổ điển (Classical / Polyhomogeneous Symbols)**:
   Có khai triển tiệm cận $p(x, \xi) \sim \sum_{j=0}^\infty p_{m-j}(x, \xi)$ với mỗi $p_{m-j}$ thuần nhất bậc $m - j$ theo $\xi$ (khi $|\xi| \ge 1$). Nhờ Định lý Borel, ta luôn cộng lại được thành một ký hiệu thật sự trong $S^m$ sai khác một phần tử $S^{-\infty}$!
4. **Lớp Tổng quát $S^m_{\rho, \delta}$ ($0 \le \delta \le \rho \le 1$)**:
   Cho phép đạo hàm theo $\xi$ giảm bậc $\rho$ và đạo hàm theo $x$ tăng bậc $\delta$ (ví dụ bài toán nhiệt cần lớp $S^m_{1/2, 0}$ vì $\tau \sim |\xi|^2$).

## Mục tiêu

Bài học này giải thích vì sao không phải ký hiệu (symbol) nào cũng đủ tốt để xây dựng một phép tính toán tử ổn định. Sau bài học, sinh viên cần đọc hiểu ký hiệu $$ S^m_{\rho,\delta} $$, nắm rõ ý nghĩa của bậc $$ m $$, vai trò của các tham số $$ \rho,\delta $$, và lý do cần kiểm soát các đạo hàm theo cả $$ x $$ lẫn $$ \xi $$ trong phép tính ký hiệu.

## Kiến thức nền

Sinh viên nên nắm khái niệm ký hiệu tổng quát $$ a(x,\xi) $$, đạo hàm riêng nhiều biến, và trực giác rằng hành vi của toán tử ở tần số cao phụ thuộc vào tốc độ tăng hoặc giảm của ký hiệu khi $$ \lvert \xi\rvert $$ lớn.

## Dẫn nhập

Một ký hiệu tùy ý có thể biến thiên quá thất thường: tăng trưởng quá nhanh, dao động quá mạnh, hoặc mất kiểm soát khi lấy đạo hàm. Khi đó, toán tử tương ứng sẽ khó hợp thành, khó xác định toán tử liên hợp và khó khảo sát tính chính quy. Vì vậy, ta cần phân loại các ký hiệu thành những lớp có điều kiện tăng trưởng và độ trơn rõ ràng.

Mục tiêu ở đây không phải là học thuộc một bất đẳng thức kỹ thuật, mà là hiểu rằng các lớp ký hiệu tạo nên khuôn khổ ổn định để phép tính giả vi phân vận hành nhất quán.


### Giải thích: Kiểm chứng bằng tay rằng $p(\xi) = \langle\xi\rangle^{-1} = (1 + \xi^2)^{-1/2}$ thuộc lớp $S^{-1}(\mathbb{R})$

Ta cần kiểm tra ước lượng $|\partial_\xi^k p(\xi)| \le C_k \langle\xi\rangle^{-1 - k}$ cho $k = 0, 1, 2$:
1. **Với $k = 0$**: $|p(\xi)| = (1 + \xi^2)^{-1/2} = \mathbf{1 \cdot \langle\xi\rangle^{-1}}$ (đúng với $C_0 = 1$).
2. **Với $k = 1$**:
   $$\partial_\xi p(\xi) = -\frac{\xi}{(1 + \xi^2)^{3/2}} \implies |\partial_\xi p(\xi)| = \underbrace{\frac{|\xi|}{(1 + \xi^2)^{1/2}}}_{\le 1} \cdot (1 + \xi^2)^{-1} \le \mathbf{1 \cdot \langle\xi\rangle^{-2}}.$$
   Bậc đã giảm đúng $1$ nấc từ $-1$ xuống $-2$!
3. **Với $k = 2$**:
   $$\partial_\xi^2 p(\xi) = \frac{2\xi^2 - 1}{(1 + \xi^2)^{5/2}} \implies |\partial_\xi^2 p(\xi)| \le \frac{2(1 + \xi^2)}{(1 + \xi^2)^{5/2}} = \mathbf{2 \cdot \langle\xi\rangle^{-3}}.$$
   Ngược lại, thử hàm dao động $e^{i\xi}$: đạo hàm $\partial_\xi(e^{i\xi}) = i e^{i\xi}$ có độ lớn luôn bằng $1$ (không hề giảm bậc!), nên $e^{i\xi} \notin S^0_{1,0}$!
## Khái niệm theo ba cách

### Cách trực giác

Hãy nghĩ đến một họ các bộ lọc tần số. Để sử dụng ổn định, các bộ lọc này không nên thay đổi thất thường khi tần số dịch chuyển, cũng không nên biến đổi đột ngột theo vị trí. Các lớp ký hiệu là cách diễn đạt chính xác yêu cầu “đều đặn có kiểm soát” đó bằng ngôn ngữ giải tích.

### Cách hình ảnh

Có thể vẽ so sánh đồ thị của một vài hàm theo $$ \lvert \xi\rvert $$:

- một hàm tăng như $$ \lvert \xi\rvert^m $$;
- một hàm suy giảm như $$ 1/(1+\lvert \xi\rvert^2) $$;
- một hàm dao động quá mạnh khi $$ \lvert \xi\rvert $$ tăng.

Qua đó, người học dễ thấy bậc $$ m $$ biểu thị xu hướng tăng trưởng tổng quát, còn các điều kiện trên đạo hàm kiểm soát độ ổn định của ký hiệu khi vi phân theo vị trí và tần số.

### Cách hình thức

Ta nói $$ a(x,\xi)\in S^m_{\rho,\delta} $$ nếu với mọi đa chỉ số $$ \alpha,\beta $$ tồn tại hằng số $$ C_{\alpha\beta} $$ sao cho

$$
\lvert \partial_x^\alpha\partial_\xi^\beta a(x,\xi)\rvert
\le
C_{\alpha\beta}(1+\lvert \xi\rvert)^{m-\rho\lvert \beta\rvert+\delta\lvert \alpha\rvert}.
$$

Ý nghĩa của các tham số:

- $$ m $$ là bậc tăng trưởng cơ bản;
- mỗi lần lấy đạo hàm theo $$ \xi $$ làm giảm bậc đi $$ \rho $$;
- mỗi lần lấy đạo hàm theo $$ x $$ có thể làm tăng bậc thêm $$ \delta $$.

Lớp tiêu chuẩn thường gặp nhất ở mức nhập môn là

$$ S^m_{1,0}. $$

## Ngộ nhận thường gặp

### “Bậc $$ m $$ chỉ là số mũ hình thức”

Không đúng. Bậc $$ m $$ quyết định trực tiếp việc toán tử khuếch đại hay làm trơn các thành phần tần số cao.

### “Chỉ cần kiểm soát bản thân ký hiệu, không cần xét đạo hàm của nó”

Sai. Phép tính toán tử giả vi phân phụ thuộc chặt chẽ vào các ước lượng trên đạo hàm của ký hiệu.

### “Nếu $$ m<0 $$ thì ký hiệu nhỏ nên ít quan trọng”

Sai. Chính các ký hiệu bậc âm lại sinh ra các toán tử làm trơn và các parametrix có vai trò thiết yếu.

### “Hai tham số $$ \rho,\delta $$ chỉ mang tính kỹ thuật”

Không phải. Chúng đo mức độ đều đặn của ký hiệu theo biến tần số và biến vị trí, đồng thời quyết định xem phép tính ký hiệu có đóng và ổn định hay không.

## Tiến trình học

### Bước 1: Bắt đầu từ bậc $$ m $$

Cần nắm rõ sự khác biệt giữa các trường hợp bậc dương, bậc 0 và bậc âm.

### Bước 2: Xét các đạo hàm theo $$ \xi $$

Quan sát cách hành vi ở tần số cao được kiểm soát sau mỗi lần vi phân theo $$ \xi $$.

### Bước 3: Xét các đạo hàm theo $$ x $$

Hiểu cách kiểm soát sự phụ thuộc của ký hiệu vào vị trí không gian.

### Bước 4: Tập trung vào lớp chuẩn $$ S^m_{1,0} $$

Đây là lớp đơn giản, phổ biến và giàu trực giác nhất trong giai đoạn làm quen.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được ý nghĩa của bậc âm và bậc dương thông qua khái niệm “làm trơn” và “khuếch đại” hay không?
- Sinh viên có đọc hiểu được định nghĩa lớp $$ S^m_{\rho,\delta} $$ hay không?
- Sinh viên có hiểu vì sao đạo hàm theo $$ \xi $$ thường làm giảm bậc của ký hiệu hay không?

## Ví dụ có lời giải

### Ví dụ 1: Ký hiệu bậc hai

Xét $$ a(\xi)=1+\lvert \xi\rvert^2 $$. Mỗi lần lấy đạo hàm theo $$ \xi $$ làm giảm bậc tăng trưởng đi một đơn vị, còn đạo hàm theo $$ x $$ triệt tiêu. Vì vậy

$$ a\in S^2_{1,0}. $$

### Ví dụ 2: Ký hiệu bậc âm

Xét

$$ a(\xi)=\frac{1}{1+\lvert \xi\rvert^2}. $$

Khi $$ \lvert \xi\rvert $$ lớn, ký hiệu giảm như $$ \lvert \xi\rvert^{-2} $$, và mỗi lần vi phân theo $$ \xi $$ tiếp tục làm tốc độ giảm mạnh thêm một bậc, nên $$ a\in S^{-2}_{1,0} $$. Đây là ví dụ tiêu biểu của ký hiệu làm trơn.

### Ví dụ 3: Ký hiệu phụ thuộc vị trí

Cho $$ a(x,\xi)=b(x)(1+\lvert \xi\rvert^2)^{m/2} $$, với $$ b(x) $$ trơn và bị chặn cùng mọi đạo hàm. Khi đó, đạo hàm theo $$ x $$ chỉ tác động lên $$ b(x) $$ mà không làm thay đổi bậc tăng trưởng $$ m $$ theo $$ \xi $$. Do đó

$$ a\in S^m_{1,0}. $$

### Ví dụ 4: Ký hiệu không thuộc lớp chuẩn

Hàm $$ a(x,\xi)=e^{\lvert \xi\rvert^2} $$ tăng nhanh hơn mọi lũy thừa của $$ \lvert \xi\rvert $$, nên không thuộc bất kỳ lớp $$ S^m_{1,0} $$ hữu hạn nào. Ví dụ này cho thấy không phải hàm trơn nào cũng sử dụng được trong phép tính ký hiệu tiêu chuẩn.

## Câu hỏi khái niệm

1. Vì sao bậc của ký hiệu liên hệ trực tiếp với tính chính quy của toán tử?
2. Tại sao cần kiểm soát đồng thời cả ký hiệu lẫn các đạo hàm của nó?
3. Điều gì khiến lớp $$ S^m_{1,0} $$ trở thành lớp chuẩn trong phần nhập môn?

## Bài toán ứng dụng

1. Nếu một bộ lọc làm suy giảm mạnh các thành phần tần số cao, ký hiệu của nó có bậc dương hay âm?
2. Trong lý thuyết chính quy elliptic, vì sao nghịch đảo xấp xỉ của toán tử vi phân thường có ký hiệu bậc âm?
3. Trong xử lý ảnh, một toán tử làm mờ và một toán tử làm sắc nét khác nhau như thế nào về bậc ký hiệu?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Một ký hiệu tăng nhanh theo $$ \lvert \xi\rvert $$ sẽ tác động như thế nào lên các dao động tần số cao?
- Khi lấy đạo hàm theo $$ \xi $$, ta kỳ vọng bậc của ký hiệu giảm hay tăng?
- Vì sao một phép tính toán tử cần một họ các ký hiệu thỏa điều kiện tăng trưởng chặt chẽ?

### Hoạt động gợi ý

- Cho sinh viên phân loại một danh sách ký hiệu theo bậc tăng trưởng.
- So sánh trực quan trên đồ thị các ký hiệu bậc $$ 2,0,-2 $$.
- Thảo luận nhóm về ý nghĩa giải tích của hai tham số $$ \rho,\delta $$.

### Cách tăng mức độ tham gia

- Bắt đầu từ hình ảnh “họ các bộ lọc tần số” trước khi viết bất đẳng thức định nghĩa.
- Đề nghị sinh viên ước lượng bậc ký hiệu trước khi kiểm tra bằng tính toán.
- Phân công mỗi nhóm phân tích một ký hiệu cụ thể rồi đối chiếu kết quả.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm việc trước với lớp chuẩn $$ S^m_{1,0} $$.
- Dùng các ký hiệu không phụ thuộc $$ x $$ để giảm bớt ký hiệu đa chỉ số.
- Nhấn mạnh quy tắc trực quan: bậc âm làm trơn, bậc dương khuếch đại cao tần.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu vai trò của điều kiện $$ \delta<\rho $$ trong phép tính ký hiệu.
- Khảo sát một số lớp ký hiệu không đẳng hướng.
- Liên hệ bậc của lớp ký hiệu với tính chất ánh xạ giữa các không gian Sobolev.

## Ghi nhớ nhanh

Các lớp ký hiệu cung cấp khuôn khổ có hệ thống để kiểm soát tốc độ tăng trưởng và độ trơn của ký hiệu theo cả vị trí lẫn tần số. Bậc $$ m $$ cho biết toán tử làm trơn hay khuếch đại cao tần, còn hai tham số $$ \rho,\delta $$ bảo đảm phép tính ký hiệu vận hành ổn định.

---

## Ứng dụng thực tế

### 1. Mô hình bộ lọc làm mờ và làm sắc nét

Một bộ lọc làm mờ thường có ký hiệu bậc âm, chẳng hạn

$$ a(\xi)=\frac{1}{(1+\lvert \xi\rvert^2)^{1/2}}, $$

trong khi một bộ lọc làm sắc nét khuếch đại vùng cao tần và tương ứng với ký hiệu bậc dương. Mô hình này giả định dữ liệu liên tục và chưa xét giới hạn lấy mẫu; bậc của ký hiệu cho biết ngay xu hướng làm trơn hay nhấn mạnh chi tiết nhỏ của toán tử.

### 2. Chính quy hóa trong bài toán ngược

Trong khử nhiễu và khử mờ ảnh, thay vì dùng phép nghịch đảo trực tiếp dễ làm nổ nhiễu cao tần, người ta thường sử dụng bộ nhân bị chặn dạng

$$
a_\alpha(\xi)=\frac{1}{1+\alpha \lvert \xi\rvert^2}.
$$

Đây là một ký hiệu bậc âm điển hình. Mô hình giả định nhiễu tập trung chủ yếu ở miền tần số cao; nếu chọn hệ số chính quy hóa quá lớn, các chi tiết hữu ích của tín hiệu cũng sẽ bị làm mờ theo.

### 3. Toán tử phân số và vật lý nhiều thang

Các toán tử dạng $$ \lvert \xi\rvert^s $$ xuất hiện trong khuếch tán dị thường, cơ học chất lưu và học máy trên đồ thị ở giới hạn liên tục. Việc phân loại chúng vào các lớp ký hiệu thích hợp giúp kiểm soát tính chất ánh xạ trên các không gian Sobolev. Điều này cho thấy ký hiệu $$ S^m_{\rho,\delta} $$ không chỉ là quy ước hình thức mà là công cụ quản lý các mô hình đa thang.

## Trực giác sâu hơn

Một ký hiệu thuộc lớp tốt không chỉ có độ lớn tăng trưởng có kiểm soát, mà mọi đạo hàm của nó theo $$ x $$ và $$ \xi $$ cũng phải thỏa mãn các ước lượng tương ứng. Nếu thiếu điều kiện trên đạo hàm, phép hợp thành, toán tử liên hợp và việc xây dựng parametrix sẽ mất tính ổn định.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(0, 10, 400)
symbols = {
    'Bậc 2': 1 + xi**2,
    'Bậc 0': np.ones_like(xi),
    'Bậc -2': 1 / (1 + xi**2),
}

plt.figure(figsize=(8, 5))
for name, values in symbols.items():
    plt.loglog(xi + 1e-2, values + 1e-6, label=name)
plt.xlabel('|xi|')
plt.ylabel('Độ lớn symbol')
plt.title('So sánh tăng trưởng của các bậc symbol')
plt.grid(alpha=0.3, which='both')
plt.legend()
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để sinh viên nhập một hàm ký hiệu và quan sát đồ thị trên thang log-log nhằm ước lượng bậc tăng trưởng khi $$ \lvert \xi\rvert $$ lớn.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `symbol class S m rho delta`, `pseudodifferential symbol order visualization`, hoặc `Sobolev mapping symbol order`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ba trường hợp bậc trực quan — dương, bằng 0 và âm — cùng mối liên hệ với việc khuếch đại, giữ nguyên hay làm trơn thành phần cao tần.

### Mức sau đại học (Graduate)

Đi sâu vào vai trò của $$ \rho,\delta $$, điều kiện $$ \delta<\rho $$, và cách các lớp ký hiệu chi phối phép hợp thành, toán tử liên hợp cùng tính chất ánh xạ trên không gian Sobolev.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Mô hình hóa khuếch tán phân số
- Bài toán: Một số môi trường có cơ chế lan truyền không chuẩn, đòi hỏi toán tử bậc không nguyên.
- Mô hình: Ký hiệu có dạng
$$ a(\xi)\sim (1+\lvert \xi\rvert^2)^{m/2}. $$
- Giả thiết và giới hạn: Ký hiệu cần thỏa mãn các ước lượng đạo hàm theo $$ \xi $$ trong lớp tương ứng.
- Diễn giải: Lớp ký hiệu xác định rõ tốc độ tăng trưởng hoặc suy giảm của toán tử ở tần số cao.

#### Chính quy hóa trong bài toán ngược
- Bài toán: Cần khuếch đại có kiểm soát một số dải tần đồng thời triệt giảm mạnh các dải tần khác.
- Mô hình: Lựa chọn ký hiệu trong lớp $$ S^m $$ để kiểm soát trước mức tăng giảm theo tần số.
- Giả thiết và giới hạn: Phải tránh khuếch đại quá mức nhiễu cao tần.
- Diễn giải: Các lớp ký hiệu cho phép phân loại toán tử theo cường độ tác động lên phổ tần số.

### 2. Trực giác bổ sung và các kết nối

Khi nói một ký hiệu thuộc $$ S^m $$, ta hiểu rằng nó hành xử như bậc $$ m $$ ở tần số lớn và các đạo hàm của nó cũng suy giảm đúng quy luật. Cách phân loại này giống như gán một “bậc vi phân tổng quát” cho những toán tử không còn là đa thức hữu hạn theo $$ \xi $$. Một sai sót thường gặp là chỉ kiểm tra độ lớn của $$ a(\xi) $$ mà bỏ qua điều kiện trên các đạo hàm.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(-20, 20, 800)
symbols = {
    "m = 2": (1 + xi**2),
    "m = 0": np.ones_like(xi),
    "m = -1": 1 / np.sqrt(1 + xi**2),
}

for label, val in symbols.items():
    plt.plot(xi, np.abs(val), label=label)

plt.yscale("log")
plt.legend()
plt.title("Cac symbol class khac nhau theo tan so")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: symbol class Sm visualization
- search: fractional Laplacian Fourier symbol intuition
- search: pseudodifferential order frequency growth plot

### 5. Bài toán mẫu có bối cảnh thực

Toán tử
$$ (I-\Delta)^{m/2} $$
có ký hiệu
$$ (1+\lvert \xi\rvert^2)^{m/2}. $$
Với $$ m>0 $$, toán tử khuếch đại các thành phần tần số cao; với $$ m<0 $$, toán tử làm trơn dữ liệu. Đây là ví dụ chuẩn mực để hình dung khái niệm bậc của ΨDO.

### 6. Phân tầng độ khó

**Bậc đại học.** Xem lớp ký hiệu như cách gán “bậc tần số” cho toán tử.

**Bậc sau đại học.** Kết nối với hệ nửa chuẩn (seminorms) trên $$ S^m $$, khai triển tiệm cận và các ký hiệu đa thuần nhất (polyhomogeneous symbols).

## Video tham khảo

- Nên xem trước: [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, tiếng Việt. Trình bày các ước lượng ký hiệu mở đầu cho định nghĩa lớp ký hiệu.
- [Ps d o’s lecture 2 (Xuwen Zhu)](https://www.youtube.com/watch?v=0OBoX9_-ndQ) — Mathematics video VAROQUI Hervé, tiếng Việt. Bài giảng thứ hai vận dụng trực tiếp các lớp ký hiệu.
- [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, tiếng Anh. Bài giảng của Masoud Khalkhali về đại số các toán tử giả vi phân.
