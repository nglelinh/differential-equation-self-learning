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

Chẳng cần giải ra một công thức nghiệm nào, trực giác vật lý mách bảo ta một điều hiển nhiên: trong một thanh kim loại không có nguồn nhiệt bên trong, **điểm nóng nhất không bao giờ có thể tự dưng bùng lên ở giữa thanh ở thời điểm sau**—nhiệt độ lớn nhất (và nhỏ nhất!) chắc chắn phải nằm ở **trạng thái ban đầu $t = 0$** hoặc trên **hai đầu biên $x = 0, L$**! Phát biểu hình học mộc mạc đó chính là **Nguyên lý Cực đại (Maximum Principle)**—vũ khí chứng minh **tính duy nhất** và **tính ổn định** nghiệm nhanh nhất toàn ngành PDE!

## Kiến thức cần nhớ: Bốn trụ cột của Nguyên lý Cực đại cho Phương trình Nhiệt

1. **Biên Parabol ($\Gamma_T$)**:
   Trên hình chữ nhật không–thời gian $Q_T = (0, L) \times (0, T]$, biên parabol $\Gamma_T$ gồm đúng **3 cạnh**: đáy ban đầu ($t = 0$), vách trái ($x = 0$) và vách phải ($x = L$) — **không bao gồm nắp trên $t = T$**!
2. **Nguyên lý Cực đại Yếu & Cực tiểu**:
   Với $u_t = \alpha u_{xx}$ (không nguồn), $\max_{\overline{Q_T}} u = \max_{\Gamma_T} u$ và $\min_{\overline{Q_T}} u = \min_{\Gamma_T} u$.
3. **Hệ quả 1 — Tính duy nhất nghiệm trong 3 dòng**:
   Nếu $u_1, u_2$ cùng thỏa phương trình, biên và điều kiện đầu, xét hiệu $w = u_1 - u_2$: $w \equiv 0$ trên toàn biên $\Gamma_T \implies 0 \le w(x, t) \le 0$ trên toàn miền $\implies u_1 \equiv u_2$!
4. **Hệ quả 2 — Ổn định liên tục theo dữ liệu (Well-posedness)**:
   Sai số ban đầu $\vert f_1 - f_2 \vert \le \varepsilon$ không bao giờ khuếch đại: $\vert u_1(x, t) - u_2(x, t) \vert \le \varepsilon$ với mọi $(x, t)$!

## Mục tiêu

Bài học này trình bày nguyên lý cực đại — một công cụ định tính quan trọng của phương trình nhiệt. Sau bài học, sinh viên cần nắm phát biểu trực giác và phát biểu hình thức của nguyên lý cực đại, hiểu vì sao nhiệt độ cực đại không thể tự hình thành bên trong miền khi không có nguồn nhiệt, rút ra được hệ quả về tính duy nhất và tính ổn định của nghiệm, đồng thời thấy được cơ sở đảm bảo tính đặt chỉnh của mô hình truyền nhiệt.

## Kiến thức nền

Sinh viên cần nắm phương trình nhiệt, điều kiện cực trị của hàm nhiều biến ở mức cơ bản và ý nghĩa vật lý của quá trình khuếch tán. Bài học này tập trung vào phân tích định tính thay vì tìm công thức nghiệm tường minh.

## Dẫn nhập

Ở các bài trước, ta đã xây dựng nghiệm phương trình nhiệt thông qua chuỗi mode và hàm Green. Tuy nhiên, trong nhiều tình huống ta không cần công thức nghiệm chi tiết mà cần những đánh giá định tính chặt chẽ: nhiệt độ lớn nhất và nhỏ nhất có thể đạt bao nhiêu, và liệu có thể xuất hiện một đỉnh nhiệt mới bên trong miền hay không. Nguyên lý cực đại trả lời trực tiếp các câu hỏi đó.

Kết quả này cho thấy quá trình khuếch tán chịu một ràng buộc chặt chẽ: giá trị nghiệm trên toàn miền được kiểm soát bởi dữ liệu trên biên parabolic chứ không thể tự tăng vọt bên trong. Đây là nền tảng để chứng minh tính duy nhất, tính ổn định và nhiều ước lượng sai số.

### Giải thích: Dùng Nguyên lý Cực đại chặn ngay nhiệt độ và ước lượng sai số đo không cần giải PDE

Giả sử một thanh kim loại dài $1\text{ m}$ có nhiệt độ ban đầu $f(x) = 20 + 60\sin(\pi x)$, đầu trái giữ $20^\circ\text{C}$, đầu phải giữ $40^\circ\text{C}$ ($u_t = \alpha u_{xx}$).
1. **Tìm cực trị trên biên parabol $\Gamma_T$**:
   - Đáy $t = 0$: $f(x) \in [20, 80]$ (đạt cực đại $80^\circ\text{C}$ tại $x = 0{,}5$).
   - Vách trái $x = 0$: $20^\circ\text{C}$. Vách phải $x = 1$: $40^\circ\text{C}$.
2. **Kết luận tức thì cho mọi $(x, t) \in [0, 1] \times [0, \infty)$**:
   $$\mathbf{20^\circ\text{C} \le u(x, t) \le 80^\circ\text{C}}.$$
   Nếu một chương trình mô phỏng số báo ra $u(0{,}3, 2) = 85^\circ\text{C}$ hoặc $18^\circ\text{C}$, bạn biết chắc **100% mã nguồn bị lỗi hoặc mất ổn định số** mà không cần biết nghiệm giải tích!
3. **Ứng dụng ngược (Phương trình nhiệt ngược thời gian là ill-posed!)**: Khi chạy ngược $t < 0$, cực đại ở $t = 0$ không còn chặn được quá khứ—nhiễu $10^{-6}$ lập tức bùng nổ thành vô cùng!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một vùng bên trong vật thể nóng hơn mọi điểm xung quanh, nhiệt sẽ truyền từ vùng đó ra ngoài. Do đó, một đỉnh nhiệt bên trong miền sẽ có xu hướng hạ xuống thay vì tự tăng cao hơn nữa; tương tự, một vùng lạnh cục bộ sẽ được lấp ấm dần lên. Đó là ý nghĩa vật lý trực tiếp của nguyên lý cực đại.

### Cách nhìn hình ảnh

Xét đồ thị nhiệt độ trong miền không gian–thời gian. Nếu tồn tại một điểm cực đại thực sự bên trong miền, đạo hàm theo thời gian tại điểm đó phải không âm, trong khi đạo hàm bậc hai theo không gian phải không dương. Phương trình nhiệt liên kết trực tiếp hai đạo hàm này và dẫn tới ràng buộc rất chặt, thậm chí mâu thuẫn khi cực đại là ngặt. Việc loại trừ các cực trị mới bên trong miền chính là nội dung hình học của nguyên lý cực đại.

### Cách nhìn hình thức

Xét phương trình $$ u_t=\alpha^2u_{xx} $$ trên miền parabolic $$ Q_T=(0,L)\times(0,T] $$. Biên parabolic của miền này là

$$
\Gamma_T=\bigl([0,L]\times\{0\}\bigr)\cup\bigl(\{0,L\}\times[0,T]\bigr).
$$

Nguyên lý cực đại yếu phát biểu rằng nếu $$ u $$ liên tục trên $$ \overline{Q_T} $$ và đủ trơn trong $$ Q_T $$, thì $$ \max_{\overline{Q_T}}u=\max_{\Gamma_T}u $$. Một khẳng định tương tự cũng đúng cho giá trị cực tiểu.

## Những ngộ nhận thường gặp

- "Nguyên lý cực đại chỉ là một nhận xét hình học mang tính trực giác." Sai; đây là một định lý chặt chẽ với nhiều hệ quả quan trọng.
- "Không có công thức nghiệm tường minh thì không thể kết luận gì về nghiệm." Không đúng; nguyên lý cực đại cho biết các chặn định tính chính xác mà không cần giải tường minh.
- "Nhiệt độ cực đại bên trong miền có thể tự tăng lên." Với phương trình nhiệt thuần nhất không có nguồn, điều này không thể xảy ra.
- "Nguyên lý cực đại chỉ có ý nghĩa lý thuyết." Sai; tính duy nhất nghiệm và nhiều ước lượng ổn định đều dựa trực tiếp vào nguyên lý này.

## Tiến trình học tập đề xuất

### Bước 1: Hiểu khái niệm biên parabolic

Phân biệt rõ biên parabolic trong không gian–thời gian với biên hình học thông thường (chú ý nắp trên $$ t=T $$ không nằm trong biên parabolic).

### Bước 2: Giả sử tồn tại cực đại bên trong miền

Đây là bước khởi đầu của lập luận chứng minh.

### Bước 3: Sử dụng dấu của các đạo hàm tại điểm cực trị

Chuyển trực giác hình học thành đánh giá dấu trong phương trình nhiệt.

### Bước 4: Suy ra tính duy nhất và tính ổn định

Vận dụng nguyên lý cực đại cho hiệu của hai nghiệm.

### Các điểm kiểm tra

- Sinh viên có mô tả chính xác biên parabolic bằng lời hay không.
- Sinh viên có giải thích được vì sao cực trị bên trong miền dẫn đến mâu thuẫn dấu trong PDE hay không.
- Sinh viên có vận dụng được nguyên lý cực đại để chứng minh tính duy nhất của nghiệm hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Kiểm tra dấu tại cực đại bên trong miền

Giả sử $$ u $$ đạt cực đại tại một điểm $$ (x_0,t_0)\in Q_T $$ với $$ t_0>0 $$. Khi đó

$$
u_x(x_0,t_0)=0,
\qquad
u_{xx}(x_0,t_0)\le 0,
\qquad
u_t(x_0,t_0)\ge 0.
$$

Tuy nhiên, từ phương trình nhiệt $$ u_t=\alpha^2u_{xx} $$, ta lại có $$ u_t(x_0,t_0)\le 0 $$. Suy ra $$ u_t(x_0,t_0)=0,\qquad u_{xx}(x_0,t_0)=0 $$. Bằng phép nhiễu nhẹ (như xét $$ v(x,t)=u(x,t)-\varepsilon t $$) hoặc lập luận nguyên lý cực đại mạnh, ta chứng minh được cực đại phải đạt được trên biên parabolic. Đây là bước lập luận trung tâm của bài học.

### Ví dụ 2: Tính duy nhất của nghiệm

Giả sử $$ u_1,\ u_2 $$ là hai nghiệm của cùng một bài toán truyền nhiệt với cùng điều kiện ban đầu và điều kiện biên. Đặt $$ w=u_1-u_2 $$. Khi đó $$ w_t=\alpha^2w_{xx} $$ và $$ w=0 $$ trên biên parabolic $$ \Gamma_T $$. Áp dụng nguyên lý cực đại cho $$ w $$ và $$ -w $$, ta suy ra $$ w\equiv 0 $$, tức $$ u_1\equiv u_2 $$. Đây là ứng dụng quan trọng nhất cần nắm vững.

### Ví dụ 3: Tính ổn định theo dữ liệu biên và dữ liệu đầu

Nếu dữ liệu ban đầu và dữ liệu biên của hai bài toán chỉ sai khác nhau rất nhỏ, hiệu hai nghiệm tương ứng bị chặn trên toàn miền bởi mức sai khác cực đại trên biên parabolic. Điều này khẳng định bài toán truyền nhiệt không chỉ có nghiệm duy nhất mà còn ổn định theo dữ liệu đầu vào.

### Ví dụ 4: Diễn giải vật lý

Nếu tại thời điểm ban đầu và dọc theo hai biên, nhiệt độ luôn nằm trong đoạn $$ [m,M] $$, thì tại mọi điểm và mọi thời điểm tiếp theo, nhiệt độ trong thanh cũng không thể vượt ra ngoài đoạn $$ [m,M] $$. Đây là cách phát biểu vật lý ngắn gọn và dễ nhớ nhất của nguyên lý cực đại.

## Câu hỏi khái niệm

1. Vì sao biên parabolic lại bao gồm thời điểm ban đầu $$ t=0 $$ nhưng không bao gồm thời điểm cuối $$ t=T $$?
2. Nguyên lý cực đại phản ánh trực giác vật lý "nhiệt không tự sinh ra đỉnh nóng mới" như thế nào?
3. Vì sao nguyên lý cực đại lại trực tiếp kéo theo tính duy nhất của nghiệm?

## Bài toán ứng dụng

1. Trong mô phỏng số phương trình nhiệt, vì sao việc sơ đồ số sinh ra các đỉnh nhiệt độ mới bên trong miền thường là dấu hiệu bất ổn định?
2. Nếu dữ liệu ban đầu và dữ liệu biên đều không âm, vì sao nghiệm của bài toán nhiệt thuần nhất cũng luôn không âm?
3. Trong bài toán kiểm soát nhiệt, nguyên lý cực đại giúp thiết lập các ngưỡng an toàn cho nhiệt độ mà không cần giải tường minh PDE như thế nào?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Một đỉnh nhiệt bên trong miền có thể tự tăng cao hơn nữa khi không có nguồn nhiệt hay không?"
- Dùng lập luận kiểm tra dấu đạo hàm tại điểm cực trị làm hoạt động để sinh viên tự hoàn thiện.
- Đặt câu hỏi: "Phần biên nào của miền không gian–thời gian thực sự kiểm soát nghiệm của phương trình nhiệt?"
- Cho sinh viên thảo luận theo cặp để tự chứng minh tính duy nhất của nghiệm từ nguyên lý cực đại.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám sát trực giác "đỉnh hạ xuống, hõm lấp lên" trước khi trình bày phát biểu hình thức. Khi trực giác vật lý đã rõ, lập luận bằng dấu của đạo hàm sẽ dễ theo dõi hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu nguyên lý cực đại mạnh, hoặc phân tích vì sao phương trình sóng không thỏa mãn một nguyên lý cực đại tương tự phương trình nhiệt.

## Tóm tắt dễ nhớ

Nguyên lý cực đại khẳng định nghiệm của phương trình nhiệt thuần nhất bị kiểm soát hoàn toàn bởi dữ liệu ban đầu và biên không gian (biên parabolic). Không thể có cực đại hay cực tiểu mới tự sinh ra bên trong miền, từ đó suy ra ngay tính duy nhất và tính ổn định của nghiệm.

## Video tham khảo

- Xem trước: [Lecture 7.4: Maximum principle for heat equation](https://www.youtube.com/watch?v=JbBt6mPAqLM) — NPTEL IIT Bombay, tiếng Anh. Trình bày và chứng minh nguyên lý cực đại cho phương trình nhiệt.
- [Lecture 6: The maximum principle for the diffusion equation](https://www.youtube.com/watch?v=zO6D-2ER6oY) — math 442 f20, tiếng Anh. Bài giảng chi tiết về nguyên lý cực đại cho phương trình khuếch tán.
- [Maximum Principle](https://www.youtube.com/watch?v=PMjzGEPkQt8) — Dr Peyam, tiếng Anh. Giải thích trực quan nguyên lý cực đại và ý nghĩa việc loại trừ cực trị bên trong miền.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Giới hạn nhiệt độ cực đại
- Bài toán: Khi không có nguồn nhiệt bên trong, nhiệt độ trong miền không thể vượt quá giá trị lớn nhất trên biên parabolic.
- Mô hình: Áp dụng nguyên lý cực đại cho
$$ u_t-\alpha^2 u_{xx}=0. $$
- Giả thiết và giới hạn: Miền chính quy, nghiệm liên tục trên miền đóng và đủ trơn bên trong miền.
- Diễn giải: Cực đại bên trong miền không thể xảy ra trừ khi nghiệm là hàm hằng theo nghĩa thích hợp.

#### Tính duy nhất của nghiệm
- Bài toán: Chứng minh bài toán truyền nhiệt với cùng dữ kiện đầu và biên chỉ có duy nhất một nghiệm.
- Mô hình: Áp dụng nguyên lý cực đại cho hiệu của hai nghiệm.
- Giả thiết và giới hạn: Điều kiện biên và điều kiện ban đầu đặt đúng quy cách.
- Diễn giải: Các tính chất định tính như tính duy nhất và ổn định có vai trò quan trọng không kém công thức nghiệm tường minh.

### 2. Trực giác bổ sung và các kết nối

Nguyên lý cực đại là minh họa điển hình cho việc phân tích PDE bằng cấu trúc định tính thay vì tìm biểu thức nghiệm tường minh. Đây không chỉ là một công cụ chứng minh lý thuyết mà còn phản ánh trực tiếp bản chất vật lý của quá trình khuếch tán thuần túy.

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

Nếu $$ u $$ là nghiệm của bài toán nhiệt thuần nhất trên đoạn với dữ kiện ban đầu và điều kiện biên đều bằng $$ 0 $$, nguyên lý cực đại cho $$ u\le 0 $$, và áp dụng cho $$ -u $$ cho $$ u\ge 0 $$. Suy ra $$ u\equiv 0 $$, khẳng định tính duy nhất của nghiệm.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm phát biểu nguyên lý cực đại và vận dụng để chứng minh tính duy nhất của nghiệm.

**Bậc sau đại học.** Mở rộng sang nguyên lý cực đại yếu và mạnh trên miền nhiều chiều cho các toán tử parabolic tổng quát.
