---
layout: post
title: "Định Nghĩa Toán Tử Giả Vi Phân"
chapter: '14'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter14
lesson_type: required
---

![Định nghĩa toán tử giả vi phân từ symbol]({{ site.imgurl }}/chapter_img/chapter14/04_pdo_definition.svg )

## Mục tiêu

Bài này xây định nghĩa chính thức của toán tử giả vi phân từ symbol. Sau bài học, sinh viên cần đọc được công thức lượng tử hóa cơ bản, hiểu vì sao differential operators là trường hợp riêng, biết vai trò của Schwartz space, và nhìn thấy cách một symbol sinh ra một toán tử thực sự tác động lên hàm.

## Kiến thức nền

Sinh viên nên nắm symbol $$ a(x,\xi) $$, biến đổi Fourier, và trực giác rằng một toán tử nên được hiểu qua cách nó xử lý các thành phần tần số. Kiến thức về không gian Schwartz $$ \mathcal{S}(\mathbb{R}^n) $$ và hàm suy giảm nhanh cũng sẽ rất hữu ích.

## Dẫn nhập

Đến đây, ta đã có một ngôn ngữ mô tả toán tử bằng symbol. Nhưng một câu hỏi thiết yếu vẫn còn đó: nếu cho trước một symbol $$ a(x,\xi) $$, ta phải biến nó thành một toán tử như thế nào? Câu trả lời là một công thức tích phân dao động kết hợp không gian vật lý và không gian tần số.

Đây là khoảnh khắc “từ dữ liệu sang cơ chế”: symbol không còn là mô tả trừu tượng nữa mà trở thành động cơ thật sự tạo ra toán tử.

## Khái niệm theo ba cách

### Cách trực giác

Ta có thể nghĩ pseudodifferential operator như một bộ lọc tần số thay đổi theo vị trí. Mỗi vị trí $$ x $$ có thể dùng một quy tắc lọc khác nhau trên các tần số $$ \xi $$. Toán tử kết quả nhận dữ liệu đầu vào, phân tích nó thành các mode, cân từng mode bằng symbol, rồi ghép lại.

### Cách hình ảnh

Sơ đồ trực quan nên là:

1. tách $$ u $$ thành các sóng cơ bản;
2. nhân mỗi thành phần với $$ a(x,\xi) $$;
3. chồng các thành phần đã sửa lại để thu được $$ Au(x) $$.

So sánh ngay với differential operator: khi symbol là đa thức theo $$ \xi $$, bộ lọc này chính là đạo hàm quen thuộc.

### Cách hình thức

Với symbol đủ tốt $$ a(x,\xi) $$, ta định nghĩa toán tử

$$
\operatorname{Op}(a)u(x)
=
\frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}
e^{i(x-y)\cdot\xi}a(x,\xi)u(y)\,dy\,d\xi.
$$

Nếu viết bằng Fourier transform thì có thể hiểu như

$$
\operatorname{Op}(a)u(x)
=
\frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n}e^{ix\cdot\xi}a(x,\xi)\widehat{u}(\xi)\,d\xi.
$$

Khi

$$
a(x,\xi)=\sum_{\lvert \alpha\rvert\le m}a_\alpha(x)(i\xi)^\alpha,
$$

ta thu được đúng differential operator

$$
\sum_{\lvert \alpha\rvert\le m}a_\alpha(x)\partial^\alpha.
$$

## Ngộ nhận thường gặp

### “Định nghĩa chỉ là một tích phân Fourier quen thuộc”

Không hẳn. Điểm mới là symbol phụ thuộc vào cả $$ x $$ và $$ \xi $$.

### “Toán tử giả vi phân luôn dễ hiểu như phép nhân trong Fourier”

Chỉ khi symbol không phụ thuộc $$ x $$ thì chuyện này mới hoàn toàn trực tiếp.

### “Schwartz space chỉ là lựa chọn phụ”

Không. Đây là môi trường tự nhiên để tích phân dao động được hiểu sạch sẽ trước khi mở rộng sang các không gian khác.

### “Nếu symbol trơn thì toán tử luôn đơn giản”

Không. Tính chất mapping của toán tử còn phụ thuộc vào bậc và lớp symbol.

## Tiến trình học

### Bước 1: Nhìn lại trường hợp hệ số hằng

Ở đây toán tử chỉ là nhân trong miền Fourier.

### Bước 2: Thêm phụ thuộc vị trí $$ x $$

Đây là bước biến differential operator thành mô hình tổng quát hơn.

### Bước 3: Đọc công thức lượng tử hóa

Sinh viên nên hiểu ý nghĩa của từng thành phần trong tích phân.

### Bước 4: Kiểm tra differential operator là trường hợp riêng

Đây là bước quan trọng để loại bỏ cảm giác “định nghĩa từ trên trời rơi xuống”.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vai trò của $$ e^{i(x-y)\cdot\xi} $$ trong công thức không?
- Sinh viên có thấy differential operator xuất hiện lại từ symbol đa thức không?
- Sinh viên có hiểu vì sao cần một lớp hàm tốt như Schwartz space không?

## Ví dụ có lời giải

### Ví dụ 1: Phép nhân bởi hàm

Nếu $$ a(x,\xi)=b(x) $$ không phụ thuộc $$ \xi $$, thì

$$ \operatorname{Op}(a)u(x)=b(x)u(x). $$

Đây là pseudodifferential operator đơn giản nhất: toán tử nhân.

### Ví dụ 2: Đạo hàm bậc nhất

Nếu $$ a(x,\xi)=i\xi_j $$, thì

$$ \operatorname{Op}(a)u=\partial_{x_j}u. $$

Ví dụ này xác nhận rằng đạo hàm cổ điển nằm trọn trong khuôn khổ mới.

### Ví dụ 3: Toán tử bậc âm

Xét

$$ a(\xi)=\frac{1}{(1+\lvert \xi\rvert^2)^{1/2}}. $$

Toán tử tương ứng là $$ (1-\Delta)^{-1/2} $$, một toán tử bậc $$ -1 $$. Nó không phải differential operator nhưng hoàn toàn tự nhiên trong calculus mới.

### Ví dụ 4: Toán tử có hệ số biến thiên

Với

$$ a(x,\xi)=b(x)\frac{1}{1+\lvert \xi\rvert^2}, $$

ta có một toán tử vừa nhân theo vị trí vừa lọc tần số cao. Đây là hình ảnh điển hình của pseudodifferential operator tổng quát.

## Câu hỏi khái niệm

1. Vì sao công thức định nghĩa pseudodifferential operator phải kết hợp cả biến $$ x $$, $$ y $$, và $$ \xi $$?
2. Điều gì làm cho differential operator chỉ là một trường hợp đặc biệt của lượng tử hóa từ symbol?
3. Tại sao việc làm việc trước trên Schwartz space lại hợp lý về mặt giải tích?

## Bài toán ứng dụng

1. Nếu một toán tử làm mịn tín hiệu bằng cách cắt giảm cao tần, symbol của nó nên có dạng tổng quát ra sao?
2. Trong bài toán nghịch đảo cho toán tử elliptic, vì sao lớp pseudodifferential operator là môi trường tự nhiên cho nghịch đảo xấp xỉ?
3. Trong mô hình môi trường không đồng nhất, việc cho symbol phụ thuộc vị trí phản ánh điều gì về vật lý?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu cho em một symbol, em sẽ “lắp” thành toán tử thế nào?
- Công thức định nghĩa có vẻ phức tạp, nhưng phần nào trong đó là quen thuộc từ Fourier?
- Em có thể tìm lại toán tử nhân và đạo hàm từ định nghĩa tổng quát không?

### Hoạt động gợi ý

- Cho sinh viên kiểm tra trực tiếp hai ví dụ: symbol hằng theo $$ \xi $$ và symbol bằng $$ i\xi_j $$.
- Dùng sơ đồ luồng “Fourier -> nhân symbol -> biến đổi ngược”.
- Thảo luận nhóm về sự khác nhau giữa bộ lọc đồng nhất và bộ lọc phụ thuộc vị trí.

### Cách tăng tham gia

- Bắt đầu bằng các symbol rất đơn giản.
- Mời sinh viên tự chỉ ra đâu là phần “nhân” và đâu là phần “ghép lại”.
- Yêu cầu giải thích công thức bằng lời trước rồi mới quay về ký hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Giới hạn ở các symbol chỉ phụ thuộc $$ \xi $$ trước.
- Dùng nhiều ví dụ hơn định nghĩa trừu tượng.
- Nhấn mạnh rằng pseudodifferential operator là bộ lọc tần số có thể thay đổi theo vị trí.

### Thử thách cho sinh viên khá giỏi

- So sánh các quy ước lượng tử hóa khác nhau, như Kohn-Nirenberg và Weyl.
- Chứng minh differential operator xuất hiện lại từ symbol đa thức.
- Tìm hiểu cách mở rộng từ Schwartz space sang Sobolev spaces.

## Ghi nhớ nhanh

Một pseudodifferential operator được sinh ra từ symbol bằng một công thức Fourier cục bộ. Differential operators là những trường hợp đặc biệt khi symbol là đa thức theo $$ \xi $$, còn symbol tổng quát cho phép ta mô tả cả các toán tử làm mịn và nghịch đảo xấp xỉ.

---

## Ứng dụng thực tế

### 1. Bộ lọc thay đổi theo vị trí trong xử lý ảnh

Trong ảnh thực, mức nhiễu ở vùng tối, vùng sáng, hay vùng biên có thể khác nhau. Một toán tử có symbol kiểu $$ a(x,\xi) $$ cho phép bộ lọc thay đổi theo vị trí thay vì dùng cùng một quy tắc trên toàn ảnh. Mô hình này hữu ích cho denoising thích nghi hoặc deblurring không đồng nhất. Giới hạn là ảnh số thật còn có phi tuyến và ràng buộc học máy, nhưng trực giác PDE vẫn rất mạnh.

### 2. Môi trường vật liệu không đồng nhất

Trong âm học hay cơ học vật liệu, cùng một mode tần số có thể bị hấp thụ hay khuếch đại khác nhau ở các vùng khác nhau của không gian. Điều này được mô tả tự nhiên bằng symbol phụ thuộc cả $$ x $$ lẫn $$ \xi $$. Mô hình giả định biến thiên đủ trơn để calculus áp dụng được. Diễn giải là: công thức lượng tử hóa biến một “luật địa phương theo vị trí và tần số” thành một toán tử thật sự tác động lên nghiệm.

### 3. Nghịch đảo xấp xỉ trong elliptic PDE

Nếu ta cần một ứng viên nghịch đảo cho toán tử elliptic, công thức $$ \operatorname{Op}(a) $$ cho phép chuyển symbol nghịch đảo dự đoán thành toán tử cụ thể. Đây là bước quan trọng trong xây parametrix. Mô hình giả định symbol đủ tốt thuộc một lớp ổn định. Giới hạn là ở miền có biên hoặc hình học phức tạp, cần thêm cấu trúc bổ sung.

## Trực giác sâu hơn

Điểm cốt lõi của định nghĩa không nằm ở tích phân kép dài, mà ở ý tưởng: ta phân tích tín hiệu thành dao động, cân mỗi dao động bằng một luật phụ thuộc vị trí và tần số, rồi ghép lại. Ngộ nhận thường gặp là nghĩ định nghĩa chỉ là “viết Fourier theo cách rắc rối hơn”; thật ra chính phụ thuộc theo $$ x $$ làm nên sức mạnh mới của ΨDO.

## Trực quan hóa bằng Python

Đoạn code sau minh họa một bộ lọc làm mịn thay đổi theo vị trí trên tín hiệu 1D.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 600)
u = np.sin(8 * x) + 0.4 * np.sin(2 * x)

# Cửa sổ làm mịn mạnh hơn ở bên phải
sigma = 0.15 + 0.25 * (x > 0)
u_filtered = np.zeros_like(u)

for j, x0 in enumerate(x):
    kernel = np.exp(-((x - x0)**2) / (2 * sigma[j]**2))
    kernel /= kernel.sum()
    u_filtered[j] = np.sum(kernel * u)

plt.figure(figsize=(9, 5))
plt.plot(x, u, label='Tín hiệu gốc', alpha=0.7)
plt.plot(x, u_filtered, label='Lọc phụ thuộc vị trí', linewidth=2)
plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
plt.title('Ý tưởng của symbol phụ thuộc vị trí a(x, xi)')
plt.xlabel('x')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `p5.js` hoặc `Plotly.js` để thêm thanh trượt điều khiển “mức làm mịn ở bên trái” và “mức làm mịn ở bên phải”, giúp sinh viên cảm được trực giác của symbol phụ thuộc $$ x $$.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `position dependent filter Fourier`, `Kohn Nirenberg quantization visualization`, hoặc `pseudodifferential operator local frequency filter`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Nên xem ΨDO như bộ lọc tần số có thể thay đổi theo vị trí và nhận ra các trường hợp riêng: toán tử nhân, đạo hàm, toán tử làm mịn.

### Mức sau đại học (Graduate)

Đi sâu vào các quy ước lượng tử hóa, không gian Schwartz, mở rộng sang Sobolev spaces, và vai trò của định nghĩa này trong composition calculus.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ảnh y sinh và deconvolution
- Bài toán: Thiết bị đo làm biến dạng tín hiệu theo cách phụ thuộc cả vị trí và tần số.
- Mô hình:
$$
(\operatorname{Op}(a)u)(x)=\frac{1}{2\pi}\int e^{ix\xi}a(x,\xi)\hat u(\xi)\,d\xi.
$$
- Giả thiết và giới hạn: Mô hình tuyến tính; bỏ qua nhiều hiệu ứng phi tuyến của thiết bị.
- Diễn giải: ΨDO định nghĩa toán tử như một bộ lọc tần số cục bộ theo vị trí.

#### Cơ học lượng tử bán cổ điển
- Bài toán: Toán tử quan sát được xây từ một hàm trên không gian pha.
- Mô hình: Từ hàm $$ a(x,\xi) $$, ta lượng tử hóa thành $$ \operatorname{Op}(a) $$.
- Giả thiết và giới hạn: Còn phụ thuộc quy ước lượng tử hóa.
- Diễn giải: Đây là cầu nối trực tiếp từ quan sát cổ điển sang toán tử.

### 2. Trực giác bổ sung và các kết nối

Định nghĩa ΨDO nói rằng ta làm Fourier theo biến không gian, nhân bởi symbol, rồi biến đổi ngược lại, nhưng phép nhân giờ có thể phụ thuộc vào vị trí. Nói ngắn gọn: "lọc tần số nhưng lọc khác nhau ở các vùng khác nhau". Một bẫy phổ biến là xem $$ a(x,\xi) $$ như chỉ là hàm phụ; thật ra nó chính là DNA của toán tử.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u = np.sin(6 * x) + 0.5 * np.sin(16 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi

window = 0.6 + 0.4 * np.cos(x - np.pi)
uhat = np.fft.fft(u)
Tu = np.zeros_like(u)
for j, xj in enumerate(x):
    a = 1 / (1 + window[j] * xi**2)
    Tu[j] = np.sum(np.exp(1j * xj * xi) * a * uhat) / len(x)

plt.plot(x, u, label="goc")
plt.plot(x, Tu.real, label="Op(a)u")
plt.legend()
plt.title("Symbol phu thuoc vi tri va tan so")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: pseudodifferential operator definition intuition
- search: local Fourier multiplier visualization
- search: quantization symbol to operator example

### 5. Bài toán mẫu có bối cảnh thực

Nếu $$ a(x,\xi)=i\xi $$, ta thu lại đạo hàm bậc nhất. Nếu $$ a(x,\xi)=1/(1+\xi^2) $$, ta được một toán tử làm trơn. Hai ví dụ này cho thấy định nghĩa ΨDO bao trùm cả toán tử vi phân lẫn các toán tử smoothing.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu định nghĩa qua hai ví dụ: đạo hàm và bộ lọc làm trơn.

**Bậc sau đại học.** Kết nối với Kohn-Nirenberg, Weyl quantization và kernels dao động.
