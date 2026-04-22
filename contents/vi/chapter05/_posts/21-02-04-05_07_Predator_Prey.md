---
layout: post
title: "05-07 Mô hình Săn mồi-Con mồi"
chapter: '05'
order: 7
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên phân tích mô hình Lotka-Volterra săn mồi-con mồi, đọc nullcline, điểm cân bằng, quỹ đạo trên mặt phẳng pha, và hiểu vì sao phản hồi chéo giữa hai quần thể có thể tạo ra dao động tự nhiên mà không cần lực ngoài tuần hoàn.

## Kiến thức nền

Sinh viên cần nắm hệ tự trị, mặt phẳng pha, điểm cân bằng và một ít trực giác sinh thái. Bài học này là nơi các công cụ định tính của chương bước vào một mô hình sinh học kinh điển.

## Dẫn nhập

![Mô hình săn mồi con mồi Lotka-Volterra]({{ site.imgurl }}/chapter_img/chapter05/07_predator_prey.svg)

Nếu chỉ nhìn riêng quần thể con mồi, ta có thể nghĩ nó tăng trưởng. Nếu chỉ nhìn riêng quần thể săn mồi, ta có thể nghĩ nó suy giảm khi thiếu thức ăn. Nhưng khi hai quần thể tương tác, một vòng phản hồi xuất hiện: nhiều con mồi làm săn mồi tăng, săn mồi tăng lại làm con mồi giảm, con mồi giảm thì săn mồi thiếu thức ăn và giảm theo, rồi con mồi lại phục hồi. Câu chuyện đó tự nó đã là một hệ động lực học hoàn chỉnh.

Mô hình Lotka-Volterra là ví dụ cực kỳ quan trọng vì nó cho sinh viên thấy một điều bất ngờ: dao động không nhất thiết đến từ forcing tuần hoàn bên ngoài. Chúng có thể xuất hiện thuần túy từ phản hồi nội tại giữa các biến của hệ.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Con mồi giống như nguồn thức ăn, săn mồi giống như bộ phận tiêu thụ. Khi nguồn thức ăn dồi dào, bên tiêu thụ phát triển. Nhưng phát triển quá mạnh lại làm nguồn thức ăn cạn. Chu trình tăng-giảm xen kẽ này tạo nên dao động sinh thái.

### Cách nhìn hình ảnh

Trên mặt phẳng pha $$ (x,y) $$, với $$ x $$ là con mồi và $$ y $$ là săn mồi, các nullcline chia mặt phẳng thành các vùng mà mỗi quần thể tăng hoặc giảm. Quỹ đạo thường quay quanh điểm cân bằng nội, tạo các đường kín trong mô hình lý tưởng.

### Cách nhìn hình thức

Mô hình Lotka-Volterra cổ điển có dạng
$$ \frac{dx}{dt}=ax-bxy, $$
$$ \frac{dy}{dt}=-cy+dxy, $$
trong đó $$ a,b,c,d>0 $$. Các điểm cân bằng là
$$ (0,0) $$
và
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Điểm cân bằng nội mô tả mức cùng tồn tại của hai quần thể trong mô hình lý tưởng.

## Những ngộ nhận thường gặp

- "Dao động trong Lotka-Volterra là do thời tiết hay lực ngoài." Sai. Chúng đến từ phản hồi nội tại của mô hình.
- "Nếu quỹ đạo đóng thì chắc chắn có chu trình giới hạn." Không đúng. Trong Lotka-Volterra cổ điển, các quỹ đạo đóng là một họ và thường phản ánh cấu trúc bảo toàn.
- "Mô hình này là mô hình sinh thái cuối cùng." Sai. Nó là mô hình nền để xây trực giác, nhưng còn rất lý tưởng hóa.
- "Săn mồi tăng thì con mồi luôn giảm ngay tức thì theo mọi nghĩa." Cần đọc điều này trong tương quan toàn hệ và theo từng vùng của mặt phẳng pha.

## Tiến trình học tập đề xuất

### Bước 1: Tìm nullcline

Đọc nơi mỗi quần thể đổi từ tăng sang giảm.

### Bước 2: Tìm điểm cân bằng

Đặc biệt là cân bằng nội sinh thái.

### Bước 3: Phác họa mặt phẳng pha

Quan sát hướng quay và các quỹ đạo kín.

### Bước 4: Diễn giải sinh học

Chuyển từ công thức sang câu chuyện quần thể.

### Các checkpoint

- Sinh viên có diễn giải được từng số hạng của mô hình hay không.
- Sinh viên có tìm đúng cân bằng nội không.
- Sinh viên có giải thích được vì sao có dao động không cần forcing ngoài không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Nullcline

Từ
$$ \frac{dx}{dt}=x(a-by), $$
ta có nullcline của con mồi:
$$ x=0 \quad \text{hoặc} \quad y=\frac{a}{b}. $$
Từ
$$ \frac{dy}{dt}=y(-c+dx), $$
ta có nullcline của săn mồi:
$$ y=0 \quad \text{hoặc} \quad x=\frac{c}{d}. $$
Chỉ riêng bước này đã cho một khung rất mạnh để đọc mặt phẳng pha.

### Ví dụ 2: Điểm cân bằng nội

Giao của hai nullcline không trục là
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Đây là trạng thái mà con mồi và săn mồi đều giữ mức không đổi trong mô hình lý tưởng.

### Ví dụ 3: Ý nghĩa của quỹ đạo kín

Các quỹ đạo kín quanh cân bằng nội cho thấy nếu hệ bắt đầu ở một mức quần thể nào đó, nó sẽ dao động lặp lại theo chu kỳ. Nhưng chu kỳ này do phản hồi nội tại giữa hai loài tạo nên, không phải do yếu tố mùa vụ từ bên ngoài.

### Ví dụ 4: Tích phân bảo toàn

Mô hình Lotka-Volterra cổ điển có một đại lượng bảo toàn dạng
$$ V(x,y)=dx-c\ln x+by-a\ln y. $$
Điều này giải thích vì sao các quỹ đạo là những đường mức đóng trong mô hình lý tưởng. Đây là điểm rất đẹp để sinh viên thấy cấu trúc sâu phía sau dao động.

## Câu hỏi khái niệm

1. Vì sao phản hồi chéo giữa hai quần thể lại đủ để tạo dao động?
2. Nullcline giúp ta đọc điều gì về tăng giảm của từng quần thể?
3. Vì sao quỹ đạo kín trong Lotka-Volterra cổ điển chưa phải là chu trình giới hạn hút?

## Bài toán ứng dụng

1. Một hệ sinh thái biển có cá nhỏ và cá săn mồi. Hãy giải thích vì sao số lượng hai loài có thể dao động lệch pha.
2. Trong nông nghiệp, việc giảm mạnh số săn mồi tự nhiên có thể làm quần thể sâu hại biến động ra sao?
3. Một mô hình bệnh ký sinh cũng có phản hồi giữa ký sinh và vật chủ. Hãy liên hệ với tư duy predator-prey.

## Chiến lược giảng dạy tương tác

- Cho sinh viên kể lại bằng lời câu chuyện "nhiều con mồi, nhiều săn mồi, rồi ít con mồi..." trước khi viết phương trình.
- Dùng nullcline như công cụ hoạt động nhóm: mỗi nhóm phụ trách một vùng dấu.
- Hỏi lớp: "Nếu săn mồi bằng 0, con mồi sẽ làm gì? Nếu con mồi bằng 0, săn mồi sẽ làm gì?"
- Khuyến khích sinh viên so sánh mô hình sinh thái với các mô hình phản hồi chéo trong kinh tế hoặc dịch tễ.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu bắt đầu bằng diễn giải từng số hạng của mô hình. Nếu các em hiểu rõ ý nghĩa của $$ ax $$, $$ -bxy $$, $$ -cy $$ và $$ dxy $$, mặt phẳng pha sẽ tự nhiên hơn rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi kiểm tra trực tiếp đại lượng bảo toàn bằng cách tính đạo hàm theo quỹ đạo, hoặc phân tích xem việc thêm tự hạn chế logistic cho con mồi sẽ thay đổi bức tranh pha như thế nào.

## Tóm tắt dễ nhớ

Lotka-Volterra cho thấy dao động có thể sinh ra từ phản hồi nội tại giữa hai loài. Nullcline và điểm cân bằng nội là chìa khóa đọc mặt phẳng pha. Mô hình rất lý tưởng, nhưng nó dạy một trực giác cực kỳ quan trọng về phản hồi và dao động sinh thái.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Linh miêu và thỏ rừng
- Bài toán: Quần thể săn mồi và con mồi thay nhau tăng giảm theo chu kỳ.
- Mô hình Lotka-Volterra:
$$ \dot{x}=ax-bxy,\qquad
\dot{y}=-cy+dxy. $$
- Giả thiết và giới hạn: Bỏ qua sức chứa môi trường, mùa vụ và độ trễ sinh học.
- Diễn giải: Khi con mồi tăng, săn mồi có thức ăn nhiều hơn; khi săn mồi tăng, con mồi giảm; chu kỳ nảy sinh tự nhiên từ phản hồi.

#### Sinh học kiểm soát dịch hại
- Bài toán: Đưa thiên địch vào ruộng để kìm sâu hại.
- Mô hình: Dùng cùng cấu trúc săn mồi-con mồi nhưng tham số được hiểu như tốc độ tấn công và chuyển hóa năng lượng.
- Giả thiết và giới hạn: Thực tế còn có môi trường không đồng nhất và can thiệp con người.
- Diễn giải: Mô hình giúp dự đoán khi nào việc kiểm soát tạo dao động mạnh thay vì ổn định dân số.

### 2. Trực giác bổ sung và các kết nối

Hệ săn mồi-con mồi là ví dụ kinh điển cho việc động lực học không đơn giản là tăng hay giảm đơn điệu. Một bẫy phổ biến là nghĩ chu kỳ trong Lotka-Volterra là luôn ổn định; thật ra mô hình gốc có quỹ đạo đóng trung tính, không phải limit cycle hút. Bài này nối nullcline, điểm cân bằng, tuyến tính hóa và cấu trúc bảo toàn kiểu Hamilton giản lược.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a, b, c, d = 1.5, 1.0, 1.0, 0.75

def lv(t, z):
    x, y = z
    return [a * x - b * x * y, -c * y + d * x * y]

t = np.linspace(0, 25, 1000)
sol = solve_ivp(lv, [0, 25], [1.8, 0.8], t_eval=t, max_step=0.05)

plt.subplot(1, 2, 1)
plt.plot(t, sol.y[0], label="prey")
plt.plot(t, sol.y[1], label="predator")
plt.xlabel("t")
plt.title("Tien hoa theo thoi gian")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sol.y[0], sol.y[1])
plt.xlabel("prey")
plt.ylabel("predator")
plt.title("Quy dao tren mat phang pha")
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Lotka Volterra phase portrait
- search: predator prey nullclines interpretation
- search: biological control predator prey dynamics

### 5. Bài toán mẫu có bối cảnh thực

Với hệ Lotka-Volterra, điểm cân bằng dương là
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Tại đó, tốc độ tăng tự nhiên của con mồi được cân bằng bởi săn mồi, còn tử vong tự nhiên của săn mồi được bù bởi nguồn thức ăn. Tuyến tính hóa quanh cân bằng cho ta dao động gần tuần hoàn.

### 6. Phân tầng độ khó

**Bậc đại học.** Tìm nullcline, điểm cân bằng và diễn giải sinh học của từng tham số.

**Bậc sau đại học.** Nghiên cứu tích phân bảo toàn, mô hình Rosenzweig-MacArthur và các cơ chế tạo limit cycle ổn định.

## Tài liệu tham khảo

- Strogatz, Chương 6: rất mạnh về nullcline, quỹ đạo và trực giác sinh thái.
- Arnold, Chương 4-5: hữu ích cho cấu trúc hình học và đại lượng bảo toàn.
