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

Bài học này trình bày định nghĩa chính thức của toán tử giả vi phân từ ký hiệu (symbol). Sau bài học, sinh viên cần đọc hiểu công thức lượng tử hóa cơ bản, giải thích vì sao toán tử vi phân là trường hợp riêng, nắm vai trò của không gian Schwartz và thấy rõ cách một ký hiệu tạo ra một toán tử tác động trực tiếp lên hàm số.

## Kiến thức nền

Sinh viên nên nắm khái niệm ký hiệu $$ a(x,\xi) $$, biến đổi Fourier và trực giác xem toán tử qua cách xử lý từng thành phần tần số. Kiến thức cơ bản về không gian Schwartz $$ \mathcal{S}(\mathbb{R}^n) $$ gồm các hàm trơn suy giảm nhanh cũng rất hữu ích.

## Dẫn nhập

Sau khi có ngôn ngữ ký hiệu, câu hỏi trọng tâm đặt ra là: từ một ký hiệu cho trước $$ a(x,\xi) $$, làm thế nào để dựng lại toán tử tương ứng? Câu trả lời là một tích phân dao động kết hợp đồng thời biến vị trí và biến tần số.

Đây là bước chuyển từ mô tả sang cơ chế tác động: ký hiệu không còn chỉ là nhãn đại số mà trực tiếp sinh ra toán tử thông qua phép lượng tử hóa.

## Khái niệm theo ba cách

### Cách trực giác

Có thể xem một toán tử giả vi phân như một bộ lọc tần số thay đổi theo vị trí. Tại mỗi điểm $$ x $$, toán tử áp dụng một quy tắc lọc riêng lên các tần số $$ \xi $$: phân tích hàm đầu vào thành các mode dao động, nhân từng mode với trọng số từ ký hiệu, rồi tổng hợp lại để thu được giá trị đầu ra.

### Cách hình ảnh

Quy trình tác động gồm ba bước:

1. phân tích hàm $$ u $$ thành các sóng phẳng cơ bản;
2. nhân mỗi thành phần tần số với $$ a(x,\xi) $$;
3. tổng hợp các thành phần đã nhân để thu được $$ Au(x) $$.

So sánh với toán tử vi phân: khi ký hiệu là đa thức theo $$ \xi $$, quy trình lọc này rút gọn đúng về phép lấy đạo hàm quen thuộc.

### Cách hình thức

Với ký hiệu đủ tốt $$ a(x,\xi) $$, ta định nghĩa toán tử giả vi phân bởi

$$
\operatorname{Op}(a)u(x)
=
\frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}
e^{i(x-y)\cdot\xi}a(x,\xi)u(y)\,dy\,d\xi.
$$

Viết thông qua biến đổi Fourier, công thức trên có dạng

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

ta thu lại chính xác toán tử vi phân

$$
\sum_{\lvert \alpha\rvert\le m}a_\alpha(x)\partial^\alpha.
$$

## Ngộ nhận thường gặp

### “Định nghĩa chỉ là một tích phân Fourier thông thường”

Không hẳn. Điểm mở rộng cốt lõi là ký hiệu phụ thuộc đồng thời vào cả $$ x $$ và $$ \xi $$.

### “Toán tử giả vi phân luôn tương đương với phép nhân trực tiếp trong miền Fourier”

Điều này chỉ đúng hoàn toàn khi ký hiệu không phụ thuộc vào biến vị trí $$ x $$.

### “Không gian Schwartz chỉ là lựa chọn phụ”

Không đúng. Đây là miền xác định tự nhiên giúp tích phân dao động hội tụ chặt chẽ trước khi mở rộng toán tử sang các không gian hàm tổng quát hơn.

### “Ký hiệu trơn thì toán tử luôn đơn giản”

Không đúng. Tính chất ánh xạ của toán tử còn phụ thuộc mạnh vào bậc và lớp ký hiệu.

## Tiến trình học

### Bước 1: Nhìn lại trường hợp hệ số hằng

Khi ký hiệu chỉ phụ thuộc $$ \xi $$, toán tử quy về phép nhân trong miền Fourier.

### Bước 2: Bổ sung sự phụ thuộc theo vị trí $$ x $$

Đây là bước mở rộng then chốt vượt qua khuôn khổ bộ nhân hằng.

### Bước 3: Phân tích công thức lượng tử hóa

Hiểu rõ vai trò của từng thành phần trong tích phân dao động.

### Bước 4: Kiểm tra toán tử vi phân là trường hợp riêng

Xác nhận sự tương thích với các toán tử quen thuộc giúp định nghĩa trở nên tự nhiên hơn.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vai trò của thừa số pha $$ e^{i(x-y)\cdot\xi} $$ trong công thức hay không?
- Sinh viên có kiểm chứng được toán tử vi phân xuất hiện lại từ ký hiệu đa thức hay không?
- Sinh viên có hiểu vì sao cần khởi đầu trên không gian Schwartz hay không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử nhân bởi hàm

Nếu $$ a(x,\xi)=b(x) $$ không phụ thuộc $$ \xi $$, thì

$$ \operatorname{Op}(a)u(x)=b(x)u(x). $$

Đây là ví dụ đơn giản nhất của toán tử giả vi phân: phép nhân theo điểm.

### Ví dụ 2: Đạo hàm bậc nhất

Nếu $$ a(x,\xi)=i\xi_j $$, thì

$$ \operatorname{Op}(a)u=\partial_{x_j}u. $$

Ví dụ này khẳng định phép lấy đạo hàm cổ điển nằm trọn trong định nghĩa mới.

### Ví dụ 3: Toán tử bậc âm

Xét ký hiệu

$$ a(\xi)=\frac{1}{(1+\lvert \xi\rvert^2)^{1/2}}. $$

Toán tử tương ứng là $$ (1-\Delta)^{-1/2} $$, có bậc $$ -1 $$. Đây không phải toán tử vi phân nhưng hoàn toàn thuộc khuôn khổ giả vi phân.

### Ví dụ 4: Toán tử có hệ số biến thiên

Với

$$ a(x,\xi)=b(x)\frac{1}{1+\lvert \xi\rvert^2}, $$

toán tử vừa lọc tần số cao vừa nhân trọng số theo vị trí. Đây là hình ảnh tiêu biểu của toán tử giả vi phân tổng quát.

## Câu hỏi khái niệm

1. Vì sao công thức định nghĩa toán tử giả vi phân phải chứa đồng thời các biến $$ x $$, $$ y $$ và $$ \xi $$?
2. Vì sao toán tử vi phân chỉ là một trường hợp đặc biệt của phép lượng tử hóa từ ký hiệu?
3. Tại sao việc xét toán tử trước hết trên không gian Schwartz lại thuận lợi về mặt giải tích?

## Bài toán ứng dụng

1. Nếu một toán tử làm trơn tín hiệu bằng cách cắt giảm cao tần, ký hiệu của nó có dạng tổng quát như thế nào?
2. Trong bài toán nghịch đảo cho toán tử elliptic, vì sao lớp toán tử giả vi phân là môi trường phù hợp cho nghịch đảo xấp xỉ?
3. Trong mô hình môi trường không đồng nhất, việc ký hiệu phụ thuộc vào vị trí phản ánh đặc trưng vật lý nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Từ một ký hiệu cho trước, làm thế nào để dựng thành toán tử tác động lên hàm?
- Trong công thức định nghĩa, phần nào là kiến thức quen thuộc từ biến đổi Fourier?
- Làm sao kiểm tra lại toán tử nhân và phép lấy đạo hàm từ công thức tổng quát?

### Hoạt động gợi ý

- Cho sinh viên tự kiểm chứng hai ví dụ cơ bản: ký hiệu không phụ thuộc $$ \xi $$ và ký hiệu $$ i\xi_j $$.
- Sử dụng sơ đồ luồng “biến đổi Fourier -> nhân với ký hiệu -> biến đổi Fourier ngược”.
- Thảo luận nhóm về sự khác biệt giữa bộ lọc đồng nhất và bộ lọc phụ thuộc vị trí.

### Cách tăng mức độ tham gia

- Bắt đầu bằng các ký hiệu đơn giản trước khi tổng quát hóa.
- Yêu cầu sinh viên chỉ rõ phần “lọc theo tần số” và phần “tổng hợp lại” trong tích phân.
- Khuyến khích diễn đạt ý nghĩa công thức bằng lời trước khi thao tác ký hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Giới hạn trước ở các ký hiệu chỉ phụ thuộc $$ \xi $$.
- Minh họa bằng nhiều ví dụ cụ thể trước khi phân tích định nghĩa trừu tượng.
- Nhấn mạnh trực giác: toán tử giả vi phân là bộ lọc tần số có thể thay đổi theo vị trí.

### Thử thách cho sinh viên khá giỏi

- So sánh các quy ước lượng tử hóa khác nhau như Kohn–Nirenberg và Weyl.
- Chứng minh chi tiết rằng ký hiệu đa thức cho lại đúng toán tử vi phân.
- Tìm hiểu cách mở rộng toán tử từ không gian Schwartz sang các không gian Sobolev.

## Ghi nhớ nhanh

Toán tử giả vi phân được xây dựng từ ký hiệu thông qua một công thức tích phân Fourier cục bộ. Toán tử vi phân là trường hợp đặc biệt ứng với ký hiệu đa thức theo $$ \xi $$, trong khi ký hiệu tổng quát bao quát cả các toán tử làm trơn và nghịch đảo xấp xỉ.

---

## Ứng dụng thực tế

### 1. Bộ lọc thay đổi theo vị trí trong xử lý ảnh

Trong ảnh thực tế, mức nhiễu ở vùng tối, vùng sáng hoặc vùng biên thường không giống nhau. Một toán tử với ký hiệu dạng $$ a(x,\xi) $$ cho phép điều chỉnh quy tắc lọc theo từng vị trí thay vì áp dụng đồng nhất trên toàn ảnh. Mô hình này hữu ích cho khử nhiễu thích nghi và khử mờ không đồng nhất, dù ảnh số thực tế còn chịu ảnh hưởng của các yếu tố phi tuyến.

### 2. Môi trường vật liệu không đồng nhất

Trong âm học và cơ học vật liệu, cùng một mode tần số có thể bị hấp thụ hoặc khuếch đại khác nhau tùy vùng không gian. Tính chất này được mô tả tự nhiên bởi ký hiệu phụ thuộc cả $$ x $$ lẫn $$ \xi $$ dưới giả thiết môi trường biến thiên đủ trơn. Công thức lượng tử hóa chuyển “luật tác động cục bộ theo vị trí và tần số” thành một toán tử cụ thể tác động lên nghiệm.

### 3. Nghịch đảo xấp xỉ trong PDE elliptic

Khi cần dựng ứng viên nghịch đảo cho một toán tử elliptic, công thức $$ \operatorname{Op}(a) $$ giúp chuyển ký hiệu nghịch đảo dự đoán thành một toán tử xác định. Đây là bước trung tâm trong quá trình xây dựng parametrix, với giả thiết ký hiệu thuộc một lớp ổn định; trên miền có biên hoặc hình học phức tạp, cần bổ sung thêm cấu trúc kỹ thuật phù hợp.

## Trực giác sâu hơn

Điểm cốt lõi của định nghĩa không nằm ở hình thức tích phân kép, mà ở quy trình: phân tích tín hiệu thành các dao động, gán trọng số cho từng dao động theo một quy tắc phụ thuộc vị trí và tần số, rồi tổng hợp lại. Chính sự phụ thuộc theo biến $$ x $$ tạo nên khả năng biểu diễn rộng rãi của ΨDO so với bộ nhân Fourier cổ điển.

## Trực quan hóa bằng Python

Đoạn mã sau minh họa một bộ lọc làm trơn thay đổi theo vị trí trên tín hiệu 1D.

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

Có thể dùng `p5.js` hoặc `Plotly.js` để tạo hai thanh trượt điều chỉnh mức làm trơn ở bên trái và bên phải gốc tọa độ, giúp người học quan sát trực tiếp hiệu ứng của ký hiệu phụ thuộc $$ x $$.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `position dependent filter Fourier`, `Kohn Nirenberg quantization visualization`, hoặc `pseudodifferential operator local frequency filter`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Xem ΨDO như bộ lọc tần số thay đổi theo vị trí và nhận diện rõ các trường hợp riêng: toán tử nhân, phép lấy đạo hàm và toán tử làm trơn.

### Mức sau đại học (Graduate)

Đi sâu vào các quy ước lượng tử hóa, không gian Schwartz, mở rộng sang các không gian Sobolev và vai trò của định nghĩa này trong phép tính hợp thành.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ảnh y sinh và giải chập
- Bài toán: Thiết bị đo làm biến dạng tín hiệu theo cơ chế phụ thuộc cả vị trí lẫn tần số.
- Mô hình:
$$
(\operatorname{Op}(a)u)(x)=\frac{1}{2\pi}\int e^{ix\xi}a(x,\xi)\hat u(\xi)\,d\xi.
$$
- Giả thiết và giới hạn: Mô hình tuyến tính, chưa tính đến các hiệu ứng phi tuyến của thiết bị đo.
- Diễn giải: ΨDO định nghĩa toán tử như một bộ lọc tần số cục bộ theo vị trí.

#### Cơ học lượng tử bán cổ điển
- Bài toán: Xây dựng toán tử tương ứng với một đại lượng quan sát trên không gian pha.
- Mô hình: Từ hàm $$ a(x,\xi) $$, thực hiện lượng tử hóa để thu được toán tử $$ \operatorname{Op}(a) $$.
- Giả thiết và giới hạn: Kết quả phụ thuộc vào quy ước lượng tử hóa được chọn.
- Diễn giải: Công thức này tạo cầu nối trực tiếp từ đại lượng cổ điển sang toán tử lượng tử.

### 2. Trực giác bổ sung và các kết nối

Định nghĩa ΨDO thực hiện biến đổi Fourier theo không gian, nhân với ký hiệu rồi biến đổi ngược lại, nhưng hệ số nhân giờ đây có thể thay đổi theo vị trí — tức lọc tần số với quy tắc khác nhau ở từng vùng không gian. Vì thế, $$ a(x,\xi) $$ không phải đại lượng phụ trợ mà chính là đặc trưng cốt lõi quyết định bản chất toán tử.

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

Nếu $$ a(x,\xi)=i\xi $$, ta thu lại đạo hàm bậc nhất; nếu $$ a(x,\xi)=1/(1+\xi^2) $$, ta thu được một toán tử làm trơn. Hai ví dụ này cho thấy định nghĩa ΨDO bao trùm đồng thời cả toán tử vi phân lẫn toán tử làm trơn.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm định nghĩa qua hai ví dụ nền tảng là đạo hàm và bộ lọc làm trơn.

**Bậc sau đại học.** Kết nối với phép lượng tử hóa Kohn–Nirenberg, lượng tử hóa Weyl và nhân tích phân dao động.

## Video tham khảo

- Nên xem trước: [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, tiếng Việt. Trình bày định nghĩa toán tử giả vi phân bằng tích phân dao động.
- [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, tiếng Anh. Giới thiệu đại số toán tử giả vi phân và các tính chất ánh xạ của nó.
- [Ps d o’s lecture 2 (Xuwen Zhu)](https://www.youtube.com/watch?v=0OBoX9_-ndQ) — Mathematics video VAROQUI Hervé, tiếng Việt. Tiếp tục phân tích và củng cố định nghĩa toán tử giả vi phân.
