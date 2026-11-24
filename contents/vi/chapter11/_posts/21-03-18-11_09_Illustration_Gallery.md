---
layout: post
title: "Bộ Minh Họa Chương 11"
chapter: '11'
order: 9
owner: Lê Minh Hoàng
lang: vi
categories:
- chapter11
lesson_type: optional
---

Phương trình Laplace và Poisson là chương giàu trực giác hình học bậc nhất trong toàn khóa học: nhìn mặt cong yên ngựa của hàm điều hòa, ta thấy ngay vì sao cực đại không bao giờ nằm ở giữa miền; nhìn lưới đường đẳng thế và đường dòng cắt nhau vuông góc $90^\circ$, ta đọc được cả tĩnh điện học lẫn thủy động lực học trong cùng một bức tranh!

## Bản đồ kiến thức nền: Bốn cấu trúc hình học cần quan sát trong Gallery Chương 11

1. **Mặt Yên ngựa và Nguyên lý Cực đại**:
   Mọi điểm bên trong của nghiệm $\Delta u = 0$ đều không có đỉnh nhô hay hố trũng; kéo thay đổi nhiệt độ trên một cạnh biên lập tức làm toàn bộ mặt bên trong điều chỉnh mượt mà theo.
2. **Suy giảm Phổ trên Hình chữ nhật & Đĩa tròn**:
   Quan sát các mode $\sinh(n\pi y/a)$ và $(r/R)^n$: dao động biên tần số cao bị xóa sạch ngay khi bước vào trong vài phần trăm kích thước miền.
3. **Hàm Green và Nguồn Ảnh Đối xứng**:
   Nhìn đỉnh logarit sắc nhọn tại vị trí đặt nguồn điểm $y$ và cách nguồn ảnh ảo ngoài biên kéo toàn bộ đường mức trên $\partial\Omega$ về đúng cao độ $0$.
4. **Lưới Trực giao của Thế vận tốc / Điện thế và Đường dòng / Đường sức**:
   Các đường $\phi = \text{const}$ và $\psi = \text{const}$ tạo thành mạng lưới các ô vuông nhỏ vô cùng ở mọi nơi (trừ điểm đình trệ)—dấu hiệu thị giác đặc trưng của hàm điều hòa 2D.

## Mục Đích Của Bài Hỗ Trợ

Bài học này tập hợp toàn bộ các hình minh họa của Chương 11 vào một không gian ôn tập trực quan thống nhất. Phương trình Laplace và phương trình Poisson giới thiệu lớp bài toán elliptic ở dạng cổ điển rõ nét nhất: trạng thái cân bằng thay cho tiến hóa theo thời gian, dữ liệu biên chi phối phần bên trong miền, và các tính chất định tính giữ vai trò quan trọng ngang với các công thức nghiệm tường minh. Bộ minh họa giúp kết nối liền mạch các chủ đề này xuyên suốt chương.

Các bài chính lần lượt đi qua hình học miền, số hạng nguồn, các nguyên lý định tính, biểu diễn nghiệm bằng hàm Green và các ứng dụng vật lý. Trang tổng hợp này giúp người học đối chiếu toàn bộ bức tranh trong cùng một giao diện: miền chữ nhật so với miền tròn, bài toán không nguồn so với bài toán có nguồn, tính chất giá trị trung bình so với nguyên lý cực đại, và lý thuyết hàm điều hòa khi áp dụng vào tĩnh điện và dòng chảy thế. Góc nhìn tổng thể này hữu ích trước khi khóa học chuyển sang giải tích hàm và lý thuyết nghiệm yếu ở Chương 12.

## Cách Sử Dụng Bài Này

Nên xem bộ minh họa theo đúng thứ tự các bài học. Sau mỗi hình, hãy đối chiếu lại với bài giảng tương ứng và xác định cấu trúc toán học đang được minh họa: vai trò chi phối của dữ liệu biên, lựa chọn hệ tọa độ theo hình học miền, tác động của nguồn bên trong, tính chất chặt chẽ của hàm điều hòa, đáp ứng của miền qua hàm Green, hay ý nghĩa vật lý của nghiệm. Nhờ đó, trang này trở thành cầu nối giữa lý thuyết elliptic hình thức và trực giác hình học.

Đây cũng là tài liệu ôn tập hữu ích trước khi bước sang Chương 12, vì nó làm rõ những đặc trưng của PDE elliptic sẽ được diễn đạt lại bằng ngôn ngữ giải tích hàm.


### Khung giải thích (nên đọc chậm): Tự kiểm chứng Nguyên lý Trung bình rời rạc bằng phép tính 4 điểm lân cận

Khi rời rạc hóa $\Delta u = 0$ trên lưới vuông bước $h$ bằng sai phân 5 điểm, ta có:
$$\frac{u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j}}{h^2} = 0 \iff u_{i,j} = \frac{u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}}{4}.$$
Giả sử một nút lưới bên trong có 4 nút lân cận mang nhiệt độ lần lượt là $10^\circ\text{C}$, $20^\circ\text{C}$, $30^\circ\text{C}$ và $60^\circ\text{C}$:
- Nhiệt độ cân bằng tại nút giữa bắt buộc là:
  $$u_{i,j} = \frac{10 + 20 + 30 + 60}{4} = \mathbf{30^\circ\text{C}}.$$
- Nhận xét ngay: $10 < \mathbf{30} < 60$! Chính quy tắc trung bình 4 lân cận giản dị này giải thích hoàn hảo vì sao không một nút bên trong nào có thể nóng hơn tất cả lân cận của nó!
## Gallery Nhúng Trực Tiếp

{% include interactive-frame.html
  title="Bộ Minh Họa Chương 11"
  description="Không gian trực quan hỗ trợ cho hàm điều hòa, cấu trúc bài toán biên, phương trình Poisson có nguồn, phương pháp hàm Green, và các ứng dụng chính của Laplace-Poisson."
  path="interactives/chapter11/index.html"
  height="980px"
%}

## Câu Hỏi Gợi Ý Khi Học

1. Hình minh họa nào nhấn mạnh cấu trúc nghiệm tường minh, và hình nào nhấn mạnh tính chất định tính mà không cần giải PDE tường minh?
2. Ở những ví dụ nào hình học miền và dữ liệu biên thể hiện rõ nhất vai trò quyết định đối với phần bên trong miền?
3. Các hình ứng dụng đã diễn giải cùng một khuôn khổ elliptic trong những bối cảnh vật lý khác nhau như thế nào?

## Liên Kết Tới Các Bài Học Chính

- [11.01 Phương trình Laplace: Giới thiệu]({{ site.baseurl }}/contents/vi/chapter11/11_01_Laplace_Equation_Introduction/)
- [11.02 Tách biến trong hình chữ nhật]({{ site.baseurl }}/contents/vi/chapter11/11_02_Separation_Variables_Rectangles/)
- [11.03 Phương trình Laplace trong tọa độ cực]({{ site.baseurl }}/contents/vi/chapter11/11_03_Laplace_Polar_Coordinates/)
- [11.04 Phương trình Poisson]({{ site.baseurl }}/contents/vi/chapter11/11_04_Poisson_Equation/)
- [11.05 Tính chất trung bình và cực đại]({{ site.baseurl }}/contents/vi/chapter11/11_05_Mean_Value_Maximum_Principle/)
- [11.06 Hàm Green cho phương trình Laplace]({{ site.baseurl }}/contents/vi/chapter11/11_06_Greens_Functions_Laplace/)
- [11.07 Ứng dụng: tĩnh điện học]({{ site.baseurl }}/contents/vi/chapter11/11_07_Applications_Electrostatics/)
- [11.08 Ứng dụng: dòng chảy chất lỏng]({{ site.baseurl }}/contents/vi/chapter11/11_08_Applications_Fluid_Flow/)

## Video tham khảo

- xem trước: [PDE 101: Separation of Variables! ...or how I learned to stop worrying and solve Laplace's equation](https://www.youtube.com/watch?v=VjWtMl6vQ3Q) — Steve Brunton, tiếng Anh. Minh họa nghiệm phương trình Laplace trên hình chữ nhật để đối chiếu với bộ hình trực quan.
- [Laplace's Equation and Potential Flow](https://www.youtube.com/watch?v=zN0zDrQimXU) — Steve Brunton, tiếng Anh. Minh họa trực quan các ví dụ về dòng chảy thế.
- [Divergence and curl:  The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) — 3Blue1Brown, tiếng Anh. Giải thích trực quan các trường vector liên quan đến các hình minh họa trong chương.
