---
layout: post
title: "Nghiệm d'Alembert"
chapter: '10'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 02 Dalembert Solution]({{ site.imgurl }}/chapter_img/chapter10/02_dalembert_solution.svg)

## Mục tiêu

Bài học này trình bày nghiệm d'Alembert cho phương trình sóng một chiều trên toàn trục. Sau bài học, sinh viên cần hiểu công thức d'Alembert không chỉ như một biểu thức cần nhớ, mà như phát biểu rằng nghiệm được tách thành sóng truyền sang phải và sang trái, biết vai trò của dữ liệu vị trí và vận tốc ban đầu, và hiểu ý tưởng miền ảnh hưởng cùng tốc độ lan truyền hữu hạn của sóng.

## Kiến thức nền

Sinh viên nên nắm phương trình sóng một chiều, đổi biến cơ bản và điều kiện đầu $$ u(x,0)=f(x),\qquad u_t(x,0)=g(x) $$. Đây là bài cốt lõi để hiểu tính lan truyền của sóng trước khi chuyển sang miền hữu hạn và sóng dừng.

## Dẫn nhập

Nếu phương trình nhiệt kể câu chuyện "dữ liệu bị làm mượt", thì nghiệm d'Alembert kể câu chuyện khác hẳn: dữ liệu ban đầu được tách thành hai phần và truyền đi theo hai hướng. Điều này làm phương trình sóng trở thành mô hình tự nhiên cho lan truyền tín hiệu, âm thanh, xung cơ học và nhiều hiện tượng khác có tốc độ lan truyền hữu hạn.

Đây là một trong những công thức đẹp nhất của PDE cổ điển vì nó cho ta thấy cấu trúc nghiệm một cách hoàn toàn trong suốt. Không cần phổ, không cần chuỗi vô hạn, chỉ cần nhìn đúng hệ tọa độ đặc trưng là bản chất của nghiệm lộ ra.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu ta kéo một đoạn dây lên rồi thả, hình dạng ban đầu không đứng yên một chỗ. Nó tách ra thành hai xung, một đi sang phải và một đi sang trái. Nghiệm d'Alembert chính là phát biểu toán học của hình ảnh vật lý này.

### Cách nhìn hình ảnh

Trong mặt phẳng $$ (x,t) $$, các đường $$ x-ct=\text{hằng số} $$ và $$ x+ct=\text{hằng số} $$ là các đặc trưng. Dữ liệu lan dọc theo những đường này. Vì vậy giá trị của nghiệm tại $$ (x,t) $$ chỉ nhận thông tin từ đoạn $$ [x-ct,x+ct] $$ trên trục ban đầu. Hình ảnh này là chìa khóa để hiểu miền ảnh hưởng và tốc độ truyền hữu hạn.

### Cách nhìn hình thức

Xét $$ u_{tt}=c^2u_{xx} $$ trên toàn trục. Đặt $$ \xi=x-ct,\qquad \eta=x+ct $$. Trong tọa độ mới, phương trình trở thành $$ u_{\xi\eta}=0 $$. Do đó nghiệm tổng quát có dạng $$ u(x,t)=F(x-ct)+G(x+ct) $$. Nếu điều kiện đầu là $$ u(x,0)=f(x),\qquad u_t(x,0)=g(x) $$, thì công thức d'Alembert là

$$
u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}
+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.
$$

## Những ngộ nhận thường gặp

- "Nghiệm d'Alembert chỉ là công thức khép kín đặc biệt." Sai. Nó tiết lộ bản chất lan truyền theo đặc trưng của phương trình sóng.
- "Dữ liệu tại một điểm ảnh hưởng ngay toàn miền." Không đúng; thông tin lan với tốc độ hữu hạn

$$ c. $$
- "Nếu

$$ g=0 $$

thì sóng đứng yên." Sai; dữ liệu hình dạng ban đầu vẫn tách thành hai sóng truyền ngược chiều.
- "Công thức d'Alembert áp dụng nguyên xi cho đoạn hữu hạn." Không phải; trên đoạn hữu hạn ta còn phải xử lý biên bằng phản xạ hay tách biến.

## Tiến trình học tập đề xuất

### Bước 1: Đổi sang biến đặc trưng

Đây là điểm kỹ thuật mở khóa toàn bài.

### Bước 2: Hiểu nghiệm dạng

$$ F(x-ct)+G(x+ct) $$

Đây là phát biểu sóng phải và sóng trái.

### Bước 3: Ghép điều kiện đầu

Sinh viên cần thấy rõ vai trò khác nhau của $$ f $$ và

$$ g. $$

### Bước 4: Diễn giải miền ảnh hưởng

Đây là lợi ích khái niệm lớn nhất của bài.

### Các checkpoint

- Sinh viên có giải thích được vì sao các đặc trưng là

$$ x\pm ct $$

hay không.
- Sinh viên có biết phần nào của công thức đến từ dữ liệu vị trí và phần nào đến từ dữ liệu vận tốc hay không.
- Sinh viên có diễn giải được tốc độ lan truyền hữu hạn bằng lời hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Dữ liệu hình dạng, không có vận tốc đầu

Nếu $$ u(x,0)=f(x),\qquad u_t(x,0)=0 $$, thì

$$ u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}. $$

Nghĩa là hình dạng ban đầu tách thành hai bản sao dịch chuyển ngược chiều nhau. Đây là ví dụ quan trọng nhất để sinh viên nhìn ra bản chất truyền sóng.

### Ví dụ 2: Sóng điều hòa

Nếu $$ f(x)=\sin x,\qquad g(x)=0 $$, thì

$$
u(x,t)=\frac{\sin(x-ct)+\sin(x+ct)}{2}
=\sin x\cos(ct).
$$

Ví dụ này cho thấy cùng một nghiệm có thể được hiểu vừa như tổng hai sóng chạy, vừa như một sóng đứng.

### Ví dụ 3: Chỉ có vận tốc đầu

Nếu $$ f(x)=0,\qquad g(x)=\delta(x) $$, thì

$$ u(x,t)=\frac{1}{2c}\mathbf 1_{\lvert x\rvert<ct}. $$

Đây là ví dụ rất mạnh về mặt trực giác: một xung vận tốc điểm tạo ra một vùng ảnh hưởng hữu hạn lan rộng với tốc độ

$$ c. $$

### Ví dụ 4: Miền ảnh hưởng

Giá trị $$ u(x,t) $$ chỉ phụ thuộc vào $$ f $$ và $$ g $$ trên đoạn $$ [x-ct,x+ct] $$. Nếu dữ liệu ban đầu bằng 0 trên đoạn này, thì nghiệm tại $$ (x,t) $$ cũng không nhận ảnh hưởng từ bên ngoài đoạn đó. Đây là điểm khác biệt lớn nhất với phương trình nhiệt.

## Câu hỏi khái niệm

1. Vì sao nghiệm d'Alembert cho thấy sóng truyền với tốc độ hữu hạn?
2. Dữ liệu vị trí ban đầu và dữ liệu vận tốc ban đầu đóng vai trò khác nhau như thế nào trong công thức?
3. Vì sao cùng một nghiệm có thể được hiểu vừa là tổng hai sóng chạy vừa là một sóng đứng trong vài trường hợp?

## Bài toán ứng dụng

1. Một xung ngắn được truyền trên dây rất dài. Vì sao sau đó ta quan sát thấy hai xung tách ra và đi về hai phía?
2. Trong truyền tín hiệu, vì sao miền ảnh hưởng hữu hạn là đặc điểm vật lý quan trọng?
3. Trong cơ học, vì sao cần cả vị trí ban đầu và vận tốc ban đầu để xác định duy nhất nghiệm của phương trình sóng?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu kéo dây lên rồi thả, hình dạng ban đầu đi đâu?"
- Vẽ các đường đặc trưng

$$ x\pm ct=\text{hằng số} $$

và yêu cầu sinh viên mô tả dữ liệu đang lan dọc theo chúng.
- Hỏi cả lớp: "Điều gì trong công thức d'Alembert chứng minh rằng thông tin không lan tức thời?"
- Cho sinh viên tự kiểm tra một ví dụ ngắn như

$$ f(x)=\sin x,\ g(x)=0 $$

để nối công thức với hình ảnh sóng đứng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào công thức $$ u=F(x-ct)+G(x+ct) $$ trước khi đi đến dạng đầy đủ với tích phân. Khi đã thấy sóng phải và sóng trái, phần còn lại sẽ dễ hiểu hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi dùng công thức d'Alembert để phân tích phản xạ trên đoạn hữu hạn bằng phương pháp mở rộng, hoặc so sánh với phương trình truyền tải bậc nhất.

## Tóm tắt dễ nhớ

Nghiệm d'Alembert nói rằng nghiệm của phương trình sóng một chiều là tổng của một sóng đi sang phải và một sóng đi sang trái. Thông tin lan theo đặc trưng $$ x\pm ct $$, nên sóng có tốc độ truyền hữu hạn và miền ảnh hưởng rõ ràng.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Xung trên dây vô hạn
- Bài toán: Một xung ban đầu trên dây truyền sang trái và phải sau khi được tạo ra.
- Mô hình:
$$
u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.
$$
- Giả thiết và giới hạn: Miền vô hạn, tốc độ sóng hằng, không có biên.
- Diễn giải: Nghiệm cho thấy dữ liệu ban đầu di chuyển mà không đổi dạng trong môi trường lý tưởng.

#### Xung điện trên đường truyền
- Bài toán: Điện áp trên cáp dài, trong xấp xỉ không tổn hao, có dạng tổng của sóng tiến và sóng lùi.
- Mô hình: Sau chuẩn hóa, điện áp thỏa một phương trình sóng một chiều với nghiệm kiểu d'Alembert.
- Giả thiết và giới hạn: Bỏ qua điện trở và tổn hao, tham số đường truyền đồng nhất.
- Diễn giải: Công thức d'Alembert xuất hiện tự nhiên trong kỹ thuật điện.

### 2. Trực giác bổ sung và các kết nối

Nghiệm d'Alembert cho thấy dữ liệu ban đầu không bị "phân tán" ngay lập tức; nó chỉ được tách thành các thành phần chạy trái và phải. Đây là một cách rất rõ để thấy phương trình sóng có tốc độ truyền hữu hạn, trái ngược với hiệu ứng làm trơn tức thời của phương trình nhiệt.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 800)
f = np.exp(-(x + 1.5) ** 2)
g = np.zeros_like(x)

for t in [0.0, 0.8, 1.6]:
    u = 0.5 * np.exp(-((x - t) + 1.5) ** 2) + 0.5 * np.exp(-((x + t) + 1.5) ** 2)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Xung ban dau tach thanh hai song chay")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: dAlembert solution animation pulse splitting
- search: transmission line lossless wave equation
- search: finite propagation speed wave equation

### 5. Bài toán mẫu có bối cảnh thực

Nếu vận tốc ban đầu bằng không và độ lệch ban đầu là
$$ u(x,0)=e^{-x^2}, $$
thì
$$
u(x,t)=\frac{1}{2}e^{-(x-ct)^2}+\frac{1}{2}e^{-(x+ct)^2}.
$$
Một xung ban đầu đối xứng tách thành hai xung giống hệt nhau đi ngược chiều. Đây là hình ảnh cơ học kinh điển của dây vô hạn.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu cách dữ liệu ban đầu tạo ra sóng đi sang trái và phải.

**Bậc sau đại học.** Liên hệ với nghiệm cơ bản của toán tử hyperbolic và nguyên lý miền ảnh hưởng.
