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

## Mục tiêu

Bài tùy chọn này cho thấy biến đổi Laplace, tích chập và góc nhìn hàm truyền của chương tái xuất trong các mô hình học toán tử 2023–2024, đặc biệt Laplace neural operator. Sinh viên cần đọc một lớp cực–thặng dư học được như hàm truyền dẫn dữ liệu, so sánh học toán tử Laplace và Fourier, và giải thích vì sao lực không liên tục vẫn là phép thử tự nhiên. Các bảng biến đổi và kỹ thuật đảo đã phát triển được giữ nguyên.

## Kiến thức nền

Sinh viên cần biết định nghĩa biến đổi Laplace, biến đổi các hàm sơ cấp, đảo phân thức, định lý tích chập, và ý niệm hàm truyền $$G(s)=Y(s)/U(s)$$ cho IVP tuyến tính.

## Dẫn nhập

Biến đổi Laplace biến IVP tuyến tính thành đại số. Đạo hàm thành nhân $$s$$, tích chập thành tích, và hàm truyền mã hóa toàn bộ ánh xạ vào–ra. Bức tranh đại số ấy hiệu quả đến mức tự nhiên phải hỏi liệu một neural operator có nên làm việc trong cùng miền.

Cao, Goswami và Karniadakis đưa ra Laplace neural operator (LNO) năm 2023 ([arXiv:2303.10528](https://arxiv.org/abs/2303.10528)) và công bố bản tạp chí trên *Nature Machine Intelligence* năm 2024 ([https://doi.org/10.1038/s42256-024-00844-4](https://doi.org/10.1038/s42256-024-00844-4)). LNO học cực và thặng dư trong miền Laplace, nên một lớp có thể biểu diễn đáp ứng quá độ lẫn xác lập và xử lý đầu vào không tuần hoàn mà Fourier neural operator xử lý vụng. Cấu trúc ấy là bản sao học được của khai triển phân thức đã luyện trong chương.

Đồng thời, Fourier neural operator (Li và cộng sự, ICLR 2021) và lý thuyết neural operator của Kovachki và cộng sự (*JMLR* 2023) cho thấy nhân tử phổ là cách mạnh để học ánh xạ giữa không gian hàm. Góc nhìn Laplace là đối tác tự nhiên cho động lực nhân quả, một phía theo thời gian: đúng bối cảnh chương này chuộng Laplace hơn Fourier.

## Khái niệm then chốt

### Cực, thặng dư, và hàm truyền học được

Với hệ tuyến tính, hàm truyền là hàm hữu tỷ $$G(s)=\sum_n \beta_n/(s-\mu_n)$$, trừ số hạng đa thức. Một lớp LNO xem $$\mu_n$$ và $$\beta_n$$ như tham số huấn luyện, rồi ánh xạ lịch sử vào thành lịch sử ra qua phép tính cực–thặng dư. Sinh viên đã đảo $$Y(s)=G(s)U(s)$$ bằng phân thức đã hiểu lớp ấy: học thay tra bảng. Phần thưởng là khả năng diễn giải. Cực gần trục ảo là mode tắt chậm; cặp cực phức là dao động; cực nửa mặt phẳng phải là mode không ổn định mà kỹ sư điều khiển sẽ loại ngay.

### Tích chập như bản sao miền thời gian

Định lý tích chập nói nhân $$G(s)$$ là tích chập với đáp ứng xung $$g(t)=\mathcal{L}^{-1}\{G(s)\}$$. Một lớp Laplace học được vì thế là toán tử tích chập có cấu trúc, với nhân là tổng mũ và sin tắt dần — cùng họ xuất hiện khi đảo biến đổi sơ cấp.

### Đầu vào không liên tục và xung

Lực bước và delta là lý do cổ điển để chuộng Laplace. Chúng vẫn là benchmark tiết lộ cho bộ giải học được. Mô hình Fourier trên cửa sổ tuần hoàn làm vết nhảy thành dao động Gibbs; mô hình Laplace sở hữu nhân quả một phía có thể giữ nhảy rồi tắt qua đúng mode. Wang, Sankaran và Perdikaris (*CMAME*, 2024) cho thấy, trong bối cảnh PINN, bỏ qua nhân quả thời gian là bệnh huấn luyện. Cảnh báo ấy áp cả cho học toán tử.

### Từ một IVP đến họ tham số

Laplace cổ điển giải một IVP. Học toán tử giải một họ: nhiều lực, nhiều trạng thái đầu, nhiều hệ số. Miền Laplace vẫn là nơi đúng để chia sẻ cấu trúc, vì cực của thiết bị tuyến tính không phụ thuộc đầu vào cụ thể.

## Phương pháp và kỹ thuật

- **PINN miền thời gian.** Biểu diễn $$y_\theta(t)$$ và phạt $$y'-f$$. Tốt cho một trường hợp, vụng cho họ lớn các đầu vào.
- **Fourier neural operator.** Nhân trọng số phức học được trong miền Fourier. Xuất sắc với trường tuần hoàn hoặc dừng thống kê, yếu hơn với quá độ.
- **Laplace neural operator.** Nhân ký hiệu cực–thặng dư học được. Tự nhiên cho dao động tử tuyến tính và phi tuyến yếu, dầm, và khuếch tán.

Quy trình đảo cổ điển vẫn là công cụ gỡ lỗi. Nếu lớp LNO báo cực $$\mu_n$$, hãy đảo hàm hữu tỷ tương ứng bằng tay và so đáp ứng xung với đáp ứng của mạng trước một xấp xỉ delta.

## Ví dụ

### Ví dụ 1: Lấy lại hàm truyền RC

Với $$y'+y=u(t)$$ ta có $$G(s)=1/(s+1)$$. Huấn luyện LNO trên vài đầu vào trơn nên lấy lại cực gần $$-1$$. Phép thử rồi là đáp ứng bước $$1-e^{-t}$$. Khớp trên bước, không trên các đầu vào huấn luyện, mới là bằng chứng đối tượng học được là hàm truyền.

### Ví dụ 2: Vì sao lớp Fourier khó với bước nhân quả

Bước $$u(t)=H(t)$$ không tuần hoàn. Tuần hoàn hóa trên $$[0,T]$$ đưa nhảy vào hai đầu đã đồng nhất và phổ nhiễm Gibbs. Biểu diễn Laplace không tuần hoàn hóa thời gian; nó mã hóa cùng nhảy như thừa số $$1/s$$.

### Ví dụ 3: Đáp ứng xung như unit test

```python
import numpy as np
from scipy.signal import dlti, dimpulse

sys = dlti([0.1], [1, -np.exp(-0.1)])
t, y = dimpulse(sys, n=40)
print(np.array(y[0][:5]).ravel())
```

Một lớp Laplace học được nên chịu cùng phép thử: đưa xấp xỉ xung, đọc đầu ra, so với $$\mathcal{L}^{-1}\{G(s)\}$$.

## Ứng dụng

Hàm truyền học được hữu ích ngay trong động lực kết cấu, điều khiển và mô hình giảm bậc. Cao, Goswami và Karniadakis minh họa LNO trên dao động Duffing và con lắc, dầm Euler–Bernoulli, khuếch tán và phản ứng–khuếch tán — đúng catalog thiết bị tuyến tính và phi tuyến yếu mà khóa Laplace đã xem là chuẩn. Sức hút kỹ thuật là đánh giá thời gian thực: một khi cực và thặng dư đã học, đánh giá lực mới là phép tính thặng dư rẻ chứ không phải chạy time-stepping mới.

Sinh viên điều khiển có thể đọc LNO như mô hình Bode hoặc cực–zero dẫn dữ liệu. Cảnh báo cổ điển vẫn đúng: cực ước lượng từ bản ghi ngắn, nhiễu có thể lang thang sang nửa mặt phẳng phải.

## Thách thức và hướng mở rộng

Hệ phi tuyến không có một hàm truyền duy nhất. LNO, như tuyến tính hóa điều hòa cổ điển, vẫn có thể hữu ích, nhưng cực rồi phụ thuộc biên độ. Nhận dạng từ dữ liệu hạn chế là không đặt chỉnh. Prior Fourier và Laplace cũng có thể kết hợp. Lực không liên tục vẫn tế nhị với mạng trơn; prior Laplace tốt không tự khôi phục độ chính quy của nhảy.

Học $$G(s)$$ nghĩa là gì nếu hệ thật chỉ gần tuyến tính? Định lý tích chập gợi một phép thử: nếu mô hình học được không biến tích trong $$s$$ thành tích chập trong $$t$$, nó không phải hàm truyền, dù lỗi huấn luyện nhỏ đến đâu.

## Bài tập

1. **Đảo cực–thặng dư.** Cho $$G(s)=(s+3)/((s+1)(s+2))$$. Đảo bằng phân thức và phác đáp ứng xung. Lớp Laplace học được phải lấy lại những đặc trưng nào?

2. **Dò bước versus điều hòa.** Giải thích vì sao chỉ khớp $$G(s)$$ trên đầu vào sin có thể giấu thặng dư sai tại cực thực. Thiết kế tập huấn luyện phơi bày lỗi ấy.

3. **Nhân quả.** Chỉ ra nhân không nhân quả $$g(-t)$$ không thể là $$\mathcal{L}^{-1}\{G(s)\}$$ cho $$G$$ hữu tỷ thực sự với cực nửa trái. Làm sao phát hiện phá nhân quả trong toán tử đã huấn luyện?

4. **Thí nghiệm tính toán.** Dùng công cụ tín hiệu SciPy hoặc lớp cực–thặng dư PyTorch nhỏ, khớp $$G(s)=1/(s^2+2s+2)$$ từ vài cặp vào–ra rồi dự đoán đáp ứng sóng vuông.

5. **Khám phá mở.** Đọc bài LNO (2023/2024) và viết so sánh một trang với Fourier neural operator: với bài nào của chương này Laplace là prior trung thực hơn?

## Tài liệu

- Boyce và DiPrima, Chương 6; Zill, Chương 7.
- Cao, Q., Goswami, S., và Karniadakis, G. E. “LNO: Laplace neural operator.” [arXiv:2303.10528](https://arxiv.org/abs/2303.10528) (2023); *Nature Machine Intelligence* (2024).
- Li, Z., và cộng sự. “Fourier neural operator for parametric partial differential equations.” *ICLR* 2021.
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., Sankaran, S., và Perdikaris, P. “Respecting causality for training physics-informed neural networks.” *CMAME* 421 (2024): 116813.
