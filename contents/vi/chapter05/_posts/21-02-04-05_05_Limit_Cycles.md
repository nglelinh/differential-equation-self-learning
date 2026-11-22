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

Bài học này giúp sinh viên hiểu chu trình giới hạn như một dạng dao động tự duy trì trong hệ phi tuyến, phân biệt chu trình giới hạn với tâm tuyến tính và nắm được vai trò của định lý Poincaré–Bendixson trong việc chứng minh sự tồn tại quỹ đạo đóng cô lập trên mặt phẳng.

## Kiến thức nền

Sinh viên cần nắm vững mặt phẳng pha, điểm cân bằng, tính ổn định và trực giác cơ bản về dao động từ các chương trước. Bài học này đánh dấu bước chuyển từ việc xét điểm cân bằng sang xét quỹ đạo tuần hoàn như đối tượng động lực học chính.

## Dẫn nhập

![Chu trình giới hạn và quỹ đạo lân cận]({{ site.imgurl }}/chapter_img/chapter05/05_limit_cycles.svg)

Không phải mọi hệ động lực đều hội tụ về một điểm cân bằng. Nhiều hệ thực tế — từ nhịp đập của tim, mạch dao động điện tử tự kích đến các phản ứng hóa học dao động — duy trì chuyển động lặp lại theo chu kỳ và bền vững trước nhiễu nhỏ. Trong động lực học, quỹ đạo như vậy thường là một chu trình giới hạn.

Đặc trưng quan trọng nhất của chu trình giới hạn là tính cô lập. Một tâm tuyến tính cũng có vô số quỹ đạo khép kín, nhưng chúng không cô lập và rất dễ bị phá vỡ khi mô hình thay đổi nhỏ. Ngược lại, chu trình giới hạn là một quỹ đạo đóng cô lập mà các quỹ đạo lân cận bị hút vào hoặc đẩy ra, nên mang ý nghĩa động lực học bền vững hơn nhiều.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một hệ có cơ chế tự điều chỉnh biên độ dao động: khi biên độ quá nhỏ, hệ bổ sung thêm năng lượng; khi biên độ quá lớn, hệ tiêu hao bớt năng lượng. Kết quả là hình thành một quỹ đạo dao động ổn định mà hệ tự động hội tụ về. Đó là trực giác của chu trình giới hạn hút.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, chu trình giới hạn hiện ra như một đường cong khép kín cô lập. Các quỹ đạo ở lân cận có thể xoắn dần vào trong, xoắn ra ngoài, hoặc bị hút từ một phía và đẩy ra ở phía kia. Cấu trúc này khác hẳn dạng tâm, vốn gồm cả một họ đường cong đóng lồng liên tiếp vào nhau.

### Cách nhìn hình thức

Một **chu trình giới hạn** (limit cycle) là một quỹ đạo tuần hoàn cô lập của hệ tự trị phẳng. **Định lý Poincaré–Bendixson** phát biểu rằng nếu một quỹ đạo bị chặn trong một miền đóng và tập giới hạn omega của nó không chứa điểm cân bằng nào, thì tập giới hạn ấy phải là một quỹ đạo tuần hoàn. Đây là kết quả nền tảng để chứng minh sự tồn tại của dao động tuần hoàn trong mặt phẳng.

## Những ngộ nhận thường gặp

- "Mọi quỹ đạo đóng đều là chu trình giới hạn." Sai. Chu trình giới hạn bắt buộc phải cô lập.
- "Chu trình giới hạn chỉ là dao động tuần hoàn thông thường." Sai. Đây là một cấu trúc phi tuyến bền vững, khác với dao động bảo toàn phụ thuộc điều kiện đầu.
- "Nếu hệ có dao động thì chắc chắn tồn tại chu trình giới hạn." Không đúng. Hệ có thể chỉ có tâm hoặc dao động tắt dần quá độ.
- "Định lý Poincaré–Bendixson chứng minh hỗn loạn trong mặt phẳng." Ngược lại, định lý này cho thấy hệ tự trị hai chiều không thể xuất hiện hỗn loạn như hệ từ ba chiều trở lên.

## Tiến trình học tập đề xuất

### Bước 1: Phân biệt quỹ đạo đóng với chu trình giới hạn

Làm rõ vai trò quyết định của tính cô lập.

### Bước 2: Quan sát hành vi của quỹ đạo lân cận

Xác định chu trình giới hạn thuộc loại hút (ổn định), đẩy (không ổn định) hay bán ổn định.

### Bước 3: Hiểu vai trò của định lý Poincaré–Bendixson

Nắm vững giả thiết (tính bị chặn, không chứa điểm cân bằng) và ý nghĩa của kết luận.

### Bước 4: Liên hệ với mô hình thực tế

Nhận diện chu trình giới hạn như cơ chế của các dao động tự duy trì.

### Các điểm kiểm tra

- Sinh viên có phân biệt được tâm tuyến tính với chu trình giới hạn hay không.
- Sinh viên có diễn giải được khái niệm "cô lập" bằng lời hay không.
- Sinh viên có hiểu vì sao điều kiện "bị chặn" lại thiết yếu trong định lý Poincaré–Bendixson hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Tâm không phải chu trình giới hạn

Hệ
$$ \dot{x}=y,\qquad \dot{y}=-x $$
có vô số quỹ đạo tròn đồng tâm quanh gốc tọa độ. Tuy nhiên, không có quỹ đạo nào là chu trình giới hạn vì không tồn tại quỹ đạo đóng cô lập tách biệt với các quỹ đạo đóng lân cận.

### Ví dụ 2: Phương trình van der Pol

Xét phương trình
$$ \ddot{x}-\mu(1-x^2)\dot{x}+x=0. $$
Chuyển về hệ bậc nhất:
$$ \dot{x}=y,
\qquad
\dot{y}=\mu(1-x^2)y-x. $$
Về mặt năng lượng, khi biên độ nhỏ, hệ được cấp thêm năng lượng (ma sát âm); khi biên độ lớn, hệ tiêu hao năng lượng (ma sát dương). Sự cân bằng giữa hai cơ chế này tạo ra một chu trình giới hạn hút — ví dụ kinh điển nhất của bài học.

### Ví dụ 3: Hút vào một quỹ đạo đóng

Nếu mọi quỹ đạo xuất phát bên trong một miền hình vành khăn đóng đều bị giữ lại bên trong và miền đó không chứa điểm cân bằng nào, định lý Poincaré–Bendixson khẳng định tồn tại ít nhất một quỹ đạo tuần hoàn bên trong miền. Đây là khuôn khổ suy luận định tính rất quan trọng.

### Ví dụ 4: Tính bền vững của chu trình giới hạn

Khác với tâm tuyến tính, chu trình giới hạn hút thường vẫn duy trì khi mô hình chịu nhiễu nhỏ. Tính bền vững này khiến nó trở thành mô hình phù hợp cho nhiều hiện tượng thực tế như nhịp tim, mạch dao động điện tử và các chu kỳ sinh học.

## Câu hỏi khái niệm

1. Vì sao tính cô lập là tiêu chí phân biệt bản chất giữa tâm và chu trình giới hạn?
2. Định lý Poincaré–Bendixson cho thấy vai trò gì của tính bị chặn trong mặt phẳng?
3. Vì sao chu trình giới hạn là mô hình tự nhiên cho các dao động tự duy trì?

## Bài toán ứng dụng

1. Một mạch dao động điện tử tự kích có biên độ ổn định sau giai đoạn khởi động. Hãy giải thích vì sao chu trình giới hạn là khái niệm phù hợp để mô tả hiện tượng này.
2. Nhịp tim bình thường có tính tuần hoàn và tự phục hồi sau các nhiễu nhỏ. Hãy diễn giải đặc điểm này bằng trực giác về chu trình giới hạn.
3. Trong sinh học hoặc hóa học, một số hệ tự dao động mà không cần lực cưỡng bức tuần hoàn từ bên ngoài. Hãy giải thích vì sao đây là hiện tượng đặc trưng của hệ phi tuyến.

## Chiến lược giảng dạy tương tác

- Cho sinh viên đối chiếu hai chân dung pha: một tâm tuyến tính và một chu trình giới hạn hút.
- Đặt câu hỏi cho lớp: nếu bị lệch nhẹ khỏi quỹ đạo đóng này, quỹ đạo có quay trở về đường cũ không?
- Phân tích phương trình van der Pol dưới góc độ năng lượng: biên độ nhỏ thì bơm năng lượng, biên độ lớn thì tiêu hao năng lượng.
- Yêu cầu sinh viên diễn đạt ý nghĩa định lý Poincaré–Bendixson bằng ngôn ngữ trực quan trước khi phát biểu hình thức.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên so sánh trực quan hình vẽ của tâm và chu trình giới hạn trước. Khi đã nắm chắc sự khác biệt hình học, khái niệm "cô lập" sẽ trở nên rõ ràng hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên xây dựng một miền bẫy (trapping region) và vận dụng định lý Poincaré–Bendixson để lập luận sự tồn tại của chu trình giới hạn.

## Tóm tắt dễ nhớ

Chu trình giới hạn là một quỹ đạo đóng cô lập và bền vững về mặt động lực học, mô tả các dao động tự duy trì trong hệ phi tuyến. Khác với tâm gồm cả một họ đường đóng lồng nhau, chu trình giới hạn là một quỹ đạo đóng riêng lẻ mà các quỹ đạo lân cận bị hút vào hoặc đẩy ra.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động điện tử tự duy trì
- Bài toán: Mạch dao động cần tự ổn định ở một biên độ xác định thay vì tắt dần về 0 hoặc tăng vô hạn.
- Mô hình van der Pol:
$$ \dot{x}=y,\qquad
\dot{y}=\mu(1-x^2)y-x. $$
- Giả thiết và giới hạn: Đây là mô hình rút gọn của cơ chế khuếch đại và bão hòa phi tuyến.
- Diễn giải: Chu trình giới hạn ổn định giải thích vì sao nhiều điều kiện đầu khác nhau đều hội tụ về cùng một dạng sóng tuần hoàn.

#### Nhịp sinh học và tế bào tim
- Bài toán: Một hệ sinh học cần duy trì nhịp dao động đều đặn bất chấp các nhiễu nhỏ.
- Mô hình: Hệ phi tuyến hai chiều có quỹ đạo đóng ổn định.
- Giả thiết và giới hạn: Hệ sinh học thực thường có nhiều biến trạng thái hơn, nhưng cơ chế dao động bền vững được nắm bắt qua chu trình giới hạn.
- Diễn giải: Chu trình giới hạn phản ánh nhịp sinh học nội tại chứ không chỉ là chuyển động tuần hoàn do bảo toàn năng lượng.

### 2. Trực giác bổ sung và các kết nối

Chu trình giới hạn là quỹ đạo tuần hoàn cô lập, khác hoàn toàn với họ quỹ đạo đóng của tâm tuyến tính. Một sai lầm thường gặp là chỉ thấy quỹ đạo khép kín rồi vội kết luận đó là chu trình giới hạn; cần kiểm tra tính cô lập và hành vi ổn định của các quỹ đạo lân cận. Bài học này kết nối khái niệm ổn định cục bộ với động lực học tuần hoàn và mở đường cho phân nhánh Hopf.

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

Với hệ van der Pol khi $$ \mu>0 $$, các quỹ đạo gần gốc bị đẩy ra ngoài, còn các quỹ đạo xa gốc lại bị kéo vào trong do số hạng $$ \mu(1-x^2)y $$. Sự kết hợp giữa đẩy gần và hút xa hình thành một quỹ đạo tuần hoàn ổn định. Vì nghiệm đóng hiếm khi tồn tại, mô phỏng số là công cụ thực hành chủ yếu để khảo sát hình dạng chu trình.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm định nghĩa, nhận diện chu trình giới hạn và phân tích tính hút hay đẩy của các quỹ đạo lân cận.

**Bậc sau đại học.** Vận dụng định lý Poincaré–Bendixson, ánh xạ Poincaré và phân nhánh Hopf để phân tích sự hình thành chu trình giới hạn.

## Video tham khảo

- Xem trước: [MAE5790-8 Index theory and introduction to limit cycles](https://www.youtube.com/watch?v=O2fcpxLT5wk) — Cornell MAE, tiếng Anh. Lý thuyết chỉ số và phần giới thiệu đầu tiên về chu trình giới hạn trong khóa học của Strogatz.
- [MAE5790-9 Testing for closed orbits](https://www.youtube.com/watch?v=nWO74rlr58Y) — Cornell MAE, tiếng Anh. Các tiêu chuẩn kiểm tra sự tồn tại của quỹ đạo đóng.
- [MAE5790-10 van der Pol oscillator](https://www.youtube.com/watch?v=O1lQrHemPsw) — Cornell MAE, tiếng Anh. Bộ dao động van der Pol làm ví dụ chuẩn cho chu trình giới hạn hút.

## Tài liệu tham khảo

- Strogatz, Chương 7: trình bày trực quan về chu trình giới hạn và phương trình van der Pol.
- Arnold, Chương 5: hữu ích cho góc nhìn hình học về quỹ đạo đóng và tính ổn định của chu trình.
