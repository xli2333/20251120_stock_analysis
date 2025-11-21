
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
from matplotlib.patches import Rectangle, Arrow

# 1. Setup Fonts
font_dir = r'C:\Users\LXG\us stocks\HarmonyOS Sans\HarmonyOS_Sans_SC'
font_path_bold = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Bold.ttf')
font_path_regular = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Regular.ttf')
font_path_light = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Light.ttf')

prop_title = fm.FontProperties(fname=font_path_bold, size=16)
prop_subtitle = fm.FontProperties(fname=font_path_regular, size=12)
prop_label = fm.FontProperties(fname=font_path_light, size=10)
prop_val = fm.FontProperties(fname=font_path_bold, size=10)

# 2. Style Config
C_BG = '#ffffff'
C_FG = '#111111'
C_ACCENT = '#c92a2a'
C_BLUE = '#1864ab'
C_GRAY = '#868e96'
C_LIGHT = '#f1f3f5'

def setup_ax(ax):
    ax.set_facecolor(C_BG)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(C_FG)
    ax.spines['bottom'].set_linewidth(1)
    ax.tick_params(axis='x', colors=C_FG, length=4)
    ax.tick_params(axis='y', length=0)
    ax.grid(axis='y', linestyle=':', color=C_LIGHT, linewidth=1)
    ax.set_axisbelow(True)

# Chart 1: Liquidity Depth
def chart_liquidity():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor=C_BG)
    labels = ['2024 Avg', '2025 Avg', '11.21 Event']
    values = [12, 11, 5]
    
    bars = ax.bar(labels, values, color=[C_GRAY, C_GRAY, C_ACCENT], width=0.5)
    ax.bar_label(bars, fmt='$%dM', fontproperties=prop_val, padding=3)
    
    ax.set_title('标普500 盘口流动性深度枯竭', fontproperties=prop_title, loc='left', pad=20)
    ax.set_ylabel('深度 (百万美元)', fontproperties=prop_label)
    
    setup_ax(ax)
    ax.spines['bottom'].set_visible(False)
    
    plt.tight_layout()
    fig.savefig('chart_liquidity_depth.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 2: Intraday Reversal (Simulated Data)
def chart_intraday():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=C_BG)
    
    # Simulate data: 9:30 - 16:00 (390 mins)
    t = np.linspace(0, 390, 390)
    spx = np.concatenate([np.linspace(1.0, 1.2, 30), np.linspace(1.2, -1.6, 360)])
    nvda = np.concatenate([np.linspace(4.5, 5.0, 30), np.linspace(5.0, -2.5, 360)])
    
    ax.plot(t, spx, label='S&P 500', color=C_FG, linewidth=2)
    ax.plot(t, nvda, label='NVDA', color=C_BLUE, linewidth=1.5, linestyle='--')
    
    ax.axhline(0, color=C_GRAY, linewidth=0.5)
    
    # Annotations
    ax.annotate('开盘非理性繁荣', xy=(15, 1.2), xytext=(50, 2.5),
                arrowprops=dict(arrowstyle='->', color=C_ACCENT), fontproperties=prop_label)
    ax.annotate('流动性崩塌', xy=(200, -0.5), xytext=(250, 0.5),
                arrowprops=dict(arrowstyle='->', color=C_ACCENT), fontproperties=prop_label)

    ax.set_title('11.21 日内走势复盘：从贪婪到恐慌', fontproperties=prop_title, loc='left', pad=20)
    ax.set_ylabel('涨跌幅 (%)', fontproperties=prop_label)
    ax.set_xticks([0, 60, 120, 180, 240, 300, 360])
    ax.set_xticklabels(['9:30', '10:30', '11:30', '12:30', '13:30', '14:30', '15:30'], fontproperties=prop_label)
    ax.legend(frameon=False, prop=prop_val)
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_intraday_reversal.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 3: Historical Returns (Boxplot)
def chart_history():
    fig, ax = plt.subplots(figsize=(8, 6), facecolor=C_BG)
    
    # Simulated distribution based on report stats
    data_t1 = np.random.normal(2.33, 0.5, 100)
    data_t5 = np.random.normal(2.88, 0.8, 100)
    data_t20 = np.random.normal(4.72, 1.2, 100)
    
    bplot = ax.boxplot([data_t1, data_t5, data_t20], patch_artist=True,
                       labels=['T+1 日', 'T+1 周', 'T+1 月'],
                       boxprops=dict(facecolor=C_LIGHT, color=C_FG),
                       medianprops=dict(color=C_ACCENT, linewidth=2))
    
    ax.set_title('历史回测：8次“高开低走”后的收益分布', fontproperties=prop_title, loc='left', pad=20)
    ax.set_ylabel('收益率 (%)', fontproperties=prop_label)
    ax.set_xticklabels(['T+1 日', 'T+1 周', 'T+1 月'], fontproperties=prop_val)
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_historical_returns.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 4: CTA Threshold
def chart_cta():
    fig, ax = plt.subplots(figsize=(10, 4), facecolor=C_BG)
    
    current = 6538
    threshold = 6456
    
    ax.set_xlim(6300, 6700)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    ax.plot([6300, 6700], [0.5, 0.5], color=C_GRAY, linewidth=2)
    ax.plot([6300, threshold], [0.5, 0.5], color=C_ACCENT, linewidth=4, alpha=0.3)
    
    # Markers
    ax.plot(current, 0.5, 'o', color=C_FG, markersize=10)
    ax.text(current, 0.6, f'当前价格\n{current}', ha='center', fontproperties=prop_val)
    
    ax.plot(threshold, 0.5, '|', color=C_ACCENT, markersize=30, markeredgewidth=3)
    ax.text(threshold, 0.3, f'CTA 阈值\n{threshold}', ha='center', fontproperties=prop_val, color=C_ACCENT)
    
    ax.annotate('', xy=(threshold, 0.55), xytext=(current, 0.55),
                arrowprops=dict(arrowstyle='<->', color=C_GRAY))
    ax.text((threshold+current)/2, 0.6, '安全缓冲', ha='center', fontproperties=prop_label)
    
    ax.set_title('风控雷达：CTA 策略触发点监控', fontproperties=prop_title, loc='left', pad=0)
    
    plt.tight_layout()
    fig.savefig('chart_cta_threshold.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 5: Rate Cut Prob
def chart_rate():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor=C_BG)
    
    days = ['11/14', '11/15', '11/18', '11/19', '11/20', '11/21']
    probs = [65, 62, 58, 50, 38, 35]
    
    ax.plot(days, probs, marker='o', color=C_BLUE, linewidth=2)
    ax.fill_between(days, probs, 0, color=C_BLUE, alpha=0.1)
    
    ax.set_title('12月降息概率骤降：宏观预期的崩塌', fontproperties=prop_title, loc='left', pad=20)
    ax.set_ylabel('概率 (%)', fontproperties=prop_label)
    ax.set_ylim(0, 80)
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_rate_cut_prob.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 6: BTC Correlation (Simulated)
def chart_btc():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor=C_BG)
    
    t = np.arange(30)
    btc = np.cumsum(np.random.randn(30))
    ndx = btc * 0.8 + np.random.randn(30) * 0.2 # High correlation simulation
    
    ax.plot(t, btc, label='Bitcoin (Normalized)', color=C_ACCENT)
    ax.plot(t, ndx, label='Nasdaq 100 (Normalized)', color=C_FG, linestyle='--')
    
    ax.set_title('加密货币与科技股的高度共振', fontproperties=prop_title, loc='left', pad=20)
    ax.legend(frameon=False, prop=prop_val)
    ax.set_xticks([])
    ax.set_yticks([])
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_btc_correlation.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 7: RSI Divergence
def chart_rsi():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor=C_BG)
    
    metrics = ['Russell 2000', 'Nasdaq 100', 'S&P 500']
    rsi_vals = [42, 68, 55]
    
    bars = ax.barh(metrics, rsi_vals, color=[C_BLUE, C_ACCENT, C_GRAY])
    ax.axvline(70, color=C_ACCENT, linestyle='--', alpha=0.5)
    ax.text(71, 2, '超买区域', fontproperties=prop_label, color=C_ACCENT)
    
    ax.bar_label(bars, fontproperties=prop_val, padding=3)
    
    ax.set_title('相对强弱分析：拥挤的科技 vs 低估的小盘', fontproperties=prop_title, loc='left', pad=20)
    ax.set_xlim(0, 100)
    ax.set_yticklabels(metrics, fontproperties=prop_val)
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_fund_flow_rsi.png', dpi=300, bbox_inches='tight')
    plt.close()

# Chart 8: Valuation Scatter
def chart_valuation():
    fig, ax = plt.subplots(figsize=(8, 6), facecolor=C_BG)
    
    # Mock Data
    tickers = ['NVDA', 'MSFT', 'GOOGL', 'AMD', 'CRM']
    pe = [45, 32, 25, 38, 28]
    growth = [50, 15, 12, 20, 10]
    
    ax.scatter(pe, growth, s=150, color=C_BLUE, alpha=0.7)
    
    for i, txt in enumerate(tickers):
        ax.annotate(txt, (pe[i]+1, growth[i]), fontproperties=prop_val)
        
    # PEG = 1 Line
    x = np.linspace(0, 60, 100)
    ax.plot(x, x, color=C_GRAY, linestyle='--', label='PEG = 1 (合理估值)')
    
    ax.set_xlabel('P/E (市盈率)', fontproperties=prop_label)
    ax.set_ylabel('Growth (预期增速 %)', fontproperties=prop_label)
    ax.set_title('AI 板块估值压力测试', fontproperties=prop_title, loc='left', pad=20)
    ax.legend(prop=prop_label)
    
    setup_ax(ax)
    plt.tight_layout()
    fig.savefig('chart_valuation_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()

print("Generating 8 Charts...")
chart_liquidity()
chart_intraday()
chart_history()
chart_cta()
chart_rate()
chart_btc()
chart_rsi()
chart_valuation()
print("Done.")
