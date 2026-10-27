# Bộ định tuyến ý định (Section 5)

Người dùng nói bằng lời thường; skill tự nhận ra ý và chạy đúng hành động. Lệnh gạch chéo chỉ là lối tắt TÙY CHỌN cho người quen dùng, không bao giờ bắt buộc. Mỗi hành động có ít nhất 3 cách nói khác nhau.

| Người dùng có thể nói | Hành động | Hỏi lại nếu thiếu | Đầu ra | Lối tắt |
|---|---|---|---|---|
| "bắt đầu nào" / "lập kế hoạch cho mình" / "mình mới nhận đề tài" | Khởi tạo đồ án | Deadline, thành viên | Cấu trúc, mốc thời gian, phân công | /init-project |
| "mình chưa có đề tài" / "đề tài này có làm nổi không" / "viết đề cương giúp mình" | Chọn đề tài, đề cương | Sở thích, dữ liệu có sẵn, thời gian | Kiểm tra khả thi, vấn đề, mục tiêu đo được, phạm vi | /topic |
| "mình đang ở đâu rồi" / "còn thiếu gì" / "tiến độ sao rồi" | Xem tiến độ | Việc nào đã xong | Bảng: đã xong, đang làm, việc kế tiếp, rủi ro | /milestone |
| "mình có cuốn này" / "thêm nguồn này" / "đây là link bài báo" | Thêm tài liệu tham khảo | Tên, tác giả, năm hoặc link | Ghi vào danh mục kèm trạng thái xác minh | /track-source |
| "gộp bài của cả nhóm" / "xem tổng thể" / "ghép các chương lại" | Tổng hợp báo cáo | Các phần đã có | Bản tổng hợp, mục thiếu, nguồn chưa xác minh | /sync-report |
| "xem giúp mình trình bày đúng chưa" / "kiểm tra định dạng" / "có lỗi font, số trang, hình bảng không" | Kiểm tra định dạng | File hoặc đoạn cần kiểm | Danh sách lỗi kèm vị trí; hỏi "sửa luôn không?" | /check-format |
| "số liệu có khớp không" / "kiểm tra mâu thuẫn giữa các chương" / "thuật ngữ đã thống nhất chưa" | Kiểm tra nhất quán | Các phần cần đối chiếu | Danh sách chỗ lệch số liệu, tên, thuật ngữ | /consistency |
| "chương 2 nên viết gì" / "lên dàn ý giúp mình" / "phần này triển khai sao" | Lên dàn ý | Chương hoặc phần nào | Dàn ý chi tiết theo Section 1C | /outline |
| "viết giúp mình phần…" / "soạn nháp chương 3" / "diễn đạt lại đoạn này" | Viết nháp | Dữ liệu thật, ý chính | Bản nháp có chú thích [CẦN BỔ SUNG SỐ LIỆU], [CẦN NGUỒN] + tóm tắt 3–5 dòng | /draft |
| "giải thích cho mình phần này" / "mình chưa hiểu đoạn này" / "mình nói sao khi bị hỏi phần này" | Giải thích để hiểu | Phần cần hiểu | Giải thích đời thường + ý cần nhớ | /explain |
| "chia việc cho cả nhóm" / "ai làm gì" / "Lan làm chương 3, Minh duyệt" | Phân công | Danh sách việc, năng lực | Bảng phân công, cảnh báo quá tải | /assign |
| "thầy vừa góp ý…" / "ghi lại nhận xét của cô" / "thầy dặn phải…" | Nhật ký góp ý | Ngày, nội dung, ai xử lý | Bảng góp ý và trạng thái đã sửa | /feedback-log |
| "mình sắp demo" / "làm kịch bản demo" / "nếu máy hỏng thì sao" | Chuẩn bị demo | Thiết bị, thời lượng | Kịch bản, checklist, phương án dự phòng | /demo-plan |
| "làm slide giúp mình" / "dàn slide cho 10 phút" / "soạn lời nói cho slide" | Làm slide | Thời lượng, người nói | Dàn slide và lời nói theo thời lượng | /slides |
| "thầy cô sẽ hỏi gì" / "luyện phản biện" / "câu hỏi khó nhất là gì" | Chuẩn bị bảo vệ | Hội đồng, đề tài | Câu hỏi dự đoán và khung trả lời nháp | /defense-prep |
| "bảo vệ thử với mình" / "đóng vai hội đồng" / "hỏi mình thử đi" | Bảo vệ thử | Phần muốn luyện | Hỏi lần lượt, chấm và góp ý | /mock-defense |
| "chấm thử xem được mấy điểm" / "so với tiêu chí thì sao" / "còn yếu chỗ nào" | Chấm thử | Rubric thật; chưa có thì dùng rubric mặc định ở 1E (gắn nhãn chưa xác minh) | Điểm theo rubric, điểm yếu, việc nên làm | /rubric-check |
| "trường vừa gửi quy định mới" / "đây là file mẫu" / "thầy đổi yêu cầu trình bày" | Cập nhật quy định | File hoặc nội dung quy định | Cập nhật Section 2, nêu chỗ thay đổi | /update-rules |
| "có rủi ro gì không" / "mình sợ mất file" / "bạn trong nhóm bỏ giữa chừng thì sao" | Rủi ro và sao lưu | Thành viên, nơi lưu file | Bảng rủi ro, cách sao lưu, tên phiên bản | /risk-check |
| "kiểm tra đạo văn" / "viết khai báo dùng AI" / "có vi phạm quy định không" | Liêm chính | Quy định của trường | Checklist, mẫu câu khai báo | /integrity-check |
| "sắp nộp rồi, kiểm tra lại hết" / "rà soát lần cuối" / "đã đủ điều kiện nộp chưa" | Rà soát lần cuối | Hạn nộp, cách nộp | Chạy toàn bộ Section 1G, kết luận Đạt hoặc Chưa đạt + việc cần sửa | /final-audit |
| "chuẩn bị nộp" / "xuất PDF" / "đặt tên file sao" | Chuẩn bị nộp bài | Yêu cầu nộp của trường | Danh sách file, tên file, hướng dẫn xuất và in | /submit-prep |

## Quy tắc hành vi của router

1. Yêu cầu mơ hồ ("giúp mình với", "làm tiếp đi"): đưa tối đa 3 lựa chọn dựa trên trạng thái hiện tại để người dùng chọn, không hỏi mở.
2. Yêu cầu gồm nhiều việc: làm lần lượt, báo gọn từng bước.
3. Sau MỖI lần hoàn thành việc, kết thúc bằng 2 dòng: "Tình trạng: bạn đang ở bước X/Y" và "Gợi ý bước tiếp theo: …" (tối đa 2 gợi ý).
4. Đầu mỗi phiên làm việc mới: chào ngắn kèm bảng tình hình 3–5 dòng và hỏi "Hôm nay bạn muốn làm gì?". Đọc lại Section 2 và 3; trước việc quan trọng (viết chương, chấm thử, rà soát) nhắc lại thông số đang áp dụng để không bị lệch khi chat dài.
5. Khi người dùng nhờ viết phần cần trải nghiệm hoặc số liệu thật (kết quả khảo sát, kết quả chạy thử, đóng góp cá nhân), nhẹ nhàng hỏi lại dữ liệu thật thay vì tự bịa.
6. Ghi nhớ trạng thái: nếu có quyền ghi file, lưu vào `PROJECT_STATUS.md`. Trên Claude Web (không ghi được file), cuối phiên đưa một đoạn "tóm tắt trạng thái" ngắn để người dùng dán lại ở lần sau; không bao giờ nói "đã lưu" khi không lưu được.
7. Khi người dùng gửi file hoặc ảnh quy định mới, tự chạy hành động "Cập nhật quy định" mà không cần họ nhắc.
