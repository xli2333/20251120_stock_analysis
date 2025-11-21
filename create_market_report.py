
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.font_manager as fm
import numpy as np

# 1. Setup Fonts
font_path_normal = 'yahei.ttf'
font_path_bold = 'yahei_bold.ttf'

# Create font properties objects
prop_normal = fm.FontProperties(fname=font_path_normal)
prop_bold = fm.FontProperties(fname=font_path_bold)
prop_title = fm.FontProperties(fname=font_path_bold, size=24)
prop_header = fm.FontProperties(fname=font_path_bold, size=16)
prop_text = fm.FontProperties(fname=font_path_normal, size=12)
prop_chart_title = fm.FontProperties(fname=font_path_bold, size=14)
prop_axis = fm.FontProperties(fname=font_path_normal, size=10)

# Color Scheme (Professional Financial)
COLOR_BG = '#F5F5F5'
COLOR_PRIMARY = '#1f77b4'  # Blue
COLOR_SECONDARY = '#ff7f0e' # Orange
COLOR_DANGER = '#d62728'   # Red
COLOR_SUCCESS = '#2ca02c'  # Green
COLOR_TEXT = '#333333'

def create_page(fig, title):
    fig.patch.set_facecolor(COLOR_BG)
    # Header
    plt.text(0.05, 0.95, title, transform=fig.transFigure, fontproperties=prop_title, color=COLOR_TEXT)
    # Footer
    plt.text(0.05, 0.02, '来源: 地平线全球策略组 / 交易台数据 / 高盛 | 生成: Gemini CLI',
             transform=fig.transFigure, fontproperties=prop_text, fontsize=8, color='#666666')

def draw_text_block(fig, x, y, title, content, width=0.9):
    plt.text(x, y, title, transform=fig.transFigure, fontproperties=prop_header, color=COLOR_PRIMARY)
    # Simple word wrap simulation or just splitting by newlines
    lines = content.split('\n')
    for i, line in enumerate(lines):
        plt.text(x, y - 0.04 - (i * 0.03), line, transform=fig.transFigure, fontproperties=prop_text, color=COLOR_TEXT)

# Initialize PDF
pdf_filename = 'Market_Analysis_Report_1121.pdf'
pp = PdfPages(pdf_filename)

# --- PAGE 1: EXECUTIVE SUMMARY ---
fig1 = plt.figure(figsize=(11.69, 8.27)) # A4 Landscape
create_page(fig1, '1. 核心定性：流动性真空下的“假摔”')

# Text Analysis
text_content = (
    "● 暴跌性质：宏观风险消退后的获利了结 (Unwind)\n"
    "  本次下跌并非恐慌性去杠杆 (De-grossing)。交易台数据显示，早盘机构活跃于\n"
    "  “解除对冲”和“做空波动率”，尾盘未见恐慌性买回保护。机构正在利用流动性\n"
    "  真空进行清洗，为年底行情腾出空间。\n\n"
    "● 为什么感觉跌得很惨？\n"
    "  这是“流动性错觉”。市场缺乏深度，少量卖单造成了巨大的价格滑点。\n"
    "  ETF成交占比激增，导致基本面优良的个股被无差别错杀。"
)
draw_text_block(fig1, 0.05, 0.85, '市场诊断：不是崩盘，是清洗', text_content)

# Visual: Market Mood Index (Conceptual)
ax1 = fig1.add_axes([0.1, 0.3, 0.8, 0.15])
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1)
ax1.axis('off')
# Gradient bar
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
ax1.imshow(gradient, aspect='auto', cmap='RdYlGn_r', extent=[0, 10, 0, 1])
# Indicator
ax1.annotate('当前位置：获利了结 (Unwind)', xy=(3.5, 0.5), xytext=(3.5, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             ha='center', fontproperties=prop_bold)
ax1.text(0, -0.5, '极度恐慌\n(De-grossing)', ha='center', fontproperties=prop_text)
ax1.text(10, -0.5, '极度贪婪\n(FOMO)', ha='center', fontproperties=prop_text)

pp.savefig(fig1)
plt.close(fig1)

# --- PAGE 2: LIQUIDITY VOID ---
fig2 = plt.figure(figsize=(11.69, 8.27))
create_page(fig2, '2. 微观真相：致命的流动性黑洞')

# Data
metrics = ['盘口流动性深度 ($)', 'ETF 成交占比 (%)']
current_vals = [5, 41]
avg_vals = [11, 28]

# Chart: Liquidity Comparison
ax2 = fig2.add_axes([0.1, 0.45, 0.35, 0.35])
x = np.arange(len(metrics))
width = 0.35
rects1 = ax2.bar(x - width/2, current_vals, width, label='11.21 当日', color=COLOR_DANGER, alpha=0.8)
rects2 = ax2.bar(x + width/2, avg_vals, width, label='2025年均值', color='gray', alpha=0.5)

ax2.set_ylabel('数值 (百万美元 / 百分比)', fontproperties=prop_axis)
ax2.set_title('市场深度枯竭对比', fontproperties=prop_chart_title)
ax2.set_xticks(x)
ax2.set_xticklabels(metrics, fontproperties=prop_bold)
ax2.legend(prop=prop_text)

# Analysis Text
text_liquidity = (
    "● 盘口深度仅剩 $500万 (正常值 $1100万)\n"
    "  意味着同等规模的抛单会造成平时 2倍+ 的价格冲击。\n"
    "  市场就像在薄冰上跳舞，任何风吹草动都会引发剧震。\n\n"
    "● ETF 成交占比高达 41% (正常值 28%)\n"
    "  证明这是“宏观一篮子抛售”。资金在通过 SPY/QQQ \n"
    "  减仓 Beta 敞口，而非针对特定公司的基本面做空。"
)
draw_text_block(fig2, 0.55, 0.80, '数据解读', text_liquidity)

# Chart: Price Impact Illustration (Conceptual)
ax2b = fig2.add_axes([0.1, 0.1, 0.8, 0.2])
t = np.linspace(0, 10, 100)
y_normal = np.sin(t) * 0.5
y_crisis = np.sin(t) * 1.5
ax2b.plot(t, y_normal, label='正常流动性下的波动', color='gray', linestyle='--')
ax2b.plot(t, y_crisis, label='当前流动性下的波动', color=COLOR_DANGER, linewidth=2)
ax2b.set_title('相同卖压下的价格波动模拟', fontproperties=prop_chart_title)
ax2b.legend(prop=prop_text)
ax2b.axis('off')

pp.savefig(fig2)
plt.close(fig2)

# --- PAGE 3: TRIGGER MECHANISM ---
fig3 = plt.figure(figsize=(11.69, 8.27))
create_page(fig3, '3. 触发机制：NVDA 与宏观预期的错位')

# Chart: NVDA Reversal vs Rate Cut Prob
ax3 = fig3.add_axes([0.1, 0.45, 0.8, 0.35])
time = ['09:30', '10:00', '11:00', '13:00', '15:00', '16:00']
nvda_price = [104.5, 105.0, 102.0, 100.0, 98.5, 97.5] # Mock normalized trend
rate_prob = [50, 48, 40, 38, 36, 35]

ax3.plot(time, nvda_price, marker='o', color=COLOR_SUCCESS, label='NVDA 价格走势 (示意)', linewidth=2)
ax3.set_ylabel('NVDA 价格趋势', fontproperties=prop_axis, color=COLOR_SUCCESS)
ax3.tick_params(axis='y', labelcolor=COLOR_SUCCESS)

ax3_r = ax3.twinx()
ax3_r.plot(time, rate_prob, marker='x', color=COLOR_SECONDARY, label='12月降息概率 (%)', linewidth=2, linestyle='--')
ax3_r.set_ylabel('降息概率 (%)', fontproperties=prop_axis, color=COLOR_SECONDARY)
ax3_r.tick_params(axis='y', labelcolor=COLOR_SECONDARY)

lines, labels = ax3.get_legend_handles_labels()
lines2, labels2 = ax3_r.get_legend_handles_labels()
ax3.legend(lines + lines2, labels + labels2, prop=prop_text, loc='upper center')
ax3.set_title('双重打击：利好出尽 + 鹰派突袭', fontproperties=prop_chart_title)

# Text
text_trigger = (
    "● NVDA: 完美的“多头陷阱”\n"
    "  财报 Beat & Raise，但股价日内回撤 ~7%。\n"
    "  这确认了市场对利好的反应弹性已耗尽 (Exhaustion)。\n\n"
    "● 宏观: 迟到的鹰派信号\n"
    "  9月非农 (+11.9万) 数据虽滞后，但被美联储官员 (Lisa Cook) \n"
    "  利用来打压降息预期。降息概率从 50% 骤降至 35%。\n"
    "  强劲的经济数据在流动性稀缺时被解读为“由于不降息而产生的利空”。"
)
draw_text_block(fig3, 0.1, 0.35, '连锁反应机制', text_trigger)

pp.savefig(fig3)
plt.close(fig3)

# --- PAGE 4: QUANT SIGNAL ---
fig4 = plt.figure(figsize=(11.69, 8.27))
create_page(fig4, '4. 量化指引：乌云背后的“黄金坑”')

# Data: Historical Returns
periods = ['T+1 日', 'T+1 周', 'T+1 月']
returns = [2.33, 2.88, 4.72]

# Chart
ax4 = fig4.add_axes([0.2, 0.4, 0.6, 0.4])
bars = ax4.bar(periods, returns, color=COLOR_SUCCESS, alpha=0.7)
ax4.bar_label(bars, fmt='+%.2f%%', padding=3, fontproperties=prop_bold)
ax4.set_ylabel('平均收益率 (%)', fontproperties=prop_axis)
ax4.set_title('历史 8 次“高开>1%后收跌”后的标普500表现', fontproperties=prop_chart_title)
ax4.set_xticklabels(periods, fontproperties=prop_bold)

# Text
text_quant = (
    "● 反直觉的看涨信号\n"
    "  历史数据显示，这种极端的日内反转往往不是熊市的开始，\n"
    "  而是多头行情的“空中加油”。\n\n"
    "● 数据铁证 (1957年至今共8次样本):\n"
    "  - 次日 (T+1) 平均反弹 +2.33%\n"
    "  - 次月 (T+1 Month) 平均大涨 +4.72%\n\n"
    "● 策略含义：\n"
    "  现在的策略绝不是防御，而是利用恐慌情绪寻找反弹切入点。\n"
    "  市场通过一次剧烈的 Unwind 完成了筹码交换。"
)
draw_text_block(fig4, 0.1, 0.30, '核心多头逻辑', text_quant)

pp.savefig(fig4)
plt.close(fig4)

# --- PAGE 5: ACTION PLAN ---
fig5 = plt.figure(figsize=(11.69, 8.27))
create_page(fig5, '5. 战术执行：盯住 6456，反击开始')

# Chart: CTA Threshold
ax5 = fig5.add_axes([0.1, 0.5, 0.5, 0.3])
levels = [6640, 6538, 6456, 6336]
level_names = ['日内高点', '当前价格', 'CTA生死线', '下行支撑']
colors = ['gray', COLOR_PRIMARY, COLOR_DANGER, 'gray']

for i, (lvl, name, col) in enumerate(zip(levels, level_names, colors)):
    ax5.axhline(y=lvl, color=col, linestyle='--' if col == 'gray' else '-', linewidth=2)
    ax5.text(0.1, lvl + 10, f"{name}: {lvl}", fontproperties=prop_bold, color=col)

ax5.set_ylim(6200, 6700)
ax5.set_xlim(0, 1)
ax5.set_xticks([])
ax5.set_title('标普500 关键风控点位监控', fontproperties=prop_chart_title)

# Strategy Text
text_strategy = (
    "1. 紧盯 CTA 阈值 (6456)\n"
    "   - 只要指数运行在 6456 上方，维持【多头思维】。\n"
    "   - 此区域是主力清洗浮筹的区间，不是出货区。\n"
    "   - 若有效跌破 6456 (小概率)，CTA 将触发机械止损，\n"
    "     此时暂停做多，下看 6336。\n\n"
    "2. 左侧布局方向\n"
    "   - 错杀科技股：在纳指企稳后，回补软件/半导体龙头。\n"
    "   - 风格轮动：关注罗素2000 (IWM) 和 沃尔玛 (WMT)，\n"
    "     利用降息预期的博弈进行对冲。\n\n"
    "3. 监控指标\n"
    "   - 必须看到比特币在 $86,000 上方企稳，\n"
    "     这代表流动性不再恶化。"
)
draw_text_block(fig5, 0.65, 0.80, '交易执行清单', text_strategy, width=0.3)

pp.savefig(fig5)
plt.close(fig5)

pp.close()
print(f"PDF Report generated: {pdf_filename}")
