---
layout: post
title: "Giới Thiệu Giải Tích Bán Cổ Điển"
chapter: '15'
order: 4
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: optional
---

![Trực giác semiclassical khi tham số nhỏ tiến về 0]({{ site.imgurl }}/chapter_img/chapter15/04_semiclassical_analysis.svg )

Làm sao một thế giới cơ học lượng tử đầy sóng xác suất, nhiễu xạ và bất định lại chuyển hóa êm ái thành thế giới cơ học cổ điển của Newton với các quỹ đạo hành tinh sắc nét khi hằng số Planck $h \to 0$? **Giải tích Bán cổ điển (Semiclassical Analysis)** đặt tham số nhỏ $h \in (0, 1]$ ngay trước mọi đạo hàm ($h D_x = -ih\partial_x$), biến ký hiệu $\Psi$DO thành hàm Hamilton cổ điển $H(x, \xi) = |\xi|^2 + V(x)$ và cho phép ta quan sát trực tiếp **ranh giới giữa Sóng và Hạt**!

## Kiến thức cần nhớ: Bốn trụ cột của Giải tích Bán cổ điển

1. **Lượng tử hóa Bán cổ điển $\operatorname{Op}_h(a)$**:
   Thay $D_x$ bằng $h D_x = -ih\partial_x$: $(Op_h(a) u)(x) = (2\pi h)^{-n}\iint e^{\frac{i}{h}(x-y)\cdot\xi} a(x, \xi) u(y)\,dy\,d\xi$. Khi $h \to 0$, tham số $1/h$ đóng vai trò tương đương tần số lớn $|\xi| \to \infty$ trong phân tích vi địa phương!
2. **Xấp xỉ WKB ($u_h(x) \sim a(x) e^{i S(x)/h}$) & Phương trình Hamilton–Jacobi**:
   Thay sóng dao động nhanh $e^{iS(x)/h}$ vào $(-h^2\Delta + V(x))u = E u$ rồi gom các lũy thừa của $h$:
   - Bậc $h^0$: phương trình **Eikonal / Hamilton–Jacobi** $|\nabla S(x)|^2 + V(x) = E$ (động lực học cổ điển!).
   - Bậc $h^1$: phương trình **Truyền tải (Transport)** quyết định biên độ $a(x)$.
3. **Định lý Egorov — Tiến hóa Lượng tử bám sát Dòng chảy Cổ điển**:
   Nếu $U(t) = e^{-it P_h / h}$ là toán tử tiến hóa Schrödinger, thì $U(-t)\operatorname{Op}_h(a) U(t) = \operatorname{Op}_h(a \circ \varphi_t) + O(h)$, với $\varphi_t$ là dòng chảy Hamilton cổ điển! Phép đo lượng tử tiến hóa theo đúng quỹ đạo Newton tới sai số $O(h)$!
4. **Vùng Cấm Cổ điển & Hiệu ứng Xuyên hầm (Tunneling)**:
   Tại nơi $V(x) > E$, phương trình $|\nabla S|^2 = E - V(x) < 0$ không có nghiệm thực—hạt cổ điển bị chặn đứng tại điểm quay đầu $V(x) = E$, nhưng hàm sóng lượng tử tắt theo hàm mũ $e^{-\phi(x)/h}$ và vẫn có thể xuyên qua rào thế!

## Mục tiêu

Bài học tùy chọn này giới thiệu giải tích bán cổ điển (semiclassical analysis) như cầu nối giữa chế độ tần số cao, PDE và cơ học cổ điển. Sau bài học, sinh viên cần hiểu ý nghĩa của tham số nhỏ $$ h $$, vai trò của giới hạn $$ h\to 0 $$, và mối liên hệ giữa quỹ đạo cổ điển, gói sóng (wave packets) và toán tử Schrödinger.

## Kiến thức nền

Sinh viên nên nắm biến đổi Fourier, toán tử giả vi phân, trực giác cơ học Hamilton và phương trình Schrödinger cơ bản. Kiến thức về lý thuyết phổ và tập mặt sóng cũng hỗ trợ tốt cho việc hiểu thang đo mới do tham số nhỏ tạo ra.

## Dẫn nhập

Giải tích bán cổ điển nghiên cứu hành vi của nghiệm PDE khi một tham số nhỏ — thường ký hiệu $$ h $$ hoặc $$ \hbar $$ — tiến về 0. Trong vật lý, đây là giới hạn chuyển từ cơ học lượng tử sang cơ học cổ điển; trong giải tích, đây cũng là cách khảo sát chế độ tần số rất cao hay bước sóng rất ngắn. Nhờ đó, giải tích bán cổ điển trở thành giao điểm của PDE, lý thuyết phổ và động lực học Hamilton.

Ưu điểm lớn của lý thuyết này là quy tụ nhiều câu hỏi tưởng như tách biệt — sự định xứ của nghiệm, quỹ đạo cổ điển và phân bố phổ năng lượng cao — vào cùng một ngôn ngữ thống nhất.


### Giải thích: Rút ra phương trình năng lượng cổ điển từ phương trình Schrödinger bán cổ điển bằng phép tính WKB 2 dòng

Xét dao động tử điều hòa lượng tử bán cổ điển $P_h u = \big(-h^2\partial_x^2 + x^2\big)u = E u$ với thử nghiệm WKB $u_h(x) = e^{iS(x)/h}$:
1. **Tính đạo hàm bậc nhất và bậc hai**:
   - $u_h' = \frac{i}{h}S'(x) u_h$.
   - $u_h'' = \left(-\frac{1}{h^2}(S'(x))^2 + \frac{i}{h}S''(x)\right) u_h$.
2. **Thay vào $(-h^2\partial_x^2 + x^2)u_h = E u_h$ và chia cho $u_h$**:
   $$\big(S'(x)\big)^2 - i h S''(x) + x^2 = E.$$
3. **Lấy giới hạn bán cổ điển $h \to 0$**:
   Số hạng $-ihS''(x)$ biến mất, để lại đúng phương trình bảo toàn năng lượng cổ điển với động lượng $p = S'(x)$:
   $$\mathbf{p^2 + x^2 = E}!$$
   Với $E = 1$, hạt cổ điển dao động qua lại giữa hai **điểm quay đầu** $x = \pm 1$ (nơi $p = 0$); còn vùng $|x| > 1$ là vùng cấm cổ điển nơi biên độ sóng tắt mũ!
## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một gói sóng ngày càng thu hẹp: khi bước sóng rất nhỏ so với kích thước đặc trưng của hệ, sóng bắt đầu hành xử giống một hạt chuyển động dọc theo quỹ đạo cổ điển. Giải tích bán cổ điển khảo sát chính vùng chuyển tiếp đó — đối tượng vẫn mang bản chất sóng, nhưng cấu trúc động lực học cổ điển đã hiện ra rõ nét.

### Cách hình ảnh

Có thể vẽ đối chiếu ba hình ảnh:

- một sóng trải rộng;
- một gói sóng hẹp;
- quỹ đạo cổ điển mà tâm gói sóng bám theo.

Cách trình bày này giúp người học thấy ngay vì sao khi tham số nhỏ tiến về 0, cấu trúc quỹ đạo cổ điển nổi lên từ nền dao động sóng.

### Cách hình thức

Ta khảo sát các họ toán tử phụ thuộc tham số nhỏ $$ h $$, tiêu biểu là $$ P_h=-h^2\Delta+V(x) $$. Khi $$ h\to 0 $$, toán tử được phân tích qua ký hiệu bán cổ điển $$ p(x,\xi)=\lvert \xi\rvert^2+V(x) $$, trùng khớp với hàm Hamilton cổ điển của hệ. Nhờ vậy, nhiều tính chất cao tần của nghiệm được đọc trực tiếp từ hình học cổ điển trên không gian pha.

## Ngộ nhận thường gặp

### “Giải tích bán cổ điển chỉ là một nhánh của vật lý lượng tử”

Không đúng. Trong giải tích toán học, đây còn là công cụ nền tảng cho các bài toán tần số cao và bước sóng ngắn.

### “Khi $$ h\to 0 $$ thì sóng biến mất hoàn toàn, chỉ còn hạt”

Không hoàn toàn. Bản chất sóng vẫn tồn tại, nhưng cấu trúc định xứ và lan truyền của sóng phản ánh chặt chẽ động lực học cổ điển.

### “Giải tích bán cổ điển chỉ là phép đổi ký hiệu”

Sai. Tham số nhỏ $$ h $$ sinh ra một phép tính ký hiệu riêng cùng nhiều kết quả sâu về phổ và lan truyền.

### “Quỹ đạo cổ điển mô tả đầy đủ hành vi lượng tử”

Không. Giới hạn cổ điển cung cấp bức tranh dẫn đầu, còn nhiều hiệu ứng lượng tử tinh vi như xuyên hầm hay giao thoa vẫn cần phân tích sâu hơn.

## Tiến trình học

### Bước 1: Hiểu vai trò của tham số nhỏ

Xem $$ h $$ như một thang đo bước sóng chứ không chỉ là hằng số vật lý cố định.

### Bước 2: Chuyển từ toán tử sang ký hiệu bán cổ điển

Liên kết trực tiếp ký hiệu bán cổ điển với hàm Hamilton cổ điển.

### Bước 3: Sử dụng gói sóng

Xem gói sóng là cầu nối trực quan nhất giữa dao động sóng và quỹ đạo hạt.

### Bước 4: Liên hệ với lý thuyết phổ và cơ học lượng tử

Nhận ra nhiều bài toán trị riêng lớn có thể viết lại thành bài toán bán cổ điển.

### Ghi chú sư phạm then chốt

Trong bài học này, người học dễ bị quá tải thuật ngữ khi phải làm việc đồng thời với sóng, hạt, phổ và quỹ đạo Hamilton. Có thể tóm tắt mạch tư duy qua ba bước liên kết:

- $$ h $$ nhỏ tương ứng với bước sóng rất ngắn;
- bước sóng ngắn cho phép nghiệm tập trung hẹp trong không gian pha;
- khi tập trung mạnh, chuyển động của gói sóng bám theo quỹ đạo cổ điển.

Nắm chắc chuỗi liên hệ này sẽ giúp các công thức hình thức phía sau dễ tiếp cận hơn nhiều.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao $$ h\to 0 $$ tương ứng với giới hạn tần số cao hay không?
- Sinh viên có hiểu mối liên hệ giữa ký hiệu bán cổ điển và hàm Hamilton cổ điển hay không?
- Sinh viên có mô tả được vai trò của gói sóng hay không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử Schrödinger tự do

Xét $$ P_h=-h^2\Delta $$. Ký hiệu bán cổ điển của nó là $$ p(x,\xi)=\lvert \xi\rvert^2 $$, trùng khớp với động năng cổ điển.

### Ví dụ 2: Bổ sung thế năng

Với $$ P_h=-h^2\Delta+V(x) $$, ký hiệu trở thành $$ \lvert \xi\rvert^2+V(x) $$ — đúng bằng hàm Hamilton quen thuộc của cơ học cổ điển, giải thích vì sao quỹ đạo cổ điển xuất hiện tự nhiên trong giải tích PDE.

### Ví dụ 3: Gói sóng

Một gói sóng hẹp định xứ trong không gian pha sẽ di chuyển bám sát dòng Hamilton của ký hiệu trong một khoảng thời gian thích hợp — đây là trực giác cốt lõi của nguyên lý tương ứng cổ điển–lượng tử.

### Ví dụ 4: Phổ năng lượng cao

Bài toán trị riêng lớn cho $$ -\Delta $$ có thể quy về bài toán bán cổ điển bằng cách đặt $$ h\sim \lambda^{-1/2} $$, cho thấy mối liên hệ trực tiếp giữa giải tích bán cổ điển và tiệm cận phổ.

### Ví dụ 5: Dạng nghiệm thử WKB

Một dạng nghiệm thử (ansatz) kinh điển là $$ u_h(x)\approx a(x)e^{iS(x)/h} $$, trong đó $$ S(x) $$ là hàm pha cổ điển còn $$ a(x) $$ là biên độ biến thiên chậm. Khi thay vào phương trình, số hạng bậc dẫn đầu cho phương trình Hamilton–Jacobi cho $$ S $$, chứng tỏ quỹ đạo cổ điển tự nảy sinh trực tiếp từ cấu trúc nghiệm dao động nhanh.

## Câu hỏi khái niệm

1. Vì sao giới hạn $$ h\to 0 $$ đồng nghĩa với giới hạn tần số cao?
2. Điều gì khiến ký hiệu bán cổ điển đóng vai trò của hàm Hamilton cổ điển?
3. Vì sao gói sóng là công cụ trực giác trung tâm của giải tích bán cổ điển?

## Bài toán ứng dụng

1. Trong cơ học lượng tử, vì sao quỹ đạo cổ điển nổi lên ở giới hạn năng lượng cao?
2. Trong quang học hình học, chế độ bước sóng ngắn liên hệ ra sao với giải tích bán cổ điển?
3. Trong lý thuyết phổ, vì sao bài toán đếm trị riêng lớn có thể chuyển về bài toán bán cổ điển?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Khi bước sóng trở nên rất nhỏ so với kích thước hệ, sóng sẽ có hành vi gần với mô hình nào?
- Vì sao việc đưa thêm một tham số nhỏ lại tạo ra cả một góc nhìn giải tích mới?
- Mối liên hệ giữa hàm Hamilton cổ điển và toán tử lượng tử thể hiện ở đâu?

### Hoạt động gợi ý

- Vẽ đối chiếu quỹ đạo cổ điển với đường đi của tâm gói sóng.
- So sánh trực tiếp toán tử Schrödinger với hàm Hamilton cổ điển tương ứng.
- Thảo luận nhóm câu hỏi: giải tích bán cổ điển nên được hiểu là “giới hạn lượng tử” hay “giới hạn cao tần”?

### Cách tăng mức độ tham gia

- Mở đầu bằng hình ảnh trực quan của gói sóng hẹp.
- Đề nghị sinh viên tự đoán ký hiệu bán cổ điển của một số toán tử quen thuộc.
- Khuyến khích giải thích ý nghĩa vật lý trước khi viết biểu thức toán tử.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám sát ví dụ mẫu $$ -h^2\Delta+V(x) $$.
- Chưa cần đi sâu vào toàn bộ phép tính giả vi phân bán cổ điển.
- Nhấn mạnh một ý chủ đạo: khi $$ h $$ nhỏ, sóng bộc lộ quỹ đạo cổ điển.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu khái niệm tập mặt sóng bán cổ điển.
- Nắm ý tưởng định lý Egorov về sự tiến hóa của đại lượng quan sát.
- Khảo sát mối liên hệ giữa phương pháp WKB và phương trình Hamilton–Jacobi.

## Ghi nhớ nhanh

Giải tích bán cổ điển khảo sát PDE phụ thuộc tham số nhỏ $$ h $$, kết nối cấu trúc sóng cao tần của nghiệm với động lực học cổ điển trên không gian pha và bắc cầu giữa giải tích Fourier, lý thuyết phổ và cơ học lượng tử.

---

## Ứng dụng thực tế

### 1. Cơ học lượng tử: Nguyên lý tương ứng Bohr

Nguyên lý tương ứng Bohr nêu rằng cơ học lượng tử phải quy về cơ học cổ điển trong giới hạn tác dụng lớn ($$ \hbar \to 0 $$ trên thang vĩ mô). Giải tích bán cổ điển cung cấp khuôn khổ toán học chặt chẽ cho nguyên lý này.

Với phương trình Schrödinger dừng:
$$ -\frac{\hbar^2}{2m}\Delta\psi + V(x)\psi = E\psi, $$
đặt $$ h = \hbar $$ và xét nghiệm thử WKB:
$$ \psi_h(x) \approx A(x) e^{iS(x)/h}, $$
số hạng bậc dẫn đầu cho phương trình Hamilton–Jacobi:
$$ \frac{\lvert \nabla S\rvert^2}{2m} + V(x) = E, $$
mô tả chính xác quỹ đạo cổ điển của hạt có năng lượng $$ E $$ trong thế năng $$ V(x) $$.

**Ứng dụng:** Tính xác suất xuyên hầm lượng tử (quantum tunneling) qua rào thế — cơ sở của điốt phát quang (LED), laser bán dẫn và kính hiển vi quét xuyên hầm (STM).

### 2. Quang học: Từ sóng điện từ đến tia sáng

Phương trình sóng Maxwell
$$
\frac{\partial^2 \mathbf{E}}{\partial t^2} = c^2 \Delta \mathbf{E}
$$
trong môi trường có chiết suất biến thiên $$ n(x) $$ chứa tham số nhỏ tự nhiên là tỉ số $$ \lambda/L $$ (bước sóng chia cho kích thước đặc trưng). Khi $$ \lambda/L \to 0 $$, sóng điện từ tập trung dọc theo các tia sáng — chính là đường song đặc trưng của phương trình eikonal:
$$ \lvert \nabla S\rvert^2 = n(x)^2. $$
Đây là nền tảng của quang học hình học, từ thiết kế kính thiên văn không gian đến kỹ thuật quang khắc (lithography) trong chế tạo vi mạch.

### 3. Địa chấn học tần số cao

Trong thăm dò địa chấn, sóng tần số cao (chu kỳ $$ T $$ rất nhỏ so với quy mô cấu trúc địa chất) truyền xấp xỉ theo các tia địa chấn với tham số nhỏ $$ h \sim T/T_{\rm geol} $$. Giải tích bán cổ điển giải thích vì sao lý thuyết tia hiệu quả ở tần số cao và chỉ ra nơi nó mất hiệu lực (tại các vùng tụ quang — caustic — nơi nhiều tia giao nhau).

### 4. Vật lý laser và quang học lượng tử

Trong buồng cộng hưởng laser, các mode dao động là trị riêng của toán tử Maxwell. Giải tích bán cổ điển dự đoán phân bố tần số mode thông qua các quỹ đạo ánh sáng tuần hoàn trong buồng, làm cơ sở cho laser Fabry–Pérot và nhiều hệ quang học hiện đại.

---

## Trực quan hóa bằng Python

### Gói sóng và sự hội tụ về quỹ đạo cổ điển khi h → 0

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# -------------------------------------------------------
# Minh họa: Wave packet Gaussian trong thế năng điều hòa
# V(x) = x²/2 → quỹ đạo cổ điển: x(t) = A cos(t + φ)
# Khi h nhỏ, tâm gói sóng đi theo quỹ đạo cổ điển
# -------------------------------------------------------

def V(x):
    """Thế năng điều hòa"""
    return 0.5 * x**2

def classical_trajectory(x0, p0, t_vals):
    """Quỹ đạo cổ điển trong thế năng điều hòa"""
    # x(t) = x0 cos(t) + p0 sin(t)
    return x0 * np.cos(t_vals) + p0 * np.sin(t_vals)

def wave_packet(x, x0, p0, h, sigma=1.0):
    """Wave packet Gaussian: Ψ(x) = (2πσ²h)^{-1/4} exp(-(x-x0)²/4σ²h + ip0x/h)"""
    norm = (2 * np.pi * sigma**2 * h)**(-0.25)
    return norm * np.exp(-(x - x0)**2 / (4 * sigma**2 * h)) * np.exp(1j * p0 * x / h)

# Thiết lập
N = 1000
x = np.linspace(-6, 6, N)
x0, p0 = 3.0, 0.0  # Điều kiện ban đầu cổ điển
t_vals = np.linspace(0, 2 * np.pi, 200)

h_values = [1.0, 0.3, 0.1, 0.03]
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, h in enumerate(h_values):
    ax = axes[i]
    psi0 = wave_packet(x, x0, p0, h)
    # Mật độ xác suất ban đầu
    prob0 = np.abs(psi0)**2
    ax.plot(x, prob0 / prob0.max(), 'steelblue', linewidth=2,
            alpha=0.8, label=f"|ψ₀|² (h={h})")

    # Mật độ tại t=π/2 (tâm gói sóng ở x=0, p=p0)
    x_cl = classical_trajectory(x0, p0, np.pi/2)
    psi_half = wave_packet(x, x_cl, -x0, h)
    prob_half = np.abs(psi_half)**2
    ax.plot(x, prob_half / prob_half.max(), 'crimson', linewidth=2,
            alpha=0.8, label=f"|ψ(t=π/2)|²")

    # Quỹ đạo cổ điển
    x_cl_traj = classical_trajectory(x0, p0, t_vals)
    ax.axvline(x=x_cl, color='crimson', linestyle='--', alpha=0.5,
               label=f"Vị trí cổ điển x={x_cl:.2f}")
    ax.axvline(x=x0,   color='steelblue', linestyle='--', alpha=0.5)

    # Thế năng
    ax2 = ax.twinx()
    ax2.plot(x, V(x), 'green', linewidth=1, alpha=0.4, linestyle=':')
    ax2.set_ylabel("V(x)", color='green', fontsize=9)
    ax2.tick_params(axis='y', labelcolor='green')

    ax.set_title(f"h = {h}: Wave packet " +
                 ("rộng (sóng)" if h >= 0.5 else "hẹp (gần hạt cổ điển)"),
                 fontweight='bold', fontsize=10)
    ax.set_xlabel("x"); ax.set_ylabel("|ψ|² (chuẩn hóa)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    ax.set_xlim(-5, 5)

plt.suptitle("Semiclassical Analysis: Khi h→0, wave packet hội tụ về quỹ đạo cổ điển\n"
             "V(x) = x²/2 (điều hòa): x(t) = x₀cos(t) + p₀sin(t)",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("semiclassical_wave_packet.png", dpi=150)
plt.show()
```

### Xấp xỉ WKB: Xuyên hầm lượng tử

```python
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# WKB: Xuyên hầm qua rào thế Gaussian
# Hệ số xuyên hầm T ∝ exp(-2/h * ∫√(V(x)-E) dx)
# -------------------------------------------------------

x = np.linspace(-4, 4, 1000)

def V_barrier(x, V0=2.0, sigma=0.8):
    """Rào thế Gaussian"""
    return V0 * np.exp(-x**2 / (2 * sigma**2))

E = 0.8  # Năng lượng hạt (dưới đỉnh rào thế V0=2.0)
V = V_barrier(x)

# Vùng cổ điển cấm: V(x) > E
classically_forbidden = V > E

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Hình 1: Rào thế và WKB wavefunction ---
ax = axes[0]
ax.fill_between(x, E, V, where=classically_forbidden,
                alpha=0.3, color='red', label="Vùng cấm cổ điển")
ax.plot(x, V, 'darkred', linewidth=2, label="V(x) (rào thế Gaussian)")
ax.axhline(y=E, color='navy', linestyle='--', linewidth=2, label=f"E = {E}")

# WKB wavefunction gần đúng
h = 0.3
psi_approx = np.zeros(len(x))
for j, xj in enumerate(x):
    if V[j] <= E:
        # Vùng cổ điển cho phép: oscillatory
        k = np.sqrt(2 * (E - V[j])) / h
        psi_approx[j] = np.cos(k * xj) / max(np.sqrt(E - V[j] + 0.01), 0.1)
    else:
        # Vùng cấm: exponential decay
        kappa = np.sqrt(2 * (V[j] - E)) / h
        psi_approx[j] = np.exp(-kappa * abs(xj) * 0.5)

psi_norm = 0.3 * psi_approx / (np.abs(psi_approx).max() + 1e-10)
ax.plot(x, E + psi_norm, 'steelblue', linewidth=2, alpha=0.8,
        label=f"WKB ψ (h={h})")
ax.fill_between(x, E, E + psi_norm, alpha=0.15, color='steelblue')
ax.set_title("Xuyên hầm lượng tử: WKB Approximation\n"
             "Sóng tắt dần trong vùng cấm, xuất hiện lại ở phía kia",
             fontweight='bold')
ax.set_xlabel("x"); ax.set_ylabel("Năng lượng / Biên độ")
ax.legend(fontsize=9); ax.grid(alpha=0.3)
ax.set_ylim(-0.5, 2.5)

# --- Hình 2: Hệ số xuyên hầm vs h ---
ax = axes[1]
h_vals = np.linspace(0.05, 1.0, 100)
dx = x[1] - x[0]
# Tích phân WKB trong vùng cấm
integrand = np.sqrt(np.maximum(V - E, 0))
tunnel_integral = np.trapz(integrand, x)
T_WKB = np.exp(-2 * tunnel_integral / h_vals)

ax.semilogy(h_vals, T_WKB, 'crimson', linewidth=2.5, label="T(h) = exp(-2S/h)")
ax.fill_between(h_vals, T_WKB * 0.5, T_WKB * 2.0, alpha=0.2, color='crimson')
ax.axvline(x=0.3, color='steelblue', linestyle='--', label="h = 0.3 (ví dụ trên)")
ax.set_title("Hệ số xuyên hầm T(h) theo tham số h\n"
             "Khi h→0: xuyên hầm gần bằng 0 (giới hạn cổ điển)",
             fontweight='bold')
ax.set_xlabel("h (tham số bán cổ điển)"); ax.set_ylabel("T(h) (log scale)")
ax.legend(); ax.grid(alpha=0.3)
ax.text(0.5, 1e-3, "Giới hạn cổ điển:\nkhông có xuyên hầm",
        ha='center', fontsize=10, color='gray',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.suptitle("Semiclassical (WKB): Xuyên hầm lượng tử và giới hạn cổ điển",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("WKB_tunneling.png", dpi=150)
plt.show()
```

---

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

**Thông điệp chính:** Khi bước sóng rất ngắn, sóng hành xử gần như hạt cổ điển, và giải tích bán cổ điển định lượng chính xác quá trình chuyển tiếp này.

**Điều cần nhớ:**
- Tham số $$ h $$ đo tỉ số giữa bước sóng và thang kích thước đặc trưng của bài toán.
- Dạng nghiệm thử WKB: $$ \psi_h \approx A(x) e^{iS(x)/h} $$ gồm pha dao động nhanh và biên độ biến thiên chậm.
- Ký hiệu bán cổ điển $$ p(x,\xi) = \lvert \xi\rvert^2 + V(x) $$ chính là hàm Hamilton cổ điển.
- Quỹ đạo cổ điển hiện ra như đường đi của tâm gói sóng khi $$ h \to 0 $$.

**Bài tập:** Với thế năng điều hòa $$ V(x) = x^2/2 $$, hãy tìm hàm pha WKB $$ S(x) $$ thỏa phương trình Hamilton–Jacobi và giải thích kết quả theo quỹ đạo cổ điển.

### Mức sau đại học (Graduate)

**Phép tính bán cổ điển:** Họ các toán tử $$ {Op_h(a) : a \in S^m} $$ với quy ước lượng tử hóa Weyl
$$
Op_h(a) u(x) = \frac{1}{(2\pi h)^n} \int e^{i(x-y)\cdot\xi/h} a\left(\frac{x+y}{2}, \xi\right) u(y)\, dy\, d\xi
$$
tạo thành một đại số với phép hợp thành thỏa mãn
$$
Op_h(a) \circ Op_h(b) = Op_h(a \# b),
\qquad a \# b = ab + \frac{h}{2i}\{a, b\} + O(h^2),
$$
trong đó $$\{a,b\} = \nabla_\xi a \cdot \nabla_x b - \nabla_x a \cdot \nabla_\xi b$$ là ngoặc Poisson.

**Định lý Egorov:** Nếu $$ \Phi_t $$ là dòng Hamilton của $$ p $$, thì
$$
e^{itP_h/h} \circ Op_h(a) \circ e^{-itP_h/h} = Op_h(a \circ \Phi_t) + O(h),
$$
nghĩa là toán tử tiến hóa lượng tử làm biến đổi đại lượng quan sát dọc theo dòng cổ điển — biểu thức toán học chặt chẽ của nguyên lý tương ứng.

**Liên kết với FIO:** Toán tử tiến hóa $$ e^{-itP_h/h} $$ là một FIO có hàm pha là hàm tác dụng Hamilton–Jacobi.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm | Kết nối |
|---|---|
| Phương pháp WKB (Ch. 6) | Dạng nghiệm thử WKB là trường hợp riêng của giải tích bán cổ điển |
| Phương trình Hamilton–Jacobi | Hàm pha WKB thỏa phương trình Hamilton–Jacobi |
| FIO (Bài 15.03) | Toán tử tiến hóa bán cổ điển là một FIO |
| Tiệm cận phổ (Bài 15.05) | Trị riêng năng lượng cao tương ứng với tham số bán cổ điển nhỏ |
| Cơ học lượng tử (Bài 15.07) | Nguyên lý tương ứng được phát biểu chặt chẽ qua định lý Egorov |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quang học hình học
- Bài toán: Khi bước sóng rất ngắn, ánh sáng truyền gần như theo tia và phản xạ, khúc xạ theo các định luật cổ điển.
- Mô hình: Sử dụng tham số nhỏ $$ h $$ trong dạng nghiệm thử WKB
$$ u_h(x)\approx a(x)e^{i\phi(x)/h}. $$
- Giả thiết và giới hạn: Hiệu quả ở chế độ tần số cao nhưng mất hiệu lực gần vùng tụ quang (caustics) hoặc điểm quay (turning points).
- Diễn giải: Giải tích bán cổ điển nối trực tiếp PDE với các quỹ đạo Hamilton cổ điển.

#### Cơ học lượng tử bán cổ điển
- Bài toán: Khảo sát cách trạng thái lượng tử tập trung quanh quỹ đạo cổ điển khi $$ h \to 0 $$.
- Mô hình: Sử dụng toán tử bán cổ điển và gói sóng.
- Giả thiết và giới hạn: Có hiệu lực ở chế độ hằng số Planck hiệu dụng nhỏ và trong khoảng thời gian thích hợp.
- Diễn giải: Đây là dạng toán học chặt chẽ của nguyên lý tương ứng.

### 2. Trực giác bổ sung và các kết nối

Giải tích bán cổ điển nghiên cứu chế độ tần số rất cao hoặc tham số lượng tử $$ h $$ rất nhỏ, nơi nghiệm dao động rất nhanh trong khi biên độ biến thiên chậm. Tham số $$ h $$ không chỉ là ký hiệu phụ mà quyết định toàn bộ cấu trúc thang đo của bài toán.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1200)
for h in [0.5, 0.25, 0.12]:
    u = np.exp(-x**2) * np.cos(x / h)
    plt.plot(x, u, label=f"h={h}")

plt.legend()
plt.title("Song goi dao dong nhanh hon khi h nho")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: semiclassical wave packet visualization
- search: WKB approximation optics intuition
- search: Egorov theorem classical trajectories animation

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Giới hạn bán cổ điển: gói sóng và quỹ đạo cổ điển" description="Thay đổi tham số h, vị trí đầu và động lượng đầu để quan sát tâm gói sóng tiến gần quỹ đạo cổ điển." path="interactives/chapter15/semiclassical-wave-packet-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Với phương trình Schrödinger tự do bán cổ điển
$$ ih \partial_t u_h = -\frac{h^2}{2}\Delta u_h, $$
một gói sóng ban đầu tập trung quanh $$ (x_0,\xi_0) $$ sẽ di chuyển bám sát quỹ đạo cổ điển
$$ \dot x = \xi, \qquad \dot \xi = 0. $$
Kết quả này minh họa trực tiếp cách động lực học lượng tử tiến gần động lực học cổ điển khi $$ h $$ nhỏ.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm dạng nghiệm thử WKB và trực giác chế độ bước sóng ngắn.

**Bậc sau đại học.** Kết nối với phép tính giả vi phân bán cổ điển, định lý Egorov và độ đo bán cổ điển.

## Video tham khảo

- Nên xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Bài giảng của Maciej Zworski theo hướng vi địa phương gắn liền với giải tích bán cổ điển.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Khung vi địa phương làm nền cho phần tinh chỉnh với tham số bán cổ điển.
- [Math of QM: 5.7. Spectral Theorem for Unbounded Selfadjoint Operators](https://www.youtube.com/watch?v=cdOkiNIONSc) — Roland Speicher, tiếng Anh. Định lý phổ cho toán tử tự liên hợp không bị chặn — nền tảng giải tích hàm của cơ học lượng tử.
