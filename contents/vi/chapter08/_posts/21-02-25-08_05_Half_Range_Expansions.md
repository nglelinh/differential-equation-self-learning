---
layout: post
title: "Khai Triển Nửa Khoảng"
chapter: '08'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter08
lesson_type: required
---
![21 02 25 08 05 Half Range Expansions]({{ site.imgurl }}/chapter_img/chapter08/05_half_range_expansions.svg)

## Mục tiêu

Bài học này giải quyết một tình huống rất thường gặp trong PDE: dữ liệu chỉ được cho trên nửa đoạn $$ [0,L] $$ thay vì trên khoảng đối xứng. Sau bài học, sinh viên cần hiểu ý tưởng mở rộng chẵn và mở rộng lẻ, biết khi nào dùng chuỗi cosine hoặc chuỗi sine, thấy được mối liên hệ trực tiếp với điều kiện biên Dirichlet và Neumann, và biết rằng cùng một dữ liệu trên $$ [0,L] $$ có thể tạo ra hai phổ Fourier khác nhau tùy cách mở rộng.

## Kiến thức nền

Sinh viên nên nắm chắc chuỗi Fourier trên miền đối xứng và vai trò của hàm chẵn, hàm lẻ. Bài này là bước rất quan trọng để kết nối Fourier series với phương pháp tách biến cho phương trình nhiệt và phương trình sóng.

## Dẫn nhập

Nhiều bài toán vật lý không được phát biểu trên đoạn đối xứng $$ [-L,L] $$, mà chỉ trên miền thực sự có ý nghĩa vật lý như $$ [0,L] $$. Khi ấy, nếu cứ bám vào chuỗi Fourier đầy đủ trên miền đối xứng thì ta sẽ lúng túng. Khai triển nửa khoảng là lời giải rất tự nhiên: ta mở rộng dữ liệu sang miền đối xứng theo cách chẵn hoặc lẻ, rồi áp dụng Fourier quen thuộc.

Điều hay của bài này là nó cho sinh viên thấy sự linh hoạt của Fourier. Dữ liệu gốc không đổi trên $$ [0,L] $$, nhưng cách ta tưởng tượng phần ngoài miền đó sẽ quyết định loại mode nào xuất hiện. Đây chính là nơi điều kiện biên và mở rộng hàm gặp nhau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Giả sử bạn chỉ biết hình dáng một sợi dây trên nửa đoạn. Muốn dùng các công cụ Fourier quen thuộc, bạn phải "đoán" phần còn lại bằng một quy tắc có đối xứng. Nếu phản chiếu như gương, ta được mở rộng chẵn. Nếu phản chiếu rồi đổi dấu, ta được mở rộng lẻ. Hai lựa chọn này tương ứng với hai cách vật lý khác nhau mà biên của hệ đang cư xử.

### Cách nhìn hình ảnh

Mở rộng chẵn tạo ra đồ thị phản chiếu qua trục tung, nên đồ thị liền mạch theo kiểu cosine. Mở rộng lẻ tạo ra đồ thị đối xứng qua gốc, nên phù hợp với sine. Nếu vẽ chúng cạnh nhau, sinh viên sẽ thấy cùng một hàm gốc trên $$ [0,L] $$ nhưng sau mở rộng lại dẫn đến hai "phiên bản tuần hoàn" rất khác nhau.

### Cách nhìn hình thức

Cho $$ f $$ trên $$ [0,L] $$. Mở rộng chẵn:

$$ g(x)=f(\lvert x\rvert),\qquad -L\le x\le L. $$

Khi đó chuỗi Fourier của $$ g $$ chỉ chứa cosine:

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{L}\right),
$$

với

$$
a_n=\frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx.
$$

Mở rộng lẻ:

$$
g(x)=
\begin{cases}
f(x), & 0\le x\le L,\\
-f(-x), & -L\le x<0.
\end{cases}
$$

Khi đó chuỗi chỉ chứa sine:

$$
f(x)\sim \sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right),
$$

với

$$
b_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

## Những ngộ nhận thường gặp

- "Mở rộng chẵn hay lẻ chỉ là lựa chọn tùy ý." Không đúng; nó phải phù hợp với điều kiện biên và ý nghĩa vật lý.
- "Chuỗi sine và cosine chỉ là hai công thức khác nhau." Sai. Chúng phản ánh hai kiểu đối xứng và hai kiểu biên khác nhau.
- "Nếu dữ liệu trên

$$ [0,L] $$

giống nhau thì chuỗi thu được phải giống nhau." Không đúng; phần mở rộng quyết định phổ ngoài miền gốc.
- "Khai triển nửa khoảng chỉ là mẹo kỹ thuật cho bài tập." Sai; nó là công cụ trung tâm trong PDE trên đoạn hữu hạn.

## Tiến trình học tập đề xuất

### Bước 1: Ôn chẵn lẻ

Sinh viên cần thật chắc cách mở rộng đối xứng.

### Bước 2: Dựng hai kiểu mở rộng

Đây là bước bản chất nhất.

### Bước 3: Viết công thức sine và cosine trên

$$ [0,L] $$

Không nên học thuộc trước khi hiểu mở rộng.

### Bước 4: Kết nối với điều kiện biên

Dirichlet thường đi với sine, Neumann thường đi với cosine.

### Các checkpoint

- Sinh viên có dựng được đúng mở rộng chẵn và lẻ từ một dữ liệu cho trên

$$ [0,L] $$

hay không.
- Sinh viên có biết chọn sine hay cosine theo điều kiện biên hay không.
- Sinh viên có hiểu vì sao hai khai triển có thể khác nhau nhưng đều đúng trên miền gốc hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khai triển sine của

$$ f(x)=x $$

trên $$ [0,1] $$ Ta dùng mở rộng lẻ. Khi đó

$$ b_n=2\int_0^1 x\sin(n\pi x)\,dx. $$

Tích phân từng phần cho

$$ b_n=\frac{2(-1)^{n+1}}{n\pi}. $$

Vì vậy

$$
x\sim \frac{2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(n\pi x).
$$

Đây là khai triển tự nhiên khi điều kiện biên ép hàm bằng 0 ở hai đầu.

### Ví dụ 2: Khai triển cosine của

$$ f(x)=x $$

trên $$ [0,1] $$ Ta dùng mở rộng chẵn. Khi đó

$$ a_0=2\int_0^1 x\,dx=1, $$

và với $$ n\ge 1 $$, $$ a_n=2\int_0^1 x\cos(n\pi x)\,dx. $$

Kết quả cho thấy chỉ các chỉ số lẻ còn lại, và ta thu được một cosine series khác hẳn ví dụ trước. Điều rất quan trọng ở đây là: hai chuỗi khác nhau nhưng đều khớp $$ f(x)=x $$ trên

$$ [0,1]. $$

### Ví dụ 3: Liên hệ với điều kiện biên

Nếu cần giải phương trình nhiệt với $$ u(0,t)=u(L,t)=0 $$, thì các mode

$$ \sin\left(\frac{n\pi x}{L}\right) $$

tự động thỏa điều kiện biên. Ngược lại, nếu $$ u_x(0,t)=u_x(L,t)=0 $$, thì cosine modes là tự nhiên hơn. Ví dụ này là nơi khai triển nửa khoảng nối trực tiếp với vật lý.

## Câu hỏi khái niệm

1. Vì sao cùng một dữ liệu trên $$ [0,L] $$ lại có thể dẫn đến hai khai triển Fourier khác nhau?
2. Tại sao mở rộng lẻ lại đi cùng chuỗi sine, còn mở rộng chẵn đi cùng chuỗi cosine?
3. Vì sao điều kiện biên của PDE quyết định nên chọn loại mở rộng nào?

## Bài toán ứng dụng

1. Trong phương trình nhiệt trên thanh với hai đầu giữ ở 0, vì sao chuỗi sine là lựa chọn tự nhiên?
2. Trong bài toán đầu thanh cách nhiệt, vì sao chuỗi cosine phù hợp hơn?
3. Nếu dữ liệu ban đầu chỉ được đo trên một nửa miền, vì sao việc chọn cách mở rộng có thể ảnh hưởng đến mô hình toàn cục?

## Chiến lược giảng dạy tương tác

- Cho sinh viên vẽ trực tiếp mở rộng chẵn và lẻ của cùng một hàm trên

$$ [0,L] $$

để các em thấy bằng mắt sự khác nhau.
- Hỏi cả lớp: "Nếu biên bằng 0 thì sine hay cosine hợp lý hơn, và vì sao?"
- Tổ chức hoạt động so sánh hai chuỗi của cùng một hàm

$$ f(x)=x $$

trên

$$ [0,1]. $$
- Khuyến khích sinh viên giải thích bằng lời ý nghĩa vật lý của việc mở rộng ra ngoài miền gốc.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu bằng đồ thị trước khi đưa công thức. Khi nhìn rõ hai kiểu mở rộng bằng hình ảnh, sinh viên sẽ hiểu sine-cosine series tự nhiên hơn nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi thảo luận cách khai triển nửa khoảng phản ánh điều kiện biên của toán tử Sturm-Liouville, hoặc so sánh các phổ thu được từ hai kiểu mở rộng khác nhau của cùng một dữ liệu.

## Tóm tắt dễ nhớ

Khai triển nửa khoảng biến dữ liệu trên $$ [0,L] $$ thành bài toán Fourier quen thuộc bằng cách mở rộng chẵn hoặc lẻ. Mở rộng chẵn dẫn đến cosine series, mở rộng lẻ dẫn đến sine series. Lựa chọn này phản ánh trực tiếp điều kiện biên của bài toán vật lý.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thanh dẫn nhiệt trên nửa đoạn
- Bài toán: Nhiệt độ được cho trên $$ [0,L] $$, nhưng phương pháp tách biến đòi hỏi cơ sở sin hoặc cos trên đoạn đối xứng.
- Mô hình: Kéo dài chẵn để có chuỗi cos, hoặc kéo dài lẻ để có chuỗi sin.
- Giả thiết và giới hạn: Cách kéo dài phải phù hợp với điều kiện biên vật lý.
- Diễn giải: Khai triển nửa khoảng là kỹ thuật biến bài toán trên $$ [0,L] $$ thành bài toán Fourier chuẩn trên $$ [-L,L] $$.

#### Dao động dây với đầu cố định hoặc tự do
- Bài toán: Dữ kiện ban đầu chỉ biết trên nửa khoảng nhưng biên Dirichlet hay Neumann gợi ý chọn sin hay cos.
- Mô hình: Chuỗi sin cho biên cố định, chuỗi cos cho biên tự do.
- Giả thiết và giới hạn: Sự lựa chọn phụ thuộc bản chất điều kiện biên.
- Diễn giải: Half-range expansions là ngôn ngữ tự nhiên của nhiều bài toán PDE trên miền hữu hạn.

### 2. Trực giác bổ sung và các kết nối

Khai triển nửa khoảng là nơi sinh viên thấy rõ Fourier không chỉ nói về hàm tuần hoàn có sẵn; ta còn chủ động tạo tính tuần hoàn bằng cách kéo dài hàm. Một bẫy phổ biến là chọn sai loại kéo dài nên thu được cơ sở không khớp với biên vật lý.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi, 400)
f = x

x_ext = np.linspace(-np.pi, np.pi, 800)
odd_ext = x_ext
even_ext = np.abs(x_ext)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x_ext, odd_ext)
axes[0].set_title("Keo dai le -> chuoi sin")
axes[1].plot(x_ext, even_ext)
axes[1].set_title("Keo dai chan -> chuoi cos")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: half range sine cosine series visualization
- search: odd even extension Fourier series
- search: boundary conditions sine cosine expansions

### 5. Bài toán mẫu có bối cảnh thực

Với $$ f(x)=x $$ trên $$ [0,\pi] $$, nếu kéo dài lẻ thì chuỗi sin là
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$
Nếu kéo dài chẵn thì ta thu được chuỗi cos khác hẳn. Điều này cho thấy cùng một profile trên nửa khoảng có thể sinh ra hai khai triển khác nhau tùy điều kiện biên được mô hình hóa.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo kéo dài chẵn/lẻ và chọn chuỗi sin/cos phù hợp.

**Bậc sau đại học.** Liên hệ với cơ sở riêng của toán tử Laplace trên các miền hữu hạn và điều kiện biên Dirichlet-Neumann.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* - trực giác tốt về chuỗi Fourier, hội tụ, và các ví dụ vật lý.
- Evans, *Partial Differential Equations* - khung chuẩn cho hội tụ $$ L^2 $$, trực giao, và không gian hàm.
