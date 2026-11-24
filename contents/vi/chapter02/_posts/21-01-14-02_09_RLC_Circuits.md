---
layout: post
title: "02-09 Mạch điện RLC"
chapter: '02'
order: 9
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---

Mỗi khi bạn xoay núm dò đài radio hoặc khi điện thoại lọc lấy đúng băng tần Wi-Fi giữa hàng trăm tín hiệu nhiễu trong không khí, bên trong thiết bị là một **mạch điện RLC** đang thực hiện phép cộng hưởng tần số! Kỳ diệu hơn nữa, phương trình Kirchhoff của mạch RLC giống hệt từng ký tự với phương trình lò xo–vật nặng—biến mọi trực giác cơ học của bạn thành hiểu biết sâu sắc về kỹ thuật điện tử.

## Bản đồ kiến thức nền: Bốn trụ cột của Mạch điện RLC nối tiếp

1. **Định luật điện áp Kirchhoff ($L q'' + R q' + \frac{1}{C} q = E(t)$)**:
   Tổng độ sụt áp qua cuộn cảm ($L i'$), điện trở ($R i$) và tụ điện ($q/C$) bằng sức điện động nguồn $E(t)$, với dòng điện $i(t) = q'(t)$.
2. **Từ điển tương đương Cơ – Điện hoàn hảo**:
   Độ tự cảm $L \leftrightarrow$ khối lượng $m$ (quán tính dòng); điện trở $R \leftrightarrow$ lực cản $c$ (tỏa nhiệt); nghịch đảo điện dung $1/C \leftrightarrow$ độ cứng lò xo $k$ (tích trữ thế năng).
3. **Trở kháng phức $Z(\omega) = R + i\left(\omega L - \frac{1}{\omega C}\right)$**:
   Trong chế độ xoay chiều $E(t) = E_0\cos(\omega t)$, biên độ dòng điện xác lập gọn đẹp thành $I_0 = \frac{E_0}{\vert Z(\omega)\vert} = \frac{E_0}{\sqrt{R^2 + (\omega L - 1/(\omega C))^2}}$.
4. **Cộng hưởng điện & Hệ số phẩm chất $Q$**:
   Khi cảm kháng triệt tiêu dung kháng ($\omega_0 = \frac{1}{\sqrt{LC}}$), trở kháng đạt cực tiểu $\vert Z\vert = R$, dòng điện đạt đỉnh cực đại $I_{\max} = E_0/R$—chính là cơ chế chọn lọc tần số của bộ lọc thông dải!

## Mục tiêu
Bài học này giúp sinh viên thấy cách phương trình cấp hai xuất hiện trong mạch điện RLC nối tiếp, nắm sự tương đồng cấu trúc giữa mạch điện và dao động cơ học, giải các bài toán đáp ứng tự do và cưỡng bức cơ bản, đồng thời diễn giải vai trò của điện trở, điện cảm và điện dung theo ngôn ngữ động học.

## Kiến thức nền
Sinh viên cần nắm ODE tuyến tính cấp hai hệ số hằng, bài học về dao động cơ học và định luật điện áp Kirchhoff. Không cần nền tảng điện tử chuyên sâu; điều quan trọng là hiểu quan hệ giữa điện tích $$ q(t) $$, dòng điện $$ i(t)=q'(t) $$ và điện áp trên từng phần tử.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-09 Mạch điện RLC]({{ site.imgurl }}/chapter_img/chapter02/02_09_rlc_circuits.svg)

Mạch RLC nối tiếp là ví dụ rõ nét về tính thống nhất của toán học ứng dụng: hệ khối lượng - lò xo - giảm chấn trong cơ học và mạch điện cảm - điện trở - tụ điện trong kỹ thuật điện tuy khác bản chất vật lý nhưng có chung một cấu trúc phương trình vi phân cấp hai.

Trong mạch RLC, điện cảm đóng vai trò quán tính, điện trở đóng vai trò tiêu tán năng lượng (lực cản), còn tụ điện tạo cơ chế hồi phục. Nhờ sự tương ứng này, các chế độ quá tắt dần, tắt dần tới hạn, dưới tắt dần và cộng hưởng điện học đều có thể phân tích bằng chính công cụ của dao động cơ học.

### Khung giải thích (nên đọc chậm): Tính tần số cộng hưởng và biên độ dòng xác lập cho mạch RLC ($L = 0{,}5\text{ H},\; R = 10\,\Omega,\; C = 2\times 10^{-3}\text{ F},\; E(t) = 20\cos(\omega t)$)

1. **Tính tần số góc cộng hưởng $\omega_0$**:
   $$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{0{,}5 \times 2\times 10^{-3}}} = \frac{1}{\sqrt{10^{-3}}} \approx \mathbf{31{,}62\text{ rad/s}} \quad (f_0 \approx 5{,}03\text{ Hz}).$$
2. **Tại đúng tần số cộng hưởng $\omega = \omega_0$**:
   Cảm kháng $\omega_0 L = 15{,}81\,\Omega$ triệt tiêu đúng dung kháng $\frac{1}{\omega_0 C} = 15{,}81\,\Omega$, nên $\vert Z(\omega_0)\vert = R = 10\,\Omega$.
   Biên độ dòng điện cực đại: $I_0(\omega_0) = \frac{20}{10} = \mathbf{2{,}0\text{ A}}$ (cùng pha với điện áp nguồn).
3. **Khi lệch tần số sang $\omega = 50\text{ rad/s}$**:
   - $\omega L - \frac{1}{\omega C} = 25 - \frac{1}{0{,}1} = 15\,\Omega$.
   - $\vert Z(50)\vert = \sqrt{10^2 + 15^2} = \sqrt{325} \approx 18{,}03\,\Omega \implies I_0(50) = \frac{20}{18{,}03} \approx \mathbf{1{,}11\text{ A}}$ (giảm gần một nửa!).

## Khái niệm theo ba cách
### Cách nhìn trực quan
Nếu trong cơ học khối lượng cản trở sự thay đổi đột ngột của vận tốc, thì trong mạch điện cuộn cảm cản trở sự thay đổi đột ngột của dòng điện. Tụ điện tích trữ năng lượng điện trường tương tự lò xo tích trữ thế năng đàn hồi, còn điện trở tiêu tán năng lượng dưới dạng nhiệt giống như ma sát.

### Cách nhìn hình ảnh
Tùy vào giá trị các phần tử, điện tích hoặc dòng điện trong mạch RLC có thể dao động tắt dần, suy giảm không dao động hoặc cộng hưởng dưới nguồn xoay chiều. Đồ thị tín hiệu theo thời gian mang hình dạng tương tự hoàn toàn với đồ thị dao động cơ học.

### Cách nhìn hình thức
Theo định luật điện áp Kirchhoff cho mạch RLC nối tiếp:
$$
L\frac{d^2q}{dt^2}+R\frac{dq}{dt}+\frac{1}{C}q=E(t),
$$
trong đó $$ q(t) $$ là điện tích trên tụ và $$ i(t)=q'(t) $$ là dòng điện. Khi $$ E(t)=0 $$, ta thu được đáp ứng tự do; khi $$ E(t)\neq 0 $$, ta thu được đáp ứng cưỡng bức.

## Những ngộ nhận thường gặp
- "Mạch điện chỉ dẫn đến phương trình cấp một." Sai: mạch RLC nối tiếp có hai phần tử tích trữ năng lượng ($$ L $$ và $$ C $$) nên tự nhiên dẫn đến ODE cấp hai.
- "Điện trở càng lớn thì mạch càng về cân bằng nhanh hơn." Không đúng: điện trở vượt quá ngưỡng tới hạn làm hệ chuyển sang chế độ quá tắt dần và quay về cân bằng chậm hơn.
- "Có dao động nghĩa là mạch không có điện trở." Sai: khi điện trở nhỏ ($$ R^2 < 4L/C $$), mạch vẫn dao động nhưng biên độ tắt dần.
- "Cộng hưởng chỉ xuất hiện trong cơ học." Sai: cộng hưởng điện học là cơ sở của mạch chọn tần, bộ lọc và xử lý tín hiệu.

## Tiến trình học tập đề xuất
### Bước 1: Áp dụng định luật Kirchhoff
Tổng điện áp trên cuộn cảm, điện trở và tụ điện bằng sức điện động của nguồn ngoài.

### Bước 2: Chọn biến trạng thái
Thường chọn điện tích $$ q(t) $$, sau đó suy ra dòng điện qua $$ i(t)=q'(t) $$.

### Bước 3: Phân tích phần thuần nhất
Xác định chế độ tắt dần từ phương trình đặc trưng.

### Bước 4: Tìm đáp ứng cưỡng bức khi có nguồn
Phân biệt rõ thành phần quá độ và thành phần trạng thái ổn định.

### Các checkpoint
- Sinh viên có viết đúng phương trình vi phân cho $$ q(t) $$ hay không.
- Sinh viên có lập được bảng tương ứng giữa mạch RLC và dao động cơ học hay không.
- Sinh viên có diễn giải được hành vi dài hạn của tín hiệu trong mạch hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Mạch không nguồn
Xét phương trình $$ q''+4q'+5q=0 $$. Phương trình đặc trưng $$ r^2+4r+5=0 $$ có nghiệm $$ r=-2\pm i $$, nên
$$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right). $$
Điện tích dao động tắt dần về 0, kéo theo dòng điện $$ i=q' $$ cũng tắt dần về 0.

### Ví dụ 2: Tắt dần tới hạn trong mạch
Xét phương trình $$ q''+6q'+9q=0 $$. Phương trình đặc trưng có nghiệm kép $$ r=-3 $$, nên
$$ q(t)=\left(c_1+c_2t\right)e^{-3t}. $$
Đây là đáp ứng không dao động và trở về 0 nhanh nhất trong các chế độ không dao động.

### Ví dụ 3: Mạch có nguồn không đổi
Xét phương trình $$ q''+3q'+2q=10 $$. Nghiệm thuần nhất là $$ q_h=c_1e^{-t}+c_2e^{-2t} $$. Thử nghiệm riêng hằng $$ q_p=A $$ cho $$ 2A=10 \Rightarrow A=5 $$. Vậy
$$ q(t)=c_1e^{-t}+c_2e^{-2t}+5. $$
Về dài hạn, điện tích trên tụ tiến dần về giá trị ổn định bằng 5.

### Ví dụ 4: Nguồn tuần hoàn và cộng hưởng
Xét mạch lý tưởng không điện trở $$ q''+q=\cos t $$, trong đó tần số nguồn trùng tần số riêng của mạch. Nghiệm riêng có dạng cộng hưởng $$ q_p=\frac{1}{2}t\sin t $$, nên
$$ q(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Biên độ tăng tuyến tính theo thời gian, minh họa hiện tượng cộng hưởng điện học không cản.

## Câu hỏi khái niệm
1. Vì sao mạch RLC nối tiếp và hệ khối lượng - lò xo có cùng cấu trúc phương trình vi phân?
2. Điện trở tác động đến tín hiệu tương tự lực cản cơ học theo cách nào?
3. Trong mạch có nguồn tuần hoàn, vì sao cần tách thành phần quá độ khỏi thành phần ổn định?

## Bài toán ứng dụng
1. Một mạch lọc tín hiệu cần triệt tiêu nhanh dao động quá độ. Hãy giải thích vai trò của điện trở trong thiết kế.
2. Một mạch thu vô tuyến cần nhạy với một tần số xác định. Hãy liên hệ yêu cầu này với tần số riêng của mạch RLC.
3. Một cảm biến điện tử có tín hiệu đầu ra dao động trước khi ổn định. Hãy giải thích hiện tượng bằng mô hình RLC.

## Chiến lược giảng dạy tương tác
- Yêu cầu sinh viên ghép cặp các đại lượng tương ứng giữa cơ học và điện học: khối lượng với điện cảm, lực cản với điện trở, độ cứng lò xo với nghịch đảo điện dung.
- Đặt hai phương trình cơ học và RLC cạnh nhau để lớp phân tích điểm giống và khác.
- Hỏi sinh viên: "Nếu tăng điện trở, đáp ứng của mạch thay đổi theo những chế độ nào?"
- Sử dụng mô phỏng mạch đơn giản hoặc đồ thị đáp ứng bước để tăng trực giác.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên dùng bảng đối chiếu song song giữa cơ học và điện học để sinh viên tận dụng ngay kiến thức đã học từ bài dao động cơ học.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên tính hàm truyền của mạch RLC hoặc khảo sát biên độ trạng thái ổn định theo tần số của nguồn xoay chiều.

## Tóm tắt dễ nhớ
Mạch RLC nối tiếp là bản tương đương điện học của hệ dao động cơ học. Trong phương trình
$$ Lq''+Rq'+\frac{1}{C}q=E(t), $$
điện cảm $$ L $$ đóng vai trò quán tính, điện trở $$ R $$ đóng vai trò lực cản và nghịch đảo điện dung $$ 1/C $$ đóng vai trò độ cứng hồi phục.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Bộ lọc điện tử bậc hai
- Bài toán: Mạch RLC được dùng để lọc nhiễu hoặc chọn tần số trong xử lý tín hiệu.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Giả thiết và giới hạn: Các linh kiện lý tưởng và tuyến tính.
- Diễn giải: Mạch có thể dao động, tắt dần hoặc cộng hưởng điện học tùy theo tham số và nguồn kích thích.

#### Đóng mạch và đáp ứng quá độ
- Bài toán: Ngay sau khi đóng công tắc, dòng điện và điện tích không đạt ngay trạng thái ổn định mà trải qua giai đoạn quá độ.
- Mô hình: Phương trình RLC cấp hai.
- Giả thiết và giới hạn: Bỏ qua đặc tính chuyển mạch phi tuyến của linh kiện bán dẫn như diode hay transistor.
- Diễn giải: Nghiệm thuần nhất mô tả giai đoạn quá độ, còn nghiệm riêng mô tả trạng thái vận hành ổn định do nguồn tạo ra.

#### Cảm biến cộng hưởng điện cơ
- Bài toán: Thiết bị đo nhạy nhất quanh một dải tần số riêng xác định.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E_0\cos \omega t. $$
- Giả thiết và giới hạn: Một chế độ dao động chi phối và nguồn kích thích điều hòa thuần.
- Diễn giải: Cộng hưởng điện học là bản tương đương trực tiếp của cộng hưởng cơ học.

### 2. Trực giác bổ sung và các kết nối

Mạch RLC củng cố sự tương đương cấu trúc giữa các ngành: điện cảm $$ L $$ tương ứng khối lượng $$ m $$, điện trở $$ R $$ tương ứng hệ số cản $$ c $$, và nghịch đảo điện dung $$ 1/C $$ tương ứng độ cứng lò xo $$ k $$. Một ngộ nhận thường gặp là cho rằng điện trở càng lớn thì đáp ứng càng tốt; thực tế, cản quá lớn khiến hệ trở về cân bằng chậm hơn so với chế độ tắt dần tới hạn.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 800)
q = np.exp(-2*t) * (np.cos(t) + 0.5*np.sin(t))
i = np.gradient(q, t)

plt.plot(t, q, label="Điện tích q(t)")
plt.plot(t, i, label="Dòng điện i(t)=q'(t)")
plt.xlabel("t")
plt.ylabel("Biên độ")
plt.title("Đáp ứng tắt dần của mạch RLC")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Vẽ điện tích và dòng điện trên cùng đồ thị giúp thấy rõ mối liên hệ đạo hàm giữa hai đại lượng khi chọn biến trạng thái là $$ q(t) $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: RLC circuit resonance interactive
- search: transient response RLC animation
- search: circuit mechanical analogy visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét mạch không nguồn
$$ q''+4q'+5q=0,\qquad q(0)=1,\qquad q'(0)=0. $$
Nghiệm tổng quát là $$ q(t)=e^{-2t}\left(c_1\cos t+c_2\sin t\right) $$. Áp dụng điều kiện đầu thu được
$$ q(t)=e^{-2t}\left(\cos t+2\sin t\right). $$
Dòng điện $$ i(t)=q'(t) $$ cũng tắt dần về 0. Đây là đáp ứng quá độ dao động tắt dần do năng lượng trao đổi qua lại giữa cuộn cảm và tụ điện đồng thời tiêu tán trên điện trở.

### 6. Phân tầng độ khó

**Bậc đại học.** Lập đúng phương trình mạch RLC, giải phần thuần nhất và đối chiếu với dao động cơ học.

**Bậc sau đại học.** Mở rộng sang hàm truyền, đáp ứng tần số và thiết kế mạch chọn lọc băng thông.

## Video tham khảo

- Xem trước: [PHYS 102 | RLC Circuits 1 - The Differential Equation for the RLC Circuit](https://www.youtube.com/watch?v=gmjyBJ9nyZU) — Professor Hafner, tiếng Anh. Xây dựng phương trình vi phân cấp hai cho mạch RLC nối tiếp, tương đồng với dao động có cản.
- [Lecture 20 - RLC circuits and resonance](https://www.youtube.com/watch?v=JSiTC1tCLBg) — Thomas Carr - Math Lectures, tiếng Anh. Phân tích hiện tượng cộng hưởng từ phương trình mạch RLC.
- [Forced Oscillations | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=xJz3NZap1lw) — MIT OpenCourseWare, tiếng Anh. Phân tích dao động cưỡng bức và đáp ứng tuần hoàn ổn định, áp dụng tương tự cho mạch điện chịu nguồn xoay chiều.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ sự tương đồng giữa mạch RLC và dao động cơ học.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài luyện về đáp ứng quá độ và cưỡng bức.
- Ross — *Differential Equations*: ngắn gọn, phù hợp để ôn cấu trúc mô hình.
