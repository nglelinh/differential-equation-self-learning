---
layout: post
title: "10-10 Ứng dụng hiện đại: Lan truyền sóng nơ-ron và ảnh địa chấn"
chapter: '10'
order: 10
owner: Course Team
lang: vi
categories:
- chapter10
lesson_type: optional
---

Làm sao các nhà địa chất biết bên dưới lớp đất đá sâu 5 km có túi dầu, mỏ địa nhiệt hay đứt gãy động đất mà không thể đào cả thành phố lên? Họ tạo một xung chấn nhỏ trên mặt đất, ghi lại tiếng vang bằng hàng nghìn cảm biến (*geophones*), rồi giải bài toán ngược **Full Waveform Inversion (FWI)** trên phương trình sóng $u_{tt} = c(x, z)^2 \nabla^2 u$—và ngày nay kết hợp với **mạng nơ-ron lan truyền sóng** để dựng bản đồ lòng đất nhanh gấp hàng chục lần!

## Kiến thức cần nhớ: Bốn trụ cột của Ảnh Địa chấn & Lan truyền Sóng Nơ-ron

![Phương trình Sóng trong Địa chấn, Âm học & PINN]({{ site.imgurl }}/chapter_img/modern_apps/ma_10_wave_pinn.svg)

1. **Bài toán Thuận (Forward Modeling) vs. Bài toán Ngược (Inversion / FWI)**:
   Bài toán thuận biết vận tốc đá $c(x, z)$ và mô phỏng sóng $u(x, z, t)$. Bài toán ngược chỉ đo được $u$ trên mặt đất $z = 0$ và phải khôi phục lại bản đồ ẩn $c(x, z)$ sâu hàng km bên dưới!
2. **Phương pháp Trạng thái Liên hợp (Adjoint-State Method)**:
   Cơ chế lan truyền ngược (backpropagation) trong vật lý sóng: chạy sóng dư sai số ngược thời gian từ các cảm biến xuống lòng đất rồi tương quan chéo với sóng nguồn xuôi để tìm gradient $\nabla_c \mathcal{L}$!
3. **Mô hình thay thế Nơ-ron (FNO / PINN cho sóng)**:
   Huấn luyện mạng nơ-ron xấp xỉ bản đồ từ trường vận tốc $c(x, z)$ sang địa chấn đồ, rút thời gian mỗi lượt lặp FWI từ hàng giờ xuống mili-giây.
4. **Thách thức đặc thù của Sóng (Cycle Skipping & Tần số cao)**:
   Khác với khuếch tán mượt mà, sóng dao động mạnh nên hàm mất mát $L^2$ có vô số cực tiểu địa phương (*cycle skipping*)—đòi hỏi chiến lược tối ưu đa tỷ lệ (từ tần số thấp lên tần số cao).

## Mục tiêu

Bài tùy chọn này kết nối công thức d’Alembert, tính chất lan truyền hữu hạn tốc độ và định luật bảo toàn năng lượng với các mô hình mạng nơ-ron tích hợp vật lý (PINN) và học toán tử cho bài toán sóng, tập trung vào các ứng dụng địa chấn và âm học giai đoạn 2022–2024. Sau bài học, sinh viên cần chỉ ra được những đồng nhất thức sóng nào mà một bộ giải học được bắt buộc phải tôn trọng, và giải thích vì sao bài toán ngược sóng vẫn mang bản chất phân tích vi cục bộ ngay cả khi áp dụng mạng nơ-ron. Lý thuyết đặt chỉnh cổ điển của phương trình sóng vẫn giữ nguyên vai trò nền tảng.

## Kiến thức nền

Sinh viên cần nắm cách thiết lập phương trình sóng, nghiệm d’Alembert, phương pháp tách biến và phương pháp năng lượng. Các bài tùy chọn về tán sắc và ứng dụng âm học là tài liệu bổ trợ hữu ích.

## Dẫn nhập

Sóng truyền thông tin với tốc độ hữu hạn. Đặc tính này phân biệt phương trình $$u_{tt}=c^2 u_{xx}$$ với phương trình nhiệt và là cơ sở để các bài toán tạo ảnh địa chấn, âm học và điện từ có thể thực hiện được: các kỳ dị trong môi trường để lại dấu vết trên biên sau một khoảng thời gian trễ xác định. Một bộ giải học được nếu bỏ qua tốc độ lan truyền hữu hạn, bảo toàn năng lượng hoặc cấu trúc đường đặc trưng có thể trông chính xác trên các đoạn mô phỏng ngắn nhưng không đáng tin cậy trong bài toán tạo ảnh.

Rasht-Behesht, de Hoop và cộng sự đã minh họa việc dùng PINN cho bài toán ngược địa chấn và nhận dạng vận tốc sóng vào đầu thập niên 2020, bao gồm công trình trên *Journal of Geophysical Research* năm 2022 về PINN theo hướng nghịch đảo toàn dạng sóng (full-waveform). Moseley, Markham và Nissen-Meyer (*Finite Basis Physics-Informed Neural Networks*, *Advances in Computational Mathematics* 2023; [arXiv:2109.09355](https://arxiv.org/abs/2109.09355)) đề xuất PINN phân rã miền, đạt hiệu quả cao hơn đáng kể trên sóng tần số cao so với một mạng toàn cục đơn lẻ. Ở hướng học toán tử, FNO và các biến thể được huấn luyện làm bộ lan truyền sóng tốc độ cao, trong khi các toán tử ngược nơ-ron và mô hình dựa trên score (Molinaro, Yang, Li, Azizzadenesheli, Stuart và Anandkumar, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) giải quyết bài toán ngược khôi phục trường hệ số từ dữ liệu đo trên biên.

Đẳng thức năng lượng và định lý miền phụ thuộc của chương đóng vai trò các phép kiểm chứng đầu vào cho mọi mô hình loại này.

### Giải thích: Tính tay độ sâu lớp đá phản xạ từ thời gian dội sóng địa chấn

Giả sử lớp đất mặt có vận tốc sóng $c_1 = 2.000\text{ m/s}$. Một nguồn nổ ở bề mặt phát xung tại $t = 0$, và cảm biến đặt ngay sát nguồn thu được tiếng vang phản xạ đầu tiên ở $t = 1{,}6\text{ giây}$:
- Tổng quãng đường sóng đi xuống tới mặt phân cách rồi dội ngược lên là $2d = c_1 \cdot t$.
- Độ sâu của tầng đá phản xạ:
  $$d = \frac{c_1 t}{2} = \frac{2.000 \times 1{,}6}{2} = \mathbf{1.600\text{ m}} \quad (1{,}6\text{ km}).$$
Nếu cảm biến thứ hai đặt cách nguồn $x = 2.400\text{ m}$ thu được sóng phản xạ tại $t_2 = 2{,}0\text{ s}$, theo Pythagoras $\sqrt{(x/2)^2 + d^2} = \frac{c_1 t_2}{2} \implies \sqrt{1200^2 + 1600^2} = 2000 = \frac{2000 \times 2{,}0}{2}$ — cho phép đồng thời ước lượng **cả độ sâu $d$ lẫn vận tốc $c_1$** mà chưa biết trước!

## Khái niệm then chốt

### Đường đặc trưng và miền phụ thuộc

Công thức d’Alembert khẳng định $$u(x,t)$$ chỉ phụ thuộc vào dữ liệu ban đầu trên đoạn $$[x-ct,x+ct]$$. Một bộ lan truyền sóng bằng mạng nơ-ron nếu để một xung cục bộ gây ảnh hưởng ra ngoài khoảng này là vi phạm giới hạn tốc độ sóng (siêu ánh sáng) và do đó sai về mặt vật lý, bất kể sai số $$L^2$$ có nhỏ đến đâu. Phép kiểm tra miền phụ thuộc rất trực tiếp: khởi tạo một xung có giá compact và đối chiếu nghiệm với nón đặc trưng (nón ánh sáng).

### Bảo toàn năng lượng như ràng buộc huấn luyện

Đẳng thức bảo toàn năng lượng

$$
\frac{d}{dt}\int\Bigl(\tfrac12 u_t^2+\tfrac12 c^2 u_x^2\Bigr)\,dx=0
$$

đối với dây hữu hạn có biên bảo toàn là một phép kiểm chứng vô hướng quan trọng. Việc bổ sung số hạng phạt mềm cho năng lượng có tác dụng hỗ trợ, nhưng các kiến trúc bảo toàn cấu trúc hoặc bộ tích phân symplectic mới đảm bảo tính nhất quán cao hơn. Các mạng PINN trên sóng tần số cao thường làm tiêu tán năng lượng do thiên kiến phổ (spectral bias) triệt tiêu các thành phần dao động nhanh của $$u_t$$ — tạo ra một dạng độ nhớt số không tồn tại trong phương trình liên tục.

### Bài toán ngược sóng và kỳ dị quan sát được

Bài toán khôi phục trường tốc độ sóng $$c(x)$$ từ dữ liệu đo trên biên không phải là bài toán biên thuận thông thường. Phân tích vi cục bộ cho thấy chỉ những kỳ dị có tia sóng phản xạ truyền tới vùng đặt cảm biến mới có thể quan sát được. Một mạng nơ-ron "tái tạo" chi tiết của $$c(x)$$ từ dữ liệu không mang thông tin tương ứng thực chất đang sinh ra chi tiết ảo. Toán tử ngược nơ-ron và phương pháp lấy mẫu hậu nghiệm khuếch tán (Chung và cộng sự, ICLR 2023) đáng tin cậy nhất khi giới hạn ở phần mặt sóng quan sát được hoặc khi báo cáo rõ độ bất định ở vùng không quan sát được.

### Phân rã miền cho sóng tần số cao

Mạng perceptron đa tầng (MLP) toàn cục gặp nhiều khó khăn khi phải biểu diễn nhiều bước sóng cùng lúc. PINN cơ sở hữu hạn (FBPINN) và các phương pháp phân rã miền giai đoạn 2022–2024 gán từng mạng cục bộ cho mỗi miền con rồi ghép nối chúng bằng điều kiện thông lượng hoặc phạt chồng lấn. Đây là phiên bản mạng nơ-ron của phương pháp phần tử hữu hạn hoặc phần tử phổ, giúp PINN giải bài toán sóng trở nên khả thi ở dải tần số thực tế.

## Phương pháp và kỹ thuật

1. Xác định rõ bài toán là bài toán thuận (lan truyền sóng) hay bài toán ngược (tạo ảnh / khôi phục môi trường).
2. Với bài toán thuận, ưu tiên mô hình học toán tử hoặc PINN phân rã miền; luôn kiểm chứng nón đặc trưng và định luật bảo toàn năng lượng.
3. Với bài toán ngược, xây dựng ánh xạ sóng thuận dưới dạng bộ mô phỏng khả vi (cổ điển hoặc học được) và thực hiện nghịch đảo với hạng điều chuẩn tôn trọng vùng quan sát được.
4. Dùng công thức d’Alembert trên trục thực hoặc nghiệm mode trên đoạn hữu hạn làm phép kiểm chứng cơ sở trước khi triển khai các thí nghiệm quy mô thực địa.
5. Đánh giá sai số dọc theo các đường đặc trưng thay vì chỉ tại thời điểm cuối: sai lệch pha dù chỉ bằng một phần bước sóng cũng có thể gây sai số lớn trong tạo ảnh.

## Ví dụ

### Ví dụ 1: Kiểm tra rò rỉ vượt tốc độ sóng

Khởi tạo $$u(x,0)=\exp(-x^2/\varepsilon^2)$$, $$u_t(x,0)=0$$ trên một miền lớn và đánh giá bộ giải học được tại các điểm có $$|x|>cT+\sqrt{\varepsilon}$$. Giá trị khác 0 đáng kể tại vùng này cho thấy mô hình đã vi phạm nón đặc trưng. Phép kiểm chứng này chỉ cần một lượt chạy thuận và sử dụng trực tiếp kiến thức của chương.

### Ví dụ 2: Sự trôi năng lượng của PINN

Trên đoạn $$[0,\pi]$$ với điều kiện biên Dirichlet, năng lượng của từng mode $$\sin(nx)\cos(nct)$$ phải không đổi theo thời gian. Một mạng PINN huấn luyện trên nhiều mode phải duy trì được năng lượng của từng mode riêng lẻ; nếu các mode bậc cao $$n$$ bị tắt dần, mô hình đang hoạt động như một bộ lọc thông thấp thay vì bộ giải sóng.

### Ví dụ 3: Phép kiểm chứng d’Alembert

```python
import numpy as np

c = 1.0
f = lambda x: np.exp(-x**2)
g = lambda x: 0 * x

def dAlembert(x, t):
    return 0.5 * (f(x - c * t) + f(x + c * t))

print(dAlembert(0.0, 0.5), dAlembert(2.0, 0.5))
```

Mọi bộ lan truyền sóng một chiều học được cần vượt qua phép đối chiếu với công thức này trước khi áp dụng cho các bài toán địa chấn phức tạp.

## Ứng dụng

Nghịch đảo toàn dạng sóng địa chấn (full-waveform inversion), kiểm tra không phá hủy bằng siêu âm, âm học phòng và mô phỏng điện từ miền thời gian đều đòi hỏi giải bài toán sóng thuận lặp đi lặp lại nhiều lần. Các mô hình thay thế đáng tin cậy giúp tăng tốc thiết kế tương tác và đóng vai trò phân bố tiên nghiệm cho bài toán tạo ảnh. Tạo ảnh quang–âm y sinh và âm học đại dương cũng chịu các ràng buộc đặc trưng tương tự. Các công trình về PINN cho bài toán ngược địa chấn (JGR 2022) và toán tử ngược nơ-ron (2023) cho thấy lý thuyết phương trình sóng hiện có những ứng dụng học máy cụ thể và thực chất.

Âm học và hệ phương trình Maxwell (được trình bày trong bài ứng dụng tùy chọn của chương) cũng mang cùng cấu trúc bảo toàn năng lượng và tốc độ lan truyền hữu hạn: một bộ giải Maxwell học được nếu vi phạm đồng nhất thức Poynting rời rạc chính là phiên bản vectơ của hiện tượng trôi năng lượng.

## Thách thức và hướng mở rộng

Sai số tán sắc số thường gây hại nghiêm trọng hơn sai số biên độ trong các bài toán tạo ảnh. Việc áp đặt điều kiện biên hấp thụ vẫn là thách thức lớn đối với PINN. Mô phỏng sóng đàn hồi ba chiều để tạo dữ liệu huấn luyện vẫn có chi phí tính toán cao. Bài toán ngược trở nên kém đặt chỉnh nghiêm trọng khi góc quan sát (khẩu độ thu nhận) bị hạn chế, trong khi các phân bố tiên nghiệm sinh có nguy cơ tạo ra các chi tiết bề ngoài hợp lý nhưng không có thật trong dữ liệu đo. Ngoài ra, các phương trình sóng phi tuyến (như Burgers, KdV hay phương trình Einstein) vượt ra ngoài bức tranh đường đặc trưng tuyến tính.

Câu hỏi suy ngẫm: nếu một mạng nơ-ron bảo toàn tốt năng lượng nhưng làm các điểm kỳ dị di chuyển sai vận tốc, tính chất toán học nào của bài toán đã bị vi phạm? Theo lý thuyết của chương, đó chính là hệ thức đường đặc trưng chứ không phải đẳng thức năng lượng.

## Video tham khảo

- Xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu kiến trúc Fourier neural operator dùng để học ánh xạ nghiệm cho các PDE dạng sóng.
- [Deriving the Wave Equation](https://www.youtube.com/watch?v=UXqUXYaRyGU) — Steve Brunton, tiếng Anh. Ôn lại phương trình sóng cổ điển làm đối tượng cho các mô hình lan truyền sóng học được.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Trình bày DeepONet, một kiến trúc học toán tử song song với FNO cho cùng lớp bài toán nghiệm.

## Bài tập

1. **Nón đặc trưng (nón ánh sáng).** Từ công thức d’Alembert, hãy chứng minh dữ liệu ban đầu có giá compact nằm trong $$[-R,R]$$ sẽ giữ giá của nghiệm trong miền $$|x|\le R+ct$$. Thiết kế một phép kiểm chứng số tương ứng cho bộ giải học được.

2. **Năng lượng của một mode đơn lẻ.** Tính năng lượng của mode $$u=\sin(nx)\cos(nct)$$ trên đoạn $$[0,\pi]$$. Làm thế nào đưa đẳng thức bảo toàn năng lượng vào ràng buộc huấn luyện mà không phá vỡ nguyên lý chồng chất?

3. **Bước nhảy quan sát được.** Giả sử trường vận tốc $$c(x)$$ có một bước nhảy mà không có tia sóng phản xạ nào từ đó truyền tới được các đầu thu hiện có. Vì sao không nên tin vào kết quả khôi phục gần bước nhảy đó ngay cả khi mạng sinh ra hình ảnh sắc nét?

4. **Thí nghiệm tính toán.** Huấn luyện hoặc xây dựng một bộ lan truyền tuyến tính đơn giản và đối chiếu với công thức d’Alembert trên một xung di chuyển. Báo cáo đồng thời sai số $$L^2$$ và phần giá trị rò rỉ ra ngoài nón đặc trưng.

5. **Tìm hiểu mở rộng.** Đọc công trình của Moseley và cộng sự (2023) hoặc Rasht-Behesht và cộng sự (2022) và viết một trang giải thích vì sao sóng tần số cao đòi hỏi phân rã miền, chỉ sử dụng các khái niệm đã học trong chương này.

## Tài liệu

- Evans, Chương 2; Haberman, Chương 4.
- Moseley, B., Markham, A., và Nissen-Meyer, T. “Finite basis physics-informed neural networks.” *Adv. Comput. Math.* 49 (2023). [arXiv:2109.09355](https://arxiv.org/abs/2109.09355).
- Rasht-Behesht, M., Huber, C., Shukla, K., và Karniadakis, G. E. “PINNs for wave propagation and full waveform inversions.” *JGR: Solid Earth* 127 (2022).
- Molinaro, R., và cộng sự. “Neural inverse operators for solving PDE inverse problems.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
