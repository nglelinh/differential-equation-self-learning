---
layout: post
title: "Tập Hợp Mặt Sóng (Wave Front Set)"
chapter: '15'
order: 1
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: required
---

![Wave front set như mô tả vị trí và hướng của singularity]({{ site.imgurl }}/chapter_img/chapter15/01_wave_front_sets.svg )

Hãy tưởng tượng bạn đứng trên một cánh đồng phẳng có một rãnh nứt kéo dài theo hướng Bắc–Nam. Nếu bạn đi dọc theo hướng Bắc–Nam, mặt đất phẳng lì trơn tru; nhưng nếu bạn bước ngang hướng Đông–Tây băng qua rãnh, bạn lập tức vấp phải bước nhảy! **Tập Mặt sóng $\operatorname{WF}(u)$ (Wave Front Set)** của Lars Hörmander nắm bắt chính xác trực giác ấy: nó không chỉ đánh dấu vị trí rãnh nứt $x$, mà còn chỉ rõ **hướng tần số $\xi$ nào bị vấp kỳ dị**—một bước nâng cấp vĩ đại biến không gian vị trí thành không gian pha $T^*\mathbb{R}^n \setminus 0$!

## Kiến thức cần nhớ: Bốn trụ cột của Tập Mặt sóng $\operatorname{WF}(u)$

1. **Định nghĩa Chặt chẽ trên $T^*\mathbb{R}^n \setminus 0$**:
   Điểm $(x_0, \xi_0) \notin \operatorname{WF}(u)$ khi và chỉ khi tồn tại hàm cắt $\phi \in C_c^\infty$ ($\phi(x_0) \neq 0$) và một hình nón mở $\Gamma$ chứa $\xi_0$ sao cho $|\widehat{\phi u}(\xi)| \le C_N (1 + |\xi|)^{-N}$ với mọi $N$ và mọi $\xi \in \Gamma$.
2. **Chiếu xuống không gian vị trí ra đúng Giá kỳ dị**:
   $\pi_x(\operatorname{WF}(u)) = \operatorname{sing\,supp}(u)$! Nếu $\operatorname{WF}(u) = \emptyset$ thì $u \in C^\infty$. Hơn nữa $\operatorname{WF}(u)$ là một tập con **đóng và hình nón** (bất biến dưới phép nhân $\xi \mapsto \lambda\xi$ với $\lambda > 0$).
3. **Tính Vi-địa phương (Microlocality) của $\Psi$DO**:
   Mạnh hơn cả tính giả-địa phương ở Chương 14: $\operatorname{WF}(Pu) \subset \operatorname{WF}(u)$ với mọi $P \in \Psi^m$—một toán tử giả vi phân không những không tạo điểm kỳ dị mới, mà còn **không bao giờ xoay chuyển hướng tần số kỳ dị**!
4. **Phép nhân hai Phân phối nhờ Điều kiện Hörmander**:
   Bình thường ta không thể nhân hai phân phối (như $\delta_0^2$ vô nghĩa!). Nhưng định lý Hörmander khẳng định: tích $u \cdot v$ **hoàn toàn định nghĩa được** miễn là tổng hai hướng mặt sóng không bao giờ triệt tiêu nhau: $(x, 0) \notin \operatorname{WF}(u) + \operatorname{WF}(v)$!

## Mục tiêu

Bài học này mở đầu chương giải tích vi địa phương bằng khái niệm trung tâm nhất: tập hợp mặt sóng (wave front set). Sau bài học, sinh viên cần hiểu vì sao giá kỳ dị (singular support) là chưa đủ, lý do tập mặt sóng phải lưu đồng thời vị trí và hướng tần số, và vai trò của định nghĩa này trong việc theo dõi điểm kỳ dị của PDE hiện đại.

## Kiến thức nền

Sinh viên nên nắm vững phân phối, biến đổi Fourier, hàm cắt trơn, giá kỳ dị và trực giác rằng một hàm có thể trơn theo một số hướng nhưng không trơn theo các hướng khác (đã ôn tập ở Bài 15.00). Nếu các chương trước chủ yếu xét tính chính quy theo vị trí, thì ở đây ta xét tinh hơn: đồng thời theo vị trí và theo hướng trong không gian đối ngẫu.

## Dẫn nhập

Giá kỳ dị chỉ cho biết một phân phối không trơn ở đâu, chứ chưa cho biết nó không trơn theo hướng nào. Thông tin hướng này lại giữ vai trò quyết định đối với cách kỳ dị lan truyền dưới tác động của PDE: một góc nhọn, một biên cạnh hay một nguồn điểm có thể nằm tại cùng một vị trí nhưng có cấu trúc tần số rất khác nhau.

Tập mặt sóng ra đời để bổ sung đúng phần thông tin còn thiếu đó, cung cấp bản đồ kỳ dị trên không gian pha cục bộ, nơi mỗi vị trí được gắn kèm các hướng tần số mà tính trơn bị vi phạm.


### Giải thích: Tính trực tiếp Tập Mặt sóng $\operatorname{WF}(u)$ của hàm bước nhảy 2D $u(x_1, x_2) = H(x_1)$

Xét phân phối 2D $u(x_1, x_2) = H(x_1)$ (nhảy từ $0$ lên $1$ qua đường thẳng $x_1 = 0$) tại điểm $x_0 = (0, 0)$. Chọn hàm cắt tách biến $\phi(x_1, x_2) = \phi_1(x_1)\phi_2(x_2) \in C_c^\infty(\mathbb{R}^2)$ với $\phi_1(0) = \phi_2(0) = 1$:
1. **Tính biến đổi Fourier cục bộ hóa**:
   $$\widehat{\phi u}(\xi_1, \xi_2) = \widehat{\phi_1 H}(\xi_1) \cdot \widehat{\phi_2}(\xi_2).$$
2. **Kiểm tra hai trường hợp của hướng $\xi = (\xi_1, \xi_2) \neq (0, 0)$**:
   - **Nếu $\xi_2 \neq 0$**: Trong hình nón đủ hẹp quanh $(\xi_1, \xi_2)$, ta có $|\xi_2| \ge c|\xi|$. Vì $\phi_2 \in C_c^\infty$ nên $|\widehat{\phi_2}(\xi_2)| \le C_N (1 + |\xi_2|)^{-N} \le C'_N (1 + |\xi|)^{-N}$ (tắt siêu nhanh!), còn $|\widehat{\phi_1 H}(\xi_1)|$ bị chặn! Do đó $(x_0, \xi) \notin \operatorname{WF}(u)$.
   - **Nếu $\xi_2 = 0$ và $\xi_1 \neq 0$**: $\widehat{\phi_2}(0) \neq 0$, còn tích phân từng phần cho $\widehat{\phi_1 H}(\xi_1) \sim \frac{1}{i\xi_1}$ (chỉ tắt bậc $-1$, không tắt siêu nhanh!).
3. **Kết luận**: $\operatorname{WF}(H(x_1)) = \mathbf{\{((0, x_2), (\xi_1, 0)) : x_2 \in \mathbb{R},\; \xi_1 \neq 0\}}$!
## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng ánh sáng chiếu vào một vật thể có cạnh sắc: nếu chỉ biết vị trí của cạnh mà không biết hướng của nó, ta không thể dự đoán chính xác bóng đổ hay hướng phản xạ. Tập mặt sóng đóng vai trò tương tự đối với điểm kỳ dị: không chỉ đánh dấu nơi hàm không trơn mà còn chỉ rõ kỳ dị biểu hiện theo những hướng tần số nào.

### Cách hình ảnh

Có thể minh họa bằng ba ví dụ đối chiếu:

- một hàm trơn, không có hướng kỳ dị nào;
- phân phối delta Dirac tại gốc, có kỳ dị theo mọi hướng;
- hàm bậc thang theo biến $$ x_1 $$, chỉ có kỳ dị theo hướng pháp tuyến với mặt nhảy.

So sánh này cho thấy cùng là “không trơn”, nhưng cấu trúc vi địa phương rất khác biệt. Nên vẽ kèm một điểm $$ x_0 $$ trong không gian vị trí cùng một nón hướng $$ \xi $$ trong không gian tần số.

### Cách hình thức

Với $$ u\in \mathcal{D}'(\Omega) $$, ta nói cặp $$ (x_0,\xi_0)\notin WF(u) $$ nếu tồn tại một hàm cắt trơn $$ \varphi\in C_c^\infty(\Omega) $$ bằng 1 trong một lân cận của $$ x_0 $$, sao cho biến đổi Fourier của $$ \varphi u $$ suy giảm nhanh trong một nón mở chứa $$ \xi_0 $$:

$$
\widehat{\varphi u}(\xi)=O(\lvert \xi\rvert^{-N})
\qquad \text{với mọi } N,
$$

khi $$ \xi $$ thuộc nón đó và $$ \lvert \xi\rvert\to\infty $$.

Nếu điều kiện này không thỏa mãn, ta nói $$ u $$ có kỳ dị vi địa phương tại

$$ (x_0,\xi_0). $$

## So sánh nhanh với giá kỳ dị

Có thể tóm tắt mối quan hệ giữa hai khái niệm như sau:

- giá kỳ dị trả lời câu hỏi: hàm hoặc phân phối không trơn ở đâu;
- tập mặt sóng trả lời câu hỏi tinh hơn: không trơn ở đâu và theo hướng tần số nào;
- hình chiếu của tập mặt sóng xuống không gian vị trí chính là giá kỳ dị.

Nói cách khác, giá kỳ dị là “bản đồ vị trí” của kỳ dị, còn tập mặt sóng là “bản đồ vị trí kèm la bàn hướng”. Trong các bài toán truyền sóng và tái tạo ảnh, chính phần thông tin hướng này quyết định kỳ dị nào khả kiến và di chuyển theo quỹ đạo nào.

## Ngộ nhận thường gặp

### “Tập mặt sóng chỉ là cách viết lại của giá kỳ dị”

Sai. Giá kỳ dị chỉ chứa thông tin vị trí, còn tập mặt sóng bổ sung thông tin hướng tần số.

### “Nếu một hàm không trơn tại một điểm thì nó kỳ dị theo mọi hướng”

Không đúng. Nhiều kỳ dị chỉ xuất hiện dọc theo một số hướng xác định.

### “Biến đổi Fourier suy giảm nhanh nghĩa là hàm phải trơn toàn cục”

Không đúng. Ta chỉ xét biến đổi Fourier của $$ \varphi u $$ sau khi đã cắt cục bộ quanh điểm $$ x_0 $$.

### “Tập mặt sóng quá trừu tượng nên chỉ dùng trong lý thuyết thuần túy”

Sai. Đây là công cụ nền tảng cho lý thuyết lan truyền kỳ dị, bài toán ngược và kỹ thuật tái tạo ảnh.

## Tiến trình học

### Bước 1: Ôn lại giá kỳ dị

Khẳng định lại vai trò của giá kỳ dị trong việc xác định vị trí mất tính trơn.

### Bước 2: Áp dụng biến đổi Fourier cục bộ

Nhân với hàm cắt trơn quanh $$ x_0 $$ rồi khảo sát tốc độ suy giảm của biến đổi Fourier.

### Bước 3: Đưa vào nón hướng

Kiểm tra sự suy giảm nhanh trong một nón mở quanh $$ \xi_0 $$ thay vì trên toàn không gian tần số.

### Bước 4: Liên hệ với PDE

Nhấn mạnh rằng các toán tử PDE thường vận chuyển từng cặp vị trí–hướng kỳ dị chứ không dịch chuyển nguyên khối giá kỳ dị.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được vì sao giá kỳ dị là chưa đủ hay không?
- Sinh viên có nêu được vai trò của hàm cắt trơn $$ \varphi $$ hay không?
- Sinh viên có hiểu vì sao cần kiểm tra sự suy giảm nhanh trong một nón mở chứ không trên toàn không gian tần số hay không?

## Ví dụ có lời giải

### Ví dụ 1: Hàm trơn

Nếu $$ u\in C^\infty(\Omega) $$, thì với mọi hàm cắt trơn $$ \varphi $$, tích $$ \varphi u $$ cũng trơn và có giá compact, nên biến đổi Fourier của nó suy giảm nhanh theo mọi hướng. Suy ra $$ WF(u)=\emptyset $$, khớp với kỳ vọng cơ bản của định nghĩa.

### Ví dụ 2: Phân phối delta Dirac

Xét $$ u=\delta_0 $$. Với $$ \varphi=1 $$ gần gốc, ta có $$ \varphi \delta_0=\delta_0 $$, mà biến đổi Fourier của delta Dirac là hằng số nên không suy giảm nhanh theo bất kỳ hướng nào. Do đó $$ WF(\delta_0)=\{(0,\xi):\xi\neq 0\} $$: kỳ dị tập trung tại gốc và xuất hiện theo mọi hướng khác không.

### Ví dụ 3: Hàm bước một chiều

Xét hàm Heaviside

$$
H(x)=
\begin{cases}
0,&x<0,\\
1,&x>0.
\end{cases}
$$

Hàm có bước nhảy duy nhất tại gốc. Trực giác Fourier cho thấy kỳ dị gắn với hướng pháp tuyến của điểm nhảy; trong một chiều, điều này gồm cả hai hướng khác 0 trên trục tần số và tạo bước đệm cho trường hợp nhiều chiều.

### Ví dụ 4: Hàm bậc thang theo một biến trong nhiều chiều

Xét $$ u(x)=H(x_1) $$ trên $$ \mathbb{R}^n $$. Giá kỳ dị là siêu phẳng $$ x_1=0 $$, nhưng tập mặt sóng không chứa mọi hướng $$ \xi $$ mà chỉ chứa các hướng pháp tuyến theo trục $$ x_1 $$, loại trừ các hướng tiếp tuyến thuần túy. Đây là ví dụ thể hiện rõ nhất sự khác biệt giữa giá kỳ dị và tập mặt sóng.

### Ví dụ 5: Một biên cạnh trong ảnh hai chiều

Xét ảnh nhị phân có nửa trái màu đen, nửa phải màu trắng với biên thẳng đứng tại $$ x_1=0 $$. Giá kỳ dị nằm trên đường biên thẳng đứng, còn tập mặt sóng chỉ ra các hướng kỳ dị tập trung theo phương pháp tuyến với biên chứ không dọc theo biên. Đây là cơ sở trực quan quan trọng cho xử lý ảnh và chụp cắt lớp: thuật toán tái tạo thường nhận diện biên theo các hướng cụ thể trước khi phục hồi toàn bộ mức xám.

## Câu hỏi khái niệm

1. Vì sao định nghĩa tập mặt sóng cần đồng thời thông tin vị trí và hướng?
2. Vì sao phải cắt cục bộ bằng hàm $$ \varphi $$ trước khi lấy biến đổi Fourier?
3. Điều gì khiến delta Dirac kỳ dị theo mọi hướng, còn mặt nhảy chỉ kỳ dị theo hướng pháp tuyến?

## Bài toán ứng dụng

1. Trong xử lý ảnh, biên của một vật thể tương ứng với kỳ dị theo hướng nào?
2. Trong chụp cắt lớp, việc biết hướng kỳ dị giúp xác định phần nào của ảnh có thể tái tạo được ra sao?
3. Trong phương trình sóng, vì sao biết “kỳ dị di chuyển theo hướng nào” lại quan trọng hơn việc chỉ biết “kỳ dị đang ở đâu”?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Nếu hai vật thể có biên đi qua cùng một điểm nhưng nghiêng theo hai hướng khác nhau, dữ liệu Fourier có phân biệt được không?
- Phân phối delta Dirac có một hướng kỳ dị hay vô số hướng kỳ dị?
- Vì sao một mặt nhảy không thể kỳ dị theo hướng tiếp tuyến?

### Hoạt động gợi ý

- Cho sinh viên phân loại một vài phân phối đơn giản theo giá kỳ dị và tập mặt sóng.
- Sử dụng hình vẽ biên thẳng, góc nhọn và nguồn điểm để thảo luận về hướng kỳ dị.
- Thảo luận nhóm về ý nghĩa hình học của “nón hướng” trong không gian tần số.

### Cách tăng mức độ tham gia

- Bắt đầu từ ví dụ hình học trực quan trước khi đưa ra định nghĩa hình thức.
- Đề nghị sinh viên dự đoán tập mặt sóng của delta Dirac trước khi tính toán.
- Yêu cầu phân biệt bằng lời giữa “vị trí kỳ dị” và “hướng kỳ dị”.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Tập trung trước vào hai ví dụ mẫu: hàm trơn và delta Dirac.
- Sử dụng nhiều hình vẽ minh họa về biên cạnh và vectơ pháp tuyến.
- Chưa đi sâu vào cấu trúc hình thức của nón đối ngẫu ở lượt học đầu tiên.

### Thử thách cho sinh viên khá giỏi

- Tìm hiểu chứng minh khẳng định $$ WF(u)=\emptyset $$ khi và chỉ khi $$ u\in C^\infty $$.
- Tính tập mặt sóng của phân phối tập trung trên siêu phẳng $$ \delta(x_1) $$ trong nhiều chiều.
- Liên hệ tập mặt sóng với tính chính quy Sobolev vi địa phương.

## Ghi nhớ nhanh

Tập mặt sóng là công cụ mô tả kỳ dị tinh tế hơn giá kỳ dị: nó cho biết cả vị trí lẫn hướng tần số của tính không trơn, tạo nền tảng mở đầu và cốt lõi cho giải tích vi địa phương.

---

## Ứng dụng thực tế

### 1. Xử lý ảnh và phát hiện biên (Thị giác máy tính)

Khi phân tích ảnh số, một bài toán trọng tâm là phát hiện biên vật thể — nơi cường độ sáng biến đổi đột ngột, tức vị trí kỳ dị của hàm ảnh. Nếu chỉ biết giá kỳ dị, ta biết điểm ảnh nào thuộc biên nhưng chưa biết phương chạy của biên. Tập mặt sóng bổ sung hướng: biên thẳng đứng có hướng kỳ dị nằm ngang, còn biên nằm ngang có hướng kỳ dị thẳng đứng.

Các thuật toán phát hiện biên như Canny hay Sobel thực chất ước lượng thông tin kiểu tập mặt sóng một cách gián tiếp: khi tính đạo hàm theo phương $$ x $$ và phương $$ y $$ riêng biệt, ta đang kiểm tra sự biến thiên tần số cao theo từng hướng.

**Mô hình hóa:** Xem ảnh như phân phối $$ u(x_1, x_2) $$. Một biên thẳng đứng tại $$ x_1 = a $$ tương ứng với
$$
WF(u) \supset \{(a, x_2, \xi_1, 0) : \xi_1 \neq 0\},
$$
tức kỳ dị chỉ nằm theo hướng pháp tuyến $$ \xi_1 $$, không theo hướng tiếp tuyến $$ \xi_2 $$.

### 2. Chụp cắt lớp y khoa (CT và MRI)

Máy chụp cắt lớp thu nhận dữ liệu biến đổi Radon của mật độ mô — tích phân mật độ dọc theo các đường thẳng theo nhiều góc chiếu — nhằm giải bài toán ngược khôi phục hàm mật độ $$ f(x) $$.

Tập mặt sóng giải thích vì sao một số biên cơ quan được tái tạo sắc nét hơn các biên khác: nếu tia chiếu tiếp tuyến với biên (tức vuông góc với pháp tuyến của biên), dữ liệu đo nhạy cảm với kỳ dị tại biên đó; ngược lại, nếu thiếu góc chiếu tương ứng, biên sẽ bị mờ hoặc mất. Đây chính là bản chất của bài toán chụp cắt lớp góc hạn chế (limited-angle tomography).

**Giới hạn mô hình:** Mô hình lý tưởng giả định tia truyền thẳng và không tán xạ; trong thực tế, xương và mô mềm có đặc tính tán xạ và hấp thụ khác nhau.

### 3. Địa chấn học và thăm dò địa chất

Trong thăm dò địa chấn, nguồn phát sóng âm truyền xuống lòng đất và các đầu thu (geophone) trên mặt đất ghi lại sóng phản xạ từ các ranh giới địa tầng — nơi mật độ và vận tốc truyền thay đổi đột ngột. Các ranh giới này chính là kỳ dị của hệ số phản xạ.

Tập mặt sóng của dữ liệu địa chấn mã hóa cả vị trí lẫn độ nghiêng của các ranh giới địa chất, cho phép phân biệt tầng nằm ngang với tầng nghiêng. Kỹ thuật di chuyển ảnh địa chấn (seismic migration) về bản chất là phép ánh xạ tập mặt sóng từ miền dữ liệu đo về không gian vật lý.

### 4. Âm học kiến trúc và thiết kế phòng hòa nhạc

Trong phòng hòa nhạc, các xung âm thanh sắc nét phản xạ và nhiễu xạ theo hình học không gian phòng. Kỳ dị của trường sóng lan truyền dọc theo đặc trưng, còn hướng kỳ dị quyết định hướng phản xạ. Kỹ thuật dò tia (ray tracing) dùng trong thiết kế âm học chính là phiên bản hình học cổ điển của cấu trúc tập mặt sóng để dự đoán tiếng vọng và phân bố năng lượng âm.

---

## Trực giác sâu hơn: Tại sao hướng lại quan trọng?

Một hiểu nhầm phổ biến là chỉ cần biết vị trí không trơn là đủ. Xét hai phân phối trên $$ \mathbb{R}^2 $$:
- $$ u_1(x_1, x_2) = H(x_1) $$ (hàm bước theo $$ x_1 $$)
- $$ u_2(x_1, x_2) = H(x_2) $$ (hàm bước theo $$ x_2 $$)

Cả hai đều có giá kỳ dị là một đường thẳng đi qua gốc tọa độ, nhưng tập mặt sóng của chúng hoàn toàn khác nhau:
$$
WF(u_1) \subset \{x_1 = 0\} \times \{(\xi_1, 0) : \xi_1 \neq 0\},
\quad
WF(u_2) \subset \{x_2 = 0\} \times \{(0, \xi_2) : \xi_2 \neq 0\}.
$$
Dưới tác động của một PDE hyperbolic, hai kỳ dị này sẽ lan truyền theo hai quỹ đạo khác hẳn nhau. Giá kỳ dị không phân biệt được sự khác nhau về hướng này, còn tập mặt sóng thì có.

---

## Trực quan hóa bằng Python

Đoạn mã dưới đây minh họa ba ví dụ cốt lõi của tập mặt sóng: hàm trơn, phân phối delta Dirac và hàm bước. Với mỗi trường hợp, ta tính và hiển thị phổ Fourier sau khi cắt cục bộ để quan sát sự suy giảm theo từng hướng.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# -------------------------------------------------------
# Thiết lập lưới không gian và tần số
# -------------------------------------------------------
N = 512
x = np.linspace(-4, 4, N)
y = np.linspace(-4, 4, N)
X, Y = np.meshgrid(x, y)
dx = x[1] - x[0]

# Hàm cắt trơn Gaussian (localization function phi)
def phi(X, Y, x0=0, y0=0, sigma=0.8):
    return np.exp(-((X - x0)**2 + (Y - y0)**2) / (2 * sigma**2))

# Lưới tần số
freq = np.fft.fftfreq(N, d=dx)
FX, FY = np.meshgrid(freq, freq)
F_magnitude = np.sqrt(FX**2 + FY**2)
F_magnitude[F_magnitude == 0] = 1e-10  # Tránh chia cho 0

# -------------------------------------------------------
# Ba hàm cần kiểm tra
# -------------------------------------------------------
phi_loc = phi(X, Y)  # Hàm cắt cục bộ gần gốc tọa độ

# 1. Hàm trơn: Gaussian
u_smooth = np.exp(-(X**2 + Y**2) / 0.5)
u1_localized = phi_loc * u_smooth

# 2. Delta Dirac (xấp xỉ bằng Gaussian hẹp)
u_delta = np.exp(-(X**2 + Y**2) / 0.01) / (0.01 * np.pi)
u2_localized = phi_loc * u_delta

# 3. Hàm bước theo x1 (Heaviside)
u_step = (X > 0).astype(float)
u3_localized = phi_loc * u_step

# -------------------------------------------------------
# Tính phổ Fourier 2D (lấy giá trị tuyệt đối)
# -------------------------------------------------------
def compute_spectrum(u):
    return np.abs(np.fft.fftshift(np.fft.fft2(u)))

spec1 = compute_spectrum(u1_localized)
spec2 = compute_spectrum(u2_localized)
spec3 = compute_spectrum(u3_localized)

# -------------------------------------------------------
# Vẽ hình
# -------------------------------------------------------
fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

titles = ["Hàm trơn (Gaussian)", "Delta Dirac (xấp xỉ)", "Hàm bước H(x₁)"]
functions = [u_smooth, u_delta, u_step]
spectra = [spec1, spec2, spec3]
wf_descriptions = [
    "WF(u) = ∅\n(không có kỳ dị)",
    "WF(u) tại (0,ξ), ξ≠0\n(kỳ dị mọi hướng)",
    "WF(u) theo hướng ξ₁\n(kỳ dị pháp tuyến mặt nhảy)"
]

for i, (title, f, spec, wf) in enumerate(zip(titles, functions, spectra, wf_descriptions)):
    # Hàm gốc
    ax_f = fig.add_subplot(gs[0, i])
    im = ax_f.pcolormesh(X, Y, f, cmap='RdBu_r', shading='auto',
                          vmin=-np.percentile(np.abs(f), 99),
                          vmax=np.percentile(np.abs(f), 99))
    ax_f.set_title(title, fontsize=11, fontweight='bold')
    ax_f.set_xlabel("x₁"); ax_f.set_ylabel("x₂")
    ax_f.set_xlim(-3, 3); ax_f.set_ylim(-3, 3)
    ax_f.set_aspect('equal')
    plt.colorbar(im, ax=ax_f, shrink=0.8)

    # Phổ Fourier (sau cắt cục bộ)
    ax_s = fig.add_subplot(gs[1, i])
    freq_range = 50  # Hiển thị tần số thấp đến trung bình
    center = N // 2
    spec_crop = spec[center-freq_range:center+freq_range,
                     center-freq_range:center+freq_range]
    ax_s.imshow(np.log1p(spec_crop), cmap='hot', origin='lower',
                extent=[-freq_range, freq_range, -freq_range, freq_range])
    ax_s.set_title(f"Phổ Fourier (cục bộ)\n{wf}", fontsize=9)
    ax_s.set_xlabel("ξ₁ (tần số)"); ax_s.set_ylabel("ξ₂ (tần số)")

plt.suptitle("Wave Front Set: So sánh ba ví dụ cốt lõi\n"
             "(Hàng trên: hàm gốc — Hàng dưới: phổ Fourier sau cắt cục bộ)",
             fontsize=13, fontweight='bold', y=1.02)
plt.savefig("wave_front_set_comparison.png", dpi=150, bbox_inches='tight')
plt.show()
print("Quan sát: Hàm trơn → phổ giảm nhanh mọi hướng (WF rỗng).")
print("          Delta Dirac → phổ gần hằng số mọi hướng (WF đầy đủ).")
print("          Hàm bước → phổ tập trung theo trục ξ₁ (WF theo hướng pháp tuyến).")
```

### Minh họa bổ sung: Tập mặt sóng theo hướng (dạng 1D)

```python
import numpy as np
import matplotlib.pyplot as plt

# Kiểm tra sự suy giảm Fourier theo từng hướng theta
N = 1024
x = np.linspace(-6, 6, N)
dx = x[1] - x[0]

# Hàm cắt cục bộ
phi_1d = np.exp(-x**2 / (2 * 0.5**2))

# Hai hàm trong 1D
u_smooth = np.exp(-x**2)           # Trơn: WF rỗng
u_step   = (x > 0).astype(float)   # Bước: WF tại (0, ξ≠0)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, u, label, color in zip(axes,
                                 [u_smooth, u_step],
                                 ["Hàm trơn", "Hàm bước H(x)"],
                                 ["steelblue", "crimson"]):
    u_loc = phi_1d * u
    freqs = np.fft.fftfreq(N, d=dx)
    spec  = np.abs(np.fft.fft(u_loc))
    # Chỉ lấy nửa dương
    pos   = freqs > 0
    ax.loglog(freqs[pos], spec[pos], color=color, linewidth=2, label=label)
    # Đường tham chiếu suy giảm nhanh (Schwartz)
    xi_ref = freqs[pos]
    ax.loglog(xi_ref, 1e2 * xi_ref**(-4), 'k--', alpha=0.5, label=r"$|\xi|^{-4}$ (suy giảm nhanh)")
    ax.loglog(xi_ref, 5e1 * xi_ref**(-1), 'k:', alpha=0.5, label=r"$|\xi|^{-1}$ (suy giảm chậm)")
    ax.set_xlabel(r"$|\xi|$ (tần số)", fontsize=12)
    ax.set_ylabel(r"$|\widehat{\varphi u}(\xi)|$", fontsize=12)
    ax.set_title(f"{label}\nPhổ Fourier sau cắt cục bộ", fontsize=11, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0.5, N/(2*6)])

plt.suptitle("Kiểm tra suy giảm Fourier: Nhanh → WF rỗng, Chậm → có singularity",
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("wf_decay_comparison.png", dpi=150)
plt.show()
```

---

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

**Trực giác:** Một hàm có thể trơn theo một số hướng và không trơn theo những hướng khác; tập mặt sóng đo lường chính xác sự phân biệt đó.

**Điều cần nhớ:**
- Tập mặt sóng được định nghĩa trên không gian pha $$ (x, \xi) $$, kết hợp vị trí và hướng tần số.
- Nếu $$ \hat{\varphi u}(\xi) \to 0 $$ nhanh khi $$ \lvert \xi\rvert \to \infty $$ trong một nón quanh $$ \xi_0 $$, thì $$ (x_0, \xi_0) \notin WF(u) $$.
- Ba ví dụ mẫu cần nắm chắc: hàm trơn (tập mặt sóng rỗng), delta Dirac (kỳ dị mọi hướng tại gốc), hàm bước (kỳ dị theo hướng pháp tuyến).

**Bài tập khởi động:** Cho một ảnh nhị phân có biên thẳng đứng. Hãy mô tả giá kỳ dị và tập mặt sóng của hàm cường độ ảnh. Nếu xoay ảnh đi 45 độ, tập mặt sóng thay đổi như thế nào?

### Mức sau đại học (Graduate)

**Lý thuyết sâu hơn:** Tập mặt sóng có nhiều định nghĩa tương đương: qua tốc độ suy giảm Fourier cục bộ, qua biến đổi FBI (Fourier–Bros–Iagolnitzer), hoặc phiên bản giải tích qua tập mặt sóng giải tích (định nghĩa Sato). Mỗi cách tiếp cận mở ra một nhánh lý thuyết riêng.

**Tính chất quan trọng:**
1. **Phép chiếu:** $$ \pi_x(WF(u)) = \text{sing supp}(u) $$.
2. **Phép vi phân:** Nếu $$ P $$ là toán tử vi phân bậc $$ m $$, thì $$ WF(Pu) \subset WF(u) $$.
3. **Phép nhân:** $$WF(uv) \subset WF(u) \cup WF(v) \cup (WF(u) + WF(v))$$ (với điều kiện tổng hai hướng đối ngẫu không triệt tiêu).
4. **Tính chính quy elliptic:** Nếu $$ P $$ elliptic tại $$ (x_0, \xi_0) $$ thì $$ (x_0, \xi_0) \notin WF(u) $$ mỗi khi $$ (x_0, \xi_0) \notin WF(Pu) $$.

**Kết nối lý thuyết:** Tập mặt sóng là tiền đề để định nghĩa tính elliptic vi địa phương, xây dựng parametrix vi địa phương và chứng minh định lý lan truyền kỳ dị của Hörmander.

**Bài tập nâng cao:** Chứng minh rằng nếu $$ \varphi \in C^\infty_c $$ và $$ u \in \mathcal{D}' $$, thì $$ WF(\varphi u) \subset WF(u) $$. Từ đó suy ra phép nhân với hàm trơn không tạo thêm kỳ dị vi địa phương mới (và giữ nguyên tập mặt sóng tại các điểm mà $$ \varphi(x) \neq 0 $$).

---

## Liên kết với các khái niệm khác trong khóa học

| Khái niệm đã học | Kết nối với Tập mặt sóng |
|---|---|
| Phân phối (Ch. 12) | Tập mặt sóng là bước tinh chỉnh có hướng của giá kỳ dị phân phối |
| Biến đổi Fourier (Ch. 8, 14) | Định nghĩa tập mặt sóng dựa trên tốc độ suy giảm Fourier cục bộ |
| Phương trình elliptic (Ch. 11, 14) | Tính chính quy elliptic: toán tử elliptic không tạo thêm kỳ dị trong tập mặt sóng |
| Phương trình sóng (Ch. 10) | Tập mặt sóng lan truyền dọc theo các đường song đặc trưng (bài tiếp theo) |
| Bài toán ngược (Bài 15.06) | Tập mặt sóng xác định phần thông tin nào có thể tái tạo được |

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Ảnh CT và phát hiện biên
- Bài toán: Trong ảnh y khoa, không chỉ vị trí mà cả hướng của các đường biên đều rất quan trọng.
- Mô hình: Tập mặt sóng $$ WF(u) $$ ghi nhận đồng thời vị trí $$ x $$ và hướng tần số $$ \xi $$ của kỳ dị.
- Giả thiết và giới hạn: Đây là mô hình vi địa phương liên tục, bổ trợ chứ không thay thế trực tiếp thuật toán xử lý ảnh rời rạc.
- Diễn giải: Hai kỳ dị nằm tại cùng một vị trí nhưng khác hướng vẫn được tách biệt rõ ràng trong $$ WF(u) $$.

#### Địa chấn và phản xạ sóng
- Bài toán: Từ dữ liệu sóng phản xạ, cần xác định cả vị trí lẫn hướng pháp tuyến của các mặt phân cách địa tầng trong lòng đất.
- Mô hình: Kỳ dị của tham số môi trường và dữ liệu đo được mô tả bằng tập mặt sóng.
- Giả thiết và giới hạn: Dựa trên mô hình truyền sóng tuyến tính và điều kiện khả kiến của cấu trúc.
- Diễn giải: Tập mặt sóng cho biết chính xác phần cấu trúc nào thực sự được ghi nhận trong dữ liệu đo.

### 2. Trực giác bổ sung và các kết nối

Giá kỳ dị chỉ trả lời “không trơn ở đâu”, còn tập mặt sóng trả lời thêm “không trơn theo hướng nào”. Một biên thẳng, một góc nhọn và một nguồn điểm có thể nằm tại cùng một điểm nhưng sở hữu cấu trúc tần số rất khác nhau. Trong giải tích vi địa phương, kỳ dị luôn gắn với hướng.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

n = 128
x = np.linspace(-1, 1, n, endpoint=False)
X, Y = np.meshgrid(x, x)
u = (X > 0).astype(float)  # buoc nhay qua duong x = 0

U = np.fft.fftshift(np.abs(np.fft.fft2(u)))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(u, extent=[-1, 1, -1, 1], origin="lower", cmap="gray")
axes[0].set_title("Phan bo co singularity theo duong x = 0")
axes[1].imshow(np.log1p(U), cmap="magma")
axes[1].set_title("Do lon Fourier: huong tan so phap tuyen noi bat")
for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: wave front set edge orientation visualization
- search: singular support vs wave front set image processing
- search: seismic singularities wave front set intuition

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Wave front set: vị trí và hướng kỳ dị" description="Thay đổi loại singularity và góc cạnh để quan sát các hướng kỳ dị nổi bật trong không gian tần số." path="interactives/chapter15/wave-front-set-vi.html" height="620px" %}

### 5. Bài toán mẫu có bối cảnh thực

Cho hàm bậc thang
$$ u(x_1,x_2)=H(x_1). $$
Kỳ dị nằm trên đường thẳng $$ x_1=0 $$ nhưng chỉ xuất hiện theo các hướng pháp tuyến với đường nhảy, tức các vectơ $$ \xi $$ song song với trục $$ x_1 $$. Như vậy $$ WF(u) $$ không chỉ xác định trục tung là tập kỳ dị mà còn chỉ rõ hướng pháp tuyến gắn với biên.

### 6. Phân tầng độ khó

**Bậc đại học.** Phân biệt giá kỳ dị và tập mặt sóng qua các ví dụ delta Dirac, hàm bước và hàm trơn.

**Bậc sau đại học.** Kết nối với định nghĩa hình nón trên bó đối tiếp tuyến, phép kéo ngược/đẩy tới (pullback/pushforward) và tính bất biến dưới phép đổi tọa độ.

## Video tham khảo

- Nên xem trước: [Andras Vasy - Microlocal analysis and wave propagation (Part 1)](https://www.youtube.com/watch?v=P9uB6J2trvM) — Institut Fourier, tiếng Anh. Giới thiệu tập mặt sóng khi phân tích vị trí kỳ dị của phân phối trong không gian pha.
- [Andras Vasy - Microlocal analysis and wave propagation (Part 2)](https://www.youtube.com/watch?v=3DN6bKJnlXc) — Institut Fourier, tiếng Anh. Phần 2 tiếp tục khảo sát mô tả vi địa phương của điểm kỳ dị.
- [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Bài giảng của Maciej Zworski về các phương pháp vi địa phương.
