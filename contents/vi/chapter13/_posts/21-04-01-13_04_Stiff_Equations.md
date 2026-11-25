---
layout: post
title: "Phương Trình Cứng"
chapter: '13'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Trực giác về phương trình cứng và miền ổn định của phương pháp số]({{ site.imgurl }}/chapter_img/chapter13/04_stiff_equations.svg )

Hãy hình dung một phản ứng hóa học có hai quá trình xảy ra đồng thời: một chất trung gian phân hủy sạch trong $10^{-6}$ giây, còn sản phẩm chính biến đổi chậm rãi suốt $10$ giây. Sau vài micro-giây đầu tiên, đường cong nghiệm trông phẳng lì và êm đềm—vậy mà nếu bạn chạy RK4 với bước $h = 0{,}01$ giây, nghiệm số lập tức nổ tung ra `NaN`! Chào mừng đến với thế giới **Phương trình Cứng (Stiff Equations)**—nơi **ổn định**, chứ không phải độ chính xác, mới là kẻ bóp nghẹt bước thời gian của mọi phương pháp hiện!

## Kiến thức cần nhớ: Bốn trụ cột để nhận diện và thuần hóa Phương trình Cứng

1. **Dấu hiệu nhận diện: Tỷ số Độ cứng (Stiffness Ratio) lớn**:
   Một hệ $y' = f(t, y)$ có tính cứng khi ma trận Jacobian $J = \partial f/\partial y$ có các giá trị riêng với phần thực âm chênh lệch nhau nhiều bậc độ lớn ($\max |\operatorname{Re}\lambda_i| \gg \min |\operatorname{Re}\lambda_i|$)—xuất hiện dày đặc trong động học hóa học, mạch điện và PDE khuếch tán sau bán rời rạc hóa!
2. **Nghịch lý của Phương pháp Hiện**:
   Dù thành phần nhanh $e^{-1000t}$ đã tắt hẳn về $0$, mọi phương pháp hiện (Euler hiện, RK4) đều có miền ổn định **hữu hạn**, buộc $h \lesssim 1/|\lambda_{\max}|$ trong suốt toàn bộ quá trình mô phỏng!
3. **Tính Ổn định A (A-stability) và Ổn định L (L-stability)**:
   - *A-ổn định*: miền ổn định chứa trọn nửa mặt phẳng trái $\operatorname{Re}(z) < 0$ (như Euler ẩn, Hình thang/Crank–Nicolson).
   - *L-ổn định*: thêm điều kiện $\lim_{\operatorname{Re}(z)\to -\infty} R(z) = 0$ để dập tắt hẳn các mode siêu nhanh thay vì để chúng dao động $\pm 1$ như quy tắc Hình thang!
4. **Chi phí của Phương pháp Ẩn (BDF, Radau) và Phép lặp Newton**:
   Mỗi bước ẩn đòi hỏi giải hệ phương trình phi tuyến $y_{n+1} - h\beta f(y_{n+1}) = g_n$ bằng Newton–Raphson—tốn hơn mỗi bước, nhưng vì bước $h$ có thể lớn gấp $1000\times$ phương pháp hiện, tổng thời gian tính lại nhanh hơn hàng trăm lần!

## Mục tiêu

Bài học này giúp sinh viên hiểu độ cứng (stiffness) như một thách thức giải tích số chứ không chỉ là đặc điểm hình dạng của nghiệm. Sau bài học, sinh viên cần giải thích được vì sao một bài toán có nghiệm trơn nhưng vẫn khó giải bằng sơ đồ tường minh, biết dùng phương trình kiểm thử $$ y'=\lambda y $$ để phân tích miền ổn định, và hiểu lý do các phương pháp ẩn được ưu tiên cho bài toán cứng.

## Kiến thức nền

Sinh viên cần nắm Euler tiến, Euler lùi, khái niệm miền ổn định cơ bản và hiện tượng mất ổn định số ngay cả khi nghiệm thật suy giảm êm. Bài học này kết nối trực tiếp lý thuyết ổn định với thực hành lựa chọn bộ giải.

## Dẫn nhập

Một tình huống thường gây ngạc nhiên khi mới học phương pháp số là có những ODE mà nghiệm chính xác rất trơn và suy giảm nhanh về trạng thái cân bằng, nhưng máy tính lại buộc phải dùng bước thời gian cực nhỏ để sơ đồ tường minh không bị bùng nổ. Hiện tượng đó gọi là độ cứng (stiffness): kích thước bước bị khống chế bởi điều kiện ổn định thay vì yêu cầu độ chính xác.

Bài toán cứng thường xuất hiện ở các hệ có nhiều thang thời gian chênh lệch nhau lớn: một thành phần suy giảm rất nhanh có thể không còn đáng kể sau thời gian ngắn, nhưng vẫn ép sơ đồ tường minh phải duy trì bước thời gian cực nhỏ trong suốt quá trình tính.


### Giải thích: Đối đầu trực diện Euler Hiện vs. Euler Ẩn trên phương trình cứng $y' = -1000y$

Xét bài toán cứng $y' = -1000y$, $y(0) = 1$ (nghiệm đúng tại $t = 0{,}01$ là $e^{-10} \approx 4{,}5 \times 10^{-5}$). Ta chọn bước thời gian hoàn toàn vừa phải $h = 0{,}01$:
1. **Euler Hiện** ($y_{n+1} = (1 - 1000h) y_n = -9 y_n$):
   $$y_1 = \mathbf{-9}, \qquad y_2 = \mathbf{+81}, \qquad y_3 = \mathbf{-729}, \qquad y_{10} \approx \mathbf{+3{,}49 \times 10^9}!$$
   Nổ tung hoàn toàn vì $h = 0{,}01 > 2/1000 = 0{,}002$!
2. **Euler Ẩn** ($y_{n+1} = y_n - 1000h y_{n+1} \implies y_{n+1} = \frac{y_n}{1 + 1000h} = \frac{y_n}{11}$):
   $$y_1 = \frac{1}{11} \approx \mathbf{0{,}0909}, \qquad y_2 = \frac{1}{121} \approx \mathbf{0{,}00826}, \qquad y_3 \approx \mathbf{0{,}00075} \to 0!$$
   Ổn định tuyệt đối và tắt êm ái về $0$ với mọi $h > 0$—minh chứng sống động cho sức mạnh của tính L-ổn định!
## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng lái xe trên một đoạn đường dài khá bằng phẳng nhưng ngay đầu đoạn có vài gờ rất gắt. Nếu phương tiện quá nhạy với dao động cục bộ, bạn vẫn bị ép chạy chậm suốt quãng đường. Các thành phần suy giảm nhanh trong hệ cứng đóng vai trò tương tự: chúng buộc sơ đồ tường minh phải dùng bước rất nhỏ.

### Cách hình ảnh

Có thể đặt hai hình ảnh cạnh nhau:

- đồ thị nghiệm thật suy giảm nhanh trong giai đoạn đầu rồi biến thiên chậm;
- miền ổn định của Euler tiến trên mặt phẳng phức (hình tròn tâm $$-1$$ bán kính $$1$$).

Khó khăn số học không đến từ hình dáng phức tạp của nghiệm, mà từ việc tích $$ h\lambda $$ dễ rơi ra ngoài miền ổn định nếu $$ h $$ không đủ nhỏ.

### Cách hình thức

Với phương trình kiểm thử chuẩn $$ y'=\lambda y,\qquad \Re(\lambda)<0 $$, Euler tiến cho $$ y_{n+1}=(1+h\lambda)y_n $$. Điều kiện ổn định là $$ \lvert 1+h\lambda\rvert\le 1 $$, buộc $$ h $$ phải rất nhỏ khi $$ \lvert\lambda\rvert $$ lớn. Ngược lại, Euler lùi cho:

$$ y_{n+1}=\frac{1}{1-h\lambda}y_n, $$

ổn định với mọi $$ h>0 $$ bất cứ khi nào $$ \Re(\lambda)<0 $$.

## Ngộ nhận thường gặp

### “Phương trình cứng nghĩa là nghiệm dao động rất nhanh”

Không nhất thiết. Nhiều phương trình cứng có nghiệm rất trơn và suy giảm đơn điệu.

### “Cứ giảm bước $$ h $$ đủ nhỏ là giải quyết xong”

Về lý thuyết thì đúng, nhưng trên thực tế bước $$ h $$ cần thiết có thể nhỏ đến mức thời gian tính toán và sai số làm tròn trở nên không chấp nhận được.

### “Độ cứng chỉ là tính chất riêng của mô hình”

Chưa đầy đủ. Độ cứng là sự tương tác giữa thang thời gian của mô hình với miền ổn định của phương pháp số được chọn.

### “Dùng phương pháp tường minh bậc cao sẽ hết cứng”

Sai. Các phương pháp tường minh bậc cao (như RK4) vẫn có miền ổn định hữu hạn nên vẫn bị ràng buộc bước chặt trên bài toán cứng.

## Tiến trình học

### Bước 1: Phân tích phương trình kiểm thử

Dùng $$ y'=\lambda y $$ để dẫn xuất tường minh điều kiện ổn định.

### Bước 2: Tách bạch yêu cầu độ chính xác và yêu cầu ổn định

Nhấn mạnh rằng trong bài toán cứng, bước nhỏ thường là để tránh bùng nổ chứ không phải để vẽ nghiệm trơn hơn.

### Bước 3: Liên hệ với hệ đa thang thời gian

Chỉ ra cách một thành phần suy giảm nhanh khống chế bước thời gian của toàn hệ.

### Bước 4: Giới thiệu giải pháp ẩn

Trình bày vai trò của phương pháp ẩn, tính A-ổn định (A-stability) và L-ổn định (L-stability).

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được khái niệm độ cứng mà không nhầm với "nghiệm biến thiên nhanh" hay không?
- Sinh viên có suy ra được điều kiện ổn định của Euler tiến trên $$ y'=\lambda y $$ hay không?
- Sinh viên có giải thích được vì sao Euler lùi vượt trội hơn trên bài toán cứng hay không?

## Ví dụ có lời giải

### Ví dụ 1: Phương trình kiểm thử cơ bản

Xét $$ y'=-100y $$. Euler tiến cho $$ y_{n+1}=(1-100h)y_n $$. Điều kiện ổn định $$ \lvert 1-100h\rvert\le 1 $$ đòi hỏi $$ 0\le h\le 0.02 $$, một ràng buộc rất chặt dù nghiệm thật chỉ suy giảm êm về 0.

### Ví dụ 2: Euler lùi trên cùng bài toán

Áp dụng Euler lùi ta có:

$$ y_{n+1}=\frac{1}{1+100h}y_n. $$

Với mọi $$ h>0 $$, hệ số khuếch đại luôn dương và nhỏ hơn 1 — minh họa trực tiếp ưu thế ổn định không điều kiện của lược đồ ẩn.

### Ví dụ 3: Hệ hai thang thời gian

Xét hệ có hai thành phần nghiệm suy giảm như $$ e^{-t} $$ và $$ e^{-1000t} $$. Sau một khoảng thời gian rất ngắn, thành phần $$ e^{-1000t} $$ hầu như bằng 0; tuy nhiên nếu dùng Euler tiến, chính thành phần này vẫn quyết định giới hạn bước thời gian $$ h $$.

### Ví dụ 4: Động học phản ứng hóa học nhanh–chậm

Trong các hệ phản ứng hóa học, một số phản ứng đạt cân bằng gần như tức thời trong khi các phản ứng khác diễn ra chậm hơn nhiều bậc độ lớn. Nếu dùng bộ giải tường minh, tốc độ tính bị ghìm chặt theo phản ứng nhanh nhất dù mục tiêu nghiên cứu là diễn biến chậm. Vì thế các bộ giải chuyên dụng cho hệ cứng đóng vai trò thiết yếu trong hóa học và sinh học tính toán.

## Câu hỏi khái niệm

1. Vì sao độ cứng phụ thuộc đồng thời vào mô hình toán học và phương pháp số sử dụng?
2. Điều gì khiến một bài toán có nghiệm trơn, đơn giản vẫn trở nên khó tính bằng sơ đồ tường minh?
3. Vì sao tính ổn định của phương pháp ẩn lại quan trọng đến vậy đối với bài toán cứng?

## Bài toán ứng dụng

1. Trong động học hóa học có cả phản ứng nhanh và phản ứng chậm, vì sao tính cứng xuất hiện tự nhiên?
2. Trong mạch điện gồm các linh kiện có hằng số thời gian chênh lệch lớn, tính cứng ảnh hưởng đến mô phỏng số như thế nào?
3. Trong dược động học, nếu thuốc hấp thụ rất nhanh nhưng đào thải chậm, bộ giải số cần lưu ý điều gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Một phương trình có nghiệm suy giảm nhanh về 0 có luôn dễ giải bằng máy tính không?
- Khi mô hình liên tục hoàn toàn ổn định nhưng nghiệm số lại bùng nổ, nguyên nhân nằm ở đâu?
- Vì sao một mode tắt gần như tức thời vẫn khống chế bước thời gian của sơ đồ tường minh?

### Hoạt động gợi ý

- Chạy thử Euler tiến với nhiều giá trị $$ h $$ khác nhau trên $$ y'=-100y $$ để quan sát ngưỡng mất ổn định.
- Vẽ so sánh miền ổn định của Euler tiến và Euler lùi trên mặt phẳng phức.
- Thảo luận nhóm các ví dụ hệ đa thang thời gian trong khoa học và kỹ thuật.

### Cách tăng tham gia

- Mở đầu bằng biểu đồ nghiệm số bùng nổ dù nghiệm thật giảm rất êm.
- Mời sinh viên tự tính bước thời gian lớn nhất cho phép trước khi chạy mô phỏng.
- Yêu cầu diễn đạt khái niệm độ cứng bằng lời trước khi dùng trị riêng.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu từ phương trình kiểm thử một chiều $$ y'=\lambda y $$.
- Luyện kỹ phép kiểm tra điều kiện $$ \lvert 1+h\lambda\rvert\le 1 $$.
- Dùng bảng giá trị vài bước đầu để thấy rõ hiện tượng đổi dấu và bùng nổ biên độ.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu sâu khái niệm A-ổn định và L-ổn định.
- Phân tích độ cứng của hệ tuyến tính thông qua tỷ số trị riêng (stiffness ratio).
- So sánh miền ổn định của Euler tiến, RK4 và Euler lùi.

## Ghi nhớ nhanh

Phương trình cứng là bài toán mà kích thước bước của sơ đồ tường minh bị khống chế bởi yêu cầu ổn định thay vì độ chính xác. Thành phần suy giảm nhanh dù không còn đáng kể về lâu dài vẫn buộc ta phải dùng phương pháp ẩn để giữ bước thời gian hợp lý.

---

## Ứng dụng thực tế

### 1. Phản ứng hóa học nhanh–chậm

Hệ ODE mô tả động học hóa học thường có các trị riêng âm rất lớn về độ lớn, khiến Euler tiến hoặc RK tường minh bị ép bước cực nhỏ. Dù phản ánh đúng cấu trúc đa thang thời gian, bài toán đòi hỏi bộ giải ẩn để mô phỏng hiệu quả diễn biến chậm.

### 2. Mạch điện nhiều hằng số thời gian

Trong mạch gồm điện trở, tụ điện và cuộn cảm có thang đáp ứng chênh lệch mạnh, hệ phương trình trạng thái thường cứng. Ngay cả khi điện áp và dòng điện biến thiên êm, sơ đồ tường minh vẫn có thể bùng nổ nếu bước vượt ngưỡng ổn định.

### 3. Dược động học nhiều ngăn

Khi tốc độ hấp thụ vào máu lớn hơn rất nhiều so với tốc độ đào thải khỏi mô, hệ phương trình nhiều ngăn trở nên cứng. Euler lùi hoặc các bộ giải BDF chuyên dụng giúp mô phỏng dài hạn ổn định và tiết kiệm chi phí.

## Trực giác sâu hơn

Độ cứng cho thấy nghiệm mượt không đồng nghĩa với bài toán số dễ. Khi một mode suy giảm rất nhanh ẩn trong hệ, yếu tố quyết định hiệu quả của bộ giải nằm ở độ rộng miền ổn định chứ không chỉ ở bậc chính xác.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

lam = -100.0
h_values = [0.005, 0.02, 0.03]
t_end = 0.2

plt.figure(figsize=(9, 5))
for h in h_values:
    n = int(t_end / h)
    t = np.linspace(0, n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = 1.0
    for k in range(n):
        y[k + 1] = (1 + h * lam) * y[k]
    plt.plot(t, y, 'o-', label=f'Euler tiến, h={h}')

t_exact = np.linspace(0, t_end, 400)
plt.plot(t_exact, np.exp(lam * t_exact), 'k--', label='Nghiệm đúng')
plt.title('Bài toán cứng: bước lớn làm sơ đồ tường minh mất ổn định')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` với thanh trượt điều chỉnh trị riêng $$ \lambda $$ và bước $$ h $$ để quan sát trực tiếp thời điểm $$ 1+h\lambda $$ vượt ra ngoài miền ổn định của Euler tiến.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `stiff ODE visualization`, `A stability region`, hoặc `chemical kinetics stiff solver`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào phương trình kiểm thử $$ y'=\lambda y $$, điều kiện ổn định của Euler tiến và ưu thế của Euler lùi.

### Mức sau đại học (Graduate)

Đi sâu vào A-ổn định, L-ổn định, họ BDF và phân tích độ cứng của hệ ODE qua phổ trị riêng của ma trận Jacobian.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phản ứng hóa học nhanh–chậm
- Bài toán: Một số phản ứng diễn ra cực nhanh trong khi đại lượng quan sát chính thay đổi chậm.
- Mô hình: Trên phương trình kiểm thử $$ y'=\lambda y,\qquad \Re(\lambda)\ll 0 $$, Euler tiến bị ép dùng bước rất nhỏ để giữ ổn định.
- Giả thiết và giới hạn: Hệ có các thang thời gian tách biệt rõ rệt.
- Diễn giải: Độ cứng không phải do sai số cục bộ lớn mà do ràng buộc ổn định ép bước quá nhỏ.

#### Mạch điện có hằng số thời gian chênh lệch lớn
- Bài toán: Hệ phương trình trạng thái chứa đồng thời mode tắt nhanh và mode biến thiên chậm.
- Mô hình: Dùng Euler lùi hoặc họ BDF cho hệ cứng.
- Giả thiết và giới hạn: Mỗi bước cần giải một hệ phương trình ẩn.
- Diễn giải: Phương pháp ẩn tốn chi phí hơn trên từng bước nhưng cho phép dùng bước lớn hơn rất nhiều.

### 2. Trực giác bổ sung và các kết nối

Độ cứng là hiện tượng xuất hiện trong tương tác giữa mô hình và thuật toán số. Nghiệm thật có thể trơn và biến thiên chậm, nhưng mode tắt nhanh ẩn trong hệ vẫn khống chế sơ đồ tường minh; do đó cần kiểm tra phổ trị riêng và miền ổn định thay vì chỉ nhìn hình dạng nghiệm.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

lam = -15.0
h_values = [0.05, 0.15, 0.2]
N = 20

for h in h_values:
    y = np.zeros(N + 1)
    y[0] = 1.0
    for n in range(N):
        y[n + 1] = y[n] + h * lam * y[n]
    plt.plot(range(N + 1), y, "o-", label=f"h={h}")

plt.axhline(0, color="black", linewidth=0.8)
plt.legend()
plt.title("Euler tien tren bai toan cung y' = lambda y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: stiff equation forward backward Euler stability
- search: Dahlquist test equation visualization
- search: chemistry stiff ODE numerical example

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Phương trình cứng: Euler tiến và Euler lùi" description="Quan sát sự khác nhau giữa explicit và implicit trên bài toán test cứng khi thay đổi lambda âm và bước h." path="interactives/chapter13/stiff-equations-vi.html" height="640px" %}

### 5. Bài toán mẫu có bối cảnh thực

Với $$ y'=-15y,\qquad y(0)=1 $$, Euler tiến có hệ số khuếch đại $$ 1+h\lambda = 1-15h $$. Điều kiện ổn định $$ \lvert 1-15h\rvert<1 $$ tương đương $$ 0<h<\frac{2}{15} $$. Dù nghiệm thật giảm êm về $$ 0 $$, bước thời gian vẫn bị giới hạn chặt.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện độ cứng qua phương trình kiểm thử và đối chiếu sơ đồ tường minh với sơ đồ ẩn.

**Bậc sau đại học.** Kết nối với A-ổn định, L-ổn định và lý thuyết nhiễu loạn kỳ dị (singular perturbations).

## Video tham khảo

- xem trước: [Stability of Forward Euler and Backward Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=RdXCGnTT6UY) — Steve Brunton, tiếng Anh. Giải thích vì sao Euler tiến mất ổn định trên bài toán suy giảm cứng trong khi Euler lùi vẫn ổn định.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, tiếng Anh. Dẫn xuất lược đồ ẩn dùng cho bài toán cứng.
- [Numerical Integration of ODEs with Forward Euler and Backward Euler in Python and Matlab](https://www.youtube.com/watch?v=ITFolyl_66U) — Steve Brunton, tiếng Anh. So sánh thực nghiệm giữa Euler tiến và Euler lùi bằng mã nguồn.
