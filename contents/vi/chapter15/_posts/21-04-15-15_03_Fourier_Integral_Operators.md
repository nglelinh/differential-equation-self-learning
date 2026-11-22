---
layout: post
title: "Toán Tử Tích Phân Fourier"
chapter: '15'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: required
---

![Fourier integral operators và biến đổi mặt sóng]({{ site.imgurl }}/chapter_img/chapter15/03_fourier_integral_operators.svg )

## Mục tiêu

Bài học này giới thiệu toán tử tích phân Fourier (FIO) như lớp toán tử tự nhiên để mô tả quá trình truyền sóng và biến đổi mặt sóng. Sau bài học, sinh viên cần phân biệt được FIO với ΨDO, nắm vai trò của hàm pha (phase function) và biên độ (amplitude), và hiểu vì sao FIO là công cụ phù hợp cho sự lan truyền kỳ dị.

## Kiến thức nền

Sinh viên nên nắm toán tử giả vi phân, tập mặt sóng và trực giác rằng sự lan truyền kỳ dị đòi hỏi lớp toán tử tổng quát hơn phép lọc tần số cục bộ. Kiến thức trực giác về pha dao động và phương trình Hamilton–Jacobi cũng rất hữu ích.

## Dẫn nhập

Toán tử giả vi phân rất hiệu quả nhưng về bản chất vẫn hành xử như các bộ lọc tần số cục bộ (giữ nguyên vị trí của tập mặt sóng). Trong các bài toán truyền sóng, điều đó chưa đủ vì sóng còn bị dịch chuyển, xoay pha, hội tụ, tán xạ và biến đổi hình học. Để mô tả các quá trình này, ta mở rộng sang lớp toán tử tích phân Fourier (FIO).

Nếu ΨDO là ngôn ngữ của việc “điều chỉnh biên độ theo tần số tại chỗ”, thì FIO là ngôn ngữ của việc “vận chuyển và biến dạng mặt sóng”.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một chùm sáng đi qua thấu kính: thấu kính không chỉ làm thay đổi cường độ mà còn làm thay đổi pha và hướng truyền của cả chùm tia. FIO thực hiện vai trò tương tự đối với các thành phần dao động của nghiệm PDE.

### Cách hình ảnh

Có thể vẽ một mặt sóng ban đầu và mặt sóng sau khi lan truyền. Nếu với ΨDO mỗi tần số chỉ bị nhân bởi một hệ số cục bộ, thì với FIO cấu trúc hàm pha đẩy mặt sóng sang vị trí mới và hướng mới trong không gian pha.

### Cách hình thức

Một toán tử tích phân Fourier điển hình có dạng

$$
Tu(x)=\int e^{i\phi(x,\xi)}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

trong đó:

- $$ \phi(x,\xi) $$ là hàm pha (phase function);
- $$ a(x,\xi) $$ là biên độ (amplitude).

Khi hàm pha có dạng chuẩn $$ \phi(x,\xi)=x\cdot\xi $$, công thức trên rút gọn về lớp toán tử giả vi phân quen thuộc. Do đó, FIO là sự mở rộng trực tiếp của ΨDO.

## Ngộ nhận thường gặp

### “FIO chỉ là cách viết phức tạp hơn của ΨDO”

Không đúng. Điểm khác biệt bản chất nằm ở hàm pha không tầm thường làm thay đổi vị trí và hướng trong không gian pha.

### “Biên độ luôn là thành phần quan trọng nhất”

Không hẳn. Trong bài toán lan truyền, chính hàm pha mới quyết định hình học của quỹ đạo và mặt sóng.

### “FIO chỉ xuất hiện trong vật lý sóng”

Sai. Lớp toán tử này còn đóng vai trò quan trọng trong bài toán ngược, hình học vi phân và lý thuyết phổ.

### “Phải nắm trọn lý thuyết hàm pha mới hiểu được trực giác của FIO”

Không cần thiết ở bước đầu; người học có thể hình dung ngay FIO như toán tử vận chuyển mặt sóng.

## Tiến trình học

### Bước 1: Nhìn lại ΨDO

Nhận diện giới hạn của ΨDO: chủ yếu thực hiện lọc cục bộ mà không dịch chuyển tập mặt sóng.

### Bước 2: Đưa vào hàm pha

Hiểu hàm pha là thành phần tạo nên biến đổi hình học của toán tử.

### Bước 3: Kết nối với sự lan truyền kỳ dị

Thấy rõ FIO là công cụ toán tử hiện thực hóa định lý lan truyền kỳ dị.

### Bước 4: Đặt FIO trong bức tranh tổng thể

Ghi nhận rằng toán tử tiến hóa của nhiều phương trình hyperbolic được biểu diễn dưới dạng FIO.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được điểm mở rộng cốt lõi của FIO so với ΨDO hay không?
- Sinh viên có thấy hàm pha chi phối hình học của mặt sóng hay không?
- Sinh viên có liên hệ được FIO với định lý lan truyền kỳ dị hay không?

## Ví dụ có lời giải

### Ví dụ 1: Trường hợp rút gọn về ΨDO

Khi $$ \phi(x,\xi)=x\cdot\xi $$, ta thu được

$$
Tu(x)=\int e^{ix\cdot\xi}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

chính là biểu thức của một toán tử giả vi phân. Ví dụ này xác nhận ΨDO là trường hợp riêng của FIO.

### Ví dụ 2: Toán tử tịnh tiến

Xét $$ Tu(x)=u(x-c) $$. Trong miền Fourier,

$$
\widehat{Tu}(\xi)=e^{-ic\cdot\xi}\widehat{u}(\xi).
$$

Hàm pha $$ (x-c)\cdot\xi $$ tạo ra phép dịch chuyển không gian. Đây là ví dụ đơn giản nhất cho thấy hàm pha làm thay đổi vị trí của điểm kỳ dị.

### Ví dụ 3: Nghiệm sóng tự do

Toán tử tiến hóa của phương trình sóng tự do có thể biểu diễn bằng FIO với hàm pha gắn liền với hàm tác dụng cổ điển hoặc nghiệm phương trình eikonal. Ở mức nhập môn, điều quan trọng là nhận ra FIO chính là dạng tự nhiên của toán tử tiến hóa sóng.

### Ví dụ 4: Biến đổi hình học mặt sóng

Nếu tập mặt sóng của $$ u $$ nằm trên một mặt nhất định, FIO sẽ đưa mặt đó sang vị trí và hướng mới theo phép biến đổi chính tắc (canonical transformation) sinh bởi hàm pha — đó chính là cơ chế “vận chuyển tập mặt sóng”.

### Ví dụ 5: Trực giác từ chụp cắt lớp

Trong nhiều mô hình chụp cắt lớp (CT), dữ liệu đo là tích phân của hàm mật độ dọc theo các đường thẳng hay tia chiếu. Cả toán tử thuận chuyển vật thể thành dữ liệu lẫn toán tử chiếu ngược (backprojection) kéo dữ liệu về ảnh đều mang bản chất FIO: chúng vận chuyển kỳ dị giữa vật thể thực và miền dữ liệu đo.

## Câu hỏi khái niệm

1. Vì sao hàm pha là thành phần mang thông tin hình học của FIO?
2. Điều gì khiến FIO trở thành ngôn ngữ tự nhiên cho quá trình truyền sóng?
3. Ở mức trực giác, vai trò của biên độ và hàm pha khác nhau như thế nào?

## Bài toán ứng dụng

1. Trong quang học hình học, thấu kính và gương phản xạ gợi trực giác gì về FIO?
2. Trong chụp cắt lớp, vì sao toán tử liên kết dữ liệu đo với kỳ dị của vật thể thường là một FIO?
3. Trong địa chấn học, sự lan truyền sóng phản xạ dọc theo các tia được mã hóa qua hàm pha như thế nào?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Nếu một toán tử không chỉ lọc mà còn dịch chuyển mặt sóng, nó cần thêm thành phần dữ liệu nào so với ΨDO?
- Hàm pha đang mã hóa cấu trúc hình học nào?
- Sự khác nhau về mặt vật lý giữa “thay đổi biên độ” và “thay đổi pha” là gì?

### Hoạt động gợi ý

- So sánh trực tiếp một ΨDO và toán tử tịnh tiến trong miền Fourier.
- Vẽ minh họa mặt sóng trước và sau khi chịu tác động của một FIO đơn giản.
- Thảo luận nhóm về phép tương tự giữa ánh sáng qua thấu kính và FIO.

### Cách tăng mức độ tham gia

- Bắt đầu từ các hiện tượng truyền sóng quen thuộc.
- Đề nghị sinh viên tự suy ra hàm pha của phép tịnh tiến.
- Mời sinh viên diễn đạt khái niệm FIO bằng một câu ngắn không dùng ký hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung vào ví dụ phép tịnh tiến và hàm pha tuyến tính.
- Chưa cần đi sâu vào định nghĩa đầy đủ của quan hệ chính tắc ở lượt học đầu.
- Nhấn mạnh trực giác: FIO là toán tử vận chuyển mặt sóng.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu phép biến đổi chính tắc sinh bởi hàm pha.
- Liên hệ FIO với nghiệm của phương trình Hamilton–Jacobi.
- Khảo sát định lý ánh xạ tập mặt sóng dưới tác động của FIO.

## Ghi nhớ nhanh

Toán tử tích phân Fourier mở rộng toán tử giả vi phân bằng cách bổ sung hàm pha tổng quát để mô tả sự dịch chuyển hình học của mặt sóng, trở thành ngôn ngữ tự nhiên cho lan truyền kỳ dị và nhiều bài toán sóng hiện đại.

---

## Ứng dụng thực tế

### 1. Seismic Migration: Đưa ảnh địa chấn về đúng vị trí

Trong thăm dò địa chấn, dữ liệu sóng phản xạ ghi nhận trên mặt đất không phản ánh trực tiếp vị trí thật của tầng địa chất do sóng truyền dọc theo các tia qua nhiều lớp môi trường. Bước *seismic migration* đưa tín hiệu phản xạ về đúng tọa độ không gian của nó.

Về mặt toán học, toán tử migration là một FIO: nó tích phân dữ liệu đo dọc theo các đường song đặc trưng để tái tổ hợp tín hiệu tại điểm phản xạ. Hàm pha mã hóa thời gian truyền sóng từ nguồn tới điểm phản xạ rồi trở về mặt đất, còn biên độ hiệu chỉnh độ phân kỳ của chùm tia và suy hao tán xạ.

**Ý nghĩa thực hành:** Mỗi điểm ảnh địa chấn sau migration ứng với một tích phân FIO trên dữ liệu thô, nên độ chính xác của ảnh phụ thuộc trực tiếp vào hàm pha (tức mô hình vận tốc địa chất).

### 2. Xử lý Radar và SAR (Synthetic Aperture Radar)

Radar khẩu độ tổng hợp thu tín hiệu phản xạ từ bề mặt Trái Đất tại nhiều vị trí dọc quỹ đạo vệ tinh rồi tổng hợp thành ảnh độ phân giải cao. Toán tử tái tạo ảnh từ dữ liệu thô là một FIO có hàm pha phụ thuộc khoảng cách giữa vệ tinh và từng điểm mặt đất theo thời gian.

Các đường biên và cấu trúc địa hình (kỳ dị của hàm phản xạ) được khôi phục thông qua FIO; độ sắc nét cũng như độ phân giải theo phương cự ly và phương vị phản ánh trực tiếp cách FIO ánh xạ tập mặt sóng.

### 3. Quang học hình học và thiết kế quang học

Sự truyền ánh sáng qua thấu kính hay gương là mô hình vật lý trực tiếp của FIO, trong đó hàm pha biểu diễn độ lệch pha tích lũy dọc mỗi tia sáng còn biên độ mô tả sự thay đổi cường độ. Trong thiết kế quang học tự do (freeform optics), bài toán dựng mặt thấu kính từ yêu cầu mặt sóng đầu ra chính là bài toán ngược xác định hàm pha phù hợp.

### 4. Lan truyền sóng đàn hồi trong môi trường không đồng nhất

Trong vật liệu composite hay môi trường địa chất có vận tốc biến thiên liên tục, toán tử tiến hóa của phương trình sóng $$ u_{tt} = c(x)^2 \Delta u $$ trong thời gian ngắn có thể xấp xỉ bởi một FIO có hàm pha thỏa phương trình eikonal $$ \lvert \nabla_x \phi\rvert^2 = 1/c(x)^2 $$, làm cơ sở cho nhiều phương pháp tính toán sóng cao tần hiệu quả.

---

## Trực quan hóa bằng Python

### FIO đơn giản: Phép tịnh tiến và biến đổi pha

```python
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Minh họa FIO đơn giản nhất: phép tịnh tiến
# Tu(x) = u(x - a)
# Trong miền Fourier: F[Tu](ξ) = e^{-iaξ} F[u](ξ)
# Phase function: φ(x,ξ) = (x-a)·ξ
# -------------------------------------------------------

N = 512
x = np.linspace(-8, 8, N)
dx = x[1] - x[0]
a = 2.5  # Khoảng tịnh tiến

# Hàm ban đầu có singularity: hàm bước mềm hóa
def u_initial(x, eps=0.1):
    return 0.5 * (1 + np.tanh(x / eps))  # Xấp xỉ hàm bước

u = u_initial(x)

# Áp dụng FIO tịnh tiến qua miền Fourier
freqs = np.fft.fftfreq(N, d=dx)
u_hat = np.fft.fft(u)
# Phase shift: e^{-i * 2π * ξ * a}
phase_shift = np.exp(-1j * 2 * np.pi * freqs * a)
Tu_hat = phase_shift * u_hat
Tu = np.real(np.fft.ifft(Tu_hat))

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# --- Hàm gốc và sau FIO ---
ax = axes[0, 0]
ax.plot(x, u,  'steelblue', linewidth=2, label="u(x) (ban đầu)")
ax.plot(x, Tu, 'crimson',   linewidth=2, label=f"Tu(x) = u(x-{a}) (sau FIO)")
ax.axvline(x=0,  color='steelblue', linestyle='--', alpha=0.5)
ax.axvline(x=a,  color='crimson',   linestyle='--', alpha=0.5, label=f"Singularity dịch sang x={a}")
ax.set_title("FIO tịnh tiến: u(x) → u(x - a)", fontweight='bold')
ax.legend(); ax.grid(alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("Biên độ")

# --- Phase shift trong miền tần số ---
ax = axes[0, 1]
ax.plot(freqs[:N//4], np.angle(phase_shift[:N//4]), 'purple', linewidth=1.5)
ax.set_title(f"Phase của FIO: φ(ξ) = -2π·{a}·ξ", fontweight='bold')
ax.set_xlabel("ξ (tần số)"); ax.set_ylabel("Góc pha (radian)")
ax.grid(alpha=0.3)

# --- FIO với phase bậc hai (thấu kính hội tụ) ---
ax = axes[1, 0]
# "Thấu kính": phase quadratic → hội tụ mặt sóng
focus = 3.0
u_gauss = np.exp(-(x+3)**2 / 0.3)  # Nguồn lệch tâm
freqs = np.fft.fftfreq(N, d=dx)
u_hat = np.fft.fft(u_gauss)
# Phase quadratic trong miền tần số: e^{i π ξ²/focus}
lens_phase = np.exp(1j * np.pi * freqs**2 / focus)
u_focused_hat = lens_phase * u_hat
u_focused = np.real(np.fft.ifft(u_focused_hat))

ax.plot(x, u_gauss,   'steelblue', linewidth=2, label="Trước thấu kính (lệch phải)")
ax.plot(x, u_focused, 'darkorange',linewidth=2, label="Sau FIO thấu kính (hội tụ)")
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5, label="Tiêu điểm x=0")
ax.set_title("FIO với phase bậc hai: thấu kính hội tụ", fontweight='bold')
ax.legend(); ax.grid(alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("Biên độ")

# --- So sánh WF trước và sau FIO ---
ax = axes[1, 1]
# WF của hàm bước tại x=0 → sau tịnh tiến, WF tại x=a
u_step = (x > 0).astype(float)
phi_loc_0 = np.exp(-x**2 / (2 * 0.5**2))        # Cắt quanh x=0
phi_loc_a = np.exp(-(x - a)**2 / (2 * 0.5**2))   # Cắt quanh x=a

spec_0 = np.abs(np.fft.fftshift(np.fft.fft(phi_loc_0 * u_step)))
spec_a_after = np.abs(np.fft.fftshift(np.fft.fft(phi_loc_a * (x > a).astype(float))))
freqs_shift = np.fft.fftshift(freqs)

ax.semilogy(freqs_shift, spec_0 + 1e-10, 'steelblue', linewidth=1.5,
            label="WF tại x=0 (trước)")
ax.semilogy(freqs_shift, spec_a_after + 1e-10, 'crimson', linewidth=1.5,
            label=f"WF tại x={a} (sau FIO)")
ax.set_xlim(-20, 20)
ax.set_title("FIO dịch chuyển Wave Front Set\n(WF: x=0 → x=a)", fontweight='bold')
ax.set_xlabel("ξ (tần số)"); ax.set_ylabel("Phổ Fourier (log scale)")
ax.legend(); ax.grid(alpha=0.3)

plt.suptitle("Fourier Integral Operators: Minh họa tác động lên hàm và Wave Front Set",
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig("FIO_illustration.png", dpi=150)
plt.show()
```

### Mô phỏng tia địa chấn: Hàm pha và đường song đặc trưng

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# -------------------------------------------------------
# Mô phỏng tia địa chấn trong môi trường vận tốc biến đổi
# Phương trình tia (bicharacteristics):
#   dx/dt = ∂p/∂ξ = 2ξ/c(x)²  →  dx/dt = ξ (đơn giản hóa)
#   dξ/dt = -∂p/∂x = ... (gradient của vận tốc)
# -------------------------------------------------------

def c_velocity(x, z):
    """Tốc độ sóng tăng theo độ sâu (mô hình địa chất đơn giản)"""
    return 1.0 + 0.5 * z / 5.0  # Tăng tuyến tính từ 1.0 đến 2.0

# Phương trình tia trong 2D (x nằm ngang, z chiều sâu)
def ray_equations(t, state):
    x, z, px, pz = state
    c = c_velocity(x, z)
    # Hamilton H = c(x,z) * sqrt(px² + pz²)
    # Đơn giản hóa: tia đi theo gradient của 1/c
    dcdx = 0.0  # Vận tốc không phụ thuộc x nằm ngang
    dcdz = 0.5 / 5.0
    p_mag = np.sqrt(px**2 + pz**2) + 1e-10
    # dx/dt = c * px / |p|, dz/dt = c * pz / |p|
    dxdt = c * px / p_mag
    dzdt = c * pz / p_mag
    # dpx/dt = -(1/c) * dc/dx * (incorrect sign - simplified)
    # dpz/dt = -(1/c) * dc/dz
    dpxdt = 0.0
    dpzdt = (1/c) * dcdz  # Tia bẻ cong về phía vận tốc thấp (Snell)
    return [dxdt, dzdt, dpxdt, dpzdt]

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# --- Tia từ nhiều góc phát ---
ax = axes[0]
n_rays = 11
angles = np.linspace(15, 75, n_rays)  # Góc phát (độ so với thẳng đứng)

for angle_deg in angles:
    angle_rad = np.radians(angle_deg)
    px0 = np.sin(angle_rad)
    pz0 = np.cos(angle_rad)
    sol = solve_ivp(ray_equations, [0, 8],
                    [0, 0, px0, pz0],
                    max_step=0.05, dense_output=True)
    x_ray = sol.y[0]
    z_ray = sol.y[1]
    # Chỉ vẽ đến khi tia đạt độ sâu tối đa rồi quay lại
    ax.plot(x_ray, -z_ray, linewidth=1.5, alpha=0.7)

# Thêm mô hình vận tốc nền
z_grid = np.linspace(0, 5, 100)
x_grid = np.linspace(-1, 8, 100)
Z, X = np.meshgrid(z_grid, x_grid)
C = c_velocity(X, Z)
ax.contourf(X, -Z, C, levels=10, cmap='YlOrRd', alpha=0.3)
ax.set_title("Tia địa chấn trong môi trường vận tốc tăng theo độ sâu\n"
             "(Bicharacteristics của symbol chính)", fontweight='bold')
ax.set_xlabel("x (nằm ngang, km)"); ax.set_ylabel("z (chiều sâu, km)")
ax.set_ylim(-5, 0.3)
ax.axhline(0, color='brown', linewidth=2)
ax.text(3, 0.1, "Bề mặt đất (thu nhận dữ liệu)", ha='center')
ax.grid(alpha=0.3)

# --- Phase function dọc tia ---
ax = axes[1]
angle_rad = np.radians(30)
px0, pz0 = np.sin(angle_rad), np.cos(angle_rad)
sol = solve_ivp(ray_equations, [0, 6], [0, 0, px0, pz0],
                max_step=0.02, dense_output=True)
t_vals = sol.t
x_ray, z_ray = sol.y[0], sol.y[1]
# Phase = integral của 1/c along ray (eikonal)
c_along_ray = c_velocity(x_ray, z_ray)
phase = np.cumsum(1.0 / c_along_ray) * np.diff(t_vals, prepend=t_vals[0])
ax.plot(t_vals, phase, 'navy', linewidth=2, label="Phase φ(t) dọc tia")
ax.fill_between(t_vals, 0, phase, alpha=0.2, color='navy')
ax.set_title("Phase function tích lũy dọc theo tia\n"
             "(FIO: amplitude × e^{iφ} tái tổ hợp tín hiệu)", fontweight='bold')
ax.set_xlabel("t (tham số tia)"); ax.set_ylabel("φ(t) (phase tích lũy)")
ax.legend(); ax.grid(alpha=0.3)

plt.suptitle("FIO trong địa chấn học: Tia = Bicharacteristics, Phase = Eikonal",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("FIO_seismic_rays.png", dpi=150)
plt.show()
```

---

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

**Thông điệp chính:** FIO là lớp toán tử đủ tổng quát để dịch chuyển mặt sóng thay vì chỉ lọc tại chỗ như ΨDO.

**Điều cần nhớ:**
- ΨDO: $$Tu(x) = \int e^{ix\cdot\xi} a(x,\xi) \hat{u}(\xi) d\xi$$ ứng với hàm pha đơn giản $$ \phi = x\cdot\xi $$.
- FIO: sử dụng hàm pha tổng quát $$ \phi(x,\xi) $$, làm mặt sóng di chuyển theo cấu trúc hình học.
- Phép tịnh tiến là FIO đơn giản nhất với hàm pha $$ \phi(x,\xi) = (x-a)\cdot\xi $$.

**Bài tập:** Kiểm chứng rằng phép tịnh tiến $$ Tu(x) = u(x-a) $$ là FIO có hàm pha $$ (x-a)\cdot\xi $$, và tính tác động của nó lên tập mặt sóng: kỳ dị tại $$ x_0 $$ dịch chuyển tới $$ x_0 + a $$.

### Mức sau đại học (Graduate)

**Cấu trúc chính tắc:** Hàm pha $$ \phi(x,\xi) $$ xác định một *quan hệ chính tắc* (canonical relation) $$ C \subset T^*X \times T^*Y $$ gồm các cặp $$ (x, d_x\phi; y, -d_y\phi) $$, chi phối cách FIO ánh xạ tập mặt sóng:
$$ WF(Tu) \subset C \circ WF(u). $$

**Phân loại toán tử:**
- ΨDO: quan hệ chính tắc là đường chéo (ánh xạ đồng nhất) nên không dịch chuyển tập mặt sóng.
- FIO tổng quát: quan hệ chính tắc là một phép biến đổi chính tắc (hoặc quan hệ chính tắc) tổng quát.

**Định lý hợp thành:** Nếu $$ A $$ là FIO có quan hệ chính tắc $$ C_A $$ và $$ B $$ là FIO có quan hệ chính tắc $$ C_B $$, thì dưới các điều kiện cắt ngang thích hợp, hợp thành $$ AB $$ cũng là FIO với quan hệ chính tắc $$ C_A \circ C_B $$.

**Ứng dụng trong lý thuyết:** Toán tử tiến hóa của phương trình sóng $$ e^{it\sqrt{-\Delta}} $$ là một FIO có quan hệ chính tắc là *dòng trắc địa* (geodesic flow) — kết nối trực tiếp với giải tích bán cổ điển và hình học phổ.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm | Kết nối với FIO |
|---|---|
| ΨDO (Ch. 14) | ΨDO là trường hợp riêng của FIO với hàm pha tuyến tính |
| Tập mặt sóng (Bài 15.01) | FIO ánh xạ tập mặt sóng theo quan hệ chính tắc của hàm pha |
| Lan truyền kỳ dị (Bài 15.02) | Toán tử tiến hóa của PDE hyperbolic là FIO |
| Phương trình Hamilton–Jacobi (Ch. 10) | Hàm pha thỏa phương trình eikonal $$ \lvert \nabla\phi\rvert^2 = p(x,\xi) $$ |
| Bài toán ngược (Bài 15.06) | Toán tử chiếu ngược trong CT và địa chấn là FIO |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chụp cắt lớp và chiếu ngược
- Bài toán: Toán tử đo kiểu Radon và toán tử tái tạo vận chuyển kỳ dị giữa vật thể và dữ liệu đo.
- Mô hình: Các toán tử này thuộc lớp toán tử tích phân Fourier (FIO), ánh xạ tập mặt sóng theo quan hệ chính tắc.
- Giả thiết và giới hạn: Chất lượng tái tạo phụ thuộc vào hình học đo và độ đầy đủ của góc chiếu.
- Diễn giải: FIO cung cấp ngôn ngữ đúng để mô tả sự dịch chuyển của kỳ dị thay vì chỉ lọc cục bộ.

#### Toán tử tiến hóa của phương trình sóng
- Bài toán: Nghiệm phương trình sóng tại thời điểm $$ t $$ thu được từ dữ liệu ban đầu qua một toán tử lan truyền.
- Mô hình: Toán tử tiến hóa hyperbolic có biểu diễn dạng FIO.
- Giả thiết và giới hạn: Đòi hỏi hàm pha không suy biến.
- Diễn giải: FIO mô tả cách kỳ dị di chuyển dọc theo các phép biến đổi chính tắc.

### 2. Trực giác bổ sung và các kết nối

Toán tử giả vi phân chủ yếu lọc cục bộ theo tần số, còn FIO vận chuyển kỳ dị từ cặp vị trí–hướng này sang cặp vị trí–hướng khác theo luồng hình học. Chính quan hệ chính tắc tạo nên sự khác biệt căn bản giữa FIO và ΨDO.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 600)
u = np.exp(-8 * (x + 1.5)**2) * np.cos(18 * x)
shift = 1.2
Tu = np.exp(-8 * (x - shift + 1.5)**2) * np.cos(18 * (x - shift))

plt.plot(x, u, label="song goi ban dau")
plt.plot(x, Tu, label="sau FIO mo phong su lan truyen")
plt.legend()
plt.title("FIO van chuyen goi song trong khong gian")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Fourier integral operator intuition wave propagation
- search: Radon transform singularities canonical relation
- search: FIO wave packet propagation visualization

### 5. Bài toán mẫu có bối cảnh thực

Toán tử tịnh tiến
$$ (Tu)(x)=u(x-a) $$
là một FIO với hàm pha tuyến tính: nó dịch chuyển mọi kỳ dị từ vị trí $$ x_0 $$ sang $$ x_0+a $$ trong khi giữ nguyên hướng tần số. Đây là ví dụ đơn giản nhất minh họa cách FIO dịch chuyển tập mặt sóng.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm FIO như toán tử vận chuyển điểm kỳ dị.

**Bậc sau đại học.** Kết nối với quan hệ chính tắc, hàm pha không suy biến và định lý ánh xạ tập mặt sóng.

## Video tham khảo

- Nên xem trước: [Introduction to Fourier Integral operators 1 (Allan Greenleaf)](https://www.youtube.com/watch?v=4O_oC9kFFWQ) — Mathematics video VAROQUI Hervé, tiếng Việt. Bài giảng nhập môn của Allan Greenleaf về toán tử tích phân Fourier.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Trình bày cách các toán tử dịch chuyển tập mặt sóng trong bài giảng đầu của András Vasy.
- [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Các phương pháp vi địa phương của Maciej Zworski xây dựng trên lớp toán tử này.
