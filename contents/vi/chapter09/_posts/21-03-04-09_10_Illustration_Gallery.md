---
layout: post
title: "Bộ Minh Họa Chương 09"
chapter: '09'
order: 10
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: optional
---

Phương trình nhiệt là bài học trực quan bậc nhất về sự khác biệt giữa *tán xạ năng lượng* và *dao động*: chỉ cần nhìn đồ thị động theo thời gian $t$, bạn thấy ngay mọi góc nhọn tan chảy trong tích tắc, đường cong nhiệt độ hạ dần về đường thẳng dừng, và lưới sai phân FTCS bỗng nhảy loạn xạ khi $r$ vượt ngưỡng $0{,}5$.

## Kiến thức cần nhớ: Bốn hiện tượng cần quan sát kỹ trong Gallery Chương 09

1. **Làm trơn tức thì (Instantaneous Smoothing)**: Góc gãy sắc của hàm ban đầu biến mất ngay tại $t = 0{,}01\text{ s}$.
2. **Hội tụ về Trạng thái Dừng**: Đường cong $u(x, t)$ tiến về $0$ (Dirichlet), về đường nằm ngang trung bình (Neumann), hoặc đường thẳng nối $T_1 \to T_2$ (biên không thuần nhất).
3. **Sự giãn nở của Nhân Nhiệt Gaussian**: Diện tích dưới đường chuông luôn bằng $1$, đỉnh giảm như $1/\sqrt{t}$ và chân loe rộng như $\sqrt{t}$.
4. **Ngưỡng ổn định CFL $r = 0{,}5$**: Kéo thanh trượt $r$ từ $0{,}49$ lên $0{,}51$ để tận mắt thấy dao động răng cưa bùng nổ!

## Mục Đích Của Bài Hỗ Trợ

Bài học này tập hợp toàn bộ hình minh họa của Chương 09 vào một không gian ôn tập trực quan chung. Phương trình nhiệt thường là PDE đầu tiên được học đầy đủ, nên khối lượng khái niệm của chương khá lớn: thiết lập phương trình từ nguyên lý vật lý, khai triển theo hàm riêng, tác động của điều kiện biên, nhân nhiệt và hàm Green, nguyên lý cực đại cũng như rời rạc hóa số. Bộ minh họa giúp kết nối các nội dung này thành một bức tranh thống nhất thay vì các kỹ thuật rời rạc.

Việc đối chiếu liên tục giữa công thức và hình ảnh giúp nắm vững bản chất bài toán hơn. Nhân nhiệt Gaussian không chỉ là một biểu thức giải tích mà còn thể hiện trực tiếp sự lan rộng và làm mượt; nguyên lý cực đại không chỉ là một chứng minh bất đẳng thức mà còn là tính chất hình học mô tả sự biến thiên của cực trị trong quá trình khuếch tán.

## Cách Sử Dụng Bài Này

Nên xem bộ minh họa theo đúng thứ tự các bài học trong chương. Sau mỗi hình, hãy đối chiếu lại bài học tương ứng để nhận diện ý tưởng toán học nào đang được thể hiện: định luật bảo toàn, phân rã phổ, lựa chọn mode theo điều kiện biên, chuẩn hóa bài toán không thuần nhất, phép tích chập, kiểm soát định tính hay điều kiện ổn định số. Nhờ vậy, bộ minh họa trở thành cầu nối giữa công thức ký hiệu và ý nghĩa vật lý.

Trang này cũng thuận tiện để ôn tập trước khi chuyển sang Chương 10 và Chương 11, vì nhiều cấu trúc phương pháp từ phương trình nhiệt sẽ tiếp tục được dùng cho phương trình sóng và phương trình elliptic.

### Giải thích: Kiểm chứng nhanh trên đồ thị tương tác tỷ lệ giảm đỉnh nhiệt độ $u_{\max}(t)$

Với nguồn điểm ở gốc ($\alpha = 1$), đỉnh nhân nhiệt là $\Phi(0, t) = \frac{1}{\sqrt{4\pi t}}$:
- Tại $t = 1\text{ s}$: $\Phi(0, 1) \approx \mathbf{0{,}282}$.
- Tại $t = 4\text{ s}$ (thời gian tăng $4\times$): đỉnh giảm đi đúng $\sqrt{4} = 2\times$ xuống $\mathbf{0{,}141}$, còn độ rộng $\sigma = \sqrt{2t}$ tăng đúng $2\times$ từ $1{,}41$ lên $2{,}83$!

## Gallery Nhúng Trực Tiếp

{% include interactive-frame.html
  title="Bộ Minh Họa Chương 09"
  description="Không gian trực quan hỗ trợ cho quá trình suy ra, phương pháp giải, các nguyên lý định tính, sơ đồ số, và ứng dụng của phương trình nhiệt."
  path="interactives/chapter09/index.html"
  height="980px"
%}

## Câu Hỏi Gợi Ý Khi Học

1. Hình nào nhấn mạnh nguồn gốc vật lý của phương trình nhiệt, và hình nào nhấn mạnh cấu trúc giải tích của nghiệm?
2. Nội dung chương chuyển từ các công thức nghiệm tường minh sang các kết quả định tính ở điểm nào?
3. Các minh họa trên miền hữu hạn và miền vô hạn chuẩn bị như thế nào cho bước chuyển từ chuỗi Fourier sang biến đổi Fourier?

## Liên Kết Tới Các Bài Học Chính

- [09.01 Suy ra phương trình nhiệt]({{ site.baseurl }}/contents/vi/chapter09/09_01_Derivation_Heat_Equation/)
- [09.02 Phương pháp tách biến cho phương trình nhiệt]({{ site.baseurl }}/contents/vi/chapter09/09_02_Separation_of_Variables/)
- [09.03 Điều kiện biên thuần nhất]({{ site.baseurl }}/contents/vi/chapter09/09_03_Homogeneous_Boundary_Conditions/)
- [09.04 Bài toán nhiệt non-thuần nhất]({{ site.baseurl }}/contents/vi/chapter09/09_04_Nonhomogeneous_Problems/)
- [09.05 Phương trình nhiệt trên miền vô hạn]({{ site.baseurl }}/contents/vi/chapter09/09_05_Heat_Infinite_Domain/)
- [09.06 Nghiệm cơ bản và hàm Green]({{ site.baseurl }}/contents/vi/chapter09/09_06_Fundamental_Solution_Greens_Functions/)
- [09.07 Nguyên lý cực đại]({{ site.baseurl }}/contents/vi/chapter09/09_07_Maximum_Principles/)
- [09.08 Phương pháp số: sai phân hữu hạn]({{ site.baseurl }}/contents/vi/chapter09/09_08_Numerical_Methods_Finite_Differences/)
- [09.09 Ứng dụng: quá trình khuếch tán]({{ site.baseurl }}/contents/vi/chapter09/09_09_Applications_Diffusion_Processes/)

## Video tham khảo

- Xem trước: [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Hoạt ảnh minh họa quá trình truyền nhiệt gắn trực tiếp với các hình trong bộ minh họa.
- [But what is a partial differential equation?  | DE2](https://www.youtube.com/watch?v=ly4S0oi3Yz8) — 3Blue1Brown, tiếng Anh. Giới thiệu trực quan bản chất của phương trình đạo hàm riêng trước khi xem các khung minh họa chi tiết.
- [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, tiếng Anh. Trình bày cách thiết lập phương trình nhiệt từ định luật bảo toàn năng lượng để đối chiếu cùng các hình vẽ.
