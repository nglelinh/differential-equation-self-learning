---
layout: post
title: "05-10 Ứng dụng: Dịch tễ học SIR"
chapter: '05'
order: 10
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: optional
---

## Mục tiêu

Bài học này giúp sinh viên phân tích mô hình SIR như một hệ phi tuyến ba ngăn, hiểu ngưỡng bùng phát $$ \mathcal{R}_0 $$, đọc ý nghĩa của miễn dịch cộng đồng và thấy vì sao hệ phương trình vi phân là ngôn ngữ tự nhiên để mô tả dịch tễ học cơ bản.

## Kiến thức nền

Sinh viên cần nắm mô hình ngăn, hệ phi tuyến và trực giác về tốc độ lây lan, hồi phục. Đây là bài kết nối đẹp giữa hệ phương trình và một ứng dụng xã hội có ý nghĩa rất rõ ràng.

## Dẫn nhập

![Mô hình dịch tễ SIR và dòng chuyển giữa các ngăn]({{ site.imgurl }}/chapter_img/chapter05/10_sir_epidemiology.svg)

Dịch bệnh không chỉ là danh sách số ca theo thời gian. Nó là một quá trình chuyển dịch dân số giữa các trạng thái: dễ nhiễm, đang nhiễm, và hồi phục hoặc miễn dịch. Một mô hình đủ đơn giản nhưng vẫn giữ được cấu trúc cốt lõi của quá trình đó là SIR.

Mô hình SIR quan trọng vì nó cho sinh viên thấy một hệ phương trình không chỉ giải thích xu hướng tăng giảm số ca, mà còn làm lộ ra khái niệm ngưỡng. Dịch không bùng phát chỉ vì "có người bệnh", mà vì tốc độ lây đủ mạnh so với tốc độ rời khỏi ngăn nhiễm. Từ đó nảy sinh khái niệm số sinh sản cơ bản và miễn dịch cộng đồng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng dân số được chia thành ba bể: một bể người nhạy cảm, một bể người đang lây và một bể người đã rời khỏi vòng lây. Dòng chảy từ bể nhạy cảm sang bể nhiễm phụ thuộc vào việc hai nhóm tiếp xúc, còn dòng chảy từ bể nhiễm sang bể hồi phục phụ thuộc vào tốc độ khỏi bệnh.

### Cách nhìn hình ảnh

Đồ thị của $$ S(t), I(t), R(t) $$ thường cho thấy: $$ S $$ giảm dần, $$ I $$ tăng rồi đạt đỉnh rồi giảm, $$ R $$ tăng dần. Ý nghĩa động học lớn nhất không chỉ là đỉnh dịch nằm ở đâu, mà là khi nào $$ I $$ bắt đầu giảm, tức là khi quần thể nhạy cảm bị kéo xuống dưới ngưỡng lây duy trì.

### Cách nhìn hình thức

Mô hình SIR cơ bản là
$$ \frac{dS}{dt}=-\beta SI, $$
$$ \frac{dI}{dt}=\beta SI-\gamma I, $$
$$ \frac{dR}{dt}=\gamma I. $$
Ta có bảo toàn tổng dân số:
$$ \frac{d}{dt}(S+I+R)=0. $$
Nếu dùng chuẩn hóa phù hợp, ngưỡng bùng phát ban đầu được đọc từ
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}. $$
Nếu $$ \mathcal{R}_0>1 $$ thì số người nhiễm tăng lúc đầu; nếu $$ \mathcal{R}_0<1 $$ thì dịch có xu hướng tắt.

## Những ngộ nhận thường gặp

- "Nếu có ca nhiễm thì dịch chắc chắn bùng phát." Sai. Còn phụ thuộc ngưỡng lây.
- "Miễn dịch cộng đồng nghĩa là hết người mắc bệnh." Sai. Nó là ngưỡng khiến dịch không còn tự duy trì tăng.
- "Mô hình SIR quá đơn giản nên vô dụng." Sai. Nó vẫn cực kỳ hữu ích để xây trực giác về ngưỡng và dòng chuyển.
- "Chỉ cần nhìn số ca hiện tại là biết dịch sẽ đi đâu." Không đúng. Cần nhìn cả số người nhạy cảm còn lại và tốc độ hồi phục.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu từng ngăn và dòng chuyển

Giải thích từng số hạng bằng lời.

### Bước 2: Kiểm tra bảo toàn tổng

Đây là bước cấu trúc đầu tiên cần làm.

### Bước 3: Phân tích điều kiện tăng ban đầu của $$ I $$

Từ đây ngưỡng $$ \mathcal{R}_0 $$ xuất hiện tự nhiên.

### Bước 4: Diễn giải miễn dịch cộng đồng

Kết nối ngôn ngữ toán với chính sách công.

### Các checkpoint

- Sinh viên có diễn giải được ý nghĩa của $$ \beta SI $$ và $$ \gamma I $$ hay không.
- Sinh viên có hiểu vì sao $$ S+I+R $$ được bảo toàn không.
- Sinh viên có phân biệt được ngưỡng bùng phát với đỉnh dịch không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bảo toàn tổng dân số

Cộng ba phương trình:
$$
\frac{dS}{dt}+\frac{dI}{dt}+\frac{dR}{dt}
=-\beta SI+\beta SI-\gamma I+\gamma I=0.
$$
Vậy
$$ S(t)+I(t)+R(t)=N $$
là hằng số. Đây là cấu trúc nền tảng của mô hình.

### Ví dụ 2: Điều kiện bùng phát ban đầu

Ta có
$$ \frac{dI}{dt}=I(\beta S-\gamma). $$
Vì vậy $$ I $$ tăng ban đầu nếu
$$ \beta S(0)-\gamma>0, $$
tức là
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}>1. $$
Đây là cách ngưỡng dịch xuất hiện cực kỳ tự nhiên từ chính phương trình.

### Ví dụ 3: Miễn dịch cộng đồng

Khi $$ S(t) $$ giảm xuống đủ nhỏ để
$$ \beta S(t)<\gamma, $$
thì
$$ \frac{dI}{dt}<0. $$
Nghĩa là từ thời điểm đó trở đi, số ca nhiễm bắt đầu giảm. Đây là nội dung động lực học của miễn dịch cộng đồng.

### Ví dụ 4: Giới hạn của mô hình

SIR cơ bản bỏ qua thời kỳ ủ bệnh, cấu trúc tuổi, dị biệt tiếp xúc, tái nhiễm và nhiều yếu tố khác. Tuy nhiên, bài học ở đây không phải "mô hình này đủ cho mọi dịch", mà là "mô hình này cho ta ngôn ngữ cơ bản để suy nghĩ về lây lan".

## Câu hỏi khái niệm

1. Vì sao ngưỡng $$ \mathcal{R}_0 $$ quan trọng hơn việc chỉ nhìn số ca hiện tại?
2. Miễn dịch cộng đồng là khái niệm động lực học theo nghĩa nào?
3. Vì sao bảo toàn tổng dân số là một kiểm tra cấu trúc rất quan trọng của mô hình?

## Bài toán ứng dụng

1. Một chính sách tiêm chủng làm giảm số người nhạy cảm. Hãy giải thích điều này tác động lên ngưỡng bùng phát như thế nào.
2. Nếu tốc độ hồi phục $$ \gamma $$ tăng nhờ điều trị tốt hơn, quỹ đạo dịch thay đổi theo hướng nào?
3. Trong một quần thể tiếp xúc không đồng đều, vì sao SIR cơ bản vừa hữu ích vừa có giới hạn?

## Chiến lược giảng dạy tương tác

- Cho sinh viên diễn giải từng số hạng của hệ bằng ngôn ngữ dân số trước khi làm tính.
- Hỏi lớp: "Muốn dịch giảm, cần kéo đại lượng nào xuống dưới đại lượng nào?"
- Dùng sơ đồ ngăn như một hoạt động nhóm để liên hệ với chương mô hình ngăn trước đó.
- Khuyến khích sinh viên bàn luận sự khác nhau giữa "có dịch" và "dịch bùng phát".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu bám vào ba bước: đọc dòng chuyển, kiểm tra bảo toàn tổng, rồi phân tích dấu của $$ I' $$. Chỉ ba bước này đã cho gần như toàn bộ trực giác chính của bài.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi giảm hệ về hai biến bằng bảo toàn tổng, hoặc so sánh SIR với các mở rộng như SEIR hay mô hình có sinh-tử.

## Tóm tắt dễ nhớ

SIR là mô hình ngăn phi tuyến cho dịch tễ học. Tổng dân số được bảo toàn, còn ngưỡng bùng phát xuất hiện từ dấu của $$ I' $$. Muốn hiểu dịch, đừng chỉ nhìn số ca hiện tại; hãy nhìn dòng chuyển giữa các ngăn và ngưỡng $$ \mathcal{R}_0 $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dịch cúm trong cộng đồng
- Bài toán: Muốn biết khi nào số ca nhiễm tăng và khi nào dịch bắt đầu giảm.
- Mô hình:
$$
\dot{S}=-\beta SI,\qquad
\dot{I}=\beta SI-\gamma I,\qquad
\dot{R}=\gamma I.
$$
- Giả thiết và giới hạn: Trộn đều dân số, không có cấu trúc tuổi, không có sinh-tử hay mùa vụ.
- Diễn giải: Điều kiện đầu và tham số quyết định liệu số người nhiễm tăng lúc đầu hay tắt dần.

#### Virus máy tính như mô hình ngăn
- Bài toán: Máy tính dễ bị nhiễm, đang nhiễm và đã vá có thể được xem như ba ngăn.
- Mô hình: Dùng cấu trúc SIR với tham số lây lan và vá lỗi.
- Giả thiết và giới hạn: Đây là ẩn dụ kỹ thuật; mạng thật không trộn đều.
- Diễn giải: Ngưỡng kiểu $$ \mathcal{R}_0 $$ vẫn cho trực giác về khả năng bùng phát.

### 2. Trực giác bổ sung và các kết nối

SIR là mô hình ngăn phi tuyến quan trọng nhất của chương. Ngưỡng $$ \mathcal{R}_0 $$ nói về xu hướng tăng ban đầu của dịch, không phải trực tiếp là kích thước cuối cùng của dịch. Một nhầm lẫn phổ biến là đồng nhất miễn dịch cộng đồng với việc không còn ca bệnh; thực ra đó là ngưỡng khiến dịch không thể tự duy trì tăng trưởng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

beta, gamma = 0.6, 0.2

def sir(t, z):
    S, I, R = z
    return [-beta * S * I, beta * S * I - gamma * I, gamma * I]

t = np.linspace(0, 80, 1000)
sol = solve_ivp(sir, [0, 80], [0.99, 0.01, 0.0], t_eval=t)

plt.plot(t, sol.y[0], label="S")
plt.plot(t, sol.y[1], label="I")
plt.plot(t, sol.y[2], label="R")
plt.xlabel("t")
plt.ylabel("fraction")
plt.title("Dong hoc cua mo hinh SIR")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: SIR model interactive simulation
- search: basic reproduction number visualization
- search: herd immunity threshold SIR

### 5. Bài toán mẫu có bối cảnh thực

Ta có
$$ \dot{I}=I(\beta S-\gamma). $$
Vì vậy nếu ban đầu
$$ \beta S(0)>\gamma, $$
thì số ca nhiễm tăng. Nếu chuẩn hóa tổng dân số bằng $$ 1 $$, ngưỡng ban đầu là
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}. $$
Từ đây sinh viên thấy ngưỡng bùng phát xuất hiện trực tiếp từ phương trình.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu dòng chuyển giữa các ngăn, bảo toàn tổng dân số và điều kiện dịch tăng ban đầu.

**Bậc sau đại học.** Mở rộng sang SEIR, mô hình có tiêm chủng, ma trận thế hệ kế tiếp và ổn định của cân bằng không bệnh.

## Tài liệu tham khảo

- Strogatz, Chương 6: rất tốt cho trực giác ngưỡng dịch và mặt phẳng pha của mô hình dân số.
- Arnold, Chương 4-5: hữu ích khi đặt mô hình SIR trong ngôn ngữ hệ động lực.
