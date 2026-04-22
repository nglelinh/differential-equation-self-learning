---
layout: post
title: "Suy Ra Phương Trình Sóng"
chapter: '10'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter10
lesson_type: required
---
![21 03 11 10 01 Derivation Wave Equation]({{ site.imgurl }}/chapter_img/chapter10/01_derivation_wave_equation.svg)

## Mục tiêu

Bài học này giúp sinh viên hiểu phương trình sóng như hệ quả tự nhiên của định luật II Newton, lực căng và xấp xỉ góc nhỏ, chứ không phải như một PDE được phát biểu sẵn. Sau bài học, sinh viên cần hiểu vì sao phương trình $$ u_{tt}=c^2u_{xx} $$ xuất hiện cho dây rung, biết ý nghĩa vật lý của hằng số $$ c $$, và nhận ra điểm khác biệt bản chất giữa sóng với khuếch tán: sóng truyền nhiễu loạn với tốc độ hữu hạn thay vì làm mượt nó ngay lập tức.

## Kiến thức nền

Sinh viên nên nắm đạo hàm riêng, định luật II Newton, lực căng, mật độ tuyến tính và trực giác về dao động cơ học. Việc phân biệt gia tốc với vận tốc cũng rất quan trọng, vì phương trình sóng là bậc hai theo thời gian.

## Dẫn nhập

Trong chương trước, phương trình nhiệt xuất hiện từ bảo toàn năng lượng cộng với dòng khuếch tán. Bây giờ ta chuyển sang một cơ chế hoàn toàn khác: lan truyền do quán tính và lực phục hồi. Nếu kéo một sợi dây đang căng ra khỏi vị trí cân bằng rồi thả, nó không làm mượt như nhiệt. Nó rung, truyền xung và bảo toàn năng lượng theo một cách rất khác.

Đây là bước chuyển rất quan trọng về mặt tư duy. Ở phương trình nhiệt, nhiễu loạn bị làm phẳng. Ở phương trình sóng, nhiễu loạn được truyền đi. Vì thế bài học đầu chương phải làm rõ mô hình cơ học phía sau PDE, để sinh viên không chỉ thấy công thức mà còn thấy nguyên nhân vật lý của từng số hạng.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng một sợi dây guitar. Khi ta gảy dây, một đoạn nhỏ của dây bị kéo lên. Đoạn dây đó có quán tính nên không thể trở về ngay, nhưng đồng thời lực căng kéo nó xuống. Sự giằng co giữa quán tính và lực phục hồi làm xung lan dọc theo dây. Đó là bản chất của phương trình sóng.

### Cách nhìn hình ảnh

Nếu đồ thị $$ u(x,t) $$ là hình dạng của dây tại thời điểm $$ t $$, thì nơi dây cong nhiều nhất là nơi lực kéo thẳng lại mạnh nhất. Vì vậy độ cong không gian $$ u_{xx} $$ đóng vai trò là nguồn gây gia tốc. Càng cong, dây càng bị kéo về vị trí cân bằng mạnh hơn. Hình ảnh này giúp sinh viên hiểu vì sao đạo hàm bậc hai theo không gian lại điều khiển đạo hàm bậc hai theo thời gian.

### Cách nhìn hình thức

Xét một đoạn dây nhỏ từ $$ x $$ đến $$ x+\Delta x $$. Gọi $$ \rho $$ là khối lượng riêng tuyến tính và $$ T $$ là lực căng gần như không đổi. Với xấp xỉ góc nhỏ, thành phần thẳng đứng của lực căng tại hai đầu đoạn dây xấp xỉ là $$ T u_x(x+\Delta x,t)-T u_x(x,t) $$. Khối lượng của đoạn là $$ \rho\Delta x $$. Áp dụng định luật II Newton:

$$
\rho\Delta x\,u_{tt}(x,t)=T\bigl(u_x(x+\Delta x,t)-u_x(x,t)\bigr).
$$

Chia cho $$ \Delta x $$ và cho $$ \Delta x\to 0 $$, ta được $$ \rho u_{tt}=T u_{xx} $$. Đặt

$$ c^2=\frac{T}{\rho}, $$

thu được phương trình sóng một chiều:

$$ u_{tt}=c^2u_{xx}. $$

## Những ngộ nhận thường gặp

- "Phương trình sóng chỉ là mô hình cho âm thanh." Sai. Nó mô tả nhiều hiện tượng lan truyền cơ học và trường.
- "Hằng số

$$ c $$

chỉ là ký hiệu tùy ý." Không đúng. Nó là tốc độ truyền sóng do môi trường quyết định.
- "Số hạng

$$ u_{xx} $$

có nghĩa giống hệt trong phương trình nhiệt." Không hẳn. Ở phương trình nhiệt nó quyết định tốc độ làm mượt, còn ở phương trình sóng nó gây gia tốc phục hồi.
- "Nếu dây nặng hơn thì sóng truyền nhanh hơn vì có nhiều quán tính." Sai; khối lượng riêng lớn hơn làm

$$ c $$

giảm.

## Tiến trình học tập đề xuất

### Bước 1: Xác định đại lượng và các giả thiết

Độ lệch nhỏ, lực căng gần như không đổi, dao động vuông góc.

### Bước 2: Cân bằng lực trên một đoạn nhỏ

Đây là trung tâm của mô hình.

### Bước 3: Dùng định luật Newton

Gia tốc đi với $$ u_{tt} $$, lực phục hồi đi với chênh lệch độ dốc.

### Bước 4: Cho đoạn co lại

Từ mô hình rời rạc cục bộ đi tới PDE liên tục.

### Bước 5: Diễn giải hằng số

$$ c $$

Sinh viên nên hiểu rõ mối liên hệ giữa lực căng, mật độ và tốc độ sóng.

### Các checkpoint

- Sinh viên có giải thích được vì sao đạo hàm thời gian là bậc hai hay không.
- Sinh viên có hiểu vai trò của xấp xỉ góc nhỏ hay không.
- Sinh viên có diễn giải được vì sao

$$ c=\sqrt{T/\rho} $$

hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ảnh hưởng của lực căng

Nếu $$ T $$ tăng trong khi $$ \rho $$ giữ nguyên, thì $$ c=\sqrt{T/\rho} $$ tăng. Điều này giải thích vì sao dây đàn căng hơn thường truyền nhiễu loạn nhanh hơn và cho cao độ lớn hơn.

### Ví dụ 2: Ảnh hưởng của mật độ tuyến tính

Nếu $$ \rho $$ tăng mà $$ T $$ không đổi, thì $$ c $$ giảm. Ví dụ này nên được dùng để giải thích vì sao dây dày và nặng hơn thường cho dao động chậm hơn.

### Ví dụ 3: So sánh với phương trình nhiệt

Phương trình nhiệt có dạng $$ u_t=\alpha^2u_{xx} $$, còn phương trình sóng có dạng $$ u_{tt}=c^2u_{xx} $$. Chỉ khác một đạo hàm theo thời gian, nhưng bản chất thay đổi hoàn toàn: một bên làm mượt, một bên truyền dao động. Đây là ví dụ khái niệm rất quan trọng để mở đầu chương.

### Ví dụ 4: Dây đàn bị gảy

Nếu hình dạng ban đầu là một tam giác nhọn, phương trình sóng sẽ khiến hình dạng đó tách thành các thành phần lan truyền chứ không bị san phẳng tức thì. Đây là ví dụ dùng để báo trước nghiệm d'Alembert ở bài sau.

## Câu hỏi khái niệm

1. Vì sao độ cong của dây lại tạo ra gia tốc phục hồi?
2. Hằng số $$ c $$ phản ánh điều gì về môi trường truyền sóng?
3. Vì sao phương trình sóng có bản chất khác hẳn phương trình nhiệt dù đều chứa

$$ u_{xx}? $$

## Bài toán ứng dụng

1. Một dây đàn được thay bằng dây dày hơn nhưng giữ cùng lực căng. Hãy giải thích định tính điều gì xảy ra với tốc độ truyền sóng.
2. Một cáp truyền dao động được kéo căng thêm. Hãy giải thích vì sao tín hiệu cơ học lan truyền nhanh hơn.
3. Trong kỹ thuật kết cấu, vì sao giả thiết dao động nhỏ lại quan trọng khi suy ra phương trình sóng tuyến tính?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu kéo một đoạn nhỏ của dây lên rồi thả, điều gì thật sự làm nó quay về?"
- Cho sinh viên tự dự đoán xem tăng lực căng hay tăng mật độ sẽ làm sóng chạy nhanh hơn.
- Vẽ một đoạn dây cong và hỏi: "Ở chỗ nào lực phục hồi mạnh nhất?"
- Khuyến khích sinh viên so sánh bằng lời giữa mô hình nhiệt và mô hình sóng trước khi viết công thức.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám chặt vào mô hình đoạn dây nhỏ và định luật Newton trong một chiều. Khi đã hiểu đoạn rất nhỏ, việc chấp nhận PDE sẽ tự nhiên hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể mời sinh viên khá giỏi thảo luận điều gì thay đổi nếu không dùng xấp xỉ góc nhỏ, hoặc suy ra phương trình sóng cho thanh đàn hồi dao động dọc để so sánh.

## Tóm tắt dễ nhớ

Phương trình sóng xuất hiện từ cân bằng giữa quán tính và lực phục hồi. Độ cong không gian tạo ra gia tốc, còn tốc độ truyền $$ c $$ được quyết định bởi lực căng và mật độ môi trường. Sóng truyền nhiễu loạn với tốc độ hữu hạn thay vì làm mượt ngay như nhiệt.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* - phát triển chặt chẽ phương trình sóng, năng lượng, và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* - trực giác vật lý tốt cho sóng, cộng hưởng, và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dây đàn rung
- Bài toán: Khi gảy dây đàn guitar, nhiễu loạn lan dọc theo dây với tốc độ hữu hạn.
- Mô hình:
$$ u_{tt}=c^2u_{xx}, \qquad c=\sqrt{\frac{T}{\rho}}. $$
- Giả thiết và giới hạn: Dây mảnh, lực căng không đổi, góc lệch nhỏ, bỏ qua ma sát.
- Diễn giải: Độ cong của dây tạo lực phục hồi, còn quán tính làm cho chuyển động có dạng lan truyền thay vì bị làm phẳng.

#### Sóng đàn hồi dọc theo thanh
- Bài toán: Một xung cơ học truyền trong thanh kim loại hoặc mô hình xấp xỉ của địa chấn một chiều.
- Mô hình: Cùng dạng phương trình sóng với $$ u(x,t) $$ là chuyển vị dọc.
- Giả thiết và giới hạn: Vật liệu tuyến tính, đồng nhất, biến dạng nhỏ.
- Diễn giải: Cơ chế toán học của dây rung xuất hiện lại trong nhiều môi trường đàn hồi.

### 2. Trực giác bổ sung và các kết nối

Phương trình sóng khác phương trình nhiệt ở chỗ nó bảo toàn tính dao động. Nếu đạo hàm bậc hai theo thời gian đo quán tính, thì đạo hàm bậc hai theo không gian đo độ cong và do đó đo lực phục hồi. Một ngộ nhận phổ biến là sóng và khuếch tán chỉ khác nhau ở ký hiệu; thật ra chúng thuộc hai lớp động lực rất khác nhau.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u = np.exp(-120 * (x - 0.5) ** 2)
uxx = np.gradient(np.gradient(u, x), x)

plt.plot(x, u, label="Do lech ban dau")
plt.plot(x, -uxx / np.max(np.abs(uxx)), label="Gia toc ty le voi -u_xx")
plt.xlabel("x")
plt.title("Do cong tao gia toc trong phuong trinh song")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: vibrating string wave equation animation
- search: derivation wave equation small angle approximation
- search: elastic wave equation string force balance

### 5. Bài toán mẫu có bối cảnh thực

Xét một phần tử dây dài $$ \Delta x $$. Hiệu hai thành phần thẳng đứng của lực căng cho ta xấp xỉ
$$
T u_x(x+\Delta x,t)-T u_x(x,t)\approx T u_{xx}\Delta x.
$$
Theo định luật II Newton,
$$ \rho \Delta x\, u_{tt}=T u_{xx}\Delta x, $$
nên
$$ u_{tt}=c^2u_{xx}, \qquad c^2=\frac{T}{\rho}. $$
Thông điệp vật lý là: dây càng căng thì sóng chạy càng nhanh, dây càng nặng thì sóng chạy càng chậm.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm được vì sao lực phục hồi cộng quán tính dẫn đến phương trình sóng.

**Bậc sau đại học.** Liên hệ với phương trình đàn hồi nhiều chiều, tính hyperbolic và miền ảnh hưởng hữu hạn.
