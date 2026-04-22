---
layout: post
title: "01-04 Phương trình Toàn phần"
chapter: '01'
order: 4
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---
## Mục tiêu
Bài học này giúp sinh viên hiểu phương trình toàn phần như bài toán truy tìm một hàm thế ẩn sau biểu thức vi phân, nhận diện điều kiện exact, và giải được các ODE dạng
$$ M(t,y)dt+N(t,y)dy=0. $$
Sinh viên cũng cần thấy mối liên hệ giữa exactness, vi phân toàn phần và ý tưởng bảo toàn trong mô hình.

## Kiến thức nền
Sinh viên nên nắm đạo hàm riêng, quy tắc vi phân của hàm nhiều biến và ý nghĩa của gradient. Bài học này là điểm nối đẹp giữa giải tích nhiều biến và ODE, nên việc nhớ rằng
$$ dF=F_tdt+F_y dy $$
sẽ giúp mọi thứ trở nên tự nhiên hơn nhiều.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-04 Phương trình Toàn phần]({{ site.imgurl }}/chapter_img/chapter01/01_04_exact_equations.svg)

Trong cơ học, ta thường gặp những đại lượng được bảo toàn như năng lượng. Trong nhiệt động lực học, ta gặp các vi phân mà một số là vi phân toàn phần, một số thì không. Trong giải tích nhiều biến, việc biết một trường vector có phải là gradient của một hàm thế hay không là câu hỏi rất tự nhiên. Phương trình toàn phần đưa tất cả những ý tưởng ấy vào một bài toán ODE rất cụ thể.

Thay vì cố giải trực tiếp cho $$ y(t) $$, ta hỏi một câu khác: biểu thức
$$ M(t,y)dt+N(t,y)dy $$
có phải là vi phân của một hàm nào đó hay không. Nếu có, bài toán lập tức rút gọn thành
$$ F(t,y)=C. $$
Đây là một trong những ví dụ đẹp nhất cho thấy nhận diện cấu trúc quan trọng hơn thao tác thuần túy.

## Khái niệm theo ba cách
### Cách nhìn trực quan
Hãy hình dung ta đang đi trên một bề mặt địa hình. Nếu độ biến thiên nhỏ của độ cao có thể viết chính xác dưới dạng vi phân của một thế năng, thì bài toán chuyển động dọc theo đường mức sẽ trở thành bài toán giữ độ cao không đổi. Exact equation cũng hoạt động theo tinh thần ấy: quỹ đạo nghiệm nằm trên những đường mức của một hàm thế.

### Cách nhìn hình ảnh
Nếu tồn tại hàm $$ F(t,y) $$ sao cho
$$ F_t=M,\qquad F_y=N, $$
thì nghiệm của ODE là các đường mức
$$ F(t,y)=C. $$
Vì vậy, thay vì tưởng tượng nghiệm như những đồ thị riêng lẻ, ta có thể nhìn cả họ nghiệm như một họ đường đồng mức trên mặt phẳng $$ \left(t,y\right) $$. Góc nhìn này rất trực quan và giúp sinh viên hiểu tại sao nghiệm thường xuất hiện dưới dạng ẩn.

### Cách nhìn hình thức
Phương trình
$$ M(t,y)dt+N(t,y)dy=0 $$
được gọi là toàn phần nếu tồn tại hàm $$ F(t,y) $$ sao cho
$$ dF=F_tdt+F_y dy=Mdt+Ndy. $$
Khi đó,
$$ F_t=M,\qquad F_y=N, $$
và nghiệm được cho bởi
$$ F(t,y)=C. $$
Trên một miền đơn liên với các đạo hàm riêng liên tục, điều kiện cần và đủ quen thuộc là
$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial t}.
$$

## Ý tưởng toán học cốt lõi
Về bản chất, ta đang hỏi liệu trường vector $$ \left(M,N\right) $$ có là gradient của một hàm vô hướng hay không. Nếu có, tích phân đường từ một điểm chuẩn đến điểm bất kỳ sẽ không phụ thuộc đường đi, và ta có thể "tích phân ngược" để dựng lại hàm thế.

Trong lớp học đầu tiên, điều quan trọng không phải là chứng minh hình thức đầy đủ, mà là giúp sinh viên tin vào ý tưởng sau: nếu một hàm thế tồn tại, thì đạo hàm riêng hỗn hợp của nó phải trùng nhau, nên
$$ F_{ty}=F_{yt}. $$
Từ đó suy ra điều kiện
$$ M_y=N_t. $$
Đây là dấu hiệu nhận diện exactness quen thuộc nhất.

## Những ngộ nhận thường gặp
- "Cứ viết được dưới dạng $$ Mdt+Ndy=0 $$ là exact." Sai. Đó chỉ là dạng biểu diễn, không đảm bảo tồn tại hàm thế.
- "Chỉ cần kiểm tra $$ M_y=N_t $$ là xong trong mọi miền." Chưa đủ tuyệt đối; còn phụ thuộc điều kiện miền, thường là đơn liên.
- "Sau khi tích phân $$ M $$ theo $$ t $$ là hoàn tất." Sai. Phần "hằng số tích phân" lúc này có thể là một hàm của $$ y $$, và ta phải dùng $$ F_y=N $$ để xác định nó.
- "Nghiệm ẩn là chưa giải xong." Sai. Với exact equations, nghiệm ẩn qua đường mức thường là dạng tự nhiên nhất.

## Tiến trình học tập đề xuất
### Bước 1: Đưa về dạng vi phân
Viết phương trình dưới dạng
$$ M(t,y)dt+N(t,y)dy=0. $$

### Bước 2: Kiểm tra điều kiện exact
Tính
$$ M_y\quad \text{và}\quad N_t. $$

### Bước 3: Dựng hàm thế $$ F $$
Tích phân $$ M $$ theo $$ t $$ hoặc $$ N $$ theo $$ y $$, rồi bổ sung "hàm hằng số" phụ thuộc biến còn lại.

### Bước 4: Khớp đạo hàm còn lại
Dùng điều kiện còn lại để xác định hàm phụ.

### Bước 5: Viết nghiệm dưới dạng đường mức
Kết luận bằng
$$ F(t,y)=C. $$

### Các checkpoint
- Sinh viên có biết vì sao hằng số tích phân bây giờ có thể là một hàm hay không.
- Sinh viên có phân biệt được "dạng vi phân" với "exact" hay không.
- Sinh viên có chấp nhận nghiệm ẩn là kết quả chuẩn của bài toán hay không.

## Ví dụ được giải chi tiết
### Ví dụ 1: Một phương trình exact cơ bản
Xét
$$ \left(2ty+y^2\right)dt+\left(t^2+2ty\right)dy=0. $$
Ta có
$$ M(t,y)=2ty+y^2,\qquad N(t,y)=t^2+2ty. $$
Tính đạo hàm riêng:
$$ M_y=2t+2y,\qquad N_t=2t+2y. $$
Hai vế bằng nhau, nên phương trình exact. Ta tìm $$ F $$ bằng cách tích phân $$ M $$ theo $$ t $$:
$$
F(t,y)=\int \left(2ty+y^2\right)dt=t^2y+ty^2+\phi(y).
$$
Lấy đạo hàm theo $$ y $$:
$$ F_y=t^2+2ty+\phi'(y). $$
So với $$ N=t^2+2ty $$, ta được
$$ \phi'(y)=0. $$
Vậy
$$ F(t,y)=t^2y+ty^2, $$
và nghiệm là
$$ t^2y+ty^2=C. $$

### Ví dụ 2: Có điều kiện đầu
Giải
$$
\left(3t^2+2y\right)dt+\left(2t+4y^3\right)dy=0,\qquad y(0)=1.
$$
Ta có
$$ M_y=2,\qquad N_t=2, $$
nên phương trình exact. Tích phân $$ M $$ theo $$ t $$:
$$ F(t,y)=t^3+2ty+\phi(y). $$
Lấy đạo hàm theo $$ y $$:
$$ F_y=2t+\phi'(y). $$
So sánh với $$ N=2t+4y^3 $$, ta có
$$ \phi'(y)=4y^3, $$
suy ra
$$ \phi(y)=y^4. $$
Vậy
$$ F(t,y)=t^3+2ty+y^4. $$
Nghiệm tổng quát:
$$ t^3+2ty+y^4=C. $$
Thay điều kiện đầu $$ t=0,\ y=1 $$:
$$ C=1. $$
Do đó nghiệm riêng là
$$ t^3+2ty+y^4=1. $$

### Ví dụ 3: Một phương trình đơn giản nhưng exact
Xét
$$ \left(y+t\right)dt+t\,dy=0. $$
Ta có
$$ M_y=1,\qquad N_t=1, $$
nên phương trình này thực ra exact. Đây là một ví dụ hay vì nhìn bề ngoài rất đơn giản nên sinh viên thường đoán bừa. Tích phân $$ M $$ theo $$ t $$:
$$ F=ty+\frac{t^2}{2}+\phi(y). $$
Suy ra
$$ F_y=t+\phi'(y). $$
Vì $$ N=t $$ nên
$$ \phi'(y)=0. $$
Do đó nghiệm là
$$ ty+\frac{t^2}{2}=C. $$
Ví dụ này nhắc rằng trực giác ban đầu đôi khi sai; exactness cần được kiểm tra bằng đạo hàm riêng.

### Ví dụ 4: Không exact và cần dừng lại đúng chỗ
Xét
$$ \left(ty+y\right)dt+t\,dy=0. $$
Ta có
$$ M_y=t+1,\qquad N_t=1. $$
Hai vế không bằng nhau, nên phương trình không exact trên dạng hiện tại. Điểm sư phạm ở đây là ta không nên cố nhồi quy trình exact cho một bài không thuộc loại này. Nhận ra "không exact" cũng là một kết quả quan trọng.

## Câu hỏi khái niệm
1. Vì sao nghiệm của phương trình toàn phần thường xuất hiện dưới dạng đường mức của một hàm thế?
2. Vì sao sau khi tích phân $$ M $$ theo $$ t $$, "hằng số" có thể là một hàm của $$ y $$?
3. Trong ngôn ngữ mô hình hóa, hàm thế giúp ta hiểu điều gì về cơ chế bảo toàn của hệ?

## Bài toán ứng dụng
1. Trong cơ học, nếu tổng năng lượng của một hệ được bảo toàn, tại sao ta thường mong đợi các quỹ đạo nghiệm nằm trên các đường mức của một hàm?
2. Một mô hình nhiệt động học cho biểu thức vi phân trạng thái. Hãy giải thích vì sao việc nhận ra vi phân toàn phần có ý nghĩa lớn hơn chuyện giải ODE thuần túy.
3. Trong một bài toán điều khiển, nếu một trường lực không phải gradient của thế năng, điều đó gợi ý điều gì về phụ thuộc đường đi của công do lực sinh ra?

## Chiến lược giảng dạy tương tác
- Cho sinh viên đoán trước phương trình nào là exact chỉ từ cảm giác, rồi kiểm tra bằng đạo hàm riêng để tạo "khoảnh khắc sửa trực giác".
- Vẽ vài đường mức của một hàm đơn giản như $$ F(t,y)=t^2+y^2 $$ để sinh viên quen với ý tưởng nghiệm là đường mức.
- Cho từng nhóm dựng hàm thế theo hai cách: tích phân $$ M $$ theo $$ t $$ hoặc tích phân $$ N $$ theo $$ y $$, rồi so sánh.
- Hỏi liên tục: "Hằng số ở đây có thật là hằng số không, hay là hàm của biến còn lại?"

## Phân hóa học tập
### Hỗ trợ sinh viên còn gặp khó khăn
Nên dùng bảng quy trình cố định: viết $$ M,N $$, tính $$ M_y,N_t $$, tích phân một trong hai, thêm hàm phụ, khớp lại bằng đạo hàm còn lại. Những bước lặp đi lặp lại này giúp sinh viên bớt sợ bài toán nhiều biến.

### Thử thách cho sinh viên khá giỏi
Có thể giao cho sinh viên khá giỏi tìm điều kiện miền mà tại đó
$$ M_y=N_t $$
thực sự đủ để suy ra exactness, hoặc yêu cầu liên hệ với khái niệm trường bảo toàn trong giải tích vector.

## Tóm tắt dễ nhớ
Phương trình toàn phần là bài toán truy tìm một hàm thế ẩn. Nếu
$$ Mdt+Ndy=dF, $$
thì nghiệm chỉ là
$$ F=C. $$
Hãy nhớ ba việc: kiểm tra $$ M_y=N_t $$, dựng hàm thế cẩn thận với hàm phụ, và chấp nhận rằng nghiệm ẩn thường là hình thức tự nhiên nhất.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Đường đẳng thế trong cơ học bảo toàn
- Bài toán: Trong một hệ không ma sát, quỹ đạo đôi khi bị ràng buộc bởi điều kiện năng lượng toàn phần không đổi.
- Mô hình: Nếu $$ F(t,y) $$ đóng vai trò như một đại lượng bảo toàn, thì
$$ dF=F_t\,dt+F_y\,dy=0 $$
là một phương trình toàn phần.
- Giả thiết và giới hạn: Ta đang giả sử hệ thực sự bảo toàn và không có ngoại lực không thế. Ma sát hoặc kích thích cưỡng bức sẽ phá exactness này.
- Diễn giải: Nghiệm
$$ F(t,y)=C $$
cho thấy quỹ đạo nằm trên các đường mức, nghĩa là hình học của nghiệm gắn trực tiếp với hình học của thế năng hay năng lượng.

#### Vi phân trạng thái trong nhiệt động lực học
- Bài toán: Kỹ sư cần phân biệt giữa đại lượng phụ thuộc trạng thái và đại lượng phụ thuộc đường đi.
- Mô hình: Một biểu thức như
$$ M(T,V)\,dT+N(T,V)\,dV $$
nếu exact sẽ là vi phân của một hàm trạng thái.
- Giả thiết và giới hạn: Điều kiện exact phụ thuộc vào biến trạng thái đã chọn và miền làm việc. Ở hệ không cân bằng, mô hình này không còn đủ.
- Diễn giải: Exactness không chỉ là mẹo giải ODE; nó cho biết khi nào một đại lượng tích lũy có thể quy về một hàm thế duy nhất.

#### Đường đồng mức chi phí trong kinh tế
- Bài toán: Doanh nghiệp muốn khảo sát các tổ hợp hai đầu vào cho cùng tổng chi phí.
- Mô hình: Nếu $$ C(x,y) $$ là hàm chi phí, thì điều kiện chi phí không đổi là
$$ dC=C_x\,dx+C_y\,dy=0. $$
- Giả thiết và giới hạn: Mô hình giả sử chi phí trơn và chỉ phụ thuộc hai biến đầu vào. Nó không nắm bắt ràng buộc rời rạc hay cú sốc giá.
- Diễn giải: Các nghiệm exact vì thế cũng có thể được hiểu như các đường đồng mức của một hàm kinh tế.

### 2. Trực giác bổ sung và các kết nối

Phương trình toàn phần là chiếc cầu đẹp giữa ODE và giải tích nhiều biến. Ở chương đầu, exactness xuất hiện như một phương pháp giải; ở các chương sau, cùng ý tưởng ấy sẽ quay lại dưới dạng gradient, thế năng, vi phân toàn phần, và sau nữa là vi phân ngoài của giải tích hiện đại. Một ngộ nhận phổ biến là nghĩ điều kiện $$ M_y=N_t $$ chỉ là "test cơ học". Thực ra, điều kiện ấy là bóng mờ của đẳng thức đạo hàm hỗn hợp và tính độc lập đường đi của tích phân đường.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
T, Y = np.meshgrid(t, y)
F = T**2 * Y + T * Y**2

plt.figure(figsize=(6, 5))
contours = plt.contour(T, Y, F, levels=12, cmap="viridis")
plt.clabel(contours, inline=True, fontsize=8)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Các đường mức của F(t, y) = t^2 y + t y^2")
plt.grid(alpha=0.2)
plt.show()
```

Nếu ta xuất phát từ exact equation tương ứng với $$ dF=0 $$, thì chính các đường mức này là họ nghiệm. Đây là một trực giác hình học rất mạnh, đặc biệt với sinh viên thích hình ảnh hơn là tính toán ký hiệu.

### 4. Gợi ý tìm thêm mô phỏng

- search: exact differential equations contour plot
- search: conservative vector field potential function
- search: thermodynamics exact differential state function

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình
$$ \left(2ty+y^2\right)dt+\left(t^2+2ty\right)dy=0. $$
Ta nhận ra
$$ M_y=N_t=2t+2y, $$
nên phương trình exact. Hàm thế là
$$ F(t,y)=t^2y+ty^2. $$
Vì thế nghiệm là
$$ t^2y+ty^2=C. $$
Ở mức ứng dụng, điều quan trọng không chỉ là tìm ra $$ C $$ mà còn là hiểu rằng mọi quỹ đạo hợp lệ đều nằm trên một bề mặt mức của một đại lượng bảo toàn ẩn.

### 6. Phân tầng độ khó

**Bậc đại học.** Luyện thành thạo quy trình kiểm tra exactness, dựng hàm thế, và chấp nhận nghiệm ẩn như dạng chuẩn.

**Bậc sau đại học.** Kết nối với vi phân 1-dạng, miền đơn liên, tích phân đường, và integrating factor cho phương trình không exact. Đây là tiền đề tốt cho cách nhìn hình học của cơ học và PDE.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: có phần exact equations rất phù hợp cho buổi học đầu tiên.
- Zill — *Differential Equations with Boundary-Value Problems*: hữu ích để luyện thao tác dựng hàm thế và xử lý điều kiện đầu.
- Ross — *Differential Equations*: trình bày ngắn gọn, đặc biệt tốt cho việc so sánh bài exact và không exact.
