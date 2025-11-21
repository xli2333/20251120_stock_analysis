
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 1. Setup Fonts (尝试混合使用黑体和宋体，如果宋体不可用则回退)
font_path_bold = 'yahei_bold.ttf'
font_path_normal = 'yahei.ttf'

prop_title = fm.FontProperties(fname=font_path_bold, size=18)
prop_label = fm.FontProperties(fname=font_path_normal, size=10)
prop_val = fm.FontProperties(fname=font_path_bold, size=10)

# 2. Premium Minimalist Style Configuration
# 调色板：克制的高级感
C_BLACK = '#1a1a1a'
C_GRAY = '#888888'
C_LIGHT_GRAY = '#f0f0f0'
C_RED = '#c92a2a'  # 重点高亮色 (高级红)
C_BLUE = '#1864ab' # 辅助高亮色 (深蓝)

def setup_chart(ax):
    # 去除多余元素，极简主义
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(C_BLACK)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.tick_params(axis='x', colors=C_BLACK, length=5)
    ax.tick_params(axis='y', length=0)
    ax.grid(axis='y', linestyle=':', color=C_LIGHT_GRAY, linewidth=1)
    ax.set_axisbelow(True) # 网格在下

def save_chart_liquidity():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    
    metrics = ['盘口深度 ($)', 'ETF 成交占比 (%)']
    # 数据：危机 vs 均值
    vals_crisis = [5, 41] 
    vals_avg = [11, 28]
    
    y_pos = np.arange(len(metrics))
    height = 0.35
    
    # 绘制条形
    rects1 = ax.barh(y_pos - height/2, vals_avg, height, label='2025均值 (Normal)', color=C_LIGHT_GRAY)
    rects2 = ax.barh(y_pos + height/2, vals_crisis, height, label='11.21当日 (Crisis)', color=C_BLACK)
    
    # 极简标注
    ax.bar_label(rects1, padding=5, fontproperties=prop_label, color=C_GRAY)
    ax.bar_label(rects2, padding=5, fontproperties=prop_val, color=C_BLACK)
    
    # 高亮重点
    # ax.patches[-1].set_color(C_RED) # 将 ETF 占比的异常值标红

    ax.set_yticks(y_pos)
    ax.set_yticklabels(metrics, fontproperties=prop_title)
    ax.set_xticks([]) # 移除X轴刻度
    
    setup_chart(ax)
    # 移除左侧轴线
    ax.spines['left'].set_visible(False)
    
    # 标题放到底部或左上角，这里留白给HTML处理
    # ax.set_title('流动性枯竭：市场微观结构的崩塌', loc='left', fontproperties=prop_title, pad=20)

    plt.tight_layout()
    fig.savefig('chart_liquidity_min.png', dpi=200, bbox_inches='tight', transparent=True)
    plt.close(fig)

def save_chart_quant():
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    
    periods = ['T+1 日', 'T+1 周', 'T+1 月']
    returns = [2.33, 2.88, 4.72]
    
    # 极简柱状图
    bars = ax.bar(periods, returns, color=C_LIGHT_GRAY, width=0.6)
    
    # 强调 T+1 月的数据
    bars[-1].set_color(C_RED) 
    
    # 数值标注
    ax.bar_label(bars, fmt='+%.2f%%', padding=5, fontproperties=prop_title, fontsize=12)
    
    ax.set_yticks([]) # 移除Y轴
    ax.set_xticklabels(periods, fontproperties=prop_title, fontsize=12)
    
    setup_chart(ax)
    ax.axhline(0, color=C_BLACK, linewidth=1.5)
    
    plt.tight_layout()
    fig.savefig('chart_quant_min.png', dpi=200, bbox_inches='tight', transparent=True)
    plt.close(fig)

def save_chart_cta():
    fig, ax = plt.subplots(figsize=(10, 3), facecolor='white')
    
    current = 6538
    threshold = 6456
    
    # 绘制单一直线轴
    ax.set_ylim(0, 1)
    ax.set_xlim(6300, 6700)
    ax.axis('off') # 关闭所有坐标轴
    
    # 主轴线
    ax.plot([6300, 6700], [0.5, 0.5], color=C_LIGHT_GRAY, linewidth=2, zorder=1)
    
    # 危险区域
    ax.plot([6300, 6456], [0.5, 0.5], color=C_RED, linewidth=4, alpha=0.3, zorder=1)

    # 关键点标记
    # CTA 阈值
    ax.scatter([threshold], [0.5], color=C_RED, s=100, zorder=2)
    ax.text(threshold, 0.35, f'CTA生死线\n{threshold}', ha='center', va='top', 
            fontproperties=prop_val, color=C_RED)
            
    # 当前价格
    ax.scatter([current], [0.5], color=C_BLACK, s=150, zorder=3, marker='|', linewidth=3)
    ax.text(current, 0.65, f'当前价格\n{current}', ha='center', va='bottom', 
            fontproperties=prop_title, color=C_BLACK)
            
    # 安全边际箭头
    ax.annotate('', xy=(threshold, 0.55), xytext=(current, 0.55),
                arrowprops=dict(arrowstyle='<->', color=C_GRAY))
    ax.text((threshold+current)/2, 0.58, '1.3% 缓冲', ha='center', 
            fontproperties=prop_label, color=C_GRAY)

    plt.tight_layout()
    fig.savefig('chart_cta_min.png', dpi=200, bbox_inches='tight', transparent=True)
    plt.close(fig)

print("Generating minimalist charts...")
save_chart_liquidity()
save_chart_quant()
save_chart_cta()
print("Charts ready.")
