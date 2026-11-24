---
layout: post
title: "01-02 Phương trình Tách biến"
chapter: '01'
order: 2
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Giữa rừng phương trình vi phân cấp một, **phương trình tách biến** là lớp bài toán đầu tiên—và cũng thanh lịch nhất—mà ta có thể giải triệt để bằng phép tích phân trực tiếp. Ý tưởng đơn giản đến bất ngờ: dồn toàn bộ biến phụ thuộc $y$ sang vế trái, biến độc lập $x$ sang vế phải, rồi tích phân hai vế—nhưng ẩn sau sự đơn giản ấy lại có những cạm bẫy tinh tế như **nghiệm kỳ dị bị mất khi chia** và **nghiệm ẩn không giải tường minh được**!

## Bản đồ kiến thức nền: Bốn trụ cột của Phương trình Tách biến

1. **Cấu trúc nhân tử hóa $\frac{dy}{dx} = g(x)\,h(y)$**:
   Nhận diện nhanh khi vế phải tách được thành tích của một hàm chỉ phụ thuộc $x$ và một hàm chỉ phụ thuộc $y$.
2. **Bảo toàn nghiệm cân bằng ($h(y_0) = 0$)**:
   Trước khi chia hai vế cho $h(y)$, **luôn kiểm tra** các giá trị $y = y_0$ làm $h(y_0) = 0$; chúng là các nghiệm hằng thực thụ dễ bị đánh rơi!
3. **Nghiệm ẩn vs. Nghiệm tường minh & Miền xác định**:
   Tích phân $\int \frac{dy}{h(y)} = \int g(x)\,dx + C$ thường cho hệ thức ẩn $H(y) = G(x) + C$; khi giải ra $y(x)$ phải chọn đúng nhánh đi qua $(x_0, y_0)$ và xác định rõ khoảng tồn tại cực đại.
4. **Bản chất chặt chẽ đằng sau ký hiệu vi phân**:
   Phép tách $dy, dx$ không phải "mẹo hủy ký hiệu" tùy tiện mà là hệ quả chặt chẽ của **quy tắc dây chuyền** $\frac{d}{dx}H(y(x)) = H'(y)y' = g(x)$.

## Mục tiêu
Bài học này giúp sinh viên nhận diện phương trình vi phân tách biến, hiểu cơ sở toán học của việc gom các biểu thức theo từng biến và giải được bài toán tách biến kèm điều kiện đầu. Sinh viên cũng cần rèn thói quen kiểm tra nghiệm cân bằng, miền xác định và vai trò của hằng số tích phân—những chi tiết dễ bị bỏ sót khi giải bài tập.

## Kiến thức nền
Sinh viên cần thành thạo đạo hàm, nguyên hàm cơ bản, biến đổi đại số và quy tắc tính với logarit. Hiểu $$ \frac{dy}{dt} $$ như đạo hàm liên hệ giữa hai đại lượng biến thiên đồng thời giúp quá trình tách biến có cơ sở rõ ràng thay vì chỉ là thao tác cơ học.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-02 Phương trình Tách biến]({{ site.imgurl }}/chapter_img/chapter01/01_02_separable_equations.svg)

Nhiều mô hình cơ bản trong khoa học có tốc độ biến thiên bằng tích của một yếu tố chỉ phụ thuộc thời gian và một yếu tố chỉ phụ thuộc trạng thái hiện tại. Chẳng hạn, tốc độ tăng trưởng của một quần thể có thể phụ thuộc đồng thời vào yếu tố mùa vụ theo $$ t $$ và quy mô hiện tại $$ P $$. Khi hai ảnh hưởng này tách được thành tích, ta có thể đưa toàn bộ phần liên quan đến biến trạng thái về một vế và phần liên quan đến thời gian về vế còn lại.

Ưu điểm của phương pháp tách biến nằm ở chỗ nó khai thác trực tiếp cấu trúc nhân tử của mô hình để tích lũy riêng phần ảnh hưởng của từng biến qua phép tích phân. Khi thực hiện cẩn thận, phương pháp này không chỉ cho công thức nghiệm mà còn giúp phát hiện các nghiệm cân bằng và giới hạn miền tồn tại của nghiệm.

### Khung giải thích (nên đọc chậm): Giải trọn vẹn IVP $\frac{dy}{dx} = -2xy^2,\; y(0) = \frac{1}{2}$ và phát hiện khoảng bùng nổ

1. **Kiểm tra nghiệm cân bằng**: $h(y) = y^2 = 0 \implies y \equiv 0$ là nghiệm hằng (nhưng không thỏa $y(0) = 1/2$).
2. **Tách biến và tích phân** (với $y \ne 0$):
   $$\frac{dy}{y^2} = -2x\,dx \implies \int y^{-2}\,dy = \int -2x\,dx \implies -\frac{1}{y} = -x^2 + C \implies \frac{1}{y} = x^2 - C.$$
3. **Ghim hằng số từ $y(0) = \frac{1}{2}$**:
   $$\frac{1}{1/2} = 0^2 - C \implies -C = 2 \implies y(x) = \mathbf{\frac{1}{x^2 + 2}}.$$
4. **Kiểm tra khoảng tồn tại**: Vì $x^2 + 2 \ge 2 > 0$ với mọi $x \in \mathbb{R}$, nghiệm tồn tại trên toàn $(-\infty, +\infty)$. Ngược lại, nếu đổi điều kiện đầu thành $y(0) = -\frac{1}{2}$, ta được $y(x) = \frac{1}{x^2 - 2}$, bị **bùng nổ tại $x = \pm\sqrt{2}$** nên khoảng tồn tại cực đại chỉ còn $(-\sqrt{2}, \sqrt{2})$!

## Khái niệm theo ba cách

### Cách nhìn trực quan
Có thể hình dung tốc độ biến thiên của hệ được điều chỉnh bởi hai yếu tố độc lập: một yếu tố chỉ thay đổi theo thời gian và một yếu tố chỉ phụ thuộc vào trạng thái hiện tại. Nhờ tính tách rời theo dạng tích đó, ta có thể tích phân riêng từng yếu tố rồi ghép chúng lại thành quan hệ giữa $$ y $$ và $$ t $$.

### Cách nhìn hình ảnh
Trên trường hướng (slope field) của phương trình

$$
\frac{dy}{dt}=g(t)h(y),
$$

hệ số góc tại mỗi điểm là tích của hai nhân tử. Nếu $$ h(y_*)=0 $$ tại một mức $$ y_* $$, thì dọc theo toàn bộ đường thẳng nằm ngang $$ y=y_* $$ hệ số góc đều bằng $$ 0 $$, tạo thành một nghiệm cân bằng. Nếu $$ g(t) $$ đổi dấu theo $$ t $$, xu hướng tăng/giảm của trường hướng sẽ đảo chiều trên các dải thẳng đứng tương ứng. Như vậy, tính tách biến phản ánh trực tiếp cấu trúc hình học của trường hướng.

### Cách nhìn hình thức
Một ODE cấp một được gọi là tách biến nếu có thể viết dưới dạng

$$
\frac{dy}{dt}=g(t)h(y).
$$

Trên miền mà $$ h(y)\neq 0 $$, ta viết lại dưới dạng vi phân

$$
\frac{1}{h(y)}dy=g(t)dt
$$

và lấy tích phân hai vế:

$$
\int \frac{1}{h(y)}dy=\int g(t)dt+C.
$$

Các giá trị $$ y_* $$ thỏa mãn $$ h(y_*)=0 $$ cần được kiểm tra riêng vì phép chia cho $$ h(y) $$ có thể làm mất các nghiệm cân bằng $$ y(t)\equiv y_* $$.

## Những điều cần nhấn mạnh về mặt lý thuyết
Phương pháp tách biến dựa trên hai điểm chính: cấu trúc nhân tử cho phép gom biến cùng loại về một vế (có cơ sở từ quy tắc dây chuyền), và kết quả sau khi lấy tích phân thường là một hệ thức ẩn giữa $$ y $$ và $$ t $$ mà không nhất thiết lúc nào cũng giải tường minh được $$ y(t) $$.

Trong thực hành, cần luôn kiểm tra ba câu hỏi: phương trình có thực sự tách biến được không? Có nghiệm cân bằng nào bị mất khi chia không? Và nghiệm thu được xác định trên khoảng nào chứa điều kiện đầu?

## Những ngộ nhận thường gặp
- "Cứ thấy cả $$ y $$ và $$ t $$ là có thể chuyển hết về hai vế." Sai. Chỉ thực hiện được khi vế phải phân tích thành tích $$ g(t)h(y) $$.
- "Chia cho $$ h(y) $$ rồi tích phân là đủ." Chưa đủ. Cần kiểm tra riêng các nghiệm $$ h(y)=0 $$ để tránh bỏ sót nghiệm cân bằng.
- "Giải xong bắt buộc phải cô lập được $$ y(t) $$." Sai. Trong nhiều bài toán, nghiệm ở dạng ẩn là hoàn toàn hợp lệ và đầy đủ.
- "Điều kiện đầu chỉ dùng ở bước cuối để tìm hằng số $$ C $$." Chưa đủ. Điều kiện đầu còn quyết định đúng nhánh nghiệm (khi bỏ dấu giá trị tuyệt đối hoặc khai căn) và xác định khoảng tồn tại của nghiệm.

## Tiến trình học tập đề xuất

### Bước 1: Nhận diện dạng nhân tử
Kiểm tra xem vế phải có phân tích được thành dạng $$ g(t)h(y) $$ hay không.

### Bước 2: Xét nghiệm cân bằng và tách biến có điều kiện
Tìm các giá trị $$ y_* $$ sao cho $$ h(y_*)=0 $$ trước, sau đó đặt điều kiện $$ h(y)\neq 0 $$ rồi mới chia và lấy tích phân.

### Bước 3: Tích phân hai vế
Tính nguyên hàm ở mỗi vế và giữ một hằng số tích phân tùy ý $$ C $$.

### Bước 4: Áp dụng điều kiện đầu và kiểm tra miền
Thay điều kiện đầu để xác định hằng số, chọn nhánh phù hợp và chỉ rõ khoảng tồn tại của nghiệm.

### Các checkpoint
- Bạn có phát hiện được các nghiệm cân bằng có thể bị mất sau phép chia không?
- Bạn có biết cách viết và sử dụng nghiệm dạng ẩn khi không cô lập được $$ y $$ không?
- Bạn có thói quen thử lại nghiệm bằng cách lấy đạo hàm và thay vào phương trình ban đầu không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tăng trưởng theo hàm mũ
Giải bài toán

$$
\frac{dy}{dt}=3y,\qquad y(0)=2.
$$

Với $$ y\neq 0 $$, tách biến ta được $$ \frac{1}{y}dy=3dt $$. Lấy tích phân hai vế cho $$ \ln \lvert y\rvert=3t+C_1 $$, suy ra $$ y=Ce^{3t} $$ (với $$ C=\pm e^{C_1} $$, và kết hợp cả nghiệm cân bằng $$ y=0 $$ ứng với $$ C=0 $$). Thay điều kiện đầu $$ y(0)=2 $$ ta được $$ C=2 $$, nên nghiệm của bài toán là

$$
y(t)=2e^{3t}.
$$

### Ví dụ 2: Phương trình logistic có nghiệm cân bằng
Giải phương trình

$$
\frac{dy}{dt}=y(1-y).
$$

Trước hết, ta thấy hai nghiệm cân bằng là $$ y=0 $$ và $$ y=1 $$. Với $$ y\neq 0 $$ và $$ y\neq 1 $$, tách biến ta có $$ \frac{1}{y(1-y)}dy=dt $$. Phân tích thành phân thức đơn giản:

$$
\frac{1}{y(1-y)}=\frac{1}{y}+\frac{1}{1-y}.
$$

Lấy tích phân hai vế thu được $$ \ln \lvert y\rvert-\ln \lvert 1-y\rvert=t+C_1 $$, suy ra $$ \frac{y}{1-y}=Ce^t $$ (với $$ C=\pm e^{C_1} $$), và giải ra

$$
y(t)=\frac{Ce^t}{1+Ce^t}.
$$

Lưu ý rằng nghiệm cân bằng $$ y=0 $$ ứng với $$ C=0 $$, còn nghiệm cân bằng $$ y=1 $$ không thu được từ bất kỳ giá trị hữu hạn nào của $$ C $$, nên bắt buộc phải ghi nhận riêng trước khi chia.

### Ví dụ 3: Nghiệm bùng nổ trong thời gian hữu hạn
Giải bài toán

$$
\frac{dy}{dt}=y^2,\qquad y(0)=1.
$$

Với $$ y\neq 0 $$, tách biến thành $$ \frac{1}{y^2}dy=dt $$ và lấy tích phân hai vế ta được $$ -\frac{1}{y}=t+C $$. Thay điều kiện đầu $$ y(0)=1 $$ cho $$ C=-1 $$, nên $$ -\frac{1}{y}=t-1 $$, hay

$$
y(t)=\frac{1}{1-t}.
$$

Nghiệm này chỉ xác định trên khoảng $$ (-\infty,1) $$ chứa $$ t=0 $$ và bùng nổ (blow-up) khi $$ t\to 1^- $$. Ví dụ này cho thấy việc xác định khoảng tồn tại quan trọng không kém công thức nghiệm.

### Ví dụ 4: Nghiệm ở dạng ẩn
Giải bài toán

$$
\frac{dy}{dt}=\frac{t}{1+y^2},\qquad y(0)=0.
$$

Tách biến ta được $$ \left(1+y^2\right)dy=t\,dt $$. Lấy tích phân hai vế cho

$$
y+\frac{y^3}{3}=\frac{t^2}{2}+C.
$$

Thay điều kiện đầu $$ y(0)=0 $$ suy ra $$ C=0 $$, vậy nghiệm ở dạng ẩn là

$$
y+\frac{y^3}{3}=\frac{t^2}{2}.
$$

Ta không cần giải công thức bậc ba để cô lập $$ y $$ mới coi là hoàn chỉnh; hệ thức ẩn này xác định duy nhất một hàm $$ y(t) $$ trên toàn $$ \mathbb{R} $$ (vì vế trái đồng biến chặt theo $$ y $$).

## Câu hỏi khái niệm
1. Vì sao phải kiểm tra các nghiệm cân bằng trước khi chia hai vế cho $$ h(y) $$?
2. Vì sao nghiệm dạng ẩn vẫn được xem là một lời giải đầy đủ của phương trình vi phân?
3. Trong ứng dụng thực tế, miền tồn tại của nghiệm cung cấp thông tin gì ngoài bản thân công thức nghiệm?

## Bài toán ứng dụng
1. Một phản ứng hóa học có tốc độ thay đổi nồng độ tỉ lệ với tích của nồng độ hiện tại và một hàm cho trước theo thời gian. Hãy giải thích vì sao mô hình này thuộc dạng tách biến.
2. Trong mô hình quần thể cá tăng trưởng logistic, hai nghiệm cân bằng có ý nghĩa sinh thái gì?
3. Nếu một mô hình dân số đơn giản cho nghiệm dạng $$ \frac{1}{1-t} $$, hiện tượng bùng nổ tại thời điểm hữu hạn $$ t=1 $$ cảnh báo điều gì về phạm vi áp dụng của mô hình?

## Chiến lược giảng dạy tương tác
- Đưa ra khoảng 10 phương trình để sinh viên phân loại nhanh "tách được" hay "không tách được" và giải thích ngắn gọn trong một câu.
- Khi giải ví dụ logistic, dừng lại ngay trước phép chia cho $$ y(1-y) $$ để cả lớp tự phát hiện nguy cơ làm mất nghiệm cân bằng.
- Yêu cầu các nhóm phác họa nghiệm cân bằng và một vài nghiệm không cân bằng trên cùng một hệ trục để thấy bức tranh định tính.
- Thảo luận ý nghĩa miền tồn tại trong ví dụ $$ y' = y^2 $$ thay vì chỉ dừng ở biểu thức đại số.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng quy trình 6 bước ngắn gọn: nhận diện dạng $$ g(t)h(y) $$, xét nghiệm cân bằng, tách biến, tích phân, thay điều kiện đầu và xác định miền tồn tại.

### Thử thách cho sinh viên khá giỏi
So sánh lời giải giải tích của phương trình logistic bằng phương pháp tách biến với phân tích định tính qua đường pha, đồng thời khảo sát các phương trình tách biến dẫn đến tích phân không sơ cấp.

## Tóm tắt dễ nhớ
Phương trình tách biến có vế phải dạng tích $$ g(t)h(y) $$, tách rời ảnh hưởng của thời gian và trạng thái. Khi giải, cần luôn nhớ ba bước kiểm soát: tìm nghiệm cân bằng $$ h(y)=0 $$ trước khi chia, chấp nhận nghiệm ẩn khi cần và xác định đúng khoảng tồn tại chứa điều kiện đầu.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Phân rã phóng xạ
- Bài toán: Một đồng vị phóng xạ dùng trong y khoa giảm dần hoạt tính theo thời gian; cần tính lượng chất còn lại sau một khoảng thời gian nhất định.
- Mô hình:

$$
\frac{dN}{dt}=-\lambda N.
$$

- Giả thiết và giới hạn: Giả sử mỗi hạt nhân phân rã độc lập với xác suất không đổi theo thời gian; mô hình chưa xét chuỗi phân rã nối tiếp hay ảnh hưởng ngoại cảnh.
- Diễn giải: Nghiệm $$ N(t)=N_0e^{-\lambda t} $$ giải thích trực tiếp khái niệm chu kỳ bán rã và cho thấy tỉ lệ giảm theo thời gian là hằng số trong khi lượng giảm tuyệt đối nhỏ dần.

#### Tăng trưởng logistic trong sinh thái
- Bài toán: Một quần thể cá trong hồ ban đầu tăng nhanh nhưng chậm dần khi mật độ tiến gần giới hạn tài nguyên của hồ.
- Mô hình:

$$
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
$$

- Giả thiết và giới hạn: Giả sử môi trường đồng nhất, sức chứa $$ K $$ không đổi và bỏ qua cấu trúc tuổi, mùa vụ hay khai thác.
- Diễn giải: Nghiệm logistic ban đầu xấp xỉ tăng trưởng mũ nhưng về dài hạn tiệm cận sức chứa $$ K $$, khắc phục hạn chế tăng vô hạn của mô hình mũ.

#### Chuyển động rơi với lực cản bậc hai
- Bài toán: Một người nhảy dù ban đầu tăng tốc nhanh rồi dần tiến tới vận tốc giới hạn không đổi.
- Mô hình:

$$
\frac{dv}{dt}=g-kv^2.
$$

- Giả thiết và giới hạn: Giả sử rơi thẳng đứng, khối lượng không đổi và lực cản tỉ lệ với bình phương vận tốc; mô hình chưa xét giai đoạn mở dù hoặc thay đổi tư thế.
- Diễn giải: Nhờ tính tách biến, ta thấy trực tiếp vận tốc không tăng vô hạn mà bị chặn bởi vận tốc giới hạn $$ \sqrt{g/k} $$.

### 2. Trực giác bổ sung và các kết nối

Bản chất của tách biến không phải là thao tác "chuyển vi phân" tùy tiện mà là khai thác cấu trúc nhân tử $$ y'=g(t)h(y) $$ để áp dụng phép đổi biến tích phân. Bài học này liên kết trực tiếp với phương trình tự trị (trường hợp riêng $$ g(t)=1 $$, nơi toàn bộ động lực được quyết định bởi dấu của $$ h(y) $$) và với lý thuyết tồn tại–duy nhất nghiệm (qua hiện tượng bùng nổ hữu hạn thời gian và các nghiệm cân bằng bị bỏ sót nếu chia thiếu điều kiện).

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.8, 100
t = np.linspace(0, 12, 400)
P0_values = [5, 20, 60, 140]

for P0 in P0_values:
    C = (K - P0) / P0
    P = K / (1 + C * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="K")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Nghiệm logistic với nhiều điều kiện đầu")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị minh họa rõ hai tính chất: điều kiện đầu quyết định quỹ đạo ngắn hạn còn sức chứa $$ K $$ quyết định giới hạn dài hạn; mọi nghiệm xuất phát trên $$ K $$ đều giảm về $$ K $$, còn nghiệm xuất phát trong khoảng $$ (0,K) $$ đều tăng lên $$ K $$.

### 4. Gợi ý tìm thêm mô phỏng

- search: logistic equation phase line
- search: radioactive decay simulation differential equation
- search: skydiver quadratic drag solution

### 5. Bài toán mẫu có bối cảnh thực

Một hồ nuôi cá có sức chứa 5000 con, tốc độ tăng trưởng nội tại $$ 0.6 $$ mỗi năm và ban đầu có 800 con. Mô hình logistic tương ứng là

$$
\frac{dP}{dt}=0.6P\left(1-\frac{P}{5000}\right),\qquad P(0)=800.
$$

Giải bằng tách biến ta thu được

$$
P(t)=\frac{5000}{1+5.25e^{-0.6t}}.
$$

Nghiệm cho thấy đàn cá tăng nhanh ở giai đoạn đầu rồi tăng chậm dần khi tiến gần sức chứa. Phương pháp Euler với bước một quý có thể mô phỏng gần đúng xu hướng này, nhưng nghiệm giải tích cho phép xác định chính xác thời điểm đạt các ngưỡng quy mô mong muốn.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo nhận diện dạng $$ g(t)h(y) $$, xét nghiệm cân bằng trước khi chia và sử dụng thành thạo cả nghiệm tường minh lẫn nghiệm ẩn.

**Bậc sau đại học.** Khảo sát sâu hơn về thời gian bùng nổ hữu hạn, tính bất biến miền và tính đơn điệu của nghiệm, đồng thời đối chiếu với kỹ thuật tách biến trong PDE (tách nghiệm thành tích các hàm một biến).

## Video tham khảo

- Xem trước: [17. Phương trình vi phân tách biến | Phương trình vi phân | Khan Academy](https://www.youtube.com/watch?v=_A1F5ygjdKk) — Khan Academy Vietnam, tiếng Việt. Hướng dẫn giải phương trình vi phân cấp một tách biến bằng tiếng Việt.
- [Separation of Variables //  Differential Equations](https://www.youtube.com/watch?v=7Y-frhf-1Zk) — Dr. Trefor Bazett, tiếng Anh. Giải thích bước tách $$ dy/g(y)=f(x)\,dx $$ và điều kiện áp dụng phương pháp.
- [Newton's Law of Cooling  // Separable ODE Example](https://www.youtube.com/watch?v=_bAjWNsNrQA) — Dr. Trefor Bazett, tiếng Anh. Giải chi tiết định luật làm nguội Newton như một ví dụ phương trình tách biến.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ phương pháp tách biến và mô hình logistic.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện nhận diện dạng phương trình và xác định hằng số tích phân.
- Ross — *Differential Equations*: cung cấp nhiều ví dụ ngắn, đa dạng về miền xác định của nghiệm.
