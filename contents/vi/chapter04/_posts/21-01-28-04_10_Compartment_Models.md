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


Khi bạn uống một viên thuốc, hoạt chất đi từ dạ dày vào máu, phân tán sang các mô rồi mới được gan thận thải trừ; tương tự, ô nhiễm hóa học luân chuyển giữa chuỗi hồ thông nhau hay carbon tuần hoàn giữa khí quyển và đại dương. Tất cả đều được mô tả bởi **Mô hình Ngăn (Compartment Models)**—một lớp hệ tuyến tính $\mathbf{x}' = A\mathbf{x} + \mathbf{b}$ có cấu trúc ma trận cực kỳ đẹp đảm bảo nồng độ không bao giờ âm và hệ luôn hội tụ về cân bằng bền vững!

## Bản đồ kiến thức nền: Bốn trụ cột của Mô hình Ngăn

1. **Nguyên lý cân bằng dòng chảy cho từng ngăn**:
   $x_i'(t) = \sum_{j \ne i} k_{ij} x_j - \left(\sum_{j \ne i} k_{ji} + k_{0i}\right)x_i + b_i(t)$: phần tử ngoài đường chéo $a_{ij} \ge 0$ (dòng chảy vào từ ngăn $j$), phần tử đường chéo $a_{ii} \le 0$ (tổng dòng chảy ra khỏi ngăn $i$).
2. **Hệ kín (Closed System) vs. Hệ mở (Open System)**:
   - **Hệ kín** (không thoát ra môi trường, tổng mỗi cột của $A$ bằng $0$): tổng lượng chất $\sum x_i(t) = \text{const}$ được bảo toàn tuyệt đối, nên $A$ luôn có **một trị riêng $\lambda = 0$** tương ứng với trạng thái phân bố cân bằng!
   - **Hệ mở** (có cửa thải ra ngoài): tổng cột $\le 0$ và có ít nhất một cột $< 0$; mọi trị riêng có $\operatorname{Re}(\lambda) < 0$, chất tan dần về $0$ nếu ngừng bơm.
3. **Tính bất biến dương (Positivity)**:
   Nhờ $a_{ij} \ge 0$ ($i \ne j$), nếu xuất phát từ $\mathbf{x}(0) \ge \mathbf{0}$ thì $\mathbf{x}(t) \ge \mathbf{0}$ ở mọi thời điểm—mô hình hoàn toàn tôn trọng thực tế vật lý!
4. **Dược động học (Pharmacokinetics) & Thời gian đạt đỉnh $t_{\max}$**:
   Mô hình hai ngăn (dạ dày $\to$ máu $\to$ thải trừ) cho phép tính chính xác thời điểm nồng độ thuốc trong máu đạt đỉnh để thiết kế liều dùng an toàn.

## Mục tiêu

Bài học này cho thấy hệ phương trình vi phân là ngôn ngữ tự nhiên cho các mô hình ngăn trong dược động học, sinh thái học và dịch tễ học. Sinh viên sẽ biết cách lập phương trình cân bằng dòng vào – dòng ra cho từng ngăn, kiểm tra tính bảo toàn hoặc hao hụt tổng lượng, và đọc ma trận hệ như bản đồ trao đổi giữa các khoang.

## Kiến thức nền

Sinh viên cần nắm hệ tuyến tính, khái niệm nguồn ngoài và nguyên tắc cân bằng "lượng vào trừ lượng ra". Kỹ năng kiểm tra đơn vị và diễn giải dấu của các hệ số quan trọng ngang với kỹ thuật giải hệ.

## Dẫn nhập

![Mô hình ngăn với dòng chuyển giữa các khoang]({{ site.imgurl }}/chapter_img/chapter04/10_compartment_models.svg)

Bên cạnh dao động và cơ học, một lớp ứng dụng rộng lớn khác của hệ ODE là mô hình ngăn (compartment model). Trong đó, mỗi biến trạng thái đo lượng vật chất, dân số, thuốc hoặc chất ô nhiễm trong một khoang, còn các hệ số biểu diễn tốc độ chuyển dịch giữa các khoang.

Mô hình ngăn không chỉ theo dõi "mỗi khoang chứa bao nhiêu" mà còn thể hiện "vật chất đi từ đâu sang đâu", giúp trả lời ngay các câu hỏi về bảo toàn khối lượng, thất thoát ra môi trường và trạng thái cân bằng dài hạn.

### Khung giải thích (nên đọc chậm): Giải mô hình dược động học 2 ngăn (Dạ dày $x_1$ $\xrightarrow{k_1 = 2}$ Máu $x_2$ $\xrightarrow{k_2 = 1}$ Thải trừ) với liều uống $x_1(0) = 100\text{ mg},\; x_2(0) = 0$

1. **Hệ phương trình tam giác**:
   $$\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}' = \begin{pmatrix} -2 & 0 \\ 2 & -1 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}.$$
   Đọc ngay trị riêng trên đường chéo: $\lambda_1 = -2 < 0,\; \lambda_2 = -1 < 0$ (hệ mở, ổn định tuyệt đối!).
2. **Giải tầng từ trên xuống**:
   - Từ $x_1' = -2x_1,\; x_1(0) = 100 \implies x_1(t) = \mathbf{100e^{-2t}}$.
   - Thay vào $x_2' + x_2 = 200e^{-2t}$ (nhân $e^t$): $(e^t x_2)' = 200e^{-t} \implies x_2(t) = -200e^{-2t} + Ce^{-t}$.
   - Với $x_2(0) = 0 \implies C = 200$, nên lượng thuốc trong máu là:
     $$x_2(t) = \mathbf{200\big(e^{-t} - e^{-2t}\big)}\text{ mg}.$$
3. **Tìm thời điểm đạt đỉnh $t_{\max}$ và nồng độ cực đại**:
   $x_2'(t) = 200(-e^{-t} + 2e^{-2t}) = 0 \iff e^{-t} = 2e^{-2t} \iff e^t = 2 \iff t_{\max} = \ln 2 \approx \mathbf{0{,}693\text{ giờ}}$.
   Khi đó $x_2(t_{\max}) = 200\left(\frac{1}{2} - \frac{1}{4}\right) = \mathbf{50\text{ mg}}$ (đúng một nửa liều uống ban đầu!).

## Khái niệm theo ba cách

### Cách nhìn trực quan

Có thể hình dung một hệ thống gồm nhiều bể chứa nối với nhau bằng các đường ống. Lượng chất trong mỗi bể tăng lên nhờ các dòng chảy vào và giảm đi do các dòng chảy ra; viết phương trình cân bằng cho từng bể tạo thành hệ phương trình của mô hình ngăn.

### Cách nhìn hình ảnh

Sơ đồ ngăn với các mũi tên nối giữa các khoang là bước khởi đầu trực quan nhất: mỗi mũi tên gắn với một tốc độ chuyển dòng, từ đó xác định trực tiếp dấu dương (dòng vào) hay âm (dòng ra) của từng số hạng trong hệ.

### Cách nhìn hình thức

Một mô hình hai ngăn tuyến tính tổng quát có dạng
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2+u_1(t),
$$
$$
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2+u_2(t).
$$
Các số hạng âm ứng với dòng rời khỏi ngăn, các số hạng dương ứng với dòng đi vào ngăn, còn $$ u_1(t), u_2(t) $$ là các nguồn cấp từ bên ngoài.

## Những ngộ nhận thường gặp

- "Mô hình ngăn chỉ là phép cộng trừ lưu lượng đơn giản." Sai: sự trao đổi hai chiều giữa các khoang tạo ra động học ghép nối đặc trưng của hệ ODE.
- "Mỗi phương trình trông đơn giản nên hành vi cả hệ cũng đơn giản." Không hẳn: sự tương tác giữa nhiều ngăn có thể tạo ra nhiều thang thời gian khác nhau.
- "Tổng lượng trong hệ luôn được bảo toàn." Sai: tổng lượng chỉ bảo toàn khi hệ kín, không có dòng thải ra ngoài hoặc nguồn cấp vào.
- "Mọi mô hình ngăn đều là hệ tuyến tính." Sai: nhiều mô hình quan trọng như mô hình dịch tễ SIR là hệ phi tuyến.

## Tiến trình học tập đề xuất

### Bước 1: Vẽ sơ đồ ngăn và các mũi tên chuyển dòng

Xác định đầy đủ các khoang, chiều trao đổi và dòng vào/ra môi trường.

### Bước 2: Viết phương trình cân bằng vào – ra cho từng ngăn

Kiểm tra kỹ dấu và đơn vị của mọi số hạng.

### Bước 3: Cộng các phương trình để kiểm tra tổng lượng

Xác định hệ kín (bảo toàn) hay hệ mở (hao hụt hoặc có nguồn bơm thêm).

### Bước 4: Phân tích động học và trạng thái dài hạn

Khảo sát tốc độ trao đổi, tính ổn định và ý nghĩa của các tham số.

### Các checkpoint

- Sinh viên có đặt đúng dấu cho các dòng vào và dòng ra hay không.
- Sinh viên có biết kiểm tra tính bảo toàn tổng lượng của hệ hay không.
- Sinh viên có phân biệt rõ dòng trao đổi nội bộ giữa các ngăn với nguồn/thải từ bên ngoài hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Mô hình dược động học hai ngăn

Xét hệ không có nguồn cấp liên tục:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2,
$$
trong đó $$ x_1 $$ là lượng thuốc trong huyết tương, $$ x_2 $$ là lượng thuốc trong mô, và $$ k_{01} $$ là hệ số thải trừ khỏi cơ thể. Từ phương trình ta đọc ngay: thuốc rời ngăn 1 theo hai hướng (sang ngăn 2 và thải ra ngoài), đồng thời nhận lại thuốc từ ngăn 2 theo tốc độ $$ k_{21}x_2 $$.

### Ví dụ 2: Kiểm tra bảo toàn tổng lượng

Cộng hai phương trình của Ví dụ 1:
$$ \frac{d}{dt}(x_1+x_2)= -k_{01}x_1. $$
Tổng lượng thuốc giảm theo thời gian do có dòng thải trừ $$ k_{01}x_1 $$ ra khỏi cơ thể; nếu $$ k_{01}=0 $$, tổng lượng thuốc trong hai ngăn được bảo toàn.

### Ví dụ 3: Mô hình dịch tễ SIR như một hệ ngăn phi tuyến

Hệ
$$
\frac{dS}{dt}=-\beta SI,\qquad \frac{dI}{dt}=\beta SI-\gamma I,\qquad \frac{dR}{dt}=\gamma I
$$
là mô hình ngăn phi tuyến: cá thể chuyển từ ngăn nhạy cảm ($$ S $$) sang ngăn nhiễm bệnh ($$ I $$) rồi sang ngăn hồi phục ($$ R $$), với tổng dân số $$ S+I+R $$ bảo toàn.

### Ví dụ 4: Cấu trúc dấu của ma trận ngăn tuyến tính

Trong mô hình ngăn tuyến tính không nguồn, các phần tử ngoài đường chéo của ma trận hệ luôn không âm (biểu diễn dòng chảy vào từ ngăn khác), còn các phần tử trên đường chéo thường âm (biểu diễn tổng tốc độ rời khỏi chính ngăn đó).

## Câu hỏi khái niệm

1. Vì sao vẽ sơ đồ ngăn thường là bước quan trọng trước khi viết hệ phương trình?
2. Phương trình cho tổng lượng các ngăn giúp kiểm tra tính chất nào của mô hình?
3. Vì sao mô hình SIR dù phi tuyến vẫn thuộc lớp mô hình ngăn?

## Bài toán ứng dụng

1. Trong dược động học, vì sao mô hình hai ngăn thường mô tả thực tế sát hơn mô hình một ngăn?
2. Trong khoa học môi trường, chất ô nhiễm trao đổi giữa sông, hồ và đất. Vì sao mô hình ngăn là khung phân tích phù hợp?
3. Trong dịch tễ học, phân chia quần thể thành các ngăn hỗ trợ việc thiết kế biện pháp can thiệp như thế nào?

## Chiến lược giảng dạy tương tác

- Yêu cầu sinh viên dựng sơ đồ ngăn trước khi viết phương trình vi phân.
- Luyện bài tập đọc dấu: từ mũi tên trên sơ đồ, xác định ngay số hạng nào dương và số hạng nào âm.
- Hỏi lớp: "Tổng lượng của hệ có bảo toàn không, và kiểm tra nhanh bằng cách nào?"
- Lấy ví dụ thực tế từ y học, môi trường và dịch tễ để gắn hệ phương trình với bối cảnh ứng dụng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Luyện trước các mô hình hai ngăn bằng bảng ba cột: tên ngăn, các dòng chảy vào, các dòng chảy ra — điền đầy đủ bảng rồi mới ghép thành phương trình.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên phân tích dấu phần thực của trị riêng trong ma trận ngăn tuyến tính (dùng định lý Gershgorin), hoặc so sánh mô hình trao đổi tuyến tính với phiên bản phi tuyến bão hòa.

## Tóm tắt dễ nhớ

Mô hình ngăn biểu diễn dòng chuyển dịch vật chất hoặc cá thể giữa các khoang: mỗi biến ghi nhận lượng hiện có, còn các mũi tên xác định luồng đi vào và đi ra. Hai thao tác cốt lõi là viết đúng cân bằng vào – ra cho từng ngăn và kiểm tra biến thiên của tổng lượng toàn hệ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dược động học hai ngăn
- Bài toán: Thuốc phân bố giữa huyết tương và mô, đồng thời bị thải trừ ra khỏi cơ thể.
- Mô hình:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2.
$$
- Giả thiết và giới hạn: Động học tuyến tính bậc nhất, trộn đều trong từng ngăn.
- Diễn giải: Hệ phương trình mô tả đồng thời quá trình phân bố và đào thải thuốc.

#### Lan truyền chất ô nhiễm giữa các môi trường
- Bài toán: Chất ô nhiễm trao đổi giữa sông, hồ, đất và khí quyển.
- Mô hình: Hệ ngăn tuyến tính hoặc gần tuyến tính.
- Giả thiết và giới hạn: Tốc độ trao đổi ổn định và phân bố đồng đều trong từng khoang.
- Diễn giải: Ma trận hệ cho thấy rõ hướng chuyển dịch và khoang tích lũy chất ô nhiễm.

#### Mô hình dịch tễ SIR
- Bài toán: Theo dõi chuyển dịch của quần thể qua ba trạng thái nhạy cảm, nhiễm và hồi phục.
- Mô hình:
$$
\frac{dS}{dt}=-\beta SI,\qquad
\frac{dI}{dt}=\beta SI-\gamma I,\qquad
\frac{dR}{dt}=\gamma I.
$$
- Giả thiết và giới hạn: Quần thể trộn đều, không xét sinh tử hay di cư trong giai đoạn dịch ngắn hạn.
- Diễn giải: Dù có số hạng phi tuyến $$ \beta SI $$, cấu trúc cân bằng giữa các ngăn vẫn giữ nguyên.

### 2. Trực giác bổ sung và các kết nối

Mô hình ngăn mở rộng phạm vi ứng dụng của hệ ODE sang sinh học, y học và môi trường — nơi việc xác định đúng dấu, đơn vị và định luật bảo toàn tổng lượng quan trọng ngang với kỹ thuật giải phương trình.

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

Xét lại mô hình hai ngăn:
$$
\frac{dx_1}{dt}=-(k_{12}+k_{01})x_1+k_{21}x_2,
\qquad
\frac{dx_2}{dt}=k_{12}x_1-k_{21}x_2.
$$
Cộng hai phương trình thu được $$ \frac{d}{dt}(x_1+x_2)=-k_{01}x_1 $$, khẳng định tổng lượng không bảo toàn do có dòng thải trừ từ ngăn 1. Phép cộng các phương trình là bước kiểm tra nhanh rất hiệu quả trong mô hình hóa.

### 6. Phân tầng độ khó

**Bậc đại học.** Vẽ sơ đồ ngăn, lập đúng dấu phương trình cân bằng và kiểm tra bảo toàn tổng lượng.

**Bậc sau đại học.** So sánh mô hình ngăn tuyến tính và phi tuyến, khảo sát phổ của ma trận ngăn và phân tích độ nhạy tham số.

## Video tham khảo

- Xem trước: [The MATH of Pandemics | Intro to the SIR Model](https://www.youtube.com/watch?v=Qrp40ck3WpI) — Dr. Trefor Bazett, tiếng Anh. Giới thiệu mô hình dịch tễ SIR như một hệ ngăn tiêu biểu.
- [SIR Model for Epidemiology, Ordinary Differential Equations](https://www.youtube.com/watch?v=f1Ewm1hyPWY) — Dr. Bevin Maultsby, tiếng Anh. Trình bày cách viết và đọc các phương trình SIR theo nguyên tắc cân bằng khoang.
- [❖ Mixing Problems and Separable Differential Equations ❖](https://www.youtube.com/watch?v=6wk9zWa-Fww) — Patrick J, tiếng Anh. Bài toán bể trộn — phiên bản một ngăn của cùng nguyên tắc cân bằng dòng vào – dòng ra.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: nhiều ví dụ ứng dụng về mô hình ngăn và hệ tuyến tính.
- Arnold, *Ordinary Differential Equations*: hữu ích cho trực giác về dòng chảy và hệ động lực nhiều biến.
