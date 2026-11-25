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

Động cơ tên lửa cháy trong đúng 10 giây rồi tắt phụt, hay công tắc điện bật lên ở giây thứ 3 rồi ngắt ở giây thứ 7—ngoài đời thực, các ngoại lực hiếm khi trơn tru mãi mãi mà thường mang **bước nhảy gián đoạn**. Nếu giải theo Chương 02, bạn sẽ phải cắt trục thời gian thành từng đoạn rồi nối khớp thủ công cực kỳ mệt mỏi; còn với **hàm bậc thang Heaviside $u_c(t)$** và biến đổi Laplace, toàn bộ cú bật–tắt ấy được xử lý gọn trong một phương trình duy nhất!

## Kiến thức cần nhớ: Bốn trụ cột của Hàm Bậc thang & Lực Gián đoạn

1. **Hàm bậc thang đơn vị $u_c(t)$ & Hàm cửa sổ $u_a(t) - u_b(t)$**:
   $u_c(t) = 0$ khi $t < c$ và $= 1$ khi $t \ge c$. Hiệu $u_a(t) - u_b(t)$ bật bằng $1$ đúng trên đoạn $[a, b)$ rồi tắt về $0$—giúp viết mọi hàm từng khúc thành một biểu thức đại số duy nhất!
2. **Định lý Dịch chuyển thứ hai (Dịch thời gian)**:
   $$\mathcal{L}\big\{u_c(t)\,f(t - c)\big\} = e^{-cs}F(s),\qquad \mathcal{L}^{-1}\big\{e^{-cs}F(s)\big\} = u_c(t)\,f(t - c).$$
   Nhân tử $e^{-cs}$ trong miền $s$ chính là chiếc đồng hồ hẹn giờ trễ đúng $c$ giây trong miền $t$!
3. **Mẹo đồng bộ tham số $g(t) \mapsto g(t - c + c)$**:
   Khi gặp $u_c(t)\,g(t)$ (chưa ở dạng $f(t - c)$), ta dùng công thức tương đương $\mathcal{L}\{u_c(t)\,g(t)\} = e^{-cs}\mathcal{L}\{g(t + c)\}$—tránh sai lầm phổ biến nhất của sinh viên!
4. **Tính trơn của nghiệm dù lực gián đoạn**:
   Với PTVP cấp hai $y'' + py' + qy = u_c(t)$, đạo hàm cấp hai $y''$ có bước nhảy tại $t = c$, nhưng cả $y(t)$ lẫn $y'(t)$ vẫn hoàn toàn **liên tục** tại $t = c$.

## Mục tiêu
Bài học này hướng dẫn cách dùng hàm bước Heaviside để mô tả các tín hiệu bật/tắt đột ngột, nắm định lý dịch thời gian trong biến đổi Laplace, và giải các phương trình vi phân có vế phải từng khúc mà không cần chia nhỏ lời giải thủ công theo từng khoảng.

## Kiến thức nền
Sinh viên cần nắm bảng Laplace cơ bản, biến đổi ngược và quy trình giải IVP bằng Laplace. Trực giác về các sự kiện đóng-ngắt nguồn điện hay ngoại lực chỉ xuất hiện sau một mốc thời gian sẽ giúp bài học dễ tiếp cận hơn.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-05 Hàm Bước và Lực Gián đoạn]({{ site.imgurl }}/chapter_img/chapter03/03_05_step_functions.svg)

Trong thực tế, nhiều tín hiệu không tồn tại liên tục từ đầu đến cuối: nguồn điện có thể bật tại giây thứ 2, một lực có thể tác động trong một khoảng thời gian rồi ngắt, hoặc hệ chịu tải theo từng giai đoạn. Nếu giải phương trình vi phân trực tiếp trên từng khoảng rồi nối điều kiện liên tục bằng tay, phép tính sẽ rất rườm rà.

Hàm bước Heaviside kết hợp với biến đổi Laplace giải quyết gọn gàng lớp bài toán này: ta viết tín hiệu gián đoạn bằng một biểu thức duy nhất và xử lý đại số trong miền $$ s $$ theo cùng quy trình đã học.

### Giải thích: Giải IVP có công tắc bật trễ $y' + y = u_2(t),\; y(0) = 0$

1. **Biến đổi Laplace hai vế** (vì $\mathcal{L}\{u_2(t)\} = \frac{e^{-2s}}{s}$):
   $$(s + 1)Y(s) = \frac{e^{-2s}}{s} \implies Y(s) = e^{-2s}\cdot\frac{1}{s(s + 1)}.$$
2. **Tách phần không chứa $e^{-2s}$**:
   $$F(s) = \frac{1}{s(s + 1)} = \frac{1}{s} - \frac{1}{s + 1} \implies f(t) = 1 - e^{-t}.$$
3. **Áp dụng Định lý Dịch chuyển thứ hai** ($\mathcal{L}^{-1}\{e^{-2s}F(s)\} = u_2(t)f(t - 2)$):
   $$y(t) = u_2(t)\big(1 - e^{-(t - 2)}\big) = \begin{cases} \mathbf{0}, & 0 \le t < 2, \\ \mathbf{1 - e^{-(t - 2)}}, & t \ge 2. \end{cases}$$
4. **Kiểm tra tại điểm bật công tắc $t = 2$**: $y(2^-) = 0$ và $y(2^+) = 1 - e^0 = 0$ (liên tục!), nhưng vận tốc nhảy từ $y'(2^-) = 0$ lên $y'(2^+) = 1$ đúng bằng bước nhảy lực!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hàm bước hoạt động như một công tắc: trước thời điểm $$ a $$, công tắc tắt nên giá trị bằng 0; từ thời điểm $$ a $$ trở đi, công tắc bật nên giá trị bằng 1. Nhân hàm bước với một hàm khác có nghĩa là tín hiệu đó chỉ bắt đầu kích hoạt tại $$ t=a $$.

### Cách nhìn hình ảnh
Đồ thị của $$ u(t-a) $$ nằm ngang ở mức 0 với $$ t<a $$ rồi nhảy lên mức 1 tại $$ t=a $$. Với $$ u(t-a)f(t-a) $$, đồ thị của $$ f $$ được tịnh tiến sang phải một đoạn $$ a $$. Chính sự trễ thời gian này sinh ra nhân tử $$ e^{-as} $$ trong miền Laplace.

### Cách nhìn hình thức
Hàm bước Heaviside được định nghĩa bởi
$$
u(t-a)=
\begin{cases}
0, & t<a,\\
1, & t\ge a.
\end{cases}
$$
Định lý dịch thời gian phát biểu:
$$ \mathcal{L}\{u(t-a)f(t-a)\}=e^{-as}F(s), $$
với $$ F(s)=\mathcal{L}\{f(t)\} $$ (và $$ a\ge 0 $$). Đây là công thức trọng tâm của bài học.

## Những ngộ nhận thường gặp
- "Hàm bước chỉ là ký hiệu minh họa cho việc bật nguồn." Sai: đây là công cụ đại số trực tiếp trong biến đổi Laplace.
- "Viết hàm từng khúc chỉ cần đặt $$ u(t-a)f(t) $$ rồi áp công thức dịch." Sai: để áp dụng trực tiếp định lý dịch thời gian, cần biểu diễn lại hàm theo biến dịch $$ t-a $$, tức dạng $$ u(t-a)f(t-a) $$.
- "Nhân tử $$ e^{-as} $$ chỉ là quy tắc nhớ máy móc." Sai: nó phản ánh trực tiếp độ trễ thời gian $$ a $$ của tín hiệu.
- "Phương trình có vế phải gián đoạn luôn phải chia từng khoảng để giải." Không cần thiết khi sử dụng biến đổi Laplace.

## Tiến trình học tập đề xuất
### Bước 1: Biểu diễn hàm từng khúc bằng hàm Heaviside
Đây là bước mô hình hóa quan trọng nhất của bài.

### Bước 2: Đưa về dạng chuẩn $$ u(t-a)f(t-a) $$
Chuẩn bị đúng biến dịch trước khi áp dụng định lý dịch thời gian.

### Bước 3: Lấy biến đổi Laplace và giải đại số
Thực hiện theo đúng quy trình giải IVP thông thường.

### Bước 4: Biến đổi ngược về miền thời gian
Đọc lại ý nghĩa bật/tắt và độ trễ của đáp ứng trên nghiệm thu được.

### Các checkpoint
- Sinh viên có chuyển đổi chính xác giữa hàm từng khúc và biểu thức Heaviside hay không.
- Sinh viên có hiểu vì sao cần dịch đối số thành $$ t-a $$ hay không.
- Sinh viên có diễn giải được ý nghĩa của nhân tử $$ e^{-as} $$ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Viết hàm từng khúc bằng Heaviside
Xét hàm
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
Ta viết gọn thành $$ f(t)=3u(t-2) $$, từ đó
$$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s}. $$

### Ví dụ 2: Kích hoạt muộn một tín hiệu sin
Xét tín hiệu
$$
f(t)=
\begin{cases}
0, & 0\le t<1,\\
\sin (t-1), & t\ge 1.
\end{cases}
$$
Biểu diễn bằng hàm bước: $$ f(t)=u(t-1)\sin (t-1) $$. Vì $$ \mathcal{L}\{\sin t\}=\frac{1}{s^2+1} $$, theo định lý dịch thời gian ta được
$$ \mathcal{L}\{f(t)\}=e^{-s}\frac{1}{s^2+1}. $$
Lưu ý đối số bên trong hàm sin là $$ t-1 $$ chứ không phải $$ t $$, nên có thể áp dụng ngay công thức dịch.

### Ví dụ 3: Giải IVP có nguồn bật muộn
Giải bài toán $$ y'+y=u(t-2) $$ với $$ y(0)=0 $$. Lấy biến đổi Laplace hai vế:
$$ sY+Y=\frac{e^{-2s}}{s} \Rightarrow Y=\frac{e^{-2s}}{s(s+1)}. $$
Vì $$ \frac{1}{s(s+1)}=\frac{1}{s}-\frac{1}{s+1} $$, ta có $$ \mathcal{L}^{-1}\left\{\frac{1}{s(s+1)}\right\}=1-e^{-t} $$. Áp dụng định lý dịch thời gian ngược:
$$ y(t)=u(t-2)\left(1-e^{-(t-2)}\right). $$
Nghiệm cho thấy hệ giữ trạng thái bằng 0 cho tới $$ t=2 $$, sau đó mới tăng dần về mức ổn định bằng 1.

### Ví dụ 4: Tín hiệu bật rồi tắt
Một tín hiệu có giá trị bằng 5 trên khoảng $$ [1,3) $$ và bằng 0 ngoài khoảng đó được viết gọn thành
$$ f(t)=5u(t-1)-5u(t-3), $$
tương ứng với thao tác bật công tắc tại $$ t=1 $$ và tắt công tắc tại $$ t=3 $$.

## Câu hỏi khái niệm
1. Vì sao nhân tử $$ e^{-as} $$ trong miền Laplace phản ánh trực tiếp độ trễ thời gian $$ a $$?
2. Vì sao cần biến đổi hàm về dạng $$ u(t-a)f(t-a) $$ thay vì để nguyên $$ u(t-a)f(t) $$?
3. Lợi ích chính của hàm bước Heaviside trong mô hình hóa là gì?

## Bài toán ứng dụng
1. Một công tắc điện chỉ đóng nguồn sau 3 giây. Hãy viết biểu thức ngoại lực bằng hàm Heaviside và giải thích ý nghĩa vật lý của nhân tử trễ.
2. Một hệ cơ học chịu lực không đổi trong một khoảng thời gian hữu hạn rồi ngắt. Vì sao dùng hàm Heaviside thuận lợi hơn giải từng khoảng thủ công?
3. Một tín hiệu điều khiển có độ trễ truyền dẫn. Biến đổi Laplace biểu diễn độ trễ đó như thế nào?

## Chiến lược giảng dạy tương tác
- Đưa trước đồ thị tín hiệu bật/tắt để sinh viên tự viết biểu thức Heaviside trước khi chốt công thức.
- Luyện chuyển đổi qua lại giữa mô tả bằng lời, định nghĩa từng khúc và biểu thức Heaviside.
- Hỏi lớp: "Nếu nguồn chỉ bắt đầu hoạt động từ giây thứ 5, biểu thức trong miền $$ s $$ thay đổi ra sao?"
- Dùng bài tập ghép cặp giữa đồ thị và biểu thức Heaviside.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Dành thời gian luyện kỹ bước chuyển từ hàm từng khúc sang biểu thức Heaviside trước khi đưa vào phương trình vi phân, vì phần lớn lỗi xảy ra ở bước mô hình hóa này.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên biểu diễn các tín hiệu nhiều bậc hoặc bật/tắt nhiều lần và đối chiếu các cách viết Heaviside tương đương của cùng một hàm.

## Tóm tắt dễ nhớ
Hàm bước Heaviside đóng vai trò công tắc trong biến đổi Laplace, giúp gom tín hiệu từng khúc vào một biểu thức duy nhất và chuyển độ trễ thời gian $$ a $$ thành nhân tử $$ e^{-as} $$ trong miền $$ s $$ thông qua dạng chuẩn $$ u(t-a)f(t-a) $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Đóng nguồn mạch điện
- Bài toán: Nguồn điện chỉ cấp vào mạch từ thời điểm $$ t=a $$.
- Mô hình: $$ u(t-a)V_0 $$.
- Giả thiết và giới hạn: Công tắc lý tưởng, thời gian chuyển mạch bằng 0.
- Diễn giải: Hàm Heaviside biểu diễn gọn thao tác đóng mạch và tạo ra nhân tử trễ $$ e^{-as} $$.

#### Tải trọng theo giai đoạn trong cơ học
- Bài toán: Dầm hoặc hệ dao động chịu tải trong khoảng $$ [a,b) $$ rồi được dỡ tải.
- Mô hình: $$ F(t)=u(t-a)-u(t-b) $$ (nhân với độ lớn lực).
- Giả thiết và giới hạn: Tải thay đổi tức thời, chưa tính giai đoạn chuyển tiếp trơn.
- Diễn giải: Toàn bộ lực từng khúc được gộp vào một biểu thức duy nhất.

#### Chính sách kinh tế kích hoạt muộn
- Bài toán: Một gói can thiệp chỉ bắt đầu triển khai từ quý thứ hai hoặc năm thứ ba.
- Mô hình: $$ u(t-a)f(t-a) $$.
- Giả thiết và giới hạn: Tác động kích hoạt ngay tại mốc $$ a $$, không có độ trễ phân tán nội tại.
- Diễn giải: Cho phép giải bài toán từng giai đoạn trong một lần biến đổi Laplace duy nhất.

### 2. Trực giác bổ sung và các kết nối

Hàm bước biến việc mô tả các tình huống thực tế (đóng-ngắt, trễ thời gian) thành thao tác đại số chuẩn mực. Điểm cần đặc biệt lưu ý là luôn đưa hàm sau công tắc về đúng biến dịch $$ t-a $$ trước khi áp dụng định lý dịch thời gian.

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

Một nguồn được bật tại $$ t=2 $$ với biên độ bằng 3:
$$
f(t)=
\begin{cases}
0, & 0\le t<2,\\
3, & t\ge 2.
\end{cases}
$$
Ta viết gọn $$ f(t)=3u(t-2) $$ và thu được $$ \mathcal{L}\{f(t)\}=3\frac{e^{-2s}}{s} $$. Khi đưa nguồn này vào ODE tuyến tính, ta giải trực tiếp một lần trong miền $$ s $$ thay vì tách hai khoảng thời gian rồi nối nghiệm thủ công.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo viết hàm từng khúc bằng Heaviside và áp dụng định lý dịch thời gian xuôi và ngược.

**Bậc sau đại học.** Xử lý tín hiệu nhiều bậc, nhiều lần đóng-ngắt và phân tích đáp ứng của hệ với đầu vào tuần hoàn từng khúc.

## Video tham khảo

- Xem trước: [Step and Delta Functions | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=q0PxCQWG3ic) — MIT OpenCourseWare, tiếng Anh. Giới thiệu hàm bước đơn vị và cách biểu diễn ngoại lực gián đoạn bằng hàm Heaviside.
- [Unit Step and Impulse Response | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=LjqUV6vqwkg) — MIT OpenCourseWare, tiếng Anh. Trình bày đáp ứng bước của hệ tuyến tính.
- [Laplace: Solving ODE's | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=5av3kiejazQ) — MIT OpenCourseWare, tiếng Anh. Minh họa quy trình giải ODE giữ nguyên sau khi vế phải được viết bằng hàm bước.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giải thích rõ định lý dịch thời gian.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ kỹ thuật về tín hiệu gián đoạn.
- Ross — *Differential Equations*: ngắn gọn, thuận tiện để ôn thao tác với hàm Heaviside.
