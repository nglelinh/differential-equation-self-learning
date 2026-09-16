---
layout: post
title: "12-12 Ứng dụng hiện đại: Học toán tử trong không gian Sobolev"
chapter: '12'
order: 12
owner: Course Team
lang: vi
categories:
- chapter12
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này dùng không gian $$L^p$$, đạo hàm yếu, chuẩn Sobolev và tính đặt chỉnh Lax–Milgram như ngôn ngữ chính thức của lý thuyết neural operator. Sinh viên cần nói được ánh xạ học được được tuyên bố liên tục trên không gian nào, vì sao bất biến rời rạc hóa là tuyên bố giải tích hàm, và bài nào 2022–2024 cung cấp tốc độ xấp xỉ. Lý thuyết dạng yếu của chương không bị viết lại.

## Kiến thức nền

Sinh viên cần biết chuẩn $$L^p$$, đạo hàm yếu, các không gian $$H^1$$ và $$H^1_0$$, định lý Lax–Milgram, và ý niệm nghiệm yếu của PDE elliptic tuyến tính.

## Dẫn nhập

Mạng nơ-ron trên lưới là ánh xạ giữa không gian hữu hạn chiều. Neural operator được quảng cáo như ánh xạ giữa không gian hàm. Quảng cáo ấy rỗng trừ khi ta nêu tên các không gian. Kovachki và cộng sự (*JMLR* 24(89), 2023) làm đúng việc ấy: họ định nghĩa neural operator như hợp thành toán tử tích phân affine và phi tuyến tác động trên không gian Banach, chứng minh định lý xấp xỉ phổ quát, và đòi cùng tham số dùng được ở nhiều rời rạc hóa.

Lanthaler, Mishra và Karniadakis (*Error estimates for DeepONets*, *Transactions of Mathematics and Its Applications*, 2022) cho tốc độ định lượng theo kích thước trunk và branch, lại trong chuẩn chiều vô hạn. De Hoop, Kovachki, Nelsen và Stuart (*Convergence rates for learning linear operators from noisy data*, *SIAM/ASA JUQ*, 2023; [arXiv:2108.12515](https://arxiv.org/abs/2108.12515)) xem trường hợp tuyến tính như bài ngược thống kê trên không gian Hilbert. Hướng dẫn toán học 2023 của Boullé và Townsend tổ chức các kết quả ấy cho nhà giải tích.

Chương này là tiên quyết những bài ấy giả định. Đạo hàm yếu nói mô hình có thể hội tụ trong $$L^2$$ vẫn có gradient vô nghĩa. Lax–Milgram nói toán tử nghiệm thật bị chặn từ $$H^{-1}$$ tới $$H^1_0$$, nên toán tử học được chỉ bị chặn trên $$\ell^2$$ nút đang trả lời câu hỏi khác.

## Khái niệm then chốt

### Không gian có tên, lỗi có tên

Lỗi $$10^{-3}$$ vô nghĩa cho tới khi ta viết $$\|u_\theta-u\|_{L^2}$$, $$\|u_\theta-u\|_{H^1}$$, hoặc một chuẩn đối ngẫu yếu hơn. Bài elliptic thường cần $$H^1$$ vì năng lượng là seminorm $$H^1$$. Bài tiến hóa có thể hài lòng với $$L^2$$ theo không gian, đều theo thời gian. Bài học toán tử chỉ báo $$L^2$$ tương đối trên một lưới đang giấu tuyên bố giải tích hàm.

### Bất biến rời rạc hóa

Họ ánh xạ rời rạc $$G_h$$ là rời rạc hóa nhất quán của toán tử $$G$$ nếu, khi cỡ lưới $$h\to 0$$, $$G_h$$ áp lên rời rạc hóa của $$a$$ hội tụ tới rời rạc hóa của $$G(a)$$. Neural operator nhằm để $$G_h$$ chia sẻ tham số qua $$h$$. Điều ấy chỉ khả thi nếu kiến trúc được định nghĩa bởi nhân tích phân, nhân tử Fourier, hoặc đối tượng liên tục khác, không bởi ma trận trọng số có kích thước bằng số nút.

### Phần dư yếu như mất mát vật lý

Dạng yếu $$a(u,v)=\langle f,v\rangle$$ đã là phần dư. Mất mát toán tử vật lý-thông tin có thể phạt

$$
\sup_{\|v\|_{H^1_0}\le 1}\bigl\lvert a(u_\theta,v)-\langle f,v\rangle\bigr\rvert,
$$

tức phần dư $$H^{-1}$$. Collocate Laplacian mạnh là lựa chọn chặt hơn, đôi khi kém ổn định. Việc chương đi từ nghiệm mạnh sang yếu vì thế là quyết định huấn luyện, không chỉ tiện lý thuyết.

### Compactness và tốc độ

Xấp xỉ phổ quát trên tập compact của không gian Banach đòi compactness. Độ đo huấn luyện giá trên tập bị chặn của $$H^s$$ với $$s$$ đủ lớn để nhúng compact vào không gian làm việc là giả định ẩn thông thường. Nếu dữ liệu chỉ nằm trong $$L^2$$, không nhúng compact cứu bạn, và không trunk hữu hạn nào chính xác đều. Đó là nhúng Sobolev dùng như nhãn cảnh báo.

## Phương pháp và kỹ thuật

1. Nêu không gian đầu vào (ví dụ $$L^\infty$$ hệ số, $$H^{-1}$$ nguồn) và không gian đầu ra (ví dụ $$H^1_0$$).
2. Xác nhận kiến trúc có nghĩa trên các không gian ấy ở mọi độ phân giải.
3. Huấn luyện với mất mát tương đương chuẩn trong đó tính đặt chỉnh giữ, hoặc giải thích sự lệch.
4. Thử trên lưới mịn hơn và họ dao động hơn, để ý thất bại compactness.
5. Với bài tuyến tính, so toán tử học được với toán tử nghiệm Lax–Milgram trên một cơ sở nguồn.

## Ví dụ

### Ví dụ 1: Thành công $$L^2$$, thất bại $$H^1$$

Mạng có thể khớp răng cưa trong $$L^2$$ trong khi đạo hàm yếu của nó vẫn xa sóng vuông. Vẽ cả hai chuẩn là bài Sobolev trong một hình. Mọi surrogate Darcy nên báo cả hai.

### Ví dụ 2: Lax–Milgram như chặn tổng quát hóa

Nếu $$a(\cdot,\cdot)$$ cưỡng bức với hằng số $$\alpha$$, thì $$\|u\|_{H^1}\le\alpha^{-1}\|f\|_{H^{-1}}$$. Toán tử học được có chuẩn toán tử trên các không gian ấy vượt $$C/\alpha$$ với $$C$$ lớn chưa phải bộ giải; nó là interpolant không ổn định. Tính chuẩn toán tử thực nghiệm trên tập kiểm là proxy rẻ.

### Ví dụ 3: Seminorm $$H^1$$ rời rạc

```python
import numpy as np

def h1_seminorm(u, dx):
    return np.sqrt(np.sum(np.diff(u)**2 / dx))

x = np.linspace(0, 1, 51)
dx = x[1] - x[0]
print(h1_seminorm(np.sin(2 * np.pi * x), dx), h1_seminorm(np.sin(20 * np.pi * x), dx))
```

Sin tần số cao lớn hơn nhiều trong $$H^1$$. Mô hình chỉ huấn luyện trong $$L^2$$ không nhất thiết thấy khác biệt ấy.

## Ứng dụng

Một khi không gian được nêu tên, tuyên bố khoa học trở nên so sánh được. Bộ giả lập thời tiết chính xác trong $$L^2$$ nhiệt độ nhưng hoang trong $$H^1$$ sẽ có thông lượng vô dụng. Toán tử ảnh y khoa ánh xạ dữ liệu biên trong $$L^2(\partial\Omega)$$ tới nội thất trong $$L^2(\Omega)$$ có thể đang làm mượt đúng những kỳ dị nhà lâm sàng cần. Định lượng bất định cho toán tử tuyến tính, như ở de Hoop và cộng sự (2023), là ngôn ngữ đúng cho thí nghiệm nhiễu: ta học hậu nghiệm trên không gian Hilbert, không phải một vector lưới.

Cùng góc nhìn ấy kỷ luật PINN. Phần dư mạnh nhỏ tại điểm collocation không kéo theo phần dư $$H^{-1}$$ nhỏ, và do đó không kéo theo lỗi $$H^1$$ nhỏ qua Lax–Milgram. Sinh viên đã chứng minh định lý ấy đã biết cách đọc bảng PINN một cách hoài nghi.

## Thách thức và hướng mở rộng

Toán tử phi tuyến, ánh xạ phụ thuộc thời gian, và đầu ra giá trị độ đo rời khỏi vùng an toàn Hilbert. Nhúng Sobolev thất bại ở chiều cao hoặc số mũ tới hạn, liên quan tới PDE tham số chiều rất cao. Aliasing rời rạc có thể phá chặn Lipschitz liên tục. Tốc độ thống kê suy giảm theo nhiễu theo cách lý thuyết xấp xỉ một mình không bắt được. Định lý xấp xỉ phổ quát không bao giờ hứa gradient descent sẽ tìm ra các tham số xấp xỉ.

Câu hỏi đáng hỏi mọi bài báo: tuyên bố được nêu trong không gian Banach nào, và đó có phải không gian trong đó PDE đặt chỉnh?

## Bài tập

1. **Từ điển chuẩn.** Với ánh xạ Poisson Dirichlet $$f\mapsto u$$, nêu tính liên tục $$H^{-1}\to H^1_0$$ và $$L^2\to H^2\cap H^1_0$$ (trên miền trơn). Neural operator nên quảng cáo cái nào nếu nó chỉ thấy $$f$$ nhiễu?

2. **Compactness.** Vì sao tập huấn luyện bị chặn trong $$H^2$$ cho tập compact trong $$H^1$$ ở một chiều? Điều gì thất bại nếu chặn chỉ trong $$H^1$$?

3. **Mất mát yếu.** Viết xấp xỉ Monte Carlo của phần dư $$H^{-1}$$ cho $$-u''=f$$. Vì sao chọn ngẫu nhiên hàm thử $$v$$ chỉ là chặn dưới?

4. **Thí nghiệm tính toán.** Lấy hai lưới và interpolant tuyến tính của một hàm $$H^1$$ cố định. Tính lỗi $$L^2$$ và $$H^1$$ rời rạc dưới tinh. Rồi thay interpolant bằng ánh xạ nơ-ron từng pixel huấn luyện trên lưới thô và quan sát điều xảy ra.

5. **Khám phá mở.** Đọc Mục 1–2 của Kovachki và cộng sự (2023) hoặc Lanthaler, Mishra và Karniadakis (2022) và dịch một phát biểu định lý sang ký hiệu của chương này.

## Tài liệu

- Brezis; Adams và Fournier, *Sobolev Spaces*.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Lanthaler, S., Mishra, S., và Karniadakis, G. E. “Error estimates for DeepONets.” *Trans. Math. Appl.* 6 (2022). [arXiv:2102.09618](https://arxiv.org/abs/2102.09618).
- de Hoop, M. V., Kovachki, N. B., Nelsen, N. H., và Stuart, A. M. “Convergence rates for learning linear operators from noisy data.” *SIAM/ASA JUQ* 11 (2023). [arXiv:2108.12515](https://arxiv.org/abs/2108.12515).
- Boullé, N., và Townsend, A. “A mathematical guide to operator learning.” 2023. [arXiv:2312.05663](https://arxiv.org/abs/2312.05663).
