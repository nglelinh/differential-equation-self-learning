---
layout: post
title: "06-03 Phương trình Euler"
chapter: '06'
order: 3
owner: Course Team
lang: vi
categories:
- chapter06
lesson_type: required
---

Trước khi chinh phục điểm kỳ dị tổng quát bằng phương pháp Frobenius, ta có một "phòng tập" hoàn hảo giải được bằng công thức đóng: **Phương trình Cauchy–Euler** $x^2 y'' + \alpha x y' + \beta y = 0$. Điểm kỳ dị tại $x = 0$ trông có vẻ đáng sợ, nhưng chỉ cần đặt nghiệm thử $y = x^r$ (hoặc đổi biến $x = e^t$), phương trình biến đổi kỳ diệu thành một phương trình đặc trưng bậc hai quen thuộc!

## Kiến thức cần nhớ: Bốn trụ cột của Phương trình Cauchy–Euler

1. **Đối xứng co giãn (Scale Invariance)**:
   Thay $x \to kx$ giữ nguyên hoàn toàn cấu trúc phương trình—đó là lý do sâu xa giải thích vì sao nghiệm tự nhiên có dạng lũy thừa $y = x^r$.
2. **Phương trình chỉ số (Indicial Equation)**:
   Thế $y = x^r$ cho $r(r - 1) + \alpha r + \beta = 0 \iff r^2 + (\alpha - 1)r + \beta = 0$.
3. **Ba dạng nghiệm theo biệt thức ($\Delta$)**:
   - Hai nghiệm thực phân biệt $r_1 \neq r_2$: $y = c_1 x^{r_1} + c_2 x^{r_2}$.
   - Nghiệm kép $r_1 = r_2 = r$: $y = (c_1 + c_2 \ln x) x^r$ (xuất hiện $\ln x$!).
   - Cặp nghiệm phức $\lambda \pm i\mu$: $y = x^\lambda\big(c_1 \cos(\mu \ln x) + c_2 \sin(\mu \ln x)\big)$.
4. **Cầu nối sang Phương pháp Frobenius**:
   Mọi phương trình có điểm kỳ dị chính quy tại $x = 0$ đều hành xử *gần giống* phương trình Euler khi $x \to 0$!

## Mục tiêu

Bài học này giúp sinh viên nhận dạng và giải phương trình Euler (hay Cauchy–Euler), xem đây là cầu nối giữa nghiệm dạng lũy thừa, phương trình chỉ số và phép đổi biến logarit. Sau bài học, sinh viên cần hiểu vì sao dạng thử $$ x^r $$ xuất hiện tự nhiên, biết phân loại ba trường hợp nghiệm và nắm được phép đổi biến đưa phương trình Euler về phương trình hệ số hằng.

## Kiến thức nền

Sinh viên nên nắm vững phương trình vi phân tuyến tính cấp hai hệ số hằng, phương trình đặc trưng, các trường hợp nghiệm kép và nghiệm phức cùng các quy tắc đạo hàm cơ bản. Hiểu rõ tính chất của hàm lũy thừa và hàm logarit là điều kiện quan trọng cho bài này.

## Dẫn nhập

![Phương trình Euler-Cauchy và dạng nghiệm lũy thừa]({{ site.imgurl }}/chapter_img/chapter06/03_euler_equations.svg)

Phương trình Euler có hệ số biến thiên theo $$ x $$, khác với phương trình hệ số hằng. Tuy nhiên, cấu trúc của nó rất đặc biệt: mỗi đạo hàm bậc $$ k $$ đều nhân với $$ x^k $$, nhờ đó phương trình bất biến dưới phép co giãn biến độc lập. Tính chất đối xứng này khiến hàm lũy thừa $$ x^r $$ xuất hiện một cách tự nhiên, tương tự như hàm mũ $$ e^{rx} $$ đối với phương trình hệ số hằng (bất biến theo phép tịnh tiến).

Qua đó, sinh viên thấy rằng việc chọn dạng nghiệm thử không phải thủ thuật tùy tiện mà phản ánh trực tiếp tính đối xứng ẩn của phương trình — ở đây là đối xứng co giãn.

### Giải thích: Giải làm từng bước 2 phương trình Euler cho trường hợp nghiệm kép và nghiệm phức ($x > 0$)

1. **Trường hợp 1**: $x^2 y'' - 3x y' + 4y = 0$ ($\alpha = -3,\; \beta = 4$).
   - Phương trình chỉ số: $r(r - 1) - 3r + 4 = r^2 - 4r + 4 = (r - 2)^2 = 0 \implies r = 2$ (nghiệm kép!).
   - Nghiệm tổng quát: $y(x) = c_1 x^2 + c_2 x^2 \ln x$.
   - Kiểm tra nhanh $y_2 = x^2 \ln x$: $y_2' = 2x\ln x + x$, $y_2'' = 2\ln x + 3 \implies x^2(2\ln x + 3) - 3x(2x\ln x + x) + 4x^2\ln x = (2 - 6 + 4)x^2\ln x + (3 - 3)x^2 = \mathbf{0}$!
2. **Trường hợp 2**: $x^2 y'' + x y' + 4y = 0$ ($\alpha = 1,\; \beta = 4$).
   - Phương trình chỉ số: $r(r-1) + r + 4 = r^2 + 4 = 0 \implies r = \pm 2i$ ($\lambda = 0, \mu = 2$).
   - Nghiệm tổng quát: $y(x) = c_1 \cos(2\ln x) + c_2 \sin(2\ln x)$ (dao động ngày càng dày đặc khi $x \to 0^+$!).

## Khái niệm theo ba cách

### Cách nhìn trực quan

Nếu một bài toán giữ nguyên cấu trúc khi ta co giãn trục tọa độ theo tỉ lệ, nghiệm của nó cũng thường biến đổi theo quy luật tỉ lệ. Hàm lũy thừa $$ y=x^r $$ đáp ứng chính xác đặc tính này: khi thay $$ x $$ bởi $$ cx $$, hàm chỉ nhân thêm hằng số $$ c^r $$.

### Cách nhìn hình ảnh

Trên đồ thị log–log, hàm lũy thừa biểu diễn thành một đường thẳng. Vì vậy, phương trình Euler trở nên đơn giản hóa khi quan sát trong thang logarit. Khi phương trình chỉ số có nghiệm phức, đồ thị nghiệm không dao động đều theo $$ x $$ mà dao động điều hòa theo $$ \ln x $$.

### Cách nhìn hình thức

Phương trình Euler cấp hai có dạng chuẩn

$$ x^2y''+a x y'+b y=0,
\qquad x>0. $$

Thử nghiệm dạng $$ y=x^r $$, ta có

$$ y'=r x^{r-1},
\qquad
y''=r(r-1)x^{r-2}. $$

Thay vào phương trình:

$$ x^2r(r-1)x^{r-2}+a x r x^{r-1}+b x^r=0. $$

Đặt nhân tử chung $$ x^r $$:

$$ \left[r(r-1)+ar+b\right]x^r=0. $$

Từ đây thu được **phương trình chỉ số** $$ r(r-1)+ar+b=0 $$. Tùy theo bản chất nghiệm của phương trình bậc hai này, ta có ba trường hợp nghiệm tương ứng.

## Những ngộ nhận thường gặp

- "Phương trình Euler chỉ là dạng biến thể nhỏ của phương trình hệ số hằng nên không cần học riêng." Sai. Nó gắn với đối xứng co giãn và đóng vai trò nền tảng trực tiếp cho phương pháp Frobenius.
- "Chỉ cần học thuộc công thức nghiệm là đủ." Chưa đủ; bước quan trọng là nhận diện đúng cấu trúc Euler và điều kiện miền xác định.
- "Khi có nghiệm kép thì hai nghiệm độc lập đều có dạng $$ x^r $$." Sai. Nghiệm độc lập thứ hai phải có thêm nhân tử $$ \ln x $$.
- "Nghiệm chỉ số phức nghĩa là phương trình không có nghiệm thực." Sai. Từ cặp nghiệm phức liên hợp, ta luôn lập được hai nghiệm thực độc lập chứa $$ \cos(\beta\ln x) $$ và $$ \sin(\beta\ln x) $$.

## Tiến trình học tập đề xuất

### Bước 1: Nhận dạng cấu trúc Euler

Kiểm tra xem phương trình có đúng dạng $$ x^2y''+a x y'+b y=0 $$ hoặc có thể biến đổi về dạng này hay không.

### Bước 2: Thử nghiệm dạng lũy thừa

Đặt $$ y=x^r $$ để rút ra phương trình chỉ số.

### Bước 3: Phân loại nghiệm của phương trình chỉ số

Xử lý ba trường hợp: hai nghiệm thực phân biệt, nghiệm kép và hai nghiệm phức liên hợp.

### Bước 4: Lưu ý miền xác định

Kiểm tra điều kiện $$ x>0 $$ (hoặc dùng $$ \lvert x\rvert $$ khi xét $$ x<0 $$) cho các biểu thức chứa lũy thừa thực và logarit.

### Bước 5: Liên hệ với phép đổi biến logarit

Thực hiện phép đặt $$ x=e^t $$ để thấy phương trình Euler quy về phương trình tuyến tính hệ số hằng theo biến $$ t $$.

### Các điểm kiểm tra

- Sinh viên có nhận diện nhanh phương trình dạng Euler hay không.
- Sinh viên có lập chính xác phương trình chỉ số hay không.
- Sinh viên có viết đúng nghiệm tổng quát trong cả ba trường hợp nghiệm hay không.
- Sinh viên có giải thích được nguồn gốc của nhân tử $$ \ln x $$ trong trường hợp nghiệm kép hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Kiểm tra biệt thức — trường hợp nghiệm kép

Giải phương trình $$ x^2y''-3xy'+4y=0 $$. Đặt $$ y=x^r $$, phương trình chỉ số là

$$
r(r-1)-3r+4=0
\quad \Longleftrightarrow \quad
r^2-4r+4=0.
$$

Phương trình có nghiệm kép $$ r=2 $$. Ví dụ này nhắc sinh viên cần tính cẩn thận biệt thức thay vì ước lượng vội. Nghiệm tổng quát là

$$ y=c_1x^2+c_2x^2\ln x. $$

### Ví dụ 2: Hai nghiệm thực phân biệt

Giải phương trình $$ x^2y''+x y'-y=0 $$. Phương trình chỉ số là:

$$
r(r-1)+r-1=0
\quad \Longleftrightarrow \quad
r^2-1=0.
$$

Suy ra $$ r_1=1,\qquad r_2=-1 $$. Nghiệm tổng quát là $$ y=c_1x+c_2x^{-1} $$, minh họa rõ ràng nghiệm Euler là tổ hợp tuyến tính của các hàm lũy thừa.

### Ví dụ 3: Nghiệm kép và vai trò của logarit

Giải phương trình $$ x^2y''-x y'+y=0 $$. Ta có

$$
r(r-1)-r+1=0
\quad \Longleftrightarrow \quad
r^2-2r+1=0
\quad \Longleftrightarrow \quad
(r-1)^2=0.
$$

Với nghiệm kép $$ r=1 $$, nghiệm tổng quát là:

$$ y=c_1x+c_2x\ln x. $$

Từ ví dụ này, sinh viên có thể kiểm tra trực tiếp bằng Wronskian để thấy $$ x $$ và $$ x\ln x $$ độc lập tuyến tính trên $$ (0,\infty) $$.

### Ví dụ 4: Nghiệm phức liên hợp

Giải phương trình $$ x^2y''+x y'+4y=0 $$. Phương trình chỉ số là:

$$
r(r-1)+r+4=0
\quad \Longleftrightarrow \quad
r^2+4=0.
$$

Suy ra $$ r=\pm 2i $$. Viết dưới dạng nghiệm thực:

$$ y=c_1\cos(2\ln x)+c_2\sin(2\ln x). $$

Nghiệm này cho thấy dao động diễn ra tuần hoàn theo $$ \ln x $$ chứ không theo $$ x $$.

### Ví dụ 5: Phép đổi biến đưa về hệ số hằng

Với phương trình $$ x^2y''+3xy'+y=0 $$, đặt

$$ x=e^t,
\qquad
u(t)=y(e^t). $$

Áp dụng quy tắc đạo hàm hàm hợp, ta thu được

$$ x y' = u',
\qquad
x^2 y''=u''-u'. $$

Thay vào phương trình ban đầu cho $$ u''+2u'+u=0 $$. Đây là phương trình hệ số hằng có nghiệm $$ u=(c_1+c_2 t)e^{-t} $$. Thay ngược $$ t=\ln x $$, ta có $$ y=(c_1+c_2\ln x)x^{-1} $$, cho thấy cấu trúc nghiệm của phương trình Euler bắt nguồn trực tiếp từ phương trình hệ số hằng.

## Câu hỏi khái niệm

1. Vì sao phép thử $$ y=x^r $$ tự nhiên hơn nhiều so với $$ y=e^{rx} $$ đối với phương trình Euler?
2. Vì sao nghiệm kép lại đi kèm nhân tử $$ \ln x $$ thay vì một số mũ mới?
3. Nghiệm phức của phương trình Euler phản ánh tính đối xứng co giãn của bài toán như thế nào?

## Bài toán ứng dụng

1. Trong bài toán đàn hồi hoặc truyền nhiệt gần một góc nhọn, các phương trình dạng Euler thường xuất hiện. Hãy giải thích mối liên hệ giữa tính tự đồng dạng của hình học với dạng phương trình này.
2. Trong cơ học chất lưu, khi một mô hình không đổi dưới phép co giãn kích thước, vì sao nghiệm dạng lũy thừa là lựa chọn tự nhiên?
3. Trong phân tích dữ liệu thực nghiệm trên đồ thị log–log, vì sao đồ thị dạng đường thẳng lại gợi ý một quy luật lũy thừa?

## Chiến lược giảng dạy tương tác

- Cho sinh viên lập bảng so sánh song song ba trường hợp nghiệm của phương trình Euler với phương trình hệ số hằng.
- Đặt câu hỏi thảo luận: khi thay $$ x $$ bởi $$ cx $$, hàm mũ và hàm lũy thừa biến đổi khác nhau như thế nào?
- Minh họa bằng đồ thị log–log để giải thích sự xuất hiện tự nhiên của hàm lũy thừa.
- Yêu cầu các nhóm tính Wronskian để kiểm chứng tính độc lập tuyến tính của $$ x^r $$ và $$ x^r\ln x $$.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên sử dụng bảng tóm tắt bốn cột: phương trình, phương trình chỉ số, loại nghiệm và dạng nghiệm tổng quát để sinh viên dễ tra cứu và tránh nhầm lẫn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên tự chứng minh các đồng nhất thức của phép đổi biến $$ x=e^t $$ chuyển phương trình Euler thành phương trình hệ số hằng, sau đó đối chiếu hai cách giải.

## Tóm tắt dễ nhớ

Phương trình Euler bất biến dưới phép co giãn nên nghiệm dạng lũy thừa $$ y=x^r $$ là lựa chọn tự nhiên. Từ phương trình chỉ số bậc hai, hai nghiệm thực phân biệt cho hai lũy thừa, nghiệm kép bổ sung nhân tử $$ \ln x $$, còn cặp nghiệm phức liên hợp cho dao động theo $$ \ln x $$.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Truyền nhiệt hoặc thế năng trong hình học tự đồng dạng
- Bài toán: Các bài toán vật lý có tính đối xứng co giãn theo tỉ lệ thường dẫn đến phương trình Euler–Cauchy.
- Mô hình:
$$ x^2 y''+a x y'+b y=0. $$
- Giả thiết và giới hạn: Xét trên miền $$ x>0 $$ với cấu trúc bất biến theo phép co giãn.
- Diễn giải: Nghiệm dạng $$ x^r $$ phản ánh trực tiếp bản chất quy luật lũy thừa của hệ.

#### Mô hình kinh tế có độ co giãn không đổi
- Bài toán: Khảo sát đại lượng tăng trưởng theo thời gian với các hệ số tỉ lệ nghịch theo $$ t $$.
- Mô hình:
$$ t^2 K''+\alpha t K'+\beta K=0. $$
- Giả thiết và giới hạn: Là mô hình lý tưởng hóa cho cấu trúc đồng thứ nguyên theo thang thời gian.
- Diễn giải: Các nghiệm lũy thừa mô tả chế độ tăng trưởng hoặc suy giảm theo hàm mũ của $$ \ln t $$.

### 2. Trực giác bổ sung và các kết nối

Điểm đặc biệt của phương trình Euler là thay vì nghiệm $$ e^{\lambda x} $$ như ở hệ số hằng, ta thu được nghiệm $$ x^r $$ nhờ tính bất biến co giãn. Phép đổi biến $$ x=e^t $$ cho thấy phương trình Euler–Cauchy tương đương hoàn toàn với một ODE hệ số hằng. Lỗi thường gặp là quên nhân tử $$ \ln x $$ trong trường hợp nghiệm kép hoặc quên dao động theo $$ \ln x $$ khi nghiệm chỉ số là số phức.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.2, 5, 400)
y1 = x**2
y2 = x**2 * np.log(x)

plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^2 log x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dang nghiem tieu bieu cua phuong trinh Euler")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Cauchy Euler equation log transform
- search: equidimensional equation power law solutions
- search: scaling invariant ODE visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình
$$ x^2 y''-3x y'+4y=0. $$
Đặt $$ y=x^r $$, ta thu được phương trình chỉ số
$$ r(r-1)-3r+4=0 $$
tương đương
$$ r^2-4r+4=(r-2)^2=0. $$
Do có nghiệm kép $$ r=2 $$, nghiệm tổng quát là
$$ y=C_1 x^2+C_2 x^2\ln x. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo dạng nghiệm thử $$ x^r $$ và xử lý ba trường hợp: hai nghiệm phân biệt, nghiệm kép và nghiệm phức.

**Bậc sau đại học.** Nhấn mạnh tính đối xứng co giãn, phép đổi biến $$ x=e^t $$ và liên hệ với các bài toán tự đồng dạng.

## Video tham khảo

- Xem trước: [Cauchy Euler Differential Equation (equidimensional equation)](https://www.youtube.com/watch?v=zXZ4qmDpblE) — blackpenredpen, tiếng Anh. Giới thiệu phương trình Cauchy–Euler và phép thử $$ x^r $$.
- [Cauchy-Euler Differential Equations (2nd Order)](https://www.youtube.com/watch?v=ep7xoctAlEY) — Houston Math Prep, tiếng Anh. Giải chi tiết một phương trình Cauchy–Euler cấp hai.
- [Introduction to Cauchy Euler Differential Equations](https://www.youtube.com/watch?v=oqpc89Lfx-E) — The Math Sorcerer, tiếng Anh. Giải thích vì sao phương trình đồng thứ nguyên là hình mẫu cho điểm kỳ dị chính quy.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 5: phương trình Euler và các trường hợp nghiệm đặc biệt.
- Zill, Chương 6: nhiều ví dụ thực hành về nghiệm lũy thừa và nghiệm chứa logarit.
