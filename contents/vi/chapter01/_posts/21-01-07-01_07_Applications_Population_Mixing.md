---
layout: post
title: "01-07 Ứng dụng: Mô hình Dân số và Pha trộn"
chapter: '01'
order: 7
owner: Course Team
lang: vi
categories:
- chapter01
lesson_type: required
---


Một quần thể vi khuẩn trong đĩa Petri hay nồng độ muối trong bể pha trộn công nghiệp trông có vẻ thuộc hai thế giới khác nhau, nhưng dưới lăng kính phương trình vi phân cấp một, chúng cùng tuân theo một nguyên lý kế toán duy nhất: **Tốc độ thay đổi = Tốc độ vào − Tốc độ ra**. Hiểu cách dịch ngôn ngữ thực tế sang phương trình vi phân sẽ biến toán học trừu tượng thành công cụ dự báo sống động.

## Bản đồ kiến thức nền: Bốn mô hình ứng dụng cốt lõi của PTVP Cấp Một

1. **Mô hình Malthus ($P' = rP$) & Thời gian nhân đôi**:
   Tốc độ tăng trưởng tỷ lệ thuận với dân số hiện tại dẫn đến tăng trưởng hàm mũ $P(t) = P_0 e^{rt}$ với chu kỳ nhân đôi $T_2 = \frac{\ln 2}{r}$—chính xác trong giai đoạn đầu khi tài nguyên dồi dào.
2. **Mô hình Logistic Verhulst ($P' = rP(1 - P/K)$)**:
   Đưa thêm **sức chứa môi trường $K$** tạo ra lực hãm phi tuyến; đồ thị hình chữ S tăng nhanh nhất tại điểm uốn $P = K/2$ rồi tiệm cận bền vững về $K$.
3. **Bài toán Pha trộn (Mixing Tank)**:
   Đặt $A(t)$ là *khối lượng* chất tan trong bể thể tích $V(t)$; khi đó $A'(t) = c_{\text{in}} r_{\text{in}} - \frac{A(t)}{V(t)} r_{\text{out}}$—luôn là **phương trình tuyến tính cấp một**!
4. **Phân rã phóng xạ & Định tuổi Carbon-14**:
   Trường hợp $r < 0$ với chu kỳ bán rã $T_{1/2} = \frac{\ln 2}{\lambda}$, giúp xác định niên đại cổ vật từ tỷ lệ đồng vị còn lại.

## Mục tiêu
Bài học này giúp sinh viên vận dụng phương trình vi phân cấp một để mô hình hóa các quá trình thực tế qua hai lớp bài toán kinh điển là tăng trưởng dân số và bể pha trộn. Sau bài học, sinh viên có thể chuyển mô tả hiện tượng sang phương trình, giải và diễn giải ý nghĩa nghiệm, đồng thời đánh giá phạm vi hợp lý của các giả thiết mô hình.

## Kiến thức nền
Sinh viên cần nắm vững phương trình tách biến, phương trình tuyến tính cấp một và kỹ năng kiểm tra thứ nguyên (đơn vị). Việc hiểu rõ ý nghĩa từng đại lượng và áp dụng đúng nguyên lý cân bằng "tốc độ vào trừ tốc độ ra" giúp tránh sai sót khi lập phương trình.

## Dẫn nhập
![Sơ đồ minh họa cho bài 01-07 Ứng dụng: Mô hình Dân số và Pha trộn]({{ site.imgurl }}/chapter_img/chapter01/01_07_applications_population_mixing.svg)

Một mô hình toán học tốt bắt đầu từ việc xác định đúng biến trạng thái và các cơ chế làm biến trạng thái đó thay đổi: quần thể biến động do sinh và chết; lượng chất tan trong bể biến động do dòng chảy vào và dòng chảy ra. Khi viết tốc độ biến thiên dưới dạng tổng hợp các cơ chế đó, ODE trở thành công cụ trực tiếp để phân tích và dự báo.

Hai lớp bài toán trong bài học bổ trợ chặt chẽ cho nhau: mô hình dân số minh họa sự tăng trưởng, bão hòa và vai trò của điểm cân bằng; mô hình pha trộn rèn luyện nguyên lý bảo toàn khối lượng "tốc độ thay đổi bằng tốc độ vào trừ tốc độ ra".

### Khung giải thích (nên đọc chậm): Tính nồng độ muối trong bể pha trộn 100 lít theo từng bước

Một bể chứa sẵn $100\text{ L}$ nước tinh khiết ($A(0) = 0$). Nước muối nồng độ $0{,}5\text{ kg/L}$ chảy vào với tốc độ $2\text{ L/phút}$, hỗn hợp khuấy đều chảy ra cũng với tốc độ $2\text{ L/phút}$ (nên thể tích giữ nguyên $V(t) = 100\text{ L}$).
1. **Thiết lập phương trình cân bằng khối lượng**:
   - Lượng muối vào: $0{,}5 \times 2 = 1\text{ kg/phút}$.
   - Lượng muối ra: $\frac{A(t)}{100} \times 2 = 0{,}02\,A(t)\text{ kg/phút}$.
   - Phương trình tuyến tính: $A'(t) + 0{,}02 A(t) = 1$.
2. **Giải với thừa số tích phân $\mu(t) = e^{0{,}02 t}$**:
   $$\frac{d}{dt}\big(e^{0{,}02 t}A\big) = e^{0{,}02 t} \implies A(t) = 50 + C e^{-0{,}02 t}.$$
3. **Ghim điều kiện $A(0) = 0$**: $C = -50 \implies A(t) = \mathbf{50(1 - e^{-0{,}02 t})}\text{ kg}$.
4. **Kiểm tra trực giác vật lý**: Sau $t = 50$ phút, $A(50) = 50(1 - e^{-1}) \approx \mathbf{31{,}61\text{ kg}}$; khi $t \to \infty$, $A(t) \to 50\text{ kg}$ (tương ứng nồng độ $50/100 = 0{,}5\text{ kg/L}$, khớp hoàn toàn với nồng độ dòng chảy vào!).

## Khái niệm theo ba cách

### Cách nhìn trực quan
Trong mô hình dân số, quần thể càng lớn thì số cá thể mới sinh trong cùng khoảng thời gian càng nhiều, nhưng khi tài nguyên hữu hạn, tốc độ tăng phải giảm dần. Trong bài toán bể trộn, lượng chất tan tăng hay giảm tùy thuộc vào sự chênh lệch giữa lượng bơm vào và lượng bị cuốn ra ngoài mỗi đơn vị thời gian.

### Cách nhìn hình ảnh
Đồ thị tăng trưởng mũ uốn cong đi lên không bị chặn, trong khi đồ thị tăng trưởng logistic lúc đầu gần giống hàm mũ rồi uốn phẳng dần khi tiệm cận sức chứa môi trường. Với bể trộn thể tích không đổi, đồ thị lượng chất tan tiến dần về một giá trị cân bằng không phụ thuộc trạng thái ban đầu, phản ánh sự chi phối dài hạn của nồng độ dòng vào.

### Cách nhìn hình thức
Ba mô hình nền tảng gồm:

**Tăng trưởng mũ**:

$$
\frac{dP}{dt}=rP.
$$

**Tăng trưởng logistic**:

$$
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
$$

**Bể trộn thể tích không đổi**:

$$
\frac{dS}{dt}=\text{tốc độ vào}-\text{tốc độ ra}.
$$

Khi dung dịch trong bể được khuấy đều, tốc độ chảy ra bằng lưu lượng ra nhân với nồng độ tức thời trong bể.

## Những ý tưởng mô hình hóa cốt lõi
Bước đầu tiên và quan trọng nhất là chọn đúng biến trạng thái: với dân số là số cá thể $$ P(t) $$; với bể trộn thường là khối lượng chất tan $$ S(t) $$ (thay vì nồng độ, trừ khi chủ đích viết theo nồng độ). Sau đó thiết lập phương trình cân bằng tốc độ và kiểm tra tính nhất quán về đơn vị ở mọi số hạng.

## Những ngộ nhận thường gặp
- "Dân số luôn tăng theo hàm mũ." Sai. Mô hình mũ chỉ phù hợp ở giai đoạn đầu hoặc khi tài nguyên chưa bị giới hạn.
- "Trong bài toán bể trộn, tốc độ chất tan chảy ra là hằng số." Sai. Tốc độ chảy ra tỉ lệ với nồng độ tức thời trong bể nên thay đổi theo thời gian.
- "Giải ra công thức đẹp nghĩa là mô hình chính xác." Sai. Độ tin cậy của dự báo phụ thuộc trực tiếp vào mức độ hợp lý của các giả thiết đặt ra.
- "Điểm cân bằng chỉ là nghiệm đặc biệt về mặt đại số." Sai. Trong ứng dụng, điểm cân bằng ổn định thường chính là trạng thái dài hạn mà hệ tiến tới.

## Tiến trình học tập đề xuất

### Bước 1: Chọn biến trạng thái
Xác định rõ đại lượng cần theo dõi theo thời gian cùng đơn vị đo của nó.

### Bước 2: Thiết lập cân bằng tốc độ
Viết tốc độ tăng thuần (sinh trừ chết) cho quần thể hoặc hiệu tốc độ vào trừ tốc độ ra cho bể trộn.

### Bước 3: Kiểm tra đơn vị
Đảm bảo mọi số hạng trong phương trình có cùng đơn vị (như kg/phút hoặc cá thể/năm).

### Bước 4: Giải và diễn giải kết quả
Đọc giới hạn dài hạn, mức bão hòa và độ nhạy của nghiệm theo các tham số.

### Các checkpoint
- Bạn có chọn đúng biến trạng thái cho từng bài toán không?
- Bạn có viết đúng tốc độ ra của bể trộn bằng tích của lưu lượng ra và nồng độ tức thời không?
- Bạn có phân biệt được ý nghĩa thực tế của mô hình mũ và mô hình logistic không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Tăng trưởng dân số theo hàm mũ
Giả sử dân số thỏa mãn

$$
\frac{dP}{dt}=0.04P,\qquad P(0)=1000.
$$

Giải bằng tách biến ta được $$ P(t)=1000e^{0.04t} $$. Mô hình dự đoán tăng trưởng không giới hạn, chỉ phù hợp trong giai đoạn đầu khi tài nguyên còn dồi dào.

### Ví dụ 2: Mô hình logistic
Xét bài toán

$$
\frac{dP}{dt}=0.5P\left(1-\frac{P}{1000}\right),\qquad P(0)=100.
$$

Đây là mô hình logistic với sức chứa môi trường $$ K=1000 $$. Giải bằng tách biến (hoặc công thức logistic) ta thu được

$$
P(t)=\frac{1000}{1+9e^{-0.5t}}.
$$

Quần thể tăng nhanh ở giai đoạn đầu rồi chậm dần và tiệm cận mức cân bằng sinh thái $$ P=1000 $$.

### Ví dụ 3: Bể trộn thể tích không đổi
Một bể 200 lít ban đầu chứa 20 kg muối. Dung dịch nồng độ $$ 0.1\text{ kg/lít} $$ chảy vào với lưu lượng $$ 4\text{ lít/phút} $$, và hỗn hợp khuấy đều chảy ra với cùng lưu lượng $$ 4\text{ lít/phút} $$. Gọi $$ S(t) $$ là khối lượng muối trong bể.

Tốc độ muối chảy vào là $$ 0.1\cdot 4=0.4\text{ kg/phút} $$. Nồng độ tức thời trong bể là $$ \frac{S}{200} $$, nên tốc độ muối chảy ra là $$ 4\cdot \frac{S}{200}=\frac{S}{50} $$. Do đó

$$
\frac{dS}{dt}=0.4-\frac{S}{50}.
$$

Giải phương trình tuyến tính cấp một này cho $$ S(t)=20+Ce^{-t/50} $$. Với điều kiện đầu $$ S(0)=20 $$, ta được $$ C=0 $$, tức $$ S(t)\equiv 20 $$. Điều này hoàn toàn hợp lý vì nồng độ ban đầu trong bể ($$ 20/200 = 0.1\text{ kg/lít} $$) đã bằng đúng nồng độ dòng vào.

### Ví dụ 4: Bể trộn khởi đầu ngoài trạng thái cân bằng
Giữ nguyên các thông số ở Ví dụ 3 nhưng đổi điều kiện đầu thành $$ S(0)=0 $$. Khi đó

$$
S(t)=20-20e^{-t/50}.
$$

Lượng muối tăng dần từ $$ 0 $$ lên $$ 20\text{ kg} $$, trong đó ảnh hưởng của điều kiện đầu nằm ở số hạng hàm mũ tắt dần $$ -20e^{-t/50} $$.

## Câu hỏi khái niệm
1. Vì sao mô hình logistic thường thực tế hơn mô hình tăng trưởng mũ khi xét dài hạn?
2. Trong bể trộn, vì sao tốc độ chất tan chảy ra phụ thuộc vào nồng độ tức thời thay vì chỉ phụ thuộc lưu lượng?
3. Việc nghiệm tiến về điểm cân bằng cho biết điều gì về vai trò của điều kiện đầu về dài hạn?

## Bài toán ứng dụng
1. Một đàn hươu trong khu bảo tồn tăng nhanh trong vài năm đầu rồi chậm lại. Trong giai đoạn nào nên dùng mô hình mũ và khi nào cần chuyển sang mô hình logistic?
2. Một bệnh nhân được truyền thuốc với tốc độ không đổi trong khi cơ thể đào thải tỉ lệ với lượng thuốc hiện có. Hãy chỉ ra sự tương đồng cấu trúc với bài toán bể trộn.
3. Một hồ chứa chất ô nhiễm có dòng thải chảy vào và dòng nước chảy ra. Cần những giả thiết nào để áp dụng mô hình bể trộn đều?

## Chiến lược giảng dạy tương tác
- Khởi động bằng bài tập chuyển mô tả lời sang phương trình: giao ba tình huống thực tế để từng nhóm chọn biến trạng thái và viết phương trình sơ bộ.
- Dừng lại ngay sau bước lập phương trình để cả lớp kiểm tra đơn vị từng số hạng trước khi giải.
- Cho sinh viên dự đoán giới hạn dài hạn bằng trực giác vật lý trước khi giải giải tích.
- Thảo luận ngắn câu hỏi: "Một mô hình đơn giản nhưng giải tích được có ưu điểm và hạn chế gì so với một mô hình chi tiết nhưng khó giải?"

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn
Dùng bảng hai cột "tốc độ vào" và "tốc độ ra" kèm đơn vị cho từng bài toán pha trộn; với bài toán dân số, diễn đạt quy luật biến thiên bằng lời trước khi viết ký hiệu ODE.

### Thử thách cho sinh viên khá giỏi
Mở rộng mô hình logistic có thêm yếu tố khai thác (thu hoạch) với tốc độ không đổi, hoặc xét bể trộn có lưu lượng vào và ra khác nhau khiến thể tích $$ V(t) $$ thay đổi theo thời gian.

## Tóm tắt dễ nhớ
Mô hình hóa bằng ODE bắt đầu từ việc chọn biến trạng thái phù hợp, thiết lập phương trình cân bằng tốc độ và kiểm tra đơn vị. Mô hình dân số minh họa cơ chế tăng trưởng và bão hòa; mô hình bể trộn minh họa quy luật bảo toàn "vào trừ ra".

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Quần thể động vật với sức chứa môi trường
- Bài toán: Một đàn hươu trong khu bảo tồn ban đầu tăng nhanh nhưng bị giới hạn dần bởi nguồn thức ăn và không gian sống.
- Mô hình:

$$
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
$$

- Giả thiết và giới hạn: Sức chứa $$ K $$ cố định và quần thể đồng nhất; chưa xét săn bắt, mùa vụ hay cấu trúc tuổi.
- Diễn giải: Nghiệm tăng gần như hàm mũ ở giai đoạn đầu và tiệm cận cân bằng sinh thái $$ K $$ về dài hạn.

#### Bể trộn xử lý nước
- Bài toán: Một bể xử lý nhận dòng nước chứa chất ô nhiễm và xả ra với cùng lưu lượng; cần tính diễn biến nồng độ theo thời gian.
- Mô hình:

$$
\frac{dS}{dt}=q_{\mathrm{in}}c_{\mathrm{in}}-q_{\mathrm{out}}\frac{S}{V}.
$$

- Giả thiết và giới hạn: Bể được khuấy đều hoàn toàn và thể tích $$ V $$ không đổi; sự phân tầng nồng độ hoặc lắng cặn mạnh sẽ vượt ngoài phạm vi mô hình.
- Diễn giải: Minh họa trực tiếp nguyên lý cân bằng khối lượng trong kỹ thuật môi trường.

#### Dược động học một ngăn với truyền liên tục
- Bài toán: Truyền thuốc tĩnh mạch với tốc độ không đổi trong khi cơ thể đào thải tỉ lệ bậc nhất với nồng độ thuốc.
- Mô hình:

$$
\frac{dC}{dt}=\frac{u_0}{V}-kC.
$$

- Giả thiết và giới hạn: Thuốc phân bố đều tức thời trong một ngăn duy nhất và thải trừ bậc một; nhiều loại thuốc thực tế đòi hỏi mô hình hai hoặc ba ngăn.
- Diễn giải: Nồng độ thuốc tiệm cận mức ổn định $$ u_0/(kV) $$, làm cơ sở thiết kế liều truyền duy trì.

### 2. Trực giác bổ sung và các kết nối

Bài học đặt tư duy mô hình hóa vào vị trí trung tâm: chọn biến trạng thái, kiểm tra thứ nguyên và nhận diện quy luật cân bằng. Mô hình logistic mở thẳng sang bài phương trình tự trị và phân tích ổn định; còn bài toán bể trộn là dạng sơ khai của phương trình cân bằng khối lượng xuất hiện xuyên suốt trong kỹ thuật hóa học, sinh học hệ thống và kỹ thuật môi trường.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 0.5, 1000
t = np.linspace(0, 25, 400)
for P0 in [50, 150, 400, 1200]:
    P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
    plt.plot(t, P, label=f"P0={P0}")

plt.axhline(K, color="black", linestyle="--", label="carrying capacity")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Quần thể logistic tiến về sức chứa")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

Đồ thị cho thấy mọi quỹ đạo xuất phát từ $$ P_0>0 $$ đều hội tụ về sức chứa $$ K $$, minh họa trực quan tính ổn định của cân bằng sinh thái.

### 4. Gợi ý tìm thêm mô phỏng

- search: mixing tank differential equation simulation
- search: logistic growth carrying capacity interactive
- search: pharmacokinetics one compartment ODE plot

### 5. Bài toán mẫu có bối cảnh thực

Một bể chứa 200 lít nước ban đầu có 8 kg muối. Dung dịch nồng độ $$ 0.05\text{ kg/lít} $$ chảy vào với lưu lượng $$ 4\text{ lít/phút} $$ và chảy ra với cùng lưu lượng $$ 4\text{ lít/phút} $$. Ta có

$$
\frac{dS}{dt}=0.2-\frac{4}{200}S, \qquad S(0)=8.
$$

Giải phương trình tuyến tính cho nghiệm

$$
S(t)=10-2e^{-0.02t}.
$$

Lượng muối trong bể tiến dần về $$ 10\text{ kg} $$ (tương ứng nồng độ $$ 0.05\text{ kg/lít} $$ của dòng vào), cho thấy về dài hạn hệ không còn phụ thuộc trạng thái ban đầu.

### 6. Phân tầng độ khó

**Bậc đại học.** Chọn đúng biến trạng thái, thiết lập cân bằng tốc độ và diễn giải nghiệm theo đơn vị và ý nghĩa thực tế.

**Bậc sau đại học.** Phân tích tính dương của nghiệm, ước lượng tham số từ dữ liệu, phi thứ nguyên hóa (nondimensionalization) và tính nhận dạng tham số của mô hình.

## Video tham khảo

- Xem trước: [The Logistic Growth Differential Equation](https://www.youtube.com/watch?v=aP4YXOo-Uko) — Dr. Trefor Bazett, tiếng Anh. Trình bày phương trình logistic, sức chứa môi trường và các điểm cân bằng.
- [❖ Mixing Problems and Separable Differential Equations ❖](https://www.youtube.com/watch?v=6wk9zWa-Fww) — Patrick J, tiếng Anh. Thiết lập và giải bài toán bể trộn bằng ODE cấp một.
- [Newton's Law of Cooling  // Separable ODE Example](https://www.youtube.com/watch?v=_bAjWNsNrQA) — Dr. Trefor Bazett, tiếng Anh. Minh họa sự tương đồng cấu trúc giữa bài toán làm nguội và bài toán pha trộn.

## Tài liệu tham khảo
- Boyce & DiPrima — *Elementary Differential Equations*: trình bày sâu các mô hình dân số, bể trộn và diễn giải vật lý.
- Zill — *Differential Equations with Boundary-Value Problems*: nhiều bài tập mô hình hóa thực tiễn.
- Ross — *Differential Equations*: cung cấp các biến thể của mô hình logistic và bài toán trộn.
