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

Bài học này giải quyết một tình huống thường gặp trong PDE: dữ liệu chỉ được cho trên nửa đoạn $$ [0,L] $$ thay vì trên một khoảng đối xứng. Sau bài học, sinh viên cần nắm ý tưởng mở rộng chẵn và mở rộng lẻ, biết khi nào sử dụng chuỗi cos hoặc chuỗi sin, hiểu mối liên hệ trực tiếp với điều kiện biên Dirichlet và Neumann, đồng thời nhận ra rằng cùng một dữ liệu trên $$ [0,L] $$ có thể tạo ra hai phổ Fourier khác nhau tùy theo cách mở rộng.

## Kiến thức nền

Sinh viên cần nắm vững chuỗi Fourier trên miền đối xứng cùng vai trò của hàm chẵn và hàm lẻ. Bài học này là cầu nối trực tiếp giữa chuỗi Fourier và phương pháp tách biến cho phương trình nhiệt cũng như phương trình sóng.

## Dẫn nhập

Nhiều bài toán vật lý không được phát biểu trên đoạn đối xứng $$ [-L,L] $$, mà chỉ trên miền có ý nghĩa thực tế là $$ [0,L] $$. Khi đó, nếu chỉ dùng chuỗi Fourier đầy đủ trên miền đối xứng, ta sẽ gặp vướng mắc. Khai triển nửa khoảng giải quyết bài toán này một cách tự nhiên bằng cách mở rộng dữ liệu sang miền đối xứng theo kiểu chẵn hoặc lẻ, rồi áp dụng các công thức Fourier quen thuộc.

Cách làm này thể hiện rõ tính linh hoạt của phương pháp Fourier: dữ liệu gốc trên $$ [0,L] $$ không thay đổi, nhưng cách mở rộng phần ngoài miền gốc sẽ quyết định lớp mode xuất hiện trong khai triển. Đây chính là điểm giao nhau giữa điều kiện biên và phép mở rộng hàm.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Giả sử ta chỉ biết hình dạng của một sợi dây trên nửa đoạn $$ [0,L] $$. Để áp dụng công cụ Fourier quen thuộc, ta cần mở rộng hàm sang nửa còn lại theo một quy tắc đối xứng: phản chiếu qua trục tung tạo ra mở rộng chẵn, còn phản chiếu rồi đổi dấu tạo ra mở rộng lẻ. Hai lựa chọn này tương ứng với hai cách ứng xử vật lý khác nhau tại biên của hệ.

### Cách nhìn hình ảnh

Mở rộng chẵn tạo ra đồ thị đối xứng qua trục tung, phù hợp tự nhiên với các mode cos. Mở rộng lẻ tạo ra đồ thị đối xứng qua gốc tọa độ, phù hợp với các mode sin. Khi đặt hai đồ thị cạnh nhau, ta thấy rõ cùng một hàm gốc trên $$ [0,L] $$ có thể sinh ra hai hàm tuần hoàn rất khác nhau sau khi mở rộng.

### Cách nhìn hình thức

Cho hàm $$ f $$ xác định trên $$ [0,L] $$. Mở rộng chẵn của $$ f $$ là

$$ g(x)=f(\lvert x\rvert),\qquad -L\le x\le L. $$

Khi đó chuỗi Fourier của $$ g $$ chỉ chứa các số hạng cos:

$$
f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{L}\right),
$$

với

$$
a_n=\frac{2}{L}\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx.
$$

Mở rộng lẻ của $$ f $$ là

$$
g(x)=
\begin{cases}
f(x), & 0\le x\le L,\\
-f(-x), & -L\le x<0.
\end{cases}
$$

Khi đó chuỗi chỉ chứa các số hạng sin:

$$
f(x)\sim \sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right),
$$

với

$$
b_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

## Những ngộ nhận thường gặp

- "Mở rộng chẵn hay lẻ chỉ là lựa chọn tùy ý." Không đúng; cách mở rộng phải tương thích với điều kiện biên và ý nghĩa vật lý của bài toán.
- "Chuỗi sin và chuỗi cos chỉ là hai công thức khác nhau." Sai; chúng phản ánh hai dạng đối xứng và hai loại điều kiện biên khác nhau.
- "Nếu dữ liệu trên $$ [0,L] $$ giống nhau thì chuỗi thu được phải giống nhau." Không đúng; phần mở rộng ngoài miền gốc quyết định toàn bộ phổ tần số.
- "Khai triển nửa khoảng chỉ là kỹ thuật phụ cho bài tập." Sai; đây là công cụ trung tâm để giải PDE trên đoạn hữu hạn.

## Tiến trình học tập đề xuất

### Bước 1: Ôn lại tính chẵn lẻ

Sinh viên cần nắm chắc quy tắc mở rộng đối xứng của hàm số.

### Bước 2: Xây dựng hai kiểu mở rộng

Đây là bước mang tính bản chất nhất của bài học.

### Bước 3: Viết công thức chuỗi sin và chuỗi cos trên $$ [0,L] $$

Nên hiểu rõ cách suy ra từ phép mở rộng trước khi ghi nhớ công thức.

### Bước 4: Kết nối với điều kiện biên

Điều kiện biên Dirichlet thường đi cùng chuỗi sin, còn điều kiện biên Neumann thường đi cùng chuỗi cos.

### Các điểm kiểm tra

- Sinh viên có dựng đúng mở rộng chẵn và mở rộng lẻ từ một hàm cho trên $$ [0,L] $$ hay không.
- Sinh viên có biết chọn chuỗi sin hay chuỗi cos tương ứng với điều kiện biên hay không.
- Sinh viên có giải thích được vì sao hai khai triển khác nhau vẫn cùng biểu diễn đúng hàm gốc trên $$ [0,L] $$ hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Khai triển sin của $$ f(x)=x $$ trên $$ [0,1] $$

Ta sử dụng mở rộng lẻ. Khi đó

$$ b_n=2\int_0^1 x\sin(n\pi x)\,dx. $$

Áp dụng tích phân từng phần, ta được

$$ b_n=\frac{2(-1)^{n+1}}{n\pi}. $$

Vì vậy

$$
x\sim \frac{2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(n\pi x).
$$

Đây là khai triển tự nhiên khi điều kiện biên ràng buộc hàm bằng 0 tại hai đầu mút.

### Ví dụ 2: Khai triển cos của $$ f(x)=x $$ trên $$ [0,1] $$

Ta sử dụng mở rộng chẵn. Khi đó

$$ a_0=2\int_0^1 x\,dx=1, $$

và với $$ n\ge 1 $$,

$$ a_n=2\int_0^1 x\cos(n\pi x)\,dx. $$

Tính tích phân cho thấy với $$ n\ge 1 $$, chỉ các chỉ số lẻ cho hệ số khác 0, tạo nên một chuỗi cos khác hẳn ví dụ trước. Điểm đáng chú ý là hai chuỗi khác nhau nhưng đều khớp với $$ f(x)=x $$ trên $$ [0,1] $$.

### Ví dụ 3: Liên hệ với điều kiện biên

Khi giải phương trình nhiệt với điều kiện $$ u(0,t)=u(L,t)=0 $$, các mode $$ \sin\left(\frac{n\pi x}{L}\right) $$ tự động thỏa mãn điều kiện biên. Ngược lại, với điều kiện cách nhiệt $$ u_x(0,t)=u_x(L,t)=0 $$, các mode cos là lựa chọn phù hợp. Ví dụ này cho thấy mối liên hệ trực tiếp giữa khai triển nửa khoảng và mô hình vật lý.

## Câu hỏi khái niệm

1. Vì sao cùng một dữ liệu trên $$ [0,L] $$ lại có thể dẫn đến hai khai triển Fourier khác nhau?
2. Tại sao mở rộng lẻ đi cùng chuỗi sin, còn mở rộng chẵn đi cùng chuỗi cos?
3. Vì sao điều kiện biên của PDE quyết định loại mở rộng cần chọn?

## Bài toán ứng dụng

1. Trong bài toán truyền nhiệt trên thanh có hai đầu giữ ở nhiệt độ 0, vì sao chuỗi sin là lựa chọn tự nhiên?
2. Trong bài toán thanh có hai đầu cách nhiệt, vì sao chuỗi cos phù hợp hơn?
3. Nếu dữ liệu ban đầu chỉ được đo trên nửa miền, việc chọn cách mở rộng ảnh hưởng ra sao đến mô hình toàn cục?

## Chiến lược giảng dạy tương tác

- Cho sinh viên tự vẽ mở rộng chẵn và mở rộng lẻ của cùng một hàm trên $$ [0,L] $$ để quan sát trực tiếp sự khác biệt.
- Đặt câu hỏi cho cả lớp: "Nếu giá trị tại biên bằng 0 thì chuỗi sin hay chuỗi cos hợp lý hơn, và vì sao?"
- Tổ chức so sánh hai chuỗi Fourier thu được từ cùng một hàm $$ f(x)=x $$ trên $$ [0,1] $$.
- Khuyến khích sinh viên diễn giải bằng lời ý nghĩa vật lý của việc mở rộng hàm ra ngoài miền gốc.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên bắt đầu bằng việc vẽ đồ thị mở rộng trước khi đưa công thức. Khi đã quan sát rõ hai dạng mở rộng bằng hình ảnh, sinh viên sẽ tiếp thu công thức chuỗi sin và chuỗi cos dễ dàng hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên phân tích cách khai triển nửa khoảng phản ánh điều kiện biên của toán tử Sturm-Liouville, hoặc so sánh tốc độ suy giảm phổ giữa hai kiểu mở rộng của cùng một hàm dữ liệu.

## Tóm tắt dễ nhớ

Khai triển nửa khoảng đưa dữ liệu trên $$ [0,L] $$ về bài toán Fourier quen thuộc thông qua phép mở rộng chẵn hoặc lẻ. Mở rộng chẵn cho chuỗi cos, mở rộng lẻ cho chuỗi sin, và lựa chọn này phản ánh trực tiếp điều kiện biên của bài toán vật lý.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Thanh dẫn nhiệt trên nửa đoạn
- Bài toán: Nhiệt độ ban đầu chỉ được cho trên $$ [0,L] $$, trong khi phương pháp tách biến cần cơ sở sin hoặc cos tương thích trên đoạn đối xứng.
- Mô hình: Mở rộng chẵn để thu chuỗi cos, hoặc mở rộng lẻ để thu chuỗi sin.
- Giả thiết và giới hạn: Cách mở rộng phải phù hợp với điều kiện biên vật lý.
- Diễn giải: Khai triển nửa khoảng chuyển bài toán trên $$ [0,L] $$ thành bài toán Fourier chuẩn trên $$ [-L,L] $$.

#### Dao động dây với đầu cố định hoặc tự do
- Bài toán: Dữ kiện ban đầu chỉ cho trên nửa khoảng, còn điều kiện biên Dirichlet hay Neumann sẽ quyết định chọn cơ sở sin hay cos.
- Mô hình: Chuỗi sin dùng cho biên cố định, chuỗi cos dùng cho biên tự do.
- Giả thiết và giới hạn: Lựa chọn cơ sở phụ thuộc vào bản chất điều kiện biên.
- Diễn giải: Khai triển nửa khoảng là ngôn ngữ tự nhiên cho nhiều bài toán PDE trên miền hữu hạn.

### 2. Trực giác bổ sung và các kết nối

Khai triển nửa khoảng cho thấy phương pháp Fourier không chỉ áp dụng cho các hàm vốn đã tuần hoàn, mà ta có thể chủ động tạo tính tuần hoàn bằng cách mở rộng hàm. Một sai sót thường gặp là chọn sai kiểu mở rộng, dẫn đến cơ sở không thỏa mãn điều kiện biên vật lý.

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

Với $$ f(x)=x $$ trên $$ [0,\pi] $$, nếu mở rộng lẻ thì chuỗi sin là
$$
x\sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nx).
$$
Nếu mở rộng chẵn thì ta thu được một chuỗi cos khác hẳn. Điều này cho thấy cùng một phân bố ban đầu trên nửa khoảng có thể sinh ra hai khai triển khác nhau tùy theo điều kiện biên đang mô hình hóa.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo cách mở rộng chẵn, lẻ và lựa chọn chuỗi sin, chuỗi cos phù hợp.

**Bậc sau đại học.** Liên hệ với hệ hàm riêng của toán tử Laplace trên miền hữu hạn kèm điều kiện biên Dirichlet và Neumann.

## Video tham khảo

- Xem trước: [Fourier sine and cosine series | Lecture 50 | Differential Equations for Engineers](https://www.youtube.com/watch?v=v5aithNXpE0) — Jeffrey Chasnov, tiếng Anh. Trình bày khai triển sin và cos nửa khoảng trên đoạn có độ dài $$ L $$.
- [Half Range Fourier sine series and cosine series](https://www.youtube.com/watch?v=liAPB8gVL5o) — MEXAMS, tiếng Anh. Giải mẫu một ví dụ chuỗi sin nửa khoảng và một ví dụ chuỗi cos nửa khoảng.
- [Introduction To Half Range Fourier Series | Sine And Cosine Series](https://www.youtube.com/watch?v=kc8e6IZoYIo) — DrAvitech, tiếng Anh. Giải thích cách lựa chọn giữa mở rộng sin và mở rộng cos.

## Tài liệu tham khảo

- Haberman, *Applied Partial Differential Equations* — trình bày trực giác rõ ràng về chuỗi Fourier, sự hội tụ và các ví dụ vật lý.
- Evans, *Partial Differential Equations* — cung cấp khung lý thuyết chuẩn cho hội tụ $$ L^2 $$, tính trực giao và không gian hàm.
