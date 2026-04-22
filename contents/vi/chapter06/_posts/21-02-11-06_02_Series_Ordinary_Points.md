---
layout: post
title: "06-02 Nghiệm Chuỗi gần Điểm Thường"
chapter: '06'
order: 2
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

## Mục tiêu

Bài học này giới thiệu trường hợp thuận lợi nhất của phương pháp nghiệm chuỗi: giải phương trình tuyến tính quanh một điểm thường. Sau bài học, sinh viên cần hiểu điều kiện nào cho phép dùng chuỗi lũy thừa thuần túy, biết cách thay chuỗi vào phương trình để thu truy hồi hệ số, và biết diễn giải vì sao tính giải tích của hệ số dẫn tới tính giải tích của nghiệm.

## Kiến thức nền

Sinh viên nên thành thạo chuỗi lũy thừa, đổi chỉ số, đạo hàm từng số hạng và khái niệm nghiệm tổng quát của phương trình vi phân tuyến tính cấp hai. Kiến thức ở bài 06-01 là điều kiện nền trực tiếp.

## Dẫn nhập

![Nghiệm chuỗi quanh điểm thường của phương trình vi phân]({{ site.imgurl }}/chapter_img/chapter06/02_series_ordinary_points.svg)

Khi hệ số của phương trình "ngoan" quanh một điểm, ta hy vọng nghiệm cũng ngoan. Trong ngôn ngữ giải tích, "ngoan" nghĩa là có thể khai triển thành chuỗi lũy thừa. Điều đẹp ở đây là phương trình vi phân không còn là đối tượng phải giải trực tiếp; nó trở thành một cỗ máy sinh ra các hệ số của chuỗi. Ta không đoán nghiệm cuối cùng trước, mà để phép truy hồi dẫn đường.

Đây là một thay đổi tư duy quan trọng. Ở các chương trước, ta thường bắt đầu bằng dạng nghiệm quen thuộc. Bây giờ, ta chỉ cần biết nghiệm đủ trơn và giải tích quanh điểm xét, rồi viết

$$ y=\sum_{n=0}^{\infty}a_n(x-x_0)^n. $$

Chính điều này mở đường cho việc giải những phương trình không có nghiệm sơ cấp dễ nhận ra.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy xem điểm thường như một vùng "mặt đường êm". Khi mặt đường êm, chiếc xe nghiệm không bị xóc đột ngột; chuyển động của nó quanh điểm đó có thể mô tả bằng một chuỗi hiệu chỉnh mượt mà. Các hệ số chuỗi giống như các nút điều chỉnh dần dần tinh chỉnh đường đi.

### Cách nhìn hình ảnh

Trên đồ thị, quanh điểm thường, nghiệm có thể được xấp xỉ bởi các đa thức bậc tăng dần mà không xuất hiện hành vi kỳ dị như nổ vô hạn hay logarit. Nếu vẽ các đa thức cắt ngắn của nghiệm, ta sẽ thấy chúng bám khá ổn định quanh điểm khai triển cho đến khi tiến gần một điểm mà hệ số phương trình mất tính giải tích.

### Cách nhìn hình thức

Xét phương trình tuyến tính thuần nhất cấp hai $$ y''+p(x)y'+q(x)y=0 $$. Nếu các hàm $$ p(x) $$ và $$ q(x) $$ giải tích tại $$ x_0 $$, thì $$ x_0 $$ được gọi là điểm thường. Khi đó ta tìm nghiệm dưới dạng

$$ y=\sum_{n=0}^{\infty}a_n(x-x_0)^n. $$

Suy ra

$$ y'=\sum_{n=1}^{\infty}n a_n(x-x_0)^{n-1}, $$

$$ y''=\sum_{n=2}^{\infty}n(n-1)a_n(x-x_0)^{n-2}. $$

Thế vào phương trình và đổi chỉ số để mọi tổng đều viết theo cùng lũy thừa của $$ (x-x_0)^n $$, ta thu được một quan hệ truy hồi cho các hệ số $$ a_n $$. Hai hệ số đầu tự do thường đóng vai trò như hai hằng số tùy ý của nghiệm tổng quát.

## Những ngộ nhận thường gặp

- "Điểm thường nghĩa là phương trình có hệ số hằng." Sai. Hệ số có thể biến thiên, chỉ cần giải tích quanh điểm xét.
- "Nghiệm chuỗi chỉ là xấp xỉ." Không nhất thiết. Trong miền hội tụ, đó là biểu diễn thật của nghiệm.
- "Chỉ cần thế chuỗi vào là xong." Chưa đủ; phần quan trọng nằm ở việc đổi chỉ số cẩn thận để đồng nhất hệ số.
- "Mọi phương trình đều cho nghiệm chuỗi thuần túy như nhau." Sai. Khi gặp điểm kỳ dị, ta thường phải chuyển sang Frobenius.

## Tiến trình học tập đề xuất

### Bước 1: Kiểm tra điểm thường

Trước hết phải nhìn xem hệ số có giải tích tại điểm đang xét hay không.

### Bước 2: Đặt nghiệm chuỗi

Viết nghiệm dưới dạng chuỗi lũy thừa quanh điểm đó.

### Bước 3: Tính đạo hàm và đổi chỉ số

Đây là khâu kỹ thuật quan trọng nhất của bài.

### Bước 4: Đồng nhất hệ số

Sau khi đưa mọi tổng về cùng lũy thừa, ta so sánh hệ số theo từng bậc.

### Bước 5: Diễn giải kết quả

Hiểu hai hệ số đầu tương ứng với hai nghiệm độc lập tuyến tính, và hiểu miền hội tụ bị chi phối bởi vị trí các điểm kỳ dị gần nhất.

### Các checkpoint

- Sinh viên có kiểm tra được một điểm có phải điểm thường hay không.
- Sinh viên có đổi được chỉ số sao cho mọi tổng cùng bậc.
- Sinh viên có viết đúng truy hồi.
- Sinh viên có phân biệt được nghiệm tổng quát với một nghiệm riêng do chọn cụ thể các hệ số đầu hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Phục hồi lại sin và cos từ phương pháp chuỗi

Xét phương trình $$ y''+y=0 $$ quanh $$ x_0=0 $$. Đặt

$$ y=\sum_{n=0}^{\infty}a_nx^n. $$

Khi đó

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n. $$

Thế vào phương trình:

$$
\sum_{n=0}^{\infty}\left[(n+2)(n+1)a_{n+2}+a_n\right]x^n=0.
$$

Suy ra

$$ a_{n+2}=-\frac{a_n}{(n+2)(n+1)}. $$

Nếu chọn $$ a_0=1,\qquad a_1=0 $$, ta thu được chuỗi của $$ \cos x $$. Nếu chọn $$ a_0=0,\qquad a_1=1 $$, ta thu được chuỗi của $$ \sin x $$. Đây là ví dụ mẫu cho thấy hai dữ kiện đầu độc lập tạo ra hai họ hệ số độc lập.

### Ví dụ 2: Phương trình với hệ số biến thiên

Xét $$ y''+x y=0 $$. Điểm $$ x=0 $$ là điểm thường vì các hệ số đều giải tích. Đặt

$$ y=\sum_{n=0}^{\infty}a_nx^n. $$

Ta có

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n, $$

và

$$ xy=\sum_{n=1}^{\infty}a_{n-1}x^n. $$

Hệ số bậc 0 cho $$ 2a_2=0 \quad \Longrightarrow \quad a_2=0 $$. Với mọi $$ n\ge 1 $$, $$ (n+2)(n+1)a_{n+2}+a_{n-1}=0 $$, nên

$$ a_{n+2}=-\frac{a_{n-1}}{(n+2)(n+1)}. $$

Truy hồi này không tách chẵn lẻ đơn giản như ví dụ trước, nên sinh viên thấy rõ rằng phương pháp chuỗi thực sự thích ứng với hệ số biến thiên.

### Ví dụ 3: Khai triển quanh điểm không phải 0

Xét $$ y''+(x-1)y=0 $$ quanh $$ x_0=1 $$. Đặt

$$ t=x-1,\qquad
y=\sum_{n=0}^{\infty}a_n t^n. $$

Phương trình trở thành $$ y''+t y=0 $$. Quy trình giống hệt ví dụ trước, nhưng bài này rất hữu ích về mặt sư phạm vì nó nhấn mạnh rằng chuỗi lũy thừa không chỉ sống quanh 0. Nhiều sinh viên quen Taylor quanh 0 nên dễ quên điểm khai triển có thể dịch chuyển.

### Ví dụ 4: Truy hồi với hệ số hữu tỉ giải tích

Xét $$ (1+x)y''+y=0 $$ quanh $$ x=0 $$. Viết lại:

$$ y''=-\frac{1}{1+x}y. $$

Vì

$$
\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^n x^n,
\qquad \lvert x\rvert<1,
$$

ta thấy rõ nghiệm chuỗi sẽ có bán kính hội tụ ít nhất bị chặn bởi khoảng cách đến điểm kỳ dị $$ x=-1 $$. Đây là ví dụ tốt để giải thích trực giác về bán kính hội tụ: nó thường dừng lại khi hệ số phương trình không còn giải tích.

## Câu hỏi khái niệm

1. Vì sao tính giải tích của hệ số tại điểm $$ x_0 $$ khiến ta kỳ vọng nghiệm cũng có khai triển chuỗi quanh điểm đó?
2. Tại sao hai hệ số đầu thường đóng vai trò như hai hằng số tùy ý của nghiệm tổng quát?
3. Vì sao miền hội tụ của nghiệm chuỗi lại gắn chặt với vị trí các điểm kỳ dị của hệ số phương trình?

## Bài toán ứng dụng

1. Một mô hình dao động có độ cứng thay đổi chậm theo vị trí, dẫn đến phương trình dạng $$ y''+p(x)y=0 $$. Vì sao nghiệm chuỗi quanh vị trí cân bằng là lựa chọn tự nhiên?
2. Trong mô hình quang học hình học, chiết suất thay đổi trơn quanh một điểm. Hãy giải thích vì sao nghiệm địa phương bằng chuỗi là hợp lý.
3. Trong tính toán số, khi không có nghiệm sơ cấp, vì sao vài số hạng đầu của nghiệm chuỗi vẫn rất hữu ích cho dự đoán gần điểm ban đầu?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự xác định đâu là "bước có thể làm máy móc" và đâu là "bước cần hiểu bản chất" trong quy trình nghiệm chuỗi.
- Yêu cầu lớp giải cùng một bài toán nhưng một nửa khai triển quanh 0, nửa còn lại khai triển quanh 1, rồi so sánh.
- Dừng lại lâu ở thao tác đổi chỉ số; đây là chỗ nên hỏi cả lớp "ta muốn mọi tổng cùng nhìn vào bậc nào?"
- Khuyến khích sinh viên giải thích bằng lời ý nghĩa của truy hồi thay vì chỉ tính toán.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cung cấp một khung bốn dòng cố định: đặt chuỗi, viết hai đạo hàm, đổi chỉ số, đồng nhất hệ số. Việc đi theo khuôn sẽ giúp các em không bị lạc giữa nhiều tổng vô hạn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tìm bán kính hội tụ dự đoán của nghiệm dựa trên vị trí điểm kỳ dị gần nhất của hệ số, thay vì chỉ dừng ở truy hồi. Điều này giúp các em kết nối ODE với trực giác giải tích phức ở mức nhẹ.

## Tóm tắt dễ nhớ

Gần một điểm thường, nghiệm của phương trình tuyến tính có thể tìm dưới dạng chuỗi lũy thừa thuần túy. Quy trình là: kiểm tra điểm thường, đặt nghiệm chuỗi, đạo hàm và đổi chỉ số, rồi đồng nhất hệ số để thu truy hồi. Phương pháp này biến bài toán vi phân thành bài toán đại số trên các hệ số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quang học có chiết suất biến thiên
- Bài toán: Cường độ trường trong môi trường biến thiên trơn thỏa một ODE hệ số biến thiên.
- Mô hình mẫu:
$$ y''+x y=0. $$
- Giả thiết và giới hạn: Hệ số phải giải tích gần điểm xét; mô hình chỉ phản ánh lân cận của một điểm thường.
- Diễn giải: Khi $$ x=0 $$ là điểm thường, nghiệm có thể được dựng hoàn toàn từ chuỗi lũy thừa.

#### Dầm đàn hồi có độ cứng biến thiên nhẹ
- Bài toán: Một dầm hay mạch có hệ số thay đổi theo vị trí/thời gian nhưng vẫn trơn.
- Mô hình mẫu:
$$ y''+(1+x)y=0. $$
- Giả thiết và giới hạn: Chỉ là mô hình địa phương gần nơi hệ số phân tích được.
- Diễn giải: Phương pháp chuỗi cho nghiệm cục bộ ngay cả khi không có hàm sơ cấp tương ứng.

### 2. Trực giác bổ sung và các kết nối

Điểm thường là nơi không có rào cản kỳ dị nào xuất hiện trong ODE sau khi đưa về dạng chuẩn. Vì vậy nghiệm địa phương "ngoan" và chuỗi Taylor là ngôn ngữ tự nhiên. Bẫy phổ biến là lệch chỉ số trong phép thế chuỗi hoặc quên rằng điều kiện đầu quyết định hai hệ số tự do đầu tiên.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def ode(t, z):
    y, yp = z
    return [yp, -t * y]

t = np.linspace(0, 2.0, 400)
sol = solve_ivp(ode, [0, 2.0], [1.0, 0.0], t_eval=t)

series = 1 - t**3 / 6 + t**6 / 180

plt.plot(t, sol.y[0], label="numerical")
plt.plot(t, series, "--", label="series truncation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("So sanh nghiem chuoi va nghiem so gan diem thuong")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: series solution ordinary point differential equation
- search: Airy equation power series visualization
- search: recurrence coefficients ODE series method

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$ y''+x y=0,\qquad
y=\sum_{n=0}^{\infty}a_n x^n. $$
Thế vào phương trình:
$$
\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n+\sum_{n=1}^{\infty}a_{n-1}x^n=0.
$$
Suy ra
$$
a_2=0,\qquad
(n+2)(n+1)a_{n+2}+a_{n-1}=0\quad (n\ge 1).
$$
Đó chính là dạng điển hình: ODE biến thành truy hồi hệ số.

### 6. Phân tầng độ khó

**Bậc đại học.** Luyện thế chuỗi, đồng nhất hệ số, và xây truy hồi.

**Bậc sau đại học.** Nói về định lý tồn tại nghiệm giải tích tại điểm thường và bán kính hội tụ gắn với điểm kỳ dị gần nhất.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: phương pháp nghiệm chuỗi tại điểm thường và các truy hồi hệ số.
- Zill, Chương 6: thêm nhiều bài tập thực hành để luyện cách đồng nhất hệ số.
