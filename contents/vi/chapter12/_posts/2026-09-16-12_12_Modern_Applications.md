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

Một mạng nơ-ron huấn luyện bằng sai số $L^2$ có thể dự đoán trường nhiệt độ sai lệch chưa tới $1\%$ về giá trị, nhưng khi kỹ sư lấy đạo hàm để tính **dòng nhiệt** $-k\nabla u$ hay **ứng suất cơ học**, kết quả lại rung lắc hỗn loạn và sai hàng trăm phần trăm! Giải pháp của học máy khoa học hiện đại (Sobolev Training & Neural Operators trong $H^s$) quay trở về đúng trực giác cốt lõi của Chương 12: muốn xấp xỉ vật lý trung thực, ta phải đo sai số trong **chuẩn Sobolev $H^1$** chứ không chỉ chuẩn $L^2$!

## Bản đồ kiến thức nền: Bốn trụ cột của Học Toán tử trong Không gian Sobolev

1. **Chuẩn $H^s$ kiểm soát đồng thời giá trị và đạo hàm**:
   Sai số trong $L^2$ mù trước các dao động nhỏ biên độ nhưng tần số cao; chuẩn Sobolev $\|e\|_{H^1}^2 = \|e\|_{L^2}^2 + \|\nabla e\|_{L^2}^2$ trừng phạt ngay lập tức mọi nhiễu răng cưa phá hủy gradient vật lý.
2. **Ánh xạ liên tục giữa các không gian Sobolev**:
   Trong lý thuyết PDE elliptic, toán tử lời giải $(-\Delta)^{-1}$ ánh xạ liên tục từ $H^{-1}(\Omega)$ vào $H_0^1(\Omega)$ (hoặc từ $L^2$ vào $H^2$). Huấn luyện mạng nơ-ron theo đúng cặp không gian nguồn–đích này bảo toàn tính ổn định của bài toán.
3. **Định lý Xấp xỉ Phổ quát trong $H^s$ và Học có Trọng số Năng lượng**:
   Nhiều bài toán biên elliptic tương đương cực tiểu hóa phiếm hàm năng lượng $J(u) = \frac{1}{2}a(u,u) - \ell(u)$ (Deep Ritz Method)—tận dụng trực tiếp dạng yếu $H^1$ để giảm bậc đạo hàm cần tính bằng tự động vi phân (autodiff).
4. **Học Toán tử trên Hình học Bất kỳ và Miền Rời rạc**:
   Kết hợp không gian hàm Sobolev với lưới đồ thị (GNO) hoặc không gian phần tử hữu hạn (FEM-informed operators) giúp mô hình tổng quát hóa vượt qua lưới chữ nhật đều.

## Mục tiêu

Bài học tùy chọn này sử dụng không gian $$L^p$$, đạo hàm yếu, chuẩn Sobolev và tính đặt chỉnh từ định lý Lax–Milgram làm ngôn ngữ chính thức cho lý thuyết neural operator. Sinh viên cần xác định được ánh xạ học được có tính liên tục trên không gian hàm nào, hiểu vì sao tính bất biến rời rạc hóa là một phát biểu của giải tích hàm, và nắm các công trình giai đoạn 2022–2024 cung cấp tốc độ hội tụ xấp xỉ. Phần lý thuyết dạng yếu của chương vẫn giữ nguyên vai trò nền tảng.

## Kiến thức nền

Sinh viên cần nắm chuẩn $$L^p$$, đạo hàm yếu, các không gian $$H^1$$ và $$H^1_0$$, định lý Lax–Milgram và khái niệm nghiệm yếu của PDE elliptic tuyến tính.

## Dẫn nhập

Mạng nơ-ron trên lưới chỉ là ánh xạ giữa các không gian hữu hạn chiều, còn neural operator được giới thiệu như ánh xạ giữa các không gian hàm. Tuy nhiên, khẳng định đó chỉ có ý nghĩa toán học khi ta chỉ rõ không gian đầu vào và không gian đầu ra. Kovachki và cộng sự (*JMLR* 24(89), 2023) đã thực hiện điều này bằng cách định nghĩa neural operator như hợp thành của các toán tử tích phân affine và phi tuyến tác động giữa các không gian Banach, chứng minh định lý xấp xỉ phổ quát, đồng thời yêu cầu cùng một bộ tham số áp dụng được ở nhiều mức rời rạc hóa khác nhau.

Lanthaler, Mishra và Karniadakis (*Error estimates for DeepONets*, *Transactions of Mathematics and Its Applications*, 2022) đưa ra các ước lượng tốc độ sai số định lượng theo kích thước mạng trunk và branch trong chuẩn vô hạn chiều. De Hoop, Kovachki, Nelsen và Stuart (*Convergence rates for learning linear operators from noisy data*, *SIAM/ASA JUQ*, 2023; [arXiv:2108.12515](https://arxiv.org/abs/2108.12515)) khảo sát trường hợp tuyến tính như bài toán ngược thống kê trên không gian Hilbert. Tài liệu tổng quan năm 2023 của Boullé và Townsend hệ thống hóa các kết quả này theo ngôn ngữ giải tích.

Chương 12 chính là nền tảng mà các công trình đó sử dụng. Khái niệm đạo hàm yếu cho thấy một mô hình có thể hội tụ trong $$L^2$$ nhưng gradient vẫn sai lệch hoàn toàn. Định lý Lax–Milgram khẳng định toán tử nghiệm thực bị chặn từ $$H^{-1}$$ vào $$H^1_0$$; do đó một toán tử học được chỉ bị chặn trên không gian vector nút $$\ell^2$$ thực chất đang trả lời một câu hỏi khác.


### Khung giải thích (nên đọc chậm): Một nhiễu nhỏ $1\%$ trong $L^2$ có thể phá nát đạo hàm trong $H^1$ như thế nào?

Giả sử sai số dự đoán của mạng nơ-ron trên $[0, 2\pi]$ là một gợn sóng biên độ rất nhỏ $e(x) = 0{,}01\sin(100x)$:
1. **Đo bằng chuẩn $L^2$**:
   $$\|e\|_{L^2}^2 = \int_0^{2\pi} (0{,}01)^2 \sin^2(100x)\,dx = 10^{-4} \cdot \pi \approx \mathbf{0{,}000314} \quad (\|e\|_{L^2} \approx 0{,}0177).$$
   Nhìn vào $L^2$ loss, mô hình trông như đã hội tụ cực kỳ đẹp!
2. **Đo phần đạo hàm $e'(x) = 1{,}00\cos(100x)$ trong $H^1$**:
   $$\|e'\|_{L^2}^2 = \int_0^{2\pi} \cos^2(100x)\,dx = \pi \approx \mathbf{3{,}1416} \quad (\|e'\|_{L^2} \approx 1{,}772).$$
   Chỉ vì tần số $k = 100$, bình phương sai số đạo hàm lớn gấp **$10.000$ lần** bình phương sai số $L^2$! Đó là lý do huấn luyện với hàm mất mát Sobolev $H^1$ là bắt buộc khi cần dự đoán gradient hay ứng suất.
## Khái niệm then chốt

### Chỉ rõ không gian và chuẩn sai số

Con số sai số $$10^{-3}$$ chưa mang đủ thông tin nếu không nêu rõ đó là chuẩn $$\|u_\theta-u\|_{L^2}$$, $$\|u_\theta-u\|_{H^1}$$ hay một chuẩn đối ngẫu yếu hơn. Bài toán elliptic thường đòi hỏi chuẩn $$H^1$$ vì năng lượng liên hệ trực tiếp với nửa chuẩn $$H^1$$, trong khi bài toán tiến hóa có thể chỉ cần chuẩn $$L^2$$ theo không gian và đều theo thời gian. Một báo cáo học toán tử chỉ công bố sai số tương đối $$L^2$$ trên một lưới cố định đã bỏ qua phần phát biểu giải tích hàm quan trọng.

### Tính bất biến rời rạc hóa

Một họ ánh xạ rời rạc $$G_h$$ là rời rạc hóa nhất quán của toán tử $$G$$ nếu khi bước lưới $$h\to 0$$, tác động của $$G_h$$ lên dạng rời rạc của $$a$$ hội tụ về dạng rời rạc của $$G(a)$$. Neural operator hướng tới việc để $$G_h$$ dùng chung một bộ tham số trên mọi mức $$h$$. Điều này chỉ khả thi khi kiến trúc được định nghĩa bằng nhân tích phân, nhân tử Fourier hoặc các đối tượng liên tục tương đương, thay vì bằng các ma trận trọng số có kích thước gắn chặt với số nút lưới.

### Phần dư yếu như hàm mất mát vật lý

Dạng yếu $$a(u,v)=\langle f,v\rangle$$ bản thân nó đã xác định một phần dư. Một hàm mất mát tích hợp ràng buộc vật lý có thể phạt đại lượng:

$$
\sup_{\|v\|_{H^1_0}\le 1}\bigl\lvert a(u_\theta,v)-\langle f,v\rangle\bigr\rvert,
$$

chính là chuẩn phần dư trong $$H^{-1}$$. Áp đặt trực tiếp toán tử Laplace dạng mạnh tại các điểm rời rạc (collocation) là lựa chọn chặt hơn về độ trơn nhưng đôi khi kém ổn định hơn. Vì vậy, bước chuyển từ nghiệm mạnh sang nghiệm yếu trong chương không chỉ thuận tiện về lý thuyết mà còn ảnh hưởng trực tiếp đến thiết kế quá trình huấn luyện.

### Tính compact và tốc độ xấp xỉ

Định lý xấp xỉ phổ quát trên tập compact của không gian Banach đòi hỏi tính compact của tập dữ liệu. Giả thiết thường được dùng là phân bố dữ liệu huấn luyện có giá nằm trong một tập bị chặn của $$H^s$$ với $$s$$ đủ lớn để nhúng compact vào không gian làm việc. Nếu dữ liệu chỉ bị chặn trong $$L^2$$, không có định lý nhúng compact nào đảm bảo sự xấp xỉ đều, và không mạng hữu hạn nào đạt độ chính xác đồng đều trên toàn tập. Ở đây, định lý nhúng Sobolev đóng vai trò như điều kiện cảnh báo rõ ràng.

## Phương pháp và kỹ thuật

1. Xác định rõ không gian đầu vào (ví dụ hệ số thuộc $$L^\infty$$, nguồn thuộc $$H^{-1}$$) và không gian đầu ra (ví dụ $$H^1_0$$).
2. Kiểm tra xem kiến trúc mô hình có xác định hợp lệ trên các không gian đó ở mọi độ phân giải hay không.
3. Huấn luyện bằng hàm mất mát tương đương với chuẩn mà bài toán đặt chỉnh, hoặc giải thích rõ lý do nếu chọn chuẩn khác.
4. Kiểm thử trên lưới mịn hơn và trên các họ hàm dao động mạnh hơn để phát hiện các giới hạn liên quan đến tính compact.
5. Với bài toán tuyến tính, đối chiếu trực tiếp toán tử học được với toán tử nghiệm Lax–Milgram trên một cơ sở hàm nguồn.

## Ví dụ

### Ví dụ 1: Thành công trong $$L^2$$ nhưng thất bại trong $$H^1$$

Một mạng nơ-ron có thể xấp xỉ tốt hàm răng cưa theo chuẩn $$L^2$$ trong khi đạo hàm yếu của nó vẫn lệch xa hàm sóng vuông tương ứng. So sánh đồng thời cả hai chuẩn là minh họa trực quan cho ý nghĩa của không gian Sobolev, và các mô hình thay thế cho bài toán Darcy nên báo cáo cả hai loại sai số này.

### Ví dụ 2: Định lý Lax–Milgram như chặn kiểm định tổng quát hóa

Nếu dạng song tuyến tính $$a(\cdot,\cdot)$$ cưỡng bức với hằng số $$\alpha$$, thì $$\|u\|_{H^1}\le\alpha^{-1}\|f\|_{H^{-1}}$$. Một toán tử học được có chuẩn toán tử thực nghiệm giữa các không gian này vượt quá $$C/\alpha$$ với $$C$$ lớn không phải là bộ giải đáng tin cậy, mà là một phép nội suy kém ổn định. Ước lượng chuẩn toán tử thực nghiệm trên tập kiểm thử là một phép kiểm tra ít tốn kém.

### Ví dụ 3: Nửa chuẩn $$H^1$$ rời rạc

```python
import numpy as np

def h1_seminorm(u, dx):
    return np.sqrt(np.sum(np.diff(u)**2 / dx))

x = np.linspace(0, 1, 51)
dx = x[1] - x[0]
print(h1_seminorm(np.sin(2 * np.pi * x), dx), h1_seminorm(np.sin(20 * np.pi * x), dx))
```

Hàm sin tần số cao có giá trị lớn hơn nhiều theo nửa chuẩn $$H^1$$. Một mô hình chỉ huấn luyện theo sai số $$L^2$$ không nhất thiết phân biệt được sự khác biệt này.

## Ứng dụng

Khi các không gian hàm được chỉ rõ, các kết quả thực nghiệm mới có cơ sở so sánh khoa học. Một mô hình dự báo thời tiết có sai số $$L^2$$ nhỏ về nhiệt độ nhưng sai lệch lớn trong $$H^1$$ sẽ cho ra thông lượng nhiệt không sử dụng được. Một toán tử xử lý ảnh y khoa ánh xạ dữ liệu biên trong $$L^2(\partial\Omega)$$ vào bên trong miền trong $$L^2(\Omega)$$ có thể vô tình làm mờ đúng các điểm kỳ dị mà bác sĩ lâm sàng cần quan sát. Định lượng bất định cho toán tử tuyến tính, như trong công trình của de Hoop và cộng sự (2023), đặt bài toán trong đúng bối cảnh thực nghiệm có nhiễu: ta ước lượng phân bố hậu nghiệm trên không gian Hilbert chứ không chỉ trên một vector nút lưới.

Góc nhìn tương tự cũng giúp đánh giá PINN một cách chặt chẽ: phần dư dạng mạnh nhỏ tại các điểm rời rạc không tự động suy ra phần dư $$H^{-1}$$ nhỏ, và do đó không đảm bảo sai số $$H^1$$ nhỏ thông qua định lý Lax–Milgram. Sinh viên đã nắm chứng minh của định lý này sẽ biết cách đọc các bảng đánh giá PINN một cách thận trọng.

## Thách thức và hướng mở rộng

Các toán tử phi tuyến, ánh xạ phụ thuộc thời gian và đầu ra mang giá trị độ đo vượt ra ngoài khuôn khổ Hilbert quen thuộc. Các định lý nhúng Sobolev không còn thuận lợi ở số chiều cao hoặc tại số mũ tới hạn, liên quan trực tiếp đến các PDE có không gian tham số rất nhiều chiều. Hiện tượng răng cưa tần số (aliasing) khi rời rạc hóa có thể phá vỡ hằng số Lipschitz liên tục. Ngoài ra, tốc độ hội tụ thống kê suy giảm khi có nhiễu theo cách mà lý thuyết xấp xỉ thuần túy không nắm bắt hết, và định lý xấp xỉ phổ quát không đảm bảo thuật toán hạ gradient sẽ tìm được bộ tham số tối ưu đó.

Câu hỏi cần đặt ra khi đọc mọi công trình trong lĩnh vực này là: kết quả được phát biểu trong không gian Banach nào, và đó có phải là không gian mà bài toán PDE đặt chỉnh hay không?

## Video tham khảo

- xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Trình bày học toán tử trên không gian hàm như một ứng dụng hiện đại của khuôn khổ Sobolev.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Giới thiệu DeepONet dưới góc nhìn ánh xạ giữa các không gian hàm.
- [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, tiếng Anh. Giải thích không gian Sobolev — nền tảng để phát biểu các ước lượng sai số trong học toán tử.

## Bài tập

1. **Chuẩn không gian và tính liên tục.** Với ánh xạ nghiệm bài toán Poisson Dirichlet $$f\mapsto u$$, hãy nêu tính liên tục từ $$H^{-1}\to H^1_0$$ và từ $$L^2\to H^2\cap H^1_0$$ (trên miền trơn). Một neural operator nên tuyên bố tính liên tục trên cặp không gian nào nếu đầu vào $$f$$ có nhiễu?

2. **Tính compact.** Vì sao một tập dữ liệu huấn luyện bị chặn trong $$H^2$$ lại tạo thành tập compact tương đối trong $$H^1$$ ở một chiều? Điều gì không còn đúng nếu tập đó chỉ bị chặn trong $$H^1$$?

3. **Hàm mất mát dạng yếu.** Viết xấp xỉ Monte Carlo cho phần dư $$H^{-1}$$ của bài toán $$-u''=f$$. Vì sao việc lấy mẫu ngẫu nhiên các hàm thử $$v$$ chỉ cho một chặn dưới của chuẩn phần dư?

4. **Thí nghiệm tính toán.** Lấy hai lưới khác nhau và xét hàm nội suy tuyến tính của một hàm thuộc $$H^1$$ cố định. Tính sai số rời rạc theo chuẩn $$L^2$$ và $$H^1$$ khi làm mịn lưới, sau đó thay phép nội suy bằng một ánh xạ nơ-ron từng điểm huấn luyện trên lưới thô và quan sát sự khác biệt.

5. **Khám phá mở.** Đọc Mục 1–2 trong công trình của Kovachki và cộng sự (2023) hoặc Lanthaler, Mishra và Karniadakis (2022), sau đó viết lại phát biểu của một định lý bằng ký hiệu của chương này.

## Tài liệu

- Brezis; Adams và Fournier, *Sobolev Spaces*.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Lanthaler, S., Mishra, S., và Karniadakis, G. E. “Error estimates for DeepONets.” *Trans. Math. Appl.* 6 (2022). [arXiv:2102.09618](https://arxiv.org/abs/2102.09618).
- de Hoop, M. V., Kovachki, N. B., Nelsen, N. H., và Stuart, A. M. “Convergence rates for learning linear operators from noisy data.” *SIAM/ASA JUQ* 11 (2023). [arXiv:2108.12515](https://arxiv.org/abs/2108.12515).
- Boullé, N., và Townsend, A. “A mathematical guide to operator learning.” 2023. [arXiv:2312.05663](https://arxiv.org/abs/2312.05663).
