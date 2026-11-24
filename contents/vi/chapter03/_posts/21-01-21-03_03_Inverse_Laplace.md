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

Giải phương trình đại số trong miền Laplace thường chỉ mất ba mươi giây—thử thách thực sự nằm ở chặng đường quay về miền thời gian: từ một phân thức hữu tỷ $F(s)$ tìm lại hàm gốc $f(t) = \mathcal{L}^{-1}\{F(s)\}$! May mắn thay, **Định lý Lerch** đảm bảo hàm gốc liên tục là duy nhất, còn bộ ba kỹ thuật **tách phân thức hữu tỷ (partial fractions)**, **bình phương đủ** và **quy tắc che Heaviside** sẽ biến mọi phân thức phức tạp thành tổng các mảnh quen thuộc trong bảng.

## Bản đồ kiến thức nền: Bốn kỹ thuật cốt lõi của Biến đổi Laplace Ngược

1. **Tính duy nhất (Định lý Lerch) & Tính tuyến tính**:
   Nếu hai hàm liên tục trên $[0, \infty)$ có cùng biến đổi Laplace thì chúng trùng nhau ở mọi nơi; ta luôn tách $F(s)$ thành tổng các phân thức đơn giản rồi tra ngược từng số hạng.
2. **Tách phân thức hữu tỷ & Phương pháp che (Heaviside Cover-Up)**:
   Với mẫu số có nghiệm đơn $(s - r_1)(s - r_2)\cdots$, hệ số $A_k$ của $\frac{A_k}{s - r_k}$ được tính nhẩm trong 2 giây bằng cách "che" $(s - r_k)$ ở mẫu rồi thay $s = r_k$!
3. **Bình phương đủ cho tam thức bậc hai vô nghiệm thực**:
   Đưa $s^2 + bs + c = (s + \alpha)^2 + \omega^2$, đồng thời viết tử số theo tổ hợp $A(s + \alpha) + B\omega$ để đọc ngay cặp $e^{-\alpha t}\cos(\omega t)$ và $e^{-\alpha t}\sin(\omega t)$.
4. **Xử lý nghiệm bội $(s - r)^k$**:
   Mỗi lũy thừa $\frac{1}{(s - r)^k}$ trả về $\frac{t^{k-1}}{(k-1)!}e^{rt}$—tương ứng chính xác với các số hạng nghiệm bội ta từng gặp ở Chương 02.

## Mục tiêu
Bài học này giúp sinh viên hiểu vai trò của biến đổi Laplace ngược như bước quay về miền thời gian, biết áp dụng phân tích phân thức hữu tỉ thành phân thức đơn và luyện kỹ năng nhận diện mẫu từ bảng biến đổi ngược một cách có hệ thống.

## Kiến thức nền
Sinh viên cần nắm bảng Laplace cơ bản, kỹ thuật phân tích phân thức đơn và các dạng chuẩn
$$
\frac{1}{s-a},\qquad \frac{s}{s^2+b^2},\qquad \frac{b}{s^2+b^2}.
$$
Bài học kết hợp chặt chẽ giữa đại số phân thức hữu tỉ và ý nghĩa động học trong miền thời gian.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-03 Biến đổi Laplace Ngược]({{ site.imgurl }}/chapter_img/chapter03/03_03_inverse_laplace.svg)

Miền Laplace thuận lợi cho việc biến đổi đại số, nhưng các đại lượng vật lý được quan sát trong miền thời gian. Vì vậy, sau khi tìm được nghiệm trong miền $$ s $$, ta cần chuyển ngược về miền $$ t $$ để đọc hành vi thực của hệ. Biến đổi Laplace ngược thực hiện bước chuyển này.

Thay vì dùng trực tiếp công thức tích phân phức Bromwich, khóa học sử dụng phương pháp thực dụng cho các bài toán phổ biến: phân tích phân thức hữu tỉ thành tổng các phân thức đơn rồi tra ngược theo bảng biến đổi cơ bản.

### Khung giải thích (nên đọc chậm): Tìm $\mathcal{L}^{-1}\!\left\{\frac{3s + 5}{(s - 1)(s^2 + 2s + 5)}\right\}$ từng bước rõ ràng

1. **Phân tích mẫu và tách phân thức**:
   Lưu ý $s^2 + 2s + 5 = (s + 1)^2 + 2^2$ (vô nghiệm thực). Đặt:
   $$\frac{3s + 5}{(s - 1)(s^2 + 2s + 5)} = \frac{A}{s - 1} + \frac{Bs + C}{s^2 + 2s + 5}.$$
2. **Dùng mẹo che tìm $A$** (thay $s = 1$ vào phần còn lại):
   $A = \frac{3(1) + 5}{1^2 + 2(1) + 5} = \frac{8}{8} = \mathbf{1}$.
3. **Đồng nhất tử số tìm $B, C$**:
   $3s + 5 = 1\cdot(s^2 + 2s + 5) + (Bs + C)(s - 1) = (1 + B)s^2 + (2 - B + C)s + (5 - C)$.
   Suy ra $1 + B = 0 \implies B = \mathbf{-1}$; và $5 - C = 5 \implies C = \mathbf{0}$.
4. **Bình phương đủ và tra ngược**:
   $$\frac{-s}{(s+1)^2 + 4} = \frac{-(s + 1) + 1}{(s+1)^2 + 2^2} = -\frac{s+1}{(s+1)^2 + 2^2} + \frac{1}{2}\cdot\frac{2}{(s+1)^2 + 2^2}.$$
   Tra bảng thu ngay: $f(t) = \mathbf{e^t - e^{-t}\cos(2t) + \frac{1}{2}e^{-t}\sin(2t)}$!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nếu biến đổi Laplace nén thông tin tín hiệu thời gian thành một biểu thức đại số, thì biến đổi ngược giải nén biểu thức đó. Các cực và hệ số trong phân thức theo $$ s $$ tương ứng trực tiếp với các thành phần hàm mũ, dao động hoặc tăng trưởng trong miền thời gian.

### Cách nhìn hình ảnh
Một phân thức như $$ \frac{1}{s-2} $$ ứng với thành phần hàm mũ $$ e^{2t} $$, còn $$ \frac{s}{s^2+9} $$ ứng với dao động $$ \cos 3t $$. Lấy biến đổi Laplace ngược tương đương với việc đọc ra cấu trúc thời gian ẩn trong dạng phân thức.

### Cách nhìn hình thức
Nếu $$ F(s)=\mathcal{L}\{f(t)\} $$, thì $$ f(t)=\mathcal{L}^{-1}\{F(s)\} $$. Khi $$ F(s) $$ là hàm hữu tỉ thực sự, quy trình chuẩn gồm:

1. Phân tích $$ F(s) $$ thành tổng các phân thức đơn.
2. Đối chiếu từng phân thức với bảng biến đổi ngược.
3. Cộng các thành phần thu được để tạo hàm theo thời gian $$ f(t) $$.

## Những ngộ nhận thường gặp
- "Biến đổi ngược chỉ là tra bảng." Chưa đủ: phần lớn bài toán cần phân tích phân thức đơn hoặc hoàn thành bình phương trước khi tra bảng.
- "Một biểu thức theo $$ s $$ chỉ có một cách tách." Sai: có thể biến đổi theo nhiều cách, miễn là đưa về đúng các dạng chuẩn trong bảng.
- "Mẫu số bậc hai luôn cho hàm sin." Sai: tử số quyết định kết quả là sin, cos hay tổ hợp tuyến tính của cả hai.
- "Tìm được $$ F(s) $$ là đã giải xong bài toán." Sai: ý nghĩa vật lý chỉ đầy đủ sau khi chuyển ngược về miền thời gian.

## Tiến trình học tập đề xuất
### Bước 1: Quan sát cấu trúc của $$ F(s) $$
Nhận diện mẫu bậc nhất, mẫu bậc hai bất khả quy hay tích của nhiều nhân tử.

### Bước 2: Phân tích thành phân thức đơn
Tách biểu thức về tổng các phân thức chuẩn khớp với bảng.

### Bước 3: Áp dụng bảng biến đổi ngược cho từng số hạng
Thực hiện cẩn thận các hệ số tỉ lệ.

### Bước 4: Kiểm tra lại bằng biến đổi xuôi nếu cần
Đây là cách tự kiểm chứng nhanh và tin cậy.

### Các checkpoint
- Sinh viên có chọn đúng dạng khai triển phân thức đơn hay không.
- Sinh viên có biết đặt tử số dạng $$ As+B $$ cho nhân tử bậc hai hay không.
- Sinh viên có diễn giải được hành vi nghiệm sau khi quay về miền thời gian hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mẫu bậc nhất đơn giản
Tính $$ \mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\} $$. Từ công thức $$ \mathcal{L}\{e^{3t}\}=\frac{1}{s-3} $$, suy ra
$$
\mathcal{L}^{-1}\left\{\frac{1}{s-3}\right\}=e^{3t}.
$$

### Ví dụ 2: Phân tích phân thức đơn
Tính $$ \mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\} $$. Ta đặt
$$ \frac{1}{(s-1)(s+2)}=\frac{A}{s-1}+\frac{B}{s+2}, $$
suy ra $$ 1=A(s+2)+B(s-1) $$. Thay $$ s=1 $$ cho $$ 1=3A \Rightarrow A=\frac{1}{3} $$; thay $$ s=-2 $$ cho $$ 1=-3B \Rightarrow B=-\frac{1}{3} $$. Do đó
$$
\frac{1}{(s-1)(s+2)}=\frac{1}{3}\frac{1}{s-1}-\frac{1}{3}\frac{1}{s+2},
$$
và kết quả biến đổi ngược là
$$
\mathcal{L}^{-1}\left\{\frac{1}{(s-1)(s+2)}\right\}=\frac{1}{3}e^t-\frac{1}{3}e^{-2t}.
$$

### Ví dụ 3: Mẫu bậc hai lượng giác
Tính $$ \mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\} $$. Vì $$ \mathcal{L}\{\sin 2t\}=\frac{2}{s^2+4} $$, ta thu được
$$
\mathcal{L}^{-1}\left\{\frac{2}{s^2+4}\right\}=\sin 2t.
$$

### Ví dụ 4: Tử số bậc nhất trên mẫu bậc hai
Tính $$ \mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\} $$. Tách thành hai phân thức:
$$
\frac{s+1}{s^2+9}=\frac{s}{s^2+9}+\frac{1}{s^2+9}.
$$
Áp dụng bảng biến đổi ngược:
$$
\mathcal{L}^{-1}\left\{\frac{s}{s^2+9}\right\}=\cos 3t,\qquad \mathcal{L}^{-1}\left\{\frac{1}{s^2+9}\right\}=\frac{1}{3}\sin 3t.
$$
Vậy
$$
\mathcal{L}^{-1}\left\{\frac{s+1}{s^2+9}\right\}=\cos 3t+\frac{1}{3}\sin 3t.
$$

## Câu hỏi khái niệm
1. Vì sao phân tích phân thức đơn là bước trung gian tự nhiên khi tính biến đổi Laplace ngược?
2. Vì sao mẫu số bậc hai có thể cho ra hàm sin, hàm cos hoặc tổ hợp của cả hai?
3. Một cực đơn tại $$ s=a $$ cho biết gì về hành vi thời gian của nghiệm?

## Bài toán ứng dụng
1. Trong một hệ cơ học, ảnh Laplace có nhiều cực thực âm. Điều đó tương ứng với dạng chuyển động nào trong miền thời gian?
2. Một tín hiệu đầu ra trong miền Laplace có mẫu số $$ s^2+b^2 $$. Điều này nói lên tính chất dao động gì của hệ?
3. Trong kỹ thuật điều khiển, việc xác định vị trí cực của hàm truyền cho biết gì về tính ổn định trước khi biến đổi ngược?

## Chiến lược giảng dạy tương tác
- Tổ chức hoạt động đọc nhanh: nhìn phân thức theo $$ s $$ và dự đoán ngay dạng hàm theo $$ t $$.
- Đánh dấu bằng màu khác nhau từng hạng phân thức đơn và thành phần thời gian tương ứng.
- Chia nhóm thực hành tách phân thức và đối chiếu với bảng biến đổi ngược.
- Khuyến khích sinh viên kiểm tra kết quả bằng cách lấy biến đổi Laplace xuôi.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Cung cấp bảng đối chiếu trực tiếp giữa các dạng phân thức theo $$ s $$ và hàm tương ứng theo $$ t $$ để tránh nhầm lẫn giữa các mẫu gần giống nhau.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên xử lý các phân thức có cực bội hoặc mẫu bậc hai bất khả quy với tử số bậc nhất tổng quát, sau đó diễn giải ý nghĩa động học của từng thành phần.

## Tóm tắt dễ nhớ
Biến đổi Laplace ngược khôi phục hàm thời gian từ biểu thức trong miền $$ s $$. Quy trình gồm ba bước: nhận diện cấu trúc phân thức, tách về tổng các phân thức chuẩn và tra ngược theo bảng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khôi phục đáp ứng thời gian từ miền $$ s $$
- Bài toán: Sau khi giải ODE trong miền Laplace, cần chuyển ngược về hàm thời gian để diễn giải vật lý.
- Mô hình: $$ F(s)\mapsto f(t)=\mathcal{L}^{-1}\{F(s)\} $$.
- Giả thiết và giới hạn: Chủ yếu áp dụng cho các phân thức hữu tỉ ở mức cơ bản.
- Diễn giải: Cực đơn tạo thành phần hàm mũ, mẫu bậc hai tạo sin-cos, cực bội tạo đa thức nhân hàm mũ.

#### Phân tích thành phần nghiệm trong cơ học
- Bài toán: Một biểu thức như $$ \frac{1}{(s+1)(s+3)} $$ biểu diễn hai thành phần suy giảm.
- Mô hình: Phân tích phân thức đơn trước khi biến đổi ngược.
- Giả thiết và giới hạn: Hệ tuyến tính có hệ số hằng.
- Diễn giải: Biến đổi ngược tách rõ từng thành phần suy giảm của hệ.

#### Mạch điện và dao động cộng hưởng
- Bài toán: Phân thức bậc hai trong miền $$ s $$ cần được chuyển về dao động hoặc đáp ứng quá độ trong thời gian.
- Mô hình: $$ \frac{s}{s^2+\omega^2} $$ và $$ \frac{\omega}{s^2+\omega^2} $$.
- Giả thiết và giới hạn: Xét trước trường hợp mẫu bậc hai chuẩn chưa dịch chuyển.
- Diễn giải: Tử số xác định tỉ lệ giữa thành phần cos và sin.

### 2. Trực giác bổ sung và các kết nối

Biến đổi Laplace ngược chuyển kết quả đại số trong miền $$ s $$ trở lại diễn biến theo thời gian. Các thành phần hàm mũ và dao động từng xuất hiện từ phương trình đặc trưng ở Chương 02 nay hiện ra trực tiếp dưới dạng các cực của phân thức.

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

Tính $$ \mathcal{L}^{-1}\left\{\frac{2s+5}{s^2+4s+13}\right\} $$. Hoàn thành bình phương ở mẫu: $$ s^2+4s+13=(s+2)^2+9 $$. Viết lại tử số theo $$ (s+2) $$: $$ 2s+5=2(s+2)+1 $$. Do đó
$$
\frac{2s+5}{(s+2)^2+9}
=2\frac{s+2}{(s+2)^2+9}+\frac{1}{(s+2)^2+9}.
$$
Lấy biến đổi Laplace ngược:
$$ f(t)=2e^{-2t}\cos 3t+\frac{1}{3}e^{-2t}\sin 3t. $$
Kết quả là một dao động tắt dần điển hình, minh họa rõ mối liên hệ giữa mẫu bậc hai có nghiệm phức và dao động tắt dần trong miền thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo phân tích phân thức đơn, hoàn thành bình phương và tra bảng biến đổi ngược.

**Bậc sau đại học.** Mở rộng sang cực bội, cực phức và phân tích tính ổn định từ vị trí cực trên mặt phẳng phức.

## Video tham khảo

- Xem trước: [Partial Fractions and Laplace Inverse | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=D6Rd1K93nSA) — MIT OpenCourseWare, tiếng Anh. Hướng dẫn phân tích phân thức đơn và biến đổi Laplace ngược.
- [Laplace: Solving ODE's | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=5av3kiejazQ) — MIT OpenCourseWare, tiếng Anh. Minh họa việc dùng biến đổi ngược để tìm lại $$ y(t) $$ sau khi giải phương trình đại số.
- [Laplace Transform: Basics | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=BniJM-ireXQ) — MIT OpenCourseWare, tiếng Anh. Ôn lại bảng biến đổi xuôi làm cơ sở cho phép biến đổi ngược.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ kỹ thuật Laplace ngược bằng phân thức đơn.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện đúng trọng tâm.
- Ross — *Differential Equations*: ngắn gọn, phù hợp để ôn nhanh các mẫu biến đổi ngược.
