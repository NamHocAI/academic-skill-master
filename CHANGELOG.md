# Nhật ký thay đổi

## [1.1.0] – 2026-10-27

### Thêm mới
- Hỗ trợ Codex của OpenAI: hướng dẫn cài trong README, script cài đặt chép skill vào cả `~/.claude/skills/` và `~/.agents/skills/`.
- Skill nhận biết môi trường Codex ở câu hỏi 7 và tạo trợ lý riêng tại `.agents/skills/do-an-<tên-ngắn>/SKILL.md`.
- `validate_skill.py` thêm lựa chọn `--env codex`.

## [1.0.0] – 2026-10-27

### Thêm mới
- Skill `academic-skill-master`: quy trình 3 giai đoạn (phỏng vấn 10 câu → bảng xác nhận → tạo `SKILL_MASTER.md`).
- Đặc tả 5 section cho file trợ lý: kiến trúc và quy trình theo ngành, khóa định dạng theo template, trích dẫn, cộng tác nhóm, bộ hiểu ý bằng lời thường.
- Rubric mặc định 10 tiêu chí (gắn nhãn giả định).
- Bảng định tuyến 22 hành động, mỗi hành động có ít nhất 3 cách nói.
- Mẫu file phụ: `PROJECT_STATUS.md`, `REFERENCES.md`, `FEEDBACK_LOG.md`.
- Script `validate_skill.py` kiểm tra tự động file trợ lý.
- Cấu hình plugin và marketplace cho Claude Code; gói zip cho Claude.ai; script cài đặt cho Windows, macOS, Linux.
