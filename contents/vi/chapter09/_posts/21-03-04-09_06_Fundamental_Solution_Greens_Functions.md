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

Bài học này trình bày nghiệm cơ bản và hàm Green theo góc nhìn đáp ứng xung của phương trình nhiệt. Sau bài học, sinh viên cần hiểu nghiệm cơ bản là nghiệm ứng với nguồn điểm, nắm vai trò của nhân Gaussian, vận dụng được công thức biểu diễn nghiệm qua hàm Green và thấy rõ vì sao chỉ cần biết đáp ứng với một xung đơn vị là đủ để xây dựng nghiệm cho dữ liệu và nguồn nhiệt tổng quát.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt trên miền vô hạn, phép tích chập và khái niệm hàm delta Dirac ở mức trực giác. Kiến thức về hàm Green trong phương trình vi phân thường (ODE) sẽ giúp nhận ra sự nhất quán của cùng một ý tưởng khi chuyển sang PDE.

## Dẫn nhập

Một cách tiếp cận tự nhiên để khảo sát hệ tuyến tính là đặt câu hỏi: nếu tác động lên hệ bằng một xung đơn giản nhất, hệ sẽ đáp ứng ra sao? Đối với phương trình nhiệt, xung cơ bản nhất là một lượng nhiệt đơn vị tập trung tại đúng một điểm ở thời điểm ban đầu. Nghiệm tương ứng với xung đó chính là nghiệm cơ bản.

Từ nghiệm cơ bản, ta xây dựng nên hàm Green. Cách nhìn này tạo ra bước chuyển quan trọng trong giải PDE: thay vì giải lại bài toán từ đầu cho mỗi điều kiện ban đầu hoặc mỗi hàm nguồn mới, ta chỉ cần xác định đáp ứng với xung đơn vị rồi chồng chất các đáp ứng đó bằng phép tích phân.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung việc chạm đầu mỏ hàn nóng vào đúng một điểm trên một thanh kim loại rất dài trong khoảng thời gian rất ngắn. Ban đầu nhiệt lượng tập trung gần như hoàn toàn tại điểm tiếp xúc, sau đó lan tỏa dần sang hai phía. Nghiệm cơ bản chính là biểu thức toán học mô tả quá trình lan tỏa này.

### Cách nhìn hình ảnh

Tại thời điểm $$ t=0 $$, phân bố nhiệt giống như một đỉnh nhọn tập trung tại một điểm. Ngay khi $$ t>0 $$, đỉnh nhọn ấy chuyển thành đường cong Gaussian có đỉnh thấp dần và bề rộng tăng dần theo thời gian, trong khi diện tích dưới đường cong (tổng nhiệt lượng) vẫn không đổi.

### Cách nhìn hình thức

Nghiệm cơ bản của phương trình nhiệt trên $$ \mathbb R $$ là nghiệm của bài toán

$$
\Phi_t=\alpha^2\Phi_{xx},
\qquad
\Phi(x,0)=\delta(x).
$$

Biểu thức tường minh của nó là

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right),
\qquad t>0.
$$

Hàm Green $$ G(x,\xi,t) $$ là nghiệm ứng với xung đặt tại vị trí $$ \xi $$. Trên toàn trục thực, do tính bất biến theo phép tịnh tiến, ta có

$$ G(x,\xi,t)=\Phi(x-\xi,t). $$

## Những ngộ nhận thường gặp

- "Delta Dirac là một hàm số thông thường nhận giá trị vô hạn tại gốc." Không chính xác; cần hiểu nó như một nguồn điểm theo nghĩa hàm suy rộng (phân phối) hoặc giới hạn của dãy hàm chuẩn hóa.
- "Nghiệm cơ bản chỉ là một trường hợp riêng ít ứng dụng." Sai; nó là viên gạch nền tảng để xây dựng công thức nghiệm tổng quát qua hàm Green.
- "Hàm Gaussian xuất hiện chỉ vì thuận tiện cho biến đổi Fourier." Không chỉ vậy; nó phản ánh trực tiếp quy luật lan tỏa vật lý của một xung nhiệt.
- "Hàm Green chỉ bổ sung thêm một công thức tích phân." Không đúng; nó cung cấp cách nhìn tổng quát về toán tử nghịch đảo của phương trình nhiệt.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu mô hình nguồn điểm

Làm quen với ý nghĩa vật lý của hàm delta Dirac như một xung nhiệt lý tưởng hóa.

### Bước 2: Khảo sát nghiệm cơ bản trên toàn trục thực

Đây là trường hợp tiêu chuẩn và gọn gàng nhất.

### Bước 3: Mở rộng sang hàm Green

Dịch chuyển vị trí xung từ gốc tọa độ sang điểm $$ \xi $$ bất kỳ.

### Bước 4: Biểu diễn nghiệm tổng quát qua hàm Green

Sử dụng phép tích chập và công thức Duhamel để xử lý cả điều kiện đầu lẫn nguồn nhiệt.

### Các điểm kiểm tra

- Sinh viên có giải thích được ý nghĩa vật lý của nghiệm cơ bản hay không.
- Sinh viên có biết vì sao tích phân toàn miền của nhân Gaussian luôn bằng 1 hay không.
- Sinh viên có hiểu công thức Green như sự chồng chất của vô số đáp ứng xung hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bảo toàn tổng nhiệt lượng

Với nghiệm cơ bản

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}
\exp\left(-\frac{x^2}{4\alpha^2 t}\right),
$$

ta có

$$ \int_{\mathbb R}\Phi(x,t)\,dx=1. $$

Đẳng thức này khẳng định tổng nhiệt lượng của xung ban đầu được bảo toàn hoàn toàn trong quá trình khuếch tán.

### Ví dụ 2: Nghiệm từ điều kiện ban đầu

Với điều kiện ban đầu $$ u(x,0)=f(x) $$, nghiệm được biểu diễn dưới dạng

$$ u(x,t)=\int_{\mathbb R}\Phi(x-y,t)f(y)\,dy. $$

Nhiệt độ tại vị trí $$ x $$ vào thời điểm $$ t $$ chính là trung bình có trọng số Gaussian của phân bố nhiệt độ ban đầu.

### Ví dụ 3: Bài toán có nguồn nhiệt theo thời gian

Khi có thêm nguồn nhiệt $$ Q(x,t) $$, công thức Duhamel cho nghiệm tổng quát

$$
u(x,t)=\int_{\mathbb R}\Phi(x-y,t)f(y)\,dy
+\int_0^t\int_{\mathbb R}\Phi(x-y,t-s)Q(y,s)\,dy\,ds.
$$

Đây là công thức biểu diễn tổng quát nhất của bài học, kết hợp tác động của điều kiện đầu và tác động tích lũy của nguồn nhiệt theo thời gian.

### Ví dụ 4: Tính đối xứng của nghiệm cơ bản

Ta có $$ \Phi(x,t)=\Phi(-x,t) $$, cho thấy một xung nhiệt đặt tại gốc tỏa đều về hai phía với tốc độ như nhau. Ví dụ này minh họa mối liên hệ trực tiếp giữa tính đối xứng của miền và tính đối xứng của hàm Green.

## Câu hỏi khái niệm

1. Vì sao biết đáp ứng của hệ đối với một xung điểm lại đủ để xây dựng nghiệm cho dữ liệu ban đầu tổng quát?
2. Dạng hàm Gaussian của nghiệm cơ bản thể hiện những tính chất vật lý nào của quá trình khuếch tán?
3. Khái niệm hàm Green thay đổi cách nhìn của ta về nghiệm PDE như thế nào?

## Bài toán ứng dụng

1. Trong truyền nhiệt, vì sao việc xác định phân bố lan tỏa của một xung nhiệt điểm lại là thông tin nền tảng?
2. Trong lý thuyết xác suất, nghiệm cơ bản của phương trình nhiệt liên hệ như thế nào với hàm mật độ của chuyển động Brown?
3. Trong kỹ thuật, khi một nguồn nhiệt tác động ngắn và cục bộ, vì sao hàm Green là công cụ tự nhiên để mô hình hóa đáp ứng của hệ?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Nếu đặt một lượng nhiệt nhỏ tập trung tại đúng một điểm, phân bố nhiệt sẽ thay đổi ra sao ngay sau đó?"
- Minh họa quá trình một đỉnh nhọn biến đổi thành đường cong Gaussian trải rộng dần.
- Đặt câu hỏi: "Khi đã biết đáp ứng với một xung đơn vị, ta làm thế nào để xử lý một nguồn nhiệt phân bố liên tục?"
- Yêu cầu sinh viên diễn giải công thức Duhamel bằng lời theo ý tưởng cộng dồn các xung nhiệt theo thời gian.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào trực giác nguồn điểm, hình dạng đường cong Gaussian và ý nghĩa của phép tích chập. Chưa cần đi sâu ngay vào lý thuyết hàm suy rộng nếu điều đó làm gián đoạn mạch ý tưởng chính.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên suy ra công thức hàm Green bằng biến đổi Fourier, hoặc so sánh hàm Green của phương trình nhiệt với hàm Green của phương trình elliptic và ODE đã học trước đó.

## Tóm tắt dễ nhớ

Nghiệm cơ bản của phương trình nhiệt là đáp ứng của hệ đối với một xung nhiệt điểm và có dạng hàm Gaussian. Hàm Green mở rộng ý tưởng này, cho phép biểu diễn nghiệm với điều kiện đầu hoặc nguồn nhiệt tổng quát dưới dạng tích phân chập.

## Video tham khảo

- Xem trước: [Introducing Green's Functions for Partial Differential Equations (PDEs)](https://www.youtube.com/watch?v=xNqLZnM-PPY) — Faculty of Khan, tiếng Anh. Giới thiệu khái niệm và cách sử dụng hàm Green cho phương trình đạo hàm riêng.
- [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, tiếng Anh. Minh họa nghiệm cơ bản Gaussian xuất hiện từ biến đổi Fourier ngược của nhân phổ nhiệt.
- [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, tiếng Anh. Giải thích trực giác nguồn điểm và đáp ứng xung làm nền cho nghiệm cơ bản.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nguồn điểm nhiệt tức thời
- Bài toán: Đặt một lượng nhiệt tập trung tại một điểm rồi theo dõi sự lan tỏa theo thời gian.
- Mô hình:
$$ u(x,t)=G(x,t)*u_0(x). $$
- Giả thiết và giới hạn: Hệ tuyến tính trên miền vô hạn, hoặc sử dụng hàm Green tương thích với điều kiện biên.
- Diễn giải: Nghiệm cơ bản đóng vai trò đặc trưng đáp ứng của hệ trước một nguồn điểm.

#### Xây dựng nghiệm từ hàm Green
- Bài toán: Tìm nghiệm ứng với một phân bố nhiệt ban đầu bất kỳ thông qua tích chập với nhân nhiệt.
- Mô hình:
$$ u(x,t)=\int_{\mathbb{R}}G(x-\xi,t)u_0(\xi)\,d\xi. $$
- Giả thiết và giới hạn: Dữ kiện ban đầu thỏa mãn điều kiện khả tích hoặc bị chặn thích hợp.
- Diễn giải: Nhiệt độ tại một điểm là trung bình có trọng số Gaussian của dữ kiện ban đầu.

### 2. Trực giác bổ sung và các kết nối

Nghiệm cơ bản của phương trình nhiệt đóng vai trò như hàm Green phụ thuộc thời gian. Nhân nhiệt không chỉ là một công thức tích phân mà còn thể hiện rõ ba đặc trưng của phương trình nhiệt: làm trơn tức thời, bảo toàn tổng khối lượng và vận tốc lan truyền vô hạn.

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

Nếu dữ liệu ban đầu có dạng xung hộp
$$ u_0(x)=\mathbf{1}_{[-1,1]}(x), $$
thì nghiệm là
$$ u(x,t)=\int_{-1}^{1}G(x-\xi,t)\,d\xi. $$
Kết quả này cho thấy phân bố ban đầu có bước nhảy sắc nét lập tức trở thành hàm giải tích trơn với mọi $$ t>0 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững công thức tích chập với nhân nhiệt và ý nghĩa vật lý của nguồn điểm.

**Bậc sau đại học.** Tìm hiểu lý thuyết nửa nhóm, tính làm trơn tức thời và cách xây dựng hàm Green trên miền có biên.
