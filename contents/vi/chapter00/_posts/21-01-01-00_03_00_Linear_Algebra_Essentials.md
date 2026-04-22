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
Bài học này giúp sinh viên củng cố nền tảng đại số tuyến tính, đặc biệt là các khái niệm về trị riêng, vector riêng, chéo hóa, và dạng toàn phương. Sinh viên sẽ hiểu cách đại số tuyến tính cung cấp ngôn ngữ để giải và phân tích hệ phương trình vi phân tuyến tính. Sau bài học, sinh viên có thể phân tích được tính ổn định của một hệ thông qua phổ của ma trận hệ số.

## Kiến thức nền
Sinh viên cần biết các phép toán ma trận cơ bản (cộng, nhân, nghịch đảo), hiểu khái niệm không gian vector và cơ sở, biết giải hệ phương trình tuyến tính bằng phương pháp Gauss. Kiến thức về định thức và hạng ma trận là cần thiết.

## Dẫn nhập
Khi ta mở rộng từ một phương trình vi phân sang hệ nhiều phương trình, ví dụ mô hình hóa hệ sinh thái hai loài, mạch điện hai vòng, hay hệ dao động ghép, ta cần đến đại số tuyến tính. Hệ $$ x' = Ax $$, trong đó $$ x $$ là vector và $$ A $$ là ma trận hệ số, là đối tượng trung tâm của chương này.

Hãy hình dung một hệ hai phương trình như một bản đồ giao thông. Vector $$ x = (x_1, x_2) $$ cho biết vị trí và hướng di chuyển của hai "xe" tại mỗi thời điểm. Ma trận $$ A $$ quyết định cách vận tốc của mỗi xe phụ thuộc vào vị trí của cả hai. Nếu ta chọn được "tọa độ đặc biệt", tức hệ vector riêng, thì hệ trở nên đơn giản hơn: mỗi thành phần dao động hoặc tăng giảm độc lập với nhau.

## Khái niệm theo ba cách

### Cách nhìn trực quan
Một ma trận $$ 2\times 2 $$ có thể được hình dung như một phép biến đổi hình học: nó co giãn, xoay, và lật mặt phẳng. Vector riêng là những hướng đặc biệt mà phép biến đổi chỉ co giãn theo một hướng mà không xoay. Trị riêng cho biết mức co giãn theo hướng đó. Nếu trị riêng dương, vector "bị kéo ra" theo hướng đó; nếu âm, bị "đẩy ngược"; nếu phức, có hiện tượng xoay, tức dao động.

### Cách nhìn hình ảnh
Vẽ phép biến đổi bởi ma trận $$A = \begin{pmatrix}2 & 1 \\ 0 & 1\end{pmatrix}$$. Vector $$ v_1 = (1,0) $$ là vector riêng với trị riêng $$ \lambda_1 = 2 $$: nó bị kéo dài gấp đôi. Vector $$ v_2 = (1,-1) $$ là vector riêng với trị riêng $$ \lambda_2 = 1 $$: nó không thay độ dài. Mọi vector khác đều bị kéo về hướng $$ v_1 $$ sau nhiều lần áp dụng $$ A $$.

### Cách nhìn hình thức
**Trị riêng, vector riêng**: Cho $$ A \in \mathbb{R}^{n\times n} $$. $$ \lambda $$ là trị riêng nếu tồn tại $$ v \neq 0 $$ sao cho $$ Av = \lambda v $$. Vector $$ v $$ tương ứng gọi là vector riêng. Phương trình đặc trưng là $$ \det(A - \lambda I) = 0 $$.

**Chéo hóa**: Nếu $$ A $$ có $$ n $$ vector riêng độc lập tuyến tính, ta có $$ A = PDP^{-1} $$ với $$D = \operatorname{diag}(\lambda_1,\ldots,\lambda_n)$$. Khi đó $$ A^k = PD^kP^{-1} $$, rất dễ tính.

**Hệ $$ x' = Ax $$**: Nghiệm có dạng $$x(t) = c_1 e^{\lambda_1 t}v_1 + \cdots + c_n e^{\lambda_n t}v_n$$. Hành vi nghiệm hoàn toàn được xác định bởi phổ, tức tập trị riêng, của $$ A $$.

**Dạng toàn phương**: $$ Q(x) = x^T A x $$, dùng để phân tích ổn định qua Lyapunov.

## Những ngộ nhận thường gặp
- "Ma trận đối xứng mới có trị riêng thực." Không đúng. Ma trận đối xứng luôn có trị riêng thực, nhưng ma trận không đối xứng vẫn có thể có trị riêng thực (ví dụ ma trận tam giác).
- "Trị riêng âm nghĩa là hệ ổn định." Chưa đủ. Cần TẤT CẢ phần thực của mọi trị riêng đều âm. Một trị riêng dương sẽ phá vỡ ổn định.
- "Vector riêng luôn duy nhất." Sai. Nếu có trị riêng đơn, vector riêng chỉ xác định được một hướng (nhân với hằng số). Nếu có trị riêng bội, không gian riêng có thể nhiều chiều.
- "Chéo hóa luôn được." Không đúng. Chỉ khi ma trận có đủ vector riêng độc lập tuyến tính (có n trị riêng phân biệt HOẶC ma trận chéo hóa được).

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại phương trình đặc trưng
Hiểu rằng $$ \det(A - \lambda I) = 0 $$ là phương trình đại số, và nghiệm của nó là trị riêng. Với ma trận $$ 2\times 2 $$, có thể tính trực tiếp: $$\lambda^2 - \operatorname{tr}(A)\lambda + \det(A) = 0$$.

### Bước 2: Tìm vector riêng và hiểu không gian riêng
Với mỗi trị riêng $$ \lambda $$, giải $$ \left(A - \lambda I\right)v = 0 $$ để tìm không gian riêng $$ E_\lambda $$. Hiểu rằng đây là không gian con một hoặc nhiều chiều.

### Bước 3: Giải hệ x' = Ax
Dùng công thức nghiệm qua trị riêng và vector riêng. Phân tích hành vi theo phổ: tất cả phần thực âm $$ \Rightarrow $$ ổn định; có một trị riêng với phần thực dương $$ \Rightarrow $$ không ổn định; thuần ảo $$ \Rightarrow $$ trung tính, tức dao động.

### Các checkpoint
- Sinh viên có tìm được trị riêng, vector riêng của ma trận $$ 2\times 2 $$ không?
- Sinh viên có phân tích được tính ổn định của hệ $$ x' = Ax $$ qua phổ không?
- Sinh viên có hiểu khi nào ma trận chéo hóa được không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Trị riêng, vector riêng của ma trận 2×2
Cho $$A = \begin{pmatrix}3 & 1 \\ 1 & 2\end{pmatrix}$$. Tính trị riêng:

$$
\det(A - \lambda I) = (3-\lambda)(2-\lambda) - 1 = \lambda^2 - 5\lambda + 5 = 0.
$$

Nghiệm là $$ \lambda = \frac{5 \pm \sqrt{5}}{2} $$. Với $$ \lambda_1 = \frac{5+\sqrt{5}}{2} $$, giải $$ \left(A - \lambda_1 I\right)v = 0 $$, ta được một vector riêng $$v_1 = \left(1,\lambda_1 - 3\right) = \left(1,\frac{\sqrt{5}-1}{2}\right)$$. Tương tự cho $$ \lambda_2 $$.

### Ví dụ 2: Hệ x' = Ax với trị riêng thực phân biệt
Cho $$A = \begin{pmatrix}2 & 0 \\ 0 & -1\end{pmatrix}$$. Trị riêng là $$ \lambda_1 = 2 $$, $$ \lambda_2 = -1 $$. Vector riêng tương ứng là $$ v_1 = (1,0) $$, $$ v_2 = (0,1) $$. Nghiệm có dạng $$ x(t) = c_1 e^{2t}(1,0) + c_2 e^{-t}(0,1) $$. Thành phần thứ nhất tăng theo hàm mũ, thành phần thứ hai giảm về $$ 0 $$. Điểm cân bằng $$ \left(0,0\right) $$ là yên ngựa.

### Ví dụ 3: Hệ x' = Ax với trị riêng phức
Cho $$A = \begin{pmatrix}0 & -1 \\ 1 & 0\end{pmatrix}$$. Phương trình đặc trưng là $$ \lambda^2 + 1 = 0 $$, nên $$ \lambda = \pm i $$. Đây là dao động thuần túy. Nghiệm có dạng $$ x(t) = c_1(\cos t,\sin t) + c_2(-\sin t,\cos t) $$. Quỹ đạo là đường tròn quanh gốc.

### Ví dụ 4: Ma trận không chéo hóa được
Cho $$A = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$$. Trị riêng duy nhất là $$ \lambda = 1 $$ với bội đại số $$ 2 $$. Không gian riêng của nó chỉ có một chiều, nên ma trận không chéo hóa được. Nghiệm vì thế có dạng $$ x(t) = e^t(c_1 + c_2 t, c_2) $$. Số hạng $$ t e^t $$ xuất hiện chính vì thiếu vector riêng.

### Ví dụ 5: Phân tích ổn định
Cho hệ $$ x' = Ax $$ với $$A = \begin{pmatrix}-2 & 1 \\ 1 & -2\end{pmatrix}$$. Ta có

$$
\det(A - \lambda I) = (\lambda + 2)^2 - 1 = \lambda^2 + 4\lambda + 3 = 0,
$$

nên $$ \lambda = -1, -3 $$. Cả hai đều âm, nên điểm cân bằng ổn định tiệm cận. Mọi nghiệm đều tiến về $$ \left(0,0\right) $$ khi $$ t \to \infty $$.

## Câu hỏi khái niệm
1. Tại sao phổ của ma trận, tức tập trị riêng, lại quyết định hoàn toàn hành vi nghiệm của hệ $$ x' = Ax $$?
2. Khi nào ma trận không chéo hóa được? Điều này ảnh hưởng như thế nào đến dạng nghiệm?
3. Trị riêng phức $$ \lambda = \alpha \pm i\beta $$ tạo ra dao động. Tại sao phần thực $$ \alpha $$ quyết định ổn định, còn phần ảo $$ \beta $$ quyết định tần số dao động?

## Bài toán ứng dụng
1. **Vật lý - Dao động tắt dần**: Hệ dao động cưỡng bức có ma trận với trị riêng âm cho biết hệ sẽ ổn định và dao động tắt dần. Giải thích ý nghĩa.
2. **Sinh học - Hệ cạnh tranh**: Mô hình hai loài cạnh tranh. Ma trận Jacobian tại điểm cân bằng có trị riêng âm $$ \Rightarrow $$ cả hai loài cùng tồn tại ổn định.
3. **Kinh tế - Mô hình tăng trưởng**: Hệ phương trình cho tích lũy vốn và lao động. Trị riêng dương cho biết tăng trưởng bền vững, trị riêng âm cho suy thoái.

## Chiến lược giảng dạy tương tác
- **Hoạt động "Phân loại trị riêng"**: Cho ma trận $$ A $$, yêu cầu sinh viên tìm trị riêng và vẽ sơ đồ pha tương ứng.
- **Thảo luận nhóm**: Cho mỗi nhóm một hệ $$ x' = Ax $$ và yêu cầu phân tích đầy đủ: tìm trị riêng, vector riêng, viết nghiệm, vẽ quỹ đạo, xác định tính ổn định.
- **Câu hỏi nhanh**: "Nếu $$A = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$$ thì trị riêng là gì? Hệ $$ x' = Ax $$ có nghiệm gì?".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
- Bắt đầu với ma trận 2×2 để tránh tính toán cồng kềnh.
- Vẽ nhiều phase portrait (đồ thị pha) trực quan hơn là chứng minh trừu tượng.
- Luyện tập với các ma trận có dạng đặc biệt: diagonal, tam giác, đối xứng.

### Thử thách cho sinh viên khá giỏi
- Nghiên cứu và trình bày về dạng Jordan và ứng dụng trong ODE.
- Tìm hiểu về phương pháp Lyapunov cho ổn định phi tuyến.
- So sánh chéo hóa với phân tích giá trị suy biến (SVD) và ứng dụng.

## Tóm tắt dễ nhớ
**Trị riêng $$ \lambda $$**: Nghiệm của $$ \det(A - \lambda I) = 0 $$.
**Vector riêng $$ v $$**: Hướng không đổi bởi phép biến đổi $$ A $$.
**Nghiệm của $$ x' = Ax $$**: $$ x(t) = \sum c_i e^{\lambda_i t} v_i $$.
**Ổn định**: Tất cả $$ \operatorname{Re}(\lambda_i) < 0 $$ $$ \Rightarrow $$ ổn định; có một $$ \operatorname{Re}(\lambda_i) > 0 $$ $$ \Rightarrow $$ không ổn định.
Đại số tuyến tính cho ta "thấu kính" để phân tích hệ ODE: nhìn vào phổ là thấy toàn bộ hành vi nghiệm.

## Tài liệu tham khảo
- Axler — *Linear Algebra Done Right*: tiếp cận trừu tượng nhưng rõ ràng.
- Lay — *Linear Algebra and Its Applications*: nhiều ví dụ và ứng dụng.
- Hirsch, Smale & Devaney — *Differential Equations, Dynamical Systems, and an Introduction to Chaos*: liên hệ trực tiếp với ODE.
- Boyce & DiPrima — *Elementary Differential Equations*: ứng dụng trong chương hệ tuyến tính.
