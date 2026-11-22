---
layout: post
title: "Lan Truyền Kỳ Dị"
chapter: '15'
order: 2
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: required
---

![Lan truyền singularity dọc theo đặc tuyến của PDE]({{ site.imgurl }}/chapter_img/chapter15/02_propagation_singularities.svg )

## Mục tiêu

Bài học này giới thiệu một trong những định lý nền tảng nhất của giải tích vi địa phương: điểm kỳ dị không lan truyền ngẫu nhiên mà di chuyển theo cấu trúc hình học của phương trình. Sau bài học, sinh viên cần nắm trực giác của sự lan truyền kỳ dị, vai trò của đường đặc trưng và đường song đặc trưng (bicharacteristics), đồng thời phân biệt rõ cách phương trình hyperbolic và phương trình elliptic xử lý điểm kỳ dị.

## Kiến thức nền

Sinh viên nên nắm vững tập mặt sóng (wave front set), ký hiệu chính của toán tử và phương pháp đường đặc trưng trong phương trình sóng hoặc phương trình đối lưu. Cần nhớ lại rằng dữ liệu ban đầu có kỳ dị của phương trình sóng thường tạo ra mặt sóng lan truyền rõ rệt thay vì bị làm trơn ngay lập tức.

## Dẫn nhập

Một kết quả cốt lõi của giải tích vi địa phương là điểm kỳ dị có quỹ đạo xác định. Khi nghiệm của một PDE chứa kỳ dị, kỳ dị đó không biến mất hay phân tán hỗn loạn mà di chuyển dọc theo các đường quỹ đạo quyết định bởi ký hiệu chính của toán tử. Đây là phiên bản sắc nét hơn nhiều của trực giác “sóng truyền theo đường đặc trưng”.

Kết quả này vừa sâu sắc về mặt lý thuyết vừa giàu ứng dụng thực tiễn, làm nền tảng cho phân tích truyền sóng, bài toán ngược, quang học hình học và chụp cắt lớp.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng khi ném một viên đá xuống mặt hồ yên tĩnh: các gợn sóng không xuất hiện hỗn độn khắp nơi mà lan tỏa theo những mặt sóng có cấu trúc xác định. Nếu vị trí ném là điểm kỳ dị ban đầu, thì hình học môi trường và phương trình chi phối sẽ quyết định gợn sóng đi về đâu. Định lý lan truyền kỳ dị chính là phiên bản vi địa phương của hiện tượng đó.

### Cách hình ảnh

Có thể vẽ một điểm kỳ dị ban đầu rồi phác thảo hai nhánh lan truyền theo thời gian của phương trình sóng một chiều: một nhánh đi sang trái, một nhánh đi sang phải. Sau đó, nâng hình ảnh này lên không gian pha bằng cách gắn thêm hướng tần số: các đường song đặc trưng (bicharacteristics) chính là các quỹ đạo trong không gian pha chứ không chỉ nằm trong không gian vị trí.

### Cách hình thức

Với toán tử kiểu chính thực (real principal type) $$ P $$ có ký hiệu chính $$ p(x,\xi) $$, các kỳ dị của nghiệm $$ u $$ của phương trình $$ Pu=f $$ nằm trên tập đặc trưng $$ \{(x,\xi):p(x,\xi)=0\} $$ (ngoài phần kỳ dị của $$ f $$) và lan truyền dọc theo dòng Hamilton của $$ p $$, tức các đường song đặc trưng. Nói ngắn gọn:

- kỳ dị của vế phải $$ f $$ có thể sinh ra kỳ dị cho $$ u $$;
- ngoài các nguồn đó, kỳ dị của $$ u $$ di chuyển dọc theo dòng Hamilton của ký hiệu chính.

## Ngộ nhận thường gặp

### “Kỳ dị chỉ lan truyền theo vị trí, không cần xét hướng”

Sai. Hướng trong không gian pha là thành phần quyết định trong phát biểu của định lý.

### “Mọi PDE đều lan truyền kỳ dị”

Không đúng. Các toán tử elliptic làm trơn kỳ dị thay vì truyền chúng đi.

### “Đường đặc trưng và đường song đặc trưng là một”

Chúng liên hệ mật thiết với nhau, nhưng đường song đặc trưng sống trong không gian pha nên mang thêm thông tin về hướng tần số.

### “Nếu dữ liệu đầu trơn thì nghiệm luôn trơn mọi nơi”

Không nhất thiết đúng trong mọi bài toán biên hay bài toán phi tuyến, nhưng với phương trình hyperbolic tuyến tính hệ số trơn trên không gian không biên, kỳ dị mới không tự phát sinh nếu không có nguồn hoặc dữ liệu kỳ dị ban đầu.

## So sánh ba lớp phương trình

Có thể đặt cạnh nhau ba cơ chế điển hình của PDE:

- phương trình elliptic: không lan truyền kỳ dị mà có xu hướng làm trơn;
- phương trình parabolic: làm trơn theo thời gian, dập tắt rất nhanh các thành phần cao tần;
- phương trình hyperbolic: vận chuyển kỳ dị dọc theo các quỹ đạo hình học xác định.

Vì vậy, hiện tượng lan truyền kỳ dị gắn liền trước hết với lớp phương trình hyperbolic hoặc kiểu chính thực, chứ không áp dụng đồng loạt cho mọi PDE.

## Tiến trình học

### Bước 1: Ôn lại phương trình sóng

Củng cố trực giác rằng điểm kỳ dị di chuyển dọc theo các tia sóng.

### Bước 2: Chuyển từ đường đặc trưng sang không gian pha

Đưa vào ký hiệu chính và dòng Hamilton tương ứng.

### Bước 3: Nắm phát biểu định lý ở mức ý tưởng

Tập trung vào cơ chế hình học của sự lan truyền trước khi đi vào chi tiết chứng minh.

### Bước 4: Đối chiếu với hiệu ứng làm trơn elliptic

So sánh hai cơ chế trái ngược để thấy rõ vai trò của giải tích vi địa phương.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao cần xét đường song đặc trưng thay vì chỉ đường đặc trưng hay không?
- Sinh viên có phân biệt được cơ chế lan truyền của phương trình hyperbolic với cơ chế làm trơn của phương trình elliptic hay không?
- Sinh viên có hiểu vai trò của ký hiệu chính trong việc xác định quỹ đạo của kỳ dị hay không?

## Ví dụ có lời giải

### Ví dụ 1: Phương trình đối lưu

Xét $$ u_t+cu_x=0 $$ với nghiệm $$ u(x,t)=u_0(x-ct) $$. Nếu dữ liệu ban đầu $$ u_0 $$ có bước nhảy, bước nhảy đó tịnh tiến nguyên vẹn với vận tốc $$ c $$. Đây là ví dụ rõ ràng nhất về kỳ dị lan truyền theo đường đặc trưng.

### Ví dụ 2: Phương trình sóng một chiều

Với phương trình sóng, một kỳ dị ở dữ liệu ban đầu tách thành hai nhánh chạy sang trái và sang phải. Kết quả này khớp hoàn toàn với công thức d'Alembert và là minh họa cơ bản cho sự lan truyền kỳ dị.

### Ví dụ 3: Đối chiếu với toán tử elliptic

Với phương trình $$ -\Delta u=f $$, nếu $$ f $$ trơn cục bộ thì nghiệm $$ u $$ cũng trơn hơn, không có kỳ dị nào di chuyển dọc theo quỹ đạo. Ví dụ này nhấn mạnh rằng lan truyền kỳ dị là đặc trưng của phương trình hyperbolic chứ không phải của mọi PDE.

### Ví dụ 4: Hình học Hamilton

Với ký hiệu chính $$ p(x,\xi) $$, trường vectơ Hamilton $$ H_p $$ mô tả sự tiến hóa đồng thời của cả vị trí và tần số — phiên bản tổng quát của tia sáng trong quang học hình học. Đây chính là cấu trúc hình học trung tâm của định lý lan truyền.

### Ví dụ 5: Phương trình nhiệt như phản ví dụ

Với phương trình nhiệt, dữ liệu ban đầu có điểm gãy hay bước nhảy sẽ trở nên trơn ngay khi $$ t>0 $$. Điều này cho thấy không phải mọi phương trình tiến hóa đều vận chuyển kỳ dị; một số cơ chế như khuếch tán sẽ lập tức dập tắt kỳ dị.

## Câu hỏi khái niệm

1. Vì sao sự lan truyền kỳ dị phải được phát biểu trong không gian pha thay vì chỉ trong không gian vật lý?
2. Điều gì giúp ký hiệu chính đủ để xác định quỹ đạo của điểm kỳ dị?
3. Vì sao phương trình elliptic không lan truyền kỳ dị giống như phương trình hyperbolic?

## Bài toán ứng dụng

1. Trong địa chấn học, vì sao kỳ dị của sóng phản xạ mang thông tin về cấu trúc dưới lòng đất?
2. Trong siêu âm y khoa, định lý lan truyền kỳ dị hỗ trợ việc tái tạo biên cơ quan như thế nào?
3. Trong quang học hình học, các tia sáng liên hệ ra sao với khái niệm đường song đặc trưng?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Nếu dữ liệu ban đầu có một bước nhảy, ta kỳ vọng bước nhảy đó biến mất, đứng yên hay di chuyển theo thời gian?
- Vì sao hướng của kỳ dị phải được theo dõi xuyên suốt quá trình lan truyền?
- Khi nâng bài toán từ không gian vị trí lên không gian pha, ta thu thêm thông tin gì?

### Hoạt động gợi ý

- Theo dõi quỹ đạo một điểm nhảy của phương trình đối lưu trên mặt phẳng không gian–thời gian.
- Đặt cạnh nhau mô phỏng phương trình sóng và mô phỏng làm trơn của phương trình nhiệt.
- Thảo luận nhóm về cách xem đường song đặc trưng như “đường đi của thông tin kỳ dị”.

### Cách tăng mức độ tham gia

- Mở đầu bằng các hiện tượng quen thuộc như sóng nước hoặc sóng âm.
- Đề nghị sinh viên dự đoán quỹ đạo kỳ dị trước khi phát biểu định lý.
- Yêu cầu diễn đạt “sự lan truyền kỳ dị” bằng ngôn ngữ vật lý trước khi chuyển sang hình thức vi địa phương.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung trước vào phương trình đối lưu và phương trình sóng một chiều.
- Giảm bớt ký hiệu hình thức của trường Hamilton trong lần tiếp cận đầu.
- Nhấn mạnh thông điệp cốt lõi: kỳ dị di chuyển dọc theo hình học của phương trình.

### Thử thách cho sinh viên khá giỏi

- Viết tường minh trường vectơ Hamilton từ ký hiệu chính.
- Liên hệ đường song đặc trưng với dòng trắc địa (geodesic flow) trên đa tạp Riemann.
- Đọc phát biểu đầy đủ của định lý Hörmander về lan truyền kỳ dị.

## Ghi nhớ nhanh

Định lý lan truyền kỳ dị khẳng định rằng kỳ dị của nghiệm PDE hyperbolic không phân tán ngẫu nhiên mà di chuyển dọc theo các đường song đặc trưng của ký hiệu chính, tạo nên cầu nối trực tiếp giữa hình học phương trình và cấu trúc nghiệm.

---

## Ứng dụng thực tế

### 1. Địa chấn học: Tia sóng phản xạ và phương pháp migration

Trong thăm dò địa chấn, sóng đàn hồi được phát xuống lòng đất và các cảm biến bề mặt ghi lại sóng phản xạ từ các ranh giới địa tầng nhằm tái tạo vị trí và hình dạng của chúng.

Các ranh giới địa tầng là điểm kỳ dị của vận tốc sóng đàn hồi $$ c(x) $$. Phương trình sóng $$ u_{tt} - c(x)^2 \Delta u = 0 $$ có ký hiệu chính $$p(x,\xi,\tau) = \tau^2 - c(x)^2 \lvert \xi\rvert^2$$. Các đường song đặc trưng của $$ p $$ chính là các tia địa chấn tuân theo định luật khúc xạ Snell, và định lý lan truyền kỳ dị khẳng định kỳ dị của nghiệm di chuyển đúng dọc theo những tia này.

**Ứng dụng thực hành:** Các thuật toán *Kirchhoff migration* và *reverse time migration (RTM)* thực chất ánh xạ kỳ dị từ miền dữ liệu đo (bề mặt và thời gian) về không gian vật lý bằng cách truy ngược dọc theo các đường song đặc trưng.

**Giới hạn:** Mô hình lý tưởng giả định môi trường địa chất trơn theo từng lớp; thực tế có thể xuất hiện tán xạ phức tạp.

### 2. Siêu âm y khoa và chụp ảnh đàn hồi (Ultrasound Elastography)

Trong siêu âm y khoa, sóng âm tần số cao truyền qua mô mềm và phản xạ tại ranh giới giữa mô lành và khối u — nơi mật độ và độ đàn hồi thay đổi đột ngột. Tập mặt sóng của tín hiệu phản xạ lưu giữ thông tin về vị trí và hướng của ranh giới đó.

**Mô hình:** Với môi trường có mật độ $$ \rho(x) $$ và vận tốc âm $$ c(x) $$:
$$
\rho(x) u_{tt} = \nabla \cdot (\rho(x) c(x)^2 \nabla u).
$$
Kỳ dị của $$ \rho(x) $$ và $$ c(x) $$ tại biên khối u sinh ra kỳ dị trong nghiệm, từ đó tập mặt sóng của tín hiệu thu được phản ánh trực tiếp hình dạng biên khối u.

### 3. Quang học hình học và thiết kế quang học

Quang học hình học cổ điển — với các tia sáng tuân theo nguyên lý Fermat — là giới hạn bước sóng ngắn ($$ \lambda \to 0 $$) của hệ phương trình sóng Maxwell. Trong bối cảnh này, định lý lan truyền kỳ dị phát biểu chính xác rằng mặt sóng và biên bóng di chuyển dọc theo tia sáng.

Trong thiết kế kính thiên văn, kính hiển vi và hệ quang học laser, việc kiểm soát biên sắc nét của chùm sáng là cơ sở để phân tích quang sai (aberration) và giới hạn độ phân giải.

### 4. Cơ học lượng tử: Giới hạn bán cổ điển (Semiclassical Limit)

Trong cơ học lượng tử, hàm sóng $$ \psi $$ thỏa phương trình Schrödinger:
$$
i\hbar \psi_t = -\frac{\hbar^2}{2m}\Delta \psi + V(x)\psi.
$$
Khi $$ \hbar \to 0 $$, kỳ dị và các gói sóng tập trung lan truyền dọc theo quỹ đạo cổ điển của hạt trong thế năng $$ V(x) $$ — chính là các đường song đặc trưng của ký hiệu chính. Đây là nền tảng trực tiếp của giải tích bán cổ điển ở Bài 15.04.

---

## Trực quan hóa bằng Python

### Mô phỏng lan truyền kỳ dị: Phương trình đối lưu 1D

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------------------------------
# Phương trình đối lưu: u_t + c u_x = 0
# Nghiệm: u(x,t) = u0(x - ct)
# Singularity tại x=0 (điểm nhảy của u0) di chuyển với vận tốc c
# -------------------------------------------------------

N = 500
x = np.linspace(-5, 5, N)
c = 1.5  # Vận tốc đối lưu
t_values = np.linspace(0, 4, 8)  # Các thời điểm hiển thị

# Dữ liệu ban đầu: hàm bước (singularity tại x=0)
def u0_step(x):
    return (x > 0).astype(float)

# Dữ liệu ban đầu: hàm trơn (không singularity)
def u0_smooth(x):
    return np.exp(-x**2)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

colors = plt.cm.viridis(np.linspace(0, 1, len(t_values)))

for ax, u0_func, title in zip(axes,
                               [u0_step, u0_smooth],
                               ["Dữ liệu ban đầu: Hàm bước (có singularity tại x=0)",
                                "Dữ liệu ban đầu: Hàm trơn (không singularity)"]):
    for t, col in zip(t_values, colors):
        u = u0_func(x - c * t)
        alpha = 0.4 + 0.6 * (t / t_values[-1])
        ax.plot(x, u, color=col, linewidth=2, alpha=alpha,
                label=f"t = {t:.1f}" if t in [0, 1, 2, 3, 4] else "")

    # Đánh dấu quỹ đạo singularity (đường đặc tuyến)
    if u0_func == u0_step:
        for t in t_values:
            ax.axvline(x=c * t, color='red', alpha=0.3, linewidth=1, linestyle='--')
        ax.plot([], [], 'r--', linewidth=1, alpha=0.6, label="Đặc tuyến (singularity)")

    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("u(x, t)", fontsize=12)
    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.set_xlim(-5, 5); ax.set_ylim(-0.2, 1.4)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

plt.suptitle("Lan truyền singularity trong phương trình đối lưu u_t + 1.5·u_x = 0\n"
             "Singularity di chuyển theo đặc tuyến x = c·t (đường đỏ)",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("propagation_advection.png", dpi=150)
plt.show()
```

### Phương trình sóng 1D: Kỳ dị tách thành hai nhánh

```python
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Phương trình sóng: u_tt - c² u_xx = 0
# d'Alembert: u(x,t) = (1/2)[u0(x+ct) + u0(x-ct)] + (1/2c) ∫ v0 ds
# Singularity ban đầu → tách thành hai nhánh truyền ngược chiều
# -------------------------------------------------------

N = 1000
x = np.linspace(-8, 8, N)
c = 1.0

# Dữ liệu ban đầu: hàm bước tại x=0
def u0(x):
    return (x > 0).astype(float)

def v0(x):
    return np.zeros_like(x)  # Vận tốc ban đầu = 0

def dalembert(x, t, c, u0_func, v0_func):
    """d'Alembert solution (v0=0 case): u = (u0(x+ct) + u0(x-ct))/2"""
    return 0.5 * (u0_func(x + c * t) + u0_func(x - c * t))

t_values = [0, 1, 2, 3, 4]
fig, axes = plt.subplots(len(t_values), 1, figsize=(12, 10), sharex=True)

for ax, t in zip(axes, t_values):
    u = dalembert(x, t, c, u0, v0)
    ax.plot(x, u, 'steelblue', linewidth=2, label=f"t = {t}")
    # Đánh dấu hai singularity
    ax.axvline(x= c * t, color='red',   linestyle='--', alpha=0.7,
               label=f"Sóng phải: x = +{c*t:.0f}")
    ax.axvline(x=-c * t, color='green', linestyle='--', alpha=0.7,
               label=f"Sóng trái: x = -{c*t:.0f}")
    ax.set_ylabel("u(x,t)", fontsize=10)
    ax.legend(fontsize=9, loc='upper right')
    ax.set_ylim(-0.2, 1.3)
    ax.grid(True, alpha=0.3)

axes[-1].set_xlabel("x", fontsize=12)
fig.suptitle("Phương trình sóng: Một singularity ban đầu tách thành hai\n"
             "(sóng trái: đặc tuyến x = -ct | sóng phải: đặc tuyến x = +ct)",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("wave_singularity_split.png", dpi=150)
plt.show()
```

### So sánh Hyperbolic và Parabolic: Lan truyền và làm trơn

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

N = 500
x = np.linspace(-5, 5, N)
dx = x[1] - x[0]

# Singularity ban đầu: hàm bước
u0 = (x > 0).astype(float)

t_values = [0, 0.5, 1.0, 2.0]
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Hyperbolic (đối lưu): singularity giữ nguyên, chỉ dịch chuyển ---
ax = axes[0]
for t, col in zip(t_values, ['black', 'steelblue', 'orange', 'red']):
    c = 1.0
    u_hyp = (x - c * t > 0).astype(float)
    ax.plot(x, u_hyp, color=col, linewidth=2, label=f"t = {t}", alpha=0.8)
ax.set_title("Hyperbolic (đối lưu u_t + u_x = 0)\nSingularity lan — không bị làm mịn",
             fontsize=10, fontweight='bold')
ax.set_xlabel("x"); ax.set_ylabel("u(x,t)")
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5); ax.set_ylim(-0.2, 1.4)

# --- Parabolic (nhiệt): singularity bị xóa mịn ---
ax = axes[1]
for t, col in zip(t_values, ['black', 'steelblue', 'orange', 'red']):
    sigma = np.sqrt(2 * t) / dx if t > 0 else 0
    if sigma > 0:
        u_par = gaussian_filter1d(u0, sigma=sigma)
    else:
        u_par = u0.copy()
    ax.plot(x, u_par, color=col, linewidth=2, label=f"t = {t}", alpha=0.8)
ax.set_title("Parabolic (nhiệt u_t = u_xx)\nSingularity bị làm mịn ngay lập tức",
             fontsize=10, fontweight='bold')
ax.set_xlabel("x"); ax.set_ylabel("u(x,t)")
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xlim(-5, 5); ax.set_ylim(-0.2, 1.4)

plt.suptitle("Hyperbolic vs Parabolic: Hai cơ chế xử lý singularity hoàn toàn khác nhau",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("hyperbolic_vs_parabolic.png", dpi=150)
plt.show()
```

---

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

**Thông điệp chính:** Các điểm kỳ dị không tự biến mất hay xuất hiện tùy tiện mà di chuyển có quy luật dọc theo các đường đặc trưng của phương trình.

**Những điều cần nhớ:**
- Phương trình đối lưu $$ u_t + cu_x = 0 $$: kỳ dị di chuyển theo $$ x = x_0 + ct $$.
- Phương trình sóng $$ u_{tt} - c^2 u_{xx} = 0 $$: một kỳ dị ban đầu tách thành hai nhánh chạy với vận tốc $$ \pm c $$.
- Phương trình nhiệt: làm trơn kỳ dị ngay lập tức thay vì lan truyền.

**Thực hành:** Viết nghiệm d'Alembert và xác định vị trí các điểm kỳ dị theo thời gian, đồng thời giải thích vai trò của họ đường đặc trưng $$ x \pm ct = \text{const} $$.

### Mức sau đại học (Graduate)

**Định lý Hörmander (1971):** Với toán tử $$ P $$ kiểu chính thực (real principal type), nếu $$ Pu = f $$ và $$ (x_0, \xi_0) \notin WF(f) $$, thì tập mặt sóng của $$ u $$ trên tập đặc trưng $$ \{p = 0\} $$ bất biến dưới dòng Hamilton của $$ p $$:
$$
H_p = \sum_j \left(\frac{\partial p}{\partial \xi_j} \partial_{x_j} - \frac{\partial p}{\partial x_j} \partial_{\xi_j}\right).
$$
Nói cách khác, nếu $$ (x_0, \xi_0) \in WF(u) $$ và $$ p(x_0, \xi_0) = 0 $$, thì toàn bộ đường song đặc trưng đi qua $$ (x_0, \xi_0) $$ đều thuộc $$ WF(u) $$ (chừng nào chưa gặp tập mặt sóng của $$ f $$).

**Hệ quả quan trọng:**
- Toán tử elliptic không có đường song đặc trưng thực nên không lan truyền kỳ dị.
- Toán tử sóng $$ \Box = \partial_t^2 - c^2\Delta $$ thuộc lớp kiểu chính thực nên định lý áp dụng đầy đủ.
- Đây là nền tảng giải tích cho các phương pháp tái tạo ảnh hiện đại.

**Kết nối với cơ học Hamilton:** Hệ phương trình song đặc trưng
$$
\dot{x}_j = \frac{\partial p}{\partial \xi_j}, \qquad \dot{\xi}_j = -\frac{\partial p}{\partial x_j}
$$
chính là hệ phương trình chính tắc Hamilton của hạt cổ điển với hàm Hamilton $$ p(x,\xi) $$, phản ánh sự tương ứng hạt–sóng trong giải tích vi địa phương.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm đã học | Kết nối |
|---|---|
| Đường đặc trưng (Ch. 9, 10) | Đường song đặc trưng là bước nâng đường đặc trưng lên không gian pha |
| Tập mặt sóng (Bài 15.01) | Tập mặt sóng là đối tượng lan truyền dọc theo đường song đặc trưng |
| Phương trình sóng (Ch. 10) | Ví dụ tiêu biểu nhất của sự lan truyền kỳ dị |
| Phương trình nhiệt (Ch. 9) | Phản ví dụ: làm trơn thay vì lan truyền |
| Bài toán ngược (Bài 15.06) | Từ tập mặt sóng dữ liệu đo suy ngược tập mặt sóng của cấu trúc cần tìm |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Sóng địa chấn
- Bài toán: Các mặt gián đoạn trong lòng đất tạo ra kỳ dị lan truyền dọc theo tia sóng.
- Mô hình: Với toán tử hyperbolic kiểu chính thực, $$ WF(u) $$ lan truyền dọc theo các đường song đặc trưng của ký hiệu chính.
- Giả thiết và giới hạn: Mô hình tuyến tính, hệ số đủ trơn và bỏ qua tán xạ phi tuyến mạnh.
- Diễn giải: Điểm kỳ dị không lan ngẫu nhiên mà tuân theo hình học Hamilton.

#### Siêu âm và radar
- Bài toán: Xung ngắn truyền qua môi trường, phản xạ và mang về thông tin kỳ dị của vật cản.
- Mô hình: Kỳ dị của nghiệm phương trình sóng di chuyển dọc theo các đường song đặc trưng trong không gian pha.
- Giả thiết và giới hạn: Đòi hỏi tính khả kiến đủ tốt; nhiễu đo có thể che lấp chi tiết.
- Diễn giải: Biết quỹ đạo lan truyền kỳ dị giúp xác định chính xác vùng dữ liệu chứa thông tin cần khai thác.

### 2. Trực giác bổ sung và các kết nối

Trong phương trình sóng, các góc nhọn và mặt gián đoạn không bị san phẳng tức thời như trong phương trình nhiệt mà di chuyển theo đường đặc trưng và đường song đặc trưng. Phát biểu đầy đủ phải đặt trong không gian pha vì hướng lan truyền giữ vai trò thiết yếu.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
t = np.linspace(0, 1.5, 240)
X, T = np.meshgrid(x, t)
c = 1.0
u = (X - c * T > 0).astype(float)

plt.figure(figsize=(7, 4))
plt.contourf(X, T, u, levels=[-0.1, 0.5, 1.1], cmap="coolwarm")
plt.plot(c * t, t, "k--", label="duong dac tuyen x = ct")
plt.xlabel("x")
plt.ylabel("t")
plt.title("Mat nhay lan truyen theo dac tuyen")
plt.legend()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: propagation of singularities wave equation animation
- search: bicharacteristics intuition microlocal analysis
- search: seismic ray tracing singularity propagation

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Lan truyền singularity theo tia" description="Kéo nguồn phát, thay đổi thời gian và vận tốc để quan sát singularity lan theo họ tia và phản xạ trên biên." path="interactives/chapter15/propagation-singularities-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Với phương trình vận chuyển
$$ u_t + c u_x = 0, \qquad u(x,0)=H(x), $$
nghiệm là
$$ u(x,t)=H(x-ct). $$
Mặt nhảy ban đầu tại $$ x=0 $$ dịch chuyển thành mặt nhảy tại $$ x=ct $$. Đây là mô hình đơn giản nhất minh họa định lý lan truyền kỳ dị.

### 6. Phân tầng độ khó

**Bậc đại học.** Theo dõi chuyển động kỳ dị bằng đường đặc trưng trong các bài toán một chiều.

**Bậc sau đại học.** Kết nối với trường vectơ Hamilton, toán tử kiểu chính thực và định lý lan truyền kỳ dị của Hörmander.

## Video tham khảo

- Nên xem trước: [Andras Vasy - Microlocal analysis and wave propagation (Part 2)](https://www.youtube.com/watch?v=3DN6bKJnlXc) — Institut Fourier, tiếng Anh. Bài giảng của András Vasy về sự lan truyền kỳ dị của toán tử không elliptic, đặc biệt là phương trình sóng.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 4)](https://www.youtube.com/watch?v=mqRbYzxLTHM) — Institut Fourier, tiếng Anh. Phần 4 của loạt bài, bàn về lan truyền toàn cục và các ứng dụng.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Trường hợp elliptic nơi kỳ dị không lan truyền, dùng để đối chiếu.
