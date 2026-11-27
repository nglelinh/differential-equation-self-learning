---
layout: post
title: "Giới Thiệu Phần Tử Hữu Hạn"
chapter: '13'
order: 7
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter13
lesson_type: optional
---

![Lưới phần tử hữu hạn và các hàm cơ sở cục bộ]({{ site.imgurl }}/chapter_img/chapter13/07_finite_element_introduction.svg)

Phương pháp sai phân hữu hạn (FDM) tuyệt vời trên hình vuông, nhưng hãy thử phủ lưới ô vuông lên một cánh tuabin máy bay hay động mạch chủ uốn lượn—biên cong sẽ bị cắt nham nhở như bậc thang! **Phương pháp Phần tử Hữu hạn (Finite Element Method — FEM)** kết hợp trực tiếp **Dạng yếu $H^1$** của Chương 12 với nghệ thuật chia miền thành các tam giác nhỏ linh hoạt và xấp xỉ nghiệm bằng tổ hợp tuyến tính của các "hàm mũ nón" địa phương—tạo nên công cụ mô phỏng kỹ thuật quyền năng nhất thế kỷ XX–XXI!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Phần tử Hữu hạn (FEM)

1. **Từ Dạng yếu Vô hạn chiều sang Bài toán Galerkin Hữu hạn chiều**:
   Thay không gian $V = H_0^1(\Omega)$ bằng không gian con hữu hạn chiều $V_h = \operatorname{span}\{\phi_1, \dots, \phi_N\}$, yêu cầu $a(u_h, v_h) = \ell(v_h)\;\forall v_h \in V_h$ lập tức dẫn tới hệ tuyến tính $K\mathbf{c} = \mathbf{F}$ với **ma trận độ cứng** $K_{ij} = a(\phi_j, \phi_i)$ và **vector tải** $F_i = \ell(\phi_i)$.
2. **Hàm Cơ sở Mũ nón (Hat Functions) & Tính Thưa Tuyệt đối**:
   Mỗi hàm cơ sở $\phi_i$ bằng $1$ tại đúng nút $x_i$ và bằng $0$ tại mọi nút khác, nên giá trị của nó chỉ khác $0$ trên vài phần tử kề quanh $x_i$. Hệ quả: $K_{ij} = 0$ hầu hết mọi nơi, ma trận $K$ cực kỳ thưa!
3. **Tính Trực giao Galerkin và Bổ đề Céa**:
   Sai số $e = u - u_h$ vuông góc với toàn bộ không gian xấp xỉ theo tích vô hướng năng lượng: $a(u - u_h, v_h) = 0\;\forall v_h \in V_h$. Do đó $u_h$ là **hình chiếu năng lượng tối ưu** của nghiệm thật lên $V_h$!
4. **Lắp ghép theo từng Phần tử (Element-by-Element Assembly)**:
   Trong thực tế lập trình, máy tính không tích phân trên cả miền mà tính ma trận nhỏ trên từng phần tử tam giác/đoạn thẳng chuẩn rồi cộng dồn vào ma trận toàn cục $K$—xử lý mượt mà vật liệu nhiều lớp lẫn biên cong!

## Mục tiêu

Bài học tùy chọn này giới thiệu phương pháp phần tử hữu hạn (FEM) như bước chuyển tự nhiên từ dạng yếu của PDE sang tính toán số. Sau bài học, sinh viên cần hiểu ý tưởng chia miền thành các phần tử nhỏ, xây dựng hàm cơ sở có giá cục bộ, thiết lập hệ phương trình tuyến tính từ dạng yếu, và nhận ra ưu thế của FEM trên các miền hình học phức tạp.

## Kiến thức nền

Sinh viên cần nắm dạng yếu của PDE, không gian $$ H^1_0(\Omega) $$ và kiến thức cơ bản về sai phân hữu hạn. Khác với sai phân hữu hạn xuất phát từ việc xấp xỉ trực tiếp đạo hàm, FEM xuất phát từ dạng biến phân và việc chọn không gian hàm xấp xỉ.

## Dẫn nhập

Nếu sai phân hữu hạn đặt câu hỏi "xấp xỉ đạo hàm tại nút lưới bằng hiệu như thế nào?", thì phần tử hữu hạn đặt câu hỏi "chọn không gian con hữu hạn chiều nào để tìm nghiệm xấp xỉ mà vẫn bảo toàn cấu trúc biến phân và năng lượng của bài toán?". Thay vì rời rạc hóa trực tiếp toán tử vi phân, FEM rời rạc hóa không gian hàm.

Cách tiếp cận này đặc biệt hiệu quả khi miền có hình học phức tạp (biên cong, lỗ khoét) hoặc khi mô hình vật lý được phát biểu tự nhiên qua nguyên lý năng lượng như trong cơ học đàn hồi, truyền nhiệt và cơ học vật rắn.


### Giải thích: Lắp ghép và giải tay bài toán FEM 1 phần tử cho $-u'' = 2$ trên $(0, 1)$

Giải dạng yếu $\int_0^1 u' v'\,dx = \int_0^1 2v\,dx$ với $u(0) = u(1) = 0$ chỉ dùng **1 nút trong** tại $x_1 = \frac{1}{2}$ và 1 hàm mũ nón duy nhất:
$$\phi_1(x) = \begin{cases} 2x, & 0 \le x \le \tfrac{1}{2}, \\ 2(1 - x), & \tfrac{1}{2} \le x \le 1. \end{cases}$$
1. **Tính ma trận độ cứng $K_{11}$** (lưu ý $\phi_1'(x) = +2$ trên $(0, \tfrac{1}{2})$ và $-2$ trên $(\tfrac{1}{2}, 1)$, nên $(\phi_1')^2 = 4$ khắp đoạn):
   $$K_{11} = \int_0^1 \big(\phi_1'(x)\big)^2\,dx = \int_0^1 4\,dx = \mathbf{4}.$$
2. **Tính vector tải $F_1$** (diện tích tam giác đáy $1$, cao $1$ bằng $\frac{1}{2}$):
   $$F_1 = \int_0^1 2\phi_1(x)\,dx = 2 \times \frac{1}{2} = \mathbf{1}.$$
3. **Giải phương trình $K_{11} c_1 = F_1$**:
   $$4 c_1 = 1 \implies c_1 = \mathbf{0{,}25}.$$
   Kiểm tra với nghiệm đúng $u(x) = x(1 - x)$ tại $x = \frac{1}{2}$: $u\left(\frac{1}{2}\right) = \frac{1}{2}\cdot\frac{1}{2} = \mathbf{0{,}25}$—chính xác **100% tại nút** ngay cả khi lưới chỉ có đúng 1 ẩn số!
## Khái niệm theo ba cách

### Cách trực giác

Để dựng một bề mặt cong phức tạp, ta có thể ghép nhiều mảnh phẳng nhỏ lại với nhau: mỗi mảnh có hình dạng đơn giản, nhưng ghép khéo trên một lưới phù hợp sẽ xấp xỉ sát hình dạng toàn cục. FEM áp dụng đúng nguyên lý đó cho nghiệm PDE bằng cách tổ hợp các hàm đơn giản xác định cục bộ trên từng phần tử.

### Cách hình ảnh

Chia một đoạn thẳng thành các đoạn con (phần tử) và tại mỗi nút gắn một hàm "mũ chóp" (hat function) nhận giá trị 1 tại nút đó, bằng 0 tại mọi nút khác và tuyến tính trên mỗi phần tử kề. Khi đó, nghiệm gần đúng là tổ hợp tuyến tính của các hàm cơ sở cục bộ này.

### Cách hình thức

Xuất phát từ dạng yếu của bài toán Poisson:

$$
\int_\Omega \nabla u\cdot\nabla v\,dx=\int_\Omega fv\,dx
\qquad \forall v\in H^1_0(\Omega),
$$

ta chọn một không gian con hữu hạn chiều $$ V_h\subset H^1_0(\Omega) $$ và tìm $$ u_h\in V_h $$ sao cho:

$$
\int_\Omega \nabla u_h\cdot\nabla v_h\,dx=\int_\Omega fv_h\,dx
\qquad \forall v_h\in V_h.
$$

Nếu $$ \{\phi_1,\dots,\phi_N\} $$ là một cơ sở của $$ V_h $$, ta viết:

$$ u_h=\sum_{j=1}^N U_j\phi_j, $$

rồi chọn lần lượt $$ v_h=\phi_i $$ để thu được hệ phương trình tuyến tính cho các ẩn số $$ U_j $$.

## Ngộ nhận thường gặp

### “FEM chỉ là một biến thể phức tạp hơn của sai phân hữu hạn”

Không đúng. Hai phương pháp xuất phát từ hai cơ sở toán học khác nhau: sai phân hữu hạn rời rạc hóa dạng mạnh, còn FEM rời rạc hóa dạng yếu trên không gian con hữu hạn chiều.

### “Phần tử hữu hạn nghĩa là nghiệm bị cắt rời thành các mảnh gián đoạn”

Sai. Trong FEM chuẩn (conforming FEM), nghiệm xấp xỉ $$ u_h $$ liên tục trên toàn miền dù được xây dựng từ các đa thức cục bộ trên từng phần tử.

### “Hàm cơ sở phải xác định trên toàn miền mới đạt độ chính xác cao”

Không đúng. Chính giá cục bộ (local support) của hàm cơ sở tạo ra ma trận thưa và hiệu quả tính toán cao cho FEM.

### “Miền càng phức tạp thì công thức FEM càng rối”

Ngược lại, FEM giữ nguyên cùng một quy trình lắp ghép trên các lưới tam giác hoặc tứ diện, nên đặc biệt thuận lợi cho miền có hình học phức tạp.

## Tiến trình học

### Bước 1: Xuất phát từ dạng yếu

Nhắc lại dạng biến phân của bài toán Poisson làm điểm khởi đầu.

### Bước 2: Chọn không gian con hữu hạn chiều $$ V_h $$

Làm rõ ý nghĩa của tham số kích thước lưới $$ h $$.

### Bước 3: Biểu diễn nghiệm theo cơ sở cục bộ

Chuyển bài toán biến phân vô hạn chiều thành hệ đại số tuyến tính hữu hạn chiều.

### Bước 4: Nhận diện tính thưa (sparsity) của ma trận

Vì các hàm cơ sở chỉ khác 0 trên các phần tử kề nút tương ứng, phần lớn phần tử của ma trận hệ số bằng 0.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao FEM gắn trực tiếp với dạng yếu hay không?
- Sinh viên có nắm rõ định nghĩa và tính chất của hàm cơ sở mũ chóp hay không?
- Sinh viên có giải thích được vì sao ma trận độ cứng của FEM thường là ma trận thưa hay không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm cơ sở mũ chóp trên đoạn $$ [0,1] $$

Chia đoạn $$ [0,1] $$ bằng một dãy nút lưới. Hàm cơ sở $$ \phi_i $$ bằng 1 tại nút $$ i $$, bằng 0 tại mọi nút khác và biến thiên tuyến tính trên hai phần tử kề nút $$ i $$. Đây là hàm cơ sở tiêu chuẩn của FEM bậc nhất.

### Ví dụ 2: Biểu diễn nghiệm xấp xỉ

Với ba nút trong, ta viết $$ u_h=U_1\phi_1+U_2\phi_2+U_3\phi_3 $$. Bài toán PDE ban đầu được quy về tìm ba hệ số $$ U_1,U_2,U_3 $$ — cũng chính là giá trị xấp xỉ của nghiệm tại ba nút đó.

### Ví dụ 3: Thiết lập ma trận độ cứng

Chọn từng hàm thử $$ v_h=\phi_i $$, ta thu được hệ phương trình:

$$
\sum_j U_j\int_\Omega \nabla \phi_j\cdot\nabla \phi_i\,dx
=
\int_\Omega f\phi_i\,dx.
$$

Viết dưới dạng ma trận, đây là hệ $$ KU=F $$, trong đó $$ K $$ gọi là ma trận độ cứng (stiffness matrix).

### Ví dụ 4: Nguồn gốc tính thưa của ma trận

Hai hàm cơ sở gắn với hai nút không thuộc chung phần tử nào sẽ có giá không giao nhau, nên:

$$ \int_\Omega \nabla \phi_j\cdot\nabla \phi_i\,dx=0. $$

Do đó phần lớn các phần tử của ma trận $$ K $$ bằng 0, giúp lưu trữ và giải hệ rất hiệu quả.

## Câu hỏi khái niệm

1. Vì sao FEM bắt đầu từ dạng yếu thay vì xấp xỉ đạo hàm từng điểm?
2. Giá cục bộ của các hàm cơ sở mang lại lợi ích tính toán gì?
3. Vì sao FEM có lợi thế nổi bật hơn sai phân hữu hạn trên lưới đều khi miền có hình học phức tạp?

## Bài toán ứng dụng

1. Trong phân tích ứng suất của khung máy có hình dạng phức tạp, vì sao FEM là công cụ tiêu chuẩn?
2. Trong bài toán truyền nhiệt trên miền có biên cong hoặc lỗ khoét, FEM khắc phục hạn chế nào của sai phân hữu hạn?
3. Trong cơ học sinh học, việc chia lưới tam giác hoặc tứ diện cho mô mềm có ý nghĩa gì?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu không thể tìm nghiệm trên toàn bộ không gian vô hạn chiều $$ H^1_0(\Omega) $$, ta thu hẹp bài toán bằng cách nào?
- Vì sao tổ hợp các hàm tuyến tính từng khúc vẫn xấp xỉ tốt một nghiệm cong trơn?
- Tính cục bộ của hàm cơ sở ảnh hưởng thế nào đến cấu trúc ma trận $$ K $$?

### Hoạt động gợi ý

- Cho sinh viên tự vẽ ba hàm mũ chóp trên đoạn $$ [0,1] $$ và tính vài phần tử của ma trận $$ K $$.
- Minh họa quá trình ghép các phần tử tam giác trên một miền 2D có lỗ khoét.
- So sánh trực tiếp ma trận thu được từ sai phân hữu hạn và FEM trên cùng bài toán Poisson 1D.

### Cách tăng tham gia

- Mở đầu bằng hình ảnh ghép bề mặt từ các mảnh phẳng nhỏ.
- Mời sinh viên tự viết biểu thức tổ hợp tuyến tính của nghiệm xấp xỉ $$ u_h $$.
- Liên hệ tính thưa của ma trận $$ K $$ với cấu trúc láng giềng trên đồ thị lưới.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung hoàn toàn vào FEM một chiều trước khi sang hai chiều.
- Chọn lưới ít nút (ví dụ 3 nút trong) để tính trực tiếp được cả ma trận $$ K $$.
- Nhấn mạnh quy trình bốn bước: dạng yếu $$ \to $$ không gian con $$ V_h $$ $$ \to $$ hàm cơ sở $$ \to $$ hệ tuyến tính $$ KU=F $$.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu trực giác và chứng minh bổ đề Céa (Céa's lemma).
- So sánh phần tử bậc nhất ($$ P_1 $$) và phần tử bậc hai ($$ P_2 $$).
- Phân tích tốc độ hội tụ sai số theo kích thước lưới $$ h $$ trong chuẩn $$ H^1 $$ và $$ L^2 $$.

## Ghi nhớ nhanh

Phương pháp phần tử hữu hạn rời rạc hóa không gian nghiệm trong dạng yếu bằng các hàm cơ sở có giá cục bộ, nhờ đó bảo toàn cấu trúc năng lượng, tạo ra hệ ma trận thưa và thích nghi tốt với miền hình học phức tạp.

---

## Ứng dụng thực tế

### 1. Phân tích ứng suất và biến dạng trong kết cấu

Trong cơ học kết cấu, bài toán đàn hồi được viết dưới dạng yếu và giải bằng FEM trên lưới tam giác hoặc tứ diện, phù hợp với hình học phức tạp của chi tiết máy, cầu đường hay cấu trúc xương sinh học.

### 2. Truyền nhiệt trên miền cong hoặc có lỗ khoét

Miền kỹ thuật thực tế hiếm khi là hình chữ nhật đơn giản. FEM cho phép chia lưới không cấu trúc bám sát biên cong, lỗ khoan và làm mịn cục bộ tại những vùng cần độ chính xác cao.

### 3. Dòng chảy và cơ học sinh học

Trong mô phỏng dòng máu hoặc biến dạng mô mềm, FEM kết hợp với làm mịn lưới thích nghi và các bộ giải hệ thưa kích thước lớn tạo thành công cụ chủ lực của tính toán khoa học hiện đại.

## Trực giác sâu hơn

Điểm khác biệt cốt lõi của FEM là bắt đầu từ không gian hàm và dạng biến phân thay vì xấp xỉ đạo hàm từng điểm. Vì thế, FEM không phải là "sai phân hữu hạn viết phức tạp hơn" mà là hiện thực hóa trực tiếp lý thuyết nghiệm yếu và định lý Lax–Milgram trong không gian hữu hạn chiều.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 6)

def hat(i, x_grid, xs):
    y = np.zeros_like(xs)
    for k, s in enumerate(xs):
        if i > 0 and x_grid[i-1] <= s <= x_grid[i]:
            y[k] = (s - x_grid[i-1]) / (x_grid[i] - x_grid[i-1])
        elif i < len(x_grid)-1 and x_grid[i] <= s <= x_grid[i+1]:
            y[k] = (x_grid[i+1] - s) / (x_grid[i+1] - x_grid[i])
    return y

xs = np.linspace(0, 1, 500)
plt.figure(figsize=(9, 5))
for i in range(1, len(x)-1):
    plt.plot(xs, hat(i, x, xs), label=f'phi_{i}')
plt.scatter(x, np.zeros_like(x), color='black')
plt.title('Các hàm cơ sở mũ chóp trong FEM 1D')
plt.xlabel('x')
plt.ylabel('Giá trị basis')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `p5.js` để cho phép kéo các nút lưới trên đoạn thẳng hoặc tam giác và quan sát trực tiếp sự thay đổi của các hàm cơ sở cục bộ.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `finite element hat functions visualization`, `FEM mesh animation`, hoặc `Poisson equation finite element tutorial`.

## Minh họa tương tác trên web

{% include interactive-frame.html title="Hàm cơ sở mũ chóp trong FEM 1D" description="Điều chỉnh số nút lưới và basis đang xét để thấy trực tiếp tính cục bộ của các hàm cơ sở phần tử hữu hạn." path="interactives/chapter13/finite-element-basis-vi.html" height="620px" %}

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào FEM một chiều, hàm cơ sở mũ chóp, thiết lập hệ từ dạng yếu và cấu trúc ma trận thưa.

### Mức sau đại học (Graduate)

Đi sâu vào bổ đề Céa, ước lượng sai số tiên nghiệm và hậu nghiệm theo $$ h $$, phần tử bậc cao, làm mịn lưới thích nghi và so sánh FEM với phương pháp phổ và thể tích hữu hạn.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 13]({{ site.baseurl }}/contents/vi/chapter13/13_09_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Kết cấu cơ học và đàn hồi
- Bài toán: Xử lý hình học phức tạp của cầu, xương hay chi tiết cơ khí mà lưới sai phân đều khó đáp ứng.
- Mô hình: Chia miền thành lưới tam giác hoặc tứ diện và tìm nghiệm xấp xỉ trong không gian hữu hạn chiều.
- Giả thiết và giới hạn: Chất lượng sinh lưới và bậc hàm cơ sở ảnh hưởng trực tiếp tới sai số.
- Diễn giải: FEM quy PDE về bài toán cân bằng năng lượng rời rạc trên các phần tử nhỏ.

#### Truyền nhiệt trong chi tiết kỹ thuật
- Bài toán: Mô phỏng truyền nhiệt trên miền có biên cong, lỗ khoét hoặc vật liệu ghép nhiều lớp.
- Mô hình: Rời rạc hóa dạng yếu trên không gian phần tử hữu hạn.
- Giả thiết và giới hạn: Cần kiểm soát chất lượng phần tử lưới để tránh suy biến ma trận.
- Diễn giải: FEM khai thác trực tiếp khuôn khổ nghiệm yếu đã xây dựng ở Chương 12.

### 2. Trực giác bổ sung và các kết nối

FEM bắt đầu từ dạng yếu và không gian xấp xỉ hữu hạn chiều nên gắn kết trực tiếp với không gian Sobolev và định lý Lax–Milgram. Đằng sau các phần mềm mô phỏng thương mại là một nền tảng giải tích chặt chẽ về xấp xỉ tối ưu và hội tụ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.0, 0.3, 0.55, 0.8, 1.0])
values = np.array([0.0, 0.6, 0.2, 0.5, 0.0])

xx = np.linspace(0, 1, 400)
yy = np.interp(xx, nodes, values)

plt.plot(xx, yy, label="xap xi phan tu huu han bac 1")
plt.plot(nodes, values, "o", label="nut luoi")
plt.legend()
plt.title("Ham co so tuyen tinh tren cac phan tu 1D")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: finite element basis functions visualization
- search: triangulation PDE FEM intuition
- search: weak form to finite element method animation

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ [0,1] $$, nghiệm xấp xỉ phần tử hữu hạn bậc nhất có dạng $$ u_h(x)=\sum_{i=1}^N U_i \phi_i(x) $$, trong đó các $$ \phi_i $$ là hàm cơ sở mũ chóp. Thay vào dạng yếu của $$ -u''=f $$ thu được hệ phương trình tuyến tính $$ KU=F $$, là phiên bản rời rạc trực tiếp của bài toán nghiệm yếu.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm khái niệm lưới, hàm cơ sở mũ chóp và ma trận độ cứng trong một chiều.

**Bậc sau đại học.** Kết nối với bổ đề Céa, làm mịn lưới thích nghi (adaptive refinement) và phương pháp phần tử hữu hạn hỗn hợp (mixed FEM).

## Video tham khảo

- xem trước: [MIT Numerical Methods for PDEs Lecture 17: FEM Error Analysis in Sobolev and L2 norms](https://www.youtube.com/watch?v=nj0fpJUOl64) — Aerodynamic CFD, tiếng Anh. Phân tích sai số của phương pháp phần tử hữu hạn theo chuẩn Sobolev và chuẩn L^2.
- [Lax-Milgram, application to Poisson equation.](https://www.youtube.com/watch?v=s5P3e1FhpTk) — Learn Maths with Dr Alex, tiếng Anh. Dạng yếu của phương trình Poisson làm cơ sở rời rạc hóa cho FEM.
- [Lax-Milgram lemma](https://www.youtube.com/watch?v=w8QjyVug78M) — Numerical Analysis by Julian Roth, tiếng Anh. Bổ đề Lax–Milgram đảm bảo tính đặt chỉnh cho cả bài toán liên tục lẫn bài toán rời rạc FEM.
