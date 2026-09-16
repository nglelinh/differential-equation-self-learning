---
layout: post
title: "01-11 Ứng dụng hiện đại: Neural ODE và mạng độ sâu liên tục"
chapter: '01'
order: 11
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: optional
---

## Mục tiêu

Bài tùy chọn này cho thấy bài toán giá trị ban đầu cấp một của chương đã tái xuất, sau 2018 và đặc biệt trong tài liệu 2022–2026, như mô hình cho mạng nơ-ron độ sâu liên tục. Sinh viên cần viết được một neural ODE, giải thích vì sao tồn tại và duy nhất vẫn chi phối kiến trúc, liên hệ mạng residual với bước Euler, và định vị các thư viện chính. Lý thuyết cổ điển không bị viết lại.

## Kiến thức nền

Sinh viên cần biết phương trình tách biến và tuyến tính cấp một, thừa số tích phân, và định lý Picard–Lindelöf. Chỉ cần hình dung trường vector tham số hóa $$f(t,y;\theta)$$; không giả định nền tảng học máy chuyên sâu.

## Dẫn nhập

Phương trình cấp một $$y'=f(t,y)$$ là quy luật biến trạng thái hiện tại thành vận tốc tức thời. Mạng residual làm điều rất giống: mỗi lớp cập nhật trạng thái ẩn bằng một gia số học được. Chen, Rubanova, Bettencourt và Duvenaud làm chính xác phép loại suy ấy trong *Neural Ordinary Differential Equations* (NeurIPS 2018) khi thay chồng lớp rời rạc bằng ODE

$$
\frac{dh}{dt}=f_\theta\bigl(t,h(t)\bigr),\qquad h(t_0)=x,
$$

và tính gradient bằng phương pháp liên hợp. Tài liệu tiếp theo, được Kidger khảo sát năm 2022 ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)), xem residual net, neural ODE, neural CDE và neural SDE như một họ mô hình độ sâu liên tục.

Vì sao sinh viên phương trình cấp một phải quan tâm? Vì mọi sự kiện định tính đã chứng minh trong chương đều trở thành ràng buộc thiết kế. Nếu $$f_\theta$$ không Lipschitz, tính duy nhất có thể mất. Nếu $$f_\theta$$ stiff, bộ giải hiện sẽ phí bước. Nếu dữ liệu đến lúc không đều, quỹ đạo liên tục tự nhiên hơn lưới rời rạc cố định. Cùng lý thuyết tồn tại làm cho mô hình quần thể và pha trộn đáng tin nay quyết định liệu mạng độ sâu liên tục có phải ánh xạ đặt chỉnh từ đầu vào đến đầu ra hay không.

## Khái niệm then chốt

### Mạng residual như rời rạc hóa Euler

Khối residual $$h_{n+1}=h_n+\Delta t\,f_\theta(h_n)$$ là Euler tiến cho $$h'=f_\theta(h)$$. Lấy giới hạn liên tục không phải ẩn dụ: đó là cùng quá trình biến thương sai phân thành đạo hàm. Augmented neural ODE (Dupont, Doucet và Teh, NeurIPS 2019) thêm chiều để quỹ đạo có thể không cắt nhau, khôi phục khả năng biểu diễn mà một dòng cấp một thuần trên không gian gốc không có. Lý do đã thấy trên đường pha của phương trình tự trị vô hướng: các dòng một chiều không thể xuyên qua nhau.

### Phương pháp liên hợp

Huấn luyện cần $$\nabla_\theta\mathcal{L}$$ khi mất mát phụ thuộc trạng thái cuối $$h(T)$$. Lấy đạo hàm qua mọi bước bộ giải phải lưu cả quỹ đạo. Phương pháp liên hợp thay vào đó tích phân

$$
\frac{da}{dt}=-a^\top D_h f_\theta(t,h),\qquad a(T)=\nabla_{h(T)}\mathcal{L}
$$

ngược và tích lũy gradient tham số dọc quỹ đạo ngược. Đây là phương trình độ nhạy khi lấy đạo hàm IVP theo tham số, nay dùng ở quy mô mạng sâu. Kidger (2022) và tài liệu `torchdiffeq` ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) nhấn mạnh liên hợp chỉ chính xác bằng bộ giải thuận và ngược; dung sai không nhất quán sinh gradient không nhất quán.

### Neural CDE

Khi đầu vào vốn là một đường $$X(t)$$, như chuỗi thời gian không đều, Kidger, Morrill, Foster và Lyons (*Neural Controlled Differential Equations*, ICLR 2021) thay ODE bằng phương trình điều khiển

$$
dh(t)=f_\theta\bigl(h(t)\bigr)\,dX(t).
$$

Lý thuyết cấp một vẫn áp dụng sau khi viết lại hệ như phương trình thường bị dẫn bởi gia số của $$X$$. Ưu điểm là quan sát không cần nằm trên lưới đều — điều mà mô hình bồn pha trộn và đếm quần thể đã gợi ý: luật liên tục là chính, lưới lấy mẫu là phụ.

### Phần mềm 2022–2026

Hai thư viện chiếm lĩnh thực hành hiện nay. `torchdiffeq` cài bộ giải ODE thích nghi và liên hợp trong PyTorch. Diffrax (Kidger, 2021–2022; [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)) làm điều tương tự trong JAX, với giao diện thống nhất cho ODE, CDE và SDE. Cả hai đều xem bộ giải như một nguyên thủy khả vi, nên phương trình cấp một không còn chỉ là bài tập: nó là một lớp.

## Phương pháp và kỹ thuật

Quy trình thực hành là hậu duệ trực tiếp của pipeline IVP trong chương này.

1. Chọn kiến trúc trường vector $$f_\theta$$ (một MLP nhỏ là điển hình).
2. Chọn bộ giải có miền ổn định khớp bài toán: Runge–Kutta hiện cho động lực không stiff, ẩn hoặc bán ẩn khi trường học được bị stiff.
3. Tích phân từ đầu vào $$x$$ đến thời điểm $$T$$, hoặc đến từng thời điểm quan sát $$t_i$$.
4. Lập mất mát trên các trạng thái quan sát và lan truyền ngược, bằng unroll hoặc liên hợp.
5. Kiểm chứng không chỉ mất mát mà cả chẩn đoán cấp một: bị chặn, so sánh với trường tuyến tính hóa, và độ nhạy theo $$T$$.

Tách biến và thừa số tích phân vẫn hữu ích như phép kiểm. Nếu trường học được gần tuyến tính, $$h'=Ah+b$$, nghiệm đúng $$e^{At}$$ là chuẩn độc lập. Nếu trường tự trị và vô hướng, đường pha dự đoán các cân bằng mà mạng được phép có.

## Ví dụ

### Ví dụ 1: Độ sâu liên tục cho chuỗi thời gian không đều

Giả sử $$y(t_i)$$ đến tại $$0=t_0<t_1<\cdots<t_n$$ không cách đều. Mạng rời rạc phải bịa quy tắc khuyết. Neural ODE chỉ đánh giá cùng quỹ đạo tại các thời điểm cho sẵn. Đó đúng cách ta xử lý mô hình bồn pha trộn khi kỹ thuật viên lấy mẫu lúc tiện.

### Ví dụ 2: Mất Lipschitz như bệnh huấn luyện

Nếu $$f_\theta$$ dùng kích hoạt không bị chặn và trọng số lớn, hằng số Lipschitz địa phương có thể nổ. Bộ giải rồi bước rất nhỏ hoặc thất bại, và tính duy nhất trên khoảng huấn luyện trở nên đáng ngờ. Weight decay, chuẩn hóa phổ, hoặc lớp tanh cuối không chỉ là regularization; chúng là nỗ lực ở lại trong giả thiết Picard–Lindelöf.

### Ví dụ 3: Phác thảo `torchdiffeq` tối thiểu

```python
import torch
from torchdiffeq import odeint

class Field(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(2, 16), torch.nn.Tanh(), torch.nn.Linear(16, 2)
        )

    def forward(self, t, y):
        return self.net(y)

y0 = torch.tensor([1.0, 0.0])
t = torch.linspace(0.0, 2.0, 21)
with torch.no_grad():
    yt = odeint(Field(), y0, t)
print(yt.shape)  # (21, 2)
```

Đầu ra là mẫu rời rạc của một quỹ đạo cấp một liên tục. Thay `Field` bằng $$f(t,y)=-y$$ ta lấy lại phân rã mũ đã giải bằng tách biến.

## Ứng dụng

Mô hình độ sâu liên tục được dùng cho chuỗi thời gian y khoa không đều, động lực ẩn trong thần kinh học, kiến trúc residual trong thị giác máy, và closure vật lý–ML lai khi một luật cấp một đã biết được giữ và chỉ học số hạng còn thiếu. Trong điều khiển và dược động học chúng cho dạng không gian trạng thái tự nhiên: trạng thái ẩn là vector ngăn, trường vector một phần cơ chế và một phần học được. Trong mọi bối cảnh, lý thuyết tồn tại của chương là phép kiểm tỉnh táo đầu tiên.

Kidger (2022) và hệ SciML quanh Diffrax cùng `torchdiffeq` cũng đổi văn hóa phần mềm: bộ giải không còn giấu trong integrator hộp đen mà là lớp khả vi hạng nhất.

## Thách thức và hướng mở rộng

Neural ODE có thể huấn luyện chậm hơn residual net rời rạc, nhất là khi trường học được bị stiff. Liên hợp ngược có thể lệch gradient thật nếu dung sai lỏng. Khả năng biểu diễn trên không gian gốc bị giới hạn vì dòng khả nghịch và không cắt nhau; tăng cường chiều, ẩn phụ, hoặc phương trình điều khiển là thuốc thường dùng. Còn một cảnh báo triết học: khớp thành công không đồng nhất một trường vector duy nhất. Nhiều vế phải cấp một có thể chia sẻ cùng quỹ đạo lấy mẫu.

Câu hỏi mang theo: tính chất nào của $$f$$ (Lipschitz, Lipschitz một phía, đơn điệu) nên bị ràng buộc khi học nếu ta muốn cùng những định lý so sánh làm cho phương trình cấp một vô hướng trở nên trong suốt?

## Bài tập

1. **Từ khối residual đến ODE.** Viết $$h_{n+1}=h_n+h\,f(h_n)$$ và lấy $$h\to 0$$. Thu lại $$h'=f(h)$$ và nêu nghĩa chính xác của giới hạn trên một khoảng hữu hạn.

2. **Vòng lặp Picard như trực giác huấn luyện.** Với $$y'=\theta y$$, $$y(0)=1$$, viết hai vòng Picard đầu. Vòng lặp này khác bước gradient trên $$\theta$$ cho mất mát $$\lvert y(1)-e\rvert^2$$ như thế nào?

3. **Liên hợp cho ODE tuyến tính vô hướng.** Cho $$y'=\theta y$$, $$y(0)=1$$, và $$\mathcal{L}=\tfrac12 y(T)^2$$. Tính $$\partial\mathcal{L}/\partial\theta$$ bằng hai cách: đạo hàm dạng đóng, và giải phương trình liên hợp.

4. **Thí nghiệm tính toán.** Dùng `torchdiffeq` hoặc Diffrax, khớp neural ODE với mẫu của phương trình logistic $$y'=y(1-y)$$. So sánh trường học được dọc đường pha với vế phải tự trị đúng. Mạng có lấy lại cân bằng tại $$0$$ và $$1$$ không?

5. **Khám phá mở.** Đọc Mục 1 của Kidger (2022) và giải thích, trong một trang, vì sao chuỗi thời gian không đều làm mô hình cấp một liên tục tự nhiên hơn kiến trúc rời rạc cố định.

## Tài liệu

- Boyce và DiPrima, Chương 1–2; Zill, Chương 1–2.
- Chen, R. T. Q., và cộng sự. “Neural ordinary differential equations.” *NeurIPS* 2018. [arXiv:1806.07366](https://arxiv.org/abs/1806.07366).
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- Kidger, P., Morrill, J., Foster, J., và Lyons, T. “Neural controlled differential equations for irregular time series.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- `torchdiffeq`: [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq). Diffrax: [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
