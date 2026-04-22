---
layout: post
title: "Tán Sắc và Hấp Thụ"
chapter: '10'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: optional
---
![21 03 11 10 07 Dispersion Dissipation]({{ site.imgurl }}/chapter_img/chapter10/07_dispersion_dissipation.svg)

## Mục tiêu

Bài học này mở rộng mô hình sóng lý tưởng sang hai cơ chế rất quan trọng trong thực tế: tán sắc và hấp thụ. Sau bài học, sinh viên cần hiểu tán sắc là gì, phân biệt vận tốc pha với vận tốc nhóm, biết vì sao gói sóng có thể biến dạng khi các tần số chạy với tốc độ khác nhau, và hiểu cách thêm tắt dần làm năng lượng sóng suy giảm theo thời gian.

## Kiến thức nền

Sinh viên nên nắm sóng phẳng, phương trình sóng cơ bản và số phức ở mức vừa đủ để hiểu nghiệm dạng $$ e^{i(kx-\omega t)} $$. Đây là bài quan trọng để chuyển từ sóng lý tưởng sang sóng thực tế.

## Dẫn nhập

Trong mô hình sóng lý tưởng, mọi tần số truyền cùng một tốc độ nên gói sóng giữ nguyên hình dạng. Nhưng thực tế hiếm khi lý tưởng như vậy. Nước sâu, plasma, sợi quang, vật liệu đàn hồi thực, và cả nhiều mô hình trường đều cho thấy các tần số khác nhau truyền khác nhau. Khi đó gói sóng bị trải ra, méo dạng hoặc chậm dần. Đó là tán sắc.

Ngoài ra, môi trường thật còn có tổn hao. Ma sát, hấp thụ, cản nhớt, mất mát điện từ làm biên độ sóng giảm dần. Khi kết hợp tán sắc và hấp thụ, ta có bức tranh gần hơn nhiều với các hệ vật lý thực.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một gói sóng là sự chồng của nhiều tần số, và mỗi tần số chạy với tốc độ hơi khác nhau, thì theo thời gian chúng sẽ không còn "đi cùng nhau" nữa. Gói sóng bị kéo dài, tách pha hoặc méo. Đó là tán sắc. Nếu đồng thời môi trường hút năng lượng từ sóng, biên độ toàn bộ gói cũng giảm đi. Đó là hấp thụ hay tắt dần.

### Cách nhìn hình ảnh

Với sóng không tán sắc, một gói xung di chuyển như một khối gần như giữ nguyên hình. Với sóng tán sắc, bao sóng thay đổi độ rộng theo thời gian. Nếu có hấp thụ, bao sóng còn hạ biên độ dần. Hình ảnh này rất mạnh vì nó cho thấy sóng thực tế hiếm khi chỉ "chạy đi" một cách lý tưởng.

### Cách nhìn hình thức

Một sóng phẳng có dạng $$ u(x,t)=e^{i(kx-\omega t)} $$. Quan hệ $$ \omega=\omega(k) $$ gọi là quan hệ tán sắc.

- Nếu

$$ \omega=ck, $$

thì không tán sắc.
- Nếu

$$ \omega $$

phụ thuộc phi tuyến vào $$ k $$, ta có tán sắc.

Vận tốc pha:

$$ v_p=\frac{\omega}{k}. $$

Vận tốc nhóm:

$$ v_g=\frac{d\omega}{dk}. $$

Nếu thêm hấp thụ, một mô hình đơn giản là

$$ u_{tt}+\gamma u_t=c^2u_{xx},
\qquad \gamma>0. $$

## Những ngộ nhận thường gặp

- "Tán sắc nghĩa là sóng bị mất năng lượng." Không đúng; tán sắc là chuyện các tần số đi lệch tốc độ, không nhất thiết làm giảm năng lượng.
- "Vận tốc pha và vận tốc nhóm luôn giống nhau." Chỉ đúng trong môi trường không tán sắc.
- "Hấp thụ và tán sắc là cùng một hiện tượng." Sai. Một cái làm lệch pha giữa các tần số, một cái rút năng lượng khỏi hệ.
- "Nếu gói sóng méo đi thì chắc chắn là do hấp thụ." Không hẳn; tán sắc một mình cũng đã đủ làm méo dạng.

## Tiến trình học tập đề xuất

### Bước 1: Học quan hệ tán sắc

Đây là cốt lõi của bài.

### Bước 2: Phân biệt vận tốc pha và vận tốc nhóm

Sinh viên nên thật rõ hai khái niệm này.

### Bước 3: Xét ví dụ tán sắc đơn giản

Klein-Gordon là ví dụ mẫu rất tốt.

### Bước 4: Thêm hấp thụ

So sánh cơ chế mất pha với cơ chế mất năng lượng.

### Các checkpoint

- Sinh viên có phát biểu được tán sắc bằng lời hay không.
- Sinh viên có phân biệt được vận tốc pha và nhóm hay không.
- Sinh viên có giải thích được vì sao thêm

$$ \gamma u_t $$

làm sóng tắt dần hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Sóng không tán sắc

Với phương trình sóng chuẩn $$ u_{tt}=c^2u_{xx} $$, ta có $$ \omega=ck $$. Khi đó $$ v_p=v_g=c $$. Điều này giải thích vì sao gói sóng lý tưởng giữ nguyên hình dạng.

### Ví dụ 2: Phương trình Klein-Gordon

Xét $$ u_{tt}-c^2u_{xx}+m^2u=0 $$. Ta có $$ \omega^2=c^2k^2+m^2 $$. Đây là quan hệ tán sắc phi tuyến, nên $$ v_p\ne v_g $$. Ví dụ này cho sinh viên thấy chỉ cần một số hạng bổ sung là cấu trúc lan truyền đã đổi khác.

### Ví dụ 3: Tắt dần

Với $$ u_{tt}+\gamma u_t=c^2u_{xx} $$, số hạng $$ \gamma u_t $$ làm năng lượng giảm theo thời gian. Ví dụ này rất tốt để nối với bài năng lượng đã học trước đó.

### Ví dụ 4: Gói sóng

Một gói sóng là chồng của nhiều tần số gần nhau. Nếu quan hệ tán sắc phi tuyến, các thành phần này sẽ dần lệch nhau, làm gói sóng trải rộng. Đây là ví dụ khái niệm quan trọng nhất của bài.

## Câu hỏi khái niệm

1. Vì sao tán sắc làm gói sóng méo dạng dù không nhất thiết làm mất năng lượng?
2. Vận tốc pha và vận tốc nhóm phản ánh hai khía cạnh nào của sóng?
3. Vì sao thêm hạng $$ \gamma u_t $$ lại tạo ra hấp thụ?

## Bài toán ứng dụng

1. Trong sợi quang, vì sao các xung tín hiệu có thể bị trải rộng theo thời gian truyền?
2. Trong sóng nước, vì sao các gợn với bước sóng khác nhau có thể di chuyển không đồng tốc?
3. Trong âm học hoặc vật liệu nhớt, vì sao biên độ sóng giảm dần ngay cả khi không có biên phản xạ?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Một gói sóng có thể chạy mà vẫn giữ nguyên hình dạng mãi không?"
- Vẽ hoặc mô tả một gói sóng không tán sắc và một gói sóng tán sắc để lớp so sánh.
- Hỏi cả lớp: "Điều gì khác nhau giữa sóng yếu dần và sóng méo dạng?"
- Khuyến khích sinh viên giải thích vận tốc pha và nhóm bằng ngôn ngữ 'sóng mang' và 'bao sóng'.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám vào một ví dụ duy nhất về sóng phẳng và một ví dụ duy nhất về gói sóng. Khi trực giác đã hình thành, các công thức $$ v_p,\ v_g $$ sẽ dễ nhớ hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thực hiện khai triển quanh một số sóng trung tâm để suy ra vận tốc nhóm, hoặc thảo luận mối liên hệ giữa tán sắc và hình học phổ của toán tử.

## Tóm tắt dễ nhớ

Tán sắc là hiện tượng các tần số khác nhau truyền với tốc độ khác nhau, làm gói sóng méo dạng. Hấp thụ là hiện tượng biên độ và năng lượng sóng giảm dần theo thời gian. Một bên làm lệch pha, một bên làm mất năng lượng, và cả hai đều rất phổ biến trong sóng thực tế.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tán sắc trong sóng nước hay quang học
- Bài toán: Các tần số khác nhau truyền với tốc độ pha khác nhau nên gói sóng dần dãn ra.
- Mô hình: Quan hệ phân tán $$ \omega=\omega(k) $$ không tuyến tính theo số sóng $$ k $$.
- Giả thiết và giới hạn: Môi trường tuyến tính nhưng có cơ chế tán sắc.
- Diễn giải: Không phải mọi phương trình dạng sóng đều truyền nguyên hình như trường hợp lý tưởng.

#### Tiêu tán trong môi trường có ma sát
- Bài toán: Dây rung trong không khí hoặc vật liệu nhớt mất biên độ theo thời gian.
- Mô hình:
$$ u_{tt}+\gamma u_t=c^2u_{xx}. $$
- Giả thiết và giới hạn: Tắt dần tuyến tính, hệ số $$ \gamma $$ hằng.
- Diễn giải: Tắt dần làm hao năng lượng và suy giảm dao động.

### 2. Trực giác bổ sung và các kết nối

Tán sắc làm thay đổi hình dạng sóng vì các thành phần Fourier chạy với tốc độ khác nhau; tiêu tán làm giảm biên độ do năng lượng bị mất đi. Hai khái niệm này thường bị trộn lẫn, nhưng về cơ chế toán học chúng hoàn toàn khác nhau.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 800)
for t in [0.0, 1.0, 2.0]:
    width = 1 + 0.5 * t
    packet = np.exp(-(x / width) ** 2) * np.cos(2 * x)
    damped = np.exp(-0.4 * t) * np.exp(-(x / 2.0) ** 2) * np.cos(2 * x)
    plt.plot(x, packet, label=f"Tan sac t={t}")
    plt.plot(x, damped, linestyle="--", label=f"Tieu tan t={t}")

plt.xlabel("x")
plt.title("So sanh tan sac va tieu tan")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: dispersion vs dissipation wave packet animation
- search: damped wave equation visualization
- search: group velocity dispersion optics simulation

### 5. Bài toán mẫu có bối cảnh thực

Một mode trên dây tắt dần có thể được viết gần đúng dưới dạng
$$ u(x,t)=e^{-\gamma t/2}\sin(kx)\cos(\omega_d t), $$
với $$ \omega_d $$ là tần số đã hiệu chỉnh bởi tắt dần. Hệ số mũ cho thấy năng lượng không còn được bảo toàn mà giảm dần theo thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt tán sắc với tiêu tán qua hành vi của biên độ và dạng sóng.

**Bậc sau đại học.** Kết nối với group velocity, semigroup tắt dần và phương trình KdV hay Schrödinger tuyến tính.
