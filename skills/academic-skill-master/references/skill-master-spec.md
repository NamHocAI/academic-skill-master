# Đặc tả SKILL_MASTER.md

File chính duy nhất, có YAML frontmatter (`name`, `description`), gồm ĐÚNG 5 section. Dùng bảng và checklist, ưu tiên cô đọng.

- Độ dài: 500–800 dòng cho Claude Web, Claude Code và Codex; 300–400 dòng cho Cursor.
- File phụ (ngoại lệ được phép): `REFERENCES.md`, `PROJECT_STATUS.md`, `FEEDBACK_LOG.md`. Mẫu ở `assets/`. Chỉ tạo khi môi trường cho ghi file; nếu không, đưa nội dung vào chat.
- Mọi lần tạo file đều theo khung dưới đây để kết quả nhất quán.

## Khung mẫu

```markdown
---
name: do-an-<ten-ngan>
description: <dưới khoảng 1000 ký tự: nói rõ skill dùng cho đồ án nào và tự kích hoạt khi người dùng nhắn các việc như viết báo cáo, sửa định dạng, làm slide, chuẩn bị bảo vệ, phân công nhóm, tìm hoặc ghi nguồn, kiểm tra lần cuối>
---

# <Tên đồ án>

## Section 1: CORE ARCHITECTURE & DOMAIN PROTOCOL
## Section 2: TEMPLATE ENFORCEMENT & MECHANICAL STYLING RULES
## Section 3: AUTONOMOUS CITATION ENGINE
## Section 4: ADAPTIVE COLLABORATION MATRIX
## Section 5: NATURAL-LANGUAGE INTENT ROUTER
```

Quy tắc frontmatter:
- `name`: chữ thường, số, nối bằng gạch ngang, tối đa 64 ký tự, không chứa chữ "claude" hoặc "anthropic".
- `description`: dưới khoảng 1000 ký tự, KHÔNG chứa dấu `<` `>`. Các dấu `< >` trong khung trên chỉ là chỗ điền.
- `description` phải viết để skill tự kích hoạt khi người dùng nói câu đời thường liên quan đến đồ án: viết báo cáo, sửa định dạng, làm slide, chuẩn bị bảo vệ, phân công nhóm, tìm hoặc ghi nguồn, kiểm tra lần cuối. Nêu tên đề tài và tên trường để không nhầm với đồ án khác.

Codex dùng đúng frontmatter `name` + `description` như trên. Với Cursor (`.mdc`), frontmatter dùng `description`, `globs`, `alwaysApply: true` thay cho `name`; vẫn giữ nguyên 5 section.

---

## Section 1: CORE ARCHITECTURE & DOMAIN PROTOCOL

Dòng đầu cố định, nguyên văn:

> LƯU Ý: Hãy kiểm tra quy định của trường/khoa về việc sử dụng AI trong đồ án và khai báo đúng yêu cầu.

Ngay sau dòng đó, chép phần nguyên tắc từ `principles.md` dưới dạng rút gọn (xưng hô, không bắt gõ lệnh, liêm chính, chế độ AI theo câu 10, văn phong, giới hạn phải nói thật). Ghi rõ chế độ AI đang áp dụng.

### 1A. Mốc thời gian
- Lập từ deadline thật (câu 8). Ghi rõ ngày hôm nay lúc tạo file.
- Mỗi mốc có điều kiện hoàn thành rõ ràng, đo được (VD "Chương 1–2 đủ checklist, đã gửi thầy" thay vì "làm xong chương 2").
- Có mốc đệm 10–15% thời gian trước mỗi hạn chính.
- Bảng: Tuần / Ngày / Việc / Điều kiện hoàn thành / Người phụ trách.

### 1B. Chọn đề tài và đề cương
- Kiểm tra tính khả thi: đủ thời gian, đủ dữ liệu, phạm vi vừa sức.
- Xác định: vấn đề nghiên cứu, mục tiêu đo được, phạm vi và giới hạn, điểm khác biệt so với đồ án cũ.
- Đã có đề tài thì ghi lại các ý trên và đánh dấu chỗ còn yếu.

### 1C. Khung báo cáo hoàn chỉnh theo template trường
Gồm: bìa, trang phụ bìa, lời cam đoan, lời cảm ơn, mục lục, danh mục hình/bảng/viết tắt, tóm tắt (abstract), các chương, kết luận và hướng phát triển, tài liệu tham khảo, phụ lục.

Mỗi chương ghi: mục tiêu, nội dung bắt buộc, độ dài tham khảo, checklist hoàn thành. Chưa có template thì dùng khung chung của ngành và gắn nhãn "chưa xác minh".

**Logic xuyên suốt (bắt buộc kiểm).** Lập bảng:

| Mục tiêu (Chương 1) | Phương pháp | Kết quả (chương nào, mục nào) | Kết luận |
|---|---|---|---|

Mỗi mục tiêu ở Chương 1 phải có kết quả tương ứng ở chương cuối; mục tiêu nào không có kết quả thì báo ngay.

**Checklist chất lượng nội dung** (bắt buộc kiểm trước khi coi một chương là xong):
- [ ] Tổng quan và cơ sở lý thuyết: nêu đúng các khái niệm và nghiên cứu liên quan, rồi chỉ ra khoảng trống mà đề tài giải quyết; không liệt kê lan man.
- [ ] Phương pháp và dữ liệu: phương pháp phù hợp với mục tiêu và được mô tả đủ chi tiết để người khác làm lại được; dữ liệu có nguồn gốc rõ; khảo sát nêu cách lấy mẫu và ẩn danh.
- [ ] Phân tích và bàn luận: kết quả được giải thích chứ không chỉ trình bày; có so sánh với nghiên cứu hoặc sản phẩm khác; nêu hạn chế và hướng phát triển.

Chương nào thiếu một mục trên thì báo ngay và đề xuất bổ sung.

### 1D. Khung sản phẩm và demo (khóa theo ngành)
Chọn đúng dòng theo ngành (câu 1). Mỗi giai đoạn có "sản phẩm bàn giao" và "bằng chứng" (ảnh chụp, log, số liệu) để đưa vào báo cáo.

| Ngành | Chuỗi giai đoạn |
|---|---|
| CNTT | Yêu cầu → thiết kế → code → kiểm thử → triển khai → hướng dẫn cài đặt và sử dụng → kịch bản demo + bản demo dự phòng (video, ảnh chụp) |
| Marketing | Nghiên cứu thị trường → insight → chiến lược → kế hoạch và ngân sách → sản phẩm truyền thông → chỉ số đo lường → demo hoặc pitch |
| Kinh tế – Tài chính | Vấn đề → cơ sở lý thuyết → mô hình và giả thuyết → dữ liệu → phân tích → kết quả → khuyến nghị |
| Kỹ thuật | Yêu cầu → tính toán và thiết kế → mô hình hoặc mô phỏng → thử nghiệm → đánh giá sai số → kết luận |
| Thiết kế | Brief → nghiên cứu người dùng hoặc bối cảnh → ý tưởng → phác thảo → bản hoàn thiện → trình bày sản phẩm |
| Y – Dược | Câu hỏi nghiên cứu → tổng quan → phương pháp và đạo đức → thu thập số liệu → phân tích → bàn luận → kết luận |
| Luật | Vấn đề pháp lý → quy định hiện hành → án lệ hoặc tình huống → phân tích → kiến nghị |
| Ngành khác | Vấn đề → phương pháp → dữ liệu → kết quả → đánh giá (dựng theo câu 5 và 6) |

Bảng trong skill: Giai đoạn / Sản phẩm bàn giao / Bằng chứng đưa vào báo cáo / Hạn.

### 1E. Chiến lược theo rubric
- Từ câu 4, chia công sức theo trọng số điểm (phần chiếm 40% điểm không được làm qua loa).
- Liệt kê "điểm ăn tiền" của từng tiêu chí; cập nhật lại sau mỗi lần chấm thử.
- Chưa có rubric thật: chép rubric mặc định từ `default-rubric.md`, gắn nhãn "giả định – CHƯA XÁC MINH, cần đối chiếu với giảng viên". Có rubric thật thì thay hoàn toàn.

### 1F. Slide và bảo vệ
- Cấu trúc slide và kịch bản nói theo thời lượng (câu 8), phân bổ phần nói cho từng thành viên.
- Nguyên tắc slide: ít chữ, một ý chính mỗi slide, hình và số liệu có chú thích rõ, cỡ chữ đọc được từ cuối phòng, bố cục và màu thống nhất; slide cuối là kết luận và đóng góp.
- Chuẩn bị: câu mở đầu và câu kết; câu hỏi phản biện dự đoán kèm khung trả lời nháp; 3 câu hỏi khó nhất về điểm yếu của đề tài; câu hỏi riêng cho từng thành viên ("bạn đóng góp gì?").
- Chế độ "bảo vệ thử": đóng vai hội đồng hỏi lần lượt, chấm và góp ý.
- Theo câu 9: nếu demo trực tiếp, thêm checklist thiết bị (máy, sạc, mạng, cổng HDMI, tài khoản đăng nhập sẵn) và bản demo dự phòng.

### 1G. Cổng chất lượng trước khi nộp
Chạy lần lượt, mỗi mục là checklist:
- [ ] Nội dung: logic xuyên suốt khớp; checklist chất lượng nội dung đạt; mọi góp ý của giảng viên đã được xử lý.
- [ ] Nhất quán: số liệu, tên hệ thống, thuật ngữ và viết tắt giống nhau ở tóm tắt, các chương, kết luận và slide.
- [ ] Định dạng: khớp Section 2, gồm phân cấp, phân trang, hình, bảng; mọi hình và bảng đều có caption, số thứ tự, nguồn và được dẫn trong bài.
- [ ] Nguồn: khớp Section 3; số liệu có nguồn gốc.
- [ ] Sản phẩm: chạy được hoặc đủ file; có bản dự phòng.
- [ ] Liêm chính: đạo văn, khai báo AI, giấy phép ảnh, font, thư viện, dataset; đạo đức dữ liệu khảo sát (cách lấy mẫu, ẩn danh).
- [ ] Nộp bài: xuất PDF và kiểm tra font, mở lại file trên máy khác, đặt tên file đúng quy định, nộp sớm hơn hạn, danh sách file kèm theo, bản in và đóng quyển nếu cần.

---

## Section 2: TEMPLATE ENFORCEMENT & MECHANICAL STYLING RULES

Chỉ ghi thông số TRÍCH XUẤT từ template hoặc quy định của người dùng. Mọi ví dụ (Times New Roman, 13pt, 1.3, "CHƯƠNG 1", "Hình 1.1") chỉ để minh họa, KHÔNG dùng làm mặc định.

Mỗi thông số có cột Nguồn: "từ template" / "từ bạn khai" / "giả định – chưa xác minh". Ghi một dòng khóa ở đầu section: "Cấm AI tự đổi bất kỳ thông số nào đã khóa. Chỉ đổi khi người dùng gửi quy định mới (hành động Cập nhật quy định)."

Thông số nào chưa có: ghi "CHƯA CÓ – hỏi khi cần" thay vì tự điền.

1. **Typography Lock (Chữ).** Font, cỡ chữ thân bài, giãn dòng, giãn đoạn (trước/sau), căn lề văn bản (đều hai bên hay trái), thụt đầu dòng.
2. **Page Setup (Trang).** Lề Top/Bottom/Left/Right (cm), khổ giấy, hướng giấy.
3. **Pagination (Phân trang).**
   - Số trang: phần đầu (bìa, cam đoan, cảm ơn, mục lục, danh mục) không đánh hay đánh i, ii, iii; phần nội dung bắt đầu từ trang nào và đánh kiểu gì (1, 2, 3); trang bìa có tính không.
   - Vị trí và định dạng số trang (giữa hay phải, đầu hay cuối trang); header và footer có hay không, nội dung gì.
   - Ngắt trang: mỗi chương có bắt đầu ở trang mới không; tài liệu tham khảo và phụ lục có sang trang mới không.
   - Tránh lỗi: tiêu đề không nằm lẻ cuối trang; hình và bảng không bị tách khỏi caption; không có trang trắng thừa.
   - Mục lục: lấy đến cấp mấy; số trang trong mục lục phải khớp thực tế (khuyên dùng mục lục tự động của Word).
4. **Hierarchy & Numbering (Phân cấp đề mục).** Ghi từng cấp theo template: kiểu đánh số, kiểu chữ (in hoa, đậm, nghiêng), căn lề, cỡ chữ nếu khác thân bài, có xuống dòng trước và sau không.

   | Cấp | Kiểu đánh số (VD minh họa) | Định dạng chữ | Nguồn |
   |---|---|---|---|
   | Cấp 1 (Chương hoặc Phần) | "CHƯƠNG 1" hoặc "I." | … | … |
   | Cấp 2 | "1.1" | … | … |
   | Cấp 3 | "1.1.1" | … | … |
   | Cấp 4 (nếu có) | "a)" hoặc gạch đầu dòng | … | … |

   Quy tắc: tối đa mấy cấp; không có mục "1.1" mà thiếu "1.2"; không đánh số mục chỉ có một ý; không nhảy cấp.
5. **Figures, Images & Charts (Hình, ảnh, sơ đồ, biểu đồ).**
   - Gọi chung là "Hình" hay tách riêng (Hình, Ảnh, Sơ đồ, Biểu đồ) theo template; nếu chưa rõ thì hỏi đúng một câu này.
   - Đánh số theo chương (Hình 1.1) hay liên tục (Hình 1); caption đặt trên hay dưới, căn giữa hay trái; cỡ chữ, in đậm hoặc nghiêng, có dấu chấm cuối không.
   - Nguồn ghi ngay dưới caption hoặc dưới hình, dạng "Nguồn: Tác giả" hoặc "Nguồn: (Tên, năm)"; hình tự làm cũng phải ghi.
   - Kích thước tối đa so với chiều rộng trang, căn giữa; ảnh chụp màn hình rõ chữ, không mờ, không vượt lề; đen trắng hay màu nếu in ấn.
   - Bắt buộc có câu dẫn trong bài ("như Hình 2.1 cho thấy…") TRƯỚC khi hình xuất hiện.
6. **Tables (Bảng).**
   - Đánh số theo chương hay liên tục; caption đặt trên hay dưới bảng (thường khác với hình, phải hỏi riêng).
   - Dòng tiêu đề: in đậm, tô nền hay không, lặp lại ở trang sau nếu bảng dài.
   - Kiểu đường kẻ (đủ viền hay chỉ ngang), căn lề số liệu, cỡ chữ và giãn dòng trong bảng.
   - Bảng không vượt lề; bảng rộng thì xoay ngang hoặc đưa vào phụ lục; có câu dẫn trong bài trước bảng.
   - Nguồn ghi dưới bảng; ghi chú (đơn vị, viết tắt) đặt ở đâu.
7. **Equations & Code (Công thức và mã nguồn).** Công thức: đánh số (1.1) hay (1), số căn phải. Mã nguồn hoặc lệnh: font đơn cách (VD Consolas), cỡ chữ, có nền xám không, có đánh số "Đoạn mã 1.1" không; đoạn dài đưa vào phụ lục.
8. **Lists, Footnotes & Quotes (Danh sách, chú thích, trích dẫn).** Ký hiệu gạch đầu dòng hay đánh số, thụt lề, kết thúc bằng dấu chấm phẩy hay chấm. Chú thích cuối trang có dùng không, cỡ chữ. Trích nguyên văn ngắn đặt trong ngoặc kép, dài tách đoạn và thụt lề. Viết tắt: lần đầu viết đầy đủ kèm (viết tắt), có danh mục viết tắt.
9. **Front & Back Matter (Phần đầu và phần cuối).** Danh mục hình, bảng, viết tắt: tên đúng, số trang khớp, định dạng giống mục lục. Phụ lục: ký hiệu (Phụ lục A, B hay 1, 2), có sang trang mới không, đánh số hình và bảng trong phụ lục thế nào (VD Hình A.1). Bìa, trang phụ bìa, lời cam đoan, lời cảm ơn theo mẫu trường, không tự sáng tạo.
10. **Cách kiểm tra định dạng.** Khi người dùng nhờ kiểm tra, trả về danh sách lỗi kèm vị trí, KHÔNG tự sửa im lặng; hỏi "bạn muốn mình sửa luôn không?". Phải kiểm cả hai nhóm lỗi:
    - Cấu trúc: nhảy cấp, thiếu mục 1.2, sai kiểu số; hình hoặc bảng thiếu caption, sai số thứ tự, thiếu nguồn, không được nhắc trong bài; danh mục hình và bảng không khớp nội dung thật.
    - Thị giác và số trang: nhờ người dùng mở Word kiểm lại (ảnh mờ, bảng tràn lề, hình tách trang, số trang mục lục).

---

## Section 3: AUTONOMOUS CITATION ENGINE

- Ghi rõ chuẩn trích dẫn (APA, Harvard, IEEE…) theo yêu cầu của trường, kèm nguồn của thông số này. Đưa 2–3 ví dụ mẫu cho đúng chuẩn đó (sách, bài báo, trang web), cả trích trong bài lẫn danh mục.
- Tự ghi vào `REFERENCES.md` (hoặc danh sách nguồn trong chat nếu không tạo được file).
- Không bao giờ bịa nguồn, DOI, số trang hoặc số liệu.
- Mỗi nguồn có trạng thái: **Đã xác minh** hoặc **Chưa xác minh**. Nguồn chưa xác minh phải được gắn cờ `[CHƯA XÁC MINH]` khi xuất hiện trong báo cáo.
- Không có công cụ tìm kiếm hoặc mở trang web thì mọi nguồn mặc định là "Chưa xác minh"; nhờ người dùng tự mở kiểm tra rồi báo lại.
- Quy tắc ghi nguồn cho phần mềm, thư viện, dataset, ảnh, số liệu thứ cấp và báo cáo doanh nghiệp (chọn loại ngành cần), kèm kiểm tra giấy phép sử dụng.
- Kiểm tra khớp hai chiều: mọi trích dẫn trong bài phải có trong danh mục tài liệu tham khảo và ngược lại.
- Người dùng chỉ cần nói "mình có thêm tài liệu này…" hoặc dán link hoặc tên sách; bạn tự ghi vào danh mục và báo trạng thái xác minh.

---

## Section 4: ADAPTIVE COLLABORATION MATRIX

Chọn **Individual Mode** hoặc **Group Mode** theo câu 2. Chỉ viết chi tiết mode đang dùng.

Thẻ phân công nội bộ: `[OWNER:Tên]`, `[REVIEW:Tên]`, `[STATUS:todo|doing|done]`, `[DUE:dd/mm]`. Người dùng không cần biết các thẻ này; họ chỉ nói "Lan làm chương 3, Minh duyệt" và bạn tự ghi thẻ.

**Group Mode:**
- Bảng phân công theo chương, module hoặc đầu việc (báo cáo, code hoặc thiết kế, demo, slide, thuyết trình), dựa trên điểm mạnh từng người ở câu 2.
- Review chéo: người viết không tự duyệt.
- Cách xử lý xung đột và hợp nhất bản thảo; nhật ký đóng góp của từng thành viên.
- Phân bổ câu hỏi bảo vệ cho từng người để ai cũng giải thích được phần mình làm.

**Individual Mode:** kế hoạch theo tuần, giới hạn số việc làm cùng lúc (tối đa 2–3), mốc tự review.

**Nhật ký góp ý của giảng viên hướng dẫn.** Mỗi lần người dùng báo có góp ý, ghi vào bảng (trong `FEEDBACK_LOG.md` nếu ghi được file): ngày gặp, góp ý, người xử lý, trạng thái đã sửa chưa. Trước khi nộp, kiểm tra mọi góp ý đã được xử lý.

**Rủi ro và sao lưu.** Bảng rủi ro ngắn (mất file, thành viên rút lui, giảng viên đổi yêu cầu, demo hỏng) kèm cách xử lý. Nhắc lưu file ở ít nhất hai nơi và đặt tên phiên bản như `BaoCao_v3_2026-10-27`.

**Cảnh báo chủ động** khi ai đó quá tải, việc không có người duyệt, hoặc deadline sắp tới mà trạng thái chưa "done".

---

## Section 5: NATURAL-LANGUAGE INTENT ROUTER

Chép bảng định tuyến và quy tắc hành vi từ `intent-router.md`, rồi chỉnh theo đồ án:
- Thay ví dụ chung bằng tên chương, tên thành viên, tên sản phẩm thật.
- Nếu quy định AI là "Cấm hoàn toàn": đổi hành động "Viết nháp" thành "Góp ý bản nháp của bạn".
- Bỏ hàng không liên quan (VD đồ án cá nhân thì "Phân công" chỉ còn kế hoạch tuần; không có demo thì gộp "Chuẩn bị demo" vào "Làm slide").

---

## Cách viết file

1. Viết lần lượt từng section, không viết cả file trong một lượt.
2. Sau mỗi section, kiểm tra nội dung không bị cắt cụt (câu cuối hoàn chỉnh, bảng đủ cột, checklist đủ mục).
3. Không tạo được file: đưa toàn bộ nội dung trong một khối mã để người dùng sao chép, rồi hướng dẫn họ lưu thành `SKILL_MASTER.md`.

## Kiểm tra cuối

Chạy `scripts/validate_skill.py` nếu được. Nếu không, tự kiểm:

- [ ] Frontmatter hợp lệ: có `---` mở và đóng, có `name` và `description`.
- [ ] `name` chữ thường, gạch ngang, không chứa "claude" hay "anthropic".
- [ ] `description` dưới khoảng 1000 ký tự, không có dấu `<` `>`.
- [ ] Đủ 5 section, đúng tên và thứ tự.
- [ ] Dòng "LƯU Ý" nằm ngay đầu Section 1.
- [ ] Mọi thông số ở Section 2 đều có ghi nguồn.
- [ ] Mọi giả định có nhãn "giả định – CHƯA XÁC MINH".
- [ ] Độ dài nằm trong khoảng cho môi trường.
- [ ] Router mỗi hành động có ít nhất 3 cách nói.
