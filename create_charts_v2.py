
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# 1. Setup Fonts (HarmonyOS Sans SC)
font_dir = r'C:\Users\LXG\us stocks\HarmonyOS Sans\HarmonyOS_Sans_SC'
font_path_bold = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Bold.ttf')
font_path_regular = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Regular.ttf')
font_path_light = os.path.join(font_dir, 'HarmonyOS_Sans_SC_Light.ttf')

prop_title = fm.FontProperties(fname=font_path_bold, size=20)
prop_subtitle = fm.FontProperties(fname=font_path_regular, size=14)
prop_label = fm.FontProperties(fname=font_path_light, size=11)
prop_val = fm.FontProperties(fname=font_path_bold, size=11)

# 2. Premium Minimalist Style Configuration
C_BLACK = '#111111'
C_GRAY = '#666666'
C_LIGHT_GRAY = '#e0e0e0'
C_ACCENT = '#d00000'  # High-end Red
C_WHITE = '#ffffff'

def setup_chart(ax):
    ax.set_facecolor(C_WHITE)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(C_BLACK)
    ax.spines['bottom'].set_linewidth(1)
    ax.tick_params(axis='x', colors=C_BLACK, length=4)
    ax.tick_params(axis='y', length=0)
    ax.grid(axis='y', linestyle=':', color=C_LIGHT_GRAY, linewidth=0.8)
    ax.set_axisbelow(True)

def save_chart_liquidity():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=C_WHITE)
    
    metrics = ['盘口深度 ($M)', 'ETF 成交占比 (%)']
    vals_crisis = [5, 41] 
    vals_avg = [11, 28]
    
    y_pos = np.arange(len(metrics))
    height = 0.35
    
    rects1 = ax.barh(y_pos - height/2, vals_avg, height, label='2025 Avg', color=C_LIGHT_GRAY)
    rects2 = ax.barh(y_pos + height/2, vals_crisis, height, label='11.21 Event', color=C_BLACK)
    
    ax.bar_label(rects1, padding=5, fontproperties=prop_label, color=C_GRAY)
    ax.bar_label(rects2, padding=5, fontproperties=prop_val, color=C_BLACK)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(metrics, fontproperties=prop_subtitle)
    ax.set_xticks([]) 
    ax.legend(frameon=False, prop=prop_label, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2)
    
    setup_chart(ax)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    plt.tight_layout()
    fig.savefig('chart_liquidity_v2.png', dpi=300, bbox_inches='tight', transparent=False)
    plt.close(fig)

def save_chart_quant():
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=C_WHITE)
    
    periods = ['T+1 日', 'T+1 周', 'T+1 月']
    returns = [2.33, 2.88, 4.72]
    
    bars = ax.bar(periods, returns, color=C_LIGHT_GRAY, width=0.5)
    bars[-1].set_color(C_ACCENT) 
    
    ax.bar_label(bars, fmt='+%.2f%%', padding=5, fontproperties=prop_val, fontsize=12)
    
    ax.set_yticks([])
    ax.set_xticklabels(periods, fontproperties=prop_title)
    
    setup_chart(ax)
    ax.axhline(0, color=C_BLACK, linewidth=1)
    ax.spines['bottom'].set_visible(False)
    
    plt.tight_layout()
    fig.savefig('chart_quant_v2.png', dpi=300, bbox_inches='tight', transparent=False)
    plt.close(fig)

def save_chart_cta():
    fig, ax = plt.subplots(figsize=(12, 4), facecolor=C_WHITE)
    
    current = 6538
    threshold = 6456
    start_range = 6300
    end_range = 6700
    
    ax.set_ylim(0, 1)
    ax.set_xlim(start_range, end_range)
    ax.axis('off') 
    
    # Base line
    ax.plot([start_range, end_range], [0.5, 0.5], color=C_LIGHT_GRAY, linewidth=2, zorder=1)
    
    # Danger Zone
    ax.plot([start_range, threshold], [0.5, 0.5], color=C_ACCENT, linewidth=4, alpha=0.2, zorder=1)

    # Points
    ax.scatter([threshold], [0.5], color=C_ACCENT, s=150, zorder=2)
    ax.text(threshold, 0.3, f'CTA 卖出阈值\n{threshold}', ha='center', va='top', 
            fontproperties=prop_val, color=C_ACCENT)
            
    ax.scatter([current], [0.5], color=C_BLACK, s=200, zorder=3, marker='|', linewidth=3)
    ax.text(current, 0.7, f'当前价格\n{current}', ha='center', va='bottom', 
            fontproperties=prop_title, color=C_BLACK)
            
    # Buffer annotation
    mid_point = (threshold + current) / 2
    ax.annotate('', xy=(threshold, 0.55), xytext=(current, 0.55),
                arrowprops=dict(arrowstyle='<->', color=C_GRAY, linewidth=1))
    ax.text(mid_point, 0.6, '1.3% 缓冲', ha='center', fontproperties=prop_label, color=C_GRAY)

    plt.tight_layout()
    fig.savefig('chart_cta_v2.png', dpi=300, bbox_inches='tight', transparent=False)
    plt.close(fig)

print("Generating charts with HarmonyOS Sans...")
save_chart_liquidity()
save_chart_quant()
save_chart_cta()
print("Charts generated.")
