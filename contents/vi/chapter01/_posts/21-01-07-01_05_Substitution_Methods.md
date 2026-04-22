---
layout: post
title: "01-05 Phương pháp Thế"
chapter: '01'
order: 5
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu rằng nhiều ODE tưởng như phi tuyến và rối rắm thực ra chứa một biến ẩn thích hợp. Khi chọn đúng phép thế, cấu trúc bài toán trở nên quen thuộc: có thể là tách biến, tuyến tính hoặc exact. Sinh viên cần học cách nhận ra những mẫu quan trọng như phương trình Bernoulli và phương trình thuần nhất cấp một.

## Kiến thức nền
Sinh viên nên nắm chắc phương trình tách biến, phương trình tuyến tính cấp một và quy tắc đạo hàm chuỗi. Phần lớn khó khăn của bài học này không nằm ở tích phân mà nằm ở việc nhìn ra biến phụ nào làm lộ ra cấu trúc thật của phương trình.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-05 Phương pháp Thế]({{ site.imgurl }}/chapter_img/chapter01/01_05_substitution_methods.svg)

Trong toán học ứng dụng, bề ngoài của phương trình đôi khi rất đánh lừa. Hai bài toán có thể trông hoàn toàn khác nhau nhưng sau một phép đổi biến phù hợp lại trở thành cùng một dạng chuẩn. Điều này cũng giống như trong vật lý, khi chọn hệ tọa độ tốt thì bài toán đơn giản đi rất nhiều; cái khó không phải là phép tính, mà là nhìn ra đại lượng nào mới là đại lượng đúng để mô tả hiện tượng.

Phương pháp thế vì vậy là một bài học rất giàu tư duy. Nó yêu cầu sinh viên vượt qua thói quen "thấy gì làm nấy" và chuyển sang câu hỏi sâu hơn: phương trình này đang ẩn giấu cấu trúc nào. Nếu trả lời được câu hỏi ấy, ta thường chuyển một bài toán khó thành một bài toán đã quen tay.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Phép thế giống như đổi góc nhìn của máy ảnh. Cảnh vật không thay đổi, nhưng góc chụp mới làm nổi bật cấu trúc thật. Khi đặt
$$ v=\frac{y}{t} $$
hoặc
$$ v=y^{1-n}, $$
ta đang chọn biến phản ánh đúng mối quan hệ nội tại của hệ.

### Cách nhìn hình ảnh
Trong phương trình thuần nhất cấp một
$$ \frac{dy}{dt}=F\left(\frac{y}{t}\right), $$
độ dốc tại điểm $$ \left(t,y\right) $$ chỉ phụ thuộc vào tỉ số $$ \frac{y}{t} $$, nghĩa là chỉ phụ thuộc vào đường thẳng đi qua gốc tọa độ chứa điểm đó. Đây là dấu hiệu hình học rất đẹp cho phép thế
$$ y=vt. $$
Trong phương trình Bernoulli, phi tuyến chỉ đến từ một lũy thừa của $$ y $$, nên phép thế làm "thẳng hóa" quan hệ đó.

### Cách nhìn hình thức
Hai mẫu quan trọng là:

Phương trình Bernoulli:
$$ \frac{dy}{dt}+p(t)y=q(t)y^n,\qquad n\neq 0,1. $$
Đặt
$$ v=y^{1-n}, $$
ta thu được một phương trình tuyến tính theo $$ v $$.

Phương trình thuần nhất cấp một:
$$ \frac{dy}{dt}=F\left(\frac{y}{t}\right). $$
Đặt
$$ y=vt $$
thì
$$ \frac{dy}{dt}=v+t\frac{dv}{dt}, $$
từ đó bài toán thường trở thành tách biến theo $$ v $$ và $$ t $$.

## Bản chất sư phạm của bài học
Điểm cốt lõi là sinh viên không nên học bài này như một danh sách mẹo rời rạc. Điều cần học là tư duy nhận dạng: có đại lượng kết hợp nào xuất hiện lặp lại không, có tỉ số nào đóng vai trò trung tâm không, có lũy thừa nào khiến phương trình gần tuyến tính không. Khi thấy được cấu trúc, phép thế xuất hiện gần như tự nhiên.

## Những ngộ nhận thường gặp
- "Phương pháp thế là đoán mò." Không đúng. Nó dựa trên mẫu cấu trúc rất cụ thể.
- "Chỉ có một phép thế đúng." Sai. Nhiều bài toán có nhiều phép đổi biến hợp lý, dù một số lựa chọn sẽ tiện hơn.
- "Đặt biến xong là xong." Chưa đủ. Cần đổi cả đạo hàm theo đúng quy tắc chuỗi.
- "Bernoulli là tuyến tính vì có $$ y $$ và $$ y' $$." Sai. Chỉ sau phép thế thích hợp nó mới trở thành tuyến tính.

## Tiến trình học tập đề xuất
### Bước 1: Tìm dấu hiệu cấu trúc
Xem bài toán thuộc mẫu thuần nhất, Bernoulli hay có tổ hợp lặp đi lặp lại nào đó.

### Bước 2: Chọn biến phụ có lý do
Giải thích vì sao phép thế ấy có khả năng làm đơn giản phương trình.

### Bước 3: Đổi đạo hàm cẩn thận
Đây là nơi nhiều lỗi kỹ thuật xảy ra nhất.

### Bước 4: Giải phương trình mới
Sau phép thế, bài toán thường quay về một dạng quen thuộc.

### Bước 5: Quay lại biến gốc
Đừng quên trả nghiệm về biến ban đầu và xét miền xác định.

### Các checkpoint
- Sinh viên có nhìn ra mẫu $$ F(y/t) $$ hay không.
- Sinh viên có đổi đạo hàm $$ y'=v+tv' $$ đúng hay không.
- Sinh viên có quay lại biến gốc sau khi giải xong hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Phương trình thuần nhất cấp một
Giải
$$ \frac{dy}{dt}=1+\frac{y}{t},\qquad t\neq 0. $$
Vì vế phải chỉ phụ thuộc vào $$ \frac{y}{t} $$, ta đặt
$$ y=vt. $$
Khi đó
$$ \frac{dy}{dt}=v+t\frac{dv}{dt}. $$
Thế vào phương trình:
$$ v+t\frac{dv}{dt}=1+v. $$
Rút gọn:
$$ t\frac{dv}{dt}=1. $$
Suy ra
$$ \frac{dv}{dt}=\frac{1}{t}. $$
Tích phân:
$$ v=\ln \lvert t\rvert+C. $$
Quay lại biến gốc:
$$ y=t\ln \lvert t\rvert+Ct. $$
Ví dụ này cho thấy điều quan trọng là nhận ra tỉ số $$ \frac{y}{t} $$ chứ không phải cố tách biến trực tiếp theo $$ y $$.

### Ví dụ 2: Phương trình Bernoulli
Giải
$$ \frac{dy}{dt}+y=ty^2,\qquad y\neq 0. $$
Đây là Bernoulli với $$ n=2 $$. Đặt
$$ v=y^{1-2}=y^{-1}. $$
Khi đó
$$
v=\frac{1}{y},\qquad \frac{dv}{dt}=-\frac{1}{y^2}\frac{dy}{dt}.
$$
Từ phương trình ban đầu:
$$ \frac{dy}{dt}=ty^2-y. $$
Nhân với $$ -\frac{1}{y^2} $$:
$$ \frac{dv}{dt}= -t+\frac{1}{y}=-t+v. $$
Do đó
$$ \frac{dv}{dt}-v=-t. $$
Ta được một phương trình tuyến tính theo $$ v $$. Nhân tử tích phân là $$ e^{-t} $$, nên
$$ \frac{d}{dt}\left(e^{-t}v\right)=-te^{-t}. $$
Tích phân hai vế:
$$
e^{-t}v=\int -te^{-t}dt + C=\left(t+1\right)e^{-t}+C.
$$
Suy ra
$$ v=t+1+Ce^t. $$
Vì
$$ v=\frac{1}{y}, $$
ta được
$$ y(t)=\frac{1}{t+1+Ce^t}. $$
Điểm quan trọng ở đây là sau phép thế, cấu trúc tuyến tính hiện ra rất rõ và lời giải quay về biến gốc cũng hoàn toàn trực tiếp.

### Ví dụ 3: Logistic qua phép nghịch đảo
Xét
$$ \frac{dP}{dt}=rP-\frac{r}{K}P^2,\qquad P>0. $$
Đây có thể tách biến, nhưng ta thử một góc nhìn khác. Đặt
$$ u=\frac{1}{P}. $$
Khi đó
$$ \frac{du}{dt}=-\frac{1}{P^2}\frac{dP}{dt}. $$
Thế vào:
$$
\frac{du}{dt}=-\frac{1}{P^2}\left(rP-\frac{r}{K}P^2\right)=-\frac{r}{P}+\frac{r}{K}=-ru+\frac{r}{K}.
$$
Ta thu được phương trình tuyến tính
$$ \frac{du}{dt}+ru=\frac{r}{K}. $$
Giải phương trình này cho ta
$$ u(t)=\frac{1}{K}+Ce^{-rt}. $$
Do đó
$$
P(t)=\frac{1}{u(t)}=\frac{1}{\frac{1}{K}+Ce^{-rt}}=\frac{K}{1+CKe^{-rt}}.
$$
Đây là ví dụ tuyệt vời để thấy một bài toán phi tuyến đôi khi ẩn một biến phụ rất tự nhiên.

### Ví dụ 4: Một phép thế do tổ hợp lặp lại
Giải
$$ \frac{dy}{dt}=\left(t+y\right)^2-1. $$
Tổ hợp $$ t+y $$ xuất hiện gọn gàng, nên đặt
$$ u=t+y. $$
Khi đó
$$
\frac{du}{dt}=1+\frac{dy}{dt}=1+\left(t+y\right)^2-1=u^2.
$$
Ta nhận được
$$ \frac{du}{dt}=u^2, $$
là phương trình tách biến quen thuộc. Tách biến:
$$ \frac{1}{u^2}du=dt. $$
Tích phân:
$$ -\frac{1}{u}=t+C. $$
Suy ra
$$ u=\frac{1}{C-t}. $$
Quay lại biến gốc:
$$ y(t)=\frac{1}{C-t}-t. $$
Bài này dạy sinh viên một thói quen quý: nếu một tổ hợp xuất hiện lặp lại, hãy nghĩ tới một biến phụ gom tổ hợp ấy.

## Câu hỏi khái niệm
1. Vì sao phép thế không phải là đoán mò mà là nhận ra biến có ý nghĩa cấu trúc?
2. Trong phương trình thuần nhất cấp một, tại sao tỉ số $$ \frac{y}{t} $$ lại là đại lượng tự nhiên?
3. Vì sao sau phép thế đúng, một bài toán phi tuyến có thể trở thành tuyến tính hoặc tách biến?

## Bài toán ứng dụng
1. Trong cơ học, nhiều bài toán phụ thuộc vào góc hoặc tỉ số giữa hai đại lượng. Hãy giải thích vì sao đổi biến có thể phản ánh một đại lượng vật lý tự nhiên hơn biến gốc.
2. Một mô hình tăng trưởng có hiệu ứng bão hòa dẫn đến số hạng bậc hai theo quần thể. Hãy giải thích vì sao phép nghịch đảo $$ u=1/P $$ có thể hợp lý.
3. Trong mô hình kiểm soát dịch bệnh, nếu một tổ hợp các biến như "số tiếp xúc hiệu quả" lặp đi lặp lại, việc đổi biến theo tổ hợp ấy có thể giúp gì cho phân tích?

## Chiến lược giảng dạy tương tác
- Cho sinh viên xem 5 phương trình khác nhau và hỏi: "Nếu phải chọn một phép thế, em sẽ thử cái gì trước và vì sao?"
- Khi chữa bài, không công bố ngay phép thế. Hãy để lớp tranh luận xem mẫu cấu trúc nổi bật là gì.
- Yêu cầu sinh viên giải thích bằng lời quy tắc đạo hàm chuỗi mỗi khi đổi biến, tránh việc nhảy thẳng vào ký hiệu.
- Cho một bài có hai cách giải, ví dụ logistic bằng tách biến và bằng phép nghịch đảo, để cả lớp so sánh ưu nhược điểm.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Giảng viên nên cung cấp bảng "dấu hiệu nhận dạng và phép thế gợi ý", chẳng hạn: thấy $$ F(y/t) $$ thì thử $$ y=vt $$, thấy $$ y^n $$ trong dạng tuyến tính thì thử Bernoulli. Bảng này giúp sinh viên bớt cảm giác mơ hồ.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi tự thiết kế một ODE mà sau phép thế phù hợp sẽ trở thành tách biến, rồi giải thích vì sao đã chọn phép thế đó. Đây là bài tập rất tốt để chuyển từ "áp dụng" sang "tạo lập".

## Tóm tắt dễ nhớ
Phương pháp thế là nghệ thuật nhìn ra biến đúng. Một ODE khó thường không khó vì phép tính, mà khó vì ta đang nhìn nó bằng biến chưa phù hợp. Hãy luôn hỏi: có tỉ số nào lặp lại không, có lũy thừa nào có thể làm thẳng hóa không, có tổ hợp nào xuất hiện như một khối không.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tăng trưởng có bão hòa do tự cạnh tranh
- Bài toán: Một quần thể vi sinh tăng trưởng gần mũ ở nồng độ thấp nhưng bị kìm lại bởi cạnh tranh nội bộ ở nồng độ cao.
- Mô hình Bernoulli:
$$ \frac{dy}{dt}+ay=by^2. $$
- Giả thiết và giới hạn: Tốc độ sinh trưởng cơ bản và tự ức chế được xem là hằng số. Mô hình chưa phản ánh môi trường thay đổi hoặc cấu trúc nhiều loài.
- Diễn giải: Phép thế $$ u=1/y $$ làm lộ cấu trúc tuyến tính ẩn sau phi tuyến bậc hai.

#### Mô hình phụ thuộc vào tỉ số trong kinh tế
- Bài toán: Một đại lượng sản lượng phản ứng theo tỉ lệ giữa tích lũy và thời gian, chứ không phản ứng theo giá trị tuyệt đối riêng lẻ.
- Mô hình thuần nhất cấp một:
$$ \frac{dy}{dt}=F\left(\frac{y}{t}\right). $$
- Giả thiết và giới hạn: Ta giả sử hiện tượng có tính đồng dạng theo thang đo. Điều này phù hợp với một số mô hình xấp xỉ, nhưng không đúng nếu có mốc thời gian ngoại sinh rõ rệt.
- Diễn giải: Phép thế $$ y=vt $$ gom phần "đồng dạng" thành một biến duy nhất $$ v $$, giúp ta thấy bài toán thực sự sống trên không gian tỉ số chứ không phải trên hai biến tách rời.

#### Phản ứng hóa học với kết tụ phi tuyến
- Bài toán: Nồng độ hạt bụi trong buồng lọc giảm do vừa có dòng bổ sung vừa có hiện tượng va chạm kết tụ làm mất hạt theo tốc độ bậc hai.
- Mô hình:
$$ \frac{dc}{dt}+kc=qc^2. $$
- Giả thiết và giới hạn: Ta coi buồng phản ứng trộn đều và hệ số kết tụ không đổi. Hệ nhiều hạt kích thước khác nhau sẽ cần mô hình nhiều phương trình hơn.
- Diễn giải: Đây là một Bernoulli điển hình, rất tốt để thấy phi tuyến có cấu trúc không hề "ngẫu hứng".

### 2. Trực giác bổ sung và các kết nối

Phương pháp thế là bài học đầu tiên nơi "chọn tọa độ đúng" quan trọng chẳng kém "tính đúng". Trong nhiều ngành ứng dụng, biến gốc không phải lúc nào cũng là biến tốt nhất. Nồng độ nghịch đảo, tỉ số, hay một tổ hợp lặp lại có thể mang ý nghĩa vật lý hoặc hình học rõ hơn nhiều. Bài học này dự báo những gì sẽ xảy ra ở chương hệ ODE, nơi một phép đổi cơ sở phù hợp có thể chéo hóa cả hệ, và ở chương PDE, nơi đổi biến có thể làm lộ đối xứng hay biến bất biến.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K, P0 = 0.9, 50, 5
t = np.linspace(0, 10, 400)
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
U = 1 / P

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(t, P, color="darkgreen")
axes[0].set_title("Biến gốc P(t)")
axes[0].set_xlabel("t")
axes[0].set_ylabel("P")

axes[1].plot(t, U, color="darkred")
axes[1].set_title("Biến phụ u(t) = 1 / P(t)")
axes[1].set_xlabel("t")
axes[1].set_ylabel("u")

for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

Hình bên phải thường gần tuyến tính hơn nhiều về mặt định tính. Điều đó giúp sinh viên cảm được vì sao phép thế tốt lại "làm phẳng" một bài toán khó.

### 4. Gợi ý tìm thêm mô phỏng

- search: Bernoulli differential equation application
- search: homogeneous first order equation visualization
- search: Riccati equation substitution linearization

### 5. Bài toán mẫu có bối cảnh thực

Xét mô hình tăng trưởng có tự cạnh tranh
$$ \frac{dy}{dt}+0.5y=0.02y^2,\qquad y(0)=4. $$
Đặt
$$ u=\frac{1}{y}, $$
ta được phương trình tuyến tính
$$ \frac{du}{dt}-0.5u=-0.02. $$
Giải ra
$$
u(t)=0.04+0.21e^{0.5t},
\qquad
y(t)=\frac{1}{0.04+0.21e^{0.5t}}.
$$
Ở mức ứng dụng, nghiệm cho thấy khi tự cạnh tranh đủ mạnh thì mật độ không thể bùng nổ vô hạn như mô hình mũ đơn giản.

### 6. Phân tầng độ khó

**Bậc đại học.** Luyện hai mẫu chủ đạo là Bernoulli và thuần nhất cấp một, đồng thời giải thích bằng lời vì sao phép thế được chọn.

**Bậc sau đại học.** Kết nối với Riccati equation, bất biến đối xứng, và tư duy đổi tọa độ trong động lực học. Đây cũng là bước đệm tự nhiên cho chuẩn hóa hệ tuyến tính ở các chương sau.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: có các ví dụ Bernoulli và phương trình thuần nhất rất nền tảng.
- Zill — *Differential Equations with Boundary-Value Problems*: hữu ích để luyện nhận dạng phép thế qua nhiều mẫu bài.
- Ross — *Differential Equations*: trình bày ngắn gọn, phù hợp để ôn nhanh các mẫu đổi biến chuẩn.
