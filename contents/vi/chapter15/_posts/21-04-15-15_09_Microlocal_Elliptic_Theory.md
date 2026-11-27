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

![Lý thuyết elliptic vi địa phương]({{ site.imgurl }}/chapter_img/chapter15/09_microlocal_elliptic_theory.svg)

Ở Chương 14, nếu ký hiệu chính $p_m(x, \xi)$ triệt tiêu dù chỉ theo *một* hướng $\xi$ duy nhất, ta buộc phải gán nhãn toàn bộ toán tử là "không elliptic" và bỏ cuộc! **Lý thuyết Elliptic Vi địa phương (Microlocal Elliptic Theory)** cứu vãn tình thế một cách đầy tinh tế: một toán tử hoàn toàn có thể **elliptic theo hướng này** và **không elliptic theo hướng kia** ngay tại cùng một điểm $x_0$—và tại mọi hướng elliptic, ta vẫn dựng được parametrix vi địa phương để khóa chặt kỳ dị ra khỏi vùng đó!

## Kiến thức cần nhớ: Bốn trụ cột của Lý thuyết Elliptic Vi địa phương

1. **Tập Elliptic $\operatorname{Ell}(P)$ và Tập Đặc trưng $\operatorname{Char}(P)$**:
   Điểm $(x_0, \xi_0) \in T^*M \setminus 0$ thuộc $\operatorname{Ell}(P)$ nếu $|p(x, \xi)| \ge c\langle\xi\rangle^m$ trong một lân cận nón quanh $(x_0, \xi_0)$. Phần bù $\operatorname{Char}(P) = (T^*M \setminus 0) \setminus \operatorname{Ell}(P)$ là nơi duy nhất kỳ dị được phép trú ngụ!
2. **Parametrix Vi địa phương (Microlocal Parametrix)**:
   Nếu $A \in \Psi^0$ có giá vi cục bộ $\operatorname{WF}'(A) \subset \operatorname{Ell}(P)$, tồn tại $Q \in \Psi^{-m}$ sao cho $QP = A \pmod{\Psi^{-\infty}}$! Nói nôm na: $P$ vẫn **khả nghịch hoàn hảo** khi ta chỉ nhìn qua "kính lọc góc" $A$ hướng vào vùng elliptic!
3. **Định lý Tính Chính quy Elliptic Vi địa phương**:
   Với *mọi* $\Psi$DO $P$ (kể cả phương trình sóng hay nhiệt, không cần elliptic toàn cục!):
   $$\operatorname{WF}(u) \subset \operatorname{WF}(Pu) \cup \operatorname{Char}(P).$$
   Đặc biệt, nếu $Pu \in C^\infty$ thì $\operatorname{WF}(u) \subset \operatorname{Char}(P)$—mọi hướng tần số nằm ngoài mặt đặc trưng đều tự động trơn vô hạn!
4. **Hợp nhất Chương 14 và Chương 15 trong Một dòng**:
   Khi $P$ elliptic toàn cục thì $\operatorname{Char}(P) = \emptyset$, nên công thức trên lập tức rút về $\operatorname{WF}(u) \subset \operatorname{WF}(Pu)$—chính là Định lý Tính Chính quy Elliptic cổ điển mạnh hơn một bậc!

## Mục tiêu

Bài học tùy chọn này trình bày lý thuyết elliptic ở cấp độ vi địa phương, tức cách kiểm tra tính khả nghịch cục bộ trên không gian pha thay vì chỉ trong không gian vị trí. Sau bài học, sinh viên cần nắm định nghĩa tập elliptic, hiểu vai trò trung tâm của parametrix vi địa phương, và giải thích vì sao toán tử không che giấu được điểm kỳ dị theo những hướng mà ký hiệu chính không triệt tiêu.

## Kiến thức nền

Sinh viên nên nắm vững ký hiệu chính của toán tử vi phân và toán tử giả vi phân, tập đặc trưng (characteristic set), tập mặt sóng và trực giác về tính chính quy vi địa phương từ Bài 15.01 và 15.02. Kiến thức về PDE elliptic cổ điển ở Chương 11 và Chương 14 sẽ giúp đối chiếu rõ bước mở rộng sang ngôn ngữ vi địa phương.

## Dẫn nhập

Trong lý thuyết PDE cổ điển, toán tử elliptic có tính làm trơn rõ rệt: vế phải trơn kéo theo nghiệm trơn hơn. Khi chuyển sang giải tích vi địa phương, câu hỏi được tinh chỉnh từ “nghiệm có trơn gần điểm $$ x_0 $$ không?” thành “nghiệm có trơn tại điểm $$ x_0 $$ theo hướng tần số $$ \xi_0 $$ hay không?”. Tính elliptic lúc này trở thành một tính chất cục bộ của ký hiệu trên không gian pha.

Nói ngắn gọn, lý thuyết elliptic vi địa phương khẳng định rằng tại các điểm pha nơi ký hiệu chính không triệt tiêu, toán tử có thể nghịch đảo xấp xỉ nhờ một parametrix vi địa phương. Do đó, nếu $$ Pu $$ trơn vi địa phương tại một điểm pha mà $$ P $$ elliptic, thì $$ u $$ cũng phải trơn vi địa phương tại đó.

Cách tiếp cận này tách bạch rõ hai chế độ khác nhau: trong vùng elliptic, kỳ dị không thể tự tồn tại mà chỉ có thể xuất phát từ vế phải; ngược lại, trên tập đặc trưng, kỳ dị có thể lan truyền tự do dọc theo các đường song đặc trưng.


### Giải thích: Xác định vùng Elliptic Vi địa phương của toán tử sóng 1D $P = \partial_t^2 - \partial_x^2$

Xét toán tử sóng $P = \partial_t^2 - \partial_x^2$ (không elliptic toàn cục!) với ký hiệu chính $p_2(t, x; \tau, \xi) = -\tau^2 + \xi^2$:
1. **Kiểm tra điểm không gian pha $(t_0, x_0;\; \tau = 2,\; \xi = 1)$**:
   $$p_2(t_0, x_0; 2, 1) = -2^2 + 1^2 = \mathbf{-3 \neq 0} \implies (t_0, x_0; 2, 1) \in \operatorname{Ell}(P)!$$
   Theo Định lý Elliptic Vi địa phương, nếu $Pu = 0$, ta kết luận **ngay lập tức** mà không cần giải sóng rằng $(t_0, x_0; 2, 1) \notin \operatorname{WF}(u)$!
2. **Kiểm tra điểm $(t_0, x_0;\; \tau = 2,\; \xi = 2)$**:
   $$p_2(t_0, x_0; 2, 2) = -2^2 + 2^2 = \mathbf{0} \implies (t_0, x_0; 2, 2) \in \operatorname{Char}(P).$$
   Đây là điểm trên nón ánh sáng $|\tau| = |\xi|$—nơi kỳ dị sóng được phép tồn tại và sẽ lan truyền dọc đường lưỡng đặc trưng theo Bài 15-02!
## Khái niệm theo ba cách

### Cách trực giác

Hãy xem toán tử $$ P $$ như một bộ lọc tín hiệu: trên những hướng tần số mà bộ lọc không làm triệt tiêu thông tin, ta có thể khôi phục gần đúng tín hiệu gốc từ đầu ra. Đó chính là trực giác của tính elliptic: ký hiệu chính khác không đảm bảo thông tin của $$ u $$ vẫn có thể đọc ngược lại từ $$ Pu $$ theo hướng đó.

### Cách hình ảnh

Có thể biểu diễn không gian đối tiếp tuyến tại một điểm $$ x_0 $$ như mặt phẳng các hướng tần số $$ \xi $$, tô màu đỏ tập đặc trưng

$$
\operatorname{Char}(P)=\{(x,\xi)\neq 0: p_m(x,\xi)=0\}
$$

và tô màu xanh vùng elliptic (phần bù của tập đặc trưng). Kỳ dị chỉ có thể tự lan truyền trong vùng đỏ, còn trong vùng xanh toán tử có nghịch đảo xấp xỉ nên tính trơn của $$ Pu $$ quyết định tính trơn của $$ u $$.

### Cách hình thức

Cho $$ P\in \Psi^m $$ có ký hiệu chính $$ p_m(x,\xi) $$. Ta nói $$ P $$ elliptic tại $$ \left(x_0,\xi_0\right)\neq 0 $$ nếu tồn tại một lân cận nón của $$ \left(x_0,\xi_0\right) $$ sao cho $$ \lvert p_m(x,\xi)\rvert\ge C\lvert \xi\rvert^m $$ khi $$ \lvert \xi\rvert $$ đủ lớn. Khi đó tồn tại $$ Q\in \Psi^{-m} $$ thỏa $$ QP=I+R $$ theo nghĩa vi địa phương gần $$ \left(x_0,\xi_0\right) $$, với $$ R $$ là toán tử làm trơn trong vùng xét. Hệ quả cơ bản là bao hàm thức

$$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P), $$

được gọi là định lý chính quy elliptic vi địa phương.

## So sánh nhanh với lý thuyết elliptic cổ điển

Trong lý thuyết PDE cổ điển, kết quả quen thuộc là nếu $$ -\Delta u=f $$ với $$ f $$ trơn trên một miền thì $$ u $$ trơn trên miền đó. Phiên bản vi địa phương giữ nguyên bản chất này nhưng tinh chỉnh đến từng hướng trong không gian pha: tính chính quy không còn chỉ là thuộc tính tại từng điểm mà trở thành thuộc tính định hướng, khiến tập mặt sóng trở thành ngôn ngữ tự nhiên của lý thuyết elliptic hiện đại.

## Ngộ nhận thường gặp

### “Elliptic chỉ là tên gọi hình thức cho một lớp phương trình quen thuộc”

Không đúng. Tính elliptic là một điều kiện chặn dưới định lượng trên ký hiệu chính, trực tiếp bảo đảm sự tồn tại của parametrix và tính chính quy.

### “Nếu toán tử không elliptic ở mọi nơi thì lý thuyết elliptic không dùng được”

Sai. Chỉ cần toán tử elliptic tại một điểm pha cụ thể là đã đủ để suy ra tính chính quy vi địa phương tại chính điểm pha đó.

### “Elliptic đồng nghĩa với tồn tại nghịch đảo chính xác”

Không nhất thiết. Thông thường ta chỉ dựng được parametrix — tức nghịch đảo đúng đến một phần dư làm trơn.

### “Nếu $$ Pu $$ trơn thì $$ u $$ luôn trơn”

Chỉ đúng ngoài tập đặc trưng. Tại các hướng thuộc tập đặc trưng, $$ u $$ vẫn có thể chứa kỳ dị dù $$ Pu $$ hoàn toàn trơn.

## Tiến trình học

### Bước 1: Ôn lại ký hiệu chính và tập đặc trưng

Nhắc lại tập đặc trưng là tập không điểm của ký hiệu chính trên bó đối tiếp tuyến bỏ lát cắt không.

### Bước 2: Định nghĩa tập elliptic

Xác định tập elliptic là vùng trên không gian pha nơi ký hiệu chính không triệt tiêu và thỏa chặn dưới cỡ $$ \lvert \xi\rvert^m $$.

### Bước 3: Xây dựng parametrix vi địa phương

Hiểu parametrix là nghịch đảo xấp xỉ cục bộ trong không gian pha, đủ để truyền tính chính quy.

### Bước 4: Rút ra bao hàm thức tập mặt sóng

Từ $$ QP=I+R $$, suy ra tính trơn vi địa phương của $$ Pu $$ kéo theo tính trơn vi địa phương của $$ u $$ trên vùng elliptic.

### Bước 5: Đối chiếu với sự lan truyền kỳ dị

Phân biệt rõ vai trò hai vùng: vùng elliptic triệt tiêu kỳ dị độc lập, còn vùng đặc trưng cho phép kỳ dị lan truyền.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao điều kiện $$ p_m\neq 0 $$ dẫn đến khả năng nghịch đảo cục bộ hay không?
- Sinh viên có phân biệt rõ tập elliptic và tập đặc trưng hay không?
- Sinh viên có diễn đạt được ý nghĩa của bao hàm thức $$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P) $$ bằng lời hay không?

## Ví dụ có lời giải

### Ví dụ 1: Toán tử $$ 1-\Delta $$ elliptic theo mọi hướng

Ký hiệu chính của $$ 1-\Delta $$ là $$ p_2(\xi)=\lvert \xi\rvert^2 $$. Vì $$ p_2(\xi)>0 $$ với mọi $$ \xi\neq 0 $$, tập đặc trưng rỗng trên bó đối tiếp tuyến bỏ lát cắt không, nên $$ 1-\Delta $$ elliptic ở mọi điểm pha và không có hướng tần số nào làm mất thông tin.

### Ví dụ 2: Đạo hàm theo một biến không elliptic

Xét $$ P=\partial_{x_1} $$ với ký hiệu chính $$ p_1(\xi)=i\xi_1 $$. Khi $$ \xi_1=0 $$ nhưng $$ \xi\neq 0 $$, ta có $$ p_1(\xi)=0 $$, nên $$ P $$ không elliptic theo các hướng vuông góc trục $$ x_1 $$. Điều này giải thích vì sao biết $$ \partial_{x_1}u $$ trơn chưa đủ để kết luận $$ u $$ trơn theo các biến còn lại.

### Ví dụ 3: Đối chiếu toán tử Laplace và toán tử sóng

Với toán tử Laplace, $$ p_2(\xi)=\lvert \xi\rvert^2 $$ không triệt tiêu ngoài $$ \xi=0 $$ nên toán tử elliptic mọi hướng. Ngược lại, với toán tử sóng $$ \Box=\partial_t^2-\Delta_x $$, ký hiệu chính $$ p_2(\tau,\xi)=\tau^2-\lvert \xi\rvert^2 $$ triệt tiêu trên nón ánh sáng $$ \tau^2=\lvert \xi\rvert^2 $$, nơi kỳ dị được phép lan truyền dọc theo các đường song đặc trưng.

### Ví dụ 4: Phác thảo chứng minh tính chính quy elliptic vi địa phương

Giả sử $$ P $$ elliptic tại $$ \left(x_0,\xi_0\right) $$ và $$ Pu $$ trơn vi địa phương tại đó. Chọn parametrix vi địa phương $$ Q $$ thỏa $$ QP=I+R $$, ta viết $$ u=Q(Pu)-Ru $$. Vì $$ Q(Pu) $$ trơn vi địa phương theo $$ Pu $$ còn $$ Ru $$ là phần tử làm trơn, nên $$ u $$ trơn vi địa phương tại $$ \left(x_0,\xi_0\right) $$.

### Ví dụ 5: Ý nghĩa trong bài toán ngược

Trong chụp cắt lớp hoặc ảnh học, nếu toán tử đo có ký hiệu chính không triệt tiêu trên một tập hướng khả kiến, các kỳ dị của vật thể theo những hướng đó có thể khôi phục ổn định hơn; ngược lại, theo các hướng thuộc tập đặc trưng hoặc vùng khuất, dữ liệu không đủ để phục hồi vi cấu trúc.

## Câu hỏi khái niệm

1. Vì sao lý thuyết elliptic hiện đại cần đặt trên không gian pha thay vì chỉ trong không gian vị trí?
2. Parametrix khác gì với nghịch đảo chính xác, và vì sao nó vẫn đủ để chứng minh tính chính quy?
3. Vì sao bao hàm thức $$ WF(u)\subset WF(Pu)\cup \operatorname{Char}(P) $$ nối trực tiếp bài tập mặt sóng với bài lan truyền kỳ dị?

## Bài toán ứng dụng

1. Trong xử lý ảnh, nhận định “ký hiệu không triệt tiêu thì thông tin còn khả năng khôi phục” gợi mở điều gì cho phép làm mờ và khử mờ?
2. Trong địa chấn học và chụp cắt lớp, việc xác định các hướng khả kiến liên hệ ra sao với việc nhận diện vùng elliptic của toán tử đo?
3. Trong cơ học lượng tử, vì sao toán tử elliptic như toán tử Schrödinger dừng thường có tính chính quy tốt hơn các toán tử hyperbolic phụ thuộc thời gian?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Khi ký hiệu chính triệt tiêu theo một hướng tần số, ta có còn khôi phục đầy đủ thông tin theo hướng đó không?
- Vì sao phần dư làm trơn trong parametrix là dạng sai số chấp nhận được cho bài toán tính chính quy?
- Giữa toán tử Laplace và toán tử sóng, toán tử nào kiểm soát kỳ dị chặt hơn và vì sao?

### Hoạt động gợi ý

- Lập bảng so sánh ký hiệu chính và tập đặc trưng của $$ -\Delta $$, $$ \partial_{x_1} $$ và $$ \Box $$.
- Chia nhóm diễn giải bao hàm thức chính quy elliptic theo ba góc nhìn: hình học, xử lý tín hiệu và PDE cổ điển.
- Vẽ tập đặc trưng của một số ký hiệu đơn giản trong không gian tần số và tô phần bù là vùng elliptic.

### Cách tăng mức độ tham gia

- Mở đầu bằng câu hỏi trực quan: khi nào một bộ lọc vẫn giữ đủ thông tin để khôi phục tín hiệu gốc?
- Khuyến khích diễn đạt bằng lời trước khi viết công thức hình thức.
- Kết nối trực tiếp với các bài trước về phương trình Laplace, Poisson và bài toán ngược.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bắt đầu từ ví dụ quen thuộc $$ -\Delta $$ để nhắc lại tính elliptic cổ điển.
- Khởi đầu bằng toán tử vi phân trước khi mở rộng sang ký hiệu $$ \Psi^m $$.
- Luyện xác định tập đặc trưng qua các đa thức bậc nhất và bậc hai đơn giản.

### Thử thách cho sinh viên khá giỏi

- Phác thảo lập luận vì sao tính elliptic kéo theo tính Fredholm trên không gian Sobolev phù hợp.
- Liên hệ parametrix vi địa phương với phép tính hợp thành ΨDO.
- Tìm hiểu vai trò của ước lượng elliptic vi địa phương trong các định lý chính quy gần biên.

## Ghi nhớ nhanh

Lý thuyết elliptic vi địa phương khẳng định rằng tại các điểm pha nơi ký hiệu chính không triệt tiêu, toán tử có parametrix và không thể che giấu điểm kỳ dị: ngoài tập đặc trưng, tính chính quy của $$ Pu $$ kéo theo tính chính quy của $$ u $$.

---

## Ứng dụng thực tế

### 1. Khử mờ ảnh và phục hồi tần số

Phép làm mờ ảnh thường được mô hình hóa bằng tích chập hoặc toán tử giả vi phân (dưới giả thiết tuyến tính, bất biến tịnh tiến và bỏ qua hiệu ứng phi tuyến của cảm biến). Nếu ký hiệu không triệt tiêu trên một dải tần, thông tin ở dải đó có thể khôi phục bằng nghịch đảo xấp xỉ; chỉ các hướng tần số không bị ký hiệu triệt tiêu mới có cơ hội phục hồi ổn định.

### 2. Bài toán nhiệt và khuếch tán trạng thái dừng

Phân bố nhiệt độ ở trạng thái dừng thỏa $$ -\nabla \cdot (k(x) \nabla u)=f $$. Khi hệ số dẫn nhiệt $$ k(x)>0 $$, toán tử có tính elliptic nên nghiệm trở nên trơn hơn ngoài nơi nguồn hoặc hệ số có kỳ dị, và không có kỳ dị nào tự lan truyền theo tia như trong phương trình sóng.

### 3. Tĩnh điện và tái tạo độ dẫn điện

Trong mô hình tĩnh điện hoặc bài toán dẫn điện gần dừng $$ \nabla \cdot (\gamma(x) \nabla u)=0 $$ với $$ \gamma(x)>0 $$, tính elliptic áp đặt ràng buộc chặt lên kỳ dị ẩn của nghiệm, miễn là hệ số không suy biến và dữ liệu không bị thiếu (trong khi hiện tượng điện từ phụ thuộc thời gian vượt ra ngoài lý thuyết elliptic thuần túy).

## Trực giác sâu hơn

Tính elliptic có nghĩa là không hướng tần số quan trọng nào bị toán tử xóa mất, nhờ đó có thể dựng parametrix để khôi phục đầu vào đúng đến sai số làm trơn. Trong bài toán tính chính quy, sai số làm trơn không tạo thêm phần tử mới cho tập mặt sóng nên hoàn toàn đủ mạnh để kết luận.

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

Có thể dùng `Plotly.js` để vẽ song song hai mặt mức của $$ \lvert \xi\rvert^2 $$ và $$ \lvert \xi_1\rvert $$, giúp quan sát ngay ở trường hợp thứ hai ký hiệu triệt tiêu trên cả một họ hướng tần số.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `elliptic symbol visualization`, `parametrix microlocal elliptic regularity`, hoặc `deblurring symbol invertibility`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào các PDE elliptic quen thuộc như phương trình Poisson và trực giác rằng nguồn trơn kéo theo nghiệm trơn hơn.

### Mức sau đại học (Graduate)

Đi sâu vào parametrix trong phép tính giả vi phân, các ước lượng elliptic trên không gian Sobolev, lý thuyết Fredholm và bao hàm thức vi địa phương $$ WF(u) \subset WF(Pu) \cup \operatorname{Char}(P) $$.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Khôi phục biên trong ảnh và bài toán ngược
- Bài toán: Xác định vùng mà kỳ dị của ảnh gốc có thể khôi phục được sau tác động của một toán tử elliptic.
- Mô hình: Tính elliptic vi địa phương cho biết ngoài tập đặc trưng,
$$ WF(u) \subset WF(Pu). $$
- Giả thiết và giới hạn: Kết luận chỉ áp dụng trong vùng không gian pha nơi ký hiệu chính không suy biến.
- Diễn giải: Toán tử elliptic không thể che giấu kỳ dị của nghiệm trong vùng elliptic.

#### Tính chính quy cục bộ cho PDE
- Bài toán: Xác định không chỉ nghiệm trơn hơn ở đâu mà còn trơn hơn theo hướng nào.
- Mô hình: Sử dụng parametrix vi địa phương để suy ra tính chính quy theo từng hướng.
- Giả thiết và giới hạn: Khi ký hiệu suy biến, kết luận elliptic mất hiệu lực tại các hướng đó.
- Diễn giải: Đây là dạng phát biểu sắc nét nhất của tính chính quy elliptic.

### 2. Trực giác bổ sung và các kết nối

Tính chính quy elliptic cổ điển cho biết nguồn trơn kéo theo nghiệm trơn hơn; phiên bản vi địa phương tinh chỉnh kết luận này cho từng điểm–hướng trên không gian pha: nếu toán tử elliptic tại một điểm pha, mọi kỳ dị tại đó của $$ u $$ đều phải đến từ $$ Pu $$.

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
và $$ f \in H^s $$, thì tính chính quy elliptic cho
$$ u \in H^{s+2}. $$
Ở cấp vi địa phương, vì ký hiệu $$ 1+\lvert \xi\rvert^2 $$ không triệt tiêu tại mọi hướng $$ \xi_0\neq 0 $$, tính chính quy của $$ u $$ theo hướng đó được quyết định hoàn toàn bởi tính chính quy của $$ f $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Liên hệ lại với tính chính quy elliptic đã học ở các chương trước.

**Bậc sau đại học.** Kết nối với parametrix, tập mặt sóng và các định lý bao hàm vi địa phương.

## Video tham khảo

- Nên xem trước: [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Trình bày định nghĩa tính elliptic vi địa phương của András Vasy.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 2)](https://www.youtube.com/watch?v=3DN6bKJnlXc) — Institut Fourier, tiếng Anh. Đối chiếu với trường hợp không elliptic: sự lan truyền kỳ dị khi tính elliptic bị vi phạm.
- [Index Theory Lecture 8: Algebra of pseudodifferential operators](https://www.youtube.com/watch?v=uUCQHWHqLCU) — Masoud Khalkhali, tiếng Anh. Xây dựng parametrix elliptic trong đại số toán tử giả vi phân.
