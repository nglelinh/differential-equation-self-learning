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

Mạng tích chập CNN truyền thống chỉ nhìn thấy các điểm ảnh lân cận trong cửa sổ $3 \times 3$—và nếu huấn luyện trên lưới $64 \times 64$ thì khi đổi sang lưới $256 \times 256$, mạng vỡ hoàn toàn. **Fourier Neural Operator (FNO)** (Li et al., 2021) đã tạo nên cuộc cách mạng trong AI mô phỏng vật lý bằng đúng một định lý Chương 8: **tích chập toàn cục trong không gian chính là phép nhân từng điểm trong miền tần số Fourier**!

## Kiến thức cần nhớ: Bốn trụ cột của Fourier Neural Operator (FNO)

1. **Định lý Tích chập Fourier ($\mathcal{F}\{K * v\} = \mathcal{F}\{K\} \cdot \mathcal{F}\{v\}$)**:
   Mỗi lớp Fourier trong FNO chạy FFT đưa tín hiệu sang miền tần số, **nhân tuyến tính** trên $k_{\max}$ tần số thấp nhất (bộ lọc toàn cục!), rồi chạy Inverse FFT (iFFT) quay về miền không gian—tốn chỉ $O(N\log N)$!
2. **Bất biến độ phân giải (Zero-Shot Super-Resolution)**:
   Vì trọng số học nằm trên các **mode tần số** (không gắn cứng vào kích thước pixel lưới), một mô hình FNO huấn luyện trên lưới thô $64 \times 64$ có thể suy luận thẳng trên lưới siêu mịn $256 \times 256$ mà không cần huấn luyện lại!
3. **Cắt cụt tần số cao (Low-Pass Spectral Truncation)**:
   Hầu hết năng lượng của dòng chảy chất lỏng (Navier–Stokes), khí tượng và truyền nhiệt tập trung ở các tần số thấp; giữ $k_{\max} = 12\text{–}32$ mode giúp mạng nhẹ, ít overfitting và chạy nhanh hơn bộ giải PDE truyền thống tới $1.000\times$.
4. **Ứng dụng thực chiến (FourCastNet / Dự báo thời tiết toàn cầu)**:
   Dự báo khí quyển toàn cầu 1 tuần chỉ trong vài giây thay vì hàng giờ trên siêu máy tính!

## Mục tiêu

Bài tùy chọn này kết nối chuỗi Fourier, đẳng thức Parseval và bước chuyển từ chuỗi sang biến đổi Fourier với kiến trúc Fourier neural operator (FNO) cùng các mở rộng giai đoạn 2022–2024. Sau bài học, sinh viên có thể hiểu một lớp FNO như một phép nhân phổ có tham số học được, giải thích tính bất biến theo độ phân giải rời rạc bằng ngôn ngữ của chương này, và nhận ra hiện tượng chồng phổ (aliasing) có cùng bản chất với hiện tượng xuất hiện trong khai triển lượng giác cắt cụt. Các kết quả cổ điển về sự hội tụ của chuỗi Fourier vẫn giữ nguyên vai trò nền tảng.

## Kiến thức nền

Sinh viên cần nắm chuỗi Fourier lượng giác và phức, phép mở rộng chẵn và lẻ, định lý Parseval, cũng như ý tưởng hình thức của biến đổi Fourier như phiên bản liên tục của các hệ số $$c_n$$.

## Dẫn nhập

Chuỗi Fourier biểu diễn một hàm tuần hoàn qua một tập rời rạc các họa âm. Một nhân tử Fourier (Fourier multiplier) tác động lên các họa âm đó theo quy tắc $$c_n\mapsto m_n c_n$$. Lý thuyết PDE cổ điển sử dụng cơ chế này thường xuyên: phép đạo hàm trở thành phép nhân với $$in$$, còn toán tử vi phân hệ số hằng tương ứng với một biểu tượng phổ (symbol). Li, Kovachki, Azizzadenesheli, Liu, Bhattacharya, Stuart và Anandkumar (*Fourier Neural Operator for Parametric Partial Differential Equations*, ICLR 2021; [arXiv:2010.08895](https://arxiv.org/abs/2010.08895)) đã biến nhân tử đó thành tham số có thể học được. Mỗi lớp FNO thực hiện biến đổi Fourier, nhân một tensor phức huấn luyện được trên một dải mode tần số thấp, biến đổi ngược về miền không gian rồi cộng thêm thành phần phi tuyến cục bộ.

Công trình trên *JMLR* năm 2023 của Kovachki và cộng sự chứng minh rằng các mạng toán tử (neural operator) dạng này có thể xấp xỉ các ánh xạ liên tục giữa các không gian hàm, đồng thời dùng chung một bộ tham số trên nhiều độ phân giải lưới khác nhau. Pathak và cộng sự (*FourCastNet*, 2022; [arXiv:2202.11214](https://arxiv.org/abs/2202.11214)) sử dụng kiến trúc nền tảng kiểu FNO cho dự báo thời tiết toàn cầu. Li, Huang, Huang và Anandkumar (*Fourier Neural Operator with Learned Deformations*, *J. Comput. Phys.* 2023) mở rộng phương pháp cho các miền hình học không đều. Bonev, Kurth, Hundt, Kossaifi, Kashinath và Anandkumar (*Spherical Fourier Neural Operators*, ICML 2023) thay thế biến đổi FFT phẳng bằng hàm điều hòa cầu để giữ đúng cấu trúc giải tích Fourier trên mặt cầu.

Kiến thức của Chương 08 giúp đọc hiểu trực tiếp các công trình này. Một lớp FNO thực chất là sự kết hợp giữa khai triển Fourier cắt cụt, biểu tượng phổ học được và phép biến đổi phi tuyến cục bộ.

### Giải thích: Tính tay tốc độ của 1 lớp FNO so với tích chập toàn cục trực tiếp trên lưới 1D cỡ $N = 1.024$

- **Tích chập toàn cục trực tiếp trong miền không gian** (mọi điểm tương tác với mọi điểm): $N^2 = 1.024^2 = \mathbf{1.048.576}$ phép nhân!
- **Một lớp FNO với $k_{\max} = 16$ mode tần số**:
  1. FFT xuôi: $\sim N \log_2 N = 1.024 \times 10 = 10.240$ phép tính.
  2. Nhân trọng số trên $16$ mode tần số thấp: chỉ **$16$** phép nhân phức (bỏ qua 1.008 mode tần số cao!).
  3. iFFT ngược: $10.240$ phép tính.
  - **Tổng cộng**: $\approx \mathbf{20.496}$ phép tính — nhanh hơn hơn **$51\times$** ngay ở 1D (và nhanh hơn hàng chục nghìn lần ở 2D/3D!).

## Khái niệm then chốt

### Biểu tượng phổ học được

Một nhân tử tuần hoàn vô hướng được xác định bởi dãy $$m_n$$. Trong lớp FNO, dãy này được thay bằng biểu tượng phổ dạng ma trận $$R_n$$ tác động lên vectơ kênh. Sinh viên đã quen với chuỗi phức $$u=\sum c_n e^{inx}$$ đã nắm rõ cả ánh xạ thuận và ngược. Điểm mới là các ma trận $$R_n$$ được huấn luyện từ các cặp hàm đầu vào–đầu ra, giúp lớp mạng xấp xỉ toàn bộ toán tử nghiệm thay vì chỉ một PDE tuyến tính riêng lẻ.

### Định lý Parseval và năng lượng mode

Định lý Parseval khẳng định năng lượng trong không gian $$L^2$$ bằng tổng năng lượng $$\ell^2$$ của các hệ số Fourier. Đây là cơ sở trực tiếp để điều chuẩn (regularize) mô hình FNO: đặt phạt lên phần đuôi tần số cao, theo dõi tốc độ suy giảm phổ và tránh đánh giá sai các mô hình có năng lượng dồn vào phần chồng phổ chưa được phân giải. Các mô hình thời tiết như FourCastNet phụ thuộc chặt chẽ vào việc bảo toàn thác năng lượng qua các thang đo — một yêu cầu vừa thuộc về định lý Parseval vừa thuộc về khí tượng học.

### Chồng phổ (aliasing), cắt cụt và hiện tượng Gibbs

Biến đổi FFT hữu hạn về bản chất là một chuỗi Fourier cắt cụt trên lưới rời rạc. Các mode vượt quá tần số Nyquist sẽ bị gập lại vào dải tần thấp (aliasing), tương tự cách đa thức lượng giác cắt cụt làm méo dạng bước nhảy. Bartolucci, de Bézenac, Raonić, Molinaro, Mishra và Alaifari (*Representation Equivalent Neural Operators*, NeurIPS 2023) phân tích điều kiện để một neural operator rời rạc thực sự là phép rời rạc hóa nhất quán của toán tử liên tục thay vì chỉ là một ánh xạ phụ thuộc vào lưới. Hiện tượng Gibbs từng xuất hiện trong ví dụ sóng vuông của chương này cũng tái hiện mỗi khi FNO phải xấp xỉ các trường gián đoạn hoặc các lớp biên có độ dốc lớn.

### Từ chuỗi Fourier đến biến đổi Fourier

Bài tùy chọn trước đó của chương đã trình bày bước chuyển từ hệ số rời rạc sang biến đổi Fourier. FNO trên hình xuyến (torus) lớn chính là phiên bản tính toán của bước chuyển đó: FFT đóng vai trò phép biến đổi, dải mode học được tương ứng với biểu tượng phổ có giá compact, và FFT ngược đưa kết quả trở lại miền không gian. Trên mặt cầu, phép biến đổi thích hợp là biến đổi điều hòa cầu, và đó là cơ sở ra đời của SFNO.

## Phương pháp và kỹ thuật

1. Lấy mẫu hàm đầu vào $$a$$ (hệ số phương trình, điều kiện đầu hoặc hàm nguồn) từ một phân bố xác định.
2. Tính nghiệm tham chiếu $$u=\mathcal{G}(a)$$ bằng bộ giải số cổ điển.
3. Huấn luyện các lớp nhân tử Fourier xếp chồng sao cho $$\mathcal{G}_\theta(a)\approx u$$ theo chuẩn $$L^2$$ hoặc chuẩn Sobolev $$H^s$$.
4. Đánh giá mô hình trên lưới mịn hơn lưới huấn luyện để kiểm chứng tính bất biến theo độ phân giải rời rạc.
5. Kiểm tra các biểu tượng phổ học được $$R_n$$: với bài toán tuyến tính hệ số hằng, chúng cần tiệm cận biểu tượng phổ chính xác của toán tử nghịch đảo.

Các biến thể xử lý hình học phức tạp bổ sung phép biến dạng học được (Geo-FNO) hoặc chuyển sang họ hàm điều hòa khác (SFNO). Trong mọi trường hợp, câu hỏi thiết kế cốt lõi vẫn là câu hỏi của chương này: hệ hàm trực giao nào tương thích với miền bài toán?

## Ví dụ

### Ví dụ 1: Phép đạo hàm dưới góc nhìn lớp FNO

Phép lấy đạo hàm trên đường tròn tương ứng với nhân tử $$m_n=in$$. Một lớp FNO đơn kênh không có hàm kích hoạt phi tuyến cần khôi phục lại dãy hệ số này nếu được huấn luyện trên đủ nhiều cặp hàm trơn $$(u,u')$$. Việc vẽ đồ thị $$\operatorname{Im}(R_n)$$ theo $$n$$ là một bài tập kiểm chứng trực tiếp về hệ số Fourier.

### Ví dụ 2: Sóng vuông như phép thử giới hạn

Chuỗi Fourier của sóng vuông hội tụ chậm và xuất hiện hiện tượng vượt biên độ tại điểm nhảy. Một mô hình FNO chỉ huấn luyện trên dữ liệu trơn sẽ khó tái tạo đúng phần đuôi phổ này. Cách khắc phục thực tế là bổ sung các mẫu có tính gián đoạn vào tập huấn luyện hoặc sử dụng cơ sở hàm thích nghi tốt hơn với bước nhảy.

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

Một lớp FNO vận hành theo đúng cấu trúc của đoạn mã trên, trong đó nhân tử cố định $$1j k$$ được thay bằng mảng trọng số phức có thể huấn luyện, kết hợp thêm nhiều kênh đặc trưng và hàm kích hoạt phi tuyến.

## Ứng dụng

FNO và các kiến trúc mở rộng được ứng dụng làm mô hình thay thế (surrogate model) cho phương trình Navier–Stokes, dòng chảy Darcy và mô phỏng thời tiết–khí hậu. FourCastNet (2022) cho thấy kiến trúc nền Fourier sau khi huấn luyện có thể tạo dự báo thời tiết toàn cầu hạn trung nhanh hơn nhiều bậc độ lớn so với các mô hình hoàn lưu chung (GCM) truyền thống. Spherical FNO (2023) mở rộng ý tưởng này theo đúng hình học cầu cho dữ liệu hành tinh. Trong kỹ thuật, các nhân tử Fourier học được còn được dùng để xây dựng bản sao số (digital twin) theo thời gian thực cho các hệ thống tuần hoàn hoặc đồng nhất thống kê.

Phép mở rộng chẵn và lẻ của chương cũng xuất hiện trong các cài đặt hiện đại: điều kiện biên trên đoạn hữu hạn thường được tích hợp bằng cách dùng biến đổi sin hoặc biến đổi cos rời rạc thay cho FFT phức đầy đủ, tương ứng trực tiếp với khai triển nửa khoảng.

## Thách thức và hướng mở rộng

FNO giả định miền hình học hỗ trợ FFT hoặc biến đổi điều hòa cầu. Các miền biến dạng phức tạp, có vết nứt hoặc dùng lưới không cấu trúc đòi hỏi cơ chế bổ sung. Những biểu tượng phổ phi cục bộ có tốc độ suy giảm chậm cần giữ lại nhiều mode tần số cao, tạo ra sự đánh đổi giữa bộ nhớ GPU và độ chính xác. Ngoài ra, lớp phi tuyến đặt sau phép biến đổi ngược có thể đưa trở lại hiện tượng chồng phổ (aliasing) mà một bộ giải phổ tuyến tính thuần túy vốn loại bỏ được. Cuối cùng, mô hình huấn luyện trên một phân bố dữ liệu đầu vào không tự động tổng quát hóa sang phân bố khác; cấu trúc Fourier không thay thế được tập dữ liệu huấn luyện phù hợp.

Câu hỏi suy ngẫm: nếu biểu tượng phổ học được $$R_n$$ không bị chặn khi $$\lvert n\rvert$$ tăng, liệu toán tử học được có còn liên tục trên $$L^2$$ hay không? Định lý Parseval cùng tiêu chuẩn nhân tử bị chặn sẽ gợi mở câu trả lời.

## Video tham khảo

- Xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu trực quan kiến trúc Fourier neural operator được trình bày trong bài.
- [But what is the Fourier Transform?  A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, tiếng Anh. Ôn lại biến đổi Fourier cổ điển làm nền cho các mode trong lớp toán tử.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Giới thiệu DeepONet, một kiến trúc học toán tử song song với FNO.

## Bài tập

1. **Nhân tử Helmholtz.** Viết biểu tượng phổ của toán tử $$(-\Delta+\kappa^2)^{-1}$$ trên đường tròn. Bạn sẽ chọn giữ lại bao nhiêu mode tần số thấp trong lớp FNO và vì sao?

2. **Kiểm chứng định lý Parseval.** Sau khi huấn luyện một mô hình FNO cỡ nhỏ, hãy tính chuẩn $$L^2$$ của hàm dự đoán và chuẩn $$\ell^2$$ của các hệ số Fourier tương ứng. Hai đại lượng này cần thỏa mãn quan hệ gì?

3. **Lựa chọn khai triển nửa khoảng.** Giả sử bài toán yêu cầu điều kiện biên Dirichlet trên $$[0,L]$$. Nên thay FFT bằng biến đổi sin hay biến đổi cos, và lựa chọn đó thể hiện trong cài đặt mã nguồn như thế nào?

4. **Thí nghiệm tính toán.** Cài đặt một lớp nhân tử Fourier tuyến tính đơn lẻ và huấn luyện ánh xạ $$u \mapsto u_{xx}$$ trên đường tròn. Vẽ đồ thị biểu tượng phổ học được và đối chiếu với $$-n^2$$.

5. **Tìm hiểu mở rộng.** Đọc bài báo của Li và cộng sự (ICLR 2021) cùng FourCastNet (2022) hoặc Bonev và cộng sự (ICML 2023). Viết một trang phân tích xem yếu tố Fourier nào — tính tuần hoàn, hàm điều hòa cầu hay phép biến dạng học được — đóng vai trò cốt lõi trong bài báo đó.

## Tài liệu

- Haberman, Chương 3; Evans, phụ lục chuỗi Fourier.
- Li, Z., và cộng sự. “Fourier neural operator for parametric PDEs.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Pathak, J., và cộng sự. “FourCastNet.” 2022. [arXiv:2202.11214](https://arxiv.org/abs/2202.11214).
- Bonev, B., và cộng sự. “Spherical Fourier neural operators.” *ICML* 2023. [arXiv:2306.03838](https://arxiv.org/abs/2306.03838).
- Li, Z., Huang, D. Z., Huang, B., và Anandkumar, A. “Fourier neural operator with learned deformations.” *J. Comput. Phys.* 498 (2023): 112666.
