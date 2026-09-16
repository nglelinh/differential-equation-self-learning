---
layout: post
title: "02-12 Ứng dụng hiện đại: Mô hình nơ-ron Hamiltonian và cấp hai"
chapter: '02'
order: 12
owner: Course Team
lang: vi
categories:
- chapter02
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này nối phương trình hệ số hằng cấp hai, dao động cơ học và phương pháp năng lượng với tài liệu 2019–2024 về mạng Hamiltonian, Lagrangian và neural ODE cấp hai. Sinh viên cần thấy một dao động tử học được như phần dư có cấu trúc của $$y''+p y'+q y=g(t)$$, giải thích vì sao kiến trúc bảo toàn symplectic hoặc năng lượng vượt mạng generic trên hệ bảo toàn, và nối độc lập Wronskian với khả năng nhận dạng mode. Các kỹ thuật giải cổ điển không bị viết lại.

## Kiến thức nền

Sinh viên cần biết phương trình đặc trưng, dao động tắt dần và cưỡng bức, hạ bậc, và ý nghĩa Wronskian. Chỉ cần nhớ động năng và thế năng của dao động tử khối lượng đơn vị.

## Dẫn nhập

Phương trình $$y''+\omega^2 y=0$$ là dao động tử bảo toàn đơn giản nhất. Nghiệm quay trong mặt phẳng $$(y,y')$$ và bảo toàn năng lượng $$\tfrac12(y')^2+\tfrac12\omega^2 y^2$$. Khi cùng cấu trúc ẩn trong dữ liệu — chuyển động hành tinh, động lực phân tử, cánh tay robot, hoặc mạch LC — một mạng generic có thể khớp quỹ đạo ngắn rồi vẫn trôi thế tục vì không có gì buộc nó bảo toàn năng lượng hay dạng symplectic.

Greydanus, Dzamba và Yosinski đưa ra Hamiltonian neural networks tại NeurIPS 2019 bằng cách học một Hamiltonian vô hướng $$H_\theta(q,p)$$ rồi tích phân phương trình Hamilton thay vì một trường vector vô cấu trúc. Cranmer và cộng sự (*Lagrangian Neural Networks*, 2020; [arXiv:2003.04630](https://arxiv.org/abs/2003.04630)) áp phương trình Euler–Lagrange, thường tiện hơn khi dữ liệu là vị trí và vận tốc. Finzi, Wang và Wilson (*Simplifying Hamiltonian and Lagrangian Neural Networks*, NeurIPS 2020) rồi làm sạch ràng buộc và tọa độ. Các bài 2022 của Sosanya–Greydanus về mạng Hamiltonian tiêu tán và của Gruver, Finzi, Goldblum và Wilson (*Deconstructing the Inductive Biases of Hamiltonian Neural Networks*, ICLR 2022) làm rõ khi nào các prior ấy thực sự giúp.

Tất cả đều là cách đọc hiện đại của chương này: cấu trúc tuyến tính cấp hai, năng lượng, và độc lập tuyến tính của mode không chỉ là thiết bị giải, chúng là prior kiến trúc.

## Khái niệm then chốt

### Từ nghiệm đặc trưng đến mode học được

Phương trình hệ số hằng $$y''+a y'+b y=0$$ có không gian nghiệm hai chiều sinh bởi các mode do nghiệm đặc trưng quyết định. Một mô hình cấp hai học được nên lấy lại bức tranh modal chiều thấp nếu dữ liệu gần tuyến tính. Khi dữ liệu phi tuyến nhưng vẫn bảo toàn, hình ảnh Hamiltonian thay đa thức đặc trưng: ta học $$H_\theta$$ và để hình học các mặt mức tổ chức chuyển động. Zhong, Dey và Chakraborty (*Symplectic ODE-Net*, ICLR 2020) đi thêm bước tích phân trường học được bằng integrator symplectic.

### Năng lượng như chẩn đoán kiểu Lyapunov

Với dao động không tắt dần năng lượng không đổi; với dao động tắt dần nó giảm. Mô hình nơ-ron chính xác về lỗi $$L^2$$ tức thời vẫn có thể tạo năng lượng, thấy ngay như biên độ tăng thế tục. Vẽ năng lượng học được dọc quỹ đạo vì thế giàu thông tin như vẽ Wronskian. Mạng Hamiltonian tiêu tán (Sosanya và Greydanus, 2022) tách trường vector thành phần bảo toàn và tiêu tán kiểu Rayleigh, vang vọng phân tích $$y''+\gamma y'+\omega^2 y=0$$.

### Neural ODE cấp hai

Ta cũng có thể học trực tiếp trường cấp hai $$q''=f_\theta(q,q',t)$$, dạng tự nhiên của hệ cơ học và tương đương hệ cấp một trong $$(q,q')$$. Ưu điểm của việc ở lại dạng cấp hai là có thể áp $$f_\theta=-\nabla V_\theta(q)-\gamma q'$$ và lấy lại mô hình cơ học tắt dần, cưỡng bức với thế học được.

### Điều các phân tích 2022–2024 đã đổi

Gruver và cộng sự (ICLR 2022) cho thấy một số lợi ích được báo của mạng Hamiltonian đến từ việc tích phân dễ hơn hoặc chọn tọa độ tốt hơn, chứ không từ một prior năng lượng thần bí. Cảnh báo ấy có giá trị sư phạm. Học bảo toàn cấu trúc có ích khi dữ liệu thực sự gần Hamiltonian, cũng như hệ số bất định có ích khi lực cưỡng bức thực sự nằm trong họ UC.

## Phương pháp và kỹ thuật

1. Quyết định dữ liệu bảo toàn, tiêu tán, hay cưỡng bức — cùng phân loại dùng cho dao động cơ học.
2. Nếu bảo toàn, học $$H_\theta$$ hoặc Lagrangian $$L_\theta$$ và tích phân symplectic hoặc biến phân.
3. Nếu tiêu tán, học năng lượng cộng thế tiêu tán, hoặc học số hạng Rayleigh.
4. Nếu cưỡng bức và gần tuyến tính, so sánh đáp ứng học được với nghiệm riêng do hệ số bất định hoặc biến thiên tham số.
5. Theo dõi chẩn đoán modal: tần số tức thời, bao biên độ, và một thước độc lập kiểu Wronskian khi có nhiều mode.

Biến thiên tham số có bản sao học máy: đóng băng lõi bảo toàn tuyến tính $$y''+\omega^2 y$$ và chỉ học mạng lực $$g_\theta(t)$$.

## Ví dụ

### Ví dụ 1: Khớp dao động tử điều hòa nhiễu

Mẫu $$y=\cos(\omega t)$$ có nhiễu nhỏ có thể được khớp bởi neural ODE vô cấu trúc, nhưng chu kỳ học được thường trôi. Mạng Hamiltonian với $$H_\theta=\tfrac12 p^2+V_\theta(q)$$ lấy lại chu kỳ không đổi vì các mặt mức của $$H_\theta$$ đóng. Đó là nội dung hình học của nghiệm đặc trưng phức, nay được gắn vào kiến trúc.

### Ví dụ 2: Cộng hưởng như chế độ thất bại khi học

Nếu huấn luyện dao động cưỡng bức gần cộng hưởng trên cửa sổ ngắn, mạng generic có thể nhớ biên độ tăng mà không phát hiện cơ chế $$y''+\omega^2 y=\cos(\omega t)$$. Mô hình có cấu trúc giữ toán tử tuyến tính và chỉ học lực cưỡng bức sẽ nhận ra khớp cộng hưởng ngay.

### Ví dụ 3: Giám sát năng lượng bằng Python

```python
import numpy as np
from scipy.integrate import solve_ivp

def f(t, z, omega=3.0):
    q, p = z
    return [p, -omega**2 * q]

sol = solve_ivp(f, [0, 20], [1.0, 0.0], rtol=1e-8, atol=1e-8, dense_output=True)
t = np.linspace(0, 20, 400)
q, p = sol.sol(t)
energy = 0.5 * p**2 + 0.5 * 9.0 * q**2
print(energy.max() - energy.min())
```

Mô hình học được bảo toàn cấu trúc phải giữ dao động năng lượng nhỏ tương đương. Mạng generic thường không.

## Ứng dụng

Mô hình Hamiltonian và Lagrangian học được xuất hiện trong mô phỏng phân tử, cơ học thiên thể, robot và dao động lưới điện. Câu hỏi kỹ thuật là ổn định chân trời dài: bộ điều khiển hoặc surrogate từ từ bơm năng lượng thì không an toàn. Nhận dạng RLC là bản điện của cùng ý tưởng. Tài liệu 2022–2024 cũng nuôi SciML rộng hơn: một prior cấp hai có thể kết hợp với PINN hoặc neural operator để mô hình liên tục thừa hưởng bảo toàn từ kiến trúc chứ không chỉ từ phạt mềm.

## Thách thức và hướng mở rộng

Chọn tọa độ vẫn tế nhị. Cấu trúc Hamiltonian không bất biến dưới mọi tái tham số hóa của $$q$$. Tiêu tán, tiếp xúc và chuyển mạch lai rời khỏi phạm trù Hamiltonian trơn. Khả năng nhận dạng là vấn đề khác: nhiều Hamiltonian sinh quỹ đạo ngắn giống nhau. Tích phân symplectic của một $$H_\theta$$ học kém sẽ trung thành bảo toàn năng lượng sai.

Câu hỏi phản tư: nếu mô hình học được bảo toàn một đại lượng không phải năng lượng vật lý, ta thành công hay thất bại? Wronskian gợi ý câu trả lời: bất biến cấu trúc chỉ có giá khi chúng tương ứng với độc lập tuyến tính hoặc luật bảo toàn của hệ thật.

## Bài tập

1. **Đẳng thức năng lượng.** Với $$y''+\gamma y'+\omega^2 y=0$$, nhân $$y'$$ và suy ra luật tiêu tán năng lượng. Làm sao biến đẳng thức ấy thành ràng buộc huấn luyện?

2. **Đa thức đặc trưng học được.** Giả sử mạng cấp hai tuyến tính sinh hai mode phức. Khôi phục $$a,b$$ trong $$y''+a y'+b y=0$$ và bàn về tính duy nhất.

3. **Chẩn đoán Wronskian.** Sinh hai nghiệm học được từ dữ liệu đầu gần nhau và tính Wronskian rời rạc. Wronskian triệt tiêu nói gì về không gian nghiệm học được?

4. **Thí nghiệm tính toán.** Khớp neural ODE vô cấu trúc và mạng Hamiltonian với mẫu $$y''+9y=0$$ trên $$[0,4]$$, rồi ngoại suy tới $$[0,40]$$. So sánh trôi biên độ.

5. **Khám phá mở.** Đọc Gruver và cộng sự (ICLR 2022) và viết phê bình ngắn: khi nào lý thuyết tuyến tính của chương nên được gắn cứng vào mạng, và khi nào chỉ dùng như chẩn đoán?

## Tài liệu

- Boyce và DiPrima, Chương 3–4; Ross, về dao động cơ và điện.
- Greydanus, S., Dzamba, M., và Yosinski, J. “Hamiltonian neural networks.” *NeurIPS* 2019. [arXiv:1906.01563](https://arxiv.org/abs/1906.01563).
- Cranmer, M., và cộng sự. “Lagrangian neural networks.” 2020. [arXiv:2003.04630](https://arxiv.org/abs/2003.04630).
- Gruver, N., và cộng sự. “Deconstructing the inductive biases of Hamiltonian neural networks.” *ICLR* 2022. [arXiv:2202.04836](https://arxiv.org/abs/2202.04836).
- Zhong, Y. D., Dey, B., và Chakraborty, A. “Symplectic ODE-Net.” *ICLR* 2020. [arXiv:1909.12077](https://arxiv.org/abs/1909.12077).
