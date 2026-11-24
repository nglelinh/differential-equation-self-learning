---
layout: post
title: "01-10 Bộ Minh họa Tương tác"
chapter: '01'
order: 10
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: optional
---


Một phương trình vi phân cấp một $y' = f(t, y)$ không cần phải đợi tìm ra công thức nghiệm mới "lên tiếng". Ngay khi bạn vẽ trường hướng (slope field) trên mặt phẳng $(t, y)$, các đường cong tích phân tự động hiện lên như những dòng chảy của sông suối—và bộ minh họa tương tác Chương 01 giúp bạn thả những "chiếc lá điều kiện đầu" $(t_0, y_0)$ trực tiếp vào dòng chảy ấy để xem số phận của chúng!

## Bản đồ kiến thức nền: Bốn hiện tượng cần quan sát trong Bộ Minh họa Chương 01

1. **Trường hướng (Direction Field) & Đường cong tích phân**:
   Mỗi đoạn gạch ngắn tại $(t, y)$ có hệ số góc đúng bằng $f(t, y)$; nghiệm $y(t)$ đơn giản là đường cong tiếp xúc mượt mà với mọi đoạn gạch nó đi qua.
2. **Sự hội tụ về nghiệm ổn định vs. phân kỳ**:
   Với phương trình tuyến tính $y' + ay = b$ ($a > 0$), mọi điều kiện đầu khác nhau đều bị hút về cùng một nghiệm cân bằng $y^* = b/a$ khi $t \to \infty$.
3. **Đường pha 1D & Điểm cân bằng của phương trình tự trị**:
   Đồ thị $f(y)$ theo $y$ cho phép đọc tức thì điểm hút (ổn định), điểm đẩy (không ổn định) và điểm bán ổn định mà không cần giải tích phân.
4. **Hiện tượng tách nghiệm (mất tính duy nhất) & Bùng nổ hữu hạn**:
   Quan sát trực tiếp vì sao nghiệm của $y' = y^2$ lao ra $+\infty$ trong thời gian hữu hạn và vì sao $y' = \sqrt{\vert y\vert}$ có vô số nhánh tách ra từ $y = 0$.

## Tổng quan

Bài học bổ sung này tập hợp toàn bộ các minh họa tương tác bằng JavaScript của Chương 01 vào một trang thống nhất, thuận tiện cho việc ôn tập trực quan, thử nghiệm thay đổi tham số và minh họa nhanh trên lớp.

## Nội dung có trong bộ minh họa

- Trường hướng và bài toán giá trị đầu
- So sánh nghiệm giải tích và nghiệm số
- Các lớp phương trình cấp một: tách biến, tuyến tính, toàn phần và tự trị
- Các mô hình ứng dụng về quần thể, bể pha trộn, cơ học và mạch điện

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 01"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 01."
  path="interactives/chapter01/index.html"
  height="920px"
%}

### Khung giải thích (nên đọc chậm): Đọc trường hướng bằng tay cho $y' = y - t$ dọc hai đường đẳng khuynh (isoclines)

Thay vì vẽ ngẫu nhiên từng điểm, hãy tìm các đường mà độ dốc $y' = m$ không đổi:
1. **Đường đẳng khuynh độ dốc $m = 0$**: $y - t = 0 \implies y = t$. Dọc đường chéo $y = t$, mọi gạch trường hướng đều **nằm ngang**.
2. **Đường đẳng khuynh độ dốc $m = 1$**: $y - t = 1 \implies y = t + 1$. Dọc đường thẳng $y = t + 1$, mọi gạch đều có độ dốc đúng bằng $1$—tức là **trùng khít với chính đường thẳng $y = t + 1$**!
3. **Phát hiện bất ngờ**: Đường thẳng $y(t) = t + 1$ chính là **một nghiệm đúng** của PTVP (thử lại: $y' = 1$, và $y - t = (t+1) - t = 1$). Mọi nghiệm xuất phát phía trên đường này ($y_0 > t_0 + 1$) sẽ vọt lên $+\infty$, còn phía dưới sẽ lao xuống $-\infty$!

## Video tham khảo

- Xem trước: [The Geometric Meaning of Differential Equations // Slope Fields, Integral Curves & Isoclines](https://www.youtube.com/watch?v=ccDMpj2UK_M) — Dr. Trefor Bazett, tiếng Anh. Giới thiệu trường hướng và đường cong tích phân tương ứng với các hình tương tác trong bộ minh họa.
- [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, tiếng Anh. Tổng quan trực quan về các mô hình cấp một trước khi thao tác trên khung tương tác.
- [Direction Fields | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=jOBBwI4CYjM) — MIT OpenCourseWare, tiếng Anh. Buổi hướng dẫn của MIT về trường hướng đi kèm công cụ trực quan hóa.
