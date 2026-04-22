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

Bài học này giúp sinh viên thấy cách hệ phương trình và trị riêng xuất hiện tự nhiên trong bài toán hai dao động liên kết, hiểu khái niệm mode chuẩn, và diễn giải hiện tượng truyền năng lượng, dao động cùng pha, ngược pha và phách. Đây là ứng dụng vật lý trung tâm của cả chương.

## Kiến thức nền

Sinh viên cần nắm hệ tuyến tính, trị riêng, vector riêng và trực giác về dao động điều hòa. Một chút vật lý về lò xo và định luật Newton là đủ để tiếp cận bài học.

## Dẫn nhập

![Dao động liên kết và các mode riêng]({{ site.imgurl }}/chapter_img/chapter04/09_coupled_oscillators.svg)

Một dao động đơn lẻ đã rất giàu cấu trúc, nhưng khi hai dao động được nối với nhau, thế giới trở nên thú vị hơn nhiều. Lúc đó ta không chỉ hỏi từng vật rung thế nào, mà hỏi cả hệ rung theo những "kiểu tự nhiên" nào. Chính những kiểu tự nhiên ấy là các mode chuẩn, và chúng được tìm ra bằng bài toán trị riêng.

Đây là bài học rất đẹp vì mọi khái niệm đại số tuyến tính của chương bỗng trở nên cực kỳ vật lý. Trị riêng trở thành tần số riêng. Vector riêng trở thành hình dạng mode. Tổ hợp tuyến tính của mode trở thành dao động thực tế mà ta quan sát. Và khi hai tần số gần nhau, phách xuất hiện như một hiện tượng nghe và thấy được.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hai vật nối lò xo có thể rung cùng nhau hoặc ngược nhau. Những kiểu rung đặc biệt này không trộn lẫn vào nhau trong lý tưởng, nên chúng là "ngôn ngữ tự nhiên" của hệ. Dao động tổng quát chỉ là sự pha trộn của các kiểu rung cơ bản ấy.

### Cách nhìn hình ảnh

Một mode chuẩn có thể là cả hai vật cùng dịch sang phải rồi sang trái cùng lúc. Mode khác có thể là một vật sang phải khi vật kia sang trái. Mỗi mode có tần số riêng, nên nếu kích hoạt cả hai đồng thời, ta sẽ thấy hình dạng dao động của hệ là sự chồng chập của hai nhịp này.

### Cách nhìn hình thức

Trong mô hình đơn giản, ta thường có hệ bậc hai dạng
$$ M\mathbf{x}''+K\mathbf{x}=0, $$
trong đó $$ M $$ là ma trận khối lượng, $$ K $$ là ma trận độ cứng. Ta thử nghiệm điều hòa
$$ \mathbf{x}(t)=\mathbf{v}\cos \omega t $$
hoặc
$$ \mathbf{x}(t)=\mathbf{v}e^{i\omega t}, $$
dẫn đến bài toán
$$ \left(K-\omega^2 M\right)\mathbf{v}=0. $$
Đây là bài toán trị riêng tổng quát. Mỗi $$ \omega^2 $$ là một trị riêng, mỗi $$ \mathbf{v} $$ là một mode chuẩn.

## Những ngộ nhận thường gặp

- "Dao động liên kết chỉ là hai dao động đơn lẻ cộng lại." Sai. Hệ có các mode chuẩn riêng của toàn bộ cấu trúc.
- "Tần số riêng chỉ là thông số của từng vật." Sai. Chúng là thông số của toàn hệ ghép.
- "Nếu hai vật giống hệt nhau thì dao động luôn đơn giản." Không hẳn. Ghép nối tạo ra mode cùng pha và ngược pha rất khác nhau.
- "Phách là một loại lực ngoài." Sai. Phách là hiện tượng chồng chập của hai tần số gần nhau.

## Tiến trình học tập đề xuất

### Bước 1: Lập hệ phương trình từ Newton

Đọc rõ lực đàn hồi giữa các vật.

### Bước 2: Đưa về dạng ma trận

Nhận ra cấu trúc $$ M\mathbf{x}''+K\mathbf{x}=0 $$.

### Bước 3: Tìm mode chuẩn

Giải bài toán trị riêng cho $$ \omega^2 $$ và $$ \mathbf{v} $$.

### Bước 4: Ghép mode thành nghiệm tổng quát

Diễn giải cùng pha, ngược pha và phách.

### Các checkpoint

- Sinh viên có viết đúng hệ lực liên kết hay không.
- Sinh viên có hiểu mode chuẩn là dạng dao động của toàn hệ chứ không phải của từng vật riêng lẻ hay không.
- Sinh viên có giải thích được phách bằng chồng chập hai tần số gần nhau hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Hai vật giống nhau với hai mode cơ bản

Giả sử hai khối lượng giống nhau và hệ cho ra hai mode:
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
Mode thứ nhất là cùng pha, mode thứ hai là ngược pha. Chỉ riêng việc đọc hai vector riêng này đã cho trực giác vật lý rất mạnh.

### Ví dụ 2: Tần số riêng khác nhau

Nếu hai mode tương ứng với
$$ \omega_1<\omega_2, $$
thì mode ngược pha thường có tần số cao hơn vì lò xo giữa hai vật bị kéo căng mạnh hơn. Đây là điểm cực kỳ đáng để sinh viên tự giải thích bằng trực giác cơ học.

### Ví dụ 3: Nghiệm tổng quát

Nghiệm có thể viết
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
Điều kiện đầu sẽ chọn cách pha trộn các mode này. Đây là phiên bản vật lý rất rõ của nguyên lý chồng chập.

### Ví dụ 4: Hiện tượng phách

Khi $$ \omega_1 $$ và $$ \omega_2 $$ gần nhau, dao động tổng hợp có thể xuất hiện biên độ lớn nhỏ xen kẽ chậm theo thời gian. Sinh viên nên hiểu phách không phải một lực bí ẩn, mà là hệ quả của việc cộng hai mode gần tần số.

## Câu hỏi khái niệm

1. Vì sao bài toán trị riêng của ma trận độ cứng và khối lượng lại cho ra tần số riêng?
2. Mode chuẩn khác gì với chuyển động tổng quát thật sự của hệ?
3. Vì sao phách xuất hiện khi hai tần số riêng gần nhau?

## Bài toán ứng dụng

1. Một cây cầu hoặc tòa nhà có nhiều mode rung tự nhiên. Hãy giải thích vì sao phân tích mode là bước thiết yếu trong kỹ thuật kết cấu.
2. Một nhạc cụ dây có nhiều mode rung. Hãy liên hệ điều đó với bài toán dao động liên kết.
3. Trong cơ học phân tử, nhiều nguyên tử rung ghép với nhau. Hãy giải thích vì sao mode chuẩn là ngôn ngữ tự nhiên để mô tả.

## Chiến lược giảng dạy tương tác

- Dùng hình hoặc video hai lò xo liên kết để sinh viên đoán trước các mode.
- Cho sinh viên vẽ vector riêng như các mẫu chuyển động chứ không chỉ là cột số.
- Hỏi lớp: "Mode cùng pha và ngược pha, mode nào nên nhanh hơn về mặt trực giác?"
- Nếu có thể, dùng mô phỏng để sinh viên thấy phách thay vì chỉ nghe mô tả.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên cho sinh viên yếu tập trung vào trường hợp hai khối lượng giống nhau với hai mode rất trực quan. Việc nhìn vector riêng như "hình dạng rung" sẽ giúp bài toán đại số bớt khô và dễ nhớ hơn.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi lập đầy đủ ma trận $$ M,K $$ từ mô hình cơ học cụ thể, hoặc phân tích trường hợp thêm giảm chấn nhẹ để thấy mode chuẩn bị thay đổi ra sao.

## Tóm tắt dễ nhớ

Dao động liên kết là nơi trị riêng trở thành tần số riêng và vector riêng trở thành mode chuẩn. Hệ không rung theo từng vật riêng lẻ, mà rung theo các kiểu tự nhiên của toàn bộ cấu trúc. Khi hiểu mode chuẩn, sinh viên thật sự nắm được trái tim vật lý của chương hệ phương trình.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Hệ hai lò xo liên kết
- Bài toán: Hai vật nối lò xo có thể rung cùng pha hoặc ngược pha.
- Mô hình:
$$ M\mathbf{x}''+K\mathbf{x}=0. $$
- Giả thiết và giới hạn: Dao động nhỏ, không ma sát, mô hình tuyến tính.
- Diễn giải: Các mode chuẩn là ngôn ngữ tự nhiên nhất để mô tả chuyển động của toàn hệ.

#### Kết cấu công trình
- Bài toán: Cầu hay tòa nhà có nhiều mode rung nội tại.
- Mô hình:
$$ (K-\omega^2M)\mathbf{v}=0. $$
- Giả thiết và giới hạn: Tuyến tính hóa quanh cân bằng, mode dao động nhỏ.
- Diễn giải: Trị riêng trở thành bình phương tần số riêng, vector riêng trở thành dạng rung.

#### Phách trong vật lý và âm học
- Bài toán: Khi hai tần số gần nhau cùng xuất hiện, biên độ quan sát dao động chậm theo "nhịp đập".
- Mô hình: Chồng chập hai mode chuẩn có tần số gần nhau.
- Giả thiết và giới hạn: Hệ nhẹ cản hoặc không cản.
- Diễn giải: Phách là hiện tượng cảm nhận được của đại số tuyến tính trong dao động.

### 2. Trực giác bổ sung và các kết nối

Dao động liên kết là ứng dụng vật lý đẹp nhất của trị riêng trong chương này. Ở đây, trị riêng không còn là số trừu tượng mà là tần số riêng, còn vector riêng là hình dạng dao động của toàn hệ. Điều đó làm cho các công cụ đại số trở nên hữu hình và rất dễ nhớ.

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

Giả sử hệ có hai mode chuẩn
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
\end{pmatrix},
$$
với tần số
$$ \omega_1<\omega_2. $$
Mode thứ nhất là cùng pha, mode thứ hai là ngược pha. Nếu kích hoạt cả hai mode, chuyển động thực của hệ là tổ hợp tuyến tính của chúng. Khi $$ \omega_1 $$ và $$ \omega_2 $$ gần nhau, ta quan sát được phách.

### 6. Phân tầng độ khó

**Bậc đại học.** Đọc được mode cùng pha, ngược pha và hiểu khái niệm tần số riêng.

**Bậc sau đại học.** Lập đầy đủ ma trận $$ M,K $$ và phân tích mode chuẩn như một bài toán trị riêng tổng quát.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 7: nhiều ví dụ tốt về mode chuẩn và dao động liên kết.
- Arnold, *Ordinary Differential Equations*: hữu ích cho góc nhìn phổ và cơ sở động học tự nhiên.
