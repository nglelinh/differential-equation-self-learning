---
layout: post
title: "06-05 Phương trình Bessel"
chapter: '06'
order: 5
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

Mỗi khi bạn ném viên sỏi xuống mặt hồ phẳng lặng, gõ vào mặt trống tròn, hay dẫn sóng điện từ qua cáp quang hình trụ, phương trình vật lý tách biến trong tọa độ trụ đều dẫn về đúng một phương trình kinh điển: **Phương trình Bessel** $x^2 y'' + x y' + (x^2 - \nu^2) y = 0$.

## Bản đồ kiến thức nền: Bốn trụ cột của Phương trình & Hàm Bessel

1. **Hàm Bessel loại I ($J_\nu(x)$) & Hàm Bessel loại II ($Y_\nu(x)$)**:
   Tại điểm kỳ dị chính quy $x = 0$, phương trình chỉ số $r^2 - \nu^2 = 0$ cho $r = \pm \nu$. Nghiệm hữu hạn tại gốc $x = 0$ là $J_\nu(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m!\,\Gamma(m+\nu+1)}\left(\frac{x}{2}\right)^{2m+\nu}$, còn $Y_\nu(x)$ chứa $\ln x$ và tiến ra $-\infty$ tại $x = 0$ (nên thường bị loại trong bài toán đĩa tròn đặc!).
2. **Dạng tiệm cận khi $x$ lớn**:
   $J_\nu(x) \approx \sqrt{\frac{2}{\pi x}}\cos\left(x - \frac{\nu\pi}{2} - \frac{\pi}{4}\right)$ — dao động tuần hoàn giống cosin nhưng biên độ suy giảm như $1/\sqrt{x}$ và có vô hạn nghiệm không $j_{\nu, k}$.
3. **Tính trực giao có trọng số $w(x) = x$**:
   Trên $[0, a]$, các hàm $J_\nu(j_{\nu, k} x / a)$ trực giao với trọng số $x$ ($\int_0^a x J_\nu(\alpha_m x) J_\nu(\alpha_n x)\,dx = 0$ khi $m \neq n$), tạo thành **chuỗi Fourier–Bessel**!
4. **Hệ thức truy hồi & Đạo hàm gọn đẹp**:
   $J_0'(x) = -J_1(x)$ và $\frac{d}{dx}[x^\nu J_\nu(x)] = x^\nu J_{\nu-1}(x)$.

## Mục tiêu

Bài học này giới thiệu phương trình Bessel như ví dụ tiêu biểu cho sức mạnh của phương pháp Frobenius và cho cách hình học bài toán quyết định họ nghiệm xuất hiện. Sau bài học, sinh viên cần nhận dạng được phương trình Bessel, hiểu vì sao hàm Bessel loại một được chọn từ điều kiện hữu hạn tại gốc và thấy được mối liên hệ giữa các không điểm của hàm Bessel với trị riêng trong các bài toán đối xứng trụ.

## Kiến thức nền

Sinh viên nên nắm vững phương pháp Frobenius, khái niệm điểm kỳ dị chính quy và trực giác về tách biến trong tọa độ cực hoặc tọa độ trụ. Đây là bài học đầu tiên trong chương khảo sát một họ hàm đặc biệt như nghiệm tự nhiên của một lớp bài toán hình học cụ thể.

## Dẫn nhập

![Phương trình Bessel và các hàm Bessel]({{ site.imgurl }}/chapter_img/chapter06/05_bessel_equation.svg)

Khi giải các bài toán có đối xứng tròn hoặc trụ — chẳng hạn dao động màng trống, truyền nhiệt trong thanh trụ, sóng trong ống dẫn tròn hay thế năng trong miền trụ — phương trình theo phương bán kính gần như luôn dẫn về phương trình Bessel. Điều này cho thấy hàm Bessel không phải một hàm nhân tạo, mà là nghiệm tự nhiên của giải tích trong hình học tròn.

Nếu ở các chương đầu nghiệm quen thuộc là sin, cos và hàm mũ, thì ở đây ta thấy mỗi hình học đặc trưng sẽ sinh ra một họ hàm dao động riêng: với đoạn thẳng là sin và cos, còn với hình tròn và hình trụ là họ hàm Bessel.

### Khung giải thích (nên đọc chậm): Tính tay giá trị $J_0(1)$ và kiểm chứng $J_0'(x) = -J_1(x)$

Với bậc $\nu = 0$, chuỗi của $J_0(x)$ là:
$$J_0(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{(m!)^2} \left(\frac{x}{2}\right)^{2m} = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \dots$$
1. **Tính tay $J_0(1)$ đến 4 chữ số thập phân**:
   $$J_0(1) \approx 1 - 0{,}2500 + 0{,}015625 - 0{,}000434 = \mathbf{0{,}7652}$$
   (giá trị chính xác là $0{,}765197\dots$ — chỉ cần 4 số hạng đã đúng đến chữ số thứ 4!).
2. **Kiểm chứng $J_0'(x) = -J_1(x)$ từng số hạng**:
   $$J_0'(x) = -\frac{x}{2} + \frac{x^3}{16} - \frac{x^5}{384} + \dots = -\left[\frac{x}{2} - \frac{1}{1!\,2!}\left(\frac{x}{2}\right)^3 + \frac{1}{2!\,3!}\left(\frac{x}{2}\right)^5 - \dots\right] = -J_1(x).$$
   Và nghiệm không dương đầu tiên $j_{0,1} \approx 2{,}4048$ chính là tần số cơ bản của màng trống tròn!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Với một sợi dây đàn dao động trên đoạn thẳng, các chế độ riêng (mode) có dạng hàm sin. Khi chuyển sang màng trống hình tròn, sự lan truyền sóng theo các vòng đồng tâm từ tâm ra biên làm thay đổi cấu trúc dao động, và hàm Bessel chính là các chế độ dao động theo hướng kính trong hình học đó.

### Cách nhìn hình ảnh

Đồ thị của $$ J_0(x) $$ dao động tương tự hàm cos nhưng biên độ tắt dần theo $$ x $$ và khoảng cách giữa các không điểm không hoàn toàn đều nhau. Trên màng trống tròn, các đường nút dao động tạo thành những vòng tròn đồng tâm có bán kính xác định bởi các không điểm của hàm Bessel.

### Cách nhìn hình thức

Phương trình Bessel bậc $$ \nu $$ có dạng $$ x^2y''+xy'+(x^2-\nu^2)y=0 $$, với điểm $$ x=0 $$ là điểm kỳ dị chính quy. Áp dụng phương pháp Frobenius, ta thu được hàm Bessel loại một:

$$
J_\nu(x)=
\sum_{m=0}^{\infty}
\frac{(-1)^m}{m!\,\Gamma(m+\nu+1)}
\left(\frac{x}{2}\right)^{2m+\nu}.
$$

Khi $$ \nu $$ không phải số nguyên, hai nghiệm độc lập tuyến tính là $$ J_\nu(x) $$ và $$ J_{-\nu}(x) $$. Khi $$ \nu $$ là số nguyên, $$ J_{-\nu}(x)=(-1)^\nu J_\nu(x) $$ phụ thuộc tuyến tính với $$ J_\nu(x) $$, nên nghiệm độc lập thứ hai được định nghĩa là hàm Bessel loại hai $$ Y_\nu(x) $$.

## Những ngộ nhận thường gặp

- "Hàm Bessel chỉ là một công thức chuỗi cần học thuộc." Sai. Ý nghĩa cốt lõi nằm ở nguồn gốc đối xứng trụ và các tính chất vật lý của nó.
- "Vì đồ thị giống sin–cos nên có thể thay bằng sin–cos." Không đúng; hình học tròn và hình học đoạn thẳng dẫn đến hai họ hàm riêng khác nhau.
- "Chỉ cần biết khai triển chuỗi định nghĩa là đủ." Chưa đủ; cần nắm vai trò của điều kiện hữu hạn tại gốc và ý nghĩa trị riêng của các không điểm.
- "Không điểm của hàm Bessel chỉ là chi tiết phụ về mặt tính toán." Sai. Các không điểm này xác định trực tiếp tần số riêng và các đường nút vật lý của bài toán biên.

## Tiến trình học tập đề xuất

### Bước 1: Nhận dạng phương trình Bessel

Nhận biết dạng chuẩn của phương trình Bessel hoặc các phương trình có thể đổi biến về dạng chuẩn.

### Bước 2: Liên hệ với phương pháp Frobenius

Xác nhận $$ x=0 $$ là điểm kỳ dị chính quy và rút ra phương trình chỉ số $$ r^2-\nu^2=0 $$.

### Bước 3: Chọn nghiệm phù hợp điều kiện vật lý

Trong các miền chứa gốc tọa độ, điều kiện hữu hạn tại gốc loại bỏ nghiệm kỳ dị và giữ lại hàm Bessel loại một $$ J_\nu $$.

### Bước 4: Khai thác các không điểm

Liên hệ các không điểm của $$ J_\nu $$ với điều kiện biên và phổ trị riêng của bài toán.

### Các điểm kiểm tra

- Sinh viên có nhận diện được phương trình Bessel xuất hiện sau phép tách biến hay không.
- Sinh viên có giải thích được vì sao điều kiện hữu hạn tại gốc chọn ra $$ J_\nu $$ hay không.
- Sinh viên có nêu được ý nghĩa vật lý của các không điểm hàm Bessel hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Phương trình Bessel bậc 0

Xét $$ x^2y''+xy'+x^2y=0 $$, tức phương trình Bessel bậc $$ \nu=0 $$. Phương trình chỉ số là $$ r^2=0 $$, cho nghiệm Frobenius hữu hạn tại gốc ứng với $$ r=0 $$. Hệ thức truy hồi dẫn đến

$$
J_0(x)=1-\frac{x^2}{2^2}+\frac{x^4}{2^2 4^2}-\cdots.
$$

Ví dụ này cho thấy chuỗi Frobenius chính là cơ chế trực tiếp định nghĩa hàm Bessel.

### Ví dụ 2: Phương trình Bessel bậc 1

Xét $$ x^2y''+xy'+(x^2-1)y=0 $$ với $$ \nu=1 $$. Nghiệm hữu hạn tại gốc là

$$
J_1(x)=\frac{x}{2}-\frac{x^3}{2^4}+\frac{x^5}{2^7\cdot 3}-\cdots.
$$

Bậc $$ \nu $$ quyết định hành vi dẫn đầu gần gốc tọa độ: với $$ \nu=1 $$, hàm tiệm cận tuyến tính theo $$ x $$ khi $$ x\to 0 $$.

### Ví dụ 3: Bài toán biên trên đĩa tròn

Giả sử phần hướng kính của một chế độ dao động thỏa phương trình $$ r^2R''+rR'+(\lambda^2r^2-m^2)R=0 $$. Nghiệm hữu hạn tại $$ r=0 $$ là $$ R(r)=J_m(\lambda r) $$. Với điều kiện biên cố định tại bán kính $$ r=a $$, ta phải có $$ J_m(\lambda a)=0 $$. Do đó các giá trị riêng cho phép của $$ \lambda $$ được xác định trực tiếp từ các không điểm của $$ J_m $$, kết nối chặt chẽ ODE với bài toán trị riêng.

### Ví dụ 4: Trường hợp bậc nửa nguyên

Với $$ \nu=\frac{1}{2} $$, hàm Bessel có thể biểu diễn tường minh bằng hàm lượng giác:

$$ J_{1/2}(x)=\sqrt{\frac{2}{\pi x}}\sin x. $$

Ví dụ này cho thấy họ hàm lượng giác và họ hàm Bessel có mối liên hệ chặt chẽ trong cùng một khung lý thuyết, tương ứng với các cấu trúc hình học khác nhau.

## Câu hỏi khái niệm

1. Vì sao các bài toán có đối xứng tròn lại dẫn đến hàm Bessel thay vì hàm sin và cos?
2. Trong nhiều bài toán vật lý trên miền chứa gốc tọa độ, vì sao ta chỉ giữ nghiệm hữu hạn tại gốc?
3. Các không điểm của hàm Bessel đóng vai trò gì khi áp đặt điều kiện biên?

## Bài toán ứng dụng

1. Hãy giải thích bằng lời vì sao dao động của màng trống tròn tạo nên các vòng nút đồng tâm và mối liên hệ của chúng với hàm Bessel.
2. Trong bài toán dẫn nhiệt trên thanh trụ dài, vì sao thành phần phụ thuộc bán kính thường thỏa phương trình Bessel?
3. Trong ống dẫn sóng hình tròn hoặc sợi quang, vì sao điều kiện biên trên thành ống lại chọn ra một tập rời rạc các trị riêng?

## Chiến lược giảng dạy tương tác

- Đặt cạnh nhau hình ảnh chế độ dao động của dây đàn và màng trống tròn để thảo luận cách hình học chi phối họ hàm riêng.
- Nhấn mạnh hình ảnh trực quan xem hàm Bessel như "hàm sin–cos của hình học tròn".
- Yêu cầu sinh viên dự đoán nghiệm nào bị loại bỏ dưới điều kiện hữu hạn tại gốc trước khi viết nghiệm tổng quát.
- Thảo luận ý nghĩa hình học của các không điểm nghiệm trong bài toán dao động.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào ba trọng tâm: dạng phương trình chuẩn, lựa chọn nghiệm hữu hạn $$ J_\nu $$ tại gốc và vai trò của các không điểm đối với điều kiện biên, chưa cần ghi nhớ ngay toàn bộ công thức chuỗi tổng quát.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự tách biến phương trình Laplace hoặc phương trình sóng trong tọa độ cực để dẫn ra phương trình Bessel, giúp nắm vững nguồn gốc hình học của phương trình.

## Tóm tắt dễ nhớ

Phương trình Bessel là phương trình đặc trưng của hình học tròn và trụ. Nghiệm hữu hạn tại gốc là hàm Bessel loại một $$ J_\nu $$, và các không điểm của nó xác định trực tiếp các trị riêng và tần số dao động trong bài toán biên.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động màng tròn
- Bài toán: Thành phần hướng kính của màng tròn cố định biên thỏa phương trình Bessel.
- Mô hình:
$$ r^2 R''+rR'+(\lambda r^2-n^2)R=0. $$
- Giả thiết và giới hạn: Màng tròn đồng nhất, biên cố định đều.
- Diễn giải: Các không điểm của $$ J_n $$ lượng tử hóa các tần số dao động riêng.

#### Dẫn nhiệt trong thanh trụ
- Bài toán: Phân bố nhiệt độ theo bán kính trong trụ tròn sau tách biến dẫn tới phương trình
$$ r^2 R''+rR'+\lambda r^2 R=0. $$
- Giả thiết và giới hạn: Vật liệu đồng nhất và đối xứng trụ.
- Diễn giải: Điều kiện hữu hạn tại trục tâm $$ r=0 $$ chọn hàm $$ J_0 $$ và loại bỏ $$ Y_0 $$.

#### Sóng điện từ trong ống dẫn sóng tròn
- Bài toán: Các chế độ truyền sóng TE/TM trong ống dẫn sóng tròn có biên dạng hướng kính là hàm Bessel.
- Mô hình: Cùng cấu trúc phương trình Bessel kết hợp điều kiện biên trên thành ống.
- Giả thiết và giới hạn: Ống dẫn sóng lý tưởng, bỏ qua tổn hao vật liệu.
- Diễn giải: Các không điểm của $$ J_n $$ hoặc $$ J_n' $$ quyết định tần số cắt của từng chế độ truyền sóng.

### 2. Trực giác bổ sung và các kết nối

Hàm Bessel trong hình học tròn đóng vai trò tương tự hàm sin và cos trên đoạn thẳng. Điều kiện chính quy (hữu hạn) tại gốc loại bỏ hàm $$ Y_\nu $$ trong các miền đặc chứa tâm. Thay vì xem $$ J_\nu $$ chỉ như hàm tra bảng, cần nhìn nhận hình dạng đồ thị, dãy không điểm và các hệ thức truy hồi của nó như biểu hiện trực tiếp của các chế độ dao động vật lý.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jn_zeros

x = np.linspace(0, 15, 600)
z = jn_zeros(0, 3)

plt.plot(x, jv(0, x), label="J0(x)")
for root in z:
    plt.axvline(root, color="gray", ls="--", alpha=0.5)
plt.xlabel("x")
plt.ylabel("J0(x)")
plt.title("Zero dau cua ham Bessel J0")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Bessel function zeros drumhead modes
- search: cylindrical heat conduction Bessel equation
- search: waveguide modes Bessel functions

### 5. Bài toán mẫu có bối cảnh thực

Với màng tròn bán kính $$ a $$ ở chế độ hướng kính bậc $$ 0 $$, điều kiện biên cố định là
$$ J_0(\sqrt{\lambda}\,a)=0. $$
Nếu $$ j_{0,1} $$ là không điểm dương đầu tiên của $$ J_0 $$, ta thu được
$$ \sqrt{\lambda}=\frac{j_{0,1}}{a}. $$
Điều này cho thấy tần số cơ bản của màng trống phụ thuộc trực tiếp vào không điểm đầu tiên của hàm Bessel.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện phương trình Bessel, phân biệt $$ J_\nu $$ với $$ Y_\nu $$ và diễn giải ý nghĩa các không điểm.

**Bậc sau đại học.** Khai thác tính trực giao có trọng số, khai triển tiệm cận khi $$ x\to\infty $$ và bài toán Sturm–Liouville dạng Bessel.

## Video tham khảo

- Xem trước: [Advanced Engineering Mathematics, Lecture 2.7: Bessel's equation](https://www.youtube.com/watch?v=lcvWAgrdFn0) — Professor Macauley, tiếng Anh. Bài giảng chi tiết về phương trình Bessel.
- [Bessel Functions and the Frobenius Method](https://www.youtube.com/watch?v=uLORiAWe63A) — Faculty of Khan, tiếng Anh. Xây dựng hàm Bessel bằng phương pháp Frobenius.
- [Bessel's Equation - Ordinary Differential Equations | Lecture 29](https://www.youtube.com/watch?v=HoV5MiyYO3M) — Jason Bramburger, tiếng Anh. Bài giảng chuyên sâu về phương trình Bessel.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: dẫn nhập phương trình Bessel từ phương pháp Frobenius.
- Haberman, *Applied PDEs*: phân tích rõ vai trò của hàm Bessel trong bài toán đối xứng trụ và tách biến.
