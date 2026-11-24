---
layout: post
title: "Ứng Dụng: Âm Thanh và Điện Từ"
chapter: '10'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: optional
---

![21 03 11 10 08 Applications Acoustics Em]({{ site.imgurl }}/chapter_img/chapter10/08_applications_acoustics_em.svg)

Một tiếng vỗ tay vang qua sân trường ở tốc độ $343\text{ m/s}$ và một tín hiệu Wi-Fi băng qua căn phòng ở gần $300.000\text{ km/s}$ tưởng chừng thuộc về hai thế giới vật lý hoàn toàn khác nhau—một bên là va chạm cơ học của phân tử không khí, bên kia là trường điện từ dao động ngay cả trong chân không tuyệt đối. Vậy mà khi đặt phương trình Euler tuyến tính hóa của âm học cạnh hệ phương trình Maxwell của điện từ học, cả hai đều rút gọn về **cùng một phương trình sóng duy nhất** $\partial_{tt} u = c^2 \Delta u$!

## Bản đồ kiến thức nền: Bốn trụ cột nối Âm học và Điện từ học qua Phương trình Sóng

1. **Âm học tuyến tính (Phương trình sóng vô hướng cho áp suất)**:
   Tuyến tính hóa bảo toàn khối lượng và bảo toàn động lượng quanh trạng thái nghỉ $(\rho_0, p_0)$ cho ra phương trình sóng cho nhiễu động áp suất $p'$ với tốc độ âm thanh $c_s = \sqrt{\gamma p_0 / \rho_0}$—sóng dọc dao động song song với phương truyền.
2. **Hệ Maxwell và Sóng điện từ (Phương trình sóng vector)**:
   Lấy toán tử $\nabla \times$ trên định luật Faraday và Ampère–Maxwell trong môi trường đồng nhất không nguồn tạo ra $\mathbf{E}_{tt} = c^2 \Delta \mathbf{E}$ và $\mathbf{B}_{tt} = c^2 \Delta \mathbf{B}$ với $c = 1/\sqrt{\mu \varepsilon}$—sóng ngang mà $\mathbf{E} \perp \mathbf{B} \perp \mathbf{k}$.
3. **Trở kháng đặc trưng và Năng lượng truyền tải**:
   Âm học dùng trở kháng âm $Z = \rho_0 c_s$ và cường độ $I = p' v$; điện từ học dùng trở kháng sóng $\eta = \sqrt{\mu/\varepsilon}$ và vector Poynting $\mathbf{S} = \frac{1}{\mu}\mathbf{E} \times \mathbf{B}$. Chính sự chênh lệch trở kháng tại mặt phân cách quyết định phần sóng phản xạ hay truyền qua.
4. **Ống dẫn sóng, Hốc cộng hưởng và Điều kiện biên**:
   Ống sáo (biên mở $p' = 0$ hay kín $\partial_n p' = 0$) và ống dẫn sóng vi ba (biên dẫn điện hoàn hảo $\mathbf{E}_\parallel = \mathbf{0}$) đều tạo ra phổ tần số rời rạc và tần số cắt—cùng một bài toán giá trị riêng của toán tử Laplace!

## Mục tiêu

Bài học này khép lại chương bằng việc đặt phương trình sóng vào hai lĩnh vực ứng dụng lớn: âm học và điện từ học. Sau bài học, sinh viên cần nhận ra phương trình sóng là cấu trúc toán học chung cho sự lan truyền áp suất âm và trường điện từ, hiểu vai trò của mode riêng, cộng hưởng, điều kiện biên và hình học miền, đồng thời thấy được tính thống nhất của PDE xuyên qua nhiều hiện tượng vật lý khác nhau.

## Kiến thức nền

Sinh viên cần nắm phương trình sóng, khái niệm mode riêng, hiện tượng cộng hưởng và phản xạ sóng. Bài học này mang tính tổng kết giúp gắn kết lý thuyết chương với các bài toán kỹ thuật và vật lý thực tế.

## Dẫn nhập

Nếu chỉ nhìn phương trình sóng qua mô hình dây đàn rung, ta dễ đánh giá thấp phạm vi ứng dụng của nó. Trên thực tế, cùng một cấu trúc toán học xuất hiện khi âm thanh truyền trong không khí, khi ánh sáng lan truyền trong không gian, khi sóng điện từ chạy trong ống dẫn sóng và khi phòng hòa nhạc hình thành các tần số cộng hưởng đặc trưng.

Thông điệp xuyên suốt của bài học là tính thống nhất của toán học ứng dụng: dù đại lượng vật lý thay đổi, các khái niệm cốt lõi vẫn là sự lan truyền với tốc độ hữu hạn, hệ mode riêng, điều kiện biên và năng lượng.


### Khung giải thích (nên đọc chậm): So sánh trực tiếp bước sóng âm thanh và sóng điện từ bằng phép tính tay

Cùng dùng một hệ thức phổ quát $\lambda = c / f$, hãy tính hai sóng quen thuộc trong đời sống:
1. **Sóng âm trong không khí ở $20^\circ\text{C}$** ($c_s \approx 343\text{ m/s}$) với nốt nhạc chuẩn $f = 1.000\text{ Hz}$:
   $$\lambda_{\text{âm}} = \frac{343}{1.000} = \mathbf{0{,}343\text{ m}} \quad (34{,}3\text{ cm}).$$
2. **Sóng phát thanh FM trong không khí** ($c_0 \approx 3{,}0 \times 10^8\text{ m/s}$) ở tần số $f = 100\text{ MHz} = 10^8\text{ Hz}$:
   $$\lambda_{\text{FM}} = \frac{3{,}0 \times 10^8}{10^8} = \mathbf{3{,}0\text{ m}}.$$
3. **Ánh sáng đi vào lõi sợi quang thủy tinh** có chiết suất $n = 1{,}5$: tốc độ sóng giảm xuống $v = c_0 / n = 2{,}0 \times 10^8\text{ m/s}$, nên bước sóng co ngắn đi đúng $1{,}5$ lần trong khi tần số $f$ giữ nguyên tuyệt đối! Đó là lý do ăng-ten radio dài vài chục cm còn màng nhĩ chỉ cần vài mm.
## Khái niệm theo ba cách

### Cách nhìn trực quan

Âm thanh là sự lan truyền của những biến thiên nén–dãn nhỏ trong không khí; sóng điện từ là sự lan truyền của dao động điện trường và từ trường trong không gian. Tuy bản chất vật lý khác nhau, cả hai đều tuân theo quy luật sóng: có tốc độ lan truyền xác định, có hiện tượng phản xạ, cộng hưởng và hệ mode riêng.

### Cách nhìn hình ảnh

Trong âm học phòng, các mode riêng biểu hiện thành những vùng áp suất tăng giảm xen kẽ với các mặt nút và bụng sóng. Trong ống dẫn sóng điện từ, các mode ngang điện (TE) và ngang từ (TM) tạo nên những cấu trúc trường đặc trưng trên mặt cắt ngang. Trong cả hai lĩnh vực, hình học miền trực tiếp định hình cấu trúc mode.

### Cách nhìn hình thức

Trong âm học tuyến tính, độ lệch áp suất nhỏ $$ p(x,t) $$ thỏa mãn gần đúng phương trình sóng $$ p_{tt}=c^2\Delta p $$. Trong điện từ học, từ hệ phương trình Maxwell trong chân không không nguồn, các thành phần của điện trường $$ \mathbf E $$ và từ trường $$ \mathbf B $$ đều thỏa mãn phương trình sóng:

$$
\Delta \mathbf E=\frac{1}{c^2}\mathbf E_{tt},
\qquad
\Delta \mathbf B=\frac{1}{c^2}\mathbf B_{tt},
$$

trong đó $$ c $$ là tốc độ ánh sáng trong chân không.

## Những ngộ nhận thường gặp

- "Âm thanh và điện từ là hai lĩnh vực hoàn toàn tách biệt nên toán học cũng khác hẳn nhau." Sai; cả hai đều được mô tả bởi cùng một cấu trúc phương trình sóng.
- "Cộng hưởng chỉ là hiện tượng trong âm học." Không đúng; cộng hưởng mode riêng xuất hiện rộng rãi trong điện từ, cơ học kết cấu và nhiều hệ vật lý khác.
- "Mode riêng chỉ là khái niệm trừu tượng trên giấy." Sai; chúng quyết định trực tiếp âm sắc, chất lượng truyền dẫn, tần số cắt và đáp ứng thực tế của thiết bị.
- "Điều kiện biên chỉ ảnh hưởng đến biên độ sóng." Không đúng; điều kiện biên quyết định trực tiếp tập mode và tần số riêng nào được phép tồn tại.

## Tiến trình học tập đề xuất

### Bước 1: Nhận diện phương trình sóng trong từng lĩnh vực

Đặt song song ba mô hình: dây rung cơ học, sóng âm và sóng điện từ.

### Bước 2: Tập trung vào mode riêng và cộng hưởng

Đây là hai khái niệm thống nhất mạnh nhất giữa các lĩnh vực.

### Bước 3: Liên hệ hình học miền với thiết kế kỹ thuật

Nhìn nhận phòng hòa nhạc, ống dẫn sóng và hốc cộng hưởng như các miền biên PDE.

### Các điểm kiểm tra

- Sinh viên có chỉ ra được điểm chung toán học giữa âm học tuyến tính và điện từ học hay không.
- Sinh viên có giải thích được vì sao hình học căn phòng hoặc tiết diện ống dẫn ảnh hưởng trực tiếp đến hệ mode hay không.
- Sinh viên có hiểu cộng hưởng là hệ quả của việc kích thích gần một tần số riêng hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Âm học phòng

Áp suất âm thỏa mãn phương trình sóng trên miền không gian của căn phòng. Hình dạng phòng và tính chất phản xạ/hấp thụ của tường quy định các mode riêng. Khi nguồn âm phát ở tần số gần một mode riêng, biên độ áp suất tại mode đó tăng mạnh — đây là lý do thiết kế âm học phòng cần kiểm soát cộng hưởng.

### Ví dụ 2: Dây đàn và nhạc cụ

Các họa âm của dây đàn chính là các mode riêng của phương trình sóng một chiều trên đoạn hữu hạn, tạo cầu nối trực quan từ bài toán dây rung sang âm học thực tế.

### Ví dụ 3: Ống dẫn sóng điện từ

Trong ống dẫn sóng (waveguide), điều kiện biên trên thành kim loại dẫn điện hình thành các mode TE và TM. Mỗi mode có một tần số cắt riêng: nếu tần số sóng thấp hơn tần số cắt, mode không thể lan truyền mà suy giảm nhanh. Đây là ví dụ rõ nét về vai trò của điều kiện biên trong truyền dẫn.

### Ví dụ 4: Hệ phương trình Maxwell và sóng điện từ

Từ các phương trình Maxwell trong chân không, ta suy ra trực tiếp điện trường và từ trường đều thỏa mãn phương trình sóng với tốc độ $$ c $$, đưa phương trình sóng vượt ra ngoài cơ học cổ điển để bước vào vật lý trường.

## Câu hỏi khái niệm

1. Vì sao hiện tượng cộng hưởng xảy ra khi hệ bị kích thích ở tần số gần tần số riêng?
2. Điểm chung toán học giữa dao động dây đàn, sóng âm và sóng điện từ là gì?
3. Vì sao hình học miền và điều kiện biên quan trọng không kém bản thân phương trình sóng?

## Bài toán ứng dụng

1. Vì sao một căn phòng có tỉ lệ hình học không hợp lý dễ khiến một số tần số âm bị cộng hưởng quá mức?
2. Trong ống dẫn sóng điện từ, vì sao tồn tại tần số cắt mà dưới ngưỡng đó sóng không truyền đi được?
3. Trong thiết kế thiết bị quang học hoặc vô tuyến, vì sao kiểm soát các mode truyền sóng là bài toán trọng tâm?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Dây đàn, phòng hòa nhạc và ống dẫn sóng điện từ có điểm chung toán học nào?"
- Cho sinh viên lập bảng đối chiếu giữa các lĩnh vực: đại lượng trường, PDE, tốc độ truyền sóng, hệ mode và điều kiện biên.
- Đặt câu hỏi: "Nếu thay đổi kích thước hoặc hình dạng phòng/ống dẫn, đại lượng nào trong lời giải thay đổi đầu tiên?"
- Khuyến khích sinh viên nêu thêm các ví dụ truyền sóng từ những ngành kỹ thuật khác mà các em quan tâm.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên quy mọi ví dụ ứng dụng về cùng một khung bốn yếu tố: phương trình sóng, mode riêng, cộng hưởng và điều kiện biên để bài học mạch lạc và dễ ghi nhớ.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự thực hiện bước khử biến từ hệ phương trình Maxwell hoặc từ hệ phương trình Euler tuyến tính hóa trong âm học để suy ra phương trình sóng, hoặc phân tích chi tiết tần số cắt của ống dẫn sóng hình chữ nhật.

## Tóm tắt dễ nhớ

Âm thanh và sóng điện từ đều tuân theo cùng một khuôn khổ toán học gồm phương trình sóng, hệ mode riêng và điều kiện biên. Hình học miền quyết định phổ cộng hưởng, còn hệ mode quyết định cách năng lượng lan truyền trong thực tế.

## Video tham khảo

- Xem trước: [Divergence and curl:  The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) — 3Blue1Brown, tiếng Anh. Giải thích trực quan toán tử phân kỳ (divergence) và xoáy (curl) — ngôn ngữ của hệ phương trình Maxwell.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Ôn lại phương trình sóng nền tảng mà cả mô hình âm học lẫn điện từ đều dẫn tới.
- [8.03 - Lect 12 - Dispersion, Phase Velocity, Group Velocity](https://www.youtube.com/watch?v=YEDUCl9t1m0) — Lectures by Walter Lewin. They will make you ♥ Physics., tiếng Anh. Thảo luận hiện tượng tán sắc như hiệu chỉnh thực tế đối với sóng âm và sóng điện từ lý tưởng.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Âm học tuyến tính
- Bài toán: Áp suất âm trong không khí lan truyền dưới dạng sóng.
- Mô hình:
$$ p_{tt}=c^2\Delta p. $$
- Giả thiết và giới hạn: Biên độ nhỏ, môi trường đồng nhất, bỏ qua hấp thụ mạnh.
- Diễn giải: Phương trình sóng giải thích các hiện tượng phản xạ âm, cộng hưởng và mode không gian của phòng.

#### Sóng điện từ
- Bài toán: Trong môi trường đồng nhất không nguồn, các thành phần của điện trường và từ trường thỏa mãn phương trình sóng.
- Mô hình: Ở dạng đơn giản theo từng thành phần,
$$ E_{tt}=c^2\Delta E. $$
- Giả thiết và giới hạn: Môi trường tuyến tính, đẳng hướng, không nguồn điện tích và dòng điện tự do.
- Diễn giải: Âm học và điện từ học chia sẻ cùng một cấu trúc toán học cơ bản.

### 2. Trực giác bổ sung và các kết nối

Một ưu thế nổi bật của lý thuyết PDE là khả năng dùng chung một cấu trúc toán học cho nhiều ngành vật lý khác nhau. Khi nhận diện được phương trình sóng trong cả âm học lẫn điện từ học, người học thấy rõ giá trị phổ quát của các phương pháp giải đã học.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 600)
t = 0.8
p = np.cos(x - t)
E = np.cos(x - t + np.pi / 3)

plt.plot(x, p, label="Song am p(x,t)")
plt.plot(x, E, label="Song dien tu E(x,t)")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.title("Hai vi du cua song phang")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: acoustic standing wave room simulation
- search: electromagnetic wave animation maxwell
- search: plane wave solution wave equation physics

### 5. Bài toán mẫu có bối cảnh thực

Một sóng phẳng một chiều có dạng
$$ u(x,t)=A\cos(kx-\omega t), $$
với hệ thức tán sắc tuyến tính
$$ \omega=ck. $$
Từ đó suy ra vận tốc pha bằng $$ c $$ và bước sóng $$ \lambda=2\pi/k $$. Cùng biểu thức này xuất hiện trong cả âm học lẫn điện từ học tuyến tính.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện phương trình sóng và ý nghĩa các tham số trong các bối cảnh vật lý khác nhau.

**Bậc sau đại học.** Nghiên cứu hệ phương trình Maxwell đầy đủ, tenxơ ứng suất âm học và bài toán truyền sóng trong môi trường không đồng nhất.
