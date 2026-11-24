---
layout: post
title: "Phương Pháp Euler"
chapter: '13'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Trực giác của phương pháp Euler tiến và Euler lùi]({{ site.imgurl }}/chapter_img/chapter13/01_eulers_method.svg )

Nếu bạn đang lái xe trong sương mù dày đặc và chỉ thấy độ dốc mặt đường ngay dưới bánh xe hiện tại, chiến lược đơn giản nhất là giữ nguyên hướng lái ấy đi thẳng một quãng ngắn $h$, rồi dừng lại đo độ dốc mới và lặp lại. Đó chính là **Phương pháp Euler (1768)**: $y_{n+1} = y_n + h f(t_n, y_n)$—thuật toán giải ODE lâu đời nhất, dễ hiểu nhất, và cũng là phòng thí nghiệm hoàn hảo nhất để tận mắt thấy hiện tượng mất ổn định số!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương pháp Euler

1. **Ý nghĩa Hình học (Đường gấp khúc Tiếp tuyến) & Đại số (Taylor bậc 1)**:
   Từ $y(t_n + h) = y(t_n) + h y'(t_n) + \frac{h^2}{2}y''(\xi)$, bỏ số hạng $O(h^2)$ cho ra bước cập nhật Euler hiện $y_{n+1} = y_n + h f(t_n, y_n)$.
2. **Sai số Cục bộ $O(h^2)$ và Sai số Toàn cục $O(h)$**:
   Euler là phương pháp **bậc 1**: muốn giảm sai số toàn cục đi $10$ lần, ta buộc phải giảm bước $h$ đi $10$ lần và tính toán tốn công gấp $10$ lần.
3. **Miền Ổn định Tuyệt đối $|1 + h\lambda| \le 1$**:
   Áp dụng cho phương trình kiểm thử Dahlquist $y' = \lambda y$ cho $y_n = (1 + h\lambda)^n y_0$. Khi $\lambda < 0$ thực, Euler hiện chỉ ổn định khi $0 < h \le \frac{2}{|\lambda|}$; vượt ngưỡng này, nghiệm số dao động trái dấu và nổ tung!
4. **Euler Ẩn (Backward Euler) — Đánh đổi Giải phương trình lấy Ổn định Tuyệt đối**:
   Dùng độ dốc tại điểm đích $y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})$ cho hệ số khuếch đại $\frac{1}{1 - h\lambda}$, luôn có độ lớn $< 1$ với mọi $h > 0$ khi $\operatorname{Re}(\lambda) < 0$!

## Mục tiêu

Bài học này giới thiệu phương pháp Euler như điểm xuất phát của giải tích số cho ODE. Sau bài học, sinh viên cần thiết lập được công thức Euler tiến và Euler lùi, giải thích được ý nghĩa hình học "đi theo tiếp tuyến", phân biệt sai số cục bộ với sai số toàn cục, và hiểu mối liên hệ giữa kích thước bước thời gian với tính ổn định số.

## Kiến thức nền

Sinh viên cần nắm khái niệm đạo hàm, khai triển Taylor, bài toán giá trị ban đầu $$ y'=f(t,y),\qquad y(t_0)=y_0 $$ và trực giác rằng nghiệm ODE là đường cong có hệ số góc tiếp tuyến cho bởi $$ f $$. Các nội dung này đã được ôn tập trong Bài 13.00.

## Dẫn nhập

Nếu biết vị trí và vận tốc hiện tại của một vật, ta có thể ước lượng vị trí sau một khoảng thời gian rất ngắn bằng cách giữ nguyên vận tốc đó — tức đi dọc theo tiếp tuyến. Phương pháp Euler áp dụng đúng ý tưởng ấy cho nghiệm của ODE trên từng bước nhỏ.

Dù có công thức rất đơn giản, phương pháp Euler giữ vai trò nền tảng vì hầu hết các phương pháp bậc cao hơn đều là sự cải tiến hoặc mở rộng từ trực giác này. Hiểu rõ phương pháp Euler giúp nắm vững ngôn ngữ cơ bản của mô phỏng phương trình vi phân.


### Khung giải thích (nên đọc chậm): Tính tay 2 bước Euler hiện trên $y' = -2y$ để thấy rõ cả hội tụ lẫn nổ tung

Xét bài toán $y' = -2y$, $y(0) = 1$ (nghiệm đúng $y(t) = e^{-2t}$, ngưỡng ổn định $h_{\max} = \frac{2}{|-2|} = 1{,}0$):
1. **Bước nhỏ ổn định $h = 0{,}25 < 1$** (hệ số $1 + h\lambda = 1 - 0{,}5 = 0{,}5$):
   - $y_1 = 1 + 0{,}25(-2)(1) = \mathbf{0{,}50}$ (so với $e^{-0{,}5} \approx 0{,}6065$).
   - $y_2 = 0{,}5 + 0{,}25(-2)(0{,}5) = \mathbf{0{,}25}$ (so với $e^{-1} \approx 0{,}3679$).
   Nghiệm giảm đều đúng xu hướng vật lý.
2. **Bước lớn vượt ngưỡng $h = 1{,}2 > 1$** (hệ số $1 + h\lambda = 1 - 2{,}4 = -1{,}4$):
   - $y_1 = 1 + 1{,}2(-2)(1) = \mathbf{-1{,}40}$ (âm vô lý!).
   - $y_2 = (-1{,}40) \times (-1{,}4) = \mathbf{+1{,}96}$, $y_3 = \mathbf{-2{,}744} \to \pm\infty$!
   Chỉ vì vượt ngưỡng $h = 1{,}0$, nghiệm số đã phản bội hoàn toàn nghiệm thật đang tắt êm ái về $0$!
## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng đang di chuyển trong sương mù với tầm nhìn ngắn: khi biết hướng di chuyển ngay tại vị trí hiện tại, cách ước lượng tự nhiên nhất cho vài bước kế tiếp là đi thẳng theo hướng đó. Phương pháp Euler thực hiện đúng nguyên tắc này bằng cách giữ nguyên độ dốc tại đầu bước trong suốt một khoảng thời gian ngắn $$ h $$.

### Cách hình ảnh

Trên đồ thị, từ điểm $$ \left(t_n,y_n\right) $$ ta kẻ đoạn tiếp tuyến có độ dốc $$ f(t_n,y_n) $$ đi ngang một đoạn $$ h $$ để thu được $$ y_{n+1} $$. Khi $$ h $$ nhỏ, tiếp tuyến bám sát đường cong nghiệm; khi $$ h $$ lớn, sai lệch tăng lên rõ rệt.

Đặt Euler tiến và Euler lùi trên cùng một hình cho thấy khác biệt căn bản: Euler tiến dùng độ dốc ở đầu bước, còn Euler lùi dùng độ dốc ở cuối bước. Sự khác biệt này làm Euler lùi ổn định hơn nhưng đòi hỏi giải phương trình tại mỗi bước.

### Cách hình thức

Với bước thời gian $$ h>0 $$ và các mốc $$ t_n=t_0+nh $$:

- Euler tiến (tường minh):

$$ y_{n+1}=y_n+h f(t_n,y_n). $$

- Euler lùi (ẩn):

$$ y_{n+1}=y_n+h f(t_{n+1},y_{n+1}). $$

Euler tiến tính trực tiếp $$ y_{n+1} $$ từ dữ liệu đã biết, còn Euler lùi có $$ y_{n+1} $$ ở cả hai vế nên thường cần giải một phương trình (tuyến tính hoặc phi tuyến) ở mỗi bước.

## Ngộ nhận thường gặp

### “Euler luôn cho nghiệm tốt miễn là viết đúng công thức”

Sai. Ngay cả khi công thức đúng hoàn toàn, bước $$ h $$ quá lớn vẫn có thể gây sai số lớn hoặc mất ổn định.

### “Sai số cục bộ nhỏ thì sai số toàn cục cũng nhỏ cùng bậc”

Không đúng. Sai số tích lũy qua nhiều bước khiến sai số toàn cục thường lớn hơn sai số cục bộ một bậc của $$ h $$.

### “Euler lùi chỉ là đổi chỉ số so với Euler tiến”

Sai. Việc đánh giá độ dốc ở cuối bước làm thay đổi hoàn toàn miền ổn định của lược đồ.

### “Kết quả số sai nghĩa là mô hình vi phân sai”

Không nhất thiết. Nhiều trường hợp mô hình đúng nhưng lược đồ số hoặc bước thời gian không ổn định.

## Tiến trình học

### Bước 1: Từ xấp xỉ tiếp tuyến đến công thức lặp

Viết xấp xỉ tuyến tính $$ y(t_n+h)\approx y(t_n)+hy'(t_n) $$, rồi thay $$ y'(t_n)=f(t_n,y(t_n)) $$.

### Bước 2: Phân tích sai số bằng khai triển Taylor

Chỉ ra rằng Euler tiến cắt bỏ các số hạng từ bậc hai trở đi, nên có sai số cục bộ bậc $$ O(h^2) $$ và sai số toàn cục bậc $$ O(h) $$.

### Bước 3: Đối chiếu Euler tiến và Euler lùi

Xét bài toán thử $$ y'=\lambda y $$ để thấy rõ sự khác biệt về miền ổn định.

### Bước 4: Mở hướng sang phương pháp bậc cao

Chuẩn bị ý tưởng cho Runge–Kutta: lấy nhiều mẫu độ dốc trong cùng một bước thay vì chỉ dùng một độ dốc.

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự suy ra được công thức Euler từ xấp xỉ tiếp tuyến hay không?
- Sinh viên có giải thích được vì sao giảm bước $$ h $$ cải thiện độ chính xác hay không?
- Sinh viên có phân biệt được phương pháp tường minh và phương pháp ẩn hay không?

## Ví dụ có lời giải

### Ví dụ 1: Một bước Euler cho bài toán tăng trưởng mũ

Xét $$ y'=y,\qquad y(0)=1 $$. Với bước $$ h=0.1 $$, Euler tiến cho $$ y_1=y_0+0.1y_0=1.1 $$, trong khi nghiệm chính xác tại $$ t=0.1 $$ là $$ e^{0.1}\approx 1.10517 $$. Sai số nhỏ đã xuất hiện ngay từ bước đầu tiên.

### Ví dụ 2: Nhiều bước Euler

Tiếp tục bài toán trên, ta có công thức tường minh $$ y_n=(1+h)^n $$ tại $$ t_n=nh $$, so với nghiệm chính xác $$ e^{t_n} $$. Khi $$ h $$ nhỏ, $$ (1+h)^n\approx e^{nh} $$, nên Euler tiến nắm bắt đúng xu hướng tăng nhưng luôn trễ hơn nghiệm thật.

### Ví dụ 3: Ổn định trên bài toán suy giảm mũ

Xét $$ y'=-2y,\qquad y(0)=1 $$. Euler tiến cho $$ y_{n+1}=(1-2h)y_n $$. Với $$ h=0.2 $$, hệ số khuếch đại là $$ 0.6 $$, nghiệm số giảm dần hợp lý. Với $$ h=1 $$, hệ số là $$ -1 $$, nghiệm số đổi dấu qua từng bước dù nghiệm thật luôn dương — minh họa rõ việc bước quá lớn làm biến dạng tính chất vật lý.

### Ví dụ 4: Euler lùi trên bài toán suy giảm nhanh

Với $$ y'=-10y,\qquad y(0)=1 $$, Euler lùi cho $$ y_{n+1}=y_n-10hy_{n+1} $$, suy ra:

$$ y_{n+1}=\frac{1}{1+10h}y_n. $$

Hệ số khuếch đại luôn dương và nhỏ hơn 1 với mọi $$ h>0 $$, cho thấy ưu thế ổn định vượt trội của Euler lùi so với Euler tiến.

## Câu hỏi khái niệm

1. Vì sao có thể mô tả phương pháp Euler là "đi theo tiếp tuyến" thay vì "đi theo đường cong nghiệm"?
2. Tại sao chỉ khác nhau ở vị trí đánh giá độ dốc (đầu bước hay cuối bước) mà Euler tiến và Euler lùi có tính ổn định khác nhau rất xa?
3. Khi nào ta cần giảm bước $$ h $$ vì yêu cầu độ chính xác, và khi nào vì yêu cầu ổn định?

## Bài toán ứng dụng

1. Nếu $$ y(t) $$ là kích thước quần thể vi khuẩn có tốc độ tăng tỷ lệ với dân số, phương pháp Euler mô phỏng quá trình này như thế nào?
2. Trong mô hình làm nguội, vì sao bước thời gian quá lớn có thể sinh ra nhiệt độ âm phi vật lý?
3. Trong mô phỏng quỹ đạo vệ tinh, việc chỉ dùng tiếp tuyến tại đầu mỗi bước sẽ gây ra loại sai số đặc trưng nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu chỉ biết độ dốc tại đúng một thời điểm, cách tự nhiên nhất để dự đoán trạng thái kế tiếp là gì?
- Khi nào một bước thời gian được xem là "quá lớn" so với độ cong của nghiệm?
- Trên bài toán suy giảm nhanh, Euler tiến thường hỏng trước do sai số tích lũy hay do mất ổn định?

### Hoạt động gợi ý

- Cho sinh viên vẽ tay 3 bước Euler trên cùng hệ trục với đồ thị nghiệm chính xác.
- Dùng bảng tính thay đổi bước $$ h $$ và theo dõi tốc độ giảm sai số toàn cục.
- Chia hai nhóm thảo luận ưu và nhược điểm của Euler tiến và Euler lùi trên bài toán suy giảm.

### Cách tăng tham gia

- Bắt đầu từ hình học tiếp tuyến trước khi viết công thức đại số.
- Mời sinh viên dự đoán hành vi nghiệm số trước khi chạy mã minh họa.
- Yêu cầu diễn giải sai số bằng ngôn ngữ trực quan trước khi giới thiệu ký hiệu $$ O(h) $$.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Luyện tập trước với phương trình tuyến tính $$ y'=\lambda y $$.
- Dùng bảng tính từng bước cụ thể trước khi viết công thức truy hồi tổng quát.
- Tóm gọn quy tắc: giá trị mới = giá trị cũ + bước $$ h $$ nhân độ dốc hiện tại.

### Thử thách cho sinh viên khá giỏi

- Chứng minh sai số toàn cục của Euler tiến có bậc $$ O(h) $$.
- Vẽ và phân tích miền ổn định tuyệt đối của Euler tiến trên mặt phẳng phức.
- So sánh phương pháp Euler với xấp xỉ Taylor bậc nhất của ánh xạ dòng.

## Ghi nhớ nhanh

Phương pháp Euler xấp xỉ nghiệm ODE bằng cách bước dọc theo tiếp tuyến trên từng đoạn nhỏ. Lược đồ đơn giản này minh họa đầy đủ hai bài học nền tảng của giải tích số: sai số tích lũy theo số bước và tính ổn định phụ thuộc chặt vào kích thước bước thời gian.

---

## Ứng dụng thực tế

### 1. Tăng trưởng quần thể và phân rã phóng xạ

Với mô hình $$ y'=ky $$, Euler tiến cho quy tắc cập nhật $$ y_{n+1}=(1+kh)y_n $$, là dạng rời rạc hóa trực tiếp của quá trình tăng trưởng hoặc suy giảm theo hàm mũ (với giả thiết hệ số $$ k $$ không đổi và không có giới hạn tài nguyên).

### 2. Định luật làm nguội Newton

Với mô hình $$ T'=-k(T-T_{\text{env}}) $$ (nhiệt độ môi trường và hệ số truyền nhiệt không đổi), Euler tiến cập nhật nhiệt độ theo độ chênh lệch nhiệt hiện tại. Nếu chọn bước $$ h $$ quá lớn, nghiệm số có thể dao động hoặc giảm xuống mức phi thực tế dù nghiệm thật tiến đều về $$ T_{\text{env}} $$ — cho thấy rõ sự khác biệt giữa sai số mô hình và bất ổn của lược đồ số.

### 3. Mô phỏng vận tốc trong cơ học cơ bản

Với phương trình $$ v'=a(t,v) $$, Euler tiến tương ứng với quy tắc cập nhật vận tốc bằng gia tốc nhân khoảng thời gian $$ h $$. Cách làm này hợp lý khi gia tốc biến thiên chậm trong một bước, nhưng với hệ dao động hoặc hệ bảo toàn năng lượng, Euler tiến dễ tích lũy sai số đáng kể.

## Trực giác sâu hơn

Phương pháp Euler thể hiện rõ sự đánh đổi giữa mô tả liên tục và tính toán rời rạc: chính xác trên bước đủ ngắn nhưng dễ tích lũy sai số hoặc mất ổn định khi chạy dài hạn. Giá trị lớn nhất của phương pháp Euler không chỉ nằm ở ứng dụng tính nhanh, mà ở việc phơi bày minh bạch mọi khái niệm cơ bản của giải tích số.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

def euler(f, t0, y0, h, n_steps):
    t = [t0]
    y = [y0]
    for _ in range(n_steps):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

f = lambda t, y: y
for h in [0.5, 0.2, 0.05]:
    n = int(2 / h)
    t, y = euler(f, 0.0, 1.0, h, n)
    plt.plot(t, y, 'o-', label=f'Euler h={h}')

t_exact = np.linspace(0, 2, 400)
plt.plot(t_exact, np.exp(t_exact), 'k--', label='e^t')
plt.title('Sai số Euler giảm khi bước h nhỏ dần')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` kèm thanh trượt điều chỉnh bước $$ h $$ để quan sát trực tiếp cách nghiệm của $$ y'=y $$ hoặc $$ y'=-2y $$ chuyển từ xấp xỉ ổn định sang dao động sai lệch vật lý khi tăng $$ h $$.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Euler method slope field animation`, `Newton cooling Euler method`, hoặc `explicit vs implicit Euler stability`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào trực giác tiếp tuyến, phân biệt sai số cục bộ và sai số toàn cục, cùng sự khác nhau giữa Euler tiến và Euler lùi trên các mô hình tuyến tính đơn giản.

### Mức sau đại học (Graduate)

Đi sâu vào tính nhất quán (consistency), ổn định bậc không (zero-stability), miền ổn định trên mặt phẳng phức và mối liên hệ với ánh xạ dòng cũng như nửa nhóm (semigroup) của hệ động lực.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo vệ tinh và cơ học thiên thể
- Bài toán: Cập nhật vị trí và vận tốc theo từng bước thời gian khi không có nghiệm đóng.
- Mô hình: Viết hệ $$ \mathbf{y}' = f(t,\mathbf{y}) $$ và áp dụng Euler tiến:
$$
\mathbf{y}_{n+1}=\mathbf{y}_n+h f(t_n,\mathbf{y}_n).
$$
- Giả thiết và giới hạn: Đòi hỏi bước thời gian nhỏ; Euler tiến có thể gây trôi pha và sai lệch năng lượng dài hạn.
- Diễn giải: Chuyển phương trình động lực liên tục thành quy tắc cập nhật từng bước trên máy tính.

#### Tăng trưởng dân số hoặc vốn
- Bài toán: Ước lượng nhanh mô hình $$ y'=ky $$ theo các chu kỳ rời rạc.
- Mô hình: $$ y_{n+1}=y_n+hky_n=(1+hk)y_n $$.
- Giả thiết và giới hạn: Hệ số tăng trưởng không đổi; bước $$ h $$ lớn làm sai số toàn cục tăng nhanh.
- Diễn giải: Minh họa trực tiếp mối liên hệ giữa tăng trưởng liên tục và lãi ghép theo chu kỳ rời rạc.

### 2. Trực giác bổ sung và các kết nối

Euler tiến đi theo tiếp tuyến tại đầu bước nên là phép xấp xỉ bậc nhất tự nhiên nhất. Điểm cốt lõi là mỗi lược đồ số thay thế tiến hóa liên tục bằng một quy tắc cập nhật rời rạc; với hệ cứng, yêu cầu ổn định còn khắt khe hơn yêu cầu độ chính xác cục bộ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

f = lambda t, y: y
t0, y0, h = 0.0, 1.0, 0.25
N = 12
t = np.linspace(t0, t0 + N * h, N + 1)
y = np.zeros(N + 1)
y[0] = y0

for n in range(N):
    y[n + 1] = y[n] + h * f(t[n], y[n])

tt = np.linspace(t0, t[-1], 400)
plt.plot(tt, np.exp(tt), label="nghiem dung")
plt.plot(t, y, "o-", label="Euler tien")
plt.legend()
plt.title("Euler tien cho y' = y")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Euler method slope field animation
- search: forward vs backward Euler stability visualization
- search: tangent line numerical ODE intuition

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Euler tiến: so sánh với nghiệm đúng" description="Điều chỉnh lambda, bước h và giá trị đầu để quan sát trực tiếp ảnh hưởng của sai số toàn cục trong Euler tiến." path="interactives/chapter13/euler-method-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Với $$ y'=y, \qquad y(0)=1 $$ và bước $$ h=0.5 $$, Euler tiến cho:
$$ y_1=1+0.5(1)=1.5, \qquad y_2=1.5+0.5(1.5)=2.25. $$
So với nghiệm đúng tại $$ t=1 $$ là $$ e \approx 2.718 $$, sai số này cho thấy cần các bước tuyến tính đủ nhỏ mới bám sát được đường cong mũ.

### 6. Phân tầng độ khó

**Bậc đại học.** Xây dựng công thức Euler từ tiếp tuyến và đánh giá sai số qua các ví dụ tường minh.

**Bậc sau đại học.** Kết nối với tính nhất quán, ổn định tuyệt đối và lý thuyết phương trình hiệu chỉnh (modified equations).

## Video tham khảo

- xem trước: [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, tiếng Anh. Dẫn xuất chi tiết lược đồ Euler tiến và Euler ẩn.
- [Numerical Integration of ODEs with Forward Euler and Backward Euler in Python and Matlab](https://www.youtube.com/watch?v=ITFolyl_66U) — Steve Brunton, tiếng Anh. Cài đặt và so sánh hai lược đồ Euler trong Python và MATLAB.
- [Euler's Method | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=X5-ucBtneVM) — MIT OpenCourseWare, tiếng Anh. Trình bày ngắn gọn về phương pháp Euler cho bài toán y'=f(x,y).
