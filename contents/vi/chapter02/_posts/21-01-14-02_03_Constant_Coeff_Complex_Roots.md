---
layout: post
title: "02-03 Hệ số Hằng: Nghiệm Phức"
chapter: '02'
order: 3
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu nguồn gốc của nghiệm phức trong phương trình đặc trưng, chuyển chúng về nghiệm thực bằng công thức Euler, và diễn giải ý nghĩa của phần thực và phần ảo trong động học dao động. Đây là bài học trung tâm để sinh viên đọc được dao động điều hòa, dao động tắt dần và cộng hưởng ở các bài ứng dụng sau.

## Kiến thức nền
Sinh viên nên nắm phương trình đặc trưng với hệ số hằng, số phức cơ bản và công thức Euler
$$ e^{i\theta}=\cos \theta+i\sin \theta. $$
Nếu sinh viên còn yếu ở số phức, giảng viên nên nhắc lại ngắn gọn trước khi đi vào kỹ thuật giải.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-03 Hệ số Hằng: Nghiệm Phức]({{ site.imgurl }}/chapter_img/chapter02/02_03_constant_coeff_complex_roots.svg)

Khi phương trình đặc trưng không có nghiệm thực, nhiều sinh viên thường lo rằng mô hình mất ý nghĩa vật lý. Thực ra điều ngược lại mới đúng: nghiệm phức thường là tín hiệu của dao động. Hệ lò xo lý tưởng, mạch LC và nhiều hiện tượng sóng đều dẫn tới nghiệm phức. Phần ảo không phải là vật thể "ảo", mà là cách đại số mã hóa tần số dao động.

Điểm đẹp của bài học này là số phức xuất hiện như công cụ trung gian, nhưng kết quả cuối cùng vẫn là nghiệm thực. Nhờ công thức Euler, cặp nghiệm liên hợp tạo ra cặp hàm sin và cos, còn phần thực của nghiệm đặc trưng điều khiển biên độ tăng hay giảm theo thời gian.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Một nghiệm phức liên hợp giống như một nhịp quay trong mặt phẳng. Khi ta nhìn chuyển động quay ấy chỉ qua một trục, ta thấy sin và cos. Nếu vòng quay đồng thời co lại, ta được dao động tắt dần. Nếu nó nở ra, ta được dao động tăng biên.

### Cách nhìn hình ảnh
Với nghiệm đặc trưng
$$ r=\alpha\pm i\beta, $$
đồ thị nghiệm có dạng
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Nếu $$ \alpha=0 $$, biên độ giữ nguyên. Nếu $$ \alpha<0 $$, biên độ tắt dần. Nếu $$ \alpha>0 $$, biên độ lớn dần. Trong khi đó $$ \beta $$ quyết định tốc độ dao động, tức là tần số góc.

### Cách nhìn hình thức
Với phương trình
$$ ay''+by'+cy=0, $$
nếu phương trình đặc trưng
$$ ar^2+br+c=0 $$
có nghiệm
$$ r=\alpha\pm i\beta,\qquad \beta\neq 0, $$
thì nghiệm tổng quát thực là
$$
y(t)=e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Điều này đến từ
$$
e^{(\alpha+i\beta)t}=e^{\alpha t}\left(\cos \beta t+i\sin \beta t\right).
$$

## Những ngộ nhận thường gặp
- "Nghiệm phức nghĩa là nghiệm vật lý không có thật." Sai. Kết quả cuối cùng vẫn là nghiệm thực.
- "Phần ảo của nghiệm đặc trưng làm nghiệm trở nên phức tạp hơn nhưng không có ý nghĩa." Sai. Nó chính là tần số dao động.
- "Nếu có sin-cos thì hệ chắc chắn ổn định." Sai. Còn phụ thuộc vào phần thực $$ \alpha $$.
- "Mọi dao động đều có biên độ không đổi." Sai. Dao động tắt dần và dao động tăng biên xuất hiện tự nhiên khi $$ \alpha\neq 0 $$.

## Tiến trình học tập đề xuất
### Bước 1: Giải phương trình đặc trưng
Kiểm tra biệt thức âm để nhận ra nghiệm phức.

### Bước 2: Viết nghiệm dạng mũ phức
Đây là bước trung gian, không phải đích cuối cùng.

### Bước 3: Dùng Euler để chuyển về nghiệm thực
Đây là cây cầu quan trọng giữa đại số và hình học.

### Bước 4: Đọc phần thực và phần ảo
Phần thực chi phối biên độ, phần ảo chi phối tần số.

### Các checkpoint
- Sinh viên có chuyển đúng từ $$ e^{(\alpha+i\beta)t} $$ sang sin-cos hay không.
- Sinh viên có giải thích được vai trò của $$ \alpha $$ và $$ \beta $$ hay không.
- Sinh viên có nhận ra sự khác nhau giữa dao động điều hòa và dao động tắt dần hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Dao động điều hòa thuần
Giải
$$ y''+4y=0. $$
Phương trình đặc trưng:
$$ r^2+4=0, $$
nên
$$ r=\pm 2i. $$
Do đó
$$ y(t)=c_1\cos 2t+c_2\sin 2t. $$
Đây là dao động điều hòa với tần số góc 2 và biên độ không đổi.

### Ví dụ 2: Dao động tắt dần
Giải
$$ y''+2y'+5y=0. $$
Phương trình đặc trưng:
$$ r^2+2r+5=0. $$
Ta có
$$ r=-1\pm 2i. $$
Vậy nghiệm tổng quát là
$$ y(t)=e^{-t}\left(c_1\cos 2t+c_2\sin 2t\right). $$
Phần mũ $$ e^{-t} $$ làm biên độ suy giảm theo thời gian, còn $$ 2 $$ là tần số dao động.

### Ví dụ 3: Áp điều kiện đầu
Với phương trình
$$ y''+2y'+5y=0, $$
giả sử
$$ y(0)=1,\qquad y'(0)=0. $$
Từ $$ y(0)=1 $$ suy ra
$$ c_1=1. $$
Ta tính
$$
y'(t)=e^{-t}\left[-c_1\cos 2t-c_2\sin 2t-2c_1\sin 2t+2c_2\cos 2t\right].
$$
Thay $$ t=0 $$:
$$ y'(0)=-c_1+2c_2=0. $$
Vì $$ c_1=1 $$ nên
$$ 2c_2=1 \Rightarrow c_2=\frac{1}{2}. $$
Vậy
$$
y(t)=e^{-t}\left(\cos 2t+\frac{1}{2}\sin 2t\right).
$$

### Ví dụ 4: Dao động tăng biên
Giải
$$ y''-2y'+5y=0. $$
Phương trình đặc trưng:
$$ r^2-2r+5=0, $$
nên
$$ r=1\pm 2i. $$
Do đó
$$ y(t)=e^t\left(c_1\cos 2t+c_2\sin 2t\right). $$
Ở đây hệ vẫn dao động nhưng biên độ tăng theo $$ e^t $$. Điều này giúp sinh viên hiểu rất rõ ý nghĩa của phần thực dương.

## Câu hỏi khái niệm
1. Vì sao nghiệm phức của phương trình đặc trưng lại dẫn đến sin và cos trong nghiệm thực?
2. Phần thực và phần ảo của nghiệm đặc trưng mã hóa hai thông tin vật lý nào?
3. Vì sao hai hệ đều dao động nhưng một hệ tắt dần còn hệ kia phình biên?

## Bài toán ứng dụng
1. Một hệ lò xo có lực cản nhỏ dao động quanh cân bằng. Hãy giải thích vì sao nghiệm mong đợi phải là dao động tắt dần chứ không phải sin-cos thuần.
2. Một mạch điện có dao động điện áp nhưng năng lượng bị tiêu hao dần. Phần nào của nghiệm đặc trưng phản ánh điều đó?
3. Một hệ điều khiển có tín hiệu dao động ngày càng lớn. Hãy giải thích vì sao điều này gợi ý phần thực dương trong nghiệm đặc trưng.

## Chiến lược giảng dạy tương tác
- Cho sinh viên nhìn ba đồ thị: biên độ không đổi, tắt dần, tăng biên, rồi yêu cầu đoán dấu của $$ \alpha $$.
- Tổ chức một hoạt động "dịch ngôn ngữ": từ nghiệm đặc trưng $$ -1\pm 3i $$ sang mô tả bằng lời "dao động tắt dần với tần số 3".
- Yêu cầu sinh viên tự chứng minh lại công thức nghiệm thực từ Euler theo nhóm nhỏ.
- Khuyến khích sinh viên biểu diễn nghiệm dưới dạng biên độ-pha nếu đã sẵn sàng để tăng trực giác.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên yếu dùng bảng hai bước cố định: giải đặc trưng, rồi áp mẫu
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Việc tách riêng vai trò của $$ \alpha $$ và $$ \beta $$ bằng màu sắc hoặc sơ đồ thường rất hiệu quả.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi viết nghiệm dưới dạng
$$ Re^{\alpha t}\cos \left(\beta t-\phi\right) $$
và giải thích ý nghĩa của biên độ đầu, pha ban đầu và tốc độ tắt dần.

## Tóm tắt dễ nhớ
Nghiệm phức không làm bài toán kém thực tế; nó là cách toán học mã hóa dao động. Nếu
$$ r=\alpha\pm i\beta, $$
thì nghiệm là
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Hãy nhớ: $$ \alpha $$ điều khiển biên độ, $$ \beta $$ điều khiển tần số.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động của khối lượng - lò xo không tắt
- Bài toán: Một vật gắn lò xo lý tưởng dao động quanh cân bằng với biên độ không đổi.
- Mô hình:
$$ x''+\omega^2 x=0. $$
- Giả thiết và giới hạn: Không có ma sát, lò xo tuyến tính, không có ngoại lực.
- Diễn giải: Nghiệm phức $$ \pm i\omega $$ được đọc vật lý như tần số dao động chứ không phải "nghiệm vô nghĩa".

#### Dao động tắt dần trong cảm biến cơ điện
- Bài toán: Một đầu đo rung sau cú va nhẹ rồi dần ổn định.
- Mô hình:
$$ x''+2\zeta\omega_n x'+\omega_n^2 x=0. $$
- Giả thiết và giới hạn: Giảm chấn tuyến tính, dao động nhỏ, thông số không đổi.
- Diễn giải: Phần thực âm làm biên độ tắt dần, phần ảo giữ vai trò nhịp dao động.

#### Mạch LC hoặc RLC dưới tắt
- Bài toán: Điện tích trong mạch điện dao động do trao đổi năng lượng giữa từ trường và điện trường.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=0. $$
- Giả thiết và giới hạn: Linh kiện lý tưởng và tuyến tính.
- Diễn giải: Nghiệm dạng sin-cos nhân mũ cho thấy mạch vừa "rung" vừa tiêu tán năng lượng.

### 2. Trực giác bổ sung và các kết nối

Nghiệm phức xuất hiện vì hình học quay trong mặt phẳng là cách tự nhiên để mã hóa dao động. Khi chiếu chuyển động quay đó xuống trục thực, ta thấy sin và cos. Bài học này là điểm giao nhau giữa đại số, hình học và vật lý. Một bẫy phổ biến là nhớ công thức
$$ e^{\alpha t}(c_1\cos \beta t+c_2\sin \beta t) $$
nhưng quên mất ý nghĩa: $$ \alpha $$ điều khiển bao biên độ, còn $$ \beta $$ điều khiển tốc độ dao động.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
signals = [
    (np.cos(3*t), "alpha=0, beta=3"),
    (np.exp(-0.4*t)*np.cos(3*t), "alpha=-0.4, beta=3"),
    (np.exp(0.2*t)*np.cos(3*t), "alpha=0.2, beta=3"),
]

for y, label in signals:
    plt.plot(t, y, label=label)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Ảnh hưởng của phần thực alpha lên dao động")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Ba đường cong giúp sinh viên phân biệt ngay dao động điều hòa, dao động tắt dần và dao động tăng biên.

### 4. Gợi ý tìm thêm mô phỏng

- search: damped oscillation envelope interactive
- search: complex roots oscillation visualization
- search: Euler formula sine cosine dynamics

### 5. Bài toán mẫu có bối cảnh thực

Một cảm biến rung theo mô hình
$$ x''+2x'+10x=0,\qquad x(0)=1,\qquad x'(0)=0. $$
Phương trình đặc trưng có nghiệm
$$ r=-1\pm 3i. $$
Do đó
$$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right). $$
Áp điều kiện đầu được
$$
x(t)=e^{-t}\left(\cos 3t+\frac{1}{3}\sin 3t\right).
$$
Vật lý của lời giải rất rõ: hệ vẫn rung với tần số gần 3, nhưng bao biên độ giảm như $$ e^{-t} $$ vì năng lượng bị tiêu tán.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo đổi từ nghiệm phức sang nghiệm thực và đọc biên độ, tần số từ $$ \alpha,\beta $$.

**Bậc sau đại học.** Dùng dạng biên độ - pha
$$ Re^{\alpha t}\cos(\beta t-\phi) $$
và nối với giá trị riêng phức của ma trận hệ tuyến tính.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rất tốt ý nghĩa động học của nghiệm phức.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài tập chuyển đổi giữa nghiệm phức và nghiệm thực.
- Ross — *Differential Equations*: ngắn gọn và rõ trong việc đọc $$ \alpha $$, $$ \beta $$ từ nghiệm đặc trưng.
