---
layout: post
title: "05-12 Ứng dụng hiện đại: Hàm Lyapunov nơ-ron và chứng chỉ học được"
chapter: '05'
order: 12
owner: Course Team
lang: vi
categories:
- chapter05
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này đưa ổn định Lyapunov, tuyến tính hóa và lập luận mặt pha vào tài liệu 2019–2023 về chứng chỉ nơ-ron. Sinh viên cần nêu được một hàm Lyapunov học được được kỳ vọng chứng minh điều gì, phân biệt giảm thực nghiệm với giảm đã kiểm chứng, và định vị khảo sát cùng các kết quả NeurIPS chính. Các định lý ổn định cổ điển của chương vẫn là chuẩn mực chân lý.

## Kiến thức nền

Sinh viên cần biết hệ tự trị, tuyến tính hóa Jacobian, kiểm hàm Lyapunov, và các rẽ nhánh sơ cấp. Chu trình giới hạn và mô hình SIR hữu ích nhưng không bắt buộc.

## Dẫn nhập

Hàm Lyapunov là chứng chỉ kiểu năng lượng: nếu $$V$$ xác định dương và $$\dot V\le 0$$ dọc dòng, cân bằng ổn định. Tìm $$V$$ bằng tay là một nghệ thuật. Ý tưởng hiện đại là tham số hóa $$V_\theta$$ bằng mạng nơ-ron và huấn luyện, thường cùng bộ điều khiển $$u_\theta$$, sao cho các bất đẳng thức Lyapunov trở thành mất mát. Chang, Roohi và Gao (*Neural Lyapunov Control*, NeurIPS 2019) cho một khuôn sớm và có ảnh hưởng. Dawson, Gao và Fan rồi khảo sát cảnh quan rộng hơn của chứng chỉ Lyapunov, barrier và contraction nơ-ron trên *IEEE Transactions on Robotics* 39 (2023): 1749–1767 ([https://doi.org/10.1109/TRO.2022.3232542](https://doi.org/10.1109/TRO.2022.3232542); [arXiv:2202.11762](https://arxiv.org/abs/2202.11762)).

Wu, Clark, Kantaros và Vorobeychik (*Neural Lyapunov Control for Discrete-Time Systems*, NeurIPS 2023; [arXiv:2305.06547](https://arxiv.org/abs/2305.06547)) mở rộng ý tưởng sang thời gian rời rạc với kiểm chứng mixed-integer, sinh bộ điều khiển ổn định có chứng minh trên các benchmark phi tuyến chuẩn. Thông điệp khái niệm cho chương này sắc: mạng nơ-ron không nới định lý Lyapunov. Nó tìm một hàm mà định lý có thể chấp nhận.

## Khái niệm then chốt

### Chứng chỉ versus bộ dự đoán

Bộ dự đoán quỹ đạo trả lời “trạng thái đi đâu?”. Chứng chỉ trả lời “vì sao ta được tin nó ở lại trong một tập an toàn?”. Câu thứ hai là câu hỏi Lyapunov. Một $$V_\theta$$ học được chỉ hữu ích nếu ta kiểm được

$$
V_\theta(0)=0,\qquad V_\theta(x)>0\ \text{khi }x\neq 0,\qquad \nabla V_\theta(x)\cdot f\bigl(x,u_\theta(x)\bigr)<0
$$

trên một miền quan tâm, không chỉ trên mẫu huấn luyện. Dawson và cộng sự (2023) nhấn mạnh tiến bộ của lĩnh vực chính là bước từ giảm trên mẫu tới giảm đã kiểm chứng.

### Lyapunov, barrier và contraction nơ-ron

Chứng chỉ barrier giữ quỹ đạo khỏi tập xấu; metric contraction làm các quỹ đạo gần nhau tiến lại. Cả hai là họ hàng gần của hàm Lyapunov và của trực giác mặt pha đã phát triển ở đây. Tuyến tính hóa vẫn là phép thử địa phương: nếu Jacobian tại cân bằng có trị riêng phần thực dương, không hàm Lyapunov trơn nào chứng minh ổn định được, dù mạng giàu biểu diễn đến đâu.

### Kiểm chứng như vòng kín

Các phương pháp hiện đại xen học và kiểm chứng. Mạng đề xuất $$V_\theta$$; bộ giải SAT hoặc mixed-integer tìm phản ví dụ $$x$$ nơi $$\dot V_\theta(x)\ge 0$$; điểm ấy được thêm vào tập huấn luyện. Wu và cộng sự (NeurIPS 2023) làm vòng ấy hiệu quả trong thời gian rời rạc. Vòng ấy là analogue tính toán của việc kiểm bài tập: sau khi bịa $$V$$, vẫn phải tính $$\dot V$$ và xét dấu.

### Rẽ nhánh và chứng chỉ mong manh

Nếu tham số vượt giá trị Hopf, một cân bằng ổn định trở thành tiêu điểm không ổn định bao quanh bởi chu trình giới hạn. Chứng chỉ huấn luyện một phía rẽ nhánh không thể tái sử dụng mù ở phía kia. Đó là lý do hiện đại để giữ sơ đồ rẽ nhánh của chương.

## Phương pháp và kỹ thuật

1. Xác định trường vòng kín $$f(x,u_\theta(x))$$, gồm bão hòa hoặc bộ lọc an toàn nếu có.
2. Huấn luyện $$V_\theta$$ (và có thể $$u_\theta$$) với mất mát thưởng tính dương và sự giảm trên một miền lấy mẫu.
3. Kiểm chứng điều kiện giảm bằng bộ kiểm đúng hoặc bảo thủ, không chỉ bằng thêm mẫu.
4. Báo tập dưới mức đã kiểm chứng $$\bigl\{x:V_\theta(x)\le c\bigr\}$$ như miền hút hoặc tập an toàn.

Chân dung pha vẫn là hình ảnh hóa đầu tiên. Một $$V_\theta$$ học được có tập dưới mức cắt ngang đa tạp ổn định của yên ngựa đang tuyên bố một miền mà lý thuyết tuyến tính hóa cấm.

## Ví dụ

### Ví dụ 1: Con lắc tắt dần

Với $$\theta''+\sin\theta+\gamma\theta'=0$$ năng lượng $$V=\tfrac12(\theta')^2+(1-\cos\theta)$$ là hàm Lyapunov cổ điển, nhưng tự nó không chứng minh tắt mũ. Một $$V_\theta$$ nơ-ron có thể thêm số hạng chéo và nới miền hút đã kiểm chứng. Sinh viên nên vẽ năng lượng bảo toàn trước, rồi hỏi mạng được phép thêm số hạng nào mà không phá xác định dương.

### Ví dụ 2: Chứng chỉ giả từ mẫu

Giả sử chỉ lấy mẫu quanh một hố xoắn và huấn luyện $$V_\theta=\|x\|^2$$. $$\dot V$$ trên mẫu có thể âm trong khi một nút không ổn định xa, hoặc một chu trình giới hạn, vẫn chưa thấy. Kiểm chứng trên hộp đủ lớn sẽ thất bại. Đây là cảnh báo của chương về ổn định địa phương versus toàn cục, nay dưới dạng phần mềm.

### Ví dụ 3: Phần dư giảm trong mã

```python
import torch

def V(x):
    return (x**2).sum(dim=-1)

def f(x, gamma=0.3):
    q, p = x[..., 0], x[..., 1]
    return torch.stack([p, -q - gamma * p], dim=-1)

x = torch.randn(1000, 2)
x.requires_grad_(True)
Vx = V(x)
gradV = torch.autograd.grad(Vx.sum(), x)[0]
Vdot = (gradV * f(x)).sum(dim=-1)
print(float((Vdot < 0).float().mean()))
```

Giá trị gần $$1$$ trên mẫu ngẫu nhiên là khích lệ và vẫn chưa phải chứng minh. Đó là toàn bộ điểm sư phạm.

## Ứng dụng

Chứng chỉ học được nay nằm trong bộ công cụ robot và điều khiển: ổn định quadrotor, bám quỹ đạo xe, và học tăng cường an toàn đều cần một lý do để tin chính sách nơ-ron sẽ không rời tập an toàn. Dịch tễ cho khán giả khác. Hàm Lyapunov học được cho mô hình kiểu SIR có thể chứng nhận cân bằng không bệnh ổn định tiệm cận khi $$R_0<1$$, hoặc thất bại theo cách lộ sai trong số hạng lây nhiễm học được. Trong SciML rộng hơn, một PINN tuyên bố trạng thái dừng ổn định có thể bị yêu cầu đưa ra chứng chỉ, không chỉ phần dư nhỏ.

Dawson và cộng sự (2023) thu thập các miền ứng dụng và cả các chế độ thất bại chính: kiểm chứng không đầy đủ, miền hút quá nhỏ, và chứng chỉ bỏ qua giới hạn chấp hành.

## Thách thức và hướng mở rộng

Kiểm chứng kém mở rộng theo chiều; mã hóa mixed-integer của mạng trở nên đắt ngoài chiều trạng thái khiêm tốn. Chứng chỉ thời gian rời rạc và liên tục không hoán đổi được nếu không có lập luận lấy mẫu cẩn thận. Hệ ngẫu nhiên và lai cần mở rộng supermartingale hoặc nhiều Lyapunov. Cuối cùng, bộ điều khiển được chứng nhận trên mô hình chưa được chứng nhận trên nhà máy: sai mô hình có thể phá $$\dot V<0$$.

Câu hỏi phản tư: nếu chứng chỉ nơ-ron được kiểm trên tập compact, nó nói gì về quỹ đạo xuất phát ngoài tập ấy? Mặt pha đã trả lời: không gì, trừ việc chúng có thể vào tập hoặc thoát sang hấp dẫn khác.

## Bài tập

1. **Cản tuyến tính.** Cho $$x'=Ax$$ với $$A$$ có trị riêng phần thực dương. Chứng minh không hàm Lyapunov $$C^1$$ nào thỏa $$\dot V<0$$ quanh gốc. Thuật toán huấn luyện phải làm gì?

2. **Từ năng lượng đến Lyapunov chặt.** Với con lắc tắt dần, bắt đầu từ năng lượng cơ học và thêm số hạng chéo nhỏ $$\varepsilon\theta\theta'$$. Với $$\varepsilon$$ nào $$V$$ vẫn xác định dương gần $$0$$, và với $$\varepsilon$$ nào $$\dot V$$ âm chặt?

3. **Barrier versus Lyapunov.** Viết điều kiện barrier giữ $$x_1\ge 0$$ cho một hệ phẳng đơn giản. Điều kiện ấy khác $$\dot V<0$$ thế nào?

4. **Thí nghiệm tính toán.** Huấn luyện mạng nhỏ $$V_\theta$$ cho $$x'=-x$$, $$y'=-2y$$ trên đĩa đơn vị rồi đánh giá $$\dot V_\theta$$ trên lưới. Chỉ các ô lưới nơi sự giảm thất bại.

5. **Khám phá mở.** Đọc Dawson, Gao và Fan (IEEE TRO 2023) và tóm tắt, trong một trang, khác biệt giữa chứng chỉ lấy mẫu và chứng chỉ đã kiểm chứng. Rồi liếc Wu và cộng sự (NeurIPS 2023) và ghi chú điều gì trở nên dễ hơn trong thời gian rời rạc.

## Tài liệu

- Strogatz, *Nonlinear Dynamics and Chaos*; Arnold, về hình học ổn định.
- Chang, Y.-C., Roohi, N., và Gao, S. “Neural Lyapunov control.” *NeurIPS* 2019. [arXiv:2005.00611](https://arxiv.org/abs/2005.00611).
- Dawson, C., Gao, S., và Fan, C. “Safe control with learned certificates.” *IEEE TRO* 39, số 3 (2023): 1749–1767.
- Wu, J., Clark, A., Kantaros, Y., và Vorobeychik, Y. “Neural Lyapunov control for discrete-time systems.” *NeurIPS* 2023. [arXiv:2305.06547](https://arxiv.org/abs/2305.06547).
