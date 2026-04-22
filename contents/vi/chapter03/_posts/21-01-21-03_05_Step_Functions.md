---
layout: post
title: "03-05 Hàm Bước và Lực Gián đoạn"
chapter: '03'
order: 5
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên dùng hàm bước Heaviside để mô hình hóa những tín hiệu bật/tắt đột ngột, hiểu định lý dịch thời gian trong Laplace, và giải được các bài toán có forcing từng đoạn mà không cần chia nhỏ lời giải theo từng khoảng một cách thủ công.

## Kiến thức nền
Sinh viên cần nắm Laplace cơ bản, Laplace ngược và quy trình giải IVP bằng Laplace. Trực giác về các tín hiệu bật nguồn, đóng công tắc hoặc ngoại lực chỉ xuất hiện sau một thời điểm cũng rất hữu ích.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-05 Hàm Bước và Lực Gián đoạn]({{ site.imgurl }}/chapter_img/chapter03/03_05_step_functions.svg)

Trong thế giới thực, nhiều tín hiệu không xuất hiện ngay từ đầu rồi kéo dài mãi một cách trơn tru. Một nguồn điện có thể bật ở giây thứ 2. Một lực có thể tác động rồi bị ngắt sau một khoảng thời gian. Một hệ có thể chịu tải theo từng giai đoạn. Những hiện tượng như vậy khó chịu nếu ta cố giải ODE trên từng đoạn rồi nối điều kiện liên tục bằng tay.

Hàm bước Heaviside và Laplace giải quyết bài toán đó rất đẹp. Chúng cho phép ta viết các tín hiệu gián đoạn bằng một biểu thức duy nhất, rồi xử lý đại số trong miền $$ s $$ như thường lệ. Đây là nơi sinh viên bắt đầu cảm thấy Laplace không chỉ tiện cho tính toán, mà thật sự sinh ra để mô hình hóa hệ thống.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hàm bước là một chiếc công tắc. Trước thời điểm $$ a $$, công tắc ở trạng thái tắt nên giá trị bằng 0. Sau thời điểm đó, công tắc bật nên giá trị bằng 1. Nếu nhân nó với một hàm khác, ta đang nói "hàm này chỉ bắt đầu hoạt động từ thời điểm $$ a $$".

### Cách nhìn hình ảnh
Đồ thị của
$$ u(t-a) $$
là một đường nằm ngang ở 0 cho tới $$ t=a $$ rồi nhảy lên 1. Nếu nhìn
$$ u(t-a)f(t-a), $$
ta thấy đồ thị của $$ f $$ không bắt đầu tại 0 mà bị tịnh tiến sang phải tới thời điểm $$ a $$. Hình ảnh dịch sang phải này chính là lý do xuất hiện hệ số $$ e^{-as} $$ trong miền Laplace.

### Cách nhìn hình thức
Hàm bước Heaviside được định nghĩa bởi
$$
u(t-a)=
\begin{cases}
0, & t<a,\\
1, & t\ge a.
\end{cases}
$$
Tính chất Laplace quan trọng nhất là
$$ \mathcal{L}\{u(t-a)f(t-a)\}=e^{-as}F(s), $$
trong đó
$$ F(s)=\mathcal{L}\{f(t)\}. $$
Đây là định lý dịch thời gian, là trung tâm của cả bài học.

## Những ngộ nhận thường gặp
- "Hàm bước chỉ là ký hiệu trang trí để mô tả bật nguồn." Sai. Nó là công cụ đại số mạnh trong Laplace.
- "Muốn viết một hàm từng đoạn thì chỉ cần đặt $$ u(t-a)f(t) $$." Chưa đủ. Cần cẩn thận với việc dịch đối số về $$ f(t-a) $$ nếu muốn dùng công thức chuẩn.
- "Hệ số $$ e^{-as} $$ là thứ phải nhớ máy móc." Sai. Nó phản ánh đúng việc tín hiệu bị trễ thời gian.
- "Bài toán gián đoạn bắt buộc phải giải trên từng khoảng." Không còn đúng khi dùng Laplace.

## Tiến trình học tập đề xuất
### Bước 1: Học viết hàm từng đoạn bằng Heaviside
Đây là bước mô hình hóa quan trọng nhất.

### Bước 2: Đưa về dạng
$$ u(t-a)f(t-a) $$
để dùng công thức dịch.

### Bước 3: Áp Laplace và giải đại số như thường lệ
Không cần thay đổi quy trình lớn.

### Bước 4: Quay lại miền thời gian
Đọc ý nghĩa của tín hiệu bật/tắt trên nghiệm cuối.

### Các checkpoint
- Sinh viên có viết đúng một hàm từng đoạn bằng Heaviside hay không.
- Sinh viên có hiểu vì sao phải dịch đối số thành $$ t-a $$ hay không.
- Sinh viên có giải thích được ý nghĩa của hệ số $$ e^{-as} $$ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Viết hàm từng đoạn bằng Heaviside
Xét hàm
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
Ta viết gọn:
$$ f(t)=3u(t-2). $$
Do đó
$$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s}. $$
Ví dụ này cho thấy bước Heaviside hóa tín hiệu thực sự rất ngắn gọn.

### Ví dụ 2: Bật một hàm sin muộn
Xét tín hiệu
$$
f(t)=
\begin{cases}
0, & 0\le t<1,\\
\sin (t-1), & t\ge 1.
\end{cases}
$$
Ta viết
$$ f(t)=u(t-1)\sin (t-1). $$
Vì
$$ \mathcal{L}\{\sin t\}=\frac{1}{s^2+1}, $$
ta được
$$ \mathcal{L}\{f(t)\}=e^{-s}\frac{1}{s^2+1}. $$
Điểm sư phạm ở đây là phần bên trong phải là $$ t-1 $$, không phải $$ t $$, nếu ta muốn áp dụng trực tiếp định lý dịch.

### Ví dụ 3: Giải IVP có nguồn bật chậm
Giải
$$ y'+y=u(t-2),\qquad y(0)=0. $$
Áp Laplace:
$$ \left(sY\right)+Y=\frac{e^{-2s}}{s}. $$
Suy ra
$$ Y=\frac{e^{-2s}}{s(s+1)}. $$
Ta biết
$$ \frac{1}{s(s+1)}=\frac{1}{s}-\frac{1}{s+1}, $$
nên
$$
\mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1-e^{-t}.
$$
Theo định lý dịch:
$$ y(t)=u(t-2)\left(1-e^{-(t-2)}\right). $$
Nghiệm cho thấy hệ đứng yên tới thời điểm 2, rồi bắt đầu tiến tới trạng thái ổn định.

### Ví dụ 4: Tín hiệu bật rồi tắt
Xét tín hiệu bằng 5 trên khoảng từ 1 đến 3 và bằng 0 ngoài khoảng đó. Ta viết
$$ f(t)=5u(t-1)-5u(t-3). $$
Đây là ví dụ rất hay để cho sinh viên thấy Heaviside giống hệt thao tác bật và tắt công tắc.

## Câu hỏi khái niệm
1. Vì sao hệ số $$ e^{-as} $$ phản ánh trực tiếp việc tín hiệu bị trễ thời gian?
2. Vì sao cần viết hàm theo dạng $$ u(t-a)f(t-a) $$ thay vì chỉ $$ u(t-a)f(t) $$ trong nhiều trường hợp?
3. Lợi thế lớn nhất của Heaviside trong mô hình hóa là gì?

## Bài toán ứng dụng
1. Một công tắc điện chỉ bật nguồn sau 3 giây. Hãy mô tả forcing bằng Heaviside và giải thích ý nghĩa vật lý của hệ số trễ.
2. Một hệ cơ học chịu lực không đổi trong một khoảng thời gian rồi bị ngắt. Hãy giải thích vì sao Heaviside phù hợp hơn cách chia tay bài toán.
3. Một tín hiệu điều khiển có độ trễ truyền tin. Hãy thảo luận cách Laplace mô tả độ trễ đó.

## Chiến lược giảng dạy tương tác
- Bắt đầu bằng một đồ thị tín hiệu bật/tắt và yêu cầu sinh viên tự viết bằng Heaviside trước khi giới thiệu công thức.
- Cho sinh viên thực hành chuyển qua lại giữa mô tả bằng lời, mô tả từng đoạn và mô tả bằng Heaviside.
- Hỏi lớp: "Nếu nguồn chỉ bắt đầu ở giây thứ 5, trên miền $$ s $$ điều gì sẽ thay đổi?"
- Dùng hoạt động ghép cặp giữa đồ thị và biểu thức Heaviside để tăng trực giác.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên yếu làm thật nhiều bài dịch giữa "hàm từng đoạn" và "Heaviside" trước khi đi vào ODE. Bài này thường khó ở khâu mô hình hóa hơn khâu tính Laplace.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi xử lý các tín hiệu nhiều mức hoặc nhiều lần bật/tắt, hoặc viết lại cùng một tín hiệu theo nhiều biểu thức Heaviside tương đương rồi so sánh.

## Tóm tắt dễ nhớ
Hàm bước Heaviside là công tắc của Laplace. Nó giúp viết gọn các tín hiệu bật/tắt và biến độ trễ thời gian thành hệ số $$ e^{-as} $$ trong miền $$ s $$. Muốn dùng đúng, hãy luyện viết tín hiệu dưới dạng
$$ u(t-a)f(t-a). $$

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bật nguồn mạch điện
- Bài toán: Một nguồn điện chỉ bắt đầu cấp vào hệ sau thời điểm $$ a $$.
- Mô hình:
$$ u(t-a)V_0. $$
- Giả thiết và giới hạn: Công tắc lý tưởng, không có thời gian chuyển tiếp hữu hạn.
- Diễn giải: Heaviside mô hình hóa cực gọn các tín hiệu bật/tắt, và trễ thời gian trở thành nhân tử $$ e^{-as} $$.

#### Tải trọng theo giai đoạn trong cơ học
- Bài toán: Dầm hoặc hệ dao động nhận tải tại một thời điểm rồi tải bị ngắt sau đó.
- Mô hình:
$$ F(t)=u(t-a)-u(t-b) $$
hoặc các biến thể nhân với biên độ.
- Giả thiết và giới hạn: Tải đổi tức thời, chưa mô hình hóa giai đoạn chuyển mượt.
- Diễn giải: Hàm bước cho phép viết toàn bộ forcing từng đoạn bằng một biểu thức duy nhất.

#### Chính sách kinh tế kích hoạt muộn
- Bài toán: Một can thiệp hay gói kích thích chỉ bắt đầu từ quý thứ hai hay năm thứ ba.
- Mô hình:
$$ u(t-a)f(t-a). $$
- Giả thiết và giới hạn: Tác động bật ngay, không có trễ phân phối bên trong.
- Diễn giải: Bài toán từng đoạn được giải như một bài Laplace duy nhất.

### 2. Trực giác bổ sung và các kết nối

Hàm bước là chiếc công tắc của chương Laplace. Bài này đặc biệt quan trọng vì nó biến mô hình hóa thực tế thành một phần trung tâm chứ không chỉ là ví dụ minh họa. Một lỗi hay gặp là viết $$ u(t-a)f(t) $$ rồi áp luôn công thức dịch; để dùng chuẩn, cần đưa tín hiệu về dạng $$ u(t-a)f(t-a) $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 600)
u2 = (t >= 2).astype(float)
signal = u2 * np.sin(t - 2)

plt.plot(t, u2, label="u(t-2)")
plt.plot(t, signal, label="u(t-2) sin(t-2)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Hàm bước và tín hiệu bật muộn")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Heaviside step function Laplace visualization
- search: delayed input signal animation
- search: piecewise forcing differential equation Laplace

### 5. Bài toán mẫu có bối cảnh thực

Một nguồn được bật ở $$ t=2 $$ với biên độ 3:
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
Viết gọn:
$$ f(t)=3u(t-2). $$
Do đó
$$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s}. $$
Nếu dùng forcing này trong ODE tuyến tính, ta không cần giải trên hai khoảng rồi nối bằng tay; chỉ cần giữ nguyên quy trình Laplace quen thuộc.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung viết đúng tín hiệu từng đoạn bằng Heaviside và dùng đúng định lý dịch.

**Bậc sau đại học.** Làm việc với nhiều công tắc, nhiều mức, và so sánh các biểu diễn Heaviside tương đương của cùng một tín hiệu.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giải thích rất rõ định lý dịch thời gian.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ kỹ thuật hay về tín hiệu gián đoạn.
- Ross — *Differential Equations*: phù hợp để ôn lại thao tác Heaviside một cách ngắn gọn.
