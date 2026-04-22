---
layout: post
title: "01-07 Ứng dụng: Mô hình Dân số và Pha trộn"
chapter: '01'
order: 7
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên thấy rõ cách ODE bước ra khỏi trang giấy để trở thành mô hình cho các hệ thực. Qua các bài toán dân số và bể trộn, sinh viên học cách dịch ngôn ngữ đời sống sang phương trình, giải mô hình, đọc ý nghĩa của nghiệm và đánh giá xem mô hình nào đơn giản quá mức hoặc đủ thuyết phục cho mục tiêu phân tích.

## Kiến thức nền
Sinh viên nên nắm phương trình tách biến, phương trình tuyến tính cấp một và kỹ năng kiểm tra đơn vị. Các mô hình ứng dụng dễ bị làm máy móc nếu người học không hiểu ý nghĩa của từng đại lượng, nên việc luyện đọc đơn vị vật lý và xác định "tốc độ vào trừ tốc độ ra" là rất quan trọng.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-07 Ứng dụng: Mô hình Dân số và Pha trộn]({{ site.imgurl }}/chapter_img/chapter01/01_07_applications_population_mixing.svg)

Một mô hình toán học hay không bắt đầu bằng công thức đẹp, mà bắt đầu bằng một câu hỏi đúng. Dân số thay đổi do sinh và chết. Muối trong bể thay đổi do dòng vào và dòng ra. Mấu chốt là xác định đại lượng trạng thái, rồi viết tốc độ biến thiên của nó thành tổng các cơ chế tác động. Khi làm được điều đó, ODE trở thành chiếc cầu nối tự nhiên giữa quan sát và dự đoán.

Hai lớp bài toán trong bài này đặc biệt tốt về mặt sư phạm. Mô hình dân số giúp sinh viên thấy được tăng trưởng, bão hòa và vai trò của điểm cân bằng. Mô hình pha trộn giúp các em thực hành một nguyên lý rất phổ quát của khoa học ứng dụng: tốc độ thay đổi bằng tốc độ vào trừ tốc độ ra. Cả hai đều là những bài toán lý tưởng để luyện tư duy mô hình hóa.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Trong mô hình dân số, nếu một quần thể càng lớn thì số cá thể sinh mới trong một khoảng thời gian ngắn càng nhiều. Nhưng nếu tài nguyên có hạn, tốc độ tăng không thể tăng mãi. Trong bể trộn, lượng chất tan thay đổi theo cán cân giữa những gì được bơm vào và những gì bị cuốn ra ngoài.

### Cách nhìn hình ảnh
Đồ thị nghiệm của tăng trưởng mũ và logistic nhìn rất khác nhau. Tăng trưởng mũ cong lên mãi, còn logistic bắt đầu giống mũ rồi dần phẳng ra khi tiến gần sức chứa. Với bể trộn, đồ thị lượng muối thường tiến dần về một mức cân bằng, cho thấy hệ "quên" trạng thái đầu và bị chi phối bởi điều kiện dòng vào lâu dài.

### Cách nhìn hình thức
Ba mô hình kinh điển là:

Tăng trưởng mũ:
$$ \frac{dP}{dt}=rP. $$

Tăng trưởng logistic:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$

Bể trộn thể tích không đổi:
$$ \frac{dS}{dt}=\text{tốc độ vào}-\text{tốc độ ra}. $$
Nếu nồng độ trong bể đồng đều, tốc độ ra thường bằng lưu lượng ra nhân với nồng độ tức thời trong bể.

## Những ý tưởng mô hình hóa cốt lõi
Trong mọi bài toán ứng dụng, bước quan trọng nhất là lựa chọn biến trạng thái. Với dân số, biến trạng thái là số cá thể $$ P(t) $$. Với bể trộn, đó là lượng chất tan $$ S(t) $$ chứ không phải nồng độ, trừ khi ta chủ ý chọn nồng độ. Sau đó ta viết cân bằng tốc độ.

Một điểm sư phạm cần nhấn mạnh là mô hình không chỉ là kỹ thuật giải. Khi sinh viên viết được phương trình đúng nhưng không giải được ngay, điều đó vẫn là một thành công lớn trong mô hình hóa. Từ góc nhìn giáo dục, đây là nơi ta dạy các em rằng toán học ứng dụng là quá trình ra quyết định có lý do.

## Những ngộ nhận thường gặp
- "Mô hình dân số luôn là tăng trưởng mũ." Sai. Tăng trưởng mũ chỉ hợp lý trong giai đoạn đầu hoặc khi tài nguyên chưa giới hạn.
- "Trong bể trộn, tốc độ ra là hằng số." Sai. Nó thường phụ thuộc vào nồng độ tức thời trong bể.
- "Giải ra được công thức thì mô hình chắc chắn đúng." Sai. Một công thức đẹp vẫn có thể dựa trên giả thiết kém thực tế.
- "Điểm cân bằng chỉ là khái niệm hình thức." Sai. Trong ứng dụng, nó thường là trạng thái dài hạn mà hệ tiến tới.

## Tiến trình học tập đề xuất
### Bước 1: Chọn biến trạng thái
Hỏi rõ đại lượng nào cần theo dõi theo thời gian.

### Bước 2: Viết cân bằng tốc độ
Với dân số là sinh trừ chết hoặc tăng trưởng thuần. Với bể trộn là vào trừ ra.

### Bước 3: Kiểm tra đơn vị
Mỗi vế của phương trình phải cùng đơn vị, ví dụ kg/phút hoặc cá thể/ngày.

### Bước 4: Giải và diễn giải
Không chỉ tìm công thức mà còn đọc giới hạn dài hạn, ngưỡng bão hòa và độ nhạy theo tham số.

### Các checkpoint
- Sinh viên có chọn đúng biến trạng thái hay không.
- Sinh viên có viết đúng tốc độ ra của bể trộn bằng nồng độ tức thời nhân lưu lượng ra hay không.
- Sinh viên có phân biệt được tăng trưởng mũ và logistic về mặt ý nghĩa hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Tăng trưởng dân số mũ
Giả sử dân số thỏa
$$ \frac{dP}{dt}=0.04P,\qquad P(0)=1000. $$
Phương trình tách biến cho nghiệm
$$ P(t)=1000e^{0.04t}. $$
Mô hình này dự đoán dân số tăng vô hạn. Nó hợp lý ở giai đoạn đầu khi tài nguyên chưa tạo áp lực.

### Ví dụ 2: Mô hình logistic
Xét
$$
\frac{dP}{dt}=0.5P\left(1-\frac{P}{1000}\right),\qquad P(0)=100.
$$
Đây là phương trình logistic với sức chứa
$$ K=1000. $$
Tách biến hoặc dùng công thức chuẩn, ta được
$$ P(t)=\frac{1000}{1+9e^{-0.5t}}. $$
Nghiệm tăng nhanh lúc đầu rồi chậm dần khi tiến về 1000. Điểm cân bằng $$ P=1000 $$ có ý nghĩa sinh thái rõ rệt: đó là mức dân số mà môi trường có thể duy trì lâu dài.

### Ví dụ 3: Bể trộn thể tích không đổi
Một bể 200 lít ban đầu chứa 20 kg muối. Dung dịch 0.1 kg/lít chảy vào với tốc độ 4 lít/phút, và hỗn hợp chảy ra cũng với 4 lít/phút. Gọi $$ S(t) $$ là lượng muối trong bể.

Tốc độ vào:
$$ 0.1\cdot 4=0.4\text{ kg/phút}. $$
Nồng độ trong bể là $$ \frac{S}{200} $$, nên tốc độ ra:
$$ 4\cdot \frac{S}{200}=\frac{S}{50}. $$
Vì vậy,
$$ \frac{dS}{dt}=0.4-\frac{S}{50}. $$
Đây là phương trình tuyến tính cấp một. Giải ra:
$$ S(t)=20+Ce^{-t/50}. $$
Với $$ S(0)=20 $$, ta được
$$ C=0. $$
Điều này có nghĩa trạng thái ban đầu đã đúng bằng trạng thái cân bằng, nên lượng muối không đổi theo thời gian. Đây là ví dụ rất hay để dạy sinh viên kiểm tra tính hợp lý trước khi lao vào tính toán dài dòng.

### Ví dụ 4: Bể trộn với trạng thái ban đầu không cân bằng
Giữ nguyên dữ kiện ví dụ trên nhưng thay $$ S(0)=0 $$. Khi đó
$$ S(t)=20-20e^{-t/50}. $$
Lượng muối tăng dần từ 0 lên 20 kg. Bài này giúp sinh viên thấy rõ "bộ nhớ của điều kiện đầu" nằm trong số hạng mũ suy giảm.

## Câu hỏi khái niệm
1. Vì sao tăng trưởng logistic thường hợp lý hơn tăng trưởng mũ trong mô hình dân số dài hạn?
2. Trong bể trộn, vì sao tốc độ ra phải phụ thuộc vào nồng độ tức thời chứ không chỉ vào lưu lượng?
3. Một nghiệm tiến dần về cân bằng cho ta thông tin gì về hành vi dài hạn của hệ?

## Bài toán ứng dụng
1. Một đàn hươu trong khu bảo tồn tăng nhanh trong vài năm đầu rồi chậm lại. Hãy tranh luận khi nào nên dùng mô hình mũ và khi nào nên dùng logistic.
2. Một bệnh nhân được truyền thuốc vào máu với tốc độ không đổi trong khi cơ thể đào thải với tốc độ tỉ lệ với lượng thuốc hiện tại. Hãy chỉ ra cấu trúc tương tự với bài toán bể trộn.
3. Một hồ chứa chất ô nhiễm nhận dòng thải vào và có dòng nước chảy ra. Hãy mô tả những giả thiết nào cần có để mô hình pha trộn đều trở nên hợp lý.

## Chiến lược giảng dạy tương tác
- Bắt đầu bằng hoạt động "dịch từ đời sống sang toán": đưa cho sinh viên ba câu mô tả hiện tượng và yêu cầu mỗi nhóm viết biến trạng thái cùng phương trình sơ bộ.
- Dừng ở bước lập mô hình và yêu cầu lớp kiểm tra đơn vị trước khi giải.
- Cho sinh viên dự đoán nghiệm dài hạn bằng trực giác trước, rồi sau đó dùng công thức để xác nhận.
- Tổ chức thảo luận ngắn về câu hỏi: "Một mô hình đơn giản nhưng giải được có tốt hơn một mô hình chân thực nhưng khó giải không?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên cung cấp sơ đồ hai cột "vào" và "ra" cho các bài toán pha trộn, đồng thời yêu cầu sinh viên luôn điền đơn vị vào mỗi số hạng. Với dân số, có thể bắt đầu bằng phân tích bằng lời trước khi viết ODE.

### Thử thách cho sinh viên khá giỏi
Có thể yêu cầu sinh viên khá giỏi thêm các hiệu ứng như thu hoạch hằng số vào logistic, hoặc xét bể trộn có thể tích thay đổi theo thời gian. Những mở rộng này giúp các em thấy mô hình có thể phát triển tự nhiên như thế nào.

## Tóm tắt dễ nhớ
Ứng dụng của ODE bắt đầu từ việc chọn đúng biến trạng thái và viết đúng cân bằng tốc độ. Dân số dạy ta về tăng trưởng và bão hòa. Bể trộn dạy ta quy luật "vào trừ ra". Công thức nghiệm quan trọng, nhưng tư duy mô hình hóa còn quan trọng hơn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quần thể động vật với sức chứa môi trường
- Bài toán: Một đàn hươu trong khu bảo tồn tăng nhanh khi còn ít cá thể, nhưng nguồn thức ăn và không gian giới hạn tốc độ tăng về sau.
- Mô hình:
$$ \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right). $$
- Giả thiết và giới hạn: Sức chứa $$ K $$ cố định và quần thể đồng nhất. Mô hình chưa có săn bắt, mùa vụ, hay cấu trúc tuổi.
- Diễn giải: Nghiệm cho thấy ban đầu gần như mũ, còn dài hạn tiến tới cân bằng sinh thái.

#### Bể trộn xử lý nước
- Bài toán: Một bể xử lý có dòng vào chứa chất ô nhiễm và dòng ra cùng lưu lượng; kỹ sư muốn biết nồng độ trong bể sau một giờ.
- Mô hình:
$$
\frac{dS}{dt}=q_{\mathrm{in}}c_{\mathrm{in}}-q_{\mathrm{out}}\frac{S}{V}.
$$
- Giả thiết và giới hạn: Bể được khuấy đều hoàn hảo và thể tích $$ V $$ không đổi. Bất đồng nhất không gian hoặc lắng cặn mạnh sẽ phá mô hình này.
- Diễn giải: Bài toán cho sinh viên thấy định luật "vào trừ ra" mạnh đến mức nào trong kỹ thuật môi trường.

#### Dược động học một ngăn với truyền liên tục
- Bài toán: Một bệnh nhân được truyền thuốc với tốc độ không đổi, trong khi cơ thể đào thải theo tốc độ tỉ lệ nồng độ.
- Mô hình:
$$ \frac{dC}{dt}=\frac{u_0}{V}-kC. $$
- Giả thiết và giới hạn: Thuốc trộn đều tức thời và tốc độ đào thải bậc một. Nhiều thuốc thật đòi hỏi mô hình hai hoặc ba ngăn.
- Diễn giải: Nồng độ tiến dần tới một giá trị ổn định, điều rất quan trọng trong thiết kế phác đồ liều.

### 2. Trực giác bổ sung và các kết nối

Bài học này là nơi mô hình hóa trở thành trung tâm chứ không chỉ là ví dụ minh họa. Sinh viên phải học cách chọn biến trạng thái hợp lý, kiểm tra đơn vị, và biết khi nào nên mô hình hóa lượng chất thay vì nồng độ. Đây cũng là cầu nối mạnh sang chương tự trị và ổn định: logistic không chỉ là bài toán tách biến, mà còn là bài toán cân bằng và hút quỹ đạo. Trong khi đó, bể trộn là mô hình tuyến tính đầu tiên mang màu sắc của cân bằng khối lượng, thứ sẽ lặp lại trong hóa kỹ thuật, sinh học hệ thống và kỹ thuật môi trường.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.5, 1000
t = np.linspace(0, 25, 400)
for P0 in [50, 150, 400, 1200]:
    P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="carrying capacity")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Quần thể logistic tiến về sức chứa")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị này rất phù hợp để bàn về ý nghĩa sinh học của cân bằng ổn định và về lý do mô hình logistic thường hợp lý hơn mô hình mũ trong trung hạn.

### 4. Gợi ý tìm thêm mô phỏng

- search: mixing tank differential equation simulation
- search: logistic growth carrying capacity interactive
- search: pharmacokinetics one compartment ODE plot

### 5. Bài toán mẫu có bối cảnh thực

Một bể chứa 200 lít nước sạch ban đầu có 8 kg muối. Dung dịch vào có nồng độ 0.05 kg/lít với lưu lượng 4 lít/phút, và dòng ra cũng là 4 lít/phút. Khi đó
$$ \frac{dS}{dt}=0.2-\frac{4}{200}S,
\qquad
S(0)=8. $$
Giải tuyến tính cho ta
$$ S(t)=10-2e^{-0.02t}. $$
Nghiệm chỉ ra bể sẽ tiến về 10 kg muối, tức là tiến về nồng độ đúng bằng nồng độ đầu vào. Cách diễn giải này quan trọng hơn chính công thức, vì nó cho thấy hệ cuối cùng "quên" điều kiện đầu như thế nào.

### 6. Phân tầng độ khó

**Bậc đại học.** Tập trung vào chọn biến đúng, viết cân bằng tốc độ, và giải thích kết quả bằng đơn vị và ý nghĩa vật lý.

**Bậc sau đại học.** Bàn thêm về tính dương của nghiệm, ước lượng tham số từ dữ liệu, nondimensionalization, và tính nhận dạng mô hình. Đây là nơi rất tốt để bắt đầu thảo luận "mọi mô hình đều sai, nhưng có mô hình hữu ích".

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: rất mạnh ở các mô hình dân số, pha trộn và diễn giải vật lý.
- Zill — *Differential Equations with Boundary-Value Problems*: có nhiều bài tập thực hành mô hình hóa bằng ngôn ngữ đời sống.
- Ross — *Differential Equations*: hữu ích để xem thêm các biến thể của logistic và các mô hình trộn đơn giản.
