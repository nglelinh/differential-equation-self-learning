---
layout: post
title: "Suy Ra Phương Trình Nhiệt"
chapter: '09'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter09
lesson_type: required
---

![21 03 04 09 01 Derivation Heat Equation]({{ site.imgurl }}/chapter_img/chapter09/01_derivation_heat_equation.svg)

Phương trình nhiệt $u_t = \alpha u_{xx}$ không rơi từ trên trời xuống—nó là kết quả trực tiếp của đúng **hai định luật vật lý sơ cấp**: định luật **Bảo toàn Năng lượng** trên một lát cắt vô cùng mỏng $[x, x+\Delta x]$ và **Định luật Fourier về Dẫn nhiệt** (nhiệt luôn chảy từ nơi nóng sang nơi lạnh tỷ lệ với độ dốc nhiệt độ).

## Kiến thức cần nhớ: Bốn bước suy diễn Phương trình Nhiệt từ Nguyên lý Đầu tiên

1. **Nhiệt năng trong phần tử thanh $[x, x + \Delta x]$**:
   $E = c \rho A\, u(x, t)\, \Delta x$ ($c$: nhiệt dung riêng, $\rho$: khối lượng riêng, $A$: tiết diện thanh).
2. **Định luật Bảo toàn Năng lượng**:
   Tốc độ tăng nhiệt năng bên trong lát cắt = (Nhiệt chảy vào ở đầu $x$) $-$ (Nhiệt chảy ra ở đầu $x + \Delta x$) + (Nguồn nhiệt sinh ra bên trong $Q$):
   $$\frac{d}{dt}\int_a^b c\rho u\,dx = \phi(a, t) - \phi(b, t) + \int_a^b Q\,dx \implies c\rho u_t = -\frac{\partial \phi}{\partial x} + Q.$$
3. **Định luật Dẫn nhiệt Fourier ($\phi = -k u_x$)**:
   Dấu trừ cực kỳ quan trọng: nếu nhiệt độ tăng dần sang phải ($u_x > 0$), nhiệt phải chảy ngược sang **trái** ($\phi < 0$)!
4. **Hợp nhất thành Phương trình Nhiệt & Mở rộng 3D**:
   Thế $\phi = -k u_x$ cho $u_t = \alpha u_{xx} + \frac{Q}{c\rho}$ với hệ số khuếch tán nhiệt $\alpha = \frac{k}{c\rho} > 0$ (và trong 3D: $u_t = \alpha \nabla^2 u$).

## Mục tiêu

Bài học này giúp sinh viên hiểu phương trình nhiệt không phải là một công thức áp đặt sẵn, mà là hệ quả trực tiếp của hai nguyên lý vật lý cơ bản: định luật bảo toàn năng lượng và định luật dẫn nhiệt Fourier. Sau bài học, sinh viên cần nắm quá trình thiết lập phương trình nhiệt trong một chiều và nhiều chiều ở mức khái niệm, hiểu ý nghĩa của các tham số vật lý và thấy được vì sao phương trình nhiệt mang bản chất khuếch tán, làm mượt dữ liệu theo thời gian.

## Kiến thức nền

Sinh viên cần nắm vững đạo hàm riêng, đạo hàm bậc hai, tích phân trên đoạn hoặc trên miền, cùng trực giác vật lý cơ bản về nhiệt độ, dòng nhiệt và năng lượng. Kiến thức về định luật bảo toàn khối lượng hoặc năng lượng trong cơ học chất lưu cũng rất hữu ích vì cấu trúc lập mô hình tương đồng.

## Dẫn nhập

Trong nhiều tài liệu, phương trình nhiệt thường được viết ngay dưới dạng $$ u_t=\alpha^2u_{xx} $$ hoặc $$ u_t=\alpha^2\Delta u $$ rồi chuyển thẳng sang phần tìm nghiệm. Nếu tiếp cận theo cách đó, người học dễ nhớ công thức mà không hiểu vì sao đạo hàm bậc nhất theo thời gian lại liên hệ với đạo hàm bậc hai theo không gian. Bài học này làm rõ mối liên hệ đó.

Ý tưởng cốt lõi bắt nguồn từ cân bằng vật lý: nhiệt lượng trong một phần vật thể chỉ thay đổi khi có dòng nhiệt truyền qua biên hoặc có nguồn nhiệt sinh ra bên trong. Khi mật độ dòng nhiệt tỉ lệ với độ dốc nhiệt độ, phương trình cân bằng năng lượng tự động dẫn đến đạo hàm bậc hai theo không gian — dấu hiệu toán học đặc trưng của quá trình khuếch tán.

### Giải thích: Kiểm tra dấu của $u_t = \alpha u_{xx}$ bằng hình học độ cong tại đỉnh nóng và đáy lạnh

Không cần giải phương trình, bạn vẫn đọc ngay được xu hướng nhiệt độ tại mọi điểm chỉ bằng đạo hàm bậc hai $u_{xx}$ (độ cong của đồ thị $u$ theo $x$):
- **Tại đỉnh nóng** (ví dụ $u(x) = 100 - (x - 5)^2$ quanh $x = 5$): đồ thị úp xuống (lõm dưới) $\implies u_{xx} = -2 < 0 \implies u_t = \alpha(-2) < 0$: **đỉnh nóng lập tức nguội đi**!
- **Tại đáy lạnh** (ví dụ $u(x) = 20 + (x - 5)^2$ quanh $x = 5$): đồ thị ngửa lên (lõm trên) $\implies u_{xx} = +2 > 0 \implies u_t = \alpha(+2) > 0$: **đáy lạnh lập tức ấm lên**!
- **Khi phân bố tuyến tính** ($u(x) = 10 + 4x$): đồ thị là đường thẳng $\implies u_{xx} = 0 \implies u_t = 0$: nhiệt chảy vào bằng đúng nhiệt chảy ra, thanh đạt **trạng thái dừng (steady state)**!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một điểm trên thanh kim loại nóng hơn vùng lân cận, nhiệt sẽ truyền từ điểm đó ra hai phía; ngược lại, nếu lạnh hơn vùng xung quanh, nhiệt sẽ truyền vào. Do đó, tốc độ biến thiên nhiệt độ tại một điểm không phụ thuộc vào giá trị nhiệt độ riêng lẻ tại đó, mà phụ thuộc vào độ chênh lệch giữa điểm đó và mức trung bình lân cận. Đây chính là ý nghĩa trực quan của đạo hàm bậc hai.

### Cách nhìn hình ảnh

Hãy xét đồ thị phân bố nhiệt độ dọc theo một thanh. Tại một đỉnh nhọn, nhiệt thoát ra hai phía khiến đỉnh hạ thấp dần; tại một vùng lõm, nhiệt từ hai bên tràn vào làm vùng lõm nâng lên. Vì vậy, phương trình nhiệt có xu hướng làm phẳng đồ thị theo thời gian: các đỉnh bị hạ xuống, các hõm được lấp đầy và các dao động tần số cao tắt nhanh hơn nhiều so với biến thiên chậm.

### Cách nhìn hình thức

Gọi $$ u(x,t) $$ là nhiệt độ. Định luật Fourier xác định mật độ dòng nhiệt là $$ q=-k u_x $$ trong một chiều, hoặc $$ \mathbf q=-k\nabla u $$ trong nhiều chiều. Dấu trừ thể hiện chiều truyền nhiệt từ nơi nhiệt độ cao sang nơi nhiệt độ thấp.

Định luật bảo toàn năng lượng trên đoạn $$ [x,x+\Delta x] $$ cho phương trình

$$
\frac{d}{dt}\int_x^{x+\Delta x}\rho c\,u(\xi,t)\,d\xi
=
q(x,t)-q(x+\Delta x,t)+\int_x^{x+\Delta x}Q(\xi,t)\,d\xi.
$$

Chia hai vế cho $$ \Delta x $$ và cho $$ \Delta x\to 0 $$, ta thu được $$ \rho c\,u_t=-q_x+Q $$. Thay $$ q=-ku_x $$, suy ra $$ \rho c\,u_t=(k u_x)_x+Q $$. Khi $$ k $$ là hằng số, phương trình trở thành

$$
u_t=\alpha^2u_{xx}+\frac{Q}{\rho c},
\qquad
\alpha^2=\frac{k}{\rho c}.
$$

## Những ngộ nhận thường gặp

- "Phương trình nhiệt chỉ áp dụng cho nhiệt độ." Sai; phương trình này còn mô tả nhiều quá trình khuếch tán khác.
- "Định luật Fourier là một hệ quả toán học hiển nhiên." Không đúng; đây là định luật thực nghiệm được đưa vào mô hình vật lý.
- "Đạo hàm bậc hai chỉ xuất hiện như một bước biến đổi giải tích." Sai; nó đo độ chênh lệch giữa giá trị tại một điểm và giá trị trung bình xung quanh.
- "Khi có nguồn nhiệt thì chỉ cần cộng thêm một hằng số vào phương trình." Không đúng; nguồn nhiệt tổng quát có thể phụ thuộc cả vào vị trí lẫn thời gian.

## Tiến trình học tập đề xuất

### Bước 1: Xác định đại lượng cần mô hình hóa

Nhiệt độ được biểu diễn như một trường hàm theo không gian và thời gian.

### Bước 2: Biểu diễn dòng nhiệt theo gradient

Đây là bước đưa định luật thực nghiệm Fourier vào mô hình.

### Bước 3: Lập phương trình cân bằng năng lượng trên một đoạn nhỏ

Cần nắm chắc dạng tích phân này trước khi chuyển sang phương trình vi phân.

### Bước 4: Chuyển từ mô tả tích phân sang mô tả vi phân

Lấy giới hạn khi độ dài đoạn tiến về 0 để thu được PDE.

### Bước 5: Diễn giải bản chất khuếch tán

Sinh viên cần giải thích được bằng lời vì sao nghiệm của phương trình nhiệt có xu hướng làm mượt dữ liệu.

### Các điểm kiểm tra

- Sinh viên có giải thích được ý nghĩa vật lý của dấu trừ trong định luật Fourier hay không.
- Sinh viên có hiểu vì sao cân bằng năng lượng dẫn đến đạo hàm theo thời gian hay không.
- Sinh viên có diễn giải được $$ u_{xx} $$ như độ lệch so với mức trung bình lân cận hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Thanh một chiều không có nguồn nhiệt

Giả sử $$ Q=0 $$ và các hệ số $$ k,\rho,c $$ đều là hằng số. Khi đó

$$ \rho c\,u_t=k u_{xx}. $$

Chia hai vế cho $$ \rho c $$, ta thu được phương trình nhiệt chuẩn $$ u_t=\alpha^2u_{xx} $$. Đây là dạng cơ bản nhất cần nắm vững trước khi xét nguồn nhiệt hoặc vật liệu không đồng nhất.

### Ví dụ 2: Thanh có nguồn nhiệt đều

Nếu thanh có nguồn nhiệt không đổi $$ Q=Q_0 $$, phương trình trở thành

$$ u_t=\alpha^2u_{xx}+\frac{Q_0}{\rho c}. $$

Về mặt vật lý, ngoài quá trình khuếch tán, toàn bộ miền còn được cấp nhiệt đều đặn theo thời gian.

### Ví dụ 3: Hệ số dẫn nhiệt biến thiên

Với vật liệu không đồng nhất, ta không thể viết đơn giản thành $$ k u_{xx} $$, mà phải giữ nguyên dạng $$ \rho c\,u_t=(k(x)u_x)_x+Q $$. Ví dụ này cho thấy dạng của PDE phản ánh trực tiếp tính chất không đồng nhất của môi trường.

### Ví dụ 4: Cơ chế làm mượt của đạo hàm bậc hai

Giả sử phân bố nhiệt độ ban đầu có một đỉnh cực đại cục bộ. Tại vùng đỉnh, $$ u_{xx}<0 $$, nên khi không có nguồn nhiệt thì $$ u_t<0 $$, nghĩa là đỉnh nhiệt hạ xuống theo thời gian. Tương tự, tại một điểm lõm cục bộ, $$ u_{xx}>0 $$ khiến nhiệt độ tăng lên. Ví dụ ngắn này nối trực tiếp dấu của đạo hàm với trực giác khuếch tán.

## Câu hỏi khái niệm

1. Vì sao tốc độ thay đổi nhiệt độ tại một điểm lại phụ thuộc vào độ cong của đồ thị nhiệt độ chứ không chỉ phụ thuộc vào giá trị nhiệt độ tại điểm đó?
2. Dấu trừ trong định luật Fourier biểu thị đặc điểm vật lý nào của dòng nhiệt?
3. Vì sao phương trình nhiệt làm mượt dữ liệu ban đầu thay vì tạo ra các đỉnh mới?

## Bài toán ứng dụng

1. Một thanh kim loại được nung nóng cục bộ ở chính giữa. Hãy giải thích bằng lời vì sao vùng nóng sẽ lan rộng đồng thời đỉnh nhiệt độ hạ dần xuống.
2. Trong sinh học, nếu $$ u $$ là nồng độ một chất đang khuếch tán, định luật tương tự định luật Fourier mang ý nghĩa vật lý gì?
3. Trong vật liệu không đồng nhất, vì sao hệ số dẫn nhiệt phụ thuộc vị trí khiến phương trình có dạng $$ (k(x)u_x)_x $$ thay vì $$ k u_{xx} $$?

## Chiến lược giảng dạy tương tác

- Khởi đầu bằng câu hỏi: "Nếu một điểm nóng hơn các điểm lân cận, nhiệt sẽ truyền theo chiều nào?"
- Yêu cầu sinh viên mô tả bằng lời dạng đồ thị khiến nhiệt độ giảm và dạng đồ thị khiến nhiệt độ tăng.
- Tổ chức thảo luận nhóm nhỏ: một nhóm trình bày định luật Fourier, nhóm khác trình bày định luật bảo toàn năng lượng, sau đó kết hợp hai phần để thiết lập PDE.
- Đưa ra đồ thị có đỉnh và hõm để cả lớp dự đoán dấu của $$ u_t $$ trước khi viết phương trình.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên trình bày kỹ trường hợp một chiều trên một đoạn thanh nhỏ trước. Khi trực giác và phép biến đổi một chiều đã vững, việc mở rộng sang nhiều chiều sẽ thuận lợi hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự thiết lập phương trình nhiệt nhiều chiều bằng định lý phân kỳ (divergence theorem), hoặc so sánh sự khác biệt căn bản về tốc độ lan truyền thông tin giữa mô hình khuếch tán và mô hình sóng.

## Tóm tắt dễ nhớ

Phương trình nhiệt hình thành từ sự kết hợp giữa bảo toàn năng lượng và định luật Fourier. Vì nhiệt truyền từ nơi nóng sang nơi lạnh, tốc độ biến thiên nhiệt độ tại mỗi điểm được quyết định bởi độ cong không gian của phân bố nhiệt độ, tạo nên tính chất khuếch tán và làm mượt dữ liệu theo thời gian.

## Video tham khảo

- Xem trước: [(PHƯƠNG TRÌNH ĐẠO HÀM RIÊNG) PHƯƠNG TRÌNH TRUYỀN NHIỆT](https://www.youtube.com/watch?v=LJ6rd2EGVEI) — Đặng Pete, tiếng Việt. Thiết lập và giới thiệu phương trình truyền nhiệt bằng tiếng Việt.
- [Deriving the Heat Equation: A Parabolic Partial Differential Equation for Heat Energy Conservation](https://www.youtube.com/watch?v=9d8PwnKVA-U) — Steve Brunton, tiếng Anh. Trình bày cách suy ra phương trình nhiệt một chiều từ nguyên lý bảo toàn năng lượng.
- [But what is a partial differential equation?  | DE2](https://www.youtube.com/watch?v=ly4S0oi3Yz8) — 3Blue1Brown, tiếng Anh. Giới thiệu khái niệm phương trình đạo hàm riêng lấy phương trình truyền nhiệt làm ví dụ trung tâm.

## Tài liệu tham khảo

- Evans, *Partial Differential Equations* — tài liệu chuẩn về phương trình nhiệt, nguyên lý cực đại và hàm Green.
- Haberman, *Applied Partial Differential Equations* — cung cấp nhiều ví dụ vật lý và phương pháp giải minh họa rõ ràng.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dẫn nhiệt trong thanh kim loại
- Bài toán: Mô tả nhiệt lượng lan truyền từ vùng nóng sang vùng lạnh dọc theo một thanh dài.
- Mô hình:
$$ u_t=\alpha^2 u_{xx}. $$
- Giả thiết và giới hạn: Dẫn nhiệt một chiều, vật liệu đồng nhất, không có nguồn nhiệt bên ngoài.
- Diễn giải: Đạo hàm theo thời gian đo tốc độ thay đổi nhiệt độ, còn đạo hàm không gian bậc hai đo độ cong của phân bố nhiệt.

#### Khuếch tán chất hòa tan
- Bài toán: Nồng độ muối hoặc chất màu lan dần trong môi trường lỏng.
- Mô hình: Sử dụng cùng phương trình nhiệt với $$ u $$ biểu thị nồng độ.
- Giả thiết và giới hạn: Hệ số khuếch tán không đổi, môi trường đồng nhất.
- Diễn giải: Phương trình nhiệt là mô hình tiêu chuẩn cho các quá trình làm san bằng chênh lệch nồng độ.

### 2. Trực giác bổ sung và các kết nối

Phương trình nhiệt là mô hình điển hình của quá trình khuếch tán: tại những vùng phân bố nhiệt có độ cong lớn, quá trình tiến hóa theo thời gian sẽ nhanh chóng làm phẳng nó. Đạo hàm bậc hai không chỉ là ký hiệu giải tích mà đo trực tiếp độ lệch khỏi trạng thái cân bằng cục bộ. Bài học này chuyển tiếp tự nhiên từ trạng thái dừng ở Chương 7 sang bài toán tiến hóa theo thời gian.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
u0 = np.where(x < 0.5, 1.0, 0.0)

plt.plot(x, u0, label="t = 0")
for t, sigma in [(0.002, 0.03), (0.01, 0.07), (0.03, 0.12)]:
    kernel = np.exp(-((x[:, None] - x[None, :])**2) / (4 * sigma**2))
    kernel /= kernel.sum(axis=1, keepdims=True)
    ut = kernel @ u0
    plt.plot(x, ut, label=f"t ~ {t}")

plt.xlabel("x")
plt.ylabel("u")
plt.title("Lam phang profile nhiet theo thoi gian")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: heat equation diffusion animation
- search: derivation Fourier law conservation energy heat equation
- search: smoothing effect heat equation

### 5. Bài toán mẫu có bối cảnh thực

Từ định luật Fourier
$$ q=-k u_x $$
và phương trình bảo toàn năng lượng trên một đoạn nhỏ, ta thu được
$$ u_t=\alpha^2 u_{xx}. $$
Ý nghĩa vật lý cốt lõi là thông lượng nhiệt luôn hướng về phía có nhiệt độ thấp hơn, và tốc độ thay đổi nhiệt độ tại một điểm được quyết định bởi hiệu thông lượng đi vào và đi ra ở hai phía.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm vững cách thiết lập phương trình nhiệt từ định luật bảo toàn năng lượng và định luật Fourier.

**Bậc sau đại học.** Phân tích bản chất parabolic, tính làm trơn tức thời của nghiệm và đối chiếu với phương trình sóng cùng hàm điều hòa.
