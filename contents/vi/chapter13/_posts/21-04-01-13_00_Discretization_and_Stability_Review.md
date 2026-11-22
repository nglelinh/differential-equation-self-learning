---
layout: post
title: "Ôn Tập Nền Tảng: Rời Rạc Hóa, Xấp Xỉ Taylor, và Trực Giác Ổn Định"
chapter: '13'
order: 0
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: optional
---

## Mục tiêu

Bài hỗ trợ này xây dựng nền tảng khái niệm cho toàn bộ giải tích số phương trình vi phân trước khi đi vào từng lược đồ cụ thể. Sau bài học, sinh viên cần hiểu vì sao phải rời rạc hóa, cách khai triển Taylor làm cơ sở cho các công thức tiến thời gian, sự khác biệt giữa sai số cục bộ và sai số toàn cục, và vì sao tính ổn định là thuộc tính của chính phương pháp số chứ không chỉ của phương trình vi phân gốc.

## Vì Sao Bài Này Cần Thiết

Nhiều sinh viên tiếp cận phương pháp số với nền tảng giải tích tốt nhưng lại xem phương pháp số chỉ là công cụ tính gần đúng tự động cho cùng một đối tượng liên tục. Thực tế, ngay khi chuyển từ mô hình liên tục sang thuật toán rời rạc, ta đã tạo ra một bài toán toán học mới: phương trình vi phân xác định trên miền liên tục, còn phương pháp số vận hành trên một lưới điểm hữu hạn, nên hành vi của hệ rời rạc phải được khảo sát riêng biệt.

Đó là tư tưởng xuyên suốt Chương 13. Từ phương pháp Euler, Runge–Kutta, phương pháp nhiều bước, bộ giải bài toán cứng đến sai phân hữu hạn và phần tử hữu hạn, tất cả đều xuất phát từ cùng một nhận thức:

> Phương trình vi phân xác định liên tục theo thời gian hoặc không gian, nhưng máy tính chỉ có thể cập nhật hữu hạn giá trị tại hữu hạn điểm lưới.

Bài học này làm rõ bước chuyển đổi đó trước khi sinh viên tiếp cận lược đồ đầu tiên.

## Kiến thức nền

Sinh viên cần nắm bài toán giá trị ban đầu cho ODE, khai triển Taylor, ý nghĩa hình học của đạo hàm và thực tế rằng nhiều mô hình không có nghiệm đóng. Bài học chưa đòi hỏi kiến thức trước về lý thuyết ổn định số.

## 1. Từ Mô Hình Liên Tục Sang Quá Trình Rời Rạc

Xét bài toán giá trị ban đầu $$ y'(t)=f(t,y(t)), \qquad y(t_0)=y_0 $$. Về mặt giải tích, ẩn số là một hàm xác định trên cả một khoảng thời gian liên tục. Về mặt tính toán, máy tính không thể lưu vô hạn giá trị mà chỉ lưu các giá trị xấp xỉ tại các mốc thời gian rời rạc $$ t_n=t_0+nh $$. Do đó, bước đầu tiên của giải tích số là thay miền liên tục bằng một lưới điểm: thay vì tìm hàm chính xác $$ y(t) $$ tại mọi $$ t $$, ta xây dựng một dãy số $$ y_0, y_1, y_2, \dots $$ xấp xỉ nghiệm thật tại các điểm lưới.

Vì vậy, một phương pháp số không đơn thuần là cách viết lại phương trình vi phân mà thực chất là một hệ động lực rời rạc. Hệ rời rạc này có thể bảo toàn cấu trúc của bài toán liên tục, làm biến dạng nó, ổn định hóa nó hoặc làm nó mất ổn định.

### Ý nghĩa ứng dụng

Trong thực tế, rời rạc hóa là một lựa chọn về độ phân giải quan sát. Các mô hình thời tiết, mạch điện hay quần thể luôn được cập nhật theo từng bước thời gian, và việc chọn độ lớn bước $$ h $$ hàm chứa giả thiết về những thang thời gian cần nắm bắt.

## 2. Khai Triển Taylor Như Nguyên Lý Số Học Đầu Tiên

Cơ sở trực tiếp nhất cho các lược đồ tiến thời gian là định lý Taylor. Nếu nghiệm thật đủ trơn, tại lân cận $$ t_n $$ ta có:

$$ y(t_n+h)=y(t_n)+hy'(t_n)+\frac{h^2}{2}y''(\xi_n) $$

với một điểm trung gian $$ \xi_n $$ giữa $$ t_n $$ và $$ t_n+h $$.

Thay $$ y'(t_n)=f(t_n,y(t_n)) $$, phép xấp xỉ bậc nhất cho $$ y(t_n+h)\approx y(t_n)+h f(t_n,y(t_n)) $$, chính là nguồn gốc của phương pháp Euler. Tổng quát hơn, mọi phương pháp một bước (one-step method) đều có thể hiểu như một phép xấp xỉ có kiểm soát đối với khai triển Taylor cục bộ của nghiệm thật.

### Vì sao Taylor quan trọng vượt ra ngoài phương pháp Euler

Các phương pháp Runge–Kutta bậc cao, dự đoán–hiệu chỉnh (predictor–corrector) hay sai phân hữu hạn khác nhau ở mức độ khớp với nhiều số hạng hơn trong khai triển Taylor. Trong giải tích số, bậc chính xác đo mức độ trung thực của quy tắc rời rạc đối với hành vi cục bộ của nghiệm trơn.

## 3. Sai Số Cục Bộ Và Sai Số Toàn Cục

Một nhầm lẫn thường gặp khi mới học giải tích số là đồng nhất sai số trong một bước với sai số tích lũy sau nhiều bước.

### Sai số cục bộ

Sai số cục bộ đo độ lệch sinh ra sau đúng một bước tính nếu ta xuất phát từ giá trị chính xác của nghiệm thật tại $$ t_n $$. Đại lượng này đánh giá độ chính xác của công thức xấp xỉ trên từng bước đơn lẻ.

### Sai số toàn cục

Sai số toàn cục đo hiệu giữa dãy nghiệm số và nghiệm thật sau nhiều bước. Nó phản ánh đồng thời hai yếu tố:

- sai số cục bộ phát sinh tại mỗi bước,
- sự lan truyền và khuếch đại của các sai số từ những bước trước đó.

Sự phân biệt này rất quan trọng: một phương pháp có sai số cục bộ nhỏ vẫn có thể cho kết quả kém trên khoảng thời gian dài nếu lược đồ khuếch đại nhiễu.

### Quan hệ định tính

Với phương pháp bậc nhất như Euler tiến, sai số cục bộ có bậc $$ O(h^2) $$, trong khi sai số toàn cục có bậc $$ O(h) $$. Việc giảm đi một lũy thừa của $$ h $$ là do trên một khoảng thời gian cố định có khoảng $$ 1/h $$ bước nên các sai số cục bộ cộng dồn lại. Điều này cho thấy giải tích số là sự kết hợp giữa lý thuyết xấp xỉ và cơ chế lan truyền sai số.

## 4. Ổn Định: Phương Pháp Số Có Động Lực Riêng

Trong giải tích số cho ODE, tính ổn định bắt đầu từ câu hỏi cơ bản:

> Nếu dữ liệu chịu một nhiễu nhỏ, quy trình lặp rời rạc có khuếch đại nhiễu đó một cách mất kiểm soát hay không?

Câu hỏi này khác với tính ổn định của chính phương trình vi phân liên tục, vì lược đồ số tạo ra một hệ thức truy hồi có quy luật khuếch đại riêng.

Bài toán kiểm thử chuẩn là $$ y'=\lambda y $$ với $$ \operatorname{Re}(\lambda)<0 $$. Nghiệm chính xác $$ y(t)=e^{\lambda t}y_0 $$ suy giảm về 0, nên một phương pháp số hợp lý cần tái hiện được sự suy giảm đó trong miền điều kiện phù hợp.

### Euler tiến trên bài toán kiểm thử

Áp dụng Euler tiến ta được $$ y_{n+1}=(1+h\lambda)y_n $$. Hành vi của dãy số bị chi phối bởi hệ số khuếch đại $$ 1+h\lambda $$: nếu $$ \lvert 1+h\lambda\rvert<1 $$, nghiệm số suy giảm; ngược lại, nghiệm số có thể dao động hoặc bùng nổ dù nghiệm thật suy giảm rất êm.

Từ đây rút ra bài học cốt lõi đầu tiên về ổn định số:

> Một phương trình vi phân đặt chỉnh vẫn có thể sinh ra hành vi số sai lệch hoàn toàn về định tính nếu bước thời gian và lược đồ không tương thích.

## 5. Vì Sao Xuất Hiện Bài Toán Cứng

Một bài toán được gọi là cứng (stiff) khi nghiệm thực tế biến thiên trên thang thời gian vừa phải, nhưng hệ lại chứa những thành phần suy giảm rất nhanh trên thang thời gian ngắn hơn nhiều. Chính các thành phần suy giảm nhanh đó buộc phương pháp tường minh phải chọn bước $$ h $$ cực nhỏ để giữ ổn định, ngay cả khi nghiệm đã trở nên rất êm.

Đó là lý do phương pháp Euler lùi và các lược đồ ẩn giữ vai trò thiết yếu: chúng không chỉ là phiên bản phức tạp hơn của Euler tiến, mà là lời giải cho sự chênh lệch giữa thang thời gian vật lý và ràng buộc ổn định của sơ đồ tường minh.

## 6. Ví Dụ Có Lời Giải

### Ví dụ 1: Rút ra bước số đầu tiên từ khai triển Taylor

Cho $$ y'(t)=f(t,y), \qquad y(t_0)=y_0 $$. Khai triển Taylor cho $$ y(t_0+h)=y_0+h y'(t_0)+O(h^2) $$. Thay $$ y'(t_0)=f(t_0,y_0) $$, ta có $$ y(t_0+h)=y_0+h f(t_0,y_0)+O(h^2) $$. Bỏ qua số hạng $$ O(h^2) $$, ta thu được quy tắc rời rạc $$ y_1=y_0+h f(t_0,y_0) $$ — hệ quả trực tiếp của xấp xỉ Taylor bậc nhất.

### Ví dụ 2: Vì sao sai số cục bộ và sai số toàn cục lệch nhau một bậc

Giả sử một phương pháp một bước gây ra sai số cục bộ cỡ $$ Ch^2 $$ ở mỗi bước. Trên khoảng thời gian cố định $$ T $$, tổng số bước là khoảng $$ T/h $$. Nếu lược đồ ổn định (không khuếch đại sai số theo cấp số nhân), tổng sai số tích lũy có cỡ:

$$ \frac{T}{h}\cdot Ch^2 = CT h. $$

Lập luận đếm này tuy chưa phải chứng minh chặt chẽ nhưng giải thích rõ vì sao sai số toàn cục giảm đi một bậc của $$ h $$ so với sai số cục bộ.

### Ví dụ 3: Ổn định trên phương trình suy giảm

Xét $$ y'=-5y, \qquad y(0)=1 $$, có nghiệm chính xác $$ y(t)=e^{-5t} $$. Euler tiến cho $$ y_{n+1}=(1-5h)y_n $$. Với $$ h=0.1 $$, hệ số khuếch đại là $$ 0.5 $$, nghiệm số suy giảm đúng xu hướng. Với $$ h=0.5 $$, hệ số là $$ -1.5 $$, nghiệm số đổi dấu liên tục và tăng biên độ ra vô hạn. Mô hình và công thức đều đúng, nhưng bước thời gian vượt ngưỡng ổn định đã làm hỏng kết quả.

### Ví dụ 4: Ổn định của phương pháp ẩn

Với cùng bài toán trên, Euler lùi cho:

$$ y_{n+1}=\frac{1}{1+5h}y_n. $$

Hệ số khuếch đại luôn dương và nhỏ hơn 1 với mọi $$ h>0 $$. Đây là minh họa đầu tiên cho khái niệm ổn định tuyệt đối và vai trò của phương pháp ẩn đối với bài toán cứng.

## 7. Trực Quan Hóa

Đoạn mã Python sau so sánh nghiệm chính xác của phương trình suy giảm với Euler tiến ở hai bước thời gian khác nhau.

```python
import numpy as np
import matplotlib.pyplot as plt

lam = -5.0
T = 2.0

def forward_euler(h):
    n = int(T / h)
    t = np.linspace(0, n * h, n + 1)
    y = np.zeros(n + 1)
    y[0] = 1.0
    for k in range(n):
        y[k + 1] = y[k] + h * lam * y[k]
    return t, y

t_exact = np.linspace(0, T, 400)
y_exact = np.exp(lam * t_exact)

t1, y1 = forward_euler(0.1)
t2, y2 = forward_euler(0.5)

plt.figure(figsize=(8, 4))
plt.plot(t_exact, y_exact, label="nghiem chinh xac", linewidth=2)
plt.plot(t1, y1, "o-", label="Euler tien, h=0.1")
plt.plot(t2, y2, "s--", label="Euler tien, h=0.5")
plt.axhline(0.0, color="black", linewidth=0.8)
plt.title("Buoc thoi gian on dinh va mat on dinh")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

Đồ thị cho thấy rõ sự đối lập: bước thời gian nhỏ bảo toàn tính suy giảm của mô hình liên tục, trong khi bước quá lớn tạo ra dao động phân kỳ không hề tồn tại ở nghiệm thật.

## 8. Những Nhầm Lẫn Thường Gặp

### Nghĩ rằng phương pháp số chỉ xấp xỉ giá trị

Thực tế, mỗi phương pháp số tạo ra một hệ động lực rời rạc mang tính chất định tính riêng.

### Nghĩ rằng chỉ cần giảm bước thời gian là giải quyết được mọi vấn đề

Giảm $$ h $$ cải thiện độ chính xác và thường giúp thỏa điều kiện ổn định, nhưng với bài toán cứng, bước thời gian yêu cầu cho sơ đồ tường minh có thể quá nhỏ đến mức không khả thi về chi phí tính toán.

### Nhầm tính nhất quán (consistency) với sự hội tụ (convergence)

Một lược đồ có thể xấp xỉ đúng phương trình trên từng bước đơn lẻ nhưng vẫn phân kỳ toàn cục nếu không ổn định.

### Xem ổn định chỉ là chi tiết kỹ thuật phụ

Tính ổn định là trụ cột trung tâm của giải tích số, quyết định xem thông tin cục bộ có kết nối thành nghiệm dài hạn đáng tin cậy hay không.

## 9. Cầu Nối Sang Chương 13 Chính

Mạch logic của toàn chương có thể tóm gọn trong 5 ý:

1. Rời rạc hóa chuyển bài toán liên tục thành hệ thức truy hồi trên lưới.
2. Khai triển Taylor đặt cơ sở cho các công thức bước thời gian.
3. Cần phân biệt rõ sai số cục bộ và sai số toàn cục.
4. Tính ổn định quyết định sai số có được kiểm soát theo thời gian hay không.
5. Các phương pháp nâng cao được thiết kế nhằm tăng bậc chính xác, mở rộng miền ổn định, hoặc kết hợp cả hai.

Bài 13.01 bắt đầu với phương pháp Euler — hiện thân trực tiếp đầu tiên của cả năm nguyên lý trên — trước khi các bài tiếp theo mở rộng sang phương pháp bậc cao, nhiều bước, bài toán cứng và giải số PDE.

## Video tham khảo

- xem trước: [Differential Equations and Dynamical Systems: Overview](https://www.youtube.com/watch?v=9fQkLQZe3u8) — Steve Brunton, tiếng Anh. Tổng quan về phương trình vi phân và hệ động lực trước khi bước vào phần phương pháp số.
- [Error Analysis of Euler Integration Scheme for Differential Equations Using Taylor Series](https://www.youtube.com/watch?v=h2i550iaEv0) — Steve Brunton, tiếng Anh. Dùng khai triển Taylor để phân tích sai số cục bộ của phương pháp một bước.
- [Stability of Forward Euler and Backward Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=RdXCGnTT6UY) — Steve Brunton, tiếng Anh. Phân tích trực quan tính ổn định của Euler tiến và Euler lùi.

## Tài liệu tham khảo

- U. Ascher và L. Petzold, *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*
- E. Hairer, S. P. Norsett, và G. Wanner, *Solving Ordinary Differential Equations I*
- R. J. LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*
