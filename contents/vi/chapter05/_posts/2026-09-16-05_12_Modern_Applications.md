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

Hơn một thế kỷ qua, phương pháp trực tiếp của Lyapunov là chuẩn vàng để chứng minh robot hay máy bay tự hành ổn định mà không cần giải tường minh hệ phi tuyến. Tuy nhiên, tìm bằng tay một hàm năng lượng $V(\mathbf{x})$ cho hệ 12 chiều là bài toán cực khó. Ngày nay, các nhà nghiên cứu dùng **mạng nơ-ron** để *học* hàm Lyapunov $V_\theta(\mathbf{x})$ và dùng bộ giải **SMT/SDP** để cấp chứng chỉ toán học tuyệt đối cho tính an toàn của nó.

## Bản đồ kiến thức nền: Bốn trụ cột của Chứng chỉ Lyapunov Nơ-ron

1. **Điều kiện Lyapunov toàn cục/địa phương**:
   $V(\mathbf{0}) = 0$, $V(\mathbf{x}) > 0$ ($\mathbf{x} \neq \mathbf{0}$) và đạo hàm dọc quỹ đạo $\dot{V}(\mathbf{x}) = \nabla V(\mathbf{x}) \cdot \mathbf{f}(\mathbf{x}) < 0$ trên miền hấp dẫn $\mathcal{D}$.
2. **Hàm mất mát Lyapunov (Lyapunov Risk)**:
   Huấn luyện mạng $V_\theta$ bằng cách phạt $\max(0, -V_\theta(\mathbf{x}))$ và $\max(0, \nabla V_\theta \cdot \mathbf{f}(\mathbf{x}) + \epsilon)$ trên các điểm lấy mẫu.
3. **Vòng lặp Người học – Người kiểm chứng (Learner–Verifier / CEGIS)**:
   Bộ giải SMT (như dReal/Z3) tìm **phản ví dụ** nơi $\dot{V}_\theta \ge 0$; nếu có, bổ sung điểm đó vào tập huấn luyện; nếu trả về `UNSAT`, $V_\theta$ chính thức trở thành chứng chỉ an toàn!
4. **Hàm rào chắn điều khiển (Control Barrier Functions — CBF)**:
   Người anh em của hàm Lyapunov, đảm bảo quỹ đạo robot không bao giờ vượt ra khỏi vùng an toàn định trước.

## Mục tiêu

Bài học tùy chọn này kết nối ổn định Lyapunov, tuyến tính hóa và lập luận trên mặt phẳng pha với các nghiên cứu giai đoạn 2019–2023 về chứng chỉ nơ-ron. Sinh viên cần nêu được một hàm Lyapunov học được có nhiệm vụ chứng minh điều gì, phân biệt sự suy giảm trên tập mẫu với sự suy giảm đã được kiểm chứng, đồng thời nắm được các kết quả chính từ bài khảo sát và hội nghị NeurIPS tiêu biểu. Các định lý ổn định cổ điển của chương vẫn đóng vai trò chuẩn mực kiểm định.

## Kiến thức nền

Sinh viên cần nắm hệ tự trị, tuyến tính hóa bằng ma trận Jacobian, cách kiểm tra hàm Lyapunov và các dạng rẽ nhánh cơ bản. Kiến thức về chu trình giới hạn và mô hình SIR có ích nhưng không bắt buộc.

## Dẫn nhập

Hàm Lyapunov đóng vai trò như một chứng chỉ dạng năng lượng: nếu $$V$$ xác định dương và $$\dot V\le 0$$ dọc theo quỹ đạo, điểm cân bằng là ổn định. Tuy nhiên, việc tìm hàm $$V$$ bằng tay thường rất khó. Ý tưởng hiện đại là tham số hóa $$V_\theta$$ bằng mạng nơ-ron và huấn luyện nó — thường đồng thời với bộ điều khiển $$u_\theta$$ — sao cho các bất đẳng thức Lyapunov được đưa vào hàm mất mát. Chang, Roohi và Gao (*Neural Lyapunov Control*, NeurIPS 2019) đã đề xuất một khuôn khổ nền tảng có ảnh hưởng lớn cho hướng tiếp cận này. Sau đó, Dawson, Gao và Fan khảo sát toàn cảnh về các chứng chỉ Lyapunov, barrier và contraction nơ-ron trên *IEEE Transactions on Robotics* 39 (2023): 1749–1767 ([https://doi.org/10.1109/TRO.2022.3232542](https://doi.org/10.1109/TRO.2022.3232542); [arXiv:2202.11762](https://arxiv.org/abs/2202.11762)).

Wu, Clark, Kantaros và Vorobeychik (*Neural Lyapunov Control for Discrete-Time Systems*, NeurIPS 2023; [arXiv:2305.06547](https://arxiv.org/abs/2305.06547)) mở rộng ý tưởng này sang hệ thời gian rời rạc bằng kiểm chứng quy hoạch nguyên hỗn hợp (mixed-integer), tạo ra các bộ điều khiển ổn định có chứng minh trên những bài toán chuẩn phi tuyến. Thông điệp khái niệm cốt lõi cho chương này rất rõ ràng: mạng nơ-ron không nới lỏng định lý Lyapunov, mà chỉ tìm kiếm một hàm đáp ứng đúng các điều kiện của định lý.

### Khung giải thích (nên đọc chậm): Kiểm chứng cầm tay chỉ việc một ứng viên hàm Lyapunov $V(x_1, x_2)$ và tìm phản ví dụ

Xét hệ phi tuyến 2 chiều $\dot{x}_1 = -x_1 + x_2^2$, $\dot{x}_2 = -x_2$ quanh gốc $(0, 0)$ với ứng viên $V(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$:
1. Rõ ràng $V(0, 0) = 0$ và $V > 0$ với mọi $(x_1, x_2) \neq (0, 0)$.
2. Tính đạo hàm dọc quỹ đạo:
   $$\dot{V} = x_1 \dot{x}_1 + x_2 \dot{x}_2 = x_1(-x_1 + x_2^2) - x_2^2 = -x_1^2 + x_2^2(x_1 - 1).$$
3. **Kiểm chứng trên miền $\mathcal{D} = \{x_1 < 1\}$**: Khi $x_1 < 1$, ta có $x_1 - 1 < 0 \implies \dot{V} < 0$ với mọi $(x_1, x_2) \neq (0, 0)$ → **chứng chỉ ổn định tiệm cận hợp lệ trên đĩa $x_1^2 + x_2^2 < 1$**!
4. **Phản ví dụ ngoài miền**: Thử điểm $(x_1, x_2) = (2, 3)$: $\dot{V} = -4 + 9(2 - 1) = +5 > 0$ — đây chính là kiểu phản ví dụ mà bộ Verifier trả về để thu hẹp miền hoặc huấn luyện lại $V_\theta$.

## Khái niệm then chốt

### Chứng chỉ so với bộ dự đoán

Bộ dự đoán quỹ đạo trả lời câu hỏi “trạng thái sẽ đi về đâu?”, còn chứng chỉ trả lời câu hỏi “vì sao ta có thể khẳng định trạng thái ở lại trong tập an toàn?”. Câu hỏi thứ hai chính là bài toán Lyapunov. Một hàm $$V_\theta$$ học được chỉ có giá trị nếu ta kiểm chứng được điều kiện

$$
V_\theta(0)=0,\qquad V_\theta(x)>0\ \text{khi }x\neq 0,\qquad \nabla V_\theta(x)\cdot f\bigl(x,u_\theta(x)\bigr)<0
$$

trên toàn bộ một miền quan tâm, chứ không chỉ trên tập điểm huấn luyện. Dawson và cộng sự (2023) nhấn mạnh rằng tiến bộ thực sự của lĩnh vực nằm ở bước chuyển từ suy giảm trên mẫu sang suy giảm đã được kiểm chứng chặt chẽ.

### Hàm Lyapunov, barrier và contraction nơ-ron

Chứng chỉ barrier giữ quỹ đạo không đi vào vùng mất an toàn, còn metric contraction đảm bảo các quỹ đạo lân cận tiến lại gần nhau. Cả hai đều liên hệ chặt chẽ với hàm Lyapunov và trực giác mặt phẳng pha của chương này. Trong khi đó, tuyến tính hóa vẫn là phép kiểm tra cục bộ thiết yếu: nếu ma trận Jacobian tại điểm cân bằng có trị riêng với phần thực dương, sẽ không tồn tại hàm Lyapunov trơn nào chứng minh được tính ổn định, bất kể mạng nơ-ron có năng lực biểu diễn lớn đến đâu.

### Kiểm chứng theo vòng kín

Các phương pháp hiện đại thường xen kẽ giữa huấn luyện và kiểm chứng. Mạng nơ-ron đề xuất một ứng viên $$V_\theta$$; bộ giải SAT hoặc quy hoạch nguyên hỗn hợp sẽ tìm phản ví dụ $$x$$ thỏa $$\dot V_\theta(x)\ge 0$$; các điểm phản ví dụ này sau đó được bổ sung vào tập huấn luyện. Wu và cộng sự (NeurIPS 2023) đã thiết kế vòng lặp này vận hành hiệu quả cho hệ thời gian rời rạc. Về bản chất, quy trình này tương ứng về mặt tính toán với cách làm bài tập cổ điển: sau khi đề xuất một hàm $$V$$, ta vẫn phải tính $$\dot V$$ và kiểm tra dấu trên miền xét.

### Rẽ nhánh và tính mong manh của chứng chỉ

Nếu tham số vượt qua ngưỡng rẽ nhánh Hopf, một điểm cân bằng ổn định có thể biến thành tiêu điểm không ổn định được bao quanh bởi chu trình giới hạn. Khi đó, chứng chỉ được huấn luyện ở một phía của điểm rẽ nhánh không thể đem tái sử dụng nguyên trạng ở phía còn lại. Đây là lý do thực tiễn cho thấy các sơ đồ rẽ nhánh trong chương vẫn giữ nguyên giá trị.

## Phương pháp và kỹ thuật

1. Xác định trường vector vòng kín $$f(x,u_\theta(x))$$, bao gồm cả giới hạn bão hòa hoặc bộ lọc an toàn nếu có.
2. Huấn luyện $$V_\theta$$ (và có thể đồng thời $$u_\theta$$) bằng hàm mất mát khuyến khích tính xác định dương và điều kiện suy giảm trên một miền lấy mẫu.
3. Kiểm chứng điều kiện suy giảm bằng bộ kiểm chứng chính xác hoặc bảo thủ, thay vì chỉ tăng số lượng điểm mẫu.
4. Xác định tập dưới mức đã kiểm chứng $$\bigl\{x:V_\theta(x)\le c\bigr\}$$ như một miền hút hoặc tập an toàn được bảo đảm.

Chân dung pha vẫn là công cụ trực quan đầu tiên nên dùng. Nếu tập dưới mức của một hàm $$V_\theta$$ học được cắt ngang đa tạp ổn định của một điểm yên ngựa, chứng chỉ đó đang khẳng định một miền hút trái với kết luận của lý thuyết tuyến tính hóa.

## Ví dụ

### Ví dụ 1: Con lắc tắt dần

Với phương trình $$\theta''+\sin\theta+\gamma\theta'=0$$, cơ năng $$V=\tfrac12(\theta')^2+(1-\cos\theta)$$ là một hàm Lyapunov cổ điển, nhưng tự bản thân nó không chứng minh được tốc độ tắt dần theo hàm mũ. Một hàm $$V_\theta$$ nơ-ron có thể bổ sung các số hạng chéo để mở rộng miền hút đã kiểm chứng. Sinh viên nên vẽ các đường đồng mức của cơ năng trước, rồi đặt câu hỏi mạng nơ-ron có thể thêm số hạng nào mà không phá vỡ tính xác định dương.

### Ví dụ 2: Chứng chỉ giả từ lấy mẫu

Giả sử ta chỉ lấy mẫu quanh một tiêu điểm hút và chọn $$V_\theta=\|x\|^2$$. Đạo hàm $$\dot V$$ có thể âm trên toàn bộ tập mẫu, trong khi ở xa hơn tồn tại một nút không ổn định hoặc một chu trình giới hạn chưa được phát hiện. Khi đem kiểm chứng trên một hình hộp đủ lớn, điều kiện sẽ thất bại. Đây chính là lưu ý quen thuộc của chương về sự khác biệt giữa ổn định cục bộ và ổn định toàn cục, được thể hiện trong bối cảnh phần mềm.

### Ví dụ 3: Kiểm tra phần dư suy giảm bằng mã nguồn

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

Kết quả tiến gần $$1$$ trên các điểm mẫu ngẫu nhiên là một tín hiệu tích cực nhưng chưa phải là chứng minh toán học. Đó chính là trọng tâm sư phạm của ví dụ này.

## Ứng dụng

Các chứng chỉ học được hiện đã được sử dụng trong kỹ thuật robot và điều khiển: ổn định máy bay bốn cánh (quadrotor), điều khiển xe bám quỹ đạo và học tăng cường an toàn đều cần cơ sở để bảo đảm chính sách nơ-ron không rời khỏi tập an toàn. Dịch tễ học mang đến một góc nhìn ứng dụng khác: hàm Lyapunov học được cho mô hình dạng SIR có thể chứng nhận trạng thái cân bằng không dịch bệnh là ổn định tiệm cận khi $$R_0<1$$, hoặc thất bại theo cách làm lộ sai lệch trong số hạng lây nhiễm đã học. Trong lĩnh vực học máy khoa học (SciML) rộng hơn, một mạng PINN tuyên bố hội tụ về trạng thái dừng ổn định có thể được yêu cầu cung cấp chứng chỉ ổn định thay vì chỉ báo cáo phần dư nhỏ.

Dawson và cộng sự (2023) đã tổng hợp các lĩnh vực ứng dụng cùng những dạng thất bại phổ biến nhất: kiểm chứng không đầy đủ, miền hút thu được quá nhỏ và chứng chỉ bỏ qua giới hạn của cơ cấu chấp hành.

## Thách thức và hướng mở rộng

Quá trình kiểm chứng gặp khó khăn khi mở rộng lên số chiều cao; việc mã hóa mạng nơ-ron dưới dạng bài toán quy hoạch nguyên hỗn hợp trở nên rất tốn kém khi vượt qua số chiều trạng thái nhỏ. Chứng chỉ cho hệ thời gian rời rạc và hệ thời gian liên tục không thể thay thế lẫn nhau nếu thiếu lập luận chặt chẽ về bước lấy mẫu. Các hệ ngẫu nhiên và hệ lai đòi hỏi mở rộng sang siêu martingale (supermartingale) hoặc họ nhiều hàm Lyapunov. Cuối cùng, một bộ điều khiển được chứng nhận trên mô hình toán học chưa chắc đã được bảo đảm trên đối tượng thực: sai số mô hình có thể làm hỏng điều kiện $$\dot V<0$$.

Câu hỏi phản tư: nếu một chứng chỉ nơ-ron chỉ được kiểm chứng trên một tập compact, nó cho biết điều gì về các quỹ đạo xuất phát bên ngoài tập đó? Phân tích mặt phẳng pha đã trả lời: không thể kết luận gì chắc chắn, ngoại trừ khả năng chúng có thể đi vào tập đó hoặc bị hút sang một miền hút khác.

## Video tham khảo

- Xem trước: [Safe Nonlinear Control using Robust Neural Lyapunov Functions](https://www.youtube.com/watch?v=ZEsQZeBOMDI) — Charles Dawson, tiếng Anh. Bài trình bày về việc học hàm Lyapunov nơ-ron bền vững cho điều khiển an toàn.
- [Arash Mehrjou:  Neural Lyapunov Redesign](https://www.youtube.com/watch?v=ylRDhiFcujs) — Machine Learning and Dynamical Systems Seminar, tiếng Anh. Arash Mehrjou trình bày về thiết kế lại hàm Lyapunov bằng mạng nơ-ron.
- [What is a Lyapunov function](https://www.youtube.com/watch?v=uXAx_641FPM) — richard pates, tiếng Anh. Giới thiệu hàm Lyapunov cổ điển làm nền tảng cho các chứng chỉ học được.

## Bài tập

1. **Rào cản tuyến tính.** Cho hệ $$x'=Ax$$ với ma trận $$A$$ có trị riêng với phần thực dương. Chứng minh rằng không tồn tại hàm Lyapunov $$C^1$$ nào thỏa mãn $$\dot V<0$$ quanh gốc tọa độ. Trong trường hợp này, thuật toán huấn luyện phải xử lý ra sao?

2. **Từ năng lượng đến hàm Lyapunov chặt.** Với con lắc tắt dần, xuất phát từ cơ năng và cộng thêm số hạng chéo nhỏ $$\varepsilon\theta\theta'$$. Với giá trị $$\varepsilon$$ nào thì $$V$$ vẫn xác định dương gần $$0$$, và với $$\varepsilon$$ nào thì $$\dot V$$ âm chặt?

3. **Barrier so với Lyapunov.** Viết điều kiện barrier để giữ $$x_1\ge 0$$ cho một hệ phẳng đơn giản. Điều kiện đó khác gì so với điều kiện $$\dot V<0$$?

4. **Thí nghiệm tính toán.** Huấn luyện một mạng nhỏ $$V_\theta$$ cho hệ $$x'=-x$$, $$y'=-2y$$ trên đĩa đơn vị rồi đánh giá $$\dot V_\theta$$ trên một lưới điểm. Chỉ ra các ô lưới nơi điều kiện suy giảm bị vi phạm.

5. **Khám phá mở.** Đọc bài báo của Dawson, Gao và Fan (IEEE TRO 2023) và tóm tắt trong một trang sự khác biệt giữa chứng chỉ dựa trên lấy mẫu và chứng chỉ đã được kiểm chứng. Sau đó tham khảo thêm Wu và cộng sự (NeurIPS 2023) để ghi chú những điểm trở nên thuận lợi hơn trong thiết lập thời gian rời rạc.

## Tài liệu

- Strogatz, *Nonlinear Dynamics and Chaos*; Arnold, về hình học của tính ổn định.
- Chang, Y.-C., Roohi, N., và Gao, S. “Neural Lyapunov control.” *NeurIPS* 2019. [arXiv:2005.00611](https://arxiv.org/abs/2005.00611).
- Dawson, C., Gao, S., và Fan, C. “Safe control with learned certificates.” *IEEE TRO* 39, số 3 (2023): 1749–1767.
- Wu, J., Clark, A., Kantaros, Y., và Vorobeychik, Y. “Neural Lyapunov control for discrete-time systems.” *NeurIPS* 2023. [arXiv:2305.06547](https://arxiv.org/abs/2305.06547).
