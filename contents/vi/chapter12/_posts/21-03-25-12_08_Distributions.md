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

Khi Paul Dirac giới thiệu "hàm" $\delta(x)$ bằng $0$ ở mọi nơi trừ $x = 0$ nhưng tích phân lại bằng $1$, các nhà toán học truyền thống lắc đầu vì không một hàm thực thụ nào làm nổi điều đó. Thế nhưng các nhà vật lý vẫn dùng nó tính toán chính xác tuyệt đối! Phải đến năm 1945, Laurent Schwartz mới giải oan ngoạn mục cho Dirac: $\delta_0$ không phải một hàm gán giá trị tại từng điểm, mà là một **phiếm hàm tuyến tính liên tục tác động lên các hàm thử trơn**—khai sinh **Lý thuyết Phân phối (Distributions)**, nơi *mọi* hàm khả tích đều khả vi vô hạn lần!

## Bản đồ kiến thức nền: Bốn trụ cột của Lý thuyết Phân phối $\mathcal{D}'(\Omega)$

1. **Không gian Hàm thử $\mathcal{D}(\Omega) = C_c^\infty(\Omega)$ và Đối ngẫu $\mathcal{D}'(\Omega)$**:
   Một phân phối $T \in \mathcal{D}'(\Omega)$ là ánh xạ tuyến tính liên tục $\varphi \mapsto \langle T, \varphi \rangle$. Mọi hàm khả tích địa phương $f \in L^1_{\text{loc}}$ tự động sinh ra một phân phối chính quy $\langle T_f, \varphi \rangle = \int f\varphi\,dx$, còn $\langle \delta_{x_0}, \varphi \rangle = \varphi(x_0)$ là phân phối kỳ dị!
2. **Đạo hàm Phân phối — Mọi phân phối đều khả vi vô hạn lần**:
   Định nghĩa $\langle D^\alpha T, \varphi \rangle := (-1)^{|\alpha|}\langle T, D^\alpha \varphi \rangle$. Vì $\varphi$ trơn vô hạn nên $D^\alpha T$ luôn tồn tại với mọi bậc $\alpha$—hàm bậc thang có đạo hàm là $\delta_0$, và $\delta_0$ có đạo hàm là lưỡng cực $\delta_0'$!
3. **Phân phối Ôn hòa $\mathcal{S}'(\mathbb{R}^n)$ và Biến đổi Fourier Mở rộng**:
   Thu hẹp hàm thử sang không gian Schwartz $\mathcal{S}(\mathbb{R}^n)$ (tắt nhanh hơn mọi đa thức) cho phép định nghĩa biến đổi Fourier trên cả các hàm không khả tích như hằng số $1$, đa thức và hàm $\delta_0$: $\widehat{\delta_0} = 1$ và $\widehat{1} = 2\pi \delta_0$!
4. **Nghiệm Cơ bản (Fundamental Solutions) của PDE**:
   Phương trình $L E = \delta_0$ chỉ thực sự có nghĩa toán học chặt chẽ trong $\mathcal{D}'(\mathbb{R}^n)$—và phép tích chập $u = E * f$ lập tức giải tổng quát $L u = f$!

## Mục tiêu

Bài học tùy chọn này giới thiệu khái niệm phân phối (distribution) như sự mở rộng của khái niệm hàm nhằm xử lý nguồn điểm và các đối tượng kỳ dị. Sau bài học, sinh viên cần nắm vai trò của hàm thử, phân phối sinh bởi hàm khả tích địa phương, đạo hàm phân phối, phân phối delta Dirac, và mối liên hệ giữa phân phối với đạo hàm yếu cũng như PDE có dữ liệu kỳ dị.

## Kiến thức nền

Sinh viên cần nắm không gian hàm thử $$ C_c^\infty(\Omega) $$, đạo hàm yếu, tích phân từng phần và trực giác về nguồn điểm trong vật lý. Nội dung này mở rộng ngôn ngữ của PDE vượt ra ngoài khuôn khổ không gian Sobolev.

## Dẫn nhập

Nhiều đối tượng vật lý quen thuộc không thể biểu diễn bằng hàm thông thường: điện tích điểm, xung lực tức thời hay khối lượng tập trung tại một điểm. Lý thuyết phân phối giải quyết vấn đề này bằng cách không mô tả đối tượng thông qua giá trị tại từng điểm, mà thông qua tác động tuyến tính của nó lên các hàm thử trơn.


### Khung giải thích (nên đọc chậm): Tính tay đạo hàm bậc nhất và bậc hai của hàm bậc thang Heaviside $H(x)$ trong $\mathcal{D}'(\mathbb{R})$

Xét hàm bước nhảy $H(x) = 0$ khi $x < 0$ và $H(x) = 1$ khi $x \ge 0$. Lấy một hàm thử bất kỳ $\varphi \in C_c^\infty(\mathbb{R})$ (nên $\varphi(x) = 0$ khi $|x|$ đủ lớn):
1. **Đạo hàm bậc nhất $H'$**:
   $$\langle H', \varphi \rangle = -\langle H, \varphi' \rangle = -\int_0^{+\infty} \varphi'(x)\,dx = -\Big[\varphi(x)\Big]_0^{+\infty} = -(0 - \varphi(0)) = \varphi(0) = \langle \delta_0, \varphi \rangle.$$
   Vậy theo nghĩa phân phối, $H' = \mathbf{\delta_0}$!
2. **Đạo hàm bậc hai $H'' = \delta_0'$**:
   $$\langle \delta_0', \varphi \rangle = -\langle \delta_0, \varphi' \rangle = \mathbf{-\varphi'(0)}.$$
   Kiểm tra với $\varphi(x) = e^{-x^2}\sin(3x)$ (nếu cắt cụt ở xa): tại $x = 0$, $\varphi'(0) = 3$, nên $\langle \delta_0', \varphi \rangle = -3$—một con số hoàn toàn cụ thể dù $\delta_0'$ không có đồ thị thông thường!
## Khái niệm theo ba cách

### Cách trực giác

Hãy hình dung việc dùng các đầu dò trơn để đo một phân bố nguồn. Với nguồn trải đều, kết quả đo là tích phân thông thường; với nguồn tập trung tại một điểm, đầu dò vẫn trả về một giá trị xác định, chính là giá trị của hàm thử tại điểm đặt nguồn. Phân phối mã hóa toàn bộ đáp ứng đó trên mọi hàm thử trơn.

### Cách hình ảnh

Có thể đặt cạnh nhau ba hình ảnh để đối chiếu:

- một hàm thông thường gắn với diện tích dưới đồ thị,
- một mũi nhọn biểu trưng cho phân phối delta Dirac,
- một hàm bậc thang có đạo hàm tập trung tại điểm nhảy.

Cách đối chiếu này cho thấy phân phối là công cụ mô hình hóa chặt chẽ cho các hiện tượng vật lý thực tế chứ không chỉ là khái niệm trừu tượng.

### Cách hình thức

Một phân phối trên $$ \Omega $$ là một phiếm hàm tuyến tính liên tục $$ T:C_c^\infty(\Omega)\to \mathbb{R} $$ (hoặc $$ \mathbb{C} $$).

Nếu $$ u\in L^1_{\mathrm{loc}}(\Omega) $$, phân phối chính quy sinh bởi $$ u $$ được định nghĩa bởi:

$$
\langle T_u,\varphi\rangle=\int_\Omega u(x)\varphi(x)\,dx.
$$

Đạo hàm phân phối của $$ T $$ được định nghĩa qua:

$$
\langle \partial_i T,\varphi\rangle=-\langle T,\partial_i\varphi\rangle.
$$

Định nghĩa này kế thừa trực tiếp công thức tích phân từng phần.

## Ngộ nhận thường gặp

### “Phân phối chỉ là ký hiệu hình thức”

Sai. Đây là đối tượng toán học được định nghĩa chặt chẽ trên không gian hàm thử $$ C_c^\infty(\Omega) $$.

### “Delta Dirac là một hàm bằng vô cùng tại một điểm”

Không chính xác về mặt giải tích. Trong lý thuyết này, delta Dirac không phải là hàm theo nghĩa thông thường mà là một phân phối.

### “Đạo hàm phân phối hoàn toàn tách biệt với đạo hàm yếu”

Không đúng. Đạo hàm yếu chính là trường hợp riêng của đạo hàm phân phối khi kết quả thu được có thể biểu diễn bởi một hàm khả tích địa phương.

### “Phân phối quá trừu tượng nên ít ứng dụng”

Sai. Nguồn điểm, xung lực, hàm Green và biến đổi Fourier đều sử dụng ngôn ngữ phân phối một cách trực tiếp.

## Tiến trình học

### Bước 1: Ôn lại vai trò của hàm thử

Xác định rõ $$ \varphi\in C_c^\infty(\Omega) $$ đóng vai trò là các "đầu dò" trơn có giá compact.

### Bước 2: Xem mọi hàm khả tích địa phương như một phân phối

Thiết lập cầu nối từ khái niệm hàm quen thuộc sang khái niệm phân phối.

### Bước 3: Khảo sát phân phối delta Dirac

Phân tích ví dụ tiêu biểu nhất của phân phối không sinh bởi hàm thông thường.

### Bước 4: Định nghĩa đạo hàm phân phối

Liên hệ trực tiếp với đạo hàm yếu và PDE có nguồn kỳ dị.

### Các điểm kiểm tra hiểu bài

- Sinh viên có nêu được tác động của $$ \delta_{x_0} $$ lên một hàm thử $$ \varphi $$ hay không?
- Sinh viên có phân biệt được hàm Heaviside và đạo hàm phân phối của nó hay không?
- Sinh viên có giải thích được vì sao mọi hàm khả tích địa phương đều xác định một phân phối hay không?

## Ví dụ có lời giải

### Ví dụ 1: Phân phối sinh bởi hàm

Cho $$ u(x)=x $$ trên $$ (-1,1) $$. Phân phối tương ứng là:

$$
\langle T_u,\varphi\rangle=\int_{-1}^1 x\varphi(x)\,dx.
$$

Đây là cách biểu diễn một hàm thông thường dưới ngôn ngữ phân phối.

### Ví dụ 2: Phân phối delta Dirac

Tại điểm $$ x_0 $$, phân phối delta Dirac được định nghĩa bởi $$ \langle \delta_{x_0},\varphi\rangle=\varphi(x_0) $$. Phép toán này lấy giá trị của hàm thử tại đúng một điểm, là mô hình toán học chuẩn cho nguồn điểm.

### Ví dụ 3: Đạo hàm phân phối của hàm Heaviside

Với hàm bậc thang

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0,
\end{cases}
$$

ta có với mọi $$ \varphi\in C_c^\infty(\mathbb{R}) $$:

$$
\langle H',\varphi\rangle=-\int_{\mathbb{R}} H(x)\varphi'(x)\,dx
=-\int_0^\infty \varphi'(x)\,dx
=\varphi(0).
$$

Do đó $$ H'=\delta_0 $$ theo nghĩa phân phối.

### Ví dụ 4: Phương trình Poisson với nguồn điểm

Trong không gian nhiều chiều, phương trình $$ -\Delta u=\delta_0 $$ được hiểu theo nghĩa phân phối. Nghiệm của phương trình này chính là nghiệm cơ bản — nền tảng để xây dựng hàm Green.

## Câu hỏi khái niệm

1. Vì sao không nên xem delta Dirac là một hàm số thông thường?
2. Định nghĩa đạo hàm phân phối kế thừa công thức tích phân từng phần như thế nào?
3. Khi nào đạo hàm phân phối của một hàm cũng chính là đạo hàm yếu dạng hàm khả tích địa phương?

## Bài toán ứng dụng

1. Trong tĩnh điện học, một điện tích điểm được mô hình hóa bằng phân phối delta Dirac như thế nào?
2. Trong cơ học, một xung lực tác dụng tức thời lên hệ được biểu diễn bằng phân phối ra sao?
3. Trong xử lý tín hiệu, vì sao xung Dirac là tín hiệu đầu vào chuẩn để khảo sát đáp ứng xung của hệ tuyến tính?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một nguồn tập trung tại duy nhất một điểm, ta có thể biểu diễn nó bằng hàm số thông thường không?
- Vì sao ngôn ngữ phân phối lại khắc phục được bế tắc đó?
- Có phải mọi phân phối đều sinh bởi một hàm khả tích địa phương không?

### Hoạt động gợi ý

- Cho sinh viên tính trực tiếp đạo hàm phân phối của hàm Heaviside.
- So sánh tác động của nguồn phân bố đều và nguồn điểm lên cùng một hàm thử.
- Thảo luận nhóm về các hiện tượng vật lý cần mô hình hóa bằng nguồn tập trung.

### Cách tăng tham gia

- Mở đầu bằng câu hỏi: "Mật độ của một điện tích điểm có phải là một hàm thông thường không?"
- Yêu cầu sinh viên diễn giải cặp ngoặc $$ \langle T,\varphi\rangle $$ bằng ngôn ngữ trực quan trước khi thao tác đại số.
- Khuyến khích sinh viên lấy thêm ví dụ từ kỹ thuật điện hoặc xử lý tín hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung trước vào trường hợp một chiều.
- Luôn diễn giải ký hiệu $$ \langle T,\varphi\rangle $$ là "tác động của phân phối $$ T $$ lên hàm thử $$ \varphi $$".
- Trình bày chậm và rõ từng bước cho ví dụ đạo hàm của hàm Heaviside.

### Thử thách cho sinh viên khá giỏi

- Chứng minh mọi đạo hàm bậc tùy ý của phân phối delta vẫn là phân phối.
- Tìm hiểu biến đổi Fourier trên không gian phân phối ôn hòa (tempered distributions).
- Khảo sát nghiệm cơ bản của toán tử Laplace trong $$ \mathbb{R}^n $$.

## Ghi nhớ nhanh

Lý thuyết phân phối mở rộng khái niệm hàm bằng cách định nghĩa đối tượng qua tác động tuyến tính lên các hàm thử trơn. Nhờ đó, nguồn điểm, xung lực và đạo hàm của các hàm gián đoạn đều được đưa vào PDE một cách chặt chẽ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Lực tập trung và tải điểm
- Bài toán: Một dầm chịu tải tập trung tại một điểm không thể biểu diễn bằng hàm tải trơn thông thường.
- Mô hình: Sử dụng phân phối delta Dirac $$ \delta_{x_0} $$ làm số hạng nguồn.
- Giả thiết và giới hạn: Là mô hình lý tưởng hóa cho tải trọng tập trung trên vùng rất nhỏ.
- Diễn giải: Phân phối mở rộng không gian hàm để xử lý các nguồn điểm.

#### Tín hiệu xung
- Bài toán: Một xung kích hoạt cực ngắn trong điện tử hoặc cơ học được mô hình hóa thuận tiện bằng xung lý tưởng.
- Mô hình: Sử dụng phân phối delta hoặc đạo hàm của phân phối delta.
- Giả thiết và giới hạn: Được hiểu là giới hạn của các xung hẹp có diện tích đơn vị.
- Diễn giải: Nhiều công thức kỹ thuật trở nên gọn gàng và chặt chẽ hơn trong khuôn khổ phân phối.

### 2. Trực giác bổ sung và các kết nối

Phân phối không phải là "hàm có giá trị vô cùng", mà là một phiếm hàm tuyến tính tác động lên mọi hàm thử trơn. Nhờ cách nhìn này, đạo hàm của hàm bậc thang, nguồn điểm và nghiệm cơ bản của PDE đều có định nghĩa rõ ràng.

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

Nếu $$ H $$ là hàm Heaviside thì theo nghĩa phân phối, $$ H'=\delta_0 $$. Đẳng thức này được hiểu là:
$$
\langle H', \varphi \rangle = -\langle H, \varphi' \rangle = \varphi(0)
$$
với mọi hàm thử $$ \varphi \in C_c^\infty(\mathbb{R}) $$. Điều này giải thích vì sao xung điểm xuất hiện tự nhiên khi lấy đạo hàm của tín hiệu bật–tắt.

### 6. Phân tầng độ khó

**Bậc đại học.** Sử dụng delta Dirac và hàm Heaviside trong mô hình hóa vật lý và kỹ thuật.

**Bậc sau đại học.** Kết nối với phân phối Schwartz, biến đổi Fourier và nghiệm cơ bản của PDE.

## Video tham khảo

- xem trước: [Dirac Delta: Not a Function but a Distribution](https://www.youtube.com/watch?v=XZKf1G5ATkM) — Scintropy, tiếng Anh. Giải thích vì sao delta Dirac là một phân phối chứ không phải hàm thông thường.
- [MM51: Dirac delta distributions](https://www.youtube.com/watch?v=uTSKsWGWpIQ) — Learn Physics with Dr. Viv!, tiếng Anh. Trình bày phân phối delta Dirac dưới dạng tác động tuyến tính lên hàm thử.
- [The Dirac Delta 'Function': How to model an impulse or infinite spike](https://www.youtube.com/watch?v=SxNVcCVj-3c) — Dr. Trefor Bazett, tiếng Anh. Giới thiệu trực giác về xung Dirac trước khi đi vào định nghĩa phiếm hàm.
