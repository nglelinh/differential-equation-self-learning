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

Khi một loại virus mới xuất hiện trong thành phố 1 triệu dân, làm sao các nhà dịch tễ học dự báo được đỉnh dịch sẽ rơi vào tuần nào, bao nhiêu phần trăm dân số cần tiêm vaccine để đạt **miễn dịch cộng đồng**, và việc đeo khẩu trang giảm 30% tiếp xúc sẽ làm phẳng đường cong đến đâu? Câu trả lời nằm trong hệ 3 phương trình vi phân phi tuyến kinh điển của Kermack và McKendrick (1927): **Mô hình SIR**.

## Kiến thức cần nhớ: Bốn trụ cột toán học của Mô hình Dịch tễ SIR

1. **Ba ngăn bảo toàn dân số ($S + I + R = N$)**:
   $S(t)$: người nhạy cảm (Susceptible); $I(t)$: người đang nhiễm bệnh (Infected); $R(t)$: người đã hồi phục/miễn dịch (Recovered). Vì $\dot{S} + \dot{I} + \dot{R} = 0$, tổng dân số $N$ là một bất biến.
2. **Hệ phương trình $\dot{S} = -\frac{\beta}{N}SI,\; \dot{I} = \frac{\beta}{N}SI - \gamma I,\; \dot{R} = \gamma I$**:
   $\beta$ là tốc độ lây truyền trung bình/ngày; $\gamma$ là tốc độ hồi phục ($1/\gamma$ là thời gian nhiễm bệnh trung bình tính theo ngày).
3. **Hệ số lây nhiễm cơ bản $R_0 = \beta / \gamma$**:
   Số ca nhiễm thứ cấp trung bình do 1 ca bệnh gây ra trong quần thể hoàn toàn nhạy cảm ($S_0 \approx N$). Dịch bùng phát khi và chỉ khi $\dot{I}(0) > 0 \iff R_0 \frac{S_0}{N} > 1$!
4. **Ngưỡng miễn dịch cộng đồng ($p_c = 1 - 1/R_0$)**:
   Nếu tiêm vaccine cho tỷ lệ $p > 1 - 1/R_0$ dân số để kéo $S_0/N < 1/R_0$, thì ngay lập tức $\dot{I}(0) < 0$—dịch tự tắt mà không cần tiêm 100% dân số!

## Mục tiêu

Bài học này giúp sinh viên phân tích mô hình SIR như một hệ phương trình phi tuyến ba ngăn, hiểu ý nghĩa ngưỡng bùng phát $$ \mathcal{R}_0 $$, diễn giải khái niệm miễn dịch cộng đồng và thấy được vì sao hệ phương trình vi phân là công cụ tự nhiên để mô tả dịch tễ học cơ bản.

## Kiến thức nền

Sinh viên cần nắm vững mô hình ngăn, hệ phi tuyến và trực giác về tốc độ lây nhiễm, tốc độ hồi phục. Bài học kết nối các công cụ toán học của chương với một ứng dụng xã hội cụ thể và trực quan.

## Dẫn nhập

![Mô hình dịch tễ SIR và dòng chuyển giữa các ngăn]({{ site.imgurl }}/chapter_img/chapter05/10_sir_epidemiology.svg)

Một đợt dịch không chỉ là chuỗi số liệu ca mắc theo thời gian, mà là quá trình chuyển dịch dân số giữa các trạng thái: dễ nhiễm (Susceptible), đang nhiễm (Infectious) và hồi phục hoặc miễn dịch (Recovered). Mô hình SIR giữ lại cấu trúc cốt lõi của quá trình chuyển dịch này dưới dạng một hệ phương trình tương đối gọn.

Giá trị lớn của mô hình SIR nằm ở chỗ nó không chỉ mô tả xu hướng tăng giảm của số ca mắc mà còn làm rõ khái niệm **ngưỡng bùng phát**. Dịch không tự bùng lên chỉ vì xuất hiện ca bệnh, mà phụ thuộc vào tỷ lệ giữa tốc độ lây truyền và tốc độ rời khỏi nhóm đang nhiễm. Từ đó xuất hiện hai khái niệm trung tâm: số sinh sản cơ bản và ngưỡng miễn dịch cộng đồng.

### Giải thích: Tính tay $R_0$, ngưỡng miễn dịch cộng đồng và đỉnh dịch cho một đợt cúm cụ thể

Giả sử một thành phố có $N = 100.000$ người, tốc độ lây $\beta = 0{,}4\text{ ngày}^{-1}$ và thời gian khỏi bệnh trung bình $1/\gamma = 10\text{ ngày}$ ($\gamma = 0{,}1\text{ ngày}^{-1}$).

1. **Tính hệ số lây nhiễm cơ bản**:
   $$R_0 = \frac{\beta}{\gamma} = \frac{0{,}4}{0{,}1} = \mathbf{4{,}0}.$$
2. **Tính ngưỡng miễn dịch cộng đồng**:
   $$p_c = 1 - \frac{1}{R_0} = 1 - \frac{1}{4} = 0{,}75 = \mathbf{75\%} \quad (75.000\text{ người cần có miễn dịch}).$$
3. **Xác định chính xác thời điểm ĐỈNH DỊCH ($I_{\max}$)**:
   Tại đỉnh dịch, $\dot{I} = \left(\frac{\beta}{N} S - \gamma\right) I = 0 \implies S_{\text{đỉnh}} = \frac{\gamma}{\beta} N = \frac{N}{R_0} = \mathbf{25.000\text{ người}}$.
   *(Nghĩa là dịch chỉ bắt đầu giảm khi đã có $75\%$ dân số rời khỏi nhóm $S$!)*
4. **Tính chính xác chiều cao đỉnh dịch** bằng tích phân bất biến $I + S - \frac{N}{R_0}\ln S = \text{hằng số}$ (khởi đầu $S_0 \approx N, I_0 \approx 0$):
   $$\frac{I_{\max}}{N} = 1 - \frac{1}{R_0} - \frac{\ln R_0}{R_0} = 1 - 0{,}25 - \frac{1{,}386}{4} \approx \mathbf{0{,}403} \quad (\approx \mathbf{40.300\text{ ca nhiễm cùng lúc!}}).$$
   Nếu giãn cách giảm $\beta$ một nửa ($R_0 = 2{,}0$), đỉnh dịch sụt xuống chỉ còn $1 - 0{,}5 - \frac{0{,}693}{2} \approx \mathbf{15{,}3\%}$ ($15.300$ ca)—giảm gần **$3\times$ áp lực giường bệnh**!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung dân số được chia thành ba ngăn: nhóm dễ nhiễm, nhóm đang mang mầm bệnh và nhóm đã rời khỏi chuỗi lây truyền. Dòng chuyển từ nhóm dễ nhiễm sang nhóm đang nhiễm phụ thuộc vào mức độ tiếp xúc giữa hai nhóm, còn dòng chuyển sang nhóm hồi phục phụ thuộc vào tốc độ khỏi bệnh.

### Cách nhìn hình ảnh

Đồ thị theo thời gian của $$ S(t), I(t), R(t) $$ thường cho thấy $$ S $$ giảm đơn điệu, $$ I $$ tăng lên đạt đỉnh rồi suy giảm, còn $$ R $$ tăng dần. Điểm mấu chốt về mặt động lực học không chỉ là vị trí đỉnh dịch mà là thời điểm $$ I $$ bắt đầu giảm — tức là khi số người dễ nhiễm giảm xuống dưới ngưỡng đủ để duy trì sự lây lan.

### Cách nhìn hình thức

Mô hình SIR cơ bản được viết dưới dạng:
$$ \frac{dS}{dt}=-\beta SI, $$
$$ \frac{dI}{dt}=\beta SI-\gamma I, $$
$$ \frac{dR}{dt}=\gamma I. $$
Tổng dân số được bảo toàn theo thời gian:
$$ \frac{d}{dt}(S+I+R)=0. $$
Với cách chuẩn hóa phù hợp, ngưỡng bùng phát ban đầu được xác định bởi số sinh sản cơ bản:
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}. $$
Nếu $$ \mathcal{R}_0>1 $$, số ca nhiễm tăng lên ngay từ đầu; nếu $$ \mathcal{R}_0<1 $$, dịch có xu hướng tự tắt dần.

## Những ngộ nhận thường gặp

- "Cứ có ca nhiễm là dịch chắc chắn bùng phát." Sai. Khả năng bùng phát phụ thuộc vào việc $$ \mathcal{R}_0 $$ lớn hơn hay nhỏ hơn 1.
- "Đạt miễn dịch cộng đồng nghĩa là không còn ai mắc bệnh." Sai. Đó là ngưỡng mà từ đó số ca đang nhiễm không còn tự duy trì đà tăng và bắt đầu giảm.
- "Mô hình SIR quá đơn giản nên không hữu ích." Sai. Nó cung cấp trực giác nền tảng và rõ ràng về ngưỡng dịch cũng như dòng chuyển trạng thái.
- "Chỉ cần nhìn số ca mắc hiện tại là dự đoán được xu hướng dịch." Không đúng. Cần xét đồng thời số người dễ nhiễm còn lại và tốc độ hồi phục.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu từng ngăn và dòng chuyển

Diễn giải ý nghĩa thực tế của từng biến trạng thái và từng số hạng trong hệ phương trình.

### Bước 2: Kiểm tra định luật bảo toàn tổng dân số

Cộng ba phương trình để kiểm chứng tính bảo toàn cấu trúc của mô hình.

### Bước 3: Phân tích điều kiện tăng ban đầu của $$ I $$

Xét dấu của $$ \frac{dI}{dt} $$ tại $$ t=0 $$ để suy ra ngưỡng $$ \mathcal{R}_0 $$.

### Bước 4: Diễn giải ngưỡng miễn dịch cộng đồng

Liên hệ kết quả toán học với các biện pháp y tế công cộng như tiêm chủng.

### Các điểm kiểm tra

- Sinh viên có giải thích được ý nghĩa của các số hạng $$ \beta SI $$ và $$ \gamma I $$ hay không.
- Sinh viên có chứng minh được tổng $$ S+I+R $$ là hằng số hay không.
- Sinh viên có phân biệt được ngưỡng bùng phát với thời điểm đạt đỉnh dịch hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bảo toàn tổng dân số

Cộng vế theo vế ba phương trình của hệ:
$$
\frac{dS}{dt}+\frac{dI}{dt}+\frac{dR}{dt}
=-\beta SI+\beta SI-\gamma I+\gamma I=0.
$$
Suy ra
$$ S(t)+I(t)+R(t)=N $$
là hằng số không đổi theo thời gian. Đây là tính chất cấu trúc cơ bản của mô hình SIR đóng.

### Ví dụ 2: Điều kiện bùng phát ban đầu

Viết lại phương trình thứ hai dưới dạng:
$$ \frac{dI}{dt}=I(\beta S-\gamma). $$
Do đó $$ I(t) $$ tăng tại thời điểm ban đầu khi và chỉ khi
$$ \beta S(0)-\gamma>0, $$
tương đương với
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}>1. $$
Như vậy, ngưỡng bùng phát xuất hiện trực tiếp từ cấu trúc đại số của phương trình.

### Ví dụ 3: Miễn dịch cộng đồng

Khi $$ S(t) $$ giảm xuống dưới ngưỡng thỏa mãn
$$ \beta S(t)<\gamma, $$
ta có
$$ \frac{dI}{dt}<0. $$
Từ thời điểm này trở đi, số ca đang nhiễm suy giảm dần. Đây chính là cơ sở động lực học của khái niệm miễn dịch cộng đồng.

### Ví dụ 4: Giới hạn của mô hình

Mô hình SIR cơ bản chưa xét đến thời kỳ ủ bệnh, cấu trúc độ tuổi, sự không đồng nhất trong tiếp xúc, khả năng tái nhiễm hay biến động sinh–tử. Tuy vậy, mục tiêu của mô hình không phải là thay thế mọi mô hình dịch tễ phức tạp, mà là cung cấp ngôn ngữ toán học nền tảng để phân tích cơ chế lây truyền.

## Câu hỏi khái niệm

1. Vì sao ngưỡng $$ \mathcal{R}_0 $$ mang lại nhiều thông tin hơn việc chỉ theo dõi số ca mắc hiện tại?
2. Miễn dịch cộng đồng được hiểu như thế nào dưới góc độ động lực học?
3. Vì sao kiểm tra bảo toàn tổng dân số là bước kiểm chứng cấu trúc quan trọng của mô hình?

## Bài toán ứng dụng

1. Một chiến dịch tiêm chủng làm giảm số người thuộc ngăn dễ nhiễm $$ S(0) $$. Hãy giải thích tác động của biện pháp này lên ngưỡng bùng phát.
2. Nếu tốc độ hồi phục $$ \gamma $$ tăng lên nhờ cải thiện điều trị, diễn biến đường cong dịch thay đổi theo hướng nào?
3. Trong một cộng đồng có mức độ tiếp xúc không đồng đều, mô hình SIR cơ bản có những điểm hữu ích và hạn chế nào?

## Chiến lược giảng dạy tương tác

- Cho sinh viên giải thích ý nghĩa từng số hạng của hệ bằng ngôn ngữ dân số trước khi biến đổi toán học.
- Đặt câu hỏi cho lớp: để số ca nhiễm giảm xuống, cần đưa đại lượng nào xuống dưới đại lượng nào?
- Sử dụng sơ đồ ngăn theo nhóm để kết nối với các bài học mô hình ngăn ở chương trước.
- Tổ chức thảo luận về sự khác nhau giữa việc "có ca bệnh" và "dịch bùng phát".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên hướng dẫn sinh viên bám sát ba bước chính: đọc dòng chuyển giữa các ngăn, kiểm tra bảo toàn tổng dân số và xét dấu của $$ I' $$. Ba bước này đã bao quát phần lớn trực giác cốt lõi của bài học.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khử một biến nhờ định luật bảo toàn tổng dân số để đưa về hệ hai chiều trên mặt phẳng pha $$(S, I)$$, hoặc so sánh SIR với các mô hình mở rộng như SEIR hay mô hình có sinh–tử.

## Tóm tắt dễ nhớ

SIR là mô hình ngăn phi tuyến cơ bản trong dịch tễ học: tổng dân số được bảo toàn, và ngưỡng bùng phát được suy ra trực tiếp từ dấu của $$ I' $$. Để đánh giá xu hướng dịch bệnh, cần xem xét dòng chuyển giữa các ngăn và ngưỡng $$ \mathcal{R}_0 $$ thay vì chỉ nhìn số ca mắc tại một thời điểm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dịch cúm trong cộng đồng
- Bài toán: Xác định điều kiện để số ca nhiễm tăng lên và thời điểm dịch bắt đầu suy giảm.
- Mô hình:
$$
\dot{S}=-\beta SI,\qquad
\dot{I}=\beta SI-\gamma I,\qquad
\dot{R}=\gamma I.
$$
- Giả thiết và giới hạn: Dân số tiếp xúc đồng đều, không phân tầng độ tuổi, không tính sinh–tử hay yếu tố mùa vụ.
- Diễn giải: Điều kiện ban đầu và các tham số lây truyền, hồi phục quyết định dịch sẽ bùng phát hay tắt dần.

#### Lan truyền phần mềm độc hại theo mô hình ngăn
- Bài toán: Các máy tính trong mạng có thể được phân loại thành ba ngăn: dễ bị nhiễm, đang nhiễm và đã vá lỗi.
- Mô hình: Áp dụng cấu trúc SIR với tham số tốc độ lây lan và tốc độ vá lỗi.
- Giả thiết và giới hạn: Đây là mô hình tương tự hóa; mạng máy tính thực tế có cấu trúc đồ thị không đồng đều.
- Diễn giải: Ngưỡng dạng $$ \mathcal{R}_0 $$ vẫn giúp ước lượng khả năng lan rộng của mã độc.

### 2. Trực giác bổ sung và các kết nối

SIR là một trong những mô hình ngăn phi tuyến quan trọng nhất của chương. Cần lưu ý rằng $$ \mathcal{R}_0 $$ cho biết xu hướng tăng hay giảm ban đầu của dịch chứ không trực tiếp bằng tổng quy mô dịch cuối cùng. Tương tự, miễn dịch cộng đồng không có nghĩa là hết sạch ca bệnh mà là ngưỡng khiến dịch không còn tự duy trì đà tăng.

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

Từ phương trình
$$ \dot{I}=I(\beta S-\gamma), $$
nếu tại thời điểm ban đầu ta có
$$ \beta S(0)>\gamma, $$
thì số ca đang nhiễm sẽ tăng. Khi chuẩn hóa tổng dân số bằng $$ 1 $$, ngưỡng ban đầu chính là
$$ \mathcal{R}_0=\frac{\beta S(0)}{\gamma}, $$
cho thấy khái niệm ngưỡng bùng phát xuất phát trực tiếp từ phương trình vi phân.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững dòng chuyển giữa các ngăn, định luật bảo toàn tổng dân số và điều kiện bùng phát ban đầu.

**Bậc sau đại học.** Mở rộng sang mô hình SEIR, mô hình có tiêm chủng, ma trận thế hệ kế tiếp và phân tích ổn định của điểm cân bằng không bệnh.

## Video tham khảo

- Xem trước: [The MATH of Pandemics | Intro to the SIR Model](https://www.youtube.com/watch?v=Qrp40ck3WpI) — Dr. Trefor Bazett, tiếng Anh. Xây dựng mô hình SIR và giải thích số sinh sản cơ bản.
- [Oxford Mathematician explains SIR Disease Model for COVID-19 (Coronavirus)](https://www.youtube.com/watch?v=NKMHhm2Zbkw) — Tom Rocks Maths, tiếng Anh. Tom Crawford phân tích hệ phương trình SIR trong bối cảnh dịch bệnh thực tế.
- [SIR Model for Epidemiology, Ordinary Differential Equations](https://www.youtube.com/watch?v=f1Ewm1hyPWY) — Dr. Bevin Maultsby, tiếng Anh. Bài giảng bám sát các phương trình vi phân của mô hình SIR.

## Tài liệu tham khảo

- Strogatz, Chương 6: trình bày trực giác về ngưỡng và mặt phẳng pha trong các mô hình quần thể.
- Arnold, Chương 4–5: hữu ích khi đặt mô hình SIR trong ngôn ngữ hệ động lực.
