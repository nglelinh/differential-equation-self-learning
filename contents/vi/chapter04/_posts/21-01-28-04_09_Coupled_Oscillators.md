---
layout: post
title: "04-09 Ứng dụng: Dao động Liên kết"
chapter: '04'
order: 9
owner: Course Team
lang: vi
categories:
- chapter04
lesson_type: required
---

## Mục tiêu

Bài học này minh họa cách hệ phương trình và bài toán trị riêng xuất hiện tự nhiên trong mô hình hai vật dao động liên kết, làm rõ khái niệm chế độ dao động chuẩn (normal modes), đồng thời giải thích các hiện tượng dao động cùng pha, ngược pha, truyền năng lượng và phách.

## Kiến thức nền

Sinh viên cần nắm hệ phương trình tuyến tính, trị riêng, vector riêng và dao động điều hòa cơ bản. Các kiến thức vật lý về định luật Hooke và định luật II Newton là đủ để theo dõi bài học.

## Dẫn nhập

![Dao động liên kết và các mode riêng]({{ site.imgurl }}/chapter_img/chapter04/09_coupled_oscillators.svg)

Khi hai vật dao động được nối với nhau bằng lò xo, chuyển động của vật này phụ thuộc trực tiếp vào vị trí của vật kia. Thay vì phân tích rời rạc từng vật, câu hỏi trọng tâm là cả hệ có thể dao động đồng bộ theo những kiểu tự nhiên nào. Các kiểu dao động tự nhiên đó gọi là các chế độ dao động chuẩn (mode chuẩn) và được xác định trực tiếp qua bài toán trị riêng.

Trong ứng dụng này, mọi khái niệm đại số tuyến tính đều mang ý nghĩa vật lý cụ thể: trị riêng xác định tần số dao động riêng, vector riêng mô tả hình dạng dao động của cả hệ, tổ hợp tuyến tính tái hiện chuyển động thực tế, và khi hai tần số riêng gần nhau ta quan sát được hiện tượng phách.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hai vật giống nhau nối lò xo có hai kiểu dao động cơ bản: cùng dịch chuyển theo một chiều (cùng pha) hoặc dịch chuyển ngược chiều nhau (ngược pha). Trong hệ lý tưởng không cản, hai kiểu dao động này không tự chuyển hóa lẫn nhau, và mọi dao động bất kỳ của hệ đều là sự tổ hợp của chúng.

### Cách nhìn hình ảnh

Mỗi chế độ chuẩn tương ứng với một hình dạng dao động có tần số góc xác định. Khi kích hoạt đồng thời cả hai chế độ chuẩn, chuyển động quan sát được trên từng vật là sự chồng chất của hai dao động điều hòa có tần số khác nhau.

### Cách nhìn hình thức

Mô hình cơ học tuyến tính không cản có dạng hệ bậc hai:
$$ M\mathbf{x}''+K\mathbf{x}=0, $$
trong đó $$ M $$ là ma trận khối lượng và $$ K $$ là ma trận độ cứng. Thử nghiệm dạng điều hòa $$ \mathbf{x}(t)=\mathbf{v}\cos \omega t $$ (hoặc $$ \mathbf{v}e^{i\omega t} $$) dẫn tới bài toán trị riêng tổng quát:
$$ \left(K-\omega^2 M\right)\mathbf{v}=0. $$
Mỗi giá trị $$ \omega^2 $$ cho một tần số góc riêng, và mỗi vector riêng $$ \mathbf{v} $$ xác định một chế độ dao động chuẩn.

## Những ngộ nhận thường gặp

- "Dao động liên kết chỉ là hai dao động độc lập đặt cạnh nhau." Sai: lò xo liên kết tạo ra các chế độ chuẩn thuộc về toàn bộ hệ ghép.
- "Tần số riêng thuộc về từng vật riêng lẻ." Sai: tần số riêng là đặc trưng của toàn bộ hệ liên kết.
- "Hai vật giống hệt nhau thì luôn dao động cùng một kiểu." Sai: sự ghép nối tạo ra chế độ cùng pha và ngược pha có tần số khác nhau.
- "Phách do một ngoại lực tuần hoàn gây ra." Sai: phách là kết quả chồng chất của hai chế độ tự do có tần số gần nhau.

## Tiến trình học tập đề xuất

### Bước 1: Lập hệ phương trình từ định luật Newton

Viết chính xác lực đàn hồi tác dụng lên từng vật theo độ dãn của các lò xo.

### Bước 2: Viết hệ dưới dạng ma trận

Nhận diện cấu trúc $$ M\mathbf{x}''+K\mathbf{x}=0 $$.

### Bước 3: Giải bài toán trị riêng tìm chế độ chuẩn

Xác định các tần số góc $$ \omega $$ và vector riêng $$ \mathbf{v} $$.

### Bước 4: Tổng hợp nghiệm và diễn giải vật lý

Đọc ý nghĩa cùng pha, ngược pha và hiện tượng phách từ nghiệm tổng quát.

### Các checkpoint

- Sinh viên có viết đúng dấu các lực đàn hồi liên kết hay không.
- Sinh viên có hiểu chế độ chuẩn là kiểu dao động của toàn hệ chứ không phải của từng vật riêng lẻ hay không.
- Sinh viên có giải thích được hiện tượng phách bằng sự chồng chất hai tần số gần nhau hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hai vật giống nhau và hai chế độ chuẩn

Với hệ đối xứng gồm hai khối lượng giống nhau, hai vector riêng chuẩn thường có dạng
$$
\mathbf{v}_1=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
\mathbf{v}_2=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$
Vector $$ \mathbf{v}_1 $$ biểu diễn dao động cùng pha (hai vật luôn dịch chuyển cùng chiều, cùng độ lớn), còn $$ \mathbf{v}_2 $$ biểu diễn dao động ngược pha.

### Ví dụ 2: So sánh hai tần số riêng

Khi $$ \omega_1<\omega_2 $$, chế độ ngược pha có tần số cao hơn vì lò xo nối giữa hai vật bị kéo giãn và nén mạnh hơn, tạo lực hồi phục lớn hơn so với chế độ cùng pha (khi lò xo giữa gần như giữ nguyên chiều dài).

### Ví dụ 3: Nghiệm tổng quát của hệ

Nghiệm tổng quát là tổ hợp tuyến tính của hai chế độ chuẩn:
$$
\mathbf{x}(t)=
c_1\mathbf{v}_1\cos \omega_1 t
+
c_2\mathbf{v}_1\sin \omega_1 t
+
c_3\mathbf{v}_2\cos \omega_2 t
+
c_4\mathbf{v}_2\sin \omega_2 t.
$$
Các điều kiện đầu (vị trí và vận tốc ban đầu của hai vật) xác định bốn hằng số $$ c_1,c_2,c_3,c_4 $$.

### Ví dụ 4: Hiện tượng phách

Khi lò xo liên kết yếu, hai tần số riêng $$ \omega_1 $$ và $$ \omega_2 $$ rất gần nhau. Sự chồng chất của hai chế độ tạo ra dao động có đường bao biên độ thay đổi chậm theo thời gian (phách), tương ứng với sự truyền năng lượng qua lại định kỳ giữa hai vật.

## Câu hỏi khái niệm

1. Vì sao bài toán trị riêng của ma trận độ cứng và ma trận khối lượng cho trực tiếp các tần số dao động riêng?
2. Chế độ dao động chuẩn khác gì với chuyển động tổng quát của hệ?
3. Vì sao hiện tượng phách xuất hiện khi hai tần số riêng gần nhau?

## Bài toán ứng dụng

1. Cầu và nhà cao tầng có nhiều chế độ dao động riêng. Vì sao phân tích chế độ chuẩn là bước bắt buộc trong thiết kế kết cấu?
2. Một dây đàn có nhiều họa âm tự nhiên. Hãy liên hệ hiện tượng này với bài toán dao động liên kết.
3. Trong vật lý phân tử, các nguyên tử liên kết dao động quanh vị trí cân bằng. Vì sao chế độ chuẩn là ngôn ngữ tự nhiên để mô tả dao động phân tử?

## Chiến lược giảng dạy tương tác

- Chiếu hình ảnh hoặc video hai lò xo liên kết để sinh viên dự đoán trước các chế độ chuẩn.
- Yêu cầu sinh viên phác họa hướng chuyển động ứng với từng vector riêng thay vì chỉ viết cột số.
- Hỏi lớp: "Giữa chế độ cùng pha và ngược pha, chế độ nào có tần số lớn hơn theo trực giác cơ học?"
- Dùng mô phỏng số minh họa trực tiếp hiện tượng phách và sự trao đổi năng lượng giữa hai vật.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Tập trung trước vào hệ hai khối lượng giống nhau đối xứng để sinh viên thấy ngay hai chế độ cùng pha và ngược pha, gắn vector riêng với hình dạng chuyển động cụ thể.

### Thử thách cho sinh viên khá giỏi

Yêu cầu sinh viên tự lập đầy đủ ma trận $$ M, K $$ cho hệ hai vật nối ba lò xo (hai lò xo gắn tường, một lò xo nối giữa), rồi khảo sát ảnh hưởng khi bổ sung lực cản nhẹ.

## Tóm tắt dễ nhớ

Trong hệ dao động liên kết $$ M\mathbf{x}''+K\mathbf{x}=0 $$, bài toán trị riêng $$ (K-\omega^2 M)\mathbf{v}=0 $$ cho các tần số riêng $$ \omega $$ và các chế độ dao động chuẩn $$ \mathbf{v} $$. Mọi chuyển động tự do của hệ đều là chồng chất của các chế độ chuẩn này.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ hai vật nối lò xo
- Bài toán: Phân tích các kiểu dao động cùng pha và ngược pha của hai vật ghép lò xo.
- Mô hình: $$ M\mathbf{x}''+K\mathbf{x}=0 $$.
- Giả thiết và giới hạn: Dao động biên độ nhỏ, không ma sát, lò xo tuyến tính.
- Diễn giải: Chế độ chuẩn tách bài toán ghép thành các dao động điều hòa độc lập.

#### Dao động kết cấu công trình
- Bài toán: Xác định các tần số rung tự nhiên và dạng rung của cầu hoặc tòa nhà.
- Mô hình: $$ (K-\omega^2M)\mathbf{v}=0 $$.
- Giả thiết và giới hạn: Tuyến tính hóa quanh trạng thái cân bằng với biên độ nhỏ.
- Diễn giải: Trị riêng cho bình phương tần số riêng, còn vector riêng cho hình dạng rung của kết cấu.

#### Hiện tượng phách trong cơ học và âm học
- Bài toán: Khi hai chế độ có tần số gần nhau cùng được kích thích, biên độ dao động của mỗi vật tăng giảm tuần hoàn chậm.
- Mô hình: Tổ hợp tuyến tính của hai chế độ chuẩn có $$ \omega_1 \approx \omega_2 $$.
- Giả thiết và giới hạn: Không cản hoặc lực cản rất nhỏ.
- Diễn giải: Phách thể hiện sự truyền năng lượng qua lại giữa các vật liên kết.

### 2. Trực giác bổ sung và các kết nối

Dao động liên kết mang lại diễn giải vật lý trực tiếp nhất cho trị riêng và vector riêng trong Chương 04: trị riêng ứng với bình phương tần số riêng, vector riêng ứng với dạng dao động đồng bộ của toàn hệ.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1200)
x1 = np.cos(1.0 * t) + np.cos(1.2 * t)
x2 = np.cos(1.0 * t) - np.cos(1.2 * t)

plt.plot(t, x1, label="Dao động tổng hợp 1")
plt.plot(t, x2, label="Dao động tổng hợp 2", alpha=0.7)
plt.xlabel("t")
plt.ylabel("Biên độ")
plt.title("Phách do chồng chập hai tần số gần nhau")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: coupled oscillators normal modes animation
- search: beats from two frequencies visualization
- search: normal mode vibration engineering

### 5. Bài toán mẫu có bối cảnh thực

Giả sử một hệ đối xứng có hai chế độ chuẩn
$$
\mathbf{v}_1=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
\mathbf{v}_2=
\begin{pmatrix}
1\\
-1
\end{pmatrix}
$$
với các tần số $$ \omega_1<\omega_2 $$. Chế độ $$ \mathbf{v}_1 $$ là dao động cùng pha, còn $$ \mathbf{v}_2 $$ là dao động ngược pha. Khi kích hoạt đồng thời cả hai chế độ, chuyển động thực tế là tổ hợp tuyến tính của chúng và xuất hiện phách nếu $$ \omega_1 $$ gần $$ \omega_2 $$.

### 6. Phân tầng độ khó

**Bậc đại học.** Nhận diện chế độ cùng pha, ngược pha, giải bài toán trị riêng cho hệ hai bậc tự do và giải thích phách.

**Bậc sau đại học.** Thiết lập tổng quát ma trận $$ M,K $$ cho hệ nhiều bậc tự do, phân tích tính trực giao của các chế độ chuẩn theo tích trong xác định bởi $$ M $$.

## Video tham khảo

- Xem trước: [Coupled oscillators | Lecture 46 | Differential Equations for Engineers](https://www.youtube.com/watch?v=-pXnfzQfupE) — Jeffrey Chasnov, tiếng Anh. Xây dựng và giải các chế độ chuẩn cho hai dao động tử ghép.
- [4. Coupled Oscillators, Normal Modes](https://www.youtube.com/watch?v=BX4QPdP7fT8) — MIT OpenCourseWare, tiếng Anh. Bài giảng MIT 8.03 về dao động tử ghép và chế độ dao động chuẩn.
- [Solving Systems of Differential Equations with Eigenvalues and Eigenvectors](https://www.youtube.com/watch?v=Zwb5eiYcL8w) — Steve Brunton, tiếng Anh. Minh họa bước dùng trị riêng để tách hệ ghép thành các chế độ độc lập.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: nhiều ví dụ rõ ràng về dao động liên kết và chế độ chuẩn.
- Arnold, *Ordinary Differential Equations*: trình bày sâu góc nhìn phổ và cơ sở động học tự nhiên.
