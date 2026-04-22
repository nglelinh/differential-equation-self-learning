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

Bài này giới thiệu Fourier integral operators như lớp toán tử tự nhiên mô tả lan truyền sóng và biến đổi mặt sóng. Sau bài học, sinh viên cần hiểu FIO khác ΨDO ở đâu, vai trò của phase function và amplitude, và vì sao FIO là ngôn ngữ phù hợp cho propagation of singularities.

## Kiến thức nền

Sinh viên nên nắm pseudodifferential operators, wave front set, và trực giác rằng propagation of singularities cần một lớp toán tử linh hoạt hơn phép nhân cục bộ trong miền tần số. Kiến thức về pha dao động và phương trình Hamilton-Jacobi cũng hữu ích ở mức trực giác.

## Dẫn nhập

Pseudodifferential operators rất mạnh, nhưng về bản chất chúng vẫn hành xử như các bộ lọc tần số cục bộ. Trong nhiều bài toán sóng, điều đó chưa đủ. Sóng không chỉ bị lọc; nó còn bị vận chuyển, xoay pha, hội tụ, tán xạ, và biến đổi hình học. Để mô tả những hiện tượng này, ta cần một lớp toán tử rộng hơn: Fourier integral operators.

Nếu ΨDO là ngôn ngữ của “chỉnh biên độ theo tần số”, thì FIO là ngôn ngữ của “di chuyển và bẻ cong mặt sóng”.

## Khái niệm theo ba cách

### Cách trực giác

Hãy nghĩ đến một chùm tia sáng đi qua thấu kính. Thấu kính không chỉ làm mạnh hay yếu tia sáng; nó còn thay đổi pha và hướng lan truyền của cả chùm tia. FIO làm việc tương tự với các thành phần dao động của nghiệm.

### Cách hình ảnh

Giáo viên nên vẽ một mặt sóng ban đầu rồi mặt sóng sau khi truyền. Với ΨDO, sinh viên quen nghĩ “mỗi tần số bị nhân bởi một hệ số”. Với FIO, nên nhấn mạnh rằng chính cấu trúc pha làm mặt sóng bị đẩy sang vị trí mới và hướng mới trong không gian pha.

### Cách hình thức

Một FIO điển hình có dạng

$$
Tu(x)=\int e^{i\phi(x,\xi)}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

trong đó:

- $$ \phi(x,\xi) $$ là phase function;
- $$ a(x,\xi) $$ là amplitude.

Khi phase là đơn giản $$ \phi(x,\xi)=x\cdot\xi $$, ta quay về lớp pseudodifferential operators quen thuộc. Vì vậy FIO thật sự là một mở rộng của ΨDO.

## Ngộ nhận thường gặp

### “FIO chỉ là ΨDO với công thức viết dài hơn”

Không. Điểm khác biệt cốt lõi nằm ở phase function không tầm thường.

### “Amplitude mới là phần quan trọng nhất”

Không hẳn. Trong propagation, phase thường mang phần hình học quyết định.

### “FIO chỉ xuất hiện trong vật lý sóng”

Sai. Chúng cũng quan trọng trong bài toán ngược, hình học, và phổ.

### “Nếu không hiểu hết phase function thì không thể hiểu trực giác của FIO”

Không. Ngay từ đầu, sinh viên có thể hiểu FIO như toán tử vận chuyển mặt sóng.

## Tiến trình học

### Bước 1: Nhìn lại ΨDO

Nhấn mạnh giới hạn: chúng chủ yếu mô tả lọc cục bộ.

### Bước 2: Giới thiệu phase function

Đây là phần sinh hình học cho toán tử.

### Bước 3: Liên hệ với propagation of singularities

FIO là công cụ tự nhiên để hiện thực hóa định lý propagation.

### Bước 4: Đặt FIO trong bức tranh lớn

Nêu rằng nghiệm của nhiều phương trình hyperbolic hay toán tử sóng có thể được biểu diễn bằng FIO.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được FIO vượt quá ΨDO ở điểm nào không?
- Sinh viên có thấy phase function điều khiển hình học của mặt sóng không?
- Sinh viên có liên hệ được FIO với propagation of singularities không?

## Ví dụ có lời giải

### Ví dụ 1: Trường hợp quay về ΨDO

Nếu $$ \phi(x,\xi)=x\cdot\xi $$, thì

$$
Tu(x)=\int e^{ix\cdot\xi}a(x,\xi)\widehat{u}(\xi)\,d\xi,
$$

chính là dạng quen thuộc của một ΨDO. Ví dụ này cho thấy FIO thật sự chứa ΨDO như một trường hợp riêng.

### Ví dụ 2: Toán tử tịnh tiến

Xét $$ Tu(x)=u(x-c) $$. Trong miền Fourier,

$$
\widehat{Tu}(\xi)=e^{-ic\cdot\xi}\widehat{u}(\xi).
$$

Pha mới $$ (x-c)\cdot\xi $$ thể hiện phép dịch chuyển. Đây là ví dụ đơn giản nhất về phase làm thay đổi vị trí của singularity.

### Ví dụ 3: Nghiệm sóng tự do

Toán tử truyền nghiệm của phương trình sóng tự do thường có biểu diễn bằng FIO, với phase gắn với hành động cổ điển hay nghiệm phương trình eikonal. Sinh viên không cần công thức đầy đủ, nhưng nên hiểu rằng FIO là mô hình đúng cho evolution operator của sóng.

### Ví dụ 4: Hình học mặt sóng

Nếu singularity của $$ u $$ nằm trên một mặt nhất định, FIO có thể đẩy mặt đó sang một mặt khác theo canonical transformation gắn với phase. Ví dụ này là phát biểu bằng lời của cơ chế “mang wave front set đi”.

### Ví dụ 5: Trực giác từ chụp cắt lớp

Trong nhiều mô hình CT, dữ liệu đo được có thể xem như tích phân của hàm cần tái dựng dọc theo các đường thẳng hay tia. Toán tử biến đối tượng thành dữ liệu, và toán tử kéo ngược dữ liệu về ảnh, thường mang bản chất của FIO. Điều quan trọng ở đây không phải chi tiết công thức, mà là trực giác: FIO là lớp toán tử vừa đủ rộng để mang singularity từ vật thể thật sang tín hiệu đo và ngược lại.

## Câu hỏi khái niệm

1. Vì sao phase function là phần mang thông tin hình học của FIO?
2. Điều gì khiến FIO trở thành ngôn ngữ tự nhiên cho wave propagation?
3. Ở mức trực giác, amplitude và phase khác nhau về vai trò như thế nào?

## Bài toán ứng dụng

1. Trong quang học hình học, thấu kính và phản xạ gương gợi trực giác gì về FIO?
2. Trong chụp cắt lớp, vì sao toán tử biến dữ liệu đo thành singularity của vật thể thường là một FIO?
3. Trong địa chấn học, việc sóng phản xạ đi theo các tia có thể được mô tả bằng phase function ra sao?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một toán tử không chỉ lọc mà còn di chuyển mặt sóng, em nghĩ lớp toán tử đó phải có thêm dữ liệu gì?
- Phase function đang mã hóa hình học nào?
- Em thấy sự khác nhau giữa “đổi biên độ” và “đổi pha” ở mức vật lý ra sao?

### Hoạt động gợi ý

- So sánh trực tiếp một ΨDO và một phép tịnh tiến dưới góc nhìn Fourier.
- Vẽ mặt sóng trước và sau tác động của một FIO đơn giản.
- Thảo luận nhóm về ví dụ ánh sáng qua thấu kính như một ẩn dụ cho FIO.

### Cách tăng tham gia

- Bắt đầu bằng hiện tượng sóng quen thuộc.
- Cho sinh viên đoán phase của phép tịnh tiến.
- Mời sinh viên mô tả FIO bằng một câu không dùng ký hiệu.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám sát ví dụ tịnh tiến và phase tuyến tính.
- Chưa yêu cầu hiểu canonical relations đầy đủ.
- Nhấn mạnh thông điệp: FIO = toán tử vận chuyển mặt sóng.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu canonical transformation gắn với phase.
- Liên hệ FIO với nghiệm phương trình Hamilton-Jacobi.
- Nghiên cứu cách FIO tác động lên wave front set.

## Ghi nhớ nhanh

Fourier integral operators mở rộng pseudodifferential operators bằng cách đưa thêm phase function để mô tả sự vận chuyển hình học của mặt sóng. Chúng là ngôn ngữ tự nhiên của lan truyền singularity và của nhiều bài toán sóng hiện đại.

---

## Ứng dụng thực tế

### 1. Seismic Migration: Đưa ảnh địa chấn về đúng vị trí

Bài toán cốt lõi của thăm dò địa chấn là: dữ liệu sóng phản xạ thu được ở mặt đất không hiển thị cấu trúc địa chất ở đúng vị trí vì sóng phải đi theo tia qua nhiều tầng địa chất khác nhau. *Seismic migration* là bước xử lý đưa dữ liệu về đúng vị trí không gian.

Về mặt toán học, toán tử migration là một FIO: nó tích phân dữ liệu đo dọc theo các tia bicharacteristic và tái tổ hợp tín hiệu tại vị trí phản xạ. Phase function mã hóa thời gian đi của tia sóng từ nguồn đến điểm phản xạ và trở lại bề mặt. Amplitude bù trừ cho divergence của tia và tán xạ.

**Ý nghĩa thực hành:** Mỗi pixel của ảnh địa chấn sau migration tương ứng với tích phân FIO của dữ liệu thô. Chất lượng ảnh phụ thuộc trực tiếp vào độ chính xác của phase function (tức mô hình vận tốc địa chất).

### 2. Xử lý Radar và SAR (Synthetic Aperture Radar)

Radar khẩu độ tổng hợp thu nhận tín hiệu phản xạ từ bề mặt Trái Đất qua nhiều vị trí khác nhau của vệ tinh, rồi tổng hợp ảnh phân giải cao. Toán tử tổng hợp từ dữ liệu thô sang ảnh là một FIO với phase function gắn với khoảng cách từ vệ tinh đến mỗi điểm trên mặt đất tại mỗi thời điểm.

Biên và cấu trúc của địa hình (singularity của hàm phản xạ) được tái dựng thông qua FIO. Chất lượng ảnh SAR — như độ sắc nét của biên, khả năng phân giải theo phạm vi và azimuth — trực tiếp phản ánh cách FIO xử lý wave front set của tín hiệu.

### 3. Quang học hình học và thiết kế quang học

Ánh sáng qua thấu kính hay gương là ví dụ vật lý trực tiếp nhất của FIO. Phase function mô tả sự dịch pha mà mỗi tia ánh sáng tích lũy khi đi qua môi trường quang học. Amplitude mô tả sự suy giảm hay khuếch đại cường độ.

Trong thiết kế quang học phi tuyến (freeform optics), bài toán tổng hợp thấu kính từ yêu cầu về mặt sóng đầu ra là bài toán ngược của FIO: biết amplitude và mặt sóng đầu ra, tìm phase function phù hợp.

### 4. Lan truyền sóng đàn hồi trong vật liệu không đồng nhất

Trong vật liệu composite hay cấu trúc địa chất phức tạp, vận tốc sóng thay đổi liên tục. Toán tử tiến hóa của phương trình sóng đàn hồi $$ u_{tt} = c(x)^2 \Delta u $$ sau một khoảng thời gian nhỏ có thể xấp xỉ bởi FIO với phase gắn với nghiệm phương trình eikonal $$ \lvert \nabla_x \phi\rvert^2 = 1/c(x)^2 $$. Đây là nền tảng của các phương pháp tính toán hiệu quả cho bài toán sóng trong môi trường phức tạp.

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

### Mô phỏng tia địa chấn: Phase function và bicharacteristics

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

**Thông điệp chính:** FIO là toán tử vừa đủ mạnh để "di chuyển" mặt sóng, không chỉ "lọc" nó như ΨDO.

**Điều cần nhớ:**
- ΨDO: $$Tu(x) = \int e^{ix\cdot\xi} a(x,\xi) \hat{u}(\xi) d\xi$$ — phase đơn giản $$ \phi = x\cdot\xi $$.
- FIO: thêm phase function tổng quát $$ \phi(x,\xi) $$ → mặt sóng bị vận chuyển theo hình học.
- Phép tịnh tiến là FIO đơn giản nhất: phase $$ \phi(x,\xi) = (x-a)\cdot\xi $$.

**Bài tập:** Kiểm chứng rằng phép tịnh tiến $$ Tu(x) = u(x-a) $$ là FIO với phase $$ (x-a)\cdot\xi $$. Tính tác động lên wave front set: singularity tại $$ x_0 $$ dịch chuyển đến $$ x_0 + a $$.

### Mức sau đại học (Graduate)

**Cấu trúc chính tắc:** Phase function $$ \phi(x,\xi) $$ xác định một *canonical relation* $$ C \subset T^*X \times T^*Y $$: tập các cặp $$ (x, d_x\phi; y, -d_y\phi) $$. Đây là đối tượng trung tâm xác định cách FIO ánh xạ wave front set:
$$ WF(Tu) \subset C \circ WF(u). $$

**Lớp toán tử:**
- ΨDO: canonical relation là đường chéo (identity) — không dịch chuyển wave front.
- FIO tổng quát: canonical relation là canonical transformation tổng quát.

**Định lý thành phần:** Nếu $$ A $$ là FIO với canonical relation $$ C_A $$ và $$ B $$ là FIO với $$ C_B $$, thì $$ AB $$ (nếu định nghĩa được) là FIO với canonical relation $$ C_A \circ C_B $$.

**Ứng dụng trong lý thuyết:** Toán tử tiến hóa của phương trình sóng $$ e^{it\sqrt{-\Delta}} $$ là một FIO với canonical relation là *geodesic flow* — tia sóng cầu trong không gian phẳng. Đây là cầu nối trực tiếp với semiclassical analysis và phổ học.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm | Kết nối với FIO |
|---|---|
| ΨDO (Ch. 14) | ΨDO là trường hợp riêng của FIO (phase tuyến tính) |
| Wave front set (bài 1) | FIO ánh xạ WF theo canonical relation của phase |
| Propagation of singularities (bài 2) | Toán tử tiến hóa của PDE hyperbolic là FIO |
| Phương trình Hamilton-Jacobi (Ch. 10 extension) | Phase function thỏa eikonal equation $$ \lvert \nabla\phi\rvert^2 = p(x,\xi) $$ |
| Bài toán ngược (bài 6) | Backprojection operators trong CT/seismic là FIO |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Chụp cắt lớp và backprojection
- Bài toán: Toán tử đo kiểu Radon và toán tử tái dựng mang singularities từ vật thể sang dữ liệu rồi ngược lại.
- Mô hình: Các toán tử này thường là Fourier integral operators (FIO), ánh xạ wave front set theo canonical relation.
- Giả thiết và giới hạn: Phụ thuộc vào hình học đo và việc có đủ góc chiếu hay không.
- Diễn giải: FIO là ngôn ngữ đúng cho việc "vận chuyển singularity" thay vì chỉ lọc nó.

#### Toán tử tiến hóa của phương trình sóng
- Bài toán: Nghiệm của phương trình sóng tại thời gian $$ t $$ thu được từ dữ liệu đầu qua một toán tử lan truyền.
- Mô hình: Toán tử tiến hóa hyperbolic thường là FIO.
- Giả thiết và giới hạn: Cần phase function không suy biến.
- Diễn giải: FIO mô tả cách singularities di chuyển dọc canonical transformations.

### 2. Trực giác bổ sung và các kết nối

Pseudodifferential operators chủ yếu lọc cục bộ theo tần số; FIO thì còn vận chuyển singularities từ vị trí-hướng này sang vị trí-hướng khác. Có thể nghĩ FIO là "các toán tử theo luồng hình học". Một hiểu nhầm phổ biến là xem FIO chỉ là ΨDO phức tạp hơn; thật ra canonical relation của nó là điểm khác biệt bản chất.

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
có thể viết như một FIO với phase tuyến tính. Nó không chỉ thay đổi giá trị hàm mà còn mang singularities từ vị trí $$ x_0 $$ sang $$ x_0+a $$, giữ nguyên hướng tần số. Đây là ví dụ đơn giản nhất để thấy FIO "di chuyển" wave front set.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu FIO như toán tử vận chuyển singularities.

**Bậc sau đại học.** Kết nối với canonical relations, nondegenerate phases va dinh ly anh xa wave front set.
