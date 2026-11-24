---
layout: post
title: "02-02 Hệ số Hằng: Nghiệm Thực Phân biệt"
chapter: '02'
order: 2
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---

Hàm số nào có đạo hàm tỷ lệ với chính nó? Chỉ có hàm mũ $e^{rt}$! Chính phép thử giản dị ấy của Euler đã biến phương trình vi phân cấp hai hệ số hằng $ay'' + by' + cy = 0$ thành một phương trình bậc hai quen thuộc từ trung học $ar^2 + br + c = 0$. Khi biệt thức $\Delta \ge 0$, bài học này giải mã trọn vẹn hai kịch bản nghiệm thực phân biệt và nghiệm thực kép—từ mạch tiêu tán năng lượng đến bộ giảm xóc tắt dần tới hạn.

## Bản đồ kiến thức nền: Bốn trụ cột của Hệ số Hằng Nghiệm Thực

1. **Phương trình đặc trưng $ar^2 + br + c = 0$**:
   Thay $y = e^{rt}$ vào $ay'' + by' + cy = 0$ cho $e^{rt}(ar^2 + br + c) = 0$; vì $e^{rt} > 0$, toàn bộ bài toán vi phân quy về tìm nghiệm đa thức bậc hai.
2. **Trường hợp $\Delta > 0$ (Hai nghiệm thực phân biệt $r_1 \ne r_2$)**:
   Nghiệm tổng quát $y(t) = c_1 e^{r_1 t} + c_2 e^{r_2 t}$; khi $t \to +\infty$, số hạng ứng với nghiệm lớn hơn $\max(r_1, r_2)$ thống trị hành vi dài hạn.
3. **Trường hợp $\Delta = 0$ (Nghiệm thực kép $r_1 = r_2 = r = -b/(2a)$)**:
   Để đủ hai nghiệm độc lập tuyến tính, nghiệm thứ hai là $t e^{rt}$, cho nghiệm tổng quát $y(t) = (c_1 + c_2 t)e^{rt}$.
4. **Dấu của nghiệm & Tính ổn định dài hạn**:
   Mọi nghiệm tiến về $0$ khi $t \to +\infty$ khi và chỉ khi cả hai nghiệm đều âm ($r_1, r_2 < 0$), tương đương $a, b, c$ cùng dấu!

## Mục tiêu
Bài học này giúp sinh viên sử dụng phương trình đặc trưng để giải các ODE tuyến tính cấp hai hệ số hằng, phân biệt trường hợp nghiệm thực phân biệt với nghiệm kép, và diễn giải các thành phần hàm mũ như các thành phần tăng trưởng hoặc suy giảm của hệ. Đây là kỹ thuật nền tảng cho toàn bộ chương.

## Kiến thức nền
Sinh viên cần nắm nguyên lý chồng chất, tính chất của hàm mũ và đạo hàm của $$ e^{rt} $$. Việc quen với cách thử một dạng nghiệm rồi thay vào kiểm tra từ chương trước sẽ giúp phương trình đặc trưng trở nên dễ hiểu hơn.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-02 Hệ số Hằng: Nghiệm Thực Phân biệt]({{ site.imgurl }}/chapter_img/chapter02/02_02_constant_coeff_real_roots.svg)

Khi các hệ số của phương trình là hằng số, phép đạo hàm giữ nguyên dạng của hàm mũ. Vì vậy, với mô hình
$$ ay''+by'+cy=0, $$
ta có cơ sở để thử nghiệm dạng $$ y=e^{rt} $$. Nhờ cách đặt này, bài toán vi phân liên tục được chuyển về bài toán đại số thông qua đa thức đặc trưng.

Quan trọng hơn bản thân công thức là cách đọc ý nghĩa động học của nghiệm. Hai nghiệm thực phân biệt tạo ra hai thành phần nghiệm độc lập với hai tốc độ tăng hoặc suy giảm khác nhau. Nghiệm kép cho thấy hai thành phần bị trùng nhau và cần bổ sung thêm nghiệm dạng $$ te^{rt} $$. Do đó, bài học này vừa cung cấp kỹ thuật giải vừa làm rõ cấu trúc không gian nghiệm.

### Khung giải thích (nên đọc chậm): Giải đối chiếu cả hai trường hợp $\Delta > 0$ và $\Delta = 0$ với cùng điều kiện đầu $y(0) = 1,\; y'(0) = 0$

**Trường hợp 1 ($\Delta > 0$)**: $y'' + 5y' + 6y = 0$.
- Đặc trưng: $r^2 + 5r + 6 = (r + 2)(r + 3) = 0 \implies r_1 = -2,\; r_2 = -3$.
- Nghiệm tổng quát: $y(t) = c_1 e^{-2t} + c_2 e^{-3t}$.
- Điều kiện đầu: $c_1 + c_2 = 1$ và $-2c_1 - 3c_2 = 0 \implies c_1 = 3,\; c_2 = -2$.
- Kết quả: $y_A(t) = \mathbf{3e^{-2t} - 2e^{-3t}}$ (tại $t = 1$: $y_A(1) \approx 0{,}306$).

**Trường hợp 2 ($\Delta = 0$)**: $y'' + 6y' + 9y = 0$.
- Đặc trưng: $(r + 3)^2 = 0 \implies r = -3$ (kép).
- Nghiệm tổng quát: $y(t) = (c_1 + c_2 t)e^{-3t}$.
- Điều kiện đầu: $y(0) = c_1 = 1$; $y'(0) = c_2 - 3c_1 = 0 \implies c_2 = 3$.
- Kết quả: $y_B(t) = \mathbf{(1 + 3t)e^{-3t}}$ (tại $t = 1$: $y_B(1) = 4e^{-3} \approx 0{,}199$, hồi về $0$ nhanh hơn hẳn $y_A$!).

## Khái niệm theo ba cách
### Cách nhìn trực quan
Có thể hình dung hệ có hai tốc độ phản ứng đặc trưng: một thành phần suy giảm nhanh, thành phần kia suy giảm chậm. Nghiệm tổng quát là sự tổ hợp của cả hai. Nếu hai tốc độ trùng nhau, hệ chỉ còn một hướng độc lập nên cần bổ sung một dạng nghiệm đặc biệt để tạo đủ hai nghiệm độc lập tuyến tính.

### Cách nhìn hình ảnh
Với nghiệm thực âm, đồ thị nghiệm suy giảm về 0; với nghiệm thực dương, đồ thị tăng không bị chặn. Nếu một nghiệm dương và một nghiệm âm, hành vi dài hạn thường do thành phần ứng với nghiệm dương chi phối. Khi xuất hiện nghiệm kép, đồ thị vẫn mang dáng dấp hàm mũ nhưng có thêm thừa số $$ t $$ làm thay đổi tốc độ chuyển tiếp.

### Cách nhìn hình thức
Xét phương trình thuần nhất
$$ ay''+by'+cy=0,\qquad a\neq 0. $$
Thử nghiệm $$ y=e^{rt} $$, ta thu được phương trình đặc trưng
$$ ar^2+br+c=0. $$
Nếu phương trình đặc trưng có hai nghiệm thực phân biệt $$ r_1\neq r_2 $$, nghiệm tổng quát là
$$ y(t)=c_1e^{r_1t}+c_2e^{r_2t}. $$
Nếu có nghiệm kép $$ r $$, nghiệm tổng quát là
$$ y(t)=\left(c_1+c_2t\right)e^{rt}. $$

## Những ngộ nhận thường gặp
- "Phương trình đặc trưng chỉ là mẹo nhớ." Sai: nó xuất phát trực tiếp từ việc họ hàm mũ đóng dưới phép đạo hàm.
- "Nghiệm kép chỉ cho một nghiệm $$ e^{rt} $$ nên không viết được nghiệm tổng quát." Sai: ta có nghiệm thứ hai độc lập tuyến tính là $$ te^{rt} $$.
- "Giải xong phương trình đặc trưng là kết thúc bài toán." Chưa đủ: cần áp dụng điều kiện đầu và diễn giải hành vi nghiệm.
- "Dấu của nghiệm đặc trưng không quan trọng." Sai: dấu của nghiệm quyết định hệ tăng trưởng, suy giảm hay tiến về cân bằng.

## Tiến trình học tập đề xuất
### Bước 1: Viết phương trình đặc trưng
Chuyển ODE sang phương trình đa thức theo biến $$ r $$.

### Bước 2: Phân loại nghiệm đặc trưng
Xác định trường hợp hai nghiệm thực phân biệt hay nghiệm kép.

### Bước 3: Viết đúng dạng nghiệm tổng quát
Đây là bước thường dễ nhầm khi gặp nghiệm kép.

### Bước 4: Áp dụng điều kiện đầu
Tìm các hằng số và xác định thành phần nghiệm chi phối về dài hạn.

### Các checkpoint
- Sinh viên có viết đúng đa thức đặc trưng hay không.
- Sinh viên có phân biệt được trường hợp nghiệm phân biệt và nghiệm kép hay không.
- Sinh viên có suy ra được hành vi dài hạn từ dấu của các nghiệm hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Hai nghiệm thực phân biệt
Giải phương trình
$$ y''-3y'+2y=0. $$
Phương trình đặc trưng là $$ r^2-3r+2=0 $$, phân tích thành
$$ \left(r-1\right)\left(r-2\right)=0, $$
nên $$ r_1=1 $$ và $$ r_2=2 $$. Nghiệm tổng quát là
$$ y(t)=c_1e^t+c_2e^{2t}. $$
Vì cả hai nghiệm đặc trưng đều dương, mọi nghiệm không tầm thường đều tăng khi $$ t $$ lớn.

### Ví dụ 2: Áp dụng điều kiện đầu
Với cùng phương trình trên, giả sử $$ y(0)=4 $$ và $$ y'(0)=5 $$. Ta có $$ y(0)=c_1+c_2=4 $$. Mặt khác,
$$ y'(t)=c_1e^t+2c_2e^{2t}, $$
nên $$ y'(0)=c_1+2c_2=5 $$. Trừ hai phương trình cho nhau, ta được $$ c_2=1 $$ và $$ c_1=3 $$. Vậy
$$ y(t)=3e^t+e^{2t}. $$
Khi $$ t\to \infty $$, thành phần $$ e^{2t} $$ chi phối hành vi của nghiệm.

### Ví dụ 3: Nghiệm kép
Giải phương trình
$$ y''-4y'+4y=0. $$
Phương trình đặc trưng là
$$ r^2-4r+4=0=\left(r-2\right)^2, $$
có nghiệm kép $$ r=2 $$. Vì vậy nghiệm tổng quát là
$$ y(t)=\left(c_1+c_2t\right)e^{2t}. $$
Một lỗi phổ biến là chỉ viết $$ c_1e^{2t}+c_2e^{2t} $$, nhưng hai số hạng này không độc lập tuyến tính.

### Ví dụ 4: Nghiệm suy giảm
Giải phương trình
$$ y''+5y'+6y=0. $$
Phương trình đặc trưng $$ r^2+5r+6=0 $$ có nghiệm $$ r=-2 $$ và $$ r=-3 $$. Do đó
$$ y(t)=c_1e^{-2t}+c_2e^{-3t}. $$
Cả hai thành phần đều suy giảm về 0, nên hệ ổn định theo nghĩa nghiệm tiến về cân bằng 0. Thành phần $$ e^{-2t} $$ suy giảm chậm hơn và chi phối hành vi về lâu dài.

## Câu hỏi khái niệm
1. Vì sao việc thử nghiệm dạng $$ e^{rt} $$ đặc biệt phù hợp khi các hệ số là hằng?
2. Vì sao nghiệm kép đòi hỏi bổ sung nghiệm thứ hai dạng $$ te^{rt} $$?
3. Từ dấu của nghiệm đặc trưng, ta suy ra được điều gì về tính ổn định hoặc tăng trưởng của hệ?

## Bài toán ứng dụng
1. Một hệ cơ học có hai thành phần tắt dần với tốc độ khác nhau. Hãy giải thích vì sao thành phần suy giảm chậm hơn quyết định hành vi dài hạn.
2. Trong mô hình tăng trưởng dân số tuyến tính hóa quanh điểm cân bằng, một nghiệm đặc trưng dương cho biết điều gì về tính ổn định?
3. Một tín hiệu điện có hai thành phần quá độ dạng hàm mũ. Hãy giải thích vì sao thành phần có tốc độ suy giảm nhỏ hơn được quan sát lâu hơn.

## Chiến lược giảng dạy tương tác
- Cho sinh viên dự đoán hình dạng đồ thị từ nghiệm đặc trưng trước khi giải chi tiết.
- Yêu cầu lớp so sánh một bài có nghiệm thực phân biệt với một bài có nghiệm kép và diễn đạt bằng lời điểm khác biệt cốt lõi.
- Cho sinh viên làm nhanh bài tập ghép cặp giữa phương trình đặc trưng và dạng nghiệm tương ứng.
- Đặt câu hỏi: "Nếu một nghiệm đặc trưng âm và một nghiệm dương, điều gì xảy ra khi $$ t $$ lớn?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên làm theo quy trình bốn bước cố định: viết phương trình đặc trưng, giải phương trình bậc hai, phân loại nghiệm và chọn dạng nghiệm tổng quát. Việc luyện theo cấu trúc lặp lại giúp hạn chế sai sót hình thức.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên chứng minh trực tiếp rằng $$ te^{rt} $$ là nghiệm khi $$ r $$ là nghiệm kép, hoặc liên hệ bội của nghiệm đặc trưng với số nghiệm độc lập tuyến tính cần xây dựng.

## Tóm tắt dễ nhớ
Với ODE cấp hai hệ số hằng thuần nhất, bước mấu chốt là thử $$ e^{rt} $$ để chuyển về phương trình đặc trưng. Hai nghiệm thực phân biệt cho hai thành phần hàm mũ độc lập; nghiệm kép cho dạng $$ \left(c_1+c_2t\right)e^{rt} $$. Dấu của nghiệm đặc trưng cho biết hệ tăng trưởng hay suy giảm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ cơ học quá tắt dần
- Bài toán: Một cửa giảm chấn hoặc bộ giảm xóc quay về vị trí cân bằng mà không dao động.
- Mô hình:
$$ m x''+c x'+k x=0,\qquad c^2>4mk. $$
- Giả thiết và giới hạn: Mô hình tuyến tính, dao động nhỏ và các tham số không đổi.
- Diễn giải: Hai nghiệm thực âm phân biệt tạo ra hai tốc độ suy giảm khác nhau; thành phần suy giảm chậm hơn chi phối hành vi dài hạn.

#### Tín hiệu điện có hai hằng số thời gian
- Bài toán: Một mạch lọc bậc hai cho đáp ứng quá độ gồm hai thành phần mũ tắt dần.
- Mô hình: $$ y''+a y'+b y=0 $$, với phương trình đặc trưng có hai nghiệm thực phân biệt.
- Giả thiết và giới hạn: Hệ số hằng và mạch làm việc trong vùng tuyến tính quanh điểm cân bằng.
- Diễn giải: Hai nghiệm đặc trưng tương ứng với hai tốc độ tắt dần khác nhau của tín hiệu quá độ.

#### Tuyến tính hóa quanh cân bằng trong sinh học
- Bài toán: Gần một điểm cân bằng, một mô hình phi tuyến có thể được xấp xỉ bởi ODE tuyến tính có nghiệm dạng hàm mũ.
- Mô hình mẫu: $$ y''-3y'+2y=0 $$.
- Giả thiết và giới hạn: Phép xấp xỉ chỉ đáng tin cậy gần điểm cân bằng và trên khoảng thời gian hữu hạn.
- Diễn giải: Nghiệm thực dương cho thấy sự mất ổn định, còn nghiệm thực âm cho thấy xu hướng trở về cân bằng.

### 2. Trực giác bổ sung và các kết nối

Phương trình đặc trưng minh họa cách giải một bài toán vi phân bằng cách tìm họ hàm bất biến dưới phép đạo hàm. Nội dung này nối trực tiếp sang chương hệ ODE, nơi phương trình đặc trưng xuất hiện dưới dạng đa thức đặc trưng của ma trận. Một ngộ nhận phổ biến là cho rằng độ lớn của các hệ số $$ c_1,c_2 $$ quyết định hành vi lâu dài; thực tế, phần số mũ mới là yếu tố chi phối khi $$ t $$ lớn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 400)
curves = [
    (np.exp(-t) - np.exp(-3*t), "e^{-t} - e^{-3t}"),
    (2*np.exp(-t) + 0.5*np.exp(-3*t), "2e^{-t} + 0.5e^{-3t}"),
    (np.exp(t) - 0.2*np.exp(-2*t), "e^{t} - 0.2e^{-2t}"),
]

for y, label in curves:
    plt.plot(t, y, label=label)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Các mode mũ với nghiệm thực phân biệt")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy chỉ cần một thành phần số mũ dương có hệ số ban đầu rất nhỏ cũng đủ làm quỹ đạo tăng không bị chặn về sau, dù ban đầu thành phần suy giảm có thể lấn át.

### 4. Gợi ý tìm thêm mô phỏng

- search: overdamped second order response plot
- search: two real roots transient response
- search: damping modes engineering visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét bộ giảm chấn đơn giản
$$ x''+4x'+3x=0,\qquad x(0)=1,\qquad x'(0)=0. $$
Phương trình đặc trưng là $$ r^2+4r+3=0=(r+1)(r+3) $$, nên $$ x(t)=c_1e^{-t}+c_2e^{-3t} $$. Áp dụng điều kiện đầu, ta thu được
$$ x(t)=\frac{3}{2}e^{-t}-\frac{1}{2}e^{-3t}. $$
Nghiệm cho thấy hệ không dao động, và về dài hạn thành phần $$ e^{-t} $$ chi phối hoàn toàn. Đây là trực giác quan trọng khi phân tích đáp ứng quá độ trong kỹ thuật.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo việc viết phương trình đặc trưng, phân biệt nghiệm phân biệt với nghiệm kép và đọc tính tăng hay giảm từ dấu của nghiệm.

**Bậc sau đại học.** Kết nối với phổ của toán tử tuyến tính, thành phần chi phối dài hạn theo phần thực lớn nhất và dạng ma trận đồng hành (companion matrix).

## Video tham khảo

- Xem trước: [How to Solve Constant Coefficient Homogeneous Differential Equations](https://www.youtube.com/watch?v=znO6v-8pvXo) — Dr. Trefor Bazett, tiếng Anh. Giới thiệu phương trình đặc trưng và các nghiệm hàm mũ cho phương trình hệ số hằng.
- [Homogeneous Constant Coefficient Equations: Real Roots | MIT 18.03SC Differential Equations](https://www.youtube.com/watch?v=zNPK_t03zds) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT tập trung vào trường hợp nghiệm thực của đa thức đặc trưng.
- [Constant Coefficient ODEs: Real & Distinct vs Real & Repeated vs Complex Pair](https://www.youtube.com/watch?v=r8Uk4tbuxVE) — Dr. Trefor Bazett, tiếng Anh. So sánh ba trường hợp nghiệm thực phân biệt, nghiệm kép và cặp nghiệm phức.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày đầy đủ kỹ thuật phương trình đặc trưng.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện về nghiệm phân biệt và nghiệm kép.
- Ross — *Differential Equations*: hữu ích để ôn nhanh cách xác định thành phần nghiệm chi phối.
