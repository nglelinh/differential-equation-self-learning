---
layout: post
title: "03-02 Biến đổi Laplace của Hàm Cơ bản"
chapter: '03'
order: 2
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên xây dựng bảng biến đổi Laplace cho các hàm cơ bản: hằng số, lũy thừa, hàm mũ, sin, cos và các tổ hợp đơn giản. Trọng tâm không phải học thuộc máy móc mà là hiểu mối liên hệ giữa hình dạng hàm trong miền thời gian với cấu trúc phân thức trong miền $$ s $$, đồng thời biết dùng tính tuyến tính và tính dịch chuyển để suy ra công thức mới.

## Kiến thức nền
Sinh viên cần nắm định nghĩa biến đổi Laplace, kỹ thuật tích phân từng phần và công thức Euler cơ bản. Hiểu cách dựng công thức từ định nghĩa giúp ghi nhớ lâu và áp dụng linh hoạt hơn.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-02 Biến đổi Laplace của Hàm Cơ bản]({{ site.imgurl }}/chapter_img/chapter03/03_02_elementary_functions.svg)

Để sử dụng biến đổi Laplace hiệu quả, ta cần nắm một hệ thống công thức nền tảng. Thay vì học thuộc rời rạc từng dòng trong bảng, cách bền vững hơn là nhận diện quy luật: đa thức tạo ra các lũy thừa của $$ 1/s $$, hàm mũ làm dịch chuyển biến $$ s $$, còn sin và cos tạo ra mẫu số bậc hai $$ s^2+b^2 $$.

Vì vậy, bài học này hướng dẫn cách xây dựng bảng biến đổi từ định nghĩa. Khi tự suy ra được vài công thức gốc, các công thức mở rộng trở nên có hệ thống và dễ nhớ hơn.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hằng số và đa thức tạo ra biến đổi Laplace có cực tại $$ s=0 $$. Hàm mũ $$ e^{at} $$ dịch chuyển cực sang vị trí $$ s=a $$. Dao động sin-cos biên độ không đổi tạo ra mẫu số bậc hai vì đạo hàm hai lần quay lại dạng ban đầu.

### Cách nhìn hình ảnh
Trong miền thời gian, $$ 1 $$, $$ t $$, $$ e^{at} $$ và $$ \sin bt $$ có hình dạng rất khác nhau, nhưng trong miền Laplace chúng đều chuyển thành các phân thức hữu tỉ gọn gàng. Chính sự cô đọng này giúp ta đọc nhanh tính chất của tín hiệu thông qua vị trí cực và hệ số.

### Cách nhìn hình thức
Các công thức nền tảng gồm:
$$ \mathcal{L}\{1\}=\frac{1}{s}, $$
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}, $$
$$ \mathcal{L}\{e^{at}\}=\frac{1}{s-a}, $$
$$ \mathcal{L}\{\cos bt\}=\frac{s}{s^2+b^2}, $$
$$ \mathcal{L}\{\sin bt\}=\frac{b}{s^2+b^2}. $$
Năm công thức này là cơ sở cho phần lớn các bài toán đầu chương.

## Những ngộ nhận thường gặp
- "Phải thuộc lòng toàn bộ bảng ngay lập tức." Sai: chỉ cần nắm các mẫu gốc và quy tắc biến đổi để tự suy ra.
- "Các công thức trong bảng không liên quan đến nhau." Sai: chúng phản ánh trực tiếp cấu trúc đạo hàm và tốc độ tăng trưởng của hàm.
- "Sin và cos có công thức hoàn toàn tách biệt." Sai: cả hai đều có chung mẫu số $$ s^2+b^2 $$.
- "Biến đổi của đa thức chỉ là quy tắc thay ký hiệu." Sai: nó thu được từ phép tích phân từng phần lặp lại.

## Tiến trình học tập đề xuất
### Bước 1: Tự suy ra các công thức gốc từ định nghĩa
Bắt đầu với $$ 1 $$, $$ e^{at} $$ và $$ t $$.

### Bước 2: Nhận diện quy luật cho lũy thừa $$ t^n $$
Mở rộng từ $$ t $$ lên $$ t^n $$ bằng tích phân từng phần.

### Bước 3: Xây dựng công thức cho sin và cos
Dùng tích phân từng phần hai lần hoặc công thức Euler.

### Bước 4: Kết hợp tính tuyến tính và dịch chuyển
Suy ra thêm nhiều công thức mới mà không cần tính lại tích phân.

### Các checkpoint
- Sinh viên có phân biệt được vai trò của $$ a $$ trong $$ e^{at} $$ và $$ b $$ trong $$ \sin bt $$ hay không.
- Sinh viên có nhận diện đúng quy luật $$ n!/s^{n+1} $$ hay không.
- Sinh viên có tự suy ra được biến đổi của các tổ hợp đơn giản mà không cần tra bảng hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Biến đổi Laplace của $$ t $$
Ta tính $$ \mathcal{L}\{t\}=\int_0^\infty te^{-st}dt $$. Tích phân từng phần với $$ u=t $$, $$ dv=e^{-st}dt $$, suy ra $$ du=dt $$ và $$ v=-\frac{1}{s}e^{-st} $$. Do đó
$$
\mathcal{L}\{t\}=\left[-\frac{t}{s}e^{-st}\right]_0^\infty+\frac{1}{s}\int_0^\infty e^{-st}dt=\frac{1}{s^2}.
$$

### Ví dụ 2: Quy luật tổng quát cho $$ t^n $$
Lặp lại phép tích phân từng phần cho các bậc cao hơn, ta thu được $$ \mathcal{L}\{t^2\}=\frac{2}{s^3} $$, $$ \mathcal{L}\{t^3\}=\frac{6}{s^4} $$, và tổng quát:
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}. $$
Nhận ra quy luật này giúp không phải tính lại tích phân từng phần cho từng số mũ.

### Ví dụ 3: Biến đổi Laplace của sin và cos
Đặt $$ I=\mathcal{L}\{\sin bt\} $$ và $$ J=\mathcal{L}\{\cos bt\} $$. Áp dụng tích phân từng phần ta thu được hệ hai phương trình tuyến tính theo $$ I, J $$, giải ra:
$$ I=\frac{b}{s^2+b^2},\qquad J=\frac{s}{s^2+b^2}. $$
Cả hai cùng có mẫu số $$ s^2+b^2 $$, phản ánh cấu trúc dao động bậc hai của hàm lượng giác.

### Ví dụ 4: Áp dụng tính chất dịch chuyển theo hàm mũ
Từ $$ \mathcal{L}\{\cos 2t\}=\frac{s}{s^2+4} $$, áp dụng tính chất dịch chuyển theo $$ s $$ thu được
$$
\mathcal{L}\{e^{3t}\cos 2t\}=\frac{s-3}{(s-3)^2+4},
$$
không cần quay lại tính tích phân suy rộng từ đầu.

## Câu hỏi khái niệm
1. Vì sao đa thức $$ t^n $$ tạo ra cực bội tại $$ s=0 $$?
2. Vì sao nhân với $$ e^{at} $$ trong miền thời gian chỉ làm dịch chuyển biến $$ s $$ trong miền Laplace?
3. Mẫu số $$ s^2+b^2 $$ phản ánh tính chất gì của dao động sin và cos?

## Bài toán ứng dụng
1. Các tín hiệu điều hòa trong điện tử thường biểu diễn bằng sin và cos. Vì sao công thức Laplace của chúng là nền tảng cho phân tích mạch?
2. Tín hiệu dạng $$ e^{at}\cos bt $$ xuất hiện trong những mô hình nào, và vì sao phép dịch chuyển biến $$ s $$ phản ánh đúng bản chất của nó?
3. Đầu vào dạng đa thức mô tả tín hiệu tăng dần theo thời gian. Vì sao cực của ảnh Laplace lại tập trung tại $$ s=0 $$?

## Chiến lược giảng dạy tương tác
- Cho sinh viên tự xây dựng bảng 5 công thức gốc trước khi phát bảng tra đầy đủ.
- Chia nhóm thực hiện riêng từng họ hàm (đa thức, hàm mũ, lượng giác) rồi tổng hợp chung.
- Yêu cầu sinh viên giải thích bằng lời lý do $$ \sin bt $$ và $$ \cos bt $$ có cùng mẫu số.
- Luyện phản xạ nhanh: nhìn hàm theo thời gian và dự đoán ngay dạng phân thức theo $$ s $$.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Cung cấp bảng tóm tắt ba cột gồm "hàm gốc", "công thức" và "quy luật nhận diện" (đa thức cho lũy thừa của $$ 1/s $$, hàm mũ gây dịch chuyển, lượng giác cho mẫu bậc hai).

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên chứng minh công thức của $$ t^n $$ bằng quy nạp hoặc dùng phép lấy đạo hàm theo tham số từ $$ \mathcal{L}\{1\} $$ để suy ra các công thức mới.

## Tóm tắt dễ nhớ
Thay vì học thuộc rời rạc, hãy nhớ ba quy luật cốt lõi: hằng và đa thức cho lũy thừa của $$ 1/s $$, hàm mũ làm dịch chuyển biến $$ s $$, còn sin-cos tạo ra mẫu bậc hai $$ s^2+b^2 $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động điều hòa
- Bài toán: Chuyển tín hiệu dao động sin-cos sang miền $$ s $$ để giải ODE hoặc phân tích đáp ứng tần số.
- Mô hình: $$ \sin bt $$, $$ \cos bt $$.
- Giả thiết và giới hạn: Dao động biên độ không đổi với một tần số duy nhất.
- Diễn giải: Mẫu số chung $$ s^2+b^2 $$ phản ánh tính chất dao động bậc hai.

#### Tăng trưởng theo hàm mũ trong sinh học và tài chính
- Bài toán: Nhiều quá trình tăng trưởng hoặc suy giảm có dạng $$ f(t)=e^{at} $$.
- Mô hình: $$ f(t)=e^{at} $$.
- Giả thiết và giới hạn: Tốc độ tăng trưởng $$ a $$ không đổi.
- Diễn giải: Cực dịch từ $$ 0 $$ sang $$ a $$, cho thấy tốc độ tăng trưởng mũ chuyển thẳng thành vị trí cực trong miền $$ s $$.

#### Tín hiệu đa thức trong kiểm định điều khiển
- Bài toán: Đầu vào dốc (ramp) hoặc parabol thường dùng để kiểm định sai số xác lập của hệ điều khiển.
- Mô hình: $$ 1,\quad t,\quad t^2,\ldots $$
- Giả thiết và giới hạn: Tín hiệu trơn xác định trên $$ t\ge 0 $$.
- Diễn giải: Công thức $$ n!/s^{n+1} $$ cho thấy bậc đa thức càng cao thì bội của cực tại $$ s=0 $$ càng lớn.

### 2. Trực giác bổ sung và các kết nối

Bảng biến đổi Laplace cơ bản đóng vai trò bản đồ nối dạng tín hiệu trong miền thời gian với cấu trúc cực trong miền $$ s $$. Kiến thức này gắn chặt với bài hàm truyền: về sau, chỉ cần quan sát tử số và mẫu số theo $$ s $$ là có thể dự đoán hành vi thời gian của hệ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0.5, 6, 500)
L1 = 1 / s
Lt = 1 / s**2
Lsin = 2 / (s**2 + 4)
Lcos = s / (s**2 + 4)

plt.plot(s, L1, label="L{1} = 1/s")
plt.plot(s, Lt, label="L{t} = 1/s^2")
plt.plot(s, Lsin, label="L{sin 2t}")
plt.plot(s, Lcos, label="L{cos 2t}")
plt.xlabel("s")
plt.ylabel("F(s)")
plt.title("Một số biến đổi Laplace cơ bản")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy các tín hiệu có hình dạng rất khác nhau trong miền thời gian đều trở thành những hàm hữu tỉ gọn trong miền $$ s $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: Laplace table intuition plot
- search: sine cosine Laplace transform visualization
- search: ramp input Laplace transform control

### 5. Bài toán mẫu có bối cảnh thực

Xét tín hiệu dốc $$ f(t)=3t $$ trong kiểm định hệ thống. Từ $$ \mathcal{L}\{t\}=\frac{1}{s^2} $$, áp dụng tính tuyến tính ta có $$ \mathcal{L}\{3t\}=\frac{3}{s^2} $$. Nếu tín hiệu có thêm nhân tử suy giảm như $$ e^{-2t}t $$, áp dụng tính chất dịch chuyển cho
$$ \mathcal{L}\{e^{-2t}t\}=\frac{1}{(s+2)^2}. $$
Cách làm này minh họa việc kết hợp hai quy luật gốc thay vì tra bảng máy móc.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm chắc các công thức nền tảng và biết kết hợp tính tuyến tính, dịch chuyển để mở rộng bảng.

**Bậc sau đại học.** Sử dụng phép đạo hàm theo tham số $$ s $$ để suy ra cả họ công thức rộng hơn từ một vài biến đổi gốc.

## Video tham khảo

- Xem trước: [Laplace Transform: Basics | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=BniJM-ireXQ) — MIT OpenCourseWare, tiếng Anh. Xây dựng biến đổi Laplace của các hàm sơ cấp cho bảng công thức cơ bản.
- [But what is a Laplace Transform?](https://www.youtube.com/watch?v=j0wJBEZdwLs) — 3Blue1Brown, tiếng Anh. Giới thiệu định nghĩa tích phân làm cơ sở để suy ra các mục trong bảng.
- [Why Laplace transforms are so useful](https://www.youtube.com/watch?v=FE-hM1kRK4Y) — 3Blue1Brown, tiếng Anh. Giải thích lợi thế tính toán khi đã có hệ thống công thức sơ cấp.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày logic cách xây dựng bảng Laplace.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện tính trực tiếp từ định nghĩa.
- Ross — *Differential Equations*: ngắn gọn, thuận tiện để ôn tập nhanh các mẫu công thức.
