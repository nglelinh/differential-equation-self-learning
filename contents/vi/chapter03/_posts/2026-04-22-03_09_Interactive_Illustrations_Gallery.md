---
layout: post
title: "03-09 Bộ Minh họa Tương tác"
chapter: '03'
order: 9
owner: Course Team
lang: vi
categories:
- chapter03
lesson_type: optional
---


Biến đổi Laplace đưa một bài toán vi phân trong miền thời gian $t$ sang miền tần số phức $s$, nơi chỉ cần nhìn vào vị trí vài dấu chấm—các **cực (poles)** của hàm truyền $H(s)$ trên mặt phẳng phức—bạn đọc ngay được toàn bộ hành vi của hệ: dao động hay không, tắt dần nhanh hay chậm, ổn định hay bùng nổ! Bộ minh họa tương tác Chương 03 giúp bạn kéo trực tiếp các cực trên mặt phẳng $s$ và quan sát đáp ứng thời gian biến hình ngay tức thì.

## Kiến thức cần nhớ: Bốn trực giác cần quan sát trong Bộ Minh họa Chương 03

1. **Bản đồ Cực–Không (Pole–Zero Map) & Miền ổn định**:
   Cực nằm bên nửa trái ($\operatorname{Re}(s) < 0$) cho đáp ứng tắt dần ổn định; nằm trên trục ảo cho dao động điều hòa; chỉ cần một cực trượt sang nửa phải ($\operatorname{Re}(s) > 0$) là hệ bùng nổ!
2. **Hàm bậc thang Heaviside $u_c(t)$ & Công tắc bật/tắt**:
   Quan sát cách xung chữ nhật $u_a(t) - u_b(t)$ bật và tắt ngoại lực tại thời điểm chính xác mà nghiệm vẫn giữ mượt nhờ tích phân.
3. **Đáp ứng xung Dirac $\delta(t - c)$**:
   Thấy tận mắt một cú đập búa tức thời không làm vật nhảy vọt vị trí $y(t)$ mà gây ra bước nhảy tức thời ở **vận tốc $y'(t)$**!
4. **Hình học Phép Tích chập $(f * g)(t)$**:
   Quan sát quá trình "lật ngược – trượt – nhân – lấy diện tích" minh họa cách hệ nhớ lại toàn bộ lịch sử lực tác động quá khứ.

## Tổng quan

Bài bổ sung này tập hợp toàn bộ các minh họa tương tác (JavaScript) của Chương 03 vào một trang, hỗ trợ củng cố trực giác về biến đổi Laplace, biến đổi Laplace ngược và góc nhìn hệ thống.

## Nội dung có trong bộ minh họa

- Trọng số tích phân của biến đổi Laplace và tính tuyến tính
- Các mẫu biến đổi cơ bản và sự dịch chuyển cực
- Biến đổi Laplace ngược và phân tích phân thức hữu tỉ
- Bài toán giá trị đầu, hàm bước đơn vị, hàm xung, tích chập và hàm truyền

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 03"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 03."
  path="interactives/chapter03/index.html"
  height="920px"
%}

### Giải thích: Đọc hành vi hệ trực tiếp từ vị trí 3 cặp cực $s$ trên bản đồ mặt phẳng phức

Giả sử hàm truyền có mẫu số $s^2 + 2\zeta\omega_0 s + \omega_0^2$ với $\omega_0 = 2$:
1. **Cặp cực $s = -1 \pm i\sqrt{3}$** ($\operatorname{Re}(s) = -1 < 0$, $\operatorname{Im}(s) = \pm\sqrt{3}$):
   Đáp ứng xung tắt dần theo đường bao $e^{-t}$ và dao động với tần số $\sqrt{3} \approx 1{,}732\text{ rad/s}$.
2. **Kéo cực sang trái tới $s = -3 \pm i\sqrt{3}$**:
   Tần số dao động giữ nguyên, nhưng đường bao trở thành $e^{-3t}$ — tắt nhanh gấp **3 lần**!
3. **Kéo cực chạm trục ảo $s = \pm 2i$** ($\operatorname{Re}(s) = 0$):
   Đường bao $e^{0\cdot t} = 1$, hệ dao động vĩnh viễn $\frac{1}{2}\sin(2t)$ không tắt dần (ổn định biên). Chỉ cần nhích sang $+0{,}1 \pm 2i$, biên độ phình theo $e^{0{,}1 t} \to \infty$!

## Video tham khảo

- Xem trước: [But what is a Laplace Transform?](https://www.youtube.com/watch?v=j0wJBEZdwLs) — 3Blue1Brown, tiếng Anh. Giới thiệu trực quan về phép biến đổi Laplace trước khi trải nghiệm các khung tương tác của chương.
- [The Laplace Transform - A Graphical Approach](https://www.youtube.com/watch?v=ZGPtPkTft8g) — Brian Douglas, tiếng Anh. Minh họa biến đổi Laplace bằng đồ thị, thuận tiện để đối chiếu trực tiếp với bộ minh họa.
- [Pole Diagrams | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=pUFSXhoazY8) — MIT OpenCourseWare, tiếng Anh. Hướng dẫn cách đọc giản đồ cực và điểm không — dạng đồ thị chính trong bộ minh họa.
