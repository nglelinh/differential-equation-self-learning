---
layout: post
title: "00-13 Ứng dụng hiện đại: Nền tảng học máy khoa học"
chapter: '00'
order: 13
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này nối ngôn ngữ giải tích, đại số tuyến tính và không gian hàm của chương với học máy khoa học (SciML) giai đoạn khoảng 2022–2026. Sau bài học, sinh viên cần thấy đạo hàm tự động như dạng tính toán của quy tắc chuỗi, nhận ra mạng nơ-ron như ánh xạ giữa không gian Euclid hoặc không gian hàm, và giải thích vì sao sự tồn tại, duy nhất và tính đặt chỉnh vẫn quyết định khi mô hình được học thay vì viết tay. Lý thuyết nền đã học không bị viết lại; đây chỉ là lớp ứng dụng.

## Kiến thức nền

Sinh viên cần vững giới hạn, đạo hàm, giải tích nhiều biến, trị riêng, và ý niệm chuẩn trên không gian định chuẩn hoặc không gian tích trong. Không cần đã học deep learning. Chỉ cần biết mạng nơ-ron là họ hàm tham số hóa, được huấn luyện bằng cách giảm một phiếm hàm mất mát, và gradient của phiếm hàm ấy được tính tự động.

## Dẫn nhập

Các nền tảng cổ điển của chương này vốn được xây để làm cho phương trình vi phân trở nên chính xác: cần tính liên tục để chuyển qua giới hạn, cần đạo hàm để viết tốc độ biến thiên, cần đại số tuyến tính để chéo hóa hệ, và cần không gian hàm để đo độ lớn của nghiệm. Chính những nguyên liệu ấy hiện đang tổ chức cả một lĩnh vực gọi là scientific machine learning. Thay vì chỉ khớp một đường cong qua vài điểm dữ liệu, các mô hình hiện đại cố học một luật động lực, một toán tử nghiệm, hoặc một mô hình thay thế tôn trọng ràng buộc vi phân.

Hai câu hỏi làm cho mối liên hệ trở nên cụ thể. Thứ nhất, nếu một mạng residual là hệ động lực rời rạc, điều gì xảy ra khi bước lưới tiến về không và kiến trúc trở thành một trường vector liên tục? Thứ hai, nếu một PDE định nghĩa ánh xạ từ dữ liệu $$a$$ sang nghiệm $$u$$, liệu ta có thể học ánh xạ ấy như một toán tử giữa các không gian Banach thay vì như một vector nút lưới? Cả hai câu hỏi đều vô nghĩa nếu thiếu ngôn ngữ của chương này: điều kiện Lipschitz, Jacobian, tính đủ, và các chuẩn không phụ thuộc ngầm vào một lưới cụ thể.

## Khái niệm then chốt

### Đạo hàm tự động như giải tích tính toán

Huấn luyện mô hình hiện đại đòi hỏi đạo hàm của một mất mát vô hướng theo hàng triệu tham số. Automatic differentiation thực hiện quy tắc chuỗi trên đồ thị tính toán, nên gradient của

$$
\mathcal{L}(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell\bigl(f_\theta(x_i),y_i\bigr)
$$

được nhận đúng (trừ sai số dấu phẩy động) chứ không nhờ khai triển ký hiệu hay sai phân thô. Đó chính là giải tích nhiều biến đã ôn trong chương, nay áp dụng cho các hợp thành quá lớn để viết tay. Hệ quả thực tiễn là mọi bộ giải, tích phân, hay nhân tử Fourier khả vi đều có thể đặt vào vòng học.

### Mạng nơ-ron như ánh xạ tham số hóa

Một mạng feed-forward với tham số $$\theta$$ định nghĩa $$f_\theta:\mathbb{R}^{d_{\mathrm{in}}}\to\mathbb{R}^{d_{\mathrm{out}}}$$. Khi ẩn số là hàm $$u(x)$$, ta hoặc đánh giá $$f_\theta$$ tại các điểm collocated, hoặc nâng cấu trúc lên một toán tử $$\mathcal{G}_\theta$$ tác động trên hàm. Trường hợp thứ nhất sống trong không gian Euclid; trường hợp thứ hai thường sống trong Banach hoặc Hilbert như $$L^2$$ hay $$H^1$$. Sự khác biệt không phải hình thức. Mô hình chỉ định nghĩa trên một lưới không thể đánh giá trên lưới mịn hơn nếu không huấn luyện lại, trong khi một toán tử bất biến rời rạc hóa, về nguyên tắc, có thể chuyển độ phân giải.

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart và Anandkumar đã phát biểu quan điểm toán tử này một cách hệ thống và chứng minh định lý xấp xỉ phổ quát cho neural operator giữa các không gian Banach ([Kovachki và cộng sự, *JMLR* 24(89), 2023](https://jmlr.org/papers/v24/21-1524.html); [arXiv:2108.08481](https://arxiv.org/abs/2108.08481)). Công trình ấy làm chính xác điều chương này đã gợi ý: lý thuyết xấp xỉ sống trong không gian hàm, không chỉ trong $$\mathbb{R}^n$$.

### Phần dư vật lý và tính đặt chỉnh

Physics-informed neural network (PINN) biểu diễn nghiệm chưa biết bằng mạng $$u_\theta$$ và phạt phần dư vi phân cùng số liệu hoặc điều kiện biên. Với bài toán $$u'=f(t,u)$$ ta cực tiểu hóa

$$
\mathcal{L}(\theta)=\sum_{k}\bigl\lvert u_\theta'(t_k)-f\bigl(t_k,u_\theta(t_k)\bigr)\bigr\rvert^2+\sum_{j}\bigl\lvert u_\theta(t_j)-u_j\bigr\rvert^2.
$$

Raissi, Perdikaris và Karniadakis đưa ra khuôn PINN hiện đại năm 2019; bài tổng quan của Karniadakis và cộng sự trên *Nature Reviews Physics* (2021) đặt PINN, học toán tử và bộ giải lai trong cùng một chương trình SciML. Khảo sát 2022 của Cuomo, Di Cola, Giampaolo, Rozza, Raissi và Piccialli rồi sắp xếp phương pháp và các chế độ thất bại ([Cuomo và cộng sự, *J. Sci. Comput.* 2022](https://doi.org/10.1007/s10915-022-01939-z); [arXiv:2201.05624](https://arxiv.org/abs/2201.05624)).

Các định lý tồn tại và duy nhất vẫn là bộ lọc khái niệm đúng. Nếu bài toán giá trị ban đầu không Lipschitz, một thay đổi nhỏ của $$\theta$$ có thể làm $$u_\theta$$ đổi lớn, và mặt cảnh tối ưu trở nên không đáng tin. Ngược lại, khi bài toán vi phân đặt chỉnh, phần dư nhỏ mới là thông tin chứ không phải artifact của một phát biểu không đặt chỉnh.

### Mô hình độ sâu liên tục và tính đủ

Luận án 2022 của Kidger, *On Neural Differential Equations* ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)), trình bày residual net, neural ODE, neural CDE và neural SDE như một họ. Tính đủ của không gian nền quan trọng ở đây như trong giải tích sơ cấp: ta cần một khung trong đó vòng lặp Picard, phương trình liên hợp và tích phân ngẫu nhiên hội tụ. Cùng ngôn ngữ metric và chuẩn dùng cho dãy Cauchy nay chống đỡ việc lấy đạo hàm ngược qua một bộ giải ODE.

## Phương pháp và kỹ thuật

Sự chuyển phương pháp tốt nhất được mô tả như sự đổi ẩn số. Giải tích cổ điển tìm hàm $$u$$ thỏa phương trình. SciML tìm tham số $$\theta$$ sao cho $$u_\theta$$, hoặc toán tử $$\mathcal{G}_\theta$$, thỏa gần đúng một họ phương trình. Động cơ tính toán hầu như luôn là phương pháp bậc nhất trên $$\theta$$, nhưng các đối tượng được lấy đạo hàm vẫn là đạo hàm, Jacobian và tích trong đã học.

Một phân loại hữu ích:

- **Xấp xỉ hàm.** Học $$u_\theta(x)$$ cho một trường hợp, như PINN.
- **Xấp xỉ toán tử.** Học $$\mathcal{G}_\theta:a\mapsto u$$ cho một họ trường hợp, như neural operator.
- **Mô hình lai.** Giữ lõi cơ chế và chỉ học trường vector, closure, hoặc lực còn thiếu.

Cả ba đều đòi hỏi cùng những câu hỏi nền: ẩn số sống ở không gian nào, topology nào làm hội tụ có nghĩa, và cấu trúc đại số tuyến tính nào đang được khai thác?

## Ví dụ

### Ví dụ 1: Khối residual như bước Euler

Lớp residual $$x_{n+1}=x_n+h\,f_\theta(x_n)$$ là Euler tiến cho $$x'=f_\theta(x)$$. Nếu $$f_\theta$$ Lipschitz, quỹ đạo rời rạc hội tụ, khi $$h\to 0$$, tới một quỹ đạo liên tục duy nhất. Đó là Picard–Lindelöf dưới dạng tính toán. Cùng hằng số Lipschitz bảo đảm tính duy nhất cũng kiểm soát độ cứng khi huấn luyện.

### Ví dụ 2: Vì sao việc chọn chuẩn rất quan trọng

Hai ứng viên $$u$$ và $$v$$ có thể trùng tại nút lưới nhưng khác nhau bởi một mode dao động mạnh giữa các nút. Trong chuẩn Euclid của giá trị nút chúng trông gần nhau; trong $$H^1$$ chúng có thể rất xa vì đạo hàm khác nhau. Các bài học toán tử do đó báo lỗi trong chuẩn không gian hàm, không chỉ trên ảnh chụp từng điểm.

### Ví dụ 3: Kiểm tra autodiff tối thiểu

```python
import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.sin(x) * torch.exp(-x)
y.backward()
print(float(x.grad), float((torch.cos(x) - torch.sin(x)) * torch.exp(-x)))
```

Hai số in ra trùng nhau. Nhân rộng ý tưởng ấy lên phần dư PINN hay liên hợp ODE không đổi giải tích; chỉ đổi kích thước đồ thị.

## Ứng dụng trong khoa học, kỹ thuật và ngữ cảnh hiện đại

SciML xuất hiện ở mọi nơi một mô hình vi phân được tin cậy nhưng đắt, không đầy đủ, hoặc chỉ quan sát được một phần. Bộ giả lập khí hậu học toán tử thay thế cho PDE khí quyển; mạng ảnh y khoa đảo ánh xạ elliptic hoặc hyperbolic; kỹ sư điều khiển học chứng chỉ ổn định thay vì chỉ khớp quỹ đạo. Trong mỗi bối cảnh, nền tảng của chương quyết định “xấp xỉ tốt” nghĩa là gì. Một mạng chính xác trong $$L^2$$ có thể vô dụng nếu cực đại điểm hoặc thông lượng mới là đại lượng kỹ thuật. Một trường vector học được mà không Lipschitz sẽ bỏ lại lý thuyết tồn tại, và do đó bỏ lại bộ mô phỏng.

Các bài tổng quan của Karniadakis và cộng sự (2021) và Cuomo và cộng sự (2022) thu thập các miền ứng dụng, trong khi Kovachki và cộng sự (2023) cùng Kidger (2022) cung cấp hai cực lý thuyết: học toán tử trong chiều vô hạn, và mô hình độ sâu liên tục như phương trình vi phân. Các chương sau sẽ gặp lại cùng những bài báo ấy ở dạng chuyên biệt hơn.

## Thách thức và hướng mở rộng

Cần nói rõ vài giới hạn. Đạo hàm tự động trên chân trời thời gian dài có thể không ổn định; phương pháp liên hợp đổi bộ nhớ lấy một ODE mới, đôi khi cũng stiff. Mất mát PINN trộn phần dư, biên và quan sát với trọng số không do phương trình cho sẵn, nên mất mát nhỏ không kéo theo sai số nghiệm nhỏ. Định lý xấp xỉ phổ quát bảo đảm sự tồn tại của một mạng tốt, không bảo đảm gradient descent tìm ra nó. Cuối cùng, mô hình học được có thể phá bảo toàn, tính dương, hoặc bất biến nếu những cấu trúc ấy không được gắn vào kiến trúc.

Câu hỏi để suy nghĩ: nếu hai mạng đạt cùng phần dư, chuẩn không gian hàm nào quyết định mạng nào gần nghiệm thật hơn? Và: tính đủ cho ta điều gì khi ẩn số là một độ đo xác suất trên các quỹ đạo thay vì một đường cong?

## Bài tập

1. **Quy tắc chuỗi và autodiff.** Cho $$y=\sin(e^{x^2})$$. Tính $$y'$$ bằng tay và kiểm tra bằng đạo hàm tự động. Đại lượng nào được lưu trên đồ thị tính toán ở mỗi phép toán sơ cấp?

2. **Hằng số Lipschitz và tính duy nhất.** Xét $$x'=|x|^{1/2}$$ với $$x(0)=0$$. Giải thích vì sao Picard–Lindelöf thất bại, và điều gì sẽ sai nếu một neural ODE dùng trường vector cùng độ chính quy địa phương ấy.

3. **Chuẩn trên lưới.** Lấy $$u_h(x)=\sin(2\pi n x)$$ lấy mẫu trên $$N$$ nút đều của $$[0,1]$$. So sánh chuẩn Euclid nút với xấp xỉ hình thang của $$\|u_h\|_{L^2}$$ và $$\|u_h'\|_{L^2}$$ khi $$n$$ tăng. Chuẩn nào phát hiện dao động?

4. **Thí nghiệm tính toán.** Dùng PyTorch hoặc JAX, huấn luyện mạng hai lớp để khớp $$u(t)=e^{-t}$$ trên $$[0,2]$$ bằng cách chỉ cực tiểu hóa phần dư $$u'+u$$ cùng $$u(0)=1$$. Lặp lại với điều kiện đầu nhiễu. Nghiệm học được đổi thế nào, và định lý nào của chương giải thích độ nhạy?

5. **Khám phá mở.** Đọc phần mở đầu Kovachki và cộng sự (2023) hoặc Kidger (2022) và viết khoảng nửa trang trả lời: neural operator gần với bộ giải số, hàm Green, hay một loại hàm đặc biệt mới?

## Tài liệu

- Boyce, W. E., và DiPrima, R. C. *Elementary Differential Equations*. Phụ lục giải tích và đại số tuyến tính; nền cổ điển mà bài này không thay thế.
- Karniadakis, G. E., và cộng sự. “Physics-informed machine learning.” *Nature Reviews Physics* 3 (2021): 422–440.
- Cuomo, S., và cộng sự. “Scientific machine learning through physics-informed neural networks.” *Journal of Scientific Computing* 92 (2022): 88. [arXiv:2201.05624](https://arxiv.org/abs/2201.05624).
- Kovachki, N., và cộng sự. “Neural operator: learning maps between function spaces with applications to PDEs.” *JMLR* 24, số 89 (2023): 1–97.
- Kidger, P. *On Neural Differential Equations*. Luận án DPhil, Đại học Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
