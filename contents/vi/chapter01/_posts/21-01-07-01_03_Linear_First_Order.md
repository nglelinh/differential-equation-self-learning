---
layout: post
title: "01-03 Phương trình Tuyến tính Cấp Một"
chapter: '01'
order: 3
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Đa số phương trình trong kỹ thuật—từ mạch điện RC chịu nguồn xoay chiều đến bể muối đang xả và bơm đồng thời—đều không tách biến được vì có thêm một "lực cưỡng bức" $q(t)$ tác động bên ngoài. May mắn thay, **phương trình tuyến tính cấp một** $y' + p(t)y = q(t)$ sở hữu một chiếc chìa khóa vạn năng mang tên **thừa số tích phân** $\mu(t) = e^{\int p(t)\,dt}$, giúp giải đóng mọi bài toán chỉ bằng hai phép tích phân!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương trình Tuyến tính Cấp Một

1. **Dạng chuẩn tắc $y' + p(t)y = q(t)$**:
   Luôn chia hai vế cho hệ số của $y'$ để đưa về hệ số $1$ trước khi tính thừa số tích phân—sai lầm phổ biến nhất là quên chuẩn hóa!
2. **Thừa số tích phân $\mu(t) = \exp\left(\int p(t)\,dt\right)$**:
   Biến vế trái thành đúng đạo hàm của một tích: $\mu(t)y' + \mu(t)p(t)y = \frac{d}{dt}\big[\mu(t)y\big]$, nhờ đó chỉ cần lấy nguyên hàm một lần.
3. **Cấu trúc nghiệm $y = y_h + y_p$ (Nguyên lý chồng chất)**:
   Nghiệm tổng quát luôn tách đôi thành phần **đáp ứng tự do** $y_h = C/\mu(t)$ (phụ thuộc điều kiện đầu) và phần **đáp ứng cưỡng bức** $y_p = \frac{1}{\mu(t)}\int \mu(t)q(t)\,dt$.
4. **Khoảng tồn tại toàn cục**:
   Khác với phương trình phi tuyến dễ bùng nổ, nghiệm của PTVP tuyến tính cấp một tồn tại duy nhất trên **toàn bộ khoảng liên tục** của $p(t)$ và $q(t)$ chứa $t_0$.

## Mục tiêu
Bài học này giúp sinh viên nhận diện phương trình vi phân tuyến tính cấp một, hiểu bản chất của nhân tử tích phân và giải được các mô hình cơ bản như làm nguội, bể trộn, mạch điện RL hoặc phương trình có hệ số biến thiên theo thời gian. Trọng tâm của bài là hiểu vì sao việc nhân phương trình với một hàm thích hợp lại đưa vế trái về đúng đạo hàm của một tích.

## Kiến thức nền
Sinh viên cần nắm vững quy tắc đạo hàm của tích, nguyên hàm cơ bản, hàm mũ, logarit và kỹ năng biến đổi phương trình về dạng chuẩn. So với phương trình tách biến ở bài trước, lớp phương trình tuyến tính cấp một bao quát nhiều bài toán không tách biến được nhưng vẫn có phương pháp giải hệ thống.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-03 Phương trình Tuyến tính Cấp Một]({{ site.imgurl }}/chapter_img/chapter01/01_03_linear_first_order.svg)

Trong nhiều hệ thực tế, tốc độ biến thiên của đại lượng cần tìm gồm hai phần: một phần tỉ lệ với chính đại lượng đó và một phần do tác động bên ngoài. Nhiệt độ của vật tiến dần về nhiệt độ môi trường; dòng điện trong mạch RL tiến về trạng thái ổn định dưới điện áp nguồn; lượng muối trong bể trộn vừa giảm do dòng chảy ra vừa tăng do dòng chảy vào. Tất cả các mô hình này đều có chung một cấu trúc tuyến tính cấp một.

Thay vì ghi nhớ công thức nhân tử tích phân một cách máy móc, bài học tập trung giải thích ý tưởng cốt lõi: tìm hệ số nhân để gom vế trái thành đạo hàm của một tích, từ đó lấy tích phân trực tiếp để tìm nghiệm.

### Khung giải thích (nên đọc chậm): Giải từng bước $t y' + 2y = 4t^2$ với $y(1) = 2$ ($t > 0$)

1. **Đưa về dạng chuẩn tắc** (chia hai vế cho $t > 0$):
   $$y' + \frac{2}{t}y = 4t \implies p(t) = \frac{2}{t},\quad q(t) = 4t.$$
2. **Tính thừa số tích phân**:
   $$\mu(t) = \exp\left(\int \frac{2}{t}\,dt\right) = e^{2\ln t} = \mathbf{t^2}.$$
3. **Nhân hai vế với $t^2$ và gộp đạo hàm tích**:
   $$t^2 y' + 2t y = 4t^3 \implies \frac{d}{dt}(t^2 y) = 4t^3.$$
4. **Tích phân và ghim điều kiện đầu**:
   $$t^2 y = \int 4t^3\,dt = t^4 + C \implies y(t) = t^2 + \frac{C}{t^2}.$$
   Thay $y(1) = 2$: $2 = 1 + C \implies C = 1$. Vậy nghiệm duy nhất trên $(0, +\infty)$ là $y(t) = \mathbf{t^2 + \frac{1}{t^2}}$ (kiểm tra nhanh: $t(2t - 2t^{-3}) + 2(t^2 + t^{-2}) = 4t^2$, chuẩn xác!).

## Khái niệm theo ba cách

### Cách nhìn trực quan
Có thể hình dung phương trình tuyến tính cấp một như một hệ vừa chịu "lực kéo nội tại" vừa chịu "nguồn kích thích ngoài". Hệ số $$ p(t) $$ quy định trạng thái hiện tại kéo hệ tăng hay giảm, còn $$ q(t) $$ biểu diễn tốc độ tác động từ bên ngoài.

### Cách nhìn hình ảnh
Với phương trình

$$
\frac{dy}{dt}+p(t)y=q(t),
$$

khi vẽ họ nghiệm ứng với cùng $$ p(t) $$ và $$ q(t) $$ nhưng thay đổi điều kiện đầu, ta thấy các quỹ đạo bị hút về (hoặc đẩy ra khỏi) một quỹ đạo chung do $$ q(t) $$ chi phối. Đặc biệt, khi $$ p(t)>0 $$, hiệu giữa hai nghiệm bất kỳ suy giảm dần về $$ 0 $$ nên các đường cong nghiệm hội tụ lại gần nhau theo thời gian.

### Cách nhìn hình thức
Phương trình tuyến tính cấp một ở dạng chuẩn là

$$
\frac{dy}{dt}+p(t)y=q(t).
$$

Ta tìm một hàm $$ \mu(t) $$ sao cho sau khi nhân hai vế với $$ \mu(t) $$, vế trái trở thành đạo hàm của tích $$ \mu y $$:

$$
\mu \frac{dy}{dt}+\mu p(t)y=\frac{d}{dt}\left(\mu y\right).
$$

Theo quy tắc đạo hàm của tích, điều kiện cần là

$$
\mu'(t)=p(t)\mu(t).
$$

Một lựa chọn đơn giản cho nhân tử tích phân là

$$
\mu(t)=e^{\int p(t)dt}.
$$

Khi đó phương trình trở thành

$$
\frac{d}{dt}\left(\mu y\right)=\mu q(t),
$$

và chỉ cần lấy tích phân hai vế rồi chia cho $$ \mu(t) $$ để thu nghiệm.

## Ý nghĩa của nhân tử tích phân
Nhân tử tích phân không phải là một mẹo tùy hứng mà là hàm hiệu chỉnh giúp vế trái khớp đúng cấu trúc của quy tắc đạo hàm tích. Khi nắm được cơ chế này, bạn có thể tự thiết lập lại công thức bất cứ lúc nào thay vì học thuộc lòng.

Bên cạnh đó, phương trình thuần nhất tương ứng $$ \frac{dy}{dt}+p(t)y=0 $$ có nghiệm $$ y_h=C e^{-\int p(t)dt} $$. Cách tách nghiệm thành nghiệm thuần nhất và nghiệm riêng cho thấy rõ: thành phần thuần nhất lưu giữ ảnh hưởng của điều kiện đầu (phần quá độ), còn thành phần riêng phản ánh đáp ứng của hệ trước tác động ngoài $$ q(t) $$.

## Những ngộ nhận thường gặp
- "Mọi phương trình cấp một đều là phương trình tuyến tính." Sai. Chẳng hạn $$ y' = y^2 + t $$ là cấp một nhưng phi tuyến.
- "Nhân tử tích phân là $$ e^{p(t)} $$." Sai. Phải lấy nguyên hàm của $$ p(t) $$ trên số mũ: $$ \mu(t)=e^{\int p(t)dt} $$.
- "Cần giữ hằng số tích phân khi tính $$ \mu(t) $$." Không cần. Mọi bội khác $$ 0 $$ của $$ \mu(t) $$ đều rút gọn khi nhân cả hai vế của phương trình.
- "Có thể đọc thẳng $$ p(t) $$ mà không cần đưa về dạng chuẩn." Sai. Nếu hệ số trước $$ y' $$ khác $$ 1 $$, cần chia hai vế cho hệ số đó trước khi xác định $$ p(t) $$ và $$ q(t) $$.

## Tiến trình học tập đề xuất

### Bước 1: Nhận diện tính tuyến tính
Kiểm tra xem $$ y $$ và $$ y' $$ chỉ xuất hiện ở bậc nhất và không nhân với nhau.

### Bước 2: Đưa về dạng chuẩn
Chia hai vế cho hệ số của $$ y' $$ để viết rõ dạng $$ \frac{dy}{dt}+p(t)y=q(t) $$.

### Bước 3: Dựng nhân tử tích phân
Từ điều kiện $$ \mu'=p\mu $$, tính $$ \mu(t)=e^{\int p(t)dt} $$.

### Bước 4: Đưa vế trái về đạo hàm của tích
Nhân hai vế với $$ \mu(t) $$ và viết gọn vế trái thành $$ \frac{d}{dt}\left(\mu y\right) $$.

### Bước 5: Tích phân và áp dụng điều kiện đầu
Lấy tích phân hai vế, giải ra $$ y(t) $$, thay điều kiện đầu và kiểm tra lại bằng cách thế vào ODE gốc.

### Các checkpoint
- Bạn có tự giải thích được vì sao điều kiện $$ \frac{d}{dt}(\mu y)=\mu y'+\mu' y $$ dẫn đến $$ \mu'=p\mu $$ không?
- Bạn có nhớ chia về hệ số $$ 1 $$ trước $$ y' $$ để xác định đúng $$ p(t) $$ không?
- Bạn có phân biệt được phần ảnh hưởng của điều kiện đầu với phần ảnh hưởng của ngoại lực trong nghiệm không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phương trình tuyến tính hệ số hằng
Giải bài toán

$$
\frac{dy}{dt}+2y=e^{-t},\qquad y(0)=1.
$$

Ở đây $$ p(t)=2 $$ và $$ q(t)=e^{-t} $$, nên nhân tử tích phân là $$ \mu(t)=e^{\int 2dt}=e^{2t} $$. Nhân hai vế với $$ e^{2t} $$ ta được

$$
e^{2t}\frac{dy}{dt}+2e^{2t}y=e^t \iff \frac{d}{dt}\left(e^{2t}y\right)=e^t.
$$

Lấy tích phân hai vế cho $$ e^{2t}y=e^t+C $$, suy ra $$ y=e^{-t}+Ce^{-2t} $$. Thay điều kiện đầu $$ y(0)=1 $$ ta có $$ C=0 $$, vậy nghiệm riêng là

$$
y(t)=e^{-t}.
$$

Ví dụ này cho thấy trong một số trường hợp, điều kiện đầu có thể làm triệt tiêu hoàn toàn thành phần thuần nhất.

### Ví dụ 2: Hệ số biến thiên theo thời gian
Giải phương trình

$$
\frac{dy}{dt}+\frac{1}{t}y=t^2,\qquad t>0.
$$

Trên miền $$ t>0 $$, nhân tử tích phân là $$ \mu(t)=e^{\int \frac{1}{t}dt}=e^{\ln t}=t $$. Nhân hai vế với $$ t $$ ta có

$$
t\frac{dy}{dt}+y=t^3 \iff \frac{d}{dt}(ty)=t^3.
$$

Lấy tích phân hai vế cho $$ ty=\frac{t^4}{4}+C $$, từ đó

$$
y(t)=\frac{t^3}{4}+\frac{C}{t}.
$$

Cần chú ý điều kiện miền $$ t>0 $$ (điểm $$ t=0 $$ là điểm kỳ dị của hệ số $$ 1/t $$); trên miền $$ t<0 $$ ta làm tương tự nhưng vẫn phải xét riêng từng khoảng không chứa $$ 0 $$.

### Ví dụ 3: Định luật làm nguội Newton
Nhiệt độ $$ T(t) $$ của một vật trong môi trường có nhiệt độ không đổi $$ T_m $$ thỏa mãn

$$
\frac{dT}{dt}=-k\left(T-T_m\right),\qquad k>0.
$$

Đưa về dạng chuẩn $$ \frac{dT}{dt}+kT=kT_m $$, nhân tử tích phân là $$ \mu=e^{kt} $$, suy ra

$$
\frac{d}{dt}\left(e^{kt}T\right)=kT_m e^{kt}.
$$

Lấy tích phân hai vế cho $$ e^{kt}T=T_m e^{kt}+C $$, nên

$$
T(t)=T_m+Ce^{-kt}.
$$

Nghiệm cho thấy nhiệt độ luôn tiến dần về trạng thái cân bằng $$ T_m $$, trong khi thành phần quá độ $$ Ce^{-kt} $$ suy giảm theo hàm mũ.

### Ví dụ 4: Bể trộn đơn giản
Một bể chứa 100 lít nước ban đầu có 10 kg muối. Dung dịch nồng độ $$ 0.2\text{ kg/lít} $$ chảy vào với lưu lượng $$ 3\text{ lít/phút} $$; hỗn hợp trong bể được khuấy đều và chảy ra với cùng lưu lượng $$ 3\text{ lít/phút} $$. Gọi $$ S(t) $$ là khối lượng muối (kg) trong bể tại thời điểm $$ t $$.

Tốc độ muối chảy vào là $$ 0.2\cdot 3=0.6\text{ kg/phút} $$. Do thể tích bể giữ nguyên ở mức 100 lít, nồng độ trong bể là $$ \frac{S(t)}{100} $$, nên tốc độ muối chảy ra là $$ 3\cdot \frac{S}{100}=\frac{3}{100}S $$. Ta thu được phương trình

$$
\frac{dS}{dt}=0.6-\frac{3}{100}S \iff \frac{dS}{dt}+\frac{3}{100}S=0.6.
$$

Với nhân tử tích phân $$ \mu=e^{\frac{3}{100}t} $$ và điều kiện đầu $$ S(0)=10 $$, ta giải được

$$
S(t)=20-10e^{-\frac{3}{100}t}.
$$

Khối lượng muối tiến dần về 20 kg, khớp đúng với trạng thái cân bằng ứng với nồng độ đầu vào $$ 0.2\text{ kg/lít} $$ trên 100 lít.

## Câu hỏi khái niệm
1. Vì sao nhân tử tích phân được xây dựng từ yêu cầu biến vế trái thành đạo hàm của một tích?
2. Trong nghiệm của phương trình tuyến tính cấp một, phần thuần nhất và phần do ngoại lực đóng vai trò khác nhau như thế nào?
3. Vì sao dấu của hệ số $$ p(t) $$ lại quyết định việc các nghiệm hội tụ lại hay phân kỳ ra xa nhau?

## Bài toán ứng dụng
1. Một vật được làm nóng trong lò có nhiệt độ không đổi. Hãy giải thích vì sao mô hình nhiệt độ của vật vẫn có cùng dạng phương trình với định luật làm nguội Newton.
2. Một bể hóa chất có lưu lượng vào và ra bằng nhau. Hãy giải thích vì sao khối lượng chất tan luôn tuân theo một ODE tuyến tính cấp một khi hỗn hợp được khuấy đều.
3. Một mạch RL nối với nguồn điện một chiều không đổi. Hãy giải thích ý nghĩa vật lý của thành phần quá độ và thành phần xác lập (ổn định) trong biểu thức dòng điện.

## Chiến lược giảng dạy tương tác
- Trước khi công bố công thức $$ \mu=e^{\int p(t)dt} $$, cho sinh viên tự dùng quy tắc đạo hàm tích để suy ra điều kiện $$ \mu'=p\mu $$.
- Đặt cạnh nhau một phương trình tách biến và một phương trình tuyến tính để cả lớp so sánh dấu hiệu nhận diện.
- Dùng bài toán bể trộn hoặc làm nguội Newton để sinh viên diễn đạt bằng lời ý nghĩa từng số hạng trước khi tính toán.
- Cho sinh viên dự đoán giới hạn dài hạn của nghiệm trước khi giải rồi đối chiếu với công thức thu được.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Áp dụng khung giải cố định gồm bốn bước: đưa về dạng chuẩn, xác định $$ p(t) $$, tìm $$ \mu(t) $$, rồi viết lại vế trái thành đạo hàm của tích $$ \mu y $$.

### Thử thách cho sinh viên khá giỏi
Chứng minh rằng hiệu của hai nghiệm bất kỳ của cùng một phương trình tuyến tính cấp một luôn là nghiệm của phương trình thuần nhất tương ứng; từ đó viết công thức nghiệm tổng quát bằng tích phân xác định gắn trực tiếp với điều kiện đầu $$ y(t_0)=y_0 $$.

## Tóm tắt dễ nhớ
Phương trình tuyến tính cấp một có dạng chuẩn $$ y'+p(t)y=q(t) $$. Ý tưởng cốt lõi là nhân hai vế với nhân tử tích phân $$ \mu(t)=e^{\int p(t)dt} $$ để đưa vế trái về đạo hàm của tích $$ (\mu y)' $$. Luôn đưa phương trình về dạng chuẩn trước khi xác định $$ p(t) $$ và $$ \mu(t) $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Làm nguội Newton trong đo lường nhiệt
- Bài toán: Một khối kim loại vừa lấy ra khỏi lò cần được ước lượng thời gian nguội về mức nhiệt an toàn.
- Mô hình:

$$
\frac{dT}{dt}+kT=kT_m.
$$

- Giả thiết và giới hạn: Nhiệt độ môi trường $$ T_m $$ không đổi, khối kim loại đủ nhỏ để nhiệt độ bên trong đồng đều và tốc độ trao đổi nhiệt tuyến tính theo hiệu nhiệt độ.
- Diễn giải: Nghiệm có dạng tổng của trạng thái cân bằng và phần quá độ suy giảm, cho biết ngay cả giới hạn dài hạn lẫn tốc độ nguội.

#### Mạch RL khi đóng nguồn
- Bài toán: Nối cuộn cảm và điện trở với nguồn một chiều không đổi; kỹ sư cần biết dòng điện mất bao lâu để đạt gần mức ổn định.
- Mô hình:

$$
L\frac{di}{dt}+Ri=E_0.
$$

- Giả thiết và giới hạn: Bỏ qua điện dung ký sinh, điện trở không đổi theo nhiệt độ và nguồn áp lý tưởng.
- Diễn giải: Nghiệm xuất hiện hằng số thời gian đặc trưng $$ \tau = L/R $$. Khi tỉ số này lớn, hệ có quán tính lớn hơn và đáp ứng chậm hơn.

#### Khoản vay có trả góp đều
- Bài toán: Một doanh nghiệp vay vốn chịu lãi liên tục và trả nợ với tốc độ đều theo thời gian.
- Mô hình:

$$
\frac{dB}{dt}=rB-p.
$$

- Giả thiết và giới hạn: Lãi suất không đổi và dòng trả nợ liên tục đều; chưa xét phí phạt, lãi suất thả nổi hoặc kỳ trả rời rạc.
- Diễn giải: Nếu tốc độ trả $$ p $$ nhỏ hơn mức lãi sinh ra $$ rB(0) $$, dư nợ vẫn tiếp tục tăng—cho thấy phương trình phản ánh trực tiếp cơ chế tài chính.

### 2. Trực giác bổ sung và các kết nối

Nhân tử tích phân chuyển một vế trái chưa ở dạng đạo hàm toàn phần về đúng đạo hàm của một tích. Về mặt cấu trúc, đây là bước khởi đầu cho phương pháp biến thiên hằng số, công thức Duhamel và các biểu diễn tích phân sẽ gặp lại ở các chương sau. Lỗi thường gặp nhất là nhớ máy móc công thức $$ \mu(t)=e^{\int p(t)\,dt} $$ mà quên chia hệ số trước $$ y' $$ về $$ 1 $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
y_eq = 1.0
for y0 in [-1.0, 0.0, 0.5, 2.0]:
    y = y_eq + (y0 - y_eq) * np.exp(-t)
    plt.plot(t, y, label=f"y(0)={y0}")

plt.axhline(y_eq, color="black", linestyle="--", label="steady state")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Họ nghiệm của y' + y = 1")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị minh họa tính ổn định, vai trò của điều kiện đầu và việc hiệu giữa hai nghiệm bất kỳ cùng suy giảm theo nghiệm của phương trình thuần nhất tương ứng.

### 4. Gợi ý tìm thêm mô phỏng

- search: integrating factor visualization
- search: Newton cooling curve differential equation
- search: RL circuit transient response plot

### 5. Bài toán mẫu có bối cảnh thực

Một cảm biến nhiệt đang ở phòng $$ 22^\circ\text{C} $$ được đưa vào môi trường $$ 80^\circ\text{C} $$. Với mô hình

$$
\frac{dT}{dt}+0.4T=32,\qquad T(0)=22,
$$

nghiệm giải tích là

$$
T(t)=80-58e^{-0.4t}.
$$

Số hạng $$ 80 $$ là nhiệt độ cân bằng dài hạn, còn $$ -58e^{-0.4t} $$ thể hiện ảnh hưởng tắt dần của trạng thái ban đầu. Nếu xấp xỉ số bằng phương pháp Euler, nghiệm số bám sát xu hướng hội tụ và sai số giảm khi thu nhỏ bước thời gian.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm chắc dạng chuẩn, phương pháp nhân tử tích phân và cách diễn giải hai thành phần ổn định–quá độ trong nghiệm.

**Bậc sau đại học.** Mở rộng sang phương pháp biến thiên hằng số, ma trận cơ bản cho hệ ODE tuyến tính, quan điểm toán tử giải và hàm Green (Green's function) của bài toán tuyến tính cấp một.

## Video tham khảo

- Xem trước: [Phương trình vi phân Tuyến tính cấp 1 (Bài 13.2) | Vi tích phân 2/Toán C](https://www.youtube.com/watch?v=m8BFHJQrLSM) — Nguyễn Văn Thùy, tiếng Việt. Bài giảng tiếng Việt về phương trình tuyến tính cấp một và nhân tử tích phân.
- [Linear Differential Equations & the Method of Integrating Factors](https://www.youtube.com/watch?v=2H6BZHlD_3g) — Dr. Trefor Bazett, tiếng Anh. Giải thích vì sao nhân tử $$ e^{\int p} $$ đưa phương trình tuyến tính về dạng đạo hàm của một tích.
- [The Method of Integrating Factors for Linear 1st Order ODEs **full example**](https://www.youtube.com/watch?v=20x2dNVztlU) — Dr. Trefor Bazett, tiếng Anh. Trình bày trọn vẹn một ví dụ giải bằng nhân tử tích phân kèm điều kiện đầu.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giải thích rõ phương pháp nhân tử tích phân và các mô hình ứng dụng cơ bản.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập tốt về dạng chuẩn và bài toán giá trị đầu.
- Ross — *Differential Equations*: hữu ích để rèn cách trình bày ngắn gọn và so sánh các dạng nghiệm.
