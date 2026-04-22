---
layout: post
title: "Ứng Dụng: Bài Toán Ngược"
chapter: '15'
order: 6
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: optional
---

![Bài toán ngược: tái dựng tham số từ dữ liệu quan sát]({{ site.imgurl }}/chapter_img/chapter15/06_inverse_problems.svg )

## Mục tiêu

Bài optional này giới thiệu bài toán ngược như hướng ứng dụng tự nhiên của vi địa phương và PDE. Sau bài học, sinh viên cần phân biệt bài toán thuận với bài toán ngược, hiểu vì sao bài toán ngược thường không ổn định, và thấy vai trò của regularization, propagation of singularities, và dữ liệu không đầy đủ trong tái dựng.

## Kiến thức nền

Sinh viên nên nắm propagation of singularities, phương trình sóng hay elliptic cơ bản, và trực giác về dữ liệu đo bị nhiễu. Cũng nên nhớ rằng trong bài toán thuận, mô hình đã biết; còn trong bài toán ngược, thứ cần tìm lại chính là cấu trúc ẩn của hệ.

## Dẫn nhập

Trong bài toán thuận, ta biết phương trình, biết hệ số, biết nguồn, rồi tính ra nghiệm hoặc dữ liệu đo. Trong bài toán ngược, thứ tự ấy bị đảo lại: ta quan sát dữ liệu ở ngoài, rồi cố suy ra bên trong. Đó là bản chất của chụp cắt lớp, địa chấn phản xạ, siêu âm, radar, và rất nhiều công nghệ hiện đại.

Điều làm bài toán ngược khó hơn nhiều là tính không ổn định. Một nhiễu rất nhỏ trong dữ liệu có thể gây thay đổi lớn trong đối tượng tái dựng. Vì vậy, đây là nơi phân tích, PDE, thống kê, và tính toán gặp nhau một cách rất thực tế.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng bạn nghe tiếng vọng trong một căn phòng và cố suy ra hình dạng của căn phòng từ tiếng vọng đó. Đây là bài toán ngược: từ kết quả đo bên ngoài, suy ra cấu trúc không nhìn thấy trực tiếp.

### Cách hình ảnh

Giáo viên nên vẽ hai mũi tên:

- bài toán thuận: tham số -> mô hình -> dữ liệu;
- bài toán ngược: dữ liệu -> tái dựng tham số.

Sau đó thêm một đám “nhiễu” ở phía dữ liệu để sinh viên thấy ngay điểm khó: dữ liệu đầu vào của bài toán ngược vốn đã không sạch.

### Cách hình thức

Nếu bài toán thuận được mô hình hóa như $$ \mathcal{F}(m)=d $$, trong đó $$ m $$ là tham số hay cấu trúc ẩn, còn $$ d $$ là dữ liệu, thì bài toán ngược là tìm $$ m $$ từ $$ d $$. Trong nhiều trường hợp, ánh xạ $$ \mathcal{F}^{-1} $$:

- không tồn tại toàn cục;
- không duy nhất;
- hoặc rất không ổn định.

Điều đó dẫn đến nhu cầu regularization và các kỹ thuật dùng thông tin trước.

## Ngộ nhận thường gặp

### “Bài toán ngược chỉ là giải ngược lại một công thức”

Sai. Khó khăn chính là không ổn định và thiếu dữ liệu.

### “Nếu dữ liệu nhiều thì tự động tái dựng tốt”

Không. Cách dữ liệu liên hệ với singularity của đối tượng quan trọng không kém số lượng dữ liệu.

### “Regularization là mẹo kỹ thuật làm sai bài toán”

Không. Nó là cách làm cho bài toán trở nên có ý nghĩa trước nhiễu.

### “Microlocal analysis quá trừu tượng để giúp bài toán ngược”

Sai. Chính nó giúp hiểu singularity nào có thể thấy được và singularity nào bị mất.

## Bộ ba câu hỏi trung tâm

Khi bắt đầu học bài toán ngược, sinh viên thường gom mọi khó khăn vào một từ chung là “khó”. Thực ra nên tách thành ba câu hỏi khác nhau:

- khả kiến: singularity hay đặc trưng nào của đối tượng có thật sự đi vào dữ liệu đo;
- duy nhất: dữ liệu hiện có có xác định được một nghiệm duy nhất hay không;
- ổn định: nhiễu nhỏ của dữ liệu có làm tái dựng dao động mạnh hay không.

Tách bộ ba này ra giúp sinh viên đọc tài liệu nghiên cứu tốt hơn, vì rất nhiều bài báo chỉ giải quyết một hoặc hai câu hỏi trong số đó, chứ không phải toàn bộ bài toán ngược một lúc.

## Tiến trình học

### Bước 1: Phân biệt thuận và ngược

Sinh viên phải thấy bài toán ngược không chỉ là “đổi chiều suy luận”.

### Bước 2: Hiểu tính không ổn định

Nhiễu nhỏ ở dữ liệu có thể khuếch đại mạnh khi tái dựng.

### Bước 3: Đưa vào regularization

Nêu vai trò của ràng buộc bổ sung hay thông tin prior.

### Bước 4: Kết nối với vi địa phương

Dùng propagation of singularities để hiểu dữ liệu nhìn thấy những cạnh hay singularity nào.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao bài toán ngược thường khó hơn bài toán thuận không?
- Sinh viên có nêu được ít nhất một lý do cần regularization không?
- Sinh viên có hiểu tại sao visibility của singularity là câu hỏi trung tâm không?

## Ví dụ có lời giải

### Ví dụ 1: Chụp cắt lớp

Trong CT scan, dữ liệu là các tích phân tia X qua cơ thể. Từ các tích phân đó, ta cố tái dựng mật độ bên trong. Đây là bài toán ngược điển hình: dữ liệu đo ngoài biên, đối tượng cần tìm ở bên trong.

### Ví dụ 2: Địa chấn phản xạ

Sóng được phát xuống lòng đất và tín hiệu phản xạ được ghi lại trên mặt đất. Từ thời gian và cấu trúc tín hiệu phản xạ, ta suy ra lớp địa chất bên dưới. Singularity của tín hiệu phản xạ thường tương ứng với biên của các lớp vật liệu.

### Ví dụ 3: Tính không ổn định

Nếu dữ liệu bị nhiễu cao tần, phép nghịch đảo thô có thể khuếch đại nhiễu này rất mạnh. Ví dụ này giải thích vì sao tái dựng trực tiếp thường cho ảnh đầy nhiễu và cần regularization.

### Ví dụ 4: Vai trò của microlocal analysis

Trong nhiều mô hình sóng, singularity quan sát được ở dữ liệu đo có thể được kéo ngược qua FIO để suy ra singularity của vật thể. Ví dụ này cho thấy vi địa phương không chỉ là lý thuyết trừu tượng mà là công cụ để quyết định “cái gì nhìn thấy được”.

### Ví dụ 5: Mất khả kiến vì góc đo hạn chế

Nếu máy đo chỉ quan sát được từ một số góc nhất định, một số biên của vật thể có thể không tạo ra dữ liệu đủ mạnh để tái dựng. Đây là ví dụ rất trực quan cho câu hỏi khả kiến: không phải mọi singularity của vật thể đều có đường đi tới thiết bị đo.

## Câu hỏi khái niệm

1. Vì sao bài toán ngược thường không ổn định hơn nhiều so với bài toán thuận?
2. Regularization đang sửa dữ liệu hay sửa chính khái niệm nghiệm của bài toán?
3. Tại sao việc hiểu singularity nào có thể được quan sát là câu hỏi quan trọng hơn việc tái dựng toàn bộ hàm một cách mù quáng?

## Bài toán ứng dụng

1. Trong y sinh, vì sao ảnh CT hay siêu âm về bản chất là kết quả của bài toán ngược?
2. Trong địa vật lý, vì sao phản xạ sóng lại mang thông tin rõ nhất về các biên lớp vật chất?
3. Trong kiểm tra không phá hủy vật liệu, việc phát hiện vết nứt là ví dụ của tái dựng singularity như thế nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu dữ liệu có nhiễu, em có nên tin hoàn toàn vào nghiệm nghịch đảo thô không?
- Trong một ảnh y khoa, ta cần tái dựng toàn bộ hàm thật hay chủ yếu là các biên quan trọng?
- Tại sao bài toán ngược luôn gắn chặt với câu hỏi “dữ liệu nào là đủ”?

### Hoạt động gợi ý

- Cho sinh viên vẽ sơ đồ thuận-ngược cho một ứng dụng thực tế.
- Thảo luận nhóm về việc regularization đánh đổi giữa ổn định và độ sắc nét.
- So sánh một dữ liệu sạch và một dữ liệu nhiễu trong mô phỏng tái dựng đơn giản.

### Cách tăng tham gia

- Bắt đầu bằng ví dụ chụp cắt lớp mà sinh viên biết.
- Cho sinh viên đề xuất nguồn nhiễu thực tế trong đo đạc.
- Mời sinh viên tranh luận xem trong ảnh y khoa, biên hay giá trị tuyệt đối quan trọng hơn.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung vào sơ đồ khái niệm hơn là mô hình chi tiết.
- Dùng các ví dụ đời thực như CT, địa chấn, siêu âm.
- Nhấn mạnh một thông điệp: bài toán ngược khó vì dữ liệu không đầy đủ và có nhiễu.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu ngắn gọn về regularization kiểu Tikhonov.
- Liên hệ Radon transform với CT.
- Khảo sát vai trò của FIO trong việc kéo ngược wave front set.

## Ghi nhớ nhanh

Bài toán ngược cố tái dựng cấu trúc ẩn từ dữ liệu quan sát. Nó thường khó vì không ổn định, và vi địa phương giúp trả lời câu hỏi cốt lõi: singularity nào của đối tượng thật sự có thể được nhìn thấy trong dữ liệu.

---

## Ứng dụng thực tế

### 1. Chụp cắt lớp vi tính

Mô hình cơ bản của CT là biến đổi Radon

$$
Rf(\theta,s)=\int_{x\cdot \theta=s} f(x)\,d\sigma(x).
$$

Bài toán ngược là tìm mật độ $$ f $$ từ các tích phân tia X. Mô hình này giả định tia đi thẳng và tán xạ không đáng kể, điều chỉ gần đúng trong thực tế. Diễn giải quan trọng là chất lượng tái dựng phụ thuộc không chỉ vào thuật toán nghịch đảo mà còn vào việc singularity nào thực sự được hình học phép đo nhìn thấy.

### 2. Chụp trở kháng điện

Trong EIT, ta áp điện áp trên biên cơ thể và đo dòng điện tạo ra. Mô hình PDE đơn giản là $$ \nabla \cdot (\gamma(x) \nabla u)=0 $$, với $$ \gamma(x) $$ là độ dẫn chưa biết. Mô hình giả định môi trường liên tục và tiếp xúc điện cực tốt. Đây là bài toán ngược rất không chỉnh, nên nhiễu nhỏ có thể phá hủy chi tiết cao tần. Diễn giải là: khôi phục cấu trúc thô thường ổn định hơn nhiều so với khôi phục biên sắc nét.

### 3. Nghịch đảo địa chấn

Với trường sóng thỏa $$ u_{tt}-c(x)^2\Delta u=s $$, ta muốn suy ra vận tốc $$ c(x) $$ hoặc các mặt phản xạ từ số liệu ở biên. Mô hình giả định biết nguồn phát và chế độ sóng gần tuyến tính. Giới hạn là multipathing, suy hao, và nguồn không chắc chắn làm bài toán khó hơn đáng kể. Diễn giải thực tế là thông tin đáng tin cậy đầu tiên thường nằm ở thời gian truyền và các biên phản xạ, chứ không phải ở toàn bộ bản đồ hệ số trơn.

## Trực giác sâu hơn

Bài toán ngược không chỉ là “làm phép ngược”. Ta đang cố đảo một ánh xạ có thể làm mất, làm mờ, hoặc khuếch đại thông tin. Ngộ nhận thường gặp là cứ có thêm dữ liệu thì nghiệm sẽ ổn định hơn. Trên thực tế, hình học đo đạc, độ nhìn thấy, và cơ chế khuếch đại nhiễu mới là các yếu tố quyết định.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 600)
f_true = (np.abs(x) < 1.5).astype(float)
kernel = np.exp(-x**2 / 0.7)
kernel /= kernel.sum()
data = np.convolve(f_true, kernel, mode='same')
noise = 0.03 * np.random.randn(len(x))
data_noisy = data + noise

K = np.fft.fft(kernel)
D = np.fft.fft(data_noisy)
recon = np.real(np.fft.ifft(D / (K + 1e-2)))

plt.figure(figsize=(9, 5))
plt.plot(x, f_true, label='đối tượng thật')
plt.plot(x, data_noisy, label='dữ liệu đo có nhiễu')
plt.plot(x, recon, label='nghịch đảo có regularization')
plt.legend()
plt.title('Mô hình bài toán ngược: làm mờ, nhiễu, tái dựng')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để cho sinh viên kéo thanh trượt mức nhiễu và tham số regularization, rồi quan sát ảnh hưởng của chúng lên nghiệm nghịch đảo trong ví dụ deblurring 1D.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `limited angle tomography artifacts`, `electrical impedance tomography inverse problem`, hoặc `seismic inversion wave front set`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào sự khác nhau giữa bài toán thuận và ngược, cùng với trực giác rằng nhiễu có thể làm phép nghịch đảo rất không ổn định.

### Mức sau đại học (Graduate)

Đi sâu vào linearization, normal operators, ước lượng ổn định, regularization kiểu Tikhonov, và các định lý khả kiến vi địa phương cho các toán tử đo kiểu Radon hay toán tử sóng.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chụp cắt lớp y học
- Bài toán: Từ các phép đo gián tiếp, ta muốn khôi phục cấu trúc bên trong cơ thể.
- Mô hình: Toán tử thuận ánh xạ vật thể sang dữ liệu; bài toán ngược là tìm nghịch đảo hay nghịch đảo gần đúng.
- Giả thiết và giới hạn: Dữ liệu hữu hạn góc, nhiễu và mô hình chưa hoàn hảo đều làm bài toán không ổn định.
- Diễn giải: Microlocal analysis cho biết singularity nào có thể thấy được từ dữ liệu.

#### Bài toán nghịch địa chấn
- Bài toán: Từ sóng đo trên bề mặt, suy ra các mặt phản xạ trong lòng đất.
- Mô hình: Dùng linearization, normal operator và FIO để phân tích stability và visibility.
- Giả thiết và giới hạn: Không phải mọi hướng singularity đều được quan sát.
- Diễn giải: "Thấy được" trong phase space quan trọng hơn chỉ "có tồn tại" trong không gian vật lý.

### 2. Trực giác bổ sung và các kết nối

Bài toán ngược thường không ổn định vì nghịch đảo của bộ lọc suy giảm cao tần sẽ khuếch đại nhiễu. Điều này giải thích vì sao regularization là bắt buộc chứ không phải tùy chọn. Một ngộ nhận phổ biến là nếu bài toán thuận có nghiệm duy nhất thì bài toán ngược cũng ổn định; điều đó sai trong rất nhiều bài toán thực tế.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 512, endpoint=False)
u_true = np.sin(3 * x) + 0.4 * np.sin(12 * x)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi
a = 1 / (1 + 0.3 * xi**2)
data = np.fft.ifft(a * np.fft.fft(u_true)).real
noise = 0.03 * np.random.default_rng(0).standard_normal(len(x))
data_noisy = data + noise

eps = 0.02
u_rec = np.fft.ifft(np.conj(a) * np.fft.fft(data_noisy) / (np.abs(a)**2 + eps)).real

plt.plot(x, u_true, label="that")
plt.plot(x, data_noisy, label="du lieu mo + nhieu")
plt.plot(x, u_rec, label="tai dung regularized")
plt.legend()
plt.title("Bai toan nghich can regularization")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: inverse problem deconvolution regularization visualization
- search: CT visible singularities microlocal analysis
- search: seismic inverse problems wave front set intuition

### 5. Bài toán mẫu có bối cảnh thực

Nếu toán tử thuận là convolution với symbol $$ a(\xi) $$ nhỏ ở cao tần, thì nghịch đảo chính thức nhân bởi $$ 1/a(\xi) $$ sẽ khuếch đại nhiễu tại nơi $$ a(\xi) $$ gần $$ 0 $$. Vì vậy regularization kiểu Tikhonov thay nghịch đảo bởi
$$
\frac{\overline{a(\xi)}}{\lvert a(\xi)\rvert^2+\varepsilon}.
$$
Đây là ví dụ điển hình cho lý do bất ổn định của bài toán ngược.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt bài toán thuận và ngược qua ví dụ deblurring đơn giản.

**Bậc sau đại học.** Kết nối với normal operators, visibility, regularization va microlocal reconstruction theorems.
