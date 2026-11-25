---
layout: post
title: "Ổn Định và Hội Tụ (CFL)"
chapter: '13'
order: 6
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: required
---

![Trực giác về ổn định, hội tụ và điều kiện CFL]({{ site.imgurl }}/chapter_img/chapter13/06_stability_convergence_cfl.svg )

Một sơ đồ sai phân trông hoàn hảo trên giấy, nhất quán bậc hai hẳn hoi, nhưng khi bấm chạy thì chỉ sau 15 bước thời gian toàn bộ màn hình biến thành răng cưa dao động $10^{30}$! Vì sao? Vì **Nhất quán một mình không bao giờ đủ cho Hội tụ**! Định lý Tương đương Lax–Richtmyer và điều kiện CFL là bộ đôi định luật tối cao giải mã trọn vẹn bí ẩn quan trọng này của mô phỏng PDE.

## Kiến thức cần nhớ: Bốn trụ cột của Ổn định, Hội tụ và Điều kiện CFL

1. **Định lý Tương đương Lax–Richtmyer**:
   Đối với một bài toán giá trị ban đầu tuyến tính đặt chỉnh, một sơ đồ sai phân **nhất quán** sẽ **hội tụ** khi và chỉ khi nó **ổn định**! Điều này chuyển bài toán khó (chứng minh hội tụ về nghiệm ẩn $u$) thành hai bài toán kiểm tra được (Taylor + Ổn định).
2. **Điều kiện CFL (Courant–Friedrichs–Lewy) — Trực giác Hình học Vật lý**:
   Sóng vật lý chạy với tốc độ $c$ đi được quãng đường $c\Delta t$ trong 1 bước thời gian; trong khi lưới sai phân hiện chỉ truyền thông tin được tối đa 1 ô $\Delta x$ mỗi bước. Do đó bắt buộc $c\Delta t \le \Delta x \iff \text{CFL} = \frac{c\Delta t}{\Delta x} \le 1$ (miền phụ thuộc số phải chứa miền phụ thuộc vật lý)!
3. **Phân tích Ổn định von Neumann (Biến đổi Fourier Rời rạc)**:
   Thay nghiệm thử dạng sóng phẳng $u_j^n = G^n e^{ij\theta}$ vào sơ đồ sai phân để tìm hệ số khuếch đại $G(\theta)$. Điều kiện cần và đủ để ổn định trong $L^2$ là $|G(\theta)| \le 1$ với mọi số sóng $\theta \in [-\pi, \pi]$!
4. **Sơ đồ Upwind (Ngược chiều gió) cho Phương trình Truyền tải**:
   Với $u_t + c u_x = 0$, sai phân trung tâm FTCS **luôn mất ổn định** với mọi $\Delta t > 0$! Ta buộc phải lấy sai phân lùi (nếu $c > 0$) hoặc sai phân tiến (nếu $c < 0$) để đón đúng hướng thông tin chảy tới.

## Mục tiêu

Bài học này trình bày ba khái niệm trụ cột trong phân tích lược đồ số: tính nhất quán (consistency), tính ổn định (stability) và sự hội tụ (convergence). Sau bài học, sinh viên cần giải thích được mối liên hệ giữa ba khái niệm này qua định lý tương đương Lax, nắm trực giác vật lý của điều kiện CFL, và hiểu vì sao một lược đồ số đáng tin cậy phải đồng thời xấp xỉ đúng phương trình và kiểm soát được sự lan truyền sai số.

## Kiến thức nền

Sinh viên cần nắm sai phân hữu hạn, phương pháp Euler và nhận thức rằng sai số ban đầu hoặc sai số làm tròn có thể lan truyền theo thời gian. Bài học này đánh giá độ tin cậy của các lược đồ đã xây dựng ở các bài trước.

## Dẫn nhập

Xây dựng được một công thức sai phân mới chỉ là bước khởi đầu; câu hỏi then chốt là khi chạy trên máy tính, nghiệm số có thực sự bám sát nghiệm đúng hay không. Một lược đồ nhìn qua rất hợp lý vẫn có thể bùng nổ vì khuếch đại nhiễu quá nhanh. Do đó, thiết kế lược đồ và phân tích sai số–ổn định là hai phần gắn chặt với nhau.

Ba tiêu chí nền tảng gồm:

- **Tính nhất quán (consistency)**: lược đồ có thực sự xấp xỉ phương trình gốc khi bước lưới tiến về 0 hay không;
- **Tính ổn định (stability)**: sai số có được chặn mà không bị khuếch đại vô hạn hay không;
- **Sự hội tụ (convergence)**: khi làm mịn lưới, nghiệm số có tiến về nghiệm chính xác hay không.


### Giải thích: Tính tay bước thời gian tối đa $\Delta t_{\max}$ và cú sốc "chia đôi lưới"

So sánh hai PDE kinh điển cùng trên lưới không gian $\Delta x = 0{,}1$:
1. **Phương trình truyền tải (Hyperbolic)** $u_t + 2 u_x = 0$ (sơ đồ Upwind, $\text{CFL} = \frac{c\Delta t}{\Delta x} \le 1$):
   $$\Delta t \le \frac{\Delta x}{c} = \frac{0{,}1}{2} = \mathbf{0{,}05\text{ s}}.$$
2. **Phương trình nhiệt (Parabolic)** $u_t = 0{,}5 u_{xx}$ (sơ đồ FTCS, $r = \frac{\alpha\Delta t}{\Delta x^2} \le 0{,}5$):
   $$\Delta t \le \frac{0{,}5\,\Delta x^2}{\alpha} = \frac{0{,}5 \times 0{,}01}{0{,}5} = \mathbf{0{,}01\text{ s}}.$$
3. **Nếu ta làm mịn lưới gấp đôi ($\Delta x \to 0{,}05$)**:
   - Với sóng/truyền tải: $\Delta t_{\max}$ giảm $2\times$ xuống $\mathbf{0{,}025\text{ s}}$ (tuyến tính theo $\Delta x$).
   - Với nhiệt FTCS: $\Delta t_{\max}$ giảm **$4\times$** xuống $\mathbf{0{,}0025\text{ s}}$ (tỷ lệ $\Delta x^2$)! Đó là lý do các bài toán khuếch tán lưới mịn hầu như luôn chuyển sang sơ đồ ẩn như Crank–Nicolson.
## Khái niệm theo ba cách

### Cách trực giác

Có thể ví việc giải số như chụp ảnh một vật thể đang chuyển động:

- Nếu ống kính lệch góc so với vật thể ngay từ đầu, đó là thiếu tính nhất quán.
- Nếu rung máy làm nhiễu khuếch đại dần qua từng khung hình, đó là thiếu tính ổn định.
- Nếu tăng độ phân giải mà ảnh vẫn không tiến gần tới hình dạng thật, đó là không hội tụ.

### Cách hình ảnh

Có thể biểu diễn mối liên hệ bằng sơ đồ tam giác với ba đỉnh là tính nhất quán, tính ổn định và sự hội tụ, trong đó mũi tên quan trọng nhất là:

$$
\text{consistency}+\text{stability}\Rightarrow \text{convergence}.
$$

Đối với điều kiện CFL, vẽ song song nón phụ thuộc vật lý và miền phụ thuộc số trên lưới cho thấy trực quan rằng miền phụ thuộc của lược đồ số phải bao trùm miền phụ thuộc vật lý — nói cách khác, trong một bước thời gian, tín hiệu vật lý không được truyền vượt quá phạm vi mà mẫu sai phân trên lưới có thể nắm bắt.

### Cách hình thức

Một lược đồ được gọi là **nhất quán** nếu sai số cắt cụt địa phương tiến về 0 khi $$ \Delta t,\Delta x\to 0 $$. Lược đồ được gọi là **ổn định** nếu các nhiễu nhỏ trong dữ liệu hoặc phép tính không bị khuếch đại vô hạn theo thời gian, và **hội tụ** nếu nghiệm số tiến về nghiệm chính xác khi làm mịn lưới.

Đối với các bài toán giá trị ban đầu tuyến tính đặt chỉnh tốt, định lý tương đương Lax khẳng định:

$$
\text{consistency}+\text{stability}\Rightarrow \text{convergence}.
$$

Điều kiện CFL thường có dạng:

$$ \frac{c\Delta t}{\Delta x}\le C, $$

trong đó $$ c $$ là tốc độ lan truyền đặc trưng của bài toán.

## Ngộ nhận thường gặp

### “Chỉ cần tính nhất quán là đủ”

Sai. Một lược đồ nhất quán vẫn có thể bùng nổ hoàn toàn nếu không ổn định.

### “Ổn định nghĩa là nghiệm số đứng yên không thay đổi”

Không đúng. Ổn định nghĩa là các nhiễu nhỏ và sai số làm tròn không bị khuếch đại vượt kiểm soát.

### “CFL là điều kiện đủ cho mọi loại PDE”

Không đúng. CFL là điều kiện cần đặc trưng cho các lược đồ tường minh của bài toán hyperbolic (đối lưu, sóng), không phải công thức duy nhất cho mọi phương trình.

### “Cứ chia lưới nhỏ hơn nữa thì chắc chắn hội tụ”

Không hẳn. Nếu lược đồ không ổn định (hoặc làm mịn $$ \Delta x $$ mà không giảm $$ \Delta t $$ tương ứng theo điều kiện ổn định), kết quả vẫn phân kỳ.

## Tiến trình học

### Bước 1: Kiểm tra tính nhất quán

Thay nghiệm chính xác vào lược đồ và kiểm tra sai số cắt cụt có tiến về 0 khi bước lưới tiến về 0 hay không.

### Bước 2: Phân tích tính ổn định

Theo dõi hệ số khuếch đại của sai số hoặc của từng mode Fourier (phân tích von Neumann).

### Bước 3: Suy ra sự hội tụ

Áp dụng định lý Lax cho các bài toán tuyến tính đặt chỉnh: nhất quán cộng ổn định kéo theo hội tụ.

### Bước 4: Hiểu ý nghĩa vật lý của điều kiện CFL

Tốc độ truyền thông tin trên lưới số phải đủ lớn để bao trùm tốc độ truyền thông tin vật lý.

### Các điểm kiểm tra hiểu bài

- Sinh viên có diễn đạt được bằng lời ba khái niệm nhất quán, ổn định và hội tụ hay không?
- Sinh viên có giải thích được vì sao tính nhất quán đơn lẻ là chưa đủ hay không?
- Sinh viên có giải thích được ý nghĩa vật lý của điều kiện CFL hay không?

## Ví dụ có lời giải

### Ví dụ 1: Tính nhất quán của phương pháp Euler

Thay nghiệm đúng $$ y(t) $$ vào lược đồ Euler:

$$ \frac{y(t+h)-y(t)}{h}-f(t,y(t)). $$

Khai triển Taylor cho thấy phần dư này có bậc $$ O(h) $$, nên phương pháp Euler nhất quán bậc một.

### Ví dụ 2: Tính ổn định của Euler tiến trên $$ y'=\lambda y $$

Sai số $$ e_n $$ thỏa mãn $$ e_{n+1}=(1+h\lambda)e_n $$. Khi $$ \lvert 1+h\lambda\rvert>1 $$, sai số tăng theo cấp số nhân — minh họa rõ nhất của sự mất ổn định.

### Ví dụ 3: Điều kiện CFL cho phương trình đối lưu

Xét phương trình $$ u_t+cu_x=0 $$ (với $$ c>0 $$). Đối với lược đồ upwind tường minh, điều kiện CFL là:

$$ \frac{c\Delta t}{\Delta x}\le 1. $$

Nếu vi phạm điều kiện này, biên độ sai lệch sẽ khuếch đại nhanh và sinh dao động phi vật lý.

### Ví dụ 4: Nhất quán nhưng không ổn định

Một lược đồ có thể có sai số cắt cụt rất nhỏ trên từng bước, nhưng nếu mỗi bước khuếch đại sai số cũ lên gấp đôi thì sau nhiều bước nghiệm số vẫn lệch xa nghiệm thật. Điều này khẳng định tính ổn định là mắt xích không thể thiếu.

## Câu hỏi khái niệm

1. Vì sao tính nhất quán chỉ đánh giá lược đồ trên một bước đơn lẻ còn tính ổn định đánh giá cả quá trình tiến hóa?
2. Vì sao điều kiện CFL có thể hiểu như một ràng buộc về tốc độ truyền thông tin trên lưới?
3. Vì sao sự hội tụ là mục tiêu cuối cùng nhưng thường được chứng minh gián tiếp qua tính nhất quán và tính ổn định?

## Bài toán ứng dụng

1. Trong dự báo thời tiết, vì sao không thể chọn bước thời gian $$ \Delta t $$ độc lập với kích thước lưới không gian $$ \Delta x $$?
2. Trong mô phỏng dòng giao thông, điều gì xảy ra với lược đồ tường minh nếu xe di chuyển qua nhiều hơn một ô lưới trong một bước thời gian?
3. Trong mô phỏng sóng xung kích, vì sao vi phạm điều kiện CFL dẫn đến nghiệm hoàn toàn phi vật lý?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một lược đồ xấp xỉ rất sát PDE trong một bước, vì sao nó vẫn có thể thất bại hoàn toàn sau nhiều bước?
- "Tính ổn định" trong bài này nói về sự ổn định của đại lượng nào?
- Điều kiện CFL chỉ là ràng buộc đại số hay còn phản ánh bản chất vật lý của bài toán?

### Hoạt động gợi ý

- Cho sinh viên tự kiểm tra tính nhất quán bằng khai triển Taylor trên một lược đồ đơn giản.
- Chạy mô phỏng thay đổi tỷ số $$ \frac{\Delta t}{\Delta x} $$ để quan sát chính xác ngưỡng mất ổn định.
- Thảo luận nhóm về mối quan hệ giữa miền phụ thuộc vật lý và miền phụ thuộc số.

### Cách tăng tham gia

- Mở đầu bằng một mô phỏng bị bùng nổ dù công thức sai phân trông rất hợp lý.
- Yêu cầu sinh viên diễn đạt lại định lý Lax bằng ngôn ngữ thông thường.
- Khuyến khích dùng trực giác sóng hoặc giao thông để giải thích điều kiện CFL.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tách rõ từng khái niệm trong bộ ba nhất quán – ổn định – hội tụ bằng các ví dụ ngắn.
- Ưu tiên sơ đồ hình học về miền phụ thuộc trước khi đi vào chứng minh đại số.
- Khảo sát kỹ bài toán đối lưu một chiều trước.

### Thử thách cho sinh viên khá giỏi

- Thực hiện phân tích ổn định von Neumann cho lược đồ upwind và lược đồ Lax–Friedrichs.
- Chứng minh định lý tương đương Lax trong trường hợp toán tử tuyến tính đơn giản.
- So sánh điều kiện CFL của các lược đồ khác nhau cho phương trình đối lưu và phương trình sóng.

## Ghi nhớ nhanh

Một lược đồ số chỉ hội tụ về nghiệm chính xác khi vừa nhất quán với PDE gốc vừa ổn định trước sự lan truyền sai số. Điều kiện CFL đảm bảo tốc độ truyền thông tin trên lưới số bao trùm tốc độ lan truyền vật lý của hệ.

---

## Ứng dụng thực tế

### 1. Dự báo thời tiết và mô phỏng khí quyển

Trong các mô hình khí quyển, sóng và dòng đối lưu lan truyền thông tin với vận tốc đặc trưng. Nếu chọn bước thời gian quá lớn so với kích thước lưới, lược đồ tường minh sẽ vi phạm điều kiện CFL và sinh dao động phân kỳ phi vật lý.

### 2. Dòng giao thông và đối lưu 1D

Điều kiện $$ \frac{c\Delta t}{\Delta x}\le C $$ cho thấy trong mỗi bước thời gian, sóng mật độ không được vượt quá phạm vi mà mẫu sai phân trên lưới có thể tiếp nhận.

### 3. Sóng nổ, thủy động lực học và CFD

Trong tính toán động lực học chất lưu (CFD), tính ổn định quyết định trực tiếp việc mô phỏng có bắt đúng biên dạng sóng xung kích hay sụp đổ do nhiễu số. Bộ ba nhất quán – ổn định – hội tụ vì thế là tiêu chuẩn thiết yếu trong mọi phần mềm mô phỏng.

## Trực giác sâu hơn

Tính nhất quán đảm bảo mỗi bước mô phỏng đúng phương trình; tính ổn định đảm bảo nhiễu nhỏ không bị khuếch đại mất kiểm soát; và sự hội tụ khẳng định toàn bộ quá trình tiến về nghiệm thật. Nhiều lược đồ thất bại không phải do sai công thức cục bộ mà do khuếch đại sai số tích lũy qua thời gian.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

def upwind(c, dx, dt, T=0.6):
    x = np.linspace(0, 1, int(1/dx) + 1)
    u = np.exp(-200 * (x - 0.3)**2)
    r = c * dt / dx
    n_steps = int(T / dt)
    for _ in range(n_steps):
        u[1:] = u[1:] - r * (u[1:] - u[:-1])
        u[0] = 0.0
    return x, u, r

plt.figure(figsize=(9, 5))
for dt in [0.004, 0.01]:
    x, u, r = upwind(c=1.0, dx=0.01, dt=dt)
    plt.plot(x, u, label=f'dt={dt}, CFL={r:.2f}')
plt.title('Ảnh hưởng của CFL trong sơ đồ đối lưu đơn giản')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` kèm thanh trượt tỷ số $$ \Delta t/\Delta x $$ để quan sát trực tiếp thời điểm số CFL vượt ngưỡng làm nghiệm số méo dạng và mất ổn định.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `CFL condition visualization`, `Von Neumann stability animation`, hoặc `numerical instability advection equation`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào bộ ba nhất quán – ổn định – hội tụ và ý nghĩa vật lý của điều kiện CFL cho phương trình đối lưu và phương trình sóng.

### Mức sau đại học (Graduate)

Đi sâu vào phân tích von Neumann, định lý tương đương Lax–Richtmyer, phổ của toán tử tiến hóa rời rạc và các tiêu chuẩn ổn định phi tuyến.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dự báo thời tiết và mô hình sóng
- Bài toán: Ràng buộc bước thời gian theo kích thước ô lưới và tốc độ lan truyền sóng.
- Mô hình: Điều kiện CFL điển hình $$ \frac{c\Delta t}{\Delta x}\le C $$.
- Giả thiết và giới hạn: Hằng số $$ C $$ phụ thuộc vào lược đồ cụ thể; vi phạm điều kiện thường gây bùng nổ số.
- Diễn giải: Tín hiệu vật lý không được truyền nhanh hơn tốc độ lan truyền thông tin trên lưới.

#### Mô phỏng giao thông và dòng chảy
- Bài toán: Mô phỏng chính xác các mặt sóng và sóng xung kích mà không sinh dao động giả.
- Mô hình: Phân tích ổn định Fourier (von Neumann) cho lược đồ sai phân.
- Giả thiết và giới hạn: Tuyến tính hóa chỉ phản ánh cục bộ hành vi của hệ phi tuyến.
- Diễn giải: Tính ổn định và sự hội tụ luôn gắn liền với tính nhất quán.

### 2. Trực giác bổ sung và các kết nối

Tính nhất quán kiểm tra độ khớp cục bộ với PDE, tính ổn định chặn sự khuếch đại sai số, còn sự hội tụ đảm bảo nghiệm số tiến về nghiệm đúng. Định lý Lax–Richtmyer liên kết cả ba khái niệm này trong khuôn khổ tuyến tính đặt chỉnh; do đó không thể chỉ kiểm tra tính nhất quán rồi mặc nhiên kết luận lược đồ hội tụ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

nu = np.linspace(0, 1.5, 400)
G = np.abs(1 - 1j * nu)

plt.plot(nu, G)
plt.axhline(1, color="black", linewidth=0.8)
plt.xlabel("so CFL / tan so vo huong")
plt.ylabel("|G|")
plt.title("He so khuech dai va on dinh")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: CFL condition animation numerical wave propagation
- search: von Neumann stability visualization
- search: Lax equivalence theorem intuition

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Điều kiện CFL trong sơ đồ upwind" description="Điều chỉnh số CFL để quan sát khi nào nghiệm số còn bám profile vật lý và khi nào bắt đầu mất ổn định." path="interactives/chapter13/cfl-condition-vi.html" height="640px" %}

### 5. Bài toán mẫu có bối cảnh thực

Cho phương trình vận chuyển $$ u_t + c u_x = 0 $$ (với $$ c>0 $$) và lược đồ upwind tường minh:
$$
u_j^{n+1}=u_j^n-\nu(u_j^n-u_{j-1}^n),\qquad \nu=\frac{c\Delta t}{\Delta x}.
$$
Lược đồ ổn định khi và chỉ khi $$ 0\le \nu \le 1 $$. Đây chính là ràng buộc CFL tiêu biểu trong mô phỏng sóng và dòng chảy.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm trực giác điều kiện CFL và mối liên hệ giữa tính nhất quán, ổn định và hội tụ.

**Bậc sau đại học.** Kết nối với phân tích von Neumann, phương pháp năng lượng và các tiêu chuẩn ổn định cho PDE phi tuyến.

## Video tham khảo

- xem trước: [Harvard AM205 video 3.18 - CFL condition & upwinding](https://www.youtube.com/watch?v=GsilBPN8Ew4) — Chris Rycroft, tiếng Anh. Giải thích điều kiện CFL và lược đồ upwind cho phương trình đối lưu.
- [Von Neumann analysis: derivation of the CFL criterion](https://www.youtube.com/watch?v=5_VtrWGaEGM) — LMU Seismology, tiếng Anh. Dẫn xuất tiêu chuẩn CFL bằng phân tích ổn định von Neumann.
- [Stability of Forward Euler and Backward Euler Integration Schemes for Differential Equations](https://www.youtube.com/watch?v=RdXCGnTT6UY) — Steve Brunton, tiếng Anh. Liên hệ với phiên bản ODE của điều kiện ổn định cho phương pháp Euler.
