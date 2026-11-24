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

Nếu phóng to một đường cong trơn bất kỳ dưới kính hiển vi, nó trông gần như một đoạn thẳng. Ý tưởng **tuyến tính hóa (linearization)** làm điều hệt như vậy cho hệ phương trình vi phân phi tuyến: phóng to cực gần một **điểm cân bằng** $(x^*, y^*)$ để thay thế hệ phi tuyến rắc rối bằng một hệ tuyến tính ma trận Jacobian $J(x^*, y^*)$ giải được trọn vẹn bằng đại số tuyến tính!

## Bản đồ kiến thức nền: Bốn trụ cột của Điểm Cân bằng & Tuyến tính hóa

1. **Điểm cân bằng (Equilibrium / Fixed Point)**:
   Nghiệm đại số của hệ $f(x^*, y^*) = 0$ và $g(x^*, y^*) = 0$—nơi vận tốc triệt tiêu hoàn toàn.
2. **Ma trận Jacobian $J(x^*, y^*)$**:
   Khai triển Taylor bậc nhất quanh $(x^*, y^*)$ với độ lệch $\mathbf{u} = (x - x^*, y - y^*)^T$ cho hệ tuyến tính hóa $\dot{\mathbf{u}} \approx J(x^*, y^*)\mathbf{u}$, trong đó $J = \begin{pmatrix} f_x & f_y \\ g_x & g_y \end{pmatrix}$.
3. **Định lý Hartman–Grobman & Điểm Hyperbolic**:
   Nếu mọi trị riêng của $J(x^*, y^*)$ đều có **phần thực khác 0** ($\operatorname{Re}(\lambda) \neq 0$, gọi là điểm *hyperbolic*), thì bức chân dung pha của hệ phi tuyến lân cận $(x^*, y^*)$ tương đương topo hoàn toàn với hệ tuyến tính hóa!
4. **Trường hợp biên (Non-hyperbolic — $\operatorname{Re}(\lambda) = 0$)**:
   Khi trị riêng thuần ảo (tâm tuyến tính) hoặc bằng $0$, các số hạng bậc cao (bậc 2, bậc 3) có thể phá vỡ quỹ đạo đóng thành xoáy hút hoặc xoáy đẩy—tuyến tính hóa không đủ kết luận!

## Mục tiêu

Bài học này giúp sinh viên xác định điểm cân bằng của hệ phi tuyến, lập ma trận Jacobian, sử dụng phép tuyến tính hóa để dự đoán động học cục bộ gần điểm cân bằng và hiểu ý nghĩa của việc hệ phi tuyến có hành vi tương tự hệ tuyến tính trong lân cận điểm cân bằng hyperbolic.

## Kiến thức nền

Sinh viên cần nắm hệ phương trình vi phân tuyến tính hai chiều, trị riêng của ma trận và mặt phẳng pha. Kiến thức cơ bản về đạo hàm riêng là cần thiết để tính ma trận Jacobian.

## Dẫn nhập

![Tuyến tính hóa gần điểm cân bằng]({{ site.imgurl }}/chapter_img/chapter05/02_equilibria_linearization.svg)

Hệ phi tuyến thường rất khó giải trực tiếp. Tuy nhiên, trong nhiều ứng dụng, ta không cần biết toàn bộ quỹ đạo ở mọi nơi mà chỉ cần hiểu diễn biến gần một **trạng thái quan trọng, chẳng hạn trạng thái cân bằng sinh học, vị trí đứng yên của cơ hệ hay điểm vận hành của một mạch điện**. Khi đó, tuyến tính hóa là công cụ phân tích tự nhiên và hiệu quả nhất.

Ý tưởng của tuyến tính hóa khá trực tiếp: khi xét đủ gần một điểm cân bằng, số hạng bậc nhất trong khai triển Taylor giữ vai trò chi phối, còn các số hạng phi tuyến bậc cao chỉ tạo ra hiệu chỉnh nhỏ. Nhờ vậy, ma trận Jacobian đóng vai trò như một bản xấp xỉ tuyến tính cục bộ của hệ phi tuyến.

### Khung giải thích (nên đọc chậm): Tuyến tính hóa cầm tay chỉ việc con lắc đơn không ma sát $\dot{\theta} = \omega,\; \dot{\omega} = -\sin\theta$

1. **Tìm điểm cân bằng**: $\omega = 0$ và $\sin\theta = 0 \implies$ hai trạng thái vật lý chính: $(\theta^*, \omega^*) = (0, 0)$ (treo thẳng xuống) và $(\pi, 0)$ (dựng ngược lên trên).
2. **Tính ma trận Jacobian tổng quát**:
   $$J(\theta, \omega) = \begin{pmatrix} 0 & 1 \\ -\cos\theta & 0 \end{pmatrix}.$$
3. **Tại điểm dựng ngược $(\pi, 0)$**:
   $$J(\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \implies \lambda^2 - 1 = 0 \implies \lambda_1 = +1,\; \lambda_2 = -1.$$
   Cả hai phần thực đều khác 0 (hyperbolic) và trái dấu → **Điểm yên ngựa (Saddle — không ổn định)**; Định lý Hartman–Grobman khẳng định con lắc thật dựng ngược cũng không ổn định!
4. **Tại điểm treo xuống $(0, 0)$**:
   $$J(0, 0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \implies \lambda = \pm i \quad (\operatorname{Re}(\lambda) = 0).$$
   Đây là trường hợp **non-hyperbolic**: tuyến tính hóa cho tâm, nhưng phải dùng định luật bảo toàn năng lượng $E = \frac{1}{2}\omega^2 - \cos\theta$ mới kết luận chắc chắn $(0, 0)$ là tâm thực sự của con lắc phi tuyến!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Tương tự như một đường cong trơn trông gần giống đường thẳng khi phóng to đủ gần, một hệ phi tuyến cũng có hành vi gần giống hệ tuyến tính khi quan sát trong lân cận nhỏ quanh điểm cân bằng. Ma trận Jacobian chính là phiên bản nhiều chiều của tiếp tuyến đó.

### Cách nhìn hình ảnh

Nếu các quỹ đạo gần điểm cân bằng có dạng yên ngựa, nút hay tiêu điểm xoắn, điều đó thường phản ánh chân dung pha của ma trận Jacobian tại điểm cân bằng ấy. Tuyến tính hóa giúp nhận diện mô hình hình học tuyến tính nào đang chi phối hệ ở quy mô nhỏ.

### Cách nhìn hình thức

**Điểm cân bằng** (equilibrium point) là trạng thái mà tại đó hệ đứng yên mãi mãi: nếu xuất phát tại điểm này, hệ sẽ không rời đi. Với hệ
$$\dot{x}=f(x,y),\qquad \dot{y}=g(x,y),$$
điểm cân bằng $$(x_*,y_*)$$ là nghiệm của hệ phương trình:
$$f(x_*,y_*)=0,\qquad g(x_*,\ y_*)=0.$$

**Ý nghĩa vật lý:**
- Trong con lắc: vị trí thấp nhất — con lắc đứng yên nếu được thả với vận tốc ban đầu bằng 0.
- Trong mạch điện: trạng thái dòng điện bằng 0 và điện tích không đổi.
- Trong sinh thái học: trạng thái quần thể ổn định, không tăng và không giảm.
- Trong hóa học: trạng thái cân bằng hóa học.

**Vai trò của điểm cân bằng:**
- Cho biết các trạng thái dừng có thể có của hệ.
- Cho phép phân biệt vùng **ổn định** (hệ quay về trạng thái cân bằng) với vùng **không ổn định** (hệ rời xa trạng thái cân bằng).
- Cấu trúc pha quanh các điểm cân bằng chi phối mạnh mẽ hành vi dài hạn của hệ.

**Ví dụ tìm điểm cân bằng:**

Xét hệ $$\dot{x}=x(1-y),\ \dot{y}=y(x-1)$$.

Giải đồng thời $$f=0$$ và $$g=0$$:
- $$x(1-y)=0 \Rightarrow x=0$$ hoặc $$y=1$$
- $$y(x-1)=0 \Rightarrow y=0$$ hoặc $$x=1$$

Các cặp nghiệm ứng viên là $$(0,0)$$, $$(0,1)$$, $$(1,0)$$, $$(1,1)$$, nhưng chỉ có $$(0,0)$$ và $$(1,1)$$ thỏa mãn đồng thời cả hai phương trình:
- Tại $$(0,0)$$: $$\dot{x}=0(1-0)=0,\ \dot{y}=0(0-1)=0$$ ✓
- Tại $$(1,1)$$: $$\dot{x}=1(1-1)=0,\ \dot{y}=1(1-1)=0$$ ✓

Vậy hệ có hai điểm cân bằng là $$(0,0)$$ và $$(1,1)$$.

### Tuyến tính hóa là gì?

**Tuyến tính hóa** (linearization) là quá trình **xấp xỉ một hệ phi tuyến bằng một hệ tuyến tính** trong lân cận của một điểm quan trọng (thường là điểm cân bằng).

Giống như đường cong trơn trông như đường thẳng ở quy mô nhỏ, hệ phi tuyến có thể được thay thế cục bộ bằng hệ tuyến tính tương ứng quanh điểm cân bằng.

**So sánh:**

| Hệ phi tuyến | Hệ tuyến tính hóa |
|---|---|
| Khó giải tường minh | Giải được dễ dàng |
| Nghiệm phức tạp | Nghiệm là tổ hợp các hàm mũ |
| Quỹ đạo có dạng bất kỳ | Quỹ đạo thuộc các dạng tuyến tính cơ bản |

### Công thức toán học

Cho hệ $$\dot{x}=f(x,y),\ \dot{y}=g(x,y)$$.

**Bước 1:** Đặt biến độ lệch $$u = x - x_*,\ v = y - y_*$$ (độ lệch so với điểm cân bằng).

**Bước 2:** Khai triển Taylor bậc nhất quanh $$(x_*, y_*)$$:
$$f(x_* + u, y_* + v) \approx f(x_*,y_*) + \frac{\partial f}{\partial x}\Big|_* u + \frac{\partial f}{\partial y}\Big|_* v$$

Do tại điểm cân bằng $$f(x_*,y_*) = 0$$ và $$g(x_*,y_*) = 0$$, ta thu được:

**Bước 3:** Hệ tuyến tính hóa
$$\begin{pmatrix}\dot{u}\\\dot{v}\end{pmatrix} = J(x_*,y_*) \begin{pmatrix}u\\v\end{pmatrix}$$

trong đó **ma trận Jacobian** tại $$(x_*, y_*)$$ là:
$$J(x_*,y_*) = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y}\\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y} \end{pmatrix}_{(x_*,y_*)}.$$

### Ví dụ tuyến tính hóa

Xét lại hệ $$\dot{x}=x(1-y),\ \dot{y}=y(x-1)$$ tại điểm cân bằng $$(1,1)$$.

Tính các đạo hàm riêng:
- $$\frac{\partial f}{\partial x} = 1-y, \quad \frac{\partial f}{\partial y} = -x$$
- $$\frac{\partial g}{\partial x} = y, \quad \frac{\partial g}{\partial y} = x-1$$

Thay $$(1,1)$$ vào:
$$J(1,1) = \begin{pmatrix} 1-1 & -1\\ 1 & 1-1 \end{pmatrix} = \begin{pmatrix} 0 & -1\\ 1 & 0 \end{pmatrix}.$$

Hệ tuyến tính hóa tương ứng là:
$$\begin{pmatrix}\dot{u}\\\dot{v}\end{pmatrix} = \begin{pmatrix} 0 & -1\\ 1 & 0 \end{pmatrix} \begin{pmatrix}u\\v\end{pmatrix}.$$

Phương trình đặc trưng $$\lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i$$ cho thấy điểm cân bằng của hệ tuyến tính hóa là một **tâm** (center), với các quỹ đạo là những đường tròn đồng tâm quanh $$(1,1)$$.

### Khi nào tuyến tính hóa đáng tin cậy?

Tuyến tính hóa cho kết luận đáng tin cậy khi:
- Điểm cân bằng là **hyperbolic**: mọi trị riêng của ma trận Jacobian đều có phần thực **khác 0**.
- Ta chỉ khảo sát hành vi **cục bộ** gần điểm cân bằng.

Tuyến tính hóa **không đủ để kết luận** khi:
- Có trị riêng có phần thực bằng 0 (trường hợp biên).
- Trị riêng thuần ảo (tâm): các số hạng phi tuyến bậc cao có thể biến tâm thành tiêu điểm hút hoặc tiêu điểm đẩy.
- Ta cần đánh giá hành vi **toàn cục** ở xa điểm cân bằng.

## Những ngộ nhận thường gặp

- "Tuyến tính hóa mô tả toàn bộ hành vi của hệ." Sai. Nó chỉ có giá trị trong lân cận đủ nhỏ quanh điểm cân bằng.
- "Chỉ cần xét Jacobian là kết luận được cho mọi điểm cân bằng." Không đúng khi Jacobian có trị riêng có phần thực bằng 0.
- "Vì hệ là phi tuyến nên xấp xỉ tuyến tính luôn kém chính xác." Không hẳn. Gần điểm cân bằng hyperbolic, tuyến tính hóa phản ánh rất chính xác cấu trúc cục bộ.
- "Điểm cân bằng là nơi hệ đứng yên nên không có gì đáng khảo sát." Sai. Cấu trúc quỹ đạo xung quanh điểm cân bằng chính là yếu tố quyết định tính ổn định hay mất ổn định của hệ.

## Tiến trình học tập đề xuất

### Bước 1: Tìm điểm cân bằng

Giải đồng thời hệ phương trình
$$ f=0,\qquad g=0. $$

### Bước 2: Tính ma trận Jacobian

Tính các đạo hàm riêng và thay tọa độ từng điểm cân bằng vào.

### Bước 3: Phân tích trị riêng của Jacobian

Xác định loại điểm cân bằng của hệ tuyến tính hóa.

### Bước 4: Diễn giải cục bộ cho hệ phi tuyến

Rút ra kết luận định tính gần điểm cân bằng và lưu ý phạm vi hiệu lực của kết luận đó.

### Các điểm kiểm tra

- Sinh viên có tìm đầy đủ và chính xác các điểm cân bằng hay không.
- Sinh viên có tính đúng ma trận Jacobian tại từng điểm cân bằng hay không.
- Sinh viên có phân biệt được trường hợp tuyến tính hóa đủ mạnh với trường hợp chưa thể kết luận ngay hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Một hệ phi tuyến đơn giản

Xét hệ
$$ \dot{x}=x-y-x^3,\qquad \dot{y}=x+y-y^3. $$
Tại gốc tọa độ, ma trận Jacobian là
$$
J(0,0)=
\begin{pmatrix}
1 & -1\\
1 & 1
\end{pmatrix}.
$$
Các trị riêng là
$$ 1\pm i. $$
Do đó gốc tọa độ là tiêu điểm đẩy của hệ tuyến tính hóa, và gần gốc, hệ phi tuyến cũng có quỹ đạo xoắn ốc đi ra.

### Ví dụ 2: Điểm cân bằng yên ngựa

Xét hệ
$$ \dot{x}=x-x^2,\qquad \dot{y}=-y. $$
Tại $$ (0,0) $$, ma trận Jacobian là
$$
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix},
$$
có một trị riêng dương và một trị riêng âm. Do đó gốc tọa độ là điểm yên ngựa, giúp ta nhận ra ngay hình học cục bộ của hệ chỉ từ Jacobian.

### Ví dụ 3: Khi tuyến tính hóa chưa đủ

Xét hệ
$$ \dot{x}=y,\qquad \dot{y}=-x+x^3. $$
Tại gốc tọa độ, ma trận Jacobian là
$$
\begin{pmatrix}
0 & 1\\
-1 & 0
\end{pmatrix},
$$
với các trị riêng $$ \pm i $$. Hệ tuyến tính hóa có dạng tâm, nhưng vì phần thực bằng 0 nên ta không thể dùng Jacobian để kết luận ngay tính ổn định thực sự của hệ phi tuyến. Ví dụ này giúp sinh viên tránh lạm dụng phép tuyến tính hóa.

### Ví dụ 4: Ý nghĩa của định lý Hartman–Grobman

Nếu điểm cân bằng là hyperbolic (mọi trị riêng của Jacobian đều có phần thực khác 0), hình học cục bộ của hệ phi tuyến tương đương tôpô với hệ tuyến tính hóa. Điều này không có nghĩa là các nghiệm trùng khớp về mặt đại số, mà có nghĩa là cấu trúc quỹ đạo quanh điểm cân bằng thuộc cùng một dạng định tính.

## Câu hỏi khái niệm

1. Vì sao tuyến tính hóa chỉ là công cụ cục bộ chứ không phải công cụ toàn cục?
2. Ma trận Jacobian đóng vai trò gì trong phân tích hệ phi tuyến?
3. Vì sao trường hợp trị riêng có phần thực bằng 0 đòi hỏi phải phân tích thận trọng hơn?

## Bài toán ứng dụng

1. Một mô hình sinh thái có điểm cân bằng nội. Hãy giải thích vì sao ma trận Jacobian tại điểm đó giúp dự đoán quần thể sẽ quay về hay rời xa trạng thái cân bằng.
2. Một hệ điều khiển vận hành quanh một điểm làm việc. Vì sao kỹ sư thường tuyến tính hóa hệ quanh điểm làm việc đó?
3. Trong cơ học, vì sao việc phân tích động học gần vị trí cân bằng thường đủ để đánh giá độ ổn định ban đầu của một thiết kế?

## Chiến lược giảng dạy tương tác

- Cho sinh viên khảo sát nhiều điểm cân bằng khác nhau trong cùng một hệ rồi so sánh ma trận Jacobian tại từng điểm.
- Tổ chức bài tập phóng to lân cận điểm cân bằng: quan sát trường vector gốc và dự đoán hệ tuyến tính hóa tương ứng.
- Đặt câu hỏi cho lớp: nếu quan sát rất gần gốc tọa độ, hệ phi tuyến này tương ứng với dạng hệ tuyến tính nào?
- Đưa ra phản ví dụ cụ thể để nhấn mạnh rằng không phải lúc nào Jacobian cũng đủ để kết luận toàn bộ hành vi ổn định.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên hướng dẫn sinh viên làm theo danh sách kiểm tra cố định: tìm điểm cân bằng, tính ma trận Jacobian, thay tọa độ điểm cân bằng, tìm trị riêng rồi mới kết luận. Phần lớn sai sót xuất phát từ việc bỏ qua một bước trung gian trong quy trình này.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên giải thích trực giác của định lý Hartman–Grobman hoặc tự xây dựng một ví dụ mà phép tuyến tính hóa không đủ để kết luận tính ổn định.

## Tóm tắt dễ nhớ

Tuyến tính hóa là cách khảo sát hệ phi tuyến trong lân cận điểm cân bằng bằng công cụ của hệ tuyến tính. Ma trận Jacobian là xấp xỉ bậc nhất của hệ tại điểm cân bằng. Khi điểm cân bằng là hyperbolic, trị riêng của Jacobian cho biết chính xác cấu trúc cục bộ về ổn định và hình học quỹ đạo.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Con lắc gần vị trí cân bằng
- Bài toán: Xấp xỉ hệ phi tuyến bằng mô hình đơn giản hơn để dự đoán dao động nhỏ quanh vị trí cân bằng.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega
$$
và trong lân cận $$ \theta=0 $$:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}\approx -\theta-c\omega.
$$
- Giả thiết và giới hạn: Chỉ phù hợp khi góc lệch nhỏ; khi ra xa vị trí cân bằng, phép tuyến tính hóa có thể sai lệch đáng kể.
- Diễn giải: Ma trận Jacobian chỉ phản ánh động học cục bộ quanh cân bằng, không đại diện cho toàn bộ không gian pha.

#### Phản ứng hóa học gần trạng thái dừng
- Bài toán: Kiểm tra xem nồng độ các chất có quay về trạng thái vận hành sau nhiễu nhỏ hay không.
- Mô hình:
$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}),\qquad
\dot{\mathbf{u}}=J(\mathbf{x}_*)\mathbf{u},
$$
trong đó $$ \mathbf{u}=\mathbf{x}-\mathbf{x}_* $$.
- Giả thiết và giới hạn: Chỉ chính xác với nhiễu nhỏ quanh $$ \mathbf{x}_* $$.
- Diễn giải: Phổ trị riêng của Jacobian là sự mở rộng tự nhiên từ phép phân tích trị riêng của hệ tuyến tính ở Chương 4 sang hệ phi tuyến.

### 2. Trực giác bổ sung và các kết nối

Tuyến tính hóa hoạt động như một kính lúp cục bộ, cho thấy hình dạng của hệ ở rất gần điểm cân bằng. Một sai lầm phổ biến là suy rộng kết luận cục bộ thành kết luận toàn cục. Khi điểm cân bằng là hyperbolic, tuyến tính hóa đáng tin cậy; khi không hyperbolic, cần áp dụng các phương pháp phi tuyến sâu hơn. Bài học này đóng vai trò cầu nối trực tiếp từ hệ tuyến tính sang động lực học phi tuyến.

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
Điểm cân bằng là $$ \left(0,0\right) $$. Ma trận Jacobian tại gốc là:
$$
J(0,0)=
\begin{pmatrix}
0 & 1\\
-1 & -1
\end{pmatrix}.
$$
Các trị riêng đều có phần thực âm nên điểm cân bằng ổn định tiệm cận cục bộ. Từ đó suy ra trong lân cận gốc tọa độ, hệ phi tuyến có hành vi giống một tiêu điểm hút (spiral sink).

### 6. Phân tầng độ khó

**Bậc đại học.** Tìm điểm cân bằng, tính ma trận Jacobian và phân loại cục bộ thông qua hệ tuyến tính hóa.

**Bậc sau đại học.** Tìm hiểu định lý Hartman–Grobman, điểm cân bằng hyperbolic và các trường hợp tuyến tính hóa thất bại tại điểm không hyperbolic.

## Video tham khảo

- Xem trước: [Linearizing Nonlinear Differential Equations Near a Fixed Point](https://www.youtube.com/watch?v=RCWkzzLgwf0) — Steve Brunton, tiếng Anh. Tuyến tính hóa trường vector phi tuyến tại điểm cân bằng và sử dụng ma trận Jacobian trong lân cận điểm đó.
- [Linearization | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=UCpMao94iFg) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về phép tuyến tính hóa.
- [MAE5790-6 Two dimensional nonlinear systems   fixed points](https://www.youtube.com/watch?v=9yh9DmNqdk4) — Cornell MAE, tiếng Anh. Strogatz trình bày về điểm cân bằng của hệ phi tuyến hai chiều.

## Tài liệu tham khảo

- Strogatz, Chương 6: trình bày rõ ràng về ma trận Jacobian và tuyến tính hóa.
- Arnold, Chương 5: tập trung vào góc nhìn hình học quanh điểm cân bằng.
