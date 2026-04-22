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

## Mục tiêu

Bài học này giúp sinh viên hiểu phương pháp Euler như bước khởi đầu của toàn bộ giải tích số cho ODE. Sau bài học, sinh viên cần thiết lập được công thức Euler tiến và Euler lùi, giải thích được vì sao Euler là “đi theo tiếp tuyến”, phân biệt sai số cục bộ với sai số toàn cục, và nhận ra mối liên hệ giữa bước thời gian với ổn định số.

## Kiến thức nền

Sinh viên nên nắm đạo hàm, khai triển Taylor, bài toán giá trị ban đầu $$ y'=f(t,y),\qquad y(t_0)=y_0 $$, và trực giác rằng nghiệm của ODE là một đường cong có tiếp tuyến xác định bởi $$ f $$. Các ý này được ôn lại trong Bài 13.00. Cũng nên ôn lại rằng đạo hàm chính là tốc độ thay đổi tức thời.

## Dẫn nhập

Nếu biết vị trí hiện tại của một vật và biết vận tốc của nó ngay lúc này, ta có thể đoán vị trí sau một khoảng thời gian rất ngắn bằng cách đi theo tiếp tuyến. Phương pháp Euler làm đúng điều đó cho nghiệm của ODE. Nó không cố nhìn xa; nó chỉ nói: “trong một bước nhỏ, tiếp tuyến là dự đoán tốt nhất”.

Euler rất đơn giản nhưng lại cực kỳ quan trọng vì mọi phương pháp bậc cao hơn đều là cách sửa, cải tiến, hoặc mở rộng trực giác này. Vì vậy, học Euler không chỉ là học một công thức số, mà là học ngôn ngữ nền của mô phỏng vi phân.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng đang lái xe trong sương mù, chỉ nhìn được rất gần. Bạn biết hướng xe đang đi ngay lúc này, nên trong vài mét tiếp theo, cách an toàn nhất là tiếp tục theo hướng đó. Euler cũng vậy: biết độ dốc hiện tại của nghiệm thì ta bước tới bằng cách giữ nguyên độ dốc ấy trong một đoạn ngắn.

### Cách hình ảnh

Giáo viên nên vẽ đồ thị nghiệm thật và tiếp tuyến tại điểm $$ \left(t_n,y_n\right) $$. Từ tiếp tuyến đó, ta đi một bước ngang dài $$ h $$ để tìm giá trị mới $$ y_{n+1} $$. Nếu bước nhỏ, tiếp tuyến gần đường cong; nếu bước lớn, điểm dự đoán có thể lệch đáng kể.

So sánh thêm Euler tiến và Euler lùi trên cùng hình: Euler tiến dùng độ dốc ở đầu bước, Euler lùi dùng độ dốc ở cuối bước. Hình này giúp sinh viên hiểu ngay vì sao Euler lùi thường ổn định hơn nhưng khó tính hơn.

### Cách hình thức

Với bước thời gian $$ h>0 $$ và $$ t_n=t_0+nh $$:

- Euler tiến:

$$ y_{n+1}=y_n+h f(t_n,y_n). $$

- Euler lùi:

$$ y_{n+1}=y_n+h f(t_{n+1},y_{n+1}). $$

Euler tiến là phương pháp tường minh vì tính thẳng được $$ y_{n+1} $$ từ dữ liệu cũ. Euler lùi là phương pháp ngầm vì $$ y_{n+1} $$ xuất hiện ở hai vế nên thường phải giải một phương trình phụ.

## Ngộ nhận thường gặp

### “Euler luôn cho nghiệm tốt nếu công thức đúng”

Sai. Công thức đúng không đảm bảo kết quả tốt khi bước $$ h $$ quá lớn.

### “Sai số cục bộ nhỏ thì sai số toàn cục cũng nhỏ như nhau”

Không. Sai số tích lũy qua nhiều bước, nên sai số toàn cục thường lớn hơn một bậc.

### “Euler lùi chỉ là phiên bản đổi chỉ số của Euler tiến”

Sai. Việc lấy độ dốc ở cuối bước làm thay đổi sâu sắc tính ổn định.

### “Phương pháp số thất bại là vì mô hình sai”

Không nhất thiết. Nhiều khi mô hình đúng nhưng sơ đồ số không ổn định.

## Tiến trình học

### Bước 1: Từ tiếp tuyến đến công thức

Viết xấp xỉ tuyến tính $$ y(t_n+h)\approx y(t_n)+hy'(t_n) $$, rồi thay $$ y'(t_n)=f(t_n,y(t_n)) $$.

### Bước 2: Hiểu sai số

Dùng Taylor để thấy Euler tiến bỏ qua các hạng từ bậc hai trở lên.

### Bước 3: So sánh Euler tiến và Euler lùi

Nhấn mạnh bài toán $$ y'=\lambda y $$ để nhìn rõ sự khác nhau về ổn định.

### Bước 4: Kết nối với phương pháp bậc cao

Giải thích rằng Runge-Kutta sẽ lấy nhiều độ dốc hơn trong một bước thay vì chỉ một độ dốc.

### Các điểm kiểm tra hiểu bài

- Sinh viên có tự suy ra được Euler từ xấp xỉ tiếp tuyến không?
- Sinh viên có giải thích được tại sao bước nhỏ làm kết quả tốt hơn không?
- Sinh viên có phân biệt được phương pháp tường minh và ngầm không?

## Ví dụ có lời giải

### Ví dụ 1: Một bước Euler cho tăng trưởng mũ

Xét $$ y'=y,\qquad y(0)=1 $$. Với bước $$ h=0.1 $$, Euler tiến cho $$ y_1=y_0+0.1y_0=1.1 $$. Trong khi nghiệm đúng tại $$ t=0.1 $$ là $$ e^{0.1}\approx 1.10517 $$. Sai số nhỏ nhưng đã xuất hiện ngay sau một bước.

### Ví dụ 2: Nhiều bước Euler

Vẫn với bài toán trên, ta có quy luật $$ y_n=(1+h)^n $$. Nếu $$ t_n=nh $$ thì nghiệm đúng là $$ e^{t_n} $$. Do $$ (1+h)^n\approx e^{nh} $$ khi $$ h $$ nhỏ, Euler bắt được xu hướng tăng nhưng không trùng chính xác.

### Ví dụ 3: Ổn định với suy giảm mũ

Xét $$ y'=-2y,\qquad y(0)=1 $$. Euler tiến cho $$ y_{n+1}=(1-2h)y_n $$. Nếu $$ h=0.2 $$ thì hệ số là $$ 0.6 $$, nghiệm số giảm dần hợp lý. Nhưng nếu $$ h=1 $$ thì hệ số là $$ -1 $$, nghiệm số dao động dấu dù nghiệm thật luôn dương. Đây là ví dụ kinh điển cho thấy bước lớn gây méo vật lý.

### Ví dụ 4: Euler lùi trên bài toán cứng đơn giản

Với $$ y'=-10y,\qquad y(0)=1 $$, Euler lùi cho $$ y_{n+1}=y_n-10hy_{n+1} $$, nên

$$ y_{n+1}=\frac{1}{1+10h}y_n. $$

Hệ số này luôn dương và nhỏ hơn 1 với mọi $$ h>0 $$, nên Euler lùi ổn định hơn nhiều so với Euler tiến.

## Câu hỏi khái niệm

1. Vì sao Euler có thể được xem là “đi theo tiếp tuyến” chứ không phải “đi theo đường cong”?
2. Tại sao hai phương pháp chỉ khác nhau ở chỗ lấy độ dốc đầu bước hay cuối bước lại cho tính ổn định rất khác nhau?
3. Khi nào việc giảm bước $$ h $$ là cần thiết vì độ chính xác, và khi nào là vì ổn định?

## Bài toán ứng dụng

1. Nếu $$ y(t) $$ là dân số vi khuẩn với tốc độ tăng trưởng tỉ lệ với dân số, Euler mô phỏng quá trình này thế nào?
2. Trong mô hình làm mát, tại sao bước thời gian quá lớn có thể tạo ra nhiệt độ âm phi thực tế?
3. Trong mô phỏng quỹ đạo vệ tinh, việc chỉ dùng tiếp tuyến trong mỗi bước sẽ gây loại sai số nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu chỉ được biết độ dốc tại đúng một thời điểm, em sẽ dự đoán điểm tiếp theo ra sao?
- Khi nào một bước số “quá dài” so với hình học của nghiệm?
- Em mong đợi Euler thất bại trước về độ chính xác hay về ổn định?

### Hoạt động gợi ý

- Cho sinh viên vẽ thủ công 3 bước Euler trên cùng đồ thị nghiệm thật.
- Dùng bảng tính để thay đổi $$ h $$ và quan sát sai số.
- Chia lớp thành hai nhóm: một nhóm bảo vệ Euler tiến, một nhóm bảo vệ Euler lùi trong bài toán suy giảm.

### Cách tăng tham gia

- Bắt đầu từ hình học tiếp tuyến thay vì công thức.
- Cho sinh viên dự đoán kết quả trước khi bấm máy.
- Yêu cầu mô tả sai số bằng lời đời thường trước khi nói bậc chính xác.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Chỉ làm việc với phương trình dạng $$ y'=\lambda y $$ trước.
- Dùng bảng giá trị thay vì ký hiệu trừu tượng ngay từ đầu.
- Nhấn mạnh một thông điệp ngắn: Euler = giá trị cũ + bước x độ dốc hiện tại.

### Thử thách cho sinh viên khá giỏi

- Chứng minh sai số toàn cục của Euler tiến là $$ O(h) $$.
- Phân tích miền ổn định của Euler tiến trên mặt phẳng phức.
- So sánh Euler với xấp xỉ Taylor bậc một của toán tử dòng.

## Ghi nhớ nhanh

Phương pháp Euler là xấp xỉ nghiệm ODE bằng cách đi theo tiếp tuyến trong từng bước ngắn. Nó đơn giản, nền tảng và cho thấy rõ hai bài học lớn của giải tích số: sai số tích lũy theo thời gian và ổn định phụ thuộc mạnh vào kích thước bước.

---

## Ứng dụng thực tế

### 1. Tăng trưởng quần thể và suy giảm phóng xạ

Với mô hình $$ y'=ky $$, Euler tiến cho công thức cập nhật $$ y_{n+1}=(1+kh)y_n $$. Đây là cách rời rạc hóa tự nhiên của tăng trưởng mũ hay suy giảm mũ. Mô hình giả định tốc độ tăng tỉ lệ với trạng thái hiện tại và không có giới hạn tài nguyên. Diễn giải là Euler cho thấy cách một định luật vi phân liên tục biến thành quy tắc lặp thời gian trên máy tính.

### 2. Làm mát Newton

Trong mô hình nhiệt độ $$ T $$ của một vật thể, $$ T'=-k(T-T_{\text{env}}) $$, Euler tiến dự đoán nhiệt độ mới từ độ lệch nhiệt hiện tại. Mô hình giả định môi trường ổn định và hệ số truyền nhiệt không đổi. Nếu bước thời gian quá lớn, nghiệm số có thể dao động hoặc âm phi thực tế dù nhiệt độ thật tiến về cân bằng rất êm. Đây là ví dụ tốt để phân biệt sai mô hình với sai sơ đồ số.

### 3. Mô phỏng vận tốc trong cơ học cơ bản

Với phương trình Newton $$ v'=a(t,v) $$, Euler tiến cập nhật vận tốc bằng công thức “vận tốc mới = vận tốc cũ + gia tốc x thời gian”. Mô hình hợp lý khi gia tốc không đổi nhiều trong một bước ngắn. Giới hạn là ở hệ dao động nhanh hoặc nhạy năng lượng, Euler có thể tích lũy sai số mạnh.

## Trực giác sâu hơn

Euler là bài học đầu tiên về mối căng kéo giữa hình học liên tục và tính toán rời rạc. Nó rất chính xác nếu ta chỉ nhìn từng bước đủ ngắn, nhưng có thể thất bại về lâu dài vì tích lũy sai số hoặc vì mất ổn định. Ngộ nhận thường gặp là nghĩ Euler kém chỉ vì “bậc thấp”; thật ra giá trị lớn nhất của nó là phơi bày rõ mọi khái niệm số học nền tảng.

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

Có thể dùng `Plotly.js` với thanh trượt bước $$ h $$ để sinh viên quan sát cùng một bài toán $$ y'=y $$ hoặc $$ y'=-2y $$ sẽ thay đổi từ xấp xỉ tốt sang dao động sai vật lý như thế nào khi tăng bước.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Euler method slope field animation`, `Newton cooling Euler method`, hoặc `explicit vs implicit Euler stability`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào trực giác tiếp tuyến, sai số cục bộ so với toàn cục, và phân biệt Euler tiến với Euler lùi trên các mô hình tăng/giảm đơn giản.

### Mức sau đại học (Graduate)

Đi sâu vào consistency, zero-stability, phân tích miền ổn định trên mặt phẳng phức, và cách Euler liên hệ với toán tử dòng và semigroup của hệ động lực.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo vệ tinh và cơ học thiên thể
- Bài toán: Khi không có nghiệm đóng thuận tiện, ta cần cập nhật vị trí và vận tốc theo từng bước thời gian.
- Mô hình: Viết hệ
$$ \mathbf{y}' = f(t,\mathbf{y}), $$
rồi dùng Euler tiến
$$
\mathbf{y}_{n+1}=\mathbf{y}_n+h f(t_n,\mathbf{y}_n).
$$
- Giả thiết và giới hạn: Bước thời gian đủ nhỏ; Euler tiến có thể trôi pha và tích lũy sai số năng lượng.
- Diễn giải: Phương pháp biến ODE thành quy tắc cập nhật từng bước trên máy tính.

#### Tăng trưởng dân số hoặc vốn
- Bài toán: Dự báo gần đúng
$$ y'=ky $$
khi chỉ cần ước lượng nhanh theo thời gian rời rạc.
- Mô hình:
$$ y_{n+1}=y_n+hky_n=(1+hk)y_n. $$
- Giả thiết và giới hạn: Hệ số tăng trưởng hằng; bước lớn làm sai số toàn cục tăng nhanh.
- Diễn giải: Euler cho thấy rõ mối liên hệ giữa mô hình liên tục và tăng trưởng theo chu kỳ rời rạc.

### 2. Trực giác bổ sung và các kết nối

Euler tiến đi theo tiếp tuyến tại đầu bước, nên nó là phép xấp xỉ bậc nhất tự nhiên nhất. Điểm quan trọng không chỉ là công thức, mà là tư duy: mỗi lược đồ số chính là một cách thay nghiệm trơn bằng quy tắc cập nhật rời rạc. Một bẫy phổ biến là nghĩ giảm bước luôn giải quyết mọi vấn đề; với hệ cứng, ổn định còn quan trọng hơn cả độ chính xác cục bộ.

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

Với
$$ y'=y, \qquad y(0)=1, $$
và bước $$ h=0.5 $$, Euler tiến cho
$$ y_1=1+0.5(1)=1.5, \qquad y_2=1.5+0.5(1.5)=2.25. $$
Trong khi nghiệm đúng tại $$ t=1 $$ là $$ e \approx 2.718 $$. Sai số này minh họa rõ việc các bước tuyến tính ngắn dần mới bám được tăng trưởng mũ.

### 6. Phân tầng độ khó

**Bậc đại học.** Dựng công thức Euler từ tiếp tuyến và tính sai số bằng ví dụ đơn giản.

**Bậc sau đại học.** Kết nối với consistency, absolute stability và modified equations.
