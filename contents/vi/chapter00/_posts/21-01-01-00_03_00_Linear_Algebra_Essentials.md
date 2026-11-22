---
layout: post
title: "00-04 Đại số Tuyến tính Cơ bản"
chapter: '00'
order: 4
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---

## Mục tiêu
Bài học này giúp sinh viên củng cố các kiến thức cốt lõi của đại số tuyến tính gồm trị riêng, vector riêng, phép chéo hóa và dạng toàn phương. Qua đó, sinh viên hiểu cách đại số tuyến tính cung cấp ngôn ngữ để giải và phân tích hệ phương trình vi phân tuyến tính, cũng như đánh giá tính ổn định của hệ thông qua phổ của ma trận hệ số.

## Kiến thức nền
Sinh viên cần nắm vững các phép toán ma trận cơ bản (cộng, nhân, tìm ma trận nghịch đảo), khái niệm không gian vector và cơ sở, cùng cách giải hệ phương trình tuyến tính bằng phép khử Gauss. Kiến thức về định thức và hạng ma trận cũng cần thiết.

## Dẫn nhập
Khi mở rộng từ một phương trình vi phân đơn lẻ sang hệ nhiều phương trình—chẳng hạn mô hình hệ sinh thái hai loài, mạch điện hai vòng hoặc hệ dao động ghép—ta cần đến đại số tuyến tính. Hệ $$ x' = Ax $$, trong đó $$ x $$ là vector trạng thái và $$ A $$ là ma trận hệ số, là đối tượng trung tâm khi nghiên cứu hệ phương trình vi phân tuyến tính.

Có thể hình dung hệ hai phương trình như sự chuyển động đồng thời của hai đại lượng biểu diễn bởi vector $$ x = (x_1, x_2) $$. Ma trận $$ A $$ quy định cách tốc độ biến thiên của mỗi thành phần phụ thuộc vào giá trị của cả hai thành phần. Nếu chọn được hệ tọa độ thích hợp theo các vector riêng, hệ phương trình sẽ tách rời và trở nên đơn giản hơn: mỗi thành phần tăng giảm hoặc dao động độc lập theo quy luật riêng.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Một ma trận $$ 2\times 2 $$ có thể xem như một phép biến đổi tuyến tính trên mặt phẳng: nó co giãn, xoay hoặc lật các vector. Vector riêng là những phương đặc biệt mà phép biến đổi chỉ làm co giãn độ dài (hoặc đổi chiều) chứ không làm lệch phương. Trị riêng cho biết hệ số co giãn theo phương đó: trị riêng thực dương kéo dài hoặc thu ngắn cùng chiều, trị riêng thực âm làm đảo chiều, còn trị riêng phức gắn với thành phần xoay (dao động).

### Cách nhìn hình ảnh
Xét phép biến đổi ứng với ma trận $$A = \begin{pmatrix}2 & 1 \\ 0 & 1\end{pmatrix}$$. Vector $$ v_1 = (1,0) $$ là vector riêng ứng với trị riêng $$ \lambda_1 = 2 $$ nên bị kéo dài gấp đôi; vector $$ v_2 = (1,-1) $$ là vector riêng ứng với trị riêng $$ \lambda_2 = 1 $$ nên giữ nguyên độ dài và hướng. Khi tác động ma trận $$ A $$ nhiều lần, các vector không nằm trên phương $$ v_2 $$ đều có xu hướng nghiêng dần về phương $$ v_1 $$.

### Cách nhìn hình thức
**Trị riêng và vector riêng**: Cho $$ A \in \mathbb{R}^{n\times n} $$. Số $$ \lambda $$ là trị riêng của $$ A $$ nếu tồn tại vector $$ v \neq 0 $$ sao cho $$ Av = \lambda v $$. Vector $$ v $$ gọi là vector riêng ứng với $$ \lambda $$. Phương trình đặc trưng của $$ A $$ là $$ \det(A - \lambda I) = 0 $$.

**Phép chéo hóa**: Nếu $$ A $$ có $$ n $$ vector riêng độc lập tuyến tính, ta viết được $$ A = PDP^{-1} $$ với $$D = \operatorname{diag}(\lambda_1,\ldots,\lambda_n)$$. Khi đó $$ A^k = PD^kP^{-1} $$, giúp việc tính lũy thừa ma trận trở nên trực tiếp.

**Hệ $$ x' = Ax $$**: Khi $$ A $$ chéo hóa được, nghiệm tổng quát có dạng $$x(t) = c_1 e^{\lambda_1 t}v_1 + \cdots + c_n e^{\lambda_n t}v_n$$. Hành vi của nghiệm phụ thuộc trực tiếp vào phổ (tập các trị riêng) của $$ A $$.

**Dạng toàn phương**: Biểu thức $$ Q(x) = x^T A x $$ thường được dùng khi xây dựng hàm Lyapunov để phân tích tính ổn định.

## Những ngộ nhận thường gặp
- "Chỉ ma trận đối xứng mới có trị riêng thực." Sai. Ma trận đối xứng thực luôn có trị riêng thực, nhưng ma trận không đối xứng vẫn có thể có toàn bộ trị riêng thực (chẳng hạn ma trận tam giác thực).
- "Có một trị riêng âm là đủ để hệ ổn định." Sai. Để hệ $$ x' = Ax $$ ổn định tiệm cận, phần thực của tất cả các trị riêng đều phải âm; chỉ cần một trị riêng có phần thực dương là hệ sẽ mất ổn định.
- "Vector riêng ứng với mỗi trị riêng là duy nhất." Sai. Ngay cả với trị riêng đơn, mọi bội khác $$ 0 $$ của một vector riêng đều là vector riêng (chỉ xác định duy nhất một phương). Với trị riêng bội, không gian riêng có thể có số chiều lớn hơn 1.
- "Mọi ma trận vuông đều chéo hóa được." Sai. Một ma trận chỉ chéo hóa được khi nó có đủ $$ n $$ vector riêng độc lập tuyến tính (chẳng hạn khi có $$ n $$ trị riêng phân biệt, hoặc khi bội hình học bằng bội đại số đối với mọi trị riêng).

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại phương trình đặc trưng
Nắm rõ $$ \det(A - \lambda I) = 0 $$ là phương trình đại số bậc $$ n $$ có nghiệm là các trị riêng của $$ A $$. Riêng với ma trận $$ 2\times 2 $$, phương trình đặc trưng có dạng gọn: $$\lambda^2 - \operatorname{tr}(A)\lambda + \det(A) = 0$$.

### Bước 2: Tìm vector riêng và hiểu không gian riêng
Với mỗi trị riêng $$ \lambda $$, giải hệ thuần nhất $$ \left(A - \lambda I\right)v = 0 $$ để tìm không gian riêng $$ E_\lambda $$, nhận biết đây là một không gian vector con có số chiều ít nhất bằng 1.

### Bước 3: Giải hệ $$ x' = Ax $$
Dùng công thức nghiệm theo trị riêng và vector riêng để phân tích hành vi hệ: mọi trị riêng có phần thực âm $$ \Rightarrow $$ ổn định tiệm cận; tồn tại trị riêng có phần thực dương $$ \Rightarrow $$ không ổn định; các trị riêng thuần ảo (không bội) $$ \Rightarrow $$ dao động tuần hoàn (ổn định trung tính).

### Các checkpoint
- Bạn có tính được trị riêng và vector riêng của một ma trận $$ 2\times 2 $$ không?
- Bạn có phân tích được tính ổn định của hệ $$ x' = Ax $$ dựa trên phổ của $$ A $$ không?
- Bạn có xác định được khi nào một ma trận chéo hóa được không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Trị riêng và vector riêng của ma trận $$ 2\times 2 $$
Cho $$A = \begin{pmatrix}3 & 1 \\ 1 & 2\end{pmatrix}$$. Phương trình đặc trưng là

$$
\det(A - \lambda I) = (3-\lambda)(2-\lambda) - 1 = \lambda^2 - 5\lambda + 5 = 0.
$$

Các trị riêng là $$ \lambda = \frac{5 \pm \sqrt{5}}{2} $$. Với $$ \lambda_1 = \frac{5+\sqrt{5}}{2} $$, giải hệ $$ \left(A - \lambda_1 I\right)v = 0 $$, ta thu được một vector riêng là $$v_1 = \left(1,\lambda_1 - 3\right) = \left(1,\frac{\sqrt{5}-1}{2}\right)$$. Thực hiện tương tự cho $$ \lambda_2 $$.

### Ví dụ 2: Hệ $$ x' = Ax $$ với trị riêng thực phân biệt
Cho $$A = \begin{pmatrix}2 & 0 \\ 0 & -1\end{pmatrix}$$. Các trị riêng là $$ \lambda_1 = 2 $$ và $$ \lambda_2 = -1 $$, tương ứng với các vector riêng $$ v_1 = (1,0) $$ và $$ v_2 = (0,1) $$. Nghiệm tổng quát là $$ x(t) = c_1 e^{2t}(1,0) + c_2 e^{-t}(0,1) $$. Thành phần thứ nhất tăng theo hàm mũ còn thành phần thứ hai suy giảm về $$ 0 $$; điểm cân bằng $$ \left(0,0\right) $$ là điểm yên ngựa.

### Ví dụ 3: Hệ $$ x' = Ax $$ với trị riêng phức
Cho $$A = \begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix}$$. Phương trình đặc trưng là $$ \lambda^2 + 1 = 0 $$, cho các trị riêng thuần ảo $$ \lambda = \pm i $$. Nghiệm tổng quát có dạng $$ x(t) = c_1(\cos t,\sin t) + c_2(-\sin t,\cos t) $$. Quỹ đạo pha là các đường tròn đồng tâm quanh gốc tọa độ, tương ứng với dao động điều hòa không tắt dần.

### Ví dụ 4: Ma trận không chéo hóa được
Cho $$A = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$$. Ma trận có trị riêng duy nhất $$ \lambda = 1 $$ với bội đại số $$ 2 $$, nhưng không gian riêng chỉ có một chiều nên không chéo hóa được. Nghiệm tổng quát của $$ x' = Ax $$ có dạng $$ x(t) = e^t(c_1 + c_2 t, c_2) $$, trong đó số hạng $$ t e^t $$ xuất hiện do thiếu một vector riêng độc lập tuyến tính.

### Ví dụ 5: Phân tích ổn định
Xét hệ $$ x' = Ax $$ với $$A = \begin{pmatrix}-2 & 1 \\ 1 & -2\end{pmatrix}$$. Phương trình đặc trưng là

$$
\det(A - \lambda I) = (\lambda + 2)^2 - 1 = \lambda^2 + 4\lambda + 3 = 0,
$$

cho hai trị riêng $$ \lambda = -1 $$ và $$ \lambda = -3 $$. Vì cả hai đều âm, điểm cân bằng $$ \left(0,0\right) $$ ổn định tiệm cận và mọi nghiệm đều tiến về $$ \left(0,0\right) $$ khi $$ t \to \infty $$.

## Câu hỏi khái niệm
1. Vì sao phổ của ma trận (tập các trị riêng) quyết định hành vi dài hạn của nghiệm hệ $$ x' = Ax $$?
2. Khi nào một ma trận không chéo hóa được, và điều đó làm thay đổi dạng nghiệm của hệ $$ x' = Ax $$ như thế nào?
3. Với cặp trị riêng phức $$ \lambda = \alpha \pm i\beta $$, vì sao phần thực $$ \alpha $$ quyết định tính ổn định còn phần ảo $$ \beta $$ quyết định tần số dao động?

## Bài toán ứng dụng
1. **Vật lý — Dao động tắt dần**: Một hệ dao động tắt dần có ma trận hệ số với các trị riêng đều có phần thực âm. Hãy giải thích ý nghĩa vật lý của điều này đối với biên độ dao động và trạng thái cân bằng.
2. **Sinh học — Hệ cạnh tranh**: Trong mô hình hai loài cạnh tranh, nếu ma trận Jacobi tại điểm cân bằng cùng tồn tại có tất cả trị riêng với phần thực âm, hãy giải thích ý nghĩa sinh thái của kết quả đó.
3. **Kinh tế — Mô hình tăng trưởng**: Xét hệ phương trình tuyến tính mô tả tích lũy vốn và lao động. Hãy phân tích ý nghĩa của chế độ trị riêng có phần thực dương so với trị riêng có phần thực âm.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Phân loại trị riêng"**: Cho trước các ma trận $$ A $$, yêu cầu sinh viên tìm trị riêng và phác họa chân dung pha tương ứng.
- **Thảo luận nhóm**: Giao cho mỗi nhóm một hệ $$ x' = Ax $$ để phân tích trọn vẹn: tìm trị riêng, vector riêng, viết nghiệm tổng quát, vẽ quỹ đạo và kết luận về tính ổn định.
- **Câu hỏi nhanh**: "Nếu $$A = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$$ thì các trị riêng là gì và nghiệm của hệ $$ x' = Ax $$ có dạng ra sao?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Bắt đầu với các ma trận $$ 2\times 2 $$ để tập trung vào bản chất khái niệm thay vì khối lượng tính toán.
- Sử dụng nhiều chân dung pha (phase portrait) trực quan song song với lập luận đại số.
- Luyện tập trước với các ma trận có cấu trúc đặc biệt như ma trận đường chéo, ma trận tam giác và ma trận đối xứng.

### Thử thách cho sinh viên khá giỏi
- Tìm hiểu dạng chuẩn Jordan và ứng dụng khi giải hệ $$ x' = Ax $$ với ma trận không chéo hóa được.
- Tìm hiểu phương pháp Lyapunov trong phân tích ổn định của hệ phi tuyến.
- So sánh phép chéo hóa với phân tích giá trị suy biến (SVD) và phạm vi ứng dụng của từng phương pháp.

## Tóm tắt dễ nhớ
- **Trị riêng $$ \lambda $$**: Nghiệm của phương trình đặc trưng $$ \det(A - \lambda I) = 0 $$.
- **Vector riêng $$ v $$**: Vector khác $$ 0 $$ không đổi phương qua phép biến đổi $$ A $$.
- **Nghiệm của $$ x' = Ax $$** (khi $$ A $$ chéo hóa được): $$ x(t) = \sum c_i e^{\lambda_i t} v_i $$.
- **Tiêu chuẩn ổn định**: Mọi $$ \operatorname{Re}(\lambda_i) < 0 $$ $$ \Rightarrow $$ ổn định tiệm cận; tồn tại $$ \operatorname{Re}(\lambda_i) > 0 $$ $$ \Rightarrow $$ không ổn định.
- Đại số tuyến tính giúp đọc trực tiếp hành vi của hệ ODE tuyến tính từ phổ của ma trận hệ số.

## Video tham khảo

- Xem trước: [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g) — 3Blue1Brown, tiếng Anh. Giải thích trực quan vector riêng là các phương mà phép biến đổi tuyến tính chỉ co giãn, nền tảng của cách giải $$ x'=Ax $$.
- [Vectors | Chapter 1, Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs) — 3Blue1Brown, tiếng Anh. Ôn tập vector và tổ hợp tuyến tính—ngôn ngữ mô tả vector trạng thái trong hệ phương trình cấp một.
- [How (and why) to raise e to the power of a matrix | DE6](https://www.youtube.com/watch?v=O85OWBJ2ayo) — 3Blue1Brown, tiếng Anh. Giải thích vì sao hàm mũ ma trận cho nghiệm dạng đóng của hệ tuyến tính hệ số hằng.

## Tài liệu tham khảo
- Axler — *Linear Algebra Done Right*: cách tiếp cận khái niệm rõ ràng và mạch lạc.
- Lay — *Linear Algebra and Its Applications*: nhiều ví dụ minh họa và ứng dụng thực tiễn.
- Hirsch, Smale & Devaney — *Differential Equations, Dynamical Systems, and an Introduction to Chaos*: kết nối trực tiếp đại số tuyến tính với hệ ODE.
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày ứng dụng trong chương hệ phương trình tuyến tính.
