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

Bài này giới thiệu một trong những định lý đẹp nhất của vi địa phương: singularity không lan truyền ngẫu nhiên mà đi theo hình học của phương trình. Sau bài học, sinh viên cần hiểu trực giác của propagation of singularities, vai trò của đặc tuyến và bicharacteristics, và vì sao phương trình hyperbolic khác hẳn phương trình elliptic ở cách xử lý kỳ dị.

## Kiến thức nền

Sinh viên nên nắm wave front set, symbol chính của toán tử, và đặc tuyến trong phương trình sóng hay đối lưu. Cũng nên nhớ từ các chương PDE rằng dữ liệu ban đầu của phương trình sóng thường tạo nên mặt lan truyền rõ rệt thay vì bị làm mượt ngay.

## Dẫn nhập

Một trong những thành quả lớn của microlocal analysis là phát hiện rằng kỳ dị có quỹ đạo. Nếu một nghiệm PDE có singularity, kỳ dị ấy không biến mất hoặc lan ra hỗn loạn; nó đi theo những đường được quyết định bởi symbol chính của toán tử. Đây là phiên bản tinh hơn rất nhiều của trực giác “sóng truyền theo đặc tuyến”.

Điều này không chỉ đẹp về mặt khái niệm mà còn cực kỳ thực dụng. Nó là nền cho phân tích sóng, bài toán ngược, quang hình học, và cả nhiều kết quả về chụp cắt lớp.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng bạn ném một hòn đá vào mặt hồ. Gợn sóng không xuất hiện đồng đều khắp nơi mà lan theo những mặt sóng có cấu trúc. Nếu điểm ném là singularity ban đầu, thì hình học mặt hồ và phương trình điều khiển sẽ xác định gợn đi đâu. Propagation of singularities là phiên bản vi địa phương của câu chuyện đó.

### Cách hình ảnh

Giáo viên nên vẽ một điểm kỳ dị ban đầu rồi các đường lan ra theo thời gian đối với phương trình sóng một chiều: một nhánh đi sang trái, một nhánh đi sang phải. Sau đó nâng hình ảnh lên không gian pha bằng cách gắn thêm hướng tần số. Bicharacteristics lúc này là các quỹ đạo trong không gian pha chứ không chỉ trong không gian vật lý.

### Cách hình thức

Với toán tử principal type $$ P $$ có symbol chính $$ p(x,\xi) $$, các singularity của nghiệm $$ u $$ của phương trình $$ Pu=f $$ được điều khiển bởi tập đặc trưng $$ \{(x,\xi):p(x,\xi)=0\} $$ và lan truyền dọc theo dòng Hamilton của $$ p $$, tức các bicharacteristics. Nói ngắn gọn:

- singularity của $$ f $$ có thể tạo singularity cho $$ u $$;
- ngoài những nguồn đó, kỳ dị của $$ u $$ di chuyển theo dòng Hamilton của symbol chính.

## Ngộ nhận thường gặp

### “Singularity chỉ lan theo vị trí, không cần hướng”

Sai. Hướng trong không gian pha là phần quyết định của định lý.

### “Mọi PDE đều lan truyền singularity”

Không. Elliptic operators thường làm mượt kỳ dị thay vì lan truyền chúng.

### “Đặc tuyến và bicharacteristics là cùng một thứ”

Chúng liên quan chặt chẽ nhưng bicharacteristics sống trong không gian pha, nên giàu thông tin hơn.

### “Nếu dữ liệu đầu trơn thì nghiệm luôn trơn mọi nơi”

Chưa chắc trong mọi bối cảnh, nhưng với nhiều bài hyperbolic, singularity mới không tự sinh ra nếu không có nguồn hay điều kiện biên gây ra.

## So sánh ba lớp phương trình

Một cách rất hiệu quả để sinh viên nhớ bài này là đặt cạnh nhau ba cơ chế lớn:

- phương trình elliptic: không “chở” singularity mà có xu hướng làm mịn;
- phương trình parabolic: làm mượt theo thời gian, thường dập tắt cao tần rất nhanh;
- phương trình hyperbolic: vận chuyển singularity dọc theo các quỹ đạo hình học.

Chính vì vậy, khi nghe cụm propagation of singularities, sinh viên nên tự động nghĩ đến lớp hyperbolic hoặc principal type hơn là nghĩ chung cho mọi PDE.

## Tiến trình học

### Bước 1: Nhắc lại wave equation

Sinh viên thường đã có trực giác rằng kỳ dị đi theo tia sóng.

### Bước 2: Chuyển từ đặc tuyến sang không gian pha

Đưa vào symbol chính và dòng Hamilton.

### Bước 3: Nêu định lý ở mức ý tưởng

Không cần chứng minh đầy đủ, mà nhấn mạnh cơ chế hình học.

### Bước 4: So sánh với elliptic smoothing

Đây là lúc thấy vì sao microlocal analysis quan trọng.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao cần bicharacteristics không?
- Sinh viên có phân biệt được lan truyền của hyperbolic với làm mịn của elliptic không?
- Sinh viên có hiểu vai trò của symbol chính trong việc định tuyến singularity không?

## Ví dụ có lời giải

### Ví dụ 1: Phương trình đối lưu

Xét $$ u_t+cu_x=0 $$. Nghiệm có dạng $$ u(x,t)=u_0(x-ct) $$. Nếu dữ liệu đầu $$ u_0 $$ có một điểm nhảy, điểm nhảy ấy chỉ đơn giản bị tịnh tiến theo tốc độ $$ c $$. Đây là ví dụ rõ nhất rằng singularity lan theo đặc tuyến.

### Ví dụ 2: Phương trình sóng một chiều

Với phương trình sóng, dữ liệu kỳ dị ban đầu thường tách thành hai nhánh, một chạy sang trái và một chạy sang phải. Điều này khớp với phân tích d'Alembert quen thuộc và là hình ảnh đầu tiên của propagation of singularities.

### Ví dụ 3: So sánh với elliptic

Nếu $$ -\Delta u=f $$, thì với $$ f $$ trơn cục bộ, nghiệm $$ u $$ trơn hơn. Không có chuyện singularity “di chuyển” dọc theo đường nào cả. Ví dụ này giúp sinh viên thấy propagation là bản chất của hyperbolic, không phải của mọi PDE.

### Ví dụ 4: Hình học Hamilton

Với symbol chính $$ p(x,\xi) $$, trường Hamilton xác định bởi $$ H_p $$ cho biết chuyển động đồng thời của vị trí và tần số. Đây là phiên bản tổng quát của “tia sáng” trong quang hình học. Dù chưa cần tính chi tiết, sinh viên nên thấy đây là cấu trúc hình học trung tâm của định lý.

### Ví dụ 5: Phương trình nhiệt như phản ví dụ

Với phương trình nhiệt, một dữ liệu ban đầu có điểm nhọn thường trở nên trơn ngay khi $$ t>0 $$. Đây là phản ví dụ khái niệm rất tốt cho propagation of singularities: không phải cứ có PDE tiến hóa là sẽ có singularity di chuyển dọc theo quỹ đạo; đôi khi singularity bị dập tắt thay vì được chuyên chở.

## Câu hỏi khái niệm

1. Vì sao propagation of singularities là một mệnh đề về không gian pha chứ không chỉ về không gian vật lý?
2. Điều gì làm cho symbol chính đủ để quyết định quỹ đạo của kỳ dị?
3. Tại sao phương trình elliptic không lan truyền singularity theo cách hyperbolic làm?

## Bài toán ứng dụng

1. Trong địa chấn học, vì sao singularity của sóng phản xạ mang thông tin về cấu trúc dưới lòng đất?
2. Trong siêu âm y khoa, lan truyền kỳ dị giúp tái dựng biên của cơ quan như thế nào?
3. Trong quang học hình học, các tia sáng có thể được hiểu như phiên bản cổ điển của bicharacteristics ra sao?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một điểm nhảy xuất hiện ở dữ liệu ban đầu, em mong nó biến mất, đứng yên, hay di chuyển?
- Tại sao hướng của singularity phải được mang theo trong quá trình truyền?
- Em thấy điều gì thay đổi khi chuyển từ vị trí sang không gian pha?

### Hoạt động gợi ý

- Cho sinh viên theo dõi một singularity của phương trình đối lưu trên đồ thị.
- So sánh hình động của phương trình sóng với hình động làm mượt của phương trình nhiệt.
- Tổ chức thảo luận nhóm về cách đọc quỹ đạo bicharacteristic như “đường đi của thông tin”.

### Cách tăng tham gia

- Bắt đầu từ ví dụ thực như sóng nước hay sóng âm.
- Cho sinh viên đoán quỹ đạo singularity trước khi nêu định lý.
- Yêu cầu giải thích “lan truyền kỳ dị” bằng ngôn ngữ vật lý trước rồi mới quay về vi địa phương.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám chặt vào phương trình đối lưu và phương trình sóng một chiều.
- Giảm lượng ký hiệu Hamiltonian trong lượt đầu.
- Nhấn mạnh thông điệp: kỳ dị đi theo hình học của phương trình.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu biểu thức trường Hamilton từ symbol chính.
- Liên hệ bicharacteristics với geodesic flow trong hình học.
- Đọc phát biểu chính xác hơn của định lý Hörmander.

## Ghi nhớ nhanh

Propagation of singularities nói rằng kỳ dị của nghiệm PDE hyperbolic không lan ngẫu nhiên mà đi theo bicharacteristics của symbol chính. Đây là cầu nối mạnh nhất giữa hình học của phương trình và cấu trúc của nghiệm.

---

## Ứng dụng thực tế

### 1. Địa chấn học: Tia sóng phản xạ và phương pháp migration

Trong thăm dò địa chấn, các kỹ sư bắn sóng đàn hồi xuống lòng đất và ghi lại sóng phản xạ từ các ranh giới địa tầng. Bài toán là: từ dữ liệu bề mặt, tái dựng vị trí và hình dạng các ranh giới đó.

Ranh giới địa tầng là singularity của hệ số đàn hồi $$ c(x) $$. Phương trình sóng đàn hồi $$ u_{tt} - c(x)^2 \Delta u = 0 $$ có symbol chính $$p(x,\xi,\tau) = \tau^2 - c(x)^2 \lvert \xi\rvert^2$$. Các bicharacteristics của $$ p $$ chính là các tia địa chấn quen thuộc, tuân theo định luật Snell khi qua ranh giới. Định lý lan truyền kỳ dị nói rằng singularity của nghiệm đi đúng theo các tia này.

**Ứng dụng thực hành:** Thuật toán *Kirchhoff migration* và *reverse time migration (RTM)* bản chất là đưa singularity từ không gian đo (bề mặt, thời gian) về không gian vật lý bằng cách theo ngược bicharacteristics.

**Giới hạn:** Mô hình giả định môi trường địa chất trơn theo từng lớp; trong thực tế có nhiều tán xạ phức tạp.

### 2. Siêu âm y khoa và chụp ảnh đàn hồi (Ultrasound Elastography)

Bác sĩ dùng siêu âm để phát hiện khối u trong mô mềm. Sóng âm tần số cao chiếu qua mô, phản xạ tại ranh giới giữa mô lành và mô bệnh (nơi mật độ và độ đàn hồi thay đổi đột ngột — singularity). Wave front của sóng phản xạ mang thông tin về vị trí và hướng của ranh giới.

**Mô hình:** Với môi trường có mật độ $$ \rho(x) $$ và tốc độ âm $$ c(x) $$:
$$
\rho(x) u_{tt} = \nabla \cdot (\rho(x) c(x)^2 \nabla u).
$$
Singularity của $$ \rho(x) $$ và $$ c(x) $$ tại biên khối u → singularity của nghiệm → wave front set của tín hiệu thu được chứa thông tin biên khối u.

### 3. Quang học hình học và thiết kế quang học

Quang học hình học cổ điển — với các tia sáng tuân theo Fermat — là giới hạn tần số cao ($$ \lambda \to 0 $$) của phương trình sóng Maxwell. Propagation of singularities trong bối cảnh này chính xác là phát biểu rằng kỳ dị (mặt sóng, bờ bóng) di chuyển theo tia sáng.

Trong thiết kế kính thiên văn, kính hiển vi, hay hệ thống laser, hiểu biên sắc nét của chùm sáng (singularity theo hướng vuông góc với mặt sóng) là cốt lõi của tính toán aberration và độ phân giải quang học.

### 4. Cơ học lượng tử: Giới hạn hình học (Semiclassical Limit)

Trong cơ học lượng tử, hàm sóng $$ \psi $$ thỏa phương trình Schrödinger:
$$
i\hbar \psi_t = -\frac{\hbar^2}{2m}\Delta \psi + V(x)\psi.
$$
Khi $$ \hbar \to 0 $$, singularity của hàm sóng lan theo các quỹ đạo cổ điển của hạt trong thế năng $$ V(x) $$ — chính là bicharacteristics của symbol chính. Đây là nền tảng của semiclassical analysis (bài 4 chương này).

---

## Trực quan hóa bằng Python

### Mô phỏng lan truyền singularity: Phương trình đối lưu 1D

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

### Phương trình sóng 1D: Singularity tách thành hai nhánh

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

### So sánh Hyperbolic vs Parabolic: Lan truyền vs Làm mịn

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

**Thông điệp chính:** Singularity không tự biến mất hay xuất hiện ngẫu nhiên. Chúng di chuyển có trật tự theo đặc tuyến của phương trình.

**Những điều cần nhớ:**
- Phương trình đối lưu $$ u_t + cu_x = 0 $$: singularity đi theo $$ x = x_0 + ct $$.
- Phương trình sóng $$ u_{tt} - c^2 u_{xx} = 0 $$: một singularity ban đầu tách thành hai nhánh chạy tốc độ $$ \pm c $$.
- Phương trình nhiệt: làm mịn singularity chứ không lan truyền.

**Thực hành:** Viết nghiệm d'Alembert và xác định vị trí singularity theo thời gian. Giải thích tại sao đặc tuyến $$ x \pm ct = \text{const} $$ là "đường đời" của singularity.

### Mức sau đại học (Graduate)

**Định lý Hörmander (1971):** Với toán tử $$ P $$ thuộc lớp principal type thực (real principal type), nếu $$ Pu = f $$ và $$ (x_0, \xi_0) \notin WF(f) $$, thì wave front set của $$ u $$ trên tập đặc trưng $$ \{p = 0\} $$ là bất biến dưới dòng Hamilton của $$ p $$:
$$
H_p = \sum_j \left(\frac{\partial p}{\partial \xi_j} \partial_{x_j} - \frac{\partial p}{\partial x_j} \partial_{\xi_j}\right).
$$
Nói khác đi, nếu $$ (x_0, \xi_0) \in WF(u) $$ và $$ p(x_0, \xi_0) = 0 $$, thì toàn bộ bicharacteristic đi qua $$ (x_0, \xi_0) $$ phải thuộc $$ WF(u) $$ (trừ khi bị "chặn" bởi WF của $$ f $$).

**Hệ quả quan trọng:**
- Elliptic operators không có bicharacteristics thực nên không lan truyền singularity.
- Toán tử sóng $$ \Box = \partial_t^2 - c^2\Delta $$ là real principal type, do đó định lý áp dụng đầy đủ.
- Đây là nền tảng lý luận cho các phương pháp imaging hiện đại.

**Kết nối với Hamilton cơ học:** Hệ phương trình bicharacteristic
$$
\dot{x}_j = \frac{\partial p}{\partial \xi_j}, \qquad \dot{\xi}_j = -\frac{\partial p}{\partial x_j}
$$
chính là phương trình Hamilton của hạt cổ điển với Hamiltonian $$ p(x,\xi) $$. Propagation of singularities là phiên bản vi địa phương (quantum → classical limit) của sự tương ứng hạt-sóng.

---

## Liên kết với các khái niệm trong khóa học

| Khái niệm đã học | Kết nối |
|---|---|
| Đặc tuyến (Ch. 9, 10) | Bicharacteristics là nâng của đặc tuyến lên không gian pha |
| Wave front set (bài 1) | WF là đối tượng được lan truyền theo bicharacteristics |
| Phương trình sóng (Ch. 10) | Ví dụ chuẩn nhất của propagation of singularities |
| Phương trình nhiệt (Ch. 9) | Phản ví dụ: smoothing thay vì propagation |
| Bài toán ngược (bài 6) | Biết WF của dữ liệu đo → suy ngược WF của cấu trúc cần tìm |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Sóng địa chấn
- Bài toán: Các discontinuity của môi trường sinh ra singularities lan dọc theo tia sóng.
- Mô hình: Với toán tử hyperbolic chính tắc, $$ WF(u) $$ lan truyền theo bicharacteristics của symbol chính.
- Giả thiết và giới hạn: Mô hình tuyến tính, hệ số trơn vừa đủ, không xét tán xạ mạnh phi tuyến.
- Diễn giải: Singularities không xuất hiện ngẫu nhiên, mà di chuyển theo hình học Hamilton.

#### Siêu âm và radar
- Bài toán: Xung ngắn đi qua môi trường, phản xạ và mang về các singularity của vật cản.
- Mô hình: Singularities của nghiệm phương trình sóng truyền dọc đặc tuyến trong không gian pha.
- Giả thiết và giới hạn: Cần visibility đủ tốt; nhiễu đo có thể làm mờ thông tin.
- Diễn giải: Nếu biết quỹ đạo truyền singularity, ta biết nên tìm thông tin ở đâu trong dữ liệu.

### 2. Trực giác bổ sung và các kết nối

Trong phương trình sóng, các góc nhọn và mặt gián đoạn không tan biến ngay như ở phương trình nhiệt. Chúng di chuyển dọc theo đặc tuyến hoặc bicharacteristics. Một bẫy phổ biến là nghĩ singularity lan chỉ trong không gian vật lý; thực ra phát biểu đúng sống trong phase space vì hướng truyền là thiết yếu.

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
Mặt nhảy ban đầu tại $$ x=0 $$ di chuyển thành mặt nhảy $$ x=ct $$. Đây là mô hình đơn giản nhất của propagation of singularities.

### 6. Phân tầng độ khó

**Bậc đại học.** Theo dõi singularities bằng đặc tuyến trong các bài toán 1D.

**Bậc sau đại học.** Kết nối với Hamilton vector field, principal type operators và dinh ly propagation cua Hormander.
