"""Generates assets/hero.svg: terminal header + rotating 3D DNA double helix.

Run: python assets/gen_hero.py
"""
import math
import random
from pathlib import Path

W, H = 1200, 440
OUT = Path(__file__).with_name("hero.svg")

# helix geometry (vertical, right side)
CX = 960            # helix axis x
AMP = 92            # radius in px
PERIOD = 200        # px per full turn
RUNGS_PER_TURN = 10  # B-DNA: ~10 bp per turn
TILE_TURNS = 2      # animation loops after this many turns
TOP, BOT = 56, 414  # visible area
STEP = 3            # strand segment length
DUR = 9             # seconds per tile scroll

BASE_COL = {"A": "#3fb950", "T": "#ff7b72", "G": "#e3b341", "C": "#58a6ff"}
PAIR = {"A": "T", "T": "A", "G": "C", "C": "G"}
SNP_COL = "#f778ba"

random.seed(7)
tile_len = PERIOD * TILE_TURNS
n_tile_rungs = RUNGS_PER_TURN * TILE_TURNS
seq_tile = [random.choice("ATGC") for _ in range(n_tile_rungs)]
SNP_IDX = 13  # one variant per tile

y0 = TOP - tile_len - 20          # draw one extra tile above so scrolling down covers view
y1 = BOT + 20
k = 2 * math.pi / PERIOD


def pt(y, phase):
    a = k * y + phase
    return CX + AMP * math.sin(a), math.cos(a)  # x, depth z in [-1, 1]


def depth_style(z, front_w=7.0, back_w=3.0):
    t = (z + 1) / 2
    w = back_w + (front_w - back_w) * t
    op = 0.25 + 0.75 * t
    return w, op


back, front, rungs, beads = [], [], [], []

# strands: phase 0 and pi. Colour per strand.
STRAND_COL = ["#79c0ff", "#d2a8ff"]
for s, phase in enumerate((0.0, math.pi)):
    y = y0
    while y < y1:
        xa, za = pt(y, phase)
        xb, zb = pt(y + STEP + 0.6, phase)
        z = (za + zb) / 2
        w, op = depth_style(z)
        seg = (f'<line x1="{xa:.1f}" y1="{y:.1f}" x2="{xb:.1f}" y2="{y+STEP+0.6:.1f}" '
               f'stroke="{STRAND_COL[s]}" stroke-width="{w:.2f}" stroke-opacity="{op:.2f}"/>')
        (front if z > 0 else back).append((z, seg))
        y += STEP

# rungs (base pairs)
spacing = PERIOD / RUNGS_PER_TURN
i = 0
y = y0 + spacing / 2
while y < y1:
    idx = i % n_tile_rungs
    base = seq_tile[idx]
    comp = PAIR[base]
    xa, za = pt(y, 0.0)
    xb, zb = pt(y, math.pi)
    xm = (xa + xb) / 2
    zr = abs(za)
    width = 2.0 + 2.5 * (1 - zr)  # rungs facing viewer look wider
    op = 0.35 + 0.55 * (1 - zr * 0.6)
    is_snp = idx == SNP_IDX
    ca = SNP_COL if is_snp else BASE_COL[base]
    cb = SNP_COL if is_snp else BASE_COL[comp]
    cls = ' class="snp"' if is_snp else ""
    rungs.append(
        f'<g{cls} opacity="{op:.2f}">'
        f'<line x1="{xa:.1f}" y1="{y:.1f}" x2="{xm:.1f}" y2="{y:.1f}" stroke="{ca}" stroke-width="{width:.1f}" stroke-linecap="round"/>'
        f'<line x1="{xm:.1f}" y1="{y:.1f}" x2="{xb:.1f}" y2="{y:.1f}" stroke="{cb}" stroke-width="{width:.1f}" stroke-linecap="round"/>'
        f'</g>')
    for x, z, c in ((xa, za, ca), (xb, zb, cb)):
        r = 2.5 + 3.0 * (z + 1) / 2
        o = 0.3 + 0.7 * (z + 1) / 2
        item = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}" fill-opacity="{o:.2f}"/>'
        (front if z > 0 else back).append((z + 0.001, item))
    if is_snp:
        lx = CX + AMP + 34
        rungs.append(
            f'<g class="snptag"><line x1="{max(xa, xb)+8:.1f}" y1="{y:.1f}" x2="{lx-4}" y2="{y:.1f}" '
            f'stroke="{SNP_COL}" stroke-width="1" stroke-dasharray="3 3"/>'
            f'<text x="{lx}" y="{y+4:.1f}" class="mono" font-size="12" fill="{SNP_COL}">'
            f'SNP {base}&gt;{ {"A":"G","G":"A","C":"T","T":"C"}[base] }</text></g>')
    y += spacing
    i += 1

back.sort(key=lambda t: t[0])
front.sort(key=lambda t: t[0])

# scrolling sequence ladder left of the helix
seq_x = CX - AMP - 70
seq_lines = []
i = 0
y = y0 + spacing / 2
while y < y1:
    b = seq_tile[i % n_tile_rungs]
    c = SNP_COL if i % n_tile_rungs == SNP_IDX else BASE_COL[b]
    seq_lines.append(
        f'<text x="{seq_x}" y="{y+4:.1f}" class="mono" font-size="12" fill="{c}" fill-opacity="0.85">{b}</text>'
        f'<text x="{seq_x+16}" y="{y+4:.1f}" class="mono" font-size="12" fill="#484f58">·</text>'
        f'<text x="{seq_x+28}" y="{y+4:.1f}" class="mono" font-size="12" fill="{BASE_COL[PAIR[b]]}" fill-opacity="0.55">{PAIR[b]}</text>')
    y += spacing
    i += 1

helix = "\n".join(s for _, s in back) + "\n" + "\n".join(rungs) + "\n" + "\n".join(s for _, s in front)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Doğukan Sahil, Genetics x Embedded">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0b0f17"/><stop offset="0.6" stop-color="#0d1420"/><stop offset="1" stop-color="#140d1f"/>
  </linearGradient>
  <radialGradient id="glow" cx="{CX/W:.3f}" cy="0.55" r="0.42">
    <stop offset="0" stop-color="#58a6ff" stop-opacity="0.22"/><stop offset="0.5" stop-color="#bc8cff" stop-opacity="0.08"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#a5f3fc"/><stop offset="0.5" stop-color="#79c0ff"/><stop offset="1" stop-color="#d2a8ff"/>
  </linearGradient>
  <linearGradient id="fadeG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.16" stop-color="#fff"/>
    <stop offset="0.86" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="fade"><rect x="700" y="{TOP}" width="500" height="{BOT-TOP}" fill="url(#fadeG)"/></mask>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="1" fill="#30363d" fill-opacity="0.55"/>
  </pattern>
  <clipPath id="win"><rect x="0" y="0" width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  .mono {{ font-family: 'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; }}
  .sans {{ font-family: 'Inter','Segoe UI',ui-sans-serif,system-ui,-apple-system,Helvetica,Arial,sans-serif; }}
  .scroll {{ animation: scroll {DUR}s linear infinite; }}
  @keyframes scroll {{ from {{ transform: translateY(0px); }} to {{ transform: translateY({tile_len}px); }} }}
  .snp line, .snp {{ animation: pulse 1.4s ease-in-out infinite; }}
  @keyframes pulse {{ 0%,100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
  .cur {{ animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  .in {{ opacity: 0; animation: in .7s ease-out forwards; }}
  @keyframes in {{ from {{ opacity: 0; transform: translateX(-8px); }} to {{ opacity: 1; transform: none; }} }}
  .d1 {{ animation-delay: .2s; }} .d2 {{ animation-delay: .5s; }} .d3 {{ animation-delay: .8s; }}
  .d4 {{ animation-delay: 1.1s; }} .d5 {{ animation-delay: 1.4s; }} .d6 {{ animation-delay: 1.7s; }}
</style>
<g clip-path="url(#win)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>

  <!-- title bar -->
  <rect width="{W}" height="40" fill="#0d1117" fill-opacity="0.85"/>
  <line x1="0" y1="40" x2="{W}" y2="40" stroke="#21262d"/>
  <circle cx="26" cy="20" r="6.5" fill="#ff5f57"/><circle cx="48" cy="20" r="6.5" fill="#febc2e"/><circle cx="70" cy="20" r="6.5" fill="#28c840"/>
  <text x="{W/2}" y="25" text-anchor="middle" class="mono" font-size="13" fill="#8b949e">dogukansahil@genome: ~/chr17 · session: ph.d</text>

  <!-- helix -->
  <g mask="url(#fade)">
    <g class="scroll">
{chr(10).join(seq_lines)}
{helix}
    </g>
  </g>
  <text x="{CX}" y="{BOT+16}" text-anchor="middle" class="mono" font-size="11" fill="#6e7681" letter-spacing="2">5' ── B-DNA · 10 bp/turn ── 3'</text>

  <!-- left text -->
  <text x="48" y="96" class="mono in d1" font-size="16" fill="#7ee787">$ whoami</text>
  <text x="48" y="156" class="sans in d2" font-size="56" font-weight="800" fill="url(#name)" letter-spacing="-1">Doğukan Sahil</text>
  <text x="50" y="192" class="sans in d3" font-size="21" font-weight="600" fill="#e6edf3">Interdisciplinary Engineer</text>
  <text x="50" y="224" class="mono in d4" font-size="14.5" fill="#8b949e"><tspan fill="#f778ba">▸</tspan> Ph.D. Candidate · ML-assisted SNP Analysis</text>
  <text x="50" y="250" class="mono in d4" font-size="14.5" fill="#8b949e"><tspan fill="#79c0ff">▸</tspan> MSc Biomedical Engineering</text>
  <text x="50" y="276" class="mono in d4" font-size="14.5" fill="#8b949e"><tspan fill="#7ee787">▸</tspan> BSc Genetics &amp; Bioengineering</text>

  <g class="in d5">
    <rect x="48" y="304" width="262" height="34" rx="17" fill="#161b22" stroke="#30363d"/>
    <text x="179" y="326" text-anchor="middle" class="mono" font-size="13" font-weight="700" fill="#e6edf3" letter-spacing="1.5">GENETICS <tspan fill="#f778ba">×</tspan> EMBEDDED</text>
  </g>

  <g class="in d6">
    <text x="48" y="384" class="mono" font-size="14" fill="#7ee787">$</text>
    <text x="64" y="384" class="mono" font-size="14" fill="#c9d1d9">./sequence --from=dna --to=silicon</text>
    <rect class="cur" x="334" y="372" width="9" height="16" fill="#7ee787"/>
  </g>
</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#30363d"/>
</svg>
'''
OUT.write_text(svg, encoding="utf-8")
print(OUT, len(svg) // 1024, "KB")
