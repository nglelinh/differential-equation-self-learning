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

## Mục tiêu

Bài tùy chọn này đọc Fourier neural operator, spectral neural operator và các kiến trúc 2022–2024 liên quan như họ hàng tính toán của toán tử giả vi phân. Sinh viên cần khớp nhân tử Fourier học được với ký hiệu trong $$S^m$$, giải thích học toán tử không alias bằng ngôn ngữ Hörmander, và thấy parametrix elliptic như mô hình giải tích cho nghịch đảo học được. Phép tính ký hiệu của chương không bị viết lại.

## Kiến thức nền

Sinh viên cần biết nhân tử Fourier, lớp ký hiệu, hợp thành ΨDO, và ý niệm parametrix elliptic. Bài ôn chuẩn bị về nhân tử là khởi động dự kiến.

## Dẫn nhập

Toán tử giả vi phân cổ điển, ở xấp xỉ đầu, là nhân tử Fourier có ký hiệu $$a(x,\xi)$$ biến thiên chậm theo $$x$$ và tuân chặn đạo hàm theo $$\xi$$. Lớp Fourier neural operator là nhân tử Fourier có ký hiệu là mảng huấn luyện $$R_\xi$$, theo sau bởi phi tuyến từng điểm. Phép loại suy không hoàn hảo — phi tuyến và dải hữu hạn đưa ta ra ngoài phép tính ΨDO tuyến tính — nhưng đó là phép loại suy đúng. Nó giải thích vì sao FNO làm việc trên bài elliptic và parabolic bất biến tịnh tiến, vì sao nó khó với hệ số thô, và vì sao aliasing là vấn đề vi cục bộ chứ không chỉ số.

Kovachki và cộng sự (*JMLR* 2023) đã mô tả FNO như họ toán tử tích phân tham số hóa với nhân bất biến tịnh tiến. Fanaskov và Oseledets (*Spectral Neural Operators*, 2022–2023; [arXiv:2205.10573](https://arxiv.org/abs/2205.10573)) làm phép tính phổ còn tường minh hơn. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra và Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023; [arXiv:2305.19913](https://arxiv.org/abs/2305.19913)) cho khung học toán tử không alias: mô hình rời rạc phải là hạn chế đúng của toán tử liên tục, không phải ánh xạ lưới tình cờ. Raonić, Molinaro, Rohner, Mishra và de Bézenac (*Convolutional Neural Operators*, ICLR 2024; [arXiv:2302.01178](https://arxiv.org/abs/2302.01178)) theo đuổi nhân tích chập nhất quán liên tục.

Những bài ấy trở nên dễ hơn một khi đã thấy $$S^m_{\rho,\delta}$$ và xây dựng parametrix. Nghịch đảo học được của toán tử elliptic là nỗ lực xây parametrix từ dữ liệu.

## Khái niệm then chốt

### Ký hiệu và nhân tử học được

Toán tử $$Au=\mathcal{F}^{-1}\bigl(a(\xi)\hat u(\xi)\bigr)$$ là trường hợp hệ số hằng của ΨDO cấp $$m$$ khi $$a\in S^m$$. Lớp FNO cụt $$a$$ về hộp tần số thấp và cho nó phụ thuộc kênh. Huấn luyện $$a$$ trên cặp $$(u,Au)$$ là nhận dạng ký hiệu. Nếu toán tử mục tiêu là $$(-\Delta+1)^{-1}$$, ký hiệu học được phải trông như $$(|\xi|^2+1)^{-1}$$ trên dải đã phân giải và không được tăng như lũy thừa dương của $$|\xi|$$.

### Hợp thành và xếp lớp

Định lý hợp thành nói ký hiệu của $$AB$$ là $$a\#b=ab$$ cộng số hạng cấp thấp. Xếp lớp FNO tuyến tính không phi tuyến vì thế là tích ký hiệu rời rạc. Kích hoạt phi tuyến giữa các lớp đưa ta ra ngoài phép tính, vừa là nguồn khả năng biểu diễn vừa là nguồn aliasing: tích từng điểm của hai hàm giới hạn dải không giới hạn dải.

### Parametrix elliptic như nghịch đảo học được

Nếu $$A$$ elliptic, tồn tại ΨDO $$B$$ sao cho $$BA-I$$ và $$AB-I$$ làm mượt. Nghịch đảo nơ-ron ánh xạ $$Au$$ về $$u$$ trừ lỗi trơn đang hiện thực hóa câu ấy bằng số. Do đó ta nên thử nghịch đảo học được trên đầu vào dao động mạnh: ký hiệu tần số cao phải đảo ký hiệu chính, trong khi phần tần số thấp có thể học tự do hơn, cũng như parametrix chỉ duy nhất modulo toán tử làm mượt.

### Aliasing như lượng tử hóa sai

Ánh xạ lưới gập mode cao lên mode thấp không phải ΨDO cấp dự kiến; nó là toán tử khác. Kiến trúc tương đương biểu diễn đòi đổi lưới không đổi toán tử, liên tục đang được rời rạc hóa. Đó là dạng tính toán của tuyên bố rằng ΨDO được định nghĩa trên hàm, không trên mảng.

## Phương pháp và kỹ thuật

1. Xác định ký hiệu chính ứng viên (hành động tần số cao).
2. Kiểm suy giảm hoặc tăng của nhân tử học được đối chiếu lớp $$S^m$$.
3. Thử hợp thành: nghịch đảo học được của toán tử thuận học được có trông như đồng nhất modulo phần dư làm mượt không?
4. Tinh lưới. Nếu toán tử đổi bản sắc, nó chưa bao giờ là ΨDO liên tục.
5. Với hệ số biến thiên, hỏi kiến trúc có biểu diễn được ký hiệu phụ thuộc $$x$$ là $$a(x,\xi)$$ hay chỉ một tích chập.

Geo-FNO và convolutional neural operator là nỗ lực khôi phục phụ thuộc $$x$$ và bất biến hình học trong khi giữ nhân liên tục.

## Ví dụ

### Ví dụ 1: Ký hiệu thế Bessel

Toán tử $$(I-\Delta)^{-s/2}$$ có ký hiệu $$(1+|\xi|^2)^{-s/2}\in S^{-s}$$. Lớp phổ tuyến tính từng huấn luyện trên ánh xạ này phải tái tạo profile kính ấy. Vẽ $$|R_\xi|$$ theo $$|\xi|$$ trên thang log-log là bài tập lớp ký hiệu.

### Ví dụ 2: Thất bại trên hệ số thô

Toán tử $$-\operatorname{div}(a(x)\nabla\cdot)$$ chỉ là ΨDO cấp $$2$$ nếu $$a$$ đủ trơn. Nếu $$a$$ chỉ bị chặn và elliptic, toán tử vẫn đặt chỉnh trong $$H^1$$ nhưng không còn là ΨDO cổ điển kiểu sách. FNO huấn luyện trên $$a$$ trơn sẽ không tự đảo độ thấm bàn cờ. Lời nhắc của chương rằng phép tính ký hiệu cần độ trơn là lời giải thích.

### Ví dụ 3: Nhân tử rời rạc

```python
import numpy as np

n = 128
k = np.fft.fftfreq(n) * n
symbol = 1.0 / (1.0 + k**2)
u = np.sin(2 * np.pi * np.arange(n) / n)
v = np.fft.ifft(symbol * np.fft.fft(u)).real
print(v.max(), v.min())
```

Đây là parametrix elliptic rời rạc cho $$I-\partial_{xx}$$ trên đường tròn. Lớp phổ học được phải so với đối tượng này trước khi so với chồng phi tuyến sâu.

## Ứng dụng

Nghĩ neural operator như ký hiệu học được làm rõ vài ứng dụng. Bộ giả lập thời tiết và khí hậu dùng xương sống Fourier đang học ký hiệu hiệu dụng cho hệ số biến thiên khổng lồ; ta không nên kỳ vọng tích chập thuần bắt địa hình nếu không có biến dạng hoặc kênh phụ thuộc vị trí. Bài elliptic và Helmholtz ngược là nỗ lực học parametrix từ dữ liệu. Khử mờ ảnh với hàm trải điểm đã biết đúng là đảo nhân tử Fourier, và mạng bỏ qua ký hiệu sẽ phát minh lại bộ lọc Wiener kém hơn.

Cùng góc nhìn nối Chương 08 (chuỗi Fourier) và Chương 12 (không gian hàm): ký hiệu trong $$S^{m}$$ ánh xạ $$H^{s}$$ sang $$H^{s-m}$$. Toán tử học được tuyên bố nghịch đảo elliptic vì thế phải cải thiện chính quy Sobolev khoảng hai đạo hàm — tuyên bố đo được.

## Thách thức và hướng mở rộng

Lớp phi tuyến rời phép tính ΨDO. Bối cảnh hệ số biến thiên và đa tạp cần ký hiệu đầy đủ $$a(x,\xi)$$, không chỉ $$a(\xi)$$. Aliasing rời rạc có thể sinh lỗi compact trông nhỏ trong $$L^2$$ và lớn trong $$H^{s}$$. Học parametrix từ dữ liệu không tự cho ước lượng phần dư mà lý thuyết Hörmander cung cấp. Trên đa tạp, FFT là giải tích điều hòa sai; analogue cầu và phổ-phần tử là bắt buộc.

Câu hỏi phản tư: nếu hai ký hiệu học được khớp ở tần số cao nhưng lệch một hàm Schwartz, chúng có định nghĩa cùng toán tử modulo làm mượt không? Câu trả lời của chương là có, và đó là vì sao phép thử tần số cao là phép thử đúng.

## Bài tập

1. **Cấp của nhân tử.** Chỉ ra $$a(\xi)=(1+|\xi|^2)^{m/2}$$ nằm trong $$S^{m}$$. Nghịch đảo học được của $$I-\Delta$$ phải có cấp nào?

2. **Phần dư hợp thành.** Với hai ký hiệu kính $$a,b$$, tích $$ab$$ là ký hiệu hợp thành đúng. Làm sao thử FNO tuyến tính hai lớp đối chiếu sự thật này?

3. **Aliasing.** Cho ví dụ một chiều trong đó nhân tử lưới cỡ chẵn đồng nhất $$k$$ với $$k-n$$. Vì sao toán tử sinh ra không phải rời rạc hóa nhất quán của nhân tử liên tục trong $$S^{0}$$?

4. **Thí nghiệm tính toán.** Huấn luyện lớp phổ tuyến tính để đảo $$I-\partial_{xx}$$ trên đường tròn và vẽ ký hiệu học được đối chiếu $$(1+k^2)^{-1}$$. Rồi đánh giá cả hai toán tử trên sin tần số cao không nằm trong dải huấn luyện.

5. **Khám phá mở.** Đọc Bartolucci và cộng sự (NeurIPS 2023) hoặc Fanaskov và Oseledets (2022) và viết một trang dịch “tương đương biểu diễn” thành tuyên bố rằng ΨDO được định nghĩa độc lập với lưới.

## Tài liệu

- Trèves; Shubin; Taylor.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Fanaskov, V., và Oseledets, I. “Spectral neural operators.” 2022. [arXiv:2205.10573](https://arxiv.org/abs/2205.10573).
- Bartolucci, F., và cộng sự. “Representation equivalent neural operators.” *NeurIPS* 2023. [arXiv:2305.19913](https://arxiv.org/abs/2305.19913).
- Raonić, B., và cộng sự. “Convolutional neural operators.” *ICLR* 2024. [arXiv:2302.01178](https://arxiv.org/abs/2302.01178).
- Li, Z., và cộng sự. “Fourier neural operator.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
