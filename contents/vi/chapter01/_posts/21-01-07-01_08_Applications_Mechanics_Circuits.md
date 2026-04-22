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
## Mục tiêu
Bài học này giúp sinh viên thấy rằng các định luật vật lý cơ bản dẫn đến ODE gần như không cần gượng ép. Qua vận tốc rơi với lực cản, mạch RC và mạch RL, sinh viên học cách biến định luật Newton và Kirchhoff thành phương trình vi phân, giải nghiệm, và đọc các tham số như thời hằng, vận tốc giới hạn hay tốc độ đáp ứng của hệ.

## Kiến thức nền
Sinh viên nên quen với phương trình tuyến tính cấp một và một ít ngôn ngữ vật lý cơ bản: lực, vận tốc, điện áp, điện tích, dòng điện. Không cần nền tảng vật lý quá sâu; điều quan trọng hơn là hiểu rằng định luật bảo toàn và định luật cân bằng thường tạo ra ODE rất tự nhiên.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-08 Ứng dụng: Cơ học và Mạch điện]({{ site.imgurl }}/chapter_img/chapter01/01_08_applications_mechanics_circuits.svg)

Nếu thả một vật trong không khí, nó không rơi nhanh vô hạn. Lực cản môi trường tăng dần và cuối cùng cân bằng với trọng lực, tạo ra vận tốc giới hạn. Nếu nối một tụ điện với nguồn, điện tích trên tụ không nhảy tức thời đến giá trị tối đa; nó tăng dần theo thời gian. Nếu bật một mạch RL, dòng điện cũng không đạt giá trị ổn định ngay mà trải qua quá trình quá độ. Những hiện tượng quen thuộc ấy đều là bài học về thay đổi theo thời gian.

Điểm đẹp của các ví dụ cơ học và mạch điện là mọi tham số đều có ý nghĩa vật lý rõ ràng. Điều này giúp sinh viên kết nối lời giải toán học với thế giới thật: dấu của số hạng nào tạo ra lực cản, hệ số nào quyết định tốc độ đáp ứng, và vì sao trạng thái ổn định lại xuất hiện.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Trong cơ học với lực cản tuyến tính, vật vừa được trọng lực kéo xuống vừa bị môi trường kéo ngược lại, nên vận tốc dần tiến đến một mức ổn định. Trong mạch điện, nguồn điện đẩy hệ tiến đến cân bằng, còn điện trở đóng vai trò cản trở sự thay đổi tức thời.

### Cách nhìn hình ảnh
Đồ thị vận tốc rơi với lực cản thường bắt đầu tăng nhanh rồi dần phẳng ra khi tiến tới vận tốc giới hạn. Đồ thị điện tích trong mạch RC khi sạc có dạng tăng nhanh lúc đầu rồi tiến tới mức bão hòa. Những đồ thị cong về phía trạng thái ổn định là dấu hiệu rất điển hình của ODE tuyến tính cấp một với một trạng thái cân bằng ổn định.

### Cách nhìn hình thức
Các mô hình chuẩn gồm:

Vật rơi với lực cản tuyến tính:
$$ m\frac{dv}{dt}=mg-cv. $$

Mạch RC:
$$ R\frac{dq}{dt}+\frac{1}{C}q=E(t). $$

Mạch RL:
$$ L\frac{di}{dt}+Ri=E(t). $$

Tất cả đều là phương trình tuyến tính cấp một sau khi chia bởi hệ số của đạo hàm.

## Những ý tưởng mô hình hóa cốt lõi
Trong các ví dụ này, ODE xuất hiện từ định luật cân bằng. Ở cơ học, ta viết tổng lực bằng khối lượng nhân gia tốc. Ở mạch điện, ta viết tổng điện áp theo định luật Kirchhoff. Một khi phương trình được lập, bài toán quay trở về đúng khung đã học: nhận dạng dạng chuẩn, dùng nhân tử tích phân, rồi đọc ý nghĩa nghiệm.

Điểm sư phạm cần nhấn mạnh là tham số không chỉ là ký hiệu. Tỉ số $$ \frac{m}{c} $$ hay $$ RC $$ hay $$ \frac{L}{R} $$ cho ta một thước đo thời gian đáp ứng của hệ. Đây là lúc giải tích và diễn giải vật lý gặp nhau rất đẹp.

## Những ngộ nhận thường gặp
- "Vật rơi luôn tăng tốc mãi." Sai. Với lực cản tuyến tính, vận tốc tiến tới một giá trị giới hạn.
- "Nguồn điện được bật thì dòng điện đạt ngay giá trị ổn định." Sai. Hệ có quá trình quá độ.
- "Điện trở chỉ làm thay đổi giá trị cuối." Sai. Nó còn chi phối tốc độ đạt đến trạng thái cuối.
- "Các tham số vật lý chỉ là con số cắm vào công thức." Sai. Mỗi tham số đều mang ý nghĩa cấu trúc về động học của hệ.

## Tiến trình học tập đề xuất
### Bước 1: Viết định luật vật lý
Xác định rõ lực hay điện áp nào tham gia vào cân bằng.

### Bước 2: Chọn biến trạng thái
Trong cơ học là vận tốc $$ v(t) $$, trong mạch RC là điện tích $$ q(t) $$, trong mạch RL là dòng điện $$ i(t) $$.

### Bước 3: Đưa về dạng tuyến tính chuẩn
Chia để hệ số của đạo hàm bằng 1.

### Bước 4: Giải và đọc trạng thái ổn định
Hỏi không chỉ "nghiệm là gì" mà còn "nó tiến về đâu" và "nhanh hay chậm".

### Các checkpoint
- Sinh viên có chọn đúng dấu của lực cản hoặc số hạng điện trở hay không.
- Sinh viên có rút ra đúng trạng thái ổn định bằng cách cho đạo hàm bằng 0 hay không.
- Sinh viên có giải thích được thời hằng của hệ bằng lời hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Vật rơi với lực cản tuyến tính
Chọn chiều dương hướng xuống. Một vật khối lượng $$ m $$ chịu trọng lực $$ mg $$ và lực cản $$ cv $$ ngược chuyển động, nên
$$ m\frac{dv}{dt}=mg-cv. $$
Viết lại:
$$ \frac{dv}{dt}+\frac{c}{m}v=g. $$
Đây là phương trình tuyến tính cấp một. Nhân tử tích phân là
$$ e^{\frac{c}{m}t}. $$
Giải ra:
$$ v(t)=\frac{mg}{c}+Ce^{-\frac{c}{m}t}. $$
Nếu vật được thả từ trạng thái nghỉ, $$ v(0)=0 $$, ta có
$$ C=-\frac{mg}{c}, $$
nên
$$
v(t)=\frac{mg}{c}\left(1-e^{-\frac{c}{m}t}\right).
$$
Vận tốc giới hạn là
$$ \frac{mg}{c}. $$

### Ví dụ 2: Mạch RC với nguồn không đổi
Một mạch RC có điện trở $$ R $$, tụ điện $$ C $$ và nguồn không đổi $$ E_0 $$. Khi đó
$$ R\frac{dq}{dt}+\frac{1}{C}q=E_0. $$
Chia cho $$ R $$:
$$ \frac{dq}{dt}+\frac{1}{RC}q=\frac{E_0}{R}. $$
Giải ra:
$$ q(t)=CE_0+Ke^{-t/(RC)}. $$
Nếu tụ ban đầu chưa tích điện, $$ q(0)=0 $$, thì
$$ K=-CE_0, $$
và
$$ q(t)=CE_0\left(1-e^{-t/(RC)}\right). $$
Điện tích tiến dần tới $$ CE_0 $$. Thời hằng $$ RC $$ cho biết tốc độ sạc.

### Ví dụ 3: Mạch RL với nguồn không đổi
Với mạch RL, dòng điện $$ i(t) $$ thỏa
$$ L\frac{di}{dt}+Ri=E_0. $$
Chia cho $$ L $$:
$$ \frac{di}{dt}+\frac{R}{L}i=\frac{E_0}{L}. $$
Giải được
$$ i(t)=\frac{E_0}{R}+Ke^{-Rt/L}. $$
Nếu $$ i(0)=0 $$, thì
$$ i(t)=\frac{E_0}{R}\left(1-e^{-Rt/L}\right). $$
Trạng thái ổn định là $$ \frac{E_0}{R} $$, còn thời hằng là $$ \frac{L}{R} $$.

### Ví dụ 4: Làm nguội như một cầu nối vật lý
Mặc dù đã gặp ở bài tuyến tính cấp một, định luật làm nguội Newton là một ứng dụng vật lý rất tốt:
$$ \frac{dT}{dt}=-k\left(T-T_m\right). $$
Giải được
$$ T(t)=T_m+\left(T(0)-T_m\right)e^{-kt}. $$
Ví dụ này giúp sinh viên nhận ra cùng một cấu trúc toán học có thể xuất hiện trong nhiệt học, cơ học và mạch điện.

## Câu hỏi khái niệm
1. Vì sao lực cản hoặc điện trở thường tạo ra số hạng làm hệ tiến về trạng thái ổn định?
2. Thời hằng của hệ cho biết điều gì về phản ứng nhanh hay chậm của hệ?
3. Vì sao nhiều mô hình vật lý rất khác nhau lại dẫn đến cùng một dạng ODE tuyến tính cấp một?

## Bài toán ứng dụng
1. Một người nhảy dù rơi trong không khí. Hãy giải thích vai trò của lực cản đối với vận tốc giới hạn và tính an toàn.
2. Một cảm biến nhiệt có thể được mô hình hóa bằng định luật làm nguội Newton. Hãy giải thích ý nghĩa của hằng số $$ k $$ đối với tốc độ phản hồi của cảm biến.
3. Một mạch RC được dùng để làm mượt tín hiệu. Hãy thảo luận vì sao việc hệ không phản ứng tức thời lại có thể là một lợi thế.

## Chiến lược giảng dạy tương tác
- Cho sinh viên dự đoán đồ thị vận tốc hoặc dòng điện trước khi giải, rồi dùng nghiệm để kiểm chứng dự đoán.
- Tổ chức hoạt động ghép đôi: một nhóm giải bài toán cơ học, một nhóm giải bài toán mạch điện, sau đó so sánh cấu trúc nghiệm.
- Hỏi lớp: "Nếu điện trở tăng gấp đôi thì điều gì xảy ra với trạng thái ổn định và với tốc độ đáp ứng?"
- Khuyến khích sinh viên giải thích tham số bằng ngôn ngữ đời sống, không chỉ bằng ký hiệu.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp sơ đồ lập mô hình gồm ba ô: định luật vật lý, biến trạng thái, ODE thu được. Việc cho sinh viên gắn đơn vị cho từng đại lượng cũng giúp các em giữ được trực giác.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi phân tích nguồn điện biến thiên theo thời gian $$ E(t) $$, hoặc so sánh mô hình lực cản tuyến tính với lực cản bậc hai. Đây là bước chuẩn bị tốt cho các chương sau về phương trình bậc cao và mô hình thực hơn.

## Tóm tắt dễ nhớ
Trong cơ học và mạch điện, ODE xuất hiện từ các định luật cân bằng cơ bản. Nghiệm thường có dạng "trạng thái ổn định cộng với phần quá độ suy giảm". Muốn hiểu mô hình, đừng chỉ hỏi công thức nghiệm; hãy hỏi hệ tiến về đâu và với tốc độ nào.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Người nhảy dù với lực cản tuyến tính
- Bài toán: Cần ước lượng vận tốc rơi trong giai đoạn đầu trước khi mở dù.
- Mô hình:
$$ m\frac{dv}{dt}=mg-cv. $$
- Giả thiết và giới hạn: Tư thế rơi và hệ số cản không đổi, chưa có gió ngang, và lực cản được xấp xỉ tuyến tính theo vận tốc. Ở vận tốc lớn, lực cản bậc hai thường thực hơn.
- Diễn giải: Nghiệm cho thấy vận tốc tiến về giới hạn $$ mg/c $$, một đại lượng có ý nghĩa an toàn trực tiếp.

#### Mạch RC như bộ lọc tín hiệu
- Bài toán: Một cảm biến điện áp cần làm mượt nhiễu cao tần nhưng vẫn giữ xu hướng chậm của tín hiệu.
- Mô hình:
$$ RC\frac{dV}{dt}+V=V_{\mathrm{in}}(t). $$
- Giả thiết và giới hạn: Linh kiện là lý tưởng và hệ tuyến tính. Nhiễu phi tuyến, bão hòa điện áp, hoặc điện cảm ký sinh bị bỏ qua.
- Diễn giải: Thời hằng $$ RC $$ cho biết mức độ "lười" của mạch. Giá trị lớn làm hệ mượt hơn nhưng phản ứng chậm hơn.

#### Điều khiển hành trình đơn giản
- Bài toán: Xe muốn đạt vận tốc đặt trước khi động cơ cấp lực gần như hằng và lực cản tổng quát tỉ lệ với vận tốc.
- Mô hình:
$$ m\frac{dv}{dt}=F_0-bv. $$
- Giả thiết và giới hạn: Đường bằng phẳng, không đổi số, và không có trễ điều khiển. Xe thật có nhiều phi tuyến và đổi số theo thời gian.
- Diễn giải: Dạng nghiệm giống hệt bài toán vật rơi với lực cản, minh họa rất đẹp tính phổ quát của ODE tuyến tính cấp một.

### 2. Trực giác bổ sung và các kết nối

Cơ học và mạch điện cho sinh viên thấy các tham số không phải đồ trang trí. Khối lượng, điện trở, điện cảm, hay hệ số cản quyết định trực tiếp thời gian đáp ứng và trạng thái ổn định. Đây là bước chuẩn bị tự nhiên cho chương sau về phương trình bậc hai, nơi động học quán tính, dao động và cộng hưởng trở nên nổi bật hơn. Một sai lầm phổ biến là chỉ chú ý giá trị cuối mà quên mất phần quá độ; trong kỹ thuật điều khiển, phần quá độ thường mới là phần quyết định hệ có "tốt" hay không.

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

Sinh viên nhìn ngay rằng hệ số cản lớn hơn vừa làm vận tốc giới hạn nhỏ hơn, vừa làm quá trình đạt tới giới hạn ấy nhanh hơn.

### 4. Gợi ý tìm thêm mô phỏng

- search: falling body with drag simulation
- search: RC circuit step response interactive
- search: RL circuit transient plot

### 5. Bài toán mẫu có bối cảnh thực

Một người nhảy dù khối lượng 80 kg rơi với lực cản tuyến tính $$ c=20 $$ kg/s và bắt đầu từ nghỉ. Phương trình là
$$ 80\frac{dv}{dt}=80\cdot 9.81-20v,
\qquad
v(0)=0. $$
Giải được
$$ v(t)=39.24\left(1-e^{-t/4}\right). $$
Sau khoảng bốn giây, vận tốc đã đạt khoảng 63 phần trăm vận tốc giới hạn; sau mười hai giây, đã rất gần trạng thái ổn định. Đây là diễn giải theo thời hằng rất hữu ích cho sinh viên kỹ thuật.

### 6. Phân tầng độ khó

**Bậc đại học.** Lập mô hình từ định luật Newton hay Kirchhoff, giải ODE, và diễn giải thời hằng cùng trạng thái ổn định.

**Bậc sau đại học.** Kết nối với hàm truyền, đáp ứng xung, năng lượng tiêu tán, và mô hình phi tuyến hơn như lực cản bậc hai hay mạch có phần tử phi lý tưởng. Đây cũng là bước đệm cho lý thuyết điều khiển.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: rất mạnh ở các mô hình cơ học, mạch điện và diễn giải tham số.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều ví dụ vật lý cấp một phù hợp cho bài giảng.
- Ross — *Differential Equations*: hữu ích để luyện nhận dạng sự tương đồng cấu trúc giữa các ứng dụng khác nhau.
