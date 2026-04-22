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

## Mục tiêu

Bài học này giúp sinh viên hiểu stiffness như một khó khăn số học chứ không chỉ là một đặc điểm hình dạng của nghiệm. Sau bài học, sinh viên cần giải thích được vì sao bài toán có thể “dễ về mặt nghiệm” nhưng “khó về mặt số”, biết dùng phương trình kiểm tra $$ y'=\lambda y $$ để phân tích ổn định, và hiểu vì sao các phương pháp ngầm thường được ưu tiên cho bài toán cứng.

## Kiến thức nền

Sinh viên nên nắm Euler tiến, Euler lùi, miền ổn định cơ bản, và khái niệm rằng phương pháp số có thể thất bại dù nghiệm thật suy giảm rất đẹp. Đây là bài nối trực tiếp giữa lý thuyết ổn định và thực hành tính toán.

## Dẫn nhập

Một trong những điều gây bối rối nhất cho sinh viên là: có những ODE mà nghiệm thật trông rất hiền, giảm nhanh về cân bằng, nhưng máy tính lại buộc dùng bước cực nhỏ mới không nổ. Tại sao? Câu trả lời là stiffness. Đó là khi phương pháp số bị điều khiển bởi ổn định nhiều hơn là bởi độ chính xác.

Nói ngắn gọn, bài toán cứng thường chứa nhiều thang thời gian rất khác nhau. Một thành phần suy giảm cực nhanh có thể không còn quan trọng về mặt vật lý sau thời gian ngắn, nhưng vẫn ép sơ đồ tường minh đi từng bước tí hon.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng đi xe trên một con đường rất dài nhưng ngay đầu đường có vài ổ gà cực nhỏ và rất gắt. Dù phần lớn con đường khá êm, bạn vẫn phải đi chậm nếu dùng một chiếc xe quá nhạy với ổ gà. Thành phần nhanh của hệ chính là những “ổ gà” đó: chúng ép phương pháp tường minh phải đi chậm.

### Cách hình ảnh

Giáo viên nên vẽ hai đồ thị:

- nghiệm thật giảm nhanh rồi bám sát trạng thái chậm,
- miền ổn định của Euler tiến trên trục thực âm.

Điều sinh viên cần thấy là khó khăn không nằm ở hình dáng nghiệm tổng thể, mà nằm ở vị trí của các trị riêng so với miền ổn định của sơ đồ.

### Cách hình thức

Phương trình kiểm tra chuẩn là $$ y'=\lambda y,\qquad \Re(\lambda)<0 $$. Euler tiến cho $$ y_{n+1}=(1+h\lambda)y_n $$. Muốn ổn định, cần $$ \lvert 1+h\lambda\rvert\le 1 $$. Nếu $$ \lambda $$ âm lớn về trị tuyệt đối, điều kiện trên ép $$ h $$ rất nhỏ. Trong khi đó, Euler lùi cho

$$ y_{n+1}=\frac{1}{1-h\lambda}y_n, $$

và ổn định với mọi $$ h>0 $$ khi $$ \Re(\lambda)<0 $$.

## Ngộ nhận thường gặp

### “Stiff nghĩa là nghiệm dao động rất nhanh”

Không nhất thiết. Nhiều bài toán cứng có nghiệm rất êm và còn suy giảm đơn điệu.

### “Nếu giảm bước đủ nhỏ thì không còn gì để bàn”

Thực tế, bước cần có thể nhỏ đến mức chi phí tính toán trở nên không chấp nhận được.

### “Bài toán cứng là vấn đề của mô hình”

Không hoàn toàn. Stiffness là quan hệ giữa mô hình và phương pháp giải.

### “Phương pháp bậc cao sẽ tự động giải quyết stiffness”

Không. Nhiều phương pháp tường minh bậc cao vẫn bị giới hạn mạnh bởi ổn định.

## Tiến trình học

### Bước 1: Phân tích phương trình kiểm tra

Dùng $$ y'=\lambda y $$ để sinh viên nhìn thấy điều kiện ổn định rõ ràng.

### Bước 2: Tách bạch độ chính xác và ổn định

Nhấn mạnh rằng bước nhỏ đôi khi không phải để mô tả nghiệm đẹp hơn mà chỉ để tránh nổ số.

### Bước 3: Liên hệ với nhiều thang thời gian

Một thành phần nhanh có thể ép toàn bộ sơ đồ chậm lại.

### Bước 4: Đưa ra giải pháp

Các phương pháp ngầm, A-stability, và đôi khi L-stability là câu trả lời tự nhiên.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được stiffness mà không nhầm với “nghiệm thay đổi nhanh” không?
- Sinh viên có suy ra điều kiện ổn định của Euler tiến không?
- Sinh viên có nói được vì sao Euler lùi phù hợp hơn không?

## Ví dụ có lời giải

### Ví dụ 1: Phương trình kiểm tra cơ bản

Xét $$ y'=-100y $$. Euler tiến cho $$ y_{n+1}=(1-100h)y_n $$. Muốn ổn định, cần $$ \lvert 1-100h\rvert\le 1 $$, tức là $$ 0\le h\le 0.02 $$. Điều này rất gắt dù nghiệm thật chỉ suy giảm êm về 0.

### Ví dụ 2: Euler lùi trên cùng bài toán

Euler lùi cho

$$ y_{n+1}=\frac{1}{1+100h}y_n. $$

Với mọi $$ h>0 $$, hệ số đều nhỏ hơn 1 về trị tuyệt đối. Đây là minh họa trực tiếp cho lợi thế ổn định của phương pháp ngầm.

### Ví dụ 3: Hệ hai thang thời gian

Xét hệ có hai nghiệm riêng suy giảm như $$ e^{-t}\quad \text{và}\quad e^{-1000t} $$. Về mặt quan sát dài hạn, thành phần $$ e^{-1000t} $$ gần như biến mất ngay. Nhưng nếu dùng Euler tiến, chính nó lại quyết định kích thước bước. Đây là hình ảnh cốt lõi của stiffness.

### Ví dụ 4: Bài toán cứng thực tế

Trong mô hình phản ứng hóa học nhanh-chậm, một số phản ứng xảy ra gần như tức thì còn số khác diễn ra chậm hơn nhiều. Nếu dùng phương pháp tường minh, mô phỏng sẽ bị thành phần nhanh khống chế dù người dùng chủ yếu quan tâm động học chậm. Đây là lý do solver stiff rất quan trọng trong hóa học và sinh học.

## Câu hỏi khái niệm

1. Vì sao stiffness là khái niệm vừa thuộc về mô hình vừa thuộc về phương pháp?
2. Điều gì khiến một bài toán có nghiệm đơn giản vẫn trở nên khó tính toán?
3. Tại sao ổn định của phương pháp ngầm lại đặc biệt quan trọng trong bài toán cứng?

## Bài toán ứng dụng

1. Trong mô hình phản ứng hóa học có phản ứng nhanh và chậm, vì sao stiffness xuất hiện tự nhiên?
2. Trong mạch điện có linh kiện với hằng số thời gian rất khác nhau, bài toán số bị ảnh hưởng ra sao?
3. Trong dược động học, nếu một chất bị hấp thụ nhanh nhưng đào thải chậm, solver số nên chú ý điều gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Có phải nghiệm giảm nhanh luôn là bài toán dễ?
- Nếu mô hình ổn định nhưng nghiệm số nổ, lỗi nằm ở đâu?
- Vì sao một mode rất nhanh nhưng ít quan trọng vẫn ép toàn bộ sơ đồ?

### Hoạt động gợi ý

- Cho sinh viên thử Euler tiến với nhiều giá trị $$ h $$ trên $$ y'=-100y $$.
- Vẽ miền ổn định của Euler tiến và Euler lùi để so sánh.
- Thảo luận nhóm về các hiện tượng nhiều thang thời gian trong thực tế.

### Cách tăng tham gia

- Bắt đầu bằng ví dụ máy tính “phát nổ” dù nghiệm thật hiền.
- Cho sinh viên dự đoán bước lớn nhất chấp nhận được.
- Khuyến khích giải thích stiffness bằng ngôn ngữ không công thức trước.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Chỉ dùng phương trình thử một chiều.
- Làm thật kỹ điều kiện

$$ \lvert 1+h\lambda\rvert\le 1. $$

- Dùng bảng giá trị để thấy hiện tượng dao động và bùng nổ.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu A-stability và L-stability.
- Phân tích stiffness bằng trị riêng của hệ tuyến tính.
- So sánh miền ổn định của Euler, RK4 và Euler lùi.

## Ghi nhớ nhanh

Phương trình cứng là bài toán mà bước thời gian bị ép nhỏ bởi ổn định hơn là bởi độ chính xác. Thành phần nhanh của hệ có thể không quan trọng về mặt vật lý dài hạn, nhưng lại khống chế mạnh việc lựa chọn phương pháp số.

---

## Ứng dụng thực tế

### 1. Phản ứng hóa học nhanh-chậm

Trong động học hóa học, một số phản ứng xảy ra gần như tức thời còn số khác diễn ra chậm hơn nhiều. Hệ ODE tương ứng thường có trị riêng âm rất lớn về độ lớn, khiến Euler tiến hoặc RK tường minh bị ép bước rất nhỏ. Mô hình phản ánh tốt hiện tượng nhiều thang thời gian, nhưng có thể còn phức tạp hơn do ràng buộc bảo toàn hay phi tuyến mạnh. Diễn giải là: stiffness xuất hiện vì solver phải tôn trọng mode nhanh dù người dùng thường chỉ quan tâm động học chậm.

### 2. Mạch điện với nhiều hằng số thời gian

Trong mạch có điện trở, tụ, và cảm với thang phản ứng rất khác nhau, mô hình trạng thái thường dẫn tới hệ cứng. Dù điện áp hoặc dòng tổng thể thay đổi khá êm, phương pháp tường minh vẫn có thể nổ nếu không chọn bước nhỏ. Đây là ví dụ kỹ thuật điển hình cho việc stiffness là vấn đề của mô hình cộng phương pháp, không phải chỉ của nghiệm thật.

### 3. Dược động học nhiều ngăn

Một chất có thể hấp thụ nhanh vào máu nhưng đào thải chậm khỏi mô. Mô hình nhiều ngăn khi đó có các thang thời gian rất lệch nhau và dễ trở nên cứng. Euler lùi hay các solver stiff chuyên dụng thường phù hợp hơn nếu cần mô phỏng dài hạn.

## Trực giác sâu hơn

Stiffness dạy sinh viên rằng “nghiệm hiền” chưa chắc là “bài toán dễ”. Một mode rất nhanh có thể biến mất gần như ngay lập tức trong nghiệm thật, nhưng phương pháp số vẫn phải đối phó với nó để không mất ổn định. Ngộ nhận phổ biến là chỉ cần tăng bậc phương pháp; thực ra chìa khóa thường nằm ở miền ổn định, không phải chỉ ở bậc chính xác.

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

Có thể dùng `Plotly.js` với thanh trượt trị riêng $$ \lambda $$ và bước $$ h $$ để sinh viên nhìn trực tiếp khi nào điểm $$ 1+h\lambda $$ rời khỏi miền ổn định của Euler tiến.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `stiff ODE visualization`, `A stability region`, hoặc `chemical kinetics stiff solver`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Giữ trọng tâm ở phương trình thử $$ y'=\lambda y $$, điều kiện ổn định của Euler tiến, và trực giác vì sao Euler lùi bền hơn.

### Mức sau đại học (Graduate)

Đi sâu vào A-stability, L-stability, BDF methods, và phân tích stiffness của hệ tuyến tính qua phổ trị riêng hoặc Jacobian.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phản ứng hóa học nhanh-chậm
- Bài toán: Một số biến đổi rất nhanh còn đại lượng quan sát chính lại thay đổi chậm.
- Mô hình: Trên test equation
$$ y'=\lambda y,\qquad \Re(\lambda)\ll 0, $$
Euler tiến đòi hỏi bước rất nhỏ để ổn định.
- Giả thiết và giới hạn: Bài toán có thang thời gian tách biệt rõ.
- Diễn giải: Stiffness không phải là sai số lớn, mà là yêu cầu ổn định làm bước bị bóp nhỏ quá mức.

#### Mạch điện có điện trở và tụ rất khác nhau
- Bài toán: Hệ phương trình trạng thái có mode tắt nhanh và mode chậm cùng tồn tại.
- Mô hình: Dùng Euler lùi hoặc BDF cho hệ tuyến tính cứng.
- Giả thiết và giới hạn: Cần giải hệ implicit ở mỗi bước.
- Diễn giải: Implicit methods tốn hơn mỗi bước nhưng cho phép bước lớn hơn rất nhiều.

### 2. Trực giác bổ sung và các kết nối

Stiffness là hiện tượng số học, không chỉ là hiện tượng vật lý. Nghiệm thật có thể trơn và chậm, nhưng phương pháp explicit vẫn buộc phải dùng bước rất bé do một mode tắt nhanh "ẩn" trong hệ. Bẫy phổ biến là chẩn đoán stiffness chỉ bằng việc nhìn nghiệm; ổn định số mới là dấu hiệu quyết định.

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

Với
$$ y'=-15y,\qquad y(0)=1, $$
Euler tiến cho hệ số khuếch đại
$$ 1+h\lambda = 1-15h. $$
Để ổn định cần
$$ \lvert 1-15h\rvert<1, $$
tức là $$ 0<h<\frac{2}{15} $$. Dù nghiệm thật chỉ tắt mượt về $$ 0 $$, bước số vẫn bị khống chế rất mạnh.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện stiffness qua test equation và so sánh explicit/implicit.

**Bậc sau đại học.** Kết nối với A-stability, L-stability và singular perturbations.
