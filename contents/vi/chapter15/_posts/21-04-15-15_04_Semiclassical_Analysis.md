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

## Mục tiêu

Bài optional này giới thiệu giải tích bán cổ điển như chiếc cầu giữa tần số cao, PDE, và cơ học cổ điển. Sau bài học, sinh viên cần hiểu ý nghĩa của tham số nhỏ $$ h $$, biết tại sao giới hạn $$ h\to 0 $$ quan trọng, và thấy được mối liên hệ giữa quỹ đạo cổ điển, wave packets, và toán tử Schrödinger.

## Kiến thức nền

Sinh viên nên nắm Fourier transform, pseudodifferential operators, Hamiltonian mechanics ở mức trực giác, và phương trình Schrödinger cơ bản. Kiến thức về phổ và wave front set cũng rất hữu ích để hiểu tại sao tham số nhỏ dẫn đến một thang nhìn mới.

## Dẫn nhập

Giải tích bán cổ điển nghiên cứu điều gì xảy ra khi một tham số nhỏ, thường ký hiệu $$ h $$ hay $$ \hbar $$, tiến về 0. Trong vật lý, đây là giới hạn từ lượng tử về cổ điển. Trong phân tích, đây cũng là cách nghiên cứu tần số rất cao hay bước sóng rất nhỏ. Vì vậy giải tích bán cổ điển là điểm gặp nhau của PDE, phổ, và động lực học Hamilton.

Một trong những nét đẹp của lý thuyết này là nó biến những câu hỏi tưởng rất khác nhau thành cùng một ngôn ngữ: localization của nghiệm, quỹ đạo cổ điển, và sự phân bố phổ cao.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một gói sóng ngày càng hẹp. Khi bước sóng rất nhỏ so với kích thước miền quan sát, sóng bắt đầu cư xử như hạt đi theo quỹ đạo cổ điển. Giải tích bán cổ điển nghiên cứu chính vùng chuyển tiếp này: vẫn là sóng, nhưng đã lộ ra cấu trúc của động lực học cổ điển.

### Cách hình ảnh

Giáo viên nên vẽ ba hình:

- một sóng trải rộng;
- một wave packet hẹp;
- quỹ đạo cổ điển mà tâm gói sóng đi theo.

Hình này rất hiệu quả vì nó cho sinh viên thấy tại sao một tham số nhỏ lại làm xuất hiện quỹ đạo thay vì chỉ các dao động mơ hồ.

### Cách hình thức

Ta xét các họ toán tử phụ thuộc tham số nhỏ $$ h $$, điển hình là $$ P_h=-h^2\Delta+V(x) $$. Khi $$ h\to 0 $$, toán tử này được phân tích thông qua symbol semiclassical $$ p(x,\xi)=\lvert \xi\rvert^2+V(x) $$. Đây đồng thời là Hamiltonian cổ điển của hệ. Nhờ đó, các hiện tượng lượng tử cao tần được đọc qua hình học cổ điển trong không gian pha.

## Ngộ nhận thường gặp

### “Giải tích bán cổ điển chỉ là vật lý lượng tử”

Không. Trong phân tích, nó cũng là lý thuyết tần số cao rất mạnh.

### “Cho $$ h\to 0 $$ thì sóng biến mất và chỉ còn hạt”

Không hoàn toàn. Sóng vẫn hiện diện, nhưng cấu trúc của chúng phản ánh mạnh động lực học cổ điển.

### “Giải tích bán cổ điển chỉ là thay biến ký hiệu”

Sai. Việc đưa vào tham số nhỏ tạo ra một calculus, một trực giác, và nhiều kết quả phổ mới.

### “Quỹ đạo cổ điển tự động cho đầy đủ hành vi lượng tử”

Không. Giới hạn cổ điển cho trực giác mạnh, nhưng vẫn còn nhiều hiệu ứng lượng tử tinh vi.

## Tiến trình học

### Bước 1: Giới thiệu tham số nhỏ

Sinh viên cần hiểu $$ h $$ không chỉ là một hằng số mà là một thang đo mới.

### Bước 2: Chuyển toán tử sang symbol semiclassical

Liên hệ với Hamiltonian cổ điển.

### Bước 3: Giới thiệu wave packets

Đây là cầu nối trực quan nhất giữa sóng và quỹ đạo.

### Bước 4: Kết nối với phổ và cơ học lượng tử

Nêu rằng nhiều bài toán phổ lớn được đọc lại thành bài toán semiclassical.

### Ghi chú sư phạm then chốt

Ở bài này, sinh viên thường bị “rơi chữ” vì có quá nhiều tầng ngôn ngữ cùng lúc: sóng, hạt, phổ, và quỹ đạo Hamilton. Một mẹo dạy rất hiệu quả là luôn quay lại một tam giác trực giác:

- $$ h $$ nhỏ nghĩa là bước sóng nhỏ;
- bước sóng nhỏ nghĩa là nghiệm tập trung mạnh trong không gian pha;
- khi tập trung mạnh, quỹ đạo cổ điển bắt đầu lộ ra.

Nếu sinh viên nắm được tam giác này, phần formalism phía sau sẽ dễ tiếp nhận hơn nhiều.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao $$ h\to 0 $$ là giới hạn tần số cao không?
- Sinh viên có hiểu symbol semiclassical liên hệ với Hamiltonian cổ điển thế nào không?
- Sinh viên có mô tả được vai trò của wave packet không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử Schrödinger tự do

Xét $$ P_h=-h^2\Delta $$. Symbol semiclassical là $$ p(x,\xi)=\lvert \xi\rvert^2 $$. Đây cũng là năng lượng động học cổ điển. Ví dụ này cho thấy ngay sự trùng khớp giữa toán tử lượng tử và Hamiltonian cổ điển.

### Ví dụ 2: Thêm thế năng

Với $$ P_h=-h^2\Delta+V(x) $$, symbol trở thành $$ \lvert \xi\rvert^2+V(x) $$. Đây là Hamiltonian quen thuộc của cơ học cổ điển. Nhờ đó, quỹ đạo cổ điển xuất hiện tự nhiên trong phân tích nghiệm của PDE.

### Ví dụ 3: Wave packet

Một gói sóng hẹp trong không gian pha thường di chuyển gần theo dòng Hamilton của symbol trong khoảng thời gian thích hợp. Đây là trực giác cốt lõi của tương ứng cổ điển-lượng tử.

### Ví dụ 4: Phổ cao

Bài toán trị riêng lớn cho $$ -\Delta $$ có thể được đọc như bài toán semiclassical bằng cách đặt $$ h\sim \lambda^{-1/2} $$. Ví dụ này giải thích vì sao semiclassical analysis gắn chặt với spectral asymptotics.

### Ví dụ 5: Ansatz WKB

Một ansatz kinh điển là tìm nghiệm dưới dạng $$ u_h(x)\approx a(x)e^{iS(x)/h} $$. Ở đây, $$ S(x) $$ đóng vai trò pha cổ điển còn $$ a(x) $$ là biên độ chậm. Khi thay vào phương trình, bậc đầu tiên thường dẫn đến phương trình Hamilton-Jacobi cho $$ S $$. Ví dụ này rất quan trọng về mặt sư phạm vì nó cho sinh viên thấy “quỹ đạo cổ điển” không phải được gắn từ bên ngoài vào, mà tự sinh ra từ phép thế của nghiệm cao tần.

## Câu hỏi khái niệm

1. Vì sao giới hạn $$ h\to 0 $$ lại là giới hạn tần số cao?
2. Điều gì làm cho symbol semiclassical đóng vai trò của Hamiltonian cổ điển?
3. Tại sao wave packets là đối tượng trực giác quan trọng trong semiclassical analysis?

## Bài toán ứng dụng

1. Trong cơ học lượng tử, vì sao quỹ đạo cổ điển vẫn xuất hiện trong giới hạn năng lượng cao?
2. Trong quang học hình học, bước sóng nhỏ gợi liên hệ gì với semiclassical analysis?
3. Trong spectral theory, tại sao đếm trị riêng lớn có thể được chuyển thành một bài toán semiclassical?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Khi bước sóng rất nhỏ, em mong đợi sóng cư xử giống cái gì?
- Tại sao một tham số nhỏ có thể thay đổi hoàn toàn góc nhìn phân tích?
- Em thấy mối liên hệ giữa Hamiltonian cổ điển và toán tử lượng tử ở đâu?

### Hoạt động gợi ý

- Vẽ quỹ đạo cổ điển và đường đi gần đúng của một wave packet.
- So sánh toán tử Schrödinger với Hamiltonian cổ điển tương ứng.
- Tổ chức thảo luận nhóm: semiclassical là “giới hạn lượng tử” hay “giới hạn cao tần”?

### Cách tăng tham gia

- Bắt đầu từ hình ảnh gói sóng hẹp.
- Cho sinh viên tự đoán symbol semiclassical của các toán tử đơn giản.
- Mời sinh viên giải thích semiclassical bằng ngôn ngữ vật lý trước rồi mới quay về PDE.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám vào ví dụ $$ -h^2\Delta+V(x) $$.
- Tránh đi sâu vào calculus semiclassical đầy đủ.
- Nhấn mạnh một dòng chủ đạo: $$ h $$ nhỏ làm sóng lộ ra quỹ đạo cổ điển.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu semiclassical wave front set.
- Liên hệ với định lý Egorov ở mức trực giác.
- Khảo sát mối liên hệ giữa WKB và phương trình Hamilton-Jacobi.

## Ghi nhớ nhanh

Giải tích bán cổ điển nghiên cứu PDE khi có một tham số nhỏ $$ h $$, qua đó nối cấu trúc sóng của nghiệm với động lực học cổ điển trong không gian pha. Đây là chiếc cầu mạnh giữa phân tích Fourier, phổ, và cơ học lượng tử.

---

## Ứng dụng thực tế

### 1. Cơ học lượng tử: Nguyên lý tương ứng Bohr

Nguyên lý tương ứng của Bohr phát biểu rằng cơ học lượng tử phải trở về cơ học cổ điển trong giới hạn tác dụng lớn ($$ \hbar \to 0 $$ theo thang vĩ mô). Giải tích bán cổ điển là phát biểu toán học chính xác của nguyên lý này.

Với phương trình Schrödinger không phụ thuộc thời gian:
$$ -\frac{\hbar^2}{2m}\Delta\psi + V(x)\psi = E\psi, $$
đặt $$ h = \hbar $$ và tìm nghiệm dạng WKB:
$$ \psi_h(x) \approx A(x) e^{iS(x)/h}, $$
thì bậc đầu của phương trình cho phương trình Hamilton-Jacobi:
$$ \frac{\lvert \nabla S\rvert^2}{2m} + V(x) = E. $$
Đây chính là phương trình mô tả quỹ đạo cổ điển của hạt với năng lượng $$ E $$ trong thế năng $$ V(x) $$.

**Ứng dụng:** Tính xác suất xuyên hầm (quantum tunneling) qua rào thế, hiệu ứng được ứng dụng trong đèn LED, laser bán dẫn, và kính hiển vi xuyên hầm (STM).

### 2. Quang học: Từ sóng điện từ đến tia sáng

Phương trình sóng Maxwell:
$$
\frac{\partial^2 \mathbf{E}}{\partial t^2} = c^2 \Delta \mathbf{E}
$$
trong môi trường không đồng nhất với chiết suất $$ n(x) $$ có tham số nhỏ tự nhiên là tỷ lệ $$ \lambda/L $$ (bước sóng so với kích thước vật lý quan trọng). Khi $$ \lambda/L \to 0 $$, nghiệm sóng điện từ tập trung dọc theo tia sáng — chính là bicharacteristics của phương trình eikonal:
$$ \lvert \nabla S\rvert^2 = n(x)^2. $$
Đây là nền tảng của quang học hình học và thiết kế các hệ thống quang học từ kính thiên văn Hubble đến hệ thống lithography trong sản xuất chip.

### 3. Địa chấn học tần số cao

Trong thăm dò địa chấn, sóng địa chấn tần số cao (chu kỳ $$ T \ll $$ kích thước cấu trúc địa chất) truyền gần đúng theo các tia ray. Tham số nhỏ ở đây là $$ h \sim T/T_{\rm geol} $$. Phân tích semiclassical giải thích tại sao ray theory hiệu quả ở tần số cao và khi nào nó phá vỡ (gần caustic, nơi nhiều tia giao nhau).

### 4. Vật lý laser và quang học lượng tử

Trong cavity laser, ánh sáng bị giữ trong buồng cộng hưởng. Mode của laser là trị riêng của toán tử Maxwell trong buồng cộng hưởng. Semiclassical analysis dự đoán tần số của mode qua quỹ đạo ánh sáng trong buồng — đây là cơ sở của laser Fabry-Pérot và nhiều cấu trúc quang học hiện đại.

---

## Trực quan hóa bằng Python

### Wave packet và sự hội tụ về quỹ đạo cổ điển khi h → 0

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

### WKB approximation: Xuyên hầm lượng tử

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

**Thông điệp chính:** Khi bước sóng nhỏ, sóng "cư xử như hạt". Semiclassical analysis là cách đo lường chính xác sự chuyển tiếp đó.

**Điều cần nhớ:**
- Tham số $$ h $$ đo tỷ lệ giữa bước sóng và kích thước đặc trưng của bài toán.
- Ansatz WKB: $$ \psi_h \approx A(x) e^{iS(x)/h} $$ — pha dao động nhanh, biên độ chậm.
- Symbol semiclassical $$ p(x,\xi) = \lvert \xi\rvert^2 + V(x) $$ là Hamiltonian cổ điển.
- Quỹ đạo cổ điển xuất hiện như "đường đi" của wave packet khi $$ h \to 0 $$.

**Bài tập:** Với thế năng điều hòa $$ V(x) = x^2/2 $$, tìm pha WKB $$ S(x) $$ thỏa phương trình Hamilton-Jacobi. Giải thích kết quả theo quỹ đạo cổ điển.

### Mức sau đại học (Graduate)

**Calculus semiclassical:** Tập hợp các toán tử $$ {Op_h(a) : a \in S^m} $$ với quantization
$$
Op_h(a) u(x) = \frac{1}{(2\pi h)^n} \int e^{i(x-y)\cdot\xi/h} a\left(\frac{x+y}{2}, \xi\right) u(y)\, dy\, d\xi
$$
tạo thành một algebra với phép nhân thỏa:
$$
Op_h(a) \circ Op_h(b) = Op_h(a \# b),
\qquad a \# b = ab + \frac{h}{2i}\{a, b\} + O(h^2),
$$
trong đó $$\{a,b\} = \nabla_\xi a \cdot \nabla_x b - \nabla_x a \cdot \nabla_\xi b$$ là bracket Poisson.

**Định lý Egorov:** Nếu $$ \Phi_t $$ là dòng Hamilton của $$ p $$, thì
$$
e^{itP_h/h} \circ Op_h(a) \circ e^{-itP_h/h} = Op_h(a \circ \Phi_t) + O(h),
$$
tức toán tử tiến hóa biến đổi observable theo dòng cổ điển. Đây là phát biểu toán học của nguyên lý tương ứng.

**Liên kết với FIO:** Toán tử tiến hóa $$ e^{-itP_h/h} $$ chính là một FIO, với phase là hàm hành động Hamilton-Jacobi.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm | Kết nối |
|---|---|
| WKB (Ch. 6 mở rộng) | Ansatz WKB là trường hợp riêng của phân tích semiclassical |
| Phương trình Hamilton-Jacobi | Phase WKB thỏa phương trình Hamilton-Jacobi |
| FIO (bài 3) | Toán tử tiến hóa semiclassical là FIO |
| Spectral asymptotics (bài 5) | Trị riêng cao ↔ tham số semiclassical nhỏ |
| Cơ học lượng tử (bài 7) | Nguyên lý tương ứng là nội dung của định lý Egorov |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quang học hình học
- Bài toán: Khi bước sóng rất nhỏ, ánh sáng lan gần như theo tia và phản xạ/khúc xạ theo luật cổ điển.
- Mô hình: Dùng tham số nhỏ $$ h $$ trong ansatz WKB
$$ u_h(x)\approx a(x)e^{i\phi(x)/h}. $$
- Giả thiết và giới hạn: Mô hình tần số cao; thất bại gần caustics hoặc turning points.
- Diễn giải: Semiclassical analysis nối trực tiếp PDE với quỹ đạo Hamilton cổ điển.

#### Cơ học lượng tử bán cổ điển
- Bài toán: Xem trạng thái lượng tử tập trung như thế nào quanh quỹ đạo cổ điển khi $$ h \to 0 $$.
- Mô hình: Nghiên cứu toán tử semiclassical và wave packets.
- Giả thiết và giới hạn: Chỉ đúng trong chế độ Planck nhỏ và thời gian thích hợp.
- Diễn giải: Đây là hình thức toán học của nguyên lý tương ứng.

### 2. Trực giác bổ sung và các kết nối

Semiclassical analysis hỏi điều gì xảy ra khi tần số rất cao hoặc khi tham số lượng tử $$ h $$ rất nhỏ. Khi đó một nghiệm vừa dao động nhanh vừa bị điều chế chậm bởi biên độ. Một bẫy phổ biến là chỉ xem $$ h $$ như tham số trang trí; thực ra toàn bộ cấu trúc scale của bài toán phụ thuộc vào nó.

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

Với phương trình Schrödinger tự do semiclassical
$$ ih \partial_t u_h = -\frac{h^2}{2}\Delta u_h, $$
một wave packet ban đầu tập trung quanh $$ (x_0,\xi_0) $$ sẽ di chuyển gần theo quỹ đạo cổ điển
$$ \dot x = \xi, \qquad \dot \xi = 0. $$
Đây là phát biểu cơ bản cho thấy động lực học lượng tử tiến gần động lực học cổ điển khi $$ h $$ nhỏ.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu ansatz WKB và trực giác sóng ngắn.

**Bậc sau đại học.** Kết nối với semiclassical pseudodifferential calculus, Egorov va semiclassical measures.
