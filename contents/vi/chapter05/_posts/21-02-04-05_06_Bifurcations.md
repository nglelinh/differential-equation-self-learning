---
layout: post
title: "05-06 Phân nhánh"
chapter: '05'
order: 6
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên hiểu phân nhánh như sự thay đổi cấu trúc định tính của nghiệm khi tham số biến thiên, phân biệt các dạng phân nhánh chuẩn gồm saddle-node, transcritical, pitchfork và Hopf, đồng thời thấy được vì sao những thay đổi nhỏ của tham số có thể dẫn đến chuyển đổi định tính lớn về động lực học.

## Kiến thức nền

Sinh viên cần nắm vững khái niệm điểm cân bằng, tính ổn định và trực giác mặt phẳng pha. Kiến thức về chu trình giới hạn cũng rất hữu ích vì phân nhánh Hopf là cầu nối giữa điểm cân bằng và dao động tuần hoàn.

## Dẫn nhập

![Bifurcation diagram cho hệ tham số]({{ site.imgurl }}/chapter_img/chapter05/06_bifurcations.svg)

Một hệ động lực không chỉ phụ thuộc vào điều kiện đầu mà còn phụ thuộc vào các tham số của mô hình. Thông thường, thay đổi rất nhỏ ở tham số chỉ làm quỹ đạo dịch chuyển nhẹ. Tuy nhiên, tại một số giá trị ngưỡng, một thay đổi rất nhỏ của tham số có thể làm thay đổi số lượng điểm cân bằng, đảo ngược tính ổn định hoặc làm xuất hiện một dao động tuần hoàn mới. Hiện tượng đó được gọi là **phân nhánh** (bifurcation).

Lý thuyết phân nhánh cung cấp ngôn ngữ toán học để phân tích các giá trị ngưỡng, sự chuyển trạng thái và cơ chế mất ổn định. Thay vì chỉ hỏi hệ đang vận hành ra sao ở một bộ tham số cố định, ta còn đánh giá xem cấu trúc động học của hệ có biến đổi định tính khi điều kiện môi trường thay đổi hay không.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một hệ có nhiều chế độ hoạt động khác nhau. Khi tham số đi qua một giá trị ngưỡng, hệ chuyển từ chế độ này sang chế độ khác — tương tự như khi nhiệt độ vượt qua điểm chuyển pha khiến vật chất thay đổi trạng thái.

### Cách nhìn hình ảnh

Biểu đồ phân nhánh biểu diễn vị trí các điểm cân bằng theo giá trị của tham số, trong đó các nhánh ổn định thường được vẽ nét liền và các nhánh không ổn định vẽ nét đứt. Từ biểu đồ này, ta nhận ra ngay thời điểm các nhánh mới được sinh ra, hai nhánh trao đổi tính ổn định, hoặc một quỹ đạo đóng xuất hiện.

### Cách nhìn hình thức

Xét phương trình một tham số
$$ \dot{x}=f(x,\mu). $$
Phân nhánh xảy ra tại giá trị ngưỡng của $$ \mu $$ khi một thay đổi tùy ý nhỏ của $$ \mu $$ làm thay đổi số lượng hoặc tính ổn định của các điểm cân bằng, hoặc làm phát sinh một đối tượng động lực học mới như chu trình giới hạn. Ba dạng chuẩn cơ bản một chiều gồm:
$$ \dot{x}=\mu+x^2 $$
cho phân nhánh saddle-node (yên–nút),
$$ \dot{x}=\mu x-x^2 $$
cho phân nhánh transcritical (xuyên tới hạn), và
$$ \dot{x}=\mu x-x^3 $$
cho phân nhánh pitchfork (chạc ba) siêu tới hạn.

## Những ngộ nhận thường gặp

- "Phân nhánh chỉ đơn thuần là vẽ đồ thị theo tham số." Sai. Nó phản ánh sự thay đổi thực sự về cấu trúc định tính của động lực học.
- "Tham số phải thay đổi rất lớn mới gây ra phân nhánh." Không đúng. Chỉ cần tham số đi qua giá trị ngưỡng tới hạn.
- "Mọi sự thay đổi về số lượng điểm cân bằng đều giống nhau." Sai. Mỗi dạng phân nhánh có cơ chế hình học và ý nghĩa mô hình hóa riêng.
- "Phân nhánh chỉ xảy ra ở hệ một chiều." Sai. Ở hệ từ hai chiều trở lên còn có phân nhánh Hopf, nơi dao động tuần hoàn xuất hiện từ điểm cân bằng.

## Tiến trình học tập đề xuất

### Bước 1: Tìm điểm cân bằng theo tham số

Giải phương trình
$$ f(x,\mu)=0 $$
để biểu diễn các nhánh cân bằng theo $$ \mu $$.

### Bước 2: Xét tính ổn định của từng nhánh

Sử dụng dấu của đạo hàm theo $$ x $$ (hệ một chiều) hoặc trị riêng của ma trận Jacobian (hệ nhiều chiều).

### Bước 3: Vẽ biểu đồ phân nhánh

Tổng hợp thông tin về vị trí và tính ổn định của các nhánh trên cùng một đồ thị.

### Bước 4: Diễn giải ý nghĩa mô hình hóa

Liên hệ giá trị ngưỡng tới hạn với hiện tượng thực tế trong bài toán đang xét.

### Các điểm kiểm tra

- Sinh viên có phân biệt được cơ chế sinh–hủy nhánh với cơ chế trao đổi tính ổn định hay không.
- Sinh viên có nhận ra vai trò của tính đối xứng trong phân nhánh pitchfork hay không.
- Sinh viên có giải thích được điểm khác biệt bản chất giữa phân nhánh Hopf và các phân nhánh cân bằng một chiều hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Phân nhánh saddle-node

Xét phương trình
$$ \dot{x}=\mu-x^2. $$
Khi $$ \mu>0 $$, hệ có hai điểm cân bằng
$$ x=\pm \sqrt{\mu}. $$
Khi $$ \mu<0 $$, hệ không có điểm cân bằng thực nào. Tại ngưỡng $$ \mu=0 $$, hai điểm cân bằng nhập lại thành một tại gốc tọa độ. Đây là mô hình chuẩn của cơ chế sinh–hủy một cặp điểm cân bằng.

### Ví dụ 2: Phân nhánh transcritical

Xét phương trình
$$ \dot{x}=\mu x-x^2=x(\mu-x). $$
Hệ luôn có hai nhánh cân bằng là
$$ x=0,\qquad x=\mu. $$
Khi $$ \mu $$ đổi dấu qua $$ 0 $$, hai nhánh này cắt nhau và trao đổi tính ổn định. Dạng phân nhánh này xuất hiện rất phổ biến trong các mô hình dịch tễ và sinh thái.

### Ví dụ 3: Phân nhánh pitchfork

Xét phương trình
$$ \dot{x}=\mu x-x^3. $$
Khi $$ \mu<0 $$, hệ chỉ có một điểm cân bằng $$ x=0 $$ và điểm này ổn định. Khi $$ \mu>0 $$, điểm $$ x=0 $$ trở nên không ổn định, đồng thời xuất hiện hai nhánh cân bằng mới đối xứng và ổn định là
$$ x=\pm \sqrt{\mu}. $$
Đây là ví dụ điển hình cho hiện tượng phá vỡ đối xứng.

### Ví dụ 4: Phân nhánh Hopf

Trong hệ hai chiều, khi tham số biến thiên làm một cặp trị riêng phức liên hợp của ma trận Jacobian cắt qua trục ảo, một chu trình giới hạn có thể hình thành hoặc biến mất. Đây là phân nhánh Hopf, cho thấy phân nhánh không chỉ tạo ra các điểm cân bằng mới mà còn có thể sinh ra dao động tuần hoàn.

## Câu hỏi khái niệm

1. Vì sao một thay đổi rất nhỏ của tham số lại có thể dẫn đến biến đổi lớn về cấu trúc động lực học?
2. Phân nhánh saddle-node và phân nhánh transcritical khác nhau ở điểm bản chất nào?
3. Vì sao phân nhánh Hopf là cầu nối quan trọng từ trạng thái cân bằng sang trạng thái dao động?

## Bài toán ứng dụng

1. Một quần thể sinh học có ngưỡng mật độ tối thiểu để duy trì tồn tại. Hãy giải thích vì sao phân nhánh saddle-node là mô hình phù hợp.
2. Trong dịch tễ học, trạng thái không có dịch và trạng thái có dịch lưu hành trao đổi tính ổn định khi tham số lây truyền vượt ngưỡng. Hãy liên hệ hiện tượng này với phân nhánh transcritical.
3. Một cơ hệ tự kích bắt đầu dao động tuần hoàn khi một tham số điều khiển vượt qua ngưỡng. Hãy diễn giải hiện tượng này theo phân nhánh Hopf.

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự dựng biểu đồ phân nhánh từ các phương trình dạng chuẩn thay vì chỉ quan sát hình vẽ sẵn.
- Đặt câu hỏi thảo luận: khi tham số vượt qua ngưỡng, yếu tố nào được giữ nguyên và yếu tố nào thay đổi?
- So sánh song song ba dạng phân nhánh một chiều chuẩn để làm rõ khác biệt về hình học nhánh.
- Gắn mỗi kiểu phân nhánh với một ví dụ ứng dụng thực tế cụ thể.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên nắm chắc ba dạng chuẩn một chiều (saddle-node, transcritical và pitchfork) trước khi mở rộng sang hệ hai chiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên xác định điều kiện phổ gợi ý phân nhánh Hopf, hoặc phân tích vai trò của tính đối xứng trong phân nhánh pitchfork siêu tới hạn và dưới tới hạn.

## Tóm tắt dễ nhớ

Phân nhánh xảy ra khi cấu trúc định tính của hệ thay đổi lúc tham số đi qua giá trị ngưỡng. Các cơ chế chính bao gồm sinh–hủy điểm cân bằng (saddle-node), trao đổi ổn định (transcritical), phá vỡ đối xứng (pitchfork) và hình thành dao động tuần hoàn (Hopf).

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Oằn cột trong cơ học
- Bài toán: Một thanh cột thẳng đột ngột mất ổn định và cong lệch sang trái hoặc sang phải khi tải trọng nén vượt ngưỡng.
- Mô hình chuẩn:
$$ \dot{x}=\mu x-x^3. $$
- Giả thiết và giới hạn: Đây là phương trình biên độ rút gọn, không thay thế mô hình đàn hồi đầy đủ.
- Diễn giải: Khi $$ \mu $$ đổi dấu sang dương, trạng thái thẳng đứng mất ổn định và hai trạng thái cong ổn định đối xứng xuất hiện.

#### Ngưỡng bùng phát dịch bệnh
- Bài toán: Dịch bệnh chuyển từ trạng thái tự tắt dần sang bùng phát khi tham số lây truyền vượt ngưỡng tới hạn.
- Mô hình chuẩn dạng transcritical:
$$ \dot{x}=\mu x-x^2. $$
- Giả thiết và giới hạn: Chỉ mô tả cấu trúc cục bộ quanh ngưỡng bùng phát.
- Diễn giải: Hai nhánh cân bằng trao đổi tính ổn định ngay tại giá trị ngưỡng.

### 2. Trực giác bổ sung và các kết nối

Phân nhánh là sự thay đổi mang tính định tính khi tham số vượt qua ngưỡng, chứ không chỉ là sự dịch chuyển định lượng của nghiệm. Một hiểu lầm phổ biến là cho rằng phải thay đổi tham số rất lớn mới gây ra chuyển đổi chế độ; thực tế chỉ cần vượt qua điểm tới hạn. Bài học này kết nối lý thuyết ổn định với việc mô hình hóa các ngưỡng và sự mất ổn định trong khoa học ứng dụng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(-2, 2, 400)
stable = np.sqrt(np.maximum(mu, 0))

plt.axhline(0, color="gray", lw=1)
plt.plot(mu[mu < 0], np.zeros_like(mu[mu < 0]), "b", lw=2)
plt.plot(mu[mu > 0], np.zeros_like(mu[mu > 0]), "r--", lw=2)
plt.plot(mu[mu >= 0], stable[mu >= 0], "b", lw=2)
plt.plot(mu[mu >= 0], -stable[mu >= 0], "b", lw=2)
plt.xlabel("mu")
plt.ylabel("equilibria")
plt.title("Bieu do phan nhanh pitchfork sieu toi han")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: saddle node transcritical pitchfork bifurcation
- search: Hopf bifurcation animation
- search: bifurcation diagram nonlinear dynamics

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình
$$ \dot{x}=\mu x-x^3. $$
Các điểm cân bằng là
$$ x=0,\qquad x=\pm\sqrt{\mu}\ \text{khi}\ \mu>0. $$
Khi $$ \mu<0 $$, hệ chỉ có điểm cân bằng ổn định $$ x=0 $$. Khi $$ \mu>0 $$, gốc mất ổn định trong khi hai nhánh mới ổn định. Đây là mô hình chuẩn của phân nhánh pitchfork siêu tới hạn.

### 6. Phân tầng độ khó

**Bậc đại học.** Đọc hiểu biểu đồ phân nhánh và phân biệt các dạng saddle-node, transcritical, pitchfork.

**Bậc sau đại học.** Tìm hiểu đa tạp tâm (center manifold), dạng chuẩn (normal form) và phân nhánh Hopf trong hệ nhiều chiều.

## Video tham khảo

- Xem trước: [MAE5790-12 Bifurcations in two dimensional systems](https://www.youtube.com/watch?v=oqKAVqe71vw) — Cornell MAE, tiếng Anh. Bài giảng của Strogatz về phân nhánh trong hệ hai chiều.
- [MAE5790-13 Hopf bifurcations in aeroelastic instabilities and chemical oscillators](https://www.youtube.com/watch?v=qV0tCroLOHk) — Cornell MAE, tiếng Anh. Phân nhánh Hopf trong mất ổn định khí đàn hồi và các hệ dao động hóa học.
- [MAE5790-4 Model of an insect outbreak](https://www.youtube.com/watch?v=P_YCvTabMO4) — Cornell MAE, tiếng Anh. Mô hình bùng phát sâu bệnh như phân nhánh yên–nút dưới góc nhìn sinh học.

## Tài liệu tham khảo

- Strogatz, Chương 3 và 8: trình bày rõ các dạng phân nhánh chuẩn và trực giác hình học.
- Arnold, Chương 5: hữu ích cho góc nhìn hình học và vai trò tham số trong phân nhánh.
