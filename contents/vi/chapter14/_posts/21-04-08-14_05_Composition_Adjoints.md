---
layout: post
title: "Composition và Adjoint"
chapter: '14'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter14
lesson_type: required
---

![Symbol calculus cho composition và adjoint của ΨDO]({{ site.imgurl }}/chapter_img/chapter14/05_composition_adjoints.svg )

## Mục tiêu

Bài học này giải thích vì sao các toán tử giả vi phân tạo thành một phép tính hoàn chỉnh chứ không chỉ là tập hợp các định nghĩa rời rạc. Sau bài học, sinh viên cần nắm trực giác của phép hợp thành $$ AB $$, ý nghĩa của ký hiệu hợp thành $$ a\# b $$, lý do toán tử liên hợp (adjoint) của một ΨDO vẫn là một ΨDO, và cách các khai triển tiệm cận cho phép thực hiện các phép toán đại số trực tiếp ở mức ký hiệu.

## Kiến thức nền

Sinh viên nên nắm khái niệm ký hiệu, lớp $$ S^m_{1,0} $$ và định nghĩa cơ bản của $$ \operatorname{Op}(a) $$. Kiến thức về toán tử liên hợp trong không gian Hilbert cùng trực giác từ đại số tuyến tính cũng rất hữu ích.

## Dẫn nhập

Một lý thuyết toán tử chỉ thực sự phát huy hiệu quả khi nó đóng dưới các phép toán tự nhiên: hợp thành hai toán tử, lấy toán tử liên hợp và so sánh với toán tử đồng nhất. Với toán tử vi phân, các tính chất này đã quen thuộc; điểm đáng chú ý là toán tử giả vi phân cũng sở hữu một phép tính tương tự với cấu trúc phong phú hơn.

Tính chất đóng này giữ vai trò nền tảng vì các công cụ trọng tâm như parametrix hay tính chính quy đều dựa trên khả năng thao tác đại số trên ký hiệu thay vì phải xử lý trực tiếp tích phân dao động của từng toán tử.

## Khái niệm theo ba cách

### Cách trực giác

Nếu mỗi toán tử là một bộ lọc tần số phụ thuộc vị trí, thì hợp thành hai toán tử tương ứng với việc áp hai bộ lọc nối tiếp nhau. Ta kỳ vọng kết quả vẫn là một bộ lọc cùng loại, và phép tính ký hiệu khẳng định điều này đồng thời cung cấp công thức xấp xỉ ký hiệu của bộ lọc hợp thành.

### Cách hình ảnh

Có thể biểu diễn phép hợp thành qua sơ đồ:

$$ u \xrightarrow{B} Bu \xrightarrow{A} ABu. $$

Song song ở mức ký hiệu:

$$
b(x,\xi)\quad \text{và}\quad a(x,\xi)\quad \longrightarrow \quad a\# b.
$$

Toán tử liên hợp có thể hình dung như phép “đảo chiều tác động qua tích vô hướng”, tương tự phép chuyển vị liên hợp của ma trận.

### Cách hình thức

Nếu

$$
A=\operatorname{Op}(a),\qquad B=\operatorname{Op}(b),
$$

thì

$$ AB=\operatorname{Op}(a\# b), $$

với khai triển tiệm cận

$$
a\# b \sim \sum_\alpha \frac{1}{\alpha!}\partial_\xi^\alpha a\,D_x^\alpha b.
$$

Ngoài ra, toán tử liên hợp hình thức của $$ A $$ theo tích vô hướng $$ L^2 $$ cũng là một toán tử giả vi phân, có ký hiệu mang khai triển tiệm cận tương tự bắt đầu bằng liên hợp phức của $$ a(x,\xi) $$.

## Ngộ nhận thường gặp

### “Hợp thành chỉ cần nhân trực tiếp hai ký hiệu”

Sai. Phép nhân trực tiếp chỉ đúng trong trường hợp hệ số hằng; khi ký hiệu phụ thuộc vị trí, các số hạng hiệu chỉnh sẽ xuất hiện.

### “Khai triển tiệm cận là một chuỗi hội tụ theo nghĩa thông thường”

Không đúng. Đây là chuỗi tiệm cận giúp xấp xỉ chính xác đến từng bậc, không nhất thiết hội tụ theo nghĩa cổ điển.

### “Toán tử liên hợp chỉ cần lấy liên hợp phức của ký hiệu”

Chưa đủ. Khi ký hiệu phụ thuộc $$ x $$, vẫn có thêm các số hạng hiệu chỉnh bậc thấp hơn.

### “Phép tính này quá kỹ thuật nên ít giá trị thực tế”

Sai. Đây là nền tảng trực tiếp để xây dựng parametrix và phân tích tính chính quy.

## Tiến trình học

### Bước 1: Ôn trực giác từ ma trận

Phép hợp thành tương tự nhân ma trận, còn toán tử liên hợp tương tự chuyển vị liên hợp.

### Bước 2: So sánh với trường hợp hệ số hằng

Khi ký hiệu chỉ phụ thuộc $$ \xi $$, phép hợp thành rút gọn về phép nhân trực tiếp các ký hiệu.

### Bước 3: Bổ sung các số hạng hiệu chỉnh theo $$ x $$

Sự phụ thuộc vào vị trí là nguồn gốc xuất hiện chuỗi khai triển tiệm cận.

### Bước 4: Sử dụng phép tính như một công cụ

Cần hiểu ý nghĩa và phạm vi ứng dụng của khai triển thay vì chỉ học thuộc từng số hạng.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao cần các số hạng hiệu chỉnh trong $$ a\# b $$ hay không?
- Sinh viên có hiểu vì sao toán tử liên hợp của một ΨDO vẫn thuộc cùng lớp toán tử hay không?
- Sinh viên có nắm được vai trò của khai triển tiệm cận trong đại số ký hiệu hay không?

## Ví dụ có lời giải

### Ví dụ 1: Hệ số hằng

Nếu $$ a=a(\xi),\qquad b=b(\xi) $$ không phụ thuộc $$ x $$, thì $$ a\# b=a(\xi)b(\xi) $$. Đây là trường hợp đơn giản nhất: áp nối tiếp hai bộ lọc Fourier tương đương với nhân hai bộ nhân của chúng.

### Ví dụ 2: Toán tử vi phân và toán tử nhân

Xét $$ A=\partial_x,\qquad B=\text{nhân bởi }b(x) $$. Tính trực tiếp cho $$ ABu=\partial_x(bu)=b'u+b\,u' $$. Ví dụ này minh họa rõ ràng rằng hợp thành không thể chỉ là tích thông thường hai ký hiệu vì sự phụ thuộc theo $$ x $$ sinh ra số hạng đạo hàm phụ thêm.

### Ví dụ 3: Toán tử liên hợp của đạo hàm

Trên không gian các hàm trơn suy giảm nhanh, ta có $$ (\partial_x)^*=-\partial_x $$. Ở mức ký hiệu, điều này khớp với liên hợp phức của $$ i\xi $$ là $$ -i\xi $$, và không xuất hiện số hạng hiệu chỉnh nào do hệ số là hằng số.

### Ví dụ 4: Gần nghịch đảo ở tần số cao

Xét

$$
a(\xi)=1+\lvert \xi\rvert^2,\qquad b(\xi)=\frac{1}{1+\lvert \xi\rvert^2}.
$$

Khi đó $$ a(\xi)b(\xi)=1 $$. Trong trường hợp tổng quát có phụ thuộc $$ x $$, tích ký hiệu không còn bằng 1 tuyệt đối nhưng vẫn có thể hiệu chỉnh tiệm cận đến các bậc tùy ý. Đây chính là cơ sở của việc xây dựng parametrix.

## Câu hỏi khái niệm

1. Vì sao phép hợp thành trong phép tính ΨDO không đơn thuần là phép nhân hai ký hiệu?
2. Khai triển tiệm cận giúp ta kiểm soát phép hợp thành toán tử như thế nào?
3. Tại sao tính đóng dưới phép lấy liên hợp lại quan trọng cho các ước lượng năng lượng và bài toán tự liên hợp?

## Bài toán ứng dụng

1. Khi xây dựng parametrix, vì sao cần tính ký hiệu hợp thành giữa một toán tử với ứng viên nghịch đảo của nó?
2. Trong cơ học lượng tử, việc xác định toán tử liên hợp liên hệ thế nào với tính tự liên hợp của các đại lượng quan sát?
3. Trong bài toán ổn định năng lượng, vì sao cấu trúc liên hợp lại quan trọng đối với các ước lượng trong $$ L^2 $$?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Khi áp nối tiếp hai bộ lọc phụ thuộc vị trí, liệu kết quả có còn là một bộ lọc thuộc cùng lớp hay không?
- Vì sao sự phụ thuộc theo vị trí lại làm phát sinh các số hạng hiệu chỉnh?
- Toán tử liên hợp của một ΨDO tương ứng với khái niệm nào trong đại số tuyến tính?

### Hoạt động gợi ý

- Cho sinh viên tự kiểm chứng ví dụ $$ \partial_x\circ b(x) $$.
- So sánh trực tiếp trên bảng hai trường hợp: ký hiệu hệ số hằng và ký hiệu phụ thuộc $$ x $$.
- Thảo luận nhóm về ý nghĩa của khái niệm “xấp xỉ đúng đến từng bậc” trong khai triển tiệm cận.

### Cách tăng mức độ tham gia

- Mở đầu bằng quy tắc đạo hàm của tích để minh họa tính không giao hoán.
- Đề nghị sinh viên dự đoán số hạng phụ thêm trước khi viết công thức khai triển.
- Yêu cầu sinh viên diễn đạt ý nghĩa toán tử liên hợp bằng lời mà không dùng ký hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu bằng nhiều ví dụ hệ số hằng.
- Nhấn mạnh trực giác: phép hợp thành có phần dẫn đầu là tích hai ký hiệu, kèm theo các số hạng hiệu chỉnh do phụ thuộc vị trí.
- Chưa yêu cầu viết chi tiết các khai triển đa chỉ số bậc cao.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu cách suy ra công thức $$ a\# b $$ từ tích phân dao động.
- Tính vài số hạng đầu trong khai triển ký hiệu của toán tử liên hợp.
- Liên hệ phép tính này với quy ước lượng tử hóa Weyl.

## Ghi nhớ nhanh

Các toán tử giả vi phân tạo thành một phép tính đóng dưới phép hợp thành và phép lấy liên hợp. Ở mức ký hiệu, phép hợp thành được biểu diễn qua khai triển tiệm cận $$ a\# b $$, mở đường trực tiếp cho lý thuyết parametrix và tính chính quy elliptic.

---

## Ứng dụng thực tế

### 1. Chuỗi bộ lọc trong xử lý tín hiệu

Trong xử lý tín hiệu và ảnh, người ta thường thực hiện làm trơn trước rồi lấy đạo hàm, hoặc ngược lại. Hai thao tác này nói chung không giao hoán khi bộ lọc thay đổi theo vị trí. Đó là hình ảnh trực quan của phép hợp thành $$ AB $$ và giải thích vì sao ký hiệu hợp thành không chỉ là tích đơn giản; phép tính ΨDO giúp dự đoán tác động tổng hợp của cả chuỗi lọc tuyến tính từ mức ký hiệu.

### 2. Tính tự liên hợp trong cơ học lượng tử

Các đại lượng quan sát vật lý được biểu diễn bằng các toán tử tự liên hợp. Việc toán tử liên hợp của một ΨDO vẫn là một ΨDO cung cấp cơ sở để kiểm tra tính tự liên hợp của toán tử Hamilton và các toán tử đo, đóng vai trò tương tự phép chuyển vị liên hợp của ma trận trong không gian vô hạn chiều (với lưu ý các mô hình thực tế còn cần xét kỹ miền xác định và điều kiện biên).

### 3. Xây dựng nghịch đảo xấp xỉ và tiền điều kiện

Trong giải số PDE, người ta thường ghép toán tử gốc với một toán tử tiền điều kiện (preconditioner) hoặc ứng viên nghịch đảo. Khảo sát ký hiệu hợp thành giúp kiểm tra xem phép ghép có xấp xỉ toán tử đồng nhất hay không, từ đó định hướng thiết kế các thuật toán ổn định.

## Trực giác sâu hơn

Phép hợp thành cho thấy ΨDO không chỉ là một định nghĩa tĩnh mà là một công cụ đại số thực sự. Khai triển tiệm cận không phải công thức hình thức thuần túy; nó diễn đạt định lượng hiệu ứng phụ phát sinh khi ghép hai quy trình lọc phụ thuộc vị trí.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 600)
u = np.exp(-x**2) + 0.2 * np.sin(12 * x)

def gaussian_blur(signal, sigma):
    kernel_x = np.linspace(-1, 1, 101)
    kernel = np.exp(-(kernel_x**2) / (2 * sigma**2))
    kernel /= kernel.sum()
    return np.convolve(signal, kernel, mode='same')

blur_then_diff = np.gradient(gaussian_blur(u, 0.12), x)
diff_then_blur = gaussian_blur(np.gradient(u, x), 0.12)

plt.figure(figsize=(9, 5))
plt.plot(x, blur_then_diff, label='Đạo hàm sau làm trơn')
plt.plot(x, diff_then_blur, '--', label='Làm trơn sau đạo hàm')
plt.title('Composition nói chung không chỉ là đổi thứ tự thao tác')
plt.xlabel('x')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để cho sinh viên hoán đổi thứ tự hai phép biến đổi làm trơn và lấy đạo hàm, rồi quan sát khi nào hai kết quả gần nhau và khi nào sai khác rõ rệt.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `pseudodifferential composition formula`, `self adjoint pseudodifferential operator`, hoặc `preconditioner symbol calculus`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào trực giác: hợp thành hai bộ lọc cho một bộ lọc mới, còn toán tử liên hợp là phiên bản đảo chiều tác động dưới tích vô hướng.

### Mức sau đại học (Graduate)

Đi sâu vào các số hạng đầu của $$ a\# b $$, ký hiệu của toán tử liên hợp, giao hoán tử (commutator), và mối liên hệ với lượng tử hóa Weyl cũng như các đại lượng quan sát lượng tử.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chuỗi xử lý tín hiệu
- Bài toán: Một quy trình xử lý thực tế thường kết hợp liên tiếp nhiều bộ lọc, phép biến đổi và toán tử ước lượng.
- Mô hình: Nếu $$ A=\operatorname{Op}(a) $$ và $$ B=\operatorname{Op}(b) $$ thì
$$ AB=\operatorname{Op}(a\# b) $$
với ký hiệu mới được cho bởi khai triển tiệm cận của $$ a $$ và $$ b $$.
- Giả thiết và giới hạn: Công thức đầy đủ có dạng chuỗi tiệm cận.
- Diễn giải: Phép hợp thành mô tả tác động nối tiếp của chuỗi toán tử trên không gian pha.

#### Toán tử liên hợp trong bài toán ngược
- Bài toán: Tái tạo ảnh và tối ưu hóa ngược thường cần toán tử liên hợp để lan truyền ngược sai số.
- Mô hình: Nếu $$ A=\operatorname{Op}(a) $$ thì $$ A^*=\operatorname{Op}(a^*) $$ đúng đến các số hạng bậc thấp hơn.
- Giả thiết và giới hạn: Cần xác định rõ tích vô hướng và chuẩn trong không gian Hilbert tương ứng.
- Diễn giải: Toán tử liên hợp là thành phần cốt lõi trong các phương pháp nghịch đảo dựa trên gradient.

### 2. Trực giác bổ sung và các kết nối

Phép hợp thành cho phép thực hiện các thao tác đại số giữa các ký hiệu, nhưng khác với phép nhân thông thường do tính không giao hoán giữa biến vị trí $$ x $$ và biến tần số $$ \xi $$. Trong khi đó, toán tử liên hợp cho biết toán tử tác động ra sao khi nhìn từ phía tích vô hướng hay năng lượng. Cần tránh thay $$ a\# b $$ bằng tích thường $$ ab $$ mà bỏ quên các số hạng hiệu chỉnh bậc thấp.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u = np.sin(5 * x) + 0.7 * np.sin(15 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi
uhat = np.fft.fft(u)

a = 1 / (1 + xi**2)
b = xi**2 / (1 + xi**2)
Au = np.fft.ifft(a * uhat).real
BAu = np.fft.ifft(b * np.fft.fft(Au)).real
abu = np.fft.ifft((a * b) * uhat).real

plt.plot(x, BAu, label="B(Au)")
plt.plot(x, abu, "--", label="motiplier ab")
plt.legend()
plt.title("Khi symbol khong phu thuoc x, composition giong nhan")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: pseudodifferential composition symbol product intuition
- search: adjoint operator imaging inverse problems
- search: noncommutativity phase space symbol calculus

### 5. Bài toán mẫu có bối cảnh thực

Nếu $$ a(\xi)=1/(1+\xi^2) $$ và $$ b(\xi)=\xi^2 $$ đều chỉ phụ thuộc $$ \xi $$, thì
$$
\operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(ab).
$$
Đây là trường hợp đơn giản nhất. Khi ký hiệu phụ thuộc thêm vào $$ x $$, công thức cần bổ sung các số hạng đạo hàm hỗn hợp để hiệu chỉnh.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm phép hợp thành thông qua trường hợp bộ nhân chỉ phụ thuộc tần số.

**Bậc sau đại học.** Kết nối với tích Moyal, khai triển ký hiệu và công thức toán tử liên hợp trên đa tạp.

## Video tham khảo

- Nên xem trước: [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, tiếng Anh. Trình bày phép nhân và phép lấy liên hợp trong đại số toán tử giả vi phân.
- [Ps d o’s lecture 2 (Xuwen Zhu)](https://www.youtube.com/watch?v=0OBoX9_-ndQ) — Mathematics video VAROQUI Hervé, tiếng Việt. Bài giảng thứ hai của Xuwen Zhu, đi sâu vào phép tính hợp thành.
- [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, tiếng Việt. Giới thiệu tích ký hiệu mà phép hợp thành hiệu chỉnh bằng các số hạng bậc thấp hơn.
