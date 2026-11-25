---
layout: post
title: "01-08 Ứng dụng: Cơ học và Mạch điện"
chapter: '01'
order: 8
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Một vận động viên nhảy dù rơi qua không khí và một tụ điện đang nạp dòng trong mạch RC nhìn bề ngoài chẳng liên quan gì đến nhau—nhưng khi viết định luật Newton $F = ma$ và định luật Kirchhoff về điện áp, cả hai lại sinh ra **cùng một phương trình vi phân tuyến tính cấp một**! Đó chính là vẻ đẹp thống nhất của toán học ứng dụng: giải một phương trình, ta hiểu đồng thời cả cơ học lẫn điện học.

## Kiến thức cần nhớ: Bốn trụ cột Cơ học & Mạch điện Cấp Một

1. **Chuyển động có lực cản không khí ($m\frac{dv}{dt} = mg - kv$ hoặc $mg - kv^2$)**:
   Khi lực cản cân bằng trọng lực ($dv/dt = 0$), vật đạt **vận tốc giới hạn (terminal velocity)** $v_T = mg/k$ (cản tuyến tính) hoặc $v_T = \sqrt{mg/k}$ (cản bậc hai).
2. **Mạch điện RC ($R\frac{dq}{dt} + \frac{1}{C}q = E(t)$)**:
   Hằng số thời gian $\tau = RC$ quyết định tốc độ nạp/xả điện tích; sau thời gian $t = \tau$, tụ điện đã nạp được $1 - e^{-1} \approx 63{,}2\%$ giá trị cân bằng.
3. **Mạch điện RL ($L\frac{di}{dt} + R i = E(t)$)**:
   Cuộn cảm chống lại sự biến thiên đột ngột của dòng điện với hằng số thời gian $\tau = L/R$, tiến tiệm cận về dòng ổn định $I_\infty = E/R$.
4. **Phân tích Thứ nguyên & Không thứ nguyên hóa**:
   Kiểm tra đơn vị từng số hạng giúp phát hiện ngay lỗi thiết lập phương trình và lộ rõ các thang thời gian đặc trưng như $\tau = m/k$ hay $\tau = RC$.

## Mục tiêu
Bài học này giúp sinh viên thấy các định luật vật lý cơ bản dẫn trực tiếp đến phương trình vi phân cấp một. Thông qua bài toán vật rơi có lực cản, mạch RC và mạch RL, sinh viên học cách chuyển định luật Newton và định luật Kirchhoff thành ODE, giải nghiệm và diễn giải các đại lượng vật lý đặc trưng như vận tốc giới hạn, trạng thái xác lập và hằng số thời gian (thời hằng).

## Kiến thức nền
Sinh viên cần nắm vững phương trình tuyến tính cấp một cùng một số khái niệm vật lý cơ bản: lực, vận tốc, điện áp, điện tích và dòng điện. Không đòi hỏi kiến thức vật lý nâng cao; trọng tâm là hiểu cách các định luật cân bằng tạo nên phương trình vi phân.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-08 Ứng dụng: Cơ học và Mạch điện]({{ site.imgurl }}/chapter_img/chapter01/01_08_applications_mechanics_circuits.svg)

Khi thả một vật rơi trong không khí, vận tốc không tăng mãi mà tiệm cận một vận tốc giới hạn khi lực cản cân bằng với trọng lực. Khi nối tụ điện với nguồn điện một chiều, điện tích trên tụ tăng dần chứ không nhảy tức thời lên giá trị cực đại. Tương tự, khi đóng mạch RL, dòng điện trải qua giai đoạn quá độ trước khi ổn định. Các hiện tượng vật lý khác nhau này lại có chung một cấu trúc ODE tuyến tính cấp một.

Ưu điểm của nhóm bài toán cơ học và mạch điện là mỗi tham số đều mang ý nghĩa vật lý trực quan: hệ số nào tạo ra sự cản trở, tổ hợp tham số nào quyết định tốc độ đáp ứng và vì sao hệ tiến tới trạng thái ổn định.

### Giải thích: Tính vận tốc giới hạn và thời gian đạt 90% vận tốc giới hạn của vật rơi có cản tuyến tính

Xét vật khối lượng $m = 10\text{ kg}$ thả rơi tự do từ nghỉ ($v(0) = 0$) với $g = 9{,}8\text{ m/s}^2$ và hệ số cản $k = 2\text{ kg/s}$:
1. **Phương trình Newton**:
   $$10\frac{dv}{dt} = 10(9{,}8) - 2v \implies \frac{dv}{dt} + 0{,}2v = 9{,}8.$$
2. **Tìm ngay vận tốc giới hạn** (đặt $dv/dt = 0$):
   $$v_T = \frac{9{,}8}{0{,}2} = \mathbf{49\text{ m/s}}.$$
3. **Nghiệm tường minh**: Với $v(0) = 0$ và hằng số thời gian $\tau = m/k = 5\text{ s}$:
   $$v(t) = 49\big(1 - e^{-0{,}2 t}\big).$$
4. **Thời gian đạt $90\%$ vận tốc giới hạn** ($v(t) = 0{,}9 \times 49$):
   $$1 - e^{-0{,}2 t} = 0{,}9 \implies e^{-0{,}2 t} = 0{,}1 \implies t = \frac{\ln 10}{0{,}2} \approx \frac{2{,}3026}{0{,}2} \approx \mathbf{11{,}51\text{ giây}}.$$

## Khái niệm theo ba cách

### Cách nhìn trực quan
Trong bài toán vật rơi với lực cản tuyến tính, trọng lực kéo vận tốc tăng còn lực cản kéo ngược lại, làm vận tốc hội tụ về một mức cố định. Trong mạch RC và RL, nguồn điện thúc đẩy hệ tiến về trạng thái cân bằng còn điện trở và phần tử lưu trữ năng lượng (tụ điện hoặc cuộn cảm) quyết định tốc độ đáp ứng của quá trình quá độ.

### Cách nhìn hình ảnh
Đồ thị vận tốc của vật rơi có lực cản, điện tích khi sạc tụ trong mạch RC và dòng điện khi đóng nguồn mạch RL đều có chung dạng cong: tăng nhanh lúc ban đầu rồi tiệm cận dần đường tiệm cận ngang ứng với trạng thái ổn định.

### Cách nhìn hình thức
Ba mô hình tiêu chuẩn gồm:

**Vật rơi với lực cản tuyến tính**:

$$
m\frac{dv}{dt}=mg-cv.
$$

**Mạch RC**:

$$
R\frac{dq}{dt}+\frac{1}{C}q=E(t).
$$

**Mạch RL**:

$$
L\frac{di}{dt}+Ri=E(t).
$$

Sau khi chia cho hệ số đứng trước đạo hàm, cả ba đều trở thành phương trình tuyến tính cấp một ở dạng chuẩn.

## Những ý tưởng mô hình hóa cốt lõi
Trong cơ học, ta áp dụng định luật II Newton (tổng lực bằng khối lượng nhân gia tốc); trong mạch điện, ta áp dụng định luật điện áp Kirchhoff (tổng độ giảm điện áp dọc vòng kín bằng sức điện động nguồn). Sau khi lập được phương trình, quá trình giải quay về phương pháp nhân tử tích phân quen thuộc.

Điều quan trọng không kém là đọc ý nghĩa của các tổ hợp tham số: các hằng số thời gian $$ \frac{m}{c} $$, $$ RC $$ và $$ \frac{L}{R} $$ đo trực tiếp thang thời gian đặc trưng mà hệ tiến về trạng thái ổn định.

## Những ngộ nhận thường gặp
- "Vật rơi trong không khí luôn tăng tốc mãi." Sai. Dưới lực cản môi trường, vận tốc tiến tới vận tốc giới hạn.
- "Vừa đóng công tắc thì dòng điện trong mạch RL đạt ngay giá trị ổn định." Sai. Cuộn cảm chống lại sự biến thiên đột ngột của dòng điện nên mạch luôn có giai đoạn quá độ.
- "Điện trở trong mạch RC hay RL chỉ ảnh hưởng đến giá trị cuối." Sai. Điện trở còn tham gia trực tiếp vào hằng số thời gian quyết định tốc độ đáp ứng.
- "Các tham số vật lý chỉ là ký hiệu thay số." Sai. Mỗi tham số chi phối trực tiếp đặc tính động học của hệ.

## Tiến trình học tập đề xuất

### Bước 1: Thiết lập định luật vật lý
Liệt kê đầy đủ các lực tác dụng (định luật Newton) hoặc các độ giảm điện áp (định luật Kirchhoff) kèm quy ước chiều dương.

### Bước 2: Xác định biến trạng thái
Chọn biến phù hợp: vận tốc $$ v(t) $$ trong cơ học, điện tích $$ q(t) $$ trong mạch RC, dòng điện $$ i(t) $$ trong mạch RL.

### Bước 3: Đưa về dạng tuyến tính chuẩn
Chia hai vế để hệ số của đạo hàm bằng $$ 1 $$.

### Bước 4: Giải và phân tích đáp ứng
Xác định cả trạng thái ổn định dài hạn lẫn hằng số thời gian của thành phần quá độ.

### Các checkpoint
- Bạn có đặt đúng dấu của lực cản và các số hạng điện áp không?
- Bạn có tìm nhanh được trạng thái ổn định bằng cách đặt đạo hàm bằng $$ 0 $$ không?
- Bạn có giải thích được ý nghĩa vật lý của hằng số thời gian trong từng hệ không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Vật rơi với lực cản tuyến tính
Chọn chiều dương hướng xuống. Một vật khối lượng $$ m $$ chịu trọng lực $$ mg $$ và lực cản $$ cv $$ ngược chiều chuyển động thỏa mãn

$$
m\frac{dv}{dt}=mg-cv \iff \frac{dv}{dt}+\frac{c}{m}v=g.
$$

Với nhân tử tích phân $$ e^{\frac{c}{m}t} $$, nghiệm tổng quát là $$ v(t)=\frac{mg}{c}+Ce^{-\frac{c}{m}t} $$. Nếu vật rơi từ trạng thái nghỉ $$ v(0)=0 $$, ta được $$ C=-\frac{mg}{c} $$, nên

$$
v(t)=\frac{mg}{c}\left(1-e^{-\frac{c}{m}t}\right).
$$

Vận tốc giới hạn của vật là $$ \frac{mg}{c} $$.

### Ví dụ 2: Mạch RC với nguồn một chiều không đổi
Mạch RC gồm điện trở $$ R $$, tụ điện $$ C $$ và nguồn áp không đổi $$ E_0 $$ thỏa mãn

$$
R\frac{dq}{dt}+\frac{1}{C}q=E_0 \iff \frac{dq}{dt}+\frac{1}{RC}q=\frac{E_0}{R}.
$$

Giải ra $$ q(t)=CE_0+Ke^{-t/(RC)} $$. Nếu tụ ban đầu chưa tích điện ($$ q(0)=0 $$), thì $$ K=-CE_0 $$ và

$$
q(t)=CE_0\left(1-e^{-t/(RC)}\right).
$$

Điện tích tiến dần về $$ CE_0 $$ với hằng số thời gian sạc là $$ RC $$.

### Ví dụ 3: Mạch RL với nguồn một chiều không đổi
Dòng điện $$ i(t) $$ trong mạch RL thỏa mãn

$$
L\frac{di}{dt}+Ri=E_0 \iff \frac{di}{dt}+\frac{R}{L}i=\frac{E_0}{L}.
$$

Nghiệm tổng quát là $$ i(t)=\frac{E_0}{R}+Ke^{-Rt/L} $$. Với điều kiện đầu $$ i(0)=0 $$, ta thu được

$$
i(t)=\frac{E_0}{R}\left(1-e^{-Rt/L}\right).
$$

Dòng điện xác lập là $$ \frac{E_0}{R} $$ và hằng số thời gian của mạch là $$ \frac{L}{R} $$.

### Ví dụ 4: Định luật làm nguội Newton — cấu trúc toán học tương đồng
Định luật làm nguội Newton

$$
\frac{dT}{dt}=-k\left(T-T_m\right)
$$

có nghiệm $$ T(t)=T_m+\left(T(0)-T_m\right)e^{-kt} $$. Đặt cạnh ba ví dụ trên, ta thấy cùng một cấu trúc phương trình tuyến tính cấp một xuất hiện lặp lại trong nhiệt học, cơ học và điện học.

## Câu hỏi khái niệm
1. Vì sao lực cản hay điện trở lại tạo ra số hạng kéo hệ về trạng thái ổn định?
2. Hằng số thời gian của một hệ cho biết điều gì về tốc độ đáp ứng?
3. Vì sao nhiều hệ vật lý khác hẳn nhau về bản chất lại được mô tả bởi cùng một dạng ODE tuyến tính cấp một?

## Bài toán ứng dụng
1. Khi nhảy dù trong không khí, hệ số cản ảnh hưởng như thế nào đến vận tốc giới hạn và an toàn tiếp đất?
2. Trong cảm biến nhiệt tuân theo định luật làm nguội Newton, hằng số $$ k $$ lớn hay nhỏ sẽ giúp cảm biến phản hồi nhanh hơn?
3. Khi dùng mạch RC để lọc nhiễu tín hiệu, vì sao việc mạch không phản ứng tức thời lại mang lại lợi ích?

## Chiến lược giảng dạy tương tác
- Yêu cầu sinh viên phác họa trước dạng đồ thị vận tốc hoặc dòng điện rồi đối chiếu với nghiệm giải tích.
- Chia lớp thành hai nhóm: một nhóm giải bài toán cơ học, một nhóm giải bài toán mạch điện, sau đó so sánh sự tương ứng giữa các tham số.
- Đặt câu hỏi định tính: "Nếu tăng điện trở $$ R $$ lên gấp đôi trong mạch RL, dòng điện xác lập và hằng số thời gian thay đổi như thế nào?"
- Khuyến khích diễn giải mọi tham số bằng ngôn ngữ vật lý thay vì chỉ đọc ký hiệu.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng sơ đồ lập mô hình ba bước: phát biểu định luật vật lý, chọn biến trạng thái kèm đơn vị và viết phương trình ở dạng chuẩn.

### Thử thách cho sinh viên khá giỏi
Khảo sát mạch RC hoặc RL với nguồn xoay chiều $$ E(t)=E_0\cos(\omega t) $$, hoặc so sánh mô hình lực cản tuyến tính với lực cản bậc hai.

## Tóm tắt dễ nhớ
Trong cơ học và mạch điện, các định luật cân bằng cơ bản dẫn trực tiếp đến ODE tuyến tính cấp một. Nghiệm thường tách thành tổng của trạng thái ổn định và thành phần quá độ suy giảm theo hằng số thời gian đặc trưng của hệ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Người nhảy dù với lực cản tuyến tính
- Bài toán: Ước lượng vận tốc rơi ở giai đoạn đầu trước khi mở dù.
- Mô hình:

$$
m\frac{dv}{dt}=mg-cv.
$$

- Giả thiết và giới hạn: Tư thế rơi và hệ số cản không đổi, bỏ qua gió ngang và xấp xỉ lực cản tuyến tính theo vận tốc (ở tốc độ cao, lực cản bậc hai chính xác hơn).
- Diễn giải: Vận tốc tiệm cận giá trị giới hạn $$ mg/c $$.

#### Mạch RC như bộ lọc tín hiệu
- Bài toán: Làm mượt nhiễu tần số cao trên tín hiệu cảm biến mà vẫn giữ được xu hướng biến thiên chậm.
- Mô hình:

$$
RC\frac{dV}{dt}+V=V_{\mathrm{in}}(t).
$$

- Giả thiết và giới hạn: Linh kiện lý tưởng và tuyến tính; bỏ qua bão hòa điện áp và điện cảm ký sinh.
- Diễn giải: Hằng số thời gian $$ RC $$ đo độ trễ đáp ứng của mạch—giá trị lớn hơn lọc nhiễu mạnh hơn nhưng làm chậm phản hồi.

#### Điều khiển hành trình đơn giản
- Bài toán: Ô tô chạy trên đường bằng với lực kéo động cơ không đổi và lực cản tỉ lệ với vận tốc.
- Mô hình:

$$
m\frac{dv}{dt}=F_0-bv.
$$

- Giả thiết và giới hạn: Đường phẳng, không chuyển số và bỏ qua độ trễ điều khiển; xe thực tế có lực cản khí động bậc hai và nhiều yếu tố phi tuyến.
- Diễn giải: Phương trình có cùng dạng với vật rơi có lực cản, minh họa tính phổ quát của ODE tuyến tính cấp một.

### 2. Trực giác bổ sung và các kết nối

Các bài toán cơ học và mạch điện cho thấy tham số vật lý (khối lượng, điện trở, điện cảm, hệ số cản) quyết định trực tiếp cả giá trị xác lập lẫn tốc độ quá độ. Đây là bước chuẩn bị tự nhiên cho chương phương trình bậc hai với hiện tượng dao động và cộng hưởng. Cần lưu ý không chỉ quan tâm giá trị dài hạn: trong kỹ thuật điều khiển, chính đặc tính quá độ mới quyết định chất lượng vận hành của hệ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
g = 9.81
m = 80.0

for c in [10, 20, 40]:
    v = (m * g / c) * (1 - np.exp(-c * t / m))
    plt.plot(t, v, label=f"c={c}")

plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("Vận tốc rơi với các hệ số cản khác nhau")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy khi hệ số cản $$ c $$ tăng, vận tốc giới hạn giảm xuống đồng thời thời gian tiến gần trạng thái ổn định cũng ngắn lại.

### 4. Gợi ý tìm thêm mô phỏng

- search: falling body with drag simulation
- search: RC circuit step response interactive
- search: RL circuit transient plot

### 5. Bài toán mẫu có bối cảnh thực

Một người nhảy dù khối lượng $$ 80\text{ kg} $$ rơi từ trạng thái nghỉ với hệ số cản tuyến tính $$ c=20\text{ kg/s} $$. Phương trình chuyển động là

$$
80\frac{dv}{dt}=80\cdot 9.81-20v, \qquad v(0)=0,
$$

cho nghiệm

$$
v(t)=39.24\left(1-e^{-t/4}\right).
$$

Với hằng số thời gian $$ \tau = 4\text{ s} $$, sau $$ 4\text{ s} $$ vận tốc đạt khoảng $$ 63\% $$ vận tốc giới hạn, và sau $$ 12\text{ s} $$ ($$ 3\tau $$) vận tốc đã rất gần trạng thái ổn định.

### 6. Phân tầng độ khó

**Bậc đại học.** Lập phương trình từ định luật Newton hoặc Kirchhoff, giải ODE và diễn giải trạng thái ổn định cùng hằng số thời gian.

**Bậc sau đại học.** Mở rộng sang hàm truyền, đáp ứng xung, phân tích tiêu tán năng lượng và các mô hình phi tuyến như lực cản bậc hai hoặc linh kiện phi lý tưởng.

## Video tham khảo

- Xem trước: [Second-Order Ordinary Differential Equations: Solving the Harmonic Oscillator Four Ways](https://www.youtube.com/watch?v=8ePqqZXSMQs) — Steve Brunton, tiếng Anh. Giới thiệu dao động điều hòa theo bốn góc nhìn, bước tiếp theo từ các mô hình cơ học cấp một.
- [Example Second-Order ODE: Spring-Mass-Damper](https://www.youtube.com/watch?v=r1eWerqrcqo) — Steve Brunton, tiếng Anh. Thiết lập và giải hệ lò xo–khối lượng–giảm chấn từ định luật Newton.
- [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, tiếng Anh. Minh họa chuyển động rơi dưới trọng lực như ví dụ mở đầu của ODE cơ học.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ các mô hình cơ học, mạch điện và ý nghĩa tham số.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ vật lý cấp một phù hợp cho tự học và giảng dạy.
- Ross — *Differential Equations*: nhấn mạnh sự tương đồng cấu trúc giữa các mô hình ứng dụng khác nhau.
