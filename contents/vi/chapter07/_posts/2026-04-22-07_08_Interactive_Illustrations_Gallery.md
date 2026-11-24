---
layout: post
title: "07-08 Bộ Minh họa Tương tác"
chapter: '07'
order: 8
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: optional
---

Khác với bài toán giá trị ban đầu (IVP) luôn có đúng một nghiệm duy nhất xuất phát từ $t = 0$, **Bài toán giá trị biên (BVP)** đặt điều kiện ở *hai đầu* $x = a$ và $x = b$—giống như bắn một mũi tên từ $a$ phải trúng chính xác hồng tâm ở $b$. Bộ minh họa tương tác Chương 07 cho bạn trực tiếp kéo tham số $\lambda$ để chứng kiến khoảnh khắc cộng hưởng khi mũi tên trúng đích (xuất hiện trị riêng và hàm riêng!), thấy các đường nút dao động tăng dần và quan sát hàm Green gãy khúc ngay tại điểm đặt lực.

## Bản đồ kiến thức nền: Bốn trực giác hình học cần nắm qua Bộ Minh họa Chương 07

1. **Khác biệt định tính giữa IVP và BVP**:
   BVP có thể có **duy nhất 1 nghiệm**, **vô nghiệm**, hoặc **vô số nghiệm** tùy vào việc tham số có trùng với trị riêng hay không.
2. **Định lý dao động Sturm (Số nút của Hàm riêng)**:
   Hàm riêng thứ $n$ của bài toán Sturm–Liouville chính quy luôn có đúng $n - 1$ điểm nút bên trong khoảng $(a, b)$—càng lên bậc cao, sóng càng nhiều nút và năng lượng càng lớn.
3. **Hàm Green $G(x, \xi)$ — Phản ứng với một lực điểm**:
   Đồ thị của $G(x, \xi)$ liên tục tại $x = \xi$ nhưng có **góc gãy** với bước nhảy đạo hàm đúng bằng $1/p(\xi)$—hình dung trực tiếp sợi dây căng bị kéo tại một điểm duy nhất $\xi$!
4. **Suy giảm mũ của chế độ nhiệt so với dao động bảo toàn của dây rung**:
   Cùng một cơ sở hàm riêng $\sin(n\pi x/L)$, phương trình nhiệt dập tắt nhanh các mode bậc cao theo $e^{-(n\pi/L)^2\alpha t}$ còn phương trình sóng giữ chúng dao động mãi theo $\cos(n\pi c t/L)$.

## Tổng quan

Bài học bổ sung này tập hợp toàn bộ các minh họa JavaScript của Chương 07 tại một nơi, đóng vai trò tài liệu trực quan đồng hành cho các khái niệm về bài toán giá trị biên và lý thuyết phổ trong chương.

## Nội dung có trong bộ minh họa

- Hình học của điều kiện biên hai điểm
- Sự chọn lọc trị riêng và cấu trúc nút của hàm riêng
- Tính trực giao có trọng số và trực giác Sturm–Liouville
- Khai triển theo hàm riêng và hàm Green
- Các ứng dụng về dây rung và dẫn nhiệt ổn định

{% include interactive-frame.html
  title="Bộ minh họa tương tác Chương 07"
  description="Trang minh họa tương tác cho toàn bộ các chủ đề của Chương 07."
  path="interactives/chapter07/index.html"
  height="920px"
%}

### Khung giải thích (nên đọc chậm): Quan sát trực quan 3 chế độ nghiệm của BVP $y'' + \lambda y = 0,\; y(0) = 0,\; y(\pi) = B$

Hãy tự thử 3 giá trị $(\lambda, B)$ để thấy sự mong manh đặc trưng của bài toán biên:
- **$\lambda = 2,\; B = 0$** (không phải trị riêng): $y = c_2\sin(\sqrt{2}x)$, mà $\sin(\sqrt{2}\pi) \neq 0 \implies c_2 = 0$ → **duy nhất nghiệm tầm thường $y \equiv 0$**.
- **$\lambda = 4,\; B = 0$** (trùng trị riêng $n = 2$): $y = c_2\sin(2x)$ thỏa $y(\pi) = 0$ với **mọi $c_2 \in \mathbb{R}$** → **vô số nghiệm**!
- **$\lambda = 4,\; B = 1$**: $y(0) = 0 \implies y = c_2\sin(2x) \implies y(\pi) = 0 \neq 1$ → **vô nghiệm hoàn toàn**!

## Video tham khảo

- Xem trước: [Solving the heat equation | DE3](https://www.youtube.com/watch?v=ToIXSwZ1pJU) — 3Blue1Brown, tiếng Anh. Trực quan hóa các chế độ nhiệt tắt dần tương ứng với phần tương tác trong bộ minh họa.
- [Solving the Wave Equation with Separation of Variables... and Guitar String Physics](https://www.youtube.com/watch?v=ywrgWRSQ3PY) — Steve Brunton, tiếng Anh. Các chế độ dao động của dây đàn để đối chiếu với các khung minh họa dây rung.
- [Green's functions: the genius way to solve DEs](https://www.youtube.com/watch?v=ism2SfZgFJg) — Mathemaniac, tiếng Anh. Minh họa đáp ứng xung của hàm Green trong các bài toán giá trị biên.
