---
layout: post
title: "Giới Thiệu Biến Đổi Fourier"
chapter: '08'
order: 8
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: optional
---
![21 02 25 08 08 Fourier Transform Introduction]({{ site.imgurl }}/chapter_img/chapter08/08_fourier_transform_introduction.svg)

## Mục tiêu

Bài học này giới thiệu biến đổi Fourier như bước mở rộng tự nhiên của chuỗi Fourier từ phổ rời rạc sang phổ liên tục. Sau bài học, sinh viên cần nắm trực giác khi chu kỳ tiến ra vô hạn, hiểu định nghĩa biến đổi Fourier và biến đổi ngược ở mức cơ bản, biết các tính chất tuyến tính, đạo hàm, tích chập và bảo toàn năng lượng, đồng thời nhận ra vì sao biến đổi Fourier là công cụ trung tâm để giải PDE trên toàn không gian.

## Kiến thức nền

Sinh viên cần nắm chuỗi Fourier phức, trực giác về phổ tần số và các kỹ năng tích phân cơ bản. Vì đây là bài giới thiệu, trọng tâm là xây dựng hình ảnh đúng về phổ liên tục chứ chưa đi sâu vào toàn bộ các điều kiện giải tích chặt chẽ.

## Dẫn nhập

Chuỗi Fourier phù hợp với các tín hiệu tuần hoàn, khi tập hợp tần số tạo thành một dãy rời rạc. Tuy nhiên, nhiều hiện tượng vật lý và kỹ thuật không tuần hoàn trên một chu kỳ cố định. Khi miền xét mở rộng ra toàn trục thực, phổ tần số không còn rời rạc nữa mà trở thành liên tục. Biến đổi Fourier là công cụ tự nhiên cho tình huống này.

Bài học này đóng vai trò chuẩn bị quan trọng cho các chương PDE tiếp theo. Trên miền vô hạn, thay vì phân rã nghiệm theo tập mode đếm được như ở chuỗi Fourier, ta phân rã theo một dải tần số liên tục và xử lý riêng từng tần số.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu chuỗi Fourier tương tự việc phân tích một bản nhạc thành các nốt ở những cao độ rời rạc, thì biến đổi Fourier giống như việc phân tích một âm thanh bất kỳ thành một quang phổ tần số liên tục. Thay vì các bậc tần số cách đều nhau, ta thu được một dải tần biến thiên liên tục.

### Cách nhìn hình ảnh

Một xung rất hẹp trong miền không gian thường có phổ trải rộng trong miền tần số. Ngược lại, một hàm dao động đều và trải rộng trong không gian lại có phổ hẹp hơn. Hình ảnh này minh họa trực quan mối quan hệ nghịch giữa độ tập trung trong miền không gian và độ rộng trong miền tần số.

### Cách nhìn hình thức

Biến đổi Fourier của $$ f $$ được định nghĩa bởi

$$
\hat f(\omega)=\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx,
$$

và công thức biến đổi ngược là

$$
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega x}\,d\omega.
$$

Ta có thể hiểu $$ \hat f(\omega) $$ là mật độ đóng góp của tần số $$ \omega $$ trong tín hiệu.

## Những ngộ nhận thường gặp

- "Biến đổi Fourier là công cụ hoàn toàn tách biệt với chuỗi Fourier." Sai; đây là giới hạn liên tục của cùng một ý tưởng phân rã theo tần số.
- "Phổ liên tục nghĩa là không còn khái niệm mode." Không đúng; các mode vẫn có dạng $$ e^{i\omega x} $$, chỉ khác là tần số $$ \omega $$ biến thiên liên tục.
- "Biến đổi Fourier chỉ dành cho kỹ thuật tín hiệu." Sai; công cụ này giữ vai trò trung tâm trong PDE, lý thuyết xác suất, quang học, cơ học lượng tử và nhiều ngành khoa học khác.
- "Hàm càng tập trung trong không gian thì càng tập trung trong miền tần số." Thực tế thường ngược lại.

## Tiến trình học tập đề xuất

### Bước 1: Xuất phát từ chuỗi Fourier phức

Nhắc lại phổ rời rạc và hệ mode $$ e^{inx} $$.

### Bước 2: Hình dung quá trình chu kỳ tiến ra vô hạn

Đây là trực giác cốt lõi giải thích bước chuyển từ tổng rời rạc sang tích phân.

### Bước 3: Nắm các tính chất cơ bản

Tính tuyến tính, quy tắc đạo hàm và định lý tích chập là ba tính chất cần ghi nhớ trước tiên.

### Bước 4: Liên hệ với PDE trên $$ \mathbb{R} $$

Đây là động lực chính của biến đổi Fourier trong học phần này.

### Các điểm kiểm tra

- Sinh viên có giải thích được bằng lời vì sao phổ chuyển từ rời rạc sang liên tục hay không.
- Sinh viên có hiểu $$ \hat f(\omega) $$ đo mức đóng góp của tần số $$ \omega $$ trong tín hiệu hay không.
- Sinh viên có thấy rõ lợi thế của việc biến đạo hàm thành phép nhân hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm cửa sổ

Xét $$ f(x)=\mathbf{1}_{\lvert x\rvert<a}(x) $$. Khi đó

$$
\hat f(\omega)=\int_{-a}^{a}e^{-i\omega x}\,dx
=\frac{2\sin(a\omega)}{\omega}.
$$

Ví dụ này cho thấy một xung hình chữ nhật cục bộ trong miền không gian biến đổi thành hàm dạng sinc trải rộng trong miền tần số.

### Ví dụ 2: Hàm Gaussian

Một ví dụ kinh điển là $$ f(x)=e^{-x^2} $$, có biến đổi Fourier vẫn là một hàm Gaussian khác. Kết quả này cho thấy có những lớp hàm giữ nguyên dạng hình học qua phép biến đổi Fourier.

### Ví dụ 3: Đạo hàm trở thành phép nhân

Nhờ tính chất

$$ \widehat{f'}(\omega)=i\omega \hat f(\omega), $$

một phương trình đạo hàm riêng như phương trình nhiệt $$ u_t=\alpha^2u_{xx} $$ trên toàn trục thực sẽ chuyển thành một phương trình vi phân thường theo biến $$ t $$ cho từng tần số $$ \omega $$. Đây là động lực chính của việc ứng dụng biến đổi Fourier vào PDE.

### Ví dụ 4: Tích chập trở thành phép nhân

Với tích chập

$$ (f*g)(x)=\int_{-\infty}^{\infty}f(x-y)g(y)\,dy, $$

ta có

$$ \widehat{f*g}=\hat f\,\hat g. $$

Tính chất này giữ vai trò nền tảng trong lọc tín hiệu và trong việc biểu diễn nghiệm PDE dưới dạng tích chập với hạt nhân cơ bản.

## Câu hỏi khái niệm

1. Vì sao biến đổi Fourier được xem là giới hạn liên tục của chuỗi Fourier?
2. Tại sao phép lấy đạo hàm trong miền thực lại trở thành phép nhân trong miền tần số?
3. Vì sao một hàm càng cục bộ trong không gian thì phổ tần số của nó thường càng trải rộng?

## Bài toán ứng dụng

1. Trong xử lý ảnh và âm thanh, vì sao người ta thường chuyển tín hiệu sang miền tần số trước khi lọc nhiễu?
2. Trong phương trình nhiệt trên toàn trục thực, biến đổi Fourier giúp chuyển PDE thành họ ODE độc lập như thế nào?
3. Trong quang học và cơ học lượng tử, vì sao mối quan hệ đối ngẫu giữa vị trí và tần số (hoặc động lượng) lại mang ý nghĩa nền tảng?

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Nếu chu kỳ của chuỗi Fourier tăng dần ra vô hạn, khoảng cách giữa các tần số rời rạc sẽ thay đổi như thế nào?"
- Sử dụng ví dụ xung chữ nhật để minh họa ngay sự đối ngẫu giữa miền không gian và miền tần số.
- Đặt câu hỏi cho cả lớp: "Phép toán nào trong miền không gian trở nên đơn giản hơn rõ rệt sau khi áp dụng biến đổi Fourier?"
- Khuyến khích sinh viên tự diễn đạt lại quá trình chuyển từ tổng sang tích phân bằng lời của mình.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên tập trung vào trực giác phổ liên tục và hai tính chất cốt lõi: đạo hàm trở thành phép nhân, tích chập trở thành tích. Không cần đi quá sâu vào các điều kiện tồn tại kỹ thuật ở bước tiếp cận đầu tiên.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tìm hiểu thêm định lý Plancherel (dạng Parseval của biến đổi Fourier), tính bất biến của hàm Gaussian hoặc mối liên hệ với nguyên lý bất định để chuẩn bị cho các chương PDE và giải tích hàm sau này.

## Tóm tắt dễ nhớ

Biến đổi Fourier là phiên bản phổ liên tục của chuỗi Fourier. Nó chuyển hàm trên toàn trục thực sang phân bố theo tần số, biến phép đạo hàm thành phép nhân đại số và là công cụ chủ lực để giải PDE trên miền vô hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiễu xạ và xử lý ảnh
- Bài toán: Các tín hiệu không tuần hoàn hoặc xác định trên miền vô hạn đòi hỏi biểu diễn phổ liên tục thay vì phổ rời rạc.
- Mô hình:
$$
\hat{f}(\xi)=\int_{-\infty}^{\infty}f(x)e^{-i\xi x}\,dx.
$$
- Giả thiết và giới hạn: Cần thỏa mãn điều kiện khả tích hoặc được hiểu theo nghĩa hàm suy rộng (phân phối).
- Diễn giải: Biến đổi Fourier thay thế phổ rời rạc bằng phổ tần số liên tục.

#### Phương trình nhiệt trên miền vô hạn
- Bài toán: Chuỗi Fourier không còn áp dụng trực tiếp khi miền không gian là toàn trục thực.
- Mô hình: Dùng biến đổi Fourier để chuyển đạo hàm theo không gian thành nhân tử đại số trong miền tần số.
- Giả thiết và giới hạn: Bài toán xét trên miền vô hạn với dữ liệu đầu vào đủ tốt.
- Diễn giải: Biến đổi Fourier là phiên bản liên tục hóa của chuỗi Fourier.

### 2. Trực giác bổ sung và các kết nối

Biến đổi Fourier xuất hiện tự nhiên khi chu kỳ tiến ra vô hạn và phổ rời rạc trở nên liên tục. Thay vì coi đây là một công thức hoàn toàn mới, nên hiểu nó như giới hạn trực tiếp của chuỗi Fourier phức.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 2000)
f = np.exp(-x**2)

dx = x[1] - x[0]
freq = np.fft.fftshift(np.fft.fftfreq(x.size, d=dx)) * 2 * np.pi
F = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f))) * dx

plt.plot(freq, np.abs(F))
plt.xlabel("xi")
plt.ylabel("|F(xi)|")
plt.title("Pho lien tuc xap xi cua Gaussian")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Fourier transform Gaussian visualization
- search: from Fourier series to Fourier transform
- search: continuous frequency spectrum animation

### 5. Bài toán mẫu có bối cảnh thực

Với hàm số
$$ f(x)=e^{-x^2}, $$
theo quy ước chuẩn hóa ở trên, biến đổi Fourier của nó là
$$ \hat{f}(\xi)=\sqrt{\pi}\,e^{-\xi^2/4}. $$
Vì giữ nguyên dạng hàm qua biến đổi Fourier, hàm Gaussian xuất hiện phổ biến trong các bài toán khuếch tán, lý thuyết xác suất và quang học.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu biến đổi Fourier như biểu diễn phổ liên tục và nắm một số ví dụ cơ bản như hàm Gaussian.

**Bậc sau đại học.** Nghiên cứu không gian Schwartz, định lý Plancherel, lý thuyết phân phối và vai trò của biến đổi Fourier trong PDE trên miền vô hạn.

## Video tham khảo

- Xem trước: [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, tiếng Anh. Giới thiệu trực quan ý tưởng và hình ảnh của biến đổi Fourier.
- [Solving the Heat Equation with the Fourier Transform](https://www.youtube.com/watch?v=7haZCrQDHpA) — Steve Brunton, tiếng Anh. Minh họa cách dùng biến đổi Fourier để giải phương trình nhiệt trên toàn trục thực.
- [The more general uncertainty principle, regarding Fourier transforms](https://www.youtube.com/watch?v=MBnnXbOM5S4) — 3Blue1Brown, tiếng Anh. Giải thích nguyên lý bất định như một hệ quả trực tiếp của biến đổi Fourier.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
