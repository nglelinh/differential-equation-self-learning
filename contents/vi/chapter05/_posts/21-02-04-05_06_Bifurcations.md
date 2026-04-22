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

Bài học này giúp sinh viên hiểu phân nhánh như sự thay đổi cấu trúc định tính của nghiệm khi một tham số biến thiên, phân biệt các phân nhánh chuẩn như saddle-node, transcritical, pitchfork và Hopf, và thấy vì sao những thay đổi nhỏ về tham số có thể dẫn đến những chuyển pha động lực học rất lớn.

## Kiến thức nền

Sinh viên cần nắm điểm cân bằng, ổn định và trực giác mặt phẳng pha. Kiến thức về chu trình giới hạn cũng hữu ích vì phân nhánh Hopf là điểm gặp giữa cân bằng và dao động.

## Dẫn nhập

![Bifurcation diagram cho hệ tham số]({{ site.imgurl }}/chapter_img/chapter05/06_bifurcations.svg)

Một hệ động lực không chỉ phụ thuộc vào trạng thái ban đầu; nó còn phụ thuộc vào các tham số mô hình. Nhiều khi, thay đổi tham số rất nhỏ chỉ làm quỹ đạo biến đổi một ít. Nhưng cũng có khi một thay đổi rất nhỏ làm số điểm cân bằng đổi hẳn, làm ổn định bị đảo, hoặc làm xuất hiện một dao động tuần hoàn mới. Hiện tượng đó được gọi là phân nhánh.

Bài học về phân nhánh đặc biệt quan trọng vì nó cho sinh viên một ngôn ngữ để nói về ngưỡng, chuyển pha và mất ổn định. Ta không chỉ hỏi hệ đang làm gì, mà còn hỏi: nếu môi trường thay đổi một chút, cấu trúc động học của hệ có đổi kiểu không? Đây là tư duy mô hình hóa rất mạnh trong khoa học ứng dụng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một hệ có nhiều "chế độ hoạt động". Khi tham số đi qua một ngưỡng, hệ bỗng chuyển từ chế độ này sang chế độ khác. Giống như việc tăng nhiệt độ tới đúng một mức khiến vật chất đổi pha, trong động lực học, tham số tới ngưỡng cũng có thể làm đổi toàn bộ hình học nghiệm.

### Cách nhìn hình ảnh

Biểu đồ phân nhánh thường vẽ các điểm cân bằng theo tham số. Các nhánh ổn định được vẽ nét liền, nhánh không ổn định nét đứt. Từ hình đó, sinh viên nhìn thấy ngay khi nào nhánh mới được tạo ra, khi nào hai nhánh trao đổi ổn định, và khi nào quỹ đạo đóng xuất hiện.

### Cách nhìn hình thức

Xét hệ hoặc phương trình một tham số
$$ \dot{x}=f(x,\mu). $$
Phân nhánh xảy ra khi thay đổi nhỏ của $$ \mu $$ làm thay đổi số lượng hoặc ổn định của điểm cân bằng, hoặc làm xuất hiện một đối tượng động lực học mới như chu trình giới hạn. Các dạng chuẩn cơ bản gồm:
$$ \dot{x}=\mu+x^2 $$
cho saddle-node,
$$ \dot{x}=\mu x-x^2 $$
cho transcritical,
$$ \dot{x}=\mu x-x^3 $$
cho pitchfork siêu tới hạn.

## Những ngộ nhận thường gặp

- "Phân nhánh chỉ là vẽ đồ thị tham số." Sai. Nó là thay đổi thực sự của cấu trúc động học.
- "Tham số phải đổi rất lớn mới gây phân nhánh." Không đúng. Chỉ cần đi qua ngưỡng tới hạn.
- "Mọi thay đổi số điểm cân bằng đều giống nhau." Sai. Các kiểu phân nhánh khác nhau có cơ chế và ý nghĩa khác nhau.
- "Phân nhánh chỉ liên quan hệ một chiều." Sai. Trong hệ hai chiều còn có Hopf, nơi quỹ đạo tuần hoàn xuất hiện.

## Tiến trình học tập đề xuất

### Bước 1: Xác định điểm cân bằng theo tham số

Giải
$$ f(x,\mu)=0. $$

### Bước 2: Xét ổn định của từng nhánh

Thường bằng đạo hàm theo $$ x $$ hoặc Jacobian.

### Bước 3: Vẽ biểu đồ phân nhánh

Đây là cách nhìn toàn cục hóa thông tin.

### Bước 4: Diễn giải ý nghĩa mô hình hóa

Hỏi ngưỡng tới hạn mang nghĩa gì trong bài toán thực tế.

### Các checkpoint

- Sinh viên có phân biệt được tạo-hủy nhánh với trao đổi ổn định hay không.
- Sinh viên có nhìn ra vai trò của tính đối xứng trong pitchfork hay không.
- Sinh viên có hiểu phân nhánh Hopf khác bản chất với các phân nhánh cân bằng một chiều như thế nào không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Saddle-node

Xét
$$ \dot{x}=\mu-x^2. $$
Điểm cân bằng thỏa
$$ x=\pm \sqrt{\mu} $$
khi $$ \mu>0 $$. Nếu $$ \mu<0 $$ thì không có cân bằng thực. Tại $$ \mu=0 $$, hai cân bằng nhập vào nhau tại gốc. Đây là mô hình chuẩn của sự tạo-hủy một cặp cân bằng.

### Ví dụ 2: Transcritical

Xét
$$ \dot{x}=\mu x-x^2=x(\mu-x). $$
Hai nhánh cân bằng là
$$ x=0,\qquad x=\mu. $$
Khi $$ \mu $$ đổi dấu, chúng trao đổi ổn định cho nhau. Đây là phân nhánh chuẩn rất quan trọng trong mô hình dịch tễ và sinh thái.

### Ví dụ 3: Pitchfork

Xét
$$ \dot{x}=\mu x-x^3. $$
Khi $$ \mu<0 $$, chỉ có cân bằng $$ x=0 $$ và nó ổn định. Khi $$ \mu>0 $$, xuất hiện hai nhánh mới
$$ x=\pm \sqrt{\mu} $$
ổn định, còn $$ x=0 $$ trở nên không ổn định. Đây là ví dụ điển hình của phá vỡ đối xứng.

### Ví dụ 4: Hopf

Trong hệ hai chiều, khi một cặp trị riêng phức của Jacobian đi qua trục ảo khi tham số thay đổi, một chu trình giới hạn có thể xuất hiện hoặc biến mất. Đây là phân nhánh Hopf. Điểm mạnh của ví dụ này là sinh viên thấy phân nhánh không chỉ tạo cân bằng mới mà còn có thể tạo dao động mới.

## Câu hỏi khái niệm

1. Vì sao thay đổi nhỏ của tham số lại có thể gây thay đổi lớn về động lực học?
2. Saddle-node và transcritical khác nhau ở bản chất nào?
3. Vì sao Hopf là bước ngoặt quan trọng từ cân bằng sang dao động?

## Bài toán ứng dụng

1. Một hệ sinh học có ngưỡng mật độ tối thiểu để tồn tại. Hãy giải thích vì sao saddle-node là mô hình hợp lý.
2. Trong dịch tễ, trạng thái không bệnh và trạng thái có bệnh có thể trao đổi ổn định khi tham số lây thay đổi. Hãy liên hệ với transcritical.
3. Một hệ cơ học tự kích bắt đầu dao động tuần hoàn khi tham số vượt ngưỡng. Hãy diễn giải điều đó như một Hopf.

## Chiến lược giảng dạy tương tác

- Cho sinh viên vẽ biểu đồ phân nhánh từ các phương trình chuẩn thay vì chỉ xem hình có sẵn.
- Hỏi lớp: "Điều gì được giữ nguyên và điều gì thay đổi khi tham số đi qua ngưỡng?"
- So sánh ba ví dụ chuẩn một chiều để sinh viên thấy rõ sự khác nhau về hình học nhánh.
- Khuyến khích sinh viên gắn mỗi kiểu phân nhánh với một câu chuyện ứng dụng thật.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu làm chắc ba ví dụ chuẩn một chiều trước. Chỉ cần hiểu rõ saddle-node, transcritical và pitchfork đã là nền rất tốt.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tìm điều kiện phổ gợi ý Hopf hoặc giải thích vai trò của đối xứng trong pitchfork siêu tới hạn và dưới tới hạn.

## Tóm tắt dễ nhớ

Phân nhánh là lúc cấu trúc định tính của hệ đổi kiểu khi tham số vượt ngưỡng. Không phải mọi thay đổi đều giống nhau: có tạo-hủy cân bằng, có trao đổi ổn định, có phá vỡ đối xứng, và có cả sự xuất hiện dao động tuần hoàn. Đây là ngôn ngữ của các ngưỡng chuyển pha trong động lực học.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Oằn cột trong cơ học
- Bài toán: Cột thẳng đột ngột mất ổn định và lệch sang trái hoặc phải khi tải vượt ngưỡng.
- Mô hình chuẩn:
$$ \dot{x}=\mu x-x^3. $$
- Giả thiết và giới hạn: Đây là mô hình biên độ chuẩn, không phải mô hình đàn hồi đầy đủ.
- Diễn giải: Khi $$ \mu $$ đổi dấu, cân bằng trung tâm mất ổn định và hai trạng thái mới xuất hiện.

#### Ngưỡng bùng phát dịch
- Bài toán: Dịch chuyển từ tắt dần sang bùng lên khi tham số lây truyền vượt ngưỡng.
- Mô hình chuẩn kiểu transcritical:
$$ \dot{x}=\mu x-x^2. $$
- Giả thiết và giới hạn: Chỉ mô tả cấu trúc ngưỡng cục bộ.
- Diễn giải: Hai nhánh cân bằng trao đổi ổn định tại ngưỡng.

### 2. Trực giác bổ sung và các kết nối

Phân nhánh là thay đổi định tính khi tham số đi qua ngưỡng, không chỉ là thay đổi định lượng của nghiệm. Một hiểu lầm thường gặp là nghĩ cần thay đổi tham số lớn mới có chuyển pha động lực học; thật ra chỉ cần đi qua giá trị tới hạn. Bài này nối ổn định với mô hình hóa ngưỡng, chuyển pha và mất ổn định trong khoa học ứng dụng.

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

Xét
$$ \dot{x}=\mu x-x^3. $$
Điểm cân bằng là
$$ x=0,\qquad x=\pm\sqrt{\mu}\ \text{khi}\ \mu>0. $$
Khi $$ \mu<0 $$, chỉ còn $$ x=0 $$ và nó ổn định. Khi $$ \mu>0 $$, gốc mất ổn định còn hai nhánh mới ổn định. Đây là pitchfork siêu tới hạn kinh điển.

### 6. Phân tầng độ khó

**Bậc đại học.** Đọc sơ đồ phân nhánh và phân biệt saddle-node, transcritical, pitchfork.

**Bậc sau đại học.** Học center manifold, normal form và phân nhánh Hopf cho hệ nhiều chiều.

## Tài liệu tham khảo

- Strogatz, Chương 3 và 8: rất tốt cho các phân nhánh chuẩn và trực giác hình học.
- Arnold, Chương 5: hữu ích cho góc nhìn hình học và tham số của phân nhánh.
