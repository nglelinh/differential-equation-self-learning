---
layout: post
title: "01-11 Lịch sử Phương trình Vi phân Cấp Một"
chapter: '01'
order: 11
owner: Course Team
lang: vi
categories:
- chapter01
---

## Mục tiêu
Bài này dựng lại lịch sử hình thành của phương trình vi phân thường cấp một từ cơ học, thiên văn học, dân số học và kỹ thuật điện. Sinh viên nên nhìn Chương 01 không phải như một danh sách mẹo giải, mà như câu trả lời có tổ chức đầu tiên của toán học cho bài toán mô hình hóa sự biến thiên.

## Kiến thức nền
Sinh viên nên nắm ngôn ngữ toán học của Chương 00 và các phương pháp giải ở Chương 01. Mục tiêu ở đây là hiểu ai đã tạo ra các phương pháp ấy, vì sao chúng xuất hiện, và bằng cách nào các bài toán mô hình hóa đã thúc đẩy lý thuyết đi lên.

## Câu chuyện mở màn
Brussels, năm 1838. Pierre-Francois Verhulst nhìn vào các bảng dân số và thấy một điều rất đáng ngờ: nếu cứ tin hoàn toàn vào luật tăng trưởng mũ của Malthus, dân số sẽ tăng mãi như thể thức ăn, đất canh tác và bệnh tật không hề tồn tại. Xung đột ở đây rất thực tế. Nhà nước cần ước lượng lương thực, thuế và sức chứa đô thị; một mô hình đẹp trên giấy nhưng bỏ qua giới hạn vật chất sẽ dẫn đến dự báo vô nghĩa.

Verhulst không giải quyết chuyện đó bằng một khẩu hiệu xã hội học, mà bằng một phương trình cấp một. Ông sửa luật tăng trưởng quen thuộc $$y' = ry$$ thành $$y' = ry\left(1 - \frac{y}{K}\right)$$. Ngay trong công thức, toán học kể luôn câu chuyện: khi $$y$$ còn nhỏ so với sức chứa $$K$$, tốc độ tăng gần như là $$ry$$; nhưng khi $$y$$ tiến gần $$K$$, thừa số $$1 - \frac{y}{K}$$ kéo tốc độ tăng xuống gần $$0$$. Ví dụ, nếu $$K = 1000$$ và hiện có $$y = 900$$, thì tốc độ tăng chỉ còn khoảng $$0.1ry$$, nhỏ hơn rất nhiều so với mô hình mũ. Đó là khoảnh khắc phương trình vi phân cấp một hiện ra như một ngôn ngữ mô hình hóa thật sự: ngắn, cục bộ, nhưng đủ thông minh để phản ánh thế giới.

## Mạch truyện lớn
Mạch truyện lớn của chương bắt đầu ở cuối thế kỷ XVII với Newton và Leibniz, khi đạo hàm còn gắn chặt với chuyển động. Sang thế kỷ XVIII, Bernoulli, Euler, Clairaut và Riccati lần lượt khám phá ra rằng có những dạng phương trình đủ đặc biệt để ta tách biến, nhân tử hóa hoặc đổi ẩn mà giải được. Từ đây, phương trình vi phân cấp một bắt đầu có “họ hàng”, có kiểu, có phương pháp riêng.

Thế kỷ XIX thêm một tầng sâu hơn. Cauchy, Lipschitz, Picard và Lindelöf đặt câu hỏi khó hơn nhiều: không chỉ “giải thế nào” mà còn “khi nào nghiệm thực sự tồn tại, duy nhất và đáng tin”. Vì vậy, nếu phần kỹ thuật của Chương 01 là một hộp công cụ, thì phần lịch sử của nó là câu chuyện về việc loài người học cách biến một hiện tượng thành luật cục bộ, biến luật cục bộ thành phương pháp, rồi biến phương pháp thành lý thuyết.

## Chủ đề này phát sinh từ đâu, giải quyết vấn đề gì, và ai đã vướng ở đâu?
**Nguồn gốc.** Phương trình vi phân cấp một sinh ra từ những hiện tượng rất gần đời sống: vật rơi có lực cản, cốc cà phê nguội đi, bể muối bị pha loãng, quần thể tăng trưởng, điện tích trên tụ điện suy giảm. Newton, Leibniz, Bernoulli và Euler không ngồi xuống để “phát minh một chapter trong giáo trình”; họ bị ép bởi những quá trình đang thay đổi theo thời gian và cần một luật cục bộ để ghi lại.

**Bài toán họ đang cố giải.** Họ muốn trả lời câu hỏi ngắn mà sâu: tại thời điểm này, tốc độ biến thiên phụ thuộc vào trạng thái hiện tại như thế nào? Từ đó mới xuất hiện các dạng tách biến, tuyến tính, exact, Bernoulli, logistic và các mô hình trộn chất hay mạch điện mà Chương 01 dạy ngày nay.

**Khó khăn và nút thắt.** Khó ở chỗ ban đầu các phương pháp xuất hiện rời rạc như những mẹo riêng. Bernoulli, Clairaut, Riccati và Euler mỗi người chạm vào một lớp phương trình khác nhau, nhưng chưa có một lý thuyết thống nhất. Sang thế kỷ XIX, Cauchy, Lipschitz, Picard và Lindelöf mới buộc toán học đối diện câu hỏi khó hơn: nếu mô hình đã viết ra, khi nào nó thực sự có nghiệm và nghiệm ấy có đáng tin là duy nhất hay không.

## Những bước ngoặt của câu chuyện
1. **Giới thiệu phương trình vi phân.** Newton và Leibniz tạo ra khung khái niệm, nhưng các giáo trình của Euler mới làm cho việc phân loại theo bậc và kiểu trở nên có hệ thống. Ngay cả cụm từ “phương trình vi phân” cũng chỉ thực sự phổ biến khi vi tích phân trưởng thành.
2. **Phương trình tách biến.** Đây là một trong những phương pháp cổ nhất vì các nhà giải tích đầu tiên thường có thể sắp xếp lại biến và tích phân trực tiếp. Các bài báo của gia đình Bernoulli và các trình bày của Euler giúp chuẩn hóa kỹ thuật này.
3. **Phương trình tuyến tính cấp một.** Phương pháp nhân tử tích phân lớn lên từ công trình thế kỷ XVIII của Euler và Lagrange rồi trở thành thao tác kinh điển trong giáo trình. Nó cho thấy có những phương trình có thể giải nhờ biến đổi cấu trúc chứ không chỉ nhờ đoán.
4. **Phương trình toàn phần chính xác.** Clairaut và sau đó là lý thuyết Pfaff làm rõ khi nào một biểu thức vi phân xuất phát từ một hàm thế ẩn. Khái niệm exact nối ODE với hình học và vi phân toàn phần, báo trước lý thuyết dạng vi phân sau này.
5. **Các phép thế.** Phương trình Bernoulli, phương trình thuần nhất, phương trình Clairaut hay Riccati đều giữ lại một mẫu đại số có thể khai thác. Lịch sử của chúng cho thấy toán học học cách phân loại phương trình qua đối xứng và khả năng quy giảm.
6. **Tồn tại và duy nhất.** Cauchy phát biểu rõ ràng bài toán giá trị đầu ở đầu thế kỷ XIX. Lipschitz đưa ra điều kiện mang tên mình, còn Picard và Lindelöf cho thấy phép lặp liên tiếp có thể chứng minh sự tồn tại và duy nhất.
7. **Mô hình dân số và trộn chất.** Luật dân số năm 1798 của Malthus cho tăng trưởng mũ thuần túy, còn các bài báo năm 1838 và 1845 của Verhulst đưa vào phương trình logistic để mô tả bão hòa. Các bài toán trộn bể chứa lớn lên từ kỹ thuật hóa học và hệ thống dòng chảy thực tế.
8. **Cơ học và mạch điện.** Các mô hình lực cản kiểu Newton cho ra ODE cấp một của vật rơi và làm nguội. Các định luật mạch của Kirchhoff trong thế kỷ XIX rồi kỹ thuật điện sau này biến phương trình tuyến tính cấp một thành trung tâm của các hệ RC và RL.
9. **Phương trình tự trị và đường pha.** Lý thuyết định tính của Poincaré vào thập niên 1880 dạy các nhà toán học nghiên cứu cân bằng và hành vi dài hạn mà không cần công thức tường minh. Đó là một bước nhảy tư duy vượt xa việc chỉ thao tác ký hiệu.

## Những cảnh đáng nhớ
Câu chuyện cấp một mở ra cùng lúc với chính phép tính biến thiên. *Principia* của Newton năm 1687 và các bài báo vi phân của Leibniz tạo ra ngôn ngữ của tốc độ thay đổi, khiến người ta lần đầu viết được luật cục bộ thay vì chỉ mô tả một quan hệ tĩnh. Sang thế kỷ XVIII, các bài báo của Bernoulli và Euler tổ chức những phương pháp giải ban đầu, còn công trình của Riccati sinh ra một trong những phương trình phi tuyến cấp một kinh điển. Từ đây, ODE cấp một bắt đầu có họ hàng, có kiểu, và có mẹo giải riêng.

Thế kỷ XIX biến mẹo thành lý thuyết. Các bài giảng của Cauchy và phương pháp xấp xỉ của Picard biến bài toán giá trị đầu thành một đối tượng nghiêm ngặt: không chỉ hỏi “giải thế nào”, mà hỏi khi nào nghiệm tồn tại và có duy nhất hay không. Cùng lúc, mô hình logistic của Verhulst khiến ODE cấp một trở thành công cụ trung tâm của động lực dân số, cho thấy một phương trình ngắn vẫn có thể kể câu chuyện bão hòa, giới hạn tài nguyên và dự báo xã hội.

## Vì sao biết lịch sử này làm toán bớt khô
Chương 01 có thể trông “dễ” vì công thức ngắn. Nhưng về mặt lịch sử, đây là nơi toán học lần đầu học được cách mã hóa một định luật biến thiên thay vì chỉ mô tả một quan hệ tĩnh. Đó là khoảnh khắc mô hình bắt đầu thật sự chuyển động trên trang giấy.

Chương này cũng dạy một bài học bền vững: lý thuyết và ứng dụng phát triển cùng nhau. Các phương pháp giải không ra đời trong chân không; chúng được phát minh vì các bài toán cụ thể trong thiên văn, cơ học, dòng chảy, hóa học và dân số đã đòi hỏi chúng.

## Câu hỏi thảo luận
1. Vì sao các phương trình cấp một lại xuất hiện gần như ngay sau khi vi tích phân được phát minh?
2. Đâu là đột phá sâu hơn: giải được nhiều dạng phương trình hơn, hay chứng minh được sự tồn tại và duy nhất?
3. Vì sao phương trình logistic là một bước tiến khái niệm so với tăng trưởng mũ đơn giản?

## Gợi ý trả lời câu hỏi thảo luận
1. Vì ngay khi có đạo hàm, các nhà toán học đã có cách viết luật biến thiên cục bộ của chuyển động, làm nguội, pha trộn hay tăng trưởng. Phương trình cấp một là hình thức tự nhiên và tối giản nhất của ý tưởng “tốc độ thay đổi hiện tại phụ thuộc vào trạng thái hiện tại”.
2. Giải được thêm nhiều dạng phương trình là một tiến bộ kỹ thuật lớn, nhưng tồn tại và duy nhất là bước sâu hơn về khái niệm. Nó trả lời câu hỏi liệu mô hình có thực sự xác định một diễn biến hay không, và liệu dữ liệu ban đầu có đủ để chọn ra đúng một quỹ đạo vật lý hay không.
3. Phương trình logistic vượt lên trên tăng trưởng mũ vì nó đưa phản hồi và giới hạn tài nguyên vào ngay trong mô hình. Nhờ vậy, nó cho thấy tăng trưởng không phải lúc nào cũng tăng mãi, mà có thể tự điều chỉnh quanh một mức cân bằng.

## Tóm tắt kiến thức toán học
- Phương trình vi phân cấp một ra đời từ nhu cầu mô tả luật biến thiên cục bộ của các hiện tượng như nguội đi, pha trộn, nạp xả điện và tăng trưởng dân số.
- Ý tưởng trung tâm là viết tốc độ thay đổi hiện tại dưới dạng một hàm của trạng thái hiện tại, từ đó sinh ra các lớp phương trình tách biến, tuyến tính, exact và logistic.
- Ví dụ trong câu chuyện là phương trình logistic $$y' = ry\left(1 - \frac{y}{K}\right)$$, cho thấy mô hình cấp một có thể tự điều chỉnh theo giới hạn tài nguyên.

## Tài liệu tham khảo
- Boyce và DiPrima, *Elementary Differential Equations and Boundary Value Problems*. Hữu ích để nối Chương 01 hiện đại với các gốc cổ điển của nó.
- Ross, *Differential Equations*. Ngắn gọn và rõ về các phương pháp cấp một cùng bối cảnh mô hình hóa.
- Ivor Grattan-Guinness, *The Rainbow of Mathematics*. Cung cấp bối cảnh lịch sử cho giải tích thế kỷ XVIII và XIX.
