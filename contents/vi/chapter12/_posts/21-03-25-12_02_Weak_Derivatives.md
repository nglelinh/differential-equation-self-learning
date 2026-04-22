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

## Mục tiêu

Bài này giúp sinh viên hiểu vì sao cần đạo hàm yếu, đạo hàm yếu được định nghĩa như thế nào qua hàm thử, và vì sao đó là bước chuyển quyết định từ giải tích cổ điển sang PDE hiện đại. Sau bài học, sinh viên cần tính được một số đạo hàm yếu cơ bản và giải thích được mối liên hệ giữa đạo hàm yếu, tích phân từng phần, và nghiệm yếu.

## Kiến thức nền

Sinh viên nên nắm đạo hàm cổ điển, tích phân từng phần, hàm trơn có hỗ compact, và ý tưởng làm việc với tích phân thay vì giá trị điểm. Việc hiểu sơ bộ về $$ L^1_{\mathrm{loc}} $$ cũng hữu ích vì đạo hàm yếu không yêu cầu hàm phải trơn.

## Dẫn nhập

Trong nhiều bài toán, nghiệm thật sự không mượt. Nó có thể có góc nhọn, chỗ gãy, hay thay đổi kiểu đột ngột. Nếu giữ khái niệm đạo hàm cổ điển, ta sẽ phải kết luận rằng những hàm này “không có đạo hàm” và do đó không thể là nghiệm của PDE. Điều đó quá cứng nhắc.

Ý tưởng của đạo hàm yếu là không nhìn đạo hàm trực tiếp trên chính hàm, mà nhìn cách hàm tương tác với các hàm thử trơn. Ta chuyển đạo hàm sang phía hàm thử bằng tích phân từng phần. Nếu công thức đó vẫn đúng, ta xem như đạo hàm vẫn tồn tại theo một nghĩa rộng hơn.

## Khái niệm theo ba cách

### Cách trực giác

Hãy nghĩ đến một con đường có một góc gấp. Nếu bạn đứng đúng tại góc, độ dốc không xác định rõ. Nhưng nếu quan sát trên một đoạn ngắn xung quanh góc, bạn vẫn cảm nhận được xu hướng thay đổi tổng thể của đường. Đạo hàm yếu ghi lại “xu hướng trung bình khi thử bằng các kính lọc trơn”, chứ không đòi hỏi độ dốc chính xác ở từng điểm.

### Cách hình ảnh

Một hình minh họa rất hữu ích là đồ thị của $$ u(x)=\lvert x\rvert $$. Tại $$ x=0 $$, đạo hàm cổ điển không tồn tại vì đồ thị đổi hướng đột ngột. Nhưng ở bên trái độ dốc là $$ -1 $$, bên phải là $$ 1 $$. Nếu nhân với một hàm thử trơn và tích phân, toàn bộ thông tin đó vẫn được ghi lại một cách ổn định.

Ta có thể vẽ thêm hình “đạo hàm được đẩy sang hàm thử”: hàm gốc giữ nguyên, còn hàm thử được lấy đạo hàm. Đây là hình ảnh trung tâm của cả chương.

### Cách hình thức

Giả sử $$ u\in L^1_{\mathrm{loc}}(\Omega) $$. Ta nói $$ v\in L^1_{\mathrm{loc}}(\Omega) $$ là đạo hàm yếu theo biến $$ x_i $$ của $$ u $$ nếu

$$
\int_\Omega u\,\partial_i\varphi\,dx=-\int_\Omega v\,\varphi\,dx
\qquad \forall \varphi\in C_c^\infty(\Omega).
$$

Khi đó ta viết $$ v=\partial_i u $$ theo nghĩa yếu.

Nếu $$ u\in C^1(\Omega) $$, tích phân từng phần cho thấy đạo hàm yếu trùng với đạo hàm cổ điển, nên khái niệm mới là một mở rộng nhất quán.

## Ngộ nhận thường gặp

### “Đạo hàm yếu là một khái niệm xấp xỉ, kém chính xác hơn”

Sai. Nó không mơ hồ hơn mà chỉ đo đạo hàm theo cách khác. Trong nhiều bối cảnh, đây mới là định nghĩa đúng để làm việc với nghiệm thực tế.

### “Nếu không có đạo hàm cổ điển thì chắc không có đạo hàm yếu”

Sai. Chính các hàm như $$ \lvert x\rvert $$ hoặc $$ x_+ $$ là ví dụ tiêu biểu cho sức mạnh của khái niệm đạo hàm yếu.

### “Đạo hàm yếu chỉ là mẹo kỹ thuật”

Không. Nó là nền móng của Sobolev space, nghiệm yếu, phương pháp biến phân, và phần lớn PDE hiện đại.

### “Đạo hàm yếu phải xác định tại mọi điểm”

Không. Nó chỉ xác định hầu khắp nơi, phù hợp với bản chất của các không gian tích phân.

## Tiến trình học

### Bước 1: Ôn lại tích phân từng phần

Nhắc sinh viên rằng trong trường hợp trơn,

$$ \int u\,\varphi'=-\int u'\varphi $$

nếu biên mất đi nhờ hỗ compact của $$ \varphi $$.

### Bước 2: Đảo chiều định nghĩa

Thay vì bắt đầu từ $$ u' $$ rồi chứng minh công thức, ta dùng chính công thức đó để định nghĩa đạo hàm.

### Bước 3: Kiểm tra trên các hàm có góc nhọn

Các ví dụ như $$ \lvert x\rvert $$, $$ x_+ $$ và hàm bậc thang giúp sinh viên thấy lợi ích ngay lập tức.

### Bước 4: Kết nối với không gian Sobolev

Giải thích rằng “có đạo hàm yếu thuộc $$ L^p $$” chính là điều kiện để một hàm nằm trong các không gian Sobolev.

### Các điểm kiểm tra hiểu bài

- Sinh viên có nói được vì sao hàm thử phải trơn và có hỗ compact không?
- Sinh viên có tính được đạo hàm yếu của $$ \lvert x\rvert $$ hay $$ x_+ $$ không?
- Sinh viên có giải thích được vì sao đạo hàm yếu trùng với đạo hàm cổ điển khi hàm đủ trơn không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm trơn

Cho $$ u(x)=x^2 $$ trên $$ (-1,1) $$. Ta biết đạo hàm cổ điển là $$ u'(x)=2x $$.

Với mọi $$ \varphi\in C_c^\infty(-1,1) $$,

$$
\int_{-1}^1 x^2\varphi'(x)\,dx
=- \int_{-1}^1 2x\varphi(x)\,dx.
$$

Vậy đạo hàm yếu là $$ 2x $$, đúng như đạo hàm cổ điển.

### Ví dụ 2: Hàm có góc nhọn

Xét $$ u(x)=\lvert x\rvert $$ trên $$ (-1,1) $$. Đạo hàm cổ điển không tồn tại tại 0.

Tuy nhiên, ta có

$$
u'(x)=
\begin{cases}
-1,& x<0,\\
1,& x>0.
\end{cases}
$$

Hàm này thuộc $$ L^\infty(-1,1) $$. Kiểm tra tích phân từng phần trên hai khoảng $$ (-1,0) $$ và $$ (0,1) $$ cho thấy đó chính là đạo hàm yếu của $$ \lvert x\rvert $$.

### Ví dụ 3: Hàm phần dương

Xét $$ u(x)=x_+=\max\{x,0\} $$. Khi đó $$ \partial_x u=\chi_{(0,\infty)} $$ theo nghĩa yếu. Đây là ví dụ tốt vì đạo hàm yếu là một hàm đơn giản nhưng đạo hàm cổ điển bị hỏng tại 0.

### Ví dụ 4: Hàm hằng theo từng đoạn

Xét hàm Heaviside

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$

Đạo hàm yếu theo nghĩa hàm không tồn tại, vì “đạo hàm” của nó là một khối lượng tập trung tại 0, chính là phân phối Dirac. Ví dụ này chuẩn bị cho sinh viên chuyển sang bài về phân phối.

## Câu hỏi khái niệm

1. Tại sao đạo hàm yếu được định nghĩa qua tất cả các hàm thử chứ không chỉ một vài hàm thử?
2. Vì sao hỗ compact của hàm thử giúp loại bỏ số hạng biên?
3. Điều gì làm cho $$ \lvert x\rvert $$ có đạo hàm yếu nhưng Heaviside không có đạo hàm yếu dạng hàm?

## Bài toán ứng dụng

1. Trong cơ học vật rắn, chuyển vị của một thanh có vết gãy nhỏ có thể vẫn mang thông tin biến dạng theo nghĩa yếu như thế nào?
2. Trong xử lý ảnh, biên sắc nét khiến đạo hàm cổ điển kém ổn định. Vì sao tư duy “yếu” lại tự nhiên hơn?
3. Trong bài toán truyền nhiệt qua vật liệu ghép nhiều lớp, nhiệt độ có thể trơn hay chỉ liên tục từng phần? Đạo hàm yếu giúp mô tả điều gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một hàm có góc nhọn thì mọi thông tin vi phân đã mất hết chưa?
- Tại sao ta tin rằng chuyển đạo hàm sang hàm thử vẫn giữ được bản chất của bài toán?
- Có phải mọi hàm không trơn đều có đạo hàm yếu dạng hàm không?

### Hoạt động gợi ý

- Cho sinh viên làm việc theo cặp để kiểm tra đạo hàm yếu của $$ \lvert x\rvert $$.
- Vẽ ba đồ thị $$ x^2 $$, $$ \lvert x\rvert $$, $$ H(x) $$ rồi yêu cầu phân loại: đạo hàm cổ điển, đạo hàm yếu dạng hàm, đạo hàm phân phối.
- Dùng thẻ màu để sinh viên bỏ phiếu “có” hay “không” trước mỗi nhận định về đạo hàm yếu.

### Cách tăng tham gia

- Cho sinh viên giải thích khái niệm mà không dùng ký hiệu trong 30 giây.
- Bắt đầu bằng phản ví dụ thay vì định nghĩa.
- Mời sinh viên tự tạo một hàm có đạo hàm yếu nhưng không có đạo hàm cổ điển mọi nơi.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Giữ bối cảnh một chiều trước.
- Dùng rất nhiều tích phân từng phần trên các khoảng con.
- Cho mẫu tính toán chi tiết cho $$ \lvert x\rvert $$ và $$ x_+ $$.

### Thử thách cho sinh viên khá giỏi

- Chứng minh tính duy nhất của đạo hàm yếu.
- Xét đạo hàm yếu của hàm giá trị tuyệt đối trong nhiều chiều.
- Tìm ví dụ hàm nằm trong $$ W^{1,1} $$ nhưng không liên tục.

## Ghi nhớ nhanh

Đạo hàm yếu không nhìn độ dốc tại từng điểm mà nhìn cách hàm tương tác với mọi hàm thử trơn. Nhờ đó, nhiều hàm không khả vi cổ điển vẫn giữ được cấu trúc vi phân đủ mạnh để làm việc trong PDE.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cơ học với chỗ gãy
- Bài toán: Một thanh hay sợi dây có thể có độ lệch liên tục nhưng độ dốc bị gãy tại một điểm.
- Mô hình: Dùng đạo hàm yếu để hiểu chuyển vị $$ u $$ ngay cả khi đạo hàm cổ điển không tồn tại ở mọi điểm.
- Giả thiết và giới hạn: Hàm vẫn đủ khả tích để ghép với test function.
- Diễn giải: Đạo hàm yếu giữ lại thông tin vật lý toàn cục dù vi phân điểm-điểm bị hỏng.

#### Xử lý ảnh theo biến phân
- Bài toán: Cạnh ảnh là nơi tín hiệu thay đổi gắt, nên đạo hàm cổ điển dễ thất bại.
- Mô hình: Làm việc với đạo hàm yếu hoặc phân bố của ảnh.
- Giả thiết và giới hạn: Ảnh được xem như hàm trên lưới mịn hoặc miền liên tục.
- Diễn giải: Đạo hàm yếu cho phép mô hình hóa biên ảnh mà không cần tính trơn tuyệt đối.

### 2. Trực giác bổ sung và các kết nối

Đạo hàm yếu không yêu cầu ta lấy giới hạn vi phân trực tiếp tại từng điểm. Thay vào đó, ta yêu cầu công thức tích phân từng phần vẫn đúng với mọi test function trơn. Một hiểu nhầm phổ biến là đạo hàm yếu "kém chính xác hơn"; thật ra nó chỉ đổi ngôn ngữ để làm việc với lớp hàm rộng hơn.

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

Với
$$ u(x)=\lvert x\rvert $$
trên $$ (-1,1) $$, đạo hàm cổ điển không tồn tại tại $$ x=0 $$. Tuy nhiên đạo hàm yếu là
$$ u'(x)=\operatorname{sgn}(x) $$
theo nghĩa
$$
\int_{-1}^1 \lvert x\rvert \varphi'(x)\,dx = -\int_{-1}^1 \operatorname{sgn}(x)\varphi(x)\,dx
$$
với mọi $$ \varphi \in C_c^\infty(-1,1) $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu vì sao các hàm có chỗ gãy vẫn có thể có đạo hàm yếu.

**Bậc sau đại học.** Kết nối với phân bố, hàm BV, trace và compactness.
