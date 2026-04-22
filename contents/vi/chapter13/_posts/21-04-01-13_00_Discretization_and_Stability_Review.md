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

Bài hỗ trợ này xây nền ý niệm cho toàn bộ giải tích số của phương trình vi phân trước khi bất kỳ sơ đồ quen thuộc nào xuất hiện. Sau bài học, sinh viên cần hiểu vì sao phải rời rạc hóa, cách khai triển Taylor biện minh cho các công thức bước thời gian, vì sao sai số cục bộ và sai số toàn cục là hai khái niệm khác nhau, và vì sao ổn định là tính chất của chính phương pháp số chứ không chỉ của phương trình vi phân ban đầu.

## Vì Sao Bài Này Cần Thiết

Nhiều sinh viên bước vào phương pháp số với kiến thức giải tích đúng nhưng kỳ vọng sai. Họ biết cách giải hay phân tích một phương trình vi phân, nên họ nghĩ phương pháp số chỉ là một chiếc máy tính tự động cho cùng đối tượng ấy. Nhưng ngay khi ta chuyển từ mô hình liên tục sang thuật toán rời rạc, một bài toán toán học mới đã được sinh ra. Phương trình vi phân sống trên một continuum; phương pháp số sống trên một lưới điểm. Hành vi của hệ rời rạc phải được nghiên cứu như một đối tượng riêng.

Đó chính là trái tim ý niệm của Chương 13. Phương pháp Euler, Runge-Kutta, multistep methods, stiff solvers, sai phân hữu hạn hay phần tử hữu hạn đều bắt đầu từ cùng một sự đổi góc nhìn:

> Phương trình vi phân là liên tục theo thời gian hay không gian, nhưng máy tính chỉ có thể tiến hóa hữu hạn nhiều con số tại hữu hạn nhiều điểm lưới.

Mục tiêu của bài này là làm cho sự chuyển đổi ấy hiện ra rõ ràng trước khi sinh viên gặp phương pháp đầu tiên.

## Kiến thức nền

Sinh viên nên nắm bài toán giá trị ban đầu cho ODE, khai triển Taylor, ý nghĩa hình học của đạo hàm, và trực giác rằng nhiều mô hình thực tế không có nghiệm đóng. Bài này chưa giả sử sinh viên đã học lý thuyết ổn định số.

## 1. Từ Mô Hình Liên Tục Sang Quá Trình Rời Rạc

Xét bài toán giá trị ban đầu $$ y'(t)=f(t,y(t)), \qquad y(t_0)=y_0 $$. Từ góc nhìn giải tích, ẩn số là một hàm được xác định trên cả một khoảng thời gian. Từ góc nhìn tính toán, điều đó ngay lập tức là bất khả thi: máy tính không thể lưu một continuum giá trị. Nó chỉ có thể lưu các xấp xỉ tại các thời điểm rời rạc $$ t_n=t_0+nh $$. Vì vậy, hành động đầu tiên của giải tích số không phải là xấp xỉ đạo hàm, mà là thay continuum bằng một lưới điểm. Khi quyết định đó được đưa ra, bài toán đổi dạng. Ta không còn hỏi về hàm chính xác $$ y(t) $$ tại mọi thời điểm. Ta hỏi về một dãy $$ y_0, y_1, y_2, \dots $$ vốn phải bám được nghiệm thật tại các điểm lưới.

Chính vì thế, một phương pháp số không chỉ là phương trình vi phân được viết lại bằng ký hiệu khác. Nó là một hệ động lực rời rạc trên dữ liệu số. Hệ rời rạc ấy có thể bảo tồn hình học của bài toán liên tục, làm méo nó, ổn định hóa nó, hoặc làm nó mất ổn định.

### Ý nghĩa ứng dụng

Trong thực tế, rời rạc hóa là một quyết định đo lường. Mô hình thời tiết, mạch điện hay tăng trưởng quần thể không bao giờ được tính "liên tục theo mọi thời điểm". Chúng được cập nhật theo từng bước. Việc chọn bước thời gian đã hàm chứa một quan niệm về những thang thời gian nào là nhìn thấy được hay quan trọng.

## 2. Khai Triển Taylor Như Nguyên Lý Số Học Đầu Tiên

Sự biện minh cơ bản nhất cho các sơ đồ bước thời gian đến từ định lý Taylor. Nếu nghiệm thật đủ trơn, thì gần $$ t_n $$ ta có

$$ y(t_n+h)=y(t_n)+hy'(t_n)+\frac{h^2}{2}y''(\xi_n) $$

với một điểm trung gian nào đó $$ \xi_n $$.

Vì $$ y'(t_n)=f(t_n,y(t_n)) $$, nên xấp xỉ bậc nhất trở thành $$ y(t_n+h)\approx y(t_n)+h f(t_n,y(t_n)) $$. Đây là nguồn ý niệm của phương pháp Euler. Điểm sâu hơn không chỉ là Taylor cho ra một công thức. Điểm sâu hơn là mọi one-step method đều có thể được đọc như một phép xấp xỉ có kiểm soát đối với hành vi Taylor cục bộ của nghiệm thật.

### Vì sao Taylor quan trọng vượt ra ngoài Euler

Các phương pháp Runge-Kutta bậc cao, predictor-corrector hay sai phân hữu hạn đều cạnh tranh với nhau một phần bằng cách khớp được nhiều hạng hơn của khai triển Taylor. Trong giải tích số, bậc chính xác là cách nói chặt chẽ về việc quy tắc rời rạc mô phỏng hành vi trơn cục bộ của nghiệm thật trung thành đến đâu.

## 3. Sai Số Cục Bộ Và Sai Số Toàn Cục

Một trong những cái bẫy ý niệm đầu tiên của giải tích số là nhầm lẫn giữa sai số của một bước và sai số tích lũy sau nhiều bước.

### Sai số cục bộ

Sai số cục bộ đo điều gì xảy ra nếu ta bắt đầu một bước từ đúng giá trị chính xác và so sánh kết quả của một bước số với nghiệm thật sau một bước thời gian. Nó kiểm tra độ chính xác của phương pháp như một quy tắc xấp xỉ cục bộ.

### Sai số toàn cục

Sai số toàn cục đo độ chênh giữa dãy số sinh ra bởi phương pháp và nghiệm thật sau nhiều bước. Sai số này chứa hai hiệu ứng:

- độ lệch cục bộ của từng bước,
- sự lan truyền và khuếch đại của những sai số đã sinh ra trước đó.

Phân biệt này có ý nghĩa quyết định. Một phương pháp có thể có sai số cục bộ rất nhỏ nhưng vẫn cho kết quả tệ trên khoảng thời gian dài nếu sơ đồ khuếch đại các nhiễu loạn.

### Quan hệ heuristic

Với một phương pháp bậc nhất "hiền" như Euler tiến, sai số cục bộ thường có cỡ $$ O(h^2) $$ còn sai số toàn cục thường có cỡ $$ O(h) $$. Ta mất đi một lũy thừa của $$ h $$ vì trên một khoảng thời gian cố định có khoảng $$ 1/h $$ bước, nên các sai số cục bộ bị cộng dồn.

Đây là nơi sinh viên nên thấy rằng giải tích số không chỉ là lý thuyết xấp xỉ. Nó là lý thuyết xấp xỉ cộng với động lực của sự lan truyền sai số.

## 4. Ổn Định: Phương Pháp Số Có Động Lực Riêng

Từ "ổn định" có nhiều nghĩa trong toán học, nhưng trong số trị ODE nó bắt đầu từ một câu hỏi đơn giản:

> Nếu dữ liệu bị nhiễu một chút, quá trình rời rạc có khuếch đại nhiễu ấy một cách mất kiểm soát hay không?

Điều này không giống với việc hỏi phương trình vi phân liên tục có ổn định hay không. Phương pháp số tạo ra chính nó một quan hệ truy hồi, và quan hệ truy hồi ấy có quy luật khuếch đại riêng.

Bài toán thử chuẩn là $$ y'=\lambda y $$, đặc biệt khi $$ \operatorname{Re}(\lambda)<0 $$. Nghiệm thật suy giảm:

$$ y(t)=e^{\lambda t}y_0. $$

Bất kỳ phương pháp số hợp lý nào cũng nên bắt chước được sự suy giảm đó, ít nhất dưới những điều kiện thích hợp.

### Euler tiến trên bài toán thử

Áp dụng Euler tiến ta được $$ y_{n+1}=(1+h\lambda)y_n $$. Nghĩa là hành vi rời rạc được điều khiển bởi phép nhân lặp lại với $$ 1+h\lambda $$. Nếu $$ \lvert 1+h\lambda\rvert<1 $$, thì nhiễu loạn suy giảm. Nếu không, nghiệm số có thể dao động hay bùng nổ ngay cả khi nghiệm thật suy giảm rất êm.

Đây là bài học đầu tiên đầy ấn tượng của ổn định số:

> Một phương trình vi phân đúng hoàn toàn có thể tạo ra hành vi số sai định tính nếu bước thời gian và sơ đồ không tương thích.

## 5. Vì Sao Xuất Hiện Bài Toán Cứng

Khái niệm stiffness thường được học ở bài sau, nhưng sinh viên nên có trực giác sớm. Một bài toán được gọi là cứng khi nghiệm liên tục thay đổi trên thang thời gian vừa phải, trong khi một số mode ẩn lại suy giảm trên thang thời gian ngắn hơn rất nhiều. Chính các mode suy giảm nhanh ấy buộc phương pháp tường minh phải dùng bước rất nhỏ để giữ ổn định, ngay cả khi bản thân nghiệm không còn biến thiên mạnh nữa.

Đó là lý do Euler lùi và các phương pháp ngầm quan trọng. Chúng không chỉ là phiên bản rắc rối hơn của Euler. Chúng là phản ứng trước một sự lệch pha có tính cấu trúc giữa thang thời gian vật lý và ràng buộc ổn định của sơ đồ tường minh.

## 6. Ví Dụ Có Lời Giải

### Ví dụ 1: Dẫn ra một bước số từ Taylor

Giả sử $$ y'(t)=f(t,y), \qquad y(t_0)=y_0 $$. Khai triển Taylor cho $$ y(t_0+h)=y_0+h y'(t_0)+O(h^2) $$. Dùng ODE, $$ y'(t_0)=f(t_0,y_0) $$, nên $$ y(t_0+h)=y_0+h f(t_0,y_0)+O(h^2) $$. Nếu bỏ qua hạng bậc cao, ta thu được quy tắc rời rạc $$ y_1=y_0+h f(t_0,y_0) $$. Đây chưa phải là "phương pháp Euler" như một công thức cần học thuộc, mà là hệ quả rời rạc đầu tiên của xấp xỉ Taylor.

### Ví dụ 2: Vì sao sai số cục bộ và toàn cục khác nhau

Giả sử một one-step method gây ra sai số cỡ $$ Ch^2 $$ trong mỗi bước. Trên một khoảng thời gian dài $$ T $$, số bước xấp xỉ là $$ T/h $$. Nếu sai số không nổ tung, ảnh hưởng tích lũy sẽ gần bằng

$$ \frac{T}{h}\cdot Ch^2 = CT h. $$

Vì vậy sai số toàn cục có cỡ $$ h $$. Lập luận đếm đơn giản này chưa phải chứng minh, nhưng nó giải thích rất tốt vì sao một lũy thừa của $$ h $$ bị mất khi đi từ sai số cục bộ sang sai số toàn cục.

### Ví dụ 3: Ổn định cho phương trình suy giảm

Xét $$ y'=-5y, \qquad y(0)=1 $$. Nghiệm thật là $$ y(t)=e^{-5t} $$. Euler tiến cho $$ y_{n+1}=(1-5h)y_n $$. Nếu $$ h=0.1 $$ thì hệ số khuếch đại là $$ 0.5 $$, nên nghiệm số suy giảm. Nếu $$ h=0.5 $$ thì hệ số là $$ -1.5 $$, nên nghiệm số đổi dấu và tăng biên độ. Mô hình đúng, công thức đúng, nhưng lựa chọn bước thời gian đã phá hỏng phép tính.

### Ví dụ 4: Cái nhìn đầu tiên về ổn định của phương pháp ngầm

Với cùng bài toán thử, Euler lùi cho

$$ y_{n+1}=\frac{1}{1+5h}y_n. $$

Bây giờ hệ số khuếch đại luôn dương và nhỏ hơn 1 với mọi $$ h>0 $$. Đây là điểm khởi đầu của ý tưởng absolute stability và lý do các phương pháp ngầm quan trọng với bài toán cứng.

## 7. Trực Quan Hóa

Đoạn mã Python sau so sánh nghiệm chính xác của một ODE suy giảm với Euler tiến ở hai bước thời gian khác nhau.

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

Đồ thị làm lộ bài học số trị rất rõ: một cách rời rạc hóa tôn trọng tính suy giảm của mô hình liên tục, còn cách kia thì bịa ra một dao động mất ổn định vốn không hề có trong nghiệm thật.

## 8. Những Nhầm Lẫn Thường Gặp

### Nghĩ rằng phương pháp số chỉ xấp xỉ giá trị

Một phương pháp số còn tạo ra cả một hệ động lực rời rạc với hành vi định tính riêng của nó.

### Nghĩ rằng chỉ cần giảm bước thời gian là xong

Giảm $$ h $$ giúp cải thiện độ chính xác và thường cũng giúp ổn định hơn, nhưng stiffness có thể khiến các phương pháp tường minh trở nên không thực tế dù ý niệm của chúng rất đơn giản.

### Nhầm consistency với convergence

Một phương pháp có thể xấp xỉ đúng phương trình trong một bước nhưng vẫn thất bại toàn cục nếu ổn định kém.

### Xem ổn định như phần phụ kỹ thuật

Ổn định là một trong những ý tưởng trung tâm của giải tích số vì nó quyết định liệu thông tin cục bộ có tạo ra được phép tính dài hạn đáng tin hay không.

## 9. Cầu Nối Sang Chương 13 Chính

Giờ đây logic của chương đã khá rõ.

1. Rời rạc hóa biến bài toán liên tục thành một quan hệ truy hồi trên lưới.
2. Khai triển Taylor biện minh cho các công thức bước đầu tiên.
3. Sai số cục bộ và sai số toàn cục phải được phân biệt.
4. Ổn định quyết định liệu sai số có còn được kiểm soát hay không.
5. Các phương pháp phức tạp hơn được tạo ra bằng cách tăng bậc chính xác, cải thiện ổn định, hoặc cả hai.

Bài 13.01 bắt đầu bằng phương pháp Euler vì đó là hiện thân hoàn chỉnh đầu tiên của tất cả các ý trên trong một sơ đồ đơn lẻ. Các bài sau chỉ tinh chỉnh cùng khuôn khổ đó cho phương pháp bậc cao, multistep methods, phương trình cứng và PDE số.

## Tài liệu tham khảo

- U. Ascher và L. Petzold, *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*
- E. Hairer, S. P. Norsett, và G. Wanner, *Solving Ordinary Differential Equations I*
- R. J. LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*
