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

Phương trình sóng lý tưởng $u_{tt} = c^2 u_{xx}$ đưa mọi xung sóng đi xa mãi mãi mà không hề méo dạng hay yếu đi. Thế nhưng ngoài đời thực, một xung ánh sáng đi qua lăng kính thủy tinh bị tách thành cầu vồng (sóng đỏ chạy nhanh hơn sóng tím!), còn tiếng hô trong rừng cứ yếu dần rồi tắt hẳn. Hai cơ chế vật lý làm thay đổi hình dạng và biên độ sóng đó chính là **Tán sắc (Dispersion)** và **Hấp thụ / Tiêu tán (Dissipation)**—được đọc trọn vẹn chỉ từ một biểu thức đại số duy nhất: **Hệ thức Tán sắc $\omega(k)$**!

## Bản đồ kiến thức nền: Bốn trụ cột của Hệ thức Tán sắc $\omega(k)$

1. **Cách tìm Hệ thức Tán sắc $\omega(k)$**:
   Thế sóng phẳng thử $u(x, t) = e^{i(kx - \omega t)}$ vào bất kỳ PDE tuyến tính hệ số hằng nào (thay $\partial_t \to -i\omega$, $\partial_x \to ik$) sẽ thu ngay phương trình đại số liên hệ tần số $\omega$ và số sóng $k$!
2. **Vận tốc Pha ($v_p = \omega/k$) vs. Vận tốc Nhóm ($v_g = d\omega/dk$)**:
   - $v_p$ là tốc độ của từng đỉnh sóng đơn sắc.
   - $v_g = \frac{d\omega}{dk}$ mới là tốc độ truyền **bao hình gói sóng và năng lượng**! Sóng có **tán sắc** khi $v_p$ phụ thuộc vào $k$ (tức $\omega''(k) \neq 0$, như phương trình Klein–Gordon $u_{tt} = c^2 u_{xx} - m^2 u$ hay sóng mặt nước).
3. **Hấp thụ / Tiêu tán ($\operatorname{Im}(\omega) < 0$)**:
   Khi $\omega(k) = \omega_R - i\gamma$ ($\gamma > 0$), nhân tử thời gian trở thành $e^{-i\omega t} = e^{-\gamma t} e^{-i\omega_R t}$ — biên độ suy giảm hàm mũ theo thời gian (ví dụ phương trình điện báo có cản $u_{tt} + 2\beta u_t = c^2 u_{xx}$)!
4. **Cân bằng Tán sắc – Phi tuyến (Soliton)**:
   Khi tán sắc (làm bè xung sóng) cân bằng hoàn hảo với phi tuyến (làm dốc xung sóng) trong phương trình KdV, ta thu được **sóng cô lập (Soliton)** đi hàng nghìn km không biến dạng—nền tảng của truyền dẫn cáp quang tốc độ cao!

## Mục tiêu

Bài học này mở rộng mô hình sóng lý tưởng sang hai cơ chế phổ biến trong thực tế: tán sắc và hấp thụ (tiêu tán). Sau bài học, sinh viên cần hiểu bản chất của hiện tượng tán sắc, phân biệt vận tốc pha và vận tốc nhóm, giải thích được vì sao gói sóng biến dạng khi các tần số truyền với tốc độ khác nhau, đồng thời hiểu cách số hạng tắt dần làm suy giảm năng lượng sóng theo thời gian.

## Kiến thức nền

Sinh viên cần nắm khái niệm sóng phẳng, phương trình sóng cơ bản và biểu diễn số phức đủ để làm việc với nghiệm dạng $$ e^{i(kx-\omega t)} $$. Bài học này tạo bước chuyển từ mô hình sóng lý tưởng sang sóng trong môi trường thực.

## Dẫn nhập

Trong phương trình sóng lý tưởng, mọi thành phần tần số truyền đi với cùng một vận tốc nên gói sóng giữ nguyên hình dạng. Tuy nhiên, trong thực tế — như sóng trên nước sâu, sóng trong plasma, sợi quang hay vật liệu đàn hồi — các tần số khác nhau thường truyền với tốc độ khác nhau, khiến gói sóng trải rộng và biến dạng theo thời gian. Hiện tượng này gọi là tán sắc.

Bên cạnh đó, môi trường thực luôn tồn tại tổn hao do ma sát, độ nhớt hoặc hấp thụ điện từ, làm biên độ và năng lượng sóng giảm dần. Kết hợp cả tán sắc và tiêu tán giúp mô tả sát thực tế hơn nhiều hệ sóng vật lý.

### Khung giải thích (nên đọc chậm): Tính tay Vận tốc Pha $v_p$ và Vận tốc Nhóm $v_g$ cho phương trình Klein–Gordon $u_{tt} = c^2 u_{xx} - m^2 u$

1. **Thế sóng phẳng $e^{i(kx - \omega t)}$** ($\partial_t \to -i\omega$, $\partial_x \to ik$):
   $$(-i\omega)^2 = c^2(ik)^2 - m^2 \implies \omega^2 = c^2 k^2 + m^2 \implies \omega(k) = \sqrt{c^2 k^2 + m^2}.$$
   Vì $\omega(k)$ thực nên **không có hấp thụ**, nhưng không tuyến tính theo $k$ nên **có tán sắc**!
2. **Tính $v_p$ và $v_g$ với con số cụ thể $c = 1,\; m = 3,\; k = 4$**:
   - Tần số: $\omega = \sqrt{4^2 + 3^2} = \mathbf{5}$.
   - **Vận tốc pha**: $v_p = \frac{\omega}{k} = \frac{5}{4} = \mathbf{1{,}25 > c}$ (đỉnh sóng chạy *nhanh hơn* tốc độ ánh sáng $c = 1$!).
   - **Vận tốc nhóm** (tốc độ truyền năng lượng & thông tin):
     $$v_g = \frac{d\omega}{dk} = \frac{c^2 k}{\sqrt{c^2 k^2 + m^2}} = \frac{4}{5} = \mathbf{0{,}80 < c}!$$
3. **Kiểm tra hệ thức đẹp mắt**: $v_p \cdot v_g = 1{,}25 \times 0{,}80 = \mathbf{1} = c^2$! Tín hiệu và năng lượng luôn truyền với vận tốc $v_g < c$, bảo toàn tuyệt đối nguyên lý nhân quả của Thuyết Tương đối!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một gói sóng là sự chồng chất của nhiều thành phần tần số. Nếu mỗi tần số di chuyển với tốc độ khác nhau, theo thời gian chúng sẽ tách pha nhau, làm gói sóng kéo dài và biến dạng — đó là tán sắc. Nếu môi trường đồng thời rút bớt năng lượng của sóng, biên độ của cả gói sẽ giảm dần — đó là hấp thụ hay tiêu tán.

### Cách nhìn hình ảnh

Với sóng không tán sắc, gói xung di chuyển gần như giữ nguyên hình dạng ban đầu. Với sóng có tán sắc, đường bao của gói sóng trải rộng dần theo thời gian. Nếu có thêm tiêu tán, biên độ đường bao cũng hạ thấp dần. Hình ảnh này phân biệt rõ hai cơ chế biến đổi của sóng thực tế.

### Cách nhìn hình thức

Xét sóng phẳng có dạng $$ u(x,t)=e^{i(kx-\omega t)} $$. Hệ thức liên hệ $$ \omega=\omega(k) $$ gọi là quan hệ tán sắc:

- Nếu $$ \omega=ck $$, môi trường không tán sắc.
- Nếu $$ \omega $$ phụ thuộc phi tuyến vào $$ k $$, môi trường có tán sắc.

Vận tốc pha được định nghĩa là

$$ v_p=\frac{\omega}{k}. $$

Vận tốc nhóm được định nghĩa là

$$ v_g=\frac{d\omega}{dk}. $$

Để mô tả thêm sự tiêu tán (tắt dần), một mô hình đơn giản là phương trình sóng có cản:

$$ u_{tt}+\gamma u_t=c^2u_{xx},
\qquad \gamma>0. $$

## Những ngộ nhận thường gặp

- "Tán sắc đồng nghĩa với việc sóng bị mất năng lượng." Không đúng; tán sắc là hiện tượng các tần số truyền với tốc độ khác nhau và có thể xảy ra trong hệ bảo toàn năng lượng.
- "Vận tốc pha và vận tốc nhóm luôn bằng nhau." Chỉ đúng trong môi trường không tán sắc.
- "Hấp thụ và tán sắc là cùng một hiện tượng." Sai; tán sắc làm lệch pha giữa các thành phần tần số, còn hấp thụ làm tiêu hao năng lượng của hệ.
- "Hễ gói sóng bị biến dạng thì chắc chắn là do hấp thụ." Không hẳn; chỉ riêng tán sắc cũng đủ làm gói sóng trải rộng và biến dạng.

## Tiến trình học tập đề xuất

### Bước 1: Thiết lập quan hệ tán sắc

Thay nghiệm sóng phẳng $$ e^{i(kx-\omega t)} $$ vào PDE để tìm $$ \omega(k) $$.

### Bước 2: Phân biệt vận tốc pha và vận tốc nhóm

Nắm rõ ý nghĩa của $$ v_p=\omega/k $$ và $$ v_g=d\omega/dk $$.

### Bước 3: Khảo sát một ví dụ tán sắc điển hình

Sử dụng phương trình Klein-Gordon làm ví dụ mẫu dễ tính toán.

### Bước 4: Bổ sung số hạng tắt dần

So sánh cơ chế lệch pha (tán sắc) với cơ chế mất năng lượng (tiêu tán).

### Các điểm kiểm tra

- Sinh viên có diễn đạt được khái niệm tán sắc bằng lời hay không.
- Sinh viên có phân biệt rõ vận tốc pha và vận tốc nhóm hay không.
- Sinh viên có giải thích được vì sao số hạng $$ \gamma u_t $$ làm sóng suy giảm năng lượng theo thời gian hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Sóng không tán sắc

Với phương trình sóng chuẩn $$ u_{tt}=c^2u_{xx} $$, ta có $$ \omega=ck $$, suy ra $$ v_p=v_g=c $$. Mọi tần số truyền cùng tốc độ nên gói sóng lý tưởng giữ nguyên hình dạng.

### Ví dụ 2: Phương trình Klein-Gordon

Xét phương trình $$ u_{tt}-c^2u_{xx}+m^2u=0 $$. Thay nghiệm sóng phẳng cho quan hệ tán sắc $$ \omega^2=c^2k^2+m^2 $$. Vì quan hệ này phi tuyến theo $$ k $$ nên $$ v_p\ne v_g $$. Chỉ cần thêm một số hạng tuyến tính bậc không là tính chất lan truyền đã thay đổi đáng kể.

### Ví dụ 3: Phương trình sóng có tắt dần

Với $$ u_{tt}+\gamma u_t=c^2u_{xx} $$ ($$ \gamma>0 $$), số hạng $$ \gamma u_t $$ làm đạo hàm năng lượng âm ($$ E'(t)=-\gamma\int u_t^2\,dx\le 0 $$), khiến dao động suy giảm dần theo thời gian.

### Ví dụ 4: Sự trải rộng của gói sóng

Một gói sóng được tạo thành từ các tần số lân cận quanh số sóng trung tâm $$ k_0 $$. Khi quan hệ tán sắc phi tuyến, các thành phần này truyền với vận tốc pha khác nhau nên dần tách nhau ra, làm gói sóng trải rộng trong khi đường bao dịch chuyển theo vận tốc nhóm $$ v_g $$.

## Câu hỏi khái niệm

1. Vì sao tán sắc làm biến dạng gói sóng ngay cả khi tổng năng lượng được bảo toàn?
2. Vận tốc pha và vận tốc nhóm đặc trưng cho hai khía cạnh nào của quá trình truyền sóng?
3. Vì sao việc thêm số hạng $$ \gamma u_t $$ với $$ \gamma>0 $$ lại gây ra tiêu tán năng lượng?

## Bài toán ứng dụng

1. Trong truyền thông cáp quang, vì sao xung ánh sáng có xu hướng bị trải rộng sau khi truyền qua quãng đường dài?
2. Trên mặt nước sâu, vì sao các gợn sóng có bước sóng khác nhau lại di chuyển với tốc độ khác nhau?
3. Trong âm học hoặc vật liệu có độ nhớt, vì sao biên độ sóng giảm dần ngay cả khi không có biên phản xạ?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Một gói sóng có thể truyền đi mãi mà giữ nguyên hình dạng ban đầu hay không?"
- So sánh trực quan một gói sóng không tán sắc với một gói sóng có tán sắc.
- Đặt câu hỏi: "Khác biệt cơ bản giữa sóng bị suy yếu biên độ và sóng bị trải rộng biến dạng là gì?"
- Gợi ý sinh viên liên hệ vận tốc pha với chuyển động của "sóng mang" và vận tốc nhóm với chuyển động của "đường bao gói sóng".

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào một ví dụ sóng phẳng (phương trình sóng chuẩn so với Klein-Gordon) và một hình ảnh gói sóng cụ thể. Khi trực giác đã rõ, các công thức $$ v_p,\ v_g $$ sẽ dễ ghi nhớ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên thực hiện khai triển Taylor của $$ \omega(k) $$ quanh số sóng trung tâm $$ k_0 $$ để rút ra ý nghĩa của vận tốc nhóm, hoặc thảo luận phương trình sóng tán sắc bậc cao như KdV và phương trình Schrödinger tuyến tính.

## Tóm tắt dễ nhớ

Tán sắc xảy ra khi các tần số khác nhau truyền với tốc độ khác nhau ($$ \omega(k) $$ phi tuyến), làm gói sóng biến dạng và tách biệt vận tốc pha với vận tốc nhóm. Hấp thụ (tiêu tán) làm biên độ và năng lượng sóng giảm dần theo thời gian. Hai cơ chế này khác nhau về bản chất nhưng thường cùng xuất hiện trong các hệ sóng thực tế.

## Video tham khảo

- Xem trước: [Phase Velocity versus Group Velocity:  Wave Dispersion](https://www.youtube.com/watch?v=EIqKG5TiSYs) — Physics Videos by Eugene Khutoryansky, tiếng Anh. Minh họa trực quan sự khác biệt giữa vận tốc pha và vận tốc nhóm trong hiện tượng tán sắc.
- [13. Dispersive Medium, Phase Velocity, Group Velocity](https://www.youtube.com/watch?v=QxemLb8-5AA) — MIT OpenCourseWare, tiếng Anh. Bài giảng về môi trường tán sắc, vận tốc pha và vận tốc nhóm.
- [8.03 - Lect 12 - Dispersion, Phase Velocity, Group Velocity](https://www.youtube.com/watch?v=YEDUCl9t1m0) — Lectures by Walter Lewin. They will make you ♥ Physics., tiếng Anh. Walter Lewin trình bày và minh họa thí nghiệm về tán sắc, vận tốc pha và vận tốc nhóm.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tán sắc trong sóng nước và quang học
- Bài toán: Các thành phần tần số khác nhau truyền với vận tốc pha khác nhau khiến gói sóng trải rộng dần.
- Mô hình: Quan hệ tán sắc $$ \omega=\omega(k) $$ phi tuyến theo số sóng $$ k $$.
- Giả thiết và giới hạn: Môi trường tuyến tính nhưng có cơ chế tán sắc.
- Diễn giải: Không phải mọi phương trình dạng sóng đều truyền nguyên hình như trường hợp lý tưởng.

#### Tiêu tán trong môi trường có ma sát
- Bài toán: Dây rung trong không khí hoặc sóng trong vật liệu nhớt mất dần biên độ theo thời gian.
- Mô hình:
$$ u_{tt}+\gamma u_t=c^2u_{xx}. $$
- Giả thiết và giới hạn: Lực cản tuyến tính với hệ số $$ \gamma $$ không đổi.
- Diễn giải: Số hạng cản rút dần năng lượng và làm tắt dao động.

### 2. Trực giác bổ sung và các kết nối

Tán sắc làm biến dạng sóng do các thành phần Fourier di chuyển không đồng tốc, còn tiêu tán làm giảm biên độ do năng lượng bị mất đi. Tuy thường đi kèm trong thực tế, hai hiện tượng này có cơ chế toán học hoàn toàn tách biệt.

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

Một mode dao động trên dây có tắt dần yếu có thể viết gần đúng dưới dạng
$$ u(x,t)=e^{-\gamma t/2}\sin(kx)\cos(\omega_d t), $$
trong đó $$ \omega_d $$ là tần số đã hiệu chỉnh do lực cản. Thừa số suy giảm mũ $$ e^{-\gamma t/2} $$ cho thấy năng lượng không còn bảo toàn mà giảm dần theo thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt rõ tán sắc và tiêu tán qua sự biến đổi của dạng sóng và biên độ.

**Bậc sau đại học.** Tìm hiểu sâu về vận tốc nhóm, nửa nhóm tắt dần, phương trình KdV và phương trình Schrödinger tuyến tính.
