---
layout: post
title: "Tập Hợp Mặt Sóng (Wave Front Set)"
chapter: '15'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: required
---

![Wave front set như mô tả vị trí và hướng của singularity]({{ site.imgurl }}/chapter_img/chapter15/01_wave_front_sets.svg )

## Mục tiêu

Bài học này mở đầu chương vi địa phương bằng khái niệm quan trọng nhất: tập hợp mặt sóng. Sau bài học, sinh viên cần hiểu tại sao singular support là chưa đủ, vì sao wave front set phải chứa cả thông tin về vị trí lẫn hướng tần số, và cách định nghĩa này trở thành công cụ trung tâm để theo dõi kỳ dị trong PDE hiện đại.

## Kiến thức nền

Sinh viên nên nắm phân phối, biến đổi Fourier, hàm cắt trơn, singular support, và trực giác rằng một hàm có thể trơn theo một số hướng nhưng không trơn theo các hướng khác. Các ý này được ôn lại trong Bài 15.00. Cũng nên nhớ rằng trong các chương trước, regularity chủ yếu được hỏi theo vị trí; ở đây ta hỏi tinh hơn: theo vị trí và theo hướng trong không gian đối ngẫu.

## Dẫn nhập

Nếu chỉ dùng singular support, ta biết một phân phối không trơn ở đâu, nhưng chưa biết nó không trơn theo hướng nào. Thông tin “hướng” này nghe có vẻ phụ, nhưng thực ra lại quyết định cách kỳ dị lan truyền dưới tác động của PDE. Một góc nhọn, một cạnh, hay một nguồn điểm có thể sống ở cùng một vị trí nhưng mang cấu trúc tần số rất khác nhau.

Wave front set ra đời để ghi lại đúng điều còn thiếu đó. Nó cho ta một bản đồ của singularity không chỉ trong không gian vị trí, mà trong không gian pha cục bộ, nơi mỗi điểm được gắn thêm các hướng tần số khả nghi.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng ánh sáng chiếu lên một vật thể có cạnh sắc. Nếu chỉ biết “cạnh ở đâu” thì chưa đủ để dự đoán bóng đổ hay phản xạ; ta còn cần biết cạnh đó hướng theo chiều nào. Wave front set làm việc tương tự với kỳ dị: nó không chỉ đánh dấu chỗ nào “xấu” mà còn nói kỳ dị ấy biểu lộ theo những hướng tần số nào.

### Cách hình ảnh

Giáo viên nên vẽ ba ví dụ:

- một hàm trơn, không có hướng kỳ dị nào;
- delta Dirac tại 0, kỳ dị theo mọi hướng;
- một hàm bậc thang theo biến $$ x_1 $$, kỳ dị chỉ theo các hướng pháp tuyến với mặt nhảy.

Hình ảnh này rất mạnh vì nó cho thấy cùng là “không trơn”, nhưng cấu trúc vi địa phương có thể rất khác. Nên minh họa bằng một điểm $$ x_0 $$ trong không gian và một nón hướng $$ \xi $$ trong không gian tần số.

### Cách hình thức

Với $$ u\in \mathcal{D}'(\Omega) $$, ta nói cặp $$ (x_0,\xi_0)\notin WF(u) $$ nếu tồn tại một hàm cắt trơn $$ \varphi\in C_c^\infty(\Omega) $$, bằng 1 gần $$ x_0 $$, sao cho Fourier transform của $$ \varphi u $$ suy giảm nhanh trong một nón mở chứa $$ \xi_0 $$:

$$
\widehat{\varphi u}(\xi)=O(\lvert \xi\rvert^{-N})
\qquad \text{với mọi } N,
$$

khi $$ \xi $$ nằm trong nón đó và $$ \lvert \xi\rvert\to\infty $$.

Nếu điều kiện này không thỏa, ta nói $$ u $$ có singularity vi địa phương tại

$$ (x_0,\xi_0). $$

## So sánh nhanh với singular support

Đây là điểm mà sinh viên thường cần một bảng neo trực giác rất rõ:

- singular support trả lời câu hỏi: hàm hay phân phối không trơn ở đâu;
- wave front set trả lời câu hỏi mạnh hơn: không trơn ở đâu và theo hướng tần số nào;
- nếu chiếu wave front set xuống không gian vị trí, ta thu lại singular support.

Nói cách khác, singular support là “bản đồ địa lý” của kỳ dị, còn wave front set là “bản đồ địa lý kèm la bàn hướng” của kỳ dị. Trong các bài toán sóng hay ảnh hóa, phần “la bàn hướng” này mới là thứ quyết định singularity nhìn thấy được và di chuyển được ra sao.

## Ngộ nhận thường gặp

### “Wave front set chỉ là singular support viết lại”

Sai. Singular support chỉ lưu thông tin theo vị trí, còn wave front set lưu thêm hướng tần số.

### “Nếu một hàm không trơn tại một điểm thì nó kỳ dị theo mọi hướng”

Không. Một số singularity chỉ xuất hiện trong các hướng nhất định.

### “Fourier transform suy giảm nhanh nghĩa là hàm phải trơn toàn cục”

Không. Ta đang xét Fourier của $$ \varphi u $$ sau khi cắt cục bộ quanh điểm $$ x_0 $$.

### “Wave front set quá trừu tượng nên chỉ có ích trong lý thuyết thuần túy”

Sai. Đây là công cụ trung tâm để mô tả lan truyền kỳ dị, bài toán ngược, và hình ảnh hóa.

## Tiến trình học

### Bước 1: Nhìn lại singular support

Nhắc sinh viên rằng singular support trả lời câu hỏi “không trơn ở đâu?”.

### Bước 2: Thêm góc nhìn Fourier cục bộ

Cắt quanh điểm $$ x_0 $$ rồi xét sự suy giảm của Fourier transform.

### Bước 3: Giới thiệu nón hướng

Không cần quan tâm mọi hướng, chỉ cần xét hướng quanh $$ \xi_0 $$.

### Bước 4: Kết nối với PDE

Nhấn mạnh rằng PDE thường không vận chuyển toàn bộ singular support như một khối, mà vận chuyển từng hướng kỳ dị.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao singular support là chưa đủ không?
- Sinh viên có biết tại sao cần hàm cắt trơn $$ \varphi $$ không?
- Sinh viên có hiểu vì sao ta xét sự suy giảm nhanh trong nón mở chứ không trên toàn không gian tần số không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm trơn

Nếu $$ u\in C^\infty(\Omega) $$ thì với mọi hàm cắt trơn $$ \varphi $$, hàm $$ \varphi u $$ cũng trơn và hỗ compact. Do đó Fourier transform của nó suy giảm nhanh theo mọi hướng. Suy ra $$ WF(u)=\emptyset $$. Đây là kiểm tra chuẩn cho định nghĩa.

### Ví dụ 2: Delta Dirac

Xét $$ u=\delta_0 $$. Với $$ \varphi=1 $$ gần 0, ta có $$ \varphi \delta_0=\delta_0 $$. Fourier transform của Dirac là hằng số, nên không suy giảm nhanh theo bất kỳ hướng nào. Vì vậy $$ WF(\delta_0)=\{(0,\xi):\xi\neq 0\} $$. Kỳ dị nằm tại vị trí 0 và xuất hiện theo mọi hướng.

### Ví dụ 3: Hàm bước một chiều

Xét hàm Heaviside

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$

Hàm chỉ có điểm nhảy tại 0. Trực giác Fourier cho thấy kỳ dị gắn với hướng pháp tuyến của mặt nhảy. Trong một chiều, điều này vẫn dẫn đến mọi hướng khác 0 trên trục tần số, nhưng ví dụ này chuẩn bị cho trường hợp nhiều chiều.

### Ví dụ 4: Hàm bậc thang theo một biến trong nhiều chiều

Xét $$ u(x)=H(x_1) $$ trên $$ \mathbb{R}^n $$. Singular support là siêu phẳng $$ x_1=0 $$, nhưng wave front set không chứa mọi hướng $$ \xi $$. Nó chỉ chứa các hướng có thành phần pháp tuyến theo trục $$ x_1 $$, tức hướng gắn với mặt nhảy, chứ không chứa các hướng tiếp tuyến thuần túy. Đây là điểm khác biệt sâu nhất giữa singular support và wave front set.

### Ví dụ 5: Một cạnh trong ảnh hai chiều

Hãy tưởng tượng một ảnh nhị phân mà nửa trái màu đen, nửa phải màu trắng, với biên thẳng đứng tại $$ x_1=0 $$. Ảnh này có singular support nằm trên đường thẳng biên. Nhưng vi địa phương cho biết thêm rằng các hướng kỳ dị tập trung vào các pháp tuyến của biên, chứ không nằm dọc theo biên. Đây là trực giác quan trọng cho xử lý ảnh và chụp cắt lớp: thuật toán tái dựng thường bắt được biên theo những hướng nhất định trước khi phục hồi toàn bộ mức xám của ảnh.

## Câu hỏi khái niệm

1. Vì sao định nghĩa wave front set cần cả thông tin vị trí lẫn hướng?
2. Tại sao phải cắt cục bộ bởi hàm $$ \varphi $$ trước khi xét Fourier transform?
3. Điều gì khiến delta Dirac kỳ dị theo mọi hướng, còn mặt nhảy thì chỉ theo một số hướng?

## Bài toán ứng dụng

1. Trong xử lý ảnh, biên của một vật thể có thể được hiểu như singularity theo hướng nào?
2. Trong chụp cắt lớp, vì sao biết hướng kỳ dị giúp hiểu phần nào của ảnh có thể tái dựng được?
3. Trong phương trình sóng, vì sao việc biết “kỳ dị đi theo hướng nào” quan trọng hơn việc chỉ biết “kỳ dị ở đâu”?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu hai vật cùng có biên tại một vị trí nhưng hướng khác nhau, dữ liệu Fourier có phân biệt được không?
- Em nghĩ delta Dirac có một hướng kỳ dị hay nhiều hướng kỳ dị?
- Tại sao một mặt nhảy không nên kỳ dị theo mọi hướng?

### Hoạt động gợi ý

- Cho sinh viên phân loại vài phân phối đơn giản theo singular support và wave front set.
- Dùng hình ảnh cạnh thẳng, góc nhọn, và điểm để thảo luận hướng kỳ dị.
- Tổ chức thảo luận nhóm về ý nghĩa của “nón hướng” trong không gian tần số.

### Cách tăng tham gia

- Bắt đầu bằng ví dụ hình học thay vì định nghĩa.
- Cho sinh viên đoán wave front set của Dirac trước khi tính.
- Yêu cầu giải thích sự khác nhau giữa “điểm xấu” và “hướng xấu”.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám sát hai ví dụ: hàm trơn và delta Dirac.
- Dùng nhiều hình trực quan về cạnh và hướng pháp tuyến.
- Tránh sa sâu vào formalism của nón đối ngẫu ở lượt học đầu.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu chứng minh rằng $$ WF(u)=\emptyset $$ khi và chỉ khi $$ u\in C^\infty $$.
- Tính wave front set của phân phối mặt $$ \delta(x_1) $$ trong nhiều chiều.
- Liên hệ wave front set với regularity Sobolev vi địa phương.

## Ghi nhớ nhanh

Wave front set là bản mô tả kỳ dị tinh hơn singular support: nó không chỉ cho biết singularity ở đâu, mà còn cho biết nó xuất hiện theo hướng tần số nào. Đây là ngôn ngữ mở đầu và cốt lõi của microlocal analysis.

---

## Ứng dụng thực tế

### 1. Xử lý ảnh và phát hiện biên (Computer Vision)

Khi máy tính phân tích một ảnh kỹ thuật số, bài toán trung tâm là tìm biên của các vật thể — nơi độ sáng thay đổi đột ngột. Biên chính là singularity của hàm cường độ ảnh. Nếu chỉ biết vị trí (singular support), ta biết pixel nào "xấu" nhưng không biết biên chạy theo hướng nào. Wave front set bổ sung thông tin hướng: một biên thẳng đứng có hướng kỳ dị pháp tuyến nằm ngang; một biên nằm ngang có hướng kỳ dị thẳng đứng.

Thuật toán phát hiện biên như Canny hay Sobel thực ra đang ước lượng thông tin wave front set của ảnh mà không dùng ngôn ngữ này một cách tường minh. Khi ta áp dụng gradient theo hướng $$ x $$ và hướng $$ y $$ riêng biệt, ta đang kiểm tra sự suy giảm Fourier theo từng hướng — đúng tinh thần định nghĩa wave front set.

**Mô hình hóa:** Ảnh là phân phối $$ u(x_1, x_2) $$. Biên tại $$ x_1 = a $$ theo hướng thẳng đứng tương ứng với
$$
WF(u) \supset \{(a, x_2, \xi_1, 0) : \xi_1 \neq 0\},
$$
tức kỳ dị theo hướng pháp tuyến $$ \xi_1 $$, không theo hướng tiếp tuyến $$ \xi_2 $$.

### 2. Chụp cắt lớp y khoa (CT Scan và MRI)

Máy chụp cắt lớp thu nhận dữ liệu Radon transform của mật độ mô — tức tích phân của hàm mật độ dọc theo các đường thẳng từ nhiều góc chiếu khác nhau. Bài toán ngược là: từ dữ liệu đo được, tái dựng hàm mật độ $$ f(x) $$.

Thông tin wave front set giải thích vì sao một số biên cơ quan được tái dựng tốt hơn biên khác. Nếu biên của một cơ quan vuông góc với hướng chiếu, dữ liệu đó nhạy cảm với singularity tại biên; nếu biên song song với hướng chiếu, thông tin bị che khuất. Đây chính là hiện tượng "limited angle tomography" và lý thuyết wave front set giải thích chính xác thông tin nào có thể tái dựng được từ góc chiếu nào.

**Giới hạn mô hình:** Giả định mô ảnh là đồng nhất và không tán xạ. Trong thực tế, xương và mô mềm có đặc tính tán xạ khác nhau.

### 3. Địa chấn học và thăm dò dầu khí

Trong thăm dò địa chấn, nguồn năng lượng phát sóng âm xuống lòng đất. Sóng phản xạ từ các ranh giới địa tầng — nơi mật độ đất thay đổi đột ngột — được thu lại bởi các geophone tại bề mặt. Ranh giới địa tầng chính là singularity của hệ số phản xạ.

Wave front set của dữ liệu địa chấn chứa thông tin về vị trí và hướng của các ranh giới. Biết hướng kỳ dị, kỹ sư có thể xác định góc nghiêng của tầng địa chất, phân biệt phản xạ từ ranh giới nằm ngang và ranh giới nghiêng. Kỹ thuật migration trong xử lý địa chấn bản chất là một ánh xạ wave front set từ không gian đo được về không gian vật lý.

### 4. Âm học kiến trúc và thiết kế phòng hòa nhạc

Trong một phòng hòa nhạc, sóng âm từ nhạc cụ phản xạ và nhiễu xạ theo hình học của phòng. Singularity của sóng âm (các xung âm thanh sắc nét) lan theo đặc tuyến, và hướng kỳ dị xác định hướng phản xạ. Kiến trúc sư âm học dùng ray tracing — phiên bản hình học cổ điển của wave front set — để dự đoán echo và phân phối năng lượng âm.

---

## Trực giác sâu hơn: Tại sao hướng lại quan trọng?

Một hiểu nhầm phổ biến là: "Nếu biết chỗ nào không trơn thì đã đủ rồi." Hãy thử với ví dụ cụ thể.

Xét hai phân phối trong $$ \mathbb{R}^2 $$:
- $$ u_1(x_1, x_2) = H(x_1) $$ (hàm bước theo $$ x_1 $$)
- $$ u_2(x_1, x_2) = H(x_2) $$ (hàm bước theo $$ x_2 $$)

Cả hai đều có singular support là một đường thẳng qua gốc tọa độ. Nhưng wave front set của chúng hoàn toàn khác nhau:
$$
WF(u_1) \subset \{x_1 = 0\} \times \{(\xi_1, 0) : \xi_1 \neq 0\},
\quad
WF(u_2) \subset \{x_2 = 0\} \times \{(0, \xi_2) : \xi_2 \neq 0\}.
$$
Khi ta áp dụng PDE hyperbolic, hai singularity này sẽ lan theo các quỹ đạo hoàn toàn khác nhau. Singular support không phân biệt được chúng; wave front set thì có.

---

## Trực quan hóa bằng Python

Đoạn code dưới đây minh họa ba ví dụ cốt lõi của wave front set: hàm trơn, delta Dirac, và hàm bước. Với mỗi hàm, ta tính và hiển thị phổ Fourier sau khi cắt cục bộ để thấy sự suy giảm (hoặc không suy giảm) theo từng hướng.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# -------------------------------------------------------
# Thiết lập lưới không gian và tần số
# -------------------------------------------------------
N = 512
x = np.linspace(-4, 4, N)
y = np.linspace(-4, 4, N)
X, Y = np.meshgrid(x, y)
dx = x[1] - x[0]

# Hàm cắt trơn Gaussian (localization function phi)
def phi(X, Y, x0=0, y0=0, sigma=0.8):
    return np.exp(-((X - x0)**2 + (Y - y0)**2) / (2 * sigma**2))

# Lưới tần số
freq = np.fft.fftfreq(N, d=dx)
FX, FY = np.meshgrid(freq, freq)
F_magnitude = np.sqrt(FX**2 + FY**2)
F_magnitude[F_magnitude == 0] = 1e-10  # Tránh chia cho 0

# -------------------------------------------------------
# Ba hàm cần kiểm tra
# -------------------------------------------------------
phi_loc = phi(X, Y)  # Hàm cắt cục bộ gần gốc tọa độ

# 1. Hàm trơn: Gaussian
u_smooth = np.exp(-(X**2 + Y**2) / 0.5)
u1_localized = phi_loc * u_smooth

# 2. Delta Dirac (xấp xỉ bằng Gaussian hẹp)
u_delta = np.exp(-(X**2 + Y**2) / 0.01) / (0.01 * np.pi)
u2_localized = phi_loc * u_delta

# 3. Hàm bước theo x1 (Heaviside)
u_step = (X > 0).astype(float)
u3_localized = phi_loc * u_step

# -------------------------------------------------------
# Tính phổ Fourier 2D (lấy giá trị tuyệt đối)
# -------------------------------------------------------
def compute_spectrum(u):
    return np.abs(np.fft.fftshift(np.fft.fft2(u)))

spec1 = compute_spectrum(u1_localized)
spec2 = compute_spectrum(u2_localized)
spec3 = compute_spectrum(u3_localized)

# -------------------------------------------------------
# Vẽ hình
# -------------------------------------------------------
fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

titles = ["Hàm trơn (Gaussian)", "Delta Dirac (xấp xỉ)", "Hàm bước H(x₁)"]
functions = [u_smooth, u_delta, u_step]
spectra = [spec1, spec2, spec3]
wf_descriptions = [
    "WF(u) = ∅\n(không có kỳ dị)",
    "WF(u) tại (0,ξ), ξ≠0\n(kỳ dị mọi hướng)",
    "WF(u) theo hướng ξ₁\n(kỳ dị pháp tuyến mặt nhảy)"
]

for i, (title, f, spec, wf) in enumerate(zip(titles, functions, spectra, wf_descriptions)):
    # Hàm gốc
    ax_f = fig.add_subplot(gs[0, i])
    im = ax_f.pcolormesh(X, Y, f, cmap='RdBu_r', shading='auto',
                          vmin=-np.percentile(np.abs(f), 99),
                          vmax=np.percentile(np.abs(f), 99))
    ax_f.set_title(title, fontsize=11, fontweight='bold')
    ax_f.set_xlabel("x₁"); ax_f.set_ylabel("x₂")
    ax_f.set_xlim(-3, 3); ax_f.set_ylim(-3, 3)
    ax_f.set_aspect('equal')
    plt.colorbar(im, ax=ax_f, shrink=0.8)

    # Phổ Fourier (sau cắt cục bộ)
    ax_s = fig.add_subplot(gs[1, i])
    freq_range = 50  # Hiển thị tần số thấp đến trung bình
    center = N // 2
    spec_crop = spec[center-freq_range:center+freq_range,
                     center-freq_range:center+freq_range]
    ax_s.imshow(np.log1p(spec_crop), cmap='hot', origin='lower',
                extent=[-freq_range, freq_range, -freq_range, freq_range])
    ax_s.set_title(f"Phổ Fourier (cục bộ)\n{wf}", fontsize=9)
    ax_s.set_xlabel("ξ₁ (tần số)"); ax_s.set_ylabel("ξ₂ (tần số)")

plt.suptitle("Wave Front Set: So sánh ba ví dụ cốt lõi\n"
             "(Hàng trên: hàm gốc — Hàng dưới: phổ Fourier sau cắt cục bộ)",
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig("wave_front_set_comparison.png", dpi=150, bbox_inches='tight')
plt.show()
print("Quan sát: Hàm trơn → phổ giảm nhanh mọi hướng (WF rỗng).")
print("          Delta Dirac → phổ gần hằng số mọi hướng (WF đầy đủ).")
print("          Hàm bước → phổ tập trung theo trục ξ₁ (WF theo hướng pháp tuyến).")
```

### Minh họa bổ sung: Wave front set theo hướng (profile 1D)

```python
import numpy as np
import matplotlib.pyplot as plt

# Kiểm tra sự suy giảm Fourier theo từng hướng theta
N = 1024
x = np.linspace(-6, 6, N)
dx = x[1] - x[0]

# Hàm cắt cục bộ
phi_1d = np.exp(-x**2 / (2 * 0.5**2))

# Hai hàm trong 1D
u_smooth = np.exp(-x**2)           # Trơn: WF rỗng
u_step   = (x > 0).astype(float)   # Bước: WF tại (0, ξ≠0)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, u, label, color in zip(axes,
                                 [u_smooth, u_step],
                                 ["Hàm trơn", "Hàm bước H(x)"],
                                 ["steelblue", "crimson"]):
    u_loc = phi_1d * u
    freqs = np.fft.fftfreq(N, d=dx)
    spec  = np.abs(np.fft.fft(u_loc))
    # Chỉ lấy nửa dương
    pos   = freqs > 0
    ax.loglog(freqs[pos], spec[pos], color=color, linewidth=2, label=label)
    # Đường tham chiếu suy giảm nhanh (Schwartz)
    xi_ref = freqs[pos]
    ax.loglog(xi_ref, 1e2 * xi_ref**(-4), 'k--', alpha=0.5, label=r"$|\xi|^{-4}$ (suy giảm nhanh)")
    ax.loglog(xi_ref, 5e1 * xi_ref**(-1), 'k:', alpha=0.5, label=r"$|\xi|^{-1}$ (suy giảm chậm)")
    ax.set_xlabel(r"$|\xi|$ (tần số)", fontsize=12)
    ax.set_ylabel(r"$|\widehat{\varphi u}(\xi)|$", fontsize=12)
    ax.set_title(f"{label}\nPhổ Fourier sau cắt cục bộ", fontsize=11, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0.5, N/(2*6)])

plt.suptitle("Kiểm tra suy giảm Fourier: Nhanh → WF rỗng, Chậm → có singularity",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("wf_decay_comparison.png", dpi=150)
plt.show()
```

---

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

**Trực giác:** Một hàm có thể "gần trơn" theo một số hướng và "không trơn" theo hướng khác. Wave front set là công cụ đo lường sự phân biệt đó.

**Điều cần nhớ:**
- Wave front set sống trong không gian pha $$ (x, \xi) $$: vị trí kết hợp với tần số.
- Nếu $$ \hat{\varphi u}(\xi) \to 0 $$ nhanh khi $$ \lvert \xi\rvert \to \infty $$ trong một nón quanh $$ \xi_0 $$, thì $$ (x_0, \xi_0) \notin WF(u) $$.
- Ba ví dụ cần thuộc lòng: hàm trơn (WF rỗng), delta Dirac (WF đầy), hàm bước (WF theo pháp tuyến).

**Bài tập khởi động:** Cho ảnh nhị phân có biên thẳng đứng. Mô tả singular support và wave front set của hàm cường độ ảnh. Hỏi: nếu xoay ảnh 45 độ, wave front set thay đổi như thế nào?

### Mức sau đại học (Graduate)

**Lý thuyết sâu hơn:** Wave front set có thể được định nghĩa qua nhiều cách tương đương: qua sự suy giảm Fourier cục bộ, qua FBI transform (Fourier-Bros-Iagolnitzer), hay qua analytic wave front set (định nghĩa Sato). Mỗi cách mở ra một mảng lý thuyết riêng.

**Tính chất quan trọng:**
1. **Phép chiếu:** $$ \pi_x(WF(u)) = \text{sing supp}(u) $$.
2. **Phép vi phân:** Nếu $$ P $$ là toán tử vi phân order $$ m $$, thì $$ WF(Pu) \subset WF(u) $$.
3. **Phép nhân:** $$WF(uv) \subset WF(u) \cup WF(v) \cup (WF(u) + WF(v))$$ (với điều kiện wave front set không "đụng" nhau theo nghĩa xác định).
4. **Elliptic regularity:** Nếu $$ P $$ elliptic tại $$ (x_0, \xi_0) $$ thì $$ (x_0, \xi_0) \notin WF(u) $$ khi $$ (x_0, \xi_0) \notin WF(Pu) $$.

**Kết nối lý thuyết:** Wave front set là tiền đề để định nghĩa microlocal ellipticity, parametrix vi địa phương, và cuối cùng là định lý lan truyền kỳ dị của Hörmander — một trong những định lý sâu nhất của phân tích hiện đại.

**Bài tập nâng cao:** Chứng minh rằng nếu $$ \varphi \in C^\infty_c $$ và $$ u \in \mathcal{D}' $$, thì $$ WF(\varphi u) \subset WF(u) $$. Từ đó suy ra rằng wave front set là bất biến dưới phép nhân với hàm trơn.

---

## Liên kết với các khái niệm khác trong khóa học

| Khái niệm đã học | Kết nối với Wave Front Set |
|---|---|
| Phân phối (Ch. 12) | Wave front set là tinh chỉnh của singular support phân phối |
| Biến đổi Fourier (Ch. 8, 14) | Định nghĩa WF dùng suy giảm Fourier cục bộ |
| Phương trình elliptic (Ch. 11, 14) | Elliptic regularity: toán tử elliptic không tạo thêm WF |
| Phương trình sóng (Ch. 10) | WF truyền theo bicharacteristics (bài tiếp theo) |
| Bài toán ngược (bài 6 chương này) | WF xác định thông tin nào có thể tái dựng được |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ảnh CT và phát hiện biên
- Bài toán: Trong ảnh y học, điều quan trọng thường không phải chỉ là vị trí mép biên, mà còn là hướng của chúng.
- Mô hình: Wave front set $$ WF(u) $$ ghi cả vị trí $$ x $$ lẫn hướng tần số $$ \xi $$ của singularity.
- Giả thiết và giới hạn: Đây là mô hình vi địa phương cục bộ; không trực tiếp thay thế thuật toán ảnh rời rạc.
- Diễn giải: Hai singularity cùng nằm ở một điểm nhưng có hướng khác nhau sẽ được phân biệt rõ trong $$ WF(u) $$.

#### Địa chấn và phản xạ sóng
- Bài toán: Từ dữ liệu phản xạ, ta muốn biết các mặt phân cách trong lòng đất nằm ở đâu và có hướng pháp tuyến như thế nào.
- Mô hình: Singularities của hệ số môi trường và dữ liệu đo được mô tả bằng wave front set.
- Giả thiết và giới hạn: Phụ thuộc vào mô hình sóng tuyến tính và visibility của cấu trúc.
- Diễn giải: Wave front set là đối tượng đúng để nói xem thông tin nào thật sự đi vào dữ liệu.

### 2. Trực giác bổ sung và các kết nối

Singular support chỉ cho biết "chỗ nào không trơn", còn wave front set nói thêm "không trơn theo hướng nào". Một mép thẳng, một góc nhọn và một delta source có thể cùng nằm tại một vị trí, nhưng chúng có cấu trúc tần số rất khác nhau. Một ngộ nhận phổ biến là singularity chỉ là tính chất điểm; trong microlocal analysis, singularity còn có hướng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

n = 128
x = np.linspace(-1, 1, n, endpoint=False)
X, Y = np.meshgrid(x, x)
u = (X > 0).astype(float)  # buoc nhay qua duong x = 0

U = np.fft.fftshift(np.abs(np.fft.fft2(u)))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(u, extent=[-1, 1, -1, 1], origin="lower", cmap="gray")
axes[0].set_title("Phan bo co singularity theo duong x = 0")
axes[1].imshow(np.log1p(U), cmap="magma")
axes[1].set_title("Do lon Fourier: huong tan so phap tuyen noi bat")
for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: wave front set edge orientation visualization
- search: singular support vs wave front set image processing
- search: seismic singularities wave front set intuition

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Wave front set: vị trí và hướng kỳ dị" description="Thay đổi loại singularity và góc cạnh để quan sát các hướng kỳ dị nổi bật trong không gian tần số." path="interactives/chapter15/wave-front-set-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Cho hàm bậc thang
$$ u(x_1,x_2)=H(x_1). $$
Singularity nằm trên đường $$ x_1=0 $$, nhưng chỉ theo các hướng pháp tuyến với đường nhảy, tức là theo các $$ \xi $$ song song với trục $$ x_1 $$. Vì vậy $$ WF(u) $$ không chỉ nói "trục tung là singular", mà nói rõ singularity gắn với hướng pháp tuyến của biên.

### 6. Phân tầng độ khó

**Bậc đại học.** So sánh singular support với wave front set qua ví dụ delta, bước nhảy và hàm trơn.

**Bậc sau đại học.** Kết nối với định nghĩa hình nón, pullback/pushforward và invariance theo đổi tọa độ.
