---
layout: post
title: "00-04-00 Số Phức và Hàm Mũ"
chapter: '00'
order: 5
owner: Course Team
lang: vi
categories:
- chapter00
lesson_type: required
---

## Mục tiêu

Bài học này giúp sinh viên nắm số phức như một ngôn ngữ tự nhiên cho dao động và nghiệm của phương trình vi phân tuyến tính. Sau bài học, sinh viên cần thực hiện được các phép toán với số phức, chuyển đổi giữa dạng đại số và dạng cực, dùng công thức Euler để kết nối hàm mũ với lượng giác, tìm căn bậc $$ n $$ của số phức, và giải thích vì sao nghiệm phức lại dẫn đến nghiệm thực dạng sin-cos trong ODE.

## Kiến thức nền

Sinh viên cần nắm căn bậc hai, tam giác lượng, hàm mũ thực, và công thức lượng giác cơ bản. Kiến thức về vector trong mặt phẳng cũng hữu ích vì số phức có một diễn giải hình học rất trực quan. Nếu sinh viên còn yếu về góc, radian, hoặc các công thức lượng giác, nên ôn lại trước khi vào phần dạng cực và công thức Euler.

## Dẫn nhập

Khi học phương trình vi phân, sinh viên thường gặp những phương trình đặc trưng như $$ r^2+2r+5=0 $$. Nghiệm của phương trình này không phải số thực mà là $$ r=-1\pm 2i $$. Nếu chưa có số phức, ta sẽ bị chặn lại ngay ở bước tìm nghiệm. Nhưng điều thú vị hơn là: **dù nghiệm trung gian là phức, lời giải cuối cùng của ODE lại thường là các hàm thực như $$ e^{-t}\cos 2t $$ và $$ e^{-t}\sin 2t $$**. Số phức không phải một lối rẽ xa lạ, mà là cây cầu ngắn nhất nối đại số với dao động.

Số phức cũng cho ta một cách nhìn hình học đẹp. Thay vì chỉ là “một ký hiệu với $$ i^2=-1 $$”, **số phức là điểm trong mặt phẳng, là phép quay, là co giãn, và là ngôn ngữ gọn nhất cho sóng điều hòa**. Vì thế, bài này không chỉ là ôn công thức, mà là xây một công cụ nền cho ODE, PDE, và cả biến đổi Fourier về sau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy tưởng tượng một mũi tên trong mặt phẳng. Nếu ta nhân mũi tên đó với một số thực dương, ta chỉ kéo dài hoặc thu ngắn nó. Nhưng nếu ta nhân với $$ i $$, ta quay nó đi một góc $$ 90^\circ $$. Vì vậy số phức cho phép ta trộn hai thao tác rất tự nhiên: quay và co giãn. Đây là lý do chúng phù hợp đặc biệt với các bài toán dao động, nơi nghiệm vừa quay pha vừa thay đổi biên độ.

### Cách nhìn hình ảnh

Trong mặt phẳng phức, số $$ z=x+iy $$ được biểu diễn bởi điểm $$ \left(x,y\right) $$. Khoảng cách từ gốc đến điểm đó là mô-đun $$ \lvert z \rvert=\sqrt{x^2+y^2} $$, còn góc tạo với trục thực dương là argument $$ \theta $$. Khi viết $$ z=r(\cos \theta+i\sin \theta) $$, ta không chỉ đổi dạng viết, mà đang nói rằng một số phức chính là “độ dài + góc quay”. Giáo viên nên vẽ một điểm như $$ 1+\sqrt{3}i $$, rồi cho sinh viên đọc ngay mô-đun và góc của nó trên hình.

### Cách nhìn hình thức

Một số phức có dạng $$ z=x+iy $$, trong đó $$ x,y\in\mathbb{R} $$ và $$ i^2=-1 $$. Các phép toán:

$$ (a+ib)+(c+id)=(a+c)+i(b+d), $$ $$ (a+ib)(c+id)=(ac-bd)+i(ad+bc) $$. Liên hợp phức của $$ z $$ là $$ \overline{z}=x-iy $$, và mô-đun là $$ \lvert z \rvert=\sqrt{z\overline{z}} $$.

Dạng cực:

$$ z=r(\cos \theta+i\sin \theta). $$

Công thức Euler:

$$ e^{i\theta}=\cos \theta+i\sin \theta. $$

Từ đó,

$$ z=re^{i\theta}. $$

## Những ngộ nhận thường gặp

- “Số phức là thứ không có ý nghĩa hình học.” Sai. Chúng có một diễn giải hình học rất đẹp trong mặt phẳng.
- “Nhân với $$ i $$ chỉ là thao tác đại số.” Chưa đủ. Về hình học, nhân với $$ i $$ tương ứng với quay $$ 90^\circ $$.
- “Nghiệm phức của ODE nghĩa là nghiệm vật lý phải là số phức.” Sai. Nghiệm phức thường chỉ là công cụ trung gian; từ đó ta trích ra các nghiệm thực qua phần thực và phần ảo.
- “Dạng cực chỉ là cách viết khác, không mang thêm lợi ích.” Sai. Dạng cực làm phép nhân, chia, lũy thừa, và khai căn trở nên đơn giản hơn nhiều.

## Tiến trình học tập đề xuất

### Bước 1: Thành thạo dạng đại số

Sinh viên nên chắc phép cộng, nhân, liên hợp, mô-đun, và phép chia bằng liên hợp.

### Bước 2: Chuyển sang dạng cực

Tập đọc một số phức thành độ dài và góc. Đây là nơi hình học bước vào.

### Bước 3: Học công thức Euler

Hiểu đây là chiếc cầu nối giữa hàm mũ và lượng giác, không chỉ là một đẳng thức đẹp.

### Bước 4: Kết nối với ODE

Nhìn nghiệm phức của phương trình đặc trưng và rút ra nghiệm thực của phương trình vi phân.

### Các checkpoint

- Sinh viên có đổi qua lại được giữa dạng $$ x+iy $$ và $$ re^{i\theta} $$ không?
- Sinh viên có giải thích được ý nghĩa hình học của phép nhân số phức không?
- Sinh viên có dùng nghiệm phức để viết nghiệm thực của ODE bậc hai không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phép toán đại số với số phức

Cho $$ z_1=2+3i,\qquad z_2=1-4i $$. Khi đó $$ z_1+z_2=3-i $$. Và $$ z_1z_2=(2+3i)(1-4i)=2-8i+3i-12i^2=14-5i $$. Ví dụ này giúp sinh viên thấy quy tắc tính hoàn toàn cụ thể, không có gì huyền bí.

### Ví dụ 2: Dạng cực

Xét $$ z=1+\sqrt{3}i $$. Mô-đun là $$ \lvert z \rvert=\sqrt{1+3}=2 $$.

Vì

$$
\cos \theta=\frac{1}{2},\qquad \sin \theta=\frac{\sqrt{3}}{2},
$$

ta có

$$ \theta=\frac{\pi}{3}. $$

Vậy

$$
z=2\left(\cos \frac{\pi}{3}+i\sin \frac{\pi}{3}\right)=2e^{i\pi/3}.
$$

### Ví dụ 3: Căn bậc ba của đơn vị

Giải $$ z^3=1 $$. Viết $$ 1=e^{i2k\pi} $$, nên các nghiệm là $$ z_k=e^{i2k\pi/3},\qquad k=0,1,2 $$. Cụ thể:

$$
1,\qquad -\frac12+\frac{\sqrt3}{2}i,\qquad -\frac12-\frac{\sqrt3}{2}i.
$$

Ví dụ này cho thấy dạng cực làm khai căn trở nên rất gọn.

### Ví dụ 4: Nghiệm phức của ODE

Xét phương trình $$ y''+2y'+5y=0 $$. Phương trình đặc trưng là $$ r^2+2r+5=0 $$, nên $$ r=-1\pm 2i $$. Từ đó nghiệm phức là $$ e^{(-1+2i)t}=e^{-t}e^{2it} $$. Dùng công thức Euler:

$$ e^{2it}=\cos 2t+i\sin 2t. $$

Vì vậy hai nghiệm thực độc lập là $$ e^{-t}\cos 2t,\qquad e^{-t}\sin 2t $$. Đây là ví dụ quan trọng nhất của bài.

## Câu hỏi khái niệm

1. Vì sao dạng cực của số phức lại tự nhiên hơn dạng đại số khi nói về phép nhân và lũy thừa?
2. Điều gì làm cho công thức Euler trở thành chiếc cầu giữa hàm mũ và dao động lượng giác?
3. Tại sao nghiệm phức của phương trình đặc trưng lại dẫn đến nghiệm thực của ODE?

## Bài toán ứng dụng

1. Trong mạch điện xoay chiều, vì sao biên độ và pha của tín hiệu thường được mô tả bằng số phức?
2. Trong dao động cơ học tắt dần, nghiệm dạng $$ e^{-\alpha t}\cos \beta t $$ phản ánh điều gì về biên độ và pha?
3. Trong biến đổi Fourier, tại sao sóng phẳng phức $$ e^{ix\xi} $$ lại tiện hơn sin và cos riêng lẻ?

## Chiến lược giảng dạy tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu nhân một số phức với $$ i $$, chuyện gì xảy ra trên hình?
- Vì sao số phức là công cụ tốt cho dao động hơn chỉ dùng sin và cos?
- Em thấy dạng nào tiện hơn cho phép nhân: $$ x+iy $$ hay $$ re^{i\theta} $$?

### Hoạt động gợi ý

- Cho sinh viên vẽ một số phức trên mặt phẳng rồi đọc mô-đun và argument.
- Tổ chức hoạt động “dịch ngôn ngữ”: từ dạng đại số sang dạng cực và ngược lại.
- Cho nhóm sinh viên giải nhanh các phương trình đặc trưng có nghiệm phức rồi diễn giải nghiệm thực.

## Phân hóa học tập

### Hỗ trợ sinh viên gặp khó khăn

- Dùng nhiều hình vẽ mặt phẳng phức.
- Tập trung vào liên hợp, mô-đun, và công thức Euler trước khi làm căn bậc $$ n $$.
- Cho nhiều bài đổi dạng giữa $$ x+iy $$ và $$ re^{i\theta} $$.

### Thử thách cho sinh viên khá giỏi

- Chứng minh công thức De Moivre bằng quy nạp.
- Tìm tất cả căn bậc bốn của một số phức cho trước.
- Giải thích vì sao nghiệm phức luôn xuất hiện theo cặp liên hợp khi hệ số phương trình đặc trưng là thực.

## Tóm tắt dễ nhớ

Số phức là ngôn ngữ của quay và dao động. Dạng đại số giúp tính cộng và nhân trực tiếp, dạng cực giúp nhìn hình học và làm lũy thừa, còn công thức Euler $$ e^{i\theta}=\cos\theta+i\sin\theta $$ là cầu nối mạnh nhất giữa đại số, lượng giác, và nghiệm dao động của phương trình vi phân.

## Tài liệu tham khảo

- Boyce & DiPrima, *Elementary Differential Equations*.
- Churchill & Brown, *Complex Variables and Applications*.
