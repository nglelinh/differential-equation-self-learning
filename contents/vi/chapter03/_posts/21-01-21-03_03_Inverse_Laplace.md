---
layout: post
title: "03-03 Biến đổi Laplace Ngược"
chapter: '03'
order: 3
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu vai trò của biến đổi Laplace ngược như bước quay lại miền thời gian, biết sử dụng phân tích phân thức đơn cho các phân thức hữu tỉ, và nhận ra rằng việc giải trong miền $$ s $$ chỉ có ý nghĩa khi ta đọc lại được nghiệm trong thời gian. Sinh viên cũng sẽ luyện kỹ năng nhận dạng mẫu từ bảng ngược một cách có hệ thống.

## Kiến thức nền
Sinh viên cần nắm bảng Laplace cơ bản, kỹ năng phân tích phân thức đơn và cách đọc các mẫu quen thuộc như
$$
\frac{1}{s-a},\qquad \frac{s}{s^2+b^2},\qquad \frac{b}{s^2+b^2}.
$$
Đây là bài giao thoa giữa đại số hữu tỉ và ý nghĩa động học.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-03 Biến đổi Laplace Ngược]({{ site.imgurl }}/chapter_img/chapter03/03_03_inverse_laplace.svg)

Miền Laplace rất tiện cho tính toán, nhưng con người và các hệ vật lý sống trong miền thời gian. Vì vậy sau khi đưa bài toán sang miền $$ s $$, ta phải quay về. Nếu không, lời giải vẫn chỉ là một biểu thức đại số chưa kể câu chuyện vật lý của hệ. Biến đổi Laplace ngược chính là cây cầu quay lại ấy.

Trong khóa học này, ta không đi sâu vào công thức tích phân Bromwich một cách đầy đủ. Thay vào đó, ta học một phiên bản thực dụng và rất mạnh: nhận dạng mẫu từ bảng và phân tích phân thức đơn. Đây là cách hầu hết các bài toán kỹ thuật đầu tiên được xử lý.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nếu biến đổi Laplace là nén một tín hiệu thời gian vào một biểu thức đại số, thì biến đổi ngược là giải nén nó. Những cực và hệ số trong phân thức theo $$ s $$ tương ứng với các mode mũ, dao động hay tăng trưởng trong thời gian.

### Cách nhìn hình ảnh
Một phân thức như
$$ \frac{1}{s-2} $$
gợi ra ngay một mode mũ $$ e^{2t} $$. Một mẫu như
$$ \frac{s}{s^2+9} $$
gợi ra dao động $$ \cos 3t $$. Vì vậy, việc lấy Laplace ngược giống như đọc cấu trúc thời gian ẩn trong hình dạng của phân thức.

### Cách nhìn hình thức
Nếu
$$ F(s)=\mathcal{L}\{f(t)\}, $$
thì
$$ f(t)=\mathcal{L}^{-1}\{F(s)\}. $$
Trong thực hành đầu chương, khi $$ F(s) $$ là hàm hữu tỉ, ta thường:

1. Phân tích thành tổng các phân thức đơn.
2. Ghép từng hạng với công thức bảng tương ứng.
3. Cộng lại để được hàm thời gian.

## Những ngộ nhận thường gặp
- "Biến đổi ngược chỉ là tra bảng ngược." Chưa đủ. Phần lớn bài cần phân tích phân thức đơn trước.
- "Một biểu thức theo $$ s $$ chỉ có một cách duy nhất để tách." Sai. Có thể có nhiều cách tách khác nhau, nhưng cần tách theo dạng phù hợp với bảng.
- "Nếu mẫu là bậc hai thì luôn cho sin." Sai. Cần xem tử số để phân biệt sin hay cos hoặc tổ hợp của cả hai.
- "Chỉ cần ra được biểu thức theo $$ s $$ là coi như đã giải xong." Sai. Ý nghĩa động học chỉ xuất hiện sau khi quay lại miền thời gian.

## Tiến trình học tập đề xuất
### Bước 1: Nhìn cấu trúc của $$ F(s) $$
Xem đó là mẫu bậc nhất, bậc hai hay tích của nhiều nhân tử.

### Bước 2: Phân tích phân thức đơn
Tách về tổng các hạng khớp với bảng.

### Bước 3: Ghép từng hạng với công thức ngược
Làm chậm và chính xác.

### Bước 4: Kiểm tra lại bằng Laplace xuôi nếu cần
Đây là cách tự kiểm tra rất tốt.

### Các checkpoint
- Sinh viên có chọn đúng dạng phân thức đơn hay không.
- Sinh viên có nhận ra khi nào cần cả tử số dạng $$ As+B $$ cho mẫu bậc hai hay không.
- Sinh viên có diễn giải lại được nghiệm trong thời gian hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mẫu bậc nhất đơn giản
Tính
$$ \mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\}. $$
Từ bảng:
$$ \mathcal{L}\{e^{3t}\}=\frac{1}{s-3}. $$
Vậy
$$
\mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\}=e^{3t}.
$$

### Ví dụ 2: Phân tích phân thức đơn
Tính
$$
\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\}.
$$
Ta viết
$$ \frac{1}{(s-1)(s+2)}=\frac{A}{s-1}+\frac{B}{s+2}. $$
Suy ra
$$ 1=A(s+2)+B(s-1). $$
Thay $$ s=1 $$:
$$ 1=3A \Rightarrow A=\frac{1}{3}. $$
Thay $$ s=-2 $$:
$$ 1=-3B \Rightarrow B=-\frac{1}{3}. $$
Vậy
$$
\frac{1}{(s-1)(s+2)}=\frac{1}{3}\frac{1}{s-1}-\frac{1}{3}\frac{1}{s+2}.
$$
Do đó
$$
\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\}=\frac{1}{3}e^t-\frac{1}{3}e^{-2t}.
$$

### Ví dụ 3: Mẫu bậc hai lượng giác
Tính
$$ \mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\}. $$
Từ công thức
$$ \mathcal{L}\{\sin 2t\}=\frac{2}{s^2+4}, $$
ta được
$$
\mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\}=\sin 2t.
$$

### Ví dụ 4: Tử số tổng quát trên mẫu bậc hai
Tính
$$ \mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\}. $$
Tách:
$$
\frac{s+1}{s^2+9}=\frac{s}{s^2+9}+\frac{1}{s^2+9}.
$$
Từ bảng:
$$
\mathcal{L}^{-1}\left\{\frac{s}{s^2+9}\right\}=\cos 3t,
$$
$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2+9}\right\}=\frac{1}{3}\sin 3t.
$$
Vậy
$$
\mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\}=\cos 3t+\frac{1}{3}\sin 3t.
$$

## Câu hỏi khái niệm
1. Vì sao phân tích phân thức đơn lại là bước trung gian tự nhiên khi lấy Laplace ngược?
2. Vì sao mẫu bậc hai có thể dẫn đến sin, cos hoặc tổ hợp của cả hai?
3. Một cực đơn tại $$ s=a $$ nói gì về hành vi thời gian của nghiệm?

## Bài toán ứng dụng
1. Trong một hệ cơ học, một phân thức có nhiều cực thực âm. Hãy giải thích vì sao điều đó gợi ra nhiều mode tắt dần trong thời gian.
2. Một tín hiệu đầu ra trong miền Laplace có mẫu số dạng $$ s^2+b^2 $$. Hãy giải thích điều gì về dao động của hệ.
3. Trong điều khiển, việc nhìn cực của hàm truyền cho biết điều gì về ổn định trước khi quay lại miền thời gian?

## Chiến lược giảng dạy tương tác
- Cho sinh viên chơi trò "dịch ngược": nhìn phân thức và đoán nhanh dạng nghiệm thời gian.
- Làm nổi bật bằng màu khác nhau các hạng phân tích phân thức đơn và hàm thời gian tương ứng.
- Cho mỗi nhóm một phân thức khác nhau để tách rồi ghép lại với bảng.
- Khuyến khích sinh viên kiểm tra lại bằng Laplace xuôi để tăng tự tin.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên yếu dùng bảng đối chiếu "mẫu theo $$ s $$" và "hàm theo $$ t $$". Bài toán của các em thường không phải là ý tưởng, mà là bị lẫn giữa nhiều mẫu rất giống nhau.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi xử lý các trường hợp cực lặp hoặc mẫu bậc hai bất khả quy với tử số tuyến tính tổng quát, rồi diễn giải ý nghĩa của từng hạng.

## Tóm tắt dễ nhớ
Lấy Laplace ngược là đọc lại thời gian từ miền $$ s $$. Muốn làm tốt, hãy nhìn cấu trúc của phân thức, tách nó thành những mảnh quen thuộc, rồi ghép với bảng ngược. Miền Laplace chỉ là trạm trung chuyển; đích cuối cùng luôn là hàm theo thời gian.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Đọc lại đáp ứng thời gian từ miền $$ s $$
- Bài toán: Sau khi giải ODE trong miền Laplace, kỹ sư vẫn cần quay về tín hiệu theo thời gian để diễn giải vật lý.
- Mô hình:
$$ F(s)\mapsto f(t)=\mathcal{L}^{-1}\{F(s)\}. $$
- Giả thiết và giới hạn: Thường làm việc với phân thức hữu tỉ ở mức cơ bản.
- Diễn giải: Các pole đơn cho mũ, cặp bậc hai cho sin-cos, pole lặp cho thừa số đa thức nhân mũ.

#### Cơ học và mode động
- Bài toán: Một biểu thức như
$$ \frac{1}{(s+1)(s+3)} $$
biểu diễn hai mode suy giảm.
- Mô hình: Phân tích phân thức đơn trước khi lấy Laplace ngược.
- Giả thiết và giới hạn: Bài toán tuyến tính với hệ số hằng.
- Diễn giải: Laplace ngược không chỉ là thao tác kỹ thuật; nó là bước "giải nén" cấu trúc mode của hệ.

#### Mạch điện và tín hiệu cộng hưởng
- Bài toán: Một phân thức bậc hai xuất hiện trong miền $$ s $$ cần được hiểu lại như dao động hay quá độ trong thời gian.
- Mô hình:
$$
\frac{s}{s^2+\omega^2},\qquad \frac{\omega}{s^2+\omega^2}.
$$
- Giả thiết và giới hạn: Chưa xét các trường hợp cực phức phức tạp hơn ở mức đầu.
- Diễn giải: Tử số quyết định ta đang đọc cos, sin hay tổ hợp tuyến tính của chúng.

### 2. Trực giác bổ sung và các kết nối

Laplace ngược là nơi miền $$ s $$ được dịch trở lại thành câu chuyện thời gian. Vì thế, kỹ năng nhận dạng mẫu và phân tích phân thức đơn là kỹ năng "đọc ngôn ngữ hệ". Bài học này kết nối mạnh với chương dao động ở trước: những mode mũ và dao động mà ta từng đọc từ phương trình đặc trưng nay xuất hiện lại dưới dạng cực của phân thức.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 500)
f1 = np.exp(2 * t)
f2 = np.cos(3 * t)
f3 = np.sin(3 * t)

plt.plot(t, f1, label="L^-1{1/(s-2)} = e^{2t}")
plt.plot(t, f2, label="L^-1{s/(s^2+9)} = cos 3t")
plt.plot(t, f3, label="L^-1{3/(s^2+9)} = sin 3t")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Một số mẫu Laplace ngược cơ bản")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: inverse Laplace transform partial fractions visualization
- search: poles to time response animation
- search: repeated poles exponential response

### 5. Bài toán mẫu có bối cảnh thực

Tính
$$
\mathcal{L}^{-1}\left\{\frac{2s+5}{s^2+4s+13}\right\}.
$$
Hoàn thành bình phương:
$$ s^2+4s+13=(s+2)^2+9. $$
Viết lại tử số:
$$ 2s+5=2(s+2)+1. $$
Vì thế
$$
\frac{2s+5}{(s+2)^2+9}
=2\frac{s+2}{(s+2)^2+9}+\frac{1}{(s+2)^2+9}.
$$
Lấy Laplace ngược:
$$ f(t)=2e^{-2t}\cos 3t+\frac{1}{3}e^{-2t}\sin 3t. $$
Đây là một đáp ứng dao động tắt dần điển hình, rất hữu ích để sinh viên gắn phân thức bậc hai với dao động trong thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phân thức đơn và nhận dạng đúng mẫu từ bảng.

**Bậc sau đại học.** Đi xa hơn sang cực lặp, cực phức, và cách đọc ổn định hay mode từ vị trí pole.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: rất tốt cho việc học Laplace ngược bằng phân thức đơn.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài luyện đúng trọng tâm của bài học này.
- Ross — *Differential Equations*: gọn, sáng rõ, phù hợp để ôn nhanh các mẫu ngược.
