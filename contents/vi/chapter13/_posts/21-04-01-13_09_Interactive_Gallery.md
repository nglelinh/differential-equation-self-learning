---
layout: post
title: "Bộ Minh Họa Tương Tác Chương 13"
chapter: '13'
order: 9
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: optional
---

Không có cách nào học giải tích số thấm nhanh bằng việc tự tay kéo thanh trượt bước lưới $h$ và nhìn điều gì xảy ra trên màn hình: đường gấp khúc Euler rời dần quỹ đạo thật, RK4 ôm sát đường cong như phép màu, lưới FTCS lập tức bốc cháy răng cưa ngay khoảnh khắc $r$ nhích từ $0{,}50$ lên $0{,}51$, còn các quỹ đạo SDE tỏa ra thành đám mây phân bố Gaussian sống động!

## Kiến thức cần nhớ: Bốn thí nghiệm trực quan nên thử ngay trong Gallery Chương 13

1. **Đường dốc Bậc Hội tụ trên Biểu đồ Log–Log**:
   Quan sát đồ thị $\log(\text{Sai số})$ theo $\log(h)$: độ dốc đường thẳng chính là bậc hội tụ $p$ ($p=1$ cho Euler, $p=2$ cho Midpoint/Heun, $p=4$ cho RK4).
2. **Bản đồ Miền Ổn định trên Mặt phẳng Phức $z = h\lambda$**:
   So sánh hình tròn nhỏ bé của Euler hiện, hình "bốn cánh" của RK4 với toàn bộ nửa mặt phẳng trái của Euler ẩn và BDF.
3. **Hiệu ứng Vượt ngưỡng CFL & Phân tán Số**:
   Chạy phương trình sóng/nhiệt ở sát biên ổn định và vượt biên ổn định để phân biệt giữa sai số tắt dần (numerical dissipation) và mất ổn định bùng nổ.
4. **Hội tụ Mạnh (từng quỹ đạo) vs. Hội tụ Yếu (phân bố) của SDE**:
   Nhìn cùng một hạt giống ngẫu nhiên $W_t$ khi mịn hóa $\Delta t$ trong Euler–Maruyama so với biểu đồ histogram mật độ xác suất khớp nghiệm Fokker–Planck.

## Mục Đích Của Bài Hỗ Trợ

Bài học này tập hợp toàn bộ các minh họa tương tác của Chương 13 vào một không gian học tập thống nhất. Các bài chính trong chương lần lượt phát triển trực giác về rời rạc hóa, sai số cục bộ và toàn cục, độ cứng, miền ổn định, lưới sai phân hữu hạn cho PDE, hàm cơ sở phần tử hữu hạn và quỹ đạo ngẫu nhiên. Bộ minh họa đặt các ý niệm đó cạnh nhau để người học thấy rõ chúng cùng thuộc một khuôn khổ thống nhất của giải tích số.

Các khái niệm giải tích số thường khó ghi nhớ nếu chỉ học qua công thức. Khi trực tiếp quan sát nghiệm số bùng nổ do bước thời gian vượt ngưỡng ổn định, hoặc thấy ràng buộc CFL xuất phát từ hình học mẫu sai phân, sinh viên sẽ dễ dàng gắn kết lý thuyết với hành vi thực tế của thuật toán.

## Cách Sử Dụng Bài Này

Nên quay lại bộ minh họa sau khi hoàn thành từng phương pháp hoặc định lý trong bài chính. Với mỗi minh họa, hãy xác định đại lượng đang được kiểm soát: sai số cắt cụt, hệ số khuếch đại, phản ứng trước độ cứng, độ mịn lưới hay sự khác biệt giữa thành phần ngẫu nhiên và xu hướng xác định. Nhờ đó, trang tổng hợp trở thành cầu nối giữa công thức toán học và hành vi mô phỏng.

Trang này cũng phù hợp để ôn tập khi chuyển từ giải số ODE sang giải số PDE, vì nó hệ thống hóa cùng một chỗ các khái niệm nhất quán, ổn định và hội tụ.


### Giải thích: Đọc nhanh bậc hội tụ $p$ bằng quy tắc "chia đôi bước $h$"

Nếu sai số toàn cục tuân theo $E(h) \approx C h^p$, thì khi ta **chia đôi bước thời gian** ($h \to h/2$), tỷ số giảm sai số là $\frac{E(h)}{E(h/2)} \approx 2^p$:
- **Euler ($p = 1$)**: chia đôi $h \implies$ sai số giảm **$2\times$** (giảm $h$ đi $10\times$ thì sai số giảm $10\times$).
- **RK2 / Crank–Nicolson ($p = 2$)**: chia đôi $h \implies$ sai số giảm **$4\times$** (giảm $h$ đi $10\times$ thì sai số giảm $100\times$).
- **RK4 ($p = 4$)**: chia đôi $h \implies$ sai số giảm **$16\times$** (giảm $h$ đi $10\times$ thì sai số giảm tới **$10.000\times$**!).
Chỉ cần bấm nút chia đôi $h$ hai lần trên đồ thị tương tác và lấy $\log_2\!\big(E(h)/E(h/2)\big)$, bạn sẽ kiểm chứng được ngay bậc chính xác thực nghiệm của bất kỳ bộ giải nào!
## Gallery Tương Tác Nhúng Trực Tiếp

{% include interactive-frame.html
  title="Bộ Minh Họa Tương Tác Chương 13"
  description="Không gian trực quan hỗ trợ cho Euler, Runge-Kutta, multistep methods, độ cứng, điều kiện CFL, sai phân hữu hạn, phần tử hữu hạn và phương trình vi phân ngẫu nhiên."
  path="interactives/chapter13/index.html"
  height="980px"
%}

## Câu Hỏi Gợi Ý Khi Học

1. Minh họa nào chủ yếu làm nổi bật độ chính xác, và minh họa nào làm nổi bật tính ổn định?
2. Ở những ví dụ nào ta thấy rõ sự khác biệt giữa tính chất của phương trình liên tục và hành vi thuần túy rời rạc của thuật toán số?
3. Các ví dụ về PDE và SDE đã mở rộng khái niệm xấp xỉ số vượt ra ngoài bài toán giá trị ban đầu cổ điển như thế nào?

## Liên Kết Tới Các Bài Học Chính

- [13.00 Ôn tập nền tảng]({{ site.baseurl }}/contents/vi/chapter13/13_00_Discretization_and_Stability_Review/)
- [13.01 Phương pháp Euler]({{ site.baseurl }}/contents/vi/chapter13/13_01_Eulers_Method/)
- [13.02 Phương pháp Runge-Kutta]({{ site.baseurl }}/contents/vi/chapter13/13_02_Runge_Kutta_Methods/)
- [13.03 Phương pháp nhiều bước]({{ site.baseurl }}/contents/vi/chapter13/13_03_Multistep_Methods/)
- [13.04 Phương trình cứng]({{ site.baseurl }}/contents/vi/chapter13/13_04_Stiff_Equations/)
- [13.05 Sai phân hữu hạn cho PDE]({{ site.baseurl }}/contents/vi/chapter13/13_05_Finite_Differences_PDEs/)
- [13.06 Ổn định và hội tụ (CFL)]({{ site.baseurl }}/contents/vi/chapter13/13_06_Stability_Convergence_CFL/)
- [13.07 Nhập môn phần tử hữu hạn]({{ site.baseurl }}/contents/vi/chapter13/13_07_Finite_Element_Introduction/)
- [13.08 Phương trình vi phân ngẫu nhiên]({{ site.baseurl }}/contents/vi/chapter13/13_08_Stochastic_Differential_Equations/)

## Video tham khảo

- xem trước: [Runge-Kutta Integrator Overview:  All Purpose Numerical Integration of Differential Equations](https://www.youtube.com/watch?v=HOWJp8NV5xU) — Steve Brunton, tiếng Anh. Tổng quan về phương pháp Runge–Kutta được đối chiếu trong bộ minh họa.
- [Deriving Forward Euler and Backward/Implicit Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=MstPeOTCVzQ) — Steve Brunton, tiếng Anh. Dẫn xuất lược đồ Euler tiến và Euler lùi tương ứng với các hình minh họa trong chương.
- [Chaotic Dynamical Systems](https://www.youtube.com/watch?v=PDeN3iCtyNY) — Steve Brunton, tiếng Anh. Giới thiệu hệ động lực hỗn loạn — nơi ngay cả lược đồ ổn định cũng bị giới hạn về tầm dự báo dài hạn.
