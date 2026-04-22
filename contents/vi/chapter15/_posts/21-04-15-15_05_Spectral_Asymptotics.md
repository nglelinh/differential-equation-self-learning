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

## Mục tiêu

Bài optional này giới thiệu spectral asymptotics, đặc biệt là định luật Weyl, như cây cầu giữa phổ cao, hình học, và giải tích vi địa phương. Sau bài học, sinh viên cần hiểu ý nghĩa của hàm đếm trị riêng, trực giác của Weyl law, và vì sao phổ lớn phản ánh thể tích pha chứ không chỉ là một danh sách số.

## Kiến thức nền

Sinh viên nên nắm eigenvalue problems, Laplacian, không gian Hilbert, và trực giác semiclassical rằng trị riêng lớn tương ứng với tần số cao. Kiến thức từ chương 12 về spectral theory sẽ giúp bài này trở nên tự nhiên hơn.

## Dẫn nhập

Khi nhìn từng trị riêng riêng lẻ, phổ có vẻ như một dãy số bí ẩn. Nhưng khi nhìn ở thang lớn, một quy luật hình học xuất hiện: số lượng trị riêng dưới một mức năng lượng cao thường tăng theo một luật lũy thừa phụ thuộc vào số chiều và bậc của toán tử. Đây là spectral asymptotics.

Điều hấp dẫn ở đây là phổ không chỉ đo “dao động” mà còn chứa dấu vết của hình học miền, của metric, và của thể tích không gian pha. Đó là lý do câu hỏi phổ luôn đứng ở giao điểm của PDE, hình học, và vật lý.

## Khái niệm theo ba cách

### Cách trực giác

Hãy tưởng tượng một nhạc cụ. Các nốt riêng lẻ nghe rất khác nhau, nhưng khi nhìn toàn bộ dãy nốt cao dần, ta bắt đầu thấy mật độ của chúng phản ánh kích thước và hình dáng của nhạc cụ. Weyl law là phiên bản toán học của trực giác đó.

### Cách hình ảnh

Giáo viên nên vẽ hàm đếm $$ N(\lambda) $$ như số lượng eigenvalue nhỏ hơn hoặc bằng $$ \lambda $$. Sau đó so sánh các đồ thị trên miền một chiều, hai chiều, và ba chiều để sinh viên thấy số chiều ảnh hưởng trực tiếp đến tốc độ tăng của $$ N(\lambda) $$.

### Cách hình thức

Nếu $$ N(\lambda) $$ là số trị riêng của một toán tử elliptic bậc $$ m $$ nhỏ hơn hoặc bằng $$ \lambda $$, thì trong nhiều bối cảnh ta có $$ N(\lambda)\sim C\lambda^{n/m} $$ khi $$ \lambda\to\infty $$, với $$ n $$ là số chiều không gian và $$ C $$ là hằng số hình học liên quan đến thể tích pha. Đây là nội dung cốt lõi của định luật Weyl.

## Ngộ nhận thường gặp

### “Phổ lớn chỉ là chuyện đếm số”

Sai. Nó mã hóa thông tin hình học sâu sắc.

### “Weyl law cho biết từng trị riêng chính xác”

Không. Nó mô tả hành vi tiệm cận tổng quát của hàm đếm.

### “Hằng số $$ C $$ chỉ là hệ số kỹ thuật”

Không. Nó thường phản ánh thể tích của miền hay thể tích trong không gian pha.

### “Nếu hai miền có phổ gần giống thì chúng phải giống nhau”

Không nhất thiết. Đây chính là nguồn gốc của các bài toán inverse spectral hấp dẫn.

## Tiến trình học

### Bước 1: Ôn hàm đếm trị riêng

Sinh viên cần hiểu $$ N(\lambda) $$ trước khi nói về tiệm cận.

### Bước 2: Nhìn vài ví dụ thấp chiều

Miền một chiều là nơi trực giác dễ nhất.

### Bước 3: Giới thiệu Weyl law

Nhấn mạnh mối liên hệ với số chiều và bậc toán tử.

### Bước 4: Kết nối với semiclassical analysis

Phổ cao có thể đọc như giới hạn $$ h\to 0 $$.

### Các điểm kiểm tra hiểu bài

- Sinh viên có giải thích được $$ N(\lambda) $$ là gì không?
- Sinh viên có nêu được tại sao số chiều xuất hiện trong mũ $$ n/m $$ không?
- Sinh viên có hiểu vì sao spectral asymptotics gắn với hình học không?

## Ví dụ có lời giải

### Ví dụ 1: Đoạn $$ [0,\pi] $$

Với Laplacian Dirichlet trên $$ [0,\pi] $$, trị riêng là $$ \lambda_k=k^2 $$. Điều kiện $$ \lambda_k\le \lambda $$ tương đương $$ k\le \sqrt{\lambda} $$. Vì thế $$ N(\lambda)\sim \sqrt{\lambda} $$. Đây chính là trường hợp $$ n=1,m=2 $$.

### Ví dụ 2: Ý nghĩa của mũ $$ n/m $$

Nếu không gian có số chiều cao hơn, số mode độc lập dưới cùng một ngưỡng năng lượng tăng nhanh hơn. Đây là trực giác vì sao mũ chứa số chiều $$ n $$.

### Ví dụ 3: Laplacian trên miền phẳng

Trong hai chiều, Weyl law cho Laplacian có dạng

$$
N(\lambda)\sim C\,\operatorname{Area}(\Omega)\,\lambda.
$$

Ví dụ này cho thấy diện tích miền xuất hiện trực tiếp trong hằng số đầu.

### Ví dụ 4: Câu hỏi “nghe hình dạng cái trống”

Hai miền có thể có phổ rất giống nhau nhưng không đồng dạng. Ví dụ khái niệm này giúp sinh viên thấy spectral asymptotics giàu thông tin nhưng chưa phải là toàn bộ thông tin hình học.

### Ví dụ 5: Đọc định luật Weyl bằng thể tích pha

Nếu ta coi các cặp $$ \left(x,\xi\right) $$ thỏa $$ \lvert \xi\rvert^2\le \lambda $$ như vùng năng lượng cho phép trong không gian pha, thì định luật Weyl nói rằng số mode dưới ngưỡng $$ \lambda $$ gần bằng thể tích của vùng đó sau khi chuẩn hóa thích hợp. Đây là cách đọc hiện đại và rất hữu ích vì nó nối spectral asymptotics trực tiếp với trực giác semiclassical.

## Câu hỏi khái niệm

1. Vì sao phổ cao lại phản ánh hình học miền thay vì chỉ phụ thuộc vào vài trị riêng đầu?
2. Điều gì làm cho Weyl law là một mệnh đề về thể tích pha chứ không chỉ về không gian vật lý?
3. Tại sao biết tiệm cận của hàm đếm không đủ để khôi phục toàn bộ hình học?

## Bài toán ứng dụng

1. Trong dao động cơ học, mật độ mode cao liên hệ thế nào với kích thước và hình dạng cấu trúc?
2. Trong cơ học lượng tử, tại sao đếm mức năng lượng cao lại gắn với thể tích pha cổ điển?
3. Trong spectral geometry, câu hỏi “nghe được hình dạng của trống không?” gợi điều gì về giới hạn của dữ liệu phổ?

## Chiến lược dạy học tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu một miền lớn hơn, em mong số trị riêng dưới cùng một ngưỡng sẽ nhiều hơn hay ít hơn?
- Vì sao tần số cao có thể “thấy” hình học ở quy mô lớn?
- Một quy luật tiệm cận có thể nói được bao nhiêu về hình dạng thật sự của miền?

### Hoạt động gợi ý

- Cho sinh viên tự đếm trị riêng trên một đoạn một chiều.
- So sánh đồ thị $$ N(\lambda) $$ cho các số chiều khác nhau.
- Thảo luận nhóm về ý nghĩa vật lý của hàm đếm trị riêng.

### Cách tăng tham gia

- Bắt đầu từ nhạc cụ hay dao động mà sinh viên quen thuộc.
- Cho sinh viên dự đoán mối liên hệ giữa kích thước miền và mật độ phổ.
- Mời sinh viên kể lại Weyl law bằng ngôn ngữ đời thường.

## Phân hóa

### Hỗ trợ sinh viên gặp khó khăn

- Bám chặt vào ví dụ một chiều $$ \lambda_k=k^2 $$.
- Giải thích bằng đồ thị hàm đếm hơn là chứng minh.
- Nhấn mạnh thông điệp: trị riêng cao được đếm theo luật hình học.

### Thử thách cho sinh viên khá giỏi

- Liên hệ Weyl law với semiclassical phase-space volume.
- Tìm hiểu phần dư trong Weyl asymptotics.
- Khảo sát inverse spectral problems và quantum chaos ở mức trực giác.

## Ghi nhớ nhanh

Spectral asymptotics nghiên cứu cách hàm đếm trị riêng tăng khi ngưỡng năng lượng lớn dần. Định luật Weyl cho thấy phổ cao không ngẫu nhiên, mà phản ánh số chiều, bậc toán tử, và hình học của không gian hay miền xét.

---

## Ứng dụng thực tế

### 1. Dao động kết cấu và mật độ mode

Trong cơ học kết cấu, tần số dao động riêng được xác định bởi bài toán trị riêng $$ L u = \lambda u $$, với $$ L $$ là toán tử elliptic mô tả độ cứng và hình học của cấu trúc. Kỹ sư không chỉ quan tâm một trị riêng riêng lẻ, mà còn quan tâm có bao nhiêu mode nằm trong một dải tần nhất định. Mô hình này giả định vật liệu tuyến tính và dao động nhỏ. Diễn giải quan trọng của Weyl law là: ở dải tần cao, mật độ mode chủ yếu phản ánh kích thước, số chiều, và hình học lớn của cấu trúc.

### 2. Mật độ trạng thái trong cơ học lượng tử

Với Hamiltonian lượng tử có phổ rời rạc, hàm đếm mức năng lượng lớn cho biết số trạng thái lượng tử khả dĩ dưới một ngưỡng năng lượng. Trong giới hạn năng lượng cao, bài toán này gần với việc đếm thể tích pha cổ điển cho phép. Mô hình giả định hệ bị giam cầm đủ mạnh để có phổ rời rạc. Giới hạn của mô hình là phần dư phổ và các hiệu ứng đối xứng tinh tế không xuất hiện trong hạng đầu của tiệm cận.

### 3. Âm học phòng và thiết kế nhạc cụ

Các cộng hưởng âm thanh trong một khoang được điều khiển bởi trị riêng của Laplacian với điều kiện biên thích hợp. Với tần số cao, mật độ mode phản ánh thể tích phòng hay khoang cộng hưởng nhiều hơn là chi tiết cực nhỏ của hình dạng. Mô hình bỏ qua damping và các hiệu ứng phi tuyến của nguồn âm. Diễn giải là: phổ cao cho biết không gian đó “chứa được bao nhiêu dao động độc lập”.

## Trực giác sâu hơn

Weyl law không chỉ là một công thức đếm số. Nó là phát biểu rằng khi năng lượng tăng lớn, điều ta đang thật sự đếm là số trạng thái dao động khả dĩ trong không gian pha. Ngộ nhận thường gặp là nghĩ rằng tiệm cận sẽ dự đoán chính xác từng trị riêng. Không phải vậy: hạng đầu chỉ mô tả xu thế chung, còn thông tin tinh vi hơn nằm trong phần dư và dao động bậc thấp.

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

Có thể dùng `Plotly.js` để vẽ đồng thời đồ thị bậc thang của $$ N(\lambda) $$ và đường xấp xỉ $$ \sqrt{\lambda} $$, rồi cho sinh viên thay đổi bài toán từ 1D sang 2D để quan sát sự thay đổi của số mũ tăng trưởng.

## Gợi ý tài nguyên ngoài

Tìm kiếm: `Weyl law visualization`, `eigenvalue counting function Laplacian`, hoặc `density of states geometry`.

## Phân tầng theo mức độ

### Mức đại học (Undergraduate)

Tập trung vào các ví dụ trên đoạn và hình chữ nhật, nơi sinh viên có thể tự đếm trị riêng và so sánh với quy luật tăng trưởng.

### Mức sau đại học (Graduate)

Đi sâu vào chứng minh qua thể tích pha, Tauberian arguments, phần dư của Weyl law, trace formulas, và mối liên hệ với spectral geometry hay quantum chaos.

> Xem toàn bộ minh họa tương tác của chương tại: [Bộ Minh họa tương tác Chương 15]({{ site.baseurl }}/contents/vi/chapter15/15_10_Interactive_Gallery/)

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Tần số của trống và buồng cộng hưởng
- Bài toán: Số mode dao động dưới ngưỡng năng lượng $$ \lambda $$ tăng theo quy luật hình học của miền.
- Mô hình: Hàm đếm trị riêng
$$ N(\lambda)=\#\{\lambda_j\le \lambda\} $$
thỏa quy luật kiểu Weyl.
- Giả thiết và giới hạn: Phần dư còn phụ thuộc hình học biên, đối xứng và động lực học geodesic.
- Diễn giải: Spectral asymptotics nối phổ rời rạc với thể tích không gian pha.

#### Mức năng lượng trong hệ lượng tử
- Bài toán: Đếm số mức năng lượng thấp của toán tử Schrödinger hoặc Laplace-Beltrami.
- Mô hình: Dùng công thức tiệm cận phổ hoặc trace formula.
- Giả thiết và giới hạn: Mô hình bán cổ điển hoặc miền đủ đều.
- Diễn giải: Phổ không phải danh sách ngẫu nhiên, mà có quy luật hình học sâu bên dưới.

### 2. Trực giác bổ sung và các kết nối

Spectral asymptotics hỏi: khi năng lượng lớn, trị riêng phân bố như thế nào? Trực giác cốt lõi là mỗi "ô" thể tích trong phase space tương ứng với xấp xỉ một trạng thái lượng tử. Một bẫy phổ biến là chỉ nhìn vài trị riêng đầu rồi suy đoán toàn bộ phổ; asymptotics nói về chế độ lớn.

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

Trên đoạn $$ [0,1] $$ với biên Dirichlet,
$$ \lambda_n = n^2\pi^2. $$
Do đó
$$
N(\lambda)=\max\{n: n^2\pi^2\le \lambda\}=\left\lfloor \frac{\sqrt{\lambda}}{\pi}\right\rfloor.
$$
Weyl law nói rằng khi $$ \lambda \to \infty $$,
$$ N(\lambda)\sim \frac{\sqrt{\lambda}}{\pi}. $$

### 6. Phân tầng độ khó

**Bậc đại học.** Đếm mode trong các miền đơn giản và so sánh với quy luật tăng trưởng.

**Bậc sau đại học.** Kết nối với Weyl law, trace formulas, remainder estimates va spectral geometry.
