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

Bài tùy chọn này nối tập sóng trước, truyền kỳ dị và bài ngược với thực hành 2022–2024 về neural inverse operator và tái tạo score. Sinh viên cần nói được kỳ dị nào bộ ảnh hóa học được được phép khôi phục, vì sao một ảnh hợp lý vẫn có thể không trung thực vi cục bộ, và chỗ nào bài hướng nghiên cứu hiện nay của chương gặp SciML. Các định lý vi cục bộ đã phát triển không bị viết lại.

## Kiến thức nền

Sinh viên cần biết tập sóng trước, định lý truyền cho toán tử kiểu chính thực, ý niệm toán tử tích phân Fourier, và bài bài ngược tùy chọn. Bài “Hướng nghiên cứu hiện nay” hiện có bổ sung: nó vẽ bản đồ giải tích; bài này thêm lớp học máy.

## Dẫn nhập

Phân tích vi cục bộ được xây để trả lời câu hỏi tầm nhìn. Kỳ dị nào của thế ẩn, tốc độ âm, hoặc suy giảm đi tới detector? Kỳ dị nào mất trong bóng? Những câu hỏi ấy không trở nên lỗi thời khi mạng nơ-ron đến. Chúng trở nên cấp bách hơn, vì mạng có thể vẽ cạnh sắc mà không tia, không hệ thức chính tắc, và không FIO nào từng mang tới dữ liệu.

Ba phát triển 2022–2024 làm tiếp xúc cụ thể. Molinaro, Yang, Li, Azizzadenesheli, Anandkumar và Stuart (*Neural Inverse Operators*, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) học nghịch đảo regularized của ánh xạ thuận PDE, gồm ảnh hóa kiểu Helmholtz. Song, Shen và cộng sự đưa mô hình sinh score vào bài ngược y khoa quanh ICLR 2022, và Chung, Kim, Mccann, Klasky và Ye (*Diffusion Posterior Sampling*, ICLR 2023; [arXiv:2209.14687](https://arxiv.org/abs/2209.14687)) cho công thức được dùng rộng để kết hợp prior khuếch tán với toán tử thuận. Rasht-Behesht và cộng sự (JGR 2022) cùng các đảo PINN liên quan tấn công bài full-waveform địa chấn bằng phần dư vật lý.

Trong mỗi trường hợp, ánh xạ thuận là FIO, hoặc hợp thành FIO, ở tần số cao. Nghịch đảo học được không tôn trọng hệ thức chính tắc không phải lý thuyết ảnh hóa mới; nó là prior có thể trung thực hoặc không về những gì dữ liệu chứa.

## Khái niệm then chốt

### Sóng trước nhìn thấy versus không nhìn thấy

Nếu $$\operatorname{WF}(f)$$ không cắt tập kỳ dị mà FIO của thí nghiệm có thể thấy, không phương pháp — giải tích hay học được — nên tuyên bố khôi phục những kỳ dị ấy từ chỉ dữ liệu. Prior sinh vẫn có thể bịa chúng. Bài báo có trách nhiệm vì thế báo bất định hoặc thành phần không gian hạch. Phân tích vi cục bộ là ngôn ngữ mô tả không gian hạch ấy.

### Neural inverse operator

Neural inverse operator xấp xỉ nghịch đảo regularized $$F_\alpha^\dagger$$ của ánh xạ thuận $$F$$. Regularization không tùy chọn: nghịch đảo thật, khi tồn tại, thường không bị chặn trên $$L^2$$. Các ánh xạ Sobolev và vi cục bộ nói $$F_\alpha^\dagger$$ có thể ánh xạ vào không gian nào. Nếu $$F$$ mất một đạo hàm và một tập hướng, mạng xuất ảnh rất thô theo hướng không nhìn thấy đang khớp prior, không phải dữ liệu.

### Hậu nghiệm score

Diffusion posterior sampling rút từ hậu nghiệm xấp xỉ $$p(x\mid y)$$ bằng cách kết hợp score học được $$\nabla\log p(x)$$ với bước nhất quán dữ liệu liên quan $$F$$. Cấu trúc mạnh cho ảnh y khoa và inpainting. Cảnh báo vi cục bộ là score prior có thể khôi phục sóng trước mà $$F^*F$$ triệt tiêu. Nhìn phần dư $$y-F\hat x$$ trong tập sóng trước của dữ liệu, không chỉ trong chuẩn $$L^2$$, là kiểm toán đúng.

### Đảo PINN và tần số cao

Đảo vật lý-thông tin mã hóa $$F$$ như phần dư chứ không như surrogate huấn luyện. Chúng hấp dẫn khi dữ liệu hiếm và PDE được tin. Chúng vẫn bị giới hạn bởi thiên kiến phổ ở tần số cao, đúng chế độ trong đó các phát biểu vi cục bộ sắc nhất. PINN sóng phân rã miền (Moseley và cộng sự, 2023) giảm thiên kiến ấy nhưng không đổi phép tính tầm nhìn.

## Phương pháp và kỹ thuật

1. Xác định toán tử thuận $$F$$ và, nếu có thể, hệ thức chính tắc của nó.
2. Nêu kỳ dị nào nhìn thấy được với hình học thu thập có sẵn.
3. Chọn nghịch đảo học được (NIO, nghịch đảo FNO, PINN, hoặc bộ lấy mẫu khuếch tán) và một regularizer.
4. Kiểm chứng trên phantom có sóng trước một phần không nhìn thấy; phương pháp “khôi phục” phần không nhìn thấy đang overfitting prior.
5. Báo cả lỗi miền ảnh lẫn phần dư sóng trước miền dữ liệu.

Pipeline này không cạnh tranh với bài hướng nghiên cứu hiện nay; nó thêm cột tính toán vào cùng bản đồ (bài ngược, hình học phổ, artifact ảnh hóa).

## Ví dụ

### Ví dụ 1: Chụp cắt lớp góc hạn chế

Dữ liệu X-quang góc hạn chế không thấy cạnh có pháp tuyến nằm trong nón thiếu. Mô hình khuếch tán huấn luyện trên ảnh đầy đủ sẽ vui vẻ hoàn tất các cạnh ấy. Tái tạo có thể trông y khoa và vẫn sai vi cục bộ. Hình đúng không phải ảnh đẹp; đó là ảnh với nón thiếu được sơn như chưa biết.

### Ví dụ 2: Ảnh Helmholtz khi số sóng tăng

Khi $$k$$ tăng, bài Helmholtz ngược trở nên giống FIO hơn và nhạy pha hơn. Nghịch đảo nơ-ron huấn luyện ở $$k$$ nhỏ sẽ không tự làm việc ở $$k$$ lớn. Đó là bài học bán cổ điển của chương dưới dạng thí nghiệm.

### Ví dụ 3: Phần dư dữ liệu như kiểm sóng trước

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

Nhảy bịa hầu như vô hình với $$F$$. Phương pháp xuất nó từ $$y=F(x_{\mathrm{true}})$$ đã dùng prior, không phải dữ liệu. Ngôn ngữ sóng trước nói cùng điều ấy không cần tích chập đồ chơi.

## Ứng dụng

CT, MRI, quang-âm, ảnh địa chấn và radar là nhà ứng dụng của cuộc thảo luận này. Bệnh viện đã dùng tái tạo học được; câu hỏi khoa học mở là những tái tạo ấy ổn định theo nghĩa vi cục bộ hay chỉ theo nghĩa tri giác. Ảnh hóa địa vật lý có cùng tách: PINN hoặc nghịch đảo nơ-ron có thể sinh mô hình vận tốc khớp vết và vẫn đặt sai một gương phản xạ dọc bicharacteristic không nhìn thấy.

Các chủ đề lượng tử và bán cổ điển của chương cũng có tiếng vang ML — biểu diễn Wigner hoặc Husimi học được, xấp xỉ nơ-ron của độ đo phổ — nhưng tiếp xúc bài ngược là câu chuyện 2022–2024 chín nhất, và là câu chuyện sinh viên có thể kiểm toán bằng công cụ họ đã có.

## Thách thức và hướng mở rộng

Prior sinh có thể át dữ liệu. Hình học thu thập đổi, và mạng huấn luyện trên một hệ thức chính tắc không nhất thiết chuyển sang hệ thức khác. Phân tích tần số cao và mô hình học được tần số thấp sống trên các hành tinh tiệm cận khác nhau; khớp chúng là bài nghiên cứu đang hoạt động. Ước lượng bất định thường hiệu chỉnh kém theo hướng không nhìn thấy. Bài ngược phi tuyến (dẫn dị hướng, sóng phi tuyến) rời phép tính FIO tuyến tính.

Bài hướng nghiên cứu hiện có đã hỏi bao nhiêu hình dạng nghe được hoặc nhìn thấy được. Bài này thêm: mạng được phép vẽ bao nhiêu hình dạng? Câu trả lời trung thực vẫn do tập sóng trước của dữ liệu cho, cộng một prior được dán nhãn rõ.

## Bài tập

1. **Nón thiếu.** Phác sóng trước nhìn thấy cho chụp cắt lớp góc hạn chế và giải thích vì sao phần dư $$\ell^2$$ có thể nhỏ trong khi cạnh không nhìn thấy sai.

2. **Hệ thức chính tắc như sơ đồ.** Vẽ $$F$$ như hệ thức giữa $$T^*X$$ và $$T^*Y$$. Ở đâu trong sơ đồ ấy nghịch đảo nơ-ron có tự do, và ở đâu thì không?

3. **Prior versus dữ liệu.** Dùng tích chập đồ chơi ở trên, thiết kế regularizer cấm nhảy trong thành phần tần số cao không nhìn thấy. Analogue vi cục bộ là gì?

4. **Thí nghiệm tính toán.** Cài nghịch đảo tuyến tính nhỏ với bộ khử nhiễu kiểu khuếch tán (thậm chí prior làm mờ Gauss) và so tái tạo của cạnh nhìn thấy với cạnh không nhìn thấy.

5. **Khám phá mở.** Đọc Chung và cộng sự (ICLR 2023) hoặc Molinaro và cộng sự (2023) cùng bài bài ngược của chương. Viết một trang về một câu nên xuất hiện trong mọi bài tái tạo học được: sóng trước nào được tuyên bố đến từ dữ liệu?

## Tài liệu

- Hörmander, Tập III–IV; Zworski; các bài bài ngược và hướng nghiên cứu hiện nay của chương này.
- Molinaro, R., và cộng sự. “Neural inverse operators.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
- Song, Y., Shen, L., Xing, L., và Ermon, S. “Solving inverse problems in medical imaging with score-based generative models.” *ICLR* 2022. [arXiv:2111.08005](https://arxiv.org/abs/2111.08005).
- Rasht-Behesht, M., và cộng sự. “PINNs for wave propagation and full waveform inversions.” *JGR: Solid Earth* 127 (2022).
- Moseley, B., Markham, A., và Nissen-Meyer, T. “Finite basis PINNs.” *Adv. Comput. Math.* 49 (2023).
