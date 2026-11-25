---
layout: post
title: "06-09 Bộ Minh họa Tương tác"
chapter: '06'
order: 9
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: optional
---

Nghiệm chuỗi lũy thừa, hàm Bessel hay đa thức Legendre thường tạo cảm giác khô khan nếu chỉ nhìn những tổng $\sum a_n x^n$ dày đặc trên giấy. Nhưng ngay khi bạn kéo thanh trượt thay đổi số hạng cắt cụt $N$ hay bậc $n$ trên đồ thị tương tác, toàn bộ bức tranh lập tức bừng sáng: bạn tận mắt thấy chuỗi hội tụ dần trong bán kính $R$, thấy màng trống tròn rung theo nghiệm không của hàm Bessel $J_0$, và thấy đa thức Legendre dao động trực giao trên $[-1, 1]$.

## Kiến thức cần nhớ: Bốn hiện tượng hình học cần quan sát trong Bộ Minh họa Chương 06

1. **Bán kính hội tụ $R$ của chuỗi lũy thừa**:
   Bên trong $\vert x - x_0 \vert < R$, tổng riêng $S_N(x)$ ôm sát nghiệm thật khi $N$ tăng; vừa bước qua biên $\vert x - x_0 \vert > R$, đường cong bung vọt ra vô cùng!
2. **Hành vi tại điểm kỳ dị chính quy (Frobenius)**:
   Khác với điểm thường, nghiệm gần điểm kỳ dị $x = 0$ có thể mang lũy thừa phân số $x^r$ hoặc số hạng $\ln \vert x \vert$ phát kỳ dị ngay tại gốc.
3. **Dao động tắt dần của Hàm Bessel $J_\nu(x)$**:
   Giống như $\cos x$ nhưng biên độ giảm dần theo $1/\sqrt{x}$—mô tả chính xác sóng tròn lan trên mặt nước và màng trống.
4. **Tính trực giao và các nghiệm nút của Đa thức Legendre $P_n(x)$**:
   Mỗi $P_n(x)$ có đúng $n$ nghiệm thực phân biệt nằm gọn trong $(-1, 1)$, là cơ sở vàng cho cầu điều hòa và cầu phương Gauss.

## Tổng quan

Bài học bổ sung này tập hợp toàn bộ các minh họa JavaScript của Chương 06 tại một nơi, đóng vai trò tài liệu trực quan đồng hành cho các phương pháp truy hồi, các họ hàm đặc biệt và các ứng dụng vật lý của chương.

## Nội dung có trong bộ minh họa

- Sự hội tụ và phép cắt cụt chuỗi lũy thừa
- Hệ thức truy hồi và nghiệm chuỗi quanh điểm thường
- Phương trình Euler và phương pháp Frobenius
- Các họ hàm Bessel, Legendre và các hàm đặc biệt khác
- Góc nhìn chế độ riêng (mode) và phổ trong các ứng dụng vật lý

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 06"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 06."
  path="interactives/chapter06/index.html"
  height="920px"
%}

### Giải thích: Tự kiểm tra bán kính hội tụ $R = 1$ của chuỗi hình học $\frac{1}{1 - x} = \sum_{n=0}^{\infty} x^n$ ngay trên thanh trượt

Hãy thử 2 giá trị $x$ đối lập nhau khi tăng số hạng $N = 2, 5, 10$:
- **Tại $x = 0{,}5$ (nằm trong $\vert x \vert < 1$)**: Nghiệm thật là $\frac{1}{1 - 0{,}5} = 2{,}000$.
  - $N = 2$: $1 + 0{,}5 + 0{,}25 = 1{,}750$ (sai số $0{,}25$).
  - $N = 5$: $1{,}96875$ (sai số $0{,}031$).
  - $N = 10$: $1{,}99902$ (sai số $< 0{,}001$ → hội tụ cực nhanh!).
- **Tại $x = 1{,}2$ (nằm ngoài $\vert x \vert > 1$)**: $S_2 = 3{,}64$, $S_5 = 9{,}93$, $S_{10} = 32{,}15 \to +\infty$ (phân kỳ hoàn toàn dù hàm $\frac{1}{1-x} = -5$ vẫn hữu hạn tại $x = 1{,}2$!).

## Video tham khảo

- Xem trước: [Taylor series | Chapter 11, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — 3Blue1Brown, tiếng Anh. Trực quan hóa các đa thức Taylor làm nền tảng cho quá trình xấp xỉ bằng chuỗi trong bộ minh họa.
- [Advanced Engineering Mathematics, Lecture 2.7: Bessel's equation](https://www.youtube.com/watch?v=lcvWAgrdFn0) — Professor Macauley, tiếng Anh. Giới thiệu phương trình và hàm Bessel để đối chiếu với các khung minh họa hàm đặc biệt.
- [Intro to Legendre Polynomials](https://www.youtube.com/watch?v=djlUmwbPw20) — Physics and Math Lectures, tiếng Anh. Giới thiệu đa thức Legendre, một họ hàm đặc biệt tiêu biểu khác được vẽ trong bộ minh họa.
