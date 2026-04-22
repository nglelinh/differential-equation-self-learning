---
layout: post
title: "06-03 Phương trình Euler"
chapter: '06'
order: 3
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên nhận ra và giải được phương trình Euler, còn gọi là Cauchy-Euler, như một cầu nối rất đẹp giữa nghiệm dạng lũy thừa, phương trình đặc trưng và phép đổi biến logarit. Sau bài học, sinh viên cần biết vì sao phép thử dạng $$ x^r $$ là tự nhiên, biết phân loại ba trường hợp nghiệm, và biết liên hệ phương trình Euler với phương trình hệ số hằng sau phép đổi biến phù hợp.

## Kiến thức nền

Sinh viên nên quen với phương trình tuyến tính cấp hai hệ số hằng, phương trình đặc trưng, nghiệm kép, nghiệm phức, cùng các phép biến đổi đạo hàm cơ bản. Trực giác về hàm lũy thừa và logarit rất quan trọng cho bài này.

## Dẫn nhập

![Phương trình Euler-Cauchy và dạng nghiệm lũy thừa]({{ site.imgurl }}/chapter_img/chapter06/03_euler_equations.svg)

Phương trình Euler trông khác các phương trình hệ số hằng vì hệ số trước đạo hàm thay đổi theo biến số. Tuy nhiên, sự thay đổi này rất đặc biệt: mỗi đạo hàm được ghép với một lũy thừa của $$ x $$ sao cho toàn bộ phương trình giữ được tính đồng dạng theo phép co giãn. Điều đó khiến nghiệm lũy thừa xuất hiện một cách tự nhiên, giống như hàm mũ xuất hiện ở phương trình hệ số hằng.

Đây là một bài học quan trọng vì nó giúp sinh viên thấy rằng "đoán dạng nghiệm" không phải mẹo tùy tiện. Dạng nghiệm đúng thường phản ánh đối xứng ẩn của phương trình. Với Euler, đối xứng đó là co giãn.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một bài toán không thay đổi bản chất khi ta phóng to hay thu nhỏ trục không gian, thì nghiệm hợp lý thường cũng thay đổi theo quy luật tỉ lệ. Hàm lũy thừa $$ y=x^r $$ có đúng tính chất này: thay $$ x $$ bởi $$ cx $$ chỉ tạo thêm một hệ số $$ c^r $$. Vì vậy nó là ứng viên rất tự nhiên.

### Cách nhìn hình ảnh

Trên đồ thị log-log, hàm lũy thừa trở thành đường thẳng. Do đó phương trình Euler có thể được hiểu như một bài toán trở nên "thẳng hóa" sau khi nhìn trong thang logarit. Khi nghiệm phức xuất hiện, đồ thị dao động không còn theo $$ x $$ trực tiếp mà theo $$ \ln x $$, tạo nên dao động theo thang logarit.

### Cách nhìn hình thức

Phương trình Euler cấp hai có dạng

$$ x^2y''+a x y'+b y=0,
\qquad x>0. $$

Thử nghiệm $$ y=x^r $$. Khi đó

$$ y'=r x^{r-1},
\qquad
y''=r(r-1)x^{r-2}. $$

Thế vào phương trình:

$$ x^2r(r-1)x^{r-2}+a x r x^{r-1}+b x^r=0. $$

Rút gọn:

$$ \left[r(r-1)+ar+b\right]x^r=0. $$

Suy ra phương trình chỉ số $$ r(r-1)+ar+b=0 $$. Tùy theo nghiệm của phương trình bậc hai này, ta có ba trường hợp nghiệm quen thuộc.

## Những ngộ nhận thường gặp

- "Phương trình Euler chỉ là một dạng lạ của hệ số hằng nên không cần hiểu riêng." Sai. Nó có đối xứng khác và nghiệm mang ý nghĩa co giãn rõ rệt.
- "Chỉ cần nhớ công thức nghiệm." Chưa đủ. Điều quan trọng là nhận ra lúc nào phương trình đúng dạng Euler.
- "Nếu có nghiệm kép thì cứ viết hai nghiệm giống nhau." Sai. Nghiệm thứ hai phải kèm thừa số logarit.
- "Nghiệm phức nghĩa là không có nghiệm thực." Sai. Từ nghiệm phức, ta luôn tổ hợp được hai nghiệm thực độc lập.

## Tiến trình học tập đề xuất

### Bước 1: Nhận dạng đúng dạng Euler

Sinh viên cần nhìn thấy mô hình $$ x^2y''+a x y'+b y=0 $$ hoặc dạng có thể quy về mô hình này.

### Bước 2: Thử nghiệm lũy thừa

Đặt $$ y=x^r $$ và xây dựng phương trình chỉ số.

### Bước 3: Phân loại nghiệm của phương trình chỉ số

Thực hiện giống tư duy phương trình đặc trưng của hệ số hằng.

### Bước 4: Kiểm tra miền xác định

Nhấn mạnh điều kiện $$ x>0 $$ khi dùng logarit và nghiệm lũy thừa thực.

### Bước 5: Kết nối với phép đổi biến

Đặt $$ x=e^t $$ để thấy phương trình Euler thật ra biến thành hệ số hằng trong biến mới.

### Các checkpoint

- Sinh viên có nhận ra dạng Euler nhanh hay không.
- Sinh viên có lập đúng phương trình chỉ số hay không.
- Sinh viên có phân biệt đúng ba loại nghiệm hay không.
- Sinh viên có giải thích được vì sao xuất hiện $$ \ln x $$ trong trường hợp nghiệm kép hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hai nghiệm thực phân biệt

Giải $$ x^2y''-3xy'+4y=0 $$. Đặt $$ y=x^r $$. Phương trình chỉ số là

$$
r(r-1)-3r+4=0
\quad \Longleftrightarrow \quad
r^2-4r+4=0.
$$

Ở đây ta được nghiệm kép $$ r=2 $$. Ví dụ này thực ra rơi vào trường hợp nghiệm kép, nên rất thích hợp để nhắc sinh viên phải kiểm tra kỹ biệt thức thay vì nhìn nhanh. Nghiệm tổng quát là

$$ y=c_1x^2+c_2x^2\ln x. $$

### Ví dụ 2: Hai nghiệm thực phân biệt thật sự

Giải $$ x^2y''+x y'-y=0 $$. Phương trình chỉ số:

$$
r(r-1)+r-1=0
\quad \Longleftrightarrow \quad
r^2-1=0.
$$

Suy ra $$ r_1=1,\qquad r_2=-1 $$. Vậy nghiệm tổng quát là $$ y=c_1x+c_2x^{-1} $$. Đây là ví dụ cơ bản nhất cho thấy nghiệm Euler thật sự là tổ hợp các hàm lũy thừa.

### Ví dụ 3: Nghiệm kép và vai trò của logarit

Giải $$ x^2y''-x y'+y=0 $$. Ta có

$$
r(r-1)-r+1=0
\quad \Longleftrightarrow \quad
r^2-2r+1=0
\quad \Longleftrightarrow \quad
(r-1)^2=0.
$$

Vậy nghiệm kép là $$ r=1 $$. Nghiệm tổng quát:

$$ y=c_1x+c_2x\ln x. $$

Ví dụ này nên được dùng để hỏi sinh viên: vì sao $$ x $$ và $$ x\ln x $$ vẫn độc lập tuyến tính dù trông khá giống nhau?

### Ví dụ 4: Nghiệm phức

Giải $$ x^2y''+x y'+4y=0 $$. Phương trình chỉ số:

$$
r(r-1)+r+4=0
\quad \Longleftrightarrow \quad
r^2+4=0.
$$

Suy ra $$ r=\pm 2i $$. Viết dưới dạng thực:

$$ y=c_1\cos(2\ln x)+c_2\sin(2\ln x). $$

Bài này rất mạnh về trực giác: dao động không theo $$ x $$ mà theo logarit của $$ x $$.

### Ví dụ 5: Dùng phép đổi biến

Với phương trình $$ x^2y''+3xy'+y=0 $$, đặt

$$ x=e^t,
\qquad
u(t)=y(e^t). $$

Khi đó có thể chứng minh rằng

$$ x y' = u',
\qquad
x^2 y''=u''-u'. $$

Phương trình trở thành $$ u''+2u'+u=0 $$. Đây là phương trình hệ số hằng với nghiệm $$ u=(c_1+c_2 t)e^{-t} $$. Suy ra $$ y=(c_1+c_2\ln x)x^{-1} $$. Ví dụ này giúp sinh viên thấy công thức nghiệm Euler không rơi từ trên trời xuống.

## Câu hỏi khái niệm

1. Vì sao phép thử $$ y=x^r $$ là tự nhiên hơn nhiều so với thử $$ y=e^{rx} $$ cho phương trình Euler?
2. Vì sao nghiệm kép lại kéo theo thừa số $$ \ln x $$ chứ không phải một lũy thừa mới?
3. Nghiệm phức của phương trình Euler cho ta trực giác gì về đối xứng co giãn của bài toán?

## Bài toán ứng dụng

1. Trong mô hình đàn hồi hoặc truyền nhiệt gần một đầu nhọn, các phương trình dạng Euler thường xuất hiện. Hãy giải thích vì sao tính co giãn của hình học liên quan đến dạng phương trình này.
2. Trong cơ học chất lưu, nếu một mô hình giữ nguyên bản chất dưới phép đổi thang kích thước, vì sao nghiệm lũy thừa thường là lựa chọn hợp lý?
3. Trong phân tích dữ liệu thực nghiệm trên đồ thị log-log, vì sao việc nhận diện đường thẳng thường gợi ý một quy luật lũy thừa?

## Chiến lược giảng dạy tương tác

- Cho sinh viên so sánh bảng ba trường hợp của Euler với bảng ba trường hợp của phương trình hệ số hằng để thấy cấu trúc tương tự.
- Hỏi cả lớp: "Nếu thay $$ x $$ bằng $$ cx $$ thì hàm mũ và hàm lũy thừa phản ứng khác nhau thế nào?"
- Dùng đồ thị log-log để minh họa tại sao hàm lũy thừa trở thành lựa chọn tự nhiên.
- Cho các nhóm tự kiểm tra tính độc lập tuyến tính của $$ x^r $$ và $$ x^r\ln x $$ bằng Wronskian.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho các em một bảng quy trình gồm bốn cột: phương trình, phương trình chỉ số, loại nghiệm, dạng nghiệm tổng quát. Khi có khung sườn rõ ràng, việc nhận dạng bài toán sẽ nhẹ hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi tự chứng minh phép đổi biến $$ x=e^t $$ biến phương trình Euler thành phương trình hệ số hằng, rồi so sánh hai cách giải để thấy cấu trúc sâu hơn phía sau công thức.

## Tóm tắt dễ nhớ

Phương trình Euler là phương trình bất biến theo co giãn, nên nghiệm lũy thừa là lựa chọn tự nhiên. Ta thử $$ y=x^r $$ để nhận phương trình chỉ số. Hai nghiệm thực cho hai lũy thừa, nghiệm kép cho thêm $$ \ln x $$, và nghiệm phức cho dao động theo

$$ \ln x. $$

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Truyền nhiệt hoặc điện thế trong hình học tự đồng dạng
- Bài toán: Các mô hình có tính co giãn theo tỷ lệ thường dẫn tới phương trình Euler-Cauchy.
- Mô hình:
$$ x^2 y''+a x y'+b y=0. $$
- Giả thiết và giới hạn: Miền thường là $$ x>0 $$ và bài toán có cấu trúc bất biến theo phép co giãn.
- Diễn giải: Nghiệm dạng $$ x^r $$ phản ánh trực tiếp bản chất power-law của hệ.

#### Mô hình kinh tế với đàn hồi không đổi
- Bài toán: Một đại lượng tăng trưởng theo thời gian với hệ số tỉ lệ nghịch theo $$ t $$.
- Mô hình:
$$ t^2 K''+\alpha t K'+\beta K=0. $$
- Giả thiết và giới hạn: Chỉ là mô hình lý tưởng hóa của cấu trúc co giãn theo thang thời gian.
- Diễn giải: Các nghiệm lũy thừa mô tả chế độ tăng trưởng hay suy giảm theo hàm mũ của $$ \ln t $$.

### 2. Trực giác bổ sung và các kết nối

Phương trình Euler đặc biệt vì thay vì nghiệm $$ e^{\lambda x} $$ như hệ số hằng, ta tìm nghiệm $$ x^r $$ do hệ bất biến theo co giãn. Phép đổi biến $$ x=e^t $$ biến Euler-Cauchy thành ODE hệ số hằng. Bẫy phổ biến là quên rằng trường hợp nghiệm kép hay nghiệm phức kéo theo nhân tử $$ \ln x $$ hoặc dao động theo $$ \ln x $$.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.2, 5, 400)
y1 = x**2
y2 = x**2 * np.log(x)

plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^2 log x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dang nghiem tieu bieu cua phuong trinh Euler")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Cauchy Euler equation log transform
- search: equidimensional equation power law solutions
- search: scaling invariant ODE visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét
$$ x^2 y''-3x y'+4y=0. $$
Đặt $$ y=x^r $$, ta được phương trình đặc trưng
$$ r(r-1)-3r+4=0 $$
hay
$$ r^2-4r+4=(r-2)^2=0. $$
Vì nghiệm kép $$ r=2 $$, nghiệm tổng quát là
$$ y=C_1 x^2+C_2 x^2\ln x. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo ansatz $$ x^r $$ và phân loại ba trường hợp: nghiệm phân biệt, kép, phức.

**Bậc sau đại học.** Nhấn mạnh đối xứng co giãn, phép đổi biến $$ x=e^t $$ và liên hệ với nhóm tự đồng dạng.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: phương trình Euler và các trường hợp nghiệm đặc biệt.
- Zill, Chương 6: luyện tập nhiều ví dụ về nghiệm lũy thừa và logarit.
