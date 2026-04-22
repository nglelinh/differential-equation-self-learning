---
layout: post
title: "Nguyên Lý Cực Đại"
chapter: '09'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---
![21 03 04 09 07 Maximum Principles]({{ site.imgurl }}/chapter_img/chapter09/07_maximum_principles.svg)

## Mục tiêu

Bài học này trình bày nguyên lý cực đại như công cụ định tính mạnh nhất của phương trình nhiệt. Sau bài học, sinh viên cần hiểu phát biểu trực giác và hình thức của nguyên lý cực đại, biết vì sao nhiệt độ cực đại không thể tự sinh ra trong nội thất nếu không có nguồn, thấy hệ quả về tính duy nhất và ổn định, và hiểu vì sao đây là một trong những lý do khiến mô hình nhiệt rất đáng tin cậy.

## Kiến thức nền

Sinh viên nên nắm phương trình nhiệt, đạo hàm cực trị của hàm nhiều biến ở mức trực giác, và ý nghĩa vật lý của khuếch tán. Đây là bài nghiêng mạnh về tính chất định tính hơn là công thức nghiệm.

## Dẫn nhập

Cho đến đây, ta đã học cách giải phương trình nhiệt bằng mode và Green. Nhưng đôi khi điều ta cần không phải công thức nghiệm chi tiết, mà là một thông tin định tính rất mạnh: nghiệm có thể lớn đến đâu, nhỏ đến đâu, và có được một đỉnh mới bên trong miền hay không. Nguyên lý cực đại trả lời chính xác loại câu hỏi đó.

Bài này rất quan trọng vì nó cho thấy khuếch tán bị ràng buộc bởi một nguyên tắc hình học sâu sắc: nghiệm bị kiểm soát bởi biên parabolic, chứ không tự ý "bùng lên" ở bên trong. Đây là nền tảng cho tính duy nhất, ổn định và nhiều lập luận đánh giá sai số.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một vùng trong vật thể đang nóng hơn mọi nơi xung quanh, nhiệt sẽ chảy ra ngoài từ vùng đó. Vì vậy một "đỉnh nhiệt" bên trong miền có xu hướng hạ xuống chứ không thể tự tăng cao hơn nữa. Tương tự, một "hõm nhiệt" bên trong miền có xu hướng được lấp lên. Đó là linh hồn vật lý của nguyên lý cực đại.

### Cách nhìn hình ảnh

Hãy tưởng tượng đồ thị nhiệt độ theo không gian-thời gian. Nếu tại một điểm nội thất có cực đại thực sự, đạo hàm theo thời gian tại đó không thể âm theo trực giác "đang ở đỉnh". Nhưng đạo hàm bậc hai theo không gian tại cực đại lại không dương. Phương trình nhiệt ép hai điều này vào nhau và tạo ra mâu thuẫn. Hình ảnh cực trị nội thất bị cấm chính là nội dung của nguyên lý cực đại.

### Cách nhìn hình thức

Xét $$ u_t=\alpha^2u_{xx} $$ trên miền parabolic $$ Q_T=(0,L)\times(0,T] $$. Biên parabolic là

$$
\Gamma_T=\bigl([0,L]\times\{0\}\bigr)\cup\bigl(\{0,L\}\times[0,T]\bigr).
$$

Nguyên lý cực đại yếu nói rằng nếu $$ u $$ liên tục trên $$ \overline{Q_T} $$ và đủ trơn trong $$ Q_T $$, thì $$ \max_{\overline{Q_T}}u=\max_{\Gamma_T}u $$. Một phát biểu tương tự đúng cho cực tiểu.

## Những ngộ nhận thường gặp

- "Nguyên lý cực đại chỉ là một quan sát hình học mơ hồ." Sai. Nó là định lý chặt chẽ với hệ quả rất mạnh.
- "Nếu không biết nghiệm cụ thể thì không thể nói gì về nó." Không đúng; nguyên lý cực đại cho thông tin định tính mạnh mà không cần công thức nghiệm.
- "Nghiệt độ cực đại bên trong miền có thể tự tăng nếu PDE cho phép." Với phương trình nhiệt thuần nhất, điều đó bị cấm.
- "Đây chỉ là kết quả đẹp nhưng ít dùng." Sai; tính duy nhất và nhiều đánh giá ổn định đều dựa trên nó.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu biên parabolic

Sinh viên cần thấy khác biệt giữa biên không gian-thời gian này với biên hình học thuần túy.

### Bước 2: Xét một cực đại nội thất giả định

Đây là hạt nhân của chứng minh.

### Bước 3: Dùng dấu của đạo hàm tại cực trị

Từ trực giác hình học đi đến mâu thuẫn PDE.

### Bước 4: Suy ra tính duy nhất

Đây là ứng dụng quan trọng nhất.

### Các checkpoint

- Sinh viên có mô tả được biên parabolic bằng lời hay không.
- Sinh viên có hiểu vì sao cực trị nội thất dẫn đến mâu thuẫn dấu trong PDE hay không.
- Sinh viên có dùng được nguyên lý cực đại để giải thích tính duy nhất hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Cực đại nội thất dẫn đến mâu thuẫn

Giả sử $$ u $$ có cực đại nội thất tại $$ (x_0,t_0) $$ với $$ t_0>0 $$. Khi đó

$$
u_x(x_0,t_0)=0,
\qquad
u_{xx}(x_0,t_0)\le 0,
\qquad
u_t(x_0,t_0)\ge 0.
$$

Nhưng PDE cho $$ u_t=\alpha^2u_{xx} $$, nên $$ u_t(x_0,t_0)\le 0 $$. Suy ra $$ u_t(x_0,t_0)=0,\qquad u_{xx}(x_0,t_0)=0 $$, và trong lập luận mạnh hơn, điều này dẫn đến việc nghiệm phải đặc biệt cứng. Ví dụ này là trái tim của toàn bài.

### Ví dụ 2: Tính duy nhất

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán nhiệt với cùng dữ liệu đầu và biên. Đặt $$ w=u_1-u_2 $$. Khi đó $$ w_t=\alpha^2w_{xx} $$, và $$ w=0 $$ trên biên parabolic. Áp dụng nguyên lý cực đại cho $$ w $$ và $$ -w $$, ta suy ra $$ w\equiv 0 $$. Đây là ứng dụng cần được nhấn mạnh nhất.

### Ví dụ 3: Ổn định theo dữ liệu biên

Nếu dữ liệu đầu và biên thay đổi rất ít, hiệu hai nghiệm tương ứng bị chặn bởi mức sai khác đó trên biên parabolic. Ví dụ này cho thấy mô hình nhiệt không chỉ duy nhất mà còn ổn định.

### Ví dụ 4: Ý nghĩa vật lý

Nếu ban đầu mọi nhiệt độ đều nằm giữa $$ m $$ và $$ M $$, và biên cũng không vượt ra ngoài khoảng ấy, thì trong toàn bộ miền-thời gian nghiệm cũng không thể vượt ra ngoài khoảng đó. Đây là cách phát biểu vật lý dễ nhớ nhất của nguyên lý cực đại.

## Câu hỏi khái niệm

1. Vì sao biên parabolic bao gồm cả thời điểm ban đầu?
2. Tại sao nguyên lý cực đại phù hợp trực giác vật lý "nhiệt không tự sinh ra đỉnh mới"?
3. Vì sao nguyên lý cực đại lại kéo theo tính duy nhất của nghiệm?

## Bài toán ứng dụng

1. Trong mô phỏng số phương trình nhiệt, vì sao một sơ đồ số tạo ra các đỉnh nhiệt mới trong nội thất thường là dấu hiệu đáng lo?
2. Nếu dữ liệu đầu và biên đều không âm, vì sao nghiệm của bài toán nhiệt thuần nhất phải không âm?
3. Trong kiểm soát nhiệt, vì sao nguyên lý cực đại giúp đưa ra các chặn an toàn cho nhiệt độ mà không cần giải chính xác PDE?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Một đỉnh nhiệt ở bên trong miền có thể tự tăng cao hơn nữa mà không cần nguồn không?"
- Dùng lập luận dấu tại cực trị như một hoạt động để sinh viên tự điền.
- Hỏi cả lớp: "Biên nào thật sự kiểm soát nghiệm của phương trình nhiệt?"
- Cho sinh viên tự chứng minh tính duy nhất từ nguyên lý cực đại theo cặp.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám chặt vào trực giác "đỉnh hạ xuống, hõm lấp lên" rồi mới đưa phát biểu hình thức. Nếu trực giác đó vững, chứng minh bằng dấu đạo hàm sẽ tự nhiên hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận nguyên lý cực đại mạnh, hoặc so sánh vì sao phương trình sóng không có một nguyên lý cực đại tương tự ở dạng đơn giản như phương trình nhiệt.

## Tóm tắt dễ nhớ

Nguyên lý cực đại nói rằng nghiệm của phương trình nhiệt bị kiểm soát bởi biên parabolic và thời điểm ban đầu. Nhiệt không tự tạo ra cực đại hay cực tiểu mới trong nội thất. Từ đó kéo theo tính duy nhất và ổn định rất mạnh của bài toán.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - nền tảng chuẩn cho phương trình nhiệt, nguyên lý cực đại, và hàm Green.
- Haberman, *Applied Partial Differential Equations* - nhiều ví dụ vật lý và phương pháp tính minh họa rất rõ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Giới hạn nhiệt độ cực đại
- Bài toán: Không có nguồn trong miền, nhiệt độ bên trong không thể tự tạo ra cực đại mới.
- Mô hình: Dùng nguyên lý cực đại cho
$$ u_t-\alpha^2 u_{xx}=0. $$
- Giả thiết và giới hạn: Miền chính quy, nghiệm đủ trơn.
- Diễn giải: Cực đại nội bộ bị cấm trừ khi nghiệm là hằng theo nghĩa thích hợp.

#### Tính duy nhất của nghiệm
- Bài toán: Muốn chứng minh bài toán nhiệt với cùng dữ kiện đầu và biên chỉ có một nghiệm.
- Mô hình: Áp dụng nguyên lý cực đại cho hiệu của hai nghiệm.
- Giả thiết và giới hạn: Cần điều kiện biên và đầu thích hợp.
- Diễn giải: Tính chất định tính mạnh này quan trọng không kém công thức nghiệm.

### 2. Trực giác bổ sung và các kết nối

Nguyên lý cực đại là một ví dụ điển hình cho việc hiểu PDE bằng cấu trúc định tính thay vì công thức tường minh. Một bẫy phổ biến là nghĩ đây chỉ là kỹ thuật chứng minh; thật ra nó nói lên bản chất vật lý rằng nhiệt độ không thể tự sinh "đỉnh nóng" mới trong quá trình khuếch tán thuần.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u0 = np.sin(np.pi * x) + 0.2 * np.sin(5 * np.pi * x)

plt.plot(x, u0, label="t=0")
for t in [0.01, 0.05, 0.15]:
    u = np.sin(np.pi * x) * np.exp(-np.pi**2 * t) + 0.2 * np.sin(5 * np.pi * x) * np.exp(-25 * np.pi**2 * t)
    plt.plot(x, u, label=f"t={t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Bien do giam dan, khong tao cuc dai moi lon hon")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: maximum principle heat equation visualization
- search: uniqueness proof heat equation maximum principle
- search: parabolic maximum principle intuition

### 5. Bài toán mẫu có bối cảnh thực

Nếu $$ u $$ thỏa bài toán nhiệt thuần nhất trên đoạn với dữ kiện đầu và biên bằng $$ 0 $$, nguyên lý cực đại cho thấy
$$ u\le 0 $$
và áp dụng cho $$ -u $$ cho
$$ u\ge 0. $$
Suy ra
$$ u\equiv 0, $$
nên nghiệm là duy nhất.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu phát biểu và ứng dụng nguyên lý cực đại vào chứng minh duy nhất.

**Bậc sau đại học.** Mở rộng sang weak maximum principle, miền nhiều chiều và toán tử parabolic tổng quát.
