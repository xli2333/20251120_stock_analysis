import os
import base64

# Configuration
OUTPUT_FILE = 'Market_Analysis_Full_Report.html'
PARTS = ['Part1_Analysis.md', 'Part2_Analysis.md', 'Part3_Analysis.md', 'Part4_Analysis.md']
CHARTS = {
    'chart_liquidity_depth.png': '1.2.1', # Insert after section 1.2.1
    'chart_intraday_reversal.png': '1.1.1',
    'chart_btc_correlation.png': '2.1.2',
    'chart_rate_cut_prob.png': '2.3.1',
    'chart_historical_returns.png': '3.1.2',
    'chart_cta_threshold.png': '3.2.2',
    'chart_fund_flow_rsi.png': '4.2.2',
    'chart_valuation_scatter.png': '4.2.3'
}

# CSS Styles (Premium Minimalist)
CSS = """
<style>
    @font-face {
        font-family: 'HarmonyOS Sans SC';
        src: url('./HarmonyOS Sans/HarmonyOS_Sans_SC/HarmonyOS_Sans_SC_Regular.ttf') format('truetype');
        font-weight: normal;
    }
    @font-face {
        font-family: 'HarmonyOS Sans SC';
        src: url('./HarmonyOS Sans/HarmonyOS_Sans_SC/HarmonyOS_Sans_SC_Bold.ttf') format('truetype');
        font-weight: bold;
    }
    
    :root {
        --bg: #ffffff;
        --text: #1a1a1a;
        --accent: #c92a2a;
        --gray: #666666;
        --light: #f8f9fa;
        --border: #e9ecef;
    }
    
    body {
        font-family: 'HarmonyOS Sans SC', "Microsoft YaHei", sans-serif;
        background: var(--bg);
        color: var(--text);
        line-height: 1.8;
        margin: 0;
        padding: 0;
    }
    
    .container {
        max-width: 900px;
        margin: 0 auto;
        padding: 60px 20px;
    }
    
    /* Header */
    header {
        border-bottom: 4px solid var(--text);
        padding-bottom: 40px;
        margin-bottom: 60px;
    }
    
    .meta {
        font-size: 14px;
        color: var(--gray);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }
    
    h1.main-title {
        font-size: 48px;
        font-weight: bold;
        line-height: 1.2;
        margin: 0 0 20px 0;
    }
    
    .subtitle {
        font-size: 24px;
        color: var(--gray);
        font-weight: normal;
    }
    
    /* Content */
    h1 { font-size: 32px; margin-top: 80px; border-left: 5px solid var(--accent); padding-left: 20px; }
    h2 { font-size: 24px; margin-top: 50px; color: #333; font-weight: bold; }
    h3 { font-size: 18px; margin-top: 30px; color: #555; font-weight: bold; }
    p { margin-bottom: 20px; font-size: 18px; text-align: justify; }
    
    /* Charts */
    .chart-box {
        margin: 40px 0;
        padding: 20px;
        background: var(--light);
        border: 1px solid var(--border);
        text-align: center;
        border-radius: 4px;
    }
    
    .chart-box img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 0 auto;
    }
    
    .caption {
        margin-top: 15px;
        font-size: 14px;
        color: var(--gray);
        font-style: italic;
    }
    
    /* Table of Contents */
    .toc {
        background: var(--light);
        padding: 40px;
        margin-bottom: 60px;
        border-radius: 8px;
    }
    
    .toc h2 { margin-top: 0; font-size: 20px; }
    .toc ul { padding-left: 20px; }
    .toc li { margin-bottom: 10px; }
    
    /* Footer */
    footer {
        margin-top: 100px;
        padding-top: 40px;
        border-top: 1px solid var(--border);
        text-align: center;
        color: var(--gray);
        font-size: 12px;
    }
</style>
"""

def get_img_tag(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"""<div class="chart-box"><img src="data:image/png;base64,{encoded_string}" alt="{filename}"><div class="caption">Figure: {filename.replace('.png', '').replace('_', ' ').title()}</div></div>"""
    return ""

def build_html():
    content_body = ""
    
    # TOC Placeholder
    toc_html = """
    <div class="toc">
        <h2>目录 (Table of Contents)</h2>
        <ul>
            <li><strong>第一部分</strong>：法医学式复盘 —— 11.21 市场崩溃的解剖</li>
            <li><strong>第二部分</strong>：全球资产联动与深层归因</li>
            <li><strong>第三部分</strong>：量化指引与历史镜像</li>
            <li><strong>第四部分</strong>：未来策略与战术执行</li>
        </ul>
    </div>
    """

    for part_file in PARTS:
        if os.path.exists(part_file):
            with open(part_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
                
                # Convert MD headers to HTML (Simple regex-free approach for stability)
                html_chunk = ""
                lines = md_content.split('\n')
                for line in lines:
                    if line.startswith('# '):
                        html_chunk += f"<h1>{line[2:]}</h1>"
                    elif line.startswith('## '):
                        html_chunk += f"<h2>{line[3:]}</h2>"
                    elif line.startswith('### '):
                        section_id = line[4:].split(' ')[0] # Extract 1.1.1
                        html_chunk += f"<h3>{line[4:]}</h3>"
                        
                        # Insert Chart Logic
                        for chart_file, chart_sec in CHARTS.items():
                            # Precise matching for section numbers like '1.1.1'
                            if chart_sec in line:
                                html_chunk += get_img_tag(chart_file)
                                
                    elif line.startswith('- ') or line.startswith('* '):
                         html_chunk += f"<li>{line[2:]}</li>"
                    elif line.strip() == '':
                        continue
                    else:
                        html_chunk += f"<p>{line}</p>"
                
                content_body += html_chunk + "<hr style='margin: 60px 0; border: 0; border-top: 1px solid #eee;'>"

    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>2025深度研报：流动性真空与市场新秩序</title>
        {CSS}
    </head>
    <body>
        <div class="container">
            <header>
                <div class="meta">Global Macro Strategy Research | Nov 2025</div>
                <h1 class="main-title">流动性真空与市场新秩序</h1>
                <div class="subtitle">2025年11月21日暴跌的全景式复盘与战略展望</div>
            </header>
            
            {toc_html}
            
            {content_body}
            
            <footer>
                <p>© 2025 Horizon Global Strategy. All Rights Reserved.</p>
                <p>本报告仅供机构内部参考，不构成投资建议。</p>
            </footer>
        </div>
    </body>
    </html>
    """
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Report Generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_html()