# Cài Academic Skill Master cho Claude Code trên Windows.
# Chuột phải file này -> Run with PowerShell.
$ErrorActionPreference = 'Stop'
$src = Join-Path $PSScriptRoot 'skills\academic-skill-master'
$dest = Join-Path $env:USERPROFILE '.claude\skills\academic-skill-master'

if (-not (Test-Path (Join-Path $src 'SKILL.md'))) {
    Write-Host 'Không tìm thấy skills\academic-skill-master\SKILL.md. Hãy chạy file này trong thư mục đã giải nén.' -ForegroundColor Red
    Read-Host 'Nhấn Enter để đóng'
    exit 1
}

if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
Copy-Item -Recurse $src $dest

Write-Host "Đã cài xong vào: $dest" -ForegroundColor Green
Write-Host 'Mở Claude Code và nhắn: "Tạo trợ lý cho đồ án của mình".'
Read-Host 'Nhấn Enter để đóng'
