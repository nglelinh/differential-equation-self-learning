---
layout: post
title: "Lý Thuyết Elliptic Vi Địa Phương"
chapter: '15'
order: 9
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: optional
---

![Lý thuyết elliptic vi địa phương]({{ site.imgurl }}/chapter_img/chapter15/09_microlocal_elliptic_theory.svg )

## Mục tiêu

Bài optional này giới thiệu elliptic theory ở mức vi địa phương, tức là cách ta kiểm tra khả nghịch cục bộ trong không gian pha thay vì chỉ trên không gian vật lý. Sau bài học, sinh viên cần hiểu elliptic set là gì, vì sao parametrix là công cụ trung tâm, và vì sao toán tử elliptic không che giấu singularity ở những hướng mà symbol không triệt tiêu.

## Kiến thức nền

Sinh viên nên nắm symbol chính của toán tử vi phân hay pseudodifferential operator, characteristic set, wave front set, và trực giác về microlocal regularity từ các bài 15.01 và 15.02. Kiến thức từ chương 11 về elliptic PDE cổ điển cũng rất hữu ích, vì bài này mở rộng tinh thần đó sang ngôn ngữ vi địa phương.

## Dẫn nhập

Trong lý thuyết PDE cổ điển, ta thường học rằng toán tử elliptic có tính regularizing mạnh: nếu vế phải trơn thì nghiệm thường trơn hơn nhiều so với trường hợp hyperbolic hay parabolic. Tuy nhiên, khi bước vào giải tích vi địa phương, ta không chỉ hỏi nghiệm có trơn ở một điểm $$ x_0 $$ hay không, mà còn hỏi nghiệm có trơn theo hướng tần số nào $$ \xi_0 $$ tại điểm đó. Chính ở đây, ellipticity được đọc như một tính chất của symbol trên không gian pha.

Một cách rất ngắn gọn, elliptic theory vi địa phương nói rằng: tại những điểm pha mà symbol chính của toán tử không bằng không, toán tử đó có thể được đảo ngược xấp xỉ bởi một parametrix. Vì thế, nếu $$ Pu $$ trơn microlocally tại một hướng nào đó và $$ P $$ elliptic tại hướng ấy, thì $$ u $$ cũng phải trơn microlocally ở đó. Đây là nguyên lý cho phép ta chuyển regularity từ dữ liệu sang nghiệm.

Ý tưởng này quan trọng vì nó tách hai cơ chế rất khác nhau. Ở vùng elliptic, singularity không được phép tồn tại độc lập; nó chỉ có thể đến từ dữ liệu. Ở vùng characteristic, ngược lại, singularity có thể lan truyền dọc theo bicharacteristics. Nói cách khác, để hiểu nơi nào singularity có thể sống, ta phải biết vùng nào là elliptic và vùng nào là characteristic.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng toán tử $$ P $$ như một bộ lọc tín hiệu. Nếu ở một dải tần số nào đó bộ lọc không làm mất thông tin, thì ta có thể phục hồi tín hiệu gốc từ tín hiệu đã qua lọc, ít nhất là gần đúng. Đó chính là tinh thần của ellipticity: symbol không triệt tiêu nghĩa là không có hướng tần số nào bị “xóa sạch”, nên thông tin của $$ u $$ vẫn có thể được đọc lại từ $$ Pu $$ trong vùng đó.

### Cách hình ảnh

Giáo viên nên vẽ cotangent space tại một điểm $$ x_0 $$ như một mặt phẳng các hướng tần số $$ \xi $$. Trên hình, tô màu đỏ tập characteristic

$$
\operatorname{Char}(P)=\{(x,\xi)\neq 0: p_m(x,\xi)=0\}
$$

và tô màu xanh vùng elliptic, là phần bù của tập đó. Thông điệp trực quan là singularity chỉ có thể “tự do di chuyển” ở vùng đỏ; còn trong vùng xanh, toán tử có một nghịch đảo xấp xỉ nên regularity của $$ Pu $$ ép regularity của $$ u $$.

### Cách hình thức

Cho $$ P\in \Psi^m $$ có symbol chính $$ p_m(x,\xi) $$. Ta nói $$ P $$ elliptic tại $$ \left(x_0,\xi_0\right)\neq 0 $$ nếu tồn tại lân cận nón của $$ \left(x_0,\xi_0\right) $$ sao cho $$ \lvert p_m(x,\xi)\rvert\ge C\lvert \xi\rvert^m $$ khi $$ \lvert \xi\rvert $$ đủ lớn. Khi đó tồn tại $$ Q\in \Psi^{-m} $$ sao cho $$ QP=I+R $$ microlocally gần $$ \left(x_0,\xi_0\right) $$, với $$ R $$ là smoothing operator trong vùng xét. Hệ quả cơ bản là

$$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P). $$

Mệnh đề này thường được gọi là elliptic regularity vi địa phương.

## So sánh nhanh với elliptic theory cổ điển

Trong khóa PDE cơ bản, sinh viên đã gặp các phát biểu kiểu: nếu $$ -\Delta u=f $$ và $$ f $$ trơn trên một miền, thì $$ u $$ thường trơn hơn kỳ vọng. Bản vi địa phương giữ nguyên tinh thần đó nhưng tinh chỉnh kết luận theo từng hướng trong không gian pha. Thay vì nói “$$ u $$ trơn gần $$ x_0 $$”, ta hỏi “$$ u $$ có singularity theo hướng $$ \xi_0 $$ tại $$ x_0 $$ hay không?”.

Điểm mới sâu sắc ở đây là regularity không còn là thuộc tính nhị phân theo điểm, mà là thuộc tính định hướng. Điều này giải thích vì sao wave front set trở thành ngôn ngữ tự nhiên của elliptic theory hiện đại.

## Ngộ nhận thường gặp

### “Elliptic chỉ là tên gọi cho một lớp phương trình đẹp”

Không. Ellipticity là điều kiện định lượng trên symbol, và chính điều kiện đó tạo ra parametrix cũng như regularity.

### “Nếu toán tử không elliptic mọi nơi thì elliptic theory vô dụng”

Sai. Ta chỉ cần ellipticity tại một điểm pha cụ thể để suy ra regularity microlocal tại điểm pha đó.

### “Elliptic nghĩa là có nghịch đảo thật sự”

Không nhất thiết. Trong nhiều bối cảnh ta chỉ có parametrix, tức là nghịch đảo đúng đến một sai số smoothing.

### “Nếu $$ Pu $$ trơn thì $$ u $$ luôn trơn”

Chỉ đúng ngoài characteristic set. Nếu $$ P $$ không elliptic ở một hướng nào đó, singularity của $$ u $$ vẫn có thể tồn tại ở hướng ấy dù $$ Pu $$ trơn.

## Tiến trình học

### Bước 1: Nhắc lại symbol chính và characteristic set

Sinh viên cần nhìn lại rằng characteristic set chính là nơi symbol chính triệt tiêu trên bó tiếp xúc đối ngẫu bỏ zero section.

### Bước 2: Định nghĩa elliptic set

Giải thích rằng elliptic set là phần của không gian pha nơi symbol không triệt tiêu và bị chặn dưới theo cỡ $$ \lvert \xi\rvert^m $$.

### Bước 3: Giới thiệu parametrix

Nhấn mạnh rằng parametrix là nghịch đảo xấp xỉ ở mức microlocal, đủ mạnh để truyền regularity.

### Bước 4: Rút ra hệ quả về wave front set

Từ $$ QP=I+R $$ suy ra rằng nếu $$ Pu $$ trơn microlocally thì $$ u $$ cũng trơn microlocally ở vùng elliptic.

### Bước 5: So sánh với propagation of singularities

Nói rõ rằng elliptic regions tiêu diệt singularity, còn characteristic regions là nơi singularity lan truyền.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao $$ p_m\neq 0 $$ lại gợi ý khả nghịch cục bộ không?
- Sinh viên có phân biệt được elliptic set và characteristic set không?
- Sinh viên có diễn giải được công thức $$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P) $$ bằng lời không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử $$ 1-\Delta $$ là elliptic ở mọi hướng

Symbol chính của $$ 1-\Delta $$ là $$ p_2(\xi)=\lvert \xi\rvert^2 $$. Với mọi $$ \xi\neq 0 $$, ta có $$ p_2(\xi)>0 $$, nên characteristic set rỗng trên bó đối ngẫu bỏ zero section. Vì vậy $$ 1-\Delta $$ elliptic mọi nơi. Điều này phù hợp với trực giác rằng toán tử này không có hướng tần số “mất thông tin”.

### Ví dụ 2: Toán tử đạo hàm theo một biến không elliptic

Xét $$ P=\partial_{x_1} $$. Symbol chính là $$ p_1(\xi)=i\xi_1 $$. Nếu $$ \xi_1=0 $$ nhưng $$ \xi\neq 0 $$, thì $$ p_1(\xi)=0 $$. Vậy $$ P $$ không elliptic trên những hướng vuông góc với trục $$ x_1 $$. Điều này giải thích vì sao chỉ biết $$ \partial_{x_1}u $$ trơn chưa đủ để kết luận toàn bộ $$ u $$ trơn.

### Ví dụ 3: Laplacian và wave operator cho hai hành vi khác nhau

Với Laplacian, $$ p_2(\xi)=\lvert \xi\rvert^2 $$, nên toán tử elliptic ngoài $$ \xi=0 $$. Với wave operator $$ \Box=\partial_t^2-\Delta_x $$, symbol chính là $$ p_2(\tau,\xi)=\tau^2-\lvert \xi\rvert^2 $$. Symbol này triệt tiêu trên nón ánh sáng $$ \tau^2=\lvert \xi\rvert^2 $$, nên wave operator không elliptic ở đó. Kết luận: Laplacian kiểm soát regularity mạnh hơn, còn wave operator cho phép singularity lan truyền theo quỹ đạo đặc trưng.

### Ví dụ 4: Đọc công thức elliptic regularity

Giả sử $$ P $$ elliptic tại $$ \left(x_0,\xi_0\right) $$ và $$ Pu $$ trơn microlocally tại đó. Chọn parametrix $$ Q $$ sao cho $$ QP=I+R $$. Khi áp dụng lên $$ u $$ ta được $$ u=Q(Pu)-Ru $$. Hạng $$ Q(Pu) $$ trơn microlocally vì $$ Pu $$ trơn, còn $$ Ru $$ smoothing. Vậy $$ u $$ trơn microlocally tại $$ \left(x_0,\xi_0\right) $$. Đây là chứng minh mô hình của mệnh đề elliptic regularity.

### Ví dụ 5: Giải thích cho bài toán nghịch đảo

Trong một mô hình chụp cắt lớp hay ảnh học, nếu toán tử tiến hóa hay toán tử đo đạc có symbol không triệt tiêu trên một tập hướng nhìn thấy được, thì singularity của vật thể ở những hướng đó có thể được khôi phục ổn định hơn. Ngược lại, ở những hướng nằm trong characteristic hay invisible set, dữ liệu không đủ để phục hồi vi cấu trúc. Ví dụ này cho thấy ellipticity không chỉ là khái niệm trừu tượng mà còn là ngôn ngữ của “độ nhìn thấy” trong inverse problems.

## Câu hỏi khái niệm

1. Vì sao trong elliptic theory ta cần làm việc trên không gian pha thay vì chỉ trên không gian vật lý?
2. Parametrix khác gì với nghịch đảo đúng, và tại sao nó vẫn đủ để suy ra regularity?
3. Vì sao công thức $$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P) $$ lại là cầu nối tự nhiên giữa bài về wave front set và bài về propagation of singularities?

## Bài toán ứng dụng

1. Trong xử lý ảnh, trực giác “symbol không triệt tiêu thì thông tin có thể phục hồi” gợi điều gì về các phép lọc làm mờ và khử mờ?
2. Trong địa chấn học hay cắt lớp vi tính, tại sao việc nhận diện các hướng nhìn thấy được lại gần với việc nhận diện vùng elliptic của toán tử đo?
3. Trong cơ học lượng tử, vì sao các toán tử elliptic như Schrödinger tĩnh thường có regularity tốt hơn các toán tử hyperbolic phụ thuộc thời gian?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu symbol triệt tiêu ở một hướng tần số, em nghĩ ta còn khôi phục hoàn toàn thông tin ở hướng đó được không?
- Tại sao smoothing remainder trong parametrix lại là “sai số chấp nhận được” cho bài toán regularity?
- Giữa Laplacian và wave operator, toán tử nào em mong kiểm soát singularity mạnh hơn, và vì sao?

### Hoạt động gợi ý

- Cho sinh viên lập bảng so sánh symbol của $$ -\Delta $$, $$ \partial_{x_1} $$, và $$ \Box $$.
- Chia nhóm để mỗi nhóm diễn giải công thức elliptic regularity bằng một ngôn ngữ khác: hình học, tín hiệu, hay PDE cổ điển.
- Vẽ characteristic set của vài toán tử mẫu trong không gian tần số rồi yêu cầu sinh viên tô vùng elliptic.

### Cách tăng tham gia

- Bắt đầu từ câu hỏi đời thường: khi nào một bộ lọc còn giữ đủ thông tin để phục hồi tín hiệu gốc?
- Khuyến khích sinh viên nói bằng lời trước khi viết công thức.
- Mời sinh viên nối khái niệm này với những gì họ đã học ở chương Laplace, Poisson, và inverse problems.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu bằng ví dụ quen thuộc $$ -\Delta $$ để nhắc lại ellipticity cổ điển.
- Tránh đi ngay vào ký hiệu $$ \Psi^m $$ nếu sinh viên còn yếu; có thể khởi đầu bằng toán tử vi phân.
- Cho sinh viên luyện đọc characteristic set qua các symbol rất đơn giản trước.

### Thử thách cho sinh viên khá giỏi

- Yêu cầu sinh viên phác thảo vì sao ellipticity dẫn đến Fredholm properties trên các không gian Sobolev thích hợp.
- Liên hệ parametrix elliptic với calculus của pseudodifferential operators.
- Tìm hiểu vì sao nhiều định lý về regularity biên thực chất bắt đầu từ elliptic microlocal estimates.

## Ghi nhớ nhanh

Microlocal elliptic theory nói rằng ở những điểm pha nơi symbol không triệt tiêu, toán tử có một nghịch đảo xấp xỉ và vì thế không thể che giấu singularity. Nói ngắn gọn: ngoài characteristic set, regularity của $$ Pu $$ kéo theo regularity của $$ u $$.

---

## Ứng dụng thực tế

### 1. Khử mờ ảnh và phục hồi tần số

Một phép làm mờ ảnh thường được mô hình hóa bằng tích chập hoặc toán tử pseudodifferential. Nếu symbol của toán tử không triệt tiêu trên một dải tần, thì thông tin ở dải đó còn có thể phục hồi bằng nghịch đảo xấp xỉ. Mô hình này giả định blur tuyến tính, bất biến theo tịnh tiến, và bỏ qua bão hòa cảm biến hay phi tuyến của camera. Diễn giải chính là trực giác elliptic: chỉ những hướng tần số không bị symbol làm sụp mới còn cơ hội được khôi phục ổn định.

### 2. Bài toán nhiệt và khuếch tán trạng thái dừng

Nhiệt độ ở trạng thái dừng thỏa $$ -\nabla \cdot (k(x) \nabla u)=f $$. Nếu $$ k(x) $$ dương, toán tử là elliptic và có xu hướng làm nghiệm trơn hơn ngoài những nơi nguồn hay hệ số tạo singularity. Mô hình giả định trạng thái cân bằng và không xét phụ thuộc thời gian. Diễn giải là: trong vùng elliptic, các irregularity sắc nét không thể tự lan theo tia như ở phương trình sóng.

### 3. Thế điện và ảnh hóa độ dẫn

Trong điện tĩnh hay mô hình độ dẫn, $$ \nabla \cdot (\gamma(x) \nabla u)=0 $$, với $$ \gamma(x)>0 $$ cho một toán tử elliptic. Mô hình giả định chế độ quasi-static và môi trường liên tục. Giới hạn là các hiện tượng điện từ phụ thuộc thời gian không còn nằm trong lý thuyết elliptic thuần túy. Diễn giải là: regularity của nghiệm đo được áp đặt ràng buộc mạnh lên singularity ẩn, trừ khi hệ số làm mất ellipticity hoặc dữ liệu bị thiếu.

## Trực giác sâu hơn

Ellipticity có nghĩa là không có hướng tần số quan trọng nào bị toán tử xóa mất. Vì vậy ta mới có thể dựng parametrix để khôi phục đầu vào tới sai số smoothing. Ngộ nhận thường gặp là nhầm “nghịch đảo xấp xỉ” với “giải xấp xỉ không đáng tin”; trong lý thuyết regularity, sai số smoothing là đủ tốt vì nó không tạo thêm wave front set.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

xi1 = np.linspace(-3, 3, 300)
xi2 = np.linspace(-3, 3, 300)
XI1, XI2 = np.meshgrid(xi1, xi2)

laplace_symbol = XI1**2 + XI2**2
dx_symbol = np.abs(XI1)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].contourf(XI1, XI2, laplace_symbol, levels=30, cmap='viridis')
axes[0].set_title('Symbol elliptic: |xi|^2')
axes[1].contourf(XI1, XI2, dx_symbol, levels=30, cmap='magma')
axes[1].contour(XI1, XI2, dx_symbol, levels=[1e-6], colors='white')
axes[1].set_title('Symbol không elliptic: |xi1|')
for ax in axes:
    ax.set_xlabel('xi1')
    ax.set_ylabel('xi2')
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để vẽ hai bề mặt mức của $$ \lvert \xi\rvert^2 $$ và $$ \lvert \xi_1\rvert $$ cạnh nhau, giúp sinh viên nhìn ngay thấy ở trường hợp thứ hai symbol triệt tiêu trên cả một họ hướng tần số.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `elliptic symbol visualization`, `parametrix microlocal elliptic regularity`, hoặc `deblurring symbol invertibility`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Giữ trọng tâm ở các PDE elliptic quen thuộc như Poisson và trực giác rằng nguồn trơn thường cho nghiệm trơn hơn.

### Mức sau đại học (Graduate)

Đi sâu vào parametrix trong pseudodifferential calculus, ước lượng elliptic trên Sobolev spaces, Fredholm theory, và bao hàm vi địa phương $$ WF(u) \subset WF(Pu) \cup \operatorname{Char}(P) $$.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khôi phục biên trong ảnh và bài toán nghịch
- Bài toán: Cần biết ở đâu singularity của ảnh gốc có thể được khôi phục sau khi áp một toán tử elliptic.
- Mô hình: Microlocal ellipticity cho biết ngoài tập đặc trưng,
$$ WF(u) \subset WF(Pu). $$
- Giả thiết và giới hạn: Kết luận chỉ đúng ở vùng phase space nơi symbol chính không suy biến.
- Diễn giải: Toán tử elliptic không thể che giấu singularity của nghiệm ở vùng elliptic.

#### Regularity cục bộ cho PDE
- Bài toán: Ta không chỉ muốn biết nghiệm trơn hơn toàn cục, mà còn muốn biết trơn hơn ở đâu và theo hướng nào.
- Mô hình: Dùng parametrix microlocal để suy regularity địa phương.
- Giả thiết và giới hạn: Nếu symbol suy biến, kết luận elliptic có thể thất bại.
- Diễn giải: Đây là phiên bản sắc nét nhất của elliptic regularity.

### 2. Trực giác bổ sung và các kết nối

Elliptic regularity cổ điển nói nguồn trơn hơn thì nghiệm trơn hơn. Phiên bản microlocal tinh chỉnh điều này: nếu toán tử là elliptic tại một điểm-hướng của phase space, thì singularity ở đó phải đến từ $$ Pu $$ chứ không tự sinh ra. Một ngộ nhận phổ biến là chỉ nhìn regularity như số đạo hàm; microlocal ellipticity quan tâm cả vị trí lẫn hướng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 600)
u = (x > 0).astype(float)
xi = np.fft.fftfreq(len(x), d=x[1] - x[0]) * 2 * np.pi
uhat = np.fft.fft(u)
filtered = np.fft.ifft(uhat / (1 + xi**2)).real

plt.plot(x, u, label="du lieu co nhay")
plt.plot(x, filtered, label="sau nghich dao elliptic 1/(1+xi^2)")
plt.legend()
plt.title("Toan tu elliptic nghich dao lam tron du lieu")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: microlocal elliptic regularity visualization
- search: parametrix wave front set intuition
- search: elliptic operator smoothing high frequencies plot

### 5. Bài toán mẫu có bối cảnh thực

Nếu
$$ (I-\Delta)u=f $$
và $$ f \in H^s $$, thì trực giác elliptic cho
$$ u \in H^{s+2}. $$
Ở mức vi địa phương, nếu symbol $$ 1+\lvert \xi\rvert^2 $$ không triệt tại một hướng $$ \xi_0\neq 0 $$, thì regularity của $$ u $$ tại hướng đó được quyết định hoàn toàn bởi regularity của $$ f $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nối lại với regularity elliptic quen thuộc từ các chương trước.

**Bậc sau đại học.** Kết nối với parametrix, wave front sets va microlocal inclusion theorems.
