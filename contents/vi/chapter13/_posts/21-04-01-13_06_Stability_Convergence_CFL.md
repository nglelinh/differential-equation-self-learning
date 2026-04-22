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

## Mục tiêu

Bài học này giúp sinh viên hiểu ba khái niệm cốt lõi của phân tích sơ đồ số: consistency, stability, và convergence. Sau bài học, sinh viên cần giải thích được mối liên hệ giữa ba khái niệm đó, hiểu trực giác của điều kiện CFL, và nhận ra rằng một sơ đồ số tốt không chỉ gần đúng phương trình gốc mà còn phải kiểm soát được sai số khi tiến hóa.

## Kiến thức nền

Sinh viên nên nắm sai phân hữu hạn, Euler, và trực giác rằng sai số ban đầu hay sai số làm tròn có thể lan truyền trong thời gian. Bài này là bước phân tích “tính đáng tin” của các sơ đồ đã xây dựng.

## Dẫn nhập

Viết ra một sơ đồ số chỉ là bước đầu. Câu hỏi lớn hơn là: nếu đưa sơ đồ ấy vào máy tính, nó có bám nghiệm thật không? Một sơ đồ có thể trông rất hợp lý nhưng vẫn thất bại vì khuếch đại sai số quá nhanh. Vì vậy, trong giải tích số, xây sơ đồ và kiểm chứng sơ đồ là hai phần không thể tách rời.

Ba ý tưởng nền tảng là:

- consistency: sơ đồ có đúng là đang xấp xỉ phương trình gốc không;
- stability: sai số có bị khuếch đại mất kiểm soát không;
- convergence: khi lưới mịn dần, nghiệm số có tiến về nghiệm thật không.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng bạn chụp ảnh một vật đang chuyển động.

- Nếu ống kính sai lệch với vật thật ngay từ đầu, đó là thiếu consistency.
- Nếu rung máy làm ảnh mờ dần sau mỗi lần chụp, đó là thiếu stability.
- Nếu tăng độ phân giải mà ảnh vẫn không giống vật thật, tức là không convergence.

### Cách hình ảnh

Giáo viên nên vẽ sơ đồ tam giác:

- một đỉnh là consistency,
- một đỉnh là stability,
- đỉnh còn lại là convergence.

Mũi tên mạnh nhất là

$$
\text{consistency}+\text{stability}\Rightarrow \text{convergence}.
$$

Với điều kiện CFL, nên vẽ một nón truyền thông tin vật lý và bước nhảy lưới của sơ đồ để sinh viên thấy thông tin số không được “nhảy xa” hơn tốc độ vật lý cho phép.

### Cách hình thức

Một sơ đồ được gọi là consistent nếu sai số cắt cụt địa phương tiến về 0 khi $$ \Delta t,\Delta x\to 0 $$. Nó được gọi là stable nếu các nhiễu nhỏ trong dữ liệu hay tính toán không bị khuếch đại vô hạn.

Nó converge nếu nghiệm số hội tụ về nghiệm đúng khi lưới mịn dần.

Trong nhiều bài toán tuyến tính đặt chỉnh tốt, định lý Lax cho biết:

$$
\text{consistency}+\text{stability}\Rightarrow \text{convergence}.
$$

Điều kiện CFL thường có dạng

$$ \frac{c\Delta t}{\Delta x}\le C, $$

với $$ c $$ là tốc độ lan truyền đặc trưng.

## Ngộ nhận thường gặp

### “Consistency là đủ”

Sai. Một sơ đồ có thể xấp xỉ phương trình đúng nhưng vẫn nổ do không ổn định.

### “Ổn định nghĩa là nghiệm số không thay đổi”

Không. Ổn định nghĩa là sai số không bị khuếch đại vô lý.

### “CFL là định lý cho mọi bài toán”

Không. Đây là điều kiện điển hình cho nhiều bài toán tiến hóa, đặc biệt kiểu đối lưu hay sóng, chứ không phải công thức vạn năng.

### “Nếu giảm lưới đủ nhỏ thì luôn hội tụ”

Không hẳn. Nếu sơ đồ không ổn định, tinh chỉnh lưới chưa chắc cứu được.

## Tiến trình học

### Bước 1: Kiểm tra consistency

Thay nghiệm đúng vào sơ đồ và xem phần dư có tiến về 0 không.

### Bước 2: Phân tích stability

Theo dõi sự lan truyền của sai số hoặc mode Fourier đơn giản.

### Bước 3: Suy ra convergence

Trong lớp bài toán phù hợp, consistency cộng stability dẫn đến convergence.

### Bước 4: Hiểu CFL như một giới hạn tốc độ

Thông tin vật lý và thông tin số phải “khớp nhịp” với nhau.

### Các điểm kiểm tra hiểu bài

- Sinh viên có diễn đạt được ba khái niệm bằng lời riêng không?
- Sinh viên có thấy vì sao consistency không đủ không?
- Sinh viên có giải thích được ý nghĩa vật lý của CFL không?

## Ví dụ có lời giải

### Ví dụ 1: Consistency của Euler

Thay nghiệm đúng $$ y(t) $$ vào công thức Euler:

$$ \frac{y(t+h)-y(t)}{h}-f(t,y(t)). $$

Khai triển Taylor cho thấy biểu thức này là $$ O(h) $$, nên Euler nhất quán bậc một.

### Ví dụ 2: Ổn định của Euler tiến trên $$ y'=\lambda y $$

Sai số $$ e_n $$ thỏa $$ e_{n+1}=(1+h\lambda)e_n $$. Nếu $$ \lvert 1+h\lambda\rvert>1 $$, sai số tăng theo cấp số nhân. Đây là hình ảnh rõ nhất của mất ổn định.

### Ví dụ 3: Điều kiện CFL cho đối lưu

Xét $$ u_t+cu_x=0 $$. Với một sơ đồ tường minh đơn giản, điều kiện CFL có dạng

$$ \frac{c\Delta t}{\Delta x}\le 1. $$

Nếu vi phạm điều kiện này, sóng số có thể khuếch đại sai lệch và tạo dao động phi thực.

### Ví dụ 4: Consistent nhưng không stable

Một sơ đồ có thể được xây sao cho sai số cắt cụt nhỏ, nhưng nếu mỗi bước khuếch đại sai số lên gấp đôi thì nghiệm số vẫn đi xa khỏi nghiệm thật. Ví dụ khái niệm này giúp sinh viên hiểu vì sao stability là mắt xích trung tâm.

## Câu hỏi khái niệm

1. Vì sao consistency chỉ nói về sơ đồ trong một bước còn stability nói về cả quá trình?
2. Tại sao CFL có thể được hiểu là giới hạn “tốc độ truyền tin” của lưới?
3. Vì sao convergence là đích cuối nhưng không phải thứ nên kiểm tra đầu tiên?

## Bài toán ứng dụng

1. Trong dự báo thời tiết, vì sao bước thời gian không thể chọn chỉ dựa trên tốc độ máy tính?
2. Trong mô phỏng giao thông, nếu xe di chuyển nhanh hơn khả năng “cập nhật” của lưới thì điều gì xảy ra với sơ đồ?
3. Trong mô phỏng sóng nổ, vì sao vi phạm CFL có thể tạo ra kết quả hoàn toàn phi vật lý?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu sơ đồ giống phương trình đúng trong một bước, tại sao vẫn có thể sai hoàn toàn sau nhiều bước?
- Em hiểu “ổn định” là ổn định của cái gì?
- CFL là ràng buộc kỹ thuật hay còn mang ý nghĩa vật lý?

### Hoạt động gợi ý

- Cho sinh viên kiểm tra consistency bằng Taylor trên một sơ đồ đơn giản.
- Dùng mô phỏng để thay đổi tỉ số

$$ \frac{\Delta t}{\Delta x} $$

và quan sát khi nào sơ đồ bắt đầu hỏng.
- Tổ chức thảo luận nhóm: stability là “kìm hãm sai số” hay “bảo vệ vật lý”?

### Cách tăng tham gia

- Bắt đầu bằng một ví dụ số bị nổ dù công thức trông hợp lý.
- Cho sinh viên tự diễn đạt định lý Lax theo ngôn ngữ không hình thức.
- Mời sinh viên dùng trực giác giao thông hoặc sóng để giải thích CFL.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tách riêng ba khái niệm và dùng ví dụ ngắn cho từng khái niệm.
- Ưu tiên giải thích bằng hình hơn bằng chứng minh.
- Dùng bài toán một chiều đơn giản trước.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu phân tích Von Neumann.
- Chứng minh định lý Lax trong bối cảnh đơn giản.
- So sánh CFL của các sơ đồ khác nhau cho phương trình đối lưu.

## Ghi nhớ nhanh

Một sơ đồ số chỉ đáng tin khi vừa nhất quán với PDE gốc, vừa ổn định trước sai số, từ đó mới hội tụ về nghiệm thật. Điều kiện CFL là lời nhắc rằng tốc độ truyền thông tin của sơ đồ phải tương thích với tốc độ vật lý của bài toán.

---

## Ứng dụng thực tế

### 1. Dự báo thời tiết và mô phỏng khí quyển

Trong các mô hình khí quyển, sóng và đối lưu lan thông tin với tốc độ đặc trưng nhất định. Nếu bước thời gian quá lớn so với kích thước lưới, sơ đồ tường minh có thể vi phạm CFL và tạo dao động hoặc bùng nổ hoàn toàn phi vật lý. Mô hình thực tế còn phức tạp hơn nhiều, nhưng trực giác CFL vẫn là nguyên tắc cốt lõi trong mọi solver tiến hóa.

### 2. Giao thông và đối lưu thông tin

Trong mô phỏng giao thông hoặc dòng chảy 1D, điều kiện

$$ \frac{c\Delta t}{\Delta x}\le C $$

cho biết trong một bước thời gian, thông tin không nên nhảy qua quá nhiều ô lưới. Diễn giải vật lý rất rõ: lưới số phải đủ nhanh để “theo kịp” chuyển động của phương tiện hay sóng mật độ.

### 3. Sóng nổ, thủy động lực và CFD

Trong CFD, stability không chỉ là câu chuyện lý thuyết mà quyết định trực tiếp việc mô phỏng có cho ra shock profile hợp lý hay sụp đổ vì nhiễu số. Đây là nơi consistency, stability, và convergence đi từ khái niệm giáo khoa thành điều kiện sống còn của phần mềm tính toán.

## Trực giác sâu hơn

Consistency nói “mỗi bước đang mô phỏng đúng bài toán”; stability nói “những gì nhỏ không bị khuếch đại điên cuồng”; convergence nói “cả quá trình đi đúng nơi cần đến”. Ngộ nhận phổ biến là kiểm tra consistency xong là đủ. Thực ra rất nhiều sơ đồ thất bại không phải vì mô hình cục bộ sai, mà vì sai số nhỏ bị thổi phồng qua thời gian.

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

Có thể dùng `Plotly.js` với thanh trượt tỉ số $$ \Delta t/\Delta x $$ để sinh viên quan sát ngay khi CFL vượt ngưỡng thì nghiệm số bắt đầu méo hoặc mất ổn định.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `CFL condition visualization`, `Von Neumann stability animation`, hoặc `numerical instability advection equation`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào ba khái niệm consistency, stability, convergence và ý nghĩa trực quan của CFL trong bài toán đối lưu, sóng.

### Mức sau đại học (Graduate)

Đi sâu vào phân tích Von Neumann, định lý Lax trong bối cảnh tuyến tính, phổ toán tử tiến hóa rời rạc, và các tiêu chuẩn stability tinh hơn cho PDE số.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dự báo thời tiết và mô hình sóng
- Bài toán: Bước thời gian phải liên hệ đúng với kích thước ô lưới và tốc độ lan truyền.
- Mô hình: Điều kiện CFL cho phương trình vận chuyển hoặc sóng có dạng điển hình
$$ \frac{c\Delta t}{\Delta x}\le C. $$
- Giả thiết và giới hạn: Phụ thuộc lược đồ cụ thể; vi phạm CFL thường làm mô phỏng nổ số.
- Diễn giải: Tín hiệu vật lý không được "đi nhanh hơn" khả năng truyền thông tin trên lưới.

#### Mô phỏng giao thông hoặc dòng chảy
- Bài toán: Các shock và front cần lưới phù hợp để ổn định và bắt đúng cấu trúc lan truyền.
- Mô hình: Phân tích ổn định Fourier hay von Neumann cho lược đồ.
- Giả thiết và giới hạn: Linearization thường chỉ phản ánh một phần hành vi phi tuyến.
- Diễn giải: Stability và convergence không thể tách rời consistency.

### 2. Trực giác bổ sung và các kết nối

Consistency nói lược đồ gần PDE cục bộ; stability nói sai số không bị khuếch đại vô hạn; convergence nói nghiệm số tiến về nghiệm đúng. Định lý Lax-Richtmyer cho thấy consistency cộng stability sinh convergence trong bối cảnh tuyến tính thích hợp. Một bẫy phổ biến là kiểm tra consistency rồi mặc nhiên tin lược đồ hội tụ.

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

Cho phương trình vận chuyển
$$ u_t + c u_x = 0 $$
và lược đồ upwind explicit,
$$
u_j^{n+1}=u_j^n-\nu(u_j^n-u_{j-1}^n),\qquad \nu=\frac{c\Delta t}{\Delta x}.
$$
Lược đồ ổn định khi $$ 0\le \nu \le 1 $$. Đây chính là ràng buộc CFL quen thuộc trong mô phỏng sóng và dòng chảy.

### 6. Phân tầng độ khó

**Bậc đại học.** Hiểu trực giác của CFL và mối liên hệ giữa consistency, stability, convergence.

**Bậc sau đại học.** Kết nối với von Neumann analysis, energy methods và nonlinear stability notions.
