---
layout: post
title: "Nghiệm Cơ Bản và Hàm Green"
chapter: '09'
order: 6
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 06 Fundamental Solution Greens Functions]({{ site.imgurl }}/chapter_img/chapter09/06_fundamental_solution_greens_functions.svg)

## Mục tiêu

Bài học này trình bày nghiệm cơ bản và hàm Green như ngôn ngữ phản ứng xung của phương trình nhiệt. Sau bài học, sinh viên cần hiểu nghiệm cơ bản là nghiệm ứng với nguồn điểm, biết vai trò của hạt nhân Gaussian, hiểu công thức biểu diễn nghiệm qua Green, và thấy được vì sao "biết phản ứng với một xung" là đủ để xây dựng nghiệm cho dữ liệu và nguồn tổng quát.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt trên miền vô hạn, chập, và khái niệm delta Dirac ở mức trực giác. Kiến thức từ bài hàm Green của ODE sẽ giúp sinh viên nhận ra cùng một ý tưởng đang quay lại trong bối cảnh PDE.

## Dẫn nhập

Một cách rất tự nhiên để hiểu một hệ tuyến tính là hỏi: nếu ta tác động vào hệ bằng một xung cực đơn giản, hệ sẽ phản ứng thế nào? Với phương trình nhiệt, xung đơn giản nhất là một lượng nhiệt tập trung tại đúng một điểm vào thời điểm ban đầu. Nghiệm tạo ra bởi xung đó chính là nghiệm cơ bản.

Từ nghiệm cơ bản, ta xây dựng hàm Green. Đây là bước chuyển cực kỳ quan trọng trong tư duy PDE: thay vì giải lại từ đầu cho từng điều kiện đầu hoặc từng nguồn nhiệt, ta chỉ cần biết cách hệ phản ứng với một xung đơn vị, rồi chồng chất các phản ứng ấy lại.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng bạn chạm đầu mỏ hàn nóng vào đúng một điểm trên một thanh rất dài trong một khoảng thời gian cực ngắn. Nhiệt lượng ban đầu được tập trung gần như toàn bộ ở một điểm, rồi sau đó lan ra hai phía. Nghiệm cơ bản chính là mô tả toán học của quá trình lan ra đó.

### Cách nhìn hình ảnh

Ban đầu, nhiệt lượng giống như một đỉnh cực nhọn. Ngay sau thời điểm $$ t=0 $$, đỉnh này trở thành một đường cong Gaussian thấp hơn và rộng hơn. Khi thời gian tăng, Gaussian trải rộng hơn nữa nhưng tổng lượng nhiệt vẫn được giữ nguyên. Hình ảnh này là một trong những trực giác mạnh nhất của cả chương.

### Cách nhìn hình thức

Nghiệm cơ bản của phương trình nhiệt trên $$ \mathbb R $$ là nghiệm của

$$
\Phi_t=\alpha^2\Phi_{xx},
\qquad
\Phi(x,0)=\delta(x).
$$

Kết quả là

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right),
\qquad t>0.
$$

Hàm Green $$ G(x,\xi,t) $$ là nghiệm ứng với xung đặt tại $$ \xi $$, nên trên toàn trục ta có

$$ G(x,\xi,t)=\Phi(x-\xi,t). $$

## Những ngộ nhận thường gặp

- "Delta Dirac là một hàm bình thường có giá trị vô hạn." Không chính xác; nên hiểu nó như một nguồn điểm theo nghĩa phân phối hoặc trực giác giới hạn.
- "Nghiệm cơ bản chỉ là trường hợp đặc biệt ít hữu ích." Sai. Nó là viên gạch nền cho công thức Green tổng quát.
- "Gaussian xuất hiện vì phép biến đổi Fourier tiện tính." Không chỉ vậy; nó thật sự là hình dạng lan tỏa tự nhiên của xung nhiệt.
- "Nếu biết Green thì chỉ có thêm một công thức tích phân." Không đúng; ta có một cách nhìn hoàn toàn mới về nghịch đảo của toán tử nhiệt.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu nguồn điểm

Sinh viên cần cảm được delta như một xung nhiệt lý tưởng hóa.

### Bước 2: Học nghiệm cơ bản trên toàn trục

Đây là trường hợp sạch nhất.

### Bước 3: Mở rộng thành hàm Green

Từ xung ở gốc sang xung ở vị trí bất kỳ.

### Bước 4: Dùng Green để biểu diễn nghiệm

Đây là mục tiêu cuối cùng của bài.

### Các checkpoint

- Sinh viên có giải thích được nghiệm cơ bản bằng ngôn ngữ vật lý hay không.
- Sinh viên có biết vì sao khối lượng của Gaussian bằng 1 hay không.
- Sinh viên có hiểu công thức Green là tổng chập của vô số xung hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khối lượng được bảo toàn

Với nghiệm cơ bản

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right),
$$

ta có

$$ \int_{\mathbb R}\Phi(x,t)\,dx=1. $$

Điều này cho thấy tổng nhiệt lượng ban đầu của xung không bị mất đi, chỉ lan ra.

### Ví dụ 2: Nghiệm từ điều kiện đầu

Nếu $$ u(x,0)=f(x) $$, thì nghiệm được viết thành

$$ u(x,t)=\int_{\mathbb R}\Phi(x-y,t)f(y)\,dy. $$

Ví dụ này nói rằng nghiệm là trung bình có trọng số Gaussian của dữ liệu ban đầu.

### Ví dụ 3: Có nguồn nhiệt theo thời gian

Nếu bài toán có nguồn $$ Q(x,t) $$, ta có công thức Duhamel:

$$
u(x,t)=\int_{\mathbb R}\Phi(x-y,t)f(y)\,dy
+\int_0^t\int_{\mathbb R}\Phi(x-y,t-s)Q(y,s)\,dy\,ds.
$$

Ví dụ này là dạng tổng quát quan trọng nhất của bài.

### Ví dụ 4: Ý nghĩa của đối xứng

Ta có $$ \Phi(x,t)=\Phi(-x,t) $$, nghĩa là xung nhiệt tại gốc lan đều về hai phía. Đây là một ví dụ đơn giản nhưng rất đáng dùng để nhấn mạnh mối liên hệ giữa đối xứng hình học của miền và đối xứng của Green.

## Câu hỏi khái niệm

1. Vì sao biết phản ứng của hệ với một xung điểm lại đủ để dựng nghiệm cho dữ liệu tổng quát?
2. Gaussian của nghiệm cơ bản phản ánh những tính chất vật lý nào của khuếch tán?
3. Hàm Green giúp thay đổi cách ta nhìn lời giải PDE như thế nào?

## Bài toán ứng dụng

1. Trong truyền nhiệt, vì sao việc biết hồ sơ lan tỏa của một xung điểm là thông tin nền tảng?
2. Trong xác suất, vì sao nghiệm cơ bản của phương trình nhiệt lại liên hệ với mật độ của chuyển động Brown?
3. Trong kỹ thuật, nếu nguồn nhiệt tác động ngắn và cục bộ, vì sao Green là công cụ tự nhiên để mô hình hóa đáp ứng của hệ?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu tôi đặt một lượng nhiệt rất nhỏ vào đúng một điểm, chuyện gì sẽ xảy ra ngay sau đó?"
- Dùng hình ảnh một đỉnh sắc biến thành Gaussian để trực quan hóa nghiệm cơ bản.
- Hỏi cả lớp: "Biết phản ứng với một xung thì ta làm gì để xử lý một nguồn phân bố?"
- Cho sinh viên tự giải thích Duhamel bằng ngôn ngữ 'cộng dồn các xung theo thời gian'.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ trọng tâm ở trực giác xung điểm, Gaussian và công thức chập. Không cần đi sâu ngay vào kỹ thuật phân phối nếu điều đó làm mất mạch ý tưởng chính.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi suy ra công thức Green bằng biến đổi Fourier, hoặc liên hệ Green của phương trình nhiệt với Green của phương trình elliptic và ODE đã học trước đó.

## Tóm tắt dễ nhớ

Nghiệm cơ bản của phương trình nhiệt là phản ứng của hệ với một xung nhiệt điểm, và nó có dạng Gaussian. Hàm Green tổng quát hóa ý tưởng đó để ta biểu diễn nghiệm của bài toán với dữ liệu hoặc nguồn bất kỳ bằng công thức tích phân chập.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nguồn điểm nhiệt tức thời
- Bài toán: Đặt một lượng nhiệt tập trung tại một điểm và quan sát nó lan đi.
- Mô hình:
$$ u(x,t)=G(x,t)*u_0(x). $$
- Giả thiết và giới hạn: Hệ tuyến tính, miền vô hạn hoặc Green thích hợp với biên.
- Diễn giải: Nghiệm cơ bản là "dấu vân tay" của hệ đối với nguồn điểm.

#### Xây dựng nghiệm từ Green
- Bài toán: Với dữ kiện đầu bất kỳ, nghiệm được dựng từ tích chập với heat kernel.
- Mô hình:
$$ u(x,t)=\int_{\mathbb{R}}G(x-\xi,t)u_0(\xi)\,d\xi. $$
- Giả thiết và giới hạn: Dữ kiện đầu đủ khả tích hay bị chặn thích hợp.
- Diễn giải: Nhiệt tại điểm hiện tại là trung bình có trọng số Gaussian của dữ kiện đầu.

### 2. Trực giác bổ sung và các kết nối

Nghiệm cơ bản cho phương trình nhiệt đóng vai trò giống Green theo biến thời gian. Một bẫy phổ biến là nghĩ kernel chỉ là công thức kỹ thuật; thật ra nó cho thấy rõ tính làm trơn, bảo toàn khối lượng, và lan truyền vô hạn vận tốc đặc trưng của phương trình nhiệt.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 800)
t = 0.2
G = (1 / np.sqrt(4 * np.pi * t)) * np.exp(-x**2 / (4 * t))

plt.plot(x, G)
plt.xlabel("x")
plt.ylabel("G")
plt.title("Nghiem co ban cua phuong trinh nhiet")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: heat kernel Green function animation
- search: fundamental solution heat equation Gaussian
- search: convolution with heat kernel visualization

### 5. Bài toán mẫu có bối cảnh thực

Nếu
$$ u_0(x)=\mathbf{1}_{[-1,1]}(x), $$
thì
$$ u(x,t)=\int_{-1}^{1}G(x-\xi,t)\,d\xi. $$
Điều này cho thấy profile ban đầu dạng "khối hộp" sẽ lập tức được làm trơn thành profile analytic khi $$ t>0 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm công thức tích chập với heat kernel và ý nghĩa nguồn điểm.

**Bậc sau đại học.** Bàn về semigroup, regularization tức thời và Green trên miền có biên.
