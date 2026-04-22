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

Bài học này giới thiệu hai hiện tượng cốt lõi khi sóng gặp biên hoặc mặt phân cách: phản xạ và truyền qua. Sau bài học, sinh viên cần hiểu vì sao sóng không chỉ đơn giản dừng lại ở biên, biết phân biệt phản xạ ở biên cố định và biên tự do, hiểu vai trò của trở kháng môi trường trong bài toán ghép hai miền, và thấy cách bảo toàn năng lượng điều khiển sự chia tách giữa sóng phản xạ và sóng truyền.

## Kiến thức nền

Sinh viên nên nắm sóng chạy một chiều, điều kiện biên cơ bản, và trực giác năng lượng của sóng. Bài này là nơi mô hình sóng bắt đầu tương tác trực tiếp với môi trường và vật cản.

## Dẫn nhập

Trong thực tế, sóng hiếm khi truyền mãi trong một môi trường đồng nhất vô hạn. Sóng âm gặp tường, xung trên dây gặp chỗ nối giữa hai đoạn dây, ánh sáng gặp mặt phân cách giữa hai vật liệu. Khi đó, một phần năng lượng dội lại, phần còn lại đi tiếp. Chính hiện tượng này tạo ra vang âm, giao thoa, phản hồi tín hiệu và nhiều hiệu ứng công nghệ quan trọng.

Đây là bài rất giàu trực giác vật lý. Nếu dạy tốt, sinh viên sẽ không chỉ nhớ công thức hệ số phản xạ, mà còn cảm được rằng biên và mặt phân cách là nơi hệ "thương lượng" xem bao nhiêu năng lượng được giữ lại, bao nhiêu năng lượng được chuyển qua.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Khi một làn sóng trên dây đi đến chỗ dây bị kẹp chặt, đầu dây không thể chuyển vị, nên sóng buộc phải dội lại với đổi dấu. Nếu đầu dây tự do, sóng phản xạ nhưng không đổi dấu. Nếu sóng đi từ một đoạn dây nhẹ sang đoạn dây nặng hơn, một phần năng lượng đi vào đoạn mới, phần còn lại bật lại. Tất cả những điều đó là phản xạ và truyền qua.

### Cách nhìn hình ảnh

Sóng tới có thể được vẽ như một đỉnh đi sang phải. Ở biên cố định, đỉnh phản xạ thành một hõm. Ở biên tự do, đỉnh phản xạ vẫn là đỉnh. Ở mặt phân cách hai môi trường, ta nhìn thấy đồng thời một sóng phản xạ quay lại và một sóng truyền tiếp đi vào môi trường thứ hai với biên độ khác.

### Cách nhìn hình thức

Với mặt phân cách giữa hai môi trường một chiều, ta viết

$$
u_i=Ae^{i(k_1x-\omega t)},
\qquad
u_r=Be^{i(-k_1x-\omega t)},
\qquad
u_t=Ce^{i(k_2x-\omega t)}.
$$

Tại biên, ta yêu cầu liên tục chuyển vị và liên tục lực hay thông lượng phù hợp. Nếu đặt trở kháng sóng $$ Z_j=\rho_j c_j $$, thì hệ số phản xạ biên độ là

$$ R=\frac{Z_2-Z_1}{Z_2+Z_1}, $$

và hệ số truyền qua là

$$ T=\frac{2Z_2}{Z_1+Z_2}. $$

## Những ngộ nhận thường gặp

- "Gặp biên thì sóng chỉ bật lại hoặc chỉ đi tiếp." Sai. Nó thường vừa phản xạ vừa truyền qua.
- "Phản xạ luôn đổi dấu." Không đúng; còn tùy loại biên hoặc mặt phân cách.
- "Nếu hai môi trường khác nhau ít thì vẫn phản xạ mạnh." Không hẳn; mức phản xạ phụ thuộc vào độ khớp trở kháng.
- "Công thức

$$ R,\ T $$

chỉ là đại số." Sai. Chúng mã hóa cách năng lượng bị chia giữa hai phía.

## Tiến trình học tập đề xuất

### Bước 1: Xét phản xạ ở biên đơn giản

Biên cố định và biên tự do là hai mẫu cơ bản dễ nhìn.

### Bước 2: Chuyển sang hai môi trường

Đây là nơi sóng phản xạ và truyền qua cùng xuất hiện.

### Bước 3: Đưa trở kháng vào câu chuyện

Giúp sinh viên có một đại lượng vật lý cô đọng.

### Bước 4: Kiểm tra bảo toàn năng lượng

Đây là bước xác nhận kết quả vật lý hợp lý.

### Các checkpoint

- Sinh viên có giải thích được vì sao biên cố định gây phản xạ đổi dấu hay không.
- Sinh viên có hiểu ý nghĩa của trở kháng sóng hay không.
- Sinh viên có thấy rằng bảo toàn năng lượng ràng buộc

$$ R $$

và $$ T $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Biên cố định

Nếu $$ u(0,t)=0 $$, thì sóng phản xạ phải triệt tiêu chuyển vị tại biên. Điều đó dẫn đến phản xạ đổi dấu. Một đỉnh tới tạo ra một hõm phản xạ. Đây là ví dụ vật lý dễ nhớ nhất của bài.

### Ví dụ 2: Biên tự do

Nếu $$ u_x(0,t)=0 $$, thì phản xạ không đổi dấu. Đỉnh tới tạo ra đỉnh phản xạ. Ví dụ này rất hữu ích để sinh viên thấy chỉ thay một điều kiện biên là pha của sóng phản xạ đã đổi khác.

### Ví dụ 3: Hai môi trường khớp nhau

Nếu $$ Z_1=Z_2 $$, thì $$ R=0 $$. Không có phản xạ. Ví dụ này giải thích vì sao "matching impedance" là ý tưởng lớn trong truyền sóng và kỹ thuật điện tử.

### Ví dụ 4: Chênh lệch trở kháng lớn

Nếu $$ Z_2\gg Z_1 $$, thì $$ R\approx 1 $$, nên phản xạ rất mạnh. Ví dụ này giúp sinh viên thấy mặt phân cách rất cứng đóng vai trò gần giống một biên cố định.

## Câu hỏi khái niệm

1. Vì sao biên cố định và biên tự do cho hai kiểu phản xạ khác nhau về pha?
2. Trở kháng sóng đo điều gì về môi trường?
3. Vì sao bảo toàn năng lượng là kiểm tra tự nhiên cho công thức phản xạ và truyền qua?

## Bài toán ứng dụng

1. Vì sao âm thanh trong phòng có thể dội lại mạnh nếu tường phản xạ tốt?
2. Trong cáp truyền tín hiệu, vì sao ghép trở kháng giúp giảm phản xạ?
3. Trong quang học, vì sao mặt phân cách giữa hai môi trường làm ánh sáng bị phản xạ một phần?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Một đỉnh sóng đi tới bức tường sẽ bật lại thành đỉnh hay thành hõm?"
- Cho sinh viên vẽ tay phản xạ ở biên cố định và biên tự do.
- Hỏi cả lớp: "Nếu hai môi trường khớp hoàn hảo, ta có mong phản xạ còn tồn tại không?"
- Tổ chức hoạt động so sánh trực giác âm học, dây rung và quang học dưới cùng một ngôn ngữ phản xạ-truyền qua.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên đi từ hai hình ảnh cực đơn giản: biên cố định và biên tự do. Khi hai trường hợp này đã rõ, công thức ghép hai môi trường sẽ bớt trừu tượng hơn rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi suy ra công thức $$ R,\ T $$ từ các điều kiện ghép, hoặc phân tích năng lượng trong trường hợp biên độ phức.

## Tóm tắt dễ nhớ

Khi sóng gặp biên hoặc mặt phân cách, nó thường tách thành phần phản xạ và phần truyền qua. Pha phản xạ phụ thuộc loại biên, còn cường độ phản xạ phụ thuộc vào độ khớp trở kháng giữa các môi trường. Năng lượng tới được chia ra chứ không tự mất đi.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Sóng địa chấn qua lớp vật liệu
- Bài toán: Khi sóng gặp ranh giới giữa hai lớp đất đá, một phần bị phản xạ và một phần truyền qua.
- Mô hình: Ghép hai phương trình sóng với trở kháng khác nhau và điều kiện liên tục tại giao diện.
- Giả thiết và giới hạn: Gần đúng một chiều, vật liệu tuyến tính, mặt phân cách phẳng.
- Diễn giải: Tương phản vật liệu quyết định mức phản xạ.

#### Dây gồm hai đoạn có mật độ khác nhau
- Bài toán: Xung trên dây ghép hai vật liệu không truyền nguyên vẹn qua mối nối.
- Mô hình: Áp điều kiện liên tục cho chuyển vị và lực kéo.
- Giả thiết và giới hạn: Nối lý tưởng, lực căng như nhau, bỏ qua mất mát tại mối nối.
- Diễn giải: Đây là mô hình cơ học đơn giản cho bài toán giao diện.

### 2. Trực giác bổ sung và các kết nối

Phản xạ và truyền qua xuất hiện vì môi trường "kháng" chuyển động theo những mức khác nhau. Ý tưởng trở kháng ở đây rất gần với mạch điện, quang học và địa chấn. Một bẫy phổ biến là tưởng biên chỉ phản xạ hoàn toàn; thực tế thường là hỗn hợp phản xạ và truyền qua.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.2, 4.0, 400)   # Z2 / Z1
R = (r - 1) / (r + 1)
T = 2 / (r + 1)

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

Nếu trở kháng sóng ở hai phía là $$ Z_1 $$ và $$ Z_2 $$, biên độ phản xạ chuẩn hóa thường có dạng
$$ R=\frac{Z_2-Z_1}{Z_2+Z_1}. $$
Khi $$ Z_2=Z_1 $$ thì $$ R=0 $$, nghĩa là không có phản xạ. Khi hai môi trường khác nhau nhiều, phản xạ mạnh lên. Đây là nguyên lý cốt lõi của ảnh địa chấn phản xạ.

### 6. Phân tầng độ khó

**Bậc đại học.** Áp điều kiện ghép và diễn giải ý nghĩa của phản xạ.

**Bậc sau đại học.** Liên hệ với scattering theory, truyền qua nhiều lớp và ma trận truyền.
