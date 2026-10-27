# Cài Academic Skill Master cho Claude Code và Codex trên Windows.
# Chuột phải file này -> Run with PowerShell.
$ErrorActionPreference = 'Stop'
$src = Join-Path $PSScriptRoot 'skills\academic-skill-master'
$targets = [ordered]@{
    'Claude Code' = Join-Path $env:USERPROFILE '.claude\skills\academic-skill-master'
    'Codex'       = Join-Path $env:USERPROFILE '.agents\skills\academic-skill-master'
}

if (-not (Test-Path (Join-Path $src 'SKILL.md'))) {
    Write-Host 'Không tìm thấy skills\academic-skill-master\SKILL.md. Hãy chạy file này trong thư mục đã giải nén.' -ForegroundColor Red
    Read-Host 'Nhấn Enter để đóng'
    exit 1
}

foreach ($tool in $targets.Keys) {
    $dest = $targets[$tool]
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
    Copy-Item -Recurse $src $dest
    Write-Host "Đã cài cho ${tool}: $dest" -ForegroundColor Green
}

Write-Host 'Mở Claude Code hoặc Codex và nhắn: "Tạo trợ lý cho đồ án của mình".'
Read-Host 'Nhấn Enter để đóng'
