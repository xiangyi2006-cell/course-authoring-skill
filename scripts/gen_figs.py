# 课程配图生成脚本模板
# 用法: python gen_figs.py [图编号|all]
# 依赖: matplotlib (pip install matplotlib)
# 字体: 中文用系统雅黑/思源黑体，按平台替换 FONT 变量

import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import os

# ── 按平台注册中文字体 ──
FONT_CANDIDATES = [
    ("Windows", r"C:\Windows\Fonts\msyh.ttc"),
    ("Windows", r"C:\Windows\Fonts\msyhbd.ttc"),
    ("macOS",   "/System/Library/Fonts/PingFang.ttc"),
    ("Linux",   "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"),
]
for _plat, _fp in FONT_CANDIDATES:
    if os.path.exists(_fp):
        fm.fontManager.addfont(_fp)

plt.rcParams["font.sans-serif"] = [
    "Microsoft YaHei", "PingFang SC", "Droid Sans Fallback", "sans-serif"
]
plt.rcParams["axes.unicode_minus"] = False

ONLY = sys.argv[1] if len(sys.argv) > 1 else "all"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
os.makedirs(OUT, exist_ok=True)

DARK = "#1F2937"
GRAY = "#6B7280"

# ── 通用绘制函数 ──

def box(ax, x, y, w, h, fc, ec, lw=1.2):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.08",
                       fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)

def arrow(ax, x1, y1, x2, y2, color="#9CA3AF", style="-", lw=1.6):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                        mutation_scale=16, color=color, lw=lw, linestyle=style)
    ax.add_patch(a)

def newfig(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax

# ── 在下面添加你的图 ──
# 每张图用 if ONLY in ("all", "N"): 包裹，独立可重生成
# 示例：

# if ONLY in ("all", "1"):
#     fig, ax = newfig(14, 4.0)
#     ax.text(7, 3.6, "课程模块 · 学习路线", ha="center", fontsize=15,
#             weight="bold", color=DARK)
#     # ... 画图逻辑 ...
#     fig.savefig(f"{OUT}/学习路线图.png", bbox_inches="tight", facecolor="white")
#     plt.close(fig)
#     print("fig 1 done")

print("done")
