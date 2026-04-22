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

Bài học này giới thiệu biến đổi Fourier như bước mở rộng tự nhiên của chuỗi Fourier từ phổ rời rạc sang phổ liên tục. Sau bài học, sinh viên cần hiểu trực giác "chu kỳ tiến ra vô hạn", biết định nghĩa biến đổi Fourier và biến đổi ngược ở mức cơ bản, thấy các tính chất tuyến tính, đạo hàm, tích chập và bảo toàn năng lượng, đồng thời hiểu vì sao biến đổi Fourier là công cụ trung tâm cho PDE trên toàn không gian.

## Kiến thức nền

Sinh viên nên nắm chuỗi Fourier phức, trực giác về phổ tần số, và các kỹ năng tích phân cơ bản. Bài này chỉ là giới thiệu, nên điều quan trọng nhất là xây dựng hình ảnh đúng về phổ liên tục chứ không phải xử lý tất cả điều kiện kỹ thuật giải tích.

## Dẫn nhập

Chuỗi Fourier rất phù hợp với tín hiệu tuần hoàn, vì khi đó tập tần số xuất hiện là rời rạc. Nhưng nhiều hiện tượng trong vật lý và kỹ thuật không tuần hoàn trên một chu kỳ cố định. Khi miền quan sát mở rộng ra toàn trục thực, phổ tần số không còn là một dãy rời rạc nữa mà trở thành liên tục. Biến đổi Fourier là ngôn ngữ tự nhiên cho tình huống đó.

Đây là bài học có ý nghĩa chiến lược cho phần PDE về sau. Trên miền vô hạn, thay vì tách nghiệm thành các mode đếm được như ở chuỗi Fourier, ta tách thành một "đám mây tần số liên tục" rồi xử lý từng tần số riêng lẻ.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu chuỗi Fourier giống như việc phân tích một bản nhạc thành các nốt ở những cao độ rời rạc, thì biến đổi Fourier giống như việc phân tích một âm thanh tự do thành cả một quang phổ liên tục các tần số. Không còn những "bậc thang tần số" cách nhau đều, mà là một dải tần liên tục.

### Cách nhìn hình ảnh

Một xung rất hẹp trong miền không gian thường có phổ rất rộng trong miền tần số. Ngược lại, một hàm dao động đều đặn và trải rộng trong không gian lại có phổ hẹp hơn. Hình ảnh này là cốt lõi để cảm nhận mối liên hệ nghịch giữa cục bộ hóa trong không gian và trải rộng trong tần số.

### Cách nhìn hình thức

Biến đổi Fourier của $$ f $$ được định nghĩa bởi

$$
\hat f(\omega)=\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx,
$$

và công thức biến đổi ngược là

$$
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega x}\,d\omega.
$$

Ta có thể xem $$ \hat f(\omega) $$ là mức hiện diện của tần số $$ \omega $$ trong tín hiệu.

## Những ngộ nhận thường gặp

- "Biến đổi Fourier là công cụ hoàn toàn khác chuỗi Fourier." Sai. Nó là giới hạn liên tục của cùng một ý tưởng phân rã tần số.
- "Phổ liên tục nghĩa là mất đi ý nghĩa mode." Không đúng; các mode vẫn là

$$ e^{i\omega x}, $$

chỉ có điều bây giờ $$ \omega $$ chạy liên tục.
- "Biến đổi Fourier chỉ dành cho kỹ sư tín hiệu." Sai; nó là công cụ rất trung tâm trong PDE, xác suất, quang học, cơ học lượng tử và nhiều lĩnh vực khác.
- "Càng tập trung trong không gian thì càng tập trung trong tần số." Thường là ngược lại.

## Tiến trình học tập đề xuất

### Bước 1: Từ chuỗi Fourier phức

Nhắc lại phổ rời rạc và mode

$$ e^{inx}. $$

### Bước 2: Hình dung chu kỳ đi ra vô hạn

Đây là trực giác bản chất nhất để chuyển từ tổng sang tích phân.

### Bước 3: Học các tính chất cơ bản

Tuyến tính, đạo hàm, tích chập là ba tính chất nên nhớ đầu tiên.

### Bước 4: Liên hệ với PDE trên

$$ \mathbb{R} $$

Đây là động lực lớn nhất của công cụ này trong học phần.

### Các checkpoint

- Sinh viên có giải thích được bằng lời vì sao phổ chuyển từ rời rạc sang liên tục hay không.
- Sinh viên có biết biến đổi Fourier đo "bao nhiêu tần số"

$$ \omega $$

trong tín hiệu hay không.
- Sinh viên có thấy lợi ích của việc đạo hàm trở thành phép nhân hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hàm cửa sổ

Xét $$ f(x)=\mathbf{1}_{\lvert x\rvert<a}(x) $$. Khi đó

$$
\hat f(\omega)=\int_{-a}^{a}e^{-i\omega x}\,dx
=\frac{2\sin(a\omega)}{\omega}.
$$

Ví dụ này rất đẹp vì một xung hình chữ nhật trong miền không gian lại cho ra một hàm dạng sinc trong miền tần số.

### Ví dụ 2: Hàm Gaussian

Một trong những ví dụ kinh điển nhất là $$ f(x)=e^{-x^2} $$, có biến đổi Fourier vẫn là một Gaussian khác. Ý nghĩa sư phạm của ví dụ này rất lớn: nó cho thấy có những hàm cực kỳ "ổn định" qua phép biến đổi Fourier.

### Ví dụ 3: Đạo hàm thành phép nhân

Nếu

$$ \widehat{f'}(\omega)=i\omega \hat f(\omega), $$

thì một PDE như $$ u_t=\alpha^2u_{xx} $$ trên toàn trục thực sẽ trở thành một ODE theo $$ t $$ cho từng tần số $$ \omega $$. Ví dụ này chính là động lực quan trọng nhất của biến đổi Fourier trong PDE.

### Ví dụ 4: Tích chập trở thành tích

Nếu

$$ (f*g)(x)=\int_{-\infty}^{\infty}f(x-y)g(y)\,dy, $$

thì

$$ \widehat{f*g}=\hat f\,\hat g. $$

Ví dụ này rất quan trọng trong lọc tín hiệu và trong cách hiểu nghiệm PDE như chập với một hạt nhân cơ bản.

## Câu hỏi khái niệm

1. Vì sao biến đổi Fourier được xem như giới hạn liên tục của chuỗi Fourier?
2. Tại sao đạo hàm trong miền thực lại trở thành phép nhân trong miền tần số?
3. Vì sao một hàm càng cục bộ trong không gian thường lại có phổ càng rộng?

## Bài toán ứng dụng

1. Trong xử lý ảnh và âm thanh, vì sao người ta thường chuyển sang miền tần số trước khi lọc nhiễu?
2. Trong phương trình nhiệt trên toàn trục thực, vì sao biến đổi Fourier giúp biến PDE thành họ ODE độc lập?
3. Trong quang học hoặc cơ học lượng tử, vì sao mối liên hệ giữa vị trí và tần số hay động lượng lại đặc biệt quan trọng?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Nếu chu kỳ của chuỗi Fourier tăng mãi, điều gì sẽ xảy ra với các tần số rời rạc?"
- Dùng ví dụ xung hình chữ nhật để cho sinh viên thấy ngay sự đối thoại giữa miền không gian và miền tần số.
- Hỏi cả lớp: "Phép toán nào trong không gian thực trở nên dễ hơn rõ rệt sau khi biến đổi Fourier?"
- Khuyến khích sinh viên kể lại câu chuyện 'từ tổng sang tích phân' bằng ngôn ngữ của mình.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ trọng tâm ở trực giác phổ liên tục và hai tính chất quan trọng nhất: đạo hàm trở thành phép nhân, tích chập trở thành tích. Không cần ép đi quá sâu vào điều kiện tồn tại kỹ thuật ở lần gặp đầu.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi tìm hiểu thêm dạng Parseval của biến đổi Fourier, vai trò của Gaussian, hoặc mối liên hệ với nguyên lý bất định như bước chuẩn bị cho các chương PDE và giải tích hàm sau.

## Tóm tắt dễ nhớ

Biến đổi Fourier là phiên bản phổ liên tục của chuỗi Fourier. Nó chuyển một hàm trên toàn trục thực thành phân bố theo tần số, biến đạo hàm thành phép nhân, và là công cụ trung tâm để giải PDE trên miền vô hạn.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Nhiễu xạ và xử lý ảnh
- Bài toán: Các cấu trúc không tuần hoàn hoặc tín hiệu trên miền vô hạn cần một công cụ liên tục thay vì phổ rời rạc.
- Mô hình:
$$
\hat{f}(\xi)=\int_{-\infty}^{\infty}f(x)e^{-i\xi x}\,dx.
$$
- Giả thiết và giới hạn: Cần điều kiện tích phân hoặc hiểu theo nghĩa phân phối.
- Diễn giải: Fourier transform thay phổ rời rạc bằng phổ liên tục các tần số.

#### Phương trình nhiệt trên miền vô hạn
- Bài toán: Chuỗi Fourier không còn phù hợp khi miền là toàn trục số.
- Mô hình: Dùng biến đổi Fourier để biến đạo hàm theo không gian thành nhân tử đại số trong miền tần số.
- Giả thiết và giới hạn: Bài toán trên miền vô hạn và dữ liệu đủ tốt.
- Diễn giải: Fourier transform là phiên bản "liên tục hóa" của chuỗi Fourier.

### 2. Trực giác bổ sung và các kết nối

Biến đổi Fourier xuất hiện khi chu kỳ tăng lên vô hạn và phổ rời rạc trở thành liên tục. Một bẫy phổ biến là xem Fourier transform như công thức hoàn toàn mới; tốt hơn là nhìn nó như giới hạn tự nhiên của chuỗi Fourier phức.

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

Nếu
$$ f(x)=e^{-x^2}, $$
thì một trong những ví dụ đẹp nhất của giải tích Fourier là
$$ \hat{f}(\xi)=\sqrt{\pi}\,e^{-\xi^2/4} $$
theo quy ước chuẩn hóa thích hợp. Gaussian là hàm ổn định dưới biến đổi Fourier, nên nó xuất hiện khắp nơi trong khuếch tán, xác suất và quang học.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu biến đổi Fourier như phổ liên tục và nắm một vài ví dụ cơ bản như Gaussian.

**Bậc sau đại học.** Bàn về các không gian Schwartz, định lý Plancherel, phân phối và vai trò trong PDE trên miền vô hạn.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
