---
layout: post
title: "07-03 Lý thuyết Sturm-Liouville"
chapter: '07'
order: 3
owner: Course Team
lang: vi
categories:
- chapter07
lesson_type: required
---

## Mục tiêu

Bài học này trình bày lý thuyết Sturm-Liouville như khung tổ chức đẹp nhất của bài toán trị riêng vi phân. Sau bài học, sinh viên cần nhận ra dạng Sturm-Liouville, hiểu ý nghĩa của tính tự liên hợp, biết vì sao trị riêng là thực, vì sao các hàm riêng khác trị riêng thì trực giao theo trọng số, và thấy được đây là chiếc cầu nối tự nhiên giữa ODE, chuỗi Fourier tổng quát và các PDE tách biến.

## Kiến thức nền

Sinh viên nên nắm bài toán trị riêng cơ bản, tích phân từng phần, và trực giác về cơ sở trực giao từ đại số tuyến tính hoặc chuỗi Fourier. Nếu bài 07-02 được hiểu như "một ví dụ điển hình", thì bài này là bức tranh tổng quát hóa và lý giải vì sao ví dụ đó đẹp đến vậy.

## Dẫn nhập

![Cấu trúc tự liên hợp của bài toán Sturm-Liouville]({{ site.imgurl }}/chapter_img/chapter07/03_sturm_liouville_theory.svg)

Khi mới gặp bài toán trị riêng, sinh viên thường nghĩ rằng ta chỉ đang giải một vài BVP có tham số. Nhưng càng học, ta càng nhận ra phía sau những bài toán ấy có một cấu trúc chung rất mạnh: một toán tử vi phân tự liên hợp, một trọng số dương, một phổ trị riêng thực và một họ hàm riêng trực giao. Tên gọi cho cấu trúc đó là lý thuyết Sturm-Liouville.

Giá trị của bài này không nằm ở việc ghi nhớ một công thức, mà ở việc giúp sinh viên nhìn thấy toàn bộ chương dưới một ngôn ngữ thống nhất. Từ đây, Bessel, Legendre, chuỗi Fourier tổng quát và khai triển hàm riêng đều bắt đầu nối với nhau rất tự nhiên.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Trong đại số tuyến tính, ma trận đối xứng là "ngoan": trị riêng thực, vector riêng trực giao, phép khai triển rất đẹp. Sturm-Liouville là phiên bản vô hạn chiều của câu chuyện đó. Toán tử vi phân tự liên hợp đóng vai trò của ma trận đối xứng, còn hàm riêng đóng vai trò của vector riêng.

### Cách nhìn hình ảnh

Nếu vẽ các hàm riêng đầu tiên của một bài toán Sturm-Liouville, ta thường thấy chúng có số nút tăng dần và "không lẫn" nhau theo nghĩa trực giao. Khi lấy tích có trọng số rồi tích phân, hai mode khác nhau triệt tiêu lẫn nhau. Hình ảnh này giúp sinh viên hiểu trực giao của hàm không chỉ là ký hiệu mà là một dạng độc lập hình học giữa các mode.

### Cách nhìn hình thức

Dạng Sturm-Liouville chuẩn là

$$ -(p(x)y')'+q(x)y=\lambda w(x)y,
\qquad a<x<b, $$

với

$$ p(x)>0,
\qquad
w(x)>0, $$

và các điều kiện biên thích hợp. Khi toán tử là tự liên hợp, ta có các tính chất then chốt:

- Mọi trị riêng đều là số thực.
- Các hàm riêng ứng với trị riêng khác nhau trực giao theo trọng số

$$ w(x). $$
- Trong nhiều trường hợp tốt, các hàm riêng tạo thành một hệ đầy đủ để khai triển hàm.

## Những ngộ nhận thường gặp

- "Sturm-Liouville chỉ là một dạng viết khác." Sai. Dạng viết đó làm lộ ra tính tự liên hợp và kéo theo toàn bộ cấu trúc phổ.
- "Trọng số chỉ là hệ số kỹ thuật." Không đúng. Trọng số quyết định tích vô hướng tự nhiên của bài toán.
- "Trực giao chỉ là phép tính tình cờ." Sai. Nó là hệ quả sâu của tự liên hợp và điều kiện biên.
- "Bài toán này quá trừu tượng, ít liên hệ vật lý." Sai. Hầu hết các mode vật lý cổ điển đều đi qua ngôn ngữ Sturm-Liouville.

## Tiến trình học tập đề xuất

### Bước 1: Nhìn lại ví dụ trị riêng cơ bản

Từ bài dây đàn, hỏi điều gì đã làm cho cấu trúc đó đẹp và ổn định.

### Bước 2: Nhận dạng dạng tự liên hợp

Sinh viên cần biết chuyển bài toán về dạng

$$ -(py')'+qy=\lambda wy. $$

### Bước 3: Hiểu tích vô hướng có trọng số

Đây là chỗ nhiều em thấy lạ, nhưng thực ra rất gần đại số tuyến tính.

### Bước 4: Chứng minh trực giao bằng tích phân từng phần

Đây là điểm then chốt và nên dạy chậm.

### Bước 5: Diễn giải hệ quả phổ

Nhấn mạnh trị riêng thực, hàm riêng trực giao, và thứ tự mode.

### Các checkpoint

- Sinh viên có nhận ra được trọng số của bài toán hay không.
- Sinh viên có giải thích được vì sao tự liên hợp gợi liên tưởng đến ma trận đối xứng hay không.
- Sinh viên có tự trình bày được ý tưởng chứng minh trực giao hay không.

## Ví dụ được giải chi tiết

### Ví dụ 1: Bài toán sin cổ điển dưới dạng Sturm-Liouville

Xét

$$ y''+\lambda y=0,
\qquad
y(0)=0,
\qquad
y(L)=0. $$

Viết lại:

$$ -y''=\lambda y. $$

Ở đây

$$ p(x)=1,
\qquad
q(x)=0,
\qquad
w(x)=1. $$

Đây là ví dụ Sturm-Liouville đơn giản nhất. Bài này nên được dùng để khẳng định với sinh viên rằng chuỗi Fourier sin không đứng riêng lẻ; nó là một trường hợp của lý thuyết tổng quát hơn.

### Ví dụ 2: Chứng minh trực giao cho hai hàm riêng

Giả sử $$ \phi_m $$ và $$ \phi_n $$ thỏa $$ -(p\phi_m')'+q\phi_m=\lambda_m w\phi_m $$, $$ -(p\phi_n')'+q\phi_n=\lambda_n w\phi_n. $$

Nhân phương trình đầu với $$ \phi_n $$ và phương trình sau với $$ \phi_m $$, rồi trừ đi. Sau khi tích phân trên $$ [a,b] $$ và dùng tích phân từng phần, các hạng biên biến mất nhờ điều kiện biên, ta được

$$
(\lambda_m-\lambda_n)\int_a^b \phi_m(x)\phi_n(x)w(x)\,dx=0.
$$

Nếu $$ \lambda_m\ne \lambda_n $$, suy ra

$$ \int_a^b \phi_m(x)\phi_n(x)w(x)\,dx=0. $$

Đây là phép tính ngắn nhưng là trái tim của cả chương.

### Ví dụ 3: Vai trò của trọng số

Xét một bài toán có dạng

$$ -(xy')'=\lambda x y,
\qquad 0<x<1. $$

Ở đây trọng số là $$ w(x)=x $$. Điều này nghĩa là trực giao đúng phải là

$$ \int_0^1 \phi_m(x)\phi_n(x)x\,dx=0, $$

không phải tích phân thông thường không trọng số. Ví dụ này cực kỳ quan trọng vì nhiều sinh viên hay quên mất trọng số khi chuyển từ công thức sang thực hành.

### Ví dụ 4: Liên hệ với Bessel và Legendre

Sau khi biến đổi thích hợp, phương trình Legendre và nhiều phương trình vật lý cổ điển đều rơi vào khung Sturm-Liouville. Ví dụ này không cần tính chi tiết nhiều, nhưng nên dùng để sinh viên thấy rằng chương trước và chương này đang ghép thành một hệ thống thống nhất.

## Câu hỏi khái niệm

1. Vì sao tính tự liên hợp của toán tử vi phân lại giống vai trò của ma trận đối xứng trong đại số tuyến tính?
2. Tại sao trực giao giữa các hàm riêng khác trị riêng lại là một tính chất cực kỳ quan trọng?
3. Vai trò của trọng số $$ w(x) $$ trong lý thuyết Sturm-Liouville là gì?

## Bài toán ứng dụng

1. Trong bài toán truyền nhiệt hoặc dao động, vì sao việc có một họ mode trực giao lại giúp ta giải bài toán hiệu quả hơn rất nhiều?
2. Một mô hình vật lý tạo ra phương trình với hệ số biến thiên. Hãy giải thích vì sao việc đưa bài toán về dạng Sturm-Liouville lại có giá trị lớn.
3. Trong các hệ dao động, vì sao các mode khác nhau thường được xem là "độc lập năng lượng" theo một nghĩa thích hợp?

## Chiến lược giảng dạy tương tác

- Bắt đầu bằng câu hỏi: "Ma trận đối xứng đẹp ở điểm nào, và nếu thay ma trận bằng toán tử vi phân thì điều gì còn giữ lại?"
- Cho sinh viên tự điền bảng tương ứng giữa đại số tuyến tính và Sturm-Liouville: vector riêng, hàm riêng, tích vô hướng, trọng số, trực giao.
- Dừng thật lâu ở phép tích phân từng phần sinh ra trực giao; đây là khoảnh khắc bản chất nhất của bài.
- Mời sinh viên giải thích bằng lời vì sao điều kiện biên làm cho các hạng biên biến mất.

## Phân hóa học tập

### Hỗ trợ sinh viên còn gặp khó khăn

Nên giữ chặt liên hệ với đại số tuyến tính và chuỗi Fourier. Khi thấy cái mới chỉ là cái cũ ở không gian hàm, sinh viên sẽ bớt ngợp rất nhiều.

### Thử thách cho sinh viên khá giỏi

Có thể yêu cầu sinh viên khá giỏi khảo sát thêm ý tưởng đầy đủ của hệ hàm riêng hoặc liên hệ với nguyên lý cực trị cho trị riêng nhỏ nhất. Đây là bước chuẩn bị tốt cho các chương PDE và giải tích hàm sau này.

## Tóm tắt dễ nhớ

Lý thuyết Sturm-Liouville là phiên bản vô hạn chiều của ma trận đối xứng. Dạng tự liên hợp kéo theo trị riêng thực, hàm riêng trực giao theo trọng số, và mở đường cho việc khai triển hàm theo các mode riêng phù hợp với toán tử và điều kiện biên của bài toán.

## Mở rộng: Ứng dụng, Trực giác và Trực quan hóa

### 1. Ứng dụng thực tế

#### Dao động dây không đồng nhất
- Bài toán: Dây có mật độ thay đổi theo vị trí, nên bài toán mode tự nhiên có trọng số.
- Mô hình:
$$ -(p(x)y')'+q(x)y=\lambda w(x)y. $$
- Giả thiết và giới hạn: Hệ tuyến tính, biên chính quy, trọng số dương.
- Diễn giải: Sturm-Liouville nói với ta rằng trị riêng là thực, hàm riêng trực giao và tạo nên cơ sở mode.

#### Truyền nhiệt hay khuếch tán với hệ số biến thiên
- Bài toán: Tách biến phương trình nhiệt với vật liệu không đồng nhất dẫn đến toán tử tự liên hợp.
- Mô hình:
$$
\frac{d}{dx}\left(p(x)\frac{dy}{dx}\right)+(\lambda w(x)-q(x))y=0.
$$
- Giả thiết và giới hạn: Tách biến và điều kiện biên thích hợp.
- Diễn giải: Tính tự liên hợp là lý do các mode có tính trực giao và phổ đẹp.

### 2. Trực giác bổ sung và các kết nối

Sturm-Liouville là nơi bài toán trị riêng được đặt vào khung toán tử rất có cấu trúc. Tự liên hợp chính là nguyên nhân sâu xa của phổ thực và trực giao. Một bẫy phổ biến là học định lý như danh sách tính chất mà không thấy rằng các tính chất ấy đều đến từ phép tích phân từng phần và điều kiện biên.

### 3. Trực quan hóa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
y1 = np.sin(np.pi * x)
y2 = np.sin(2 * np.pi * x)

plt.plot(x, y1, label="phi1")
plt.plot(x, y2, label="phi2")
plt.fill_between(x, y1 * y2, alpha=0.3, color="orange", label="phi1 * phi2")
plt.xlabel("x")
plt.ylabel("value")
plt.title("Truc giao cua cac ham rieng co dinh bien")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

### 4. Gợi ý tìm thêm mô phỏng

- search: Sturm Liouville orthogonality visualization
- search: self adjoint operator boundary value problem
- search: weighted orthogonality eigenfunctions

### 5. Bài toán mẫu có bối cảnh thực

Với bài toán đơn giản
$$ y''+\lambda y=0,\qquad y(0)=y(L)=0, $$
hàm riêng là
$$ \phi_n(x)=\sin\left(\frac{n\pi x}{L}\right). $$
Ta có tính trực giao:
$$ \int_0^L \phi_m(x)\phi_n(x)\,dx=0\qquad (m\ne n). $$
Đây là ví dụ cốt lõi cho cơ chế trực giao trong Sturm-Liouville.

### 6. Phân tầng độ khó

**Bậc đại học.** Nắm dạng chuẩn, phổ thực và trực giao của hàm riêng.

**Bậc sau đại học.** Bàn về toán tử tự liên hợp, không gian Hilbert có trọng số và định lý phổ.

## Tài liệu tham khảo

- Boyce & DiPrima, Chương 11: trình bày khung Sturm-Liouville, trọng số và trực giao hàm riêng.
- Haberman, Chương 5: giải thích trực giác của toán tử tự liên hợp trong các bài toán vật lý cổ điển.
