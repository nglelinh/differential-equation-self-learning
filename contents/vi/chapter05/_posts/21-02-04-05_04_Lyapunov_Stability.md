---
layout: post
title: "05-04 Ổn định Lyapunov"
chapter: '05'
order: 4
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: required
---

Điều gì xảy ra khi tuyến tính hóa bó tay—chẳng hạn trị riêng bằng $0$ hoặc thuần ảo, hoặc bạn muốn chứng minh ổn định trên một **miền lớn** chứ không chỉ trong lân cận vô cùng bé? Aleksandr Lyapunov (1892) đã đưa ra một ý tưởng trực quan tuyệt đẹp lấy cảm hứng từ vật lý: nếu tìm được một "hàm năng lượng tổng quát" $V(\mathbf{x})$ có đáy duy nhất tại điểm cân bằng và **luôn giảm dần** theo thời gian dọc theo mọi quỹ đạo, thì hệ chắc chắn phải lăn xuống đáy và đứng yên!

## Bản đồ kiến thức nền: Bốn trụ cột của Lý thuyết Ổn định Lyapunov

1. **Ba bậc ổn định (Lyapunov, Tiệm cận, Toàn cục)**:
   - **Ổn định Lyapunov**: Khởi đầu đủ gần gốc thì mãi mãi ở gần gốc ($\forall \varepsilon > 0, \exists \delta > 0$).
   - **Ổn định tiệm cận**: Ổn định Lyapunov VÀ $\lim_{t\to\infty}\mathbf{x}(t) = \mathbf{0}$.
   - **Ổn định tiệm cận toàn cục**: Mọi quỹ đạo xuất phát từ bất kỳ đâu trong $\mathbb{R}^n$ đều hội tụ về gốc (cần thêm điều kiện $V(\mathbf{x}) \to \infty$ khi $\|\mathbf{x}\| \to \infty$).
2. **Hàm xác định dương ($V > 0$) và Đạo hàm quỹ đạo ($\dot{V} = \nabla V \cdot \mathbf{f}$)**:
   Ta tính trực tiếp tốc độ biến thiên của $V$ mà **không cần biết nghiệm $\mathbf{x}(t)$** nhờ quy tắc dây chuyền $\frac{d}{dt}V(\mathbf{x}(t)) = \nabla V(\mathbf{x}) \cdot \mathbf{f}(\mathbf{x})$.
3. **Định lý trực tiếp Lyapunov**:
   Nếu $\dot{V} \le 0$ → ổn định Lyapunov; nếu $\dot{V} < 0$ (xác định âm) → ổn định tiệm cận!
4. **Nguyên lý bất biến LaSalle**:
   Ngay cả khi $\dot{V} \le 0$ chỉ bán xác định âm (ví dụ con lắc có ma sát với $\dot{E} = -c\dot{\theta}^2 \le 0$), nếu tập $\{\dot{V} = 0\}$ không chứa quỹ đạo trọn vẹn nào khác ngoài gốc, hệ vẫn ổn định tiệm cận!

## Mục tiêu

Bài học này giúp sinh viên nắm được phương pháp Lyapunov như một công cụ chứng minh tính ổn định mà không cần tìm nghiệm tường minh, hiểu các tiêu chuẩn của một hàm Lyapunov phù hợp và nhận thấy vai trò của tư duy năng lượng trong phân tích hệ phi tuyến.

## Kiến thức nền

Sinh viên cần nắm vững khái niệm điểm cân bằng, đạo hàm theo quỹ đạo và trực giác về ổn định. Sự quen thuộc với khái niệm năng lượng trong cơ học sẽ giúp tiếp cận bài học tự nhiên hơn.

## Dẫn nhập

![Hàm Lyapunov như năng lượng suy giảm]({{ site.imgurl }}/chapter_img/chapter05/04_lyapunov_stability.svg)

Nhiều hệ phi tuyến quan trọng không thể giải được bằng công thức tường minh. Nếu chỉ xét tính ổn định sau khi tìm được nghiệm đóng, ta sẽ không thể phân tích phần lớn các mô hình thực tế. Phương pháp Lyapunov mở ra một hướng tiếp cận khác: thay vì theo dõi trực tiếp quỹ đạo, ta xây dựng một hàm vô hướng đóng vai trò tương tự năng lượng rồi khảo sát xem đại lượng đó tăng, giảm hay giữ nguyên dọc theo chuyển động.

Ý tưởng cốt lõi là tìm một "thước đo độ lệch khỏi vị trí cân bằng" mà hệ không thể làm tăng lên. Nếu thước đo này giảm nghiêm ngặt theo thời gian, ta suy ra hệ bị kéo dần về điểm cân bằng. Cách tiếp cận này vừa có ý nghĩa hình học và vật lý rõ ràng, vừa có tính ứng dụng cao.

### Khung giải thích (nên đọc chậm): Chứng minh ổn định tiệm cận cho hệ phi tuyến $\dot{x} = -x^3 + y,\; \dot{y} = -x - y^3$ nơi tuyến tính hóa bó tay

Kiểm tra nhanh tuyến tính hóa tại $(0, 0)$: $J(0,0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ có trị riêng $\lambda = \pm i$ (non-hyperbolic → tuyến tính hóa **bó tay**!).

Bây giờ áp dụng hàm năng lượng Lyapunov $V(x, y) = \frac{1}{2}(x^2 + y^2)$:
1. **Xác định dương**: $V(0, 0) = 0$ và $V(x, y) > 0$ với mọi $(x, y) \neq (0, 0)$, lại có $V \to \infty$ khi $x^2 + y^2 \to \infty$.
2. **Tính $\dot{V}$ dọc quỹ đạo**:
   $$\dot{V} = x\dot{x} + y\dot{y} = x(-x^3 + y) + y(-x - y^3) = -x^4 + xy - xy - y^4 = -(x^4 + y^4).$$
3. **Kết luận ngay**: $-(x^4 + y^4) < 0$ với mọi $(x, y) \neq (0, 0)$! Vậy gốc $(0, 0)$ **ổn định tiệm cận toàn cục**—một kết quả mạnh mẽ mà tuyến tính hóa không bao giờ nhìn thấy được!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung $$ V(x,y) $$ như độ cao của một bề mặt năng lượng có đáy tại điểm cân bằng. Nếu quỹ đạo của hệ luôn đi xuống hoặc giữ nguyên độ cao trên bề mặt đó, hệ không thể tự thoát lên các vùng cao hơn. Nếu quỹ đạo luôn đi xuống, hệ sẽ tiến về đáy.

### Cách nhìn hình ảnh

Các đường mức của $$ V $$ giống như những vòng bao quanh điểm cân bằng. Nếu dọc theo mọi quỹ đạo, trường vector luôn hướng vào phía trong các đường mức này, ta có hình ảnh trực quan rõ ràng về tính ổn định. Nhờ đó, Lyapunov chuyển bài toán theo dõi quỹ đạo thành bài toán hình học về họ các đường mức.

### Cách nhìn hình thức

Một hàm trơn $$ V(x,y) $$ là ứng viên hàm Lyapunov quanh điểm cân bằng gốc nếu
$$ V(0,0)=0, $$
và
$$ V(x,y)>0 \quad \text{khi } (x,y)\neq (0,0) $$
trong một lân cận của gốc tọa độ (tức là $$ V $$ xác định dương). Đạo hàm của $$ V $$ dọc theo quỹ đạo của hệ là
$$ \dot{V}=V_x f(x,y)+V_y g(x,y). $$
Nếu
$$ \dot{V}\le 0 $$
trong lân cận đó, điểm cân bằng ổn định theo Lyapunov. Nếu
$$ \dot{V}<0 $$
nghiêm ngặt ngoài điểm cân bằng, điểm cân bằng ổn định tiệm cận.

## Những ngộ nhận thường gặp

- "Muốn chứng minh ổn định thì bắt buộc phải tìm ra nghiệm." Sai. Mục đích chính của phương pháp Lyapunov là xét ổn định mà không cần giải nghiệm tường minh.
- "Mọi hàm xác định dương đều là hàm Lyapunov." Sai. Điều kiện quyết định nằm ở dấu của đạo hàm dọc theo quỹ đạo $$ \dot{V} $$.
- "Nếu $$ \dot{V}=0 $$ thì không kết luận được gì." Không đúng; khi $$ \dot{V}=0 $$ ta đã có ổn định Lyapunov, và trong nhiều trường hợp $$ \dot{V}\le 0 $$ còn có thể kết hợp thêm nguyên lý bất biến LaSalle để suy ra ổn định tiệm cận.
- "Phương pháp Lyapunov chỉ dùng trong cơ học." Sai. Nó được ứng dụng rộng rãi trong lý thuyết điều khiển, sinh học, mạch điện và nhiều lớp hệ phi tuyến khác.

## Tiến trình học tập đề xuất

### Bước 1: Chọn ứng viên $$ V $$

Thường bắt đầu từ những dạng tương tự năng lượng như $$ x^2+y^2 $$.

### Bước 2: Kiểm tra tính xác định dương

Đảm bảo $$ V(0,0)=0 $$ và $$ V(x,y)>0 $$ ngoài gốc, để $$ V $$ thực sự đo được độ lệch khỏi cân bằng.

### Bước 3: Tính đạo hàm $$ \dot{V} $$ dọc theo quỹ đạo

Sử dụng quy tắc dây chuyền để thay $$ \dot{x}=f(x,y) $$ và $$ \dot{y}=g(x,y) $$.

### Bước 4: Rút ra kết luận ổn định phù hợp

Phân biệt rõ trường hợp suy ra ổn định Lyapunov với trường hợp suy ra ổn định tiệm cận.

### Các điểm kiểm tra

- Sinh viên có phân biệt rõ hai điều kiện $$ V>0 $$ và $$ \dot{V}<0 $$ hay không.
- Sinh viên có tính chính xác đạo hàm theo quỹ đạo hay không.
- Sinh viên có tránh việc kết luận quá mạnh từ điều kiện chưa đủ (chẳng hạn chỉ có $$ \dot{V}\le 0 $$) hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hệ tuyến tính có tắt dần

Xét hệ
$$ x'=-x-y,\qquad y'=x-y. $$
Chọn hàm ứng viên
$$ V=x^2+y^2. $$
Đạo hàm dọc theo quỹ đạo là:
$$ \dot{V}=2xx'+2yy'
=2x(-x-y)+2y(x-y)
=-2x^2-2y^2. $$
Vì
$$ \dot{V}<0 $$
tại mọi điểm khác gốc tọa độ, điểm cân bằng gốc là ổn định tiệm cận.

### Ví dụ 2: Hệ bảo toàn năng lượng

Với hệ
$$ x'=y,\qquad y'=-x, $$
chọn
$$ V=x^2+y^2. $$
Khi đó
$$ \dot{V}=2xy+2y(-x)=0. $$
Năng lượng được bảo toàn dọc theo quỹ đạo. Gốc tọa độ ổn định theo Lyapunov nhưng không ổn định tiệm cận. Ví dụ này minh họa rõ ranh giới giữa hai khái niệm.

### Ví dụ 3: Chọn sai hàm ứng viên

Nếu chọn một hàm không xác định dương, chẳng hạn
$$ V=x^2-y^2, $$
thì dù biểu thức $$ \dot{V} $$ có gọn đẹp đến đâu, $$ V $$ vẫn không thể đóng vai trò thước đo khoảng cách tới cân bằng. Do đó việc xây dựng hàm $$ V $$ đòi hỏi cả tư duy cấu trúc lẫn trực giác toán học.

### Ví dụ 4: Cơ năng trong hệ có ma sát

Trong nhiều hệ cơ học, cơ năng toàn phần
$$ V=\text{động năng}+\text{thế năng} $$
là ứng viên tự nhiên. Khi có ma sát hoặc lực cản, $$ \dot{V} $$ thường không dương. Đây là mối liên hệ trực tiếp nhất giữa phương pháp Lyapunov và vật lý.

## Câu hỏi khái niệm

1. Vì sao phương pháp Lyapunov cho phép kết luận tính ổn định mà không cần công thức nghiệm?
2. Hai điều kiện "xác định dương" và "đạo hàm không dương" đóng vai trò khác nhau như thế nào?
3. Vì sao điều kiện $$ \dot{V}=0 $$ cho thấy tính ổn định Lyapunov nhưng chưa đủ để suy ra ổn định tiệm cận?

## Bài toán ứng dụng

1. Trong điều khiển robot, vì sao việc xây dựng một hàm "năng lượng sai lệch" là chiến lược thiết kế tự nhiên?
2. Trong mạch điện có điện trở, vì sao năng lượng điện từ thường tiêu hao dần và kéo hệ về trạng thái ổn định?
3. Trong mô hình sinh học, một đại lượng đo độ lệch khỏi trạng thái cân bằng có thể được dùng làm hàm Lyapunov như thế nào?

## Chiến lược giảng dạy tương tác

- Cho sinh viên thử nghiệm nhiều hàm ứng viên khác nhau để thấy không phải hàm nào cũng phù hợp.
- Đặt câu hỏi cho lớp: nếu xem $$ V $$ như năng lượng, hệ đang tiêu hao hay tích lũy năng lượng dọc theo quỹ đạo?
- Đối chiếu trực tiếp hai ví dụ có $$ \dot{V}<0 $$ và $$ \dot{V}=0 $$ để làm rõ sự khác biệt.
- Khuyến khích sinh viên mô tả ý nghĩa hình học của họ đường mức $$ V=\text{hằng số} $$.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên để sinh viên làm quen từ ứng viên đơn giản
$$ V=x^2+y^2 $$
trong các bài tập đầu tiên nhằm xây dựng vững chắc cách tính và diễn giải $$ \dot{V} $$ trước khi chuyển sang những hàm phức tạp hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự xây dựng một hàm Lyapunov cho một hệ phi tuyến cụ thể, hoặc phân tích ví dụ có $$ \dot{V}\le 0 $$ nhưng vẫn ổn định tiệm cận nhờ các công cụ mở rộng.

## Tóm tắt dễ nhớ

Phương pháp Lyapunov chuyển bài toán tìm nghiệm quỹ đạo thành bài toán tìm một đại lượng không tăng dọc theo chuyển động. Khi $$ V $$ đo độ lệch khỏi cân bằng (xác định dương) và $$ \dot{V}\le 0 $$, hệ ổn định theo Lyapunov; nếu $$ \dot{V}<0 $$ nghiêm ngặt ngoài cân bằng, hệ ổn định tiệm cận.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Cơ học có ma sát
- Bài toán: Chứng minh con lắc có ma sát giảm dần năng lượng và tiến về vị trí cân bằng thấp nhất mà không cần tìm nghiệm tường minh.
- Mô hình:
$$
\dot{\theta}=\omega,\qquad
\dot{\omega}=-\sin\theta-c\omega,
$$
với ứng viên Lyapunov là cơ năng:
$$
V(\theta,\omega)=1-\cos\theta+\frac{1}{2}\omega^2.
$$
- Giả thiết và giới hạn: Kết luận dựa trên cấu trúc năng lượng, chưa tự động cho biết tốc độ hội tụ chính xác.
- Diễn giải: Do $$ \dot{V}\le 0 $$, hệ không thể tự chuyển lên mức năng lượng cao hơn.

#### Điều khiển robot
- Bài toán: Thiết kế luật điều khiển sao cho sai số vị trí và vận tốc giảm về $$ 0 $$.
- Mô hình:
$$ \dot{e}_1=e_2,\qquad
\dot{e}_2=-k_1 e_1-k_2 e_2, $$
với hàm ứng viên
$$ V=\frac{1}{2}(k_1 e_1^2+e_2^2). $$
- Giả thiết và giới hạn: Mô hình bỏ qua giới hạn bão hòa của cơ cấu chấp hành và nhiễu đo.
- Diễn giải: Hàm Lyapunov cung cấp bằng chứng toán học chặt chẽ cho tính ổn định của bộ điều khiển.

### 2. Trực giác bổ sung và các kết nối

Phương pháp Lyapunov thay việc giải quỹ đạo bằng việc tìm một đại lượng suy giảm. Hai điều kiện $$ V>0 $$ và $$ \dot{V}\le 0 $$ đảm nhiệm vai trò riêng biệt: một điều kiện đo khoảng cách đến điểm cân bằng, điều kiện kia kiểm soát chiều biến thiên theo thời gian. Một lỗi thường gặp là vội kết luận ổn định tiệm cận khi mới chứng minh được $$ \dot{V}\le 0 $$. Bài học này kết nối trực tiếp hệ phi tuyến với nguyên lý năng lượng trong cơ học và kỹ thuật điều khiển.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, z):
    x, y = z
    return [-x - y, x - y]

t = np.linspace(0, 8, 400)
for z0 in [(2, 0), (0, 2), (-2, 1)]:
    sol = solve_ivp(system, [0, 8], z0, t_eval=t)
    V = sol.y[0]**2 + sol.y[1]**2
    plt.plot(t, V, label=f"IC={z0}")

plt.xlabel("t")
plt.ylabel("V(t)")
plt.title("Ham Lyapunov giam theo thoi gian")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Lyapunov function energy dissipation pendulum
- search: contour plot Lyapunov function trajectories
- search: asymptotic stability energy method

### 5. Bài toán mẫu có bối cảnh thực

Xét hệ
$$ x'=-x-y,\qquad
y'=x-y. $$
Chọn
$$ V=x^2+y^2. $$
Ta có
$$ \dot{V}=2x(-x-y)+2y(x-y)=-2x^2-2y^2<0 $$
với mọi điểm khác gốc. Do đó gốc tọa độ là ổn định tiệm cận — một minh họa điển hình cho việc chứng minh ổn định mà không cần giải nghiệm tường minh.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện và kiểm tra các hàm Lyapunov cơ bản như dạng toàn phương $$ x^2+y^2 $$.

**Bậc sau đại học.** Nghiên cứu định lý trực tiếp của Lyapunov, nguyên lý bất biến LaSalle và tính ổn định tiệm cận toàn cục.

## Video tham khảo

- Xem trước: [What is a Lyapunov function](https://www.youtube.com/watch?v=uXAx_641FPM) — richard pates, tiếng Anh. Giới thiệu khái niệm hàm Lyapunov và cách sự suy giảm của nó chứng minh tính ổn định.
- [A Visual Explanation of Lyapunov Stability](https://www.youtube.com/watch?v=W8YpgG0KuOo) — Prof Gio | Giordano Scarciotti, tiếng Anh. Diễn giải trực quan về ổn định Lyapunov.
- [MAE5790-7 Conservative Systems](https://www.youtube.com/watch?v=3s2lmZspEU8) — Cornell MAE, tiếng Anh. Strogatz trình bày về hệ bảo toàn, nơi năng lượng đóng vai trò hàm Lyapunov.

## Tài liệu tham khảo

- Strogatz, Chương 7: giới thiệu trực quan về phương pháp Lyapunov.
- Arnold, Chương 5: trình bày rõ trực giác năng lượng và ổn định phi tuyến.
