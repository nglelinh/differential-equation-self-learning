---
layout: post
title: "02-06 Biến thiên Hằng số"
chapter: '02'
order: 6
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---

Điều gì xảy ra nếu ngoại lực tác động lên lò xo là $\sec(t)$, $\ln(t)$, hay $e^t / t$—những hàm mà đạo hàm của chúng sinh ra vô hạn dạng mới khiến phương pháp hệ số bất định hoàn toàn bó tay? Năm 1774, Lagrange đã tạo ra chiếc chìa khóa vạn năng **Biến thiên hằng số (Variation of Parameters)**: chỉ cần biết hai nghiệm thuần nhất $y_1, y_2$, ta có thể giải **mọi** phương trình tuyến tính không thuần nhất, kể cả khi hệ số biến thiên!

## Bản đồ kiến thức nền: Bốn trụ cột của Biến thiên Hằng số

1. **Ý tưởng thay hằng số bằng hàm số ($y_p = u_1(t)y_1(t) + u_2(t)y_2(t)$)**:
   Vì có 2 hàm ẩn $u_1, u_2$ nhưng chỉ có 1 phương trình, ta tự do áp đặt thêm điều kiện phụ thanh lịch $u_1' y_1 + u_2' y_2 = 0$ để loại bỏ toàn bộ đạo hàm cấp hai $u_1'', u_2''$.
2. **Hệ đại số Cramer & Vai trò của Wronskian**:
   Hai ẩn $u_1', u_2'$ thỏa hệ $\begin{cases} u_1' y_1 + u_2' y_2 = 0 \\ u_1' y_1' + u_2' y_2' = g(t) \end{cases}$ (nhớ đưa về dạng chuẩn $y'' + py' + qy = g(t)$!), cho nghiệm duy nhất nhờ $W(y_1, y_2) \ne 0$:
   $$u_1' = \frac{-y_2 g}{W},\qquad u_2' = \frac{y_1 g}{W}.$$
3. **Công thức Hàm Green tích phân**:
   Gộp lại ta được $y_p(t) = \int_{t_0}^t \frac{y_1(s)y_2(t) - y_2(s)y_1(t)}{W(s)}\,g(s)\,ds$—biểu diễn nghiệm như tổng chồng chất đáp ứng xung của ngoại lực $g(s)$!
4. **Tính tổng quát tuyệt đối**:
   Áp dụng được cho cả phương trình hệ số biến thiên và mọi vế phải liên tục $g(t)$, đánh đổi duy nhất là phải tính hai tích phân.

## Mục tiêu
Bài học này giúp sinh viên nắm vững phương pháp biến thiên hằng số như một công cụ tổng quát để tìm nghiệm riêng cho phương trình không thuần nhất, đặc biệt khi vế phải không phù hợp với phương pháp hệ số bất định. Sinh viên sẽ biết cách thay hằng số bằng hàm số, thiết lập hệ phương trình cho các đạo hàm tương ứng và hiểu vai trò của định thức Wronskian trong quy trình giải.

## Kiến thức nền
Sinh viên cần nắm cách tìm nghiệm thuần nhất của phương trình tuyến tính cấp hai, nguyên lý chồng chất, kỹ thuật hạ bậc và cách giải hệ hai phương trình tuyến tính. Biết trước về định thức Wronskian là một lợi thế, nhưng bài học này cũng giúp thấy rõ vì sao Wronskian cần thiết.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-06 Biến thiên Hằng số]({{ site.imgurl }}/chapter_img/chapter02/02_06_variation_of_parameters.svg)

Phương pháp hệ số bất định gọn gàng nhưng chỉ áp dụng được cho một số họ hàm nhất định. Khi vế phải là $$ \ln t $$, $$ \tan t $$ hoặc một hàm không đóng dưới phép đạo hàm, ta cần một phương pháp tổng quát hơn: biến thiên hằng số. Ý tưởng cốt lõi xuất phát trực tiếp từ nghiệm thuần nhất $$ c_1y_1+c_2y_2 $$: khi có ngoại lực, thay vì giữ $$ c_1,c_2 $$ là hằng số, ta cho chúng biến thiên theo thời gian.

Cách làm này không dựa vào việc đoán dạng nghiệm từ bên ngoài mà dùng ngay cơ sở nghiệm của hệ thuần nhất để xây dựng đáp ứng cưỡng bức. Vì vậy, biến thiên hằng số là sự mở rộng tự nhiên của nguyên lý chồng chất.

### Khung giải thích (nên đọc chậm): Giải $y'' + y = \sec(t)$ trên $(-\frac{\pi}{2}, \frac{\pi}{2})$ bằng Biến thiên Hằng số

1. **Hệ nghiệm cơ bản & Wronskian**:
   $y_1 = \cos t,\; y_2 = \sin t$, và $W = \cos t(\cos t) - (-\sin t)\sin t = \cos^2 t + \sin^2 t = \mathbf{1}$.
2. **Tính $u_1'$ và $u_2'$** (với $g(t) = \sec t = \frac{1}{\cos t}$):
   - $u_1'(t) = \frac{-\sin t \cdot \sec t}{1} = -\tan t \implies u_1(t) = \int -\tan t\,dt = \mathbf{\ln\vert\cos t\vert}$.
   - $u_2'(t) = \frac{\cos t \cdot \sec t}{1} = 1 \implies u_2(t) = \int 1\,dt = \mathbf{t}$.
3. **Ghép nghiệm riêng $y_p = u_1 y_1 + u_2 y_2$**:
   $$y_p(t) = \cos t \ln(\cos t) + t\sin t.$$
4. **Nghiệm tổng quát**: $y(t) = \mathbf{c_1\cos t + c_2\sin t + \cos t\ln(\cos t) + t\sin t}$ (lưu ý phương pháp hệ số bất định hoàn toàn bất lực trước $\sec t$!).

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nghiệm thuần nhất cung cấp hai thành phần chuyển động cơ bản của hệ. Khi không có ngoại lực, trọng số của hai thành phần này là hằng số. Khi có ngoại lực, hệ vẫn biểu diễn được qua hai thành phần đó nhưng các trọng số thay đổi theo thời gian — chính là hai hàm $$ u_1(t) $$ và $$ u_2(t) $$.

### Cách nhìn hình ảnh
Nếu nghiệm thuần nhất sinh ra một họ quỹ đạo cơ sở, thì nghiệm không thuần nhất có thể xem là quỹ đạo liên tục điều chỉnh tỉ lệ pha trộn giữa hai hướng cơ sở ấy để đáp ứng với ngoại lực.

### Cách nhìn hình thức
Xét phương trình đã chuẩn hóa
$$ y''+p(t)y'+q(t)y=g(t). $$
Giả sử $$ y_1,y_2 $$ là hai nghiệm độc lập tuyến tính của phương trình thuần nhất. Ta tìm nghiệm riêng dưới dạng
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
Để tránh xuất hiện đạo hàm cấp hai của $$ u_1,u_2 $$, ta áp đặt điều kiện phụ $$ u_1'y_1+u_2'y_2=0 $$. Thay vào phương trình ban đầu, ta thu được hệ tuyến tính
$$ u_1'y_1+u_2'y_2=0, $$
$$ u_1'y_1'+u_2'y_2'=g(t). $$
Giải hệ này theo $$ u_1',u_2' $$ sẽ dẫn trực tiếp tới công thức chứa định thức Wronskian.

## Những ngộ nhận thường gặp
- "Biến thiên hằng số chỉ là phiên bản phức tạp hơn của hệ số bất định." Sai: đây là phương pháp tổng quát hơn nhiều, dùng được cho cả phương trình hệ số biến thiên và nhiều dạng vế phải tổng quát.
- "Hai hàm $$ u_1,u_2 $$ có thể chọn tùy ý." Sai: chúng bị ràng buộc bởi hệ phương trình thu được khi thay vào ODE.
- "Điều kiện phụ $$ u_1'y_1+u_2'y_2=0 $$ là lựa chọn tùy tiện." Sai: nó được chọn để khử đạo hàm bậc hai của $$ u_1,u_2 $$ và đưa về hệ bậc nhất dễ giải.
- "Nếu tích phân không tính được bằng hàm sơ cấp thì phương pháp sai." Không đúng: phương pháp vẫn hoàn toàn chính xác về mặt lý thuyết dù tích phân có thể phải tính bằng phương pháp số.

## Tiến trình học tập đề xuất
### Bước 1: Giải phương trình thuần nhất
Tìm hai nghiệm độc lập $$ y_1,y_2 $$ trước khi làm tiếp.

### Bước 2: Đặt nghiệm riêng dạng biến thiên hằng số
Viết $$ y_p=u_1y_1+u_2y_2 $$.

### Bước 3: Áp đặt điều kiện phụ
Điều kiện này giúp tránh xuất hiện đạo hàm cấp hai của $$ u_1,u_2 $$.

### Bước 4: Giải hệ cho $$ u_1',u_2' $$
Sử dụng công thức chứa định thức Wronskian.

### Bước 5: Tích phân và dựng $$ y_p $$
Lấy nguyên hàm để tìm $$ u_1,u_2 $$, sau đó cộng với $$ y_h $$ để có nghiệm tổng quát.

### Các checkpoint
- Sinh viên có nhớ $$ u_1,u_2 $$ là các hàm số chứ không phải hằng số hay không.
- Sinh viên có lập đúng hệ hai phương trình cho $$ u_1',u_2' $$ hay không.
- Sinh viên có giải thích được vì sao Wronskian phải khác 0 hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Vế phải không xử lý được bằng hệ số bất định
Giải phương trình
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
Nghiệm thuần nhất là $$ y_h=c_1\cos t+c_2\sin t $$. Chọn $$ y_1=\cos t $$ và $$ y_2=\sin t $$, ta có Wronskian
$$ W=y_1y_2'-y_1'y_2=\cos^2 t+\sin^2 t=1. $$
Theo công thức biến thiên hằng số:
$$
u_1'=-\frac{y_2g}{W}=-\sin t\tan t=-\frac{\sin^2 t}{\cos t},\qquad u_2'=\frac{y_1g}{W}=\cos t\tan t=\sin t.
$$
Suy ra $$ u_2=-\cos t $$. Với $$ u_1' $$, biến đổi
$$ u_1'=-\frac{1-\cos^2 t}{\cos t}=-\sec t+\cos t, $$
nên $$ u_1=-\ln \lvert \sec t+\tan t\rvert+\sin t $$. Do đó
$$ y_p=u_1\cos t+u_2\sin t. $$
Ví dụ này cho thấy phương pháp vẫn hoạt động bình thường với vế phải không thuộc họ đóng dưới phép đạo hàm.

### Ví dụ 2: Áp dụng cho vế phải đa thức
Giải phương trình $$ y''+y=t $$. Nghiệm thuần nhất là $$ y_h=c_1\cos t+c_2\sin t $$. Với $$ W=1 $$, ta có $$ u_1'=-t\sin t $$ và $$ u_2'=t\cos t $$. Tích phân từng phần:
$$ u_1=t\cos t-\sin t,\qquad u_2=t\sin t+\cos t. $$
Suy ra
$$
y_p=\left(t\cos t-\sin t\right)\cos t+\left(t\sin t+\cos t\right)\sin t=t,
$$
và nghiệm tổng quát là $$ y=c_1\cos t+c_2\sin t+t $$. Kết quả cho thấy phương pháp tổng quát vẫn cho đáp số gọn gàng khi áp dụng cho bài toán đơn giản.

### Ví dụ 3: Vai trò của Wronskian
Nếu $$ W=0 $$, hai nghiệm $$ y_1,y_2 $$ phụ thuộc tuyến tính nên hệ phương trình xác định $$ u_1',u_2' $$ bị suy biến. Điều này phản ánh trực giác rõ ràng: nếu chưa có hai hướng nghiệm độc lập trong cơ sở thuần nhất, ta không thể biểu diễn mọi đáp ứng cưỡng bức bằng chúng.

### Ví dụ 4: Khi nào nên chọn biến thiên hằng số
Nếu vế phải là đa thức hay hàm mũ đơn giản, hệ số bất định thường nhanh hơn. Ngược lại, khi vế phải là $$ \ln t $$, $$ \tan t $$, $$ \sec t $$ hoặc hàm không đóng dưới phép đạo hàm, biến thiên hằng số là lựa chọn phù hợp. Đây là kỹ năng lựa chọn phương pháp cần rèn luyện.

## Câu hỏi khái niệm
1. Vì sao biến thiên hằng số là sự mở rộng tự nhiên của nghiệm thuần nhất?
2. Điều kiện phụ $$ u_1'y_1+u_2'y_2=0 $$ đóng vai trò gì?
3. Vì sao định thức Wronskian xuất hiện tự nhiên trong phương pháp này?

## Bài toán ứng dụng
1. Một hệ dao động chịu tác động của vế phải không chuẩn như $$ \ln t $$. Hãy giải thích vì sao hệ số bất định không áp dụng được nhưng biến thiên hằng số vẫn giải được.
2. Một hệ điều khiển tuyến tính có hai chế độ dao động cơ bản đã biết. Hãy diễn giải ý nghĩa vật lý của việc cho các trọng số biến thiên theo thời gian.
3. Trong mô hình sóng cưỡng bức, vì sao một cơ sở nghiệm độc lập của hệ thuần nhất là điều kiện cần thiết để dựng đáp ứng đầy đủ?

## Chiến lược giảng dạy tương tác
- Trước khi viết công thức, hỏi lớp: "Nếu ngoại lực làm thay đổi cách hệ pha trộn hai thành phần cơ bản, ta nên điều chỉnh dạng nghiệm thuần nhất ra sao?"
- Chia nhóm thực hiện từng phần: tìm $$ y_h $$, lập hệ cho $$ u_1',u_2' $$ và tính Wronskian.
- So sánh lời giải của cùng một bài bằng hệ số bất định và biến thiên hằng số để thấy sự đánh đổi giữa tính tổng quát và độ gọn.
- Thảo luận khi nào không cần dùng biến thiên hằng số dù về nguyên tắc vẫn áp dụng được.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp khung làm bài cố định theo năm bước trên. Sinh viên thường gặp khó khăn không phải ở bước tích phân mà ở việc theo dõi nhiều ký hiệu cùng lúc.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên tự suy ra công thức Cramer cho $$ u_1',u_2' $$ từ hệ hai phương trình, hoặc đối chiếu biến thiên hằng số với phương pháp hàm Green trong bài toán tuyến tính.

## Tóm tắt dễ nhớ
Biến thiên hằng số thay các hằng số trong nghiệm thuần nhất bằng các hàm thời gian để hấp thụ vế phải không thuần nhất. Quy trình chuẩn là tìm cơ sở nghiệm $$ y_1,y_2 $$ trước, sau đó lập hệ cho $$ u_1',u_2' $$ và tích phân để dựng nghiệm riêng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ngoại lực không chuẩn trong cơ học
- Bài toán: Hệ dao động chịu kích thích bởi tín hiệu như $$ \tan t $$, $$ \ln t $$ hoặc dữ liệu đo thực nghiệm.
- Mô hình:
$$ y''+p(t)y'+q(t)y=g(t). $$
- Giả thiết và giới hạn: Cần biết trước cơ sở nghiệm thuần nhất với Wronskian khác 0.
- Diễn giải: Biến thiên hằng số tổng quát hơn hệ số bất định vì không đòi hỏi vế phải thuộc họ đóng dưới phép đạo hàm.

#### Điều khiển tuyến tính với hai chế độ cơ bản
- Bài toán: Hệ có hai chế độ riêng và ngoại lực làm thay đổi tỉ lệ pha trộn giữa chúng theo thời gian.
- Mô hình:
$$ y_p=u_1(t)y_1(t)+u_2(t)y_2(t). $$
- Giả thiết và giới hạn: Tích phân thu được có thể phức tạp, nhưng về nguyên lý phương pháp luôn áp dụng cho ODE tuyến tính cấp hai.
- Diễn giải: Các hằng số trong nghiệm thuần nhất trở thành các trọng số phụ thuộc thời gian.

#### Truyền nhiệt hoặc dao động với nguồn phức tạp
- Bài toán: Hệ chịu tác động của nguồn không tuần hoàn đơn giản và không tra được trong bảng hệ số bất định.
- Mô hình: ODE tuyến tính cấp hai không thuần nhất.
- Giả thiết và giới hạn: Đòi hỏi tính tích phân, đôi khi phải dùng tích phân số.
- Diễn giải: Minh họa rõ việc tính tổng quát thường đi kèm chi phí tính toán cao hơn.

### 2. Trực giác bổ sung và các kết nối

Biến thiên hằng số mở rộng trực tiếp nguyên lý chồng chất: khi không có ngoại lực, trọng số của hai thành phần cơ bản là hằng số; khi có ngoại lực, các trọng số này thay đổi dưới tác động của nguồn ngoài. Ý tưởng này gắn chặt với công thức Duhamel, hàm Green và phương pháp nghiệm cơ bản cho phương trình đạo hàm riêng (PDE). Điều kiện phụ $$ u_1'y_1+u_2'y_2=0 $$ không phải lựa chọn tùy tiện mà là ràng buộc giúp khử đạo hàm bậc hai của $$ u_1,u_2 $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t = np.linspace(0.05, 1.2, 400)
g = np.tan(t)
y1 = np.cos(t)
y2 = np.sin(t)
u1p = -y2 * g
u2p = y1 * g
u1 = np.concatenate(([0], cumulative_trapezoid(u1p, t)))
u2 = np.concatenate(([0], cumulative_trapezoid(u2p, t)))
yp = u1 * y1 + u2 * y2

plt.plot(t, yp, label="y_p from variation of parameters")
plt.xlabel("t")
plt.ylabel("y_p(t)")
plt.title("Nghiệm riêng cho y'' + y = tan(t)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy trực tiếp cách nghiệm riêng được tạo nên từ tổ hợp hai thành phần cơ bản với trọng số biến thiên theo thời gian.

### 4. Gợi ý tìm thêm mô phỏng

- search: variation of parameters visualization
- search: Wronskian Cramer rule animation
- search: Green function second order ODE intuition

### 5. Bài toán mẫu có bối cảnh thực

Xét lại phương trình
$$ y''+y=\tan t,\qquad \lvert t\rvert<\frac{\pi}{2}. $$
Nghiệm thuần nhất là $$ y_h=c_1\cos t+c_2\sin t $$. Lấy $$ y_1=\cos t $$, $$ y_2=\sin t $$ và $$ W=1 $$, ta có
$$
u_1'=-y_2g=-\sin t\tan t,\qquad u_2'=y_1g=\cos t\tan t=\sin t.
$$
Suy ra $$ u_2=-\cos t $$, còn $$ u_1 $$ tìm được qua phép tích phân như ở Ví dụ 1. Dù biểu thức tích phân của $$ u_1 $$ phức tạp hơn các bài hệ số bất định thông thường, phương pháp vẫn nhất quán và cho nghiệm riêng chính xác.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững quy trình năm bước và biết khi nào nên chọn biến thiên hằng số thay cho hệ số bất định.

**Bậc sau đại học.** Kết nối với quy tắc Cramer, hàm Green và biểu diễn tích phân của toán tử nghịch đảo.

## Video tham khảo

- Xem trước: [Variation of Parameters || How to solve non-homogeneous ODEs](https://www.youtube.com/watch?v=wSMad7QpaqE) — Dr. Trefor Bazett, tiếng Anh. Hướng dẫn biến thiên hằng số khi không áp dụng được hệ số bất định.
- [Differential Equations with Forcing: Method of Variation of Parameters](https://www.youtube.com/watch?v=wCeDUbZQ_zA) — Steve Brunton, tiếng Anh. Xây dựng công thức nghiệm riêng từ một hệ nghiệm cơ bản.
- [Undetermined Coefficients: Solving non-homogeneous ODEs](https://www.youtube.com/watch?v=AgyeJEO2a-k) — Dr. Trefor Bazett, tiếng Anh. Đặt cạnh phương pháp hệ số bất định để thấy rõ mối quan hệ tổng quát hóa.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ công thức và cơ sở của phương pháp.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập vế phải không chuẩn để luyện biến thiên hằng số.
- Ross — *Differential Equations*: hữu ích để ôn tập ý tưởng tổng quát khi đối chiếu với hệ số bất định.
