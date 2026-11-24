---
layout: post
title: "03-10 Ứng dụng hiện đại: Laplace neural operator và hàm truyền học được"
chapter: '03'
order: 10
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: optional
---


Trong khi Fourier Neural Operator (FNO) tỏa sáng với tín hiệu tuần hoàn, phần lớn hệ thống kỹ thuật ngoài đời thực lại có **đáp ứng tắt dần, tín hiệu quá độ và lực gián đoạn**—những thứ mà biến đổi Fourier khó biểu diễn gọn. **Laplace Neural Operator (LNO)** cùng các mô hình không gian trạng thái sâu hiện đại (S4, Mamba) đã đưa mặt phẳng cực–không $s$ của thế kỷ XIX vào thẳng kiến trúc học sâu để học hàm truyền và giải PDE nhanh vượt trội!

## Bản đồ kiến thức nền: Bốn trụ cột của Biến đổi Laplace trong AI Khoa học

1. **Laplace Neural Operator (LNO)**:
   Phân tách nghiệm thành phần quá độ (tương ứng các cực hữu hạn $s_k$) và phần xác lập (tần số kích thích) ngay trong miền Laplace, khắc phục sai số biên của FNO trên tín hiệu không tuần hoàn.
2. **Học Hàm truyền & Nhận dạng hệ thống (Neural Transfer Functions)**:
   Tham số hóa trực tiếp các cực $p_k$ (ràng buộc $\operatorname{Re}(p_k) < 0$ để **đảm bảo tuyệt đối tính ổn định**) và hệ số thặng dư $r_k$ từ dữ liệu cảm biến đầu vào–đầu ra.
3. **Tích chập dài & Mô hình Không gian Trạng thái S4 / Mamba**:
   Chuỗi dài hàng chục nghìn bước được mô hình hóa như tích chập với nhân hàm mũ suy giảm $K(t) = \mathbf{C}e^{\mathbf{A}t}\mathbf{B}$—chính là biến đổi Laplace ngược của hàm truyền $H(s) = \mathbf{C}(sI - \mathbf{A})^{-1}\mathbf{B}$!
4. **Điều khiển phản hồi & Phân tích độ bền vững**:
   Các mạng điều khiển học được (Neural Controllers) vẫn dựa vào chuẩn $H_\infty$ và vị trí cực miền $s$ để chứng minh hệ không bao giờ mất ổn định khi gặp nhiễu.

## Mục tiêu

Bài đọc tùy chọn này cho thấy biến đổi Laplace, tích chập và góc nhìn hàm truyền của Chương 03 xuất hiện trở lại trong các mô hình học toán tử giai đoạn 2023–2024, tiêu biểu là Laplace neural operator (LNO). Sinh viên sẽ đọc hiểu một lớp cực–thặng dư học từ dữ liệu như một hàm truyền dữ liệu hóa, so sánh học toán tử trong miền Laplace và miền Fourier, đồng thời giải thích vì sao đầu vào gián đoạn vẫn là phép kiểm định quan trọng. Bài không lặp lại bảng biến đổi và kỹ thuật biến đổi ngược cổ điển.

## Kiến thức nền

Sinh viên cần nắm định nghĩa biến đổi Laplace, biến đổi của các hàm sơ cấp, phép phân tích phân thức hữu tỉ khi biến đổi ngược, định lý tích chập và khái niệm hàm truyền $$G(s)=Y(s)/U(s)$$ cho bài toán giá trị đầu (IVP) tuyến tính.

## Dẫn nhập

Biến đổi Laplace đưa bài toán giá trị đầu tuyến tính về đại số: đạo hàm trở thành phép nhân với $$s$$, tích chập trở thành phép nhân thông thường, và hàm truyền mã hóa toàn bộ ánh xạ vào–ra của hệ. Cấu trúc đại số gọn gàng này đặt ra một câu hỏi tự nhiên trong học máy khoa học: liệu một toán tử nơ-ron (neural operator) có nên hoạt động trực tiếp trong miền Laplace hay không?

Cao, Goswami và Karniadakis đã đề xuất Laplace neural operator (LNO) năm 2023 ([arXiv:2303.10528](https://arxiv.org/abs/2303.10528)) và công bố phiên bản tạp chí trên *Nature Machine Intelligence* năm 2024 ([https://doi.org/10.1038/s42256-024-00844-4](https://doi.org/10.1038/s42256-024-00844-4)). LNO học các cực và thặng dư trong miền Laplace, nhờ đó một lớp duy nhất có thể biểu diễn cả đáp ứng quá độ lẫn đáp ứng xác lập, đồng thời xử lý tốt các đầu vào không tuần hoàn — trường hợp mà Fourier neural operator thường gặp hạn chế. Về cấu trúc, đây chính là phiên bản học từ dữ liệu của phép khai triển phân thức hữu tỉ trong chương.

Song song đó, Fourier neural operator (Li và cộng sự, ICLR 2021) cùng khung lý thuyết neural operator của Kovachki và cộng sự (*JMLR* 2023) đã chứng minh hiệu quả của các nhân tử phổ trong việc học ánh xạ giữa các không gian hàm. Miền Laplace là lựa chọn bổ sung tự nhiên cho các hệ động lực nhân quả, một phía theo thời gian — đúng bối cảnh mà Chương 03 sử dụng Laplace thay vì Fourier.

### Khung giải thích (nên đọc chậm): Thấy mối liên hệ trực tiếp giữa một cực học được $p = -0{,}5$ và nhân tích chập S4 $K(t) = r e^{pt}$

Giả sử một lớp S4/LNO học được hàm truyền 1 cực $H(s) = \frac{2}{s + 0{,}5}$ (cực $p = -0{,}5 < 0$, thặng dư $r = 2$):
1. **Nhân đáp ứng xung miền thời gian**: $K(t) = \mathcal{L}^{-1}\!\left\{\frac{2}{s+0{,}5}\right\} = \mathbf{2e^{-0{,}5 t}}$ ($t \ge 0$).
2. **Dự đoán đầu ra cho tín hiệu bậc thang $u(t) = 1$ ($t \ge 0$)**:
   - Trong miền thời gian (tích chập): $y(t) = \int_0^t 2e^{-0{,}5\tau}\cdot 1\,d\tau = \mathbf{4(1 - e^{-0{,}5 t})}$.
   - Trong miền Laplace (nhân trực tiếp): $Y(s) = \frac{2}{s+0{,}5}\cdot\frac{1}{s} = \frac{4}{s} - \frac{4}{s+0{,}5} \implies y(t) = \mathbf{4(1 - e^{-0{,}5 t})}$.
3. **Đảm bảo ổn định bằng tham số hóa**: Chỉ cần đặt $p = -e^\alpha < 0$ với tham số tự do $\alpha \in \mathbb{R}$, mọi trọng số mạng học ra đều tự động có cực nằm bên nửa trái mặt phẳng $s$!

## Khái niệm then chốt

### Cực, thặng dư và hàm truyền học từ dữ liệu

Với hệ tuyến tính, hàm truyền thường có dạng hàm hữu tỉ $$G(s)=\sum_n \beta_n/(s-\mu_n)$$ (trừ phần đa thức nếu có). Một lớp LNO xem các cực $$\mu_n$$ và thặng dư $$\beta_n$$ là tham số huấn luyện, rồi ánh xạ tín hiệu vào sang tín hiệu ra thông qua biểu diễn cực–thặng dư. Nếu đã quen với việc biến đổi ngược $$Y(s)=G(s)U(s)$$ bằng phân tích phân thức, ta có thể hiểu ngay lớp này: thay vì tra bảng và tính tay, mô hình học trực tiếp các cực và thặng dư từ dữ liệu. Điểm mạnh của cách biểu diễn này là khả năng diễn giải trực tiếp: cực gần trục ảo tương ứng thành phần tắt dần chậm; cặp cực phức tương ứng dao động; còn cực nằm ở nửa mặt phẳng phải cho thấy thành phần mất ổn định mà kỹ sư điều khiển cần loại bỏ.

### Tích chập như phiên bản miền thời gian

Theo định lý tích chập, phép nhân với $$G(s)$$ trong miền Laplace tương ứng với phép tích chập cùng đáp ứng xung $$g(t)=\mathcal{L}^{-1}\{G(s)\}$$ trong miền thời gian. Vì vậy, một lớp Laplace học từ dữ liệu thực chất là một toán tử tích chập có cấu trúc, với nhân tích phân là tổng các hàm mũ và dao động tắt dần — đúng họ hàm xuất hiện khi biến đổi ngược các phân thức sơ cấp.

### Đầu vào gián đoạn và tác động xung

Hàm bước đơn vị và hàm delta là lý do kinh điển khiến biến đổi Laplace được ưa chuộng, và chúng cũng là bài kiểm tra nhạy cho các mô hình học toán tử. Các mô hình Fourier trên đoạn hữu hạn tuần hoàn hóa tín hiệu nên dễ biến bước nhảy thành dao động Gibbs; ngược lại, mô hình Laplace mang tính nhân quả một phía có thể giữ nguyên bước nhảy và mô tả đúng quá trình suy giảm qua các cực. Wang, Sankaran và Perdikaris (*CMAME*, 2024) cũng chỉ ra rằng trong mạng PINN, bỏ qua tính nhân quả theo thời gian gây khó khăn lớn khi huấn luyện — nhận xét này cũng có giá trị trực tiếp với học toán tử.

### Từ một bài toán giá trị đầu đến cả họ bài toán tham số

Biến đổi Laplace cổ điển thường dùng để giải từng IVP riêng lẻ, trong khi học toán tử nhắm tới cả một họ bài toán: nhiều tín hiệu kích thích, nhiều trạng thái đầu và nhiều bộ tham số khác nhau. Miền Laplace là không gian thích hợp để chia sẻ cấu trúc chung, vì vị trí các cực của một hệ tuyến tính phụ thuộc vào bản thân hệ chứ không phụ thuộc vào từng đầu vào cụ thể.

## Phương pháp và kỹ thuật

- **PINN miền thời gian.** Xấp xỉ nghiệm $$y_\theta(t)$$ bằng mạng nơ-ron và phạt phần dư $$y'-f$$. Phù hợp với từng bài toán riêng lẻ nhưng kém hiệu quả khi cần suy luận trên họ lớn các đầu vào.
- **Fourier neural operator.** Nhân với trọng số phức học được trong miền Fourier. Hoạt động tốt với các trường tuần hoàn hoặc dừng thống kê, nhưng kém tự nhiên hơn với đáp ứng quá độ không tuần hoàn.
- **Laplace neural operator.** Học trực tiếp biểu diễn cực–thặng dư trong miền Laplace. Phù hợp với bộ dao động tuyến tính và phi tuyến yếu, bài toán dầm và quá trình khuếch tán.

Quy trình biến đổi ngược cổ điển vẫn hữu ích như một công cụ kiểm tra: nếu lớp LNO ước lượng được các cực $$\mu_n$$, ta có thể biến đổi ngược hàm hữu tỉ tương ứng bằng tay và so sánh đáp ứng xung lý thuyết với đầu ra của mạng trước một xung xấp xỉ delta.

## Ví dụ

### Ví dụ 1: Khôi phục hàm truyền mạch RC

Với phương trình $$y'+y=u(t)$$, hàm truyền là $$G(s)=1/(s+1)$$. Khi huấn luyện LNO trên một số đầu vào trơn, mô hình cần khôi phục được cực gần $$-1$$. Phép kiểm định tiếp theo là thử với đầu vào bước đơn vị để kiểm tra đáp ứng $$1-e^{-t}$$: khả năng dự đoán đúng đáp ứng bước (vốn không có trong tập huấn luyện) mới là bằng chứng cho thấy mô hình đã học đúng hàm truyền.

### Ví dụ 2: Vì sao lớp Fourier gặp khó khăn với hàm bước nhân quả

Hàm bước $$u(t)=H(t)$$ không tuần hoàn. Khi tuần hoàn hóa trên đoạn $$[0,T]$$, một bước nhảy giả xuất hiện tại biên nối hai đầu đoạn, gây ra hiện tượng Gibbs trong phổ Fourier. Biểu diễn Laplace không tuần hoàn hóa trục thời gian mà mã hóa trực tiếp bước nhảy qua thừa số $$1/s$$.

### Ví dụ 3: Kiểm tra đáp ứng xung bằng Python

```python
import numpy as np
from scipy.signal import dlti, dimpulse

sys = dlti([0.1], [1, -np.exp(-0.1)])
t, y = dimpulse(sys, n=40)
print(np.array(y[0][:5]).ravel())
```

Một lớp Laplace học từ dữ liệu cần vượt qua phép kiểm tra tương tự: đưa vào một xấp xỉ xung đơn vị, quan sát đầu ra và đối chiếu với $$\mathcal{L}^{-1}\{G(s)\}$$.

## Ứng dụng

Hàm truyền học từ dữ liệu có ứng dụng trực tiếp trong động lực học kết cấu, điều khiển tự động và mô hình giảm bậc. Cao, Goswami và Karniadakis đã thử nghiệm LNO trên bộ dao động Duffing, con lắc, dầm Euler–Bernoulli, bài toán khuếch tán và phản ứng–khuếch tán — đúng nhóm mô hình tuyến tính và phi tuyến yếu quen thuộc trong chương biến đổi Laplace. Lợi thế thực tiễn lớn là tốc độ suy luận thời gian thực: sau khi các cực và thặng dư đã được học, việc dự đoán đáp ứng cho ngoại lực mới chỉ cần phép tính thặng dư gọn nhẹ thay vì chạy lại bộ giải tích phân theo từng bước thời gian.

Trong lĩnh vực điều khiển, LNO có thể được nhìn nhận như một mô hình Bode hoặc cực–không học từ dữ liệu. Tuy nhiên, lưu ý cổ điển vẫn còn nguyên giá trị: các cực ước lượng từ chuỗi dữ liệu ngắn hoặc có nhiễu có thể dịch chuyển sai sang nửa mặt phẳng phải.

## Thách thức và hướng mở rộng

Hệ phi tuyến không có một hàm truyền duy nhất. Tương tự kỹ thuật tuyến tính hóa điều hòa cổ điển, LNO vẫn có thể phát huy tác dụng nhưng các cực hiệu dụng khi đó phụ thuộc vào biên độ. Ngoài ra, nhận dạng hệ thống từ dữ liệu hạn chế thường là bài toán ngược đặt không chỉnh. Các cấu trúc tiên nghiệm Fourier và Laplace cũng có thể được kết hợp trong cùng mô hình. Đầu vào gián đoạn vẫn là thách thức đối với mạng nơ-ron trơn: riêng cấu trúc Laplace không tự động khôi phục trọn vẹn độ sắc nét tại điểm nhảy.

Câu hỏi đặt ra là: học $$G(s)$$ có ý nghĩa gì nếu hệ thực chỉ gần tuyến tính? Định lý tích chập gợi ý một tiêu chí kiểm chứng trực tiếp: nếu mô hình học được không chuyển phép nhân trong miền $$s$$ thành phép tích chập trong miền $$t$$, thì nó chưa thực sự là một hàm truyền bất kể sai số huấn luyện nhỏ đến đâu.

## Video tham khảo

- Xem trước: [Control Systems Lectures - Transfer Functions](https://www.youtube.com/watch?v=RJleGwXorUk) — Brian Douglas, tiếng Anh. Giới thiệu khái niệm hàm truyền cổ điển — đối tượng mà lớp học trong miền Laplace hướng tới mô phỏng.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Trình bày Fourier neural operator, minh họa rõ nguyên lý học ánh xạ giữa không gian hàm vào và ra.
- [The Laplace Transform and the Important Role it Plays](https://www.youtube.com/watch?v=VJ9phDRys_I) — Brian Douglas, tiếng Anh. Phân tích vai trò của biến đổi Laplace trong mô hình hóa hệ tuyến tính nhân quả.

## Bài tập

1. **Biến đổi ngược dạng cực–thặng dư.** Cho $$G(s)=(s+3)/((s+1)(s+2))$$. Hãy phân tích phân thức, tìm đáp ứng xung và phác họa đồ thị. Một lớp Laplace học từ dữ liệu cần khôi phục những đặc trưng nào?

2. **Đầu vào bước so với đầu vào điều hòa.** Giải thích vì sao chỉ khớp $$G(s)$$ trên các tín hiệu sin có thể che khuất sai số thặng dư tại cực thực. Đề xuất một tập huấn luyện giúp phát hiện sai số đó.

3. **Tính nhân quả.** Chứng minh rằng một nhân không nhân quả $$g(-t)$$ không thể là $$\mathcal{L}^{-1}\{G(s)\}$$ của hàm hữu tỉ thực sự $$G(s)$$ có các cực nằm ở nửa mặt phẳng trái. Làm thế nào phát hiện sự vi phạm tính nhân quả trong một toán tử đã huấn luyện?

4. **Thử nghiệm tính toán.** Sử dụng công cụ xử lý tín hiệu trong SciPy hoặc một lớp cực–thặng dư nhỏ bằng PyTorch để khớp $$G(s)=1/(s^2+2s+2)$$ từ vài cặp tín hiệu vào–ra, rồi dự đoán đáp ứng với sóng vuông.

5. **Khám phá mở.** Đọc bài báo về LNO (2023/2024) và viết bài so sánh khoảng một trang với Fourier neural operator: với những bài toán nào trong Chương 03 thì cấu trúc tiên nghiệm Laplace phù hợp hơn?

## Tài liệu

- Boyce và DiPrima, Chương 6; Zill, Chương 7.
- Cao, Q., Goswami, S., và Karniadakis, G. E. “LNO: Laplace neural operator.” [arXiv:2303.10528](https://arxiv.org/abs/2303.10528) (2023); *Nature Machine Intelligence* (2024).
- Li, Z., và cộng sự. “Fourier neural operator for parametric partial differential equations.” *ICLR* 2021.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., Sankaran, S., và Perdikaris, P. “Respecting causality for training physics-informed neural networks.” *CMAME* 421 (2024): 116813.
