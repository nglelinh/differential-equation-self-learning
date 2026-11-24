---
layout: post
title: "05-08 Cạnh tranh Loài"
chapter: '05'
order: 8
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

Khi hai loài sinh vật (hoặc hai doanh nghiệp công nghệ trên cùng một thị trường) cùng tranh giành một nguồn tài nguyên hữu hạn, liệu chúng có thể **cùng tồn tại hòa bình** hay một loài sẽ **đẩy loài kia đến tuyệt chủng**? Hệ phương trình cạnh tranh Lotka–Volterra trả lời câu hỏi này bằng một bất đẳng thức cực kỳ rõ nét: **Nguyên lý Loại trừ Cạnh tranh (Gause's Principle)**.

## Bản đồ kiến thức nền: Bốn kịch bản của Hệ Cạnh tranh Hai Loài

1. **Cạnh tranh nội loài vs. Cạnh tranh liên loài**:
   Trong $\dot{x} = r_1 x\left(1 - \frac{x + a_{12} y}{K_1}\right)$ và $\dot{y} = r_2 y\left(1 - \frac{y + a_{21} x}{K_2}\right)$, $K_1, K_2$ là sức chứa môi trường còn $a_{12}, a_{21}$ đo cường độ loài này kìm hãm loài kia.
2. **Hình học hai đường thẳng Nullcline**:
   Hai đoạn thẳng $x + a_{12} y = K_1$ và $a_{21} x + y = K_2$ trong góc phần tư thứ nhất có đúng **4 vị trí tương đối**: không cắt nhau (2 trường hợp một loài thắng tuyệt đối) hoặc cắt nhau tại $E^*$ (ổn định hoặc yên ngựa).
3. **Điều kiện Cùng tồn tại ổn định (Stable Coexistence)**:
   Hai loài cùng sống bền vững khi và chỉ khi **cạnh tranh nội loài mạnh hơn cạnh tranh liên loài** ($a_{12} < K_1/K_2$ và $a_{21} < K_2/K_1$).
4. **Lưỡng ổn định (Bistability — Người đến trước thắng)**:
   Khi cạnh tranh liên loài quá mạnh ($a_{12} > K_1/K_2$ và $a_{21} > K_2/K_1$), điểm giao $E^*$ là **yên ngựa**, đường phân thủy (*separatrix*) chia mặt phẳng thành hai miền: loài nào có lợi thế ban đầu sẽ loại trừ hoàn toàn loài kia!

## Mục tiêu

Bài học này giúp sinh viên phân tích mô hình hai loài cạnh tranh tài nguyên, sử dụng đường nullcline để đánh giá khả năng cùng tồn tại hay loại trừ lẫn nhau và hiểu cách các hệ số cạnh tranh quyết định kết cục sinh thái dài hạn.

## Kiến thức nền

Sinh viên cần nắm vững mặt phẳng pha, đường nullcline, điểm cân bằng và mô hình tăng trưởng logistic. Bài học này áp dụng trực tiếp tư duy phân tích hệ phi tuyến vào câu hỏi sinh học cốt lõi: hai loài sẽ cùng tồn tại hay một loài sẽ loại trừ loài kia?

## Dẫn nhập

![Hai loài cạnh tranh nguồn lực]({{ site.imgurl }}/chapter_img/chapter05/08_competing_species.svg)

Không phải mọi tương tác sinh thái đều thuộc dạng săn mồi – con mồi. Trong nhiều trường hợp, hai loài không tiêu thụ nhau nhưng cùng khai thác một nguồn tài nguyên hữu hạn. Khi đó, tốc độ tăng trưởng của mỗi loài vừa bị giới hạn bởi mật độ của chính nó, vừa bị kìm hãm bởi sự hiện diện của loài kia. Câu hỏi động lực học đặt ra là: hai loài có thể cùng tồn tại lâu dài hay một loài sẽ chiếm ưu thế và đẩy loài còn lại đến tuyệt chủng?

Mô hình cạnh tranh hai loài cho thấy chỉ với một số ít tham số định lượng, hệ đã có thể dẫn đến nhiều kịch bản sinh thái khác nhau. Qua đó, sinh viên thấy rằng "ổn định sinh thái" không phải khái niệm cảm tính mà là hệ quả trực tiếp của cấu trúc các hệ số tương tác.

### Khung giải thích (nên đọc chậm): Xác định số phận hai loài bằng tay qua giao điểm Nullclines

Xét hệ cạnh tranh cụ thể:
$$\dot{x} = x(6 - 2x - y), \qquad \dot{y} = y(4 - x - y).$$

1. **Tìm các giao điểm trục của hai Nullclines**:
   - $x$-nullcline $2x + y = 6$: cắt trục $Ox$ tại $(3, 0)$, cắt trục $Oy$ tại $(0, 6)$.
   - $y$-nullcline $x + y = 4$: cắt trục $Ox$ tại $(4, 0)$, cắt trục $Oy$ tại $(0, 4)$.
2. **Tìm điểm cân bằng nội $E^*$**: Giải $2x + y = 6$ và $x + y = 4 \implies x^* = 2,\; y^* = 2$ (nằm trong góc phần tư thứ I!).
3. **Kiểm tra ổn định tại $E^* = (2, 2)$ bằng Jacobian**:
   $$J(x, y) = \begin{pmatrix} 6 - 4x - y & -x \\ -y & 4 - x - 2y \end{pmatrix} \implies J(2, 2) = \begin{pmatrix} -4 & -2 \\ -2 & -2 \end{pmatrix}.$$
   - Vết $\tau = -4 + (-2) = -6 < 0$.
   - Định thức $\Delta = (-4)(-2) - (-2)(-2) = 8 - 4 = +4 > 0$.
   - Vì $\tau < 0$ và $\Delta > 0$, $E^* = (2, 2)$ là **Nút hút ổn định**! Dù khởi đầu với bao nhiêu cá thể ($x_0, y_0 > 0$), hai loài đều tiến về **cùng tồn tại ổn định tại $(2, 2)$**!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu sống tách biệt, mỗi loài tăng trưởng theo quy luật logistic. Khi cùng chung sống, sự hiện diện của loài kia làm giảm sức chứa hiệu dụng của môi trường. Như vậy, hai loài vừa tự hạn chế mật độ của bản thân, vừa hạn chế lẫn nhau.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, các đường nullcline phân chia miền tăng và giảm của từng loài. Vị trí tương đối giữa hai đường nullcline quyết định xem có tồn tại điểm cân bằng nội ổn định hay không; do đó, chỉ cần quan sát cấu hình nullcline thường đã đủ để dự đoán kết cục sinh thái.

### Cách nhìn hình thức

Một dạng chuẩn của mô hình cạnh tranh hai loài là
$$
\frac{dx}{dt}=r_1x\left(1-\frac{x+\alpha_{12}y}{K_1}\right),
$$
$$
\frac{dy}{dt}=r_2y\left(1-\frac{y+\alpha_{21}x}{K_2}\right).
$$
Trong đó $$ K_1,K_2 $$ là sức chứa môi trường riêng của từng loài, còn $$ \alpha_{12},\alpha_{21} $$ đo mức độ cạnh tranh chéo. Nếu cạnh tranh chéo đủ yếu so với mức tự hạn chế, điểm cân bằng cùng tồn tại có thể ổn định; nếu cạnh tranh chéo quá mạnh, một loài có thể loại trừ loài kia.

## Những ngộ nhận thường gặp

- "Cạnh tranh luôn dẫn đến việc một loài tuyệt chủng." Không đúng. Hai loài vẫn có thể cùng tồn tại ổn định nếu cạnh tranh chéo đủ yếu.
- "Chỉ cần so sánh tốc độ tăng trưởng nội tại $$ r_1,r_2 $$ là biết loài nào thắng." Sai. Sức chứa môi trường và các hệ số cạnh tranh chéo mới là yếu tố quyết định kết cục dài hạn.
- "Hễ có điểm cân bằng nội thì hệ chắc chắn hội tụ về đó." Không đúng; cần kiểm tra tính ổn định của điểm cân bằng đó.
- "Mô hình cạnh tranh chỉ là phương trình logistic viết dài hơn." Sai. Chính các số hạng tương tác chéo tạo ra những kịch bản động lực học mới.

## Tiến trình học tập đề xuất

### Bước 1: Xác định các đường nullcline

Tìm tập hợp các điểm mà tốc độ tăng trưởng của từng loài bằng 0 để phân vùng tăng, giảm.

### Bước 2: Tìm các điểm cân bằng

Xác định đầy đủ cả các điểm cân bằng biên (một hoặc hai loài bằng 0) lẫn điểm cân bằng nội.

### Bước 3: So sánh vị trí tương đối của hai đường nullcline

Phân loại các cấu hình cắt nhau hoặc không cắt nhau để đọc kết cục dài hạn.

### Bước 4: Diễn giải ý nghĩa sinh học

Chuyển kết quả từ hình học mặt phẳng pha sang kịch bản cùng tồn tại hoặc loại trừ cạnh tranh.

### Các điểm kiểm tra

- Sinh viên có giải thích đúng ý nghĩa của các hệ số cạnh tranh chéo hay không.
- Sinh viên có xác định được điều kiện để tồn tại điểm cân bằng nội hay không.
- Sinh viên có phân biệt được giữa sự tồn tại và tính ổn định của điểm cân bằng nội hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Đường nullcline của loài thứ nhất

Từ phương trình
$$
\frac{dx}{dt}=r_1x\left(1-\frac{x+\alpha_{12}y}{K_1}\right),
$$
các đường nullcline của loài 1 là
$$ x=0 $$
và
$$ x+\alpha_{12}y=K_1. $$
Đường thẳng thứ hai cho biết loài 1 ngừng tăng trưởng khi tổng mật độ quy đổi đạt đúng sức chứa môi trường của nó.

### Ví dụ 2: Cạnh tranh yếu và cùng tồn tại ổn định

Khi hai đường nullcline cắt nhau trong góc phần tư thứ nhất sao cho mọi quỹ đạo lân cận đều hướng về giao điểm đó, hệ đạt trạng thái cùng tồn tại ổn định. Đây là kịch bản cả hai loài cùng duy trì mật độ dương lâu dài.

### Ví dụ 3: Cạnh tranh mạnh và loại trừ cạnh tranh

Nếu tác động ức chế của mỗi loài lên loài kia mạnh hơn tác động tự hạn chế lên chính nó, điểm cân bằng nội có thể không ổn định (dạng yên ngựa) hoặc không nằm trong miền dương. Khi đó các quỹ đạo hội tụ về một trong hai điểm cân bằng biên, nghĩa là một loài loại trừ loài còn lại.

### Ví dụ 4: Đọc kết cục sinh học từ hình học

Nếu đường nullcline dương của loài 1 nằm hoàn toàn phía ngoài đường nullcline dương của loài 2 trên cả hai trục, loài 1 có lợi thế cạnh tranh tuyệt đối và sẽ loại trừ loài 2. Đây là minh họa rõ nét cho việc đọc kết luận sinh thái trực tiếp từ hình học mặt phẳng pha.

## Câu hỏi khái niệm

1. Vì sao vị trí tương đối của hai đường nullcline lại quan trọng hơn việc xét riêng từng phương trình?
2. Trong điều kiện nào điểm cân bằng nội biểu thị trạng thái cùng tồn tại bền vững?
3. Vì sao nguyên lý loại trừ cạnh tranh là một hệ quả động lực học cụ thể thay vì một nhận định định tính chung chung?

## Bài toán ứng dụng

1. Hai loài thực vật cùng cạnh tranh nước và ánh sáng. Hãy giải thích vai trò của các hệ số cạnh tranh chéo trong kết cục dài hạn.
2. Trong vi sinh học, hai chủng vi khuẩn cùng sử dụng một nguồn carbon chung. Hãy liên hệ tình huống này với mô hình cạnh tranh hai loài.
3. Khi xây dựng chính sách bảo tồn nhằm duy trì sự cùng tồn tại của hai loài, cần tác động vào những tham số nào của mô hình?

## Chiến lược giảng dạy tương tác

- Yêu cầu sinh viên vẽ các cấu hình nullcline trước khi dự đoán kết cục sinh thái.
- Tổ chức thảo luận nhóm để xác định loài nào có lợi thế trong từng cấu hình hình học và giải thích lý do.
- Cho lớp diễn đạt bằng lời ý nghĩa sinh học của từng tham số $$ K_i $$ và $$ \alpha_{ij} $$.
- Đối chiếu mô hình cạnh tranh với mô hình săn mồi – con mồi để làm nổi bật sự khác biệt về cơ chế tương tác.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên lập bảng hai cột phân tách rõ phần "tự hạn chế" và phần "cạnh tranh chéo" cho mỗi loài trước khi chuyển sang vẽ nullcline. Khi ý nghĩa sinh học rõ ràng, việc đọc hình học sẽ dễ dàng hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên xét tính ổn định của điểm cân bằng nội bằng ma trận Jacobian, hoặc khảo sát sự chuyển đổi kịch bản khi tham số cạnh tranh vượt qua ngưỡng tới hạn.

## Tóm tắt dễ nhớ

Mô hình cạnh tranh hai loài là mô hình logistic có bổ sung tương tác chéo. Cấu hình đường nullcline là công cụ hình học chủ yếu để xác định hai loài cùng tồn tại hay loại trừ nhau. Kết cục sinh thái phụ thuộc vào quan hệ định lượng giữa mức tự hạn chế và các hệ số cạnh tranh chéo.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hai loài cạnh tranh tài nguyên
- Bài toán: Hai loài cùng khai thác một nguồn sống hữu hạn và gây tác động bất lợi cho nhau.
- Mô hình:
$$
\dot{x}=x(1-x-\alpha y),\qquad
\dot{y}=y(1-y-\beta x).
$$
- Giả thiết và giới hạn: Các tham số không đổi theo thời gian và môi trường đồng nhất.
- Diễn giải: Tùy theo giá trị của $$ \alpha,\beta $$, hệ hội tụ về trạng thái cùng tồn tại hoặc dẫn tới việc một loài loại trừ loài kia.

#### Cạnh tranh thị phần
- Bài toán: Hai doanh nghiệp cùng cạnh tranh trong một thị trường có quy mô hữu hạn.
- Mô hình: Sử dụng cấu trúc hệ logistic ghép nối tương tự mô hình cạnh tranh loài.
- Giả thiết và giới hạn: Đây là mô hình tương tự hóa kinh tế, bỏ qua chiến lược định giá và truyền thông phức tạp.
- Diễn giải: Mô hình giúp minh họa cách một lợi thế nhỏ trong hệ số cạnh tranh chéo có thể dẫn đến ưu thế chiếm lĩnh dài hạn.

### 2. Trực giác bổ sung và các kết nối

Mô hình cạnh tranh là ví dụ tiêu biểu nơi hình học nullcline mang lại cái nhìn trực tiếp nhất. Giao điểm của hai đường nullcline là trạng thái mà tốc độ thay đổi tức thời của cả hai loài đều bằng 0. Cần tránh nhầm lẫn đường nullcline với quỹ đạo thực của quần thể. Bài học này mở rộng phương trình logistic một chiều sang hệ hai chiều và làm rõ cơ chế giữa cùng tồn tại (coexistence) và loại trừ cạnh tranh (competitive exclusion).

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

alpha, beta = 0.6, 0.8

def comp(t, z):
    x, y = z
    return [x * (1 - x - alpha * y), y * (1 - y - beta * x)]

for z0 in [(0.2, 0.7), (0.8, 0.2), (0.9, 0.9)]:
    sol = solve_ivp(comp, [0, 20], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

x = np.linspace(0, 1.8, 200)
plt.plot(x, (1 - x) / alpha, "--", label="x-nullcline")
plt.plot((1 - x) / beta, x, "--", label="y-nullcline")
plt.xlim(0, 1.8)
plt.ylim(0, 1.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Canh tranh loai va cac nullcline")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: competing species nullclines coexistence
- search: competitive exclusion phase plane
- search: two species competition model visualization

### 5. Bài toán mẫu có bối cảnh thực

Cho hệ
$$ \dot{x}=x(1-x-0.6y),\qquad
\dot{y}=y(1-y-0.8x). $$
Các đường nullcline dương là
$$ x+0.6y=1,\qquad y+0.8x=1. $$
Giao điểm của hai đường thẳng này nằm trong góc phần tư dương, do đó hệ có một điểm cân bằng nội ứng viên cho trạng thái cùng tồn tại. Việc xét ma trận Jacobian tại giao điểm đó sẽ xác định trạng thái này có ổn định hay không.

### 6. Phân tầng độ khó

**Bậc đại học.** Vẽ các đường nullcline, xác định điểm cân bằng biên và cân bằng nội, sau đó diễn giải bằng ngôn ngữ sinh học.

**Bậc sau đại học.** Phân tích điều kiện cùng tồn tại bền vững, cấu trúc tập hút (attractor) và liên hệ với lý thuyết cạnh tranh trong sinh thái học toán.

## Video tham khảo

- Xem trước: [Lotka-Volterra Competition Explained: Rabbits vs. Sheep | Phase Plane Analysis](https://www.youtube.com/watch?v=07V_UNLz0qs) — Dr. Shane Ross, tiếng Anh. Shane Ross phân tích mô hình cạnh tranh Lotka–Volterra, đường nullcline và nguyên lý loại trừ cạnh tranh.
- [Competition Explained by Lotka-Volterra Model](https://www.youtube.com/watch?v=8GxwFrAyD9Q) — EcologyTalks, tiếng Anh. Giải thích cạnh tranh sinh học thông qua phân tích mặt phẳng pha.
- [V7-4e Two Competing Species, critical points, stability, phase portrait. Elem Differential Equations](https://www.youtube.com/watch?v=btQVm3PGT4k) — wenshenpsu, tiếng Anh. Xác định điểm cân bằng, tính ổn định và chân dung pha của hai loài cạnh tranh.

## Tài liệu tham khảo

- Strogatz, Chương 6: trình bày rõ ràng về phân tích nullcline và điều kiện cùng tồn tại.
- Arnold, Chương 5: hữu ích cho góc nhìn hình học về điểm cân bằng và miền hút.
