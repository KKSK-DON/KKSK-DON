"""Draw the profile banner: a dark card with the name on the left and a causal-attention heatmap on the right.

The heatmap is decoration, not data: a lower-triangular grid (each token attends to itself and earlier
tokens) with the patterns real attention maps show: a bright diagonal, a bright first column
("attention sink"), a band next to the diagonal, and two key columns many queries look at.

Setup, once (the font is subset and embedded in the SVG as WOFF2, so it needs fontTools and brotli):
    pip install fonttools brotli
    curl -L -o Manrope-VF.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/Manrope%5Bwght%5D.ttf"

Usage, from the repository root:
    python build_banner.py Manrope-VF.ttf assets/banner.svg

Do not commit Manrope-VF.ttf; the banner already carries the subset it needs.
"""

import base64
import io
import sys

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

W, H = 1280, 320
NAME = "Yang Liu"
ROLE = "LLM inference & AI infrastructure engineer"
CHIPS = ["vLLM contributor", "CUDA kernels", "KV-cache quantization", "MoE"]

BG = ("#0A0F1F", "#0F1D3A", "#0B2A3A")  # card gradient, left to right
CYAN, VIOLET = (0x22, 0xD3, 0xEE), (0xA7, 0x8B, 0xFA)
NAME_FILL, ROLE_FILL, CHIP_TEXT = "#F8FAFC", "#A5B4CF", "#BAE6FD"


def width(font_path, text, wght, size):
    f = instantiateVariableFont(TTFont(font_path), {"wght": wght})
    cmap, hmtx, upm = f.getBestCmap(), f["hmtx"].metrics, f["head"].unitsPerEm
    return sum(hmtx[cmap[ord(c)]][0] for c in text) * size / upm


def font_b64(font_path, chars):
    f = TTFont(font_path)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga"]
    sub = subset.Subsetter(opts)
    sub.populate(text=chars)
    sub.subset(f)
    buf = io.BytesIO()
    f.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def noise(i, j):
    """Deterministic value in [0, 1) so the heatmap looks the same on every build."""
    return ((i * 73856093) ^ (j * 19349663) ^ 0x5BD1E995) % 1000 / 1000


def heat(i, j):
    if j == i:
        return 0.95
    if j == 0:
        return 0.72
    if i - j == 1:
        return 0.55
    if j in (5, 9):
        return 0.38 + 0.12 * noise(i, j)
    return 0.07 + 0.16 * noise(i, j)


def mix(t):
    r, g, b = (round(a + (c - a) * t) for a, c in zip(CYAN, VIOLET))
    return f"#{r:02X}{g:02X}{b:02X}"


def build(font_path):
    b64 = font_b64(font_path, NAME + ROLE + "".join(CHIPS))
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="{NAME}, {ROLE.replace("&", "&amp;")}">',
        "<defs>",
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{BG[0]}"/><stop offset=".55" stop-color="{BG[1]}"/>'
        f'<stop offset="1" stop-color="{BG[2]}"/></linearGradient>',
        f'<linearGradient id="accent" x1="0" x2="1"><stop offset="0" stop-color="{mix(0)}"/>'
        f'<stop offset="1" stop-color="{mix(1)}"/></linearGradient>',
        '<radialGradient id="glow"><stop offset="0" stop-color="#22D3EE" stop-opacity=".28"/>'
        '<stop offset="1" stop-color="#22D3EE" stop-opacity="0"/></radialGradient>',
        '<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
        '<circle cx="2" cy="2" r="1.1" fill="#FFFFFF" fill-opacity=".07"/></pattern>',
        f'<clipPath id="card"><rect width="{W}" height="{H}" rx="28"/></clipPath>',
        "<style>"
        "@font-face{font-family:'Manrope';"
        f"src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:200 800}}"
        "text{font-family:'Manrope',sans-serif}"
        "</style>",
        "</defs>",
        '<g clip-path="url(#card)">',
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#dots)"/>',
    ]

    # heatmap on the right, with a soft glow behind it
    n, cell, gap = 12, 15, 4
    size = n * (cell + gap) - gap
    hx, hy = W - 120 - size, (H - size) // 2
    out.append(f'<circle cx="{hx + size / 2}" cy="{hy + size / 2}" r="{size * 0.85}" fill="url(#glow)"/>')
    for i in range(n):
        for j in range(i + 1):
            x, y = hx + j * (cell + gap), hy + i * (cell + gap)
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" '
                       f'fill="{mix((i + j) / (2 * n - 2))}" fill-opacity="{heat(i, j):.2f}"/>')

    # text on the left
    x0 = 88
    out.append(f'<rect x="{x0}" y="78" width="56" height="6" rx="3" fill="url(#accent)"/>')
    out.append(f'<text x="{x0 - 4}" y="168" font-size="80" font-weight="800" letter-spacing="-1.5" '
               f'fill="{NAME_FILL}">{NAME}</text>')
    out.append(f'<text x="{x0}" y="214" font-size="26" font-weight="600" fill="{ROLE_FILL}">'
               f'{ROLE.replace("&", "&amp;")}</text>')
    cx, cy, ch = x0, 246, 38
    for label in CHIPS:
        w = width(font_path, label, 600, 17) + 32
        out.append(f'<rect x="{cx}" y="{cy}" width="{w:.1f}" height="{ch}" rx="{ch / 2}" fill="#FFFFFF" '
                   f'fill-opacity=".05" stroke="#22D3EE" stroke-opacity=".38"/>')
        out.append(f'<text x="{cx + w / 2:.1f}" y="{cy + 25}" font-size="17" font-weight="600" '
                   f'text-anchor="middle" fill="{CHIP_TEXT}">{label}</text>')
        cx += w + 12

    out.append("</g></svg>")
    return "".join(out)


if __name__ == "__main__":
    svg = build(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{sys.argv[2]}  {len(svg) / 1024:.1f} KB")
