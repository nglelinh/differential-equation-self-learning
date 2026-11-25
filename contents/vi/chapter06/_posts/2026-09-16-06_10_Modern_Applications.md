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

Đa thức Legendre, hàm Chebyshev hay hàm Bessel không phải là di vật bảo tàng thế kỷ 19. Trong điện toán khoa học và AI vật lý hiện đại (2020–2026), chúng chính là **cơ sở phổ (spectral basis)** giúp đạt độ chính xác 15 chữ số chỉ với vài chục bậc tự do—và là xương sống của các mô hình **Học toán tử (Operator Learning / DeepONet / Neural Spectral Methods)** dự báo thời tiết và khí động học nhanh hơn mô phỏng truyền thống hàng nghìn lần!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Phổ & Học Toán tử hiện đại

1. **Hội tụ phổ (Spectral Convergence)**:
   Trong khi sai phân hữu hạn bậc 2 giảm sai số theo lũy thừa $O(N^{-2})$, khai triển theo đa thức trực giao (Legendre/Chebyshev) cho hàm trơn giảm sai số theo **hàm mũ $O(e^{-\alpha N})$**!
2. **Chiếu Galerkin & Điểm nút Gauss–Lobatto**:
   Chiếu phương trình vi phân lên không gian con hữu hạn sinh bởi $\{P_0, \dots, P_N\}$ biến PTVP thành hệ ma trận thưa/băng giải cực nhanh, không gặp hiện tượng dao động biên Runge.
3. **Học Toán tử (Neural Operators — DeepONet, Spectral Neural Operators)**:
   Thay vì giải lại PTVP từ đầu mỗi khi đổi điều kiện đầu $u_0(x)$, mạng học trực tiếp ánh xạ vô hạn chiều $\mathcal{G}: u_0 \mapsto u(\cdot, T)$ bằng cách học các hệ số trong cơ sở phổ!
4. **Cầu điều hòa (Spherical Harmonics) trong AI khí hậu & Hóa học lượng tử**:
   Tổ hợp đa thức Legendre liên kết $P_\ell^m(\cos\theta)e^{im\phi}$ là cơ sở tự nhiên trên mặt cầu dùng trong mô hình dự báo thời tiết AI toàn cầu (SFNO/FourCastNet) và mạng nơ-ron phân tử đẳng biến $E(3)$.

## Mục tiêu

Bài học tùy chọn này kết nối chuỗi lũy thừa, nghiệm Frobenius và các hàm đặc biệt cổ điển với thực hành nghiên cứu giai đoạn 2021–2024 về mạng nơ-ron tích hợp vật lý (PINN) theo miền phổ và học toán tử. Sinh viên cần nhìn nhận các họ Chebyshev, Legendre và Fourier không chỉ là bài học sách giáo khoa mà là những hệ tọa độ trong không gian hàm giúp các mô hình thay thế hiện đại đạt độ ổn định cao. Phương pháp Frobenius và các đồng nhất thức Bessel, Legendre vẫn giữ nguyên vai trò nền tảng.

## Kiến thức nền

Sinh viên cần nắm khái niệm điểm thường, điểm kỳ dị chính quy, hệ thức truy hồi của chuỗi lũy thừa và các tính chất cơ bản của hàm Bessel, Legendre. Hiểu về tính trực giao trên một khoảng là nền tảng bổ trợ quan trọng nhất.

## Dẫn nhập

Nghiệm chuỗi thực chất là phép khai triển hàm ẩn trong một cơ sở do chính phương trình vi phân gợi ý. Học máy khoa học (SciML) ngày nay tái khám phá chiến lược tương tự. Một mạng perceptron đa tầng thông thường có xu hướng ưu tiên học các thành phần tần số thấp và gặp khó khăn trước lớp biên mỏng hoặc các dao động nhanh kiểu hàm đặc biệt; ngược lại, kiến trúc phổ khai triển nghiệm (hoặc toán tử) theo các chế độ Chebyshev, Legendre hay Fourier rồi chỉ học các hệ số. Lu, Jin, Pang, Zhang và Karniadakis đã giới thiệu DeepONet trên *Nature Machine Intelligence* (2021) với cấu trúc tích nhánh–thân (branch–trunk), về tinh thần tương tự một khai triển Fourier tổng quát được học từ dữ liệu. Sau đó, Kovachki và cộng sự (*JMLR* 2023) đặt các kiến trúc toán tử nơ-ron Fourier, hạng thấp và đồ thị trên cùng một nền tảng không gian Banach.

Ở nhánh PINN, Wang, Sankaran, Wang và Perdikaris tổng hợp các hướng dẫn thực hành về kiến trúc và phổ trong bài viết “An expert’s guide to training physics-informed neural networks” ([arXiv:2308.08468](https://arxiv.org/abs/2308.08468), 2023). Hao và cộng sự (*PINNacle*, NeurIPS 2024; [arXiv:2306.08827](https://arxiv.org/abs/2306.08827)) cũng cho thấy thiên kiến phổ, cấu trúc đa thang và hình học miền vẫn là những thách thức hàng đầu trên hơn hai mươi bài toán PDE chuẩn. Đây chính là lý do chương này dành nhiều thời lượng cho hàm đặc biệt: chúng là những hệ cơ sở chéo hóa sẵn các toán tử vi phân quan trọng.

### Giải thích: So sánh tốc độ hội tụ giữa Sai phân hữu hạn $O(N^{-2})$ và Cơ sở Phổ $O(e^{-N})$ bằng con số

Giả sử bạn cần xấp xỉ nghiệm trơn của một PTVP với sai số mục tiêu $\varepsilon = 10^{-8}$:
- **Sai phân hữu hạn bậc 2** (sai số $\approx 1/N^2$): Cần $1/N^2 \le 10^{-8} \implies N \ge \mathbf{10.000\text{ điểm lưới}}$!
- **Cơ sở phổ Legendre/Chebyshev** (sai số $\approx e^{-N}$): Cần $e^{-N} \le 10^{-8} \implies N \ge \ln(10^8) \approx \mathbf{19\text{ hàm cơ sở}}$!

Chỉ với **19 hệ số phổ** thay vì **10.000 điểm lưới** (nén bậc tự do hơn **$500\times$**!), phương pháp phổ và các mạng Neural Operator dựa trên cơ sở phổ đạt cùng độ chính xác $10^{-8}$ với chi phí tính toán nhỏ hơn hàng bậc độ lớn.

## Khái niệm then chốt

### Thiên kiến phổ và các hệ cơ sở cổ điển

Mạng sâu huấn luyện bằng hạ gradient thường khớp các thành phần trơn, tần số thấp trước. Đặc tính này thuận lợi cho nghiệm giải tích quanh điểm thường nhưng bất lợi đối với dao động kiểu Bessel hoặc lớp biên mỏng gần điểm kỳ dị chính quy. Việc khai triển $$u_N(x)=\sum c_n\phi_n(x)$$ với cơ sở $$\phi_n$$ là đa thức Chebyshev, Legendre hoặc họ hàm gợi ý từ Frobenius giúp chuyển phần dao động vào bản thân hàm cơ sở, để mạng nơ-ron hay bộ giải tuyến tính chỉ cần tìm các hệ số $$c_n$$ biến thiên chậm. Điều này tương đồng với lý do ta chọn dạng thử Frobenius $$x^r\sum a_k x^k$$ thay cho chuỗi lũy thừa thông thường tại điểm kỳ dị.

### DeepONet như khai triển hàm đặc biệt học được

DeepONet xấp xỉ toán tử theo dạng $$\mathcal{G}(a)(x)\approx\sum_k b_k(a)\,t_k(x)$$. Trong đó, các hàm thân (trunk) $$t_k$$ đóng vai trò như họ hàm đặc biệt học được của biến không gian, còn các hàm nhánh (branch) $$b_k$$ đóng vai trò các hệ số phụ thuộc vào hàm đầu vào $$a$$. Khi toán tử nghiệm thật là compact hoặc có trị riêng suy giảm nhanh, chỉ cần một số lượng nhỏ hàm thân là đủ — tương tự như chỉ cần vài đa thức Legendre để xấp xỉ tốt nghiệm trơn của bài toán Sturm–Liouville chính quy.

### Truy hồi, tính ổn định và đánh giá số

Các hàm đặc biệt cổ điển đi kèm những hệ thức truy hồi ổn định về mặt số học khi được tính theo đúng chiều. Các mô hình phổ học được cũng cần cơ chế tương ứng: trực giao hóa, thêm số hạng phạt suy giảm phổ hoặc ràng buộc hệ số ở các bậc cao phải nhỏ. Nếu thiếu kỷ luật này, mô hình dễ rơi vào hiện tượng phân kỳ tương tự như khi sử dụng chuỗi lũy thừa ngoài bán kính hội tụ.

### Ứng dụng vật lý làm bài toán kiểm chuẩn cho học toán tử

Các bài toán màng dao động và phương trình Schrödinger hướng kính trong chương không chỉ mang ý nghĩa lịch sử mà còn là bài toán kiểm chuẩn rõ ràng: nghiệm có dạng tích giữa thành phần Fourier theo góc và thành phần Bessel hoặc Legendre theo hướng kính. Nếu một toán tử nơ-ron không tái hiện được cấu trúc tách biến đó, mô hình vẫn chưa tôn trọng đầy đủ hình học mà hàm đặc biệt đã mã hóa.

## Phương pháp và kỹ thuật

- **PINN phổ.** Thay đầu ra trực tiếp của mạng bằng một khai triển trực giao cắt cụt và huấn luyện các hệ số, thường kết hợp tính phần dư bằng cầu phương số (quadrature).
- **Mạng thân lai.** Cố định các hàm thân $$t_k$$ là đa thức Chebyshev hoặc hàm riêng giải tích, chỉ huấn luyện các hệ số nhánh — tức là DeepONet với cơ sở thân cổ điển.
- **Toán tử nơ-ron Fourier / Laplace.** Học trực tiếp phép nhân trong miền phổ rồi biến đổi ngược; đây là phiên bản ở cấp độ toán tử của phương pháp nghiệm chuỗi.

Trong mọi cách tiếp cận trên, bán kính hội tụ, hàm trọng số trực giao và sự phân biệt giữa điểm thường với điểm kỳ dị vẫn là các tiêu chí chẩn đoán quan trọng.

## Ví dụ

### Ví dụ 1: Đa thức Legendre như cơ sở thân học được

Nghiệm của phương trình $$(1-x^2)y''-2x y'+n(n+1)y=0$$ là các đa thức Legendre $$P_n(x)$$. Nếu mạng thân của DeepONet có đủ năng lực biểu diễn trên $$[-1,1]$$ và tập huấn luyện gồm các bài toán hàm riêng dạng này, các hàm thân học được sẽ tương quan chặt với $$P_n$$.

### Ví dụ 2: Số mũ Frobenius như đặc trưng đầu vào

Gần một điểm kỳ dị chính quy, số mũ đặc trưng đầu $$r$$ mang thông tin đại số cốt lõi của nghiệm. Một mạng nơ-ron đưa $$\log x$$ hoặc $$x^r$$ làm đặc trưng đầu vào thực chất đang tích hợp sẵn tư tưởng Frobenius. Nếu không có đặc trưng này, mạng phải tiêu tốn nhiều năng lực biểu diễn để cố xấp xỉ điểm rẽ nhánh và thường thất bại. Đây là một dạng thất bại đa thang đã được ghi nhận trong tài liệu PINN giai đoạn 2023–2024 và bộ kiểm chuẩn PINNacle.

### Ví dụ 3: Kiểm tra sai số xấp xỉ Chebyshev

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

Một PINN phổ không đạt được mức sai số tương đương trên một hàm mục tiêu giải tích như vậy cho thấy nó chưa tận dụng hiệu quả cơ sở hàm mà chương đã cung cấp.

## Ứng dụng

Các phương pháp học toán tử phổ hiện được ứng dụng cho nhiều bài toán PDE có tham số trong cơ học chất lưu, truyền bức xạ và điện từ học — những lĩnh vực có nghiệm tự nhiên dưới dạng khai triển theo hàm điều hòa trụ hoặc cầu. Mô hình thay thế trong cơ học lượng tử cho toán tử Schrödinger hướng kính là sự nối tiếp trực tiếp các ứng dụng vật lý của chương. Trong kỹ thuật, PINN dùng cơ sở Chebyshev thường đóng vai trò bộ giải nội bộ chi phí thấp trong vòng lặp tối ưu thiết kế.

Ngôn ngữ hàm đặc biệt cũng tạo cầu nối chính xác giữa nhà giải tích và nhà tính toán khoa học: nhận định “mạng thân đã học được một cơ sở hướng kính dạng Bessel” truyền đạt nhiều thông tin cấu trúc hơn hẳn nhận định chung chung “mạng tổng quát hóa tốt”.

## Thách thức và hướng mở rộng

Phương pháp phổ gặp khó khăn trước các nghiệm có điểm gián đoạn; hiện tượng Gibbs vẫn tái xuất hiện trong các mô hình Fourier và Chebyshev học được. Hình học miền tính toán cũng là một thách thức lớn: cơ sở trên đoạn thẳng không tự động chuyển sang vành khuyên hay mặt cầu, dẫn tới sự ra đời của kiến trúc spherical FNO (Bonev và cộng sự, ICML 2023). Lý thuyết xấp xỉ cho DeepONet trong không gian vô hạn chiều (Lanthaler, Mishra và Karniadakis, 2022) đưa ra tốc độ hội tụ theo độ rộng mạng thân và mạng nhánh, nhưng các ước lượng này giả định độ trơn vốn có thể bị phá vỡ tại điểm kỳ dị chính quy. Ngoài ra, cơ sở học được mặc định không trực giao, nên độ lớn hệ số không thể diễn giải trực tiếp như phân bố năng lượng nếu không trực giao hóa lại.

Một câu hỏi mở đáng chú ý là: mạng thân nơ-ron có tạo ra hàm đặc biệt mới hay chỉ là xấp xỉ số của các hàm cổ điển? Câu trả lời phụ thuộc vào việc các hàm thân sau huấn luyện có còn thỏa mãn những hệ thức truy hồi có cấu trúc hoặc đồng nhất thức Sturm–Liouville hay không.

## Video tham khảo

- Xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu toán tử nơ-ron Fourier sử dụng cơ sở phổ, gắn trực tiếp với nội dung bài học.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Giới thiệu DeepONet với kiến trúc nhánh–thân (branch–trunk) bên cạnh các cơ sở phổ.
- [Taylor series | Chapter 11, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — 3Blue1Brown, tiếng Anh. Chuỗi cổ điển đóng vai trò cơ sở phổ dựng tay mà các mạng học toán tử tổng quát hóa.

## Bài tập

1. **Bán kính hội tụ.** So sánh khai triển chuỗi lũy thừa và khai triển Chebyshev của hàm $$1/(1+25x^2)$$ trên đoạn $$[-1,1]$$. Giải thích vì sao chuỗi lũy thừa phân kỳ gần hai đầu mút khi tăng bậc còn chuỗi Chebyshev vẫn hội tụ.

2. **Nhận dạng cấu trúc nhánh–thân (branch–trunk).** Xét toán tử ánh xạ hàm nguồn $$f$$ sang nghiệm của bài toán $$y''=f$$, $$y(\pm 1)=0$$. Hãy đề xuất một họ hàm thân cổ điển phù hợp và nêu rõ mạng nhánh cần tính đại lượng nào.

3. **Đặc trưng Bessel.** Giải thích cách mã hóa số mũ Frobenius của phương trình Bessel bậc $$\nu$$ thành đặc trưng đầu vào cho mạng nơ-ron. Điều gì xảy ra nếu $$\nu$$ là số nguyên và nghiệm độc lập thứ hai chứa số hạng $$\log x$$?

4. **Thí nghiệm tính toán.** Huấn luyện một mô hình dạng DeepONet nhỏ, hoặc một mô hình thay thế phổ tuyến tính, ánh xạ nguồn $$f$$ sang nghiệm của $$-y''=f$$ trên $$[0,\pi]$$ với điều kiện biên Dirichlet bằng cách dùng cơ sở thân hàm sin. Đối chiếu các hệ số thu được với chuỗi sin Fourier chính xác.

5. **Khám phá mở.** Đọc bài báo DeepONet (2021) và báo cáo PINNacle (2024), sau đó viết một ghi chú ngắn phân tích trong trường hợp nào nên giữ cố định cơ sở thân bằng các hàm đặc biệt cổ điển thay vì huấn luyện tự do.

## Tài liệu

- Boyce và DiPrima, Chương 5; Haberman, về ứng dụng hàm Bessel và Legendre.
- Lu, L., và cộng sự. “Learning nonlinear operators via DeepONet.” *Nature Machine Intelligence* 3 (2021): 218–229.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., và cộng sự. “An expert’s guide to training physics-informed neural networks.” 2023. [arXiv:2308.08468](https://arxiv.org/abs/2308.08468).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024 Datasets and Benchmarks. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
