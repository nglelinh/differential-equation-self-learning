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

Xét phương trình Airy $y'' - xy = 0$ (mô tả cầu vồng quang học và hạt lượng tử trong trường lực đều): nhìn tưởng cực kỳ đơn giản nhưng nó **không có nghiệm sơ cấp**! May mắn thay, tại $x_0 = 0$ các hệ số đều giải tích (trơn mượt hoàn hảo), nên $x_0 = 0$ là một **điểm thường (ordinary point)**—và Định lý Fuchs đảm bảo ta luôn tìm được hai nghiệm chuỗi lũy thừa độc lập tuyến tính hội tụ ít nhất tới điểm kỳ dị gần nhất trên mặt phẳng phức!

## Bản đồ kiến thức nền: Bốn bước chuẩn mực giải PTVP gần Điểm Thường

1. **Nhận diện Điểm Thường ($x_0$)**:
   Viết phương trình về dạng chuẩn $y'' + p(x)y' + q(x)y = 0$. Điểm $x_0$ là **điểm thường** nếu cả $p(x)$ và $q(x)$ đều giải tích (khai triển được thành chuỗi Taylor) tại $x_0$.
2. **Định lý Bán kính Hội tụ tối thiểu**:
   Nghiệm chuỗi quanh $x_0$ chắc chắn hội tụ với bán kính $R \ge \text{khoảng cách từ } x_0 \text{ đến điểm kỳ dị phức gần nhất}$ của $p(x)$ hoặc $q(x)$ (ví dụ với $p(x) = \frac{1}{1+x^2}$, điểm kỳ dị là $x = \pm i \implies R \ge \vert 0 - i \vert = 1$!).
3. **Bốn bước cơ học tìm nghiệm**:
   (1) Giả sử $y = \sum_{n=0}^\infty a_n x^n$; (2) Tính $y', y''$ và thế vào PTVP; (3) Dịch chỉ số để gộp về $\sum [\dots] x^k = 0$ và rút hệ thức truy hồi; (4) Tách hai nghiệm cơ sở $y_1(x)$ (chọn $a_0 = 1, a_1 = 0$) và $y_2(x)$ (chọn $a_0 = 0, a_1 = 1$).
4. **Kiểm chứng nghiệm cắt cụt**:
   Luôn kiểm tra 3–4 số hạng đầu bằng cách thế ngược vào PTVP để đảm bảo không sai dấu hay giai thừa.

## Mục tiêu

Bài học này giới thiệu trường hợp thuận lợi nhất của phương pháp nghiệm chuỗi: giải phương trình vi phân tuyến tính quanh một điểm thường. Sau bài học, sinh viên cần nắm điều kiện cho phép sử dụng chuỗi lũy thừa thuần túy, biết thay chuỗi vào phương trình để thiết lập hệ thức truy hồi cho các hệ số và hiểu vì sao tính giải tích của hệ số kéo theo tính giải tích của nghiệm.

## Kiến thức nền

Sinh viên cần thành thạo chuỗi lũy thừa, đổi chỉ số tổng, đạo hàm từng số hạng và khái niệm nghiệm tổng quát của phương trình vi phân tuyến tính cấp hai. Nội dung bài 06-01 là nền tảng trực tiếp cho bài này.

## Dẫn nhập

![Nghiệm chuỗi quanh điểm thường của phương trình vi phân]({{ site.imgurl }}/chapter_img/chapter06/02_series_ordinary_points.svg)

Khi các hệ số của phương trình vi phân có tính giải tích quanh một điểm, nghiệm của phương trình cũng giải tích quanh điểm đó, nghĩa là có thể khai triển thành chuỗi lũy thừa. Khi đó, phương trình vi phân không còn phải giải trực tiếp bằng công thức sơ cấp, mà đóng vai trò như quy tắc sinh ra dãy hệ số của chuỗi thông qua hệ thức truy hồi.

Đây là một bước chuyển tư duy quan trọng: thay vì đoán dạng nghiệm sơ cấp ngay từ đầu, ta giả sử nghiệm có dạng

$$ y=\sum_{n=0}^{\infty}a_n(x-x_0)^n $$

rồi để chính phương trình xác định các hệ số $$ a_n $$. Cách tiếp cận này mở đường cho việc giải nhiều phương trình không có nghiệm sơ cấp.

### Khung giải thích (nên đọc chậm): Giải cầm tay chỉ việc phương trình Airy $y'' - xy = 0$ quanh điểm thường $x_0 = 0$

1. **Thế chuỗi $y = \sum_{n=0}^\infty a_n x^n$**:
   $$\sum_{n=2}^{\infty} n(n-1) a_n x^{n-2} - \sum_{n=0}^{\infty} a_n x^{n+1} = 0.$$
2. **Dịch chỉ số về $x^k$**:
   - Tổng 1 ($k = n - 2$): $\sum_{k=0}^\infty (k+2)(k+1) a_{k+2} x^k = 2a_2 + \sum_{k=1}^\infty (k+2)(k+1) a_{k+2} x^k$.
   - Tổng 2 ($k = n + 1$): $\sum_{k=1}^\infty a_{k-1} x^k$.
3. **Đồng nhất hệ số**:
   - Với $k = 0$: $2a_2 = 0 \implies \mathbf{a_2 = 0}$.
   - Với $k \ge 1$: $(k+2)(k+1) a_{k+2} - a_{k-1} = 0 \implies \mathbf{a_{k+2} = \frac{a_{k-1}}{(k+2)(k+1)}}$ (nhảy bước 3!).
4. **Tính tay 6 hệ số đầu**:
   - Nhánh $a_0$: $a_3 = \frac{a_0}{3 \cdot 2} = \frac{a_0}{6}$; $a_6 = \frac{a_3}{6 \cdot 5} = \frac{a_0}{180}$.
   - Nhánh $a_1$: $a_4 = \frac{a_1}{4 \cdot 3} = \frac{a_1}{12}$; $a_7 = \frac{a_4}{7 \cdot 6} = \frac{a_1}{504}$.
   - Nhánh $a_2 = 0$: kéo theo $a_5 = a_8 = \dots = 0$!
5. **Nghiệm tổng quát**:
   $$y(x) = a_0\left(1 + \frac{x^3}{6} + \frac{x^6}{180} + \dots\right) + a_1\left(x + \frac{x^4}{12} + \frac{x^7}{504} + \dots\right).$$
   Kiểm tra nhanh $y_1'' - xy_1$: $y_1'' = x + \frac{x^4}{6} + \dots = x\left(1 + \frac{x^3}{6} + \dots\right) = x y_1$ — khớp chính xác tuyệt đối!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Có thể hình dung điểm thường như một đoạn mặt đường bằng phẳng: nghiệm không gặp đột biến kỳ dị quanh điểm đó nên có thể được mô tả bằng một chuỗi các số hạng hiệu chỉnh trơn tru. Mỗi hệ số chuỗi đóng góp một mức tinh chỉnh cho đường cong nghiệm.

### Cách nhìn hình ảnh

Trên đồ thị, quanh điểm thường, nghiệm được xấp xỉ ngày càng sát bởi các đa thức tổng riêng bậc tăng dần mà không xuất hiện hành vi kỳ dị như phân kỳ vô hạn hay logarit. Các đa thức cắt cụt bám ổn định quanh điểm khai triển trong suốt miền hội tụ cho đến khi tiến gần điểm mà hệ số phương trình mất tính giải tích.

### Cách nhìn hình thức

Xét phương trình tuyến tính thuần nhất cấp hai $$ y''+p(x)y'+q(x)y=0 $$. Nếu các hàm $$ p(x) $$ và $$ q(x) $$ giải tích tại $$ x_0 $$, điểm $$ x_0 $$ được gọi là **điểm thường** (ordinary point). Khi đó ta tìm nghiệm dưới dạng

$$ y=\sum_{n=0}^{\infty}a_n(x-x_0)^n. $$

Lấy đạo hàm từng số hạng:

$$ y'=\sum_{n=1}^{\infty}n a_n(x-x_0)^{n-1}, $$

$$ y''=\sum_{n=2}^{\infty}n(n-1)a_n(x-x_0)^{n-2}. $$

Thay vào phương trình và đổi chỉ số tổng để mọi tổng đều biểu diễn theo cùng lũy thừa $$ (x-x_0)^n $$, ta thu được một hệ thức truy hồi cho các hệ số $$ a_n $$. Hai hệ số tự do đầu tiên $$ a_0, a_1 $$ đóng vai trò hai hằng số tùy ý của nghiệm tổng quát.

## Những ngộ nhận thường gặp

- "Điểm thường có nghĩa là phương trình có hệ số hằng." Sai. Hệ số hoàn toàn có thể biến thiên, miễn là giải tích quanh điểm đang xét.
- "Nghiệm chuỗi chỉ là nghiệm gần đúng." Không đúng. Trong miền hội tụ, chuỗi biểu diễn chính xác nghiệm của phương trình.
- "Chỉ cần thay chuỗi vào phương trình là xong." Chưa đủ; bước quyết định nằm ở việc đổi chỉ số tổng chính xác để đồng nhất hệ số từng bậc.
- "Mọi phương trình đều giải được bằng chuỗi lũy thừa thông thường." Sai. Tại điểm kỳ dị, ta thường phải chuyển sang phương pháp Frobenius.

## Tiến trình học tập đề xuất

### Bước 1: Kiểm tra điểm thường

Kiểm tra tính giải tích của $$ p(x) $$ và $$ q(x) $$ tại điểm khai triển $$ x_0 $$.

### Bước 2: Đặt dạng nghiệm chuỗi

Viết nghiệm dưới dạng chuỗi lũy thừa quanh $$ x_0 $$.

### Bước 3: Tính đạo hàm và đổi chỉ số tổng

Đạo hàm từng số hạng và dịch chỉ số sao cho mọi tổng có chung số mũ $$ (x-x_0)^n $$.

### Bước 4: Đồng nhất hệ số

Cho tổng hệ số ứng với mỗi bậc bằng 0 để lập hệ thức truy hồi.

### Bước 5: Diễn giải kết quả

Tách nghiệm tổng quát thành tổ hợp tuyến tính của hai nghiệm độc lập ứng với $$ a_0, a_1 $$, đồng thời ước lượng bán kính hội tụ dựa trên vị trí điểm kỳ dị gần nhất.

### Các điểm kiểm tra

- Sinh viên có kiểm tra chính xác một điểm có phải điểm thường hay không.
- Sinh viên có đổi chỉ số tổng đúng để đưa mọi chuỗi về cùng bậc hay không.
- Sinh viên có lập chính xác hệ thức truy hồi hay không.
- Sinh viên có phân biệt được nghiệm tổng quát với một nghiệm riêng ứng với giá trị cụ thể của $$ a_0, a_1 $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khôi phục hàm sin và cos bằng phương pháp chuỗi

Xét phương trình $$ y''+y=0 $$ quanh $$ x_0=0 $$. Đặt

$$ y=\sum_{n=0}^{\infty}a_nx^n. $$

Khi đó

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n. $$

Thay vào phương trình:

$$
\sum_{n=0}^{\infty}\left[(n+2)(n+1)a_{n+2}+a_n\right]x^n=0.
$$

Suy ra hệ thức truy hồi:

$$ a_{n+2}=-\frac{a_n}{(n+2)(n+1)}. $$

Nếu chọn $$ a_0=1,\qquad a_1=0 $$, ta thu được khai triển chuỗi của $$ \cos x $$. Nếu chọn $$ a_0=0,\qquad a_1=1 $$, ta thu được khai triển chuỗi của $$ \sin x $$. Ví dụ này cho thấy hai hệ số đầu độc lập sinh ra hai họ hệ số và hai nghiệm độc lập tuyến tính.

### Ví dụ 2: Phương trình có hệ số biến thiên

Xét phương trình $$ y''+x y=0 $$. Điểm $$ x=0 $$ là điểm thường vì các hệ số đều giải tích. Đặt

$$ y=\sum_{n=0}^{\infty}a_nx^n. $$

Ta có

$$ y''=\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n, $$

và

$$ xy=\sum_{n=1}^{\infty}a_{n-1}x^n. $$

Đồng nhất hệ số bậc 0 cho $$ 2a_2=0 \quad \Longrightarrow \quad a_2=0 $$. Với mọi $$ n\ge 1 $$, ta có $$ (n+2)(n+1)a_{n+2}+a_{n-1}=0 $$, nên

$$ a_{n+2}=-\frac{a_{n-1}}{(n+2)(n+1)}. $$

Hệ thức truy hồi này có bước nhảy bằng 3 chứ không tách chẵn–lẻ đơn giản như ví dụ trước, minh họa khả năng xử lý hệ số biến thiên của phương pháp chuỗi.

### Ví dụ 3: Khai triển quanh điểm khác 0

Xét $$ y''+(x-1)y=0 $$ quanh $$ x_0=1 $$. Đặt

$$ t=x-1,\qquad
y=\sum_{n=0}^{\infty}a_n t^n. $$

Phương trình trở thành $$ y''+t y=0 $$, có quy trình giải giống hệt Ví dụ 2. Ví dụ này nhắc sinh viên rằng tâm khai triển có thể dịch chuyển sang bất kỳ điểm thường nào, không bị giới hạn ở $$ x_0=0 $$.

### Ví dụ 4: Hệ số hữu tỉ giải tích và bán kính hội tụ

Xét $$ (1+x)y''+y=0 $$ quanh $$ x=0 $$. Chia hai vế cho $$ 1+x $$:

$$ y''=-\frac{1}{1+x}y. $$

Do khai triển

$$
\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^n x^n,
\qquad \lvert x\rvert<1,
$$

bán kính hội tụ của nghiệm chuỗi quanh $$ x=0 $$ được đảm bảo ít nhất bằng khoảng cách từ $$ 0 $$ đến điểm kỳ dị $$ x=-1 $$ (tức là $$ R\ge 1 $$). Điều này minh họa trực giác rằng miền hội tụ thường bị chặn bởi điểm mà hệ số phương trình mất tính giải tích.

## Câu hỏi khái niệm

1. Vì sao tính giải tích của các hệ số tại $$ x_0 $$ cho phép kỳ vọng nghiệm cũng có khai triển chuỗi lũy thừa quanh $$ x_0 $$?
2. Tại sao hai hệ số tự do đầu tiên thường đóng vai trò hai hằng số tùy ý của nghiệm tổng quát?
3. Miền hội tụ của nghiệm chuỗi liên hệ như thế nào với vị trí các điểm kỳ dị của hệ số phương trình?

## Bài toán ứng dụng

1. Một hệ dao động có độ cứng biến thiên trơn theo vị trí dẫn đến phương trình dạng $$ y''+p(x)y=0 $$. Vì sao nghiệm chuỗi quanh vị trí cân bằng là lựa chọn tự nhiên?
2. Trong quang học hình học, khi chiết suất thay đổi trơn quanh một điểm, hãy giải thích vì sao khai triển nghiệm cục bộ bằng chuỗi lũy thừa là hợp lý.
3. Trong tính toán số, khi không có nghiệm sơ cấp, vì sao vài số hạng đầu của nghiệm chuỗi vẫn rất hữu ích cho việc ước lượng nghiệm gần điểm ban đầu?

## Chiến lược giảng dạy tương tác

- Cho sinh viên phân biệt đâu là bước thao tác chuẩn hóa và đâu là bước cần hiểu bản chất trong quy trình tìm nghiệm chuỗi.
- Chia lớp giải cùng một phương trình với hai tâm khai triển khác nhau (quanh 0 và quanh 1) rồi đối chiếu kết quả.
- Dành thời gian thực hành kỹ thao tác đổi chỉ số tổng bằng câu hỏi định hướng: ta cần quy mọi tổng về cùng bậc lũy thừa nào?
- Khuyến khích sinh viên diễn giải bằng lời quy luật của hệ thức truy hồi thay vì chỉ biến đổi ký hiệu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên hướng dẫn sinh viên đi theo khung bốn bước cố định: đặt chuỗi, viết hai đạo hàm, đổi chỉ số tổng và đồng nhất hệ số. Khung thao tác rõ ràng giúp tránh nhầm lẫn khi làm việc với nhiều tổng vô hạn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên dự đoán cận dưới bán kính hội tụ của nghiệm chuỗi dựa vào khoảng cách đến điểm kỳ dị phức gần nhất của các hệ số, qua đó kết nối ODE với kiến thức giải tích phức cơ bản.

## Tóm tắt dễ nhớ

Quanh một điểm thường, nghiệm của phương trình vi phân tuyến tính có thể viết dưới dạng chuỗi lũy thừa thuần túy. Quy trình gồm bốn bước: kiểm tra điểm thường, đặt nghiệm chuỗi, đạo hàm kết hợp đổi chỉ số tổng và đồng nhất hệ số để lập hệ thức truy hồi. Phương pháp này chuyển bài toán giải phương trình vi phân thành bài toán đại số tìm dãy hệ số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quang học trong môi trường có chiết suất biến thiên
- Bài toán: Cường độ trường trong môi trường có chiết suất thay đổi trơn thỏa một ODE hệ số biến thiên.
- Mô hình mẫu:
$$ y''+x y=0. $$
- Giả thiết và giới hạn: Hệ số phải giải tích gần điểm xét; mô hình phản ánh hành vi cục bộ quanh một điểm thường.
- Diễn giải: Vì $$ x=0 $$ là điểm thường, nghiệm có thể được xây dựng hoàn chỉnh bằng chuỗi lũy thừa.

#### Dầm đàn hồi có độ cứng biến thiên nhẹ
- Bài toán: Khảo sát hệ đàn hồi hoặc mạch điện có thông số biến thiên trơn theo không gian hoặc thời gian.
- Mô hình mẫu:
$$ y''+(1+x)y=0. $$
- Giả thiết và giới hạn: Chỉ mô tả cục bộ trên miền mà các hệ số là hàm giải tích.
- Diễn giải: Phương pháp chuỗi cho phép xây dựng nghiệm chính xác cục bộ dù không biểu diễn được qua hàm sơ cấp.

### 2. Trực giác bổ sung và các kết nối

Điểm thường là điểm mà các hệ số sau khi đưa phương trình về dạng chuẩn không có bất kỳ tính kỳ dị nào, nên chuỗi Taylor là dạng biểu diễn tự nhiên cho nghiệm. Hai sai sót phổ biến nhất cần tránh là làm lệch chỉ số khi thay chuỗi và quên rằng điều kiện ban đầu quyết định trực tiếp hai hệ số tự do $$ a_0, a_1 $$.

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

Xét phương trình
$$ y''+x y=0,\qquad
y=\sum_{n=0}^{\infty}a_n x^n. $$
Thay vào phương trình:
$$
\sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n+\sum_{n=1}^{\infty}a_{n-1}x^n=0.
$$
Đồng nhất hệ số thu được:
$$
a_2=0,\qquad
(n+2)(n+1)a_{n+2}+a_{n-1}=0\quad (n\ge 1).
$$
Đây là cấu trúc tiêu biểu của phương pháp: ODE được chuyển thành hệ thức truy hồi cho dãy hệ số.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo việc thay chuỗi, đổi chỉ số, đồng nhất hệ số và thiết lập hệ thức truy hồi.

**Bậc sau đại học.** Tìm hiểu định lý tồn tại nghiệm giải tích quanh điểm thường và mối liên hệ giữa bán kính hội tụ với điểm kỳ dị gần nhất trên mặt phẳng phức.

## Video tham khảo

- Xem trước: [How to solve ODEs with infinite series | Intro & Easiest Example: y'=y](https://www.youtube.com/watch?v=xeeM3TT4Zgg) — Dr. Trefor Bazett, tiếng Anh. Tìm nghiệm chuỗi cho phương trình $$ y'=y $$ tại điểm thường làm khuôn mẫu của phương pháp.
- [When can you use Series to solve ODEs? Ordinary vs Singular Points](https://www.youtube.com/watch?v=nCT3P8EsoPw) — Dr. Trefor Bazett, tiếng Anh. Phân biệt điểm thường với điểm kỳ dị và điều kiện áp dụng chuỗi lũy thừa thông thường.
- [Solving Differential Equations with Power Series: A Simple Example](https://www.youtube.com/watch?v=3icbG3geC60) — Steve Brunton, tiếng Anh. Giải một phương trình vi phân đơn giản bằng chuỗi lũy thừa và hệ thức truy hồi.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: phương pháp nghiệm chuỗi tại điểm thường và các hệ thức truy hồi.
- Zill, Chương 6: bổ sung nhiều bài tập thực hành về đổi chỉ số và đồng nhất hệ số.
