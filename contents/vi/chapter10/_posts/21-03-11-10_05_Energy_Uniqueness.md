---
layout: post
title: "Năng Lượng và Tính Duy Nhất"
chapter: '10'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 05 Energy Uniqueness]({{ site.imgurl }}/chapter_img/chapter10/05_energy_uniqueness.svg)

## Mục tiêu

Bài học này giúp sinh viên hiểu vì sao năng lượng là đại lượng tự nhiên nhất để kiểm soát phương trình sóng. Sau bài học, sinh viên cần biết viết năng lượng của dây rung, hiểu cơ chế bảo toàn năng lượng dưới các điều kiện biên phù hợp, dùng năng lượng để suy ra tính duy nhất, và so sánh bản chất bảo toàn của sóng với bản chất tắt dần của phương trình nhiệt.

## Kiến thức nền

Sinh viên nên nắm phương trình sóng, tích phân từng phần và trực giác về động năng, thế năng. Đây là bài có giá trị kết nối mạnh giữa cơ học và PDE: một đại lượng vật lý quen thuộc trở thành công cụ toán học để chứng minh định lý.

## Dẫn nhập

Cho đến đây, ta đã thấy sóng truyền và dao động. Nhưng làm sao biết nghiệm không nổ vô lý, không mất ổn định, và với cùng dữ liệu đầu thì không thể có hai nghiệm khác nhau? Câu trả lời nằm ở năng lượng. Năng lượng không chỉ là khái niệm vật lý; nó là đại lượng toán học kiểm soát toàn bộ bài toán.

Điều rất đẹp là phương trình sóng không làm mất năng lượng như phương trình nhiệt. Thay vào đó, nó chuyển đổi qua lại giữa động năng và thế năng đàn hồi. Chính cấu trúc này là lý do ta có bảo toàn năng lượng và từ đó có tính duy nhất rất sạch.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một dây rung vừa chuyển động lên xuống vừa bị kéo căng. Vì vậy năng lượng của nó có hai phần: động năng do vận tốc, và thế năng do biến dạng. Khi dây đi qua vị trí cân bằng, động năng lớn còn thế năng nhỏ. Khi dây đạt biên lớn nhất, vận tốc nhỏ đi nhưng biến dạng lớn hơn. Tổng hai phần này được giữ nguyên nếu không có ma sát.

### Cách nhìn hình ảnh

Nếu ta vẽ dây ở các thời điểm khác nhau, hình dạng có thể thay đổi liên tục, nhưng "mức độ hoạt động tổng thể" của hệ không đổi trong bài toán thuần nhất. Điều đó nghĩa là năng lượng không biến mất cũng không tự sinh ra, chỉ chuyển giữa dao động và độ cong không gian của dây.

### Cách nhìn hình thức

Với dây rung một chiều, năng lượng thường được viết là

$$
E(t)=\frac{1}{2}\int_0^L\bigl(\rho u_t^2+T u_x^2\bigr)\,dx.
$$

Nếu dùng dạng chuẩn $$ u_{tt}=c^2u_{xx} $$, ta có thể viết tương đương

$$
E(t)=\frac{1}{2}\int_0^L\bigl(u_t^2+c^2u_x^2\bigr)\,dx
$$

sau khi chuẩn hóa hệ số. Nhân PDE với $$ u_t $$ và tích phân theo $$ x $$, ta thu được

$$ \frac{dE}{dt}=c^2[u_xu_t]_0^L. $$

Nếu hạng biên bằng 0, ta có

$$ \frac{dE}{dt}=0. $$

## Những ngộ nhận thường gặp

- "Năng lượng chỉ là phần trực giác vật lý, không cần cho chứng minh." Sai. Đây là công cụ chứng minh mạnh nhất của bài.
- "Phương trình sóng luôn làm năng lượng giảm như phương trình nhiệt." Không đúng; với hệ thuần nhất không tắt dần, năng lượng được bảo toàn.
- "Tính duy nhất phải đến từ công thức nghiệm." Không nhất thiết; lập luận năng lượng cho ta tính duy nhất mà không cần viết nghiệm rõ ràng.
- "Nếu năng lượng bằng 0 thì chỉ suy ra vận tốc bằng 0." Sai; còn suy ra độ dốc không gian bằng 0, và từ dữ liệu đầu-biên ta suy ra nghiệm bằng 0.

## Tiến trình học tập đề xuất

### Bước 1: Viết đúng năng lượng

Sinh viên cần thấy rõ động năng và thế năng nằm ở đâu.

### Bước 2: Nhân PDE với

$$ u_t $$

Đây là thao tác trung tâm.

### Bước 3: Tích phân từng phần và đọc hạng biên

Điều kiện biên thực sự xuất hiện ở đây.

### Bước 4: Dùng năng lượng cho tính duy nhất

Đây là phần cần được nhấn mạnh nhất.

### Các checkpoint

- Sinh viên có giải thích được vì sao năng lượng có hai phần hay không.
- Sinh viên có tính đúng đạo hàm theo thời gian của năng lượng hay không.
- Sinh viên có biết điều kiện biên nào làm hạng biên triệt tiêu hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bảo toàn năng lượng với biên cố định

Nếu $$ u(0,t)=u(L,t)=0 $$, thì suy ra $$ u_t(0,t)=u_t(L,t)=0 $$ trên biên cố định theo thời gian. Vì vậy $$ [u_xu_t]_0^L=0 $$ và $$ E'(t)=0 $$. Ví dụ này là trường hợp chuẩn nên được học thật chắc.

### Ví dụ 2: Tính duy nhất

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán. Đặt $$ w=u_1-u_2 $$. Khi đó $$ w_{tt}=c^2w_{xx} $$ với dữ liệu đầu và biên bằng 0. Năng lượng của $$ w $$ tại $$ t=0 $$ bằng 0, nên nhờ bảo toàn năng lượng ta có $$ E_w(t)=0 $$ với mọi $$ t $$. Do đó $$ w_t=0,\qquad w_x=0 $$, và cuối cùng $$ w\equiv 0 $$. Đây là ví dụ chứng minh đẹp nhất của bài.

### Ví dụ 3: So sánh với phương trình nhiệt

Với phương trình nhiệt, năng lượng kiểu

$$ \int u^2 $$

thường giảm theo thời gian. Với phương trình sóng, năng lượng cơ học được bảo toàn. Ví dụ so sánh này cực kỳ hữu ích để phân biệt bản chất của hai lớp PDE.

### Ví dụ 4: Biên tự do

Nếu điều kiện biên là $$ u_x(0,t)=u_x(L,t)=0 $$, thì hạng biên cũng triệt tiêu. Ví dụ này giúp sinh viên thấy không chỉ Dirichlet mà cả Neumann tự nhiên cũng có thể bảo toàn năng lượng.

## Câu hỏi khái niệm

1. Vì sao năng lượng của phương trình sóng có thể được hiểu là tổng của động năng và thế năng?
2. Tại sao hạng biên đóng vai trò quyết định trong công thức năng lượng?
3. Vì sao bảo toàn năng lượng dẫn đến tính duy nhất rất tự nhiên?

## Bài toán ứng dụng

1. Một dây đàn lý tưởng không có ma sát. Vì sao năng lượng không mất đi dù hình dạng dây thay đổi liên tục?
2. Trong mô hình có tắt dần, nếu thêm hạng $$ \gamma u_t $$, vì sao ta kỳ vọng năng lượng giảm?
3. Trong mô phỏng số sóng, vì sao việc theo dõi năng lượng là cách tốt để kiểm tra độ tin cậy của chương trình?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Khi dây rung, năng lượng đang nằm ở đâu?"
- Cho sinh viên tự nhân PDE với

$$ u_t $$

và thử đoán trước dạng của năng lượng.
- Hỏi cả lớp: "Điều kiện biên nào làm biên không bơm hay rút năng lượng khỏi hệ?"
- Tổ chức hoạt động chứng minh tính duy nhất theo nhóm từ công thức năng lượng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào phiên bản một chiều với biên cố định trước. Khi động năng, thế năng và hạng biên đã rõ, lập luận tổng quát sẽ nhẹ nhàng hơn rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận không gian năng lượng cho nghiệm yếu, hoặc so sánh cơ chế bảo toàn năng lượng với các hệ Hamilton trong cơ học.

## Tóm tắt dễ nhớ

Phương trình sóng thuần nhất bảo toàn năng lượng. Năng lượng gồm phần vận tốc và phần biến dạng không gian. Chính cấu trúc này cho ta công cụ mạnh để chứng minh tính duy nhất và hiểu vì sao sóng khác căn bản với nhiệt.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kiểm chứng mô phỏng dao động
- Bài toán: Trong mô phỏng cấu trúc, bảo toàn năng lượng là phép kiểm tra chất lượng quan trọng.
- Mô hình:
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx.
$$
- Giả thiết và giới hạn: Hệ không có tắt dần và biên thích hợp.
- Diễn giải: Năng lượng toàn phần đổi chỗ giữa động năng và thế năng đàn hồi nhưng tổng giữ nguyên.

#### Tính duy nhất của đáp án vật lý
- Bài toán: Nếu hai mô hình có cùng dữ liệu đầu và biên, ta muốn biết chúng có thể cho hai nghiệm khác nhau hay không.
- Mô hình: Áp dụng phương pháp năng lượng cho hiệu của hai nghiệm.
- Giả thiết và giới hạn: Bài toán tuyến tính, dữ liệu đủ trơn.
- Diễn giải: Bảo toàn năng lượng dẫn trực tiếp đến tính duy nhất.

### 2. Trực giác bổ sung và các kết nối

Phương pháp năng lượng ít phụ thuộc vào việc có công thức nghiệm tường minh hay không. Nó cho một "định luật vật lý toàn cục" từ đó suy ra ổn định và duy nhất. Đây là ý tưởng sẽ quay lại nhiều lần trong PDE hiện đại.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
kinetic = np.sin(t) ** 2
potential = np.cos(t) ** 2

plt.plot(t, kinetic, label="Dong nang")
plt.plot(t, potential, label="The nang")
plt.plot(t, kinetic + potential, label="Tong nang luong", linewidth=2)
plt.xlabel("t")
plt.title("Trao doi nang luong trong mot mode song")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: wave equation energy conservation animation
- search: uniqueness proof wave equation energy method
- search: numerical wave solver energy drift

### 5. Bài toán mẫu có bối cảnh thực

Với dây cố định hai đầu, lấy đạo hàm theo thời gian của
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx
$$
và dùng tích phân từng phần, các hạng biên triệt tiêu nên $$ E'(t)=0 $$. Nếu hiệu của hai nghiệm có dữ liệu đầu bằng không, năng lượng của hiệu bằng không với mọi $$ t $$, do đó hiệu bằng không và nghiệm là duy nhất.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu năng lượng là tổng của động năng và thế năng đàn hồi.

**Bậc sau đại học.** Mở rộng sang ước lượng năng lượng, ổn định yếu và bài toán hyperbolic với hệ số biến thiên.
