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

Bài học tùy chọn này đặt phương trình Laplace, phương trình Poisson, tính chất giá trị trung bình và hàm Green bên cạnh neural operator cùng PINN cho các bài toán elliptic. Sinh viên cần nhìn nhận dòng Darcy và bài toán tĩnh điện như các bài toán chuẩn (benchmark) của học toán tử, sử dụng nguyên lý cực đại như một phép kiểm tra chặt chẽ, đồng thời nắm được các công trình giai đoạn 2021–2024 đã đưa ánh xạ elliptic thành bài thử tiêu chuẩn cho FNO, DeepONet và PINO. Phần lý thuyết thế cổ điển của chương vẫn được giữ làm nền tảng.

## Kiến thức nền

Sinh viên cần nắm phương trình Laplace, số hạng nguồn trong phương trình Poisson, tính chất giá trị trung bình, nguyên lý cực đại và ý niệm hàm Green trên đĩa tròn hoặc hình chữ nhật.

## Dẫn nhập

Phương trình elliptic không mô tả sự tiến hóa theo thời gian mà mô tả trạng thái cân bằng. Nghiệm tại một điểm là giá trị trung bình của các điểm lân cận, hoặc là thế sinh bởi nguồn ở xa, và đạt cực trị trên biên trừ khi số hạng nguồn làm thay đổi điều đó. Chính sự phụ thuộc toàn cục này khiến ánh xạ nghiệm của bài toán elliptic trở thành bài thử ưa thích trong lĩnh vực học toán tử: ánh xạ từ hệ số hoặc nguồn sang thế có tính phi cục bộ, có tác dụng làm trơn và nhạy cảm với hình học của miền.

Bài toán dòng Darcy — $$-\nabla\cdot(a\nabla u)=f$$ với độ thấm $$a$$ biến thiên mạnh — là ví dụ xuyên suốt trong công trình về Fourier neural operator của Li và cộng sự (ICLR 2021) và của Kovachki và cộng sự (*JMLR* 2023). Physics-informed DeepONet (Wang, Wang và Perdikaris, *Science Advances* 2021) cùng PINO (Li và cộng sự, [arXiv:2111.03794](https://arxiv.org/abs/2111.03794)) bổ sung thông tin phần dư của phương trình để ngay cả tập dữ liệu huấn luyện có độ phân giải thô vẫn cho ra trường thế độ phân giải cao. Bộ chuẩn PINNacle (Hao và cộng sự, NeurIPS 2024) cũng đưa các bài toán elliptic và gần elliptic vào khuôn khổ so sánh công khai.

Tĩnh điện và dòng chảy không nén được, không xoáy — vốn đã xét trong chương — thực chất dùng cùng một toán tử dưới các ký hiệu khác nhau. Sinh viên đã biết cách viết hàm Green trên đĩa tròn tức là đã hiểu đối tượng toán học mà các mô hình mạng này đang cố gắng xấp xỉ.

## Khái niệm then chốt

### Toán tử từ hệ số sang nghiệm

Với phương trình Poisson có hệ số khuếch tán cố định, toán tử nghiệm là tuyến tính và được biểu diễn qua nhân Green. Với bài toán dòng Darcy, toán tử $$a\mapsto u$$ lại là phi tuyến. Neural operator được thiết kế cho trường hợp thứ hai: mô hình phải tổng quát hóa trên cả một họ hệ số, chứ không chỉ đảo ngược một toán tử Laplace cố định. Khi đó, tính chất giá trị trung bình không còn đúng nguyên dạng, nhưng nguyên lý so sánh vẫn còn hiệu lực và vẫn là phép kiểm tra hợp lệ.

### Tính làm trơn và siêu phân giải

Tính chính quy elliptic khẳng định rằng $$u$$ trơn hơn $$a$$ hoặc $$f$$ trên thang không gian Sobolev, cho tới tận biên. Một mô hình không làm mịn được dữ liệu thô, hoặc tự phát sinh dao động giả khi tăng độ mịn lưới, sẽ không hành xử đúng như toán tử nghịch đảo elliptic. Ưu điểm chính của PINO nằm ở chỗ phần dư vật lý đánh giá trên lưới mịn có thể khôi phục tính làm trơn này ngay cả khi dữ liệu huấn luyện ở độ phân giải thô.

### Phép kiểm tra theo nguyên lý cực đại và giá trị trung bình

Nếu $$f=0$$ và dữ liệu biên nằm trong đoạn $$[m,M]$$, một trường thế học được vượt ra ngoài $$[m,M]$$ là không đạt yêu cầu. Nếu miền là đĩa tròn và $$a\equiv 1$$, tính chất giá trị trung bình cho một kiểm chứng định lượng: giá trị tại tâm phải bằng trung bình tích phân trên biên. Các phép kiểm tra này không đòi hỏi phải có sẵn bộ giải đối chiếu.

### Hình học miền

Hình chữ nhật, đĩa tròn và miền ngoài có các hàm Green khác nhau. Geo-FNO (Li, Huang, Huang và Anandkumar, *J. Comput. Phys.* 2023) học một phép biến dạng đưa miền phức tạp về miền đều chuẩn hóa để vẫn áp dụng được toán tử dựa trên FFT. Đây là cách tiếp cận hiện đại tương ứng với kỹ thuật ánh xạ bảo giác và tọa độ cực trong chương.

## Phương pháp và kỹ thuật

1. Xác định họ hệ số hoặc nguồn cùng ánh xạ dữ liệu biên.
2. Sinh các cặp dữ liệu huấn luyện bằng bộ giải phần tử hữu hạn hoặc phương pháp phổ.
3. Huấn luyện FNO, DeepONet hoặc PINO; có thể bổ sung hàm mất mát theo phần dư phương trình trên lưới mịn hơn.
4. Kiểm chứng mô hình bằng phép kiểm tra cực đại/trung bình, bảo toàn thông lượng, và thử nghiệm trên hình học hoặc tỷ lệ tương phản hệ số mới.
5. Kiểm tra trực tiếp lát cắt hàm Green học được $$f\mapsto u(\cdot;f=\delta)$$ khi bài toán là tuyến tính.

PINN vẫn hữu ích khi cần giải trên một miền bất quy tắc đơn lẻ hoặc nhận dạng nguồn trong bài toán ngược, nhưng thường kém hiệu quả hơn mô hình học toán tử khi phải giải hàng trăm bài toán Poisson có cấu trúc tương tự.

## Ví dụ

### Ví dụ 1: Tái tạo hàm Green trên đĩa tròn

Trên đĩa đơn vị với điều kiện biên Dirichlet, nhân Poisson và hàm Green đều có biểu thức tường minh. Khi huấn luyện một mô hình toán tử tuyến tính trên các nguồn ngẫu nhiên rồi kiểm tra bằng hàm xấp xỉ delta, mô hình cần tái tạo được nhân điện tích ảnh. Sai lệch gần biên phản ánh trực tiếp mức độ mà mô hình nắm bắt được nguyên lý ảnh.

### Ví dụ 2: Bài toán Darcy có tương phản cao

Nếu độ thấm $$a$$ nhận hai giá trị chênh lệch nhau vài bậc độ lớn, trường thế sẽ hình thành gradient rất dốc dọc theo mặt phân cách. Một mô hình FNO chỉ được huấn luyện trên tương phản thấp thường làm nhòe các mặt phân cách này. Hạn chế đó phản ánh đúng tính chính quy elliptic: nghiệm nằm trong không gian hàm yếu hơn khi $$a$$ chỉ bị chặn và thỏa tính elliptic chứ không trơn.

### Ví dụ 3: Kiểm tra tính chất trung bình rời rạc

```python
import numpy as np

u = np.array([[0., 0., 0.],
              [0., 1., 0.],
              [0., 0., 0.]])
resid = 4 * u[1, 1] - u[1, 0] - u[1, 2] - u[0, 1] - u[2, 1]
print(resid)
```

Một trường thế rời rạc học được cho phương trình Laplace phải làm cho phần dư này nhỏ tại các điểm bên trong miền. Mẫu sai phân năm điểm chính là dạng rời rạc của tính chất giá trị trung bình trên lưới.

## Ứng dụng

Dòng chảy dưới mặt đất, thiết kế thiết bị tĩnh điện, dòng chảy thế không nén được và chụp cắt lớp trở kháng điện trong y khoa đều dẫn đến bài toán elliptic hoặc gần elliptic. Mô hình thay thế (surrogate) dựa trên học toán tử giúp chuyển các bản sao số (digital twin) phần tử hữu hạn thành ánh xạ tương tác nhanh từ độ thấm hoặc mật độ điện tích sang trường thế. Các bài toán elliptic ngược — khôi phục hệ số $$a$$ hoặc nguồn từ phép đo trên biên — thuộc lớp bài toán Calderón và các bài toán liên quan; trong giai đoạn 2022–2024, toán tử ngược nơ-ron và phương pháp lấy mẫu hậu nghiệm dựa trên score thường được lựa chọn, song vẫn chịu các giới hạn về tính nhận dạng mà lý thuyết thế đã chỉ ra.

Phần ứng dụng dòng chảy tùy chọn của chương (dòng không xoáy, không nén được) liên hệ trực tiếp với chủ đề này: hàm dòng hoặc thế vận tốc học được vẫn phải là hàm điều hòa, nên phần dư của toán tử Laplace chính là một hàm mất mát vật lý mang ý nghĩa cổ điển.

## Thách thức và hướng mở rộng

Tỷ lệ tương phản lớn, tính dị hướng và tính elliptic suy biến làm mất các ước lượng đều và gây khó khăn cho các mô hình chỉ huấn luyện trên họ bài toán nhẹ hơn. Các góc nhọn và điều kiện biên hỗn hợp tạo ra kỳ dị khiến cơ sở Fourier toàn cục dễ gặp hiện tượng dao động Gibbs. Bài toán ngược vẫn đặt không chỉnh nghiêm trọng; một ảnh tái tạo trông sắc nét từ mạng nơ-ron không phải là bằng chứng về tính duy nhất của nghiệm. Trong không gian ba chiều, các toán tử dựa trên FFT cũng gây áp lực lớn lên bộ nhớ GPU. Ngoài ra, khi ghép với phương trình vận chuyển hoặc hệ Stokes, bài toán không còn thuộc phạm vi elliptic thuần túy.

Nếu một trường thế học được thỏa mãn nguyên lý cực đại nhưng không đảm bảo tính liên tục của thông lượng qua mặt phân cách, đồng nhất thức biến phân nào đã bị vi phạm? Các đồng nhất thức Green trong chương cung cấp câu trả lời trực tiếp.

## Video tham khảo

- xem trước: [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu Fourier neural operator cho việc học ánh xạ nghiệm của các bài toán elliptic như nội dung bài này.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Giới thiệu DeepONet như một kiến trúc học toán tử nghiệm khác cho bài toán elliptic.
- [Physics Informed Neural Networks (PINNs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — Steve Brunton, tiếng Anh. Trình bày cách đưa phần dư vật lý của phương trình Poisson hoặc Laplace vào hàm mất mát để ràng buộc phương trình.

## Bài tập

1. **Phép kiểm tra giá trị trung bình.** Với một đa thức điều hòa trên đĩa tròn, viết đồng nhất thức giá trị trung bình và chuyển nó thành tiêu chí kiểm định cho mô hình học được.

2. **Tính tuyến tính của toán tử Green.** Nếu $$\mathcal{G}(f)$$ là toán tử giải bài toán Poisson Dirichlet, mô hình học được $$\mathcal{G}_\theta$$ cần thỏa mãn những đồng nhất thức nào? Thiết kế hai thí nghiệm: một để kiểm tra tính tuyến tính và một để kiểm tra tính bảo toàn dấu (tính dương).

3. **Tương phản hệ số và tính chính quy.** Chỉ dùng trực giác về phương trình elliptic, giải thích vì sao việc nhân đôi tỷ lệ tương phản của $$a$$ có thể làm gradient của $$u$$ gần mặt phân cách tăng hơn hai lần.

4. **Thí nghiệm tính toán.** Giải $$-u''=f$$ trên $$(0,1)$$ với $$u(0)=u(1)=0$$ cho nhiều hàm nguồn $$f$$ ngẫu nhiên, huấn luyện một ánh xạ tuyến tính trên các giá trị nút lưới, rồi so sánh ma trận học được với ma trận Green rời rạc.

5. **Khám phá mở.** Đọc các thí nghiệm dòng Darcy trong Li và cộng sự (ICLR 2021) hoặc Kovachki và cộng sự (2023), sau đó viết lại chú thích cho một hình minh họa bằng ngôn ngữ của chương này (nguyên lý cực đại, hàm Green, tính chính quy).

## Tài liệu

- Evans, Chương 2 và 6; Haberman, Chương 6–7.
- Li, Z., và cộng sự. “Fourier neural operator.” *ICLR* 2021. [arXiv:2010.08895](https://arxiv.org/abs/2010.08895).
- Kovachki, N., và cộng sự. “Neural operator.” *JMLR* 24, số 89 (2023).
- Wang, S., Wang, H., và Perdikaris, P. “Physics-informed DeepONets.” *Science Advances* 7, số 40 (2021).
- Li, Z., và cộng sự. “Physics-informed neural operator.” [arXiv:2111.03794](https://arxiv.org/abs/2111.03794).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
