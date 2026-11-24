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


Nếu bạn huấn luyện một mạng nơ-ron thông thường để dự đoán chuyển động con lắc, chỉ sau vài chục chu kỳ, năng lượng dự đoán sẽ tự phình to hoặc tắt lịm—vì mạng không biết gì về định luật bảo toàn năng lượng! **Hamiltonian Neural Networks (HNN)** và **Lagrangian Neural Networks (LNN)** khắc phục triệt để điều này bằng cách nhúng thẳng cấu trúc phương trình vi phân cấp hai bảo toàn năng lượng vào kiến trúc mạng nơ-ron.

## Bản đồ kiến thức nền: Bốn trụ cột của Mạng nơ-ron Cấp Hai & Bảo toàn Vật lý

1. **Hamiltonian Neural Networks (HNN)**:
   Thay vì học trực tiếp $(\dot{q}, \dot{p})$, mạng học một hàm vô hướng duy nhất—năng lượng $H_\theta(q, p)$—rồi suy ra động lực qua phương trình Hamilton $\dot{q} = \frac{\partial H_\theta}{\partial p},\; \dot{p} = -\frac{\partial H_\theta}{\partial q}$, bảo toàn $H_\theta$ chính xác theo cấu trúc!
2. **Lagrangian Neural Networks (LNN)**:
   Học trực tiếp hàm Lagrange $\mathcal{L}_\theta(q, \dot{q})$ và tự động lấy phương trình Euler–Lagrange bậc hai, lý tưởng cho robot nhiều khớp có tọa độ suy rộng phức tạp.
3. **Bộ tích phân Symplectic (Verlet / Leapfrog)**:
   Khi rời rạc hóa hệ cấp hai, bộ giải Euler làm trôi năng lượng theo thời gian; bộ giải symplectic bảo toàn thể tích không gian pha và giữ sai số năng lượng bị chặn suốt hàng triệu bước.
4. **Second-Order Neural ODE (SONODE)**:
   Mở rộng Neural ODE lên bậc hai $\ddot{\mathbf{x}} = f_\theta(\mathbf{x}, \dot{\mathbf{x}}, t)$, cho phép học trực tiếp các hệ dao động, quán tính và quỹ đạo cắt nhau trong không gian vị trí.

## Mục tiêu

Bài đọc tùy chọn này kết nối phương trình hệ số hằng cấp hai, dao động cơ học và phương pháp năng lượng với các nghiên cứu giai đoạn 2019–2024 về mạng nơ-ron Hamiltonian, Lagrangian và neural ODE cấp hai. Sinh viên sẽ nhìn nhận một bộ dao động được học từ dữ liệu như phần mở rộng có cấu trúc của $$y''+p y'+q y=g(t)$$, hiểu vì sao các kiến trúc bảo toàn cấu trúc symplectic hoặc năng lượng thường hoạt động ổn định hơn mạng thông thường trên hệ bảo toàn, và liên hệ tính độc lập theo Wronskian với khả năng nhận dạng các chế độ dao động. Bài không nhắc lại các kỹ thuật giải cổ điển.

## Kiến thức nền

Sinh viên cần nắm phương trình đặc trưng, dao động tắt dần và cưỡng bức, phương pháp hạ bậc và ý nghĩa của định thức Wronskian, đồng thời nhớ công thức động năng và thế năng của bộ dao động có khối lượng đơn vị.

## Dẫn nhập

Phương trình $$y''+\omega^2 y=0$$ là mô hình dao động bảo toàn đơn giản nhất. Nghiệm của nó quay trong mặt phẳng $$(y,y')$$ và bảo toàn năng lượng $$\tfrac12(y')^2+\tfrac12\omega^2 y^2$$. Khi cấu trúc tương tự ẩn trong dữ liệu thực tế — như chuyển động hành tinh, động lực học phân tử, cánh tay robot hay mạch LC — một mạng nơ-ron tổng quát có thể khớp tốt trên quỹ đạo ngắn nhưng vẫn xuất hiện sai số trôi tích lũy dài hạn, vì không có ràng buộc nào buộc mạng bảo toàn năng lượng hay cấu trúc symplectic.

Greydanus, Dzamba và Yosinski đã đề xuất mạng nơ-ron Hamiltonian (Hamiltonian Neural Networks) tại NeurIPS 2019 bằng cách học một hàm Hamiltonian vô hướng $$H_\theta(q,p)$$ rồi tích phân phương trình Hamilton thay vì học trực tiếp một trường vector không có cấu trúc. Cranmer và cộng sự (*Lagrangian Neural Networks*, 2020; [arXiv:2003.04630](https://arxiv.org/abs/2003.04630)) áp dụng phương trình Euler–Lagrange, vốn thuận tiện hơn khi dữ liệu quan sát là vị trí và vận tốc. Tiếp đó, Finzi, Wang và Wilson (*Simplifying Hamiltonian and Lagrangian Neural Networks*, NeurIPS 2020) tinh gọn cách xử lý ràng buộc và hệ tọa độ. Các công trình năm 2022 của Sosanya và Greydanus về mạng Hamiltonian tiêu tán, cùng nghiên cứu của Gruver, Finzi, Goldblum và Wilson (*Deconstructing the Inductive Biases of Hamiltonian Neural Networks*, ICLR 2022), đã làm rõ điều kiện để các giả định cấu trúc này thực sự phát huy hiệu quả.

Tất cả các hướng nghiên cứu trên đều cho thấy một cách nhìn hiện đại đối với Chương 02: cấu trúc tuyến tính cấp hai, năng lượng và tính độc lập tuyến tính của các chế độ dao động không chỉ là công cụ giải tích mà còn là định hướng thiết kế kiến trúc mô hình.

### Khung giải thích (nên đọc chậm): So sánh độ trôi năng lượng của Euler cổ điển vs. Symplectic Euler cho dao động tử $q'' + q = 0$ ($H = \frac{1}{2}(q^2 + p^2)$)

Xuất phát từ $(q_0, p_0) = (1, 0)$ (năng lượng ban đầu $H_0 = 0{,}5$) với bước thời gian $h = 0{,}5$:
1. **Euler hiện (không bảo toàn năng lượng)**:
   - $q_1 = q_0 + h p_0 = 1 + 0 = 1$, $\;p_1 = p_0 - h q_0 = -0{,}5$.
   - Năng lượng sau 1 bước: $H_1 = \frac{1}{2}(1^2 + 0{,}5^2) = \mathbf{0{,}625}$ (tăng vọt **$+25\%$** chỉ sau 1 bước! Sau $N$ bước tăng theo $(1+h^2)^N \to \infty$).
2. **Symplectic Euler (dùng $p_1$ vừa cập nhật để tính $q_1$)**:
   - $p_1 = p_0 - h q_0 = -0{,}5$, $\;q_1 = q_0 + h p_1 = 1 + 0{,}5(-0{,}5) = 0{,}75$.
   - Năng lượng sau 1 bước: $H_1 = \frac{1}{2}(0{,}75^2 + 0{,}5^2) = \mathbf{0{,}40625}$—nó **dao động bị chặn** quanh $0{,}5$ chứ không bao giờ phình ra vô hạn! Đây là lý do HNN luôn đi cặp với bộ giải symplectic.

## Khái niệm then chốt

### Từ nghiệm đặc trưng đến chế độ dao động học được

Phương trình hệ số hằng $$y''+a y'+b y=0$$ có không gian nghiệm hai chiều sinh bởi các thành phần cơ bản do nghiệm đặc trưng quyết định. Nếu dữ liệu gần tuyến tính, một mô hình cấp hai học từ dữ liệu cần khôi phục được bức tranh dao động chiều thấp này. Khi dữ liệu phi tuyến nhưng vẫn bảo toàn năng lượng, hàm Hamiltonian thay thế vai trò của đa thức đặc trưng: mô hình học $$H_\theta$$ để hình học các đường mức tổ chức quỹ đạo chuyển động. Zhong, Dey và Chakraborty (*Symplectic ODE-Net*, ICLR 2020) đi xa hơn khi kết hợp trường động lực học được với bộ tích phân symplectic.

### Năng lượng như công cụ chẩn đoán kiểu Lyapunov

Với dao động không tắt dần, năng lượng được bảo toàn; với dao động tắt dần, năng lượng giảm dần theo thời gian. Một mô hình nơ-ron có sai số $$L^2$$ tức thời nhỏ vẫn có thể tự sinh thêm năng lượng giả tạo, biểu hiện ngay ở biên độ tăng dần theo thời gian. Do đó, theo dõi đồ thị năng lượng dọc theo quỹ đạo mang lại thông tin chẩn đoán quan trọng tương tự việc kiểm tra Wronskian. Mạng Hamiltonian tiêu tán (Sosanya và Greydanus, 2022) tách trường vector thành phần bảo toàn và phần tiêu tán kiểu Rayleigh, tương ứng trực tiếp với cấu trúc của phương trình $$y''+\gamma y'+\omega^2 y=0$$.

### Neural ODE cấp hai

Ta cũng có thể học trực tiếp phương trình cấp hai $$q''=f_\theta(q,q',t)$$, vốn là dạng tự nhiên của các hệ cơ học và tương đương với hệ cấp một theo cặp biến $$(q,q')$$. Lợi thế của việc giữ nguyên dạng cấp hai là ta có thể đặt trực tiếp $$f_\theta=-\nabla V_\theta(q)-\gamma q'$$, qua đó tái hiện mô hình cơ học có tắt dần và lực cưỡng bức với hàm thế học từ dữ liệu.

### Những điều chỉnh từ các phân tích giai đoạn 2022–2024

Gruver và cộng sự (ICLR 2022) chỉ ra rằng một phần lợi thế từng được ghi nhận của mạng Hamiltonian thực chất đến từ việc bài toán dễ tích phân hơn hoặc lựa chọn hệ tọa độ phù hợp hơn, chứ không hoàn toàn do bản thân giả định bảo toàn năng lượng. Nhận xét này có ý nghĩa sư phạm quan trọng: học bảo toàn cấu trúc chỉ hiệu quả khi dữ liệu thực sự gần với hệ Hamiltonian, cũng như phương pháp hệ số bất định chỉ áp dụng được khi hàm cưỡng bức thuộc đúng lớp hàm phù hợp.

## Phương pháp và kỹ thuật

1. Xác định xem dữ liệu thuộc hệ bảo toàn, tiêu tán hay chịu lực cưỡng bức — tương tự cách phân loại trong dao động cơ học.
2. Nếu hệ bảo toàn, học hàm Hamiltonian $$H_\theta$$ hoặc Lagrangian $$L_\theta$$ và dùng bộ tích phân symplectic hoặc biến phân.
3. Nếu hệ tiêu tán, học hàm năng lượng kết hợp thế tiêu tán hoặc số hạng Rayleigh.
4. Nếu hệ chịu lực cưỡng bức và gần tuyến tính, đối chiếu đáp ứng học được với nghiệm riêng tìm bằng hệ số bất định hoặc biến thiên hằng số.
5. Theo dõi các chỉ số chẩn đoán động học: tần số tức thời, đường bao biên độ và thước đo độc lập kiểu Wronskian khi hệ có nhiều chế độ dao động.

Phương pháp biến thiên hằng số cũng có dạng tương ứng trong học máy: giữ cố định lõi bảo toàn tuyến tính $$y''+\omega^2 y$$ và chỉ dùng mạng nơ-ron để học thành phần ngoại lực $$g_\theta(t)$$.

## Ví dụ

### Ví dụ 1: Khớp dao động điều hòa có nhiễu

Dữ liệu lấy mẫu từ $$y=\cos(\omega t)$$ kèm nhiễu nhỏ có thể được khớp bằng một neural ODE không có cấu trúc, nhưng chu kỳ dự đoán thường bị trôi dần. Ngược lại, mạng Hamiltonian với $$H_\theta=\tfrac12 p^2+V_\theta(q)$$ giữ được chu kỳ ổn định vì các đường mức của $$H_\theta$$ là đường cong đóng. Đây chính là ý nghĩa hình học của cặp nghiệm đặc trưng phức được đưa vào kiến trúc mạng.

### Ví dụ 2: Cộng hưởng và hạn chế khi học trên cửa sổ ngắn

Nếu huấn luyện mô hình cho dao động cưỡng bức gần cộng hưởng trên một khoảng thời gian ngắn, mạng nơ-ron thông thường có thể chỉ ghi nhớ xu hướng tăng biên độ mà không nắm được cơ chế $$y''+\omega^2 y=\cos(\omega t)$$. Một mô hình có cấu trúc giữ nguyên toán tử tuyến tính và chỉ học thành phần lực cưỡng bức sẽ nhận diện trực tiếp hiện tượng cộng hưởng này.

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

Một mô hình học máy bảo toàn cấu trúc cần giữ độ dao động năng lượng nhỏ ở mức tương đương, điều mà mạng nơ-ron thông thường khó đảm bảo.

## Ứng dụng

Các mô hình Hamiltonian và Lagrangian học từ dữ liệu được sử dụng trong mô phỏng phân tử, cơ học thiên thể, điều khiển robot và phân tích dao động lưới điện. Vấn đề kỹ thuật cốt lõi là độ ổn định trên khoảng thời gian dài: một bộ điều khiển hoặc mô hình thay thế tự tích lũy thêm năng lượng dần theo thời gian sẽ không an toàn khi vận hành. Bài toán nhận dạng mạch RLC là phiên bản điện học của cùng cách tiếp cận này. Các nghiên cứu giai đoạn 2022–2024 cũng bổ sung cho lĩnh vực học máy khoa học (SciML): giả định cấu trúc cấp hai có thể kết hợp với PINN hoặc toán tử nơ-ron để mô hình liên tục thừa hưởng tính chất bảo toàn ngay từ kiến trúc, thay vì chỉ dựa vào thành phần phạt mềm trong hàm mất mát.

## Thách thức và hướng mở rộng

Việc chọn hệ tọa độ vẫn đòi hỏi sự cẩn trọng, vì cấu trúc Hamiltonian không bất biến dưới mọi phép biến đổi tọa độ của $$q$$. Các hiện tượng tiêu tán mạnh, va chạm tiếp xúc và hệ chuyển mạch lai nằm ngoài phạm vi của cơ học Hamiltonian trơn. Ngoài ra còn có bài toán khả năng nhận dạng: nhiều hàm Hamiltonian khác nhau có thể sinh ra các quỹ đạo ngắn gần như trùng khớp. Nếu tích phân symplectic một hàm $$H_\theta$$ được học sai lệch, mô hình vẫn sẽ bảo toàn chính xác một đại lượng năng lượng không đúng.

Câu hỏi gợi mở: nếu mô hình học được bảo toàn một đại lượng không phải năng lượng vật lý thực, kết quả đó nên được đánh giá là thành công hay thất bại? Định thức Wronskian gợi ra một cách nhìn rõ ràng: các bất biến cấu trúc chỉ thực sự có giá trị khi chúng gắn với tính độc lập tuyến tính hoặc định luật bảo toàn của hệ vật lý thật.

## Video tham khảo

- Xem trước: [Hamiltonian Neural Networks (HNN) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=AEOcss20nDA) — Steve Brunton, tiếng Anh. Giới thiệu mạng nơ-ron Hamiltonian: học hàm Hamiltonian để trường vector bảo toàn cấu trúc symplectic.
- [Second-Order Ordinary Differential Equations: Solving the Harmonic Oscillator Four Ways](https://www.youtube.com/watch?v=8ePqqZXSMQs) — Steve Brunton, tiếng Anh. Trình bày mô hình dao động điều hòa cổ điển mà các kiến trúc mạng trong bài hướng tới bảo toàn.
- [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, tiếng Anh. Trình bày mô hình neural ODE liên tục, nền tảng mà cấu trúc Hamiltonian bổ sung ràng buộc.

## Bài tập

1. **Đẳng thức năng lượng.** Với phương trình $$y''+\gamma y'+\omega^2 y=0$$, nhân hai vế với $$y'$$ để suy ra quy luật tiêu tán năng lượng. Làm thế nào để đưa đẳng thức này thành ràng buộc trong quá trình huấn luyện?

2. **Đa thức đặc trưng học được.** Giả sử một mạng cấp hai tuyến tính sinh ra hai chế độ dao động phức. Hãy khôi phục các hệ số $$a,b$$ trong $$y''+a y'+b y=0$$ và thảo luận về tính duy nhất.

3. **Chẩn đoán bằng Wronskian.** Tạo hai nghiệm học được từ các điều kiện đầu gần nhau và tính Wronskian rời rạc. Việc Wronskian triệt tiêu cho biết điều gì về không gian nghiệm mà mô hình học được?

4. **Thử nghiệm tính toán.** Huấn luyện một neural ODE không có cấu trúc và một mạng Hamiltonian trên dữ liệu lấy mẫu của $$y''+9y=0$$ trong đoạn $$[0,4]$$, rồi ngoại suy sang $$[0,40]$$. So sánh mức độ trôi biên độ giữa hai mô hình.

5. **Khám phá mở.** Đọc bài báo của Gruver và cộng sự (ICLR 2022) và viết nhận xét ngắn: khi nào nên gắn trực tiếp lý thuyết tuyến tính của chương vào kiến trúc mạng, và khi nào chỉ nên dùng nó làm công cụ chẩn đoán?

## Tài liệu

- Boyce và DiPrima, Chương 3–4; Ross, phần dao động cơ và điện.
- Greydanus, S., Dzamba, M., và Yosinski, J. “Hamiltonian neural networks.” *NeurIPS* 2019. [arXiv:1906.01563](https://arxiv.org/abs/1906.01563).
- Cranmer, M., và cộng sự. “Lagrangian neural networks.” 2020. [arXiv:2003.04630](https://arxiv.org/abs/2003.04630).
- Gruver, N., và cộng sự. “Deconstructing the inductive biases of Hamiltonian neural networks.” *ICLR* 2022. [arXiv:2202.04836](https://arxiv.org/abs/2202.04836).
- Zhong, Y. D., Dey, B., và Chakraborty, A. “Symplectic ODE-Net.” *ICLR* 2020. [arXiv:1909.12077](https://arxiv.org/abs/1909.12077).
