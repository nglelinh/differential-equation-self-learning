---
layout: post
title: "05-11 Bộ Minh họa Tương tác"
chapter: '05'
order: 11
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: optional
---


Động lực học phi tuyến là thế giới của những cú nhảy bất ngờ: chỉ cần xoay nhẹ một tham số điều khiển, một điểm cân bằng ổn định bỗng biến mất, một **chu trình giới hạn (limit cycle)** tự bừng nở như nhịp tim đập, hay quỹ đạo của hệ Lorenz đột ngột bước vào **hỗn loạn (chaos)** nhạy cảm đến từng chữ số thập phân! Bộ minh họa tương tác Chương 05 biến toàn bộ những hiện tượng hình học kỳ diệu đó thành một phòng thí nghiệm trực quan sống động.

## Bản đồ kiến thức nền: Bốn hiện tượng phi tuyến cốt lõi trong Bộ Minh họa Chương 05

1. **Tuyến tính hóa cục bộ vs. Bức tranh toàn cục (Con lắc phi tuyến)**:
   Gần điểm cân bằng $(0, 0)$, con lắc phi tuyến giống hệt tâm tuyến tính; nhưng nhìn toàn cục, nó xuất hiện đường **separatrix** nối các điểm yên ngựa $(\pm\pi, 0)$ phân tách dao động lắc qua lại với chuyển động quay tròn!
2. **Chu trình giới hạn (Limit Cycle — Van der Pol)**:
   Quỹ đạo kín cô lập hút mọi quỹ đạo cả từ bên trong lẫn bên ngoài—hiện tượng **chỉ có ở hệ phi tuyến**, là cơ chế toán học của đồng hồ quả lắc, nhịp tim và xung thần kinh.
3. **Rẽ nhánh (Bifurcations — Yên ngựa–Nút, Chạc ba, Hopf)**:
   Khi kéo tham số $\mu$ vượt giá trị tới hạn $\mu_c$, số lượng hoặc tính ổn định của điểm cân bằng thay đổi đột ngột—ví dụ rẽ nhánh Hopf sinh ra dao động tự duy trì từ một điểm cân bằng yên tĩnh.
4. **Độ nhạy điều kiện đầu & Bầu hút kỳ lạ (Lorenz Attractor)**:
   Hai quỹ đạo xuất phát cách nhau chỉ $10^{-6}$ tách rời nhau theo hàm mũ (hệ số Lyapunov dương) nhưng vẫn bị giam mãi mãi trong một miền hữu hạn mang hình đôi cánh bướm!

## Tổng quan

Bài học bổ sung này tập hợp toàn bộ các minh họa JavaScript của Chương 05 tại một nơi, đóng vai trò tài liệu trực quan đồng hành cho các ý tưởng hình học và định tính trong chương.

## Nội dung có trong bộ minh họa

- Mặt phẳng pha phi tuyến, đường đẳng nghiêng (nullcline) và quỹ đạo
- Điểm cân bằng, tuyến tính hóa và phân loại tính ổn định
- Hàm Lyapunov, chu trình giới hạn và rẽ nhánh
- Mô hình vật ăn thịt – con mồi, cạnh tranh giữa các loài, hỗn loạn và mô hình SIR

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 05"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 05."
  path="interactives/chapter05/index.html"
  height="920px"
%}

### Khung giải thích (nên đọc chậm): Quan sát rẽ nhánh Hopf sinh chu trình giới hạn ngay bằng tay trên hệ cực $\dot{r} = r(\mu - r^2),\; \dot{\theta} = 1$

Đây là mô hình chuẩn mực nhất trong bộ minh họa rẽ nhánh Hopf:
1. **Khi $\mu = -1 < 0$**:
   $\dot{r} = r(-1 - r^2) < 0$ với mọi $r > 0$. Mọi quỹ đạo đều xoáy thu vào gốc $r = 0$ (**xoáy ốc hút duy nhất**).
2. **Khi kéo thanh trượt vượt $\mu = 0$ tới $\mu = +4 > 0$**:
   - Gốc $r = 0$ đổi tính chất thành **không ổn định** (vì gần $r = 0$, $\dot{r} \approx 4r > 0$).
   - Xuất hiện nghiệm cân bằng bán kính dương $r^* = \sqrt{\mu} = \mathbf{2}$: với $0 < r < 2$ thì $\dot{r} > 0$ (đẩy ra ngoài), với $r > 2$ thì $\dot{r} < 0$ (kéo vào trong)!
3. **Kết luận trực quan**: Đường tròn bán kính $r = \sqrt{\mu}$ trở thành một **chu trình giới hạn ổn định**—từ một trạng thái đứng yên, chỉ cần kéo $\mu$ qua $0$ là hệ tự bật dao động bền vững!

## Video tham khảo

- Xem trước: [MAE5790-1 Course introduction and overview](https://www.youtube.com/watch?v=ycJEoqmQvwg) — Cornell MAE, tiếng Anh. Giới thiệu quan điểm không gian pha mà bộ minh họa trực quan hóa.
- [MAE5790-10 van der Pol oscillator](https://www.youtube.com/watch?v=O1lQrHemPsw) — Cornell MAE, tiếng Anh. Ví dụ về chu trình giới hạn để đối chiếu với các chân dung pha phi tuyến trong bộ minh họa.
- [MAE5790-15 Chaotic waterwheel](https://www.youtube.com/watch?v=HljJv7Hf6Zo) — Cornell MAE, tiếng Anh. Bánh xe nước Lorenz minh họa trực quan cho hiện tượng hỗn loạn trong bộ công cụ.
