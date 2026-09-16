---
layout: post
title: "11-10 Ứng dụng hiện đại: Neural operator cho bài elliptic"
chapter: '11'
order: 10
owner: Course Team
lang: vi
categories:
- chapter11
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này đặt phương trình Laplace và Poisson, tính chất trung bình và hàm Green cạnh neural operator cùng PINN cho bài elliptic. Sinh viên cần xem dòng Darcy và tĩnh điện như benchmark học toán tử, dùng nguyên lý cực đại như phép thử cứng, và định vị các bài 2021–2024 đã làm ánh xạ elliptic thành bãi thử chuẩn cho FNO, DeepONet và PINO. Lý thuyết thế cổ điển của chương được giữ nguyên.

## Kiến thức nền

Sinh viên cần biết phương trình Laplace, nguồn Poisson, tính chất trung bình, nguyên lý cực đại, và ý niệm hàm Green trên đĩa hoặc hình chữ nhật.

## Dẫn nhập

Phương trình elliptic không tiến hóa. Nó cân bằng. Nghiệm tại một điểm là trung bình các giá trị lân cận, hoặc thế sinh bởi nguồn xa, và đạt cực trị trên biên trừ khi nguồn buộc khác. Phụ thuộc toàn cục ấy đúng là lý do ánh xạ elliptic trở thành bài thử ưa thích của học toán tử: ánh xạ từ hệ số hoặc nguồn tới thế là nonlocal, làm mượt, và nhạy hình học.

Bài dòng Darcy — $$-\nabla\cdot(a\nabla u)=f$$ với độ thấm $$a$$ dao động mạnh — là ví dụ chạy của Fourier neural operator của Li và cộng sự (ICLR 2021) và của Kovachki và cộng sự (*JMLR* 2023). Physics-informed DeepONet (Wang, Wang và Perdikaris, *Science Advances* 2021) cùng PINO (Li và cộng sự, [arXiv:2111.03794](https://arxiv.org/abs/2111.03794)) thêm thông tin phần dư để tập dữ liệu thô vẫn sinh thế độ phân giải cao. PINNacle (Hao và cộng sự, NeurIPS 2024) gồm các bài elliptic và gần elliptic trong so sánh công khai.

Tĩnh điện và dòng không nén, không xoáy, đã có trong chương, là cùng toán tử dưới ký hiệu khác. Sinh viên viết được hàm Green trên đĩa đã biết đối tượng các mạng này đang cố học.

## Khái niệm then chốt

### Toán tử hệ số-sang-nghiệm

Với phương trình Poisson dẫn cố định, toán tử tuyến tính và cho bởi nhân Green. Với dòng Darcy, toán tử $$a\mapsto u$$ phi tuyến. Neural operator được xây cho trường hợp thứ hai: chúng phải tổng quát hóa qua một họ hệ số, không chỉ đảo một Laplacian. Tính chất trung bình rồi không còn đúng, nhưng nguyên lý so sánh vẫn đúng, và vẫn là phép thử hợp lệ.

### Làm mượt và siêu phân giải

Tính chính quy elliptic nói $$u$$ trơn hơn $$a$$ hoặc $$f$$ trên thang Sobolev, tới biên. Mô hình không tinh được thế thô, hoặc bịa dao động mới dưới tinh lưới, không hành xử như nghịch đảo elliptic. Điểm bán của PINO chính là phần dư vật lý ở độ phân giải cao có thể khôi phục sự làm mượt ấy dù ảnh chụp huấn luyện thô.

### Phép thử cực đại và trung bình

Nếu $$f=0$$ và dữ liệu biên nằm giữa $$m$$ và $$M$$, thế học được thoát $$[m,M]$$ thì không đủ tư cách. Nếu miền là đĩa và $$a\equiv 1$$, tính chất trung bình định lượng: giá trị tại tâm là tích phân biên. Các phép thử này không cần bộ giải chuẩn.

### Hình học

Hình chữ nhật, đĩa và miền ngoài dùng hàm Green khác nhau. Geo-FNO (Li, Huang, Huang và Anandkumar, *J. Comput. Phys.* 2023) học biến dạng về miền chuẩn đều để toán tử dựa FFT vẫn dùng được. Đó là tiếng vang hiện đại của kỹ thuật ánh xạ bảo giác và tọa độ cực của chương.

## Phương pháp và kỹ thuật

1. Cố định họ hệ số hoặc nguồn và ánh xạ biên.
2. Sinh cặp huấn luyện bằng bộ giải phần tử hữu hạn hoặc phổ.
3. Huấn luyện FNO, DeepONet hoặc PINO; tùy chọn thêm mất mát phần dư trên lưới mịn hơn.
4. Kiểm chứng bằng phép thử cực đại/trung bình, bảo toàn thông lượng, và hình học hoặc tỷ số tương phản mới.
5. Soi lát Green học được $$f\mapsto u(\cdot;f=\delta)$$ khi bài toán tuyến tính.

PINN vẫn hữu ích cho một miền không đều đơn hoặc nhận dạng nguồn ngược, nhưng thường kém mô hình toán tử khi hàng trăm bài Poisson tương tự phải được giải.

## Ví dụ

### Ví dụ 1: Lấy lại hàm Green trên đĩa

Trên đĩa đơn vị với dữ liệu Dirichlet, nhân Poisson và hàm Green tường minh. Huấn luyện mô hình toán tử tuyến tính trên nguồn ngẫu nhiên rồi dò bằng xấp xỉ delta phải tái tạo nhân điện tích ảnh. Lệch gần biên là tuyên bố về mức mô hình học được nguyên lý ảnh.

### Ví dụ 2: Darcy tương phản cao

Nếu $$a$$ lấy hai giá trị chênh vài bậc độ lớn, thế phát triển gradient dốc dọc giao diện. FNO huấn luyện trên tương phản nhẹ sẽ làm nhoè các giao diện ấy. Thất bại ấy là tuyên bố chính quy elliptic: nghiệm sống trong không gian yếu hơn khi $$a$$ chỉ bị chặn và elliptic, không trơn.

### Ví dụ 3: Kiểm trung bình rời rạc

```python
import numpy as np

u = np.array([[0., 0., 0.],
              [0., 1., 0.],
              [0., 0., 0.]])
resid = 4 * u[1, 1] - u[1, 0] - u[1, 2] - u[0, 1] - u[2, 1]
print(resid)
```

Thế rời rạc học được cho phương trình Laplace phải làm phần dư này nhỏ trong miền trong. Khuôn năm điểm là tính chất trung bình trên lưới.

## Ứng dụng

Dòng dưới mặt đất, thiết kế thiết bị tĩnh điện, dòng thế không nén, và chụp trở kháng điện y khoa là elliptic hoặc gần elliptic. Surrogate học toán tử biến digital twin phần tử hữu hạn thành ánh xạ tương tác từ độ thấm hoặc mật độ điện tích tới thế. Bài elliptic ngược — khôi phục $$a$$ hoặc nguồn từ đo biên — là bài Calderón và họ hàng; neural inverse operator và lấy mẫu hậu nghiệm score là công cụ 2022–2024 được chọn, luôn chịu giới hạn nhận dạng mà lý thuyết thế đã biết.

Bài dòng chảy tùy chọn của chương (dòng không xoáy, không nén) là ứng dụng trực tiếp: hàm dòng hoặc thế học được phải vẫn điều hòa, nên phần dư Laplacian là mất mát vật lý có tên cổ điển.

## Thách thức và hướng mở rộng

Tương phản cao, dị hướng và elliptic suy biến phá ước lượng đều và đánh bại mô hình huấn luyện trên họ nhẹ hơn. Góc và điều kiện biên hỗn hợp sinh kỳ dị mà cơ sở Fourier toàn cục sẽ dao động Gibbs. Dẫn ngược vẫn không đặt chỉnh nặng; ảnh sắc từ mạng không phải chứng minh duy nhất. Bài ba chiều làm căng bộ nhớ GPU cho toán tử dựa FFT. Ghép với vận chuyển hoặc Stokes rời chương elliptic thuần.

Nếu thế học được thỏa nguyên lý cực đại nhưng không liên tục thông lượng qua giao diện, đồng nhất thức biến phân nào đã thất bại? Các đồng nhất thức Green của chương cho câu trả lời.

## Bài tập

1. **Phép thử trung bình.** Với đa thức điều hòa trên đĩa, viết đồng nhất thức trung bình và biến nó thành phép nhận mô hình học được.

2. **Tuyến tính của toán tử Green.** Nếu $$\mathcal{G}(f)$$ là bộ giải Poisson Dirichlet, những đồng nhất thức nào $$\mathcal{G}_\theta$$ học được phải thỏa? Thiết kế hai thí nghiệm, một cho tuyến tính và một cho tính dương.

3. **Tương phản và chính quy.** Giải thích, chỉ dùng trực giác elliptic, vì sao nhân đôi tương phản của $$a$$ có thể hơn nhân đôi gradient của $$u$$ gần giao diện.

4. **Thí nghiệm tính toán.** Giải $$-u''=f$$ trên $$(0,1)$$ với $$u(0)=u(1)=0$$ cho nhiều $$f$$ ngẫu nhiên, huấn luyện ánh xạ tuyến tính trên giá trị nút, và so ma trận học được với ma trận Green rời rạc.

5. **Khám phá mở.** Đọc các thí nghiệm Darcy trong Li và cộng sự (ICLR 2021) hoặc Kovachki và cộng sự (2023) và viết lại một chú thích hình bằng ngôn ngữ chương này (nguyên lý cực đại, hàm Green, chính quy).

## Tài liệu

- Evans, Chương 2 và 6; Haberman, Chương 6–7.
- Li, Z., và cộng sự. “Fourier neural operator.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., Wang, H., và Perdikaris, P. “Physics-informed DeepONets.” *Science Advances* 7, số 40 (2021).
- Li, Z., và cộng sự. “Physics-informed neural operator.” [arXiv:2111.03794](https://arxiv.org/abs/2111.03794).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
