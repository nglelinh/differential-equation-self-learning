---
layout: post
title: "Tiệm Cận Phổ"
chapter: '15'
order: 5
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter15
lesson_type: optional
---

![Asymptotics của phổ và đếm eigenvalue]({{ site.imgurl }}/chapter_img/chapter15/05_spectral_asymptotics.svg )

Năm 1911, Hermann Weyl chứng minh một định lý khiến giới vật lý và toán học kinh ngạc: nếu bạn chỉ được nghe toàn bộ danh sách các tần số dao động riêng $\lambda_1 \le \lambda_2 \le \dots$ của một mặt trống phẳng $\Omega$ mà **không hề nhìn thấy hình dạng của nó**, bạn vẫn có thể tính chính xác **diện tích** của cái trống! Công thức đếm $N(\lambda) \sim \frac{\operatorname{Area}(\Omega)}{4\pi}\lambda$—**Định luật Weyl**—là viên ngọc mở đầu cho **Tiệm cận Phổ (Spectral Asymptotics)**, nơi giải tích vi địa phương đọc ra hình học của không gian từ âm thanh của nó!

## Kiến thức cần nhớ: Bốn trụ cột của Tiệm cận Phổ & Định luật Weyl

1. **Hàm Đếm Giá trị riêng $N(\lambda) = \#\{k : \lambda_k \le \lambda\}$ và Thể tích Không gian Pha**:
   Theo nguyên lý bán cổ điển, mỗi trạng thái lượng tử chiếm đúng một ô thể tích $(2\pi)^n$ trong không gian pha $T^*\Omega$. Do đó số giá trị riêng $\le \lambda$ của $-\Delta$ tiệm cận bằng thể tích vùng $\{(x, \xi) \in T^*\Omega : |\xi|^2 \le \lambda\}$ chia cho $(2\pi)^n$:
   $$N(\lambda) \sim \frac{\omega_n \operatorname{Vol}(\Omega)}{(2\pi)^n}\,\lambda^{n/2}.$$
2. **Số hạng Hiệu chỉnh Biên (Biên Dirichlet vs. Biên Neumann)**:
   Giả thuyết Weyl (được Ivrii chứng minh năm 1980 dưới điều kiện tia phản xạ tuần hoàn có độ đo $0$) cho biết số hạng bậc hai tiết lộ luôn **chu vi** $|\partial\Omega|$: dấu **trừ** cho biên Dirichlet ($-\frac{|\partial\Omega|}{4\pi}\sqrt{\lambda}$ ở 2D) và dấu **cộng** cho biên Neumann!
3. **Hai công cụ chứng minh: Vết Nhân Nhiệt (Tauberian) vs. Vết Sóng (FIO)**:
   Dùng vết nhiệt $\operatorname{Tr}(e^{t\Delta}) = \sum e^{-t\lambda_k}$ cho nhanh số hạng chính (nhưng phần dư yếu); dùng vết sóng $\operatorname{Tr}(e^{it\sqrt{-\Delta}})$ bằng FIO (Hörmander 1968) cho phần dư sắc bén $O(\lambda^{(n-1)/2})$!
4. **Câu hỏi Mark Kac (1966): "Có nghe được hình dáng cái trống không?"**:
   Phổ cho biết diện tích, chu vi, thậm chí số lỗ thủng (đặc trưng Euler)—nhưng năm 1992, Gordon, Webb và Wolpert đã dựng hai đa giác khác nhau có phổ giống hệt nhau: ta nghe được *rất nhiều* hình học, nhưng không phải toàn bộ!

## Mục tiêu

Bài học tùy chọn này giới thiệu tiệm cận phổ (spectral asymptotics), trọng tâm là định luật Weyl, như cầu nối giữa phổ năng lượng cao, hình học và giải tích vi địa phương. Sau bài học, sinh viên cần hiểu ý nghĩa của hàm đếm trị riêng, trực giác của định luật Weyl, và lý do phổ năng lượng cao phản ánh thể tích không gian pha chứ không chỉ là một dãy số rời rạc.

## Kiến thức nền

Sinh viên nên nắm bài toán trị riêng, toán tử Laplace, không gian Hilbert và trực giác bán cổ điển rằng trị riêng lớn tương ứng với tần số cao. Kiến thức về lý thuyết phổ từ Chương 12 là nền tảng trực tiếp cho bài học này.

## Dẫn nhập

Khi xét từng trị riêng riêng lẻ, phổ toán tử có vẻ như một dãy số phức tạp. Tuy nhiên, ở quy mô năng lượng lớn, một quy luật hình học rõ rệt xuất hiện: số lượng trị riêng nhỏ hơn một ngưỡng cao tăng theo một hàm lũy thừa phụ thuộc trực tiếp vào số chiều không gian và bậc của toán tử. Đó là nội dung của tiệm cận phổ.

Điểm đáng chú ý là phổ không chỉ mô tả các tần số dao động mà còn mã hóa thông tin về hình học miền, metric và thể tích không gian pha, đặt bài toán phổ vào giao điểm của PDE, hình học và vật lý.


### Giải thích: Kiểm chứng số trực tiếp Định luật Weyl (2 số hạng) trên hình vuông $[0, \pi]^2$

Xét bài toán Dirichlet $-\Delta u = \lambda u$ trên hình vuông $\Omega = [0, \pi]^2$ (Diện tích $= \pi^2$, Chu vi $= 4\pi$). Các giá trị riêng chính xác là $\lambda_{m, n} = m^2 + n^2$ với $m, n \in \mathbb{Z}_{\ge 1}$. Hãy đếm $N(100)$ (số cặp nguyên dương thỏa mãn $m^2 + n^2 \le 100$):
1. **Đếm tay chính xác**:
   - $m = 1, 2, 3, 4$: mỗi hàng có $9$ giá trị $n$ ($4 \times 9 = 36$).
   - $m = 5, 6$: mỗi hàng có $8$ giá trị $n$ ($2 \times 8 = 16$).
   - $m = 7$: $7$ giá trị ($7^2 + 7^2 = 98 \le 100$); $m = 8$: $6$ giá trị; $m = 9$: $4$ giá trị.
   - **Tổng chính xác**: $N(100) = 36 + 16 + 7 + 6 + 4 = \mathbf{69}$.
2. **Dự đoán bằng Định luật Weyl 2 số hạng** (biên Dirichlet có dấu trừ):
   $$N_{\text{Weyl}}(100) = \frac{\operatorname{Area}}{4\pi}\lambda - \frac{\operatorname{Perimeter}}{4\pi}\sqrt{\lambda} = \frac{\pi^2}{4\pi}(100) - \frac{4\pi}{4\pi}(10) = 25\pi - 10 \approx 78{,}54 - 10 = \mathbf{68{,}54}!$$
   Sai lệch chưa tới **$0{,}5$ giá trị riêng** trên tổng số $69$—một độ chính xác đáng kinh ngạc!
## Khái niệm theo ba cách

### Cách trực giác

Hãy liên tưởng đến một nhạc cụ: từng nốt riêng lẻ mang âm sắc khác nhau, nhưng khi xét mật độ của dãy tần số ở vùng âm cao, ta nhận ra mật độ đó phản ánh trực tiếp kích thước và hình dáng của nhạc cụ. Định luật Weyl là phát biểu toán học chính xác cho trực giác đó.

### Cách hình ảnh

Có thể vẽ đồ thị hàm đếm trị riêng $$ N(\lambda) $$ — số lượng trị riêng nhỏ hơn hoặc bằng $$ \lambda $$ — rồi so sánh trên miền một chiều, hai chiều và ba chiều để thấy số chiều quyết định trực tiếp tốc độ tăng trưởng của $$ N(\lambda) $$.

### Cách hình thức

Nếu $$ N(\lambda) $$ là số trị riêng (kể cả bội) không vượt quá $$ \lambda $$ của một toán tử elliptic bậc $$ m $$ (tự liên hợp, dương), thì trong nhiều bối cảnh chuẩn ta có $$ N(\lambda)\sim C\lambda^{n/m} $$ khi $$ \lambda\to\infty $$, trong đó $$ n $$ là số chiều không gian và $$ C $$ là hằng số hình học gắn với thể tích không gian pha. Đây là nội dung cốt lõi của định luật Weyl.

## Ngộ nhận thường gặp

### “Phổ năng lượng cao chỉ là bài toán đếm số thuần túy”

Sai. Phân bố trị riêng bậc cao mã hóa các bất biến hình học quan trọng của miền hoặc đa tạp.

### “Định luật Weyl xác định chính xác từng trị riêng”

Không đúng. Định luật chỉ mô tả tốc độ tăng trưởng tiệm cận trung bình của hàm đếm.

### “Hằng số $$ C $$ chỉ là hệ số kỹ thuật”

Không phải. Hằng số này trực tiếp chứa thể tích miền hoặc thể tích vùng tương ứng trong không gian pha.

### “Hai miền có cùng phổ thì nhất thiết phải đồng dạng”

Không nhất thiết. Thực tế tồn tại những cặp miền không đẳng cự nhưng đẳng phổ — đây là điểm xuất phát của các bài toán phổ ngược.

## Tiến trình học

### Bước 1: Ôn tập hàm đếm trị riêng

Nắm chắc định nghĩa và ý nghĩa của $$ N(\lambda) $$ trước khi xét giới hạn tiệm cận.

### Bước 2: Khảo sát ví dụ số chiều thấp

Bắt đầu từ bài toán một chiều để dễ tính toán trực tiếp.

### Bước 3: Phát biểu định luật Weyl

Làm rõ vai trò của số chiều $$ n $$ và bậc toán tử $$ m $$ trong số mũ $$ n/m $$.

### Bước 4: Liên hệ với giải tích bán cổ điển

Nhìn nhận giới hạn phổ cao tương đương với giới hạn bán cổ điển $$ h\to 0 $$.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được định nghĩa của $$ N(\lambda) $$ hay không?
- Sinh viên có nêu được vì sao số chiều xuất hiện trong số mũ $$ n/m $$ hay không?
- Sinh viên có hiểu mối liên hệ giữa tiệm cận phổ và hình học miền hay không?

## Ví dụ có lời giải

### Ví dụ 1: Đoạn $$ [0,\pi] $$

Với toán tử Laplace có điều kiện biên Dirichlet trên $$ [0,\pi] $$, các trị riêng là $$ \lambda_k=k^2 $$. Điều kiện $$ \lambda_k\le \lambda $$ tương đương $$ k\le \sqrt{\lambda} $$, suy ra $$ N(\lambda)\sim \sqrt{\lambda} $$. Kết quả này khớp đúng với trường hợp $$ n=1,m=2 $$.

### Ví dụ 2: Ý nghĩa của số mũ $$ n/m $$

Khi số chiều không gian tăng, số mode dao động độc lập nằm dưới cùng một ngưỡng năng lượng tăng nhanh hơn nhiều — đó là lý do số chiều $$ n $$ xuất hiện ở tử số của số mũ $$ n/m $$.

### Ví dụ 3: Toán tử Laplace trên miền phẳng

Trong hai chiều, định luật Weyl cho toán tử Laplace có dạng

$$
N(\lambda)\sim C\,\operatorname{Area}(\Omega)\,\lambda.
$$

Công thức cho thấy diện tích miền xuất hiện trực tiếp ngay trong số hạng dẫn đầu.

### Ví dụ 4: Bài toán “có thể nghe ra hình dạng chiếc trống không?”

Hai miền có thể sở hữu cùng dãy trị riêng nhưng không đồng dạng với nhau. Điều này cho thấy phổ chứa nhiều thông tin hình học quan trọng (như diện tích, chu vi) nhưng chưa đủ để xác định duy nhất toàn bộ hình dạng.

### Ví dụ 5: Diễn giải định luật Weyl qua thể tích không gian pha

Nếu xem tập các cặp $$ \left(x,\xi\right) $$ thỏa $$ \lvert \xi\rvert^2\le \lambda $$ như vùng năng lượng khả dĩ trong không gian pha, định luật Weyl khẳng định số mode dưới ngưỡng $$ \lambda $$ tiệm cận bằng thể tích của vùng đó sau khi chuẩn hóa theo hằng số $$ (2\pi)^n $$. Cách nhìn này nối trực tiếp tiệm cận phổ với giải tích bán cổ điển.

## Câu hỏi khái niệm

1. Vì sao phổ năng lượng cao phản ánh hình học miền rõ nét hơn so với vài trị riêng đầu tiên?
2. Vì sao định luật Weyl có thể xem là một phát biểu về thể tích không gian pha chứ không chỉ không gian vật lý?
3. Vì sao biết tiệm cận hàm đếm trị riêng vẫn chưa đủ để khôi phục hoàn toàn hình dạng miền?

## Bài toán ứng dụng

1. Trong dao động cơ học, mật độ mode ở tần số cao liên hệ thế nào với kích thước và hình dạng kết cấu?
2. Trong cơ học lượng tử, vì sao số mức năng lượng cao gắn liền với thể tích pha cổ điển?
3. Trong hình học phổ, câu hỏi “có thể nghe ra hình dạng chiếc trống không?” phản ánh giới hạn gì của dữ liệu phổ?

## Chiến lược dạy học tương tác

### Câu hỏi nên đặt trên lớp

- Nếu mở rộng kích thước miền, số trị riêng dưới cùng một ngưỡng năng lượng sẽ tăng hay giảm?
- Vì sao các tần số cao lại phản ánh được các đặc trưng hình học lớn như diện tích hay thể tích?
- Một công thức tiệm cận cho biết bao nhiêu thông tin về hình dạng thực của miền?

### Hoạt động gợi ý

- Cho sinh viên tự đếm trị riêng trên một đoạn một chiều và trên hình chữ nhật hai chiều.
- So sánh đồ thị $$ N(\lambda) $$ ứng với các số chiều khác nhau.
- Thảo luận nhóm về ý nghĩa vật lý của hàm đếm trị riêng.

### Cách tăng mức độ tham gia

- Bắt đầu từ ví dụ nhạc cụ hoặc dao động màng trống quen thuộc.
- Đề nghị sinh viên dự đoán mối liên hệ giữa kích thước miền và mật độ phổ trước khi viết công thức.
- Mời sinh viên diễn đạt nội dung định luật Weyl bằng ngôn ngữ trực quan.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám sát ví dụ một chiều $$ \lambda_k=k^2 $$.
- Minh họa bằng đồ thị hàm bậc thang trước khi nói đến chứng minh.
- Nhấn mạnh ý cốt lõi: số lượng trị riêng bậc cao tuân theo quy luật hình học.

### Thử thách cho sinh viên khá giỏi

- Liên hệ định luật Weyl với thể tích không gian pha bán cổ điển.
- Tìm hiểu ước lượng phần dư trong tiệm cận Weyl.
- Khảo sát trực giác về bài toán phổ ngược và hỗn loạn lượng tử (quantum chaos).

## Ghi nhớ nhanh

Tiệm cận phổ nghiên cứu tốc độ tăng của hàm đếm trị riêng khi ngưỡng năng lượng tiến ra vô cực. Định luật Weyl cho thấy phân bố phổ cao phản ánh trực tiếp số chiều, bậc toán tử và hình học không gian pha của miền khảo sát.

---

## Ứng dụng thực tế

### 1. Dao động kết cấu và mật độ mode

Trong cơ học kết cấu, các tần số dao động riêng xuất phát từ bài toán trị riêng $$ L u = \lambda u $$, với $$ L $$ là toán tử elliptic mô tả độ cứng và hình học kết cấu (dưới giả thiết vật liệu tuyến tính và dao động nhỏ). Ngoài từng tần số riêng lẻ, kỹ sư còn cần biết mật độ mode trong một dải tần; định luật Weyl cho thấy ở dải tần cao, mật độ này chủ yếu phụ thuộc vào kích thước, số chiều và hình học tổng thể.

### 2. Mật độ trạng thái trong cơ học lượng tử

Với toán tử Hamilton lượng tử có phổ rời rạc, hàm đếm mức năng lượng cho biết số trạng thái lượng tử nằm dưới một ngưỡng năng lượng cho trước. Ở giới hạn năng lượng cao, đại lượng này xấp xỉ thể tích vùng khả dĩ trong không gian pha cổ điển; các hiệu ứng đối xứng tinh vi và dao động phần dư nằm ở những số hạng bậc thấp hơn.

### 3. Âm học phòng và thiết kế nhạc cụ

Các tần số cộng hưởng trong phòng hoặc khoang nhạc cụ được xác định bởi trị riêng của toán tử Laplace cùng điều kiện biên tương ứng. Ở dải tần cao, mật độ mode phản ánh thể tích khoang cộng hưởng nhiều hơn là các chi tiết hình học nhỏ (khi bỏ qua tiêu hao và hiệu ứng phi tuyến), cho biết không gian đó hỗ trợ bao nhiêu dao động độc lập.

## Trực giác sâu hơn

Định luật Weyl không đơn thuần là công thức đếm trị riêng mà diễn đạt nguyên lý rằng khi năng lượng lớn, số trạng thái dao động tỷ lệ với thể tích vùng tương ứng trong không gian pha. Số hạng dẫn đầu mô tả xu thế chung, còn các thông tin hình học tinh vi hơn (như diện tích biên hay quỹ đạo tuần hoàn) ẩn trong phần dư bậc thấp hơn.

## Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

k = np.arange(1, 300)
lam = k**2
grid = np.linspace(1, lam[-1], 600)
N = np.array([np.sum(lam <= val) for val in grid])

plt.figure(figsize=(8, 5))
plt.plot(grid, N, label='Hàm đếm chính xác')
plt.plot(grid, np.sqrt(grid), '--', label='Tiệm cận Weyl trong 1D')
plt.xlabel('lambda')
plt.ylabel('N(lambda)')
plt.title('Laplacian Dirichlet trên [0, pi]')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

## Trực quan hóa bằng JavaScript

Có thể dùng `Plotly.js` để vẽ đồng thời đồ thị bậc thang $$ N(\lambda) $$ và đường tiệm cận $$ \sqrt{\lambda} $$, sau đó cho phép chuyển từ 1D sang 2D để quan sát trực tiếp sự thay đổi bậc tăng trưởng.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Weyl law visualization`, `eigenvalue counting function Laplacian`, hoặc `density of states geometry`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào các ví dụ trên đoạn thẳng và hình chữ nhật, nơi có thể tính tường minh trị riêng rồi đối chiếu trực tiếp với luật tăng trưởng.

### Mức sau đại học (Graduate)

Đi sâu vào chứng minh qua thể tích pha, lập luận Tauberian, ước lượng phần dư Weyl, công thức vết (trace formulas) và mối liên hệ với hình học phổ hay hỗn loạn lượng tử.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tần số của trống và buồng cộng hưởng
- Bài toán: Số mode dao động dưới ngưỡng năng lượng $$ \lambda $$ tăng theo quy luật gắn với hình học miền.
- Mô hình: Hàm đếm trị riêng
$$ N(\lambda)=\#\{\lambda_j\le \lambda\} $$
tuân theo tiệm cận kiểu Weyl.
- Giả thiết và giới hạn: Phần dư phụ thuộc thêm vào hình học biên, tính đối xứng và động lực học trắc địa.
- Diễn giải: Tiệm cận phổ kết nối phổ rời rạc với thể tích không gian pha.

#### Mức năng lượng trong hệ lượng tử
- Bài toán: Đếm số mức năng lượng dưới một ngưỡng cho toán tử Schrödinger hoặc Laplace–Beltrami.
- Mô hình: Sử dụng công thức tiệm cận phổ hoặc công thức vết.
- Giả thiết và giới hạn: Cần chế độ bán cổ điển hoặc miền đủ đều.
- Diễn giải: Phân bố phổ ẩn chứa cấu trúc hình học rõ ràng thay vì ngẫu nhiên.

### 2. Trực giác bổ sung và các kết nối

Tiệm cận phổ khảo sát phân bố trị riêng ở miền năng lượng lớn với trực giác cốt lõi rằng mỗi ô thể tích đơn vị trong không gian pha tương ứng xấp xỉ một trạng thái lượng tử. Cần tránh suy đoán toàn bộ phổ chỉ từ vài trị riêng đầu tiên, vì quy luật tiệm cận chỉ thể hiện rõ ở chế độ năng lượng cao.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

lam = np.linspace(1, 400, 400)
N_exact = np.floor(np.sqrt(lam) / np.pi)
N_weyl = np.sqrt(lam) / np.pi

plt.plot(lam, N_exact, label="N(lambda) exact tren [0,1]")
plt.plot(lam, N_weyl, "--", label="xap xi Weyl")
plt.legend()
plt.title("Spectral asymptotics tren doan")
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Weyl law visualization drum frequencies
- search: spectral asymptotics interval eigenvalue counting
- search: quantum chaos Weyl law intuition

### 4a. Minh họa tương tác trên web

{% include interactive-frame.html title="Tiệm cận phổ và định luật Weyl" description="So sánh hàm đếm trị riêng chính xác với đường tiệm cận Weyl khi thay đổi số chiều và kích thước miền." path="interactives/chapter15/weyl-law-vi.html" height="700px" %}

### 5. Bài toán mẫu có bối cảnh thực

Trên đoạn $$ [0,1] $$ với điều kiện biên Dirichlet,
$$ \lambda_n = n^2\pi^2. $$
Do đó
$$
N(\lambda)=\max\{n: n^2\pi^2\le \lambda\}=\left\lfloor \frac{\sqrt{\lambda}}{\pi}\right\rfloor.
$$
Định luật Weyl khẳng định khi $$ \lambda \to \infty $$,
$$ N(\lambda)\sim \frac{\sqrt{\lambda}}{\pi}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Đếm mode trong các miền đơn giản và đối chiếu với quy luật tăng trưởng.

**Bậc sau đại học.** Kết nối với định luật Weyl, công thức vết, ước lượng phần dư và hình học phổ.

## Video tham khảo

- Nên xem trước: [Maciej Zworski - Microlocal methods for operators with analytic coefficients III](https://www.youtube.com/watch?v=9MbKr2z9fxs) — Erwin Schrödinger International Institute for Mathematics and Physics (ESI), tiếng Anh. Các phương pháp vi địa phương áp dụng cho các bài toán phổ.
- [Lecture 22: The Spectral Theorem for a Compact Self-Adjoint Operator](https://www.youtube.com/watch?v=-sfaHVFWBU8) — MIT OpenCourseWare, tiếng Anh. Định lý phổ cho toán tử compact tự liên hợp — cấu trúc trị riêng mà tiệm cận phổ tinh chỉnh.
- [Lecture 20: Compact Operators and the Spectrum of a Bounded Linear Operator on a Hilbert Space](https://www.youtube.com/watch?v=SFDMFbzCsH0) — MIT OpenCourseWare, tiếng Anh. Giới thiệu phổ của toán tử bị chặn, đối tượng mà tiệm cận phổ khảo sát.
