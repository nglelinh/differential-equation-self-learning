---
layout: post
title: "01-05 Phương pháp Thế"
chapter: '01'
order: 5
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Nhiều phương trình vi phân thoạt nhìn trông vừa không tách biến, vừa không tuyến tính, lại chẳng toàn phần—nhưng chỉ cần một phép đổi góc nhìn thông minh (phép thế biến), toàn bộ cấu trúc rắc rối lập tức sụp đổ thành bài toán quen thuộc! Trong toán học, **phép thế (substitution)** chính là nghệ thuật khai thác **đối xứng ẩn** của phương trình—như đối xứng co giãn ở phương trình đẳng cấp hay đối xứng lũy thừa ở phương trình Bernoulli.

## Kiến thức cần nhớ: Bốn họ Phép thế kinh điển cho PTVP Cấp Một

1. **Phương trình đẳng cấp $y' = F(y/x)$ (Đối xứng co giãn)**:
   Đặt $v = y/x \implies y = vx,\; y' = v + xv'$; phương trình lập tức tách biến được giữa $v$ và $x$.
2. **Phương trình Bernoulli $y' + P(x)y = Q(x)y^n$ ($n \ne 0, 1$)**:
   Đặt $u = y^{1-n}$ biến phương trình phi tuyến bậc $n$ thành phương trình **tuyến tính cấp một** cho $u(x)$.
3. **Phép thế tổ hợp tuyến tính $y' = G(ax + by + c)$**:
   Đặt $u = ax + by + c \implies u' = a + b\,G(u)$, đưa ngay về phương trình tách biến thuần túy.
4. **Phương trình Riccati $y' = P(x) + Q(x)y + R(x)y^2$**:
   Khi biết trước một nghiệm riêng $y_1(x)$, phép thế $y = y_1 + \frac{1}{u}$ biến phương trình phi tuyến bậc hai thành tuyến tính cấp một!

## Mục tiêu
Bài học này giúp sinh viên nhận ra rằng nhiều phương trình vi phân phi tuyến có vẻ phức tạp thực chất ẩn chứa một biến phụ tự nhiên. Khi chọn đúng phép thế, phương trình được đưa về các dạng quen thuộc như tách biến, tuyến tính hoặc toàn phần. Trọng tâm bài học là nhận diện và giải thành thạo các dạng tiêu biểu gồm phương trình Bernoulli và phương trình thuần nhất cấp một.

## Kiến thức nền
Sinh viên cần nắm chắc phương trình tách biến, phương trình tuyến tính cấp một và quy tắc dây chuyền. Khó khăn chính của bài học không nằm ở bước lấy tích phân mà ở việc phát hiện biến phụ giúp bộc lộ cấu trúc ẩn của phương trình.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-05 Phương pháp Thế]({{ site.imgurl }}/chapter_img/chapter01/01_05_substitution_methods.svg)

Trong toán học ứng dụng, hình thức ban đầu của một phương trình đôi khi che khuất cấu trúc đơn giản bên trong. Tương tự việc chọn hệ tọa độ thích hợp trong vật lý giúp rút gọn đáng kể phép tính, việc đổi biến trong ODE giúp chuyển một bài toán phi tuyến khó thành một dạng chuẩn đã biết cách giải.

Vì vậy, phương pháp thế rèn luyện tư duy nhận diện cấu trúc: thay vì vội biến đổi rời rạc, ta đặt câu hỏi phương trình đang lặp lại tổ hợp, tỉ số hay lũy thừa nào để chọn phép đổi biến hợp lý.

### Giải thích: Giải phương trình đẳng cấp $\frac{dy}{dx} = \frac{x + y}{x}$ ($x > 0$) qua phép thế $v = y/x$

1. **Nhận diện cấu trúc $y/x$**:
   $$\frac{dy}{dx} = 1 + \frac{y}{x}.$$
2. **Đặt $v = \frac{y}{x} \implies y = vx \implies \frac{dy}{dx} = v + x\frac{dv}{dx}$**:
   Thay vào phương trình:
   $$v + x\frac{dv}{dx} = 1 + v \implies x\frac{dv}{dx} = 1.$$
3. **Tách biến và tích phân**:
   $$dv = \frac{dx}{x} \implies v(x) = \ln x + C.$$
4. **Trả về biến gốc $y = vx$**:
   $$y(x) = \mathbf{x\ln x + C x}.$$
   Kiểm chứng lại trực tiếp: $y' = (\ln x + 1) + C = 1 + \frac{x\ln x + Cx}{x} = 1 + \frac{y}{x}$, khớp 100%!

## Khái niệm theo ba cách

### Cách nhìn trực quan
Phép thế giống như đổi hệ tọa độ quan sát: bản chất của bài toán không đổi, nhưng biến mới giúp cấu trúc quan hệ hiện lên rõ ràng hơn. Khi đặt $$ v=\frac{y}{t} $$ hoặc $$ v=y^{1-n} $$, ta đang chuyển sang đại lượng phản ánh trực tiếp quy luật nội tại của phương trình.

### Cách nhìn hình ảnh
Trong phương trình thuần nhất cấp một

$$
\frac{dy}{dt}=F\left(\frac{y}{t}\right),
$$

hệ số góc tại điểm $$ \left(t,y\right) $$ chỉ phụ thuộc vào tỉ số $$ \frac{y}{t} $$, nghĩa là không đổi dọc theo mỗi tia xuất phát từ gốc tọa độ. Điều này gợi ý trực tiếp phép thế $$ y=vt $$. Trong phương trình Bernoulli, tính phi tuyến chỉ xuất hiện qua lũy thừa $$ y^n $$, nên phép thế lũy thừa sẽ "tuyến tính hóa" phương trình.

### Cách nhìn hình thức
Hai lớp phương trình tiêu biểu dùng phương pháp thế là:

**Phương trình Bernoulli**:

$$
\frac{dy}{dt}+p(t)y=q(t)y^n,\qquad n\neq 0,1.
$$

Đặt $$ v=y^{1-n} $$, phương trình chuyển thành một phương trình tuyến tính cấp một theo ẩn hàm $$ v(t) $$.

**Phương trình thuần nhất cấp một (đẳng cấp)**:

$$
\frac{dy}{dt}=F\left(\frac{y}{t}\right).
$$

Đặt $$ y=vt $$, suy ra $$ \frac{dy}{dt}=v+t\frac{dv}{dt} $$, từ đó phương trình chuyển về dạng tách biến theo $$ v $$ và $$ t $$.

## Bản chất sư phạm của bài học
Thay vì ghi nhớ phương pháp thế như một danh sách mẹo rời rạc, cần tập trung vào các dấu hiệu cấu trúc: có tỉ số $$ y/t $$ xuất hiện lặp lại không? Có lũy thừa $$ y^n $$ nào phá vỡ tính tuyến tính không? Có tổ hợp như $$ t+y $$ xuất hiện thành khối không? Khi nhìn ra cấu trúc, phép thế phù hợp sẽ tự nhiên lộ diện.

## Những ngộ nhận thường gặp
- "Phương pháp thế chỉ là đoán mò." Sai. Các phép thế tiêu chuẩn đều xuất phát từ dấu hiệu cấu trúc rõ ràng của phương trình.
- "Mỗi bài chỉ có duy nhất một phép thế đúng." Sai. Nhiều bài toán có thể giải bằng hơn một phép đổi biến khác nhau, dù có lựa chọn gọn hơn.
- "Chỉ cần thay biến $$ y $$ bằng biến mới là xong." Sai. Phải biến đổi cả đạo hàm $$ \frac{dy}{dt} $$ theo đúng quy tắc dây chuyền.
- "Phương trình Bernoulli là phương trình tuyến tính." Sai. Phương trình Bernoulli phi tuyến (khi $$ n\neq 0,1 $$); nó chỉ trở thành tuyến tính sau khi đổi biến $$ v=y^{1-n} $$.

## Tiến trình học tập đề xuất

### Bước 1: Tìm dấu hiệu cấu trúc
Quan sát xem phương trình có dạng thuần nhất, dạng Bernoulli hay chứa một tổ hợp biểu thức lặp lại.

### Bước 2: Chọn biến phụ có cơ sở
Xác định biến mới giúp loại bỏ thành phần gây khó (tỉ số, lũy thừa hoặc tổ hợp lồng nhau).

### Bước 3: Biến đổi đạo hàm cẩn thận
Áp dụng chính xác quy tắc dây chuyền khi thay $$ \frac{dy}{dt} $$ theo biến mới—đây là bước dễ sai nhất.

### Bước 4: Giải phương trình mới
Sử dụng kỹ thuật tách biến hoặc nhân tử tích phân cho phương trình đã rút gọn.

### Bước 5: Trả về biến gốc
Thay ngược lại để biểu diễn nghiệm theo $$ y $$ và $$ t $$, đồng thời kiểm tra các nghiệm bị mất khi chia (như $$ y=0 $$ trong phương trình Bernoulli với $$ n>0 $$) và miền xác định.

### Các checkpoint
- Bạn có nhận diện nhanh được dạng thuần nhất $$ F(y/t) $$ và dạng Bernoulli không?
- Bạn có biến đổi chính xác đạo hàm $$ y'=v+tv' $$ và $$ v'=(1-n)y^{-n}y' $$ không?
- Bạn có nhớ quay lại biến gốc và kiểm tra các nghiệm đặc biệt sau khi giải không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phương trình thuần nhất cấp một
Giải phương trình

$$
\frac{dy}{dt}=1+\frac{y}{t},\qquad t\neq 0.
$$

Vì vế phải chỉ phụ thuộc vào tỉ số $$ \frac{y}{t} $$, đặt $$ y=vt $$, suy ra $$ \frac{dy}{dt}=v+t\frac{dv}{dt} $$. Thay vào phương trình ta được

$$
v+t\frac{dv}{dt}=1+v \implies t\frac{dv}{dt}=1 \implies \frac{dv}{dt}=\frac{1}{t}.
$$

Lấy tích phân hai vế cho $$ v=\ln \lvert t\rvert+C $$. Quay lại biến gốc, ta thu được

$$
y=t\ln \lvert t\rvert+Ct.
$$

### Ví dụ 2: Phương trình Bernoulli
Giải phương trình

$$
\frac{dy}{dt}+y=ty^2,\qquad y\neq 0.
$$

Đây là phương trình Bernoulli với $$ n=2 $$. Đặt $$ v=y^{1-2}=y^{-1}=\frac{1}{y} $$, ta có

$$
\frac{dv}{dt}=-\frac{1}{y^2}\frac{dy}{dt}.
$$

Từ phương trình ban đầu $$ \frac{dy}{dt}=ty^2-y $$, nhân hai vế với $$ -\frac{1}{y^2} $$ thu được

$$
\frac{dv}{dt}=-t+\frac{1}{y}=-t+v \iff \frac{dv}{dt}-v=-t.
$$

Đây là phương trình tuyến tính cấp một theo $$ v $$ với nhân tử tích phân $$ e^{-t} $$, nên

$$
\frac{d}{dt}\left(e^{-t}v\right)=-te^{-t}.
$$

Tích phân từng phần hai vế:

$$
e^{-t}v=\int -te^{-t}dt + C=\left(t+1\right)e^{-t}+C,
$$

suy ra $$ v=t+1+Ce^t $$. Trả về biến $$ y=\frac{1}{v} $$, ta nhận được

$$
y(t)=\frac{1}{t+1+Ce^t}
$$

(bên cạnh nghiệm hằng $$ y\equiv 0 $$ nếu không giới hạn $$ y\neq 0 $$).

### Ví dụ 3: Phương trình logistic qua phép nghịch đảo
Xét phương trình

$$
\frac{dP}{dt}=rP-\frac{r}{K}P^2,\qquad P>0.
$$

Bên cạnh cách tách biến, ta có thể xem đây là phương trình Bernoulli với $$ n=2 $$ và đặt $$ u=\frac{1}{P} $$. Khi đó $$ \frac{du}{dt}=-\frac{1}{P^2}\frac{dP}{dt} $$, nên

$$
\frac{du}{dt}=-\frac{1}{P^2}\left(rP-\frac{r}{K}P^2\right)=-\frac{r}{P}+\frac{r}{K}=-ru+\frac{r}{K},
$$

hay $$ \frac{du}{dt}+ru=\frac{r}{K} $$. Giải phương trình tuyến tính này cho $$ u(t)=\frac{1}{K}+Ce^{-rt} $$, từ đó

$$
P(t)=\frac{1}{u(t)}=\frac{1}{\frac{1}{K}+Ce^{-rt}}=\frac{K}{1+CKe^{-rt}}.
$$

### Ví dụ 4: Phép thế theo tổ hợp lặp lại
Giải phương trình

$$
\frac{dy}{dt}=\left(t+y\right)^2-1.
$$

Nhận thấy tổ hợp $$ t+y $$ xuất hiện nguyên khối, đặt $$ u=t+y $$. Khi đó

$$
\frac{du}{dt}=1+\frac{dy}{dt}=1+\left(t+y\right)^2-1=u^2.
$$

Phương trình $$ \frac{du}{dt}=u^2 $$ có nghiệm cân bằng $$ u=0 $$ (ứng với $$ y(t)=-t $$). Với $$ u\neq 0 $$, tách biến $$ \frac{1}{u^2}du=dt $$ rồi tích phân cho $$ -\frac{1}{u}=t+C_1 $$, đặt $$ C=-C_1 $$ ta được $$ u=\frac{1}{C-t} $$. Quay về biến gốc:

$$
y(t)=\frac{1}{C-t}-t.
$$

## Câu hỏi khái niệm
1. Vì sao phương pháp thế là kỹ thuật nhận diện cấu trúc chứ không phải đoán mò?
2. Trong phương trình thuần nhất cấp một, vì sao tỉ số $$ \frac{y}{t} $$ là biến phụ tự nhiên?
3. Vì sao một phép đổi biến phù hợp có thể chuyển phương trình phi tuyến thành phương trình tuyến tính hoặc tách biến?

## Bài toán ứng dụng
1. Trong cơ học, khi bài toán chỉ phụ thuộc vào góc hoặc tỉ số giữa hai tọa độ, vì sao phép đổi biến tương ứng lại phản ánh đại lượng vật lý tự nhiên hơn biến gốc?
2. Trong mô hình tăng trưởng có số hạng bậc hai, phép đổi biến nghịch đảo $$ u=1/P $$ đem lại thuận lợi gì?
3. Trong mô hình dịch tễ, nếu một tổ hợp đại lượng lặp lại nhiều lần trong phương trình, việc đặt biến phụ cho tổ hợp đó giúp ích gì cho phân tích?

## Chiến lược giảng dạy tương tác
- Đưa ra 5 phương trình khác nhau và yêu cầu sinh viên đề xuất phép thế ưu tiên cùng lý do chọn trước khi tính.
- Khi chữa bài, để lớp tự xác định mẫu cấu trúc nổi bật thay vì nêu sẵn phép đặt ẩn phụ.
- Yêu cầu sinh viên giải thích bằng lời bước áp dụng quy tắc dây chuyền mỗi khi biến đổi đạo hàm.
- So sánh hai cách giải phương trình logistic (tách biến và phép nghịch đảo Bernoulli) để thấy ưu điểm của từng cách.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Sử dụng bảng đối chiếu giữa dấu hiệu nhận dạng và phép thế gợi ý: thấy $$ F(y/t) $$ thử $$ y=vt $$; thấy dạng $$ y'+p(t)y=q(t)y^n $$ thử $$ v=y^{1-n} $$; thấy tổ hợp $$ at+by+c $$ lặp lại thử đặt $$ u=at+by+c $$.

### Thử thách cho sinh viên khá giỏi
Tự thiết kế một ODE cấp một phi tuyến mà sau một phép đổi biến cho trước sẽ rút về dạng tách biến hoặc tuyến tính, rồi trình bày rõ cơ chế biến đổi.

## Tóm tắt dễ nhớ
Phương pháp thế dựa trên việc chọn lại tọa độ phù hợp với cấu trúc ẩn của phương trình. Trước khi tính toán, hãy kiểm tra ba dấu hiệu quen thuộc: tỉ số $$ y/t $$ (thuần nhất), lũy thừa $$ y^n $$ (Bernoulli) hoặc tổ hợp biểu thức lặp lại.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tăng trưởng có bão hòa do tự cạnh tranh
- Bài toán: Một quần thể vi sinh tăng nhanh ở mật độ thấp nhưng bị kìm hãm do cạnh tranh nội bộ ở mật độ cao.
- Mô hình Bernoulli:

$$
\frac{dy}{dt}+ay=by^2.
$$

- Giả thiết và giới hạn: Tốc độ sinh trưởng và hệ số tự ức chế được xem là hằng số; mô hình chưa xét môi trường biến thiên hay tương tác nhiều loài.
- Diễn giải: Phép thế $$ u=1/y $$ bộc lộ cấu trúc tuyến tính ẩn sau số hạng phi tuyến bậc hai.

#### Mô hình phụ thuộc tỉ số trong kinh tế
- Bài toán: Tốc độ thay đổi sản lượng chỉ phụ thuộc vào tỉ lệ giữa tích lũy và thời gian thay vì từng giá trị riêng lẻ.
- Mô hình thuần nhất cấp một:

$$
\frac{dy}{dt}=F\left(\frac{y}{t}\right).
$$

- Giả thiết và giới hạn: Giả sử hiện tượng có tính đồng dạng theo thang đo; giả thiết này không còn đúng nếu có các mốc thời gian ngoại sinh cụ thể.
- Diễn giải: Phép thế $$ y=vt $$ gom tính đồng dạng vào một biến tỉ số duy nhất $$ v $$.

#### Phản ứng hóa học với kết tụ phi tuyến
- Bài toán: Nồng độ hạt trong buồng lọc biến thiên đồng thời do suy giảm bậc nhất và quá trình va chạm kết tụ bậc hai.
- Mô hình:

$$
\frac{dc}{dt}+kc=qc^2.
$$

- Giả thiết và giới hạn: Buồng phản ứng trộn đều và hệ số kết tụ không đổi; hệ gồm nhiều cỡ hạt khác nhau sẽ đòi hỏi hệ phương trình.
- Diễn giải: Cấu trúc Bernoulli cho phép giải chính xác dù phương trình là phi tuyến.

### 2. Trực giác bổ sung và các kết nối

Phương pháp thế cho thấy việc chọn biến mô tả đúng quan trọng không kém kỹ thuật tính toán. Những biến phụ như nghịch đảo nồng độ, tỉ số hay tổ hợp tuyến tính thường mang ý nghĩa hình học hoặc vật lý rõ ràng hơn biến gốc. Tư duy này nối tiếp sang các chương sau: đổi cơ sở để chéo hóa hệ ODE tuyến tính, hay đổi biến để bộc lộ tính đối xứng trong PDE.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K, P0 = 0.9, 50, 5
t = np.linspace(0, 10, 400)
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
U = 1 / P

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(t, P, color="darkgreen")
axes[0].set_title("Biến gốc P(t)")
axes[0].set_xlabel("t")
axes[0].set_ylabel("P")

axes[1].plot(t, U, color="darkred")
axes[1].set_title("Biến phụ u(t) = 1 / P(t)")
axes[1].set_xlabel("t")
axes[1].set_ylabel("u")

for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

Đồ thị bên phải minh họa đường cong suy giảm mũ đơn giản của nghiệm phương trình tuyến tính theo $$ u $$, giúp thấy rõ cách phép thế làm đơn giản hóa bài toán phi tuyến gốc.

### 4. Gợi ý tìm thêm mô phỏng

- search: Bernoulli differential equation application
- search: homogeneous first order equation visualization
- search: Riccati equation substitution linearization

### 5. Bài toán mẫu có bối cảnh thực

Xét phương trình Bernoulli

$$
\frac{dy}{dt}+0.5y=0.02y^2,\qquad y(0)=4.
$$

Đặt $$ u=\frac{1}{y} $$, ta thu được phương trình tuyến tính $$ \frac{du}{dt}-0.5u=-0.02 $$ với điều kiện đầu $$ u(0)=0.25 $$. Giải ra ta được

$$
u(t)=0.04+0.21e^{0.5t}, \qquad y(t)=\frac{1}{0.04+0.21e^{0.5t}}.
$$

Nghiệm này cho thấy với mật độ ban đầu $$ y(0)=4 $$ nằm dưới ngưỡng cân bằng không ổn định $$ y=25 $$, thành phần suy giảm bậc nhất chi phối nên $$ y(t) $$ giảm dần về $$ 0 $$ khi $$ t\to\infty $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Thành thạo hai mẫu chuẩn là Bernoulli và thuần nhất cấp một, luôn nêu rõ lý do chọn phép thế và bước biến đổi đạo hàm.

**Bậc sau đại học.** Mở rộng sang phương trình Riccati, bất biến đối xứng Lie và kỹ thuật đổi tọa độ chuẩn hóa trong lý thuyết hệ động lực.

## Video tham khảo

- Xem trước: [The Bernoulli Equation // Substitutions in Differential Equations](https://www.youtube.com/watch?v=iCN8nGXE29o) — Dr. Trefor Bazett, tiếng Anh. Trình bày phép thế Bernoulli đưa phương trình phi tuyến về dạng tuyến tính.
- [Separation of Variables //  Differential Equations](https://www.youtube.com/watch?v=7Y-frhf-1Zk) — Dr. Trefor Bazett, tiếng Anh. Ôn phương pháp tách biến dùng ngay sau phép thế thuần nhất.
- [Linear Differential Equations & the Method of Integrating Factors](https://www.youtube.com/watch?v=2H6BZHlD_3g) — Dr. Trefor Bazett, tiếng Anh. Ôn phương pháp nhân tử tích phân để hoàn tất bước giải phương trình Bernoulli.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày rõ các ví dụ Bernoulli và phương trình thuần nhất cơ bản.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập luyện nhận diện phép thế qua đa dạng mẫu bài.
- Ross — *Differential Equations*: trình bày ngắn gọn, tiện ôn tập nhanh các phép đổi biến chuẩn.
