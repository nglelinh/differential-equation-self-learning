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
## Mục tiêu
Bài học này giúp sinh viên sử dụng phương trình đặc trưng để giải các ODE tuyến tính cấp hai hệ số hằng, nhận ra sự khác biệt giữa nghiệm thực phân biệt và nghiệm kép, và diễn giải các mode mũ như những thành phần tăng trưởng hoặc suy giảm của hệ. Đây là bước kỹ thuật nền tảng cho toàn bộ chương.

## Kiến thức nền
Sinh viên cần nắm nguyên lý chồng chập, kiến thức về hàm mũ và đạo hàm của $$ e^{rt} $$. Việc quen với cách "thử một dạng nghiệm rồi kiểm tra" từ chương trước sẽ giúp phương trình đặc trưng hiện ra như một ý tưởng rất tự nhiên.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-02 Hệ số Hằng: Nghiệm Thực Phân biệt]({{ site.imgurl }}/chapter_img/chapter02/02_02_constant_coeff_real_roots.svg)

Khi hệ số của phương trình là hằng, ta có một lợi thế lớn: phép đạo hàm không làm thay đổi bản chất của hàm mũ. Vì vậy, nếu mô hình có dạng
$$ ay''+by'+cy=0, $$
ta có cơ sở để thử
$$ y=e^{rt}. $$
Đây là một trong những khoảnh khắc đẹp nhất của giải tích ứng dụng: một bài toán vi phân liên tục được chuyển thành bài toán đại số rời rạc qua đa thức đặc trưng.

Điều quan trọng hơn công thức là cách đọc ý nghĩa của nghiệm. Hai nghiệm thực phân biệt cho hai mode độc lập, thường là hai tốc độ tăng hoặc suy giảm khác nhau. Nghiệm kép cho thấy hệ có sự trùng mode và cần một nghiệm bổ sung dạng $$ te^{rt} $$. Bài học vì thế vừa là kỹ thuật giải, vừa là bài học về cấu trúc nghiệm.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy tưởng tượng hệ có hai "nhịp phản ứng" khác nhau. Một mode có thể suy giảm nhanh, mode kia suy giảm chậm. Nghiệm tổng là sự pha trộn của cả hai. Nếu hai nhịp trùng nhau, hệ mất đi một hướng độc lập và ta phải tìm thêm một mode đặc biệt để bù lại.

### Cách nhìn hình ảnh
Với nghiệm thực âm, đồ thị thường suy giảm về 0. Với nghiệm thực dương, đồ thị tăng bùng. Nếu một nghiệm dương, một nghiệm âm, ta thường có hành vi bị chi phối dài hạn bởi mode dương. Khi nghiệm kép xuất hiện, đồ thị vẫn giống một hàm mũ nhưng có thêm yếu tố $$ t $$ làm thay đổi tốc độ chuyển tiếp.

### Cách nhìn hình thức
Xét phương trình thuần nhất
$$ ay''+by'+cy=0,\qquad a\neq 0. $$
Thử nghiệm
$$ y=e^{rt} $$
ta được
$$ ar^2+br+c=0. $$
Đây là phương trình đặc trưng. Nếu có hai nghiệm thực phân biệt $$ r_1\neq r_2 $$, nghiệm tổng quát là
$$ y(t)=c_1e^{r_1t}+c_2e^{r_2t}. $$
Nếu có nghiệm kép $$ r $$, nghiệm tổng quát là
$$ y(t)=\left(c_1+c_2t\right)e^{rt}. $$

## Những ngộ nhận thường gặp
- "Phương trình đặc trưng chỉ là mẹo nhớ." Sai. Nó đến trực tiếp từ việc hàm mũ là họ đóng dưới phép đạo hàm.
- "Nghiệm kép chỉ cho một nghiệm $$ e^{rt} $$ nên không thể giải bài toán." Sai. Ta còn có nghiệm thứ hai độc lập $$ te^{rt} $$.
- "Chỉ cần giải phương trình đặc trưng là xong." Chưa đủ. Còn phải áp điều kiện đầu và diễn giải hành vi nghiệm.
- "Dấu của nghiệm đặc trưng không quan trọng." Sai. Nó quyết định hệ tăng, giảm hay tiến về cân bằng.

## Tiến trình học tập đề xuất
### Bước 1: Viết phương trình đặc trưng
Chuyển ODE sang đa thức theo $$ r $$.

### Bước 2: Phân loại nghiệm đặc trưng
Xác định có hai nghiệm thực phân biệt hay nghiệm kép.

### Bước 3: Viết nghiệm tổng quát đúng dạng
Đây là bước sinh viên thường nhầm nhất khi gặp nghiệm kép.

### Bước 4: Dùng điều kiện đầu
Tìm các hằng số và đọc mode chi phối dài hạn.

### Các checkpoint
- Sinh viên có viết đúng đa thức đặc trưng hay không.
- Sinh viên có phân biệt được nghiệm phân biệt và nghiệm kép hay không.
- Sinh viên có diễn giải được hành vi dài hạn từ dấu của các nghiệm hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Hai nghiệm thực phân biệt
Giải
$$ y''-3y'+2y=0. $$
Phương trình đặc trưng là
$$ r^2-3r+2=0, $$
phân tích thành
$$ \left(r-1\right)\left(r-2\right)=0. $$
Do đó
$$ r_1=1,\qquad r_2=2. $$
Nghiệm tổng quát:
$$ y(t)=c_1e^t+c_2e^{2t}. $$
Vì cả hai nghiệm đặc trưng đều dương, mọi nghiệm không tầm thường đều tăng khi $$ t $$ lớn.

### Ví dụ 2: Áp điều kiện đầu
Với cùng phương trình, giả sử
$$ y(0)=4,\qquad y'(0)=5. $$
Ta có
$$ y(0)=c_1+c_2=4. $$
Mặt khác
$$ y'(t)=c_1e^t+2c_2e^{2t}, $$
nên
$$ y'(0)=c_1+2c_2=5. $$
Trừ hai phương trình cho nhau:
$$ c_2=1,\qquad c_1=3. $$
Vậy
$$ y(t)=3e^t+e^{2t}. $$
Khi $$ t\to \infty $$, mode $$ e^{2t} $$ chi phối.

### Ví dụ 3: Nghiệm kép
Giải
$$ y''-4y'+4y=0. $$
Phương trình đặc trưng:
$$ r^2-4r+4=0=\left(r-2\right)^2. $$
Ta có nghiệm kép $$ r=2 $$. Vì vậy nghiệm tổng quát là
$$ y(t)=\left(c_1+c_2t\right)e^{2t}. $$
Nhiều sinh viên mắc lỗi viết chỉ $$ c_1e^{2t}+c_2e^{2t} $$, nhưng hai hạng ấy không độc lập tuyến tính.

### Ví dụ 4: Nghiệm suy giảm
Giải
$$ y''+5y'+6y=0. $$
Phương trình đặc trưng:
$$ r^2+5r+6=0, $$
cho
$$ r=-2,\qquad r=-3. $$
Vậy
$$ y(t)=c_1e^{-2t}+c_2e^{-3t}. $$
Cả hai mode đều suy giảm về 0, nên hệ ổn định theo nghĩa nghiệm tiến về cân bằng 0. Mode $$ e^{-2t} $$ suy giảm chậm hơn và chi phối lâu dài.

## Câu hỏi khái niệm
1. Vì sao việc thử $$ e^{rt} $$ lại hợp lý đặc biệt khi hệ số là hằng?
2. Vì sao nghiệm kép đòi hỏi nghiệm thứ hai dạng $$ te^{rt} $$?
3. Từ dấu của nghiệm đặc trưng, ta đọc được gì về ổn định hay tăng trưởng của hệ?

## Bài toán ứng dụng
1. Một hệ cơ học có hai mode tắt dần với tốc độ khác nhau. Hãy giải thích vì sao mode suy giảm chậm hơn quyết định hành vi dài hạn.
2. Trong mô hình tăng trưởng dân số tuyến tính hóa quanh cân bằng, một nghiệm đặc trưng dương gợi ý điều gì về ổn định?
3. Một tín hiệu điện có hai thành phần quá độ mũ. Hãy giải thích vì sao thành phần có tốc độ suy giảm nhỏ hơn sẽ được quan sát lâu hơn.

## Chiến lược giảng dạy tương tác
- Cho sinh viên đoán trước hình dạng đồ thị từ nghiệm đặc trưng mà không giải chi tiết.
- Yêu cầu lớp so sánh hai bài: một có nghiệm thực phân biệt, một có nghiệm kép, rồi nói bằng lời điểm khác nhau thực sự.
- Cho sinh viên làm nhanh bài tập ghép cặp giữa phương trình đặc trưng và dạng nghiệm tương ứng.
- Hỏi lớp: "Nếu một nghiệm đặc trưng âm và một nghiệm dương, em dự đoán điều gì xảy ra khi $$ t $$ lớn?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên dùng bảng thao tác cố định: viết đặc trưng, giải phương trình bậc hai, phân loại nghiệm, chọn dạng nghiệm tổng quát. Việc luyện cấu trúc lặp lại giúp giảm lỗi hình thức.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi chứng minh trực tiếp rằng $$ te^{rt} $$ là nghiệm khi $$ r $$ là nghiệm kép, hoặc liên hệ đa bội của nghiệm đặc trưng với số nghiệm độc lập cần dựng.

## Tóm tắt dễ nhớ
Với ODE cấp hai hệ số hằng thuần nhất, chìa khóa là thử $$ e^{rt} $$ để chuyển sang phương trình đặc trưng. Hai nghiệm thực phân biệt cho hai mode mũ độc lập. Nghiệm kép cho dạng $$ \left(c_1+c_2t\right)e^{rt} $$. Dấu của nghiệm đặc trưng cho biết hệ tăng hay suy giảm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ cơ học quá tắt dần
- Bài toán: Một cửa giảm chấn hoặc bộ giảm xóc quay về cân bằng mà không dao động.
- Mô hình:
$$ m x''+c x'+k x=0,\qquad c^2>4mk. $$
- Giả thiết và giới hạn: Mô hình tuyến tính, dao động nhỏ, tham số không đổi.
- Diễn giải: Hai nghiệm thực âm phân biệt tạo ra hai mode suy giảm khác nhau; mode suy giảm chậm chi phối hành vi dài hạn.

#### Tín hiệu điện có hai hằng số thời gian
- Bài toán: Một mạch lọc bậc hai cho đáp ứng quá độ gồm hai thành phần mũ tắt dần.
- Mô hình:
$$ y''+a y'+b y=0, $$
với phương trình đặc trưng có hai nghiệm thực phân biệt.
- Giả thiết và giới hạn: Hệ số hằng và mạch tuyến tính quanh điểm làm việc.
- Diễn giải: Hai nghiệm đặc trưng cho thấy hệ có hai "tốc độ quên" khác nhau.

#### Tuyến tính hóa quanh cân bằng trong sinh học
- Bài toán: Gần một điểm cân bằng, một mô hình phi tuyến có thể được xấp xỉ bởi ODE tuyến tính với nghiệm mũ.
- Mô hình:
$$ y''-3y'+2y=0 $$
như một bài mẫu cấu trúc.
- Giả thiết và giới hạn: Xấp xỉ chỉ đáng tin gần cân bằng và trong thời gian không quá dài.
- Diễn giải: Nghiệm thực dương báo hiệu mất ổn định, còn nghiệm âm báo hiệu xu hướng quay về cân bằng.

### 2. Trực giác bổ sung và các kết nối

Phương trình đặc trưng là một ví dụ rất đẹp cho việc giải một bài toán vi phân bằng cách tìm họ hàm bất biến dưới phép đạo hàm. Bài học này nối trực tiếp với chương hệ ODE, nơi phương trình đặc trưng sẽ xuất hiện dưới dạng đa thức đặc trưng của ma trận. Một ngộ nhận phổ biến là nghĩ hệ số $$ c_1,c_2 $$ lớn hay nhỏ mới quyết định lâu dài; thực ra phần mũ mới là yếu tố thống trị hành vi khi $$ t $$ lớn.

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

Sinh viên sẽ thấy rõ chỉ cần một mode dương rất nhỏ cũng đủ làm quỹ đạo cuối cùng tăng bùng, dù ban đầu mode suy giảm có thể lấn át.

### 4. Gợi ý tìm thêm mô phỏng

- search: overdamped second order response plot
- search: two real roots transient response
- search: damping modes engineering visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét bộ giảm chấn đơn giản
$$ x''+4x'+3x=0,\qquad x(0)=1,\qquad x'(0)=0. $$
Phương trình đặc trưng là
$$ r^2+4r+3=0=(r+1)(r+3), $$
nên
$$ x(t)=c_1e^{-t}+c_2e^{-3t}. $$
Áp điều kiện đầu:
$$ x(t)=\frac{3}{2}e^{-t}-\frac{1}{2}e^{-3t}. $$
Nghiệm cho thấy hệ không dao động, và về dài hạn thành phần $$ e^{-t} $$ chi phối hoàn toàn. Đây là trực giác rất quan trọng cho việc đọc đáp ứng quá độ kỹ thuật.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo viết phương trình đặc trưng, phân biệt nghiệm phân biệt và nghiệm kép, rồi đọc tăng hay giảm từ dấu nghiệm.

**Bậc sau đại học.** Kết nối với phổ của toán tử tuyến tính, chi phối lâu dài bởi phần thực lớn nhất, và tổng quát hóa sang ma trận companion.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: rất mạnh ở kỹ thuật phương trình đặc trưng.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài luyện về nghiệm phân biệt và nghiệm kép.
- Ross — *Differential Equations*: hữu ích để ôn nhanh cách đọc mode chi phối.
