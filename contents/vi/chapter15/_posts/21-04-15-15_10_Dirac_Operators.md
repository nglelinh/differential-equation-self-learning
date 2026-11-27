---
layout: post
title: "Toán Tử Dirac: Xuất Phát, Tính Chất, và Các Định Lý Cốt Lõi"
chapter: '15'
order: 10
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
---

![Toan tu Dirac va cac cau noi giua vat ly, hinh hoc, va topology]({{ site.imgurl }}/chapter_img/chapter15/10_dirac_operators.svg)

Năm 1928, Paul Dirac đứng trước một bài toán tưởng chừng bất khả thi: tìm một phương trình lượng tử **bậc nhất theo cả thời gian lẫn không gian** sao cho bình phương của nó khớp chính xác với phương trình sóng tương đối tính Klein–Gordon $(\partial_t^2 - \Delta + m^2)\psi = 0$. Không một số thực hay số phức nào thỏa mãn $(a\partial_x + b\partial_y)^2 = \partial_x^2 + \partial_y^2$—nhưng nếu $a, b$ là các **ma trận phản giao hoán** ($ab + ba = 0$) thì điều kỳ diệu xảy ra! Phát minh ấy không chỉ tiên đoán ra **phản vật chất (positron)** và **spin electron**, mà còn trở thành toán tử elliptic trung tâm của hình học vi phân hiện đại!

## Kiến thức cần nhớ: Bốn trụ cột của Toán tử Dirac

1. **Ý tưởng "Lấy căn bậc hai" của Toán tử Laplace bằng Đại số Clifford**:
   Tìm các ma trận $\gamma_1, \dots, \gamma_n$ thỏa mãn quan hệ phản giao hoán $\gamma_j \gamma_k + \gamma_k \gamma_j = 2\delta_{jk} I$ (Đại số Clifford). Khi đó toán tử vi phân hệ bậc nhất $D = -i\sum_{j=1}^n \gamma_j \partial_{x_j}$ thỏa mãn đúng đẳng thức vàng $D^2 = -\Delta\, I$!
2. **Tính Elliptic và Tự liên hợp của Hệ Toán tử Dirac**:
   Ký hiệu chính là ma trận $\sigma_1(D)(\xi) = \sum_{j=1}^n \gamma_j \xi_j$, thỏa mãn $(\sigma_1(D)(\xi))^2 = |\xi|^2 I$—khả nghịch với mọi $\xi \neq 0$! Do đó $D$ là toán tử elliptic bậc $1$ tự liên hợp, có phổ trải rộng về **cả hai phía $\pm\infty$** (nhánh năng lượng âm dẫn Dirac tới dự đoán phản hạt!).
3. **Ứng dụng Hiện đại: Graphene (Electron Dirac 2D) & Vật liệu Tôpô**:
   Trong tấm vật liệu graphene một lớp nguyên tử carbon, các electron gần điểm Dirac di chuyển theo đúng phương trình Dirac 2D không khối lượng—giải thích độ dẫn điện phi thường của graphene!
4. **Định lý Chỉ số Atiyah–Singer cho Toán tử Dirac trên Đa tạp Spin**:
   Trên đa tạp spin compact chẵn chiều, toán tử Dirac tách thành hai nửa $D^+, D^-$; chỉ số giải tích $\operatorname{ind}(D^+) = \dim\ker D^+ - \dim\ker D^-$ bằng chính **giống tôpô $\hat{A}(M)$**—một trong những định lý sâu sắc nhất lịch sử toán học thế kỷ XX!

## Mục tiêu

Bài học tùy chọn này giới thiệu toán tử Dirac trong Chương 15 như một ví dụ tiêu biểu nơi PDE, hình học vi phân, cơ học lượng tử và tôpô giao nhau. Sau bài học, sinh viên cần hiểu vì sao toán tử Dirac xuất phát từ nhu cầu tìm một “căn bậc hai bậc nhất” của toán tử Laplace hoặc toán tử Klein–Gordon, nắm cách biểu diễn qua phép nhân Clifford và bó spinor, hiểu các tính chất cơ bản như tính elliptic, tính tự liên hợp hình thức và công thức bình phương, đồng thời nhận diện vai trò của công thức Lichnerowicz, tính chính quy elliptic và định lý chỉ số Atiyah–Singer.

## Kiến thức nền

Sinh viên nên nắm toán tử elliptic, ký hiệu chính, tính chính quy vi địa phương, biến đổi Fourier, không gian Hilbert và trực giác cơ bản về spinor hoặc tối thiểu là dạng vi phân (differential forms). Nếu chưa học sâu hình học spin, có thể dùng toán tử Hodge–Dirac $$d+d^*$$ làm mô hình dẫn nhập trước khi chuyển sang toán tử Dirac hình học trên đa tạp spin.

## Dẫn nhập

Các chương trước chủ yếu làm việc với những toán tử bậc hai như toán tử Laplace, toán tử sóng và toán tử Schrödinger. Khi toán học và vật lý đi sâu hơn, một câu hỏi tự nhiên được đặt ra: liệu có thể dựng một toán tử bậc nhất sao cho bình phương của nó là một toán tử kiểu Laplace hay không? Một toán tử như vậy sẽ tinh hơn, nhạy hơn với cấu trúc hình học và giàu đối xứng hơn.

Toán tử Dirac chính là câu trả lời cho câu hỏi đó. Trong vật lý, Dirac tìm một phương trình tương đối tính bậc nhất theo cả thời gian lẫn không gian cho electron thay vì phương trình Klein–Gordon bậc hai. Trong hình học, các toán tử “kiểu Dirac” được xây dựng từ đại số Clifford và liên thông (connection) tương thích, có bình phương bằng toán tử kiểu Laplace cộng thêm các số hạng độ cong. Nhờ đó, toán tử Dirac trở thành cầu nối chặt chẽ giữa giải tích, hình học và tôpô.

Trong khóa học PDE nâng cao, toán tử Dirac cho thấy các toán tử elliptic bậc nhất thường bộc lộ những cấu trúc hình học sâu sắc nhất: nếu toán tử Laplace gắn với tính chính quy và phổ, thì toán tử Dirac mang thêm thông tin về cấu trúc spin, độ cong, chỉ số giải tích và bản chất vật lý của hạt spin-$$\frac12$$.

## Xuất phát của toán tử Dirac

Toán tử Dirac hình thành từ hai nguồn động lực lớn.

Thứ nhất là từ vật lý tương đối tính. Phương trình Klein–Gordon

$$
\left(\partial_t^2-\Delta_x+m^2\right)\psi=0
$$

là phương trình bậc hai. Dirac tìm kiếm một phương trình bậc nhất theo cả không gian và thời gian để mô tả động học electron một cách nhất quán và tự nhiên bao hàm spin. Ý tưởng cốt lõi là phân tích nhân tử toán tử bậc hai bằng các ma trận thỏa mãn quan hệ phản giao hoán — bước đi mở trực tiếp sang đại số Clifford.

Thứ hai là từ hình học vi phân. Trên các dạng vi phân, toán tử

$$
D_{\mathrm{dR}}=d+d^*
$$

là một toán tử bậc nhất tự nhiên thỏa mãn

$$
D_{\mathrm{dR}}^2=\Delta_H,
$$

trong đó $$\Delta_H$$ là toán tử Laplace–Hodge. Khi hình học spin phát triển, mô hình này được tổng quát hóa lên bó spinor với phép nhân Clifford, tạo nên toán tử Dirac hình học của hình học vi phân hiện đại.

Dưới góc nhìn PDE, toán tử Dirac chính là lời giải cho bài toán phân tích nhân tử toán tử bậc hai trong khi vẫn bảo toàn tính elliptic và tích hợp thêm cấu trúc hình học.


### Giải thích: Tự tay kiểm chứng $D^2 = -\Delta\,I$ bằng hai ma trận Pauli $2 \times 2$

Xét hai ma trận Pauli $\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ và $\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ trên $\mathbb{R}^2$. Đặt toán tử Dirac 2D là $D = -i(\sigma_1 \partial_x + \sigma_2 \partial_y)$:
1. **Kiểm tra đại số Clifford của $\sigma_1, \sigma_2$**:
   - $\sigma_1^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$, $\quad \sigma_2^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$.
   - $\sigma_1 \sigma_2 = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$, $\quad \sigma_2 \sigma_1 = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \implies \mathbf{\sigma_1\sigma_2 + \sigma_2\sigma_1 = 0}$!
2. **Bình phương toán tử $D$**:
   $$D^2 = (-i)^2\big(\sigma_1^2\partial_x^2 + \sigma_2^2\partial_y^2 + (\sigma_1\sigma_2 + \sigma_2\sigma_1)\partial_x\partial_y\big) = -\big(I\,\partial_x^2 + I\,\partial_y^2 + 0\big) = \mathbf{(-\Delta)\,I}!$$
   Số hạng đạo hàm chéo $\partial_x\partial_y$ tự triệt tiêu tuyệt đối nhờ tính phản giao hoán—và ta thu được đúng "căn bậc hai bậc nhất" của $-\Delta$!
## Khái niệm theo ba cách

### Cách trực giác

Nếu toán tử Laplace đo độ cong bậc hai của một trường vô hướng, thì toán tử Dirac giống như một “đạo hàm có hướng và có spin”: nó vừa lấy đạo hàm, vừa ghi nhận cách các thành phần của spinor biến đổi theo hình học không gian. Vì là bậc nhất, nó nhạy với cấu trúc tinh; vì bình phương của nó thuộc kiểu Laplace, nó vẫn giữ trọn sức mạnh của lý thuyết elliptic.

### Cách hình ảnh

Có thể vẽ một tam giác nối ba đỉnh: vật lý (electron tương đối tính), hình học (liên thông spin và phép nhân Clifford) và tôpô (chỉ số). Toán tử Dirac nằm ở tâm, nối xuống công thức bình phương $$D^2=\nabla^*\nabla+\text{curvature term}$$ và nối sang định lý chỉ số — minh họa việc dữ kiện giải tích của toán tử phản ánh trực tiếp bất biến tôpô toàn cục của đa tạp.

### Cách hình thức

Trên không gian Euclid với cơ sở trực chuẩn $$e_1,\dots,e_n$$, một biểu diễn Clifford là ánh xạ tuyến tính $$v\mapsto c(v)$$ thỏa mãn

$$
c(v)c(w)+c(w)c(v)=-2g(v,w)\operatorname{Id}.
$$

Với bó spinor $$S$$ và liên thông tương thích $$\nabla$$, toán tử Dirac hình học được định nghĩa bởi

$$
D=\sum_{j=1}^n c(e_j)\nabla_{e_j}.
$$

Theo quy ước giải tích chuẩn, ký hiệu chính của $$D$$ là

$$
\sigma_D(x,\xi)=i\,c(\xi).
$$

Do quan hệ Clifford cho

$$
c(\xi)^2=-|\xi|^2\operatorname{Id},
$$

ký hiệu chính $$\sigma_D(x,\xi)$$ khả nghịch với mọi $$\xi\neq 0$$, khẳng định toán tử Dirac là elliptic. Trên không gian phẳng với hệ số hằng, bình phương của $$D$$ cho

$$
D^2=-\Delta \operatorname{Id},
$$

theo quy ước hình học.

## Tính chất cốt lõi

### Bậc nhất nhưng sở hữu tính chất của toán tử elliptic

Là toán tử bậc nhất, toán tử Dirac gắn gần với cấu trúc động học và vận chuyển hơn toán tử Laplace, nhưng nhờ bình phương có dạng toán tử kiểu Laplace, nó vẫn hưởng trọn lý thuyết chính quy elliptic và lý thuyết phổ.

### Tính elliptic

Tính elliptic xuất phát trực tiếp từ quan hệ Clifford: với $$\xi\neq 0$$, bình phương của $$c(\xi)$$ là bội khác không của toán tử đồng nhất nên $$c(\xi)$$ khả nghịch. Hệ quả là toán tử Dirac có parametrix, có hạt nhân hữu hạn chiều trên đa tạp compact và áp dụng được toàn bộ công cụ của lý thuyết elliptic.

### Tính tự liên hợp hình thức

Với metric Hermite thích hợp trên bó spinor và liên thông tương thích, toán tử Dirac hình học là tự liên hợp hình thức trên đa tạp đóng. Điều này bảo đảm phổ gồm các trị riêng thực, cho phép vận dụng lý thuyết phổ để nghiên cứu dao động và trạng thái lượng tử.

### Độ nhạy cao với độ cong

Trong khi toán tử Laplace trên hàm vô hướng chỉ phụ thuộc metric, toán tử Dirac phụ thuộc thêm vào cấu trúc spin và liên thông, khiến bình phương của nó xuất hiện tường minh số hạng độ cong — nền tảng của các định lý triệt tiêu (vanishing theorems) và lý thuyết chỉ số.

## Các định lý trung tâm

### Định lý 1: Tính elliptic của toán tử Dirac

Với toán tử kiểu Dirac $$D$$, ký hiệu chính $$\sigma_D(x,\xi)=i\,c(\xi)$$ khả nghịch với mọi $$\xi\neq 0$$, do đó $$D$$ là toán tử elliptic bậc nhất.

Hệ quả là toàn bộ kết quả chính quy elliptic áp dụng được: nếu $$Du=f$$ và $$f$$ trơn thì $$u$$ trơn; trên đa tạp compact, hạt nhân của $$D$$ hữu hạn chiều, và khi $$D$$ tự liên hợp thì phổ rời rạc chỉ tích tụ ở vô cực.

### Định lý 2: Công thức Lichnerowicz

Trên đa tạp Riemann spin đóng,

$$
D^2=\nabla^*\nabla+\frac14\operatorname{Scal}.
$$

Đây là một trong những công thức quan trọng nhất của chủ đề: bình phương toán tử Dirac bằng toán tử Laplace thô (rough Laplacian) cộng đúng một phần tư độ cong vô hướng, đưa độ cong vô hướng đi thẳng vào giải tích nghiệm PDE.

Hệ quả kinh điển là định lý triệt tiêu: nếu đa tạp đóng có $$\operatorname{Scal}>0$$ tại mọi điểm, thì mọi spinor điều hòa đều đồng nhất bằng 0 (chỉ cần lấy tích vô hướng phương trình $$D\psi=0$$ với $$\psi$$ rồi tích phân để thấy tổng hai số hạng không âm bằng 0).

### Định lý 3: Tính chính quy elliptic và tính Fredholm

Nếu $$D$$ là toán tử kiểu Dirac trên đa tạp compact thì

$$
D:H^s(S)\to H^{s-1}(S)
$$

là toán tử Fredholm với mọi $$s$$ phù hợp, nghĩa là hạt nhân và đối hạt nhân đều hữu hạn chiều, nên nghiệm tồn tại modulo một số hữu hạn điều kiện trực giao.

Điều này khẳng định toán tử Dirac có cấu trúc giải tích rất chặt chẽ, cho phép khảo sát phổ, chỉ số và độ ổn định nghiệm trên các không gian Sobolev.

### Định lý 4: Định lý chỉ số Atiyah–Singer cho toán tử spin Dirac

Trên đa tạp spin compact chẵn chiều, bó spinor tách thành $$S^+\oplus S^-$$ và toán tử Dirac hạn chế thành

$$
D^+: \Gamma(S^+) \to \Gamma(S^-).
$$

Khi đó, chỉ số giải tích

$$
\operatorname{ind}(D^+)=\dim\ker D^+ - \dim\ker (D^+)^*
$$

bằng đúng một bất biến tôpô toàn cục (trong trường hợp spin thuần túy là giống $$\widehat{A}(M)$$). Đây là một trong những kết quả nổi bật của toán học thế kỷ XX, liên kết trực tiếp dữ kiện giải tích của một PDE elliptic bậc nhất với bất biến tôpô của đa tạp.

## Định lý, bổ đề, và chứng minh trọng tâm

### Định lý: Tính elliptic của toán tử Dirac
Với toán tử Dirac hình học $$ D $$, ký hiệu chính có dạng
$$
\sigma_D(x,\xi)=i\,c(\xi),
$$
và khả nghịch với mọi $$ \xi\neq 0 $$. Do đó $$ D $$ là toán tử elliptic bậc nhất.

### Chứng minh
Quan hệ Clifford trên đồng vectơ $$\xi$$ cho
$$
c(\xi)^2=-|\xi|^2\operatorname{Id}.
$$
Khi $$\xi\neq 0$$ thì $$|\xi|^2\neq 0$$, nên $$c(\xi)$$ khả nghịch với nghịch đảo tường minh
$$
c(\xi)^{-1}=-\frac{c(\xi)}{|\xi|^2}.
$$
Ký hiệu chính $$\sigma_D(x,\xi)=i\,c(\xi)$$ do đó cũng khả nghịch với nghịch đảo $$i\,c(\xi)/|\xi|^2$$ (kiểm tra: $$(i\,c(\xi))\cdot (i\,c(\xi)/|\xi|^2) = -c(\xi)^2/|\xi|^2 = \operatorname{Id}$$). Việc ký hiệu chính khả nghịch ngoài lát cắt không đúng là định nghĩa tính elliptic bậc $$1$$. Suy ra toán tử Dirac có parametrix thuộc $$\Psi^{-1}$$, và theo tính chính quy elliptic (Bài 15.09), nếu $$Du$$ trơn thì $$u$$ trơn.

Công thức Lichnerowicz $$D^2=\nabla^*\nabla+\operatorname{Scal}/4$$ là một đồng nhất thức của liên thông tương thích trên bó spinor (không phải chứng minh của định lý chỉ số), thu được bằng cách khai triển $$D^2$$ thành toán tử Laplace thô cộng các số hạng độ cong Riemann rồi dùng đồng nhất thức Bianchi để rút gọn thành $$\operatorname{Scal}/4$$. Định lý Atiyah–Singer vượt ngoài phạm vi chứng minh của bài học này.

## Ví dụ có lời giải

### Ví dụ 1: Toán tử Hodge–Dirac trên các dạng vi phân

Xét

$$
D_{\mathrm{dR}}=d+d^*.
$$

Khi bình phương (do $$d^2=0$$ và $$(d^*)^2=0$$), ta được

$$
D_{\mathrm{dR}}^2=dd^*+d^*d=\Delta_H.
$$

Ví dụ này là điểm khởi đầu thuận lợi khi chưa quen với spinor: nó cho thấy một toán tử bậc nhất tự nhiên có bình phương bằng toán tử Laplace, đồng thời hạt nhân của $$D_{\mathrm{dR}}$$ chính là không gian các dạng điều hòa gắn trực tiếp với đối đồng điều de Rham.

### Ví dụ 2: Toán tử Dirac phẳng trên $$\mathbb{R}^n$$

Trên không gian phẳng với các ma trận Clifford hằng,

$$
D=\sum_{j=1}^n c(e_j)\partial_{x_j}.
$$

Khi khai triển $$D^2$$, các đạo hàm hỗn hợp đi kèm hệ số

$$
c(e_j)c(e_k)+c(e_k)c(e_j),
$$

triệt tiêu với mọi $$j\neq k$$. Các số hạng đường chéo cho

$$
D^2=\sum_{j=1}^n c(e_j)^2\partial_{x_j}^2
=-\sum_{j=1}^n \partial_{x_j}^2 \operatorname{Id}
=-\Delta \operatorname{Id}.
$$

Phép tính cơ bản này cho thấy chính quan hệ phản giao hoán giúp bình phương của toán tử bậc nhất quy về toán tử vô hướng bậc hai.

### Ví dụ 3: Hệ quả của độ cong vô hướng dương

Giả sử $$M$$ là đa tạp spin compact và $$D\psi=0$$. Theo công thức Lichnerowicz,

$$
0=\langle D^2\psi,\psi\rangle
=\|\nabla\psi\|^2+\frac14\int_M \operatorname{Scal}\,|\psi|^2.
$$

Nếu $$\operatorname{Scal}>0$$ tại mọi điểm, cả hai số hạng ở vế phải đều không âm và có tổng bằng 0, buộc $$\psi=0$$. Ví dụ này minh họa cách một lập luận giải tích ngắn gọn có thể rút ra cản trở hình học toàn cục.

### Ví dụ 4: Mode Fourier trên hình xuyến phẳng

Trên hình xuyến phẳng, xét mode spinor

$$
\psi_k(x)=e^{i k\cdot x}u,
$$

với $$k\in \mathbb{Z}^n$$ và $$u$$ là spinor hằng. Khi đó

$$
D\psi_k = i\,c(k)e^{i k\cdot x}u.
$$

Vì các trị riêng của ma trận $$c(k)$$ có môđun bằng $$|k|$$, phổ của toán tử Dirac phản ánh trực tiếp mạng tần số của đa tạp phẳng, kết nối với giải tích Fourier và tiệm cận phổ.

## Câu hỏi khái niệm

1. Vì sao trong nhiều bài toán, toán tử bậc nhất như toán tử Dirac lại lưu giữ nhiều thông tin hình học hơn toán tử bậc hai?
2. Vì sao quan hệ Clifford $$c(\xi)^2=-|\xi|^2\operatorname{Id}$$ quyết định trực tiếp tính elliptic của toán tử Dirac?
3. Việc xuất hiện số hạng độ cong khi bình phương toán tử Dirac cho thấy điều gì về mối liên hệ giữa hình học và giải tích?
4. Vì sao định lý chỉ số Atiyah–Singer được coi là cầu nối căn bản giữa PDE và tôpô?

## Bài toán ứng dụng

1. Hãy so sánh $$D_{\mathrm{dR}}=d+d^*$$ với toán tử Laplace–Hodge và giải thích vì sao bài toán dạng điều hòa vừa thuộc PDE vừa thuộc tôpô.
2. Trong mô hình electron tương đối tính, vì sao phương trình bậc nhất mang lại nhiều thông tin hơn chỉ phương trình bậc hai Klein–Gordon?
3. Nếu một đa tạp spin compact có độ cong vô hướng dương tại mọi điểm, điều này kéo theo kết luận gì về các spinor điều hòa và chỉ số giải tích của $$D^+$$?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Nếu chỉ biết $$D^2$$ mà không biết $$D$$, ta mất đi những thông tin hình học nào?
- Vì sao một toán tử bậc nhất vẫn tạo ra tính chính quy tương đương với toán tử Laplace?
- Điểm khác biệt về bản chất giữa công thức Lichnerowicz và định lý chỉ số Atiyah–Singer là gì?

### Hoạt động gợi ý

- Cho sinh viên tự khai triển bình phương của $$D=\sum c(e_j)\partial_{x_j}$$ để quan sát các số hạng chéo triệt tiêu.
- Chia lớp thành hai nhóm: một nhóm trình bày nguồn gốc vật lý của phương trình Dirac, nhóm kia trình bày góc nhìn hình học qua Hodge–Dirac và spinor.
- Vẽ sơ đồ liên kết $$D$$, $$D^2$$, độ cong, hạt nhân và chỉ số rồi giải thích từng mối nối bằng lời.

### Cách tăng mức độ tham gia

- Mở đầu bằng câu hỏi: “Làm sao lấy căn bậc hai bậc nhất của toán tử Laplace mà vẫn giữ được ý nghĩa hình học?”
- Đề nghị sinh viên dự đoán nguồn gốc của tính elliptic trước khi viết quan hệ Clifford.
- Liên hệ nội dung bài với cơ học lượng tử, lý thuyết elliptic vi địa phương và tiệm cận phổ.

## Ghi nhớ nhanh

Toán tử Dirac là toán tử elliptic bậc nhất được xây dựng từ phép nhân Clifford và liên thông tương thích, xuất phát từ cả vật lý tương đối tính lẫn hình học dạng vi phân và spinor. Tính elliptic đến từ quan hệ phản giao hoán, bình phương của nó cho toán tử kiểu Laplace cộng số hạng độ cong, còn chỉ số giải tích của nó kết nối trực tiếp PDE với tôpô toàn cục.

---

## Ứng dụng thực tế

### 1. Cơ học lượng tử tương đối tính và hạt spin-$$\frac12$$

Phương trình Dirac là mô hình nền tảng cho electron tương đối tính (trong chế độ một hạt tương đối tính, chưa xét đầy đủ lý thuyết trường lượng tử). Cấu trúc toán tử bậc nhất, tự liên hợp với phổ đối xứng cho thấy spin không phải yếu tố bổ sung bên ngoài mà xuất hiện trực tiếp từ phép phân tích nhân tử của toán tử.

### 2. Hình học độ cong và bài toán độ cong vô hướng dương

Công thức Lichnerowicz biến toán tử Dirac thành công cụ chứng minh các định lý không tồn tại metric có độ cong vô hướng dương trên nhiều đa tạp spin đóng. Ở đây, PDE đóng vai trò công cụ phát hiện các cản trở hình học–tôpô toàn cục.

### 3. Vật liệu Dirac và nón phổ

Trong graphene và một số vật liệu tôpô, mô hình hiệu dụng gần điểm Dirac có hệ thức tán sắc tuyến tính thay vì bậc hai, tạo nên “nón Dirac” (Dirac cone) trong không gian xung lượng. Dù không phải toán tử Dirac hình học trên đa tạp cong, mô hình này chia sẻ cùng cấu trúc bậc nhất, giá trị spinor và phổ tuyến tính quanh điểm đặc biệt.

## Trực giác sâu hơn

Có thể xem toán tử Laplace đo độ cong bậc hai của trường, còn toán tử Dirac là đạo hàm có hướng gắn với cấu trúc spin. Khi bình phương, nó vừa khôi phục phần khuếch tán kiểu Laplace vừa giữ lại thông tin về liên thông và độ cong. Vì vậy, toán tử Dirac vừa đủ tính giải tích để áp dụng lý thuyết elliptic, vừa đủ tinh để phát hiện các bất biến tôpô.

Trong toán học hiện đại, toán tử Dirac không chỉ là đối tượng của vật lý mà là khuôn mẫu chuẩn cho cả lớp toán tử kiểu Dirac, đóng vai trò trung tâm trong nhiều định lý liên kết độ cong với hạt nhân của toán tử vi phân.

## Trực quan hóa bằng Python

Đoạn mã sau vẽ hai nhánh phổ của ký hiệu Dirac phẳng hai chiều có khối lượng $$m$$:

```python
import numpy as np
import matplotlib.pyplot as plt

xi1 = np.linspace(-3, 3, 220)
xi2 = np.linspace(-3, 3, 220)
XI1, XI2 = np.meshgrid(xi1, xi2)
m = 1.0

E = np.sqrt(XI1**2 + XI2**2 + m**2)

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

ax1.plot_surface(XI1, XI2, E, cmap='viridis', linewidth=0, antialiased=True)
ax1.set_title("Nhanh duong: +sqrt(|xi|^2 + m^2)")
ax1.set_xlabel("xi1")
ax1.set_ylabel("xi2")

ax2.plot_surface(XI1, XI2, -E, cmap='plasma', linewidth=0, antialiased=True)
ax2.set_title("Nhanh am: -sqrt(|xi|^2 + m^2)")
ax2.set_xlabel("xi1")
ax2.set_ylabel("xi2")

plt.tight_layout()
plt.show()
```

Đồ thị cho thấy trực quan hình dạng “nón Dirac” với hệ thức tán sắc tuyến tính khi $$m=0$$.

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để vẽ đồng thời hai mặt $$\pm \sqrt{\xi_1^2+\xi_2^2+m^2}$$ kèm thanh trượt điều chỉnh $$m$$: khi $$m\to 0$$, khe phổ đóng lại tại gốc tọa độ; khi $$m>0$$, hai nhánh tách nhau bởi một khoảng trống phổ.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Dirac operator intuition`, `Lichnerowicz formula visualization`, `Atiyah Singer Dirac operator introduction`, hoặc `graphene Dirac cone animation`.

## Bài tập

1. Từ $$c(\xi)^2=-|\xi|^2\operatorname{Id}$$, viết nghịch đảo tường minh của $$c(\xi)$$ khi $$\xi\neq 0$$, rồi suy ra nghịch đảo của $$\sigma_D(x,\xi)=i\,c(\xi)$$ và kết luận tính elliptic bậc $$1$$.
2. Trên $$\mathbb{R}^n$$ với các ma trận Clifford hằng, khai triển $$D=\sum_j c(e_j)\partial_{x_j}$$ và kiểm chứng $$D^2=-\Delta\operatorname{Id}$$ nhờ quan hệ phản giao hoán.
3. Từ công thức Lichnerowicz, nếu $$M$$ là đa tạp spin đóng có $$\operatorname{Scal}>0$$ và $$D\psi=0$$, hãy chứng minh $$\psi=0$$ bằng cách lấy tích vô hướng $$L^2$$ (lưu ý đây là đồng nhất thức của liên thông, không phải định lý chỉ số).
4. Với toán tử Hodge–Dirac $$D_{\mathrm{dR}}=d+d^*$$: kiểm chứng $$D_{\mathrm{dR}}^2=\Delta_H$$ và giải thích tính elliptic từ ký hiệu chính của $$d+d^*$$.
5. Giải thích vì sao $$\sigma_D$$ thuần nhất bậc $$1$$, so sánh bậc của $$D^2$$ với toán tử Laplace, và nêu hệ quả định luật Weyl: $$N(\Lambda)\sim C\Lambda^{n}$$ cho $$|D|$$ (bậc $$1$$) thay vì $$\Lambda^{n/2}$$.

## Tài liệu tham khảo

- L. Hörmander, *The Analysis of Linear Partial Differential Operators III*: tính elliptic, ký hiệu chính và tính chính quy cho các hệ bậc nhất kiểu Dirac.
- M. Taylor, *Pseudodifferential Operators and Nonlinear PDE*: ký hiệu của toán tử bậc nhất trên phân thớ và parametrix elliptic, đủ để tiếp cận $$D$$ như một hệ elliptic.

## Điều kiện Biên Toàn cục Atiyah–Patodi–Singer (APS)

Khi đa tạp $$X$$ có biên $$Y = \partial X$$, gần biên ta viết toán tử Dirac dưới dạng trụ $$D_X = \sigma(dt)\left(\frac{\partial}{\partial t} + D_Y\right)$$, trong đó $$A_Y = \sigma(dt)^{-1} D_Y$$ là toán tử Dirac tự liên hợp trên biên $$Y$$ với phân rã phổ $$\bigoplus_{\lambda \in \operatorname{spec}(A_Y)} E_\lambda$$. Khác với điều kiện biên địa phương kiểu Dirichlet/Neumann, bài toán biên elliptic cho toán tử Dirac đòi hỏi **điều kiện biên toàn cục Atiyah–Patodi–Singer (APS)**: triệt tiêu các mode ứng với trị riêng $$\lambda \ge 0$$ trên biên $$Y$$, tạo nên bài toán Fredholm gắn liền với bất biến $\eta(0)$ đo độ bất đối xứng phổ.
