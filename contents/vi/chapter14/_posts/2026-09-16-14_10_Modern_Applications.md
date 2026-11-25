---
layout: post
title: "14-10 Ứng dụng hiện đại: Neural operator như ký hiệu học được"
chapter: '14'
order: 10
owner: Course Team
lang: vi
categories:
- chapter14
lesson_type: optional
---

Nhìn vào công thức của một tầng mạng Fourier Neural Operator (FNO): biến đổi FFT dữ liệu sang miền tần số, nhân với một ma trận trọng số học được $R(\xi)$, rồi biến đổi ngược IFFT! Dưới con mắt của Chương 14, FNO không hề là một "hộp đen bí ẩn"—nó chính là một **toán tử giả vi phân (hoặc bộ nhân Fourier) có ký hiệu được học trực tiếp từ dữ liệu**! Kết nối này mở ra cách thiết kế kiến trúc AI vật lý vừa tiết kiệm tham số, vừa đảm bảo tính bị chặn trên không gian Sobolev $H^s$.

## Kiến thức cần nhớ: Bốn trụ cột nối Toán tử Giả vi phân với Neural Operators

1. **Tầng FNO như Toán tử Giả vi phân Hệ số Hằng**:
   Phép toán $\mathcal{F}^{-1}\big(R(\xi)\widehat{u}(\xi)\big)$ chính là $\operatorname{Op}(R)$ với ký hiệu chỉ phụ thuộc $\xi$. Cắt cụt tần số cao $|\xi| \le k_{\max}$ hoạt động như một toán tử làm trơn thuộc $\Psi^{-\infty}$!
2. **Ký hiệu Phụ thuộc Không gian $p(x, \xi)$ và Kiến trúc Đa thang**:
   Khi môi trường vật lý không đồng nhất (như đá địa chất hay vật liệu composite), một bộ nhân hằng không đủ; ta cần tổng các nhánh điều biến không gian $\sum_j a_j(x)\mathcal{F}^{-1}(R_j(\xi)\widehat{u}(\xi))$—xấp xỉ hạng thấp của ký hiệu đầy đủ $p(x, \xi)$!
3. **Bậc $m$ của Ký hiệu quyết định Không gian Nguồn–Đích**:
   Theo Định lý Calderón–Vaillancourt và tính bị chặn Sobolev, nếu ký hiệu học được suy giảm như $\langle\xi\rangle^m$ thì toán tử ánh xạ liên tục $H^s \to H^{s-m}$—giúp chẩn đoán ngay mô hình đang học toán tử làm trơn ($m < 0$) hay toán tử vi phân ($m > 0$).
4. **Parametrix Học được làm Bộ Tiền điều kiện (Neural Preconditioners)**:
   Thay vì ép mạng thay thế hoàn toàn bộ giải PDE, xu hướng tiên tiến nhất là dùng mạng học một **parametrix xấp xỉ** $Q_\theta \approx P^{-1}$ rồi dùng $Q_\theta$ làm bộ tiền điều kiện cho phương pháp lặp GMRES/CG đạt độ chính xác máy $10^{-12}$!

## Mục tiêu

Bài học tùy chọn này trình bày cách nhìn nhận Fourier neural operator (FNO), spectral neural operator và các kiến trúc liên quan giai đoạn 2022–2024 như phiên bản tính toán của toán tử giả vi phân. Sau bài học, sinh viên cần biết cách đối chiếu bộ nhân Fourier học được với ký hiệu trong lớp $$S^m$$, giải thích bài toán học toán tử không aliasing bằng ngôn ngữ của Hörmander, và hiểu parametrix elliptic như mô hình giải tích cho toán tử nghịch đảo học được. Nội dung này bổ sung góc nhìn ứng dụng chứ không thay thế phép tính ký hiệu của chương.

## Kiến thức nền

Sinh viên cần nắm vững bộ nhân Fourier, các lớp ký hiệu, phép hợp thành toán tử giả vi phân (ΨDO) và khái niệm parametrix elliptic. Bài ôn tập về bộ nhân Fourier ở đầu chương là phần chuẩn bị phù hợp.

## Dẫn nhập

Ở xấp xỉ bậc nhất, một toán tử giả vi phân cổ điển là một bộ nhân Fourier có ký hiệu $$a(x,\xi)$$ biến thiên chậm theo $$x$$ và có các đạo hàm theo $$\xi$$ được kiểm soát. Một lớp Fourier neural operator hoạt động như một bộ nhân Fourier với ký hiệu là mảng tham số huấn luyện $$R_\xi$$, theo sau bởi một phép biến đổi phi tuyến tác động từng điểm. Phép tương tự này không hoàn toàn đồng nhất — tính phi tuyến và dải tần hữu hạn đưa mô hình ra ngoài khuôn khổ phép tính ΨDO tuyến tính — nhưng đây là cách nhìn rất hữu ích. Nó giải thích vì sao FNO hoạt động hiệu quả trên các bài toán elliptic và parabolic bất biến tịnh tiến, vì sao mô hình gặp khó khăn với hệ số không trơn, và vì sao aliasing là một vấn đề mang bản chất vi cục bộ chứ không đơn thuần là lỗi số học.

Kovachki và cộng sự (*JMLR* 2023) đã mô tả FNO như một họ toán tử tích phân tham số hóa với nhân bất biến tịnh tiến. Fanaskov và Oseledets (*Spectral Neural Operators*, 2022–2023; [arXiv:2205.10573](https://arxiv.org/abs/2205.10573)) trình bày phép tính phổ một cách tường minh hơn nữa. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra và Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023; [arXiv:2305.19913](https://arxiv.org/abs/2305.19913)) xây dựng khung lý thuyết cho việc học toán tử không aliasing: mô hình rời rạc phải là hạn chế đúng đắn của một toán tử liên tục, thay vì chỉ là một ánh xạ phụ thuộc vào lưới tính. Raonić, Molinaro, Rohner, Mishra và de Bézenac (*Convolutional Neural Operators*, ICLR 2024; [arXiv:2302.01178](https://arxiv.org/abs/2302.01178)) tiếp tục phát triển hướng sử dụng nhân tích chập nhất quán với bài toán liên tục.

Các công trình này trở nên dễ tiếp cận hơn nhiều khi người học đã nắm lớp ký hiệu $$S^m_{\rho,\delta}$$ và cách xây dựng parametrix. Về bản chất, việc học toán tử nghịch đảo của một toán tử elliptic từ dữ liệu chính là nỗ lực xấp xỉ một parametrix.


### Giải thích: Đọc trực tiếp ký hiệu $p(x, \xi)$ của một tầng FNO điều biến không gian

Xét một tầng học toán tử 1D đơn giản kết hợp hai nhánh không gian–tần số:
$$(Tu)(x) = a_1(x)\,\mathcal{F}^{-1}\!\left(\frac{1}{1 + \xi^2}\widehat{u}(\xi)\right)(x) + a_2(x)\,\mathcal{F}^{-1}\!\left(\frac{i\xi}{1 + \xi^2}\widehat{u}(\xi)\right)(x).$$
1. **Ký hiệu tương đương của tầng mạng**:
   $$p(x, \xi) = \frac{a_1(x) + i\xi\,a_2(x)}{1 + \xi^2}.$$
2. **Xác định bậc ký hiệu khi $|\xi| \to \infty$**:
   - Nhánh 1 suy giảm như $O(|\xi|^{-2}) \in S^{-2}$ (tăng 2 bậc trơn).
   - Nhánh 2 suy giảm như $O(|\xi|^{-1}) \in S^{-1}$ (tăng 1 bậc trơn).
   - Toàn tầng là một $\Psi$DO bậc $m = \mathbf{-1}$, nên nó ánh xạ liên tục từ $L^2(\mathbb{R})$ vào $H^1(\mathbb{R})$—giải thích chính xác bằng ngôn ngữ $\Psi$DO tại sao tầng FNO tự động tạo ra đầu ra mượt mà!
## Khái niệm then chốt

### Ký hiệu và bộ nhân học được

Toán tử $$Au=\mathcal{F}^{-1}\bigl(a(\xi)\hat u(\xi)\bigr)$$ là trường hợp hệ số hằng của một ΨDO cấp $$m$$ khi $$a\in S^m$$. Một lớp FNO cắt cụt $$a$$ trên một miền tần số thấp và cho phép ký hiệu phụ thuộc theo kênh. Việc huấn luyện $$a$$ trên các cặp dữ liệu $$(u,Au)$$ chính là bài toán nhận dạng ký hiệu. Nếu toán tử mục tiêu là $$(-\Delta+1)^{-1}$$, ký hiệu học được cần có dạng xấp xỉ $$(|\xi|^2+1)^{-1}$$ trên dải tần đã phân giải và không được tăng như một lũy thừa dương của $$|\xi|$$.

### Phép hợp thành và xếp chồng các lớp

Định lý hợp thành chỉ ra rằng ký hiệu của $$AB$$ có dạng $$a\#b=ab$$ cộng với các số hạng bậc thấp hơn. Do đó, việc xếp chồng các lớp FNO tuyến tính (chưa có hàm kích hoạt phi tuyến) tương ứng với phép nhân ký hiệu rời rạc. Hàm kích hoạt phi tuyến đặt giữa các lớp đưa mô hình ra ngoài phép tính ΨDO tuyến tính; đây vừa là nguồn tạo nên khả năng biểu diễn phong phú, vừa là nguyên nhân gây ra aliasing, vì tích từng điểm của hai hàm giới hạn dải tần nói chung không còn giới hạn dải tần.

### Parametrix elliptic như toán tử nghịch đảo học được

Nếu $$A$$ là toán tử elliptic, tồn tại một ΨDO $$B$$ sao cho $$BA-I$$ và $$AB-I$$ là các toán tử làm trơn. Một mạng nơ-ron học toán tử nghịch đảo, ánh xạ $$Au$$ về $$u$$ sai khác một phần dư trơn, chính là cách hiện thực hóa ý tưởng này bằng phương pháp số. Vì vậy, ta nên kiểm tra toán tử nghịch đảo học được trên các đầu vào dao động mạnh: ở tần số cao, ký hiệu học được phải nghịch đảo đúng ký hiệu chính, trong khi ở tần số thấp nó có thể tự do hơn — hoàn toàn tương tự việc parametrix chỉ xác định duy nhất modulo các toán tử làm trơn.

### Aliasing như phép lượng tử hóa sai lệch

Một ánh xạ trên lưới làm gập các mode tần số cao lên mode tần số thấp không còn là một ΨDO cấp dự kiến mà đã trở thành một toán tử khác. Các kiến trúc tương đương biểu diễn đòi hỏi việc thay đổi lưới không làm thay đổi toán tử liên tục đang được rời rạc hóa. Đó chính là phiên bản tính toán của nguyên lý rằng ΨDO được định nghĩa trên không gian hàm chứ không phải trên mảng rời rạc.

## Phương pháp và kỹ thuật

1. Xác định ký hiệu chính dự kiến (tức hành vi của toán tử ở tần số cao).
2. Kiểm tra tốc độ suy giảm hoặc tăng trưởng của bộ nhân học được so với lớp ký hiệu $$S^m$$.
3. Kiểm tra phép hợp thành: hợp thành của toán tử nghịch đảo học được với toán tử thuận có xấp xỉ toán tử đồng nhất modulo phần dư làm trơn hay không.
4. Làm mịn lưới tính: nếu bản sắc của toán tử thay đổi khi tinh lưới, mô hình đó không đại diện cho một ΨDO liên tục.
5. Với bài toán có hệ số biến thiên, cần xem xét kiến trúc có khả năng biểu diễn ký hiệu phụ thuộc vị trí $$a(x,\xi)$$ hay chỉ giới hạn ở một phép tích chập.

Các kiến trúc như Geo-FNO và convolutional neural operator đều nhằm khôi phục sự phụ thuộc vào $$x$$ và tính bất biến hình học trong khi vẫn duy trì tính nhất quán với toán tử liên tục.

## Ví dụ

### Ví dụ 1: Ký hiệu thế Bessel

Toán tử $$(I-\Delta)^{-s/2}$$ có ký hiệu $$(1+|\xi|^2)^{-s/2}\in S^{-s}$$. Một lớp phổ tuyến tính được huấn luyện trên ánh xạ này cần tái tạo được dạng hàm hướng kính đó. Việc vẽ đồ thị $$|R_\xi|$$ theo $$|\xi|$$ trên thang log-log là một cách kiểm chứng trực quan thuộc bài tập về lớp ký hiệu.

### Ví dụ 2: Hạn chế trên hệ số không trơn

Toán tử $$-\operatorname{div}(a(x)\nabla\cdot)$$ chỉ là một ΨDO cấp $$2$$ khi hệ số $$a$$ đủ trơn. Nếu $$a$$ chỉ bị chặn và thỏa điều kiện elliptic, bài toán vẫn đặt chỉnh trong $$H^1$$ nhưng toán tử không còn là một ΨDO cổ điển. Một mô hình FNO huấn luyện trên các hệ số $$a$$ trơn sẽ không tự động đảo tốt bài toán có hệ số thấm dạng bàn cờ. Điều này phản ánh trực tiếp yêu cầu về độ trơn của phép tính ký hiệu trong chương.

### Ví dụ 3: Bộ nhân rời rạc

```python
import numpy as np

n = 128
k = np.fft.fftfreq(n) * n
symbol = 1.0 / (1.0 + k**2)
u = np.sin(2 * np.pi * np.arange(n) / n)
v = np.fft.ifft(symbol * np.fft.fft(u)).real
print(v.max(), v.min())
```

Đoạn mã trên biểu diễn một parametrix elliptic rời rạc cho toán tử $$I-\partial_{xx}$$ trên đường tròn. Trước khi so sánh với các mô hình phi tuyến nhiều lớp, một lớp phổ học được cần được kiểm chứng đối chiếu với đối tượng chuẩn này.

## Ứng dụng

Góc nhìn xem neural operator như ký hiệu học được giúp làm rõ nhiều bài toán thực tế. Các mô hình giả lập thời tiết và khí hậu dùng kiến trúc nền Fourier thực chất đang học một ký hiệu hiệu dụng cho hệ có hệ số biến thiên phức tạp; do đó, không nên kỳ vọng phép tích chập thuần túy có thể mô phỏng tốt địa hình nếu thiếu biến đổi tọa độ hoặc kênh phụ thuộc vị trí. Các bài toán ngược cho phương trình elliptic và Helmholtz có thể hiểu như nỗ lực học parametrix từ dữ liệu. Tương tự, khử mờ ảnh với hàm lan truyền điểm (PSF) đã biết chính là bài toán đảo bộ nhân Fourier, và một mạng nơ-ron bỏ qua cấu trúc ký hiệu có nguy cơ học lại một bộ lọc Wiener kém hiệu quả hơn.

Cách tiếp cận này cũng kết nối trực tiếp Chương 08 (chuỗi Fourier) và Chương 12 (không gian hàm): một ký hiệu thuộc $$S^{m}$$ ánh xạ $$H^{s}$$ vào $$H^{s-m}$$. Do đó, một toán tử học được dùng để nghịch đảo toán tử elliptic bậc hai cần cải thiện độ chính quy Sobolev thêm khoảng hai bậc đạo hàm — đây là một tính chất có thể đo đạc và kiểm chứng được.

## Thách thức và hướng mở rộng

Các lớp phi tuyến nằm ngoài khuôn khổ phép tính ΨDO tuyến tính. Những bài toán có hệ số biến thiên hoặc đặt trên đa tạp đòi hỏi ký hiệu đầy đủ $$a(x,\xi)$$ thay vì chỉ $$a(\xi)$$. Ngoài ra, aliasing rời rạc có thể tạo ra sai số tưởng như nhỏ trong chuẩn $$L^2$$ nhưng lại lớn trong chuẩn $$H^{s}$$. Việc học parametrix từ dữ liệu cũng không tự động cung cấp các ước lượng phần dư chặt chẽ như lý thuyết Hörmander. Trên đa tạp cong, biến đổi Fourier nhanh (FFT) không còn là công cụ giải tích điều hòa phù hợp; khi đó cần đến các dạng tương tự trên mặt cầu hoặc phương pháp phần tử phổ.

Câu hỏi suy ngẫm: nếu hai ký hiệu học được trùng khớp ở tần số cao và chỉ sai khác nhau một hàm Schwartz, liệu chúng có xác định cùng một toán tử modulo toán tử làm trơn hay không? Câu trả lời theo lý thuyết của chương là có, và đó cũng là lý do kiểm tra hành vi ở tần số cao là phép thử cốt lõi.

## Video tham khảo

- Nên xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Fourier neural operator như một bộ nhân Fourier học được, tương ứng về mặt số học với khái niệm ký hiệu.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. DeepONet học toán tử trực tiếp từ dữ liệu mà không cần viết ký hiệu tường minh.
- [Ps d o’s lecture 1 (Xuwen Zhu)](https://www.youtube.com/watch?v=kP9sxwBJQv4) — Mathematics video VAROQUI Hervé, tiếng Việt. Bài giảng về ký hiệu giả vi phân cổ điển mà các lớp mạng trên đang mô phỏng theo nghĩa mở rộng.

## Bài tập

1. **Cấp của bộ nhân.** Chứng minh $$a(\xi)=(1+|\xi|^2)^{m/2}$$ thuộc lớp $$S^{m}$$. Từ đó suy ra toán tử nghịch đảo học được của $$I-\Delta$$ phải có cấp bao nhiêu?

2. **Phần dư hợp thành.** Với hai ký hiệu không phụ thuộc $$x$$ (chẳng hạn ký hiệu hướng kính) $$a,b$$, tích $$ab$$ là ký hiệu chính xác của phép hợp thành. Làm thế nào để kiểm nghiệm tính chất này trên một mô hình FNO tuyến tính hai lớp?

3. **Aliasing.** Xây dựng một ví dụ một chiều trong đó bộ nhân trên lưới cỡ chẵn đồng nhất tần số $$k$$ với $$k-n$$. Giải thích vì sao toán tử thu được không phải là rời rạc hóa nhất quán của một bộ nhân liên tục thuộc $$S^{0}$$.

4. **Thí nghiệm tính toán.** Huấn luyện một lớp phổ tuyến tính để nghịch đảo toán tử $$I-\partial_{xx}$$ trên đường tròn và vẽ đồ thị so sánh ký hiệu học được với $$(1+k^2)^{-1}$$. Sau đó, đánh giá cả hai toán tử trên các hàm sin tần số cao nằm ngoài dải huấn luyện.

5. **Khám phá mở.** Đọc bài báo của Bartolucci và cộng sự (NeurIPS 2023) hoặc Fanaskov và Oseledets (2022) và viết một trang phân tích mối liên hệ giữa tính “tương đương biểu diễn” với phát biểu rằng ΨDO được định nghĩa độc lập với lưới rời rạc.

## Tài liệu

- Trèves; Shubin; Taylor.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Fanaskov, V., và Oseledets, I. “Spectral neural operators.” 2022. [arXiv:2205.10573](https://arxiv.org/abs/2205.10573).
- Bartolucci, F., và cộng sự. “Representation equivalent neural operators.” *NeurIPS* 2023. [arXiv:2305.19913](https://arxiv.org/abs/2305.19913).
- Raonić, B., và cộng sự. “Convolutional neural operators.” *ICLR* 2024. [arXiv:2302.01178](https://arxiv.org/abs/2302.01178).
- Li, Z., và cộng sự. “Fourier neural operator.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
