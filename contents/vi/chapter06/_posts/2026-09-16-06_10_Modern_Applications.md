---
layout: post
title: "06-10 Ứng dụng hiện đại: Cơ sở phổ và học toán tử"
chapter: '06'
order: 10
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này nối chuỗi lũy thừa, nghiệm Frobenius và hàm đặc biệt cổ điển với thực hành 2021–2024 về PINN phổ và học toán tử. Sinh viên cần thấy Chebyshev, Legendre và Fourier như hơn cả họ sách giáo khoa: chúng là tọa độ không gian hàm trong đó các mô hình thay thế hiện đại ổn định nhất. Phương pháp Frobenius và các đồng nhất thức Bessel, Legendre không bị viết lại.

## Kiến thức nền

Sinh viên cần biết điểm thường và điểm kỳ dị chính quy, hệ thức truy hồi cho chuỗi lũy thừa, và tính chất sơ cấp của hàm Bessel, Legendre. Trực giao trên một khoảng là ý bổ sung hữu ích nhất.

## Dẫn nhập

Nghiệm chuỗi là khai triển hàm chưa biết trong một cơ sở mà chính phương trình vi phân gợi ý. Học máy khoa học phát hiện lại cùng chiến thuật. Một multilayer perceptron generic chuộng tần số thấp và khó với lớp biên mỏng hoặc hành vi hàm đặc biệt dao động mạnh; kiến trúc phổ khai triển ẩn số, hoặc toán tử, theo mode Chebyshev, Legendre hoặc Fourier và chỉ học hệ số. Lu, Jin, Pang, Zhang và Karniadakis đưa ra DeepONet trên *Nature Machine Intelligence* (2021) như nhân tử trunk–branch, về tinh thần là khai triển Fourier tổng quát học được. Kovachki và cộng sự (*JMLR* 2023) rồi đặt Fourier, hạng thấp và graph neural operator trên cùng nền Banach.

Ở phía PINN, Wang, Sankaran, Wang và Perdikaris thu thập lời khuyên phổ và kiến trúc trong “An expert’s guide to training physics-informed neural networks” ([arXiv:2308.08468](https://arxiv.org/abs/2308.08468), 2023). Hao và cộng sự (*PINNacle*, NeurIPS 2024; [arXiv:2306.08827](https://arxiv.org/abs/2306.08827)) cho thấy thiên kiến phổ, cấu trúc đa thang và hình học vẫn là chướng ngại bậc nhất trên hơn hai mươi bài PDE. Những chướng ngại ấy đúng là lý do chương này dành thời gian cho hàm đặc biệt: chúng là các cơ sở đã chéo hóa toán tử ta quan tâm.

## Khái niệm then chốt

### Thiên kiến phổ và cơ sở cổ điển

Mạng sâu huấn luyện bằng gradient descent khớp nội dung trơn, tần số thấp trước. Điều ấy hữu ích cho nghiệm giải tích quanh điểm thường và tai hại cho dao động Bessel hoặc lớp mỏng gần điểm kỳ dị chính quy. Khai triển $$u_N(x)=\sum c_n\phi_n(x)$$ với $$\phi_n$$ Chebyshev, Legendre, hoặc họ gợi ý Frobenius chuyển dao động vào cơ sở, nên mạng hoặc bộ giải tuyến tính chỉ thấy hệ số $$c_n$$ biến thiên chậm. Đó cùng lý do ta dùng ansatz Frobenius $$x^r\sum a_k x^k$$ thay vì chuỗi lũy thừa trần tại điểm kỳ dị.

### DeepONet như khai triển hàm đặc biệt học được

DeepONet viết toán tử $$\mathcal{G}(a)(x)\approx\sum_k b_k(a)\,t_k(x)$$. Các trunk $$t_k$$ đóng vai hàm đặc biệt học được của biến độc lập; các branch $$b_k$$ đóng vai hệ số phụ thuộc hàm đầu vào $$a$$. Khi toán tử nghiệm thật compact hoặc có trị riêng suy giảm nhanh, cơ sở trunk ngắn đủ, cũng như vài đa thức Legendre đủ cho nghiệm trơn của bài Sturm–Liouville chính quy.

### Truy hồi, ổn định, và đánh giá

Hàm đặc biệt cổ điển đi kèm truy hồi ổn định số nếu dùng đúng chiều. Mô hình phổ học được cần analogue: trực giao hóa, phạt suy giảm phổ, hoặc ràng buộc cứng hệ số mode cao phải nhỏ. Không kỷ luật ấy ta tái nhập phân kỳ mà chuỗi lũy thừa bất cẩn đã thể hiện ngoài bán kính hội tụ.

### Ứng dụng vật lý như phép thử học toán tử

Màng dao động và Schrödinger hướng kính của chương không chỉ là ứng dụng lịch sử. Chúng là benchmark sạch: thừa số Fourier góc nhân thừa số Bessel hoặc Legendre kính. Neural operator không lấy lại những tách ấy thì chưa tôn trọng hình học mà hàm đặc biệt mã hóa.

## Phương pháp và kỹ thuật

- **PINN phổ.** Thay đầu ra mạng bằng khai triển trực giao cụt và huấn luyện hệ số, đôi khi với phần dư tính bằng quadrature.
- **Trunk lai.** Đóng băng $$t_k$$ như Chebyshev hoặc hàm riêng và chỉ học hệ số branch — DeepONet với trunk cổ điển.
- **Fourier / Laplace neural operator.** Học nhân tử trong miền phổ rồi đảo. Đây là nghiệm chuỗi ở cấp toán tử chứ không phải hàm.

Trong mỗi trường hợp, bán kính hội tụ, trọng số trực giao, và phân biệt điểm thường/kỳ dị vẫn là chẩn đoán đúng.

## Ví dụ

### Ví dụ 1: Hệ số Legendre như trunk học được

Nghiệm của $$(1-x^2)y''-2x y'+n(n+1)y=0$$ là $$P_n(x)$$. Nếu trunk DeepONet đủ khả năng trên $$[-1,1]$$ và họ huấn luyện gồm các bài hàm riêng ấy, một hàm trunk nên tương quan mạnh với $$P_n$$.

### Ví dụ 2: Số mũ Frobenius như đặc trưng

Gần điểm kỳ dị chính quy, số mũ đầu $$r$$ là ẩn đại số. Mạng lấy $$\log x$$ hoặc $$x^r$$ làm đầu vào đang làm Frobenius bằng tay. Không đặc trưng ấy nó sẽ tốn dung lượng để bịa điểm rẽ nhánh, thường không thành công. Đây là một thất bại đa thang được tài liệu PINN 2023–2024 và PINNacle ghi nhận.

### Ví dụ 3: Phần dư Chebyshev

```python
import numpy as np

n = 8
k = np.arange(n + 1)
x = np.cos(np.pi * k / n)
c = np.polynomial.chebyshev.chebfit(x, np.exp(x), n)
xx = np.linspace(-1, 1, 200)
uu = np.polynomial.chebyshev.chebval(xx, c)
print(np.max(np.abs(uu - np.exp(xx))))
```

PINN phổ không thắng lỗi này trên mục tiêu giải tích đang lãng phí cơ sở mà chương đã cung cấp.

## Ứng dụng

Học toán tử phổ nay dùng cho PDE tham số trong chất lưu, truyền bức xạ và điện từ, nơi nghiệm thật là khai triển theo hàm điều hòa trụ hoặc cầu. Surrogate cơ lượng tử cho toán tử Schrödinger kính là tiếp nối trực tiếp các ứng dụng vật lý của chương. Trong kỹ thuật, PINN Chebyshev xuất hiện như bộ giải trong rẻ bên trong vòng thiết kế.

Góc nhìn hàm đặc biệt cũng giúp giao tiếp giữa nhà giải tích và nhà tính toán. Nói “trunk học được cơ sở kính kiểu Bessel” giàu thông tin hơn “mạng tổng quát hóa”. Đó là đóng góp từ vựng của chương này cho tài liệu 2022–2026.

## Thách thức và hướng mở rộng

Phương pháp phổ ghét bất liên tục; hiện tượng Gibbs tái xuất trong mô hình Fourier và Chebyshev học được. Hình học là chướng ngại khác: cơ sở cho khoảng không tự chuyển sang vành khuyên hoặc mặt cầu, vì thế spherical FNO (Bonev và cộng sự, ICML 2023) phải được phát minh. Lý thuyết xấp xỉ DeepONet trong chiều vô hạn (Lanthaler, Mishra và Karniadakis, 2022) cho tốc độ theo độ rộng trunk và branch, nhưng các tốc độ ấy giả định độ trơn mà điểm kỳ dị chính quy có thể phá. Cơ sở học được mặc định không trực giao, nên độ lớn hệ số không đọc được như năng lượng trừ khi tái trực giao hóa.

Câu hỏi hay: trunk nơ-ron là hàm đặc biệt mới, hay xấp xỉ số của hàm cũ? Câu trả lời phụ thuộc việc trunk có còn thỏa truy hồi có cấu trúc hoặc đồng nhất thức Sturm–Liouville sau huấn luyện hay không.

## Bài tập

1. **Bán kính hội tụ.** Khớp chuỗi lũy thừa và chuỗi Chebyshev với $$1/(1+25x^2)$$ trên $$[-1,1]$$. Vì sao cái thứ nhất phân kỳ ở đầu mút trong giới hạn bậc cao còn cái thứ hai thì không nhất thiết?

2. **Nhận dạng trunk–branch.** Với toán tử ánh xạ $$f$$ sang nghiệm của $$y''=f$$, $$y(\pm 1)=0$$, đề xuất trunk cổ điển và nói branch phải tính gì.

3. **Đặc trưng Bessel.** Giải thích cách mã hóa số mũ Frobenius của phương trình Bessel cấp $$\nu$$ như đầu vào mạng. Điều gì sai nếu $$\nu$$ không nguyên và nghiệm thứ hai chứa $$\log x$$?

4. **Thí nghiệm tính toán.** Huấn luyện mô hình kiểu DeepONet nhỏ, hoặc surrogate phổ tuyến tính, ánh xạ nguồn $$f$$ sang nghiệm của $$-y''=f$$ trên $$[0,\pi]$$ với dữ liệu Dirichlet, dùng trunk sin. So hệ số với chuỗi sin Fourier đúng.

5. **Khám phá mở.** Đọc bài DeepONet (2021) và báo cáo PINNacle (2024) rồi viết ghi chú ngắn về khi nào trunk hàm đặc biệt cổ điển nên bị đóng băng chứ không học.

## Tài liệu

- Boyce và DiPrima, Chương 5; Haberman, về ứng dụng Bessel và Legendre.
- Lu, L., và cộng sự. “Learning nonlinear operators via DeepONet.” *Nature Machine Intelligence* 3 (2021): 218–229.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., và cộng sự. “An expert’s guide to training physics-informed neural networks.” 2023. [arXiv:2308.08468](https://arxiv.org/abs/2308.08468).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024 Datasets and Benchmarks. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
