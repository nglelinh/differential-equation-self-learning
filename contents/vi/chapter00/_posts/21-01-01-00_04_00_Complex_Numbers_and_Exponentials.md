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

Bài học này giúp sinh viên nắm vững số phức như một ngôn ngữ tự nhiên cho dao động và nghiệm của phương trình vi phân tuyến tính. Sau bài học, sinh viên có thể thực hiện các phép toán với số phức, chuyển đổi giữa dạng đại số và dạng cực, vận dụng công thức Euler để liên kết hàm mũ với hàm lượng giác, tìm căn bậc $$ n $$ của số phức và giải thích vì sao nghiệm phức của phương trình đặc trưng lại dẫn đến nghiệm thực dạng sin–cos trong ODE.

## Kiến thức nền

Sinh viên cần nắm vững căn bậc hai, hệ thức lượng trong tam giác, hàm mũ thực và các công thức lượng giác cơ bản. Kiến thức về vector trong mặt phẳng cũng rất hữu ích vì số phức có diễn giải hình học trực quan. Nếu còn chưa chắc về góc, đơn vị radian hoặc công thức lượng giác, sinh viên nên ôn lại trước khi học phần dạng cực và công thức Euler.

## Dẫn nhập

Khi giải phương trình vi phân tuyến tính hệ số hằng, ta thường gặp những phương trình đặc trưng như $$ r^2+2r+5=0 $$. Phương trình này không có nghiệm thực mà có hai nghiệm phức liên hợp $$ r=-1\pm 2i $$. Dù bước trung gian dùng đến số phức, **lời giải cuối cùng của ODE lại là các hàm thực như $$ e^{-t}\cos 2t $$ và $$ e^{-t}\sin 2t $$**. Vì thế, số phức là cầu nối trực tiếp giữa đại số và dao động.

Bên cạnh đại số, số phức còn mang ý nghĩa hình học rõ ràng: thay vì chỉ là một ký hiệu thỏa mãn $$ i^2=-1 $$, **mỗi số phức là một điểm trong mặt phẳng, đồng thời biểu diễn phép quay kết hợp co giãn**. Đây là công cụ nền tảng cho ODE, PDE và biến đổi Fourier ở các chương sau.

## Khái niệm theo ba cách

### Cách nhìn trực quan

Hãy hình dung một mũi tên xuất phát từ gốc tọa độ trong mặt phẳng. Khi nhân mũi tên đó với một số thực dương, ta chỉ kéo dài hoặc thu ngắn độ dài của nó. Khi nhân với $$ i $$, ta quay mũi tên đi một góc $$ 90^\circ $$ ngược chiều kim đồng hồ. Nhờ vậy, phép nhân số phức kết hợp tự nhiên cả hai thao tác quay và co giãn—rất phù hợp với các bài toán dao động, nơi nghiệm vừa thay đổi pha vừa thay đổi biên độ.

### Cách nhìn hình ảnh

Trong mặt phẳng phức, số $$ z=x+iy $$ tương ứng với điểm $$ \left(x,y\right) $$. Khoảng cách từ gốc tọa độ đến điểm đó là mô-đun $$ \lvert z \rvert=\sqrt{x^2+y^2} $$, còn góc tạo với chiều dương trục thực là argument $$ \theta $$. Khi viết $$ z=r(\cos \theta+i\sin \theta) $$, ta biểu diễn số phức bằng đúng hai thông số hình học là độ dài và góc quay. Trên lớp, giảng viên có thể vẽ điểm $$ 1+\sqrt{3}i $$ để sinh viên đọc trực tiếp mô-đun và argument từ hình vẽ.

### Cách nhìn hình thức

Một số phức có dạng $$ z=x+iy $$, trong đó $$ x,y\in\mathbb{R} $$ và $$ i^2=-1 $$. Hai phép toán cơ bản là

$$
(a+ib)+(c+id)=(a+c)+i(b+d), \qquad (a+ib)(c+id)=(ac-bd)+i(ad+bc).
$$

Liên hợp phức của $$ z $$ là $$ \overline{z}=x-iy $$, và mô-đun là $$ \lvert z \rvert=\sqrt{z\overline{z}} $$.

Dạng cực của số phức là

$$
z=r(\cos \theta+i\sin \theta).
$$

Với công thức Euler

$$
e^{i\theta}=\cos \theta+i\sin \theta,
$$

ta viết gọn được thành dạng mũ

$$
z=re^{i\theta}.
$$

## Những ngộ nhận thường gặp

- "Số phức chỉ là ký hiệu trừu tượng, không có ý nghĩa hình học." Sai. Mỗi số phức biểu diễn một điểm (hay vector) trong mặt phẳng phức, và phép nhân số phức tương ứng với phép quay kết hợp vị tự.
- "Nhân với $$ i $$ chỉ là thao tác đại số." Chưa đủ. Về mặt hình học, nhân với $$ i $$ là phép quay ngược chiều kim đồng hồ một góc $$ 90^\circ $$.
- "Phương trình đặc trưng có nghiệm phức thì nghiệm vật lý của ODE phải là số phức." Sai. Nghiệm phức chỉ đóng vai trò công cụ trung gian; từ phần thực và phần ảo của nó ta thu được các nghiệm thực độc lập tuyến tính.
- "Dạng cực chỉ là cách viết khác, không có lợi ích tính toán." Sai. Dạng cực (và dạng mũ) giúp phép nhân, chia, lũy thừa và khai căn trở nên gọn hơn nhiều so với dạng đại số.

## Tiến trình học tập đề xuất

### Bước 1: Thành thạo dạng đại số

Nắm chắc các phép cộng, nhân, lấy liên hợp, tính mô-đun và phép chia số phức bằng cách nhân tử và mẫu với số phức liên hợp.

### Bước 2: Chuyển sang dạng cực

Luyện đọc một số phức theo độ dài (mô-đun) và góc (argument) trên mặt phẳng phức để gắn đại số với hình học.

### Bước 3: Nắm vững công thức Euler

Hiểu công thức Euler như cầu nối giữa hàm mũ và hàm lượng giác, từ đó suy ra nhanh các quy tắc nhân, lũy thừa và khai căn.

### Bước 4: Kết nối với ODE

Thực hành chuyển từ cặp nghiệm phức liên hợp của phương trình đặc trưng sang cặp nghiệm thực dạng $$ e^{\alpha t}\cos(\beta t) $$ và $$ e^{\alpha t}\sin(\beta t) $$.

### Các checkpoint

- Bạn có chuyển đổi qua lại thành thạo giữa dạng $$ x+iy $$ và $$ re^{i\theta} $$ không?
- Bạn có giải thích được ý nghĩa hình học của phép nhân hai số phức không?
- Bạn có biết cách trích nghiệm thực cho ODE tuyến tính bậc hai từ nghiệm phức của phương trình đặc trưng không?

## Ví dụ được giải chi tiết

### Ví dụ 1: Phép toán đại số với số phức

Cho $$ z_1=2+3i $$ và $$ z_2=1-4i $$. Khi đó tổng là $$ z_1+z_2=3-i $$, còn tích là $$ z_1z_2=(2+3i)(1-4i)=2-8i+3i-12i^2=14-5i $$. Phép tính tuân theo đúng quy tắc đại số thông thường kèm điều kiện $$ i^2=-1 $$.

### Ví dụ 2: Biểu diễn ở dạng cực

Xét $$ z=1+\sqrt{3}i $$. Mô-đun của $$ z $$ là $$ \lvert z \rvert=\sqrt{1+3}=2 $$. Vì

$$
\cos \theta=\frac{1}{2},\qquad \sin \theta=\frac{\sqrt{3}}{2},
$$

ta suy ra $$ \theta=\frac{\pi}{3} $$. Do đó

$$
z=2\left(\cos \frac{\pi}{3}+i\sin \frac{\pi}{3}\right)=2e^{i\pi/3}.
$$

### Ví dụ 3: Căn bậc ba của đơn vị

Giải phương trình $$ z^3=1 $$. Viết $$ 1=e^{i2k\pi} $$ (với $$ k\in\mathbb{Z} $$), ta thu được ba nghiệm phân biệt ứng với $$ k=0,1,2 $$ là $$ z_k=e^{i2k\pi/3} $$. Cụ thể:

$$
1,\qquad -\frac12+\frac{\sqrt3}{2}i,\qquad -\frac12-\frac{\sqrt3}{2}i.
$$

Cách biểu diễn ở dạng mũ giúp việc khai căn bậc $$ n $$ trở nên trực tiếp và hệ thống.

### Ví dụ 4: Nghiệm phức của ODE

Xét phương trình $$ y''+2y'+5y=0 $$. Phương trình đặc trưng là $$ r^2+2r+5=0 $$, có hai nghiệm $$ r=-1\pm 2i $$. Từ đó ta có nghiệm phức $$ e^{(-1+2i)t}=e^{-t}e^{2it} $$. Áp dụng công thức Euler

$$
e^{2it}=\cos 2t+i\sin 2t,
$$

ta tách phần thực và phần ảo để thu được hai nghiệm thực độc lập tuyến tính là $$ e^{-t}\cos 2t $$ và $$ e^{-t}\sin 2t $$.

## Câu hỏi khái niệm

1. Vì sao dạng cực của số phức lại thuận tiện hơn dạng đại số khi thực hiện phép nhân, lũy thừa và khai căn?
2. Công thức Euler liên kết hàm mũ với dao động lượng giác như thế nào?
3. Vì sao nghiệm phức của phương trình đặc trưng với hệ số thực lại dẫn đến nghiệm thực cho phương trình vi phân?

## Bài toán ứng dụng

1. Trong mạch điện xoay chiều, vì sao biên độ và pha của tín hiệu thường được biểu diễn bằng số phức?
2. Trong dao động cơ học tắt dần, nghiệm dạng $$ e^{-\alpha t}\cos \beta t $$ cho biết thông tin gì về biên độ và tần số dao động?
3. Trong biến đổi Fourier, vì sao hàm sóng phức $$ e^{ix\xi} $$ thường gọn hơn khi dùng thay cho sin và cos tách rời?

## Chiến lược giảng dạy tương tác

### Câu hỏi nên hỏi trên lớp

- Nếu nhân một số phức với $$ i $$, vị trí điểm biểu diễn trên mặt phẳng phức thay đổi thế nào?
- Vì sao số phức là công cụ gọn hơn so với việc chỉ dùng sin và cos khi phân tích dao động?
- Giữa hai dạng $$ x+iy $$ và $$ re^{i\theta} $$, dạng nào thuận tiện hơn cho phép nhân và phép lũy thừa?

### Hoạt động gợi ý

- Cho sinh viên biểu diễn một số phức lên mặt phẳng phức rồi đọc mô-đun và argument.
- Tổ chức bài tập chuyển đổi nhanh giữa dạng đại số và dạng cực.
- Chia nhóm giải nhanh các phương trình đặc trưng có nghiệm phức và viết nghiệm thực tương ứng của ODE.

## Phân hóa học tập

### Hỗ trợ sinh viên gặp khó khăn

- Sử dụng nhiều hình vẽ minh họa trên mặt phẳng phức.
- Luyện vững liên hợp, mô-đun và công thức Euler trước khi sang bài toán căn bậc $$ n $$.
- Tăng cường bài tập chuyển đổi giữa $$ x+iy $$ và $$ re^{i\theta} $$.

### Thử thách cho sinh viên khá giỏi

- Chứng minh công thức De Moivre bằng phương pháp quy nạp.
- Tìm tất cả các căn bậc bốn của một số phức cho trước và biểu diễn chúng trên mặt phẳng phức.
- Giải thích vì sao các nghiệm phức của phương trình đặc trưng hệ số thực luôn xuất hiện thành từng cặp liên hợp.

## Tóm tắt dễ nhớ

Số phức là ngôn ngữ gọn gàng cho phép quay và dao động. Dạng đại số thuận tiện cho phép cộng và nhân trực tiếp, dạng cực thể hiện rõ hình học và giúp tính lũy thừa, khai căn nhanh chóng, còn công thức Euler $$ e^{i\theta}=\cos\theta+i\sin\theta $$ là cầu nối trực tiếp giữa đại số, lượng giác và nghiệm dao động của phương trình vi phân.

## Video tham khảo

- Xem trước: [Taylor Series of the Exponential Function and Euler's Formula!](https://www.youtube.com/watch?v=H0Zbg_CqMCs) — Steve Brunton, tiếng Anh. Suy ra công thức Euler từ chuỗi Taylor của hàm mũ, nền tảng cho nghiệm đặc trưng phức.
- [What's so special about Euler's number e? | Chapter 5, Essence of calculus](https://www.youtube.com/watch?v=m2MIpDrF7Es) — 3Blue1Brown, tiếng Anh. Giải thích vì sao hàm mũ cơ số $$ e $$ không đổi qua phép lấy đạo hàm.
- [Complex Numbers and Euler's Formula | MIT 18.03SC Differential Equations, Fall 2011](https://www.youtube.com/watch?v=sn3orkHWqUQ) — MIT OpenCourseWare, tiếng Anh. Bài giảng ngắn của MIT về số phức và công thức Euler theo đúng cách vận dụng trong khóa 18.03.

## Tài liệu tham khảo

- Boyce & DiPrima, *Elementary Differential Equations*.
- Churchill & Brown, *Complex Variables and Applications*.
