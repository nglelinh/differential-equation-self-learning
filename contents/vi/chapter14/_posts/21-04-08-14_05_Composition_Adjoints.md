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

Bài này giúp sinh viên hiểu vì sao pseudodifferential operators tạo thành một calculus thật sự, chứ không chỉ là một tập hợp định nghĩa rời rạc. Sau bài học, sinh viên cần hiểu trực giác của phép ghép $$ AB $$, ý nghĩa của symbol mới $$ a\# b $$, vì sao adjoint của một ΨDO vẫn là ΨDO, và cách các khai triển tiệm cận cho phép làm đại số trên level symbol.

## Kiến thức nền

Sinh viên nên nắm khái niệm symbol, lớp $$ S^m_{1,0} $$, và định nghĩa cơ bản của $$ \operatorname{Op}(a) $$. Kiến thức về adjoint trong không gian Hilbert và trực giác từ đại số tuyến tính cũng rất hữu ích.

## Dẫn nhập

Một lý thuyết toán tử chỉ thực sự mạnh khi nó ổn định dưới các phép toán tự nhiên: ghép hai toán tử, lấy adjoint, và so sánh với đồng nhất. Với differential operators, điều này đã quá quen. Điều kỳ diệu là pseudodifferential operators cũng có một calculus tương tự, dù phức tạp hơn.

Điều này rất quan trọng vì các công cụ lớn như parametrix hay regularity đều dựa trên khả năng “làm đại số” với symbol thay vì phải điều khiển trực tiếp tích phân dao động của từng toán tử.

## Khái niệm theo ba cách

### Cách trực giác

Nếu mỗi toán tử là một bộ lọc tần số phụ thuộc vị trí, thì ghép hai toán tử nghĩa là áp hai bộ lọc liên tiếp. Ta kỳ vọng kết quả vẫn là một bộ lọc cùng loại, chỉ phức tạp hơn. Symbol calculus nói rằng điều này đúng, và còn cho ta cách tính gần đúng symbol của bộ lọc ghép.

### Cách hình ảnh

Nên vẽ sơ đồ:

$$ u \xrightarrow{B} Bu \xrightarrow{A} ABu. $$

Song song, ở mức symbol:

$$
b(x,\xi)\quad \text{và}\quad a(x,\xi)\quad \longrightarrow \quad a\# b.
$$

Adjoint cũng nên được vẽ như “đảo chiều cách thử nghiệm qua tích vô hướng”, tương tự chuyển vị liên hợp của ma trận.

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

Ngoài ra, adjoint hình thức của $$ A $$ theo tích vô hướng $$ L^2 $$ cũng là một pseudodifferential operator, với symbol có khai triển tiệm cận tương tự, bắt đầu bằng liên hợp phức của $$ a(x,\xi) $$.

## Ngộ nhận thường gặp

### “Composition chỉ cần nhân hai symbol”

Sai. Điều này chỉ đúng rất gần trong trường hợp hệ số hằng. Khi phụ thuộc vị trí, xuất hiện các hạng sửa.

### “Khai triển tiệm cận nghĩa là chuỗi hội tụ thật”

Không. Đây là chuỗi tiệm cận dùng để mô tả chính xác tới từng bậc, không nhất thiết hội tụ theo nghĩa cổ điển.

### “Adjoint chỉ việc lấy liên hợp phức của symbol”

Chưa đủ. Có thêm các hiệu chỉnh từ sự phụ thuộc theo vị trí.

### “Calculus này quá kỹ thuật nên không có ý nghĩa thực”

Sai. Đây là công cụ nền để xây parametrix và theo dõi regularity.

## Tiến trình học

### Bước 1: Ôn trực giác từ ma trận

Composition giống nhân ma trận, adjoint giống chuyển vị liên hợp.

### Bước 2: So sánh với hệ số hằng

Khi symbol chỉ phụ thuộc $$ \xi $$, composition gần như là nhân trực tiếp.

### Bước 3: Thêm hiệu chỉnh do phụ thuộc $$ x $$

Đây là nơi xuất hiện khai triển tiệm cận.

### Bước 4: Dùng calculus như công cụ

Nhấn mạnh rằng ta không cần thuộc lòng toàn bộ khai triển, mà cần hiểu nó cho phép làm gì.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao phải có các hạng sửa trong $$ a\# b $$ không?
- Sinh viên có biết tại sao adjoint vẫn ở trong cùng lớp toán tử không?
- Sinh viên có thấy vai trò của khai triển tiệm cận trong đại số symbol không?

## Ví dụ có lời giải

### Ví dụ 1: Hệ số hằng

Nếu $$ a=a(\xi),\qquad b=b(\xi) $$, thì không có phụ thuộc $$ x $$, nên về bản chất $$ a\# b=a(\xi)b(\xi) $$. Đây là trường hợp đơn giản nhất: ghép hai bộ lọc Fourier chỉ là nhân hai bộ lọc.

### Ví dụ 2: Một toán tử vi phân và một toán tử nhân

Lấy $$ A=\partial_x,\qquad B=\text{nhân bởi }b(x) $$. Ta biết trực tiếp $$ ABu=\partial_x(bu)=b'u+b\,u' $$. Ví dụ này cho thấy composition không thể chỉ là “nhân symbol” vì phụ thuộc theo $$ x $$ tạo ra hạng phụ thêm.

### Ví dụ 3: Adjoint của đạo hàm

Trên hàm trơn suy giảm nhanh, $$ (\partial_x)^*=-\partial_x $$. Ở mức symbol, điều này phù hợp với liên hợp phức của $$ i\xi $$ là $$ -i\xi $$, cộng với không có hiệu chỉnh thêm trong trường hợp hệ số hằng.

### Ví dụ 4: Gần nghịch đảo ở tần số cao

Cho

$$
a(\xi)=1+\lvert \xi\rvert^2,\qquad b(\xi)=\frac{1}{1+\lvert \xi\rvert^2}.
$$

Khi đó $$ a(\xi)b(\xi)=1 $$. Ở trường hợp phụ thuộc $$ x $$, ta không còn đúng tuyệt đối nhưng vẫn có thể đúng tiệm cận đến các bậc cao. Đây là mầm mống của parametrix.

## Câu hỏi khái niệm

1. Vì sao composition trong ΨDO calculus không đơn giản là nhân symbol?
2. Khai triển tiệm cận giúp ta điều khiển phép ghép toán tử như thế nào?
3. Tại sao việc adjoint của một ΨDO vẫn là ΨDO lại quan trọng cho phân tích năng lượng và tự liên hợp?

## Bài toán ứng dụng

1. Trong xây dựng parametrix, vì sao cần biết cách ghép một toán tử với ứng viên nghịch đảo của nó?
2. Trong cơ học lượng tử, việc theo dõi adjoint của toán tử liên hệ gì với tính tự liên hợp của các observable?
3. Trong bài toán ổn định năng lượng, tại sao cấu trúc adjoint lại quan trọng cho ước lượng $$ L^2 $$?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu hai bộ lọc phụ thuộc vị trí được áp nối tiếp, em có mong chúng vẫn tạo thành một bộ lọc cùng loại không?
- Tại sao phụ thuộc theo vị trí làm xuất hiện hạng sửa?
- Em thấy adjoint của ΨDO gần với ý tưởng nào từ đại số tuyến tính?

### Hoạt động gợi ý

- Cho sinh viên kiểm tra trực tiếp ví dụ $$ \partial_x\circ b(x) $$.
- So sánh trên bảng giữa hệ số hằng và hệ số phụ thuộc $$ x $$.
- Tổ chức thảo luận nhóm về ý nghĩa của “xấp xỉ tới từng bậc” trong khai triển tiệm cận.

### Cách tăng tham gia

- Bắt đầu bằng ví dụ quen thuộc từ tích đạo hàm với hàm nhân.
- Cho sinh viên dự đoán hạng phụ trước khi khai triển.
- Mời sinh viên mô tả adjoint mà không dùng công thức.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Dùng thật nhiều ví dụ với hệ số hằng.
- Nhấn mạnh rằng composition “gần là nhân”, nhưng có sửa vì phụ thuộc vị trí.
- Tránh đòi hỏi viết đầy đủ các multi-index dài.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu nguồn gốc của công thức $$ a\# b $$ từ tích phân dao động.
- Viết các hạng đầu của symbol adjoint.
- Liên hệ calculus này với Weyl quantization.

## Ghi nhớ nhanh

Pseudodifferential operators tạo thành một calculus ổn định dưới composition và adjoint. Ở mức symbol, phép ghép được mô tả bằng khai triển tiệm cận $$ a\# b $$, và chính công cụ này mở đường cho parametrix và regularity elliptic.

---

## Ứng dụng thực tế

### 1. Chuỗi bộ lọc trong xử lý tín hiệu

Trong một pipeline xử lý tín hiệu hay ảnh, ta thường làm trơn trước rồi lấy đạo hàm, hoặc ngược lại. Hai thao tác này không nhất thiết hoán đổi được khi bộ lọc phụ thuộc vị trí. Đó chính là trực giác của composition $$ A B $$ và vì sao symbol ghép không chỉ là tích đơn giản. Mô hình này giả định các bước đều tuyến tính. Diễn giải là: calculus của ΨDO cho phép dự đoán hiệu ứng tổng hợp của cả pipeline từ level symbol.

### 2. Tự liên hợp trong cơ học lượng tử

Các observable vật lý phải được mô hình hóa bởi toán tử tự liên hợp. Việc biết adjoint của một ΨDO vẫn là ΨDO là nền tảng để kiểm tra self-adjointness của Hamiltonian và các toán tử đo. Mô hình lý tưởng hóa bỏ qua miền xác định không bị chặn và điều kiện biên tinh tế. Nhưng về mặt trực giác, adjoint giữ vai trò giống chuyển vị liên hợp của ma trận trong không gian vô hạn chiều.

### 3. Xây dựng gần nghịch đảo và tiền điều kiện

Trong giải số cho PDE, ta ghép toán tử gốc với một preconditioner hay một ứng viên nghịch đảo. Hiểu symbol của composition giúp biết liệu phép ghép này có thực sự gần đồng nhất hay không. Đây là ứng dụng trực tiếp của công thức $$ a\# b $$ vào thiết kế thuật toán ổn định.

## Trực giác sâu hơn

Composition là cách ΨDO chứng minh rằng nó không chỉ là một định nghĩa tĩnh, mà là một ngôn ngữ đại số động. Ngộ nhận thường gặp là nghĩ khai triển tiệm cận chỉ là công thức kỹ thuật dài dòng. Thật ra nó nói bằng ngôn ngữ rất thực tế rằng: ghép hai cơ chế lọc phụ thuộc vị trí sẽ sinh ra hiệu ứng phụ từ sự biến thiên không gian của chúng.

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

Có thể dùng `Plotly.js` để cho sinh viên đổi thứ tự hai thao tác `smooth` và `differentiate`, rồi quan sát khi nào kết quả gần nhau và khi nào khác nhau rõ rệt.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `pseudodifferential composition formula`, `self adjoint pseudodifferential operator`, hoặc `preconditioner symbol calculus`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Giữ trọng tâm ở trực giác: ghép hai bộ lọc tạo ra bộ lọc mới, và adjoint là phiên bản “đảo chiều dưới tích vô hướng”.

### Mức sau đại học (Graduate)

Đi sâu vào các hạng đầu của $$ a\# b $$, symbol của adjoint, commutator, và liên hệ với Weyl quantization hay quantum observables.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chuỗi xử lý tín hiệu
- Bài toán: Một pipeline thực tế thường gồm nhiều bộ lọc, biến đổi và toán tử ước lượng nối tiếp nhau.
- Mô hình: Nếu $$ A=\operatorname{Op}(a) $$ và $$ B=\operatorname{Op}(b) $$ thì
$$ AB=\operatorname{Op}(a\# b) $$
với symbol mới là khai triển bất đối xứng của $$ a $$ và $$ b $$.
- Giả thiết và giới hạn: Công thức đầy đủ là một chuỗi tiệm cận.
- Diễn giải: Composition cho biết tác động nối tiếp lên không gian pha.

#### Toán tử adjoint trong đo đạc nghịch
- Bài toán: Chụp ảnh nghịch đảo và bài toán tối ưu thường cần toán tử adjoint để lan truyền ngược sai số.
- Mô hình: Nếu $$ A=\operatorname{Op}(a) $$ thì $$ A^*=\operatorname{Op}(a^*) $$ tới các hạng bậc thấp hơn.
- Giả thiết và giới hạn: Cần chú ý tới chuẩn trong không gian Hilbert thích hợp.
- Diễn giải: Adjoint là công cụ trung tâm trong gradient-based inversion.

### 2. Trực giác bổ sung và các kết nối

Composition nói rằng các symbol cũng "tính toán với nhau", nhưng không chỉ đơn giản là nhân thường vì còn có hiệu ứng không giao hoán giữa $$ x $$ và $$ \xi $$. Adjoint thì trả lời câu hỏi: toán tử nhìn từ phía năng lượng hoặc tích vô hướng trông như thế nào. Một bẫy phổ biến là thay $$ a\# b $$ bằng $$ ab $$ mà quên các hiệu chỉnh bậc thấp.

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
Đây là trường hợp thuận lợi nhất. Khi symbol phụ thuộc cả $$ x $$, công thức phải thêm các đạo hàm hỗn hợp để hiệu chỉnh.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu composition qua trường hợp multiplier chỉ phụ thuộc tần số.

**Bậc sau đại học.** Kết nối với Moyal product, symbolic expansions và adjoint formulas trên manifold.
