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

Bài học này giúp sinh viên phân tích mô hình Lotka–Volterra săn mồi – con mồi, đọc các đường nullcline, điểm cân bằng và quỹ đạo trên mặt phẳng pha, đồng thời hiểu vì sao phản hồi chéo giữa hai quần thể có thể tạo ra dao động tự nhiên mà không cần lực cưỡng bức tuần hoàn từ bên ngoài.

## Kiến thức nền

Sinh viên cần nắm vững hệ tự trị, mặt phẳng pha, điểm cân bằng và một số khái niệm sinh thái cơ bản. Bài học này đưa các công cụ định tính của chương vào một mô hình sinh học kinh điển.

## Dẫn nhập

![Mô hình săn mồi con mồi Lotka-Volterra]({{ site.imgurl }}/chapter_img/chapter05/07_predator_prey.svg)

Nếu xét riêng quần thể con mồi, số lượng của chúng có xu hướng tăng trưởng; nếu xét riêng quần thể săn mồi, số lượng của chúng sẽ suy giảm khi thiếu nguồn thức ăn. Khi hai quần thể tương tác, một vòng phản hồi hình thành: nhiều con mồi giúp loài săn mồi tăng lên, loài săn mồi tăng lại làm con mồi suy giảm, con mồi giảm khiến loài săn mồi thiếu thức ăn và giảm theo, nhờ đó con mồi lại phục hồi. Quá trình này tạo nên một hệ động lực học hoàn chỉnh.

Mô hình Lotka–Volterra có ý nghĩa quan trọng vì cho thấy dao động không nhất thiết xuất phát từ lực cưỡng bức tuần hoàn bên ngoài, mà có thể nảy sinh thuần túy từ cơ chế phản hồi nội tại giữa các biến trạng thái.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Con mồi đóng vai trò nguồn thức ăn, còn loài săn mồi là thành phần tiêu thụ. Khi nguồn thức ăn dồi dào, quần thể tiêu thụ phát triển; khi tiêu thụ tăng quá mức, nguồn thức ăn cạn dần. Chu trình tăng – giảm luân phiên này tạo nên dao động sinh thái.

### Cách nhìn hình ảnh

Trên mặt phẳng pha $$ (x,y) $$, với $$ x $$ là mật độ con mồi và $$ y $$ là mật độ loài săn mồi, các đường nullcline chia mặt phẳng thành các miền tăng và giảm của từng quần thể. Trong mô hình lý tưởng, các quỹ đạo quay quanh điểm cân bằng nội và tạo thành những đường cong khép kín.

### Cách nhìn hình thức

Mô hình Lotka–Volterra cổ điển có dạng
$$ \frac{dx}{dt}=ax-bxy, $$
$$ \frac{dy}{dt}=-cy+dxy, $$
trong đó $$ a,b,c,d>0 $$. Hệ có hai điểm cân bằng là
$$ (0,0) $$
và
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Điểm cân bằng nội biểu diễn trạng thái cùng tồn tại của hai quần thể trong mô hình lý tưởng.

## Những ngộ nhận thường gặp

- "Dao động trong mô hình Lotka–Volterra là do thời tiết hoặc yếu tố mùa vụ bên ngoài." Sai. Dao động này xuất phát trực tiếp từ phản hồi nội tại trong hệ.
- "Có quỹ đạo khép kín nghĩa là có chu trình giới hạn." Không đúng. Trong mô hình Lotka–Volterra cổ điển, các quỹ đạo đóng tạo thành một họ liên tục và phản ánh cấu trúc bảo toàn, không phải chu trình giới hạn cô lập.
- "Đây là mô hình sinh thái đầy đủ nhất." Sai. Đây là mô hình nền tảng để xây dựng trực giác, còn nhiều giả thiết lý tưởng hóa.
- "Khi loài săn mồi tăng thì con mồi lập tức giảm trong mọi trường hợp." Cần xét dấu của $$ \dot{x} $$ theo từng miền trên mặt phẳng pha thay vì suy luận rời rạc.

## Tiến trình học tập đề xuất

### Bước 1: Tìm các đường nullcline

Xác định nơi mỗi quần thể chuyển từ xu hướng tăng sang xu hướng giảm.

### Bước 2: Tìm các điểm cân bằng

Xác định cân bằng tầm thường và đặc biệt là điểm cân bằng nội.

### Bước 3: Phác họa mặt phẳng pha

Xác định chiều quay của trường vector và dạng các quỹ đạo kín quanh điểm cân bằng nội.

### Bước 4: Diễn giải ý nghĩa sinh học

Chuyển kết quả hình học thành diễn biến thực tế của hai quần thể.

### Các điểm kiểm tra

- Sinh viên có giải thích được ý nghĩa sinh học của từng số hạng trong mô hình hay không.
- Sinh viên có tìm đúng điểm cân bằng nội hay không.
- Sinh viên có giải thích được vì sao hệ dao động mà không cần tác động tuần hoàn từ bên ngoài hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Các đường nullcline

Từ
$$ \frac{dx}{dt}=x(a-by), $$
nullcline của con mồi là
$$ x=0 \quad \text{hoặc} \quad y=\frac{a}{b}. $$
Từ
$$ \frac{dy}{dt}=y(-c+dx), $$
nullcline của loài săn mồi là
$$ y=0 \quad \text{hoặc} \quad x=\frac{c}{d}. $$
Các đường thẳng này tạo nên bộ khung cơ bản để chia miền dấu trên mặt phẳng pha.

### Ví dụ 2: Điểm cân bằng nội

Giao điểm của hai nullcline khác các trục tọa độ là
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Tại trạng thái này, số lượng con mồi và loài săn mồi đều giữ nguyên theo thời gian trong mô hình lý tưởng.

### Ví dụ 3: Ý nghĩa của quỹ đạo kín

Các quỹ đạo khép kín quanh điểm cân bằng nội cho thấy nếu hệ xuất phát tại một trạng thái dương bất kỳ (khác điểm cân bằng), hai quần thể sẽ dao động tuần hoàn lệch pha nhau. Chu kỳ dao động xuất phát từ tương tác nội tại giữa hai loài chứ không phải từ biến động mùa vụ bên ngoài.

### Ví dụ 4: Đại lượng bảo toàn

Mô hình Lotka–Volterra cổ điển sở hữu một đại lượng bảo toàn có dạng
$$ V(x,y)=dx-c\ln x+by-a\ln y. $$
Do $$ V(x,y) $$ không đổi dọc theo nghiệm, các quỹ đạo chính là các đường đồng mức khép kín của $$ V $$, giải thích cấu trúc bảo toàn đứng sau dao động của hệ.

## Câu hỏi khái niệm

1. Vì sao cơ chế phản hồi chéo giữa hai quần thể đủ để tạo ra dao động?
2. Các đường nullcline cung cấp thông tin gì về xu hướng tăng giảm của từng quần thể?
3. Vì sao các quỹ đạo kín trong mô hình Lotka–Volterra cổ điển không phải là chu trình giới hạn hút?

## Bài toán ứng dụng

1. Trong một hệ sinh thái biển gồm cá nhỏ và cá săn mồi, hãy giải thích vì sao số lượng hai loài có thể dao động lệch pha theo thời gian.
2. Trong nông nghiệp, việc giảm mạnh số lượng thiên địch tự nhiên có thể ảnh hưởng đến biến động quần thể sâu hại như thế nào?
3. Một mô hình ký sinh cũng có cơ chế phản hồi giữa vật ký sinh và vật chủ. Hãy liên hệ cấu trúc đó với mô hình săn mồi – con mồi.

## Chiến lược giảng dạy tương tác

- Cho sinh viên diễn đạt bằng lời vòng phản hồi giữa hai quần thể trước khi viết phương trình vi phân.
- Tổ chức hoạt động nhóm với các đường nullcline: mỗi nhóm xác định dấu và hướng chuyển động trên một miền.
- Đặt câu hỏi kiểm tra biên: nếu loài săn mồi bằng 0 thì con mồi biến đổi ra sao; ngược lại, nếu con mồi bằng 0 thì loài săn mồi biến đổi ra sao?
- Liên hệ mô hình sinh thái với các hệ phản hồi chéo trong kinh tế học hoặc dịch tễ học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu bằng việc phân tích ý nghĩa của từng số hạng $$ ax $$, $$ -bxy $$, $$ -cy $$ và $$ dxy $$. Khi hiểu rõ ý nghĩa sinh học của phương trình, việc đọc mặt phẳng pha sẽ tự nhiên hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tính trực tiếp đạo hàm theo thời gian của đại lượng bảo toàn $$ V(x,y) $$, hoặc khảo sát sự thay đổi của mặt phẳng pha khi bổ sung số hạng tự hạn chế logistic cho con mồi.

## Tóm tắt dễ nhớ

Mô hình Lotka–Volterra minh họa cách dao động nảy sinh từ phản hồi nội tại giữa hai loài. Đường nullcline và điểm cân bằng nội là công cụ chính để đọc mặt phẳng pha. Dù mang tính lý tưởng hóa cao, mô hình cung cấp trực giác nền tảng về phản hồi và dao động sinh thái.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Linh miêu và thỏ rừng
- Bài toán: Quần thể loài săn mồi và con mồi thay phiên nhau tăng giảm theo chu kỳ.
- Mô hình Lotka–Volterra:
$$ \dot{x}=ax-bxy,\qquad
\dot{y}=-cy+dxy. $$
- Giả thiết và giới hạn: Bỏ qua sức chứa môi trường, yếu tố mùa vụ và độ trễ sinh học.
- Diễn giải: Khi con mồi tăng, loài săn mồi có thêm thức ăn nên phát triển; khi loài săn mồi tăng, con mồi giảm; chu kỳ dao động hình thành tự nhiên từ vòng phản hồi.

#### Kiểm soát dịch hại bằng biện pháp sinh học
- Bài toán: Đưa thiên địch vào đồng ruộng nhằm kìm hãm quần thể sâu hại.
- Mô hình: Giữ cấu trúc săn mồi – con mồi với các tham số biểu diễn tốc độ săn bắt và hiệu suất chuyển hóa sinh khối.
- Giả thiết và giới hạn: Thực tế còn chịu ảnh hưởng của môi trường không đồng nhất và các tác động canh tác.
- Diễn giải: Mô hình giúp dự đoán khi nào biện pháp sinh học dẫn đến dao động biên độ lớn thay vì ổn định quần thể.

### 2. Trực giác bổ sung và các kết nối

Hệ săn mồi – con mồi là ví dụ kinh điển cho thấy động lực học không chỉ là quá trình tăng hay giảm đơn điệu. Một sai lầm phổ biến là cho rằng chu kỳ trong mô hình Lotka–Volterra cổ điển luôn ổn định; thực tế mô hình gốc chỉ có họ quỹ đạo đóng trung tính chứ không phải chu trình giới hạn hút. Bài học này liên kết đường nullcline, điểm cân bằng, tuyến tính hóa và cấu trúc bảo toàn dạng Hamilton giản lược.

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

Trong hệ Lotka–Volterra, điểm cân bằng dương là
$$ \left(\frac{c}{d},\frac{a}{b}\right). $$
Tại điểm này, tốc độ sinh trưởng tự nhiên của con mồi cân bằng với mức tiêu thụ của loài săn mồi, còn tỷ lệ tử vong tự nhiên của loài săn mồi được bù đắp bởi nguồn thức ăn. Tuyến tính hóa quanh điểm cân bằng này cho thấy động học cục bộ dạng dao động tuần hoàn.

### 6. Phân tầng độ khó

**Bậc đại học.** Xác định đường nullcline, điểm cân bằng và diễn giải ý nghĩa sinh học của từng tham số.

**Bậc sau đại học.** Khảo sát đại lượng bảo toàn, mô hình Rosenzweig–MacArthur và các cơ chế tạo chu trình giới hạn ổn định.

## Video tham khảo

- Xem trước: [Predator-Prey Population Models || Lotka-Volterra Equations](https://www.youtube.com/watch?v=DDEvlLa9z_U) — Exploring Maths, tiếng Anh. Giới thiệu phương trình Lotka–Volterra và quỹ đạo đóng của hệ săn mồi – con mồi.
- [Predator-Prey Model (Lotka-Volterra)](https://www.youtube.com/watch?v=Tc05IbqTsFM) — Mike Saint-Antoine, tiếng Anh. Trình bày chi tiết mô hình cùng phân tích mặt phẳng pha.
- [Lotka-Volterra Equation and Their Periodic Solutions](https://www.youtube.com/watch?v=WPck8AhuOsc) — Mike, the Mathematician, tiếng Anh. Giải thích vì sao các nghiệm tuần hoàn của Lotka–Volterra không bền vững về mặt cấu trúc.

## Tài liệu tham khảo

- Strogatz, Chương 6: trình bày trực quan về đường nullcline, quỹ đạo và ý nghĩa sinh thái.
- Arnold, Chương 4–5: hữu ích cho cấu trúc hình học và đại lượng bảo toàn.
