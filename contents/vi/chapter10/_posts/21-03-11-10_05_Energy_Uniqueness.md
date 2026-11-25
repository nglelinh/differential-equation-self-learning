---
layout: post
title: "Năng Lượng và Tính Duy Nhất"
chapter: '10'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---

![21 03 11 10 05 Energy Uniqueness]({{ site.imgurl }}/chapter_img/chapter10/05_energy_uniqueness.svg)

Với phương trình nhiệt (Chương 9), ta chứng minh tính duy nhất nghiệm bằng Nguyên lý Cực đại. Nhưng phương trình sóng **không** thỏa Nguyên lý Cực đại (hai sóng nhỏ gặp nhau có thể cộng hưởng tạo đỉnh cao gấp đôi!). Thay vào đó, vũ khí sắc bén nhất cho phương trình sóng là **Phương pháp Năng lượng (Energy Method)**: chứng minh tổng động năng + thế năng không đổi (hoặc không tăng) theo thời gian!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Năng lượng cho Phương trình Sóng

1. **Hàm Năng lượng của Sóng 1D**:
   $$E(t) = \frac{1}{2}\int_0^L \big(u_t^2 + c^2 u_x^2\big)\,dx \ge 0$$
   gồm động năng ($\frac{1}{2}\int u_t^2\,dx$) và thế năng đàn hồi ($\frac{1}{2}\int c^2 u_x^2\,dx$).
2. **Định luật Bảo toàn Năng lượng ($E'(t) = 0$)**:
   Lấy đạo hàm theo $t$, tích phân từng phần và thay $u_{tt} = c^2 u_{xx}$ cho:
   $$E'(t) = \big[c^2 u_t u_x\big]_0^L.$$
   Với biên cố định ($u_t = 0$) hoặc biên tự do ($u_x = 0$), vế biên triệt tiêu $\implies E'(t) = 0 \implies E(t) = E(0)$ không đổi mãi mãi!
3. **Chứng minh Tính Duy nhất Nghiệm trong 4 dòng**:
   Xét hiệu hai nghiệm $w = u_1 - u_2$: $w(x, 0) = 0,\; w_t(x, 0) = 0 \implies E_w(0) = 0 \implies E_w(t) = 0 \implies w_t \equiv 0, w_x \equiv 0 \implies w \equiv 0$!
4. **Sóng có ma sát ($u_{tt} + \gamma u_t = c^2 u_{xx}$, $\gamma > 0$)**:
   Khi có lực cản, $E'(t) = -\gamma \int_0^L u_t^2\,dx \le 0$ — năng lượng giảm dần (tiêu tán), tính duy nhất vẫn giữ nguyên hoàn toàn!

## Mục tiêu

Bài học này giúp sinh viên hiểu vì sao năng lượng là đại lượng tự nhiên nhất để kiểm soát nghiệm của phương trình sóng. Sau bài học, sinh viên cần biết viết biểu thức năng lượng của dây rung, hiểu cơ chế bảo toàn năng lượng dưới các điều kiện biên thích hợp, vận dụng phương pháp năng lượng để chứng minh tính duy nhất của nghiệm và so sánh tính bảo toàn của phương trình sóng với tính tiêu tán của phương trình nhiệt.

## Kiến thức nền

Sinh viên cần nắm phương trình sóng, kỹ thuật tích phân từng phần và trực giác cơ học về động năng và thế năng. Bài học này cho thấy một đại lượng vật lý quen thuộc có thể trở thành công cụ chứng minh định lý chặt chẽ trong PDE.

## Dẫn nhập

Ở các bài trước, ta đã khảo sát cách sóng truyền đi và dao động. Tuy nhiên, làm thế nào để chắc chắn rằng nghiệm không tăng vọt bất thường, không mất ổn định và ứng với cùng một bộ dữ liệu ban đầu chỉ tồn tại duy nhất một nghiệm? Câu trả lời nằm ở phương pháp năng lượng.

Khác với phương trình nhiệt vốn làm tiêu tán năng lượng theo thời gian, phương trình sóng thuần nhất chuyển hóa qua lại giữa động năng và thế năng đàn hồi mà không làm thất thoát tổng năng lượng. Chính định luật bảo toàn này mang lại phép chứng minh tính duy nhất ngắn gọn và chặt chẽ.

### Giải thích: Kiểm chứng trực tiếp bảo toàn năng lượng $E(t) = \text{hằng số}$ trên 1 sóng đứng $u(x, t) = A\cos(\omega t)\sin(kx)$

Với $L = \pi$, $k = 1$, $\omega = c$ (tức $u(x, t) = A\cos(ct)\sin x$):
1. Tính các đạo hàm: $u_t = -Ac\sin(ct)\sin x$, $u_x = A\cos(ct)\cos x$.
2. Tính động năng $K(t)$ và thế năng $U(t)$ (nhớ $\int_0^\pi \sin^2 x\,dx = \int_0^\pi \cos^2 x\,dx = \frac{\pi}{2}$):
   $$K(t) = \frac{1}{2}\int_0^\pi A^2 c^2 \sin^2(ct)\sin^2 x\,dx = \frac{\pi}{4} A^2 c^2 \sin^2(ct),$$
   $$U(t) = \frac{1}{2} c^2 \int_0^\pi A^2 \cos^2(ct)\cos^2 x\,dx = \frac{\pi}{4} A^2 c^2 \cos^2(ct).$$
3. **Cộng tổng năng lượng**:
   $$E(t) = K(t) + U(t) = \frac{\pi}{4} A^2 c^2 \big(\sin^2(ct) + \cos^2(ct)\big) = \mathbf{\frac{\pi}{4} A^2 c^2} \quad (\text{hằng số tuyệt đối!}).$$
   Động năng và thế năng liên tục chuyển hóa qua lại cho nhau như con lắc, nhưng tổng năng lượng không hao hụt một giọt nào!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một sợi dây đang dao động vừa có chuyển động ngang (tạo ra động năng nhờ vận tốc) vừa bị kéo căng biến dạng (tạo ra thế năng đàn hồi nhờ độ dốc). Khi dây đi qua vị trí cân bằng, động năng lớn còn thế năng nhỏ; khi dây đạt biên độ cực đại, vận tốc giảm về 0 trong khi thế năng đạt cực đại. Nếu không có ma sát hay ngoại lực, tổng hai phần năng lượng này luôn không đổi.

### Cách nhìn hình ảnh

Khi quan sát hình dạng dây tại các thời điểm liên tiếp, đồ thị dây thay đổi liên tục nhưng tổng mức năng lượng của hệ vẫn giữ nguyên trong bài toán thuần nhất. Năng lượng không tự sinh ra hay mất đi, mà chỉ luân chuyển giữa chuyển động và biến dạng đàn hồi của dây.

### Cách nhìn hình thức

Đối với dây rung một chiều, năng lượng cơ học được định nghĩa là

$$
E(t)=\frac{1}{2}\int_0^L\bigl(\rho u_t^2+T u_x^2\bigr)\,dx.
$$

Với dạng chuẩn hóa $$ u_{tt}=c^2u_{xx} $$, ta viết tương đương

$$
E(t)=\frac{1}{2}\int_0^L\bigl(u_t^2+c^2u_x^2\bigr)\,dx.
$$

Nhân hai vế PDE với $$ u_t $$ rồi tích phân theo $$ x $$ trên $$ [0,L] $$ và áp dụng tích phân từng phần, ta thu được

$$ \frac{dE}{dt}=c^2[u_xu_t]_0^L. $$

Khi số hạng biên bằng 0, năng lượng được bảo toàn:

$$ \frac{dE}{dt}=0. $$

## Những ngộ nhận thường gặp

- "Năng lượng chỉ mang ý nghĩa minh họa vật lý, không dùng để chứng minh toán học." Sai; phương pháp năng lượng là công cụ chứng minh chủ lực của bài học.
- "Phương trình sóng luôn làm năng lượng suy giảm như phương trình nhiệt." Không đúng; với hệ thuần nhất không có tắt dần, tổng cơ năng được bảo toàn.
- "Muốn chứng minh tính duy nhất thì phải tìm được công thức nghiệm tường minh." Không cần thiết; lập luận năng lượng chứng minh tính duy nhất mà không cần viết công thức nghiệm.
- "Nếu năng lượng bằng 0 thì chỉ suy ra vận tốc bằng 0." Sai; từ $$ E(t)=0 $$ ta suy ra cả $$ u_t\equiv 0 $$ lẫn $$ u_x\equiv 0 $$, kết hợp với điều kiện đầu và biên sẽ suy ra nghiệm bằng 0 đồng nhất.

## Tiến trình học tập đề xuất

### Bước 1: Viết biểu thức năng lượng

Nhận diện rõ thành phần động năng (gắn với $$ u_t^2 $$) và thế năng (gắn với $$ u_x^2 $$).

### Bước 2: Nhân PDE với $$ u_t $$

Đây là phép biến đổi cốt lõi tạo ra đạo hàm toàn phần của năng lượng.

### Bước 3: Tích phân từng phần và phân tích số hạng biên

Kiểm tra tác động của điều kiện biên lên sự bảo toàn năng lượng.

### Bước 4: Chứng minh tính duy nhất bằng phương pháp năng lượng

Áp dụng cho hiệu của hai nghiệm cùng thỏa mãn một bài toán biên–đầu.

### Các điểm kiểm tra

- Sinh viên có giải thích được ý nghĩa vật lý của hai số hạng trong biểu thức năng lượng hay không.
- Sinh viên có tính đúng đạo hàm theo thời gian $$ E'(t) $$ hay không.
- Sinh viên có xác định được những loại điều kiện biên nào làm số hạng biên triệt tiêu hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bảo toàn năng lượng với biên cố định

Nếu $$ u(0,t)=u(L,t)=0 $$ với mọi $$ t $$, thì đạo hàm theo thời gian tại biên cũng triệt tiêu: $$ u_t(0,t)=u_t(L,t)=0 $$. Do đó $$ [u_xu_t]_0^L=0 $$ và $$ E'(t)=0 $$. Đây là trường hợp mẫu chuẩn cần nắm vững.

### Ví dụ 2: Chứng minh tính duy nhất của nghiệm

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán phương trình sóng với cùng điều kiện đầu và biên. Đặt $$ w=u_1-u_2 $$. Khi đó $$ w_{tt}=c^2w_{xx} $$ với dữ liệu ban đầu và dữ liệu biên đều bằng 0. Năng lượng của $$ w $$ tại $$ t=0 $$ bằng 0, và nhờ định luật bảo toàn năng lượng, $$ E_w(t)=0 $$ với mọi $$ t $$. Suy ra $$ w_t\equiv 0,\qquad w_x\equiv 0 $$, kết hợp điều kiện đầu cho $$ w\equiv 0 $$, tức $$ u_1\equiv u_2 $$.

### Ví dụ 3: So sánh với phương trình nhiệt

Trong phương trình nhiệt thuần nhất, đại lượng kiểu năng lượng $$ \int u^2\,dx $$ thường giảm dần theo thời gian. Ngược lại, trong phương trình sóng thuần nhất, năng lượng cơ học $$ E(t) $$ được bảo toàn hoàn toàn. Phép so sánh này làm nổi bật sự khác biệt căn bản giữa hai lớp PDE.

### Ví dụ 4: Bảo toàn năng lượng với biên tự do

Với điều kiện biên Neumann $$ u_x(0,t)=u_x(L,t)=0 $$, số hạng biên $$ [u_xu_t]_0^L $$ cũng triệt tiêu. Như vậy cả biên cố định lẫn biên tự do đều bảo toàn năng lượng của hệ.

## Câu hỏi khái niệm

1. Vì sao năng lượng của phương trình sóng được hiểu là tổng của động năng và thế năng đàn hồi?
2. Tại sao số hạng biên giữ vai trò quyết định trong công thức $$ E'(t) $$?
3. Vì sao định luật bảo toàn năng lượng lại dẫn trực tiếp đến tính duy nhất của nghiệm?

## Bài toán ứng dụng

1. Xét một sợi dây đàn lý tưởng không có ma sát. Vì sao tổng năng lượng không thay đổi dù hình dạng dây biến đổi liên tục?
2. Khi bổ sung số hạng tắt dần $$ \gamma u_t $$ ($$ \gamma>0 $$) vào phương trình sóng, năng lượng của hệ biến thiên theo chiều hướng nào?
3. Trong mô phỏng số bài toán sóng, vì sao việc theo dõi giá trị năng lượng theo thời gian là một phép kiểm chứng hữu ích cho độ tin cậy của sơ đồ số?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Khi một sợi dây đang rung, năng lượng của nó tồn tại dưới những dạng nào?"
- Hướng dẫn sinh viên nhân phương trình sóng với $$ u_t $$ và tự suy ra biểu thức năng lượng.
- Đặt câu hỏi: "Những điều kiện biên nào bảo đảm biên không truyền thêm hay rút bớt năng lượng khỏi hệ?"
- Tổ chức hoạt động nhóm để sinh viên tự hoàn thiện phép chứng minh tính duy nhất từ đẳng thức năng lượng.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào trường hợp một chiều với biên cố định trước. Khi đã hiểu rõ từng bước tính $$ E'(t) $$ và vai trò của số hạng biên, việc mở rộng sang các điều kiện biên khác sẽ nhẹ nhàng hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu khái niệm không gian năng lượng cho nghiệm yếu, hoặc liên hệ cấu trúc bảo toàn năng lượng của phương trình sóng với hệ Hamilton trong cơ học giải tích.

## Tóm tắt dễ nhớ

Phương trình sóng thuần nhất với biên bảo toàn thỏa mãn định luật bảo toàn năng lượng, trong đó năng lượng là tổng động năng và thế năng đàn hồi. Đẳng thức năng lượng là công cụ trực tiếp và chặt chẽ để chứng minh tính duy nhất của nghiệm, đồng thời phân biệt rõ phương trình sóng với phương trình nhiệt.

## Video tham khảo

- Xem trước: [Energy Methods for the Wave Equation](https://www.youtube.com/watch?v=fOmON6ubkTM) — Mike, the Mathematician, tiếng Anh. Trình bày phương pháp năng lượng cho phương trình sóng.
- [Lecture 5.4: Qualitative analysis of Wave equation - Uniqueness by Energy method](https://www.youtube.com/watch?v=Sq7DQpaVFbc) — NPTEL IIT Bombay, tiếng Anh. Vận dụng đẳng thức năng lượng để chứng minh tính duy nhất của nghiệm.
- [Energy Method](https://www.youtube.com/watch?v=-8_nuZFVAMQ) — Dr Peyam, tiếng Anh. Giải thích gọn gàng lập luận chứng minh tính duy nhất bằng phương pháp năng lượng.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kiểm chứng mô phỏng dao động
- Bài toán: Trong mô phỏng kết cấu cơ học, kiểm tra bảo toàn năng lượng là tiêu chuẩn quan trọng để đánh giá chất lượng sơ đồ số.
- Mô hình:
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx.
$$
- Giả thiết và giới hạn: Hệ không có ma sát hay tắt dần và thỏa điều kiện biên bảo toàn.
- Diễn giải: Năng lượng luân chuyển giữa động năng và thế năng đàn hồi trong khi tổng không đổi.

#### Tính duy nhất của nghiệm vật lý
- Bài toán: Xác định xem hai nghiệm cùng thỏa mãn một bài toán biên–đầu có bắt buộc trùng nhau hay không.
- Mô hình: Áp dụng phương pháp năng lượng cho hiệu của hai nghiệm.
- Giả thiết và giới hạn: Bài toán tuyến tính, nghiệm đủ trơn để thực hiện phép tích phân từng phần.
- Diễn giải: Bảo toàn năng lượng trực tiếp dẫn tới tính duy nhất.

### 2. Trực giác bổ sung và các kết nối

Phương pháp năng lượng không phụ thuộc vào việc tìm được công thức nghiệm tường minh. Nó khai thác một định luật toàn cục của hệ để chứng minh tính ổn định và tính duy nhất — một kỹ thuật xuất hiện xuyên suốt trong lý thuyết PDE hiện đại.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
kinetic = np.sin(t) ** 2
potential = np.cos(t) ** 2

plt.plot(t, kinetic, label="Dong nang")
plt.plot(t, potential, label="The nang")
plt.plot(t, kinetic + potential, label="Tong nang luong", linewidth=2)
plt.xlabel("t")
plt.title("Trao doi nang luong trong mot mode song")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: wave equation energy conservation animation
- search: uniqueness proof wave equation energy method
- search: numerical wave solver energy drift

### 5. Bài toán mẫu có bối cảnh thực

Với dây cố định hai đầu, lấy đạo hàm theo thời gian của
$$
E(t)=\frac{1}{2}\int_0^L \left(u_t^2+c^2u_x^2\right)\,dx
$$
và áp dụng tích phân từng phần, các số hạng biên triệt tiêu nên $$ E'(t)=0 $$. Nếu hiệu của hai nghiệm có dữ liệu ban đầu bằng 0, năng lượng của hiệu bằng 0 với mọi $$ t $$, suy ra hiệu bằng 0 và nghiệm là duy nhất.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm biểu thức năng lượng như tổng động năng và thế năng đàn hồi, vận dụng để chứng minh tính duy nhất.

**Bậc sau đại học.** Mở rộng sang các ước lượng năng lượng, tính ổn định của nghiệm yếu và phương trình hyperbolic có hệ số biến thiên.
