---
layout: post
title: "07-09 Ứng dụng hiện đại: PINN cho bài toán biên"
chapter: '07'
order: 9
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: optional
---

## Mục tiêu

Bài học tùy chọn này đặt bài toán giá trị biên hai điểm, bài toán trị riêng Sturm–Liouville và hàm Green cạnh mạng nơ-ron tích hợp vật lý (PINN) cùng các bộ giải nơ-ron biến phân. Sinh viên cần viết được hàm mất mát PINN cho bài toán giá trị biên (BVP), giải thích vì sao bài toán trị riêng khó hơn bài toán nguồn tuyến tính và biết sử dụng các kết quả nghiên cứu giai đoạn 2021–2024 về chế độ thất bại làm công cụ chẩn đoán. Lý thuyết Sturm–Liouville cổ điển của chương vẫn là chuẩn mực kiểm chứng.

## Kiến thức nền

Sinh viên cần nắm điều kiện biên hai điểm, dạng tự liên hợp Sturm–Liouville, khai triển theo hàm riêng và ý nghĩa của hàm Green như toán tử nghịch đảo của toán tử vi phân.

## Dẫn nhập

Bài toán giá trị biên đòi hỏi nghiệm phải đồng thời thỏa phương trình vi phân bên trong miền và các điều kiện ràng buộc tại hơn một điểm biên. Tính toàn cục này làm BVP khác căn bản so với bài toán giá trị đầu (IVP) và giải thích vì sao bộ giải nơ-ron đơn giản dễ thất bại: mạng có thể thỏa tốt phương trình vi phân bên trong miền nhưng sai lệch ở biên thứ hai, hoặc thỏa cả hai biên nhưng rơi vào nhầm không gian riêng.

Raissi, Perdikaris và Karniadakis (2019) đã đặt nền móng cho khuôn khổ PINN hiện đại. Sau đó, Krishnapriyan, Gholami, Zhe, Kirby và Mahoney (*Characterizing possible failure modes in physics-informed neural networks*, NeurIPS 2021) chỉ ra rằng ngay cả các BVP đối lưu, phản ứng và tần số cao đơn giản cũng có thể khiến PINN thất bại. Wang, Yu và Perdikaris phân tích hiện tượng bất ổn gradient và tính cứng (stiffness) trong hàm mất mát của PINN. Cuomo và cộng sự (*J. Sci. Comput.*, 2022) khảo sát sự phát triển của phương pháp, còn Hao và cộng sự (*PINNacle*, NeurIPS 2024) hệ thống hóa các quan sát này thành một bộ kiểm chuẩn công khai.

Song song với đó, nhánh biến phân — tiêu biểu là phương pháp Deep Ritz của E và Yu (2018) cùng các mở rộng sau này — cực tiểu hóa phiếm hàm năng lượng thay vì phần dư dạng mạnh, gần gũi hơn với dạng yếu trong lý thuyết Sturm–Liouville. Ở chiều ngược lại, quan điểm hàm Green cho thấy khi toán tử đã khả nghịch, việc học trực tiếp toán tử nghịch đảo (DeepONet, toán tử nơ-ron) sẽ giải quyết bài toán ở cấp độ toàn bộ lớp BVP thay vì từng nghiệm đơn lẻ.

## Khái niệm then chốt

### Hàm mất mát PINN cho bài toán hai điểm

Với bài toán $$-u''=f$$ trên $$(0,1)$$, $$u(0)=u(1)=0$$, hàm mất mát PINN tiêu chuẩn có dạng

$$
\mathcal{L}(\theta)=\sum_i\bigl(u_\theta''(x_i)+f(x_i)\bigr)^2+\lambda\bigl(u_\theta(0)^2+u_\theta(1)^2\bigr).
$$

Trọng số $$\lambda$$ không được phương trình quy định sẵn. Nếu $$\lambda$$ quá nhỏ, mạng không thỏa điều kiện biên; nếu $$\lambda$$ quá lớn, phần dư vi phân bị huấn luyện kém. Sự đánh đổi này phản ánh về mặt tính toán một thực tế toán học: BVP là phương trình toán tử trên một không gian con thỏa điều kiện biên, chứ không phải một IVP cộng thêm số hạng phạt.

### Trị riêng như ẩn số đồng thời

Bài toán trị riêng Sturm–Liouville yêu cầu tìm đồng thời cả cặp $$(\lambda,u)$$. PINN phải học cả hai đại lượng này, thường kèm theo điều kiện chuẩn hóa $$\|u\|_{L^2}=1$$ và số hạng phạt trực giao với các hàm riêng đã tìm trước đó. Nếu thiếu các ràng buộc này, mạng dễ suy biến về nghiệm tầm thường hoặc hội tụ về tổ hợp trộn lẫn nhiều chế độ. Định lý về tính trực giao của các hàm riêng trong chương chính là cơ sở điều chuẩn (regularization) cho bài toán học.

### Hàm Green và học toán tử

Biểu diễn nghiệm $$u(x)=\int G(x,s)f(s)\,ds$$ bản thân nó là một toán tử tích phân. Việc học hạt nhân $$G$$, hoặc học trực tiếp ánh xạ $$f\mapsto u$$, thường có khả năng tái sử dụng cao hơn việc chỉ huấn luyện cho một nghiệm $$u$$ cố định. Physics-informed DeepONet (Wang, Wang và Perdikaris, *Science Advances*, 2021) và lý thuyết toán tử nơ-ron của Kovachki và cộng sự (2023) phát triển theo hướng này. Với toán tử tự liên hợp, hạt nhân Green học được phải gần đối xứng — đây là một phép kiểm chứng trực tiếp mà sinh viên có thể thực hiện.

### Các chế độ thất bại mà lý thuyết cổ điển đã dự báo

Số Péclet cao, lớp biên mỏng và các hàm riêng dao động nhanh đều tạo ra hiện tượng thiên kiến phổ tương tự chương chuỗi. Với BVP elliptic, tính nhân quả theo thời gian không đặt ra như ở bài toán tiến hóa, nhưng nguyên lý tương đương gần nhất là nguyên lý cực đại: một nghiệm nơ-ron nhận giá trị nhỏ hơn giá trị biên trên miền không có nguồn là đang vi phạm định lý toán học, chứ không đơn thuần là sai số tối ưu nhỏ. Bộ kiểm chuẩn PINNacle (2024) ghi nhận mức độ hiệu quả lẫn giới hạn của các kỹ thuật khắc phục phổ biến như trọng số thích nghi, phân rã miền và tái lấy mẫu theo phần dư.

## Phương pháp và kỹ thuật

1. Xác định dạng mạnh, toán tử biên và dạng phiếm hàm năng lượng (nếu có).
2. Chọn biểu diễn nghiệm: mạng thông thường, mạng ép cứng điều kiện biên bằng nhân tử như $$x(1-x)$$, hoặc cơ sở thân phổ gồm các hàm riêng.
3. Huấn luyện theo phần dư vi phân và điều kiện biên (hoặc phiếm hàm năng lượng); điều chỉnh trọng số thích nghi nếu gradient của một thành phần lấn át thành phần còn lại.
4. Với bài toán trị riêng, bổ sung ràng buộc chuẩn hóa và cơ chế loại trừ chế độ đã tìm (deflation).
5. Kiểm chứng kết quả bằng công cụ của chương: tích phân trực giao, đồng nhất thức Green và đếm số không điểm của hàm riêng.

Ép cứng điều kiện biên Dirichlet là cải tiến cơ bản mang lại hiệu quả rõ rệt nhất, tương ứng về mặt mạng nơ-ron với việc chọn trực tiếp không gian hàm nằm sẵn trong $$H^1_0$$.

## Ví dụ

### Ví dụ 1: Ép cứng điều kiện biên

Dạng nghiệm thử $$u_\theta(x)=x(1-x)n_\theta(x)$$ tự động thỏa chính xác $$u(0)=u(1)=0$$. Khi đó hàm mất mát chỉ còn lại phần dư của phương trình vi phân — một thay đổi một dòng nhưng thường hiệu quả hơn việc dùng hệ số phạt biên lớn.

### Ví dụ 2: Hàm riêng đầu tiên của $$-u''=\lambda u$$

Cặp nghiệm chính xác là $$\lambda=\pi^2$$ và $$u=\sqrt{2}\sin(\pi x)$$ trên $$(0,1)$$. Nếu một PINN báo $$\lambda\approx 9.87$$ nhưng hàm riêng thu được có hai không điểm bên trong miền thì mạng đã nhảy sang chế độ bậc cao hơn. Việc đếm số không điểm chính là định lý dao động Sturm được vận dụng như một phép kiểm thử đơn vị (unit test).

### Ví dụ 3: Tính phần dư bằng mã nguồn

```python
import torch

def u_hat(x, net):
    return x * (1 - x) * net(x)

x = torch.linspace(0, 1, 64, requires_grad=True).view(-1, 1)
net = torch.nn.Sequential(torch.nn.Linear(1, 32), torch.nn.Tanh(), torch.nn.Linear(32, 1))
u = u_hat(x, net)
du = torch.autograd.grad(u.sum(), x, create_graph=True)[0]
d2u = torch.autograd.grad(du.sum(), x, create_graph=True)[0]
f = torch.ones_like(x)
loss = ((-d2u - f)**2).mean()
print(float(loss))
```

Giá trị phần dư in ra chưa phải nghiệm đã huấn luyện, nhưng kiến trúc mạng đã bảo đảm thỏa mãn chính xác điều kiện biên hai điểm.

## Ứng dụng

Các bộ giải BVP nơ-ron được ứng dụng trong bài toán đàn hồi có tham số, dòng chảy nước ngầm và phương trình Helmholtz khi cần giải lặp lại cho nhiều vế phải hoặc nhiều cấu hình hệ số khác nhau. PINN cho bài toán trị riêng xuất hiện trong nhận dạng dao động kết cấu và tính toán trạng thái cơ học lượng tử. Trong cả hai bối cảnh, đối tượng có giá trị tái sử dụng cao là toán tử nghịch đảo chứ không phải một nghiệm đơn lẻ — đó là lý do hàm Green và học toán tử gắn kết chặt chẽ với nhau.

Độ tin cậy kỹ thuật vẫn dựa trên các tiêu chuẩn kiểm chứng cổ điển: một dạng chế độ (mode shape) học được không trực giao với các chế độ bậc thấp hơn, hoặc một trường độ võng vi phạm nguyên lý cực đại, cần bị loại bỏ trước khi đưa vào thiết kế.

## Thách thức và hướng mở rộng

PINN vẫn nhạy với cách chọn trọng số hàm mất mát, chiến lược lấy mẫu và kiến trúc mạng. Phương trình Helmholtz tần số cao và các bài toán có lớp biên đối lưu mạnh vẫn là thách thức lớn trong các bộ kiểm chuẩn năm 2024. Phương pháp biến phân đòi hỏi không gian hàm phù hợp và phép cầu phương số đủ mịn để không bỏ sót lớp biên. Các mô hình học toán tử nghịch đảo cần tập dữ liệu huấn luyện bao phủ đầy đủ lớp hàm nguồn quan tâm chứ không tự động khôi phục được hàm Green ngoài miền huấn luyện. Ngoài ra, điều kiện biên hỗn hợp và bài toán truyền qua giao diện đòi hỏi các số hạng phần dư tại giao diện mà mô hình hai điểm cơ bản chưa đề cập.

Câu hỏi phản tư: nếu một PINN có phần dư vi phân nhỏ nhưng vi phạm đồng nhất thức Green rời rạc, sai số nào đáng lo ngại hơn? Lý thuyết của chương gợi ý ưu tiên kiểm tra đồng nhất thức Green, vì nó phản ánh trực tiếp tính tự liên hợp và các định luật bảo toàn của toán tử.

## Video tham khảo

- Xem trước: [Physics Informed Neural Networks (PINNs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=-zrY7P2dVC4) — Steve Brunton, tiếng Anh. Giới thiệu mạng nơ-ron tích hợp vật lý áp đặt phần dư phương trình vi phân và điều kiện biên.
- [Sturm-Liouville Theory - Partial Differential Equations | Lecture 23](https://www.youtube.com/watch?v=q6R734ukoCo) — Jason Bramburger, tiếng Anh. Nền tảng lý thuyết Sturm–Liouville cổ điển mà các mô hình học cần tuân thủ.
- [Deep Operator Networks (DeepONet) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=CDCyOHXDRcI) — Steve Brunton, tiếng Anh. Giới thiệu mạng học toán tử như một hướng tiếp cận khác cho ánh xạ nghiệm của bài toán giá trị biên.

## Bài tập

1. **Ràng buộc không gian hàm từ trước.** Giải thích vì sao dạng thử $$u=x(1-x)n(x)$$ ép cứng điều kiện biên Dirichlet nhưng không ép điều kiện Neumann. Hãy đề xuất một dạng thử phù hợp cho điều kiện $$u'(0)=u'(1)=0$$.

2. **Loại trừ chế độ (Deflation).** Viết số hạng hàm mất mát phạt sự chồng lấn của hàm riêng mới với $$\sin(\pi x)$$ và $$\sin(2\pi x)$$. Giải thích vì sao tích trong $$L^2$$ là lựa chọn tự nhiên.

3. **Kiểm chứng hàm Green.** Với bài toán $$-u''=f$$, $$u(0)=u(1)=0$$, hàm Green là $$G(x,s)=\min(x,s)-xs$$. Hãy đề xuất cách kiểm tra xem một toán tử học được $$\mathcal{G}(f)$$ có xấp xỉ tốt toán tử tích phân này hay không.

4. **Thí nghiệm tính toán.** Huấn luyện PINN ép cứng điều kiện biên ở trên với $$f\equiv 1$$ và so sánh $$u_\theta$$ với nghiệm chính xác $$u(x)=\tfrac12 x(1-x)$$. Sau đó tăng tần số nguồn lên $$f=\sin(8\pi x)$$ và ghi nhận sự thay đổi của sai số.

5. **Khám phá mở.** Đọc bài báo của Krishnapriyan và cộng sự (NeurIPS 2021) hoặc PINNacle (2024), liệt kê ba đặc trưng của BVP thường gây thất bại cho PINN cơ bản, và chỉ ra định lý hoặc cấu trúc nào trong chương đã dự báo trước những khó khăn đó.

## Tài liệu

- Boyce và DiPrima, Chương 10–11; Haberman, Chương 5.
- Krishnapriyan, A. S., và cộng sự. “Characterizing possible failure modes in physics-informed neural networks.” *NeurIPS* 2021. [arXiv:2109.01050](https://arxiv.org/abs/2109.01050).
- Cuomo, S., và cộng sự. “Scientific machine learning through physics-informed neural networks.” *J. Sci. Comput.* 92 (2022).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Wang, S., Wang, H., và Perdikaris, P. “Learning the solution operator of parametric PDEs with physics-informed DeepONets.” *Science Advances* 7, số 40 (2021).
