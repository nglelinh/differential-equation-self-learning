---
layout: post
title: "00-13 Ứng dụng hiện đại: Nền tảng học máy khoa học"
chapter: '00'
order: 13
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: optional
---

## Mục tiêu

Bài học tùy chọn này kết nối ngôn ngữ giải tích, đại số tuyến tính và không gian hàm của Chương 00 với học máy khoa học (Scientific Machine Learning — SciML) giai đoạn 2022–2026. Sau bài học, sinh viên có thể nhìn nhận đạo hàm tự động như phiên bản tính toán của quy tắc dây chuyền, hiểu mạng nơ-ron như ánh xạ giữa các không gian Euclid hoặc không gian hàm, và giải thích vì sao tính tồn tại, tính duy nhất cùng tính đặt chỉnh vẫn đóng vai trò quyết định khi mô hình được học từ dữ liệu thay vì thiết lập hoàn toàn bằng tay.

## Kiến thức nền

Sinh viên cần nắm vững giới hạn, đạo hàm, giải tích nhiều biến, trị riêng và khái niệm chuẩn trên không gian định chuẩn hoặc không gian tích vô hướng. Bài học không yêu cầu kiến thức sâu về học sâu (deep learning); chỉ cần hiểu mạng nơ-ron là một họ hàm tham số hóa được huấn luyện bằng cách cực tiểu hóa hàm mất mát, trong đó gradient theo tham số được tính tự động.

## Dẫn nhập

Các công cụ cổ điển trong Chương 00 ban đầu được xây dựng để đặt nền móng chặt chẽ cho phương trình vi phân: tính liên tục phục vụ phép lấy giới hạn, đạo hàm mô tả tốc độ biến thiên, đại số tuyến tính giúp chéo hóa hệ phương trình, còn không gian hàm cho phép đo độ lớn và sai số của nghiệm. Hiện nay, chính những công cụ này đang định hình lĩnh vực học máy khoa học (SciML). Thay vì chỉ khớp đường cong qua một tập điểm rời rạc, các mô hình SciML hướng tới việc học quy luật động lực, toán tử nghiệm hoặc mô hình thay thế tôn trọng các ràng buộc vi phân.

Hai câu hỏi cụ thể minh họa rõ mối liên hệ này. Thứ nhất, nếu một mạng dư (residual network) là một hệ động lực rời rạc, điều gì xảy ra khi bước rời rạc tiến về $$ 0 $$ và kiến trúc mạng trở thành một trường vector liên tục? Thứ hai, nếu một PDE xác định ánh xạ từ dữ liệu đầu vào $$a$$ sang nghiệm $$u$$, liệu ta có thể học ánh xạ đó như một toán tử giữa các không gian Banach thay vì chỉ như một vector giá trị tại các nút lưới? Cả hai câu hỏi đều đòi hỏi trực tiếp ngôn ngữ của chương này: điều kiện Lipschitz, ma trận Jacobi, tính đầy đủ và các chuẩn độc lập với phép rời rạc hóa lưới.

## Khái niệm then chốt

### Đạo hàm tự động như giải tích tính toán

Huấn luyện mô hình học máy hiện đại đòi hỏi tính đạo hàm của một hàm mất mát vô hướng theo hàng triệu tham số. Đạo hàm tự động (automatic differentiation) áp dụng quy tắc dây chuyền trực tiếp trên đồ thị tính toán, nhờ đó gradient của

$$
\mathcal{L}(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell\bigl(f_\theta(x_i),y_i\bigr)
$$

được tính chính xác đến sai số dấu phẩy động, không cần khai triển ký hiệu thủ công và cũng không mắc sai số cắt cụt như sai phân hữu hạn. Đây chính là giải tích nhiều biến đã ôn trong chương, áp dụng cho các hàm hợp có kích thước quá lớn để tính bằng tay. Nhờ đó, các bộ giải ODE, phép tích phân hay nhân tử Fourier khả vi đều có thể đưa trực tiếp vào vòng lặp huấn luyện.

### Mạng nơ-ron như ánh xạ tham số hóa

Một mạng truyền thẳng với tham số $$\theta$$ xác định ánh xạ $$f_\theta:\mathbb{R}^{d_{\mathrm{in}}}\to\mathbb{R}^{d_{\mathrm{out}}}$$. Khi ẩn số là một hàm $$u(x)$$, ta có hai cách tiếp cận: đánh giá $$f_\theta$$ tại các điểm lưới (collocation points), hoặc nâng mô hình lên thành một toán tử $$\mathcal{G}_\theta$$ tác động trực tiếp trên không gian hàm. Cách thứ nhất làm việc trong không gian Euclid hữu hạn chiều; cách thứ hai làm việc trong các không gian Banach hoặc Hilbert như $$L^2$$ hay $$H^1$$. Sự khác biệt này mang ý nghĩa thực tiễn rõ rệt: mô hình định nghĩa cố định trên một lưới không thể tự đánh giá trên lưới mịn hơn nếu không huấn luyện lại, còn toán tử bất biến với phép rời rạc hóa về nguyên tắc có thể chuyển đổi độ phân giải.

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart và Anandkumar đã hệ thống hóa cách tiếp cận toán tử này và chứng minh định lý xấp xỉ phổ quát cho mạng toán tử (neural operator) giữa các không gian Banach ([Kovachki và cộng sự, *JMLR* 24(89), 2023](https://jmlr.org/papers/v24/21-1524.html); [arXiv:2108.08481](https://arxiv.org/abs/2108.08481)). Kết quả đó minh họa trực tiếp tinh thần của Chương 00: lý thuyết xấp xỉ có thể vận hành ngay trên không gian hàm chứ không chỉ giới hạn trong $$\mathbb{R}^n$$.

### Phần dư vật lý và tính đặt chỉnh

Mạng nơ-ron tích hợp vật lý (Physics-Informed Neural Network — PINN) biểu diễn nghiệm chưa biết bằng mạng $$u_\theta$$ và đưa phần dư của phương trình vi phân cùng dữ liệu hoặc điều kiện biên vào hàm mất mát. Với bài toán $$u'=f(t,u)$$, ta cực tiểu hóa

$$
\mathcal{L}(\theta)=\sum_{k}\bigl\lvert u_\theta'(t_k)-f\bigl(t_k,u_\theta(t_k)\bigr)\bigr\rvert^2+\sum_{j}\bigl\lvert u_\theta(t_j)-u_j\bigr\rvert^2.
$$

Raissi, Perdikaris và Karniadakis đề xuất khuôn khổ PINN hiện đại năm 2019; bài tổng quan của Karniadakis và cộng sự trên *Nature Reviews Physics* (2021) đặt PINN, học toán tử và các bộ giải kết hợp trong cùng bức tranh SciML. Sau đó, bài khảo sát năm 2022 của Cuomo, Di Cola, Giampaolo, Rozza, Raissi và Piccialli hệ thống hóa các biến thể phương pháp và phân tích những dạng lỗi thường gặp ([Cuomo và cộng sự, *J. Sci. Comput.* 2022](https://doi.org/10.1007/s10915-022-01939-z); [arXiv:2201.05624](https://arxiv.org/abs/2201.05624)).

Các định lý tồn tại và duy nhất vẫn giữ vai trò bộ lọc lý thuyết quan trọng. Nếu bài toán giá trị đầu vi phạm điều kiện Lipschitz, một nhiễu nhỏ ở tham số $$\theta$$ có thể khiến $$u_\theta$$ thay đổi rất mạnh, làm bài toán tối ưu mất ổn định. Ngược lại, khi bài toán vi phân đặt chỉnh, phần dư nhỏ mới thực sự phản ánh nghiệm gần đúng đáng tin cậy.

### Mô hình độ sâu liên tục và tính đầy đủ

Luận án năm 2022 của Kidger, *On Neural Differential Equations* ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)), thống nhất mạng dư (residual network), neural ODE, neural CDE và neural SDE vào cùng một họ mô hình. Tính đầy đủ của không gian nền đóng vai trò thiết yếu tương tự trong giải tích cổ điển: ta cần một không gian đầy đủ để phép lặp Picard, phương trình liên hợp và tích phân ngẫu nhiên hội tụ. Chính ngôn ngữ metric và chuẩn dùng cho dãy Cauchy nay nâng đỡ việc lan truyền ngược gradient qua bộ giải ODE.

## Phương pháp và kỹ thuật

Điểm khác biệt cốt lõi về mặt phương pháp nằm ở việc thay đổi ẩn số cần tìm. Giải tích cổ điển tìm hàm $$u$$ thỏa mãn phương trình; SciML tìm vector tham số $$\theta$$ sao cho hàm $$u_\theta$$ hoặc toán tử $$\mathcal{G}_\theta$$ thỏa mãn gần đúng một phương trình hay một họ phương trình. Thuật toán tối ưu thường dùng các phương pháp gradient bậc nhất theo $$\theta$$, nhưng các đối tượng bên trong vẫn là đạo hàm, ma trận Jacobi và tích vô hướng quen thuộc.

Có thể phân loại các cách tiếp cận thành ba nhóm chính:

- **Xấp xỉ hàm.** Học trực tiếp nghiệm $$u_\theta(x)$$ cho một bài toán cụ thể, điển hình là PINN.
- **Xấp xỉ toán tử.** Học ánh xạ $$\mathcal{G}_\theta:a\mapsto u$$ cho cả một họ bài toán, điển hình là neural operator.
- **Mô hình kết hợp (hybrid).** Giữ phần phương trình cơ chế đã biết và chỉ dùng mạng nơ-ron để học thành phần trường vector, quan hệ đóng (closure) hoặc lực chưa biết.

Cả ba hướng đều phải trả lời cùng những câu hỏi nền tảng: ẩn số thuộc không gian nào, cấu trúc tôpô nào xác định sự hội tụ, và cấu trúc đại số tuyến tính nào đang được khai thác?

## Ví dụ

### Ví dụ 1: Khối residual như một bước Euler

Lớp mạng dư $$x_{n+1}=x_n+h\,f_\theta(x_n)$$ có đúng dạng sơ đồ Euler hiện cho phương trình $$x'=f_\theta(x)$$. Nếu $$f_\theta$$ thỏa điều kiện Lipschitz, quỹ đạo rời rạc sẽ hội tụ khi $$h\to 0$$ tới một quỹ đạo liên tục duy nhất—biểu hiện tính toán của định lý Picard–Lindelöf. Hằng số Lipschitz vừa bảo đảm tính duy nhất của nghiệm vừa ảnh hưởng trực tiếp đến mức độ ổn định khi huấn luyện.

### Ví dụ 2: Vai trò của việc chọn chuẩn

Hai hàm ứng viên $$u$$ và $$v$$ có thể nhận cùng giá trị tại mọi nút lưới nhưng sai khác nhau bởi một thành phần dao động nhanh giữa các nút. Theo chuẩn Euclid trên các giá trị tại nút lưới, chúng trông rất gần nhau; nhưng theo chuẩn $$H^1$$, khoảng cách giữa chúng có thể rất lớn do đạo hàm chênh lệch đáng kể. Vì vậy, các bài toán học toán tử thường đánh giá sai số theo chuẩn của không gian hàm thay vì chỉ so sánh từng điểm rời rạc.

### Ví dụ 3: Kiểm tra đạo hàm tự động cơ bản

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.sin(x) * torch.exp(-x)
y.backward()
print(float(x.grad), float((torch.cos(x) - torch.sin(x)) * torch.exp(-x)))
```

Hai giá trị in ra khớp nhau. Khi mở rộng sang tính phần dư PINN hay phương trình liên hợp cho neural ODE, bản chất giải tích của quy tắc dây chuyền không thay đổi; chỉ có quy mô đồ thị tính toán tăng lên.

## Ứng dụng trong khoa học, kỹ thuật và ngữ cảnh hiện đại

SciML được ứng dụng rộng rãi ở những bài toán có mô hình vi phân đáng tin cậy nhưng chi phí mô phỏng cao, mô hình chưa đầy đủ hoặc chỉ có dữ liệu quan sát một phần. Các mô hình giả lập khí hậu học toán tử thay thế cho bộ giải PDE khí quyển; các mạng tái tạo ảnh y khoa giải bài toán ngược elliptic hoặc hyperbolic; còn trong điều khiển học, mạng nơ-ron được dùng để học hàm chứng chỉ ổn định thay vì chỉ khớp quỹ đạo. Trong mọi trường hợp, kiến thức nền của Chương 00 quyết định tiêu chuẩn "xấp xỉ tốt": một mô hình có sai số nhỏ theo chuẩn $$L^2$$ vẫn có thể chưa đạt yêu cầu nếu bài toán kỹ thuật đòi hỏi kiểm soát giá trị cực đại tại từng điểm hoặc thông lượng biên; và một trường vector học được không thỏa điều kiện Lipschitz sẽ mất bảo đảm về tính tồn tại và duy nhất nghiệm.

Các bài tổng quan của Karniadakis và cộng sự (2021) và Cuomo và cộng sự (2022) hệ thống hóa các lĩnh vực ứng dụng, trong khi Kovachki và cộng sự (2023) cùng Kidger (2022) đại diện cho hai trục lý thuyết chính: học toán tử trên không gian vô hạn chiều và mô hình độ sâu liên tục gắn với phương trình vi phân.

## Thách thức và hướng mở rộng

Các phương pháp SciML vẫn tồn tại nhiều giới hạn cần lưu ý. Tính đạo hàm tự động trên khoảng thời gian dài có thể gặp bất ổn số; phương pháp liên hợp giúp giảm bộ nhớ nhưng lại sinh ra một hệ ODE ngược thời gian đôi khi rất cứng (stiff). Hàm mất mát của PINN kết hợp phần dư phương trình, điều kiện biên và dữ liệu quan sát với các trọng số chọn thủ công, nên giá trị hàm mất mát nhỏ không tự động kéo theo sai số nghiệm nhỏ. Định lý xấp xỉ phổ quát chỉ bảo đảm sự tồn tại của một mạng đủ tốt, chứ không bảo đảm thuật toán hạ gradient sẽ tìm được mạng đó. Ngoài ra, mô hình học từ dữ liệu có thể vi phạm các định luật bảo toàn, tính dương hoặc tính bất biến nếu những ràng buộc này không được tích hợp vào kiến trúc.

Hai câu hỏi gợi mở đáng suy nghĩ: nếu hai mạng đạt cùng mức phần dư, chuẩn không gian hàm nào quyết định mạng nào gần nghiệm đúng hơn? Và tính đầy đủ của không gian đóng vai trò gì khi ẩn số là một phân bố xác suất trên tập quỹ đạo thay vì một đường cong đơn lẻ?

## Video tham khảo

- Xem trước: [Physics Informed Neural Networks (PINNs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — Steve Brunton, tiếng Anh. Giải thích cách đưa phần dư PDE vào hàm mất mát của mạng nơ-ron theo đúng hướng tiếp cận SciML của bài.
- [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, tiếng Anh. Giới thiệu neural ODE như mô hình độ sâu liên tục, tương ứng với nhánh lý thuyết thứ hai trong bài.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Trình bày Fourier neural operator học ánh xạ giữa các không gian hàm, minh họa trực tiếp cho hướng học toán tử.

## Bài tập

1. **Quy tắc dây chuyền và đạo hàm tự động.** Cho $$y=\sin(e^{x^2})$$. Hãy tính $$y'$$ bằng tay rồi kiểm chứng bằng đạo hàm tự động. Tại mỗi phép toán sơ cấp trên đồ thị tính toán, cần lưu lại đại lượng trung gian nào?

2. **Điều kiện Lipschitz và tính duy nhất.** Xét bài toán $$x'=|x|^{1/2}$$ với $$x(0)=0$$. Hãy giải thích vì sao định lý Picard–Lindelöf không áp dụng được, và điều gì có thể xảy ra nếu một neural ODE sử dụng trường vector có cùng mức độ chính quy cục bộ như vậy.

3. **Chuẩn trên lưới.** Xét hàm $$u_h(x)=\sin(2\pi n x)$$ lấy mẫu trên $$N$$ nút cách đều thuộc $$[0,1]$$. Hãy so sánh chuẩn Euclid trên vector giá trị nút với xấp xỉ hình thang của $$\|u_h\|_{L^2}$$ và $$\|u_h'\|_{L^2}$$ khi $$n$$ tăng. Chuẩn nào phát hiện được dao động tần số cao?

4. **Thí nghiệm tính toán.** Dùng PyTorch hoặc JAX để huấn luyện một mạng hai lớp khớp nghiệm $$u(t)=e^{-t}$$ trên $$[0,2]$$ bằng cách chỉ cực tiểu hóa phần dư $$u'+u$$ cùng điều kiện đầu $$u(0)=1$$. Lặp lại thí nghiệm khi thêm nhiễu vào điều kiện đầu, quan sát sự thay đổi của nghiệm học được và chỉ ra định lý nào trong chương giải thích độ nhạy này.

5. **Khám phá mở.** Đọc phần mở đầu của Kovachki và cộng sự (2023) hoặc Kidger (2022) và viết khoảng nửa trang nhận xét: neural operator gần với bộ giải số, hàm Green hay một lớp công cụ xấp xỉ mới?

## Tài liệu

- Boyce, W. E., và DiPrima, R. C. *Elementary Differential Equations*. Phụ lục giải tích và đại số tuyến tính—nền tảng cổ điển của bài học.
- Karniadakis, G. E., và cộng sự. “Physics-informed machine learning.” *Nature Reviews Physics* 3 (2021): 422–440.
- Cuomo, S., và cộng sự. “Scientific machine learning through physics-informed neural networks.” *Journal of Scientific Computing* 92 (2022): 88. [arXiv:2201.05624](https://arxiv.org/abs/2201.05624).
- Kovachki, N., và cộng sự. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, số 89 (2023): 1–97.
- Kidger, P. *On Neural Differential Equations*. Luận án DPhil, Đại học Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
