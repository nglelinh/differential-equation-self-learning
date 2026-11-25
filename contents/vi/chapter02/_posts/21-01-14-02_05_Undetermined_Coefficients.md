---
layout: post
title: "02-05 Phương trình Không thuần nhất: Hệ số Bất định"
chapter: '02'
order: 5
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: required
---

Trong thế giới thực, một cây cầu chịu gió thổi tuần hoàn hay một mạch điện cắm vào nguồn xoay chiều $g(t)$ đều là **phương trình không thuần nhất** $ay'' + by' + cy = g(t)$. Nếu vế phải $g(t)$ thuộc "câu lạc bộ khép kín dưới phép đạo hàm"—gồm đa thức, hàm mũ, $\sin/\cos$ và tích của chúng—thì **phương pháp Hệ số bất định** cho phép ta đoán chính xác hình dáng của nghiệm riêng $y_p$ rồi giải một hệ đại số tuyến tính nhỏ để tìm hệ số!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Hệ số Bất định

1. **Phạm vi áp dụng (Lớp hàm đóng dưới đạo hàm)**:
   Chỉ áp dụng khi phương trình có **hệ số hằng** và vế phải $g(t)$ là tổ hợp của $t^m$, $e^{\alpha t}$, $\cos(\beta t)$, $\sin(\beta t)$ (không dùng được cho $\tan t$, $\ln t$ hay $1/t$).
2. **Nguyên lý chồng chất cho vế phải**:
   Nếu $g(t) = g_1(t) + g_2(t)$, ta tìm riêng $y_{p1}$ cho $g_1$ và $y_{p2}$ cho $g_2$, rồi cộng lại $y_p = y_{p1} + y_{p2}$.
3. **Quy tắc nhân $t^s$ khi trùng nghiệm thuần nhất (Cộng hưởng đại số)**:
   Nếu dạng thử ban đầu chứa số hạng đã là nghiệm của phương trình thuần nhất $y_h$, ta phải nhân toàn bộ dạng thử đó với $t^s$ ($s = 1$ hoặc $2$, nhỏ nhất để không còn trùng nữa)—nếu quên nhân $t^s$, hệ phương trình sẽ vô nghiệm ($0 = 1$)!
4. **Liên hệ với Toán tử triệt tiêu (Annihilator)**:
   Thực chất phương pháp này tương đương với việc tác động một toán tử vi phân triệt tiêu $g(t)$ lên cả hai vế để đưa về phương trình thuần nhất bậc cao hơn.

## Mục tiêu
Bài học này giúp sinh viên giải phương trình tuyến tính cấp hai không thuần nhất bằng phương pháp hệ số bất định, chọn đúng dạng nghiệm riêng thử, xử lý hiện tượng cộng hưởng bằng cách nhân thêm lũy thừa của $$ t $$, và hiểu vì sao phương pháp này chỉ áp dụng được cho những họ hàm đóng dưới phép đạo hàm.

## Kiến thức nền
Sinh viên cần nắm cách tìm nghiệm thuần nhất của phương trình hệ số hằng, nguyên lý chồng chất và kỹ năng đạo hàm đa thức, hàm mũ, hàm sin-cos. Trong bài này, việc nhận diện đúng dạng vế phải quan trọng ngang với kỹ thuật thay vào phương trình.

## Dẫn nhập
![Sơ đồ minh họa cho bài 02-05 Phương trình Không thuần nhất: Hệ số Bất định]({{ site.imgurl }}/chapter_img/chapter02/02_05_undetermined_coefficients.svg)

Khi vế phải của phương trình khác 0, ta cần tìm một nghiệm riêng biểu diễn đáp ứng của hệ trước ngoại lực. Nếu hàm cưỡng bức có dạng đặc biệt như đa thức, hàm mũ, hàm lượng giác sin-cos hoặc tích của chúng, ta không cần dùng đến công cụ tổng quát nặng nề mà có thể thử một nghiệm cùng họ rồi xác định các hệ số chưa biết. Đó là phương pháp hệ số bất định.

Điểm cần lưu ý của phương pháp là không thể chỉ sao chép y nguyên biểu thức vế phải. Nếu dạng nghiệm thử trùng với một thành phần của nghiệm thuần nhất, ta phải nhân thêm $$ t $$ (hoặc $$ t^2 $$) để đảm bảo tính độc lập tuyến tính. Đây chính là biểu hiện đại số của hiện tượng cộng hưởng.

### Giải thích: Giải $y'' - 3y' + 2y = 4e^{2t}$ để thấy rõ quy tắc nhân $t$ khi xảy ra trùng nghiệm

1. **Giải phương trình thuần nhất trước** (BẮT BUỘC làm trước khi đoán $y_p$!):
   $r^2 - 3r + 2 = (r - 1)(r - 2) = 0 \implies y_h(t) = c_1 e^t + c_2 e^{2t}$.
2. **Chọn dạng thử $y_p$**:
   - Vế phải $4e^{2t}$ gợi ý thử $A e^{2t}$, nhưng $e^{2t}$ **đã nằm trong $y_h$** (nghiệm đơn $r = 2$)!
   - Nhân thêm $t^1$: đặt $y_p(t) = \mathbf{A\,t\,e^{2t}}$.
3. **Tính đạo hàm và thay vào phương trình**:
   - $y_p' = A(1 + 2t)e^{2t}$
   - $y_p'' = A(4 + 4t)e^{2t}$
   - Thay vào vế trái: $A\big[(4+4t) - 3(1+2t) + 2t\big]e^{2t} = A\big[1 + 0\cdot t\big]e^{2t} = A e^{2t}$.
4. **Đồng nhất hệ số**: $A e^{2t} = 4e^{2t} \implies A = \mathbf{4}$.
   Vậy nghiệm tổng quát là $y(t) = \mathbf{c_1 e^t + c_2 e^{2t} + 4t\,e^{2t}}$.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Có thể hình dung hệ như một cơ cấu chịu tác động từ một tín hiệu ngoài thuộc họ hàm "ổn định dưới phép đạo hàm", nên đáp ứng cưỡng bức cũng thường nằm trong họ hàm đó. Tuy nhiên, nếu tín hiệu kích thích trùng với chế độ dao động tự nhiên của hệ, biên độ đáp ứng sẽ thay đổi theo quy luật khác — đó là lý do xuất hiện thừa số $$ t $$.

### Cách nhìn hình ảnh
Nếu vế phải là hằng số hoặc đa thức, nghiệm riêng thường có dạng đa thức. Nếu vế phải là $$ e^{at} $$, nghiệm riêng thường mang cùng dạng hàm mũ. Nếu vế phải là $$ \sin bt $$ hoặc $$ \cos bt $$, nghiệm riêng thường là tổ hợp tuyến tính của sin và cos. Khi xảy ra cộng hưởng, đồ thị nghiệm riêng xuất hiện số hạng nhân thêm $$ t $$ với thành phần tự nhiên của hệ.

### Cách nhìn hình thức
Với phương trình
$$ ay''+by'+cy=g(t), $$
nghiệm tổng quát có dạng $$ y=y_h+y_p $$. Phương pháp hệ số bất định tìm $$ y_p $$ bằng cách chọn dạng nghiệm thử thuộc cùng họ hàm với $$ g(t) $$ và các đạo hàm của nó. Nếu dạng thử trùng với một phần của $$ y_h $$, ta nhân thêm $$ t^s $$, với $$ s $$ là số nguyên dương nhỏ nhất sao cho không còn thành phần nào trùng với $$ y_h $$.

## Những ngộ nhận thường gặp
- "Chỉ cần chép nguyên vế phải làm nghiệm riêng thử." Sai: phải bao gồm cả các dạng sinh ra từ đạo hàm và kiểm tra khả năng trùng với nghiệm thuần nhất.
- "Dạng thử sai nghĩa là phương pháp không dùng được." Không đúng: phần lớn sai sót đến từ việc thiếu số hạng cùng họ hoặc quên nhân thêm $$ t $$.
- "Mọi vế phải đều dùng được hệ số bất định." Sai: phương pháp chỉ áp dụng cho các họ hàm đóng dưới phép đạo hàm.
- "Cộng hưởng chỉ là khái niệm vật lý." Sai: nó biểu hiện trực tiếp về mặt đại số khi dạng thử trùng với nghiệm thuần nhất.

## Tiến trình học tập đề xuất
### Bước 1: Giải phương trình thuần nhất
Luôn thực hiện bước này trước để biết có xảy ra cộng hưởng hay không.

### Bước 2: Nhận diện vế phải và chọn họ hàm thử
Liệt kê đầy đủ các số hạng có thể xuất hiện sau khi lấy đạo hàm.

### Bước 3: Kiểm tra sự trùng lặp với nghiệm thuần nhất
Nếu có thành phần trùng, nhân thêm $$ t $$ hoặc bậc cao hơn.

### Bước 4: Thay vào phương trình để tìm hệ số
Đồng nhất hệ số hai vế một cách gọn gàng, có hệ thống.

### Các checkpoint
- Sinh viên có chọn đủ các số hạng trong họ hàm thử hay không.
- Sinh viên có phát hiện kịp thời trường hợp cộng hưởng hay không.
- Sinh viên có phân biệt rõ nghiệm riêng và nghiệm tổng quát hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Vế phải đa thức
Giải phương trình $$ y''-3y'+2y=t $$. Nghiệm thuần nhất là $$ y_h=c_1e^t+c_2e^{2t} $$. Vì vế phải là đa thức bậc nhất, ta thử $$ y_p=At+B $$. Khi đó $$ y_p'=A $$ và $$ y_p''=0 $$. Thế vào phương trình:
$$ 0-3A+2(At+B)=t. $$
Đồng nhất hệ số hai vế: $$ 2A=1 \Rightarrow A=\frac{1}{2} $$, và
$$
-3A+2B=0 \Rightarrow -\frac{3}{2}+2B=0 \Rightarrow B=\frac{3}{4}.
$$
Vậy nghiệm tổng quát là
$$ y(t)=c_1e^t+c_2e^{2t}+\frac{1}{2}t+\frac{3}{4}. $$

### Ví dụ 2: Vế phải hàm mũ không cộng hưởng
Giải phương trình $$ y''+y=e^t $$. Nghiệm thuần nhất là $$ y_h=c_1\cos t+c_2\sin t $$. Thử $$ y_p=Ae^t $$ rồi thay vào phương trình:
$$
Ae^t+Ae^t=e^t \Rightarrow 2A=1 \Rightarrow A=\frac{1}{2}.
$$
Do đó
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}e^t. $$

### Ví dụ 3: Vế phải hàm mũ có cộng hưởng
Giải phương trình $$ y''-y=e^t $$. Nghiệm thuần nhất là $$ y_h=c_1e^t+c_2e^{-t} $$. Vì $$ Ae^t $$ trùng với thành phần trong $$ y_h $$, ta thử $$ y_p=Ate^t $$. Tính đạo hàm:
$$ y_p'=Ae^t+Ate^t,\qquad y_p''=2Ae^t+Ate^t. $$
Thế vào phương trình:
$$ \left(2Ae^t+Ate^t\right)-Ate^t=e^t \Rightarrow 2A=1 \Rightarrow A=\frac{1}{2}. $$
Vậy
$$ y(t)=c_1e^t+c_2e^{-t}+\frac{1}{2}te^t. $$
Đây là ví dụ tiêu biểu của hiện tượng cộng hưởng về mặt đại số.

### Ví dụ 4: Vế phải lượng giác
Giải phương trình $$ y''+4y=\cos t $$. Nghiệm thuần nhất là $$ y_h=c_1\cos 2t+c_2\sin 2t $$. Vì vế phải là $$ \cos t $$, ta thử $$ y_p=A\cos t+B\sin t $$. Khi đó $$ y_p''=-A\cos t-B\sin t $$. Thế vào phương trình:
$$ 3A\cos t+3B\sin t=\cos t, $$
suy ra $$ A=\frac{1}{3} $$ và $$ B=0 $$. Vậy
$$ y(t)=c_1\cos 2t+c_2\sin 2t+\frac{1}{3}\cos t. $$

## Câu hỏi khái niệm
1. Vì sao phương pháp hệ số bất định chỉ áp dụng được cho một số loại hàm vế phải nhất định?
2. Vì sao khi dạng thử trùng với nghiệm thuần nhất, ta phải nhân thêm $$ t $$?
3. Về mặt vật lý, hiện tượng cộng hưởng đại số tương ứng với điều gì?

## Bài toán ứng dụng
1. Một hệ cơ học chịu tác động của lực tuần hoàn. Hãy giải thích vì sao vế phải lượng giác dẫn đến nghiệm riêng lượng giác.
2. Một mạch điện nhận tín hiệu tăng theo hàm mũ. Hãy giải thích vì sao đáp ứng cưỡng bức thường thuộc cùng họ hàm.
3. Một hệ rung được kích thích đúng theo chế độ dao động tự nhiên. Hãy phân tích vì sao nghiệm xuất hiện số hạng nhân thêm $$ t $$.

## Chiến lược giảng dạy tương tác
- Cho sinh viên luyện nhanh bước dự đoán dạng nghiệm riêng trước khi tính hệ số.
- Viết nhiều dạng vế phải khác nhau lên bảng và yêu cầu lớp xác định trường hợp nào xảy ra cộng hưởng.
- Dừng trước bước nhân thêm $$ t $$ để hỏi lớp điều gì sẽ xảy ra nếu giữ nguyên dạng thử ban đầu.
- Yêu cầu sinh viên giải thích bằng lời vì sao phải đưa cả sin và cos vào dạng thử ngay cả khi vế phải chỉ chứa một trong hai hàm.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp bảng đối chiếu giữa các dạng vế phải (đa thức, hàm mũ, lượng giác, tích của chúng) và dạng nghiệm thử tương ứng để sinh viên dễ hệ thống hóa.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên giải thích bằng ngôn ngữ không gian vector vì sao các họ hàm áp dụng được phải đóng dưới phép đạo hàm, hoặc luyện thêm với vế phải dạng $$ te^t $$ và $$ e^t\cos t $$.

## Tóm tắt dễ nhớ
Phương pháp hệ số bất định áp dụng khi vế phải thuộc họ hàm đóng dưới phép đạo hàm. Quy trình gồm bốn bước: giải phần thuần nhất, chọn họ hàm thử, kiểm tra cộng hưởng (nhân thêm $$ t $$ nếu trùng) và đồng nhất hệ số để tìm nghiệm riêng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động cưỡng bức trong cơ học
- Bài toán: Một hệ lò xo chịu tác động của ngoại lực tuần hoàn hoặc không đổi.
- Mô hình: $$ m x''+c x'+k x=F_0\cos \omega t $$ hoặc $$ m x''+c x'+k x=P_0 $$.
- Giả thiết và giới hạn: Hệ số hằng và hàm ngoại lực thuộc họ đóng dưới phép đạo hàm.
- Diễn giải: Nghiệm riêng được chọn cùng họ với ngoại lực, trừ trường hợp cộng hưởng cần nhân thêm lũy thừa của $$ t $$.

#### Tín hiệu đầu vào trong mạch điện
- Bài toán: Nguồn kích thích có dạng đa thức, hàm mũ, sin-cos hoặc tích của chúng.
- Mô hình:
$$ Lq''+Rq'+\frac{1}{C}q=E(t). $$
- Giả thiết và giới hạn: Phương pháp chỉ dùng được khi phép đạo hàm không đưa hàm ra khỏi họ đang xét.
- Diễn giải: Do đó, các nguồn vào như $$ \ln t $$ hay $$ \tan t $$ không xử lý được bằng hệ số bất định.

#### Kích thích điều hòa tại tần số riêng
- Bài toán: Hệ bị kích thích đúng theo tần số tự nhiên khiến biên độ đáp ứng tăng theo thời gian.
- Mô hình:
$$ y''+\omega_0^2 y=\cos \omega_0 t. $$
- Giả thiết và giới hạn: Không có lực cản hoặc lực cản rất nhỏ.
- Diễn giải: Việc nhân thêm $$ t $$ trong dạng nghiệm thử là dấu hiệu đại số của hiện tượng cộng hưởng.

### 2. Trực giác bổ sung và các kết nối

Phương pháp hệ số bất định hoạt động vì các họ hàm đóng dưới phép đạo hàm tạo thành không gian vector hữu hạn chiều, biến bài toán vi phân thành hệ phương trình đại số tuyến tính cho các hệ số chưa biết. Một lỗi thường gặp là chỉ chép nguyên biểu thức vế phải mà quên bổ sung các thành phần sinh ra khi lấy đạo hàm.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 1000)
y_res = 0.5 * t * np.sin(t)
y_nonres = 0.75 * np.cos(2*t)

plt.plot(t, y_res, label="Cộng hưởng: y_p ~ t sin(t)")
plt.plot(t, y_nonres, label="Không cộng hưởng: y_p ~ cos(2t)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("So sánh nghiệm riêng khi có và không có cộng hưởng")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy rõ sự khác biệt: khi có cộng hưởng, biên độ tăng dần theo thời gian thay vì giữ bị chặn như trường hợp không cộng hưởng.

### 4. Gợi ý tìm thêm mô phỏng

- search: undetermined coefficients resonance animation
- search: forced oscillator particular solution visualization
- search: resonance t sin t explanation

### 5. Bài toán mẫu có bối cảnh thực

Xét hệ dao động
$$ y''+y=\cos t. $$
Nghiệm thuần nhất là $$ y_h=c_1\cos t+c_2\sin t $$. Vì dạng thử $$ A\cos t+B\sin t $$ trùng với $$ y_h $$, ta nhân thêm $$ t $$ và đặt $$ y_p=t\left(A\cos t+B\sin t\right) $$. Thay vào phương trình, ta tìm được một nghiệm riêng là $$ y_p=\frac{1}{2}t\sin t $$, nên
$$ y(t)=c_1\cos t+c_2\sin t+\frac{1}{2}t\sin t. $$
Thừa số $$ t $$ cho thấy ngoại lực kích thích đúng tần số riêng làm hệ liên tục tích lũy năng lượng.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo bảng chọn dạng nghiệm thử, kiểm tra cộng hưởng và giải hệ tìm hệ số.

**Bậc sau đại học.** Diễn giải phương pháp bằng ngôn ngữ không gian bất biến dưới phép đạo hàm và liên hệ với toán tử triệt tiêu (annihilator).

## Video tham khảo

- Xem trước: [Undetermined Coefficients: Solving non-homogeneous ODEs](https://www.youtube.com/watch?v=AgyeJEO2a-k) — Dr. Trefor Bazett, tiếng Anh. Hướng dẫn chọn dạng nghiệm riêng cho vế phải đa thức, hàm mũ và lượng giác.
- [Undetermined Coefficients | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=pGECDB15L9o) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về phương pháp hệ số bất định.
- [Differential Equations with Forcing: Method of Undetermined Coefficients](https://www.youtube.com/watch?v=Jvmb2jeRaGE) — Steve Brunton, tiếng Anh. Xây dựng phương pháp hệ số bất định cho phương trình tuyến tính có ngoại lực.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ phương pháp hệ số bất định và hiện tượng cộng hưởng.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện chọn dạng nghiệm thử.
- Ross — *Differential Equations*: trình bày gọn, thuận tiện để ôn tập bảng các dạng vế phải.
