---
layout: post
title: "03-02 Biến đổi Laplace của Hàm Cơ bản"
chapter: '03'
order: 2
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên xây dựng bảng Laplace cho các hàm cơ bản: hằng, lũy thừa, mũ, sin, cos và các tổ hợp đơn giản. Mục tiêu không phải thuộc lòng máy móc, mà là hiểu quan hệ giữa hình dạng của hàm trong miền thời gian và cấu trúc phân thức trong miền $$ s $$, đồng thời biết dùng tính tuyến tính và dịch chuyển để suy ra nhanh nhiều công thức mới.

## Kiến thức nền
Sinh viên cần nắm định nghĩa Laplace, kỹ năng tích phân từng phần và công thức Euler cơ bản. Đây là bài luyện thao tác nhưng cũng là bước xây bảng từ định nghĩa, nên hiểu lý do quan trọng hơn việc nhớ kết quả.

## Dẫn nhập
![Sơ đồ minh họa cho bài 03-02 Biến đổi Laplace của Hàm Cơ bản]({{ site.imgurl }}/chapter_img/chapter03/03_02_elementary_functions.svg)

Muốn dùng Laplace như một công cụ giải bài toán, ta cần một vốn từ cơ bản. Vốn từ ấy chính là bảng các biến đổi quen thuộc. Nhưng nếu học bảng như danh sách công thức rời rạc, sinh viên rất nhanh quên. Điều bền vững hơn là nhận ra các mẫu: hàm mũ dịch chuyển biến $$ s $$, đa thức tạo ra lũy thừa của $$ 1/s $$, còn sin-cos tạo ra các mẫu phân thức bậc hai.

Vì vậy, bài học này nên được hiểu như một buổi "xây bảng" chứ không phải "chép bảng". Khi sinh viên tự dựng được vài công thức đầu từ định nghĩa, những công thức còn lại trở nên có cấu trúc và dễ nhớ hơn nhiều.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Một hàm tăng chậm như hằng số hoặc đa thức sẽ cho biến đổi Laplace có cực ở $$ s=0 $$. Một hàm mũ $$ e^{at} $$ dịch chuyển cực sang $$ s=a $$. Một dao động sin-cos không tăng biên sẽ dẫn đến mẫu bậc hai vì đạo hàm hai lần quay trở lại chính nó.

### Cách nhìn hình ảnh
Trong miền thời gian, $$ 1 $$ là mức không đổi, $$ t $$ tăng đều, $$ e^{at} $$ tăng mũ, còn $$ \sin bt $$ dao động. Trong miền Laplace, những dạng rất khác nhau này được chuyển thành những phân thức hữu tỉ khá gọn. Chính sự nén này làm Laplace hữu ích: nó gom hành vi thời gian vào vài cực và hệ số đơn giản.

### Cách nhìn hình thức
Một số công thức nền tảng là
$$ \mathcal{L}\{1\}=\frac{1}{s}, $$
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}, $$
$$ \mathcal{L}\{e^{at}\}=\frac{1}{s-a}, $$
$$ \mathcal{L}\{\cos bt\}=\frac{s}{s^2+b^2}, $$
$$ \mathcal{L}\{\sin bt\}=\frac{b}{s^2+b^2}. $$
Những công thức này đủ để xây phần lớn ví dụ đầu chương.

## Những ngộ nhận thường gặp
- "Phải nhớ toàn bộ bảng ngay lập tức." Sai. Chỉ cần nắm các mẫu gốc và cách suy ra.
- "Các công thức là ngẫu nhiên." Sai. Chúng phản ánh chặt chẽ cấu trúc đạo hàm và tăng trưởng của hàm.
- "Sin và cos khác hẳn nhau nên công thức cũng không liên hệ." Sai. Chúng gắn với cùng mẫu $$ s^2+b^2 $$.
- "Laplace của đa thức chỉ là phép thay thế ký hiệu." Sai. Nó đến từ tích phân từng phần lặp lại.

## Tiến trình học tập đề xuất
### Bước 1: Dựng lại vài công thức đầu từ định nghĩa
Đặc biệt là $$ 1 $$, $$ e^{at} $$, $$ t $$.

### Bước 2: Nhìn ra mẫu cho lũy thừa
Từ $$ t $$ đến $$ t^n $$ qua tích phân từng phần.

### Bước 3: Dựng sin và cos
Dùng tích phân từng phần hoặc Euler.

### Bước 4: Dùng tính tuyến tính và dịch chuyển
Để tạo thêm công thức mới từ các công thức gốc.

### Các checkpoint
- Sinh viên có phân biệt được tác động của tham số $$ a $$ trong $$ e^{at} $$ và của tham số $$ b $$ trong $$ \sin bt $$ hay không.
- Sinh viên có nhận ra mẫu $$ n! / s^{n+1} $$ hay không.
- Sinh viên có suy ra được công thức tổ hợp đơn giản mà không tra bảng ngay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Laplace của $$ t $$
Ta tính
$$ \mathcal{L}\{t\}=\int_0^\infty te^{-st}dt. $$
Tích phân từng phần với
$$ u=t,\qquad dv=e^{-st}dt. $$
Suy ra
$$ du=dt,\qquad v=-\frac{1}{s}e^{-st}. $$
Do đó
$$
\mathcal{L}\{t\}=\left[-\frac{t}{s}e^{-st}\right]_0^\infty+\frac{1}{s}\int_0^\infty e^{-st}dt=\frac{1}{s^2}.
$$

### Ví dụ 2: Mẫu tổng quát cho $$ t^n $$
Từ ví dụ trên và tích phân từng phần lặp lại, ta được
$$ \mathcal{L}\{t^2\}=\frac{2}{s^3}, $$
$$ \mathcal{L}\{t^3\}=\frac{6}{s^4}, $$
và tổng quát
$$ \mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}. $$
Ví dụ này dạy sinh viên nhận ra mẫu thay vì tính lại từ đầu.

### Ví dụ 3: Laplace của sin và cos
Với
$$
I=\mathcal{L}\{\sin bt\},\qquad J=\mathcal{L}\{\cos bt\},
$$
ta có thể tích phân từng phần để thu một hệ liên hệ giữa $$ I $$ và $$ J $$, rồi giải ra:
$$ I=\frac{b}{s^2+b^2},\qquad J=\frac{s}{s^2+b^2}. $$
Điểm đáng nhớ là cả hai cùng có mẫu số $$ s^2+b^2 $$, phản ánh tính chất dao động bậc hai của sin-cos.

### Ví dụ 4: Dùng dịch chuyển theo mũ
Từ
$$ \mathcal{L}\{\cos 2t\}=\frac{s}{s^2+4}, $$
ta suy ra
$$
\mathcal{L}\{e^{3t}\cos 2t\}=\frac{s-3}{(s-3)^2+4}.
$$
Đây là ví dụ điển hình cho việc không cần tính lại tích phân từ đầu.

## Câu hỏi khái niệm
1. Vì sao đa thức $$ t^n $$ lại dẫn đến cực bậc cao tại $$ s=0 $$?
2. Vì sao $$ e^{at} $$ chỉ đơn giản dịch chuyển biến $$ s $$?
3. Mẫu số $$ s^2+b^2 $$ nói gì về bản chất dao động của sin và cos?

## Bài toán ứng dụng
1. Một tín hiệu điều hòa trong điện tử thường được viết bằng sin hoặc cos. Hãy giải thích vì sao công thức Laplace của chúng là nền tảng cho phân tích mạch.
2. Một tín hiệu tăng mũ rồi dao động, như $$ e^{at}\cos bt $$, có thể xuất hiện trong mô hình nào và vì sao dịch chuyển theo $$ s $$ là hợp lý?
3. Một đa thức theo thời gian có thể mô tả một đầu vào tăng dần. Hãy giải thích vì sao ảnh của nó trong miền Laplace lại tập trung gần $$ s=0 $$.

## Chiến lược giảng dạy tương tác
- Cho sinh viên tự dựng bảng "gốc" gồm 5 công thức trước khi được phát bảng đầy đủ.
- Chia lớp thành nhóm: một nhóm phụ trách đa thức, một nhóm phụ trách mũ, một nhóm phụ trách lượng giác, rồi ghép kết quả.
- Yêu cầu sinh viên giải thích bằng lời vì sao công thức của $$ \sin bt $$ và $$ \cos bt $$ lại giống nhau ở mẫu số.
- Tổ chức bài tập đoán nhanh: nhìn hàm trong thời gian, dự đoán hình dạng phân thức theo $$ s $$.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cho sinh viên yếu dùng một bảng tóm tắt gồm "hàm gốc", "công thức", "mẫu ghi nhớ". Ví dụ: đa thức cho lũy thừa của $$ 1/s $$, mũ cho dịch chuyển, lượng giác cho mẫu bậc hai.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi tự chứng minh công thức cho $$ t^n $$ bằng quy nạp hoặc dùng đạo hàm theo tham số để suy ra nhiều công thức mới từ $$ \mathcal{L}\{1\} $$.

## Tóm tắt dễ nhớ
Muốn dùng Laplace hiệu quả, đừng chỉ học bảng hãy học mẫu. Hằng và đa thức cho các lũy thừa của $$ 1/s $$. Hàm mũ dịch chuyển $$ s $$. Sin-cos tạo ra mẫu $$ s^2+b^2 $$. Khi hiểu ba mẫu này, phần lớn bảng Laplace trở nên dễ nhớ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động điều hòa
- Bài toán: Vị trí của hệ dao động sin-cos cần được chuyển sang miền $$ s $$ để giải ODE hay phân tích đáp ứng.
- Mô hình:
$$ \sin bt,\qquad \cos bt. $$
- Giả thiết và giới hạn: Dao động biên độ không đổi, tần số đơn.
- Diễn giải: Cùng mẫu số $$ s^2+b^2 $$ phản ánh bản chất dao động bậc hai của sin-cos.

#### Tăng trưởng dân số và đầu tư mũ
- Bài toán: Nhiều quá trình tự nhiên hay tài chính có dạng $$ e^{at} $$.
- Mô hình:
$$ f(t)=e^{at}. $$
- Giả thiết và giới hạn: Tham số tăng trưởng không đổi.
- Diễn giải: Pole dịch từ $$ 0 $$ sang $$ a $$ cho thấy cấu trúc tăng trưởng mũ dịch chuyển trực tiếp trong miền $$ s $$.

#### Tín hiệu đa thức trong điều khiển
- Bài toán: Một nguồn ramp hoặc parabolic input xuất hiện thường xuyên trong kiểm định hệ điều khiển.
- Mô hình:
$$ 1,\quad t,\quad t^2,\ldots $$
- Giả thiết và giới hạn: Tín hiệu trơn, xác định trên $$ t\ge 0 $$.
- Diễn giải: Mẫu $$ n!/s^{n+1} $$ cho thấy bậc đa thức càng cao thì pole tại 0 càng lặp nhiều.

### 2. Trực giác bổ sung và các kết nối

Bảng Laplace cơ bản không nên được học như một danh sách rời rạc. Nó là bản đồ cho thấy dạng tín hiệu trong miền thời gian nén thành cấu trúc cực trong miền $$ s $$ như thế nào. Bài này nối rất mạnh với chương hàm truyền: về sau, chỉ cần nhìn mẫu số và tử số ta sẽ đoán được nhiều hành vi thời gian mà chưa cần tính đầy đủ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0.5, 6, 500)
L1 = 1 / s
Lt = 1 / s**2
Lsin = 2 / (s**2 + 4)
Lcos = s / (s**2 + 4)

plt.plot(s, L1, label="L{1} = 1/s")
plt.plot(s, Lt, label="L{t} = 1/s^2")
plt.plot(s, Lsin, label="L{sin 2t}")
plt.plot(s, Lcos, label="L{cos 2t}")
plt.xlabel("s")
plt.ylabel("F(s)")
plt.title("Một số biến đổi Laplace cơ bản")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Biểu đồ này giúp sinh viên thấy rằng những tín hiệu rất khác nhau trong thời gian trở thành các đường cong hữu tỉ khá gọn trong miền $$ s $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: Laplace table intuition plot
- search: sine cosine Laplace transform visualization
- search: ramp input Laplace transform control

### 5. Bài toán mẫu có bối cảnh thực

Một tín hiệu ramp trong kiểm định hệ là
$$ f(t)=3t. $$
Từ công thức cơ bản
$$ \mathcal{L}\{t\}=\frac{1}{s^2}, $$
ta suy ra ngay
$$ \mathcal{L}\{3t\}=\frac{3}{s^2}. $$
Nếu tín hiệu được nhân thêm một mũ suy giảm như $$ e^{-2t}t $$, ta dùng dịch chuyển:
$$ \mathcal{L}\{e^{-2t}t\}=\frac{1}{(s+2)^2}. $$
Đây là một ví dụ tốt để sinh viên thấy cách xây bảng từ hai mẫu gốc thay vì học thuộc nguyên dòng.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm chắc các mẫu cơ bản và dùng tính tuyến tính, dịch chuyển để tạo công thức mới.

**Bậc sau đại học.** Dùng tham số hóa và đạo hàm theo tham số để suy ra họ công thức rộng hơn từ vài biến đổi gốc.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: tốt cho việc xây bảng Laplace một cách có lý do.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài luyện trực tiếp từ định nghĩa.
- Ross — *Differential Equations*: gọn, phù hợp để ôn nhanh các mẫu công thức.
