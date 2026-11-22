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
Bài học này giúp sinh viên hiểu nguồn gốc của nghiệm phức trong phương trình đặc trưng, chuyển chúng về nghiệm thực bằng công thức Euler, và diễn giải ý nghĩa của phần thực cùng phần ảo trong động học dao động. Đây là nền tảng để phân tích dao động điều hòa, dao động tắt dần và cộng hưởng ở các bài ứng dụng tiếp theo.

## Kiến thức nền
Sinh viên nên nắm phương trình đặc trưng với hệ số hằng, kiến thức cơ bản về số phức và công thức Euler
$$ e^{i\theta}=\cos \theta+i\sin \theta. $$
Nếu sinh viên chưa quen với số phức, giảng viên nên ôn lại ngắn gọn trước khi đi vào kỹ thuật giải.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-03 Hệ số Hằng: Nghiệm Phức]({{ site.imgurl }}/chapter_img/chapter02/02_03_constant_coeff_complex_roots.svg)

Khi phương trình đặc trưng không có nghiệm thực, nhiều sinh viên dễ lo rằng mô hình mất ý nghĩa vật lý. Thực tế lại ngược lại: nghiệm phức là dấu hiệu của dao động. Hệ lò xo lý tưởng, mạch LC và nhiều hiện tượng sóng đều dẫn tới nghiệm phức. Phần ảo không phải đại lượng "không có thật", mà là cách đại số mã hóa tần số dao động.

Điểm đáng chú ý của bài học là số phức chỉ đóng vai trò công cụ trung gian, còn kết quả cuối cùng vẫn là nghiệm thực. Nhờ công thức Euler, cặp nghiệm phức liên hợp tạo ra hai hàm sin và cos, trong khi phần thực của nghiệm đặc trưng điều khiển biên độ tăng hay giảm theo thời gian.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Một cặp nghiệm phức liên hợp có thể hình dung như chuyển động quay trong mặt phẳng. Khi chiếu chuyển động quay đó lên một trục, ta thu được hàm sin và cos. Nếu bán kính quay thu nhỏ dần, ta có dao động tắt dần; nếu bán kính mở rộng dần, ta có dao động tăng biên.

### Cách nhìn hình ảnh
Với nghiệm đặc trưng $$ r=\alpha\pm i\beta $$, đồ thị nghiệm có dạng
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Nếu $$ \alpha=0 $$, biên độ giữ nguyên; nếu $$ \alpha<0 $$, biên độ tắt dần; nếu $$ \alpha>0 $$, biên độ tăng dần. Trong khi đó, $$ \beta $$ quyết định tốc độ dao động, tức tần số góc.

### Cách nhìn hình thức
Với phương trình $$ ay''+by'+cy=0 $$, nếu phương trình đặc trưng $$ ar^2+br+c=0 $$ có cặp nghiệm phức liên hợp
$$ r=\alpha\pm i\beta,\qquad \beta\neq 0, $$
thì nghiệm tổng quát thực là
$$
y(t)=e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Kết quả này suy trực tiếp từ công thức Euler:
$$
e^{(\alpha+i\beta)t}=e^{\alpha t}\left(\cos \beta t+i\sin \beta t\right).
$$

## Những ngộ nhận thường gặp
- "Nghiệm phức nghĩa là nghiệm vật lý không có thật." Sai: nghiệm cuối cùng vẫn là hàm thực.
- "Phần ảo của nghiệm đặc trưng chỉ làm biểu thức phức tạp hơn chứ không có ý nghĩa." Sai: phần ảo chính là tần số góc của dao động.
- "Có sin và cos thì hệ chắc chắn ổn định." Sai: tính ổn định còn phụ thuộc vào dấu của phần thực $$ \alpha $$.
- "Mọi dao động đều có biên độ không đổi." Sai: dao động tắt dần và dao động tăng biên xuất hiện khi $$ \alpha\neq 0 $$.

## Tiến trình học tập đề xuất
### Bước 1: Giải phương trình đặc trưng
Kiểm tra biệt thức âm để nhận diện trường hợp nghiệm phức.

### Bước 2: Viết nghiệm ở dạng hàm mũ phức
Đây là bước trung gian trước khi chuyển về hàm thực.

### Bước 3: Áp dụng công thức Euler để chuyển về nghiệm thực
Bước này nối liền biến đổi đại số với biểu diễn lượng giác.

### Bước 4: Đọc ý nghĩa phần thực và phần ảo
Phần thực quyết định sự thay đổi biên độ, còn phần ảo quyết định tần số dao động.

### Các checkpoint
- Sinh viên có chuyển đúng từ $$ e^{(\alpha+i\beta)t} $$ sang dạng sin và cos hay không.
- Sinh viên có giải thích được vai trò của $$ \alpha $$ và $$ \beta $$ hay không.
- Sinh viên có phân biệt được dao động điều hòa với dao động tắt dần hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Dao động điều hòa thuần
Giải phương trình $$ y''+4y=0 $$. Phương trình đặc trưng là $$ r^2+4=0 $$, suy ra $$ r=\pm 2i $$. Do đó
$$ y(t)=c_1\cos 2t+c_2\sin 2t. $$
Đây là dao động điều hòa với tần số góc bằng 2 và biên độ không đổi.

### Ví dụ 2: Dao động tắt dần
Giải phương trình $$ y''+2y'+5y=0 $$. Phương trình đặc trưng $$ r^2+2r+5=0 $$ có nghiệm $$ r=-1\pm 2i $$. Vậy nghiệm tổng quát là
$$ y(t)=e^{-t}\left(c_1\cos 2t+c_2\sin 2t\right). $$
Thừa số $$ e^{-t} $$ làm biên độ suy giảm theo thời gian, còn $$ 2 $$ là tần số góc của dao động.

### Ví dụ 3: Áp dụng điều kiện đầu
Với phương trình $$ y''+2y'+5y=0 $$, giả sử $$ y(0)=1 $$ và $$ y'(0)=0 $$. Từ $$ y(0)=1 $$ suy ra $$ c_1=1 $$. Tính đạo hàm:
$$
y'(t)=e^{-t}\left[-c_1\cos 2t-c_2\sin 2t-2c_1\sin 2t+2c_2\cos 2t\right].
$$
Thay $$ t=0 $$, ta được $$ y'(0)=-c_1+2c_2=0 $$. Vì $$ c_1=1 $$ nên $$ 2c_2=1 \Rightarrow c_2=\frac{1}{2} $$. Vậy
$$
y(t)=e^{-t}\left(\cos 2t+\frac{1}{2}\sin 2t\right).
$$

### Ví dụ 4: Dao động tăng biên
Giải phương trình $$ y''-2y'+5y=0 $$. Phương trình đặc trưng $$ r^2-2r+5=0 $$ có nghiệm $$ r=1\pm 2i $$. Do đó
$$ y(t)=e^t\left(c_1\cos 2t+c_2\sin 2t\right). $$
Hệ vẫn dao động nhưng biên độ tăng theo $$ e^t $$, minh họa rõ tác động của phần thực dương.

## Câu hỏi khái niệm
1. Vì sao nghiệm phức của phương trình đặc trưng lại dẫn tới các hàm sin và cos trong nghiệm thực?
2. Phần thực và phần ảo của nghiệm đặc trưng mã hóa hai đại lượng vật lý nào?
3. Vì sao hai hệ đều dao động nhưng một hệ tắt dần còn hệ kia tăng biên?

## Bài toán ứng dụng
1. Một hệ lò xo có lực cản nhỏ dao động quanh vị trí cân bằng. Hãy giải thích vì sao nghiệm thu được là dao động tắt dần chứ không phải sin-cos thuần.
2. Một mạch điện có điện áp dao động nhưng năng lượng tiêu hao dần. Thành phần nào của nghiệm đặc trưng phản ánh sự tiêu hao này?
3. Một hệ điều khiển có tín hiệu dao động với biên độ ngày càng lớn. Hãy giải thích vì sao điều đó cho thấy nghiệm đặc trưng có phần thực dương.

## Chiến lược giảng dạy tương tác
- Cho sinh viên quan sát ba đồ thị (biên độ không đổi, tắt dần, tăng biên) và đoán dấu của $$ \alpha $$.
- Tổ chức hoạt động chuyển đổi ngôn ngữ: từ nghiệm đặc trưng $$ -1\pm 3i $$ sang mô tả bằng lời "dao động tắt dần với tần số góc 3".
- Yêu cầu sinh viên làm việc theo nhóm nhỏ để tự suy ra công thức nghiệm thực từ công thức Euler.
- Khuyến khích sinh viên biểu diễn nghiệm dưới dạng biên độ - pha để tăng trực giác vật lý.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên dùng quy trình hai bước cố định: giải phương trình đặc trưng, rồi áp dụng mẫu
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right).
$$
Việc tách riêng vai trò của $$ \alpha $$ và $$ \beta $$ bằng màu sắc hoặc sơ đồ thường giúp sinh viên dễ nhớ hơn.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên viết nghiệm dưới dạng $$ Re^{\alpha t}\cos \left(\beta t-\phi\right) $$ và giải thích ý nghĩa của biên độ ban đầu, pha ban đầu và tốc độ tắt dần.

## Tóm tắt dễ nhớ
Nghiệm phức là cách toán học mã hóa dao động. Nếu $$ r=\alpha\pm i\beta $$, thì nghiệm tổng quát có dạng
$$
e^{\alpha t}\left(c_1\cos \beta t+c_2\sin \beta t\right),
$$
trong đó $$ \alpha $$ điều khiển đường bao biên độ và $$ \beta $$ quyết định tần số góc.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động của hệ khối lượng - lò xo không cản
- Bài toán: Một vật gắn lò xo lý tưởng dao động quanh vị trí cân bằng với biên độ không đổi.
- Mô hình:
$$ x''+\omega^2 x=0. $$
- Giả thiết và giới hạn: Không có ma sát, lò xo tuyến tính và không có ngoại lực.
- Diễn giải: Cặp nghiệm thuần ảo $$ \pm i\omega $$ biểu diễn tần số dao động của hệ.

#### Dao động tắt dần trong cảm biến cơ điện
- Bài toán: Một đầu đo rung sau tác động nhẹ rồi ổn định dần.
- Mô hình:
$$ x''+2\zeta\omega_n x'+\omega_n^2 x=0. $$
- Giả thiết và giới hạn: Lực cản tuyến tính, dao động nhỏ và thông số không đổi.
- Diễn giải: Phần thực âm làm biên độ tắt dần, còn phần ảo xác định tần số dao động.

#### Mạch LC hoặc RLC dưới tắt dần
- Bài toán: Điện tích trong mạch điện dao động do năng lượng trao đổi qua lại giữa từ trường và điện trường.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=0. $$
- Giả thiết và giới hạn: Các linh kiện lý tưởng và tuyến tính.
- Diễn giải: Nghiệm dạng sin-cos nhân hàm mũ cho thấy mạch vừa dao động vừa tiêu tán năng lượng.

### 2. Trực giác bổ sung và các kết nối

Nghiệm phức xuất hiện vì chuyển động quay trong mặt phẳng là cách tự nhiên để mô tả dao động; khi chiếu chuyển động quay xuống trục thực, ta thu được hàm sin và cos. Nội dung này kết nối trực tiếp đại số, hình học và vật lý. Một lỗi thường gặp là nhớ công thức $$ e^{\alpha t}(c_1\cos \beta t+c_2\sin \beta t) $$ nhưng quên vai trò riêng của từng tham số: $$ \alpha $$ điều khiển đường bao biên độ, còn $$ \beta $$ điều khiển tốc độ dao động.

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

Ba đường cong giúp phân biệt trực quan dao động điều hòa, dao động tắt dần và dao động tăng biên.

### 4. Gợi ý tìm thêm mô phỏng

- search: damped oscillation envelope interactive
- search: complex roots oscillation visualization
- search: Euler formula sine cosine dynamics

### 5. Bài toán mẫu có bối cảnh thực

Một cảm biến rung theo mô hình
$$ x''+2x'+10x=0,\qquad x(0)=1,\qquad x'(0)=0. $$
Phương trình đặc trưng có nghiệm $$ r=-1\pm 3i $$, nên $$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right) $$. Áp dụng điều kiện đầu, ta được
$$
x(t)=e^{-t}\left(\cos 3t+\frac{1}{3}\sin 3t\right).
$$
Ý nghĩa vật lý thể hiện rõ trên biểu thức: hệ dao động với tần số góc bằng 3, còn đường bao biên độ giảm theo $$ e^{-t} $$ do năng lượng bị tiêu tán.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo việc chuyển từ nghiệm phức sang nghiệm thực và đọc biên độ, tần số từ $$ \alpha,\beta $$.

**Bậc sau đại học.** Sử dụng dạng biên độ - pha $$ Re^{\alpha t}\cos(\beta t-\phi) $$ và liên hệ với giá trị riêng phức của ma trận hệ tuyến tính.

## Video tham khảo

- Xem trước: [Constant Coefficient ODEs: Real & Distinct vs Real & Repeated vs Complex Pair](https://www.youtube.com/watch?v=r8Uk4tbuxVE) — Dr. Trefor Bazett, tiếng Anh. Phân tích trường hợp cặp nghiệm phức và cách phần thực, phần ảo tạo thành nghiệm dao động.
- [Lec 10 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=YQ7HEE8-OfA) — MIT OpenCourseWare, tiếng Anh. Bài giảng của giáo sư Mattuck về nghiệm đặc trưng phức.
- [Taylor Series of the Exponential Function and Euler's Formula!](https://www.youtube.com/watch?v=H0Zbg_CqMCs) — Steve Brunton, tiếng Anh. Trình bày công thức Euler — bước chuyển đổi từ hàm mũ phức sang sin và cos.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ ý nghĩa động học của nghiệm phức.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập chuyển đổi giữa nghiệm phức và nghiệm thực.
- Ross — *Differential Equations*: ngắn gọn và rõ ràng khi đọc $$ \alpha $$, $$ \beta $$ từ nghiệm đặc trưng.
