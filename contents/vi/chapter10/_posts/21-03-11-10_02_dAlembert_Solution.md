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

Bài học này trình bày nghiệm d'Alembert cho phương trình sóng một chiều trên toàn trục thực. Sau bài học, sinh viên cần hiểu công thức d'Alembert như sự phân tách nghiệm thành hai sóng truyền ngược chiều sang phải và sang trái, nắm rõ vai trò riêng biệt của vị trí ban đầu và vận tốc ban đầu, đồng thời hiểu khái niệm miền ảnh hưởng và tốc độ lan truyền hữu hạn của sóng.

## Kiến thức nền

Sinh viên cần nắm phương trình sóng một chiều, kỹ thuật đổi biến đơn giản và điều kiện ban đầu $$ u(x,0)=f(x),\qquad u_t(x,0)=g(x) $$. Đây là nền tảng để hiểu bản chất lan truyền của sóng trước khi xét miền hữu hạn và sóng dừng.

## Dẫn nhập

Nếu phương trình nhiệt mô tả quá trình làm mượt dữ liệu, thì nghiệm d'Alembert thể hiện một cơ chế hoàn toàn khác: dữ liệu ban đầu tách thành hai thành phần và truyền đi theo hai chiều ngược nhau với tốc độ hữu hạn. Nhờ đặc tính này, phương trình sóng là mô hình tự nhiên cho sự truyền tín hiệu, sóng âm và xung cơ học.

Công thức d'Alembert cho thấy cấu trúc nghiệm một cách trực tiếp mà không cần chuỗi vô hạn hay phân tích phổ: chỉ cần chuyển sang hệ tọa độ đặc trưng thích hợp, bản chất hình học của nghiệm sẽ hiện ra rõ ràng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi kéo một đoạn dây lên khỏi vị trí cân bằng rồi thả ra, hình dạng ban đầu không đứng yên tại chỗ mà tách làm hai xung nhỏ hơn, một xung chạy sang phải và một xung chạy sang trái. Công thức d'Alembert diễn đạt chính xác hiện tượng vật lý này.

### Cách nhìn hình ảnh

Trong mặt phẳng không gian–thời gian $$ (x,t) $$, các đường thẳng $$ x-ct=\text{hằng số} $$ và $$ x+ct=\text{hằng số} $$ là các đường đặc trưng. Thông tin lan truyền dọc theo các đường này, nên giá trị nghiệm tại điểm $$ (x,t) $$ chỉ phụ thuộc vào dữ liệu ban đầu trên đoạn $$ [x-ct,x+ct] $$. Đây là hình ảnh trực quan của miền ảnh hưởng và tốc độ truyền hữu hạn.

### Cách nhìn hình thức

Xét phương trình $$ u_{tt}=c^2u_{xx} $$ trên toàn trục thực. Đổi biến đặc trưng $$ \xi=x-ct,\qquad \eta=x+ct $$, phương trình chuyển thành $$ u_{\xi\eta}=0 $$, nên nghiệm tổng quát có dạng $$ u(x,t)=F(x-ct)+G(x+ct) $$. Với điều kiện ban đầu $$ u(x,0)=f(x),\qquad u_t(x,0)=g(x) $$, ta thu được công thức d'Alembert:

$$
u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}
+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.
$$

## Những ngộ nhận thường gặp

- "Nghiệm d'Alembert chỉ là một công thức đóng đặc biệt." Sai; nó bộc lộ trực tiếp bản chất lan truyền dọc theo đường đặc trưng của phương trình sóng.
- "Nhiễu loạn tại một điểm ảnh hưởng ngay lập tức đến toàn bộ không gian." Không đúng; thông tin chỉ lan truyền với tốc độ hữu hạn $$ c $$.
- "Nếu vận tốc ban đầu $$ g=0 $$ thì dây đứng yên." Sai; độ lệch ban đầu vẫn tách thành hai sóng truyền theo hai hướng ngược nhau.
- "Công thức d'Alembert áp dụng nguyên vẹn cho đoạn hữu hạn." Không chính xác; trên đoạn hữu hạn cần xử lý thêm phản xạ tại biên bằng phương pháp mở rộng hoặc tách biến.

## Tiến trình học tập đề xuất

### Bước 1: Đổi sang biến đặc trưng

Thực hiện phép đổi biến $$ \xi=x-ct,\ \eta=x+ct $$ để rút gọn phương trình về $$ u_{\xi\eta}=0 $$.

### Bước 2: Hiểu cấu trúc nghiệm $$ F(x-ct)+G(x+ct) $$

Nhận diện thành phần sóng truyền sang phải và sóng truyền sang trái.

### Bước 3: Áp đặt điều kiện ban đầu

Xác định rõ đóng góp riêng biệt của độ lệch ban đầu $$ f $$ và vận tốc ban đầu $$ g $$.

### Bước 4: Diễn giải miền ảnh hưởng và miền phụ thuộc

Liên hệ đoạn $$ [x-ct,x+ct] $$ với tốc độ lan truyền hữu hạn của thông tin.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao các đường đặc trưng có dạng $$ x\pm ct=\text{hằng số} $$ hay không.
- Sinh viên có phân biệt được phần nghiệm do vị trí ban đầu và phần nghiệm do vận tốc ban đầu tạo ra hay không.
- Sinh viên có diễn đạt được ý nghĩa của tốc độ lan truyền hữu hạn bằng lời hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Có độ lệch ban đầu, vận tốc ban đầu bằng 0

Nếu $$ u(x,0)=f(x),\qquad u_t(x,0)=0 $$, công thức d'Alembert rút gọn thành

$$ u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}. $$

Hình dạng ban đầu tách thành hai bản sao có biên độ bằng một nửa và dịch chuyển ngược chiều nhau với tốc độ $$ c $$.

### Ví dụ 2: Sóng điều hòa

Nếu $$ f(x)=\sin x,\qquad g(x)=0 $$, ta thu được

$$
u(x,t)=\frac{\sin(x-ct)+\sin(x+ct)}{2}
=\sin x\cos(ct).
$$

Ví dụ này cho thấy cùng một nghiệm có thể được nhìn nhận đồng thời như sự chồng chất của hai sóng chạy ngược chiều và như một sóng dừng.

### Ví dụ 3: Chỉ có vận tốc ban đầu dạng xung điểm

Nếu $$ f(x)=0,\qquad g(x)=\delta(x) $$, ta có

$$ u(x,t)=\frac{1}{2c}\mathbf 1_{\lvert x\rvert<ct}. $$

Một xung vận tốc tập trung tại gốc tạo ra vùng nhiễu loạn hữu hạn mở rộng về hai phía với tốc độ $$ c $$.

### Ví dụ 4: Miền phụ thuộc

Giá trị $$ u(x,t) $$ chỉ phụ thuộc vào $$ f $$ và $$ g $$ trên đoạn $$ [x-ct,x+ct] $$. Nếu dữ liệu ban đầu bằng 0 trên đoạn này, nghiệm tại $$ (x,t) $$ cũng bằng 0 bất kể dữ liệu bên ngoài đoạn đó ra sao. Đây là điểm khác biệt cơ bản so với phương trình nhiệt.

## Câu hỏi khái niệm

1. Vì sao công thức d'Alembert chứng tỏ sóng lan truyền với tốc độ hữu hạn?
2. Vị trí ban đầu và vận tốc ban đầu đóng vai trò khác nhau như thế nào trong nghiệm d'Alembert?
3. Vì sao trong một số trường hợp, cùng một nghiệm vừa có thể xem là tổng hai sóng chạy vừa có thể xem là một sóng đứng?

## Bài toán ứng dụng

1. Một xung ngắn được tạo ra ở giữa một sợi dây rất dài rồi thả tự do. Vì sao sau đó ta quan sát thấy hai xung tách ra và truyền về hai phía?
2. Trong truyền tín hiệu, vì sao miền ảnh hưởng hữu hạn là một đặc trưng vật lý quan trọng?
3. Trong cơ học, vì sao cần biết cả vị trí ban đầu lẫn vận tốc ban đầu để xác định duy nhất chuyển động của dây?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Nếu kéo một đoạn dây lên rồi thả nhẹ từ trạng thái nghỉ, hình dạng ban đầu sẽ chuyển động ra sao?"
- Vẽ các đường đặc trưng $$ x\pm ct=\text{hằng số} $$ trên mặt phẳng $$ (x,t) $$ để sinh viên theo dõi hướng lan truyền dữ liệu.
- Đặt câu hỏi: "Chi tiết nào trong công thức d'Alembert khẳng định thông tin không truyền đi tức thời?"
- Cho sinh viên tự kiểm chứng ví dụ $$ f(x)=\sin x,\ g(x)=0 $$ để nối nghiệm sóng chạy với hình ảnh sóng dừng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào dạng tổng quát $$ u=F(x-ct)+G(x+ct) $$ trước khi đưa vào số hạng tích phân của vận tốc đầu. Khi đã nắm rõ hình ảnh sóng chạy sang phải và sang trái, công thức đầy đủ sẽ dễ hiểu hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên áp dụng công thức d'Alembert kết hợp phép mở rộng lẻ/chẵn để mô tả hiện tượng phản xạ sóng trên đoạn hữu hạn, hoặc so sánh với phương trình truyền tải bậc nhất.

## Tóm tắt dễ nhớ

Nghiệm d'Alembert biểu diễn nghiệm của phương trình sóng một chiều như tổng của một sóng truyền sang phải và một sóng truyền sang trái. Dữ liệu lan truyền dọc theo các đường đặc trưng $$ x\pm ct $$, đảm bảo tốc độ lan truyền hữu hạn và miền ảnh hưởng xác định rõ ràng.

## Video tham khảo

- Xem trước: [PDE 10 | Wave equation: d'Alembert's formula](https://www.youtube.com/watch?v=j2G91naZ8bo) — commutant, tiếng Anh. Thiết lập công thức d'Alembert cho phương trình sóng trên dây vô hạn.
- [D'Alembert Solution to the Wave Equation](https://www.youtube.com/watch?v=Sc21aPg2RyE) — Faculty of Khan, tiếng Anh. Trình bày chi tiết cách suy ra và áp dụng nghiệm d'Alembert.
- [The Method of Characteristics and the Wave Equation](https://www.youtube.com/watch?v=eI2x99SxJgU) — Steve Brunton, tiếng Anh. Giải thích phương pháp đường đặc trưng làm nền tảng cho công thức d'Alembert.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Xung cơ học trên dây vô hạn
- Bài toán: Theo dõi một xung ban đầu lan truyền về hai phía trên sợi dây rất dài.
- Mô hình:
$$
u(x,t)=\frac{f(x-ct)+f(x+ct)}{2}+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.
$$
- Giả thiết và giới hạn: Miền vô hạn, tốc độ sóng không đổi, không có phản xạ biên.
- Diễn giải: Trong môi trường lý tưởng không tán sắc và không tổn hao, hai xung thành phần giữ nguyên hình dạng khi di chuyển.

#### Xung điện trên đường dây truyền tải
- Bài toán: Điện áp trên đường dây truyền tải dài không tổn hao biểu diễn thành tổng của sóng thuận và sóng nghịch.
- Mô hình: Sau khi chuẩn hóa, điện áp thỏa mãn phương trình sóng một chiều với nghiệm dạng d'Alembert.
- Giả thiết và giới hạn: Bỏ qua điện trở và tổn hao, đường truyền đồng nhất.
- Diễn giải: Công thức d'Alembert xuất hiện trực tiếp trong phân tích mạch và đường truyền cao tần.

### 2. Trực giác bổ sung và các kết nối

Nghiệm d'Alembert cho thấy dữ liệu ban đầu không bị làm phẳng tức thì mà tách thành các thành phần dịch chuyển sang trái và sang phải với tốc độ hữu hạn, trái ngược hoàn toàn với hiệu ứng làm trơn tức thời của phương trình nhiệt.

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

Nếu vận tốc ban đầu bằng 0 và độ lệch ban đầu là
$$ u(x,0)=e^{-x^2}, $$
thì nghiệm là
$$
u(x,t)=\frac{1}{2}e^{-(x-ct)^2}+\frac{1}{2}e^{-(x+ct)^2}.
$$
Xung đối xứng ban đầu tách thành hai xung giống hệt nhau có biên độ bằng một nửa và chuyển động ngược chiều nhau.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững công thức d'Alembert và cách dữ liệu ban đầu tách thành hai sóng truyền ngược chiều.

**Bậc sau đại học.** Liên hệ với nghiệm cơ bản của toán tử hyperbolic và nguyên lý miền ảnh hưởng hữu hạn.
