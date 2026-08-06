#!/usr/bin/env python3
"""Build the single-file index.html for Noor Ahmad Trader."""
import pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "index.html"

def read(name):
    return (SRC / name).read_text(encoding="utf-8")

css = read("style.css")
js = "\n".join(read(f) for f in
    ["i18n.js", "sim.js", "chart.js", "chat.js", "ui.js", "pages.js"])

html = f"""<!DOCTYPE html>
<html lang="ps" dir="rtl" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Noor Ahmad Trader — AI Trading Platform</title>
<meta name="description" content="Noor Ahmad Trader — AI Trading Platform for XAU/USD & EUR/USD with ICT analysis">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%233b82f6'/%3E%3Cstop offset='1' stop-color='%231d4ed8'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect x='2' y='2' width='44' height='44' rx='12' fill='url(%23g)'/%3E%3Cpath d='M13 30 L21 20 L26 25 L34 14' stroke='white' stroke-width='3.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3Ccircle cx='34' cy='14' r='3.4' fill='%2322c55e'/%3E%3C/svg%3E">
<style>
{css}
</style>
</head>
<body>
<div id="app"></div>
<script>
{js}
</script>
<script>
document.addEventListener("DOMContentLoaded", function(){{
  initApp();
  nav("home");
}});
</script>
</body>
</html>
"""
OUT.write_text(html, encoding="utf-8")
print(f"Built {OUT} ({OUT.stat().st_size/1024:.1f} KB)")
