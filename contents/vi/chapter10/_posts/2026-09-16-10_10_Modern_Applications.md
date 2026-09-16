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

## Mục tiêu

Bài tùy chọn này nối công thức d’Alembert, tốc độ hữu hạn và bảo toàn năng lượng với các mô hình vật lý-thông tin và học toán tử cho sóng, nhấn mạnh ứng dụng địa chấn và âm học 2022–2024. Sinh viên cần nói được những đồng nhất thức sóng nào bộ giải học được buộc phải tôn trọng, và vì sao bài ngược sóng vẫn vi cục bộ ngay cả sau khi đưa mạng vào. Lý thuyết đặt chỉnh cổ điển không bị viết lại.

## Kiến thức nền

Sinh viên cần biết suy ra phương trình sóng, nghiệm d’Alembert, tách biến, và phương pháp năng lượng. Các bài tùy chọn về tán sắc và âm học hữu ích.

## Dẫn nhập

Sóng mang thông tin với tốc độ hữu hạn. Sự thật ấy phân biệt $$u_{tt}=c^2 u_{xx}$$ với phương trình nhiệt và là lý do ảnh địa chấn, âm học và điện từ thậm chí có thể được thử: kỳ dị để lại dấu trên biên sau một trễ tính được. Bộ giải học được bỏ qua tốc độ hữu hạn, năng lượng hoặc đặc trưng có thể trông chính xác trên phim ngắn vẫn vô dụng như động cơ ảnh hóa.

Rasht-Behesht, de Hoop và cộng sự đã minh họa PINN cho đảo địa chấn và nhận dạng tốc độ sóng vào đầu những năm 2020, gồm công trình *Journal of Geophysical Research* 2022 về PINN kiểu full-waveform. Moseley, Markham và Nissen-Meyer (*Finite Basis Physics-Informed Neural Networks*, *Advances in Computational Mathematics* 2023; [arXiv:2109.09355](https://arxiv.org/abs/2109.09355)) đưa ra PINN phân rã miền thành công hơn nhiều trên sóng tần số cao so với một mạng toàn cục. Ở phía học toán tử, FNO và hậu duệ được huấn luyện như bộ lan truyền sóng rẻ, trong khi toán tử ngược nơ-ron và mô hình score (Molinaro, Yang, Li, Azizzadenesheli, Stuart và Anandkumar, 2023; [arXiv:2201.12904](https://arxiv.org/abs/2201.12904)) tấn công bài ngược khôi phục hệ số từ vết biên.

Đẳng thức năng lượng và định lý miền phụ thuộc của chương là các phép kiểm đầu vào cho mọi mô hình ấy.

## Khái niệm then chốt

### Đặc trưng và miền phụ thuộc

Công thức d’Alembert nói $$u(x,t)$$ chỉ phụ thuộc dữ liệu đầu trên $$[x-ct,x+ct]$$. Bộ lan truyền nơ-ron để xung định xứ ảnh hưởng một điểm ngoài khoảng ấy là siêu ánh sáng và do đó sai, bất kể điểm $$L^2$$. Kiểm miền phụ thuộc đơn giản: khởi tạo bump compact và vẽ nón ánh sáng.

### Bảo toàn năng lượng như ràng buộc huấn luyện

Đẳng thức

$$
\frac{d}{dt}\int\Bigl(\tfrac12 u_t^2+\tfrac12 c^2 u_x^2\Bigr)\,dx=0
$$

cho dây hữu hạn với biên bảo toàn là unit test vô hướng. Phạt năng lượng mềm giúp, nhưng kiến trúc bảo toàn cấu trúc hoặc integrator symplectic trung thực hơn. PINN tần số cao thường tiêu tán năng lượng vì thiên kiến phổ giết phần dao động của $$u_t$$; đó là nhớt số mà phương trình liên tục không chứa.

### Sóng ngược và kỳ dị nhìn thấy được

Khôi phục $$c(x)$$ từ vết biên không phải BVP chuẩn. Phân tích vi cục bộ, được xem trước ở các chương sau, nói chỉ một số kỳ dị nhìn thấy được. Mạng “tái tạo” $$c$$ trơn từ dữ liệu không thể thấy nó đang ảo giác. Neural inverse operator và diffusion posterior sampling (Chung và cộng sự, ICLR 2023) đáng tin nhất khi bị hạn chế vào phần nhìn thấy của mặt sóng, hoặc khi chúng báo bất định trên phần không nhìn thấy.

### Phân rã miền cho tần số cao

Multilayer perceptron toàn cục không thích nhiều bước sóng. PINN cơ sở hữu hạn và các phân rã 2022–2024 liên quan gán mạng địa phương cho mỗi miền con và nối chúng bằng thông lượng hoặc phạt chồng. Đó là analogue nơ-ron của lưới phần tử hữu hạn hoặc phổ-phần tử, và là lý do PINN sóng trở nên khả thi ở tần số thực tế.

## Phương pháp và kỹ thuật

1. Quyết định nhiệm vụ là thuận (lan truyền) hay ngược (ảnh hóa).
2. Với nhiệm vụ thuận, ưu tiên mô hình toán tử hoặc PINN phân rã; kiểm nón ánh sáng và năng lượng.
3. Với nhiệm vụ ngược, viết ánh xạ sóng thuận như bộ mô phỏng khả vi (cổ điển hoặc học được) và đảo với regularizer tôn trọng tầm nhìn.
4. Dùng d’Alembert trên đường thẳng, hoặc nghiệm modal trên khoảng, như unit test trước mọi thí nghiệm quy mô hiện trường.
5. Báo lỗi trên đặc trưng, không chỉ tại thời cuối: lỗi pha một phần bước sóng là lỗi ảnh hóa lớn.

## Ví dụ

### Ví dụ 1: Rò siêu ánh sáng

Khởi tạo $$u(x,0)=\exp(-x^2/\varepsilon^2)$$, $$u_t=0$$, trên khoảng lớn và đánh giá bộ giải học được tại điểm có $$|x|>cT+\sqrt{\varepsilon}$$. Giá trị khác không là phá nón ánh sáng. Phép thử tốn một lượt thuận và không dùng gì ngoài chương này.

### Ví dụ 2: Trôi năng lượng của PINN

Trên $$[0,\pi]$$ với dữ liệu Dirichlet, năng lượng modal của $$\sin(nx)\cos(nct)$$ không đổi. PINN huấn luyện trên vài mode phải giữ từng năng lượng modal. Nếu $$n$$ cao tắt, mô hình là bộ lọc thông thấp, không phải bộ giải sóng.

### Ví dụ 3: Unit test d’Alembert

```python
import numpy as np

c = 1.0
f = lambda x: np.exp(-x**2)
g = lambda x: 0 * x

def dAlembert(x, t):
    return 0.5 * (f(x - c * t) + f(x + c * t))

print(dAlembert(0.0, 0.5), dAlembert(2.0, 0.5))
```

Mọi bộ lan truyền một chiều học được phải so với công thức này trước khi được yêu cầu làm địa chấn.

## Ứng dụng

Đảo dạng sóng đầy đủ địa chấn, kiểm không phá hủy siêu âm, âm học phòng, và mô phỏng điện từ miền thời gian đều cần nhiều lần giải sóng thuận. Surrogate đáng tin biến các vòng ấy thành thiết kế tương tác hoặc prior cho ảnh hóa. Ảnh quang-âm y khoa và âm học đại dương đặt cùng ràng buộc đặc trưng. Các đảo PINN kiểu JGR 2022 và các bài neural inverse operator 2023 là dấu hiệu sớm nhưng cụ thể rằng chương sóng nay có thực hành học máy, không chỉ ẩn dụ.

Âm học và hệ Maxwell, đã bàn ở bài ứng dụng tùy chọn, thừa hưởng cùng cấu trúc năng lượng và tốc độ hữu hạn. Bộ giải Maxwell học được phá đồng nhất thức Poynting rời rạc là phiên bản vector của trôi năng lượng.

## Thách thức và hướng mở rộng

Lỗi tán sắc hại hơn lỗi biên độ cho ảnh hóa. Điều kiện biên hấp thụ khó với PINN. Sóng đàn hồi ba chiều vẫn đắt để mô phỏng cho huấn luyện. Bài ngược không đặt chỉnh nặng tại khẩu độ thiếu. Prior sinh có thể khôi phục kết cấu hợp lý không có trong dữ liệu. Sóng phi tuyến (Burgers, KdV, Einstein) rời bức tranh đặc trưng tuyến tính.

Câu hỏi giữ lại: nếu mạng bảo toàn năng lượng nhưng di chuyển kỳ dị với tốc độ sai, đồng nhất thức nào đã thất bại? Câu trả lời của chương là hệ thức đặc trưng, không phải đẳng thức năng lượng.

## Bài tập

1. **Nón ánh sáng.** Từ d’Alembert, chứng minh dữ liệu đầu giá compact ở lại trong $$|x|\le R+ct$$. Thiết kế phép thử số cho bộ giải học được.

2. **Năng lượng của một mode.** Tính năng lượng của $$u=\sin(nx)\cos(nct)$$ trên $$[0,\pi]$$. Làm sao biến đẳng thức thành ràng buộc huấn luyện mà không phá chồng chất?

3. **Nhảy nhìn thấy được.** Giả sử $$c(x)$$ có nhảy mà không tia phản xạ từ các thu có sẵn có thể chạm. Vì sao tái tạo không nên được tin gần nhảy ấy, dù mạng sinh ảnh sắc?

4. **Thí nghiệm tính toán.** Huấn luyện hoặc gắn cứng một bộ lan truyền tuyến tính và so với d’Alembert trên xung chuyển động. Báo cả lỗi $$L^2$$ lẫn rò giá ngoài nón ánh sáng.

5. **Khám phá mở.** Đọc Moseley và cộng sự (2023) hoặc Rasht-Behesht và cộng sự (2022) và viết một trang về vì sao sóng tần số cao buộc phân rã miền, chỉ dùng ý của chương này.

## Tài liệu

- Evans, Chương 2; Haberman, Chương 4.
- Moseley, B., Markham, A., và Nissen-Meyer, T. “Finite basis physics-informed neural networks.” *Adv. Comput. Math.* 49 (2023). [arXiv:2109.09355](https://arxiv.org/abs/2109.09355).
- Rasht-Behesht, M., Huber, C., Shukla, K., và Karniadakis, G. E. “PINNs for wave propagation and full waveform inversions.” *JGR: Solid Earth* 127 (2022).
- Molinaro, R., và cộng sự. “Neural inverse operators for solving PDE inverse problems.” 2023. [arXiv:2201.12904](https://arxiv.org/abs/2201.12904).
- Chung, H., và cộng sự. “Diffusion posterior sampling.” *ICLR* 2023. [arXiv:2209.14687](https://arxiv.org/abs/2209.14687).
