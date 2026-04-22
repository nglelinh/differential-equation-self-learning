---
layout: post
title: "05-02 Điểm Cân bằng và Tuyến tính hóa"
chapter: '05'
order: 2
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên xác định điểm cân bằng của hệ phi tuyến, xây dựng ma trận Jacobian, dùng tuyến tính hóa để dự đoán động học cục bộ gần cân bằng, và hiểu ý nghĩa của việc hệ phi tuyến "trông giống" hệ tuyến tính ở lân cận điểm cân bằng hyperbolic.

## Kiến thức nền

Sinh viên cần nắm hệ tuyến tính hai chiều, trị riêng của ma trận và mặt phẳng pha. Một ít kiến thức về đạo hàm riêng là bắt buộc vì Jacobian là trái tim của bài học.

## Dẫn nhập

![Tuyến tính hóa gần điểm cân bằng]({{ site.imgurl }}/chapter_img/chapter05/02_equilibria_linearization.svg)

Hệ phi tuyến thường rất khó giải trực tiếp. Nhưng trong nhiều ứng dụng, ta không cần biết mọi quỹ đạo ở khắp nơi. Ta chỉ cần hiểu điều gì xảy ra gần một **trạng thái quan trọng, như trạng thái cân bằng sinh học, vị trí đứng yên của hệ cơ học hay điểm vận hành của một mạch điện**. Khi đó, tuyến tính hóa trở thành công cụ mạnh nhất và tự nhiên nhất.

Ý tưởng của tuyến tính hóa rất đơn giản nhưng sâu sắc: nếu nhìn đủ gần một điểm cân bằng, phần bậc nhất của khai triển Taylor thường chi phối, còn phần phi tuyến bậc cao chỉ là hiệu chỉnh nhỏ. Vì thế, ma trận Jacobian đóng vai trò như "bản sao tuyến tính cục bộ" của toàn bộ hệ phi tuyến.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Giống như một đường cong trơn trông gần như thẳng nếu ta zoom đủ gần, một hệ phi tuyến trông gần như tuyến tính nếu ta chỉ quan sát quanh một điểm cân bằng. Jacobian là "đường tiếp tuyến ma trận" của hệ.

### Cách nhìn hình ảnh

Nếu quỹ đạo gần cân bằng trông như yên ngựa, nút hay tiêu điểm, đó thường là vì Jacobian tại cân bằng có cùng kiểu chân dung pha. Tuyến tính hóa cho ta biết hệ đang phóng to một trong những kiểu hình học tuyến tính nào ở quy mô rất nhỏ.

### Cách nhìn hình thức

**Điểm cân bằng** (equilibrium point) là trạng thái mà tại đó hệ **đứng yên vĩnh viễn** — **nếu hệ bắt đầu ở đó, nó sẽ không bao giờ rời đi**. Về mặt toán học, với hệ:
$$\dot{x}=f(x,y),\qquad \dot{y}=g(x,y),$$
điểm cân bằng $$(x_*,y_*)$$ thỏa mãn đồng thời:
$$f(x_*,y_*)=0,\qquad g(x_*,\ y_*)=0.$$

**Ý nghĩa vật lý**:
- Trong con lắc: vị trí thấp nhất — con lắc sẽ đứng yên nếu thả không vận tốc
- Trong mạch điện: trạng thái dòng điện = 0, điện tích không đổi
- Trong sinh thái: trạng thái quần thể cân bằng — không tăng không giảm
- Trong phản ứng hóa: trạng thái cân bằng hóa học

**Tại sao điểm cân bằng quan trọng?**
- Cho biết hệ có thể "nghỉ" ở đâu
- Xung quanh điểm cân bằng là nơi **ổn định** (hệ trở về) hay **không ổn định** (hệ đi xa)
- Cấu trúc pha gần cân bằng quyết định hành vi long-term của hệ

**Ví dụ tìm điểm cân bằng**:

Xét hệ: $$\dot{x}=x(1-y),\ \dot{y}=y(x-1)$$

Giải $$f=0, g=0$$:
- $$x(1-y)=0 \Rightarrow x=0$$ hoặc $$y=1$$
- $$y(x-1)=0 \Rightarrow y=0$$ hoặc $$x=1$$

Kết hợp: $$(0,0)$$, $$(0,1)$$, $$(1,0)$$, $$(1,1)$$. Nhưng chỉ có $$(0,0)$$ và $$(1,1)$$ thỏa cả hai phương trình. Kiểm tra:
- Tại $$(0,0)$$: $$\dot{x}=0(1-0)=0,\ \dot{y}=0(0-1)=0$$ ✓
- Tại $$(1,1)$$: $$\dot{x}=1(1-1)=0,\ \dot{y}=1(1-1)=0$$ ✓

Hai điểm cân bằng là $$(0,0)$$ và $$(1,1)$$.

### Tuyến tính hóa là gì?

**Tuyến tính hóa** (linearization) là quá trình **xấp xỉ một hệ phi tuyến bằng một hệ tuyến tính** gần một điểm quan trọng (thường là điểm cân bằng).

**Ý tưởng**: Giống như khi nhìn đủ gần một đường cong, nó trông như một đường thẳng — khi nhìn đủ gần một điểm cân bằng, hệ phi tuyến trông như hệ tuyến tính.

**So sánh**:

| Hệ phi tuyến | Hệ tuyến tính hóa |
|---|---|
| Khó giải tường minh | Giải được dễ dàng |
| Nghiệm phức tạp | Nghiệm là tổ hợp hàm mũ |
| Quỹ đạo bất kỳ | Quỹ đạo là các đường cơ bản |

### Công thức toán học

Cho hệ: $$\dot{x}=f(x,y),\ \dot{y}=g(x,y)$$

**Bước 1**: Đặt biến lệch $$u = x - x_*, v = y - y_*$$ (khoảng cách đến cân bằng)

**Bước 2**: Khai triển Taylor bậc nhất:
$$f(x_*,y_* + v) \approx f(x_*,y_*) + \frac{\partial f}{\partial x}\Big|_* u + \frac{\partial f}{\partial y}\Big|_* v$$

Vì tại cân bằng: $$f(x_*,y_*) = 0, g(x_*,y_*) = 0$$

**Bước 3**: Ta được hệ tuyến tính:
$$\begin{pmatrix}\dot{u}\\\dot{v}\end{pmatrix} = J(x_*,y_*) \begin{pmatrix}u\\v\end{pmatrix}$$

trong đó **ma trận Jacobian**:
$$J(x_*,y_*) = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}\\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y} \end{pmatrix}_{(x_*,y_*)}.$$

### Ví dụ tuyến tính hóa

Xét hệ: $$\dot{x}=x(1-y),\ \dot{y}=y(x-1)$$

Tại điểm cân bằng $$(1,1)$$:

Tính các đạo hàm riêng:
- $$\frac{\partial f}{\partial x} = 1-y, \quad \frac{\partial f}{\partial y} = -x$$
- $$\frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = x-1$$

Thay $$(1,1)$$ vào:
$$J(1,1) = \begin{pmatrix} 1-1 & -1\\ 1 & 1-1 \end{pmatrix} = \begin{pmatrix} 0 & -1\\ 1 & 0 \end{pmatrix}.$$

Hệ tuyến tính hóa:
$$\begin{pmatrix}\dot{u}\\\dot{v}\end{pmatrix} = \begin{pmatrix} 0 & -1\\ 1 & 0 \end{pmatrix} \begin{pmatrix}u\\v\end{pmatrix}.$$

Tính trị riêng: $$\lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i$$ — đây là **tâm trung tâm** (center), quỹ đạo là các vòng tròn quanh điểm cân bằng.

### Khi nào tuyến tính hóa đáng tin?

Tuyến tính hóa cho kết quả **tốt** khi:
- Điểm cân bằng là **hyperbolic**: tất cả trị riêng của Jacobian có phần thực **khác 0**
- Ta chỉ quan tâm **gần** điểm cân bằng

Tuyến tính hóa **không đáng tin** khi:
- Trị riêng có phần thực **gần 0** (điểm cận biên)
- Trị riêng nằm trên **trục ảo** (center) — hệ phi tuyến có thể khác biệt
- Ta muốn hiểu hành vi **toàn cục** (xa cân bằng)

## Những ngộ nhận thường gặp

- "Tuyến tính hóa cho ta toàn bộ hành vi của hệ." Sai. Nó chỉ đáng tin gần điểm cân bằng.
- "Chỉ cần nhìn Jacobian là xong cho mọi cân bằng." Không đúng khi trị riêng nằm trên trục ảo hoặc có phần thực bằng 0.
- "Nếu hệ phi tuyến thì xấp xỉ tuyến tính chắc sẽ kém." Không hẳn. Gần cân bằng hyperbolic, nó thường cực kỳ hữu ích.
- "Điểm cân bằng là nơi mọi thứ đứng yên mãi mãi nên không thú vị." Sai. Cấu trúc xung quanh cân bằng chính là nơi ổn định và mất ổn định lộ ra.

## Tiến trình học tập đề xuất

### Bước 1: Tìm điểm cân bằng

Giải đồng thời
$$ f=0,\qquad g=0. $$

### Bước 2: Tính Jacobian

Đạo hàm riêng và thay vào cân bằng.

### Bước 3: Phân tích trị riêng của Jacobian

Đọc kiểu điểm cân bằng tuyến tính hóa.

### Bước 4: Diễn giải cục bộ cho hệ phi tuyến

Nhấn mạnh giới hạn của kết luận.

### Các checkpoint

- Sinh viên có tìm đúng các cân bằng hay không.
- Sinh viên có tính đúng Jacobian tại từng cân bằng hay không.
- Sinh viên có biết khi nào tuyến tính hóa đủ mạnh và khi nào chưa kết luận được không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Một hệ phi tuyến đơn giản

Xét
$$ \dot{x}=x-y-x^3,\qquad \dot{y}=x+y-y^3. $$
Tại gốc, Jacobian là
$$
J(0,0)=
\begin{pmatrix}
1 & -1\\
1 & 1
\end{pmatrix}.
$$
Trị riêng là
$$ 1\pm i. $$
Do đó gốc là tiêu điểm đẩy của hệ tuyến tính hóa, và gần gốc hệ phi tuyến cũng có động học cục bộ kiểu xoắn ốc đi ra.

### Ví dụ 2: Một cân bằng yên ngựa

Xét
$$ \dot{x}=x-x^2,\qquad \dot{y}=-y. $$
Tại $$ (0,0) $$, Jacobian là
$$
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix},
$$
nên có một trị riêng dương và một trị riêng âm. Cân bằng là yên ngựa. Chỉ từ Jacobian, ta đã đọc được ngay hình học cục bộ.

### Ví dụ 3: Khi tuyến tính hóa chưa đủ

Xét
$$ \dot{x}=y,\qquad \dot{y}=-x+x^3. $$
Tại gốc, Jacobian là
$$
\begin{pmatrix}
0 & 1\\
-1 & 0
\end{pmatrix},
$$
có trị riêng $$ \pm i $$. Ở đây tuyến tính hóa cho hình tâm, nhưng vì phần thực bằng 0 nên không thể kết luận ngay ổn định thật của hệ phi tuyến. Đây là ví dụ sinh viên rất cần thấy để tránh lạm dụng Jacobian.

### Ví dụ 4: Ý nghĩa của Hartman-Grobman

Nếu điểm cân bằng là hyperbolic, nghĩa là mọi trị riêng của Jacobian có phần thực khác 0, thì hình học cục bộ của hệ phi tuyến và hệ tuyến tính hóa là cùng kiểu topo. Điều này không có nghĩa nghiệm y hệt nhau, nhưng nghĩa là loại quỹ đạo gần cân bằng là cùng một kiểu.

## Câu hỏi khái niệm

1. Vì sao tuyến tính hóa chỉ là công cụ cục bộ chứ không phải toàn cục?
2. Vai trò thật sự của Jacobian trong phân tích hệ phi tuyến là gì?
3. Vì sao trường hợp trị riêng có phần thực bằng 0 là tình huống phải cẩn thận đặc biệt?

## Bài toán ứng dụng

1. Một mô hình sinh thái có điểm cân bằng nội. Hãy giải thích vì sao Jacobian tại đó có thể dự đoán quần thể quay về cân bằng hay rời xa nó.
2. Một hệ điều khiển được vận hành quanh một điểm làm việc. Vì sao kỹ sư thường tuyến tính hóa quanh điểm ấy?
3. Trong cơ học, vì sao biết động học gần vị trí cân bằng thường đủ để đánh giá ổn định ban đầu của một thiết kế?

## Chiến lược giảng dạy tương tác

- Cho sinh viên giải nhiều điểm cân bằng khác nhau trong cùng một hệ rồi so sánh Jacobian tại từng điểm.
- Tổ chức bài tập "phóng to quanh cân bằng": nhìn trường vector gốc và dự đoán hệ tuyến tính hóa.
- Hỏi lớp: "Nếu zoom rất gần gốc, hệ phi tuyến này trông giống hệ tuyến tính nào?"
- Nhấn mạnh bằng ví dụ phản ví dụ rằng không phải lúc nào Jacobian cũng kết luận được toàn bộ câu chuyện.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu dùng checklist: tìm cân bằng, tính Jacobian, thay điểm cân bằng vào, tìm trị riêng, rồi mới kết luận. Nhiều sai sót đến từ việc bỏ sót một bước nhỏ trong quy trình.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi giải thích trực giác của định lý Hartman-Grobman hoặc tìm một ví dụ mà tuyến tính hóa không đủ để kết luận ổn định.

## Tóm tắt dễ nhớ

Tuyến tính hóa là cách nhìn gần điểm cân bằng bằng con mắt của hệ tuyến tính. Jacobian là bản sao bậc nhất của hệ tại cân bằng. Nếu cân bằng hyperbolic, trị riêng của Jacobian thường cho ta câu chuyện cục bộ rất chính xác về ổn định và hình học quỹ đạo.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Con lắc gần vị trí cân bằng
- Bài toán: Gần vị trí cân bằng, ta muốn thay hệ phi tuyến bằng mô hình đơn giản hơn để dự đoán dao động nhỏ.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega
$$
và gần $$ \theta=0 $$:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}\approx -\theta-c\omega.
$$
- Giả thiết và giới hạn: Chỉ đúng khi góc nhỏ; xa cân bằng thì tuyến tính hóa có thể sai đáng kể.
- Diễn giải: Jacobian cho hành vi cục bộ gần cân bằng, không phải toàn bộ động lực học.

#### Phản ứng hóa học gần trạng thái dừng
- Bài toán: Kiểm tra nồng độ có trở về trạng thái vận hành hay không sau nhiễu nhỏ.
- Mô hình:
$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}),\qquad
\dot{\mathbf{u}}=J(\mathbf{x}_*)\mathbf{u},
$$
trong đó $$ \mathbf{u}=\mathbf{x}-\mathbf{x}_* $$.
- Giả thiết và giới hạn: Chỉ mô tả tốt cho nhiễu nhỏ quanh $$ \mathbf{x}_* $$.
- Diễn giải: Phổ của Jacobian là phiên bản phi tuyến của phân tích trị riêng ở Chương 4.

### 2. Trực giác bổ sung và các kết nối

Tuyến tính hóa là kính lúp địa phương: nó cho biết hệ nhìn như thế nào ở rất gần cân bằng. Một ngộ nhận lớn là dùng kết luận cục bộ như kết luận toàn cục. Nếu điểm cân bằng là hyperbolic, tuyến tính hóa thường rất đáng tin; nếu không hyperbolic, cần cẩn trọng hơn nhiều. Bài này là chiếc cầu nối trực tiếp từ hệ tuyến tính sang động lực học phi tuyến.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def nonlinear(t, z):
    x, y = z
    return [y, -np.sin(x) - 0.2 * y]

def linearized(t, z):
    x, y = z
    return [y, -x - 0.2 * y]

t = np.linspace(0, 20, 600)
z0 = [0.3, 0.0]
sol1 = solve_ivp(nonlinear, [0, 20], z0, t_eval=t)
sol2 = solve_ivp(linearized, [0, 20], z0, t_eval=t)

plt.plot(t, sol1.y[0], label="phi tuyen")
plt.plot(t, sol2.y[0], "--", label="tuyen tinh hoa")
plt.xlabel("t")
plt.ylabel("theta")
plt.title("So sanh he phi tuyen va tuyen tinh hoa")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: linearization near equilibrium nonlinear system
- search: Jacobian local behavior phase plane
- search: pendulum linearization comparison

### 5. Bài toán mẫu có bối cảnh thực

Cho hệ
$$ \dot{x}=y-x^3,\qquad
\dot{y}=-x-y. $$
Điểm cân bằng là $$ \left(0,0\right) $$. Jacobian tại gốc:
$$
J(0,0)=
\begin{pmatrix}
0 & 1\\
-1 & -1
\end{pmatrix}.
$$
Trị riêng có phần thực âm nên cân bằng ổn định tiệm cận về mặt cục bộ. Từ đây ta hiểu: gần gốc, hệ phi tuyến cư xử giống một spiral sink.

### 6. Phân tầng độ khó

**Bậc đại học.** Tính Jacobian, tìm điểm cân bằng, phân loại cục bộ bằng ma trận tuyến tính hóa.

**Bậc sau đại học.** Nói về định lý Hartman-Grobman, điểm hyperbolic và những thất bại của tuyến tính hóa tại điểm không hyperbolic.

## Tài liệu tham khảo

- Strogatz, Chương 6: trình bày rất rõ Jacobian và tuyến tính hóa.
- Arnold, Chương 5: mạnh về góc nhìn hình học quanh cân bằng.
