---
layout: post
title: "Đạo Hàm Yếu"
chapter: '12'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: required
---

![Đạo hàm yếu được hiểu qua tích phân từng phần]({{ site.imgurl }}/chapter_img/chapter12/02_weak_derivatives.svg )

Một sợi dây đàn bị gảy kéo căng thành hình tam giác nhọn tại giữa dây: rõ ràng nó là trạng thái vật lý hoàn toàn hợp lệ, nhưng tại đỉnh tam giác, đạo hàm cổ điển $u'(x)$ **không tồn tại**! Làm sao giải phương trình sóng hay phương trình đàn hồi cho những hình dạng có góc gãy như thế? Sergei Sobolev đã nghĩ ra một cú xoay chuyển tuyệt diệu: thay vì lấy giới hạn tỷ số sai phân tại từng điểm, hãy **đẩy phép đạo hàm sang một hàm thử trơn vô hạn $\varphi$** thông qua công thức tích phân từng phần!

## Kiến thức cần nhớ: Bốn trụ cột của Đạo hàm Yếu (Weak Derivative)

1. **Công thức Tích phân Từng phần làm Định nghĩa**:
   Hàm $v \in L^1_{\text{loc}}(\Omega)$ là đạo hàm yếu bậc $\alpha$ của $u$ nếu với mọi hàm thử $\varphi \in C_c^\infty(\Omega)$:
   $$\int_\Omega u\, D^\alpha \varphi\,dx = (-1)^{|\alpha|} \int_\Omega v\, \varphi\,dx.$$
   Vì $\varphi$ triệt tiêu gần biên $\partial\Omega$, mọi số hạng biên đều tự động biến mất!
2. **Tính nhất quán và Tính duy nhất (a.e.)**:
   Nếu $u$ khả vi cổ điển thì đạo hàm yếu trùng khít với đạo hàm cổ điển; và nếu đạo hàm yếu tồn tại, nó là **duy nhất hầu khắp nơi** (nhờ bổ đề cơ bản của phép tính biến phân).
3. **Góc gãy (liên tục) có Đạo hàm Yếu; Bước nhảy (gián đoạn) thì KHÔNG**:
   Hàm có góc gãy như $|x|$ có đạo hàm yếu là hàm bậc thang $\operatorname{sgn}(x) \in L^\infty$. Ngược lại, hàm bậc thang Heaviside $H(x)$ có đạo hàm là $\delta_0$—không phải một hàm khả tích địa phương, nên $H(x)$ **không có đạo hàm yếu dạng hàm**!
4. **Quy tắc tính toán quen thuộc vẫn sống sót**:
   Tính tuyến tính, quy tắc tích (với hàm trơn) và quy tắc đạo hàm hàm hợp (với hàm Lipschitz) đều giữ nguyên cho đạo hàm yếu, tạo nền tảng để xây dựng không gian Sobolev $W^{k,p}$.

## Mục tiêu

Bài học này giúp sinh viên hiểu vì sao cần khái niệm đạo hàm yếu, cách định nghĩa đạo hàm yếu thông qua hàm thử, và vì sao đây là bước chuyển quan trọng từ giải tích cổ điển sang lý thuyết PDE hiện đại. Sau bài học, sinh viên cần tính được một số đạo hàm yếu cơ bản và giải thích được mối liên hệ giữa đạo hàm yếu, tích phân từng phần và nghiệm yếu.

## Kiến thức nền

Sinh viên cần nắm đạo hàm cổ điển, tích phân từng phần, hàm trơn có giá compact và cách tiếp cận hàm thông qua tích phân thay vì giá trị tại từng điểm. Hiểu sơ bộ về không gian $$ L^1_{\mathrm{loc}} $$ cũng hữu ích vì đạo hàm yếu không đòi hỏi hàm phải trơn.

## Dẫn nhập

Trong nhiều bài toán thực tế, nghiệm không trơn mà có thể xuất hiện góc nhọn, điểm gãy hoặc thay đổi đột ngột. Nếu giữ chặt khái niệm đạo hàm cổ điển, ta sẽ phải loại bỏ các hàm này vì chúng không khả vi tại mọi điểm.

Đạo hàm yếu khắc phục hạn chế đó bằng cách không tính trực tiếp độ dốc tại từng điểm mà khảo sát cách hàm tương tác với mọi hàm thử trơn. Thông qua tích phân từng phần, phép lấy đạo hàm được chuyển sang hàm thử; nếu đẳng thức tích phân vẫn đúng với mọi hàm thử, ta xác định được đạo hàm theo nghĩa rộng hơn.


### Giải thích: Tính từng bước đạo hàm yếu của hàm giá trị tuyệt đối $u(x) = |x|$ trên $(-1, 1)$

Xét $u(x) = |x|$ trên $\Omega = (-1, 1)$ và lấy một hàm thử bất kỳ $\varphi \in C_c^\infty(-1, 1)$ (nên $\varphi(-1) = \varphi(1) = 0$):
1. **Tách tích phân tại điểm gãy $x = 0$**:
   $$\int_{-1}^{1} |x|\varphi'(x)\,dx = \int_{-1}^{0} (-x)\varphi'(x)\,dx + \int_{0}^{1} x\varphi'(x)\,dx.$$
2. **Tích phân từng phần trên từng nửa khoảng**:
   - Nửa trái: $\big[-x\varphi(x)\big]_{-1}^0 + \int_{-1}^0 \varphi(x)\,dx = 0 + \int_{-1}^0 \varphi(x)\,dx$.
   - Nửa phải: $\big[x\varphi(x)\big]_0^1 - \int_0^1 \varphi(x)\,dx = 0 - \int_0^1 \varphi(x)\,dx$.
3. **Cộng hai vế lại**:
   $$\int_{-1}^{1} |x|\varphi'(x)\,dx = -\int_{-1}^{1} \operatorname{sgn}(x)\varphi(x)\,dx, \qquad \operatorname{sgn}(x) = \begin{cases} -1 & x < 0, \\ +1 & x > 0. \end{cases}$$
   Đối chiếu với định nghĩa $\int u\varphi' = -\int v\varphi$, ta kết luận ngay đạo hàm yếu của $|x|$ chính là $v(x) = \mathbf{\operatorname{sgn}(x)}$!
## Khái niệm theo ba cách

### Cách trực giác

Hãy hình dung một con đường có một điểm gấp khúc. Đứng đúng tại điểm gấp, độ dốc cổ điển không xác định, nhưng quan sát trên một đoạn ngắn quanh đó vẫn cho thấy rõ xu hướng biến thiên hai bên. Đạo hàm yếu ghi nhận xu hướng biến thiên đó khi kiểm tra bằng các hàm thử trơn, thay vì đòi hỏi giới hạn sai phân tại từng điểm riêng lẻ.

### Cách hình ảnh

Ví dụ minh họa trực quan nhất là đồ thị của $$ u(x)=\lvert x\rvert $$. Tại $$ x=0 $$, đạo hàm cổ điển không tồn tại do đồ thị đổi hướng đột ngột; tuy nhiên bên trái có độ dốc $$ -1 $$ và bên phải có độ dốc $$ 1 $$. Khi nhân với hàm thử trơn và lấy tích phân, toàn bộ thông tin độ dốc này vẫn được ghi nhận chính xác.

Hình ảnh trọng tâm của cả chương là phép "chuyển đạo hàm sang hàm thử": giữ nguyên hàm gốc trong tích phân và lấy đạo hàm trên hàm thử trơn.

### Cách hình thức

Giả sử $$ u\in L^1_{\mathrm{loc}}(\Omega) $$. Ta nói $$ v\in L^1_{\mathrm{loc}}(\Omega) $$ là đạo hàm yếu theo biến $$ x_i $$ của $$ u $$ nếu:

$$
\int_\Omega u\,\partial_i\varphi\,dx=-\int_\Omega v\,\varphi\,dx
\qquad \forall \varphi\in C_c^\infty(\Omega).
$$

Khi đó ta viết $$ v=\partial_i u $$ theo nghĩa yếu. Nếu $$ u\in C^1(\Omega) $$, phép tích phân từng phần chứng tỏ đạo hàm yếu trùng với đạo hàm cổ điển, nên khái niệm mới mở rộng nhất quán khái niệm cũ.

## Ngộ nhận thường gặp

### “Đạo hàm yếu là khái niệm xấp xỉ, kém chính xác hơn”

Sai. Đạo hàm yếu là định nghĩa toán học hoàn toàn chặt chẽ, chỉ khác ở cách đo qua tích phân với hàm thử, và là công cụ phù hợp cho các nghiệm không trơn.

### “Không có đạo hàm cổ điển thì chắc chắn không có đạo hàm yếu”

Sai. Các hàm như $$ \lvert x\rvert $$ hay $$ x_+ $$ không có đạo hàm cổ điển tại 0 nhưng vẫn có đạo hàm yếu xác định rõ ràng.

### “Đạo hàm yếu chỉ là một mẹo tính toán”

Không đúng. Nó là nền tảng cho không gian Sobolev, nghiệm yếu, phương pháp biến phân và phần lớn lý thuyết PDE hiện đại.

### “Đạo hàm yếu phải xác định tại mọi điểm”

Không. Đạo hàm yếu chỉ xác định hầu khắp nơi, tương thích với cấu trúc của các không gian tích phân $$ L^p $$.

## Tiến trình học

### Bước 1: Ôn lại tích phân từng phần

Nhắc lại rằng với hàm trơn, $$ \int u\,\varphi'=-\int u'\varphi $$ vì các số hạng biên triệt tiêu nhờ giá compact của $$ \varphi $$.

### Bước 2: Đảo chiều để định nghĩa

Thay vì xuất phát từ $$ u' $$ rồi suy ra công thức tích phân từng phần, ta dùng chính đẳng thức tích phân đó để định nghĩa đạo hàm yếu.

### Bước 3: Thực hành trên các hàm có điểm gãy

Kiểm tra các ví dụ $$ \lvert x\rvert $$, $$ x_+ $$ và hàm bậc thang để thấy rõ ranh giới tồn tại đạo hàm yếu.

### Bước 4: Kết nối với không gian Sobolev

Chỉ ra rằng yêu cầu hàm cùng các đạo hàm yếu thuộc $$ L^p $$ chính là định nghĩa của không gian Sobolev.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao hàm thử phải trơn và có giá compact hay không?
- Sinh viên có tính được đạo hàm yếu của $$ \lvert x\rvert $$ và $$ x_+ $$ hay không?
- Sinh viên có giải thích được vì sao đạo hàm yếu trùng với đạo hàm cổ điển khi hàm thuộc $$ C^1 $$ hay không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm trơn

Cho $$ u(x)=x^2 $$ trên $$ (-1,1) $$. Đạo hàm cổ điển là $$ u'(x)=2x $$. Với mọi $$ \varphi\in C_c^\infty(-1,1) $$,

$$
\int_{-1}^1 x^2\varphi'(x)\,dx
=- \int_{-1}^1 2x\varphi(x)\,dx.
$$

Vậy đạo hàm yếu của $$ u $$ là $$ 2x $$, trùng với đạo hàm cổ điển.

### Ví dụ 2: Hàm có góc nhọn

Xét $$ u(x)=\lvert x\rvert $$ trên $$ (-1,1) $$. Đạo hàm cổ điển không tồn tại tại $$ x=0 $$. Tuy nhiên, đặt:

$$
u'(x)=
\begin{cases}
-1,& x<0,\\
1,& x>0.
\end{cases}
$$

Hàm này thuộc $$ L^\infty(-1,1) $$. Thực hiện tích phân từng phần riêng trên hai khoảng $$ (-1,0) $$ và $$ (0,1) $$ rồi cộng lại cho thấy đây chính là đạo hàm yếu của $$ \lvert x\rvert $$.

### Ví dụ 3: Hàm phần dương

Xét $$ u(x)=x_+=\max\{x,0\} $$. Khi đó $$ \partial_x u=\chi_{(0,\infty)} $$ theo nghĩa yếu. Dù đạo hàm cổ điển không tồn tại tại 0, đạo hàm yếu của hàm này là một hàm chỉ thị rất đơn giản.

### Ví dụ 4: Hàm bậc thang Heaviside

Xét hàm Heaviside:

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$

Hàm này không có đạo hàm yếu dạng hàm khả tích địa phương, vì đạo hàm theo nghĩa rộng hơn của nó là một khối lượng tập trung tại 0 — tức phân bố Dirac. Ví dụ này chuẩn bị trực tiếp cho bài học về phân bố.

## Câu hỏi khái niệm

1. Tại sao định nghĩa đạo hàm yếu phải đúng với mọi hàm thử chứ không chỉ một vài hàm thử cụ thể?
2. Vì sao điều kiện hàm thử có giá compact giúp triệt tiêu các số hạng biên?
3. Điểm khác biệt nào khiến $$ \lvert x\rvert $$ có đạo hàm yếu dạng hàm còn hàm Heaviside thì không?

## Bài toán ứng dụng

1. Trong cơ học vật rắn, chuyển vị của một thanh có điểm gấp khúc vẫn mang thông tin biến dạng theo nghĩa yếu như thế nào?
2. Trong xử lý ảnh, các cạnh sắc nét làm đạo hàm cổ điển kém ổn định; vì sao cách tiếp cận theo đạo hàm yếu lại phù hợp hơn?
3. Trong bài toán truyền nhiệt qua vật liệu ghép nhiều lớp, phân bố nhiệt độ có thể không trơn tại mặt tiếp giáp; đạo hàm yếu giúp mô tả đại lượng vật lý nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một hàm có điểm gấp khúc thì mọi thông tin về đạo hàm có mất hết không?
- Vì sao việc chuyển đạo hàm sang hàm thử vẫn bảo toàn bản chất của bài toán?
- Có phải mọi hàm không trơn đều có đạo hàm yếu dạng hàm không?

### Hoạt động gợi ý

- Cho sinh viên làm việc theo cặp để kiểm tra trực tiếp đạo hàm yếu của $$ \lvert x\rvert $$.
- Vẽ ba đồ thị $$ x^2 $$, $$ \lvert x\rvert $$, $$ H(x) $$ rồi phân loại theo ba mức: có đạo hàm cổ điển, có đạo hàm yếu dạng hàm, chỉ có đạo hàm phân bố.
- Tổ chức khảo sát nhanh đúng/sai với các phát biểu về đạo hàm yếu.

### Cách tăng tham gia

- Yêu cầu sinh viên giải thích khái niệm đạo hàm yếu trong 30 giây mà không dùng ký hiệu.
- Mở đầu bằng ví dụ $$ \lvert x\rvert $$ trước khi đưa ra định nghĩa hình thức.
- Mời sinh viên tự đề xuất một hàm có đạo hàm yếu nhưng không khả vi cổ điển tại một số điểm.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Giữ bối cảnh một chiều trước khi mở rộng sang nhiều chiều.
- Luyện kỹ thao tác tách tích phân từng phần trên từng khoảng con.
- Trình bày mẫu tính chi tiết cho $$ \lvert x\rvert $$ và $$ x_+ $$.

### Thử thách cho sinh viên khá giỏi

- Chứng minh tính duy nhất hầu khắp nơi của đạo hàm yếu.
- Khảo sát đạo hàm yếu của hàm khoảng cách $$ \lvert x\rvert $$ trong nhiều chiều.
- Tìm ví dụ một hàm thuộc $$ W^{1,1} $$ nhưng không liên tục.

## Ghi nhớ nhanh

Đạo hàm yếu không đánh giá độ dốc tại từng điểm mà xác định thông qua đẳng thức tích phân từng phần với mọi hàm thử trơn có giá compact. Nhờ đó, nhiều hàm không khả vi cổ điển vẫn giữ được cấu trúc vi phân chặt chẽ trong lý thuyết PDE.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cơ học vật thể có điểm gãy độ dốc
- Bài toán: Một thanh hoặc sợi dây có độ võng liên tục nhưng độ dốc thay đổi đột ngột tại một điểm.
- Mô hình: Dùng đạo hàm yếu để mô tả chuyển vị $$ u $$ ngay cả khi đạo hàm cổ điển không tồn tại tại điểm gãy.
- Giả thiết và giới hạn: Hàm đủ khả tích địa phương để ghép với hàm thử.
- Diễn giải: Đạo hàm yếu bảo toàn thông tin vật lý toàn cục dù đạo hàm từng điểm không tồn tại.

#### Xử lý ảnh theo phương pháp biến phân
- Bài toán: Các cạnh ảnh có cường độ thay đổi đột ngột nên đạo hàm cổ điển không áp dụng được trực tiếp.
- Mô hình: Làm việc với đạo hàm yếu hoặc đạo hàm phân bố của ảnh.
- Giả thiết và giới hạn: Ảnh được xem như hàm trên lưới mịn hoặc miền liên tục.
- Diễn giải: Đạo hàm yếu cho phép mô hình hóa cạnh ảnh mà không đòi hỏi ảnh phải trơn.

### 2. Trực giác bổ sung và các kết nối

Đạo hàm yếu không yêu cầu tính giới hạn thương sai phân tại từng điểm, mà đòi hỏi công thức tích phân từng phần thỏa mãn với mọi hàm thử trơn. Đây không phải là khái niệm kém chính xác hơn đạo hàm cổ điển, mà là ngôn ngữ tổng quát hóa phù hợp với lớp hàm rộng hơn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 600)
u = np.abs(x)
weak_du = np.sign(x)
weak_du[np.abs(x) < 1e-12] = 0.0

plt.plot(x, u, label="u(x)=|x|")
plt.plot(x, weak_du, label="dao ham yeu xap xi")
plt.legend()
plt.title("Ham co cho goc nhon nhung van co dao ham yeu")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: weak derivative absolute value visualization
- search: image edges weak derivatives variational methods
- search: distributional derivative Heaviside function

### 5. Bài toán mẫu có bối cảnh thực

Với $$ u(x)=\lvert x\rvert $$ trên $$ (-1,1) $$, đạo hàm cổ điển không tồn tại tại $$ x=0 $$, nhưng đạo hàm yếu là $$ u'(x)=\operatorname{sgn}(x) $$ theo nghĩa:
$$
\int_{-1}^1 \lvert x\rvert \varphi'(x)\,dx = -\int_{-1}^1 \operatorname{sgn}(x)\varphi(x)\,dx
$$
với mọi $$ \varphi \in C_c^\infty(-1,1) $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu vì sao các hàm có điểm gấp khúc vẫn có thể có đạo hàm yếu.

**Bậc sau đại học.** Kết nối với lý thuyết phân bố, hàm biến phân bị chặn (BV), định lý vết biên và tính compact.

## Video tham khảo

- xem trước: [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, tiếng Anh. Giải thích tổng hợp đạo hàm yếu, không gian W^{1,p} và H^1.
- [UPB Math 237 LEC5A Sobolev Spaces](https://www.youtube.com/watch?v=GhBM6L-avYU) — Gilbert Peralta, tiếng Anh. Bài giảng xây dựng không gian Sobolev xuất phát từ đạo hàm yếu.
- [Lec 36 Sobolev lemma](https://www.youtube.com/watch?v=ln4N51019qk) — NPTEL - Indian Institute of Science, Bengaluru, tiếng Anh. Trình bày bổ đề Sobolev về mức độ trơn có thể suy ra từ đạo hàm yếu.
