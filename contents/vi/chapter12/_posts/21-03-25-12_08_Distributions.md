---
layout: post
title: "Phân Phối"
chapter: '12'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: optional
---

![Phân phối như nguồn kỳ dị và đạo hàm của hàm bước]({{ site.imgurl }}/chapter_img/chapter12/08_distributions.svg )

## Mục tiêu

Bài này giới thiệu phân phối như một mở rộng của khái niệm hàm để xử lý nguồn điểm và các đối tượng kỳ dị. Sau bài học, sinh viên cần hiểu test functions, phân phối sinh bởi hàm, đạo hàm phân phối, delta Dirac, và mối liên hệ giữa phân phối với đạo hàm yếu cùng PDE có dữ liệu singular.

## Kiến thức nền

Sinh viên nên nắm hàm thử $$ C_c^\infty(\Omega) $$, đạo hàm yếu, tích phân từng phần và trực giác về nguồn điểm trong vật lý. Đây là bài optional nhưng đặc biệt có giá trị vì nó cho thấy ngôn ngữ của PDE còn rộng hơn Sobolev space.

## Dẫn nhập

Có những đối tượng vật lý rất tự nhiên nhưng không thể mô tả bằng hàm cổ điển: một điện tích điểm, một xung lực tức thời, một khối lượng tập trung tại một điểm. Nếu chỉ cho phép hàm thông thường, ta không thể viết chúng gọn gàng. Phân phối giải quyết điều đó bằng cách không mô tả đối tượng qua giá trị điểm, mà qua tác động của nó lên các hàm thử trơn.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng dùng một bộ cảm biến trơn để “quét” một nguồn. Nếu nguồn trải đều, cảm biến trả về tích phân quen thuộc. Nếu nguồn tập trung tại một điểm, cảm biến vẫn cho kết quả, cụ thể là giá trị của hàm thử tại điểm đó. Phân phối là cách ghi lại toàn bộ phản ứng trước mọi phép quét trơn.

### Cách hình ảnh

Một hình minh họa nên đặt cạnh nhau:

- một hàm thông thường với diện tích dưới đồ thị,
- một mũi nhọn vô hạn tượng trưng cho delta Dirac,
- và một hàm bước có đạo hàm tập trung tại điểm nhảy.

Hình này giúp sinh viên thấy phân phối không phải “hàm kỳ lạ”, mà là mô hình hóa những hiện tượng rất thật.

### Cách hình thức

Một phân phối trên $$ \Omega $$ là ánh xạ tuyến tính liên tục $$ T:C_c^\infty(\Omega)\to \mathbb{R} $$ hoặc $$ \mathbb{C} $$.

Nếu $$ u\in L^1_{\mathrm{loc}}(\Omega) $$, ta định nghĩa phân phối sinh bởi $$ u $$ qua

$$
\langle T_u,\varphi\rangle=\int_\Omega u(x)\varphi(x)\,dx.
$$

Đạo hàm phân phối được định nghĩa bởi

$$
\langle \partial_i T,\varphi\rangle=-\langle T,\partial_i\varphi\rangle.
$$

Đây chính là sự tiếp nối hoàn hảo của ý tưởng tích phân từng phần.

## Ngộ nhận thường gặp

### “Phân phối chỉ là ký hiệu hình thức”

Sai. Nó là một đối tượng toán học chặt chẽ với không gian kiểm tra rõ ràng.

### “Dirac delta là một hàm vô hạn tại một điểm”

Không nên hiểu như vậy trong khóa học này. Delta không phải hàm theo nghĩa thông thường mà là một phân phối.

### “Đạo hàm phân phối là khái niệm hoàn toàn khác đạo hàm yếu”

Không. Đạo hàm yếu chính là đạo hàm phân phối trong trường hợp kết quả vẫn là một hàm khả tích cục bộ.

### “Phân phối quá trừu tượng nên không có ứng dụng thật”

Sai. Nguồn điểm, xung lực, hàm Green và biến đổi Fourier đều dùng ngôn ngữ này rất tự nhiên.

## Tiến trình học

### Bước 1: Nhìn lại hàm thử

Sinh viên cần chắc rằng $$ \varphi\in C_c^\infty(\Omega) $$ là các “thiết bị đo” trơn.

### Bước 2: Hiểu mọi hàm khả tích cục bộ đều sinh ra phân phối

Điều này giúp chuyển từ thế giới cũ sang thế giới mới một cách nhẹ nhàng.

### Bước 3: Giới thiệu Dirac delta

Đây là ví dụ gây ấn tượng mạnh nhất.

### Bước 4: Định nghĩa đạo hàm phân phối

Kết nối trực tiếp với đạo hàm yếu và PDE có nguồn kỳ dị.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được $$ \delta_{x_0} $$ làm gì với một hàm thử không?
- Sinh viên có phân biệt được hàm Heaviside và đạo hàm phân phối của nó không?
- Sinh viên có hiểu vì sao mọi hàm khả tích cục bộ là một phân phối không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm sinh phân phối

Cho $$ u(x)=x $$ trên $$ (-1,1) $$. Phân phối tương ứng là

$$
\langle T_u,\varphi\rangle=\int_{-1}^1 x\varphi(x)\,dx.
$$

Đây chỉ là cách viết lại một hàm thông thường bằng ngôn ngữ phân phối.

### Ví dụ 2: Dirac delta

Tại điểm $$ x_0 $$, định nghĩa $$ \langle \delta_{x_0},\varphi\rangle=\varphi(x_0) $$. Nó “lấy mẫu” giá trị của hàm thử tại đúng một điểm. Đây là mô hình lý tưởng cho nguồn điểm.

### Ví dụ 3: Đạo hàm của Heaviside

Với hàm bước

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0,
\end{cases}
$$

ta có

$$
\langle H',\varphi\rangle=-\int_{\mathbb{R}} H(x)\varphi'(x)\,dx
=-\int_0^\infty \varphi'(x)\,dx
=\varphi(0).
$$

Vậy $$ H'=\delta_0 $$ theo nghĩa phân phối.

### Ví dụ 4: Nguồn điểm cho Poisson

Trong không gian nhiều chiều, bài toán $$ -\Delta u=\delta_0 $$ được hiểu theo nghĩa phân phối. Nghiệm cơ bản của bài toán này chính là nền tảng của hàm Green. Ví dụ này cho thấy vì sao phân phối là ngôn ngữ tự nhiên của PDE.

## Câu hỏi khái niệm

1. Vì sao delta Dirac không nên được xem là một hàm thông thường?
2. Đạo hàm phân phối kế thừa tích phân từng phần theo cách nào?
3. Khi nào đạo hàm phân phối của một hàm cũng là một hàm khả tích cục bộ?

## Bài toán ứng dụng

1. Trong điện học, một điện tích điểm được mô hình hóa bằng delta Dirac như thế nào?
2. Trong cơ học, một xung lực tức thời tác dụng lên hệ được biểu diễn bằng phân phối ra sao?
3. Trong xử lý tín hiệu, vì sao xung Dirac là đầu vào lý tưởng để khảo sát đáp ứng của hệ?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một nguồn tập trung tại duy nhất một điểm, em sẽ mô tả nó bằng hàm thế nào?
- Tại sao ngôn ngữ phân phối lại phù hợp hơn ngôn ngữ hàm ở đây?
- Có phải mọi phân phối đều đến từ một hàm không?

### Hoạt động gợi ý

- Cho sinh viên tính trực tiếp đạo hàm phân phối của Heaviside.
- So sánh phản ứng của một hàm thử trước nguồn đều và nguồn điểm.
- Thảo luận nhóm về các hiện tượng vật lý đòi hỏi mô hình hóa bằng nguồn tập trung.

### Cách tăng tham gia

- Bắt đầu bằng câu hỏi “điện tích điểm là hàm gì?”.
- Cho sinh viên đóng vai “hàm thử” và “nguồn” để diễn giải bằng ngôn ngữ đời thường.
- Khuyến khích sinh viên nêu ví dụ ngoài vật lý, như xung trong tín hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Giữ trọng tâm ở một chiều trước.
- Luôn diễn giải cặp ngoặc

$$ \langle T,\varphi\rangle $$

thành “tác động của phân phối lên hàm thử”.
- Làm thật chậm ví dụ Heaviside.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu vì sao mọi đạo hàm của delta đều là phân phối.
- Liên hệ phân phối với biến đổi Fourier.
- Khảo sát nghiệm cơ bản của Laplacian trong $$ \mathbb{R}^n $$.

## Ghi nhớ nhanh

Phân phối mở rộng khái niệm hàm bằng cách mô tả đối tượng qua tác động của nó lên các hàm thử. Nhờ đó, nguồn điểm, xung lực và đạo hàm của các hàm không trơn đều được đưa vào PDE một cách chặt chẽ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Lực tập trung và tải điểm
- Bài toán: Một dầm chịu tải tập trung tại một điểm không thể mô tả bằng hàm trơn thông thường.
- Mô hình: Dùng delta Dirac $$ \delta_{x_0} $$ làm nguồn.
- Giả thiết và giới hạn: Mô hình lý tưởng hóa lực rất tập trung.
- Diễn giải: Distributions mở rộng khái niệm hàm để chứa các nguồn điểm.

#### Tín hiệu xung
- Bài toán: Một cú kích hoạt cực ngắn trong điện tử hay cơ học được mô tả tốt hơn bằng xung lý tưởng.
- Mô hình: Dùng phân bố như delta hoặc đạo hàm của delta.
- Giả thiết và giới hạn: Là giới hạn của các xung hẹp hữu hạn năng lượng hoặc hữu hạn diện tích.
- Diễn giải: Nhiều công thức vật lý trở nên gọn và chính xác hơn trong ngôn ngữ phân bố.

### 2. Trực giác bổ sung và các kết nối

Phân bố không phải là "hàm lạ", mà là cách gán giá trị cho mọi test function. Tư tưởng này giúp đạo hàm của hàm bậc thang, nguồn điểm, hay nghiệm cơ bản đều có nghĩa. Một ngộ nhận phổ biến là delta là một hàm vô hạn tại một điểm; tốt hơn nên hiểu nó như một toán tử tuyến tính.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)
for eps in [0.2, 0.1, 0.05]:
    delta_eps = np.exp(-(x / eps) ** 2) / (eps * np.sqrt(np.pi))
    plt.plot(x, delta_eps, label=f"eps={eps}")

plt.legend()
plt.title("Day Gaussian xap xi delta Dirac")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Dirac delta approximation Gaussian visualization
- search: point load beam distribution theory
- search: Heaviside derivative distribution

### 5. Bài toán mẫu có bối cảnh thực

Nếu $$ H $$ là hàm Heaviside, thì theo nghĩa phân bố,
$$ H'=\delta_0. $$
Điều này được đọc là
$$
\langle H', \varphi \rangle = -\langle H, \varphi' \rangle = \varphi(0)
$$
với mọi test function $$ \varphi $$. Đây là lý do xung điểm xuất hiện tự nhiên khi lấy đạo hàm của tín hiệu bật-tắt.

### 6. Phân tầng độ khó

**Bậc đại học.** Dùng delta và Heaviside như công cụ mô hình hóa.

**Bậc sau đại học.** Kết nối với Schwartz distributions, Fourier transform và nghiệm cơ bản của PDE.
