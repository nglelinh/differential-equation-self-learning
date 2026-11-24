---
layout: post
title: "04-11 Bộ Minh họa Tương tác"
chapter: '04'
order: 11
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: optional
---


Với hệ tuyến tính hai chiều $\mathbf{x}' = A\mathbf{x}$, toàn bộ vũ trụ quỹ đạo có thể xảy ra—nút hút, nút đẩy, điểm yên ngựa, xoáy ốc, tâm dao động—đều được đóng gói gọn gàng trong **đúng một mặt phẳng hai tham số** gọi là **mặt phẳng Vết–Định thức (Trace–Determinant Plane)**! Bộ minh họa tương tác Chương 04 cho phép bạn kéo trực tiếp một điểm $(\tau, \Delta)$ trên mặt phẳng này và xem chân dung pha lập tức biến đổi ngoạn mục trước mắt.

## Bản đồ kiến thức nền: Bốn hình ảnh trực quan cốt lõi của Chương 04

1. **Mặt phẳng Vết–Định thức ($\tau = \operatorname{tr} A,\; \Delta = \det A$)**:
   Parabol $\tau^2 - 4\Delta = 0$ phân chia thế giới nghiệm thực (dưới parabol) và thế giới xoáy ốc phức (trên parabol); trục $\Delta = 0$ phân tách điểm yên ngựa ($\Delta < 0$) khỏi nút và xoáy ốc ($\Delta > 0$).
2. **Hai đường thẳng bất biến của Vectơ riêng**:
   Khi $A$ có hai trị riêng thực $\lambda_1, \lambda_2$, mọi quỹ đạo đều bị dẫn hướng bởi hai trục vectơ riêng $\mathbf{v}_1, \mathbf{v}_2$—tiếp tuyến với trục chậm khi tiến về gốc và song song với trục nhanh khi rời xa!
3. **Hướng quay của Xoáy ốc & Tâm**:
   Chỉ cần kiểm tra một vectơ vận tốc duy nhất tại điểm $(1, 0)$ (tức cột 1 của ma trận $A$: $(a_{11}, a_{21})$) là biết ngay quỹ đạo quay cùng hay ngược chiều kim đồng hồ!
4. **Chế độ chuẩn (Normal Modes) của Dao động liên kết**:
   Hai vật nối lò xo có vẻ rung hỗn loạn, nhưng thực chất là chồng chất của đúng 2 chế độ chuẩn cực kỳ đơn giản: cùng pha (tần số thấp) và ngược pha (tần số cao).

## Tổng quan

Bài bổ sung này tập hợp toàn bộ các minh họa tương tác (JavaScript) của Chương 04 vào một trang, giúp củng cố trực giác hình học cho các hệ phương trình vi phân.

## Nội dung có trong bộ minh họa

- Dạng ma trận, trường vector và các hướng riêng
- Hành vi nghiệm ứng với trị riêng thực phân biệt, trị riêng phức và trị riêng lặp
- Hàm mũ ma trận, chân dung pha và hệ không thuần nhất
- Bộ dao động ghép và mô hình ngăn chứa

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 04"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 04."
  path="interactives/chapter04/index.html"
  height="920px"
%}

### Khung giải thích (nên đọc chậm): Phân loại tức thì 3 ma trận trên mặt phẳng $(\tau, \Delta)$ mà KHÔNG cần giải phương trình bậc hai!

Nhớ $\lambda^2 - \tau\lambda + \Delta = 0$ và biệt thức $D = \tau^2 - 4\Delta$:
1. $A_1 = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$: $\tau = 1$, $\Delta = 0 - 6 = \mathbf{-6} < 0 \implies$ **Điểm yên ngựa (Saddle)**, luôn không ổn định!
2. $A_2 = \begin{pmatrix} -1 & -2 \\ 2 & -1 \end{pmatrix}$: $\tau = -2 < 0$, $\Delta = 1 + 4 = 5 > 0$, $D = 4 - 20 = -16 < 0 \implies$ **Xoáy ốc hút (Stable Spiral)**; tại $(1, 0)$ có $\mathbf{x}' = (-1, +2)$ hướng lên trên nên quay **ngược chiều kim đồng hồ**!
3. $A_3 = \begin{pmatrix} -3 & 1 \\ 0 & -2 \end{pmatrix}$: $\tau = -5 < 0$, $\Delta = 6 > 0$, $D = 25 - 24 = +1 > 0 \implies$ **Nút hút (Stable Node)** ổn định tiệm cận!

## Video tham khảo

- Xem trước: [Phase Portraits | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=zmzyW1rP-hk) — MIT OpenCourseWare, tiếng Anh. Giới thiệu các dạng chân dung pha cơ bản để đối chiếu trực tiếp với bộ minh họa.
- [Trace-Determinant Diagram | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=oEskbXrhkkk) — MIT OpenCourseWare, tiếng Anh. Phân tích giản đồ vết – định thức đứng sau việc phân loại các chân dung pha.
- [How (and why) to raise e to the power of a matrix | DE6](https://www.youtube.com/watch?v=O85OWBJ2ayo) — 3Blue1Brown, tiếng Anh. Giải thích trực quan hàm mũ ma trận như toán tử sinh ra quỹ đạo tuyến tính.
