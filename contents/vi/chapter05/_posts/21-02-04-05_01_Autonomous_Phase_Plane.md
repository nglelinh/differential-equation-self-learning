---
layout: post
title: "05-01 Hệ Tự trị và Mặt phẳng Pha"
chapter: '05'
order: 1
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này mở đầu chương **động lực học phi tuyến** bằng cách chuyển trọng tâm từ "giải công thức nghiệm" sang "đọc hình học của quỹ đạo". Sinh viên sẽ hiểu hệ tự trị hai chiều, trường vector, nullcline, quỹ đạo trên mặt phẳng pha, và thấy vì sao mặt phẳng pha là công cụ trung tâm để hiểu hệ phi tuyến ngay cả khi không có nghiệm tường minh.

## Kiến thức nền

Sinh viên nên nắm hệ phương trình vi phân hai chiều, trường hợp tuyến tính hóa từ chương trước và ý nghĩa của điểm cân bằng. Trực giác về đường pha một chiều cũng rất hữu ích vì mặt phẳng pha là bước mở rộng tự nhiên từ đó.

## Dẫn nhập

![Mặt phẳng pha của hệ tự trị hai chiều]({{ site.imgurl }}/chapter_img/chapter05/01_autonomous_phase_plane.svg)

### Động lực học phi tuyến là gì?

**Động lực học phi tuyến** (nonlinear dynamics) nghiên cứu cách các hệ thống thay đổi theo thời gian khi các thành phần tương tác **không theo quan hệ tỷ lệ thuận**. Trong hệ tuyến tính, nếu bạn tăng gấp đôi đầu vào, đầu ra cũng tăng gấp đôi — nhưng trong thực tế, nhiều hiện tượng không tuân theo nguyên lý này. Ví dụ:
- Con lắc: lực hồi phục tỷ lệ với $$\sin\theta$$ chứ không phải $$\theta$$ (phi tuyến khi góc lệch lớn)
- Dịch bệnh: số người nhiễm tăng theo số người chưa nhiễm nhân với số người đã nhiễm (tích phi tuyến)
- Hóa học: tốc độ phản ứng phụ thuộc nồng độ các chất tham gia theo cách phức tạp

Điểm khác biệt cốt lõi: trong hệ tuyến tính, ta có thể viết nghiệm tường minh; trong hệ phi tuyến, **công thức nghiệm hiếm khi tồn tại** — nhưng ta vẫn có thể hiểu hệ qua hình học.

### Mặt phẳng pha là gì?

**Mặt phẳng pha** (phase plane) là không gian 2 chiều mà mỗi điểm biểu diễn **trạng thái hoàn chỉnh** của hệ tại một thời điểm. Với hệ 2 biến $$x$$ và $$y$$, mặt phẳng pha có:
- Trục hoành $$x$$: biến thứ nhất (ví dụ: vị trí, nồng độ, dân số)
- Trục tung $$y$$: biến thứ hai (ví dụ: vận tốc, tốc độ phản ứng, tốc độ tăng trưởng)

Mỗi điểm $$(x, y)$$ trên mặt phẳng cho biết **toàn bộ trạng thái** của hệ tại thời điểm đó — không chỉ một thành phần mà cả hai.

### Tại sao dùng mặt phẳng pha?

Thay vì vẽ đồ thị $$x(t)$$ và $$y(t)$$ riêng biệt theo thời gian (mỗi đồ thị là một sợi dây), ta vẽ **quỹ đạo** (trajectory) của cặp $$(x, y)$$ trên mặt phẳng. Điều này cho ta:
- **Bức tranh toàn cảnh**: thấy hệ đi về đâu, quay quanh đâu, có dao động không
- **Hiểu cấu trúc**: điểm cân bằng, quỹ đạo ổn định/unstable, dao động tự duy trì
- **Trực giác mạnh**: không cần công thức nghiệm vẫn hiểu hệ

Hãy tưởng tượng bạn quan sát một con cá voi bơi trong đại dương. Nếu chỉ nhìn đồ thị độ sâu theo thời gian, bạn không biết nó di chuyển theo đường nào. Nhưng nếu bạn có bản đồ vệ tinh cho thấy **toàn bộ quỹ đạo** đường đi của nó, bạn sẽ hiểu nó săn mồi như thế nào, có quay lại vùng cũ không — mặt phẳng pha chính là "bản đồ vệ tinh" cho hệ động lực.

### Hai cách nhìn một hệ

| Nhìn theo thời gian | Nhìn trên mặt phẳng pha |
|---|---|
| $$x(t)$$: sợi dây lên xuống | Quỹ đạo: đường cong trong mặt phẳng |
| $$y(t)$$: sợi dây lên xuống | Cùng đường cong đó |
| Hai đồ thị tách biệt | Một hình duy nhất |
| Cần nghiệm tường minh | Chỉ cần trường vector |

Ở các chương trước, nhiều bài toán có thể được giải bằng công thức rõ ràng. Nhưng trong **động lực học phi tuyến, công thức thường không còn là nhân vật chính**. Điều quan trọng hơn là **biết hệ đi về đâu, quay quanh đâu, có bị chặn không, có dao động bền hay không**. Những câu hỏi này mang tính hình học nhiều hơn là tính toán.

**Hệ tự trị** là nơi lý tưởng để bước vào thế giới đó. Vì vế phải không phụ thuộc tường minh vào thời gian, hình học của quỹ đạo chỉ phụ thuộc vào vị trí trong không gian trạng thái. Thay vì nhìn đồ thị của từng biến theo thời gian, ta nhìn trực tiếp **chuyển động của cả hệ trên mặt phẳng pha**. Đây là sự chuyển dịch tư duy lớn nhất của chương.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng mỗi điểm trong mặt phẳng là một trạng thái có thể của hệ. Tại mỗi điểm, hệ "muốn đi" theo một hướng nhất định. Nếu ta vẽ mũi tên chỉ hướng ấy ở mọi nơi, ta có một bản đồ động học. Quỹ đạo là đường mà hệ sẽ lần theo trên bản đồ đó.

### Cách nhìn hình ảnh

Với hệ
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
ta gắn tại điểm $$ (x,y) $$ vector
$$ \left(f(x,y),g(x,y)\right). $$
Các quỹ đạo luôn tiếp tuyến với trường vector này. Nullcline $$ \dot{x}=0 $$ là nơi chuyển động theo phương ngang biến mất, còn nullcline $$ \dot{y}=0 $$ là nơi chuyển động theo phương đứng biến mất. Chúng chia mặt phẳng thành các vùng có hướng chuyển động khác nhau.

### Cách nhìn hình thức

**Hệ tự trị** (autonomous system) là hệ phương trình vi phân mà vế phải **không phụ thuộc tường minh vào thời gian $$t$$**. Nghĩa là:
$$\dot{x} = f(x, y),\qquad \dot{y} = g(x, y)$$
Thay vì $$\dot{x} = f(x, y, t)$$ (hệ không tự trị), ta có các quy luật chỉ phụ thuộc vào **vị trí hiện tại** $$(x, y)$$ chứ không phải thời điểm.

**So sánh**:

| Hệ tự trị | Hệ không tự trị |
|---|---|
| $$\dot{x} = x(1-x)$$ | $$\dot{x} = x(1-x) + \sin(t)$$ |
| Không có $$t$$ ở vế phải | Có $$t$$ ở vế phải |
| Quỹ đạo chỉ phụ thuộc vị trí | Quỹ đạo phụ thuộc cả thời gian |
| Hình học pha cố định | Hình học pha thay đổi theo thời gian |

**Ý nghĩa của tính tự trị**:
- Quy luật chuyển động **không đổi** theo thời gian — hệ "nhớ" cùng một cách ở mọi thời điểm
- Nếu hệ bắt đầu ở trạng thái $$(x_0, y_0)$$ tại $$t_0$$ hoặc tại $$t_1$$, quỹ đạo sẽ **giống nhau** — chỉ khác thời điểm bắt đầu
- Điều này có nghĩa: hình học pha là **bất biến theo thời gian** — "đồng hồ tuyệt đối" không quan trọng, chỉ có "vị trí tương đối" quan trọng

**Ví dụ**:
- Hệ tự trị: $$\dot{x} = x(1-x),\ \dot{y} = y(x-1)$$ — quy luật chỉ phụ thuộc $$x, y$$
- Hệ không tự trị: $$\dot{x} = x(1-x) + \cos(t)$$ — quy luật thay đổi theo thời gian

Một hệ tự trị phẳng có dạng
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
trong đó $$ f,g $$ không phụ thuộc tường minh vào $$ t $$. Một quỹ đạo là ảnh của nghiệm
$$ t\mapsto (x(t),y(t)) $$
trong mặt phẳng trạng thái. Điểm cân bằng là điểm thỏa
$$ f(x_*,y_*)=0,\qquad g(x_*,y_*)=0. $$

## Những ngộ nhận thường gặp

- "Không có công thức nghiệm thì không hiểu được hệ." Sai. Mặt phẳng pha cho rất nhiều thông tin định tính mạnh.
- "Quỹ đạo trên mặt phẳng pha chính là đồ thị theo thời gian." Sai. Nó mô tả trạng thái so với trạng thái, không phải trạng thái theo thời gian.
- "Nullcline là quỹ đạo của hệ." Sai. Chúng chỉ là các đường nơi một thành phần vận tốc bằng 0.
- "Hệ tự trị nghĩa là hệ đơn giản." Không đúng. Hệ tự trị có thể rất giàu cấu trúc và rất phi tuyến.

## Tiến trình học tập đề xuất

### Bước 1: Xác định trường vector

Xem hệ "muốn đi" theo hướng nào tại từng điểm.

### Bước 2: Tìm điểm cân bằng và nullcline

Đây là bộ khung đầu tiên của mặt phẳng pha.

### Bước 3: Chia mặt phẳng thành các vùng dấu

Đọc chiều tăng giảm của từng biến.

### Bước 4: Phác họa quỹ đạo

Chú ý chúng phải tiếp tuyến với trường vector và tôn trọng nullcline.

### Các checkpoint

- Sinh viên có phân biệt được quỹ đạo với nullcline hay không.
- Sinh viên có đọc đúng dấu của $$ \dot{x},\dot{y} $$ trên các miền hay không.
- Sinh viên có hiểu vì sao hệ tự trị cho quỹ đạo "giống nhau" nếu dịch thời gian hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ tuyến tính đơn giản trong mặt phẳng pha

Xét
$$ \dot{x}=x,\qquad \dot{y}=-y. $$
Ta có nullcline
$$ x=0,\qquad y=0. $$
Nếu $$ x>0 $$ thì $$ \dot{x}>0 $$, còn $$ x<0 $$ thì $$ \dot{x}<0 $$. Tương tự, nếu $$ y>0 $$ thì $$ \dot{y}<0 $$, còn $$ y<0 $$ thì $$ \dot{y}>0 $$. Do đó quỹ đạo bị đẩy ra theo trục $$ x $$ nhưng hút vào theo trục $$ y $$. Đây là chân dung yên ngựa, nhưng điều quan trọng ở đây là thấy cách đọc trực tiếp từ dấu.

### Ví dụ 2: Nullcline và điểm cân bằng

Xét
$$ \dot{x}=x(1-x-y),\qquad \dot{y}=y(2-x-y). $$
Nullcline của $$ x $$ là
$$ x=0 \quad \text{hoặc} \quad x+y=1. $$
Nullcline của $$ y $$ là
$$ y=0 \quad \text{hoặc} \quad x+y=2. $$
Từ đây, sinh viên có thể chia mặt phẳng thành các vùng và đọc dấu của $$ \dot{x},\dot{y} $$ trước cả khi giải nghiệm.

### Ví dụ 3: Một quỹ đạo không cần công thức

Nếu trong một vùng ta biết
$$ \dot{x}>0,\qquad \dot{y}<0, $$
thì quỹ đạo đi về phía phải và phía dưới. Chỉ với thông tin này, ta đã có thể phác hướng chuyển động cục bộ của hệ mà không cần lời giải explicit.

### Ví dụ 4: Tính tự trị và dịch thời gian

Nếu một quỹ đạo là nghiệm của hệ tự trị, thì cùng quỹ đạo đó nhưng bắt đầu ở thời điểm khác vẫn là nghiệm. Điều này giải thích vì sao hình học pha của hệ tự trị không phụ thuộc vào "đồng hồ tuyệt đối", mà chỉ phụ thuộc vào trạng thái.

## Câu hỏi khái niệm

1. Vì sao mặt phẳng pha cho trực giác mạnh hơn đồ thị theo thời gian trong hệ hai chiều?
2. Vai trò của nullcline trong việc phác họa quỹ đạo là gì?
3. Vì sao tính tự trị làm cho quỹ đạo được hiểu như hình học trạng thái chứ không phải như lịch biểu thời gian?

## Bài toán ứng dụng

1. Trong sinh thái học, hai quần thể cùng tiến hóa. Hãy giải thích vì sao mặt phẳng pha phù hợp hơn việc chỉ vẽ riêng từng đồ thị dân số theo thời gian.
2. Trong hóa học, hai nồng độ tương tác qua phản ứng. Hãy diễn giải trường vector như bản đồ của hướng thay đổi phản ứng.
3. Trong điều khiển, vì sao việc biết các vùng hệ đi lên hay đi xuống trong không gian trạng thái lại quan trọng?

## Chiến lược giảng dạy tương tác

- Cho sinh viên nhìn một trường vector và đoán đường đi của quỹ đạo trước khi được cho hệ phương trình.
- Tổ chức hoạt động "đọc dấu" trên các miền được chia bởi nullcline.
- Yêu cầu sinh viên so sánh cùng một nghiệm nhìn theo đồ thị thời gian và nhìn trong mặt phẳng pha.
- Khuyến khích sinh viên dùng lời mô tả hướng chuyển động trước khi vẽ hình chi tiết.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên yếu tập trung vào ba bước cố định: tìm nullcline, xét dấu trên các vùng, rồi vẽ vài mũi tên mẫu. Cách làm từng bước này giúp các em không bị choáng bởi mặt phẳng pha.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi giải thích vì sao quỹ đạo của hệ tự trị không thể tự cắt nhau, hoặc phân tích thêm vùng bất biến dương trong các mô hình sinh học.

## Tóm tắt dễ nhớ

Mặt phẳng pha là bản đồ động học của hệ tự trị hai chiều. Muốn đọc hệ, hãy tìm điểm cân bằng, vẽ nullcline, xét dấu của $$ \dot{x},\dot{y} $$ và nhìn quỹ đạo như những đường tiếp tuyến với trường vector. Không cần công thức nghiệm mới hiểu được hệ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Con lắc có ma sát
- Bài toán: Muốn hiểu vật dao động có quay về vị trí cân bằng hay còn dao động mãi.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega.
$$
- Giả thiết và giới hạn: Bỏ qua nhiễu ngoài và giả sử lực cản tuyến tính theo vận tốc góc.
- Diễn giải: Mặt phẳng pha cho thấy ngay quỹ đạo xoắn vào cân bằng hay chạy vòng qua nhiều chu kỳ.

#### Tương tác hai quần thể
- Bài toán: Hai loài cùng biến đổi, một loài tăng làm loài kia giảm.
- Mô hình:
$$ \dot{x}=x(1-y),\qquad
\dot{y}=y(x-1). $$
- Giả thiết và giới hạn: Mô hình hóa rất lý tưởng, chưa có sức chứa môi trường hay trễ thời gian.
- Diễn giải: Trường vector và nullcline cho ta hình học định tính trước cả khi tìm nghiệm.

### 2. Trực giác bổ sung và các kết nối

Mặt phẳng pha là bước chuyển từ "giải ra công thức" sang "đọc cấu trúc quỹ đạo". Nullcline không phải là quỹ đạo, mà là nơi một thành phần vận tốc bằng $$ 0 $$. Một bẫy phổ biến là lẫn lộn đồ thị theo thời gian với quỹ đạo trạng thái. Bài này nối trực tiếp với Chương 4: thay vì chỉ phân loại hệ tuyến tính, ta bắt đầu dùng hình học để hiểu cả hệ phi tuyến.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, z):
    x, y = z
    return [x * (1 - y), y * (x - 1)]

x = np.linspace(0.1, 2.5, 20)
y = np.linspace(0.1, 2.5, 20)
X, Y = np.meshgrid(x, y)
U = X * (1 - Y)
V = Y * (X - 1)
N = np.sqrt(U**2 + V**2) + 1e-9

plt.quiver(X, Y, U / N, V / N, color="teal", alpha=0.7)
for z0 in [(0.5, 0.5), (1.8, 0.6), (0.8, 1.8)]:
    sol = solve_ivp(f, [0, 20], z0, max_step=0.05)
    plt.plot(sol.y[0], sol.y[1], lw=2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Mặt phẳng pha của hệ tự trị")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: autonomous system phase plane nullclines
- search: damped pendulum phase portrait
- search: nonlinear vector field trajectories

### 5. Bài toán mẫu có bối cảnh thực

Xét hệ
$$ \dot{x}=x(1-y),\qquad
\dot{y}=y(x-1). $$
Nullcline là
$$ x=0,\ y=1,\ y=0,\ x=1. $$
Trong miền $$ x>1,\ y<1 $$ ta có $$ \dot{x}>0,\ \dot{y}>0 $$ nên quỹ đạo đi lên và sang phải. Chỉ từ dấu của trường vector, ta đã phác được động học cục bộ mà không cần nghiệm tường minh.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào trường vector, nullcline, điểm cân bằng và cách đọc hướng chuyển động.

**Bậc sau đại học.** Nhấn mạnh dòng chảy, tập bất biến, cấu trúc tôpô của quỹ đạo và tính duy nhất của nghiệm.

## Tài liệu tham khảo

- Strogatz, Chương 5-6: trực giác rất mạnh về hệ tự trị và mặt phẳng pha.
- Arnold, Chương 4: làm rõ góc nhìn hình học của trường vector và dòng chảy.
