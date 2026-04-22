---
layout: post
title: "Giới Thiệu Phần Tử Hữu Hạn"
chapter: '13'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: optional
---

![Lưới phần tử hữu hạn và các hàm cơ sở cục bộ]({{ site.imgurl }}/chapter_img/chapter13/07_finite_element_introduction.svg )

## Mục tiêu

Bài optional này giới thiệu phương pháp phần tử hữu hạn như con đường tự nhiên đi từ dạng yếu sang mô phỏng số. Sau bài học, sinh viên cần hiểu ý tưởng chia miền thành phần tử nhỏ, xây hàm cơ sở cục bộ, thiết lập hệ tuyến tính từ weak formulation, và nhận ra điểm mạnh của FEM đối với miền hình học phức tạp.

## Kiến thức nền

Sinh viên nên nắm dạng yếu của PDE, không gian $$ H^1_0(\Omega) $$, và sơ bộ về sai phân hữu hạn. Khác với finite differences bắt đầu từ đạo hàm, FEM bắt đầu từ nguyên lý biến phân và không gian hàm.

## Dẫn nhập

Nếu finite differences hỏi “xấp xỉ đạo hàm bằng chênh lệch thế nào?”, thì finite elements hỏi “ta nên tìm nghiệm trong một không gian hữu hạn chiều nào để vẫn giữ cấu trúc năng lượng của bài toán?”. Đây là một thay đổi rất sâu về tư duy. Ta không rời rạc hóa trực tiếp đạo hàm, mà rời rạc hóa không gian nghiệm.

Phương pháp phần tử hữu hạn đặc biệt mạnh khi miền có hình học phức tạp hoặc khi dạng yếu là ngôn ngữ tự nhiên của bài toán, chẳng hạn trong đàn hồi, truyền nhiệt, và cơ học chất rắn.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng muốn dựng một bề mặt cong bằng nhiều tấm nhỏ ghép lại. Mỗi tấm rất đơn giản, nhưng khi ghép đúng cách, toàn bộ bề mặt có thể xấp xỉ tốt hình dạng phức tạp. FEM làm điều đó với nghiệm của PDE: ghép từ các “mảnh” cục bộ đơn giản.

### Cách hình ảnh

Giáo viên nên vẽ một đoạn thẳng được chia thành nhiều phần tử nhỏ, và tại mỗi nút vẽ một hàm “mũ chóp” bằng 1 tại nút đó, bằng 0 tại các nút lân cận xa hơn. Hình này rất quan trọng vì nó cho thấy nghiệm gần đúng là tổ hợp tuyến tính của các basis functions cục bộ.

### Cách hình thức

Với bài toán Poisson dạng yếu:

$$
\int_\Omega \nabla u\cdot\nabla v\,dx=\int_\Omega fv\,dx
\qquad \forall v\in H^1_0(\Omega),
$$

ta chọn không gian con hữu hạn chiều $$ V_h\subset H^1_0(\Omega) $$ và tìm $$ u_h\in V_h $$ sao cho

$$
\int_\Omega \nabla u_h\cdot\nabla v_h\,dx=\int_\Omega fv_h\,dx
\qquad \forall v_h\in V_h.
$$

Nếu $$ V_h $$ được sinh bởi các hàm cơ sở $$ \phi_1,\dots,\phi_N $$, ta viết

$$ u_h=\sum_{j=1}^N U_j\phi_j, $$

và thu được hệ tuyến tính cho các hệ số $$ U_j $$.

## Ngộ nhận thường gặp

### “FEM chỉ là một phiên bản phức tạp của finite differences”

Không. Hai phương pháp xuất phát từ những triết lý khác nhau.

### “Phần tử hữu hạn nghĩa là nghiệm bị chia thành các đoạn rời rạc”

Sai. Nghiệm gần đúng thường vẫn liên tục toàn cục, chỉ được xây từ các mảnh cục bộ.

### “Hàm cơ sở phải toàn cục mới chính xác”

Không. Điểm mạnh của FEM là tính cục bộ của các basis functions.

### “Miền phức tạp thì công thức phải xấu đi”

Ngược lại, FEM thường càng tỏa sáng ở miền hình học phức tạp.

## Tiến trình học

### Bước 1: Bắt đầu từ dạng yếu

Nhắc sinh viên rằng đây là nơi FEM khởi động.

### Bước 2: Chọn không gian con hữu hạn chiều

Giải thích ý nghĩa của chỉ số $$ h $$ như kích thước lưới.

### Bước 3: Viết nghiệm gần đúng theo basis

Biến bài toán vô hạn chiều thành hệ tuyến tính hữu hạn chiều.

### Bước 4: Hiểu tính sparse

Vì basis functions có hỗ cục bộ nên ma trận thu được thường thưa.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao FEM gắn tự nhiên với dạng yếu không?
- Sinh viên có hiểu hàm cơ sở “mũ chóp” hoạt động ra sao không?
- Sinh viên có thấy vì sao ma trận của FEM thường sparse không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm cơ sở trên một đoạn

Chia đoạn $$ [0,1] $$ thành các nút. Hàm cơ sở $$ \phi_i $$ bằng 1 tại nút $$ i $$, bằng 0 tại các nút còn lại, và tuyến tính trên mỗi phần tử lân cận. Đây là viên gạch cơ bản của FEM bậc một.

### Ví dụ 2: Biểu diễn nghiệm gần đúng

Với ba nút nội, ta viết $$ u_h=U_1\phi_1+U_2\phi_2+U_3\phi_3 $$. Lúc này bài toán PDE được thay bằng việc tìm ba hệ số $$ U_1,U_2,U_3 $$.

### Ví dụ 3: Tạo ma trận độ cứng

Nếu chọn thử từng $$ v_h=\phi_i $$, ta thu được các phương trình

$$
\sum_j U_j\int_\Omega \nabla \phi_j\cdot\nabla \phi_i\,dx
=
\int_\Omega f\phi_i\,dx.
$$

Đây chính là hệ ma trận

$$ KU=F. $$

### Ví dụ 4: Vì sao ma trận sparse

Hai basis functions xa nhau thường không chồng lấp hỗ, nên

$$ \int_\Omega \nabla \phi_j\cdot\nabla \phi_i\,dx=0 $$

khi $$ i $$ và $$ j $$ không kề nhau. Vì thế ma trận có rất nhiều phần tử bằng 0.

## Câu hỏi khái niệm

1. Vì sao FEM bắt đầu từ weak formulation thay vì đạo hàm điểm?
2. Điều gì làm cho basis functions cục bộ trở nên hiệu quả?
3. Tại sao hình học phức tạp lại là lợi thế tương đối của FEM?

## Bài toán ứng dụng

1. Trong mô phỏng ứng suất của một khung máy có hình dạng phức tạp, vì sao FEM là lựa chọn tự nhiên?
2. Trong truyền nhiệt trên một miền cong hoặc có lỗ, finite element giúp gì hơn finite differences?
3. Trong cơ học sinh học, khi mô phỏng mô mềm có hình dạng không đều, việc dùng lưới tam giác hay tứ diện mang ý nghĩa gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu không thể tìm nghiệm trong cả không gian vô hạn chiều, em sẽ thu hẹp nó thế nào?
- Vì sao “ghép từ mảnh nhỏ” lại có thể xấp xỉ tốt bề mặt toàn cục?
- Ta được gì khi basis chỉ sống cục bộ?

### Hoạt động gợi ý

- Cho sinh viên tự vẽ ba hàm mũ chóp trên đoạn $$ [0,1] $$.
- Dùng giấy cắt ghép để minh họa các phần tử và nút.
- So sánh trực tiếp một bài toán đơn giản giữa finite differences và FEM.

### Cách tăng tham gia

- Bắt đầu từ hình ảnh ghép các tấm nhỏ thành một bề mặt.
- Cho sinh viên tự viết nghiệm gần đúng dưới dạng tổ hợp basis.
- Mời sinh viên giải thích “ma trận sparse” bằng ngôn ngữ đồ thị hoặc mạng lưới.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Chỉ làm FEM một chiều.
- Dùng rất ít basis functions trong ví dụ đầu.
- Nhấn mạnh pipeline: dạng yếu -> không gian con -> basis -> hệ tuyến tính.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu lemma Cea ở mức trực giác.
- So sánh phần tử bậc một và bậc hai.
- Phân tích sai số theo kích thước lưới $$ h $$.

## Ghi nhớ nhanh

Phần tử hữu hạn không rời rạc hóa trực tiếp đạo hàm mà rời rạc hóa không gian nghiệm trong dạng yếu. Nhờ đó, FEM giữ được cấu trúc năng lượng và xử lý rất tốt các miền hình học phức tạp.

---

## Ứng dụng thực tế

### 1. Ứng suất và biến dạng trong kết cấu

Trong cơ học kết cấu, các bài toán đàn hồi thường được viết ở dạng yếu và giải bằng FEM trên lưới tam giác hoặc tứ diện. Hình học của chi tiết máy, cầu, hay xương sinh học thường quá phức tạp cho lưới sai phân đều. Mô hình giả định vật liệu và điều kiện biên được mô tả đủ chính xác. Diễn giải là FEM mạnh vì nó đi theo hình học thực của miền.

### 2. Truyền nhiệt trên miền cong hoặc có lỗ

Miền vật lý thật hiếm khi là hình chữ nhật hoàn hảo. FEM cho phép chia miền thành phần tử nhỏ thích nghi với biên cong, lỗ khoan, hoặc vùng cần lưới mịn. Đây là lợi thế thực hành rất lớn so với finite differences truyền thống trên lưới đều.

### 3. Dòng chảy và mô phỏng sinh học

Trong mô phỏng dòng chảy máu, mô mềm, hay tăng trưởng mô sinh học, hình học phức tạp và điều kiện biên tinh tế làm FEM trở thành lựa chọn tự nhiên. Mô hình số thường còn phải kết hợp với thích nghi lưới và solver sparse lớn, cho thấy FEM là cửa ngõ vào tính toán khoa học hiện đại.

## Trực giác sâu hơn

FEM không hỏi “đạo hàm tại điểm này là bao nhiêu?” trước tiên. Nó hỏi “nghiệm gần đúng nên sống trong không gian hữu hạn chiều nào để vẫn giữ cấu trúc yếu và năng lượng của bài toán?”. Ngộ nhận phổ biến là nghĩ FEM chỉ là finite differences viết cầu kỳ hơn; thực ra hai phương pháp đi từ hai triết lý hoàn toàn khác nhau.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 6)

def hat(i, x_grid, xs):
    y = np.zeros_like(xs)
    for k, s in enumerate(xs):
        if i > 0 and x_grid[i-1] <= s <= x_grid[i]:
            y[k] = (s - x_grid[i-1]) / (x_grid[i] - x_grid[i-1])
        elif i < len(x_grid)-1 and x_grid[i] <= s <= x_grid[i+1]:
            y[k] = (x_grid[i+1] - s) / (x_grid[i+1] - x_grid[i])
    return y

xs = np.linspace(0, 1, 500)
plt.figure(figsize=(9, 5))
for i in range(1, len(x)-1):
    plt.plot(xs, hat(i, x, xs), label=f'phi_{i}')
plt.scatter(x, np.zeros_like(x), color='black')
plt.title('Các hàm cơ sở mũ chóp trong FEM 1D')
plt.xlabel('x')
plt.ylabel('Giá trị basis')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `p5.js` để cho sinh viên kéo các nút lưới trên đoạn hoặc tam giác đơn giản và xem các hàm cơ sở cục bộ thay đổi ra sao.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `finite element hat functions visualization`, `FEM mesh animation`, hoặc `Poisson equation finite element tutorial`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Hàm cơ sở mũ chóp trong FEM 1D" description="Điều chỉnh số nút lưới và basis đang xét để thấy trực tiếp tính cục bộ của các hàm cơ sở phần tử hữu hạn." path="interactives/chapter13/finite-element-basis-vi.html" height="620px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào FEM một chiều, hàm mũ chóp, dạng yếu, và ma trận thưa từ các basis functions cục bộ.

### Mức sau đại học (Graduate)

Đi sâu vào lemma Cea, ước lượng sai số theo $$ h $$, phần tử bậc cao, adaptivity, và so sánh FEM với spectral methods hoặc finite volumes.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kết cấu cơ học và đàn hồi
- Bài toán: Hình học phức tạp của cầu, xương hay khung cơ khí khó xử lý bằng lưới sai phân đều.
- Mô hình: Chia miền thành tam giác hoặc tứ diện rồi tìm nghiệm xấp xỉ trong không gian hữu hạn chiều.
- Giả thiết và giới hạn: Cần sinh lưới và chọn hàm cơ sở phù hợp.
- Diễn giải: FEM biến PDE thành bài toán năng lượng trên các phần tử nhỏ.

#### Truyền nhiệt trong chi tiết kỹ thuật
- Bài toán: Miền có biên cong, lỗ hổng, hoặc vật liệu ghép khiến finite differences kém linh hoạt.
- Mô hình: Dùng dạng yếu và không gian phần tử hữu hạn để xấp xỉ nghiệm.
- Giả thiết và giới hạn: Chất lượng lưới ảnh hưởng trực tiếp sai số.
- Diễn giải: FEM tận dụng cấu trúc weak solution của chương trước.

### 2. Trực giác bổ sung và các kết nối

Finite element không bắt đầu từ đạo hàm rời rạc, mà bắt đầu từ dạng yếu và không gian xấp xỉ hữu hạn chiều. Đây là lý do nó hợp tự nhiên với Sobolev spaces và Lax-Milgram. Một bẫy phổ biến là chỉ xem FEM như kỹ thuật phần mềm; thật ra nền tảng giải tích của nó là cực kỳ sâu.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.0, 0.3, 0.55, 0.8, 1.0])
values = np.array([0.0, 0.6, 0.2, 0.5, 0.0])

xx = np.linspace(0, 1, 400)
yy = np.interp(xx, nodes, values)

plt.plot(xx, yy, label="xap xi phan tu huu han bac 1")
plt.plot(nodes, values, "o", label="nut luoi")
plt.legend()
plt.title("Ham co so tuyen tinh tren cac phan tu 1D")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: finite element basis functions visualization
- search: triangulation PDE FEM intuition
- search: weak form to finite element method animation

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ [0,1] $$, nghiệm xấp xỉ phần tử hữu hạn bậc 1 có dạng
$$ u_h(x)=\sum_{i=1}^N U_i \phi_i(x), $$
trong đó các $$ \phi_i $$ là hàm hat. Thế vào dạng yếu của
$$ -u''=f $$
ta thu được hệ ma trận
$$ KU=F. $$
Đây là bản rời rạc trực tiếp của tư duy weak solution.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu lưới, hàm hat và ma trận stiffness trong 1D.

**Bậc sau đại học.** Kết nối với Cea's lemma, adaptive refinement và mixed methods.
