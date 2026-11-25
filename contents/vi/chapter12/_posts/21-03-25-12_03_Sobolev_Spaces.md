---
layout: post
title: "Không Gian Sobolev"
chapter: '12'
order: 3
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter12
lesson_type: required
---

![Trực giác về Sobolev space và gradient yếu]({{ site.imgurl }}/chapter_img/chapter12/03_sobolev_spaces.svg )

Không gian $L^2(\Omega)$ đủ rộng và đầy đủ nhưng lại không hề kiểm soát đạo hàm; không gian $C^1(\bar{\Omega})$ kiểm soát được đạo hàm nhưng lại bị "thủng" khi lấy giới hạn (như phản ví dụ Weierstrass đã chỉ ra). **Không gian Sobolev $W^{k,p}(\Omega)$**—và đặc biệt là không gian Hilbert $H^1(\Omega) = W^{1,2}(\Omega)$—là giao điểm hoàn hảo của cả hai thế giới: vừa đo được cả hàm lẫn các đạo hàm yếu tới bậc $k$, vừa **đầy đủ tuyệt đối**!

## Kiến thức cần nhớ: Bốn trụ cột của Không gian Sobolev $W^{k,p}(\Omega)$

1. **Định nghĩa và Chuẩn Sobolev**:
   $W^{k,p}(\Omega)$ gồm mọi hàm $u \in L^p(\Omega)$ sao cho mọi đạo hàm yếu $D^\alpha u$ ($|\alpha| \le k$) đều nằm trong $L^p(\Omega)$, với chuẩn $\|u\|_{W^{k,p}} = \left(\sum_{|\alpha|\le k} \|D^\alpha u\|_{L^p}^p\right)^{1/p}$.
2. **Không gian Hilbert $H^k(\Omega) = W^{k,2}(\Omega)$**:
   Khi $p = 2$, $H^1(\Omega)$ có tích vô hướng $\langle u, v \rangle_{H^1} = \int_\Omega (uv + \nabla u \cdot \nabla v)\,dx$. Trong vật lý, $\int |\nabla u|^2\,dx$ chính là năng lượng đàn hồi hay năng lượng tĩnh điện hữu hạn!
3. **Không gian biên $0$: $H_0^1(\Omega)$ và Toán tử Vết (Trace Operator)**:
   $H_0^1(\Omega)$ là bao đóng của $C_c^\infty(\Omega)$ trong $H^1(\Omega)$—nơi ở tự nhiên cho bài toán Dirichlet thuần nhất $u|_{\partial\Omega} = 0$. Dù phần tử $H^1$ chỉ xác định hầu khắp nơi, định lý Vết vẫn cho phép gán giá trị biên $T u \in L^2(\partial\Omega)$ một cách hoàn toàn chặt chẽ!
4. **Bất đẳng thức Poincaré trên $H_0^1(\Omega)$**:
   Trên miền bị chặn $\Omega$, $\|u\|_{L^2} \le C_P \|\nabla u\|_{L^2}$ với mọi $u \in H_0^1(\Omega)$—nghĩa là chỉ riêng nửa chuẩn năng lượng $\|\nabla u\|_{L^2}$ đã là một chuẩn tương đương trọn vẹn trên $H_0^1(\Omega)$!

## Mục tiêu

Bài học này xây dựng không gian Sobolev — khuôn khổ cho phép đo đồng thời độ lớn của bản thân hàm và các đạo hàm yếu của nó. Sau bài học, sinh viên cần nắm định nghĩa $$ W^{k,p} $$, ý nghĩa đặc biệt của $$ H^k=W^{k,2} $$, vai trò của $$ H^1_0 $$ trong bài toán biên, và trực giác về cách nhúng Sobolev nối kết kiểm soát năng lượng với tính trơn của hàm.

## Kiến thức nền

Sinh viên cần nắm không gian $$ L^p $$, đạo hàm yếu, chuẩn, tích vô hướng và khái niệm cơ bản về bài toán biên Dirichlet. Trong lý thuyết PDE, độ trơn cổ điển thường không được giả định ngay từ đầu mà là kết quả suy ra sau khi đã chứng minh sự tồn tại nghiệm yếu.

## Dẫn nhập

Khi nghiên cứu PDE, chỉ biết hàm có tích phân hữu hạn trong $$ L^p $$ thường chưa đủ; ta cần kiểm soát thêm độ dốc, độ cong hoặc các đạo hàm bậc cao hơn. Tuy nhiên, nếu đòi hỏi đạo hàm cổ điển thì lớp hàm lại quá hẹp và loại bỏ nhiều nghiệm có ý nghĩa vật lý. Không gian Sobolev giải quyết cân bằng này: đủ rộng để chứa nghiệm yếu nhưng vẫn đủ chặt để bảo toàn cấu trúc hình học và năng lượng.


### Giải thích: Tính tay chính xác chuẩn $H^1(0, 1)$ của một "hàm mũ nón" phần tử hữu hạn

Xét hàm mũ nón (hat function) có góc nhọn tại giữa đoạn $\Omega = (0, 1)$:
$$u(x) = \begin{cases} x, & 0 \le x \le \tfrac{1}{2}, \\ 1 - x, & \tfrac{1}{2} \le x \le 1. \end{cases}$$
1. **Tính phần $L^2$ của hàm $u$**:
   $$\|u\|_{L^2}^2 = 2\int_0^{1/2} x^2\,dx = 2\left[\frac{x^3}{3}\right]_0^{1/2} = \frac{2}{24} = \mathbf{\frac{1}{12}}.$$
2. **Tính phần $L^2$ của đạo hàm yếu $u'$**:
   Đạo hàm yếu là $u'(x) = +1$ trên $(0, \tfrac{1}{2})$ và $u'(x) = -1$ trên $(\tfrac{1}{2}, 1)$, nên $(u'(x))^2 = 1$ hầu khắp nơi:
   $$\|u'\|_{L^2}^2 = \int_0^1 1\,dx = \mathbf{1}.$$
3. **Cộng lại ra chuẩn $H^1(0, 1)$**:
   $$\|u\|_{H^1} = \sqrt{\frac{1}{12} + 1} = \sqrt{\frac{13}{12}} \approx \mathbf{1{,}0408} < \infty.$$
   Vì $u(0) = u(1) = 0$ và liên tục từng khúc, ta có $u \in H_0^1(0, 1)$—đó là lý do các hàm mũ nón gãy khúc trở thành viên gạch cơ bản của Phương pháp Phần tử Hữu hạn (FEM)!
## Khái niệm theo ba cách

### Cách trực giác

Hãy hình dung một tấm vải căng: để đánh giá tấm vải phẳng hay nhăn, ta không chỉ đo độ cao mà còn phải đo độ dốc biến thiên mạnh hay nhẹ. Chuẩn Sobolev đo đồng thời cả hai yếu tố đó: độ lớn của chính hàm và độ lớn của các đạo hàm yếu.

### Cách hình ảnh

Một hàm có thể liên tục nhưng dao động rất gắt, hoặc ngược lại có giá trị lớn nhưng biến thiên chậm. Chuẩn $$ L^2 $$ đơn thuần không phân biệt được mức độ dao động, trong khi không gian Sobolev nắm bắt được cả biên độ lẫn gradient. Việc so sánh hai hàm có cùng chuẩn $$ L^2 $$ nhưng gradient rất khác nhau cho thấy rõ lý do cần đến chuẩn Sobolev.

### Cách hình thức

Với $$ k\in\mathbb{N} $$ và $$ 1\le p\le\infty $$, không gian Sobolev được định nghĩa là:

$$
W^{k,p}(\Omega)=\left\{u\in L^p(\Omega):D^\alpha u\in L^p(\Omega)\ \text{với mọi }\lvert \alpha\rvert\le k\right\},
$$

trong đó các đạo hàm $$ D^\alpha u $$ hiểu theo nghĩa yếu.

Khi $$ p=2 $$, ta ký hiệu $$ H^k(\Omega)=W^{k,2}(\Omega) $$. Đặc biệt, chuẩn $$ H^1 $$ được cho bởi:

$$
\lVert u\rVert_{H^1}^2=\lVert u\rVert_{L^2}^2+\lVert \nabla u\rVert_{L^2}^2.
$$

Không gian $$ H^1_0(\Omega) $$ là bao đóng của $$ C_c^\infty(\Omega) $$ theo chuẩn $$ H^1 $$, dùng để biểu diễn điều kiện biên Dirichlet thuần nhất.

## Ngộ nhận thường gặp

### “Không gian Sobolev chỉ là không gian $$ L^p $$ của đạo hàm”

Chưa đủ. Cần cả bản thân hàm và mọi đạo hàm yếu đến bậc $$ k $$ đều thuộc $$ L^p $$.

### “Hàm không trơn thì không thể thuộc không gian Sobolev”

Sai. Nhiều hàm có góc nhọn, như $$ \lvert x\rvert $$ trên khoảng hữu hạn, vẫn thuộc $$ H^1 $$.

### “$$ H^1_0 $$ nghĩa là hàm bằng 0 tại mọi điểm biên theo nghĩa cổ điển”

Không hoàn toàn đúng. Điều kiện biên trong không gian Sobolev được hiểu thông qua toán tử vết biên (trace) hoặc qua phép lấy bao đóng của các hàm trơn có giá compact.

### “Nhúng Sobolev luôn đảm bảo tính liên tục”

Sai. Kết quả nhúng phụ thuộc trực tiếp vào bậc đạo hàm $$ k $$, số chiều không gian và chỉ số $$ p $$.

## Tiến trình học

### Bước 1: Xuất phát từ đạo hàm yếu

Nhắc lại rằng đạo hàm yếu cho phép định nghĩa phép vi phân cho các hàm không trơn; không gian Sobolev là tập hợp các hàm có đủ đạo hàm yếu khả tích.

### Bước 2: Tập trung vào $$ H^1 $$

Đây là không gian phổ biến nhất trong PDE elliptic, với chuẩn:

$$
\lVert u\rVert_{H^1}^2=\lVert u\rVert_{L^2}^2+\lVert \nabla u\rVert_{L^2}^2.
$$

### Bước 3: Giới thiệu $$ H^1_0 $$

Làm rõ đây là không gian hàm tự nhiên cho nhiều bài toán biên Dirichlet thuần nhất.

### Bước 4: Hiểu trực giác về định lý nhúng Sobolev

Kiểm soát đủ nhiều đạo hàm yếu sẽ hạn chế hành vi dao động bất thường của hàm — đây là cầu nối giữa năng lượng hữu hạn và tính trơn.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao $$ \lvert x\rvert $$ thuộc $$ H^1(-1,1) $$ hay không?
- Sinh viên có phân biệt được $$ H^1 $$ và $$ H^1_0 $$ hay không?
- Sinh viên có hiểu vì sao số chiều không gian ảnh hưởng đến các kết quả nhúng Sobolev hay không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm tuyến tính trên khoảng

Xét $$ u(x)=x $$ trên $$ (0,1) $$. Ta có $$ u\in L^2(0,1) $$ và đạo hàm yếu $$ u'=1\in L^2(0,1) $$, nên $$ u\in H^1(0,1) $$. Tuy nhiên, do $$ u(1)\ne 0 $$ nên $$ u\notin H^1_0(0,1) $$.

### Ví dụ 2: Hàm giá trị tuyệt đối

Xét $$ u(x)=\lvert x\rvert $$ trên $$ (-1,1) $$:

- Bản thân hàm thuộc $$ L^2(-1,1) $$.
- Đạo hàm yếu bằng $$ -1 $$ trên $$ (-1,0) $$ và $$ 1 $$ trên $$ (0,1) $$, thuộc $$ L^2(-1,1) $$.

Vậy $$ \lvert x\rvert\in H^1(-1,1) $$.

### Ví dụ 3: Hàm có điểm kỳ dị mạnh

Xét $$ u(x)=x^{-1/2} $$ trên $$ (0,1) $$. Vì $$ u\notin L^2(0,1) $$ nên chắc chắn $$ u\notin H^1(0,1) $$. Ví dụ này nhấn mạnh rằng để thuộc không gian Sobolev, trước hết chính bản thân hàm phải đủ khả tích.

### Ví dụ 4: Hàm trơn có giá compact

Nếu $$ u\in C_c^\infty(\Omega) $$ thì mọi đạo hàm của $$ u $$ đều trơn và có giá compact, nên thuộc mọi $$ L^p(\Omega) $$ trên miền bị chặn. Do đó $$ u\in W^{k,p}(\Omega) $$ với mọi $$ k $$ và mọi $$ p $$ hữu hạn. Đây là lớp hàm cơ sở dùng để xây dựng các không gian Sobolev thông qua phép lấy bao đóng.

## Câu hỏi khái niệm

1. Vì sao $$ H^1 $$ là không gian làm việc tự nhiên hơn $$ C^1 $$ trong nhiều bài toán PDE?
2. Tại sao chuẩn $$ H^1 $$ phải bao gồm cả chuẩn $$ L^2 $$ của chính hàm lẫn của gradient?
3. Vì sao kết quả nhúng Sobolev phụ thuộc vào số chiều không gian?

## Bài toán ứng dụng

1. Trong bài toán màng đàn hồi, vì sao năng lượng biến dạng liên hệ trực tiếp với $$ \lVert \nabla u\rVert_{L^2} $$?
2. Trong xử lý ảnh, việc thêm số hạng phạt gradient trong các mô hình làm mịn ảnh liên hệ như thế nào với chuẩn Sobolev?
3. Trong cơ học vật rắn, tại sao trường chuyển vị có năng lượng hữu hạn thường được đặt trong không gian Sobolev thay vì không gian hàm trơn cổ điển?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Một hàm có góc nhọn có thể vẫn mang năng lượng biến dạng hữu hạn không?
- Tại sao bài toán biên Dirichlet thuần nhất cần đến $$ H^1_0 $$ thay vì toàn bộ $$ H^1 $$?
- Một chuẩn chỉ đo độ lớn của bản thân hàm có đủ kiểm soát hành vi đạo hàm hay không?

### Hoạt động gợi ý

- Cho sinh viên phân loại các hàm mẫu vào $$ L^2 $$, $$ H^1 $$ và $$ H^1_0 $$.
- So sánh đồ thị hai hàm có cùng chuẩn $$ L^2 $$ nhưng gradient rất khác nhau.
- Thảo luận nhóm về ý nghĩa vật lý của chuẩn gradient trong biểu thức năng lượng.

### Cách tăng tham gia

- Yêu cầu sinh viên diễn đạt định nghĩa $$ H^1 $$ bằng lời không dùng ký hiệu.
- Cho dự đoán trước khi tính toán xem một hàm có thuộc $$ H^1 $$ hay không.
- Đề nghị mỗi nhóm tự xây dựng một ví dụ hàm thuộc $$ H^1 $$ nhưng không khả vi cổ điển.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Làm việc trên miền một chiều trước khi chuyển sang nhiều chiều.
- Khai thác các ví dụ quen thuộc như $$ x $$, $$ \lvert x\rvert $$, $$ x^2 $$.
- Tóm tắt ngắn gọn: không gian Sobolev gồm các hàm có cả bản thân hàm và đạo hàm yếu khả tích.

### Thử thách cho sinh viên khá giỏi

- Chứng minh $$ H^1(\Omega) $$ là không gian Hilbert.
- Tìm hiểu khái niệm toán tử vết biên (trace) trên $$ H^1 $$.
- Phân tích các định lý nhúng Sobolev vào $$ L^q $$ ứng với các số chiều không gian khác nhau.

## Ghi nhớ nhanh

Không gian Sobolev kiểm soát đồng thời giá trị của hàm và độ lớn của các đạo hàm yếu, tạo thành khuôn khổ tự nhiên cho nghiệm yếu, năng lượng hữu hạn và bài toán biên trong PDE hiện đại.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Trường chuyển vị đàn hồi hữu hạn năng lượng
- Bài toán: Trong cơ học môi trường liên tục, điều kiện vật lý thiết yếu là biến dạng bình phương khả tích chứ không nhất thiết trơn cổ điển.
- Mô hình: Không gian $$ H^1(\Omega) $$ chứa các hàm mà cả bản thân hàm và gradient yếu đều thuộc $$ L^2 $$.
- Giả thiết và giới hạn: Mô hình đàn hồi tuyến tính, năng lượng biến dạng dạng toàn phương.
- Diễn giải: Không gian Sobolev là ngôn ngữ tự nhiên cho các bài toán năng lượng đàn hồi.

#### Truyền nhiệt và dòng thấm
- Bài toán: Phân bố nhiệt độ hoặc áp suất trong môi trường không đồng nhất có thể không trơn nhưng vẫn có gradient bình phương khả tích.
- Mô hình: Tìm nghiệm trong $$ H^1 $$ thay vì trong lớp hàm trơn cổ điển.
- Giả thiết và giới hạn: Miền và hệ số vật liệu có thể không trơn.
- Diễn giải: Không gian Sobolev giúp đặt bài toán PDE hợp lệ trên các miền thực tế hơn.

### 2. Trực giác bổ sung và các kết nối

Không gian Sobolev đo đồng thời độ lớn của hàm và độ lớn của đạo hàm yếu, nằm ở khoảng giữa giữa không gian $$ L^2 $$ (không kiểm soát đạo hàm) và $$ C^1 $$ (đòi hỏi tính khả vi liên tục từng điểm). Một sai sót phổ biến là đồng nhất $$ H^1 $$ với lớp hàm khả vi cổ điển, trong khi nhiều phần tử của $$ H^1 $$ chỉ có đạo hàm theo nghĩa yếu.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
u = np.abs(x - 0.5)
v = x * (1 - x)

du = np.gradient(u, x)
dv = np.gradient(v, x)

print("Approx H1 seminorm of u:", np.sqrt(np.trapz(du**2, x)))
print("Approx H1 seminorm of v:", np.sqrt(np.trapz(dv**2, x)))

plt.plot(x, u, label="u=|x-1/2|")
plt.plot(x, v, label="v=x(1-x)")
plt.legend()
plt.title("Hai ham khong tron giong nhau nhung van nam trong H1(0,1)")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Sobolev space intuition H1 finite energy
- search: weak gradient visualization Sobolev spaces
- search: finite element Sobolev space motivation

### 5. Bài toán mẫu có bối cảnh thực

Hàm $$ u(x)=\lvert x-\tfrac12\rvert $$ trên $$ [0,1] $$ không khả vi cổ điển tại $$ x=\tfrac12 $$, nhưng đạo hàm yếu của nó bằng $$ -1 $$ ở bên trái và $$ 1 $$ ở bên phải, nên thuộc $$ L^2(0,1) $$. Do đó $$ u \in H^1(0,1) $$. Ví dụ này minh họa rằng không gian Sobolev chấp nhận các nghiệm có điểm gấp khúc nhưng vẫn hữu hạn năng lượng.

### 6. Phân tầng độ khó

**Bậc đại học.** Làm quen với $$ H^1 $$ như không gian của các hàm hữu hạn năng lượng.

**Bậc sau đại học.** Kết nối với định lý vết biên (trace theorem), phép nhúng compact và định lý Rellich–Kondrachov.

## Video tham khảo

- xem trước: [UPB Math 237 LEC5A Sobolev Spaces](https://www.youtube.com/watch?v=GhBM6L-avYU) — Gilbert Peralta, tiếng Anh. Bài giảng định nghĩa không gian Sobolev từ đạo hàm yếu.
- [Sobolev Spaces Explained | Weak Derivatives, W¹ᵖ and H¹](https://www.youtube.com/watch?v=bUIZGQ7T0rU) — Sciwords, tiếng Anh. Giải thích đạo hàm yếu, W^{1,p} và H^1 trong cùng một bài giảng.
- [Index Theory Lecture 7: Sobolev space theory](https://www.youtube.com/watch?v=Q1JecioLurc) — Masoud Khalkhali, tiếng Anh. Bài giảng chuyên sâu về lý thuyết không gian Sobolev.
