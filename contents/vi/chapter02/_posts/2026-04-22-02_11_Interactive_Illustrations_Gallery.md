---
layout: post
title: "02-11 Bộ Minh họa Tương tác"
chapter: '02'
order: 11
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: optional
---


Với phương trình cấp hai, chỉ cần xoay nhẹ hệ số cản $c$ hay tần số cưỡng bức $\omega$, đồ thị nghiệm lập tức biến hình ngoạn mục: từ tắt dần chậm chạp sang dao động tắt dần, rồi bất ngờ tạo ra hiệu ứng **phách (beats)** hay **cộng hưởng (resonance)** làm biên độ vọt lên vô hạn! Bộ minh họa tương tác Chương 02 biến những công thức đặc trưng thành phòng thí nghiệm cơ–điện sống động ngay trên màn hình của bạn.

## Kiến thức cần nhớ: Bốn hiện tượng cần khám phá trong Bộ Minh họa Chương 02

1. **Chuyển pha theo biệt thức $\Delta = c^2 - 4mk$**:
   Kéo thanh trượt $c$ để chứng kiến hệ lò xo chuyển mượt qua 3 chế độ: tắt dần yếu ($\Delta < 0$), tắt dần tới hạn ($\Delta = 0$, hồi vị nhanh nhất không vượt lố) và tắt dần mạnh ($\Delta > 0$).
2. **Đường bao hàm mũ $e^{-\gamma t}$ của nghiệm phức**:
   Khi nghiệm đặc trưng là $-\gamma \pm i\omega_d$, đồ thị dao động luôn bị kẹp chặt giữa hai đường bao $\pm A e^{-\gamma t}$.
3. **Hiện tượng Phách (Beats) & Cộng hưởng (Resonance)**:
   Khi hệ không cản chịu lực cưỡng bức $\cos(\omega t)$ với $\omega \approx \omega_0$, hai sóng giao thoa tạo nhịp phách; khi $\omega = \omega_0$, biên độ tăng tuyến tính theo $t$!
4. **Phổ biên độ–tần số & Sự tương đồng Cơ–Điện**:
   Quan sát đỉnh cộng hưởng thực tế dịch nhẹ sang trái khi có cản và đối chiếu trực tiếp giữa con lắc lò xo $(m, c, k)$ với mạch điện $(L, R, 1/C)$.

## Tổng quan

Bài bổ sung này tập hợp toàn bộ các minh họa tương tác (JavaScript) của Chương 02 vào một trang, đóng vai trò tài liệu trực quan song hành cùng các phương pháp giải và ứng dụng trong chương.

## Nội dung có trong bộ minh họa

- Nghiệm đặc trưng và sự suy giảm theo từng thành phần nghiệm
- Nghiệm kép, nghiệm phức và đường bao dao động
- Hạ bậc, hệ số bất định và biến thiên hằng số
- Phương trình bậc cao, dao động cơ học, mạch RLC và định thức Wronskian

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 02"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 02."
  path="interactives/chapter02/index.html"
  height="920px"
%}

### Giải thích: Tính nhanh ngưỡng tắt dần tới hạn $c_{\text{crit}}$ cho hệ lò xo $m = 1\text{ kg},\; k = 9\text{ N/m}$ trước khi kéo thanh trượt

Phương trình dao động tự do: $y'' + c\,y' + 9y = 0 \implies r^2 + c\,r + 9 = 0$.
- **Biệt thức**: $\Delta = c^2 - 4(1)(9) = c^2 - 36$.
- **Ngưỡng tới hạn**: $\Delta = 0 \iff c_{\text{crit}} = \mathbf{6\text{ N}\cdot\text{s/m}}$.
- Thử 3 điểm trên thanh trượt:
  1. $c = 2 < 6$: $r = -1 \pm i\sqrt{8} \implies$ **dao động tắt dần** với đường bao $e^{-t}$.
  2. $c = 6$: $r_1 = r_2 = -3 \implies y = (c_1 + c_2 t)e^{-3t}$ (**tắt dần tới hạn**—tiêu chuẩn thiết kế giảm xóc ô tô!).
  3. $c = 10 > 6$: $r = -1, -9 \implies y = c_1 e^{-t} + c_2 e^{-9t}$ (**tắt dần mạnh**, trễ hơn do số hạng $e^{-t}$ tắt chậm).

## Video tham khảo

- Xem trước: [Mechanical Vibrations: Underdamped vs Overdamped vs Critically Damped](https://www.youtube.com/watch?v=CTd1uVq5-l8) — Dr. Trefor Bazett, tiếng Anh. Phân biệt các chế độ tắt dần để đối chiếu với minh họa dao động trong bài.
- [Second-Order Ordinary Differential Equations: Solving the Harmonic Oscillator Four Ways](https://www.youtube.com/watch?v=8ePqqZXSMQs) — Steve Brunton, tiếng Anh. Giải bài toán dao động điều hòa theo bốn cách khác nhau, giúp liên hệ các mô hình tương tác trong chương.
- [Undamped Mechanical Vibrations & Hooke's Law // Simple Harmonic Motion](https://www.youtube.com/watch?v=Z52emur7Rko) — Dr. Trefor Bazett, tiếng Anh. Trình bày dao động điều hòa đơn giản làm trường hợp tham chiếu khi không có lực cản.
