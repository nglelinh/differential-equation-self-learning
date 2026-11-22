---
layout: post
title: "Phản Xạ và Truyền Qua"
chapter: '10'
order: 6
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 06 Reflection Transmission]({{ site.imgurl }}/chapter_img/chapter10/06_reflection_transmission.svg)

## Mục tiêu

Bài học này giới thiệu hai hiện tượng cơ bản khi sóng gặp biên hoặc mặt phân cách: phản xạ và truyền qua. Sau bài học, sinh viên cần hiểu vì sao sóng không dừng lại tại biên, phân biệt được phản xạ tại biên cố định và biên tự do, nắm vai trò của trở kháng sóng khi ghép hai môi trường và thấy được định luật bảo toàn năng lượng chi phối sự phân chia giữa sóng phản xạ và sóng truyền qua.

## Kiến thức nền

Sinh viên cần nắm sóng chạy một chiều, các điều kiện biên cơ bản và khái niệm năng lượng sóng. Bài học này đưa mô hình sóng vào tình huống tương tác trực tiếp với vật cản và ranh giới môi trường.

## Dẫn nhập

Trong thực tế, sóng hiếm khi truyền mãi trong một môi trường đồng nhất vô hạn. Sóng âm gặp tường, xung cơ học gặp mối nối giữa hai đoạn dây có mật độ khác nhau, ánh sáng gặp mặt phân cách giữa hai môi trường quang học. Tại ranh giới, một phần năng lượng dội ngược trở lại và phần còn lại truyền tiếp sang môi trường kế tiếp. Hiện tượng này tạo ra tiếng vang, sự giao thoa, phản hồi tín hiệu và nhiều ứng dụng kỹ thuật.

Thay vì chỉ ghi nhớ công thức hệ số phản xạ, cần nắm rõ ý nghĩa vật lý: mặt phân cách là nơi điều kiện liên tục quyết định tỷ lệ năng lượng được giữ lại và năng lượng truyền sang môi trường mới.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi một xung sóng trên dây truyền đến đầu bị kẹp cố định, đầu dây không thể dịch chuyển nên xung phản xạ ngược lại và đổi dấu. Nếu đầu dây tự do, xung phản xạ trở lại nhưng giữ nguyên dấu. Khi sóng đi từ đoạn dây nhẹ sang đoạn dây nặng hơn, một phần năng lượng truyền tiếp sang đoạn mới và phần còn lại phản xạ về phía cũ.

### Cách nhìn hình ảnh

Hãy hình dung sóng tới là một đỉnh truyền sang phải. Tại biên cố định, đỉnh sóng phản xạ thành một hõm; tại biên tự do, đỉnh sóng phản xạ vẫn là một đỉnh. Tại mặt phân cách giữa hai môi trường khác nhau, ta quan sát đồng thời một sóng phản xạ quay ngược lại và một sóng truyền qua đi vào môi trường thứ hai với biên độ đã thay đổi.

### Cách nhìn hình thức

Xét mặt phân cách giữa hai môi trường một chiều, viết sóng tới, sóng phản xạ và sóng truyền qua dưới dạng sóng phẳng điều hòa:

$$
u_i=Ae^{i(k_1x-\omega t)},
\qquad
u_r=Be^{i(-k_1x-\omega t)},
\qquad
u_t=Ce^{i(k_2x-\omega t)}.
$$

Tại mặt phân cách, ta áp đặt điều kiện liên tục của đại lượng trường và thông lượng tương ứng. Đặt trở kháng sóng của mỗi môi trường là $$ Z_j=\rho_j c_j $$. Trong quy ước theo áp suất âm (tại đó $$ 1+R=T $$), hệ số phản xạ biên độ là

$$ R=\frac{Z_2-Z_1}{Z_2+Z_1}, $$

và hệ số truyền qua là

$$ T=\frac{2Z_2}{Z_1+Z_2}. $$

(Lưu ý: nếu viết cho độ lệch ngang trên sợi dây có cùng lực căng, dấu của $$ R $$ đảo lại thành $$ (Z_1-Z_2)/(Z_1+Z_2) $$ và $$ T=2Z_1/(Z_1+Z_2) $$, nhưng tỉ lệ năng lượng phản xạ $$ R^2 $$ là như nhau.)

## Những ngộ nhận thường gặp

- "Khi gặp ranh giới, sóng chỉ phản xạ hoàn toàn hoặc truyền qua hoàn toàn." Sai; nói chung sóng vừa phản xạ vừa truyền qua.
- "Sóng phản xạ lúc nào cũng bị đổi dấu (đảo pha)." Không đúng; dấu của sóng phản xạ phụ thuộc vào loại biên hoặc tương quan trở kháng hai môi trường.
- "Hai môi trường khác nhau rất ít vẫn gây phản xạ mạnh." Không chính xác; cường độ phản xạ phụ thuộc vào mức chênh lệch trở kháng.
- "Các công thức $$ R,\ T $$ chỉ là biến đổi đại số." Sai; chúng phản ánh trực tiếp cách năng lượng sóng phân bổ giữa hai phía mặt phân cách.

## Tiến trình học tập đề xuất

### Bước 1: Xét phản xạ tại biên đơn giản

Bắt đầu từ hai trường hợp trực quan nhất là biên cố định và biên tự do.

### Bước 2: Mở rộng sang mặt phân cách hai môi trường

Quan sát sự xuất hiện đồng thời của sóng phản xạ và sóng truyền qua.

### Bước 3: Đưa vào đại lượng trở kháng sóng

Dùng $$ Z=\rho c $$ để cô đọng tính chất môi trường thành một tham số duy nhất.

### Bước 4: Kiểm chứng bằng bảo toàn năng lượng

Xác nhận tổng thông lượng năng lượng phản xạ và truyền qua bằng thông lượng sóng tới.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao biên cố định gây phản xạ đổi dấu hay không.
- Sinh viên có nắm rõ ý nghĩa vật lý của trở kháng sóng hay không.
- Sinh viên có thấy mối liên hệ giữa định luật bảo toàn năng lượng với $$ R $$ và $$ T $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Biên cố định

Với điều kiện $$ u(0,t)=0 $$, sóng phản xạ phải triệt tiêu độ lệch của sóng tới ngay tại biên, dẫn đến phản xạ đảo dấu: một đỉnh sóng tới tạo ra một hõm sóng phản xạ.

### Ví dụ 2: Biên tự do

Với điều kiện $$ u_x(0,t)=0 $$, sóng phản xạ không bị đảo dấu: một đỉnh sóng tới tạo ra một đỉnh sóng phản xạ. Chỉ cần đổi điều kiện biên là pha của sóng phản xạ đã thay đổi.

### Ví dụ 3: Hai môi trường khớp trở kháng

Khi $$ Z_1=Z_2 $$, ta có $$ R=0 $$, tức không xảy ra phản xạ và toàn bộ năng lượng truyền qua. Đây là nguyên lý nền tảng của kỹ thuật phối hợp trở kháng (impedance matching) trong truyền sóng và điện tử.

### Ví dụ 4: Chênh lệch trở kháng rất lớn

Khi $$ Z_2\gg Z_1 $$, ta có $$ R\approx 1 $$ (hoặc $$ R\approx -1 $$ theo quy ước chuyển vị), tức gần như toàn bộ năng lượng bị phản xạ. Mặt phân cách với môi trường quá cứng hoạt động gần tương đương một biên phản xạ hoàn toàn.

## Câu hỏi khái niệm

1. Vì sao biên cố định và biên tự do tạo ra hai kiểu phản xạ khác nhau về pha?
2. Trở kháng sóng phản ánh đặc tính gì của môi trường truyền sóng?
3. Vì sao định luật bảo toàn năng lượng là phép kiểm tra tự nhiên cho các công thức hệ số phản xạ và truyền qua?

## Bài toán ứng dụng

1. Vì sao âm thanh trong một căn phòng có tường cứng và nhẵn lại dội vang mạnh?
2. Trong đường dây truyền tín hiệu cao tần, vì sao phối hợp trở kháng giúp hạn chế phản xạ tín hiệu?
3. Trong quang học, vì sao ánh sáng bị phản xạ một phần khi đi qua mặt phân cách giữa hai môi trường có chiết suất khác nhau?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Một đỉnh sóng chạy tới đầu dây cố định sẽ phản xạ lại thành đỉnh hay thành hõm?"
- Yêu cầu sinh viên vẽ phác thảo xung phản xạ cho cả hai trường hợp biên cố định và biên tự do.
- Đặt câu hỏi: "Nếu hai môi trường có trở kháng bằng nhau, liệu có xuất hiện sóng phản xạ hay không?"
- So sánh hiện tượng phản xạ–truyền qua trong dây rung, âm học và quang học dưới cùng một ngôn ngữ trở kháng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu thật vững từ hai tình huống đơn giản là biên cố định và biên tự do. Khi đã hiểu cơ chế đổi pha tại biên, công thức ghép hai môi trường sẽ dễ tiếp thu hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự thiết lập công thức $$ R,\ T $$ từ các điều kiện liên tục tại $$ x=0 $$, kiểm tra hệ thức bảo toàn thông lượng năng lượng và mở rộng sang trường hợp biên độ phức.

## Tóm tắt dễ nhớ

Khi sóng gặp biên hoặc mặt phân cách, nó thường tách thành sóng phản xạ và sóng truyền qua. Pha phản xạ phụ thuộc vào loại biên, còn cường độ phản xạ phụ thuộc vào độ chênh lệch trở kháng giữa hai môi trường, luôn tuân theo định luật bảo toàn năng lượng.

## Video tham khảo

- Xem trước: [Strings: reflection and transmission of an incoming wave at a discontinuity.](https://www.youtube.com/watch?v=Zokrkuc2EgU) — Mooc Bogazici, tiếng Anh. Phân tích sự phản xạ và truyền qua của sóng tới tại điểm gián đoạn trên dây.
- [Reflection and Transmission of Transverse Waves](https://www.youtube.com/watch?v=L5-RuMtXDyo) — Physics Ninja, tiếng Anh. Giải thích chi tiết hiện tượng phản xạ và truyền qua đối với sóng ngang.
- [PDE 10 | Wave equation: d'Alembert's formula](https://www.youtube.com/watch?v=j2G91naZ8bo) — commutant, tiếng Anh. Ôn lại cấu trúc sóng truyền sang phải và sang trái trong nghiệm d'Alembert.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Sóng địa chấn qua các lớp địa chất
- Bài toán: Khi sóng địa chấn gặp ranh giới giữa hai tầng đất đá, một phần năng lượng phản xạ trở lại mặt đất và một phần truyền tiếp xuống sâu hơn.
- Mô hình: Ghép hai phương trình sóng có trở kháng khác nhau kèm điều kiện liên tục tại mặt phân cách.
- Giả thiết và giới hạn: Xấp xỉ một chiều, vật liệu đàn hồi tuyến tính, ranh giới phẳng.
- Diễn giải: Độ tương phản trở kháng giữa các tầng vật liệu quyết định cường độ tín hiệu phản xạ.

#### Dây ghép từ hai đoạn có mật độ khác nhau
- Bài toán: Một xung cơ học truyền qua mối nối giữa hai đoạn dây không đi qua nguyên vẹn mà tách thành xung phản xạ và xung truyền qua.
- Mô hình: Áp đặt điều kiện liên tục chuyển vị và lực căng tại mối nối.
- Giả thiết và giới hạn: Mối nối lý tưởng, cùng lực căng, bỏ qua tổn hao năng lượng tại điểm nối.
- Diễn giải: Đây là mô hình cơ học đơn giản nhất cho bài toán truyền sóng qua mặt phân cách.

### 2. Trực giác bổ sung và các kết nối

Phản xạ và truyền qua phát sinh do hai môi trường cản trở chuyển động sóng ở các mức độ khác nhau. Khái niệm trở kháng tạo cầu nối thống nhất giữa cơ học sóng, mạch điện, quang học và địa chấn học.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.2, 4.0, 400)   # Z2 / Z1
R = (r - 1) / (r + 1)
T = 2 * r / (r + 1)

plt.plot(r, R, label="He so phan xa")
plt.plot(r, T, label="He so truyen")
plt.axhline(0, color="black", linewidth=0.8)
plt.xlabel("Ti so tro khang Z2/Z1")
plt.title("Phan xa va truyen qua theo do lech tro khang")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: reflection transmission wave interface animation
- search: seismic reflection coefficient tutorial
- search: string with density jump wave pulse

### 5. Bài toán mẫu có bối cảnh thực

Với trở kháng sóng hai phía là $$ Z_1 $$ và $$ Z_2 $$, hệ số phản xạ áp suất có dạng
$$ R=\frac{Z_2-Z_1}{Z_2+Z_1}. $$
Khi $$ Z_2=Z_1 $$ thì $$ R=0 $$ (không có phản xạ); khi hai môi trường chênh lệch trở kháng lớn, sóng phản xạ trở nên mạnh. Đây là nguyên lý cơ sở của phương pháp khảo sát địa chấn phản xạ.

### 6. Phân tầng độ khó

**Bậc đại học.** Thiết lập điều kiện ghép tại ranh giới và diễn giải ý nghĩa vật lý của hệ số phản xạ và truyền qua.

**Bậc sau đại học.** Mở rộng sang lý thuyết tán xạ (scattering theory), bài toán truyền qua nhiều lớp và phương pháp ma trận truyền.
