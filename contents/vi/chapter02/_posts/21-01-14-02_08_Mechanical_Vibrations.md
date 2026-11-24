---
layout: post
title: "02-08 Dao động Cơ học"
chapter: '02'
order: 8
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---

Tại sao một đoàn binh phải bước đi lệch nhịp khi qua cầu treo, còn hệ thống treo trên ô tô lại được kỹ sư tinh chỉnh chính xác đến từng phần trăm hệ số cản? Tất cả đều là biểu hiện vật lý trực tiếp của phương trình dao động cơ học $m x'' + c x' + k x = F(t)$—nơi các đại lượng đại số như phần thực nghiệm đặc trưng hay đỉnh hàm truyền biến thành cảm giác êm ái hay thảm họa cộng hưởng ngoài đời thực!

## Bản đồ kiến thức nền: Bốn trụ cột của Dao động Cơ học

1. **Cân bằng động lực $m x'' + c x' + k x = F(t)$**:
   Ba lực cạnh tranh nhau: lực quán tính ($m x''$), lực cản nhớt tiêu tán năng lượng ($c x'$) và lực hồi phục Hooke ($k x$); tần số tự nhiên không cản là $\omega_0 = \sqrt{k/m}$.
2. **Tỷ số cản $\zeta = \frac{c}{2\sqrt{mk}}$ & Ba chế độ dao động tự do**:
   $\zeta < 1$ (tắt dần yếu—dao động với $\omega_d = \omega_0\sqrt{1-\zeta^2}$), $\zeta = 1$ (tắt dần tới hạn—hồi vị nhanh nhất không dao động), $\zeta > 1$ (tắt dần mạnh—ì ạch).
3. **Dao động cưỡng bức: Trạng thái quá độ (Transient) vs. Xác lập (Steady-State)**:
   Khi $c > 0$, phần $y_h(t) \to 0$ theo hàm mũ; sau một thời gian ngắn, hệ hoàn toàn bị dẫn dắt bởi đáp ứng xác lập $y_p(t) = A(\omega)\cos(\omega t - \delta)$.
4. **Hiện tượng Phách & Cộng hưởng (Resonance)**:
   Biên độ xác lập $A(\omega) = \frac{F_0}{\sqrt{(k - m\omega^2)^2 + (c\omega)^2}}$ đạt đỉnh cực đại tại $\omega_{\text{res}} = \sqrt{\omega_0^2 - \frac{c^2}{2m^2}}$ (khi $c$ nhỏ); nếu $c = 0$ và $\omega = \omega_0$, biên độ tăng vô hạn theo $t$!

## Mục tiêu
Bài học này áp dụng các kỹ thuật của Chương 02 vào một mô hình vật lý trọng tâm: hệ khối lượng - lò xo - giảm chấn. Sinh viên sẽ học cách thiết lập phương trình, phân biệt dao động tự do với dao động cưỡng bức, nhận diện ba chế độ quá tắt dần, tắt dần tới hạn và dưới tắt dần, đồng thời hiểu hiện tượng cộng hưởng dưới góc nhìn cơ học.

## Kiến thức nền
Sinh viên cần nắm phương trình tuyến tính cấp hai hệ số hằng, nghiệm thực, nghiệm phức và phương trình không thuần nhất. Về vật lý, chỉ cần các kiến thức cơ bản: định luật Newton, lực đàn hồi Hooke và lực cản nhớt tuyến tính.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-08 Dao động Cơ học]({{ site.imgurl }}/chapter_img/chapter02/02_08_mechanical_vibrations.svg)

Dao động cơ học là ứng dụng tiêu biểu của ODE cấp hai vì mỗi hệ số trong phương trình đều mang ý nghĩa vật lý trực tiếp: khối lượng $$ m $$ đại diện cho quán tính, độ cứng lò xo $$ k $$ tạo lực hồi phục, còn hệ số cản $$ c $$ biểu diễn sự tiêu tán năng lượng. Từ ba tham số này, mô hình tái hiện được nhiều hiện tượng quen thuộc như dao động điều hòa, tắt dần, quay về cân bằng nhanh nhất không dao động và cộng hưởng dưới ngoại lực tuần hoàn.

Bài học cũng nhấn mạnh kỹ năng diễn giải nghiệm: mỗi dấu và tham số trả lời trực tiếp một câu hỏi cơ học như hệ có dao động không, dao động kéo dài bao lâu, trở về cân bằng theo cách nào và khi nào ngoại lực gây ra cộng hưởng.

### Khung giải thích (nên đọc chậm): Tính biên độ xác lập và độ khuếch đại cộng hưởng cho hệ $x'' + 0{,}4 x' + 4 x = 2\cos(\omega t)$

Hệ có $m = 1,\; c = 0{,}4,\; k = 4,\; F_0 = 2 \implies$ tần số riêng $\omega_0 = \sqrt{4/1} = \mathbf{2\text{ rad/s}}$, tỷ số cản $\zeta = \frac{0{,}4}{2\cdot 2} = \mathbf{0{,}1}$.
1. **Khi kích thích ở tần số thấp $\omega = 0$ (tải tĩnh $F = 2$)**:
   $A(0) = \frac{2}{4} = \mathbf{0{,}5\text{ m}}$.
2. **Khi kích thích đúng tần số riêng $\omega = \omega_0 = 2$**:
   $$A(2) = \frac{2}{\sqrt{(4 - 4)^2 + (0{,}4 \times 2)^2}} = \frac{2}{0{,}8} = \mathbf{2{,}5\text{ m}}.$$
3. **Hệ số khuếch đại động lực**: $\frac{A(2)}{A(0)} = \frac{2{,}5}{0{,}5} = \mathbf{5\text{ lần}}$ (đúng bằng $\frac{1}{2\zeta} = \frac{1}{0{,}2} = 5$)! Dù lực cưỡng bức không đổi cường độ $F_0 = 2$, chỉ cần chỉnh tần số trùng $\omega_0 = 2$ là biên độ rung vọt lên gấp 5 lần!

## Khái niệm theo ba cách
### Cách nhìn trực quan
Khi kéo lệch một vật gắn lò xo rồi thả ra, lò xo kéo vật về vị trí cân bằng. Nếu không có ma sát, vật vượt qua vị trí cân bằng và dao động mãi; nếu có lực cản, biên độ dao động giảm dần. Khi có ngoại lực tuần hoàn, vật có thể dao động mạnh nếu tần số kích thích gần tần số riêng của hệ.

### Cách nhìn hình ảnh
Ba chế độ tắt dần thể hiện rõ trên đồ thị:
- Quá tắt dần: vật trở về vị trí cân bằng không dao động nhưng chậm.
- Tắt dần tới hạn: vật trở về vị trí cân bằng nhanh nhất mà không dao động.
- Dưới tắt dần: vật dao động quanh cân bằng với biên độ giảm dần.

Khi có ngoại lực tuần hoàn, đồ thị kết hợp phần quá độ suy giảm dần và phần cưỡng bức ổn định theo tần số của nguồn kích thích.

### Cách nhìn hình thức
Với chuyển vị $$ x(t) $$ đo quanh vị trí cân bằng, mô hình chuẩn là
$$ m x''+c x'+k x=F(t). $$
Khi $$ F(t)=0 $$, hệ thực hiện dao động tự do; khi $$ F(t)\neq 0 $$, hệ thực hiện dao động cưỡng bức. Phương trình đặc trưng của phần thuần nhất là $$ m r^2+c r+k=0 $$, và biệt thức $$ \Delta=c^2-4mk $$ quyết định chế độ tắt dần của hệ.

## Những ngộ nhận thường gặp
- "Có lực cản thì vật không còn dao động." Sai: khi lực cản nhỏ ($$ c^2<4mk $$), hệ vẫn dao động với biên độ giảm dần.
- "Tắt dần tới hạn là mức cản lớn nhất." Sai: đó là ngưỡng cản vừa đủ để hệ trở về cân bằng nhanh nhất mà không dao động.
- "Cộng hưởng chỉ xảy ra khi không có lực cản." Sai: lực cản làm hữu hạn hóa biên độ cộng hưởng nhưng hệ vẫn có cực đại đáp ứng gần tần số riêng.
- "Nghiệm tổng chỉ là phép cộng hình thức." Sai: nó tách rõ phần đáp ứng quá độ và phần đáp ứng ổn định dài hạn.

## Tiến trình học tập đề xuất
### Bước 1: Thiết lập phương trình từ định luật Newton
Viết phương trình cân bằng lực với tổng lực bằng $$ mx'' $$.

### Bước 2: Phân tích phần thuần nhất
Xác định chế độ tắt dần dựa vào dấu của biệt thức $$ c^2-4mk $$.

### Bước 3: Tìm nghiệm riêng khi có ngoại lực
Thường xét trường hợp ngoại lực tuần hoàn hoặc không đổi.

### Bước 4: Diễn giải vật lý
Phân biệt phần quá độ và phần đáp ứng cưỡng bức dài hạn.

### Các checkpoint
- Sinh viên có đặt đúng dấu cho lực đàn hồi và lực cản hay không.
- Sinh viên có xác định đúng ba chế độ tắt dần từ biệt thức hay không.
- Sinh viên có giải thích được điều kiện và ý nghĩa của cộng hưởng hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Dao động tự do không cản
Xét phương trình $$ x''+9x=0 $$. Nghiệm tổng quát là
$$ x(t)=c_1\cos 3t+c_2\sin 3t. $$
Hệ dao động điều hòa với tần số góc bằng 3; cơ năng được bảo toàn nên biên độ không đổi.

### Ví dụ 2: Chế độ dưới tắt dần
Xét phương trình $$ x''+2x'+10x=0 $$. Phương trình đặc trưng $$ r^2+2r+10=0 $$ có nghiệm $$ r=-1\pm 3i $$, nên
$$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right). $$
Hệ vẫn dao động nhưng biên độ giảm theo $$ e^{-t} $$.

### Ví dụ 3: Chế độ tắt dần tới hạn
Xét phương trình $$ x''+6x'+9x=0 $$. Ta có $$ r^2+6r+9=\left(r+3\right)^2=0 $$, nên
$$ x(t)=\left(c_1+c_2t\right)e^{-3t}. $$
Hệ trở về cân bằng mà không dao động — đây là trường hợp tắt dần tới hạn.

### Ví dụ 4: Dao động cưỡng bức tuần hoàn có cộng hưởng
Xét phương trình $$ x''+x=\cos t $$. Nghiệm thuần nhất là $$ x_h=c_1\cos t+c_2\sin t $$. Do vế phải trùng tần số riêng của hệ, ta thử $$ x_p=At\sin t $$ (hoặc tổng quát $$ t(A\cos t+B\sin t) $$). Thay vào phương trình thu được $$ A=\frac{1}{2} $$, nên
$$ x(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Biên độ tăng tuyến tính theo thời gian vì tần số kích thích trùng đúng tần số riêng của hệ không cản.

## Câu hỏi khái niệm
1. Vì sao cùng một hệ khối lượng - lò xo nhưng mức cản khác nhau lại sinh ra ba chế độ hành vi khác nhau?
2. Vì sao cần phân biệt rõ phần quá độ và phần cưỡng bức ổn định về mặt vật lý?
3. Vì sao cộng hưởng là hiện tượng quan trọng cả về mặt toán học lẫn kỹ thuật?

## Bài toán ứng dụng
1. Hệ thống treo của xe máy nên thiết kế gần chế độ nào trong ba chế độ tắt dần, và vì sao?
2. Một tòa nhà cao tầng chịu tải trọng gió tuần hoàn. Hãy giải thích vì sao kỹ sư phải khảo sát tần số riêng của công trình.
3. Một thiết bị đo rung cần dập tắt dao động nhanh nhất mà không vượt quá vị trí cân bằng. Hãy liên hệ yêu cầu này với chế độ tắt dần tới hạn.

## Chiến lược giảng dạy tương tác
- Cho sinh viên quan sát ba đồ thị và nhận diện chế độ tắt dần trước khi giải phương trình.
- Sử dụng mô hình lò xo hoặc video minh họa để gắn biểu thức toán học với hiện tượng thực.
- Hỏi lớp: "Nếu tăng hệ số cản lên gấp đôi, chuyển động của hệ thay đổi thế nào?"
- Tổ chức thảo luận ngắn về hiện tượng cộng hưởng trong cầu, tòa nhà, nhạc cụ và máy móc.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên lập bảng so sánh bốn cột cho ba chế độ: điều kiện biệt thức, dạng nghiệm, dạng đồ thị và diễn giải cơ học.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên tính biên độ trạng thái ổn định của dao động cưỡng bức có cản và tìm tần số kích thích làm biên độ đạt cực đại.

## Tóm tắt dễ nhớ
Dao động cơ học được mô hình hóa bởi
$$ mx''+cx'+kx=F(t), $$
với $$ m,c,k $$ lần lượt biểu diễn quán tính, lực cản và lực hồi phục. Phần thuần nhất mô tả dao động tự do, còn vế phải mô tả tác động cưỡng bức. Khi phân tích bài toán, cần xác định mức độ cản và khoảng cách giữa tần số kích thích với tần số riêng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ treo ô tô
- Bài toán: Khung xe và bánh xe phản ứng trước mặt đường gồ ghề như một hệ lò xo - giảm chấn.
- Mô hình:
$$ m x''+c x'+k x=F(t). $$
- Giả thiết và giới hạn: Mô hình một bậc tự do là phép xấp xỉ; hệ treo thực có nhiều khối lượng và yếu tố phi tuyến.
- Diễn giải: Sự lựa chọn giữa dưới tắt dần, quá tắt dần và tắt dần tới hạn ảnh hưởng trực tiếp đến độ êm và độ bám đường.

#### Tòa nhà chịu kích thích tuần hoàn
- Bài toán: Gió hoặc rung động nền kích thích công trình gần tần số riêng.
- Mô hình:
$$ m x''+c x'+k x=F_0\cos \omega t. $$
- Giả thiết và giới hạn: Giả sử mô hình tuyến tính với dao động nhỏ quanh cân bằng.
- Diễn giải: Hiện tượng cộng hưởng giải thích vì sao thiết kế kết cấu phải tránh trùng tần số riêng với tần số kích thích phổ biến.

#### Cảm biến MEMS và dao động nội tại
- Bài toán: Một đầu cảm biến cơ điện vi mô có thể rung kéo dài nếu hệ số giảm chấn nhỏ.
- Mô hình: Hệ khối lượng - lò xo - giảm chấn.
- Giả thiết và giới hạn: Lực cản tuyến tính và một chế độ dao động chi phối.
- Diễn giải: Đáp ứng quá độ cho biết cảm biến ổn định nhanh hay tiếp tục dao động dư quá lâu.

### 2. Trực giác bổ sung và các kết nối

Dao động cơ học là nơi hội tụ các trường hợp của Chương 02: nghiệm thực phân biệt ứng với quá tắt dần, nghiệm kép ứng với tắt dần tới hạn, nghiệm phức ứng với dưới tắt dần, và nghiệm riêng mô tả đáp ứng cưỡng bức cùng cộng hưởng. Một nhầm lẫn phổ biến là nghĩ tắt dần tới hạn tương ứng với lực cản lớn nhất; thực chất đây là mức cản nhỏ nhất giúp hệ không dao động và trở về cân bằng nhanh nhất.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
over = 2*np.exp(-t) - np.exp(-3*t)
critical = (1 + t) * np.exp(-2*t)
under = np.exp(-0.5*t) * np.cos(3*t)

plt.plot(t, over, label="Quá tắt dần")
plt.plot(t, critical, label="Tắt dần tới hạn")
plt.plot(t, under, label="Dưới tắt dần")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Ba chế độ dao động cơ học")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị đặt cả ba chế độ trên cùng hệ trục giúp so sánh trực tiếp tốc độ trở về cân bằng và tính chất dao động.

### 4. Gợi ý tìm thêm mô phỏng

- search: mass spring damper interactive
- search: critical damping animation
- search: mechanical resonance simulation

### 5. Bài toán mẫu có bối cảnh thực

Một hệ treo đơn giản hóa được mô tả bởi
$$ x''+2x'+10x=0,\qquad x(0)=0.05,\qquad x'(0)=0. $$
Nghiệm tổng quát là $$ x(t)=e^{-t}\left(c_1\cos 3t+c_2\sin 3t\right) $$. Áp dụng điều kiện đầu, ta được
$$
x(t)=0.05e^{-t}\left(\cos 3t+\frac{1}{3}\sin 3t\right).
$$
Hệ vẫn dao động với biên độ suy giảm theo $$ e^{-t} $$, mô tả phản ứng giảm chấn tương đối êm nhưng vẫn có dao động trước khi ổn định hẳn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập mô hình và phân biệt chính xác ba chế độ tắt dần từ biệt thức.

**Bậc sau đại học.** Khảo sát biên độ trạng thái ổn định dưới ngoại lực tuần hoàn, cộng hưởng có cản và hàm truyền cơ học.

## Video tham khảo

- Xem trước: [Undamped Mechanical Vibrations & Hooke's Law // Simple Harmonic Motion](https://www.youtube.com/watch?v=Z52emur7Rko) — Dr. Trefor Bazett, tiếng Anh. Giới thiệu dao động Hooke không cản và ý nghĩa của tần số riêng.
- [Mechanical Vibrations: Underdamped vs Overdamped vs Critically Damped](https://www.youtube.com/watch?v=CTd1uVq5-l8) — Dr. Trefor Bazett, tiếng Anh. So sánh dao động tự do dưới tắt dần, quá tắt dần và tắt dần tới hạn.
- [Damped Harmonic Oscillators | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=2-5oq-igwtU) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về dao động điều hòa có cản.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: phần dao động cơ học trình bày trực quan và hệ thống.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều ví dụ về hệ khối lượng - lò xo và cộng hưởng.
- Ross — *Differential Equations*: hữu ích để ôn nhanh các chế độ tắt dần.
