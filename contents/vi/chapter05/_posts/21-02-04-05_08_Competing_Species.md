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

## Mục tiêu

Bài học này giúp sinh viên phân tích mô hình hai loài cạnh tranh tài nguyên, dùng nullcline để đọc khả năng cùng tồn tại hay loại trừ, và hiểu cách các hệ số cạnh tranh quyết định kết quả sinh thái dài hạn.

## Kiến thức nền

Sinh viên cần nắm mặt phẳng pha, nullcline, điểm cân bằng và trực giác logistic. Bài học này là nơi tư duy mô hình hóa hệ phi tuyến bước thẳng vào một câu hỏi sinh học rất thực: cùng tồn tại hay loại trừ.

## Dẫn nhập

![Hai loài cạnh tranh nguồn lực]({{ site.imgurl }}/chapter_img/chapter05/08_competing_species.svg)

Không phải mọi tương tác sinh thái đều là săn mồi-con mồi. Nhiều khi hai loài không ăn nhau, nhưng cùng cần một nguồn tài nguyên giới hạn. Khi đó, mỗi loài không chỉ bị cản bởi mật độ của chính mình mà còn bởi sự hiện diện của loài kia. Từ đây nảy sinh câu hỏi động lực học rất tự nhiên: hai loài sẽ cùng tồn tại, hay một loài sẽ đẩy loài kia ra khỏi hệ?

Mô hình cạnh tranh hai loài là ví dụ rất hay vì chỉ cần vài hệ số là ta đã có thể thấy nhiều kịch bản sinh thái khác nhau. Nó dạy sinh viên rằng "ổn định sinh thái" không phải là một ý niệm mơ hồ, mà là hệ quả của những tỷ lệ tương tác định lượng rất cụ thể.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Mỗi loài lớn lên theo kiểu logistic nếu sống một mình. Nhưng khi có loài kia, sức chứa hiệu dụng của môi trường giảm đi. Hai loài vì thế không chỉ tự hạn chế mà còn hạn chế lẫn nhau.

### Cách nhìn hình ảnh

Trên mặt phẳng pha, nullcline của mỗi loài là những đường chia vùng tăng và giảm. Vị trí tương đối của hai nullcline quyết định liệu có điểm cân bằng cùng tồn tại ổn định hay không. Nhìn hình nullcline thường đã đủ để dự đoán kết quả sinh thái.

### Cách nhìn hình thức

Một dạng chuẩn là
$$
\frac{dx}{dt}=r_1x\left(1-\frac{x+\alpha_{12}y}{K_1}\right),
$$
$$
\frac{dy}{dt}=r_2y\left(1-\frac{y+\alpha_{21}x}{K_2}\right).
$$
Ở đây $$ K_1,K_2 $$ là sức chứa riêng, còn $$ \alpha_{12},\alpha_{21} $$ đo mức độ cạnh tranh chéo. Nếu cạnh tranh chéo yếu đủ, cân bằng cùng tồn tại có thể ổn định. Nếu cạnh tranh chéo quá mạnh, một loài có thể loại trừ loài kia.

## Những ngộ nhận thường gặp

- "Cạnh tranh luôn làm một loài tuyệt chủng." Không đúng. Đồng tồn tại ổn định vẫn có thể xảy ra.
- "Chỉ cần nhìn tốc độ tăng trưởng nội tại $$ r_1,r_2 $$ là đủ." Sai. Hệ số cạnh tranh chéo mới là yếu tố quyết định lớn về lâu dài.
- "Nếu có điểm cân bằng nội thì chắc chắn hệ sẽ tiến tới đó." Không nhất thiết; còn phải xét ổn định.
- "Mô hình cạnh tranh chỉ là logistic viết dài hơn." Sai. Chính tương tác chéo tạo ra động lực học mới.

## Tiến trình học tập đề xuất

### Bước 1: Viết nullcline

Xác định vùng tăng giảm của từng loài.

### Bước 2: Tìm các điểm cân bằng

Cân bằng biên và cân bằng nội.

### Bước 3: So sánh vị trí nullcline

Đây là chìa khóa hình học để đọc kết quả sinh thái.

### Bước 4: Diễn giải sinh học

Chuyển từ hình học pha sang cùng tồn tại hay loại trừ.

### Các checkpoint

- Sinh viên có đọc đúng ý nghĩa của các hệ số cạnh tranh không.
- Sinh viên có nhìn ra khi nào có cân bằng nội không.
- Sinh viên có phân biệt được tồn tại cân bằng với ổn định của cân bằng không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Nullcline của loài thứ nhất

Từ
$$
\frac{dx}{dt}=r_1x\left(1-\frac{x+\alpha_{12}y}{K_1}\right),
$$
ta có nullcline:
$$ x=0 $$
hoặc
$$ x+\alpha_{12}y=K_1. $$
Đường thẳng thứ hai cho biết loài 1 dừng tăng khi tổng "gánh nặng hiệu dụng" đạt sức chứa của nó.

### Ví dụ 2: Cạnh tranh yếu và đồng tồn tại

Nếu hai nullcline cắt nhau theo cách tạo ra một điểm cân bằng nội nằm trong góc phần tư dương và quỹ đạo lân cận tiến về đó, ta có đồng tồn tại ổn định. Đây là kịch bản sinh thái hòa hợp tương đối.

### Ví dụ 3: Cạnh tranh mạnh và loại trừ

Nếu mỗi loài tác động lên loài kia mạnh hơn chính nó tự hạn chế bản thân, cân bằng nội có thể không ổn định hoặc không tồn tại trong miền dương. Khi đó hệ thường đi tới một trong hai cân bằng biên, nghĩa là một loài thắng thế.

### Ví dụ 4: Đọc sinh học từ hình học

Nếu nullcline của loài 1 nằm "xa hơn" nullcline của loài 2 theo cả hai trục, điều đó thường gợi ý loài 1 có lợi thế cạnh tranh toàn cục. Đây là nơi hình học mặt phẳng pha trở thành trực giác sinh thái.

## Câu hỏi khái niệm

1. Vì sao vị trí tương đối của nullcline quan trọng hơn việc chỉ nhìn riêng từng phương trình?
2. Khi nào cân bằng nội biểu thị đồng tồn tại bền?
3. Vì sao loại trừ cạnh tranh là một kết quả động lực học chứ không chỉ là một khẩu hiệu sinh thái?

## Bài toán ứng dụng

1. Hai loài thực vật cùng tranh nước và ánh sáng. Hãy giải thích vì sao hệ số cạnh tranh chéo quyết định kết cục lâu dài.
2. Trong vi sinh, hai dòng vi khuẩn cùng dùng một nguồn carbon. Hãy liên hệ với mô hình cạnh tranh hai loài.
3. Một chính sách bảo tồn muốn giữ hai loài cùng tồn tại. Hãy giải thích cần chú ý tham số nào của mô hình.

## Chiến lược giảng dạy tương tác

- Cho sinh viên vẽ nullcline trước rồi mới hỏi kết quả sinh thái.
- Tổ chức thảo luận nhóm: "Loài nào đang có lợi thế và vì sao?"
- Yêu cầu lớp giải thích bằng lời ý nghĩa sinh học của từng tham số $$ K_i $$ và $$ \alpha_{ij} $$.
- So sánh mô hình cạnh tranh với mô hình săn mồi-con mồi để thấy hai cơ chế tương tác khác nhau về bản chất.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu dùng bảng hai cột "tự hạn chế" và "cạnh tranh chéo" cho từng loài trước khi đi vào nullcline. Khi nghĩa sinh học rõ ràng, hình học sẽ dễ theo hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi phân tích ổn định của cân bằng nội bằng Jacobian, hoặc khảo sát cách kết quả thay đổi khi tham số cạnh tranh đi qua một ngưỡng.

## Tóm tắt dễ nhớ

Mô hình cạnh tranh hai loài là logistic có tương tác chéo. Nullcline là chìa khóa hình học để đọc kết quả: cùng tồn tại hay loại trừ. Kết cục sinh thái không do một loài "mạnh hơn" theo cảm giác, mà do cấu trúc định lượng của các hệ số cạnh tranh.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hai loài tranh tài nguyên
- Bài toán: Hai loài cùng dùng một nguồn sống hữu hạn và ảnh hưởng bất lợi lẫn nhau.
- Mô hình:
$$
\dot{x}=x(1-x-\alpha y),\qquad
\dot{y}=y(1-y-\beta x).
$$
- Giả thiết và giới hạn: Tham số không đổi theo thời gian, môi trường đồng nhất.
- Diễn giải: Tùy $$ \alpha,\beta $$, hệ có thể dẫn đến cùng tồn tại hoặc một loài loại trừ loài kia.

#### Cạnh tranh thị phần
- Bài toán: Hai công ty tranh cùng một thị trường hữu hạn.
- Mô hình: Dùng cấu trúc logistic ghép nối tương tự mô hình cạnh tranh loài.
- Giả thiết và giới hạn: Đây là mô hình ẩn dụ kinh tế, bỏ qua chiến lược giá và quảng cáo phức tạp.
- Diễn giải: Hệ giúp giải thích vì sao ưu thế nhỏ trong cạnh tranh chéo có thể dẫn đến chiếm lĩnh dài hạn.

### 2. Trực giác bổ sung và các kết nối

Mô hình cạnh tranh là nơi hình học nullcline trở nên rất giàu ý nghĩa. Giao điểm của hai nullcline biểu diễn trạng thái mà cả hai loài đều không đổi tức thời. Bẫy thường gặp là đọc nullcline như đường đi thật của dân số. Bài này nối logistic một chiều với hệ hai chiều và làm rõ cơ chế coexistence so với competitive exclusion.

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

Cho
$$ \dot{x}=x(1-x-0.6y),\qquad
\dot{y}=y(1-y-0.8x). $$
Nullcline dương là
$$ x+0.6y=1,\qquad y+0.8x=1. $$
Giao điểm nằm trong góc phần tư dương, nên về mặt hình học có ứng viên cân bằng cùng tồn tại. Phân tích Jacobian tại đó cho biết trạng thái này ổn định hay không.

### 6. Phân tầng độ khó

**Bậc đại học.** Vẽ nullcline, xác định cân bằng biên và cân bằng trong, rồi diễn giải bằng ngôn ngữ sinh học.

**Bậc sau đại học.** Phân tích điều kiện cùng tồn tại bền vững, kéo theo tập hấp dẫn và liên hệ với lý thuyết cạnh tranh trong sinh thái học toán.

## Tài liệu tham khảo

- Strogatz, Chương 6: rất tốt cho phân tích nullcline và đồng tồn tại.
- Arnold, Chương 5: hữu ích cho góc nhìn hình học của các cân bằng và miền hút.
