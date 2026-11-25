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

Để suy ra phương trình sóng 1D $u_{tt} = c^2 u_{xx}$, ta chẳng cần công cụ cao siêu nào ngoài **Định luật II Newton ($F = ma$)** áp dụng cho một đoạn dây đàn vô cùng ngắn $[x, x + \Delta x]$ dưới giả thiết dao động biên độ nhỏ ($\vert u_x \vert \ll 1$).

## Kiến thức cần nhớ: Bốn bước suy diễn Phương trình Sóng từ $F = ma$

1. **Giả thiết dây đàn lý tưởng**:
   Dây mềm hoàn toàn (không chống uốn), khối lượng riêng dài đều $\rho$, dao động thẳng đứng nhỏ ($\vert u_x \vert \ll 1 \implies \cos\theta \approx 1,\; \sin\theta \approx \tan\theta = u_x$), nên lực căng ngang $T$ không đổi dọc dây.
2. **Hợp lực thẳng đứng trên đoạn $[x, x + \Delta x]$**:
   $$F_y = T\sin\theta(x + \Delta x) - T\sin\theta(x) \approx T\big[u_x(x + \Delta x, t) - u_x(x, t)\big].$$
3. **Áp dụng $F = ma$ và lấy giới hạn $\Delta x \to 0$**:
   $$\rho \Delta x\, u_{tt} = T\big[u_x(x + \Delta x, t) - u_x(x, t)\big] \implies u_{tt} = \frac{T}{\rho} u_{xx} = c^2 u_{xx}, \qquad c = \sqrt{\frac{T}{\rho}}.$$
4. **Phân loại PDE Hyperbolic vs. Parabolic**:
   Khác với phương trình nhiệt ($u_t = \alpha u_{xx}$ — Parabolic, bất đối xứng thời gian), phương trình sóng ($u_{tt} = c^2 u_{xx}$ — Hyperbolic) **đối xứng hoàn toàn khi đảo ngược thời gian $t \to -t$**, bảo toàn năng lượng và truyền tín hiệu với **tốc độ hữu hạn đúng bằng $c$**!

## Mục tiêu

Bài học này giúp sinh viên hiểu phương trình sóng là hệ quả trực tiếp của định luật II Newton, lực căng dây và xấp xỉ góc nhỏ, thay vì một công thức cho sẵn. Sau bài học, sinh viên cần giải thích được vì sao phương trình $$ u_{tt}=c^2u_{xx} $$ xuất hiện cho dây đàn dao động, hiểu ý nghĩa vật lý của hằng số $$ c $$ và phân biệt rõ bản chất giữa sóng và khuếch tán: sóng lan truyền nhiễu loạn với tốc độ hữu hạn thay vì làm mượt nó ngay lập tức.

## Kiến thức nền

Sinh viên cần nắm đạo hàm riêng, định luật II Newton, khái niệm lực căng, khối lượng riêng tuyến tính và trực giác về dao động cơ học. Việc phân biệt rõ gia tốc và vận tốc rất quan trọng vì phương trình sóng có bậc hai theo thời gian.

## Dẫn nhập

Ở chương trước, phương trình nhiệt xuất phát từ định luật bảo toàn năng lượng kết hợp với dòng khuếch tán. Sang chương này, ta xét một cơ chế vật lý hoàn toàn khác: sự lan truyền do tương tác giữa quán tính và lực phục hồi. Khi kéo một sợi dây căng lệch khỏi vị trí cân bằng rồi thả ra, dây không phẳng dần ngay như nhiệt độ mà dao động, truyền xung dọc theo dây và bảo toàn cơ năng.

Đây là điểm phân biệt cơ bản về mặt mô hình: trong phương trình nhiệt, nhiễu loạn bị san phẳng; trong phương trình sóng, nhiễu loạn được truyền đi. Vì vậy, bài mở đầu chương cần làm rõ cơ sở cơ học phía sau từng số hạng của phương trình.

### Giải thích: Tính tay vận tốc sóng và tần số cơ bản của một dây đàn guitar thật

Một dây đàn guitar dài $L = 0{,}65\text{ m}$, khối lượng riêng dài $\rho = 0{,}001\text{ kg/m}$ ($1\text{ g/m}$), được lên dây với lực căng $T = 72{,}9\text{ N}$:
1. **Tốc độ truyền sóng dọc dây**:
   $$c = \sqrt{\frac{T}{\rho}} = \sqrt{\frac{72{,}9}{0{,}001}} = \sqrt{72.900} = \mathbf{270\text{ m/s}}.$$
2. **Tần số âm cơ bản $f_1 = \frac{c}{2L}$**:
   $$f_1 = \frac{270}{2 \times 0{,}65} \approx \mathbf{207{,}7\text{ Hz}} \quad (\text{nốt G\#3}).$$
3. **Kiểm tra trực giác lên dây**: Muốn nâng cao độ lên đúng 1 quãng tám (tần số tăng $2\times$), ta phải tăng lực căng $T$ lên gấp **$4\times$** (vì $c \propto \sqrt{T}$)!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một sợi dây đàn guitar. Khi gảy dây, một đoạn nhỏ bị kéo lệch khỏi vị trí cân bằng. Nhờ quán tính, đoạn dây không dừng ngay tại vị trí cân bằng mà vượt qua nó, trong khi lực căng luôn kéo dây trở về. Sự phối hợp liên tục giữa quán tính và lực phục hồi làm cho nhiễu loạn lan dọc theo dây — đó là bản chất của quá trình truyền sóng.

### Cách nhìn hình ảnh

Nếu đồ thị $$ u(x,t) $$ biểu diễn hình dạng sợi dây tại thời điểm $$ t $$, thì nơi dây uốn cong mạnh nhất cũng là nơi lực căng kéo thẳng lại mạnh nhất. Do đó, độ cong không gian $$ u_{xx} $$ đóng vai trò tạo ra gia tốc: dây càng cong, lực kéo về vị trí cân bằng càng lớn. Hình ảnh này giải thích trực tiếp vì sao đạo hàm bậc hai theo không gian điều khiển đạo hàm bậc hai theo thời gian.

### Cách nhìn hình thức

Xét một đoạn dây nhỏ từ $$ x $$ đến $$ x+\Delta x $$, có khối lượng riêng tuyến tính $$ \rho $$ và lực căng $$ T $$ gần như không đổi. Dưới giả thiết góc lệch nhỏ, hợp lực theo phương thẳng đứng do lực căng tác dụng lên hai đầu đoạn dây xấp xỉ bằng $$ T u_x(x+\Delta x,t)-T u_x(x,t) $$. Với khối lượng đoạn dây là $$ \rho\Delta x $$, định luật II Newton cho

$$
\rho\Delta x\,u_{tt}(x,t)=T\bigl(u_x(x+\Delta x,t)-u_x(x,t)\bigr).
$$

Chia hai vế cho $$ \Delta x $$ và cho $$ \Delta x\to 0 $$, ta thu được $$ \rho u_{tt}=T u_{xx} $$. Đặt

$$ c^2=\frac{T}{\rho}, $$

ta nhận được phương trình sóng một chiều:

$$ u_{tt}=c^2u_{xx}. $$

## Những ngộ nhận thường gặp

- "Phương trình sóng chỉ mô tả sóng âm." Sai; nó còn mô tả nhiều hiện tượng lan truyền cơ học và trường điện từ.
- "Hằng số $$ c $$ chỉ là một tham số hình thức." Không đúng; $$ c $$ chính là tốc độ truyền sóng do tính chất môi trường quyết định.
- "Số hạng $$ u_{xx} $$ mang cùng ý nghĩa như trong phương trình nhiệt." Không hoàn toàn; trong phương trình nhiệt nó xác định tốc độ làm mượt, còn trong phương trình sóng nó tạo ra gia tốc phục hồi.
- "Dây càng nặng thì sóng truyền càng nhanh nhờ quán tính lớn hơn." Sai; khối lượng riêng $$ \rho $$ tăng làm tốc độ sóng $$ c=\sqrt{T/\rho} $$ giảm xuống.

## Tiến trình học tập đề xuất

### Bước 1: Xác định đại lượng và các giả thiết mô hình

Nêu rõ các giả thiết: độ lệch nhỏ, lực căng gần như không đổi, dao động theo phương vuông góc với trục dây.

### Bước 2: Phân tích cân bằng lực trên một đoạn dây nhỏ

Đây là bước trọng tâm nối vật lý với toán học.

### Bước 3: Áp dụng định luật II Newton

Liên kết gia tốc $$ u_{tt} $$ với hiệu thành phần thẳng đứng của lực căng ở hai đầu đoạn dây.

### Bước 4: Lấy giới hạn khi $$ \Delta x\to 0 $$

Chuyển từ phương trình trên phần tử rời rạc sang phương trình đạo hàm riêng liên tục.

### Bước 5: Diễn giải ý nghĩa của hằng số $$ c $$

Phân tích sự phụ thuộc của tốc độ sóng vào lực căng và mật độ tuyến tính.

### Các điểm kiểm tra

- Sinh viên có giải thích được vì sao đạo hàm theo thời gian có bậc hai hay không.
- Sinh viên có nêu được vai trò của giả thiết góc lệch nhỏ trong phép xấp xỉ hay không.
- Sinh viên có diễn giải được ý nghĩa vật lý của công thức $$ c=\sqrt{T/\rho} $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Ảnh hưởng của lực căng

Nếu lực căng $$ T $$ tăng trong khi mật độ $$ \rho $$ giữ nguyên, tốc độ truyền sóng $$ c=\sqrt{T/\rho} $$ tăng lên. Điều này giải thích vì sao căng dây đàn chặt hơn làm sóng truyền nhanh hơn và âm phát ra có cao độ cao hơn.

### Ví dụ 2: Ảnh hưởng của mật độ tuyến tính

Nếu $$ \rho $$ tăng trong khi $$ T $$ không đổi, tốc độ $$ c $$ giảm đi. Do đó, các dây đàn dày và nặng hơn thường dao động chậm hơn và phát ra âm trầm hơn.

### Ví dụ 3: Đối chiếu với phương trình nhiệt

Phương trình nhiệt có dạng $$ u_t=\alpha^2u_{xx} $$, còn phương trình sóng có dạng $$ u_{tt}=c^2u_{xx} $$. Chỉ khác nhau ở bậc đạo hàm theo thời gian nhưng hành vi nghiệm hoàn toàn khác biệt: một bên làm mượt dữ liệu theo thời gian, một bên truyền đi các dao động.

### Ví dụ 4: Dây đàn bị gảy tạo góc nhọn

Nếu hình dạng ban đầu của dây là một đường gấp khúc hình tam giác, phương trình sóng sẽ tách hình dạng đó thành các thành phần lan truyền dọc theo dây chứ không làm phẳng góc nhọn ngay lập tức. Ví dụ này dẫn trực tiếp sang nghiệm d'Alembert ở bài tiếp theo.

## Câu hỏi khái niệm

1. Vì sao độ cong của sợi dây lại sinh ra gia tốc phục hồi?
2. Hằng số $$ c $$ phản ánh những đặc tính vật lý nào của môi trường truyền sóng?
3. Vì sao phương trình sóng có bản chất hoàn toàn khác phương trình nhiệt mặc dù cả hai đều chứa $$ u_{xx} $$?

## Bài toán ứng dụng

1. Một dây đàn được thay bằng dây có mật độ lớn hơn nhưng giữ nguyên lực căng. Hãy giải thích định tính sự thay đổi của tốc độ truyền sóng.
2. Một sợi cáp truyền dao động được kéo căng thêm. Vì sao tín hiệu cơ học lan truyền dọc theo cáp nhanh hơn?
3. Trong kỹ thuật kết cấu, vì sao giả thiết dao động nhỏ là điều kiện thiết yếu để thu được phương trình sóng tuyến tính?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Khi kéo một đoạn nhỏ của sợi dây lên rồi thả tay, lực nào kéo nó quay về vị trí cân bằng?"
- Yêu cầu sinh viên dự đoán xem tăng lực căng hay tăng khối lượng riêng sẽ làm sóng truyền nhanh hơn.
- Vẽ một đoạn dây uốn cong và hỏi: "Tại vị trí nào trên dây lực phục hồi đạt cực đại?"
- Tổ chức so sánh ngắn bằng lời giữa mô hình truyền nhiệt và mô hình truyền sóng trước khi thiết lập công thức.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bám sát hình vẽ một đoạn dây nhỏ và định luật II Newton trong một chiều. Khi đã hiểu rõ lực tác dụng lên phần tử nhỏ, việc chấp nhận dạng PDE sẽ tự nhiên hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên phân tích phương trình sẽ thay đổi ra sao nếu bỏ giả thiết góc nhỏ, hoặc thiết lập phương trình sóng cho dao động dọc của một thanh đàn hồi để đối chiếu.

## Tóm tắt dễ nhớ

Phương trình sóng hình thành từ cân bằng giữa quán tính và lực phục hồi theo định luật II Newton. Độ cong không gian tạo ra gia tốc, còn tốc độ truyền sóng $$ c=\sqrt{T/\rho} $$ phụ thuộc vào lực căng và mật độ môi trường. Khác với phương trình nhiệt, sóng truyền nhiễu loạn đi với tốc độ hữu hạn.

## Video tham khảo

- Xem trước: [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Thiết lập phương trình sóng một chiều từ cân bằng lực trên một sợi dây căng.
- [Partial Differential Equations Overview](https://www.youtube.com/watch?v=pvrIagjEk4c) — Steve Brunton, tiếng Anh. Tổng quan ba PDE tuyến tính chính tắc, đặt phương trình sóng cạnh phương trình nhiệt và phương trình Laplace.
- [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, tiếng Anh. Liên hệ phương trình sóng vừa thiết lập với vật lý dao động của dây đàn guitar.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — trình bày chặt chẽ về phương trình sóng, phương pháp năng lượng và tính duy nhất.
- Haberman, *Applied Partial Differential Equations* — cung cấp trực giác vật lý rõ ràng về sóng, cộng hưởng và phản xạ.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dây đàn rung
- Bài toán: Khi gảy dây đàn guitar, nhiễu loạn lan truyền dọc theo dây với tốc độ hữu hạn.
- Mô hình:
$$ u_{tt}=c^2u_{xx}, \qquad c=\sqrt{\frac{T}{\rho}}. $$
- Giả thiết và giới hạn: Dây mảnh, lực căng không đổi, góc lệch nhỏ, bỏ qua ma sát.
- Diễn giải: Độ cong của dây tạo ra lực phục hồi, còn quán tính duy trì sự lan truyền dao động thay vì làm phẳng tức thì.

#### Sóng đàn hồi dọc theo thanh
- Bài toán: Mô tả một xung cơ học truyền dọc theo thanh kim loại hoặc mô hình địa chấn một chiều đơn giản.
- Mô hình: Sử dụng cùng dạng phương trình sóng với $$ u(x,t) $$ là chuyển vị dọc.
- Giả thiết và giới hạn: Vật liệu đàn hồi tuyến tính, đồng nhất, biến dạng nhỏ.
- Diễn giải: Cấu trúc toán học của dây rung xuất hiện tương tự trong nhiều môi trường đàn hồi khác.

### 2. Trực giác bổ sung và các kết nối

Phương trình sóng khác phương trình nhiệt ở chỗ nó bảo toàn tính dao động của hệ: đạo hàm bậc hai theo thời gian gắn với quán tính, còn đạo hàm bậc hai theo không gian đo độ cong và lực phục hồi. Sóng và khuếch tán đại diện cho hai lớp động lực học hoàn toàn khác nhau.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
u = np.exp(-120 * (x - 0.5) ** 2)
uxx = np.gradient(np.gradient(u, x), x)

plt.plot(x, u, label="Do lech ban dau")
plt.plot(x, uxx / np.max(np.abs(uxx)), label="Gia toc ty le voi u_xx")
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

Xét một phần tử dây dài $$ \Delta x $$. Hiệu hai thành phần thẳng đứng của lực căng ở hai đầu phần tử xấp xỉ bằng
$$
T u_x(x+\Delta x,t)-T u_x(x,t)\approx T u_{xx}\Delta x.
$$
Theo định luật II Newton,
$$ \rho \Delta x\, u_{tt}=T u_{xx}\Delta x, $$
suy ra
$$ u_{tt}=c^2u_{xx}, \qquad c^2=\frac{T}{\rho}. $$
Kết quả cho thấy dây càng căng thì sóng truyền càng nhanh, còn dây càng nặng thì sóng truyền càng chậm.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững cách lực phục hồi kết hợp quán tính dẫn đến phương trình sóng.

**Bậc sau đại học.** Mở rộng sang phương trình đàn hồi nhiều chiều, tính hyperbolic và khái niệm miền ảnh hưởng hữu hạn.
