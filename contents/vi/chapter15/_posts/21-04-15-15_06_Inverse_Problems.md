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

![Bài toán ngược: tái dựng tham số từ dữ liệu quan sát]({{ site.imgurl }}/chapter_img/chapter15/06_inverse_problems.svg)

Mọi bài toán thuận từ Chương 1 đến Chương 14 đều đi theo chiều xuôi: biết vật liệu bên trong, dự đoán kết quả đo bên ngoài. **Bài toán Ngược (Inverse Problems)** lật ngược toàn bộ câu hỏi: bác sĩ chỉ đo tia X hay dòng điện **trên mặt da**, nhà địa chất chỉ nghe sóng rung **trên mặt đất**, vậy có thể suy ngược ra chính xác hình ảnh cơ quan nội tạng hay túi dầu nằm sâu bên trong không? Câu hỏi tưởng giản dị ấy lại ẩn chứa thách thức lớn nhất của toán ứng dụng: **tính đặt không chỉnh (ill-posedness)** theo nghĩa Hadamard!

## Kiến thức cần nhớ: Bốn trụ cột của Bài toán Ngược trong PDE

1. **Ba câu hỏi cốt lõi: Tính Duy nhất, Ổn định và Tái tạo (Reconstruction)**:
   Một bài toán đặt chỉnh theo Hadamard cần tồn tại, duy nhất và ổn định. Bài toán ngược thường vi phạm nặng nề điều kiện thứ ba: nhiễu đo $10^{-4}$ trên dữ liệu có thể thổi phồng thành sai số khổng lồ trong nghiệm phục hồi!
2. **Ba bài toán ngược kinh điển trong khoa học & y học**:
   - *Chụp cắt lớp X-quang (Biến đổi Radon)*: tính không ổn định nhẹ (mất $1/2$ bậc đạo hàm—giải được bằng chiếu ngược lọc FBP).
   - *Bài toán Calderón (Chụp ảnh trở kháng điện EIT)*: khôi phục độ dẫn điện $\sigma(x)$ từ ánh xạ Dirichlet-to-Neumann—chỉ đạt **ổn định logarit** cực yếu!
   - *Tán xạ ngược & Địa chấn (FWI)*: khôi phục tốc độ sóng $c(x)$ từ sóng phản xạ.
3. **Điều chuẩn hóa (Regularization — Tikhonov, Total Variation & Prior Bayes)**:
   Thay vì giải trực tiếp $A u = y^\delta$ (nổ nhiễu), ta giải bài toán tối ưu $\min_u \|Au - y^\delta\|^2 + \alpha \mathcal{R}(u)$: tham số $\alpha > 0$ cân bằng giữa độ khớp dữ liệu và độ mượt/thưa của nghiệm!
4. **Sức mạnh của Phân tích Vi địa phương trong Bài toán Ngược**:
   Dù bài toán ngược phi tuyến toàn cục rất khó, công cụ $\operatorname{WF}$ và FIO chỉ ra chính xác phần ranh giới (kỳ dị) nào của vật thể bên trong có thể phục hồi ổn định từ dữ liệu biên!

## Mục tiêu

Bài học tùy chọn này giới thiệu bài toán ngược như một hướng ứng dụng quan trọng của giải tích vi địa phương và PDE. Sau bài học, sinh viên cần phân biệt rõ bài toán thuận với bài toán ngược, hiểu vì sao bài toán ngược thường không ổn định, và nắm vai trò của chính quy hóa (regularization), sự lan truyền kỳ dị và tính không đầy đủ của dữ liệu trong quá trình tái tạo.

## Kiến thức nền

Sinh viên nên nắm định lý lan truyền kỳ dị, các phương trình sóng và elliptic cơ bản cùng trực giác về dữ liệu đo có nhiễu. Điểm khác biệt cốt lõi là trong bài toán thuận, mô hình và tham số đã biết trước; còn trong bài toán ngược, chính cấu trúc ẩn của hệ là đối tượng cần tìm.

## Dẫn nhập

Trong bài toán thuận, ta biết phương trình, hệ số và nguồn, từ đó tính ra nghiệm hoặc dữ liệu quan sát. Trong bài toán ngược, chiều suy luận đảo lại: từ dữ liệu đo ở bên ngoài, ta tìm cách suy ra cấu trúc bên trong. Đây là bản chất của chụp cắt lớp vi tính, địa chấn phản xạ, siêu âm, radar và nhiều kỹ thuật đo đạc hiện đại.

Thách thức lớn nhất của bài toán ngược là tính không ổn định: một nhiễu rất nhỏ trong dữ liệu đo có thể dẫn tới sai lệch lớn trong kết quả tái tạo. Vì thế, đây là điểm giao thoa thực tiễn giữa giải tích PDE, thống kê và tính toán khoa học.


### Giải thích: Tận mắt thấy sự khuếch đại nhiễu khủng khiếp trong bài toán ngược truyền nhiệt

Xét bài toán ngược của phương trình nhiệt 1D $u_t = u_{xx}$ trên $(0, \pi)$ với $u(0,t)=u(\pi,t)=0$: ta đo được nhiệt độ $u(x, T)$ tại $T = 0{,}1\text{ s}$ và muốn suy ngược lại nhiệt độ ban đầu $u_0(x) = u(x, 0)$!
1. **Chiều thuận (làm trơn mũ)**: Mỗi mode $\sin(nx)$ bị suy giảm bởi thừa số $e^{-n^2 T}$:
   $$u_0(x) = \sin(nx) \xrightarrow{\text{thuận}} u(x, 0{,}1) = e^{-0{,}1 n^2}\sin(nx).$$
2. **Chiều ngược (khuếch đại nhiễu nổ tung!)**: Giả sử cảm biến tại $T = 0{,}1$ có một nhiễu đo siêu nhỏ $\delta u(x, 0{,}1) = 10^{-4}\sin(10x)$ (chỉ $0{,}01\%$ ở mode $n = 10$). Khi đảo ngược về $t = 0$:
   $$\delta u_0(x) = e^{+0{,}1 \times 10^2} \cdot 10^{-4}\sin(10x) = e^{10} \cdot 10^{-4}\sin(10x) \approx 22.026 \times 10^{-4}\sin(10x) \approx \mathbf{2{,}20\,\sin(10x)}!$$
   Nhiễu $0{,}0001$ bị thổi phồng gấp **$22.026$ lần** thành sai số $2{,}20$—chứng minh bằng con số vì sao bài toán ngược bắt buộc phải có **điều chuẩn hóa (regularization)**!
## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng việc lắng nghe tiếng vọng trong một căn phòng để suy đoán hình dạng căn phòng đó. Bài toán ngược hoạt động theo nguyên tắc tương tự: từ các phép đo gián tiếp bên ngoài, khôi phục cấu trúc không thể quan sát trực tiếp bên trong.

### Cách hình ảnh

Có thể biểu diễn hai chiều đối ngược bằng hai mũi tên:

- bài toán thuận: tham số -> mô hình -> dữ liệu;
- bài toán ngược: dữ liệu -> tái tạo tham số.

Khi bổ sung thêm thành phần nhiễu vào phía dữ liệu đo, người học thấy ngay bản chất khó khăn của bài toán ngược: đầu vào của phép nghịch đảo luôn chứa sai số.

### Cách hình thức

Nếu bài toán thuận được biểu diễn dưới dạng $$ \mathcal{F}(m)=d $$, với $$ m $$ là tham số hoặc cấu trúc ẩn còn $$ d $$ là dữ liệu quan sát, thì bài toán ngược yêu cầu xác định $$ m $$ từ $$ d $$. Trong nhiều trường hợp thực tế, ánh xạ ngược $$ \mathcal{F}^{-1} $$:

- không tồn tại trên toàn miền dữ liệu;
- không duy nhất;
- hoặc không liên tục (rất nhạy cảm với nhiễu).

Do đó, ta cần các phương pháp chính quy hóa và thông tin tiên nghiệm (prior).

## Ngộ nhận thường gặp

### “Bài toán ngược chỉ là giải ngược một công thức đại số”

Sai. Trở ngại cốt lõi nằm ở tính không ổn định và sự thiếu hụt dữ liệu đo.

### “Càng nhiều dữ liệu thì kết quả tái tạo tự động càng tốt”

Không hẳn. Cách dữ liệu ghi nhận các hướng kỳ dị của đối tượng quan trọng không kém số lượng phép đo.

### “Chính quy hóa là thủ thuật làm sai lệch bài toán”

Không đúng. Chính quy hóa là cơ chế toán học giúp xác định một nghiệm ổn định và có ý nghĩa trước nhiễu đo.

### “Giải tích vi địa phương quá trừu tượng để áp dụng cho bài toán ngược”

Sai. Chính giải tích vi địa phương xác định được kỳ dị nào là khả kiến và kỳ dị nào bị khuất trong dữ liệu đo.

## Bộ ba câu hỏi trung tâm

Thay vì gộp chung mọi trở ngại của bài toán ngược thành một khái niệm mơ hồ là “khó”, nên tách thành ba câu hỏi độc lập:

- **tính khả kiến:** những kỳ dị hoặc đặc trưng nào của đối tượng thực sự đi vào dữ liệu đo;
- **tính duy nhất:** dữ liệu hiện có có xác định duy nhất một nghiệm hay không;
- **tính ổn định:** nhiễu nhỏ trong dữ liệu có gây dao động lớn ở nghiệm tái tạo hay không.

Cách phân tách này giúp đọc tài liệu nghiên cứu rõ ràng hơn, vì nhiều công trình tập trung giải quyết riêng một hoặc hai khía cạnh trong bộ ba trên.

## Tiến trình học

### Bước 1: Phân biệt bài toán thuận và bài toán ngược

Nhấn mạnh rằng bài toán ngược không đơn thuần là đảo chiều công thức.

### Bước 2: Hiểu tính không ổn định

Phân tích cơ chế nhiễu nhỏ trong dữ liệu bị khuếch đại mạnh khi nghịch đảo trực tiếp.

### Bước 3: Áp dụng chính quy hóa

Làm rõ vai trò của các ràng buộc bổ sung và thông tin tiên nghiệm.

### Bước 4: Kết nối với giải tích vi địa phương

Sử dụng định lý lan truyền kỳ dị để xác định những biên cạnh nào có thể quan sát được từ dữ liệu.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao bài toán ngược thường không ổn định hơn bài toán thuận hay không?
- Sinh viên có nêu được lý do cần dùng chính quy hóa hay không?
- Sinh viên có hiểu vì sao tính khả kiến của kỳ dị là câu hỏi trọng tâm hay không?

## Ví dụ có lời giải

### Ví dụ 1: Chụp cắt lớp vi tính (CT)

Trong chụp cắt lớp vi tính, dữ liệu đo là các tích phân tia X đi qua cơ thể; từ đó cần khôi phục hàm mật độ mô bên trong. Đây là bài toán ngược điển hình với dữ liệu đo ở ngoài biên và đối tượng cần tìm nằm bên trong.

### Ví dụ 2: Địa chấn phản xạ

Sóng đàn hồi được phát xuống lòng đất và tín hiệu phản xạ được ghi nhận tại bề mặt. Từ thời gian truyền và dạng sóng phản xạ, ta suy ra cấu trúc địa tầng bên dưới; các kỳ dị của tín hiệu đo tương ứng trực tiếp với ranh giới giữa các lớp đất đá.

### Ví dụ 3: Tính không ổn định trước nhiễu cao tần

Khi dữ liệu chứa nhiễu tần số cao, phép nghịch đảo thô sẽ khuếch đại mạnh thành phần nhiễu đó, khiến ảnh tái tạo bị hỏng nếu không áp dụng chính quy hóa.

### Ví dụ 4: Vai trò của giải tích vi địa phương

Trong các mô hình truyền sóng, kỳ dị ghi nhận trên dữ liệu đo có thể được ánh xạ ngược thông qua toán tử FIO để suy ra kỳ dị của vật thể. Điều này cho thấy giải tích vi địa phương là công cụ thực tiễn để xác định chính xác phần cấu trúc nào là khả kiến.

### Ví dụ 5: Mất tính khả kiến do góc đo hạn chế

Nếu thiết bị chỉ thu thập dữ liệu trên một dải góc chiếu hạn chế, một số biên cạnh của vật thể sẽ không tạo tín hiệu đủ rõ để tái tạo. Đây là minh họa trực tiếp cho câu hỏi khả kiến: không phải mọi kỳ dị của vật thể đều truyền được thông tin tới thiết bị đo.

## Câu hỏi khái niệm

1. Vì sao bài toán ngược thường kém ổn định hơn nhiều so với bài toán thuận?
2. Chính quy hóa thực chất đang điều chỉnh dữ liệu đo hay điều chỉnh bản thân khái niệm nghiệm?
3. Vì sao xác định những kỳ dị nào khả kiến lại quan trọng trước khi cố tái tạo toàn bộ hàm?

## Bài toán ứng dụng

1. Trong y sinh, vì sao ảnh CT hay siêu âm về bản chất là nghiệm của một bài toán ngược?
2. Trong địa vật lý, vì sao sóng phản xạ mang thông tin sắc nét nhất về các ranh giới địa tầng?
3. Trong kiểm tra không phá hủy vật liệu, việc phát hiện vết nứt liên hệ thế nào với bài toán tái tạo kỳ dị?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Khi dữ liệu đo có nhiễu, ta có thể tin hoàn toàn vào nghiệm nghịch đảo trực tiếp không?
- Trong ảnh y khoa, mục tiêu quan trọng hơn là tái tạo chính xác mọi giá trị nền hay định vị đúng các đường biên?
- Vì sao bài toán ngược luôn gắn liền với câu hỏi “hình học đo như thế nào là đủ”?

### Hoạt động gợi ý

- Cho sinh viên vẽ sơ đồ thuận–ngược cho một ứng dụng cụ thể.
- Thảo luận nhóm về sự đánh đổi giữa độ ổn định và độ sắc nét khi điều chỉnh tham số chính quy hóa.
- So sánh trực quan kết quả tái tạo từ dữ liệu sạch và dữ liệu có nhiễu trên một mô phỏng đơn giản.

### Cách tăng mức độ tham gia

- Mở đầu bằng ứng dụng quen thuộc như chụp cắt lớp CT.
- Đề nghị sinh viên liệt kê các nguồn nhiễu thực tế trong phép đo.
- Thảo luận xem trong ảnh y khoa, biên cấu trúc hay giá trị tuyệt đối quan trọng hơn.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung vào sơ đồ khái niệm trước khi đi vào công thức chi tiết.
- Khai thác các ví dụ thực tiễn như CT, địa chấn và siêu âm.
- Nhấn mạnh thông điệp cốt lõi: bài toán ngược khó do dữ liệu không đầy đủ và có nhiễu.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu ngắn gọn phương pháp chính quy hóa Tikhonov.
- Liên hệ biến đổi Radon với mô hình toán học của CT.
- Khảo sát vai trò của FIO trong việc ánh xạ ngược tập mặt sóng.

## Ghi nhớ nhanh

Bài toán ngược hướng tới việc khôi phục cấu trúc ẩn từ dữ liệu quan sát. Do tính không ổn định trước nhiễu, chính quy hóa là bắt buộc, còn giải tích vi địa phương giúp xác định chính xác kỳ dị nào của đối tượng thực sự khả kiến trong dữ liệu.

---

## Ứng dụng thực tế

### 1. Chụp cắt lớp vi tính

Mô hình toán học cơ bản của CT là biến đổi Radon:

$$
Rf(\theta,s)=\int_{x\cdot \theta=s} f(x)\,d\sigma(x).
$$

Bài toán ngược là xác định mật độ $$ f $$ từ các tích phân tia X (dưới giả thiết tia đi thẳng và bỏ qua tán xạ). Chất lượng ảnh tái tạo không chỉ phụ thuộc vào thuật toán nghịch đảo mà còn phụ thuộc vào những kỳ dị nào thực sự được hình học phép đo ghi nhận.

### 2. Chụp ảnh trở kháng điện (EIT)

Trong EIT, ta đặt điện áp trên biên cơ thể và đo dòng điện sinh ra. Mô hình PDE cơ bản là $$ \nabla \cdot (\gamma(x) \nabla u)=0 $$, với độ dẫn $$ \gamma(x) $$ chưa biết (giả sử môi trường liên tục và tiếp xúc điện cực tốt). Đây là bài toán ngược không chỉnh nghiêm trọng nên nhiễu nhỏ dễ phá hủy chi tiết tần số cao; việc khôi phục cấu trúc thô vì thế ổn định hơn nhiều so với khôi phục biên sắc nét.

### 3. Nghịch đảo địa chấn

Với phương trình sóng $$ u_{tt}-c(x)^2\Delta u=s $$, mục tiêu là suy ra vận tốc $$ c(x) $$ hoặc các mặt phản xạ từ dữ liệu bề mặt (dưới giả thiết biết nguồn phát và chế độ gần tuyến tính). Hiện tượng đa đường truyền (multipathing), suy hao và sai số nguồn khiến bài toán khó hơn nhiều; thông tin tin cậy nhất thường nằm ở thời gian truyền và vị trí các mặt phản xạ thay vì toàn bộ trường vận tốc trơn.

## Trực giác sâu hơn

Bài toán ngược không đơn thuần là đảo chiều một phép tính mà là đảo một ánh xạ vốn có thể làm mờ, suy giảm hoặc mất mát thông tin. Thêm dữ liệu chỉ hữu ích khi hình học đo bổ sung được các hướng khả kiến mới và kiểm soát tốt mức khuếch đại nhiễu.

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

Có thể dùng `Plotly.js` để sinh viên điều chỉnh mức nhiễu và tham số chính quy hóa bằng thanh trượt, quan sát trực tiếp tác động lên nghiệm tái tạo trong bài toán khử mờ 1D.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `limited angle tomography artifacts`, `electrical impedance tomography inverse problem`, hoặc `seismic inversion wave front set`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào sự khác biệt giữa bài toán thuận và ngược, cùng trực giác về cách nhiễu làm phép nghịch đảo mất ổn định.

### Mức sau đại học (Graduate)

Đi sâu vào tuyến tính hóa, toán tử chuẩn tắc (normal operators), ước lượng ổn định, chính quy hóa Tikhonov và các định lý khả kiến vi địa phương cho biến đổi Radon và toán tử sóng.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chụp cắt lớp y học
- Bài toán: Khôi phục cấu trúc bên trong cơ thể từ các phép đo gián tiếp bên ngoài.
- Mô hình: Toán tử thuận ánh xạ vật thể sang dữ liệu; bài toán ngược tìm nghịch đảo hoặc nghịch đảo xấp xỉ.
- Giả thiết và giới hạn: Góc chiếu hữu hạn, nhiễu đo và sai số mô hình đều làm giảm độ ổn định.
- Diễn giải: Giải tích vi địa phương chỉ rõ kỳ dị nào khả kiến từ dữ liệu đo.

#### Bài toán ngược địa chấn
- Bài toán: Suy ra các mặt phản xạ trong lòng đất từ dữ liệu sóng trên bề mặt.
- Mô hình: Kết hợp tuyến tính hóa, toán tử chuẩn tắc và FIO để phân tích tính ổn định và tính khả kiến.
- Giả thiết và giới hạn: Không phải mọi hướng kỳ dị đều được ghi nhận bởi hệ cảm biến.
- Diễn giải: Tính khả kiến trên không gian pha quan trọng hơn sự tồn tại đơn thuần trong không gian vật lý.

### 2. Trực giác bổ sung và các kết nối

Bài toán ngược thường không ổn định vì nghịch đảo của một toán tử làm suy giảm cao tần sẽ khuếch đại mạnh nhiễu đo; do đó chính quy hóa là yêu cầu bắt buộc. Ngay cả khi bài toán thuận có nghiệm duy nhất, bài toán ngược tương ứng vẫn có thể rất kém ổn định.

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

Nếu toán tử thuận là phép tích chập với ký hiệu $$ a(\xi) $$ rất nhỏ ở tần số cao, phép nghịch đảo hình thức nhân bởi $$ 1/a(\xi) $$ sẽ khuếch đại mạnh nhiễu tại nơi $$ a(\xi) $$ gần $$ 0 $$. Chính quy hóa Tikhonov thay thế bằng bộ nhân ổn định hơn:
$$
\frac{\overline{a(\xi)}}{\lvert a(\xi)\rvert^2+\varepsilon}.
$$
Đây là minh họa tiêu biểu cho bản chất bất ổn định của bài toán ngược.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt bài toán thuận và ngược qua ví dụ khử mờ đơn giản.

**Bậc sau đại học.** Kết nối với toán tử chuẩn tắc, tính khả kiến, chính quy hóa và các định lý tái tạo vi địa phương.

## Video tham khảo

- Nên xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Các phương pháp vi địa phương của Maciej Zworski dùng cho bài toán biên và phổ ngược.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Bài giảng của András Vasy về lý thuyết tán xạ và các bài toán toàn cục kiểu ngược cho toán tử sóng.
- [Introduction to Fourier Integral operators 1 (Allan Greenleaf)](https://www.youtube.com/watch?v=4O_oC9kFFWQ) — Mathematics video VAROQUI Hervé, tiếng Việt. Toán tử tích phân Fourier — công cụ mô tả phép đo trong nhiều bài toán ngược.
