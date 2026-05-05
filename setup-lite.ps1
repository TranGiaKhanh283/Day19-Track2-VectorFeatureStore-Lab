# Lite path on Windows — same steps as setup-lite.sh (no Docker).
# Run from repo root:  powershell -ExecutionPolicy Bypass -File .\setup-lite.ps1
$ErrorActionPreference = "Stop"
$env:PYTHONIOENCODING = "utf-8"

Write-Host "[lite] Day 19 lightweight setup (Windows)"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "python not found. Install Python 3.10+."
}

if (-not (Test-Path .venv)) {
    python -m venv .venv
}

$py = Join-Path .venv "Scripts\python.exe"
$pip = Join-Path .venv "Scripts\pip.exe"
$jupytext = Join-Path .venv "Scripts\jupytext.exe"

& $pip install -q -U pip
& $pip install -q -r requirements.txt

if (Test-Path $jupytext) {
    & $jupytext --to notebook --update notebooks\*.py 2>$null
    if ($LASTEXITCODE -ne 0) { & $jupytext --to notebook notebooks\*.py }
}

if (-not (Test-Path .env)) { Copy-Item .env.example .env }

& $py scripts\seed_corpus.py
& $py scripts\verify_lite.py

Write-Host "`n[lite] Done. Next:"
Write-Host "  .\.venv\Scripts\uvicorn.exe app.main:app --reload --port 8000"
Write-Host "  .\.venv\Scripts\python.exe scripts\benchmark.py"
