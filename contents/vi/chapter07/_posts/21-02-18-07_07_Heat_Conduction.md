---
layout: post
title: "07-07 Ứng dụng: Dẫn nhiệt"
chapter: '07'
order: 7
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

## Mục tiêu

Bài học này áp dụng toàn bộ tư duy bài toán giá trị biên vào mô hình dẫn nhiệt trạng thái dừng. Sau bài học, sinh viên cần hiểu profile nhiệt độ cân bằng như nghiệm của một BVP, biết diễn giải các điều kiện biên nhiệt học, và thấy cách hàm Green hay khai triển theo hàm riêng hỗ trợ giải các bài toán nhiệt thực tế.

## Kiến thức nền

Sinh viên nên nắm BVP hai điểm, điều kiện biên Dirichlet-Neumann-Robin, và trực giác về nhiệt độ cùng thông lượng nhiệt. Một nền tảng cơ bản về phương trình nhiệt cũng rất có ích, dù bài này tập trung vào trạng thái dừng.

## Dẫn nhập

![Dẫn nhiệt trạng thái dừng trong một thanh]({{ site.imgurl }}/chapter_img/chapter07/07_heat_conduction.svg)

Khi nói đến dẫn nhiệt, nhiều sinh viên lập tức nghĩ đến một quá trình phụ thuộc thời gian: nhiệt lan truyền từ chỗ nóng sang chỗ lạnh, profile thay đổi dần theo thời gian. Nhưng nếu chờ đủ lâu để hệ đạt cân bằng, ta bước vào một bài toán hoàn toàn khác. Thời gian biến mất, và điều còn lại là một cấu hình nhiệt độ không gian ổn định. Đó chính là một bài toán giá trị biên.

Bài học này rất quan trọng vì nó cho sinh viên thấy BVP không chỉ là phần chuẩn bị kỹ thuật cho lý thuyết phổ. Nó mô tả trực tiếp một hiện tượng vật lý quen thuộc và rất thực tế. Đồng thời, đây cũng là chiếc cầu tự nhiên sang chương phương trình nhiệt sau này, nơi trạng thái dừng sẽ đóng vai trò nền cho bài toán phụ thuộc thời gian.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một profile nhiệt độ trạng thái dừng là hình dạng nhiệt mà thanh "chấp nhận" sau khi mọi chuyển tiếp đã tắt. Nó không còn thay đổi theo thời gian, nhưng vẫn có thể cong, dốc hoặc bất đối xứng theo không gian nếu có nguồn nhiệt hay điều kiện biên khác nhau.

### Cách nhìn hình ảnh

Nếu hai đầu thanh bị giữ ở nhiệt độ cố định, profile thường bị "ghim" ở hai đầu. Nếu một đầu cách nhiệt, độ dốc tại đó bằng 0. Nếu đầu thanh trao đổi nhiệt với môi trường, điều kiện Robin xuất hiện và profile phản ánh vừa nhiệt độ vừa thông lượng tại biên. Các hình ảnh này giúp sinh viên gắn điều kiện biên với hành vi hình học của đồ thị nhiệt độ.

### Cách nhìn hình thức

Một mô hình dẫn nhiệt trạng thái dừng một chiều điển hình là
$$ -(k(x)T')'=f(x), $$
trong đó $$ k(x) $$ là hệ số dẫn nhiệt và $$ f(x) $$ là nguồn nhiệt phân bố. Điều kiện biên có thể là
$$ T(0)=T_0,\qquad T(L)=T_L $$
hoặc các điều kiện thông lượng như
$$ T'(0)=0. $$
Đây là một BVP elliptic một chiều cổ điển.

## Những ngộ nhận thường gặp

- "Dẫn nhiệt luôn là PDE phụ thuộc thời gian." Không đúng ở trạng thái dừng.
- "Trạng thái dừng thì nhiệt độ phải hằng." Sai; chỉ cần không đổi theo thời gian, không nhất thiết đồng đều theo không gian.
- "Điều kiện biên nhiệt chỉ có dạng cố định nhiệt độ." Không đúng; thông lượng và điều kiện trao đổi với môi trường cũng rất quan trọng.
- "Bài này không liên hệ gì với Sturm-Liouville." Sai. Nó dùng đúng cùng tư duy toán tử và biên của cả chương.

## Tiến trình học tập đề xuất

### Bước 1: Diễn giải thiết lập vật lý

Sinh viên cần phân biệt nguồn nhiệt, độ dẫn, và điều kiện ở hai đầu thanh.

### Bước 2: Viết BVP trạng thái dừng

Đây là bước mô hình hóa trung tâm.

### Bước 3: Giải các trường hợp cơ bản

Ví dụ có nguồn hằng hoặc không nguồn là nơi trực giác được hình thành tốt nhất.

### Bước 4: Liên hệ với các công cụ của chương

Hàm Green, trị riêng và khai triển theo mode đều sẽ quay lại ở đây hoặc ở chương sau.

### Các checkpoint

- Sinh viên có nhận ra đâu là điều kiện nhiệt độ, đâu là điều kiện thông lượng hay không.
- Sinh viên có hiểu vì sao trạng thái dừng loại bỏ biến thời gian hay không.
- Sinh viên có giải thích được hình dạng vật lý của profile nhiệt thu được hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Thanh với nguồn nhiệt đều

Giải
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Tích phân hai lần:
$$ T''=-1, $$
$$ T'=-x+C_1, $$
$$ T=-\frac{x^2}{2}+C_1x+C_2. $$
Từ điều kiện biên:
$$ C_2=0,\qquad C_1=\frac{1}{2}, $$
nên
$$ T(x)=\frac{x(1-x)}{2}. $$
Profile này đạt cực đại ở giữa thanh, phản ánh nhiệt được sinh ra đều trong lòng thanh và thoát ra ở hai đầu.

### Ví dụ 2: Đầu cách nhiệt

Nếu một đầu được cách nhiệt, ta có điều kiện
$$ T'(0)=0. $$
Ví dụ này giúp sinh viên hiểu rằng "không có dòng nhiệt qua biên" không nói về giá trị nhiệt độ, mà nói về độ dốc của profile nhiệt.

### Ví dụ 3: Điều kiện Robin

Điều kiện
$$ T'(L)+hT(L)=0 $$
mô tả trao đổi nhiệt với môi trường bên ngoài. Ví dụ này rất quan trọng vì nó cho thấy điều kiện biên không chỉ là ràng buộc toán học mà là mô hình hóa trực tiếp một cơ chế vật lý.

### Ví dụ 4: Liên hệ với hàm Green

Khi nguồn nhiệt phức tạp hơn, nghiệm có thể được viết dưới dạng
$$ T(x)=\int_0^L G(x,\xi)f(\xi)\,d\xi. $$
Đây là cách nhìn giúp sinh viên thấy sự thống nhất giữa BVP, Green và dẫn nhiệt trạng thái dừng.

## Câu hỏi khái niệm

1. Vì sao bài toán nhiệt trạng thái dừng là một BVP thay vì IVP?
2. Ý nghĩa vật lý của điều kiện Neumann và Robin trong dẫn nhiệt là gì?
3. Vì sao có nguồn nhiệt bên trong thì profile cân bằng thường là hàm cong chứ không phải đường thẳng?

## Bài toán ứng dụng

1. Trong thiết kế tường hay thanh dẫn nhiệt, vì sao cần biết profile nhiệt độ cân bằng chứ không chỉ nhiệt độ tại một điểm?
2. Một lớp cách nhiệt ở biên sẽ làm thay đổi điều kiện biên như thế nào?
3. Trong hệ nhiều lớp vật liệu, vì sao việc ghép điều kiện nhiệt độ và thông lượng ở mặt phân cách lại quan trọng?

## Chiến lược giảng dạy tương tác

- Cho sinh viên dịch các mô tả vật lý thành điều kiện biên toán học.
- So sánh profile nhiệt dưới các lựa chọn Dirichlet, Neumann, Robin để tạo trực giác mạnh.
- Yêu cầu lớp dự đoán điểm nóng nhất trước khi giải bài toán cụ thể.
- Liên hệ trực tiếp với các tình huống đời thật như tường, thanh gia nhiệt, hay bộ tản nhiệt.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu làm chắc các ví dụ tích phân trực tiếp và tập diễn giải nghĩa vật lý của từng điều kiện biên trước khi đi vào Green hay khai triển mode.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi xét hệ số dẫn nhiệt biến thiên hoặc bài toán nhiều lớp vật liệu với điều kiện nối ở các mặt phân cách.

## Tóm tắt dễ nhớ

Dẫn nhiệt trạng thái dừng là một ứng dụng tự nhiên và rất thực của bài toán giá trị biên. Ở đây, nghiệm là profile nhiệt độ không gian cân bằng, còn điều kiện biên biểu diễn cách hệ tương tác với môi trường ở hai đầu. Bài học này là chiếc cầu rất đẹp sang chương phương trình nhiệt.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiệt độ trạng thái dừng trong thanh không đồng đều
- Bài toán: Tìm phân bố nhiệt cân bằng khi có nguồn trong thanh và hai đầu được giữ hay cách nhiệt.
- Mô hình:
$$ -(k(x)T')'=f(x), $$
kèm điều kiện biên Dirichlet, Neumann hay Robin.
- Giả thiết và giới hạn: Chế độ dừng, một chiều, không có tích trữ theo thời gian.
- Diễn giải: Đây là BVP điển hình dẫn tới Green hoặc khai triển theo hàm riêng.

#### Truyền nhiệt trong tường nhiều lớp
- Bài toán: Tường ghép vật liệu có độ dẫn khác nhau nhưng vẫn cần profile nhiệt độ cân bằng.
- Mô hình:
$$ -(k(x)T')'=0 $$
trên từng lớp với điều kiện ghép thông lượng ở các mặt phân cách.
- Giả thiết và giới hạn: Mô hình một chiều, ổn định theo thời gian.
- Diễn giải: Điều kiện biên và điều kiện nối xác định hoàn toàn profile nhiệt không gian.

### 2. Trực giác bổ sung và các kết nối

Bài toán nhiệt dẫn trạng thái dừng cho thấy rõ nhất sự khác nhau giữa BVP và bài toán tiến hóa: ở đây không còn biến thời gian, chỉ còn cấu hình không gian cân bằng. Một bẫy phổ biến là không phân biệt profile dừng với nghiệm phụ thuộc thời gian của phương trình nhiệt. Bài này cũng chuẩn bị trực tiếp cho Chương 9.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

def ode(x, y):
    return np.vstack((y[1], -10 * np.ones_like(x)))

def bc(ya, yb):
    return np.array([ya[0], yb[0] - 100])

x = np.linspace(0, 1, 200)
y_guess = np.zeros((2, x.size))
sol = solve_bvp(ode, bc, x, y_guess)

plt.plot(sol.x, sol.y[0], label="T(x)")
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("Phan bo nhiet do trang thai dung")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: steady state heat conduction boundary value problem
- search: rod temperature profile with heat source
- search: Dirichlet Neumann Robin heat boundary conditions

### 5. Bài toán mẫu có bối cảnh thực

Giải
$$ -T''=1,\qquad 0<x<1,\qquad T(0)=0,\qquad T(1)=0. $$
Tích phân hai lần:
$$
T''=-1,\qquad
T'=-x+C_1,\qquad
T=-\frac{x^2}{2}+C_1 x+C_2.
$$
Từ điều kiện biên suy ra
$$ C_2=0,\qquad C_1=\frac{1}{2}, $$
nên
$$ T(x)=\frac{x(1-x)}{2}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Giải các profile nhiệt dừng đơn giản và diễn giải ý nghĩa vật lý của từng loại điều kiện biên.

**Bậc sau đại học.** Kết nối với toán tử elliptic một chiều, nguyên lý cực đại và chuẩn bị cho PDE elliptic ở các chương sau.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 10: các ví dụ BVP dẫn nhiệt trạng thái dừng.
- Haberman, Chương 5: liên hệ mạnh với mô hình vật lý và các điều kiện biên nhiệt học.
