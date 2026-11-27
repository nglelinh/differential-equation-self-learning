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


Năm 2018, một bài báo đạt giải Best Paper tại NeurIPS đã làm chấn động cộng đồng AI khi phát hiện ra rằng mạng nơ-ron sâu ResNet thực chất chỉ là **phương pháp Euler rời rạc** của một phương trình vi phân cấp một! Từ khoảnh khắc đó, **Neural ODE** và **Flow Matching** ra đời—biến chiều sâu rời rạc của mạng nơ-ron thành thời gian liên tục $t \in [0, T]$ và mở khóa các mô hình sinh ảnh, video hàng đầu hiện nay.

## Kiến thức cần nhớ: Bốn trụ cột của Neural ODE & Mạng độ sâu liên tục

![Phương trình Vi phân Bậc 1 & Neural ODEs (Chen et al.)]({{ site.imgurl }}/chapter_img/modern_apps/ma_01_neural_odes.svg)

1. **ResNet là bước Euler của PTVP cấp một**:
   Công thức cập nhật lớp $\mathbf{h}_{k+1} = \mathbf{h}_k + \Delta t\, f_\theta(\mathbf{h}_k, t_k)$ khi cho $\Delta t \to 0$ hội tụ trực tiếp về $\frac{d\mathbf{h}}{dt} = f_\theta(\mathbf{h}(t), t)$.
2. **Phương pháp Liên hợp (Adjoint Sensitivity Method)**:
   Thay vì lưu hàng nghìn bước trung gian trong bộ nhớ GPU để lan truyền ngược, ta giải ngược một PTVP liên hợp $\frac{d\mathbf{a}}{dt} = -\mathbf{a}^\top \frac{\partial f_\theta}{\partial \mathbf{h}}$ với chi phí bộ nhớ $O(1)$!
3. **Tính bất khả giao của quỹ đạo & Biểu diễn đồng phôi (Diffeomorphism)**:
   Theo định lý Picard–Lindelöf, quỹ đạo của Neural ODE không thể cắt nhau, giúp mô hình hóa các phép biến đổi mật độ xác suất khả nghịch (Continuous Normalizing Flows).
4. **Flow Matching & Mô hình sinh hiện đại (2023–2026)**:
   Thay vì mô phỏng ngẫu nhiên đắt đỏ, học trực tiếp trường vận tốc $v_\theta(\mathbf{x}, t)$ đưa phân phối nhiễu Gaussian về phân phối ảnh/dữ liệu theo đường thẳng mượt mà.

## Mục tiêu

Bài học tùy chọn này trình bày cách bài toán giá trị đầu cấp một của Chương 01 được ứng dụng từ sau năm 2018—và đặc biệt trong giai đoạn 2022–2026—như nền tảng cho các mạng nơ-ron độ sâu liên tục (continuous-depth neural networks). Sau bài học, sinh viên có thể viết phương trình của một neural ODE, giải thích vì sao định lý tồn tại và duy nhất vẫn chi phối thiết kế kiến trúc, liên hệ mạng dư (residual network) với sơ đồ Euler và nhận diện các thư viện tính toán phổ biến.

## Kiến thức nền

Sinh viên cần nắm phương trình tách biến, phương trình tuyến tính cấp một, nhân tử tích phân và định lý Picard–Lindelöf. Chỉ cần hiểu trường vector tham số hóa $$f(t,y;\theta)$$; bài học không yêu cầu nền tảng học máy chuyên sâu.

## Dẫn nhập

Phương trình vi phân cấp một $$y'=f(t,y)$$ quy định vận tốc tức thời theo trạng thái hiện tại. Mạng dư (residual network) hoạt động theo cơ chế tương tự: mỗi tầng cập nhật trạng thái ẩn bằng một lượng gia số học từ dữ liệu. Chen, Rubanova, Bettencourt và Duvenaud đã chính thức hóa mối liên hệ này trong bài báo *Neural Ordinary Differential Equations* (NeurIPS 2018) bằng cách thay chuỗi tầng rời rạc bằng hệ ODE

$$
\frac{dh}{dt}=f_\theta\bigl(t,h(t)\bigr),\qquad h(t_0)=x,
$$

và tính gradient theo tham số bằng phương pháp liên hợp (adjoint method). Các nghiên cứu tiếp theo, được Kidger tổng hợp năm 2022 ([arXiv:2202.02435](https://arxiv.org/abs/2202.02435)), đặt mạng dư, neural ODE, neural CDE và neural SDE trong cùng một họ mô hình độ sâu liên tục.

Với người học ODE cấp một, điểm đáng chú ý là mọi kết quả định tính đã học trong chương đều trở thành ràng buộc thiết kế thực tế: nếu $$f_\theta$$ không thỏa điều kiện Lipschitz, tính duy nhất có thể bị phá vỡ; nếu $$f_\theta$$ cứng (stiff), bộ giải hiện sẽ phải dùng bước cực nhỏ; còn khi dữ liệu quan sát đến tại các mốc thời gian không đều, mô hình quỹ đạo liên tục tự nhiên hơn nhiều so với mạng lưới rời rạc cố định. Chính lý thuyết tồn tại–duy nhất dùng cho mô hình dân số và bể trộn nay quyết định việc mạng độ sâu liên tục có xác định một ánh xạ đặt chỉnh từ đầu vào sang đầu ra hay không.

### Giải thích: So sánh 1 bước ResNet (Euler) với nghiệm liên tục của Neural ODE tuyến tính $h'(t) = -\frac{1}{2}h(t),\; h(0) = 1$ trên $[0, 1]$

1. **Nghiệm liên tục chính xác tại $t = 1$**:
   $$h(1) = e^{-0{,}5} \approx \mathbf{0{,}60653}.$$
2. **Xấp xỉ kiểu ResNet 2 lớp ($\Delta t = 0{,}5$, phương pháp Euler)**:
   - Lớp 1 ($t = 0{,}5$): $h_1 = h_0 + 0{,}5(-0{,}5 h_0) = 1 - 0{,}25 = \mathbf{0{,}75}$.
   - Lớp 2 ($t = 1{,}0$): $h_2 = 0{,}75 + 0{,}5(-0{,}5 \cdot 0{,}75) = 0{,}75 - 0{,}1875 = \mathbf{0{,}5625}$ (sai số $0{,}044$).
3. **Xấp xỉ kiểu ResNet 4 lớp ($\Delta t = 0{,}25$)**:
   $h_4 = (1 - 0{,}125)^4 = (0{,}875)^4 \approx \mathbf{0{,}58618}$ (sai số giảm một nửa còn $0{,}020$).
4. **Định lý giới hạn**: Với $N$ lớp độ sâu, $(1 - \frac{0{,}5}{N})^N \to e^{-0{,}5}$ khi $N \to \infty$—Neural ODE dùng bộ giải thích nghi (như RK45) đạt sai số $10^{-6}$ mà không cần cố định số lớp!

## Khái niệm then chốt

### Mạng dư như phép rời rạc hóa Euler

Một khối mạng dư $$h_{n+1}=h_n+\Delta t\,f_\theta(h_n)$$ chính là sơ đồ Euler hiện cho phương trình $$h'=f_\theta(h)$$. Lấy giới hạn liên tục khi $$\Delta t \to 0$$ hoàn toàn tương tự bước chuyển từ thương sai phân sang đạo hàm. Mô hình Augmented Neural ODE (Dupont, Doucet và Teh, NeurIPS 2019) bổ sung thêm chiều cho không gian trạng thái để các quỹ đạo có thể tránh cắt nhau, qua đó mở rộng khả năng biểu diễn so với dòng cấp một thuần trên không gian gốc—đúng như tính chất không cắt nhau của các quỹ đạo nghiệm đã thấy trên đường pha của phương trình tự trị một chiều.

### Phương pháp liên hợp (adjoint method)

Quá trình huấn luyện cần tính gradient $$\nabla_\theta\mathcal{L}$$ khi hàm mất mát phụ thuộc vào trạng thái cuối $$h(T)$$. Nếu lan truyền ngược trực tiếp qua mọi bước của bộ giải số, ta phải lưu toàn bộ quỹ đạo trong bộ nhớ. Thay vào đó, phương pháp liên hợp giải ngược thời gian phương trình độ nhạy

$$
\frac{da}{dt}=-a^\top D_h f_\theta(t,h),\qquad a(T)=\nabla_{h(T)}\mathcal{L}
$$

và tích lũy gradient theo tham số dọc theo quỹ đạo ngược. Đây chính là phương trình độ nhạy khi lấy đạo hàm nghiệm của bài toán giá trị đầu theo tham số, áp dụng ở quy mô mạng nơ-ron. Kidger (2022) cùng tài liệu `torchdiffeq` ([https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq)) lưu ý rằng độ chính xác của phương pháp liên hợp phụ thuộc chặt vào sai số tích phân thuận và ngược; nếu đặt dung sai quá lỏng, gradient thu được có thể sai lệch.

### Neural CDE

Khi dữ liệu đầu vào là một chuỗi thời gian liên tục hoặc lấy mẫu không đều $$X(t)$$, Kidger, Morrill, Foster và Lyons (*Neural Controlled Differential Equations*, ICLR 2021) thay ODE bằng phương trình vi phân điều khiển:

$$
dh(t)=f_\theta\bigl(h(t)\bigr)\,dX(t).
$$

Sau khi nội suy đường dẫn $$X(t)$$, phương trình có thể viết lại thành một hệ ODE dẫn động bởi đạo hàm của $$X$$. Ưu điểm là các điểm quan sát không cần cách đều nhau—tương tự mô hình bể pha trộn hay quần thể trong thực tế, nơi quy luật tiến hóa là liên tục còn lịch lấy mẫu chỉ là rời rạc.

### Hệ sinh thái phần mềm giai đoạn 2022–2026

Hai thư viện tiêu biểu trong thực hành hiện nay là `torchdiffeq` (cài đặt các bộ giải ODE bước thích nghi và phương pháp liên hợp trên PyTorch) và Diffrax (Kidger, 2021–2022; [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/)), cung cấp giao diện thống nhất cho ODE, CDE và SDE trên JAX. Cả hai đều xem bộ giải vi phân như một thành phần cơ sở khả vi (differentiable primitive), biến phương trình vi phân cấp một thành một tầng mạng hoàn chỉnh.

## Phương pháp và kỹ thuật

Quy trình xây dựng một neural ODE kế thừa trực tiếp quy trình bài toán giá trị đầu trong Chương 01:

1. Chọn kiến trúc cho trường vector $$f_\theta$$ (thường là một mạng MLP nhỏ).
2. Chọn bộ giải có miền ổn định phù hợp: Runge–Kutta hiện cho hệ không cứng, hoặc bộ giải ẩn/bán ẩn khi trường học được có tính cứng (stiff).
3. Tích phân từ trạng thái đầu $$x$$ đến thời điểm cuối $$T$$ hoặc tại danh sách các mốc quan sát $$t_i$$.
4. Tính hàm mất mát trên các trạng thái quan sát và lan truyền ngược gradient bằng cách trải bước bộ giải (discretize-then-optimize) hoặc bằng phương pháp liên hợp (optimize-then-discretize).
5. Kiểm tra chẩn đoán động lực học bên cạnh hàm mất mát: tính bị chặn của quỹ đạo, hành vi tuyến tính hóa cục bộ và độ nhạy theo thời đoạn $$T$$.

Các kỹ thuật cổ điển như tách biến và nhân tử tích phân vẫn đóng vai trò bài kiểm chuẩn độc lập: nếu trường học được gần tuyến tính $$h'=Ah+b$$, nghiệm giải tích $$e^{At}$$ là mốc đối chiếu; nếu trường tự trị một chiều, đường pha cho biết trước cấu trúc các điểm cân bằng mà mạng có thể biểu diễn.

## Ví dụ

### Ví dụ 1: Chuỗi thời gian lấy mẫu không đều

Giả sử dữ liệu quan sát $$y(t_i)$$ thu được tại các mốc $$0=t_0<t_1<\cdots<t_n$$ không cách đều. Các mạng rời rạc theo bước cố định thường phải nội suy hoặc điền giá trị khuyết, trong khi neural ODE chỉ cần tích phân cùng một quỹ đạo liên tục đến đúng các thời điểm $$t_i$$—tương tự cách xử lý số liệu lấy mẫu không đều trong bài toán bể pha trộn.

### Ví dụ 2: Mất tính Lipschitz gây sự cố khi huấn luyện

Nếu $$f_\theta$$ dùng hàm kích hoạt không bị chặn cùng trọng số lớn, hằng số Lipschitz cục bộ có thể tăng rất mạnh. Khi đó bộ giải bước thích nghi phải thu bước về cực nhỏ hoặc thất bại, còn tính duy nhất trên khoảng huấn luyện trở nên kém đảm bảo. Các kỹ thuật như suy giảm trọng số (weight decay), chuẩn hóa phổ (spectral normalization) hay dùng hàm kích hoạt bị chặn như `tanh` ở tầng cuối không chỉ để chống quá khớp mà còn nhằm giữ trường vector nằm trong phạm vi giả thiết của định lý Picard–Lindelöf.

### Ví dụ 3: Minh họa tối giản với `torchdiffeq`

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

Kết quả trả về là giá trị của quỹ đạo liên tục lấy mẫu tại 21 mốc thời gian. Nếu thay `Field` bằng trường tuyến tính $$f(t,y)=-y$$, ta thu lại đúng nghiệm phân rã mũ quen thuộc từ bài tách biến.

## Ứng dụng

Các mô hình độ sâu liên tục được ứng dụng trong phân tích chuỗi thời gian y khoa lấy mẫu không đều, mô hình hóa động lực ẩn trong khoa học thần kinh, kiến trúc mạng dư trong thị giác máy tính và các mô hình kết hợp vật lý–học máy (giữ lại phần phương trình cơ chế đã biết và chỉ học số hạng còn thiếu). Trong kỹ thuật điều khiển và dược động học, chúng cung cấp biểu diễn không gian trạng thái tự nhiên với trạng thái ẩn là vector các ngăn. Trong mọi trường hợp, lý thuyết tồn tại và duy nhất của Chương 01 là bước kiểm tra độ hợp lý đầu tiên.

Công trình của Kidger (2022) cùng hệ sinh thái Diffrax và `torchdiffeq` cũng thay đổi cách thiết kế phần mềm khoa học: bộ giải ODE không còn nằm tách biệt như hộp đen ngoài mô hình mà trở thành một tầng khả vi tích hợp trực tiếp.

## Thách thức và hướng mở rộng

Neural ODE thường huấn luyện chậm hơn mạng dư rời rạc, đặc biệt khi trường vector học được trở nên cứng (stiff). Phương pháp liên hợp có thể cho gradient sai lệch nếu dung sai tích phân đặt quá lỏng. Ngoài ra, vì dòng nghiệm của ODE khả nghịch và không tự cắt nhau, khả năng biểu diễn trên không gian gốc bị hạn chế; các giải pháp thường dùng gồm tăng chiều trạng thái (augmented neural ODE), bổ sung biến ẩn phụ hoặc dùng phương trình vi phân điều khiển (neural CDE). Một lưu ý quan trọng khác là việc khớp tốt dữ liệu lấy mẫu không đảm bảo xác định duy nhất một trường vector, bởi nhiều vế phải cấp một khác nhau có thể đi qua cùng một tập điểm quan sát hữu hạn.

Một câu hỏi mở đáng suy nghĩ: những tính chất giải tích nào của $$f$$ (như điều kiện Lipschitz, Lipschitz một phía hoặc tính đơn điệu) nên được áp đặt trong quá trình huấn luyện để mô hình học được vẫn giữ được các định lý so sánh rõ ràng như ở ODE cấp một vô hướng?

## Video tham khảo

- Xem trước: [Neural ODEs (NODEs) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=nJphsM4obOk) — Steve Brunton, tiếng Anh. Giới thiệu neural ODE với mạng nơ-ron đóng vai trò trường vector của mô hình độ sâu liên tục.
- [David Duvenaud | Reflecting on Neural ODEs | NeurIPS 2019](https://www.youtube.com/watch?v=YZ-_E7A3V2w) — Preserve Knowledge, tiếng Anh. David Duvenaud trao đổi lại về ý tưởng Neural ODE và vai trò của phương pháp liên hợp.
- [On Neural Differential Equations](https://www.youtube.com/watch?v=TGfGiBhDEi0) — Patrick Kidger, tiếng Anh. Bài giảng của Patrick Kidger về hệ phương trình vi phân nơ-ron như một khung mô hình thống nhất.

## Bài tập

1. **Từ khối residual đến ODE.** Xuất phát từ $$h_{n+1}=h_n+h\,f(h_n)$$ và cho $$h\to 0$$, hãy thu lại phương trình $$h'=f(h)$$ và nêu rõ ý nghĩa của giới hạn này trên một khoảng thời gian hữu hạn.

2. **Phép lặp Picard và bước cập nhật huấn luyện.** Xét $$y'=\theta y$$, $$y(0)=1$$. Hãy viết hai bước lặp Picard đầu tiên và so sánh quá trình lặp đó với bước hạ gradient theo $$\theta$$ cho hàm mất mát $$\lvert y(1)-e\rvert^2$$.

3. **Phương trình liên hợp cho ODE tuyến tính vô hướng.** Cho $$y'=\theta y$$, $$y(0)=1$$ và $$\mathcal{L}=\tfrac12 y(T)^2$$. Hãy tính $$\partial\mathcal{L}/\partial\theta$$ theo hai cách: lấy đạo hàm trực tiếp từ nghiệm dạng đóng và giải phương trình liên hợp ngược thời gian.

4. **Thí nghiệm tính toán.** Dùng `torchdiffeq` hoặc Diffrax để huấn luyện một neural ODE khớp dữ liệu mẫu từ phương trình logistic $$y'=y(1-y)$$. So sánh trường vector học được dọc theo đường pha với vế phải đúng và kiểm tra xem mạng có tái tạo được hai điểm cân bằng $$0$$ và $$1$$ hay không.

5. **Khám phá mở.** Đọc Chương 1 luận án của Kidger (2022) và viết khoảng một trang phân tích vì sao dữ liệu chuỗi thời gian lấy mẫu không đều phù hợp tự nhiên hơn với mô hình liên tục cấp một so với kiến trúc rời rạc cố định.

## Tài liệu

- Boyce và DiPrima, Chương 1–2; Zill, Chương 1–2.
- Chen, R. T. Q., và cộng sự. “Neural ordinary differential equations.” *NeurIPS* 2018. [arXiv:1806.07366](https://arxiv.org/abs/1806.07366).
- Kidger, P. *On Neural Differential Equations*. Oxford, 2022. [arXiv:2202.02435](https://arxiv.org/abs/2202.02435).
- Kidger, P., Morrill, J., Foster, J., và Lyons, T. “Neural controlled differential equations for irregular time series.” *ICLR* 2021. [arXiv:2005.08926](https://arxiv.org/abs/2005.08926).
- `torchdiffeq`: [https://github.com/rtqichen/torchdiffeq](https://github.com/rtqichen/torchdiffeq). Diffrax: [https://docs.kidger.site/diffrax/](https://docs.kidger.site/diffrax/).
