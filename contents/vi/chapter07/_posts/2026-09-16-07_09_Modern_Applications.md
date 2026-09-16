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

Bài tùy chọn này đặt bài toán biên hai điểm, trị riêng Sturm–Liouville và hàm Green cạnh mạng vật lý-thông tin và bộ giải nơ-ron biến phân. Sinh viên cần viết được mất mát PINN cho BVP, giải thích vì sao bài trị riêng khó hơn bài nguồn tuyến tính, và dùng tài liệu chế độ thất bại 2021–2024 như chẩn đoán chứ không như lý do bỏ phương pháp. Lý thuyết Sturm–Liouville của chương không bị viết lại.

## Kiến thức nền

Sinh viên cần biết điều kiện biên hai điểm, dạng tự liên hợp Sturm–Liouville, khai triển hàm riêng, và ý niệm hàm Green như nghịch đảo của toán tử vi phân.

## Dẫn nhập

Bài toán biên đòi hỏi hàm thỏa phương trình vi phân và điều kiện tại hơn một điểm. Ràng buộc toàn cục ấy làm BVP khác IVP, và là lý do bộ giải nơ-ron ngây thơ thường thất bại: mạng có thể thỏa ODE trong miền trong vẫn trượt biên thứ hai, hoặc thỏa cả hai biên vẫn ngồi nhầm không gian riêng.

Raissi, Perdikaris và Karniadakis (2019) đặt khuôn PINN hiện đại. Krishnapriyan, Gholami, Zhe, Kirby và Mahoney (*Characterizing possible failure modes in physics-informed neural networks*, NeurIPS 2021) rồi cho thấy các BVP đối lưu, phản ứng và tần số cao đơn giản có thể làm PINN sụp. Wang, Yu và Perdikaris phân tích bệnh gradient và độ cứng trong mất mát PINN. Cuomo và cộng sự (*J. Sci. Comput.*, 2022) khảo sát phương pháp hình thành. Hao và cộng sự (*PINNacle*, NeurIPS 2024) biến những quan sát ấy thành benchmark công khai.

Một dòng biến phân song song, phương pháp Deep Ritz của E và Yu (2018) và các hậu duệ, cực tiểu hóa năng lượng chứ không phải phần dư mạnh và gần hơn với dạng yếu mà lý thuyết Sturm–Liouville đã dùng. Hàm Green nằm ở đầu kia: một khi toán tử đã đảo, học nghịch đảo như toán tử (DeepONet, neural operator) trở thành nhiệm vụ cấp BVP chứ không phải từng điểm.

## Khái niệm then chốt

### Mất mát PINN cho bài hai điểm

Với $$-u''=f$$ trên $$(0,1)$$, $$u(0)=u(1)=0$$, một mất mát chuẩn là

$$
\mathcal{L}(\theta)=\sum_i\bigl(u_\theta''(x_i)+f(x_i)\bigr)^2+\lambda\bigl(u_\theta(0)^2+u_\theta(1)^2\bigr).
$$

Trọng số $$\lambda$$ không do phương trình cho. Quá nhỏ thì mạng bỏ biên; quá lớn thì phần dư bị thiếu huấn luyện. Đánh đổi ấy là ảnh tính toán của sự thật rằng BVP là phương trình toán tử cộng ràng buộc không gian con, không phải IVP cộng phạt.

### Trị riêng như ẩn chung

Bài trị riêng Sturm–Liouville đòi cặp $$(\lambda,u)$$. PINN phải học cả hai, thường với chuẩn hóa $$\|u\|_{L^2}=1$$ và phạt trực giao với các hàm riêng đã tìm. Không ràng buộc ấy mạng trôi về nghiệm tầm thường hoặc hỗn hợp mode. Định lý các hàm riêng trực giao của chương chính là regularization.

### Hàm Green và học toán tử

Nghiệm $$u(x)=\int G(x,s)f(s)\,ds$$ đã là một toán tử. Học $$G$$, hoặc học trực tiếp ánh xạ $$f\mapsto u$$, thường tái sử dụng được hơn học một $$u$$. Physics-informed DeepONet (Wang, Wang và Perdikaris, *Science Advances*, 2021) và lý thuyết neural operator của Kovachki và cộng sự (2023) đi đường ấy. Với toán tử tự liên hợp âm, nhân học được phải ra gần đối xứng — phép kiểm cụ thể sinh viên có thể làm.

### Các chế độ thất bại mà lý thuyết dự đoán

Số Péclet cao, lớp mỏng, và dao động hàm riêng sắc tạo cùng thiên kiến phổ đã gặp ở chương chuỗi. Nhân quả ít là vấn đề hơn với BVP elliptic so với tiến hóa, nhưng analogue gần nhất là nguyên lý cực đại: mạng chìm dưới giá trị biên trên khoảng không nguồn đang phá định lý, không chỉ một số hạng mất mát. PINNacle (2024) ghi nhận các sửa phổ biến (trọng số thích nghi, phân rã miền, tái lấy mẫu theo phần dư) giúp thường xuyên thế nào, và không giúp thường xuyên thế nào.

## Phương pháp và kỹ thuật

1. Viết dạng mạnh, toán tử biên, và nếu có, dạng năng lượng.
2. Chọn biểu diễn: mạng thô, mạng ép cứng biên bằng nhân $$x(1-x)$$, hoặc trunk phổ các hàm riêng.
3. Huấn luyện với phần dư và biên (hoặc năng lượng); thích nghi trọng số nếu gradient một số hạng át.
4. Với trị riêng, thêm chuẩn hóa và deflation.
5. Kiểm chứng bằng công cụ của chương: tích phân trực giao, đồng nhất thức Green, đếm nút của hàm riêng.

Ép cứng dữ liệu Dirichlet là cải tiến sơ cấp hiệu quả nhất. Đó là analogue nơ-ron của việc chọn không gian hàm đã nằm trong $$H^1_0$$.

## Ví dụ

### Ví dụ 1: Mã hóa biên cứng

Ansatz $$u_\theta(x)=x(1-x)n_\theta(x)$$ giải $$u(0)=u(1)=0$$ đúng. Mất mát rồi chỉ còn phần dư vi phân. Đây là thay đổi một dòng thường thắng phạt biên lớn.

### Ví dụ 2: Hàm riêng đầu của $$-u''=\lambda u$$

Cặp đúng là $$\lambda=\pi^2$$, $$u=\sqrt{2}\sin(\pi x)$$ trên $$(0,1)$$. PINN báo $$\lambda\approx 9.87$$ nhưng hàm riêng có hai không nội tại đã nhảy sang mode cao hơn. Đếm không là định lý dao động Sturm dùng như unit test.

### Ví dụ 3: Lắp phần dư

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

Phần dư in ra chưa phải nghiệm, nhưng cấu trúc đã tôn trọng điều kiện hai điểm.

## Ứng dụng

Bộ giải BVP nơ-ron được dùng cho đàn hồi tham số, dòng nước ngầm, và Helmholtz khi nhiều vế phải hoặc nhiều hệ số phải đảo. PINN trị riêng xuất hiện trong nhận dạng kết cấu dao động và tìm trạng thái cơ lượng tử. Trong cả hai bối cảnh, đối tượng tái sử dụng thường là toán tử nghịch đảo, không phải một ảnh chụp — vì thế hàm Green và học toán tử thuộc cùng cuộc trò chuyện.

Niềm tin kỹ thuật vẫn chạy qua các phép thử cổ điển. Mode shape học được không trực giao với mode thấp hơn, hoặc độ võng học được phá nguyên lý cực đại, phải bị loại trước khi vào vòng thiết kế.

## Thách thức và hướng mở rộng

PINN vẫn nhạy với trọng số mất mát, lấy mẫu và kiến trúc. Helmholtz tần số cao và lớp đối lưu mạnh vẫn khó trong benchmark 2024. Phương pháp biến phân cần đúng không gian hàm và quadrature không giấu lớp biên. Nghịch đảo học toán tử cần họ huấn luyện phủ các nguồn liên quan; chúng không tạo hàm Green miễn phí. Điều kiện biên hỗn hợp và bài truyền cần phần dư giao diện mà câu chuyện hai điểm cơ bản không chứa.

Câu hỏi phản tư: nếu phần dư PINN nhỏ nhưng đồng nhất thức Green rời rạc thất bại, lỗi nào quan trọng hơn? Chương gợi ý đồng nhất thức, vì nó mã hóa tính tự liên hợp và bảo toàn.

## Bài tập

1. **Không gian hàm trước.** Giải thích vì sao ansatz $$u=x(1-x)n(x)$$ mã hóa cứng Dirichlet nhưng không phải Neumann. Đề xuất ansatz cho $$u'(0)=u'(1)=0$$.

2. **Deflation.** Viết số hạng mất mát phạt chồng lấn của hàm riêng mới với $$\sin(\pi x)$$ và $$\sin(2\pi x)$$. Vì sao $$L^2$$ là tích trong tự nhiên?

3. **Kiểm Green.** Với $$-u''=f$$, $$u(0)=u(1)=0$$, nhân là $$G(x,s)=\min(x,s)-xs$$. Làm sao thử liệu toán tử học được $$\mathcal{G}(f)$$ có gần toán tử tích phân này?

4. **Thí nghiệm tính toán.** Huấn luyện PINN mã hóa cứng ở trên với $$f\equiv 1$$ và so $$u_\theta$$ với $$u(x)=\tfrac12 x(1-x)$$ đúng. Rồi tăng tần số lên $$f=\sin(8\pi x)$$ và ghi điều xảy ra với lỗi.

5. **Khám phá mở.** Đọc Krishnapriyan và cộng sự (NeurIPS 2021) hoặc bài PINNacle (2024) và liệt kê ba đặc trưng BVP làm hỏng PINN vanilla một cách hệ thống. Với mỗi đặc trưng, nêu định lý hoặc cấu trúc của chương đã dự đoán khó khăn.

## Tài liệu

- Boyce và DiPrima, Chương 10–11; Haberman, Chương 5.
- Krishnapriyan, A. S., và cộng sự. “Characterizing possible failure modes in physics-informed neural networks.” *NeurIPS* 2021. [arXiv:2109.01050](https://arxiv.org/abs/2109.01050).
- Cuomo, S., và cộng sự. “Scientific machine learning through physics-informed neural networks.” *J. Sci. Comput.* 92 (2022).
- Hao, Z., và cộng sự. “PINNacle.” *NeurIPS* 2024. [arXiv:2306.08827](https://arxiv.org/abs/2306.08827).
- Wang, S., Wang, H., và Perdikaris, P. “Learning the solution operator of parametric PDEs with physics-informed DeepONets.” *Science Advances* 7, số 40 (2021).
