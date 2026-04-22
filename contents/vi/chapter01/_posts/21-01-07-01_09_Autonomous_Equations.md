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
Bài học này giúp sinh viên đọc được hành vi định tính của một ODE tự trị mà không cần giải tường minh. Sinh viên sẽ học cách xác định điểm cân bằng, dùng dấu của $$ f(y) $$ để vẽ đường pha, phân loại ổn định, và hiểu vì sao phân tích định tính là công cụ không thể thiếu khi công thức nghiệm khó tìm hoặc không cần thiết.

## Kiến thức nền
Sinh viên cần biết phương trình cấp một dạng
$$ y'=f(y), $$
khái niệm nghiệm cân bằng và kỹ năng phân tích dấu của một biểu thức. Nếu đã học logistic và một số phương trình tách biến, sinh viên sẽ thấy bài học này như bước chuyển từ "giải công thức" sang "đọc động lực học".

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-09 Phương trình Tự trị và Đường Pha]({{ site.imgurl }}/chapter_img/chapter01/01_09_autonomous_equations.svg)

Không phải lúc nào ta cũng cần công thức nghiệm để hiểu một hệ động. Nếu biết tại mỗi mức trạng thái $$ y $$ thì hệ tăng hay giảm, ta đã có thể dự đoán tương lai dài hạn, phát hiện ngưỡng ổn định và hiểu vai trò của các điểm cân bằng. Đây là một thay đổi rất quan trọng trong tư duy toán học: từ tính toán chính xác sang phân tích cấu trúc.

Phương trình tự trị là nơi lý tưởng để bắt đầu tư duy ấy, vì vế phải chỉ phụ thuộc vào trạng thái hiện tại. Điều này cho phép ta nghiên cứu động lực trên một trục một chiều gọi là trục pha. Dù công cụ cực kỳ đơn giản, nó mở ra cánh cửa vào lý thuyết động lực học và ổn định ở các chương sau.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy tưởng tượng một hạt chuyển động trên một sợi dây thẳng. Tại mỗi vị trí, ta biết nó có xu hướng đi sang phải hay sang trái. Nếu ở một vị trí nào đó nó đứng yên, đó là điểm cân bằng. Nếu các mũi tên xung quanh hướng vào điểm đó, nó ổn định; nếu hướng ra, nó không ổn định.

### Cách nhìn hình ảnh
Ta vẽ trục thẳng đứng cho biến trạng thái $$ y $$. Các nghiệm của
$$ y'=f(y) $$
được quyết định bởi dấu của $$ f(y) $$:

- Nếu $$ f(y)>0 $$, nghiệm đi lên theo thời gian.
- Nếu $$ f(y)<0 $$, nghiệm đi xuống theo thời gian.
- Nếu $$ f(y)=0 $$, ta có điểm cân bằng.

Các mũi tên trên trục pha vì thế thay thế cho việc phải vẽ cả họ nghiệm trên mặt phẳng $$ \left(t,y\right) $$.

### Cách nhìn hình thức
Với phương trình tự trị
$$ \frac{dy}{dt}=f(y), $$
giá trị $$ y_*$ được gọi là điểm cân bằng nếu $$
f(y_*)=0.
$$
Điểm cân bằng ổn định nếu các nghiệm bắt đầu gần đó vẫn ở gần và thường tiến về đó. Trong thực hành của chương này, ta thường xét dấu của $$f(y)$$ ở hai phía:
- Nếu mũi tên hai bên hướng vào $$y_*$$
, cân bằng ổn định.
- Nếu mũi tên hai bên hướng ra, cân bằng không ổn định.
- Nếu một bên vào, một bên ra, cân bằng bán ổn định.
## Ý nghĩa toán học cốt lõi
Phân tích đường pha cho thấy hành vi dài hạn của hệ thường được quyết định bởi các điểm cân bằng và dấu của
$$f(y)$$
giữa chúng. Ta không cần biết chính xác nghiệm tiến về cân bằng theo tốc độ nào để vẫn hiểu rõ xu hướng của hệ. Đây là lý do phương pháp này đặc biệt mạnh trong mô hình hóa sinh học, hóa học và xã hội, nơi công thức tường minh không phải lúc nào cũng cần thiết.
Đường pha cũng là cơ hội để nhấn mạnh rằng nghiệm của ODE không chỉ là đồ thị theo thời gian, mà là quỹ đạo trong không gian trạng thái. Đây là ý tưởng sẽ lớn dần lên ở chương về hệ ODE và ổn định phi tuyến.
## Những ngộ nhận thường gặp
- "Phải giải được nghiệm rồi mới phân tích ổn định." Sai. Với phương trình tự trị một chiều, nhiều kết luận định tính đến trực tiếp từ dấu của
$$f(y)$$
.
- "Điểm cân bằng luôn ổn định." Sai. Có điểm cân bằng đẩy nghiệm ra xa.
- "Nếu
$$f(y)$$ dương thì mọi nghiệm đều tăng mãi." Chưa chắc; còn phải xét miền mà $$f(y)$$
dương và các điểm cân bằng chặn hai đầu.
- "Đường pha chỉ là hình vẽ minh họa." Sai. Nó là công cụ phân tích chính xác cho hành vi định tính.
## Tiến trình học tập đề xuất
### Bước 1: Tìm điểm cân bằng
Giải
$$
f(y)=0.
$$
### Bước 2: Chia trục thành các khoảng
Các điểm cân bằng chia trục trạng thái thành nhiều khoảng rời.
### Bước 3: Kiểm tra dấu trên từng khoảng
Chọn điểm thử để xác định chiều mũi tên.
### Bước 4: Kết luận về ổn định và hành vi dài hạn
Không cần giải công thức cũng có thể nói nghiệm sẽ tiến về đâu.
### Các checkpoint
- Sinh viên có tìm đủ các điểm cân bằng hay không.
- Sinh viên có kiểm tra dấu theo từng khoảng thay vì chỉ nhìn hệ số đầu hay không.
- Sinh viên có phân biệt được ổn định, không ổn định và bán ổn định hay không.
## Ví dụ được giải chi tiết
### Ví dụ 1: Logistic cổ điển
Xét
$$
\frac{dy}{dt}=y(1-y).
$$ Các điểm cân bằng là $$
y=0,\qquad y=1.
$$ Xét dấu:
- Nếu $$y<0$$ , thì $$y<0$$ và $$1-y>0$$ nên $$y'<0$$ .
- Nếu $$0<y<1$$ , thì $$y'>0$$ .
- Nếu $$y>1$$ , thì $$1-y<0$$ nên $$y'<0$$ .
Vì vậy mũi tên hướng ra khỏi $$0$$ và hướng vào $$1$$ . Kết luận: $$y=0$$ không ổn định, còn $$y=1$$
ổn định. Ta hiểu ngay sức chứa của hệ mà không cần công thức nghiệm logistic.
### Ví dụ 2: Cân bằng bán ổn định
Xét
$$
\frac{dy}{dt}=y^2.
$$ Điểm cân bằng duy nhất là $$
y=0.
$$ Với mọi $$y\neq 0$$ , ta có $$y^2>0$$
nên mũi tên đều hướng lên. Vì vậy nghiệm ở bên trái tăng về 0, còn nghiệm ở bên phải lại đi xa khỏi 0. Điểm này bán ổn định: hút từ một phía nhưng đẩy từ phía còn lại.
### Ví dụ 3: Nhiều điểm cân bằng
Xét
$$
\frac{dy}{dt}=y(y-1)(2-y).
$$ Các điểm cân bằng: $$
y=0,\qquad y=1,\qquad y=2.
$$ Xét dấu trên bốn khoảng:
- $$y<0$$ : tích dương, nên $$y'>0$$ .
- $$0<y<1$$ : tích âm, nên $$y'<0$$ .
- $$1<y<2$$ : tích dương, nên $$y'>0$$ .
- $$y>2$$ : tích âm, nên $$y'<0$$ .
Do đó mũi tên hướng vào $$0$$ , ra khỏi $$1$$ và vào $$2$$ . Kết luận: $$0$$ và $$2$$ ổn định, còn $$1$$
không ổn định.
### Ví dụ 4: Thu hoạch trong logistic
Xét mô hình
$$
\frac{dy}{dt}=y(1-y)-h,
$$ trong đó $$h>0$$ là mức thu hoạch hằng số. Khi thay đổi $$h$$
, số điểm cân bằng có thể thay đổi. Đây là ví dụ rất tốt để gợi mở ý tưởng phân nhánh: một thay đổi nhỏ về tham số có thể thay đổi mạnh cấu trúc động lực học. Ngay ở mức đầu chương, sinh viên đã có thể cảm nhận được sức mạnh của phân tích định tính.
## Câu hỏi khái niệm
1. Vì sao dấu của
$$f(y)$$
đủ để quyết định chiều chuyển động trên trục pha?
2. Vì sao có thể kết luận về ổn định mà không cần công thức nghiệm tường minh?
3. Một điểm cân bằng bán ổn định khác gì với điểm ổn định và không ổn định?
## Bài toán ứng dụng
1. Một mô hình dân số có mức sinh giảm khi quần thể lớn và có thu hoạch hằng số. Hãy giải thích vì sao số điểm cân bằng có thể thay đổi khi mức khai thác tăng.
2. Một phản ứng hóa học có nồng độ cân bằng ở nhiều mức khác nhau. Hãy mô tả cách đường pha giúp dự đoán nồng độ cuối cùng từ nồng độ ban đầu.
3. Trong kinh tế học, một biến thị trường có thể có hai trạng thái ổn định và một ngưỡng bất ổn ở giữa. Hãy giải thích ý nghĩa ra quyết định của cấu trúc này.
## Chiến lược giảng dạy tương tác
- Cho sinh viên vẽ đường pha trước khi giải bất kỳ bài nào, kể cả logistic đã quen.
- Chia lớp thành các nhóm nhỏ, mỗi nhóm phân tích một phương trình tự trị khác nhau rồi trình bày bằng mũi tên trên bảng.
- Hỏi liên tục: "Nếu trạng thái hiện tại nằm ở đây, nó sẽ đi lên hay đi xuống?"
- Dùng màu khác nhau cho các khoảng dấu để sinh viên nhìn thấy cấu trúc động học rõ ràng hơn.
## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên yêu cầu sinh viên dùng bảng ba cột: khoảng giá trị của
$$y$$ , dấu của $$f(y)$$
, chiều mũi tên. Cách làm có cấu trúc này giúp các em tránh suy luận cảm tính.
### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi liên hệ dấu của
$$f'(y_*)$$
với ổn định của điểm cân bằng, hoặc khảo sát sự thay đổi đường pha khi một tham số thay đổi. Đây là bước đệm rất tốt cho chương về ổn định và phân nhánh.
## Tóm tắt dễ nhớ
Với phương trình tự trị
$$
y'=f(y),
$$
muốn hiểu hệ hãy làm ba việc: tìm các điểm cân bằng, kiểm tra dấu của $$f$$
trên từng khoảng, rồi vẽ mũi tên trên trục pha. Không phải lúc nào cũng cần công thức nghiệm để hiểu hệ sẽ đi về đâu.
## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa
### 1. Ứng dụng thực tế
#### Khai thác sinh học có ngưỡng sụp đổ
- Bài toán: Một nghề cá bị khai thác đều mỗi mùa, và nhà quản lý muốn biết mức khai thác nào còn bền vững.
- Mô hình:
$$
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)-h.
$$
- Giả thiết và giới hạn: Mô hình coi mức khai thác $$h$$
là hằng số và quần thể đồng nhất. Mùa vụ, cấu trúc tuổi và biến động khí hậu bị bỏ qua.
- Diễn giải: Chỉ nhìn đường pha ta đã thấy có thể xuất hiện một ngưỡng: bắt đầu dưới ngưỡng thì quần thể đi tới tuyệt diệt, bắt đầu trên ngưỡng thì phục hồi.
#### Điều chỉnh giá về cân bằng thị trường
- Bài toán: Một mức giá điều chỉnh theo chênh lệch cung cầu hiện tại.
- Mô hình:
$$
\frac{dp}{dt}=f(p).
$$
- Giả thiết và giới hạn: Ta giả sử nhà làm giá phản ứng tức thì và thị trường có thể gom vào một biến giá. Trong thực tế có trễ, kỳ vọng và nhiều biến trạng thái.
- Diễn giải: Đường pha trả lời trực tiếp câu hỏi giá bị kéo về cân bằng hay bị đẩy khỏi nó.
#### Phản ứng hóa học với nhiều trạng thái ổn định
- Bài toán: Một lò phản ứng có thể vận hành ở chế độ nhiệt thấp hoặc nhiệt cao tùy vào điều kiện ban đầu.
- Mô hình đơn giản:
$$
\frac{dy}{dt}=f(y),
$$ với $$f(y)$$
có nhiều nghiệm.
- Giả thiết và giới hạn: Đây là rút gọn một chiều của một hệ phức tạp hơn nhiều. Dù vậy, nó vẫn giữ được hiện tượng nhiều cân bằng và ngưỡng chuyển trạng thái.
- Diễn giải: Phase line làm lộ cấu trúc đa ổn định mà không cần công thức nghiệm tường minh.
### 2. Trực giác bổ sung và các kết nối
Phương trình tự trị là nơi sinh viên bắt đầu học cách đọc động học mà không cần "giải". Đây là bước chuyển tư duy rất lớn và sẽ trở thành trung tâm ở chương hệ ODE, ổn định phi tuyến, bifurcation, rồi xa hơn là động lực học vô hạn chiều. Một bẫy thường gặp là kết luận từ dấu của
$$f(y)$$ tại một điểm mà quên kiểm tra trên từng khoảng. Điều đúng là dấu trên cả khoảng mới quyết định chiều di chuyển của nghiệm.

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

Ví dụ này cho thấy ngay vai trò của ngưỡng $$ 0.3 $$: điều kiện đầu ở dưới ngưỡng bị kéo về 0, còn ở trên ngưỡng bị hút về 1.

### 4. Gợi ý tìm thêm mô phỏng

- search: autonomous equation phase line interactive
- search: harvesting logistic bifurcation
- search: Allee effect phase line simulation

### 5. Bài toán mẫu có bối cảnh thực

Xét mô hình thu hoạch chuẩn hóa
$$ \frac{dx}{dt}=x(1-x)-0.16. $$
Điểm cân bằng nghiệm từ
$$ x^2-x+0.16=0, $$
nên
$$ x=0.2,\qquad x=0.8. $$
Phân tích dấu cho thấy $$ x=0.2 $$ là cân bằng không ổn định còn $$ x=0.8 $$ là ổn định. Nghĩa là nếu quần thể rơi xuống dưới 0.2 thì khai thác hiện tại là quá lớn và hệ suy về 0; còn nếu quần thể ở trên ngưỡng này, nó có thể phục hồi về mức 0.8.

### 6. Phân tầng độ khó

**Bậc đại học.** Tìm điểm cân bằng, vẽ đường pha, và suy luận hành vi dài hạn từ dấu của $$ f(y) $$.

**Bậc sau đại học.** Kết nối với tiêu chuẩn $$ f'(y_*) $$, bifurcation một tham số, ổn định cấu trúc, và tư duy Lyapunov một chiều. Đây là cánh cửa mở sang động lực học phi tuyến hiện đại.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: có phần rất rõ về autonomous equations và phase lines.
- Zill — *Differential Equations with Boundary-Value Problems*: hữu ích để luyện kỹ năng phân tích dấu và ổn định một chiều.
- Strogatz — *Nonlinear Dynamics and Chaos*: trực giác xuất sắc về đường pha, điểm cân bằng và hành vi định tính.
