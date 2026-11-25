---
layout: post
title: "04-01 Giới thiệu Hệ Phương trình"
chapter: '04'
order: 1
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---


Trong tự nhiên, hiếm khi nào một đại lượng biến đổi trong cô lập: số lượng thỏ ảnh hưởng đến số lượng cáo, dòng điện ở nhánh mạch này cảm ứng sang nhánh kia, và chuyển động của con lắc kéo theo phản lực lên điểm treo. **Hệ phương trình vi phân thường** gom tất cả những mối tương tác đan xen đó vào một vectơ trạng thái duy nhất $\mathbf{x}(t) \in \mathbb{R}^n$—và đáng kinh ngạc hơn nữa, **mọi** phương trình vi phân bậc $n$ bất kỳ đều quy đổi tương đương hoàn toàn về một hệ bậc một!

## Kiến thức cần nhớ: Bốn viên gạch đầu tiên của Hệ PTVP

1. **Chuyển đổi PTVP bậc $n$ thành Hệ bậc một**:
   Đặt $x_1 = y,\; x_2 = y', \dots, x_n = y^{(n-1)}$—mọi bộ giải số máy tính (như `scipy.integrate.solve_ivp`) thực chất chỉ cần một thuật toán duy nhất cho hệ bậc một $\mathbf{x}' = \mathbf{f}(t, \mathbf{x})$!
2. **Không gian trạng thái (Phase Space) & Quỹ đạo vectơ**:
   Thay vì $n$ đồ thị rời rạc theo $t$, trạng thái tức thời của toàn hệ là **một điểm duy nhất $\mathbf{x}(t) \in \mathbb{R}^n$** chuyển động theo trường vectơ vận tốc $\mathbf{f}(t, \mathbf{x})$.
3. **Phân loại Tuyến tính vs. Phi tuyến & Tự trị vs. Không tự trị**:
   Hệ tuyến tính có dạng $\mathbf{x}' = A(t)\mathbf{x} + \mathbf{g}(t)$; hệ tự trị không chứa $t$ tường minh ở vế phải nên trường vectơ cố định theo thời gian.
4. **Định lý Tồn tại & Duy nhất cho Hệ**:
   Với hệ tuyến tính $\mathbf{x}' = A(t)\mathbf{x} + \mathbf{g}(t)$, nếu mọi phần tử của $A(t)$ và $\mathbf{g}(t)$ liên tục trên $I \ni t_0$, thì bài toán giá trị đầu $\mathbf{x}(t_0) = \mathbf{x}_0$ có **duy nhất một nghiệm** trên toàn $I$.

## Mục tiêu

Bài học này mở đầu chương về hệ phương trình vi phân, giúp sinh viên hiểu vì sao nhiều hiện tượng không thể mô tả đầy đủ bằng một ẩn duy nhất, biết cách biểu diễn trạng thái dưới dạng vector, và nắm mối liên hệ giữa phương trình bậc cao với hệ bậc nhất. Qua đó, sinh viên chuyển từ cách nhìn "một hàm theo thời gian" sang "toàn bộ vector trạng thái tiến hóa theo thời gian".

## Kiến thức nền

Sinh viên nên nắm ODE cấp một, ODE cấp hai, khái niệm điều kiện đầu và kiến thức cơ bản về vector, ma trận. Trực giác vật lý về vị trí, vận tốc, dòng chảy hoặc các quần thể tương tác sẽ giúp bài học dễ tiếp cận hơn.

## Dẫn nhập

![Sơ đồ chuyển từ phương trình bậc cao sang hệ trạng thái]({{ site.imgurl }}/chapter_img/chapter04/01_introduction_systems.svg)

Ở các chương trước, ta thường xét một phương trình cho một hàm ẩn duy nhất. Tuy nhiên, nhiều hiện tượng thực tế đòi hỏi nhiều biến cùng tiến hóa: một vật dao động cần cả vị trí và vận tốc, một mạch điện cần điện tích và dòng điện, còn một mô hình sinh thái cần theo dõi đồng thời nhiều loài. Khi nhiều đại lượng ảnh hưởng lẫn nhau, mô tả tự nhiên nhất là một hệ phương trình vi phân.

Hệ phương trình không chỉ là cách viết dài hơn của ODE một ẩn, mà là ngôn ngữ chuẩn cho các mô hình nhiều biến trạng thái. Khi biểu diễn trạng thái bằng vector, ta có thể vận dụng ngay ma trận, trị riêng, hàm mũ ma trận và chân dung pha để phân tích hình học của chuyển động.

### Giải thích: Chuyển PTVP bậc ba không thuần nhất $y''' - 2y'' + 5y' - y = \sin t$ thành hệ bậc một dạng ma trận

1. **Đặt 3 biến trạng thái**:
   $x_1 = y$, $\;x_2 = y'$, $\;x_3 = y''$.
2. **Viết đạo hàm từng biến** (chỉ dùng $x_1, x_2, x_3$ và $t$):
   - $x_1' = x_2$
   - $x_2' = x_3$
   - $x_3' = y''' = x_1 - 5x_2 + 2x_3 + \sin t$
3. **Đóng gói thành phương trình ma trận $\mathbf{x}' = A\mathbf{x} + \mathbf{g}(t)$**:
   $$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}' = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & -5 & 2 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ \sin t \end{pmatrix}.$$
   Nếu điều kiện đầu là $y(0) = 2,\; y'(0) = -1,\; y''(0) = 0$, thì vectơ đầu vào chỉ đơn giản là $\mathbf{x}(0) = (2, -1, 0)^\top$!

## Khái niệm theo ba cách

### Cách nhìn trực quan

Một hệ phương trình giống như một nhóm nhiều đối tượng cùng di chuyển, trong đó chuyển động của mỗi đối tượng phụ thuộc vào vị trí và trạng thái của các đối tượng còn lại. Để dự đoán diễn biến, ta phải theo dõi toàn bộ cấu hình của cả nhóm thay vì tách rời từng cá thể.

### Cách nhìn hình ảnh

Nếu ODE một ẩn biểu diễn nghiệm như đồ thị trên mặt phẳng $$ \left(t,y\right) $$, thì hệ hai ẩn tạo ra quỹ đạo trong mặt phẳng trạng thái $$ \left(x_1,x_2\right) $$, hệ ba ẩn tạo ra quỹ đạo trong không gian ba chiều, và tổng quát hơn là trong không gian trạng thái $$ \mathbb{R}^n $$. Nghiệm khi đó được nhìn như đường cong biểu diễn chuỗi cấu hình mà hệ đi qua.

### Cách nhìn hình thức

Một hệ phương trình vi phân cấp một tổng quát có dạng
$$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}), $$
trong đó
$$
\mathbf{x}(t)=
\begin{pmatrix}
x_1(t)\\
x_2(t)\\
\vdots\\
x_n(t)
\end{pmatrix}.
$$
Mọi phương trình bậc $$ n $$ dạng $$ y^{(n)}=F\left(t,y,y',\ldots,y^{(n-1)}\right) $$ đều đưa được về hệ bậc nhất bằng phép đặt
$$
x_1=y,\quad x_2=y',\quad \ldots,\quad x_n=y^{(n-1)},
$$
thu được:
$$
\begin{cases}
x_1'=x_2,\\
x_2'=x_3,\\
\vdots\\
x_{n-1}'=x_n,\\
x_n'=F(t,x_1,\ldots,x_n).
\end{cases}
$$

## Những ngộ nhận thường gặp

- "Hệ phương trình chỉ là cách viết lại của ODE bậc cao." Sai: tuy tương đương về mặt thông tin trong trường hợp chuyển đổi từ ODE bậc cao, dạng hệ làm lộ rõ cấu trúc trạng thái và sự tương tác giữa các biến.
- "Có thể hiểu riêng lẻ từng phương trình trong hệ." Không đúng: hành vi của hệ phát sinh từ sự ghép nối giữa các thành phần.
- "Trạng thái chỉ là giá trị của biến chính." Sai: trạng thái phải bao gồm toàn bộ các biến cần thiết để xác định diễn biến tương lai.
- "Chỉ hệ phi tuyến mới có hành vi đa dạng." Sai: ngay cả hệ tuyến tính cũng mang lại nhiều cấu trúc hình học và động lực học quan trọng.

## Tiến trình học tập đề xuất

### Bước 1: Xác định các biến trạng thái

Liệt kê những đại lượng cần biết tại một thời điểm để dự đoán tương lai của hệ.

### Bước 2: Biểu diễn trạng thái dưới dạng vector

Làm quen với ký hiệu vector gọn gàng và nhất quán.

### Bước 3: Chuyển ODE bậc cao thành hệ bậc nhất

Thực hành thuần thục phép đặt biến trạng thái.

### Bước 4: Đọc quỹ đạo trong không gian trạng thái

Phân biệt đồ thị theo thời gian với quỹ đạo trên mặt phẳng pha.

### Các checkpoint

- Sinh viên có giải thích được vì sao hệ cần nhiều biến trạng thái hay không.
- Sinh viên có chuyển chính xác một ODE bậc cao về hệ bậc nhất hay không.
- Sinh viên có phân biệt được quỹ đạo trạng thái với đồ thị hàm theo thời gian hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Chuyển dao động bậc hai sang hệ bậc nhất

Xét phương trình $$ y''+2y'+5y=0 $$. Đặt $$ x_1=y $$ và $$ x_2=y' $$, ta có $$ x_1'=x_2 $$ và $$ x_2'=-2x_2-5x_1 $$, thu được hệ
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
Ví dụ này cho thấy một ODE bậc hai thực chất tương đương với một hệ hai biến trạng thái.

### Ví dụ 2: Mô hình tương tác hai quần thể

Giả sử $$ x(t) $$ và $$ y(t) $$ là kích thước hai quần thể tương tác tuyến tính:
$$
\begin{cases}
x'=2x-y,\\
y'=x+3y.
\end{cases}
$$
Tốc độ thay đổi của mỗi quần thể phụ thuộc đồng thời vào cả hai quần thể; giữ nguyên dạng hệ giúp bảo toàn trực giác mô hình ban đầu.

### Ví dụ 3: Biến trạng thái trong mạch điện LC

Một mạch LC có thể mô tả bằng ODE bậc hai theo điện tích $$ q $$. Đặt $$ x_1=q $$ và $$ x_2=q' $$, ta thu được hệ hai chiều trong đó $$ x_1 $$ là điện tích trên tụ và $$ x_2 $$ là dòng điện chạy qua cuộn cảm. Cặp biến này phản ánh trực tiếp trạng thái năng lượng của mạch.

### Ví dụ 4: Điều kiện đầu của hệ

Với hệ $$ \mathbf{x}'=\mathbf{f}(t,\mathbf{x}) $$, điều kiện đầu có dạng $$ \mathbf{x}(t_0)=\mathbf{x}_0 $$, tức cho trước toàn bộ cấu hình khởi đầu của mọi thành phần trạng thái tại thời điểm $$ t_0 $$.

## Câu hỏi khái niệm

1. Vì sao nhiều mô hình vật lý và sinh học cần biểu diễn dưới dạng hệ thay vì một ODE một ẩn?
2. Khi chuyển ODE bậc hai sang hệ bậc nhất, thông tin trạng thái nào được làm rõ hơn?
3. Vì sao quỹ đạo trong không gian trạng thái thường bổ sung trực giác tốt hơn so với chỉ xem từng đồ thị theo thời gian?

## Bài toán ứng dụng

1. Một xe tự hành chuyển động trên đường thẳng được mô tả bởi vị trí và vận tốc. Vì sao chỉ biết vị trí tại một thời điểm là chưa đủ để dự đoán chuyển động tiếp theo?
2. Một mô hình dịch tễ gồm ba nhóm dân số: nhạy cảm, nhiễm bệnh và hồi phục. Vì sao hệ phương trình là cách mô tả tự nhiên?
3. Trong một mạch điện có điện tích và dòng điện cùng biến thiên, hãy giải thích ý nghĩa của vector trạng thái gồm hai thành phần này.

## Chiến lược giảng dạy tương tác

- Mở đầu bằng câu hỏi: "Để dự đoán chuyển động tiếp theo của một vật dao động, chỉ biết vị trí hiện tại có đủ không?"
- Cho sinh viên thực hành theo cặp chuyển 2–3 ODE bậc hai thành hệ bậc nhất.
- Vẽ song song đồ thị $$ y(t) $$ và quỹ đạo trên mặt phẳng $$ \left(y,y'\right) $$ để so sánh hai góc nhìn.
- Yêu cầu sinh viên diễn giải bằng lời ý nghĩa vật lý của từng thành phần trong vector trạng thái.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Cho sinh viên luyện theo quy trình cố định: đặt các biến trạng thái từ $$ y $$ đến $$ y^{(n-1)} $$, viết các phương trình nối tiếp $$ x_k'=x_{k+1} $$, sau đó thay phương trình gốc vào phương trình cuối cùng.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên khảo sát điều kiện để khử biến đưa một hệ bậc nhất hai chiều về một ODE bậc hai, và thảo luận những gì có thể bị mờ đi về mặt trực giác khi khử biến.

## Tóm tắt dễ nhớ

Hệ phương trình vi phân là ngôn ngữ của các hệ nhiều biến trạng thái. Mọi ODE bậc cao đều chuyển được về hệ bậc nhất, nhưng giá trị lớn hơn của dạng hệ là làm rõ tương tác giữa các thành phần và mở ra góc nhìn hình học qua quỹ đạo trong không gian trạng thái.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quỹ đạo của vật chuyển động trong mặt phẳng
- Bài toán: Để mô tả chuyển động hai chiều, cần theo dõi đồng thời tọa độ vị trí và hai thành phần vận tốc.
- Mô hình:
$$
\mathbf{x}(t)=
\begin{pmatrix}
x\\
y\\
v_x\\
v_y
\end{pmatrix},
\qquad
\mathbf{x}'=\mathbf{f}(t,\mathbf{x}).
$$
- Giả thiết và giới hạn: Bỏ qua các yếu tố phức tạp như lực cản phi tuyến mạnh hoặc chuyển động quay quanh trục.
- Diễn giải: Hệ bậc nhất tổ chức đầy đủ các thành phần trạng thái gắn kết trong một vector duy nhất.

#### Mô hình dịch tễ nhiều ngăn
- Bài toán: Số người nhạy cảm, nhiễm bệnh và hồi phục biến đổi đồng thời theo thời gian.
- Mô hình:
$$
\frac{dS}{dt}=f_1(S,I,R),\qquad
\frac{dI}{dt}=f_2(S,I,R),\qquad
\frac{dR}{dt}=f_3(S,I,R).
$$
- Giả thiết và giới hạn: Quần thể trộn đều, tham số không đổi, chưa xét phân bố độ tuổi hay không gian.
- Diễn giải: Dạng hệ thể hiện trực tiếp luồng chuyển dịch giữa các nhóm dân số.

#### Chuyển ODE bậc cao sang hệ trạng thái
- Bài toán: Đưa mô hình dao động cơ học bậc hai về dạng hệ bậc nhất để áp dụng công cụ ma trận và mặt phẳng pha.
- Mô hình:
$$
y''+2y'+5y=0
\quad\Longrightarrow\quad
\begin{cases}
x_1'=x_2,\\
x_2'=-2x_2-5x_1.
\end{cases}
$$
- Giả thiết và giới hạn: Chỉ thay đổi dạng biểu diễn, giữ nguyên hoàn toàn nội dung động học.
- Diễn giải: Là bước chuẩn bị trực tiếp cho toàn bộ Chương 04.

### 2. Trực giác bổ sung và các kết nối

Chuyển từ một hàm vô hướng sang một vector trạng thái nhiều chiều là thay đổi tư duy cốt lõi của chương. Mọi ODE bậc cao đều có thể xem như hệ bậc nhất, tạo nền trực tiếp cho việc nghiên cứu phổ ma trận và chân dung pha ở các bài sau. Cần tránh đọc rời rạc từng phương trình thành phần, vì đặc trưng của hệ nằm ở sự liên kết giữa chúng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def system(t, X):
    x1, x2 = X
    return [x2, -2*x2 - 5*x1]

t = np.linspace(0, 12, 600)
for x10, x20 in [(1, 0), (0, 1), (1, -1)]:
    sol = solve_ivp(system, [0, 12], [x10, x20], t_eval=t)
    plt.plot(sol.y[0], sol.y[1], label=f"IC=({x10},{x20})")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Quỹ đạo trạng thái của hệ bậc nhất tương đương")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: state space intuition differential equations
- search: converting second order ODE to first order system
- search: phase trajectory system of ODEs visualization

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình dao động $$ y''+2y'+5y=0 $$. Đặt $$ x_1=y $$ và $$ x_2=y' $$, ta thu được hệ
$$
\begin{cases}
x_1'=x_2,\\
x_2'=-5x_1-2x_2.
\end{cases}
$$
Điều kiện đầu $$ y(0)=1 $$, $$ y'(0)=0 $$ chuyển thành vector trạng thái ban đầu
$$
\mathbf{x}(0)=
\begin{pmatrix}
1\\
0
\end{pmatrix}.
$$
Biểu diễn này giữ nguyên thông tin của phương trình gốc đồng thời làm rõ cấu trúc trạng thái hai chiều.

### 6. Phân tầng độ khó

**Bậc đại học.** Chọn đúng biến trạng thái và chuyển thành thạo ODE bậc cao sang hệ bậc nhất.

**Bậc sau đại học.** Mở rộng sang không gian trạng thái, dòng động lực học và toán tử tiến hóa trên $$ \mathbb{R}^n $$.

## Video tham khảo

- Xem trước: [Systems of Differential Equations // Part 1: Linear Systems and the Eigenvalue Method](https://www.youtube.com/watch?v=aTMNQtzU0rU) — Dr. Trefor Bazett, tiếng Anh. Cách chuyển phương trình bậc cao thành hệ cấp một và viết hệ tuyến tính.
- [Matrix Systems of Differential Equations](https://www.youtube.com/watch?v=Vtijyyo5fKI) — Steve Brunton, tiếng Anh. Giới thiệu dạng ma trận $$ \mathbf{x}'=A\mathbf{x} $$ cho hệ phương trình vi phân.
- [Lec 24 | MIT 18.03 Differential Equations, Spring 2006](https://www.youtube.com/watch?v=MCrDzhpu3-s) — MIT OpenCourseWare, tiếng Anh. Bài giảng mở đầu của giáo sư Mattuck về hệ cấp một trong khóa MIT 18.03.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: phần mở đầu rõ ràng về chuyển đổi từ ODE bậc cao sang hệ trạng thái.
- Arnold, *Ordinary Differential Equations*: trình bày giàu trực giác hình học về hệ và không gian trạng thái.
