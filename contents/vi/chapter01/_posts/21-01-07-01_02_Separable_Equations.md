---
layout: post
title: "01-02 Phương trình Tách biến"
chapter: '01'
order: 2
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên nhận ra khi nào một ODE có thể tách biến, hiểu vì sao việc "gom các yếu tố theo biến" lại hợp lý về mặt toán học, và biết giải các bài toán tách biến kèm điều kiện đầu. Sinh viên cũng cần học cách kiểm tra nghiệm cân bằng, miền xác định và ý nghĩa của hằng số tích phân, vì đây là những điểm thường bị bỏ sót.

## Kiến thức nền
Sinh viên cần thành thạo đạo hàm, nguyên hàm cơ bản, biến đổi đại số và quy tắc xử lý logarit. Việc hiểu rằng $$ \frac{dy}{dt} $$ có thể được xem như một đạo hàm liên hệ giữa hai đại lượng thay đổi đồng thời sẽ giúp quá trình tách biến trở nên tự nhiên hơn thay vì chỉ là một mẹo thao tác.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-02 Phương trình Tách biến]({{ site.imgurl }}/chapter_img/chapter01/01_02_separable_equations.svg)

Nhiều mô hình đầu tiên trong khoa học có dạng "tốc độ thay đổi bằng một yếu tố phụ thuộc thời gian nhân với một yếu tố phụ thuộc trạng thái". Chẳng hạn, tốc độ tăng dân số có thể phụ thuộc vào mùa vụ qua biến $$ t $$ nhưng cũng phụ thuộc vào quy mô hiện tại $$ P $$. Nếu hai ảnh hưởng ấy tách rời được, ta có thể gom mọi thứ liên quan tới trạng thái về một phía và mọi thứ liên quan tới thời gian về phía còn lại.

Điểm đẹp của phương pháp tách biến là nó vừa đơn giản vừa giàu ý nghĩa. Ta không chỉ "chuyển vế" cho thuận tay; ta đang lợi dụng cấu trúc nhân tử của mô hình để tích lũy ảnh hưởng của biến trạng thái và biến thời gian một cách riêng rẽ. Khi làm đúng, phương pháp này cho ta nghiệm một cách trực tiếp, đồng thời hé lộ các nghiệm cân bằng và các giới hạn miền xác định.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy tưởng tượng tốc độ thay đổi của một hệ là kết quả của hai chiếc núm vặn độc lập. Một núm chỉ phụ thuộc vào thời gian, một núm chỉ phụ thuộc vào trạng thái hiện tại. Nếu tách riêng được hai núm này, ta có thể nghiên cứu từng ảnh hưởng một rồi ghép lại qua tích phân.

### Cách nhìn hình ảnh
Trên slope field của
$$ \frac{dy}{dt}=g(t)h(y), $$
độ dốc tại mỗi điểm là tích của hai yếu tố. Nếu $$ h(y)=0 $$ tại một mức $$ y=y_* $$ thì cả một đường ngang sẽ có độ dốc bằng 0, tức là nghiệm cân bằng. Nếu $$ g(t) $$ đổi dấu theo thời gian, toàn bộ trường hướng có thể lật xu hướng trên các dải thẳng đứng. Hình ảnh này giúp sinh viên hiểu rằng việc tách biến phản ánh đúng cấu trúc hình học của trường hướng.

### Cách nhìn hình thức
Một ODE cấp một được gọi là tách biến được nếu có thể viết dưới dạng
$$ \frac{dy}{dt}=g(t)h(y). $$
Trên miền mà $$ h(y)\neq 0 $$, ta có thể viết
$$ \frac{1}{h(y)}dy=g(t)dt $$
và tích phân hai vế:
$$ \int \frac{1}{h(y)}dy=\int g(t)dt+C. $$
Tuy nhiên, các giá trị làm $$ h(y)=0 $$ phải được xét riêng vì chúng thường cho nghiệm cân bằng mà phép chia đã làm mất.

## Những điều cần nhấn mạnh về mặt lý thuyết
Phương pháp tách biến dựa trên hai ý tưởng. Thứ nhất, cấu trúc nhân tử cho phép ta gom các đại lượng cùng loại về một phía. Thứ hai, sau khi tích phân, ta nhận được quan hệ ẩn giữa $$ y $$ và $$ t $$, không phải lúc nào cũng cần hoặc có thể giải tường minh ra $$ y(t) $$.

Trong thực hành, ba câu hỏi quan trọng là: có thật sự tách được không, có bỏ quên nghiệm cân bằng nào không, và nghiệm hợp lệ trên miền nào. Nhiều sai sót phát sinh không phải ở phần tích phân, mà ở việc quên xét các trường hợp đặc biệt.

## Những ngộ nhận thường gặp
- "Cứ thấy có $$ y $$ và $$ t $$ là chuyển hết sang hai phía." Sai. Chỉ khi phương trình thật sự có dạng tách được.
- "Sau khi chia cho $$ h(y) $$ là xong." Chưa đủ. Nếu $$ h(y)=0 $$ ở đâu đó, ta có thể đã làm mất nghiệm cân bằng.
- "Tích phân xong là luôn giải được $$ y $$ tường minh." Không đúng. Nhiều bài cho nghiệm ẩn vẫn hoàn toàn chấp nhận được.
- "Điều kiện đầu chỉ cần thay vào cuối cùng." Không hẳn. Điều kiện đầu còn giúp chọn đúng miền và đúng nhánh của logarit hoặc căn thức.

## Tiến trình học tập đề xuất
### Bước 1: Nhận diện dạng nhân tử
Sinh viên luyện nhìn nhanh xem vế phải có thể viết thành $$ g(t)h(y) $$ hay không.

### Bước 2: Tách biến có kiểm soát
Viết rõ điều kiện $$ h(y)\neq 0 $$ trước khi chia, sau đó mới tích phân.

### Bước 3: Xét nghiệm cân bằng
Tìm các giá trị $$ y=y_* $$ làm vế phải bằng 0 và kiểm tra chúng có là nghiệm riêng hay không.

### Bước 4: Dùng điều kiện đầu
Thay điều kiện đầu để tìm hằng số và xác định miền nghiệm phù hợp.

### Các checkpoint
- Sinh viên có phát hiện được nghiệm cân bằng bị mất sau phép chia hay không.
- Sinh viên có viết được lời giải dưới dạng ẩn nếu cần hay không.
- Sinh viên có biết kiểm tra lại nghiệm bằng đạo hàm hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Tăng trưởng mũ
Giải bài toán
$$ \frac{dy}{dt}=3y,\qquad y(0)=2. $$
Ta tách biến:
$$ \frac{1}{y}dy=3dt. $$
Tích phân hai vế:
$$ \ln \lvert y\rvert=3t+C. $$
Suy ra
$$ y=Ce^{3t}. $$
Dùng điều kiện đầu:
$$ 2=Ce^0=C, $$
nên
$$ y(t)=2e^{3t}. $$
Đây là ví dụ cơ bản nhất, nhưng nó cho thấy rõ luồng suy nghĩ: tách, tích phân, dùng điều kiện đầu, rồi diễn giải nghiệm.

### Ví dụ 2: Bài toán có nghiệm cân bằng
Giải
$$ \frac{dy}{dt}=y(1-y). $$
Ta thấy ngay $$ y=0 $$ và $$ y=1 $$ là các nghiệm cân bằng. Với $$ y\neq 0,1 $$, ta tách biến:
$$ \frac{1}{y(1-y)}dy=dt. $$
Phân tích phân thức:
$$ \frac{1}{y(1-y)}=\frac{1}{y}+\frac{1}{1-y}. $$
Tích phân:
$$ \ln \lvert y\rvert-\ln \lvert 1-y\rvert=t+C. $$
Suy ra
$$ \frac{y}{1-y}=Ce^t $$
và
$$ y(t)=\frac{Ce^t}{1+Ce^t}. $$
Điểm sư phạm quan trọng là hai nghiệm cân bằng phải được nhắc riêng, vì phép chia cho $$ y(1-y) $$ đã loại chúng ra từ đầu.

### Ví dụ 3: Nghiệm nổ hữu hạn thời gian
Giải
$$ \frac{dy}{dt}=y^2,\qquad y(0)=1. $$
Ta viết
$$ \frac{1}{y^2}dy=dt. $$
Tích phân:
$$ -\frac{1}{y}=t+C. $$
Dùng điều kiện đầu:
$$ -1=C. $$
Vậy
$$ -\frac{1}{y}=t-1 $$
hay
$$ y(t)=\frac{1}{1-t}. $$
Nghiệm tồn tại với $$ t<1 $$ và nổ tại $$ t=1 $$. Đây là dịp rất tốt để nhấn mạnh rằng lời giải ODE không chỉ là công thức, mà còn là miền tồn tại của công thức đó.

### Ví dụ 4: Làm việc với nghiệm ẩn
Giải
$$ \frac{dy}{dt}=\frac{t}{1+y^2},\qquad y(0)=0. $$
Ta tách biến:
$$ \left(1+y^2\right)dy=tdt. $$
Tích phân:
$$ y+\frac{y^3}{3}=\frac{t^2}{2}+C. $$
Dùng điều kiện đầu $$ y(0)=0 $$ cho $$ C=0 $$, nên
$$ y+\frac{y^3}{3}=\frac{t^2}{2}. $$
Ta không cần giải tường minh ra $$ y $$ để xem đây là một nghiệm hợp lệ. Điều này giúp sinh viên thoát khỏi tâm lý "không cô lập được $$ y $$ tức là chưa giải xong".

## Câu hỏi khái niệm
1. Vì sao phải xét riêng các nghiệm cân bằng trước khi chia cho $$ h(y) $$?
2. Vì sao một nghiệm ẩn vẫn là một lời giải hoàn chỉnh của ODE?
3. Trong bối cảnh ứng dụng, miền xác định của nghiệm cho ta thông tin gì ngoài công thức?

## Bài toán ứng dụng
1. Một phản ứng hóa học có tốc độ biến thiên nồng độ tỉ lệ với tích của nồng độ hiện tại và một hàm đã biết của thời gian. Hãy giải thích vì sao mô hình này gợi ý phương pháp tách biến.
2. Một quần thể cá tăng trưởng theo logistic. Hãy giải thích ý nghĩa vật lý của hai nghiệm cân bằng.
3. Một mô hình dân số đơn giản cho nghiệm có dạng $$ \frac{1}{1-t} $$. Trong thực tế, việc nghiệm nổ tại thời gian hữu hạn cảnh báo điều gì về mô hình?

## Chiến lược giảng dạy tương tác
- Cho sinh viên quyết định nhanh 10 phương trình: tách được hay không tách được, và yêu cầu giải thích chỉ bằng một câu.
- Khi chữa ví dụ logistic, dừng lại trước bước chia để hỏi: "Nếu chia bây giờ, ta có nguy cơ làm mất điều gì?"
- Yêu cầu từng nhóm vẽ sơ bộ đồ thị các nghiệm cân bằng và nghiệm không cân bằng trên cùng một hình để thấy bức tranh toàn cục.
- Mời sinh viên diễn giải bằng lời miền tồn tại của nghiệm ở ví dụ $$ y' = y^2 $$ thay vì chỉ đọc công thức.

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp một checklist ngắn: nhận dạng dạng $$ g(t)h(y) $$, xét nghiệm cân bằng, tách biến, tích phân, dùng điều kiện đầu, kiểm tra miền. Việc cho sinh viên điền vào từng ô trong checklist thường hiệu quả hơn việc cho lời giải hoàn chỉnh ngay từ đầu.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi so sánh hai lời giải của logistic: dùng tách biến và dùng phân tích định tính qua đường pha. Một hướng mở rộng khác là yêu cầu giải thích vì sao một số ODE tách biến dẫn đến nghiệm ẩn không sơ cấp.

## Tóm tắt dễ nhớ
Phương trình tách biến là ODE mà ảnh hưởng của thời gian và trạng thái có thể tách riêng. Cốt lõi không phải là "chuyển vế", mà là nhận ra cấu trúc nhân tử của mô hình. Luôn nhớ ba điều: xét nghiệm cân bằng trước khi chia, chấp nhận nghiệm ẩn khi cần, và kiểm tra miền tồn tại sau khi giải.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân rã phóng xạ
- Bài toán: Một đồng vị y khoa mất dần hoạt tính theo thời gian và bác sĩ cần biết lượng hoạt chất còn lại sau vài giờ.
- Mô hình:
$$ \frac{dN}{dt}=-\lambda N. $$
- Giả thiết và giới hạn: Ta giả sử mỗi hạt nhân phân rã độc lập với xác suất không đổi theo thời gian. Mô hình không mô tả chuỗi phân rã nhiều bước hay ảnh hưởng môi trường.
- Diễn giải: Nghiệm
$$ N(t)=N_0e^{-\lambda t} $$
giải thích trực tiếp khái niệm chu kỳ bán rã và vì sao phần trăm giảm không đổi nhưng lượng giảm tuyệt đối thì nhỏ dần.

#### Tăng trưởng logistic trong sinh thái
- Bài toán: Một quần thể cá trong hồ tăng nhanh khi còn ít cá, nhưng chậm dần khi tiến gần sức chứa môi trường.
- Mô hình:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$
- Giả thiết và giới hạn: Ta giả sử môi trường đồng nhất, sức chứa $$ K $$ cố định, và không có cấu trúc tuổi hay mùa vụ. Thực tế, thời tiết, thức ăn và khai thác làm mô hình phức tạp hơn nhiều.
- Diễn giải: Nghiệm logistic cho thấy ban đầu gần giống tăng trưởng mũ, nhưng dài hạn bị bão hòa quanh $$ K $$. Đây là một bài học rất mạnh về việc mô hình đơn giản có thể sửa sai cho mô hình mũ ở đâu.

#### Vận tốc rơi với lực cản bậc hai
- Bài toán: Một người nhảy dù ban đầu tăng tốc nhanh, rồi dần tiến tới vận tốc giới hạn.
- Mô hình:
$$ \frac{dv}{dt}=g-kv^2. $$
- Giả thiết và giới hạn: Ta giả sử hướng rơi thẳng đứng, khối lượng không đổi, và lực cản tỉ lệ với bình phương vận tốc. Giai đoạn mở dù hoặc thay đổi tư thế không nằm trong mô hình này.
- Diễn giải: Vì phương trình tách biến được, ta thấy rất rõ vận tốc không thể tăng vô hạn mà bị chặn bởi $$ \sqrt{g/k} $$.

### 2. Trực giác bổ sung và các kết nối

Điểm sâu sắc của phương trình tách biến là ta không "chuyển vi phân" một cách mơ hồ, mà đang khai thác cấu trúc nhân tử của luật động học. Khi một ODE có dạng $$ y'=g(t)h(y) $$, ảnh hưởng của đồng hồ và ảnh hưởng của trạng thái đã tách rời, nên phép tích phân hai phía là hợp lý. Bài học này nối tự nhiên sang chương về phương trình tự trị: nếu $$ g(t)=1 $$, toàn bộ động lực nằm trong dấu của $$ h(y) $$. Nó cũng nối sang chương tồn tại và duy nhất, vì nhiều nghiệm tách biến có thể nổ hữu hạn thời gian hoặc có nghiệm cân bằng bị bỏ quên nếu ta chia ẩu cho $$ h(y) $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.8, 100
t = np.linspace(0, 12, 400)
P0_values = [5, 20, 60, 140]

for P0 in P0_values:
    C = (K - P0) / P0
    P = K / (1 + C * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="K")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Nghiệm logistic với nhiều điều kiện đầu")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Hình này làm nổi bật hai ý: dữ kiện đầu thay đổi quỹ đạo ngắn hạn, còn sức chứa $$ K $$ quyết định hành vi dài hạn; và nghiệm trên $$ K $$ sẽ giảm xuống, trong khi nghiệm dưới $$ K $$ tăng lên.

### 4. Gợi ý tìm thêm mô phỏng

- search: logistic equation phase line
- search: radioactive decay simulation differential equation
- search: skydiver quadratic drag solution

### 5. Bài toán mẫu có bối cảnh thực

Một hồ nuôi cá có sức chứa 5000 con, tốc độ tăng trưởng nội tại 0.6 mỗi năm, và hiện có 800 con. Mô hình logistic là
$$
\frac{dP}{dt}=0.6P\left(1-\frac{P}{5000}\right),\qquad P(0)=800.
$$
Tách biến cho ta
$$ P(t)=\frac{5000}{1+5.25e^{-0.6t}}. $$
Nếu muốn dự đoán nhanh trong quản lý thủy sản, nghiệm này cho thấy đàn cá tăng nhanh trong giai đoạn đầu nhưng tốc độ tăng giảm dần khi hồ trở nên chật hơn. Một Euler sơ cấp với bước một quý cũng có thể tái hiện xu hướng, nhưng nghiệm giải tích giúp ta nhìn chính xác hơn thời gian tiến gần sức chứa.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo nhận diện dạng $$ g(t)h(y) $$, xét nghiệm cân bằng trước khi chia, và chấp nhận nghiệm ẩn khi không thể cô lập $$ y $$.

**Bậc sau đại học.** Thảo luận thêm về thời gian nổ hữu hạn, bất biến miền, và tính đơn điệu của nghiệm. Đây cũng là chỗ thích hợp để nối với kỹ thuật tách biến trong PDE, nơi ta tách không phải hai biến của cùng một hàm mà là các nhân tử của một nghiệm giả định.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rất rõ phương pháp tách biến và logistic.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài luyện nhận dạng và phân tích hằng số tích phân.
- Ross — *Differential Equations*: phù hợp để xem thêm những ví dụ ngắn nhưng đa dạng về miền xác định.
