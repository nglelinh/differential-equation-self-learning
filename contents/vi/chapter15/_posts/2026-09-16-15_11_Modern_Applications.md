---
layout: post
title: "15-11 Ứng dụng hiện đại: Bài ngược học được và prior vi cục bộ"
chapter: '15'
order: 11
owner: Course Team
lang: vi
categories:
- chapter15
lesson_type: optional
---

## Mục tiêu

Bài học tùy chọn này kết nối tập mặt sóng, sự lan truyền kỳ dị và bài toán ngược với các hướng thực hành giai đoạn 2022–2024 về neural inverse operator và tái tạo ảnh dựa trên hàm score. Sau bài học, sinh viên cần xác định được những kỳ dị nào một mô hình tái tạo ảnh học được có cơ sở để khôi phục, giải thích vì sao một hình ảnh trông hợp lý về mặt thị giác vẫn có thể sai lệch về mặt vi địa phương, và nhận diện giao điểm giữa bài “Các hướng nghiên cứu hiện nay” của chương với học máy khoa học (SciML). Nội dung này bổ sung góc nhìn tính toán chứ không thay thế các định lý vi địa phương đã học.

## Kiến thức nền

Sinh viên cần nắm vững tập mặt sóng (wave front set), định lý lan truyền kỳ dị cho toán tử kiểu chính thực, khái niệm toán tử tích phân Fourier (FIO) và bài tùy chọn về bài toán ngược. Bài “Các hướng nghiên cứu hiện nay” vẽ bản đồ từ phía giải tích; bài này bổ sung góc nhìn từ học máy.

## Dẫn nhập

Giải tích vi địa phương được xây dựng nhằm trả lời bài toán về tính khả kiến (visibility): những kỳ dị nào của thế ẩn, vận tốc âm thanh hay hệ số suy giảm thực sự truyền tới được đầu thu, và những kỳ dị nào rơi vào vùng khuất? Những câu hỏi đó không hề trở nên lỗi thời khi mạng nơ-ron xuất hiện; trái lại, chúng càng cấp thiết hơn vì mạng học sâu có thể tạo ra các biên cạnh sắc nét dù không có tia truyền, quan hệ chính tắc hay toán tử FIO nào mang thông tin đó tới dữ liệu đo.

Ba hướng phát triển trong giai đoạn 2022–2024 minh họa rõ giao điểm này. Molinaro, Yang, Li, Azizzadenesheli, Anandkumar và Stuart (*Neural Inverse Operators*, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) học nghịch đảo chính quy hóa của ánh xạ thuận PDE, bao gồm tái tạo ảnh kiểu Helmholtz. Song, Shen và cộng sự đưa mô hình sinh dựa trên hàm score vào bài toán ngược y khoa (ICLR 2022), còn Chung, Kim, Mccann, Klasky và Ye (*Diffusion Posterior Sampling*, ICLR 2023; [arXiv:2209.14687](https://arxiv.org/abs/2209.14687)) đề xuất công thức phổ biến để kết hợp tiên nghiệm khuếch tán với toán tử thuận. Rasht-Behesht và cộng sự (JGR 2022) cùng các phương pháp nghịch đảo dùng PINN giải quyết bài toán nghịch đảo dạng sóng đầy đủ (full-waveform inversion) trong địa chấn thông qua phần dư vật lý.

Trong mọi trường hợp trên, ánh xạ thuận ở tần số cao là một FIO hoặc hợp thành các FIO. Một nghịch đảo học được không tôn trọng quan hệ chính tắc không phải là một lý thuyết ảnh học mới; nó chỉ là một tiên nghiệm (prior) có thể phản ánh đúng hoặc sai những gì dữ liệu đo thực sự chứa.

## Khái niệm then chốt

### Tập mặt sóng khả kiến và không khả kiến

Nếu $$\operatorname{WF}(f)$$ không giao với tập các kỳ dị mà toán tử FIO của thí nghiệm có thể quan sát được, thì không một phương pháp nào — dù giải tích hay học máy — có thể khẳng định khôi phục được các kỳ dị ấy chỉ từ dữ liệu đo. Một tiên nghiệm sinh vẫn có thể tự điền vào các chi tiết đó. Do đó, các công trình đáng tin cậy cần báo cáo độ bất định hoặc thành phần thuộc không gian hạch, và giải tích vi địa phương chính là ngôn ngữ mô tả không gian hạch này.

### Neural inverse operator

Neural inverse operator xấp xỉ nghịch đảo chính quy hóa $$F_\alpha^\dagger$$ của toán tử thuận $$F$$. Chính quy hóa là bước bắt buộc vì toán tử nghịch đảo chính xác, ngay cả khi tồn tại, thường không bị chặn trên $$L^2$$. Các định lý ánh xạ Sobolev và vi địa phương xác định không gian đích mà $$F_\alpha^\dagger$$ có thể ánh xạ vào. Nếu $$F$$ làm mất một bậc đạo hàm cùng một tập hướng nhất định, thì mạng nơ-ron tạo ra ảnh chi tiết cao theo các hướng không khả kiến thực chất đang khớp với tiên nghiệm chứ không phải dữ liệu.

### Lấy mẫu hậu nghiệm dựa trên hàm score

Phương pháp Diffusion Posterior Sampling lấy mẫu từ phân phối hậu nghiệm xấp xỉ $$p(x\mid y)$$ bằng cách kết hợp hàm score học được $$\nabla\log p(x)$$ với bước cập nhật nhất quán dữ liệu liên quan đến $$F$$. Cách tiếp cận này rất hiệu quả cho ảnh y khoa và phục hồi vùng khuyết (inpainting). Tuy nhiên, cảnh báo vi địa phương là tiên nghiệm score có thể tự sinh các thành phần mặt sóng vốn bị $$F^*F$$ triệt tiêu. Do đó, việc kiểm tra phần dư $$y-F\hat x$$ trên tập mặt sóng của dữ liệu, thay vì chỉ đo chuẩn $$L^2$$, là tiêu chuẩn kiểm chứng đúng đắn.

### Nghịch đảo bằng PINN và chế độ tần số cao

Phương pháp nghịch đảo dùng mạng nơ-ron tích hợp vật lý (PINN) đưa toán tử thuận $$F$$ trực tiếp vào hàm mất mát dưới dạng phần dư PDE thay vì huấn luyện mô hình thay thế. Cách làm này phù hợp khi dữ liệu ít và phương trình vật lý đáng tin cậy, nhưng vẫn chịu giới hạn thiên kiến phổ ở tần số cao — đúng vùng mà các phát biểu vi địa phương sắc nét nhất. Các biến thể PINN phân rã miền cho bài toán sóng (Moseley và cộng sự, 2023) giúp giảm thiên kiến phổ nhưng không làm thay đổi giới hạn tính khả kiến.

## Phương pháp và kỹ thuật

1. Xác định toán tử thuận $$F$$ và quan hệ chính tắc của nó (nếu có thể).
2. Phân loại rõ những kỳ dị nào là khả kiến với hình học thu thập dữ liệu hiện có.
3. Lựa chọn phương pháp nghịch đảo học được (NIO, nghịch đảo FNO, PINN hoặc bộ lấy mẫu khuếch tán) cùng cơ chế chính quy hóa phù hợp.
4. Kiểm thử trên mẫu chuẩn (phantom) có một phần tập mặt sóng không khả kiến; phương pháp “tái tạo” được phần không khả kiến đó thực chất đang quá khớp với tiên nghiệm.
5. Báo cáo đồng thời sai số trong miền ảnh và phần dư tập mặt sóng trong miền dữ liệu.

Quy trình này bổ sung trực tiếp góc nhìn tính toán cho bản đồ giải tích (bài toán ngược, hình học phổ, nhiễu giả ảnh học) ở bài “Các hướng nghiên cứu hiện nay”.

## Ví dụ

### Ví dụ 1: Chụp cắt lớp góc hạn chế

Dữ liệu chụp cắt lớp X-quang góc hạn chế không ghi nhận được các biên cạnh có pháp tuyến nằm trong nón góc thiếu. Một mô hình khuếch tán huấn luyện trên ảnh đầy đủ vẫn dễ dàng điền nốt các biên cạnh ấy, tạo ra ảnh trông hợp lý về mặt y khoa nhưng sai lệch về mặt vi địa phương. Kết quả trung thực không phải là ảnh nhìn đẹp mắt nhất, mà là ảnh chỉ rõ vùng nón thiếu là phần chưa xác định được từ dữ liệu.

### Ví dụ 2: Tái tạo ảnh Helmholtz khi số sóng tăng

Khi số sóng $$k$$ tăng, bài toán ngược Helmholtz mang rõ đặc trưng FIO hơn và nhạy cảm mạnh hơn với pha. Một mạng nghịch đảo huấn luyện ở $$k$$ nhỏ không tự động tổng quát sang $$k$$ lớn. Đây là minh họa thực nghiệm trực tiếp cho bài học bán cổ điển của chương.

### Ví dụ 3: Kiểm tra phần dư dữ liệu theo tập mặt sóng

```python
import numpy as np

def F(x):
    return np.convolve(x, np.ones(5) / 5.0, mode="same")

x_true = np.zeros(64)
x_true[20:22] = 1.0
x_prior = np.zeros(64)
x_prior[40:42] = 1.0  # nhảy bịa
print(np.linalg.norm(F(x_true) - F(x_true)), np.linalg.norm(F(x_true) - F(x_prior)))
```

Bước nhảy tự sinh hầu như khó phân biệt qua toán tử làm trơn $$F$$. Một phương pháp tạo ra bước nhảy đó từ dữ liệu $$y=F(x_{\mathrm{true}})$$ thực chất đã dựa vào tiên nghiệm chứ không phải thông tin đo. Ngôn ngữ tập mặt sóng diễn đạt tổng quát hiện tượng này cho các toán tử thực tế phức tạp hơn nhiều so với ví dụ tích chập đơn giản trên.

## Ứng dụng

Các lĩnh vực ứng dụng tiêu biểu gồm chụp cắt lớp vi tính (CT), cộng hưởng từ (MRI), ảnh quang–âm, ảnh địa chấn và radar. Trong y khoa, các phương pháp tái tạo học sâu đã được sử dụng thực tế, nhưng câu hỏi mở vẫn là liệu chúng ổn định theo nghĩa vi địa phương hay chỉ theo cảm nhận thị giác. Trong địa vật lý cũng tồn tại tách biệt tương tự: PINN hay neural inverse operator có thể sinh mô hình vận tốc khớp tốt dữ liệu đo nhưng lại đặt sai vị trí một mặt phản xạ nằm trên đường song đặc trưng không khả kiến.

Các chủ đề lượng tử và bán cổ điển của chương cũng có hướng tiếp cận tương ứng trong học máy — như học biểu diễn Wigner hoặc Husimi, hay xấp xỉ độ đo phổ bằng mạng nơ-ron — nhưng giao điểm với bài toán ngược là mảng phát triển rõ nét nhất trong giai đoạn 2022–2024 và sinh viên có thể trực tiếp kiểm chứng bằng các công cụ đã học.

## Thách thức và hướng mở rộng

Tiên nghiệm sinh có thể lấn át thông tin từ dữ liệu đo. Khi hình học thu thập thay đổi, mạng huấn luyện theo một quan hệ chính tắc không nhất thiết tổng quát hóa sang quan hệ chính tắc khác. Giải tích tần số cao và các mô hình học máy vốn mạnh ở tần số thấp hoạt động ở những chế độ tiệm cận khác nhau, nên việc kết nối hai miền này vẫn là bài toán nghiên cứu mở. Ngoài ra, ước lượng độ bất định thường hiệu chỉnh kém theo các hướng không khả kiến, còn các bài toán ngược phi tuyến (độ dẫn dị hướng, truyền sóng phi tuyến) vượt ra ngoài khuôn khổ phép tính FIO tuyến tính.

Nếu bài “Các hướng nghiên cứu hiện nay” đặt câu hỏi dữ liệu cho phép “nghe” hoặc “nhìn thấy” bao nhiêu phần của hình dạng, thì bài này bổ sung câu hỏi: một mạng nơ-ron được phép tái dựng bao nhiêu phần của hình dạng đó? Câu trả lời chặt chẽ vẫn phụ thuộc vào tập mặt sóng của dữ liệu đo, đi kèm một tiên nghiệm được khai báo minh bạch.

## Video tham khảo

- Nên xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Trình bày các công cụ vi địa phương cổ điển làm chuẩn đối chiếu cho các mô hình ngược học được.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu toán tử học được cho ánh xạ thuận hoặc ngược, phần nền tảng tính toán của bài.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Trình bày hình học mặt sóng — ràng buộc cấu trúc mà các tiên nghiệm vi địa phương mô tả.

## Bài tập

1. **Nón góc thiếu.** Phác thảo tập mặt sóng khả kiến trong chụp cắt lớp góc hạn chế và giải thích vì sao phần dư $$\ell^2$$ có thể rất nhỏ ngay cả khi biên cạnh không khả kiến bị tái dựng sai.

2. **Quan hệ chính tắc dưới dạng sơ đồ.** Biểu diễn $$F$$ như một quan hệ giữa $$T^*X$$ và $$T^*Y$$. Chỉ ra trên sơ đồ vùng nào mạng nghịch đảo có độ tự do và vùng nào bị ràng buộc chặt bởi dữ liệu.

3. **Tiên nghiệm và dữ liệu.** Từ ví dụ tích chập đơn giản ở trên, hãy thiết kế một số hạng chính quy hóa hạn chế các bước nhảy ở thành phần tần số cao không khả kiến. Phiên bản vi địa phương tương ứng là gì?

4. **Thí nghiệm tính toán.** Cài đặt một bài toán ngược tuyến tính cỡ nhỏ kèm bộ khử nhiễu kiểu khuếch tán (hoặc tiên nghiệm làm mờ Gauss) rồi so sánh chất lượng tái tạo giữa biên khả kiến và biên không khả kiến.

5. **Khám phá mở.** Đọc bài báo của Chung và cộng sự (ICLR 2023) hoặc Molinaro và cộng sự (2023) kết hợp với bài toán ngược của chương, sau đó viết một trang phân tích yêu cầu cần có trong mọi bài báo tái tạo ảnh học sâu: cần chỉ rõ phần tập mặt sóng nào thực sự xuất phát từ dữ liệu đo.

## Tài liệu

- Hörmander, Tập III–IV; Zworski; các bài về bài toán ngược và hướng nghiên cứu hiện nay trong chương này.
- Molinaro, R., và cộng sự. “Neural inverse operators.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
- Song, Y., Shen, L., Xing, L., và Ermon, S. “Solving inverse problems in medical imaging with score-based generative models.” *ICLR* 2022. [arXiv:2111.08005](https://arxiv.org/abs/2111.08005).
- Rasht-Behesht, M., và cộng sự. “PINNs for wave propagation and full waveform inversions.” *JGR: Solid Earth* 127 (2022).
- Moseley, B., Markham, A., và Nissen-Meyer, T. “Finite basis PINNs.” *Adv. Comput. Math.* 49 (2023).
