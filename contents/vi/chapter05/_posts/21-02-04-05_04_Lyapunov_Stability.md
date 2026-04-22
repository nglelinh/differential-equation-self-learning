---
layout: post
title: "05-04 Ổn định Lyapunov"
chapter: '05'
order: 4
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên hiểu phương pháp Lyapunov như cách chứng minh ổn định mà không cần giải nghiệm tường minh, biết thế nào là một hàm Lyapunov tốt, và thấy vai trò của tư duy năng lượng trong phân tích hệ phi tuyến.

## Kiến thức nền

Sinh viên cần nắm điểm cân bằng, đạo hàm theo quỹ đạo và trực giác ổn định. Một ít quen thuộc với năng lượng trong cơ học sẽ giúp bài học trở nên tự nhiên hơn.

## Dẫn nhập

![Hàm Lyapunov như năng lượng suy giảm]({{ site.imgurl }}/chapter_img/chapter05/04_lyapunov_stability.svg)

Có rất nhiều hệ phi tuyến quan trọng mà ta không thể giải explicit. Nếu cứ đòi hỏi công thức nghiệm rồi mới nói về ổn định, ta sẽ bó tay với phần lớn mô hình thực tế. Phương pháp Lyapunov mở ra một con đường khác: thay vì theo dõi quỹ đạo trực tiếp, ta tìm một đại lượng vô hướng đóng vai trò như năng lượng, rồi quan sát xem nó tăng, giảm hay giữ nguyên dọc theo chuyển động.

Đây là một trong những ý tưởng đẹp nhất của động lực học. Thay vì giải bài toán chuyển động, ta giải bài toán tìm một "thước đo độ xa khỏi cân bằng" mà hệ không thể làm tăng lên. Nếu thước đo ấy giảm nghiêm ngặt, ta còn biết hệ bị kéo về cân bằng. Ý tưởng vừa hình học, vừa vật lý, vừa rất thực dụng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng $$ V(x,y) $$ là độ cao của một bề mặt năng lượng. Nếu quỹ đạo của hệ luôn đi xuống hoặc đi ngang trên bề mặt đó, hệ khó có thể tự nhiên chạy ra vùng cao hơn. Nếu nó luôn đi xuống, hệ bị hút về đáy.

### Cách nhìn hình ảnh

Các đường mức của $$ V $$ giống như những vòng rào bao quanh cân bằng. Nếu dọc theo quỹ đạo, hệ luôn đi vào phía trong các đường mức, ta có một bức tranh rất rõ về ổn định. Đây là cách Lyapunov biến một vấn đề quỹ đạo thành một vấn đề hình học của họ mức.

### Cách nhìn hình thức

Một hàm $$ V(x,y) $$ thường được dùng làm hàm Lyapunov quanh cân bằng gốc nếu
$$ V(0,0)=0, $$
và
$$ V(x,y)>0 \quad \text{khi } (x,y)\neq (0,0) $$
trong một lân cận. Đạo hàm theo quỹ đạo là
$$ \dot{V}=V_x f(x,y)+V_y g(x,y). $$
Nếu
$$ \dot{V}\le 0, $$
ta có thông tin mạnh về ổn định. Nếu
$$ \dot{V}<0 $$
nghiêm ngặt ngoài cân bằng, thường ta có ổn định tiệm cận.

## Những ngộ nhận thường gặp

- "Muốn chứng minh ổn định phải biết nghiệm." Sai. Đây chính là điều Lyapunov giúp ta tránh.
- "Bất kỳ hàm dương nào cũng là hàm Lyapunov tốt." Sai. Điều quyết định là đạo hàm dọc theo quỹ đạo.
- "Nếu $$ \dot{V}=0 $$ thì chắc chắn không kết luận được gì." Không hẳn; đôi khi còn cần thêm ý tưởng LaSalle, nhưng trong bài cơ bản ta thường cẩn thận hơn.
- "Lyapunov chỉ là kỹ thuật cơ học." Sai. Nó áp dụng rộng trong điều khiển, sinh học, mạch điện và nhiều hệ phi tuyến khác.

## Tiến trình học tập đề xuất

### Bước 1: Chọn ứng viên $$ V $$

Thường bắt đầu từ dạng giống năng lượng như $$ x^2+y^2 $$.

### Bước 2: Kiểm tra tính dương xác định

Không có bước này thì $$ V $$ không đo đúng "độ xa".

### Bước 3: Tính $$ \dot{V} $$ theo quỹ đạo

Đây là bước quyết định.

### Bước 4: Kết luận ổn định hay tiệm cận

Phải nói rõ loại kết luận nào thực sự thu được.

### Các checkpoint

- Sinh viên có phân biệt được $$ V>0 $$ với $$ \dot{V}<0 $$ không.
- Sinh viên có tính đúng đạo hàm theo quỹ đạo hay không.
- Sinh viên có kết luận quá mạnh từ giả thiết chưa đủ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ tuyến tính có tắt dần

Xét
$$ x'=-x-y,\qquad y'=x-y. $$
Chọn
$$ V=x^2+y^2. $$
Ta có
$$ \dot{V}=2xx'+2yy'
=2x(-x-y)+2y(x-y)
=-2x^2-2y^2. $$
Vì
$$ \dot{V}<0 $$
ngoài gốc, hệ ổn định tiệm cận tại gốc. Đây là ví dụ kinh điển cho sức mạnh của Lyapunov.

### Ví dụ 2: Hệ bảo toàn năng lượng

Với hệ
$$ x'=y,\qquad y'=-x, $$
chọn
$$ V=x^2+y^2. $$
Khi đó
$$ \dot{V}=2xy+2y(-x)=0. $$
Điều này cho thấy năng lượng được bảo toàn. Gốc ổn định theo Lyapunov nhưng không tiệm cận. Đây là ví dụ rất tốt để phân biệt hai khái niệm.

### Ví dụ 3: Chọn sai ứng viên

Nếu chọn một hàm không dương xác định, chẳng hạn
$$ V=x^2-y^2, $$
thì ngay cả khi tính $$ \dot{V} $$ đẹp, nó cũng không còn là thước đo đáng tin của khoảng cách tới cân bằng. Ví dụ này nhắc sinh viên rằng chọn $$ V $$ là nghệ thuật, không chỉ là thao tác.

### Ví dụ 4: Năng lượng cơ học có ma sát

Trong nhiều hệ cơ học, năng lượng toàn phần
$$ V=\text{động năng}+\text{thế năng} $$
là ứng viên tự nhiên. Nếu có ma sát hay lực cản, $$ \dot{V} $$ thường âm. Đây là chiếc cầu trực giác mạnh nhất nối Lyapunov với vật lý.

## Câu hỏi khái niệm

1. Vì sao Lyapunov cho phép nói về ổn định mà không cần công thức nghiệm?
2. Hai yêu cầu "dương xác định" và "đạo hàm không dương" đóng vai trò gì khác nhau?
3. Vì sao $$ \dot{V}=0 $$ thường cho ổn định nhưng chưa chắc cho ổn định tiệm cận?

## Bài toán ứng dụng

1. Trong điều khiển robot, vì sao việc tìm một hàm "năng lượng sai lệch" là chiến lược rất tự nhiên?
2. Trong mạch điện có điện trở, vì sao năng lượng của hệ thường giảm dần và dẫn tới ổn định?
3. Trong sinh học, một đại lượng đo độ lệch khỏi cân bằng có thể đóng vai trò hàm Lyapunov như thế nào?

## Chiến lược giảng dạy tương tác

- Cho sinh viên thử nhiều hàm ứng viên khác nhau để thấy không phải hàm nào cũng hiệu quả.
- Hỏi lớp: "Nếu coi $$ V $$ là năng lượng, hệ đang tiêu hao hay tích lũy năng lượng?"
- So sánh hai ví dụ: một có $$ \dot{V}<0 $$ và một có $$ \dot{V}=0 $$ để nhấn mạnh khác biệt.
- Khuyến khích sinh viên diễn giải hình học của các đường mức $$ V=\text{hằng số} $$.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu bắt đầu từ ứng viên chuẩn
$$ V=x^2+y^2 $$
trong vài bài đầu. Mục tiêu là xây trực giác về $$ \dot{V} $$ trước khi yêu cầu các hàm tinh tế hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi thử xây dựng một hàm Lyapunov riêng cho một hệ phi tuyến cụ thể, hoặc tìm ví dụ mà $$ \dot{V}\le 0 $$ nhưng kết luận tiệm cận cần thêm công cụ mở rộng.

## Tóm tắt dễ nhớ

Phương pháp Lyapunov thay bài toán giải quỹ đạo bằng bài toán tìm một đại lượng luôn giảm. Nếu $$ V $$ đo được độ xa khỏi cân bằng và $$ \dot{V} $$ không tăng, ta có ổn định; nếu $$ \dot{V} $$ giảm nghiêm ngặt, ta thường có ổn định tiệm cận. Đây là ngôn ngữ năng lượng của động lực học.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cơ học có ma sát
- Bài toán: Không giải nghiệm explicit vẫn muốn chứng minh con lắc có ma sát sẽ hạ năng lượng và tiến về đáy.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega,
$$
với ứng viên Lyapunov
$$
V(\theta,\omega)=1-\cos\theta+\frac{1}{2}\omega^2.
$$
- Giả thiết và giới hạn: Kết luận dựa trên cấu trúc năng lượng, không cho tốc độ hội tụ chính xác ngay.
- Diễn giải: Nếu $$ \dot{V}\le 0 $$, hệ không thể tự leo lên mức năng lượng cao hơn.

#### Điều khiển robot
- Bài toán: Thiết kế luật điều khiển để sai số vị trí và vận tốc giảm về $$ 0 $$.
- Mô hình:
$$ \dot{e}_1=e_2,\qquad
\dot{e}_2=-k_1 e_1-k_2 e_2, $$
với
$$ V=\frac{1}{2}(k_1 e_1^2+e_2^2). $$
- Giả thiết và giới hạn: Mô hình hóa đã bỏ qua bão hòa cơ cấu chấp hành và nhiễu đo.
- Diễn giải: Hàm Lyapunov là chứng cứ ổn định, không chỉ là trực giác.

### 2. Trực giác bổ sung và các kết nối

Lyapunov thay bài toán "tìm nghiệm" bằng bài toán "tìm đại lượng giảm". Điều kiện $$ V>0 $$ và $$ \dot{V}\le 0 $$ có vai trò khác nhau: một cái đo khoảng cách tới cân bằng, cái kia kiểm soát hướng tiến hóa. Bẫy thường gặp là kết luận ổn định tiệm cận chỉ từ $$ \dot{V}\le 0 $$. Bài này nối hệ phi tuyến với trực giác năng lượng trong cơ học và điều khiển.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, z):
    x, y = z
    return [-x - y, x - y]

t = np.linspace(0, 8, 400)
for z0 in [(2, 0), (0, 2), (-2, 1)]:
    sol = solve_ivp(system, [0, 8], z0, t_eval=t)
    V = sol.y[0]**2 + sol.y[1]**2
    plt.plot(t, V, label=f"IC={z0}")

plt.xlabel("t")
plt.ylabel("V(t)")
plt.title("Ham Lyapunov giam theo thoi gian")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Lyapunov function energy dissipation pendulum
- search: contour plot Lyapunov function trajectories
- search: asymptotic stability energy method

### 5. Bài toán mẫu có bối cảnh thực

Xét hệ
$$ x'=-x-y,\qquad
y'=x-y. $$
Chọn
$$ V=x^2+y^2. $$
Khi đó
$$ \dot{V}=2x(-x-y)+2y(x-y)=-2x^2-2y^2<0 $$
ngoài gốc. Vì vậy gốc ổn định tiệm cận. Đây là ví dụ mẫu cho việc chứng minh ổn định mà không cần giải nghiệm.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện và kiểm tra các hàm Lyapunov cơ bản như $$ x^2+y^2 $$.

**Bậc sau đại học.** Bàn về định lý Lyapunov trực tiếp, nguyên lý bất biến LaSalle và tính toàn cục của ổn định.

## Tài liệu tham khảo

- Strogatz, Chương 7: giới thiệu rất trực quan phương pháp Lyapunov.
- Arnold, Chương 5: tốt cho trực giác năng lượng và ổn định phi tuyến.
