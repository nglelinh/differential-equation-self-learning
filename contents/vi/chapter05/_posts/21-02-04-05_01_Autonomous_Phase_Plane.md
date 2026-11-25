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

Hầu hết các phương trình vi phân phi tuyến trong tự nhiên—từ con lắc biên độ lớn đến hệ sinh thái—đều **không có nghiệm công thức sơ cấp**. Thay vì cố viết $x(t)$ dưới dạng biểu thức tường minh, Henri Poincaré đã mở ra một góc nhìn thiên tài: vẽ trực tiếp quỹ đạo chuyển động $(x(t), y(t))$ trên **mặt phẳng pha (phase plane)** để đọc trọn vẹn số phận của hệ chỉ bằng hình học!

## Kiến thức cần nhớ: Bốn viên gạch của Hệ Tự trị & Mặt phẳng Pha

1. **Hệ tự trị (Autonomous System)**:
   Hệ $\dot{x} = f(x, y),\; \dot{y} = g(x, y)$ không chứa biến thời gian $t$ tường minh ở vế phải; quy luật vận tốc tại mỗi điểm $(x, y)$ là bất biến theo thời gian.
2. **Trường vectơ (Vector Field) & Đường quỹ đạo (Trajectories)**:
   Tại mỗi điểm $(x, y)$, vectơ $(f(x, y), g(x, y))$ chỉ hướng tiếp tuyến và tốc độ di chuyển. Theo định lý tồn tại–duy nhất, **hai quỹ đạo khác nhau của hệ tự trị trơn không bao giờ cắt nhau** trên mặt phẳng pha!
3. **Đường đẳng khuynh không (Nullclines)**:
   Đường $x$-nullcline ($f(x, y) = 0$) có trường vectơ thẳng đứng; đường $y$-nullcline ($g(x, y) = 0$) có trường vectơ nằm ngang. Giao điểm của chúng chính là các **điểm cân bằng (equilibria)**.
4. **Bức chân dung pha (Phase Portrait)**:
   Bản đồ hình học tổng hợp các điểm cân bằng, nullclines và quỹ đạo đại diện cho phép dự đoán hành vi dài hạn của mọi điều kiện ban đầu.

## Mục tiêu

Bài học này mở đầu chương **động lực học phi tuyến**, chuyển trọng tâm từ việc tìm công thức nghiệm sang phân tích hình học của quỹ đạo. Sinh viên sẽ nắm được khái niệm hệ tự trị hai chiều, trường vector, đường nullcline và quỹ đạo trên mặt phẳng pha, qua đó hiểu vì sao mặt phẳng pha là công cụ trung tâm để khảo sát hệ phi tuyến ngay cả khi không có nghiệm tường minh.

## Kiến thức nền

Sinh viên nên nắm vững hệ phương trình vi phân hai chiều, hệ tuyến tính từ chương trước và ý nghĩa của điểm cân bằng. Trực giác về đường pha một chiều cũng rất hữu ích vì mặt phẳng pha là sự mở rộng tự nhiên từ đó.

## Dẫn nhập

![Mặt phẳng pha của hệ tự trị hai chiều]({{ site.imgurl }}/chapter_img/chapter05/01_autonomous_phase_plane.svg)

### Động lực học phi tuyến là gì?

**Động lực học phi tuyến** (nonlinear dynamics) nghiên cứu cách các hệ thống biến đổi theo thời gian khi các thành phần tương tác **không theo quan hệ tỷ lệ thuận**. Trong hệ tuyến tính, khi đầu vào tăng gấp đôi thì đầu ra cũng tăng gấp đôi; tuy nhiên, nhiều hiện tượng thực tế không tuân theo tính chất này:
- Con lắc: lực hồi phục tỷ lệ với $$\sin\theta$$ thay vì $$\theta$$ (phi tuyến khi góc lệch lớn).
- Dịch bệnh: tốc độ lây nhiễm tỷ lệ với tích giữa số người chưa nhiễm và số người đã nhiễm (tích phi tuyến).
- Hóa học: tốc độ phản ứng phụ thuộc vào nồng độ các chất tham gia theo những hàm phi tuyến phức tạp.

Điểm khác biệt cốt lõi là: với hệ tuyến tính, ta thường viết được nghiệm tường minh; còn với hệ phi tuyến, **công thức nghiệm đóng hiếm khi tồn tại**, nhưng ta vẫn có thể hiểu hành vi của hệ thông qua hình học.

### Mặt phẳng pha là gì?

**Mặt phẳng pha** (phase plane) là không gian hai chiều mà mỗi điểm biểu diễn **trạng thái đầy đủ** của hệ tại một thời điểm. Với hệ hai biến $$x$$ và $$y$$, mặt phẳng pha gồm:
- Trục hoành $$x$$: biến trạng thái thứ nhất (ví dụ: vị trí, nồng độ, dân số).
- Trục tung $$y$$: biến trạng thái thứ hai (ví dụ: vận tốc, tốc độ phản ứng, tốc độ tăng trưởng).

Mỗi điểm $$(x, y)$$ trên mặt phẳng xác định đồng thời cả hai thành phần trạng thái của hệ tại thời điểm đang xét.

### Tại sao dùng mặt phẳng pha?

Thay vì vẽ riêng hai đồ thị $$x(t)$$ và $$y(t)$$ theo thời gian, ta vẽ **quỹ đạo** (trajectory) của cặp $$(x, y)$$ trực tiếp trên mặt phẳng. Cách biểu diễn này mang lại:
- **Bức tranh toàn cảnh**: cho thấy hệ tiến về đâu, quay quanh vùng nào và có dao động hay không.
- **Cấu trúc động lực**: làm lộ rõ điểm cân bằng, quỹ đạo ổn định hay không ổn định và dao động tự duy trì.
- **Trực giác hình học**: giúp phân tích hệ ngay cả khi không tìm được công thức nghiệm.

Hãy hình dung việc quan sát một con cá voi bơi trong đại dương. Nếu chỉ xem đồ thị độ sâu theo thời gian, ta không biết đường di chuyển của nó trong không gian. Ngược lại, một bản đồ vệ tinh cho thấy **toàn bộ quỹ đạo** sẽ giúp nhận ra lộ trình săn mồi và việc nó có quay lại vùng cũ hay không. Mặt phẳng pha đóng vai trò tương tự như tấm bản đồ đó đối với hệ động lực.

### Hai cách nhìn một hệ

| Nhìn theo thời gian | Nhìn trên mặt phẳng pha |
|---|---|
| $$x(t)$$: đường cong biến thiên theo $$t$$ | Quỹ đạo: đường cong trong mặt phẳng trạng thái |
| $$y(t)$$: đường cong biến thiên theo $$t$$ | Cùng đường cong đó |
| Hai đồ thị tách biệt | Một hình biểu diễn duy nhất |
| Cần nghiệm tường minh | Chỉ cần trường vector |

Ở các chương trước, nhiều bài toán có thể giải bằng công thức rõ ràng. Tuy nhiên, trong **động lực học phi tuyến, công thức nghiệm không còn là trọng tâm**. Điều quan trọng hơn là xác định **hệ tiến về đâu, quay quanh đâu, có bị chặn không và có dao động bền vững hay không**. Những câu hỏi này thiên về hình học hơn là tính toán đại số.

**Hệ tự trị** là điểm khởi đầu phù hợp cho hướng tiếp cận này. Do vế phải không phụ thuộc tường minh vào thời gian, hình học quỹ đạo chỉ phụ thuộc vào vị trí trong không gian trạng thái. Thay vì khảo sát từng biến riêng lẻ theo thời gian, ta quan sát trực tiếp chuyển động của cả hệ trên mặt phẳng pha.

### Giải thích: Vẽ bằng tay Nullclines và xác định hướng quỹ đạo cho hệ con lắc tuyến tính $\dot{x} = y,\; \dot{y} = -x$

1. **Tìm Nullclines**:
   - $x$-nullcline: $\dot{x} = y = 0$ (trục hoành $Ox$). Tại $x > 0, y = 0$ ta có $\dot{y} = -x < 0$ (mũi tên đi thẳng **xuống**); tại $x < 0, y = 0$ ta có $\dot{y} > 0$ (đi **lên**).
   - $y$-nullcline: $\dot{y} = -x = 0$ (trục tung $Oy$). Tại $y > 0, x = 0$ ta có $\dot{x} = y > 0$ (đi sang **phải**); tại $y < 0, x = 0$ ta có $\dot{x} < 0$ (đi sang **trái**).
2. **Tìm điểm cân bằng**: Giao của $y = 0$ và $x = 0$ là gốc $(0, 0)$.
3. **Tìm phương trình quỹ đạo bằng cách khử $dt$**:
   $$\frac{dy}{dx} = \frac{-x}{y} \implies y\,dy + x\,dx = 0 \implies x^2 + y^2 = C.$$
   Mọi quỹ đạo là các **đường tròn đồng tâm** quanh gốc, quay theo **chiều kim đồng hồ** (phù hợp với mũi tên phải–xuống–trái–lên vừa xác định!).

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy xem mỗi điểm trong mặt phẳng là một trạng thái có thể của hệ. Tại mỗi điểm, hệ có xu hướng dịch chuyển theo một hướng xác định. Khi vẽ các mũi tên chỉ hướng tại mọi điểm, ta thu được một bản đồ động học, và quỹ đạo chính là đường đi men theo các mũi tên đó.

### Cách nhìn hình ảnh

Với hệ
$$ \dot{x}=f(x,y),\qquad \dot{y}=g(x,y), $$
ta gắn tại mỗi điểm $$ (x,y) $$ vector vận tốc
$$ \left(f(x,y),g(x,y)\right). $$
Các quỹ đạo luôn tiếp tuyến với trường vector này. Đường nullcline $$ \dot{x}=0 $$ là tập hợp các điểm mà chuyển động theo phương ngang triệt tiêu, còn đường nullcline $$ \dot{y}=0 $$ là nơi chuyển động theo phương đứng triệt tiêu. Các đường nullcline chia mặt phẳng thành những miền có chiều chuyển động khác nhau.

### Cách nhìn hình thức

**Hệ tự trị** (autonomous system) là hệ phương trình vi phân có vế phải **không phụ thuộc tường minh vào thời gian $$t$$**:
$$\dot{x} = f(x, y),\qquad \dot{y} = g(x, y).$$
Khác với hệ không tự trị $$\dot{x} = f(x, y, t)$$, quy luật biến thiên của hệ tự trị chỉ phụ thuộc vào **trạng thái hiện tại** $$(x, y)$$, không phụ thuộc vào thời điểm.

**So sánh:**

| Hệ tự trị | Hệ không tự trị |
|---|---|
| $$\dot{x} = x(1-x)$$ | $$\dot{x} = x(1-x) + \sin(t)$$ |
| Không chứa $$t$$ ở vế phải | Có chứa $$t$$ ở vế phải |
| Quỹ đạo chỉ phụ thuộc vị trí | Quỹ đạo phụ thuộc cả thời gian |
| Hình học pha cố định | Hình học pha thay đổi theo thời gian |

**Ý nghĩa của tính tự trị:**
- Quy luật chuyển động không đổi theo thời gian.
- Nếu hệ xuất phát tại trạng thái $$(x_0, y_0)$$ ở thời điểm $$t_0$$ hay $$t_1$$, đường quỹ đạo thu được vẫn giống hệt nhau, chỉ dịch chuyển theo thời gian.
- Hình học pha bất biến theo phép tịnh tiến thời gian: mốc thời gian tuyệt đối không làm thay đổi dạng quỹ đạo.

**Ví dụ:**
- Hệ tự trị: $$\dot{x} = x(1-x),\ \dot{y} = y(x-1)$$ — vế phải chỉ phụ thuộc vào $$x, y$$.
- Hệ không tự trị: $$\dot{x} = x(1-x) + \cos(t)$$ — quy luật thay đổi tường minh theo thời gian.

Về mặt hình thức, một **quỹ đạo** là ảnh của nghiệm
$$ t\mapsto (x(t),y(t)) $$
trong mặt phẳng trạng thái. **Điểm cân bằng** là điểm $$(x_*, y_*)$$ thỏa mãn đồng thời
$$ f(x_*,y_*)=0,\qquad g(x_*,y_*)=0. $$

## Những ngộ nhận thường gặp

- "Không có công thức nghiệm thì không thể hiểu được hệ." Sai. Mặt phẳng pha cung cấp nhiều thông tin định tính quan trọng về hành vi của hệ.
- "Quỹ đạo trên mặt phẳng pha chính là đồ thị theo thời gian." Sai. Quỹ đạo thể hiện mối liên hệ giữa các biến trạng thái với nhau, không phải biến thiên của từng biến theo thời gian.
- "Nullcline là quỹ đạo của hệ." Sai. Nullcline chỉ là đường mà tại đó một thành phần vận tốc bằng 0.
- "Hệ tự trị là hệ đơn giản." Không đúng. Hệ tự trị vẫn có thể rất phi tuyến và có cấu trúc động lực phức tạp.

## Tiến trình học tập đề xuất

### Bước 1: Xác định trường vector

Quan sát hướng dịch chuyển của hệ tại từng vị trí trên mặt phẳng.

### Bước 2: Tìm điểm cân bằng và nullcline

Xây dựng bộ khung cơ bản cho mặt phẳng pha.

### Bước 3: Chia mặt phẳng thành các miền dấu

Xác định chiều tăng, giảm của từng biến trên mỗi miền.

### Bước 4: Phác họa quỹ đạo

Vẽ các đường cong tiếp tuyến với trường vector và cắt các đường nullcline đúng phương (đứng hoặc ngang).

### Các điểm kiểm tra

- Sinh viên có phân biệt được quỹ đạo với đường nullcline hay không.
- Sinh viên có xác định đúng dấu của $$ \dot{x},\dot{y} $$ trên các miền hay không.
- Sinh viên có giải thích được vì sao phép dịch thời gian không làm thay đổi quỹ đạo của hệ tự trị hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ tuyến tính đơn giản trên mặt phẳng pha

Xét hệ
$$ \dot{x}=x,\qquad \dot{y}=-y. $$
Các đường nullcline là
$$ x=0,\qquad y=0. $$
Khi $$ x>0 $$ thì $$ \dot{x}>0 $$, còn khi $$ x<0 $$ thì $$ \dot{x}<0 $$. Tương tự, khi $$ y>0 $$ thì $$ \dot{y}<0 $$, còn khi $$ y<0 $$ thì $$ \dot{y}>0 $$. Do đó, quỹ đạo bị đẩy ra dọc theo trục $$ x $$ và hút vào dọc theo trục $$ y $$. Đây là chân dung điểm yên ngựa, cho thấy ta có thể đọc trực tiếp dạng chuyển động chỉ từ việc xét dấu.

### Ví dụ 2: Nullcline và điểm cân bằng

Xét hệ
$$ \dot{x}=x(1-x-y),\qquad \dot{y}=y(2-x-y). $$
Nullcline theo $$ x $$ là
$$ x=0 \quad \text{hoặc} \quad x+y=1. $$
Nullcline theo $$ y $$ là
$$ y=0 \quad \text{hoặc} \quad x+y=2. $$
Từ các đường này, sinh viên có thể chia mặt phẳng thành các miền và xác định dấu của $$ \dot{x},\dot{y} $$ mà chưa cần giải hệ.

### Ví dụ 3: Phác họa quỹ đạo không cần công thức nghiệm

Nếu trong một miền ta có
$$ \dot{x}>0,\qquad \dot{y}<0, $$
thì quỹ đạo sẽ đi sang phải và xuống dưới. Chỉ từ thông tin về dấu này, ta đã xác định được hướng chuyển động cục bộ mà không cần nghiệm tường minh.

### Ví dụ 4: Tính tự trị và phép dịch thời gian

Nếu một đường cong là quỹ đạo nghiệm của hệ tự trị, thì cùng đường cong đó nhưng xuất phát tại thời điểm khác vẫn là một nghiệm. Điều này giải thích vì sao hình học pha của hệ tự trị không phụ thuộc vào mốc thời gian tuyệt đối mà chỉ phụ thuộc vào trạng thái.

## Câu hỏi khái niệm

1. Vì sao mặt phẳng pha mang lại trực giác tốt hơn đồ thị theo thời gian đối với hệ hai chiều?
2. Đường nullcline đóng vai trò gì trong việc phác họa quỹ đạo?
3. Vì sao tính tự trị cho phép xem quỹ đạo là đối tượng hình học trong không gian trạng thái thay vì một biểu đồ phụ thuộc mốc thời gian?

## Bài toán ứng dụng

1. Trong sinh thái học, khi hai quần thể cùng biến đổi, hãy giải thích vì sao mặt phẳng pha phù hợp hơn việc chỉ vẽ riêng hai đồ thị dân số theo thời gian.
2. Trong hóa học, hai nồng độ tương tác qua phản ứng. Hãy diễn giải trường vector như bản đồ chỉ hướng tiến triển của phản ứng.
3. Trong lý thuyết điều khiển, vì sao việc xác định các miền tăng giảm trong không gian trạng thái lại có ý nghĩa thực tiễn?

## Chiến lược giảng dạy tương tác

- Cho sinh viên quan sát một trường vector và dự đoán dạng quỹ đạo trước khi cung cấp hệ phương trình.
- Tổ chức hoạt động xét dấu trên các miền được phân chia bởi các đường nullcline.
- Yêu cầu sinh viên đối chiếu cùng một nghiệm khi biểu diễn trên đồ thị thời gian và trên mặt phẳng pha.
- Khuyến khích sinh viên mô tả bằng lời chiều chuyển động trước khi vẽ hình chi tiết.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên hướng dẫn sinh viên tập trung theo quy trình ba bước cố định: tìm nullcline, xét dấu trên từng miền, sau đó vẽ một số mũi tên mẫu. Cách làm tuần tự này giúp tránh lúng túng khi tiếp cận mặt phẳng pha.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên giải thích vì sao hai quỹ đạo khác nhau của hệ tự trị không thể cắt nhau, hoặc phân tích miền bất biến dương trong các mô hình sinh học.

## Tóm tắt dễ nhớ

Mặt phẳng pha là bản đồ động học của hệ tự trị hai chiều. Để phân tích hệ, ta tìm điểm cân bằng, vẽ các đường nullcline, xét dấu của $$ \dot{x},\dot{y} $$ và phác họa quỹ đạo sao cho luôn tiếp tuyến với trường vector. Ta vẫn hiểu được hành vi định tính của hệ mà không cần công thức nghiệm đóng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Con lắc có ma sát
- Bài toán: Xác định xem vật dao động sẽ dừng về vị trí cân bằng hay tiếp tục dao động mãi.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega.
$$
- Giả thiết và giới hạn: Bỏ qua nhiễu ngoài và giả sử lực cản tỷ lệ tuyến tính với vận tốc góc.
- Diễn giải: Mặt phẳng pha cho thấy trực quan quỹ đạo xoắn dần về vị trí cân bằng hay quay qua nhiều chu kỳ.

#### Tương tác hai quần thể
- Bài toán: Hai loài cùng biến đổi, sự gia tăng của một loài làm suy giảm loài kia.
- Mô hình:
$$ \dot{x}=x(1-y),\qquad
\dot{y}=y(x-1). $$
- Giả thiết và giới hạn: Mô hình lý tưởng hóa, chưa tính đến sức chứa môi trường hay độ trễ thời gian.
- Diễn giải: Trường vector và các đường nullcline thể hiện cấu trúc định tính trước khi giải nghiệm.

### 2. Trực giác bổ sung và các kết nối

Mặt phẳng pha đánh dấu bước chuyển từ việc tìm công thức nghiệm sang phân tích cấu trúc quỹ đạo. Cần phân biệt rõ: nullcline không phải là quỹ đạo mà là tập hợp điểm có một thành phần vận tốc bằng $$ 0 $$, và quỹ đạo trạng thái không phải là đồ thị theo thời gian. Bài học này nối tiếp trực tiếp Chương 4: thay vì dừng ở việc phân loại hệ tuyến tính, ta bắt đầu vận dụng hình học để khảo sát hệ phi tuyến.

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
Các đường nullcline là
$$ x=0,\ y=1,\ y=0,\ x=1. $$
Trong miền $$ x>1,\ y<1 $$, ta có $$ \dot{x}>0,\ \dot{y}>0 $$ nên quỹ đạo đi sang phải và lên trên. Chỉ cần xét dấu của trường vector, ta đã phác họa được xu hướng động học cục bộ mà không cần nghiệm tường minh.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào trường vector, đường nullcline, điểm cân bằng và cách đọc chiều chuyển động.

**Bậc sau đại học.** Nhấn mạnh khái niệm dòng chảy (flow), tập bất biến, cấu trúc tôpô của quỹ đạo và tính duy nhất của nghiệm.

## Video tham khảo

- Xem trước: [MAE5790-1 Course introduction and overview](https://www.youtube.com/watch?v=ycJEoqmQvwg) — Cornell MAE, tiếng Anh. Strogatz mở đầu khóa học với cách tiếp cận không gian pha thay cho công thức nghiệm.
- [MAE5790-2 One dimensional Systems](https://www.youtube.com/watch?v=YNIm2Op7UPg) — Cornell MAE, tiếng Anh. Đường pha một chiều là bước khởi đầu trước khi chuyển sang mặt phẳng pha.
- [Drawing Phase Portraits for Nonlinear Systems](https://www.youtube.com/watch?v=vBwyD4JJlSs) — Steve Brunton, tiếng Anh. Hướng dẫn phác họa chân dung pha phi tuyến từ trường vector.

## Tài liệu tham khảo

- Strogatz, Chương 5–6: trình bày trực quan về hệ tự trị và mặt phẳng pha.
- Arnold, Chương 4: làm rõ góc nhìn hình học của trường vector và dòng chảy.
