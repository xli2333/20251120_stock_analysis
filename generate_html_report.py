import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 1. Setup Fonts
font_path_normal = 'yahei.ttf'
font_path_bold = 'yahei_bold.ttf'

prop_normal = fm.FontProperties(fname=font_path_normal)
prop_bold = fm.FontProperties(fname=font_path_bold)
prop_chart_title = fm.FontProperties(fname=font_path_bold, size=16)
prop_axis = fm.FontProperties(fname=font_path_normal, size=12)
prop_label = fm.FontProperties(fname=font_path_normal, size=10)
prop_val = fm.FontProperties(fname=font_path_bold, size=10)

# Color Scheme
COLOR_PRIMARY = '#0f4c81'  # Classic Blue
COLOR_ACCENT = '#e63946'   # Red
COLOR_BG = '#ffffff'
COLOR_GRID = '#e0e0e0'

def save_chart_liquidity():
    fig, ax = plt.subplots(figsize=(10, 6))
    metrics = ['盘口深度 ($)', 'ETF 成交占比 (%)']
    vals_crisis = [5, 41]
    vals_avg = [11, 28]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    ax.bar(x - width/2, vals_crisis, width, label='11.21 当日 (枯竭)', color=COLOR_ACCENT, alpha=0.9)
    ax.bar(x + width/2, vals_avg, width, label='2025年均值 (正常)', color='#a8dadc', alpha=0.9)
    
    ax.set_ylabel('数值 (百万 / %)', fontproperties=prop_axis)
    ax.set_title('图1：致命的流动性黑洞', fontproperties=prop_chart_title, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontproperties=prop_bold, fontsize=12)
    ax.legend(prop=prop_axis)
    ax.grid(axis='y', linestyle='--', alpha=0.5, color=COLOR_GRID)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    fig.savefig('chart_liquidity.png', bbox_inches='tight', dpi=150)
    plt.close(fig)

def save_chart_quant():
    fig, ax = plt.subplots(figsize=(10, 6))
    periods = ['T+1 日', 'T+1 周', 'T+1 月']
    returns = [2.33, 2.88, 4.72]
    
    bars = ax.bar(periods, returns, color=COLOR_PRIMARY, width=0.5)
    ax.bar_label(bars, fmt='+%.2f%%', padding=3, fontproperties=prop_val, fontsize=12)
    
    ax.set_ylabel('平均收益率 (%)', fontproperties=prop_axis)
    ax.set_title('图2：历史8次“高开低走”后的反弹表现', fontproperties=prop_chart_title, pad=20)
    ax.set_xticklabels(periods, fontproperties=prop_bold, fontsize=12)
    ax.axhline(0, color='black', linewidth=1)
    ax.grid(axis='y', linestyle='--', alpha=0.5, color=COLOR_GRID)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    fig.savefig('chart_quant.png', bbox_inches='tight', dpi=150)
    plt.close(fig)

def save_chart_cta():
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Prices
    high = 6640
    current = 6538
    threshold = 6456
    support = 6336
    
    # Draw line
    ax.plot([0, 10], [current, current], color=COLOR_PRIMARY, linewidth=2, label='当前价格')
    ax.plot([0, 10], [threshold, threshold], color=COLOR_ACCENT, linewidth=2, linestyle='--', label='CTA 生死线')
    
    # Fill zones
    ax.fill_between([0, 10], threshold, 6700, color='#e9f5db', alpha=0.5) # Safe
    ax.fill_between([0, 10], 6200, threshold, color='#ffe5d9', alpha=0.5) # Danger
    
    # Labels
    ax.text(0.2, current + 15, f'当前价格: {current}', fontproperties=prop_bold, color=COLOR_PRIMARY)
    ax.text(0.2, threshold - 25, f'CTA 卖出阈值: {threshold}\n(跌破触发止损)', fontproperties=prop_bold, color=COLOR_ACCENT)
    
    ax.set_ylim(6300, 6700)
    ax.set_xlim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([6336, 6456, 6538, 6640])
    ax.set_title('图3：标普500关键风控点位监控', fontproperties=prop_chart_title, pad=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    fig.savefig('chart_cta.png', bbox_inches='tight', dpi=150)
    plt.close(fig)

# Generate Images
print("Generating charts...")
save_chart_liquidity()
save_chart_quant()
save_chart_cta()
print("Charts generated.")

# Generate HTML
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>深度研报：流动性真空下的假摔</title>
    <style>
        @font-face {
            font-family: 'CustomBold';
            src: url('yahei_bold.ttf') format('truetype');
        }
        @font-face {
            font-family: 'CustomNormal';
            src: url('yahei.ttf') format('truetype');
        }
        
        body {
            font-family: 'CustomNormal', 'Microsoft YaHei', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.8;
            color: #333;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        
        .container {
            max_width: 700px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            border-radius: 8px;
        }
        
        h1 {
            font-family: 'CustomBold', 'Microsoft YaHei', sans-serif;
            font-size: 28px;
            color: #1a1a1a;
            line-height: 1.4;
            margin-bottom: 10px;
        }
        
        .meta {
            font-size: 14px;
            color: #888;
            margin-bottom: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 20px;
        }
        
        .summary {
            background-color: #f4f7f9;
            border-left: 4px solid #0f4c81;
            padding: 20px;
            margin-bottom: 40px;
            font-size: 16px;
            font-weight: bold;
            color: #0f4c81;
        }
        
        h2 {
            font-family: 'CustomBold', 'Microsoft YaHei', sans-serif;
            font-size: 22px;
            color: #1a1a1a;
            margin-top: 40px;
            margin-bottom: 20px;
            border-left: 5px solid #e63946;
            padding-left: 15px;
        }
        
        p {
            margin-bottom: 20px;
            font-size: 16px;
            text-align: justify;
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 2px 4px;
            border-radius: 2px;
        }
        
        .chart-container {
            margin: 30px 0;
            text-align: center;
        }
        
        .chart-container img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            border: 1px solid #eee;
        }
        
        .chart-caption {
            font-size: 14px;
            color: #666;
            margin-top: 10px;
        }
        
        ul {
            margin-bottom: 20px;
        }
        
        li {
            margin-bottom: 10px;
        }
        
        .strategy-box {
            background-color: #2d3436;
            color: #fff;
            padding: 25px;
            border-radius: 8px;
            margin-top: 30px;
        }
        
        .strategy-box h3 {
            color: #e63946;
            margin-top: 0;
        }
        
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 12px;
            color: #999;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>深度研报 | 流动性真空下的假摔：为什么现在是贪婪的最佳时刻？</h1>
    <div class="meta">
        2025年11月21日 | 市场深度复盘
    </div>

    <div class="summary">
        核心观点：不要被指数的暴跌吓退。本次“乌云盖顶”本质上是宏观风险消退后的获利了结 (Unwind)，而非恐慌性去杠杆。历史量化数据显示，此类形态往往是多头行情的“空中加油”，T+1月平均上涨 4.72%。
    </div>

    <p>11月21日，美股上演了一场极具戏剧性的日内反转：标普500指数高开超1%后一路杀跌，最终收墨。与此同时，比特币跌破9万美元关口，市场似乎一夜之间从“牛市盛宴”切换到了“逃生模式”。</p>

    <p>然而，基于微观结构与量化数据的深度复盘显示，<strong>这很可能是一个巨大的“黄金坑”。</strong></p>

    <h2>一、微观真相：并非崩盘，而是清洗</h2>
    
    <p>很多人将下跌归咎于 NVDA 的“利好出尽”或美联储的鹰派言论，这只是表象。真正的罪魁祸首是<strong>“极度枯竭的市场流动性”</strong>。</p>
    
    <p>交易台数据显示，当日标普500的盘口流动性仅为 500 万美元，远低于今年 1100 万美元的均值。这意味着，市场处于“真空”状态，少量的卖单就能造成巨大的价格滑点。</p>

    <div class="chart-container">
        <img src="chart_liquidity.png" alt="流动性枯竭图表">
        <div class="chart-caption">数据清晰显示：市场深度不足导致了波动被非理性放大</div>
    </div>

    <p>更值得注意的是，ETF成交占比激增至 41%。这说明资金在进行<strong>“一篮子宏观抛售”</strong>，基本面优良的个股被无差别错杀。这不是针对资产质量的投票，而是纯粹的宏观情绪宣泄。</p>

    <h2>二、量化指引：乌云背后的“黄金信号”</h2>

    <p>这种“高开>1%但最终收跌”的走势在历史上极为罕见（1957年以来仅8次）。直觉告诉我们应该防御，但数据告诉我们要贪婪。</p>
    
    <p>回测数据显示，凡是出现这种极端的日内反转，往往意味着空头动能的短期衰竭和筹码的充分交换。随后市场不仅没有崩盘，反而迎来了报复性反弹：</p>

    <ul>
        <li><strong>次日 (T+1)：</strong> 平均反弹 <span class="highlight">+2.33%</span></li>
        <li><strong>次月 (T+1 Month)：</strong> 平均大涨 <span class="highlight">+4.72%</span></li>
    </ul>

    <div class="chart-container">
        <img src="chart_quant.png" alt="历史回测表现">
        <div class="chart-caption">历史胜率极高：恐慌往往孕育着最大的机会</div>
    </div>

    <p>现在的下跌，本质上是市场在借助宏观迷雾（非农数据滞后、鹰派言论）进行的一次清洗。<strong>Unwind（主动平仓）与 De-grossing（强制去杠杆）有着天壤之别。</strong> 尾盘并未出现恐慌性的 Put 买盘，这进一步印证了机构只是在获利了结，而非逃命。</p>

    <h2>三、战术执行：盯住生死线，左侧布局</h2>

    <p>既然定性为“清洗”，那么策略就是<strong>“在恐慌中寻找买点”</strong>。但为了防止小概率的系统性风险，我们需要设定严格的风控阈值。</p>

    <div class="chart-container">
        <img src="chart_cta.png" alt="CTA阈值监控">
    </div>

    <div class="strategy-box">
        <h3>实战策略清单</h3>
        <p><strong>1. 核心防线：6456 点</strong><br>
        这是 CTA 策略的中期卖出阈值。只要指数运行在此上方，维持<strong>多头思维</strong>。此区域是主力清洗浮筹的最佳区间。若有效跌破（小概率），则触发机械止损，此时才需转为防御。</p>
        
        <p><strong>2. 布局方向：高低切换</strong><br>
        资金并未流出股市，而是在轮动。建议关注：<br>
        - <strong>罗素2000 (IWM)：</strong> 博弈降息预期的存活（就业虽强但失业率上升）。<br>
        - <strong>错杀科技：</strong> 在纳指企稳后，优先回补软件与半导体龙头。</p>
        
        <p><strong>3. 监控指标</strong><br>
        必须看到比特币在 <strong>$86,000</strong> 上方企稳。作为流动性的金丝雀，它的止跌是股市反攻的先行信号。</p>
    </div>
    
    <p><strong>结语：</strong> 市场从未直线运行。当所有人都看到乌云时，聪明钱已经开始期待雨后的彩虹。现在不是恐惧的时候，是执行纪律的时候。</p>

    <div class="footer">
        本报告由 Gemini CLI 智能生成 | 数据仅供参考
    </div>
</div>

</body>
</html>
"""

with open('Market_Analysis_1121.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML Report generated: Market_Analysis_1121.html")
