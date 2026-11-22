---
layout: post
title: "01-09 Phương trình Tự trị và Đường Pha"
chapter: '01'
order: 9
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: optional
---

## Mục tiêu
Bài học này giúp sinh viên phân tích hành vi định tính của một phương trình vi phân tự trị cấp một mà không cần giải ra công thức nghiệm tường minh. Sau bài học, sinh viên có thể xác định các điểm cân bằng, sử dụng dấu của $$ f(y) $$ để dựng đường pha, phân loại tính ổn định và hiểu vì sao phân tích định tính là công cụ cốt lõi khi nghiệm dạng đóng khó tìm hoặc không cần thiết.

## Kiến thức nền
Sinh viên cần nắm dạng phương trình cấp một tự trị $$ y'=f(y) $$, khái niệm nghiệm cân bằng và kỹ năng xét dấu biểu thức đại số. Nền tảng từ phương trình logistic và tách biến sẽ giúp chuyển tiếp tự nhiên từ "tìm công thức nghiệm" sang "phân tích động lực học".

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-09 Phương trình Tự trị và Đường Pha]({{ site.imgurl }}/chapter_img/chapter01/01_09_autonomous_equations.svg)

Không phải lúc nào ta cũng cần công thức nghiệm tường minh để hiểu một hệ động lực. Chỉ cần biết tại mỗi giá trị trạng thái $$ y $$ thì hệ đang tăng hay giảm, ta đã có thể dự đoán hành vi dài hạn, xác định các ngưỡng chuyển trạng thái và phân loại các điểm cân bằng. Đây là bước chuyển tư duy quan trọng từ tính toán công thức sang phân tích cấu trúc định tính.

Phương trình tự trị là điểm khởi đầu lý tưởng cho tư duy này vì vế phải chỉ phụ thuộc vào trạng thái hiện tại $$ y $$ mà không phụ thuộc tường minh vào thời gian $$ t $$. Nhờ vậy, toàn bộ động lực học có thể biểu diễn gọn trên một trục một chiều gọi là đường pha (phase line).

## Khái niệm theo ba cách

### Cách nhìn trực quan
Hãy hình dung một hạt chuyển động trên một đường thẳng: tại mỗi vị trí, ta biết hạt đang bị đẩy sang phải hay sang trái. Những vị trí mà hạt đứng yên là các điểm cân bằng. Nếu các mũi tên hai bên đều hướng vào điểm cân bằng thì điểm đó ổn định; nếu hướng ra xa thì không ổn định.

### Cách nhìn hình ảnh
Trên trục thẳng đứng biểu diễn biến trạng thái $$ y $$, chiều biến thiên của nghiệm phương trình $$ y'=f(y) $$ được xác định hoàn toàn bởi dấu của $$ f(y) $$:

- Nếu $$ f(y)>0 $$, nghiệm tăng (mũi tên hướng lên).
- Nếu $$ f(y)<0 $$, nghiệm giảm (mũi tên hướng xuống).
- Nếu $$ f(y)=0 $$, ta có điểm cân bằng (nghiệm hằng).

Các mũi tên trên đường pha cô đọng thông tin định tính của cả họ đường cong nghiệm trên mặt phẳng $$ \left(t,y\right) $$.

### Cách nhìn hình thức
Với phương trình tự trị

$$
\frac{dy}{dt}=f(y),
$$

giá trị $$ y_* $$ được gọi là điểm cân bằng nếu $$ f(y_*)=0 $$. Một điểm cân bằng là ổn định nếu các quỹ đạo xuất phát đủ gần $$ y_* $$ luôn ở gần và tiến về $$ y_* $$. Trong trường hợp một chiều, ta phân loại trực tiếp bằng dấu của $$ f(y) $$ ở hai phía của $$ y_* $$:

- Nếu mũi tên hai phía đều hướng vào $$ y_* $$, điểm cân bằng ổn định (hút).
- Nếu mũi tên hai phía đều hướng ra khỏi $$ y_* $$, điểm cân bằng không ổn định (đẩy).
- Nếu một phía hướng vào và phía kia hướng ra, điểm cân bằng bán ổn định.

## Ý nghĩa toán học cốt lõi
Phân tích đường pha cho thấy hành vi dài hạn của hệ tự trị một chiều được quyết định bởi các điểm cân bằng và dấu của $$ f(y) $$ trên các khoảng nằm giữa chúng. Ngay cả khi không cần tốc độ hội tụ chi tiết, ta vẫn xác định được trạng thái giới hạn của mọi điều kiện đầu—điều rất hữu ích trong các mô hình sinh học, hóa học và kinh tế.

Đường pha cũng giới thiệu góc nhìn không gian trạng thái: xem nghiệm không chỉ là đồ thị theo thời gian mà là quỹ đạo chuyển động trong không gian trạng thái, mở đường trực tiếp sang chân dung pha của hệ ODE nhiều chiều và phân tích ổn định phi tuyến.

## Những ngộ nhận thường gặp
- "Phải giải ra công thức nghiệm rồi mới xét được tính ổn định." Sai. Với phương trình tự trị một chiều, tính ổn định đọc trực tiếp từ dấu của $$ f(y) $$ quanh từng điểm cân bằng.
- "Mọi điểm cân bằng đều ổn định." Sai. Điểm cân bằng có thể đẩy các quỹ đạo lân cận ra xa (không ổn định) hoặc chỉ hút từ một phía (bán ổn định).
- "Nếu $$ f(y)>0 $$ tại một điểm thì nghiệm tăng ra vô cực." Sai. Nghiệm chỉ tăng trong khoảng mà $$ f(y)>0 $$ và sẽ bị chặn lại bởi điểm cân bằng nằm phía trên khoảng đó (nếu có).
- "Đường pha chỉ là hình minh họa phụ." Sai. Đây là công cụ phân tích định tính chặt chẽ cho mọi phương trình tự trị một chiều.

## Tiến trình học tập đề xuất

### Bước 1: Tìm điểm cân bằng
Giải phương trình đại số $$ f(y)=0 $$.

### Bước 2: Chia trục trạng thái thành các khoảng
Các điểm cân bằng chia trục $$ y $$ thành các khoảng rời nhau trên đó $$ f(y) $$ giữ nguyên dấu (khi $$ f $$ liên tục).

### Bước 3: Xét dấu trên từng khoảng
Chọn điểm thử trong mỗi khoảng để xác định dấu của $$ f(y) $$ và chiều mũi tên tương ứng.

### Bước 4: Kết luận tính ổn định và hành vi dài hạn
Phân loại từng điểm cân bằng (ổn định, không ổn định, bán ổn định) và đọc giới hạn khi $$ t\to\infty $$ cho từng miền điều kiện đầu.

### Các checkpoint
- Bạn có tìm đủ tất cả các điểm cân bằng của $$ f(y)=0 $$ không?
- Bạn có kiểm tra dấu của $$ f(y) $$ trên từng khoảng thay vì chỉ đoán theo hệ số bậc cao nhất không?
- Bạn có phân biệt chính xác ba loại cân bằng: ổn định, không ổn định và bán ổn định không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phương trình logistic cổ điển
Xét phương trình

$$
\frac{dy}{dt}=y(1-y).
$$

Các điểm cân bằng là $$ y=0 $$ và $$ y=1 $$. Xét dấu trên ba khoảng:

- Với $$ y<0 $$, ta có $$ y<0 $$ và $$ 1-y>0 $$ nên $$ y'<0 $$.
- Với $$ 0<y<1 $$, ta có $$ y'>0 $$.
- Với $$ y>1 $$, ta có $$ 1-y<0 $$ nên $$ y'<0 $$.

Do đó mũi tên hướng ra khỏi $$ 0 $$ và hướng vào $$ 1 $$. Vậy $$ y=0 $$ không ổn định, còn $$ y=1 $$ ổn định—cho thấy ngay vai trò sức chứa của $$ y=1 $$ mà không cần giải tường minh.

### Ví dụ 2: Điểm cân bằng bán ổn định
Xét phương trình

$$
\frac{dy}{dt}=y^2.
$$

Điểm cân bằng duy nhất là $$ y=0 $$. Với mọi $$ y\neq 0 $$, ta đều có $$ y^2>0 $$ nên mũi tên cả hai phía đều hướng lên: nghiệm xuất phát với $$ y_0<0 $$ tăng dần tiến về $$ 0 $$, còn nghiệm xuất phát với $$ y_0>0 $$ tăng rời xa $$ 0 $$. Vì vậy $$ y=0 $$ là điểm cân bằng bán ổn định.

### Ví dụ 3: Nhiều điểm cân bằng
Xét phương trình

$$
\frac{dy}{dt}=y(y-1)(2-y).
$$

Các điểm cân bằng là $$ y=0 $$, $$ y=1 $$ và $$ y=2 $$. Xét dấu trên bốn khoảng:

- Với $$ y<0 $$: tích dương, nên $$ y'>0 $$.
- Với $$ 0<y<1 $$: tích âm, nên $$ y'<0 $$.
- Với $$ 1<y<2 $$: tích dương, nên $$ y'>0 $$.
- Với $$ y>2 $$: tích âm, nên $$ y'<0 $$.

Mũi tên hướng vào $$ 0 $$, ra khỏi $$ 1 $$ và hướng vào $$ 2 $$. Do đó $$ y=0 $$ và $$ y=2 $$ ổn định, còn $$ y=1 $$ không ổn định.

### Ví dụ 4: Mô hình logistic có thu hoạch
Xét mô hình

$$
\frac{dy}{dt}=y(1-y)-h,
$$

trong đó $$ h>0 $$ là mức thu hoạch không đổi. Khi thay đổi tham số $$ h $$, số lượng và vị trí các điểm cân bằng có thể thay đổi (khi $$ h $$ vượt quá $$ 1/4 $$, hai điểm cân bằng biến mất hoàn toàn). Ví dụ này mở đầu trực quan cho khái niệm phân nhánh (bifurcation): một thay đổi nhỏ ở tham số có thể làm đổi hẳn cấu trúc định tính của hệ.

## Câu hỏi khái niệm
1. Vì sao chỉ cần dấu của $$ f(y) $$ là đủ xác định chiều chuyển động trên đường pha?
2. Vì sao ta có thể kết luận tính ổn định của điểm cân bằng mà không cần giải tường minh phương trình?
3. Điểm cân bằng bán ổn định khác điểm ổn định và không ổn định ở đặc điểm nào?

## Bài toán ứng dụng
1. Trong mô hình quần thể có thu hoạch hằng số, vì sao khi mức khai thác vượt một ngưỡng nhất định thì quần thể không còn điểm cân bằng dương nào?
2. Trong một phản ứng hóa học có nhiều nồng độ cân bằng, đường pha giúp dự đoán nồng độ cuối cùng từ nồng độ ban đầu như thế nào?
3. Trong kinh tế học, một biến thị trường có hai trạng thái cân bằng ổn định ngăn cách bởi một ngưỡng không ổn định gợi ý điều gì cho việc ra quyết định?

## Chiến lược giảng dạy tương tác
- Yêu cầu sinh viên dựng đường pha trước khi giải đại số, kể cả với phương trình logistic đã quen.
- Chia nhóm nhỏ phân tích các phương trình tự trị khác nhau rồi biểu diễn mũi tên đường pha lên bảng để so sánh.
- Thường xuyên hỏi nhanh: "Nếu trạng thái ban đầu nằm trong khoảng này, nghiệm sẽ tăng hay giảm và tiến về đâu?"
- Dùng màu sắc phân biệt các khoảng dương và âm trên trục trạng thái để trực quan hóa cấu trúc động lực học.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng bảng xét dấu ba cột gồm: khoảng giá trị của $$ y $$, dấu của $$ f(y) $$ và chiều mũi tên tương ứng, giúp lập luận chặt chẽ và tránh nhầm lẫn.

### Thử thách cho sinh viên khá giỏi
Liên hệ dấu của đạo hàm $$ f'(y_*) $$ với tính ổn định của điểm cân bằng (tiêu chuẩn tuyến tính hóa) và khảo sát sự thay đổi của đường pha theo tham số $$ h $$ (giới thiệu sơ đồ phân nhánh).

## Tóm tắt dễ nhớ
Với phương trình tự trị $$ y'=f(y) $$, quy trình phân tích gồm ba bước: tìm điểm cân bằng từ $$ f(y)=0 $$, xét dấu $$ f(y) $$ trên từng khoảng và vẽ mũi tên trên đường pha để đọc ngay tính ổn định và giới hạn dài hạn mà không cần công thức nghiệm.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khai thác sinh học có ngưỡng sụp đổ
- Bài toán: Một quần thể cá bị khai thác với tốc độ đều mỗi mùa; cần xác định ngưỡng khai thác bền vững.
- Mô hình:

$$
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)-h.
$$

- Giả thiết và giới hạn: Mức khai thác $$ h $$ không đổi và quần thể đồng nhất; bỏ qua yếu tố mùa vụ, cấu trúc tuổi và biến động môi trường.
- Diễn giải: Đường pha chỉ rõ sự tồn tại của ngưỡng cân bằng không ổn định: nếu quần thể tụt xuống dưới ngưỡng này sẽ suy kiệt dần, còn ở trên ngưỡng sẽ phục hồi về cân bằng ổn định.

#### Điều chỉnh giá về cân bằng thị trường
- Bài toán: Giá hàng hóa biến thiên theo độ lệch giữa cung và cầu tại từng mức giá.
- Mô hình:

$$
\frac{dp}{dt}=f(p).
$$

- Giả thiết và giới hạn: Giả sử cơ chế điều chỉnh giá phản ứng tức thời và thị trường mô tả được bằng một biến giá duy nhất; thực tế có độ trễ, kỳ vọng và nhiều hàng hóa liên kết.
- Diễn giải: Đường pha cho biết ngay giá cân bằng có khả năng tự điều chỉnh (ổn định) hay dễ lệch xa (không ổn định).

#### Phản ứng hóa học với đa trạng thái ổn định
- Bài toán: Một lò phản ứng có thể ổn định ở chế độ nhiệt thấp hoặc nhiệt cao tùy thuộc điều kiện khởi động.
- Mô hình đơn giản:

$$
\frac{dy}{dt}=f(y),
$$

trong đó $$ f(y) $$ có nhiều nghiệm thực.
- Giả thiết và giới hạn: Đây là mô hình rút gọn một chiều từ hệ nhiều biến, nhưng vẫn giữ lại đặc trưng đa ổn định và ngưỡng chuyển trạng thái.
- Diễn giải: Đường pha làm rõ cấu trúc đa ổn định mà không cần giải công thức tường minh.

### 2. Trực giác bổ sung và các kết nối

Phương trình tự trị mở ra cách tiếp cận định tính cho động lực học, vốn trở thành trọng tâm ở các chương hệ ODE, ổn định phi tuyến và phân nhánh (bifurcation). Cần tránh sai lầm chỉ kiểm tra dấu của $$ f(y) $$ tại một điểm đơn lẻ mà bỏ sót khoảng giữa các điểm cân bằng: phải xét đầy đủ mọi khoảng do các nghiệm của $$ f(y)=0 $$ chia ra.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

f = lambda t, y: y * (1 - y) * (y - 0.3)
t_eval = np.linspace(0, 20, 400)

for y0 in [0.1, 0.25, 0.5, 1.2]:
    sol = solve_ivp(f, [0, 20], [y0], t_eval=t_eval, max_step=0.1)
    plt.plot(sol.t, sol.y[0], label=f"y0={y0}")

plt.axhline(0, color="black", linestyle=":")
plt.axhline(0.3, color="black", linestyle="--")
plt.axhline(1, color="black", linestyle=":")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Quỹ đạo cho một phương trình tự trị có ngưỡng")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy rõ vai trò của ngưỡng không ổn định $$ y=0.3 $$: các quỹ đạo xuất phát dưới $$ 0.3 $$ bị kéo về $$ 0 $$, còn các quỹ đạo xuất phát trên $$ 0.3 $$ hội tụ về $$ 1 $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: autonomous equation phase line interactive
- search: harvesting logistic bifurcation
- search: Allee effect phase line simulation

### 5. Bài toán mẫu có bối cảnh thực

Xét mô hình thu hoạch đã chuẩn hóa

$$
\frac{dx}{dt}=x(1-x)-0.16.
$$

Các điểm cân bằng là nghiệm của $$ x^2-x+0.16=0 $$, tức $$ x=0.2 $$ và $$ x=0.8 $$. Xét dấu cho thấy $$ x=0.2 $$ là cân bằng không ổn định còn $$ x=0.8 $$ là cân bằng ổn định: nếu mật độ quần thể giảm xuống dưới ngưỡng $$ 0.2 $$, mức khai thác hiện tại vượt quá khả năng tái tạo khiến quần thể suy giảm về $$ 0 $$; nếu ở trên $$ 0.2 $$, quần thể phục hồi về mức $$ 0.8 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Tìm điểm cân bằng, vẽ đường pha và suy luận hành vi dài hạn từ dấu của $$ f(y) $$.

**Bậc sau đại học.** Kết nối với tiêu chuẩn đạo hàm $$ f'(y_*) $$, phân nhánh một tham số (bifurcation), tính ổn định cấu trúc và hàm Lyapunov một chiều.

## Video tham khảo

- Xem trước: [Autonomous Equations, Equilibrium Solutions, and Stability](https://www.youtube.com/watch?v=pZOmToxx-R8) — Dr. Trefor Bazett, tiếng Anh. Trình bày nghiệm cân bằng và phân loại tính ổn định từ đường pha.
- [Autonomous Equations and Phase Lines | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=elMskF8Uzmg) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về phương trình tự trị và đường pha.
- [MAE5790-2 One dimensional Systems](https://www.youtube.com/watch?v=YNIm2Op7UPg) — Cornell MAE, tiếng Anh. Bài giảng của Strogatz về hệ động lực một chiều theo cách nhìn hình học.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ phương trình tự trị và đường pha.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập rèn kỹ năng xét dấu và phân loại ổn định một chiều.
- Strogatz — *Nonlinear Dynamics and Chaos*: trình bày trực giác hình học sâu sắc về đường pha, điểm cân bằng và phân tích định tính.
