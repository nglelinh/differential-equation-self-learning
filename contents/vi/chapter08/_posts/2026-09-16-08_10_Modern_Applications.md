---
layout: post
title: "08-10 Ứng dụng hiện đại: Fourier neural operator"
chapter: '08'
order: 10
owner: Course Team
lang: vi
categories:
- chapter08
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này lấy chuỗi Fourier, đồng nhất thức Parseval và bước từ chuỗi sang biến đổi rồi đặt chúng dưới Fourier neural operator cùng các hậu duệ 2022–2024. Sinh viên cần đọc một lớp FNO như nhân tử Fourier học được, giải thích bất biến rời rạc hóa bằng ngôn ngữ chương này, và thấy aliasing như cùng hiện tượng đã xuất hiện trong khai triển lượng giác cụt. Lý thuyết hội tụ chuỗi Fourier không bị viết lại.

## Kiến thức nền

Sinh viên cần biết chuỗi Fourier lượng giác và phức, thác chẵn/lẻ, định lý Parseval, và ý formal của biến đổi Fourier như analogue liên tục của hệ số $$c_n$$.

## Dẫn nhập

Chuỗi Fourier biểu diễn hàm tuần hoàn bằng một tập rời rạc các điều hòa. Nhân tử Fourier tác động trên các điều hòa ấy bằng $$c_n\mapsto m_n c_n$$. Lý thuyết PDE cổ điển dùng thiết bị này liên tục: đạo hàm thành nhân $$in$$, và toán tử hệ số hằng thành một ký hiệu. Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart và Anandkumar (*Fourier Neural Operator for Parametric Partial Differential Equations*, ICLR 2021; [arXiv:2010.08895](https://arxiv.org/abs/2010.08895)) làm nhân tử học được. Mỗi lớp FNO tính biến đổi Fourier, nhân một tensor phức huấn luyện được trên một dải mode thấp, đảo biến đổi, và cộng phần dư phi tuyến địa phương.

Bài JMLR 2023 của Kovachki và cộng sự chứng minh các neural operator ấy có thể xấp xỉ ánh xạ liên tục giữa không gian hàm và cùng tham số dùng được ở nhiều độ phân giải. Pathak và cộng sự (*FourCastNet*, 2022; [arXiv:2202.11214](https://arxiv.org/abs/2202.11214)) dùng xương sống kiểu FNO cho dự báo thời tiết toàn cầu. Li, Huang, Huang và Anandkumar (*Fourier Neural Operator with Learned Deformations*, *J. Comput. Phys.* 2023) thích nghi ý tưởng cho hình học không đều. Bonev, Kurth, Hundt, Kossaifi, Kashinath và Anandkumar (*Spherical Fourier Neural Operators*, ICML 2023) thay FFT phẳng bằng hàm điều hòa cầu, đúng lý thuyết Fourier trung thực trên mặt cầu.

Chương này là lý do những bài ấy đọc được. Lớp FNO không phải khối attention bí ẩn; nó là khai triển Fourier cụt cộng ký hiệu học được cộng ánh xạ phi tuyến.

## Khái niệm then chốt

### Ký hiệu học được

Nhân tử tuần hoàn vô hướng là dãy $$m_n$$. Lớp FNO dùng ký hiệu giá trị ma trận $$R_n$$ tác động trên vector kênh. Sinh viên đã viết chuỗi phức $$u=\sum c_n e^{inx}$$ đã biết các ánh xạ thuận và ngược. Điều mới là $$R_n$$ được huấn luyện từ cặp hàm, nên lớp có thể xấp xỉ toán tử nghiệm chứ không phải một PDE tuyến tính đơn.

### Parseval và năng lượng mode

Định lý Parseval nói năng lượng $$L^2$$ là năng lượng $$\ell^2$$ của hệ số. Đó là cách đúng để regularize FNO: phạt đuôi mode cao, giám sát suy giảm phổ, và từ chối ca ngợi mô hình có năng lượng nằm trong alias chưa phân giải. Mô hình thời tiết kiểu FourCastNet sống chết vì việc giữ đúng thác năng lượng qua các thang — câu hỏi Parseval không kém câu hỏi khí tượng.

### Aliasing, cụt, và Gibbs

FFT hữu hạn là chuỗi Fourier cụt trên lưới. Mode trên tần số Nyquist gập lại, đúng như đa thức lượng giác cụt xuyên tạc nhảy. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra và Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023) phân tích khi nào neural operator rời rạc là rời rạc hóa nhất quán của toán tử liên tục chứ không phải ánh xạ lưới tình cờ. Hiện tượng Gibbs, đã thấy ở ví dụ sóng vuông của chương, tái xuất mỗi khi FNO được yêu cầu học trường không liên tục hoặc lớp sắc.

### Từ chuỗi đến biến đổi

Bài tùy chọn cuối của chương đã đi từ hệ số rời rạc tới biến đổi Fourier. FNO trên torus lớn là phiên bản tính toán của bước ấy: FFT là biến đổi, dải mode học được là ký hiệu giá compact, và FFT ngược trả về hàm. Trên mặt cầu phải dùng biến đổi điều hòa cầu, vì thế SFNO tồn tại.

## Phương pháp và kỹ thuật

1. Lấy mẫu hàm đầu vào $$a$$ (hệ số, dữ liệu đầu, lực) từ một họ.
2. Tính nghiệm chuẩn $$u=\mathcal{G}(a)$$ bằng bộ giải cổ điển.
3. Huấn luyện các lớp nhân tử xếp chồng sao cho $$\mathcal{G}_\theta(a)\approx u$$ trong chuẩn $$L^2$$ hoặc $$H^s$$.
4. Thử ở độ phân giải mịn hơn lưới huấn luyện; thành công là bằng chứng bất biến rời rạc hóa.
5. Soi các ký hiệu học được $$R_n$$. Với mục tiêu hệ số hằng tuyến tính chúng phải giống ký hiệu thật của toán tử nghịch đảo.

Các biến thể nhận hình học chèn biến dạng học được (Geo-FNO) hoặc đổi họ điều hòa (SFNO). Trong mọi trường hợp, quyết định thiết kế là cùng quyết định chương này đã dạy: hệ trực giao nào khớp miền?

## Ví dụ

### Ví dụ 1: Đạo hàm như lớp FNO

Đạo hàm trên đường tròn là nhân tử $$m_n=in$$. Lớp FNO một kênh không phi tuyến phải lấy lại dãy này nếu huấn luyện trên đủ cặp trơn $$(u,u')$$. Vẽ $$\operatorname{Im}(R_n)$$ theo $$n$$ là bài tập hệ số Fourier trực tiếp.

### Ví dụ 2: Sóng vuông như phép thử căng

Chuỗi Fourier của sóng vuông hội tụ chậm và vượt tại nhảy. FNO chỉ huấn luyện trên đầu vào trơn sẽ không học đuôi ấy. Thêm vài mẫu không liên tục, hoặc chuyển sang cơ sở thích nghi nhảy hơn, là đáp ứng thực tiễn.

### Ví dụ 3: Nhân tử FFT trong NumPy

```python
import numpy as np

n = 256
x = np.linspace(0, 2 * np.pi, n, endpoint=False)
u = np.sin(3 * x) + 0.3 * np.cos(8 * x)
uhat = np.fft.rfft(u)
k = np.fft.rfftfreq(n, d=2 * np.pi / n) * 2 * np.pi
dudx = np.fft.irfft(1j * k * uhat, n=n)
print(np.max(np.abs(dudx - 3 * np.cos(3 * x) + 2.4 * np.sin(8 * x))))
```

Lớp FNO là đoạn mã này với $$1j k$$ được thay bằng mảng phức huấn luyện và thêm kênh cùng kích hoạt quanh nó.

## Ứng dụng

FNO và hậu duệ được dùng như surrogate cho Navier–Stokes, dòng Darcy, và giả lập thời tiết–khí hậu. FourCastNet (2022) cho thấy xương sống Fourier có thể sinh dự báo toàn cầu hạn vừa nhanh hơn GCM thông thường nhiều bậc sau khi huấn luyện. Spherical FNO (2023) làm cùng ý tưởng đúng hình học cho dữ liệu hành tinh. Trong kỹ thuật, nhân tử Fourier học được phục vụ như digital twin thời gian thực cho thiết bị tuần hoàn hoặc đồng nhất thống kê.

Thác chẵn/lẻ của chương cũng có tiếng vang hiện đại. Điều kiện biên trên khoảng thường được mã hóa bằng cách chọn biến đổi sin hoặc cos chứ không FFT phức đầy đủ, đúng như chọn khai triển nửa khoảng.

## Thách thức và hướng mở rộng

FNO giả định hình học có FFT hoặc biến đổi điều hòa cầu. Miền biến dạng, nứt gãy và lưới không cấu trúc cần máy móc thêm. Ký hiệu nonlocal suy giảm chậm đòi nhiều mode, rồi bộ nhớ GPU cạnh tranh với độ chính xác. Lớp phi tuyến sau biến đổi ngược tái nhập aliasing mà bộ giải phổ tuyến tính thuần sẽ lọc. Mô hình huấn luyện trên một họ thống kê đầu vào không nhất thiết tổng quát hóa sang họ khác; cấu trúc Fourier không thay độ đo huấn luyện đúng.

Câu hỏi phản tư: nếu ký hiệu học được $$R_n$$ không suy giảm, toán tử bạn đang học có thực sự liên tục trên $$L^2$$? Parseval cộng định lý nhân tử bị chặn gợi câu trả lời.

## Bài tập

1. **Nhân tử Helmholtz.** Viết ký hiệu của $$(-\Delta+\kappa^2)^{-1}$$ trên đường tròn. Bạn sẽ giữ bao nhiêu mode thấp trong lớp FNO, và vì sao?

2. **Kiểm toán Parseval.** Sau khi huấn luyện FNO đồ chơi, tính chuẩn $$L^2$$ của dự đoán và chuẩn $$\ell^2$$ của hệ số Fourier. Bạn phải thấy gì?

3. **Chọn nửa khoảng.** Bạn muốn điều kiện Dirichlet trên $$[0,L]$$. FFT nên được thay bằng khai triển sin hay cos, và lựa chọn ấy xuất hiện trong mã thế nào?

4. **Thí nghiệm tính toán.** Cài một lớp nhân tử Fourier tuyến tính đơn và huấn luyện nó ánh xạ $$u$$ sang $$u_{xx}$$ trên đường tròn. Vẽ ký hiệu học được đối chiếu $$-n^2$$.

5. **Khám phá mở.** Đọc Li và cộng sự (ICLR 2021) và FourCastNet (2022) hoặc Bonev và cộng sự (ICML 2023). Viết một trang về ý Fourier nào — tuần hoàn, điều hòa cầu, hay biến dạng học được — đang làm việc thật.

## Tài liệu

- Haberman, Chương 3; Evans, phụ lục chuỗi Fourier.
- Li, Z., và cộng sự. “Fourier neural operator for parametric PDEs.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Pathak, J., và cộng sự. “FourCastNet.” 2022. [arXiv:2202.11214](https://arxiv.org/abs/2202.11214).
- Bonev, B., và cộng sự. “Spherical Fourier neural operators.” *ICML* 2023. [arXiv:2306.03838](https://arxiv.org/abs/2306.03838).
- Li, Z., Huang, D. Z., Huang, B., và Anandkumar, A. “Fourier neural operator with learned deformations.” *J. Comput. Phys.* 498 (2023): 112666.
