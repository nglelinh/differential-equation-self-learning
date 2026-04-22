---
layout: post
title: "05-05 Chu trình Giới hạn"
chapter: '05'
order: 5
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên hiểu chu trình giới hạn như dao động tự duy trì trong hệ phi tuyến, phân biệt nó với tâm tuyến tính, và nắm vai trò của định lý Poincaré-Bendixson trong việc suy ra sự tồn tại quỹ đạo đóng cô lập trên mặt phẳng.

## Kiến thức nền

Sinh viên cần nắm mặt phẳng pha, điểm cân bằng, ổn định và một chút trực giác về dao động từ các chương trước. Bài học này là bước chuyển từ cân bằng sang quỹ đạo tuần hoàn như đối tượng động lực học chính.

## Dẫn nhập

![Chu trình giới hạn và quỹ đạo lân cận]({{ site.imgurl }}/chapter_img/chapter05/05_limit_cycles.svg)

Không phải mọi hệ đều tiến về một điểm cân bằng. Nhiều hệ thực tế, từ tim đập, mạch điện tự kích, đến phản ứng hóa học dao động, có hành vi lặp lại theo chu kỳ mà vẫn bền dưới nhiễu nhỏ. Trong ngôn ngữ động lực học, quỹ đạo như vậy thường là một chu trình giới hạn.

Điều làm chu trình giới hạn thú vị là tính cô lập của nó. Một tâm tuyến tính cũng có vô số quỹ đạo khép kín, nhưng chúng không cô lập và rất nhạy với thay đổi mô hình. Chu trình giới hạn thì khác: nó là một quỹ đạo đóng được các quỹ đạo lân cận hút vào hoặc đẩy ra. Vì vậy nó có ý nghĩa động lực học bền hơn nhiều.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một hệ luôn tự điều chỉnh biên độ dao động. Nếu biên độ quá nhỏ, hệ bơm thêm năng lượng. Nếu biên độ quá lớn, hệ tiêu hao bớt năng lượng. Kết quả là có một vòng dao động ổn định mà hệ bị hút vào. Đó chính là trực giác của chu trình giới hạn hút.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, chu trình giới hạn là một đường cong khép kín cô lập. Các quỹ đạo ở gần nó có thể xoắn vào, xoắn ra, hoặc hút từ một phía và đẩy từ phía kia. Hình học này rất khác với tâm, nơi ta có cả một họ đường đóng lồng vào nhau.

### Cách nhìn hình thức

Một chu trình giới hạn là một quỹ đạo tuần hoàn cô lập của hệ tự trị phẳng. Định lý Poincaré-Bendixson phát biểu rằng nếu một quỹ đạo bị chặn trong một miền đóng và vùng giới hạn omega của nó không chứa điểm cân bằng, thì vùng giới hạn ấy phải là một quỹ đạo tuần hoàn. Đây là kết quả trung tâm để chứng minh tồn tại dao động tuần hoàn trong mặt phẳng.

## Những ngộ nhận thường gặp

- "Mọi quỹ đạo đóng đều là chu trình giới hạn." Sai. Cần tính cô lập.
- "Chu trình giới hạn chỉ là dao động tuần hoàn bình thường." Sai. Nó là một đối tượng động lực học bền.
- "Nếu hệ dao động thì chắc chắn có chu trình giới hạn." Không đúng. Có thể chỉ là tâm hoặc dao động quá độ.
- "Poincaré-Bendixson chứng minh hỗn loạn trong mặt phẳng." Ngược lại, nó cho thấy mặt phẳng hai chiều không hỗn loạn theo cách ba chiều có thể.

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt quỹ đạo đóng và chu trình giới hạn

Nhấn mạnh tính cô lập.

### Bước 2: Quan sát quỹ đạo lân cận

Hút vào, đẩy ra hay bán ổn định.

### Bước 3: Học vai trò của Poincaré-Bendixson

Không cần chứng minh đầy đủ, nhưng cần hiểu sức mạnh kết luận.

### Bước 4: Liên hệ với mô hình thực

Nhìn chu trình giới hạn như dao động tự duy trì.

### Các checkpoint

- Sinh viên có phân biệt được tâm với chu trình giới hạn không.
- Sinh viên có giải thích được "cô lập" bằng lời không.
- Sinh viên có thấy vì sao bị chặn là điều kiện quan trọng trong Poincaré-Bendixson không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Tâm không phải chu trình giới hạn

Hệ
$$ \dot{x}=y,\qquad \dot{y}=-x $$
có vô số quỹ đạo tròn quanh gốc. Nhưng đó không phải chu trình giới hạn vì không có quỹ đạo đóng nào cô lập khỏi các quỹ đạo đóng lân cận.

### Ví dụ 2: Phương trình van der Pol

Xét
$$ \ddot{x}-\mu(1-x^2)\dot{x}+x=0. $$
Đưa về hệ:
$$ \dot{x}=y,
\qquad
\dot{y}=\mu(1-x^2)y-x. $$
Trực giác động học là: biên độ nhỏ thì hệ bơm năng lượng, biên độ lớn thì hệ tắt năng lượng. Vì vậy xuất hiện một chu trình giới hạn hút. Đây là ví dụ kinh điển nhất của bài học.

### Ví dụ 3: Hút vào một quỹ đạo đóng

Nếu mọi quỹ đạo xuất phát trong một vành nào đó đều bị chặn và không tiến về cân bằng bên trong, thì Poincaré-Bendixson gợi ý mạnh rằng chúng phải tiến về một chu trình giới hạn. Đây là khuôn suy luận định tính rất quan trọng.

### Ví dụ 4: Ý nghĩa bền của chu trình giới hạn

Khác với tâm tuyến tính, chu trình giới hạn thường vẫn tồn tại dưới nhiễu nhỏ của hệ. Điều này làm nó phù hợp hơn nhiều với mô hình thực tế như nhịp tim, dao động điện tử hoặc sinh học.

## Câu hỏi khái niệm

1. Vì sao tính cô lập là điểm phân biệt bản chất giữa tâm và chu trình giới hạn?
2. Poincaré-Bendixson nói gì về vai trò của tính bị chặn trong mặt phẳng?
3. Vì sao chu trình giới hạn là mô hình tự nhiên của dao động tự duy trì?

## Bài toán ứng dụng

1. Một mạch dao động điện tử tự kích có biên độ ổn định sau một thời gian. Hãy giải thích vì sao chu trình giới hạn là ngôn ngữ phù hợp.
2. Nhịp tim bình thường là dao động định kỳ nhưng bền. Hãy diễn giải điều này bằng trực giác của chu trình giới hạn.
3. Trong sinh học hoặc hóa học, một hệ dao động không cần lực ngoài tuần hoàn. Hãy giải thích vì sao đây là hiện tượng phi tuyến thực sự.

## Chiến lược giảng dạy tương tác

- Cho sinh viên so sánh hai hình: một tâm và một chu trình giới hạn hút.
- Hỏi lớp: "Nếu lệch nhỏ khỏi quỹ đạo đóng này, hệ có quay lại không?"
- Dùng van der Pol như ví dụ kể chuyện bằng năng lượng: nhỏ thì bơm, lớn thì tắt.
- Khuyến khích sinh viên diễn giải Poincaré-Bendixson bằng lời thường trước khi viết mệnh đề toán.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu tập trung vào so sánh tâm và chu trình giới hạn bằng hình vẽ trước. Khi trực giác hình học vững, định nghĩa cô lập sẽ dễ vào hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi phân tích một vùng bẫy và dùng Poincaré-Bendixson như khuôn suy luận để dự đoán sự tồn tại chu trình giới hạn.

## Tóm tắt dễ nhớ

Chu trình giới hạn là quỹ đạo đóng cô lập và bền về mặt động lực học. Nó mô tả dao động tự duy trì của hệ phi tuyến. Tâm thì có nhiều đường đóng, còn chu trình giới hạn là một đường đóng đặc biệt mà quỹ đạo lân cận bị hút vào hoặc đẩy ra.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động điện tử tự duy trì
- Bài toán: Mạch dao động cần tự ổn định biên độ thay vì tắt dần hoặc tăng vô hạn.
- Mô hình van der Pol:
$$ \dot{x}=y,\qquad
\dot{y}=\mu(1-x^2)y-x. $$
- Giả thiết và giới hạn: Đây là mô hình rút gọn của cơ chế khuếch đại và phi tuyến bão hòa.
- Diễn giải: Chu trình giới hạn ổn định giải thích vì sao nhiều điều kiện đầu khác nhau vẫn hội tụ về cùng một dao động tuần hoàn.

#### Nhịp sinh học và tế bào tim
- Bài toán: Một hệ sinh học cần dao động lặp lại đều đặn bất chấp nhiễu nhỏ.
- Mô hình: Dùng hệ phi tuyến hai chiều có quỹ đạo đóng ổn định.
- Giả thiết và giới hạn: Hệ thực thường nhiều biến hơn, nhưng cơ chế dao động bền được nắm qua limit cycle.
- Diễn giải: Chu trình giới hạn mô tả nhịp nội tại chứ không chỉ là chuyển động tuần hoàn do bảo toàn năng lượng.

### 2. Trực giác bổ sung và các kết nối

Chu trình giới hạn là quỹ đạo tuần hoàn cô lập. Điều đó khác với họ quỹ đạo đóng của một tâm tuyến tính. Một bẫy phổ biến là thấy quỹ đạo kín rồi kết luận có limit cycle; phải kiểm tra tính cô lập và ổn định lân cận. Bài này nối ổn định địa phương với động lực học tuần hoàn và mở đường cho phân nhánh Hopf.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

mu = 1.5

def vdp(t, z):
    x, y = z
    return [y, mu * (1 - x**2) * y - x]

for z0 in [(0.2, 0.0), (2.0, 0.0), (0.5, 2.0)]:
    sol = solve_ivp(vdp, [0, 30], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Hoi tu ve chu trinh gioi han van der Pol")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: van der Pol limit cycle phase portrait
- search: Poincare Bendixson visualization
- search: stable periodic orbit nonlinear oscillator

### 5. Bài toán mẫu có bối cảnh thực

Với hệ van der Pol khi $$ \mu>0 $$, nghiệm gần gốc bị đẩy ra nhưng xa gốc lại bị kéo vào do hạng $$ \mu(1-x^2)y $$. Sự kết hợp giữa đẩy gần và hút xa tạo một quỹ đạo tuần hoàn ổn định. Đây là tình huống mà lời giải đóng hiếm khi có, nên mô phỏng số là công cụ thực hành chính.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu định nghĩa, nhận diện limit cycle và diễn giải hút hay đẩy của quỹ đạo lân cận.

**Bậc sau đại học.** Dùng định lý Poincare-Bendixson, bản đồ Poincare và phân nhánh Hopf để giải thích sự xuất hiện chu trình giới hạn.

## Tài liệu tham khảo

- Strogatz, Chương 7: trình bày rất trực quan về chu trình giới hạn và van der Pol.
- Arnold, Chương 5: hữu ích cho trực giác hình học của quỹ đạo đóng và ổn định chu trình.
