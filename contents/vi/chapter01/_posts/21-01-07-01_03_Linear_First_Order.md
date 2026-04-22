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
## Mục tiêu
Bài học này giúp sinh viên nhận diện đúng phương trình tuyến tính cấp một, hiểu bản chất của nhân tử tích phân, và giải được các mô hình chuẩn như làm nguội, bể trộn, mạch điện đơn giản hay phương trình có hệ số biến thiên theo thời gian. Quan trọng hơn, sinh viên cần hiểu vì sao phép nhân bởi một hàm phù hợp lại biến phương trình thành đạo hàm của một tích.

## Kiến thức nền
Sinh viên cần nắm đạo hàm của tích, nguyên hàm cơ bản, hàm mũ và logarit, cùng với kỹ năng đưa phương trình về dạng chuẩn. Nếu đã quen với phương trình tách biến, sinh viên cũng sẽ thấy rõ điểm khác biệt: không phải mọi ODE cấp một đều tách được, nhưng một lớp rất lớn lại có thể xử lý bằng tính tuyến tính.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-03 Phương trình Tuyến tính Cấp Một]({{ site.imgurl }}/chapter_img/chapter01/01_03_linear_first_order.svg)

Trong nhiều hệ thực, tốc độ thay đổi của đại lượng cần tìm bằng tổng của hai cơ chế: một cơ chế tỉ lệ với chính đại lượng đó và một cơ chế ngoại lực từ bên ngoài. Nhiệt độ của vật tiến dần về nhiệt độ môi trường. Dòng điện trong mạch RL tiến dần về trạng thái ổn định dưới tác động của nguồn. Nồng độ muối trong bể vừa bị pha loãng bởi dòng ra, vừa được bổ sung bởi dòng vào. Tất cả đều dẫn tới một cấu trúc toán học chung.

Chính cấu trúc này làm phương trình tuyến tính cấp một trở thành một trong những mô hình quan trọng nhất của giải tích ứng dụng. Bài học ở đây không chỉ là thuộc công thức nhân tử tích phân, mà là hiểu vì sao một bài toán tưởng như khó lại có thể được "nén" thành đạo hàm của một tích, rồi tích phân trực tiếp.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Ta có thể xem phương trình tuyến tính cấp một như một hệ vừa có "ma sát nội tại" vừa có "nguồn kích thích". Hệ số $$ p(t) $$ cho biết trạng thái hiện tại kéo hệ theo hướng nào, còn $$ q(t) $$ cho biết ngoại lực đang bơm vào hoặc rút ra điều gì.

### Cách nhìn hình ảnh
Với phương trình
$$ \frac{dy}{dt}+p(t)y=q(t), $$
nếu vẽ các nghiệm cho cùng $$ p(t) $$ nhưng điều kiện đầu khác nhau, ta thường thấy chúng bị hút hoặc bị đẩy bởi một quỹ đạo điều khiển bởi $$ q(t) $$. Trong trường hợp $$ p(t)>0 $$, hiệu giữa hai nghiệm thường giảm theo thời gian, nên hình ảnh các nghiệm dần hội tụ lại là một trực giác rất mạnh.

### Cách nhìn hình thức
Phương trình tuyến tính cấp một có dạng chuẩn
$$ \frac{dy}{dt}+p(t)y=q(t). $$
Ta tìm một hàm $$ \mu(t) $$ sao cho khi nhân cả hai vế với $$ \mu $$, vế trái trở thành đạo hàm của tích:
$$
\mu \frac{dy}{dt}+\mu p(t)y=\frac{d}{dt}\left(\mu y\right).
$$
Theo quy tắc tích, điều này đòi hỏi
$$ \mu'(t)=p(t)\mu(t). $$
Một lựa chọn tự nhiên là
$$ \mu(t)=e^{\int p(t)dt}. $$
Khi đó,
$$ \frac{d}{dt}\left(\mu y\right)=\mu q(t), $$
và ta tích phân để thu nghiệm.

## Ý nghĩa của nhân tử tích phân
Nhân tử tích phân không phải là một mẹo thần bí. Nó là một hàm "cân chỉnh" phương trình để phần bên trái có đúng cấu trúc quy tắc đạo hàm của tích. Nếu không hiểu điều này, sinh viên dễ biến phương pháp thành quy trình thuộc lòng. Khi hiểu rồi, các em có thể tự dựng lại phương pháp nếu lỡ quên công thức.

Ngoài ra, phương trình đồng nhất tương ứng
$$ \frac{dy}{dt}+p(t)y=0 $$
cho ta nghiệm
$$ y_h=C e^{-\int p(t)dt}. $$
Điều này cho thấy phần đồng nhất mô tả "trí nhớ" của điều kiện đầu, còn phần không đồng nhất mô tả ảnh hưởng của ngoại lực.

## Những ngộ nhận thường gặp
- "Hễ là cấp một thì tuyến tính." Sai. $$ y' = y^2 + t $$ là cấp một nhưng phi tuyến.
- "Nhân tử tích phân luôn là $$ e^{p(t)} $$." Sai. Phải là $$ e^{\int p(t)dt} $$.
- "Cần nhớ chính xác hằng số trong $$ \mu $$." Không cần. Một bội số khác 0 của nhân tử tích phân vẫn hoạt động.
- "Sau khi tìm được $$ \mu $$ thì có thể quên dạng chuẩn." Sai. Nếu chưa đưa về dạng chuẩn, sinh viên rất dễ chọn sai $$ p(t) $$ và nhân tử tích phân.

## Tiến trình học tập đề xuất
### Bước 1: Nhận diện tính tuyến tính
Kiểm tra xem $$ y $$ và $$ y' $$ có xuất hiện tuyến tính hay không.

### Bước 2: Đưa về dạng chuẩn
Viết rõ
$$ \frac{dy}{dt}+p(t)y=q(t). $$

### Bước 3: Dựng nhân tử tích phân
Từ điều kiện $$ \mu'=p\mu $$ suy ra
$$ \mu=e^{\int p(t)dt}. $$

### Bước 4: Biến vế trái thành đạo hàm của tích
Đây là bước mang ý nghĩa cấu trúc, không chỉ là bước kỹ thuật.

### Bước 5: Tích phân và áp điều kiện đầu
Sau khi tích phân, luôn nên kiểm tra lại bằng cách thế vào ODE ban đầu.

### Các checkpoint
- Sinh viên có viết được vì sao $$ \frac{d}{dt}(\mu y)=\mu y'+\mu' y $$ hay không.
- Sinh viên có xác định đúng $$ p(t) $$ sau khi chia về hệ số 1 trước $$ y' $$ hay không.
- Sinh viên có diễn giải được ảnh hưởng của điều kiện đầu và của ngoại lực riêng rẽ hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Phương trình tuyến tính với hệ số hằng
Giải
$$ \frac{dy}{dt}+2y=e^{-t},\qquad y(0)=1. $$
Ta có
$$ p(t)=2,\qquad q(t)=e^{-t}. $$
Nhân tử tích phân là
$$ \mu(t)=e^{\int 2dt}=e^{2t}. $$
Nhân vào phương trình:
$$ e^{2t}\frac{dy}{dt}+2e^{2t}y=e^t. $$
Vế trái là
$$ \frac{d}{dt}\left(e^{2t}y\right)=e^t. $$
Tích phân:
$$ e^{2t}y=e^t+C. $$
Suy ra
$$ y=e^{-t}+Ce^{-2t}. $$
Dùng điều kiện đầu $$ y(0)=1 $$, ta được $$ C=0 $$, nên
$$ y(t)=e^{-t}. $$
Ví dụ này cho thấy đôi khi nghiệm riêng và điều kiện đầu có thể triệt tiêu phần đồng nhất.

### Ví dụ 2: Hệ số biến thiên theo thời gian
Giải
$$ \frac{dy}{dt}+\frac{1}{t}y=t^2,\qquad t>0. $$
Nhân tử tích phân là
$$ \mu(t)=e^{\int \frac{1}{t}dt}=e^{\ln t}=t. $$
Nhân cả hai vế với $$ t $$:
$$ t\frac{dy}{dt}+y=t^3. $$
Vế trái là
$$ \frac{d}{dt}(ty)=t^3. $$
Tích phân:
$$ ty=\frac{t^4}{4}+C, $$
nên
$$ y(t)=\frac{t^3}{4}+\frac{C}{t}. $$
Điểm quan trọng ở đây là miền $$ t>0 $$. Nếu làm việc trên $$ t<0 $$, ta cũng có thể xử lý tương tự nhưng phải nhất quán miền.

### Ví dụ 3: Định luật làm nguội Newton
Nhiệt độ $$ T(t) $$ của vật trong môi trường nhiệt độ không đổi $$ T_m $$ thỏa
$$ \frac{dT}{dt}=-k\left(T-T_m\right),\qquad k>0. $$
Viết lại:
$$ \frac{dT}{dt}+kT=kT_m. $$
Nhân tử tích phân là
$$ \mu=e^{kt}. $$
Suy ra
$$ \frac{d}{dt}\left(e^{kt}T\right)=kT_m e^{kt}. $$
Tích phân:
$$ e^{kt}T=T_m e^{kt}+C. $$
Do đó
$$ T(t)=T_m+Ce^{-kt}. $$
Nghiệm cho thấy nhiệt độ luôn tiến dần về $$ T_m $$. Đây là cơ hội rất tốt để giải thích ý nghĩa động học của phần đồng nhất và trạng thái cân bằng.

### Ví dụ 4: Bể trộn đơn giản
Một bể chứa 100 lít nước ban đầu có 10 kg muối. Dung dịch chứa 0.2 kg muối mỗi lít chảy vào với tốc độ 3 lít/phút, dung dịch trong bể được khuấy đều và chảy ra với cùng tốc độ 3 lít/phút. Gọi $$ S(t) $$ là lượng muối trong bể.

Ta có tốc độ vào:
$$ 0.2\cdot 3=0.6\text{ kg/phút}. $$
Nồng độ trong bể tại thời điểm $$ t $$ là $$ \frac{S(t)}{100} $$, nên tốc độ ra là
$$ 3\cdot \frac{S}{100}=\frac{3}{100}S. $$
Vì vậy,
$$ \frac{dS}{dt}=0.6-\frac{3}{100}S. $$
Viết dạng chuẩn:
$$ \frac{dS}{dt}+\frac{3}{100}S=0.6. $$
Nhân tử tích phân:
$$ \mu=e^{\frac{3}{100}t}. $$
Sau khi giải, ta được
$$ S(t)=20-10e^{-\frac{3}{100}t}. $$
Lượng muối tiến dần về 20 kg, đúng bằng trạng thái cân bằng mà ta dự đoán từ nồng độ đầu vào.

## Câu hỏi khái niệm
1. Vì sao nhân tử tích phân được dựng từ yêu cầu vế trái phải trở thành đạo hàm của một tích?
2. Trong phương trình tuyến tính cấp một, phần đồng nhất và phần ngoại lực đóng vai trò gì khác nhau?
3. Vì sao cùng một công thức nghiệm có thể mang ý nghĩa hội tụ, tăng trưởng hay điều chỉnh về cân bằng tùy vào dấu của tham số?

## Bài toán ứng dụng
1. Một vật đang được hâm nóng trong lò có nhiệt độ không đổi. Hãy giải thích vì sao mô hình nhiệt độ của vật cũng mang cùng cấu trúc với định luật làm nguội Newton.
2. Một bể hóa chất có dòng vào và dòng ra không đổi. Hãy chỉ ra vì sao lượng chất tan gần như luôn dẫn đến một ODE tuyến tính cấp một nếu thể tích bể giữ nguyên.
3. Một mạch RL được nối với nguồn điện một chiều. Hãy giải thích ý nghĩa vật lý của phần "quá độ" và phần "ổn định" trong nghiệm.

## Chiến lược giảng dạy tương tác
- Trước khi đưa công thức $$ \mu=e^{\int p(t)dt} $$, yêu cầu sinh viên tự dùng quy tắc đạo hàm của tích để đoán điều kiện mà $$ \mu $$ cần thỏa.
- Cho lớp so sánh hai phương trình: một phương trình tách biến và một phương trình tuyến tính, rồi tranh luận xem dấu hiệu nhận dạng nào đáng tin nhất.
- Dùng bể trộn hoặc làm nguội Newton làm tình huống đóng vai, yêu cầu sinh viên giải thích bằng lời ý nghĩa của từng số hạng trước khi tính.
- Cho sinh viên dự đoán nghiệm dài hạn của một mô hình trước khi giải chính xác, sau đó đối chiếu dự đoán với công thức.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Giảng viên nên chuẩn bị mẫu giải cố định gồm bốn dòng: đưa về dạng chuẩn, viết $$ p(t) $$, tìm $$ \mu $$, viết lại thành đạo hàm của tích. Nhiều sinh viên yếu tiến bộ rõ khi được luyện cấu trúc này một cách nhất quán.

### Thử thách cho sinh viên khá giỏi
Yêu cầu sinh viên khá giỏi chứng minh rằng hiệu của hai nghiệm bất kỳ của cùng một phương trình tuyến tính cấp một luôn thỏa phương trình đồng nhất tương ứng. Một bài mở rộng khác là yêu cầu rút ra công thức nghiệm tổng quát trực tiếp bằng tích phân xác định từ điều kiện đầu.

## Tóm tắt dễ nhớ
Phương trình tuyến tính cấp một có dạng
$$ y'+p(t)y=q(t). $$
Ý tưởng trung tâm là tìm một hàm nhân vào để vế trái trở thành đạo hàm của một tích. Nhân tử tích phân không phải mẹo nhớ máy móc; nó là cách khôi phục cấu trúc quy tắc tích. Hãy luôn đưa phương trình về dạng chuẩn trước, rồi mới tìm $$ \mu $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Làm nguội Newton trong đo lường nhiệt
- Bài toán: Một khối kim loại được lấy ra khỏi lò và kỹ sư muốn ước lượng thời gian nguội tới mức an toàn để thao tác.
- Mô hình:
$$ \frac{dT}{dt}+kT=kT_m. $$
- Giả thiết và giới hạn: Nhiệt độ môi trường $$ T_m $$ không đổi, vật đủ nhỏ để xem là có nhiệt độ đồng nhất, và trao đổi nhiệt tuyến tính theo chênh lệch nhiệt độ.
- Diễn giải: Nghiệm luôn có dạng "trạng thái cân bằng cộng quá độ suy giảm", giúp đọc ngay nhiệt độ dài hạn và tốc độ thư giãn của hệ.

#### Mạch RL khi bật nguồn
- Bài toán: Một cuộn cảm được nối với nguồn một chiều và kỹ sư muốn biết dòng điện lên ổn định nhanh đến đâu.
- Mô hình:
$$ L\frac{di}{dt}+Ri=E_0. $$
- Giả thiết và giới hạn: Bỏ qua điện dung ký sinh, nhiệt độ không làm thay đổi điện trở, và nguồn được xem là lý tưởng.
- Diễn giải: Nghiệm cho ta một thời hằng đặc trưng $$ L/R $$. Nếu tỉ số này lớn, hệ "lì" hơn và phản ứng chậm hơn.

#### Khoản vay có trả góp đều
- Bài toán: Một doanh nghiệp vay vốn với lãi suất liên tục và trả nợ đều theo tháng.
- Mô hình:
$$ \frac{dB}{dt}=rB-p. $$
- Giả thiết và giới hạn: Lãi suất không đổi và dòng trả nợ đều. Mô hình không xét phí phạt, lãi suất thả nổi, hay lịch trả nợ rời rạc.
- Diễn giải: Nếu $$ p $$ quá nhỏ so với $$ rB $$, khoản nợ vẫn tăng. Điều này cho thấy ODE có thể làm lộ cơ chế tài chính rất trực tiếp.

### 2. Trực giác bổ sung và các kết nối

Nhân tử tích phân quan trọng vì nó biến một phương trình "chưa là đạo hàm của tích" thành một phương trình "đã là đạo hàm của tích". Ở mức khái niệm, đây là bản sơ khai của phương pháp biến thiên hằng số, của công thức Duhamel, và của các biểu diễn tích phân sẽ lặp lại nhiều lần trong khóa học. Một bẫy thường gặp là sinh viên nhớ công thức $$ \mu(t)=e^{\int p(t)\,dt} $$ nhưng không nhớ vì sao nó xuất hiện; khi đó chỉ cần hệ số trước $$ y' $$ khác 1 là các em dễ dùng sai ngay.

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

Hình này rất phù hợp để nói về ổn định, về vai trò của điều kiện đầu, và về việc hiệu giữa hai nghiệm của cùng một phương trình tuyến tính thường suy giảm theo phương trình đồng nhất tương ứng.

### 4. Gợi ý tìm thêm mô phỏng

- search: integrating factor visualization
- search: Newton cooling curve differential equation
- search: RL circuit transient response plot

### 5. Bài toán mẫu có bối cảnh thực

Một cảm biến nhiệt đặt trong phòng có nhiệt độ 22 độ C được chuyển vào môi trường 80 độ C. Nếu mô hình là
$$ \frac{dT}{dt}+0.4T=32,\qquad T(0)=22, $$
thì nghiệm là
$$ T(t)=80-58e^{-0.4t}. $$
Phần $$ 80 $$ là cân bằng lâu dài; phần $$ -58e^{-0.4t} $$ là trí nhớ của điều kiện đầu. Nếu đo tại các mốc rời rạc rồi nội suy bằng Euler, sinh viên sẽ thấy mô phỏng số vẫn giữ đúng trực giác hội tụ nhưng sai số giảm rõ khi chọn bước thời gian nhỏ hơn.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm chắc dạng chuẩn, nhân tử tích phân, và cách tách phần ổn định với phần quá độ trong lời giải.

**Bậc sau đại học.** Mở rộng sang công thức biến thiên hằng số, nhân tử tích phân ma trận ở chương hệ ODE, và quan điểm toán tử giải. Đây cũng là nơi thích hợp để nhấn mạnh Green function của bài toán tuyến tính cấp một.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: giải thích rất rõ nhân tử tích phân và các mô hình ứng dụng đầu tiên.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài tập tốt về dạng chuẩn và điều kiện đầu.
- Ross — *Differential Equations*: hữu ích để luyện lời giải ngắn gọn và so sánh các cách trình bày nghiệm.
