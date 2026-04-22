---
layout: post
title: "04-10 Ứng dụng: Mô hình Ngăn"
chapter: '04'
order: 10
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: optional
---

## Mục tiêu

Bài học này giúp sinh viên thấy hệ phương trình là ngôn ngữ tự nhiên của các mô hình ngăn trong dược động học, sinh thái và dịch tễ học. Sinh viên sẽ học cách viết phương trình cân bằng dòng vào-dòng ra cho từng ngăn, nhận ra tính bảo toàn hoặc hao hụt tổng lượng, và diễn giải ma trận hệ như một bản đồ chuyển dòng giữa các khoang.

## Kiến thức nền

Sinh viên cần nắm hệ tuyến tính, ý tưởng nguồn ngoài và một ít trực giác mô hình hóa kiểu "vào trừ ra". Kỹ năng kiểm tra đơn vị và đọc ý nghĩa của các hệ số rất quan trọng hơn cả kỹ thuật giải thuần túy.

## Dẫn nhập

![Mô hình ngăn với dòng chuyển giữa các khoang]({{ site.imgurl }}/chapter_img/chapter04/10_compartment_models.svg)

Không phải mọi hệ phương trình đều đến từ dao động và cơ học. Một lớp ứng dụng rất quan trọng khác là mô hình ngăn, trong đó mỗi biến trạng thái đo lượng vật chất, dân số, thuốc hoặc chất ô nhiễm trong một khoang, và các hệ số mô tả tốc độ chuyển từ khoang này sang khoang khác.

Điểm đẹp của mô hình ngăn là chúng cho thấy hệ phương trình không chỉ mô tả "bao nhiêu", mà còn mô tả "đi đâu". Câu hỏi động học khi đó không còn đơn giản là tăng hay giảm, mà là: lượng này đang rời khỏi đâu, chảy vào đâu, và tổng cộng của toàn hệ có được bảo toàn hay không.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng một hệ thống nhiều bể nối với nhau bằng ống. Mỗi bể chứa một lượng chất nào đó. Mức chất trong từng bể thay đổi vì có dòng chảy vào và chảy ra. Viết phương trình cho từng bể chính là viết phương trình cho từng ngăn.

### Cách nhìn hình ảnh

Một sơ đồ ngăn với các mũi tên giữa các khoang thường còn quan trọng hơn công thức lúc đầu. Mỗi mũi tên mang một tốc độ chuyển dòng, và từ sơ đồ đó ta có thể đọc ngay dấu của từng số hạng trong hệ.

### Cách nhìn hình thức

Trong mô hình hai ngăn tuyến tính, ta có thể viết
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2+u_1(t),
$$
$$ \frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2+u_2(t). $$
Mỗi hạng âm biểu diễn dòng rời khỏi ngăn, mỗi hạng dương biểu diễn dòng đi vào ngăn. Tổng của hệ nhiều khi có cấu trúc bảo toàn hoặc suy giảm đơn giản.

## Những ngộ nhận thường gặp

- "Mô hình ngăn chỉ là bài toán cộng trừ lưu lượng." Sai. Nó còn chứa động học tương tác giữa các khoang.
- "Nếu mỗi phương trình nhìn đơn giản thì hệ cũng đơn giản." Không nhất thiết; tương tác giữa các ngăn có thể tạo hành vi rất phong phú.
- "Tổng lượng luôn được bảo toàn." Sai. Còn phụ thuộc có dòng ra ngoài hệ hay không.
- "Mọi mô hình ngăn đều tuyến tính." Không đúng. Nhiều mô hình quan trọng như SIR là phi tuyến.

## Tiến trình học tập đề xuất

### Bước 1: Vẽ sơ đồ các ngăn và mũi tên chuyển dòng

Đây là bước mô hình hóa quan trọng nhất.

### Bước 2: Viết cân bằng vào-trừ-ra cho từng ngăn

Mỗi phương trình phải có nghĩa vật lý rõ ràng.

### Bước 3: Kiểm tra tổng lượng

Xem hệ bảo toàn, hao hụt hay có bơm thêm từ ngoài.

### Bước 4: Phân tích động học

Hỏi trạng thái dài hạn, tốc độ trao đổi và ý nghĩa tham số.

### Các checkpoint

- Sinh viên có đặt dấu đúng cho các dòng vào và ra hay không.
- Sinh viên có kiểm tra được tổng lượng của hệ hay không.
- Sinh viên có phân biệt được ngăn và dòng giữa ngăn với nguồn ngoài hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Mô hình hai ngăn thuốc

Cho
$$ \frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2, $$
$$ \frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2. $$
Ở đây $$ x_1 $$ có thể là lượng thuốc trong huyết tương, $$ x_2 $$ là lượng thuốc trong mô. Hệ số $$ k_{01} $$ là tốc độ thải khỏi cơ thể. Từ mô hình này, sinh viên có thể đọc ngay: thuốc rời ngăn 1 vì hai con đường, nhưng chỉ quay lại từ ngăn 2 theo một đường.

### Ví dụ 2: Kiểm tra bảo toàn tổng lượng

Với hệ trên,
$$ \frac{d}{dt}(x_1+x_2)= -k_{01}x_1. $$
Điều này cho thấy tổng thuốc trong hai ngăn không bảo toàn vì có thất thoát ra ngoài cơ thể. Đây là một bước giải thích mô hình cực kỳ quan trọng.

### Ví dụ 3: Mô hình SIR như hệ ngăn

Hệ
$$ \frac{dS}{dt}=-\beta SI, $$
$$ \frac{dI}{dt}=\beta SI-\gamma I, $$
$$ \frac{dR}{dt}=\gamma I $$
là mô hình ngăn không tuyến tính. Dù không còn tuyến tính, trực giác ngăn vẫn giữ nguyên: người rời ngăn nhạy cảm để sang ngăn nhiễm, rồi từ đó sang ngăn hồi phục.

### Ví dụ 4: Ý nghĩa của ma trận hệ

Trong mô hình ngăn tuyến tính, ma trận hệ thường có các phần tử ngoài đường chéo không âm vì đó là dòng đi vào từ ngăn khác, còn đường chéo thường âm vì phản ánh mất mát khỏi chính ngăn đó. Đây là một đặc điểm cấu trúc đáng để sinh viên ghi nhớ.

## Câu hỏi khái niệm

1. Vì sao sơ đồ ngăn thường là bước quan trọng hơn cả việc giải hệ?
2. Tổng lượng của hệ cho ta biết điều gì về bảo toàn hoặc thất thoát?
3. Vì sao mô hình SIR dù phi tuyến vẫn là một mô hình ngăn điển hình?

## Bài toán ứng dụng

1. Trong dược động học, vì sao mô hình hai ngăn thường tốt hơn mô hình một ngăn đơn giản?
2. Trong môi trường học, chất ô nhiễm di chuyển giữa sông, hồ và đất. Hãy giải thích vì sao mô hình ngăn là ngôn ngữ phù hợp.
3. Trong dịch tễ, việc nhìn quần thể như các ngăn giúp ích gì cho việc thiết kế chính sách can thiệp?

## Chiến lược giảng dạy tương tác

- Cho sinh viên bắt đầu từ sơ đồ ngăn rồi mới viết hệ, thay vì ngược lại.
- Tổ chức hoạt động "đọc dấu": nhìn mũi tên và dự đoán số hạng nào dương, số hạng nào âm.
- Hỏi lớp: "Tổng lượng của hệ có được bảo toàn không, và làm sao biết?"
- Dùng ví dụ từ y học hoặc dịch tễ để làm hệ phương trình trở nên gần với thực tế hơn.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu làm các mô hình hai ngăn đơn giản trước, với bảng rõ ràng gồm ba cột: ngăn, dòng vào, dòng ra. Việc điền bảng trước khi viết phương trình thường rất hiệu quả.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi phân tích ổn định của một mô hình ngăn tuyến tính, hoặc so sánh phiên bản tuyến tính và phi tuyến của cùng một quá trình trao đổi.

## Tóm tắt dễ nhớ

Mô hình ngăn là bài toán hệ phương trình của dòng chuyển. Mỗi ngăn theo dõi "bao nhiêu", còn mũi tên theo dõi "đi đâu". Cốt lõi của bài là viết đúng cân bằng vào-trừ-ra và kiểm tra tổng lượng của toàn hệ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dược động học hai ngăn
- Bài toán: Thuốc di chuyển giữa huyết tương và mô, đồng thời có thể bị thải ra ngoài.
- Mô hình:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2.
$$
- Giả thiết và giới hạn: Hệ tuyến tính, tốc độ chuyển theo bậc một.
- Diễn giải: Hệ phương trình là ngôn ngữ tự nhiên vì từng ngăn chỉ kể một phần của dòng chuyển tổng thể.

#### Chất ô nhiễm giữa nhiều khoang
- Bài toán: Chất di chuyển giữa sông, hồ, đất và khí quyển.
- Mô hình: Hệ ngăn tuyến tính hay gần tuyến tính.
- Giả thiết và giới hạn: Tốc độ chuyển ổn định và mô hình trộn đều trong từng khoang.
- Diễn giải: Ma trận hệ nói cho ta ngay khoang nào mất chất, khoang nào nhận chất.

#### SIR như mô hình ngăn phi tuyến
- Bài toán: Người đi từ ngăn nhạy cảm sang nhiễm rồi hồi phục.
- Mô hình:
$$
\frac{dS}{dt}=-\beta SI,\qquad
\frac{dI}{dt}=\beta SI-\gamma I,\qquad
\frac{dR}{dt}=\gamma I.
$$
- Giả thiết và giới hạn: Đồng nhất hóa quần thể và tiếp xúc trộn đều.
- Diễn giải: Dù phi tuyến, trực giác ngăn vẫn là nền tảng.

### 2. Trực giác bổ sung và các kết nối

Mô hình ngăn cho thấy hệ phương trình không chỉ dành cho dao động hay cơ học. Đây là ngôn ngữ của dòng chuyển, bảo toàn, thất thoát và tích lũy. Bài này cũng là cầu nối rất tốt sang mô hình hóa trong sinh học, môi trường và y học, nơi ý nghĩa của dấu và đơn vị còn quan trọng hơn cả kỹ thuật giải.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, X):
    x1, x2 = X
    k12, k21, k01 = 0.4, 0.2, 0.1
    dx1 = -(k12 + k01) * x1 + k21 * x2
    dx2 = k12 * x1 - k21 * x2
    return [dx1, dx2]

t = np.linspace(0, 20, 500)
sol = solve_ivp(system, [0, 20], [10, 0], t_eval=t)

plt.plot(sol.t, sol.y[0], label="Ngăn 1")
plt.plot(sol.t, sol.y[1], label="Ngăn 2")
plt.plot(sol.t, sol.y[0] + sol.y[1], label="Tổng", linestyle="--")
plt.xlabel("t")
plt.ylabel("Lượng")
plt.title("Mô hình ngăn hai khoang")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: compartment model pharmacokinetics visualization
- search: two compartment model simulation
- search: SIR compartment diagram animation

### 5. Bài toán mẫu có bối cảnh thực

Cho mô hình hai ngăn:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2.
$$
Tổng lượng thuốc thỏa
$$ \frac{d}{dt}(x_1+x_2)=-k_{01}x_1. $$
Điều này cho thấy tổng lượng không được bảo toàn vì ngăn 1 có dòng thải ra ngoài cơ thể. Đây là một ví dụ rất mạnh để sinh viên thấy việc cộng các phương trình có thể cho thông tin mô hình hóa rất quý.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào việc vẽ sơ đồ ngăn, viết đúng dấu và kiểm tra tổng lượng của hệ.

**Bậc sau đại học.** So sánh mô hình ngăn tuyến tính và phi tuyến, phân tích ổn định và ý nghĩa sinh học của từng tham số.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: nhiều ứng dụng tốt về mô hình ngăn và hệ tuyến tính.
- Arnold, *Ordinary Differential Equations*: hữu ích cho trực giác về dòng chuyển và hệ động lực nhiều biến.
