
import os
import re
import base64

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
OUTPUT_FILE = 'Market_Analysis_Final.html'
PARTS = ['Part1_Analysis.md', 'Part2_Analysis.md', 'Part3_Analysis.md', 'Part4_Analysis.md']
FONT_PATH_REGULAR = './HarmonyOS Sans/HarmonyOS_Sans_SC/HarmonyOS_Sans_SC_Regular.ttf'
FONT_PATH_BOLD = './HarmonyOS Sans/HarmonyOS_Sans_SC/HarmonyOS_Sans_SC_Bold.ttf'
FONT_PATH_LIGHT = './HarmonyOS Sans/HarmonyOS_Sans_SC/HarmonyOS_Sans_SC_Light.ttf'

# Chart Mapping (Filename -> Section Keyword or ID)
CHARTS_MAPPING = {
    'chart_intraday_reversal.png': '1.1.1',
    'chart_liquidity_depth.png': '1.2.1',
    'chart_btc_correlation.png': '2.1.2',
    'chart_rate_cut_prob.png': '2.3.1',
    'chart_historical_returns.png': '3.1.2',
    'chart_cta_threshold.png': '3.2.2',
    'chart_fund_flow_rsi.png': '4.2.2',
    'chart_valuation_scatter.png': '4.2.3'
}

# ---------------------------------------------------------
# ADVANCED PARSER LOGIC
# ---------------------------------------------------------
def parse_markdown(text):
    lines = text.split('\n')
    html_output = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines but close lists if open
        if not line:
            if in_list:
                html_output.append("</ul>")
                in_list = False
            continue
            
        # 1. Handle Headers
        if line.startswith('# '):
            html_output.append(f'<h1>{process_inline(line[2:])}</h1>')
            continue
        if line.startswith('## '):
            html_output.append(f'<h2>{process_inline(line[3:])}</h2>')
            continue
        if line.startswith('### '):
            html_output.append(f'<h3>{process_inline(line[4:])}</h3>')
            continue
            
        # 2. Handle Lists
        if line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html_output.append("<ul>")
                in_list = True
            html_output.append(f'<li>{process_inline(line[2:])}</li>')
            continue
        else:
            if in_list:
                html_output.append("</ul>")
                in_list = False
                
        # 3. Handle Blockquotes
        if line.startswith('> '):
            html_output.append(f'<blockquote>{process_inline(line[2:])}</blockquote>')
            continue
            
        # 4. Normal Paragraphs
        html_output.append(f'<p>{process_inline(line)}</p>')
        
    if in_list:
        html_output.append("</ul>")
        
    return '\n'.join(html_output)

def process_inline(text):
    # Bold: **text** -> <strong>text</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text* -> <em>text</em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    return text

def get_base64_image(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return None

# ---------------------------------------------------------
# HTML GENERATION
# ---------------------------------------------------------
def build_report():
    # Load Content
    full_content = ""
    
    # Intro Section
    full_content += """
    <div class="intro-section">
        <div class="meta-tag">2025 Q4 STRATEGY</div>
        <h1 class="report-title">流动性真空与<br>市场新秩序</h1>
        <p class="report-subtitle">2025年11月21日暴跌的全景式复盘与战略展望</p>
        
        <div class="executive-summary">
            <span class="summary-label">EXECUTIVE SUMMARY</span>
            <p>2025年11月21日，美股经历了一场罕见的“高开低走”，标普500在利好中暴跌。本报告通过微观结构分析指出，这并非熊市的开始，而是<strong>宏观风险消退后的获利了结 (Unwind)</strong>。在极度枯竭的流动性下，市场完成了一次剧烈的清洗。历史量化数据显示，此类形态往往是多头行情的“空中加油”，T+1月平均上涨 <strong>4.72%</strong>。</p>
        </div>
    </div>
    <hr class="divider">
    """

    # Process Markdown Files
    for part_file in PARTS:
        if os.path.exists(part_file):
            with open(part_file, 'r', encoding='utf-8') as f:
                raw_md = f.read()
                
            # Custom parsing per line to inject charts correctly
            lines = raw_md.split('\n')
            in_list = False
            
            for line in lines:
                line = line.strip()
                if not line:
                    if in_list: full_content += "</ul>"; in_list = False
                    continue
                
                # Inject Charts Logic
                chart_to_insert = None
                for filename, key in CHARTS_MAPPING.items():
                    if key in line: # If section header matches key (e.g., "1.1.1")
                        chart_to_insert = filename
                        break
                
                # Parse Logic Copy (Simplified integration)
                processed_line = ""
                if line.startswith('# '):
                    processed_line = f'<h1 class="chapter-title">{process_inline(line[2:])}</h1>'
                elif line.startswith('## '):
                    processed_line = f'<h2>{process_inline(line[3:])}</h2>'
                elif line.startswith('### '):
                    processed_line = f'<h3>{process_inline(line[4:])}</h3>'
                elif line.startswith('- ') or line.startswith('* '):
                    if not in_list: full_content += "<ul>"; in_list = True
                    processed_line = f'<li>{process_inline(line[2:])}</li>'
                elif line.startswith('> '):
                    processed_line = f'<blockquote>{process_inline(line[2:])}</blockquote>'
                else:
                    if in_list: full_content += "</ul>"; in_list = False
                    processed_line = f'<p>{process_inline(line)}</p>'
                
                full_content += processed_line
                
                # Insert Chart if matched
                if chart_to_insert:
                    b64 = get_base64_image(chart_to_insert)
                    if b64:
                        full_content += f"""
                        <figure class="chart-wrapper">
                            <img src="data:image/png;base64,{b64}" alt="Chart">
                            <figcaption>图表数据来源：Horizon Global Strategy / 交易台监控</figcaption>
                        </figure>
                        """
            
            if in_list: full_content += "</ul>"
            full_content += "<div class='section-break'></div>"

    # HTML Template
    html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Market Analysis Report</title>
        <style>
            /* 1. FONTS */
            @font-face {{
                font-family: 'HarmonyOS Sans SC';
                src: url('{FONT_PATH_REGULAR}') format('truetype');
                font-weight: 400;
            }}
            @font-face {{
                font-family: 'HarmonyOS Sans SC';
                src: url('{FONT_PATH_BOLD}') format('truetype');
                font-weight: 700;
            }}
            @font-face {{
                font-family: 'HarmonyOS Sans SC';
                src: url('{FONT_PATH_LIGHT}') format('truetype');
                font-weight: 300;
            }}

            /* 2. VARIABLES */
            :root {{
                --bg-color: #fcfcfc;
                --paper-color: #ffffff;
                --text-main: #1a1a1a;
                --text-muted: #666666;
                --accent: #b91c1c; /* Premium Red */
                --border: #e5e7eb;
                --spacing: 2rem;
                --font-main: 'HarmonyOS Sans SC', system-ui, -apple-system, sans-serif;
            }}

            /* 3. RESET & BASE */
            * {{ box-sizing: border-box; }}
            body {{
                font-family: var(--font-main);
                background-color: var(--bg-color);
                color: var(--text-main);
                line-height: 1.75;
                margin: 0;
                font-size: 17px;
                -webkit-font-smoothing: antialiased;
            }}

            /* 4. LAYOUT */
            .container {{
                max-width: 760px;
                margin: 0 auto;
                background: var(--paper-color);
                padding: 80px 60px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.03);
                min-height: 100vh;
            }}

            /* 5. TYPOGRAPHY */
            h1, h2, h3 {{ 
                color: #000;
                margin-top: 3rem;
                margin-bottom: 1.5rem;
                font-weight: 700;
                letter-spacing: -0.02em;
            }}

            .chapter-title {{
                font-size: 32px;
                border-top: 2px solid #000;
                padding-top: 20px;
                margin-top: 60px;
            }}

            h2 {{ font-size: 24px; }}
            h3 {{ font-size: 19px; color: #333; margin-top: 2rem; }}
            
            p {{ margin-bottom: 1.5rem; text-align: justify; }}
            
            strong {{
                font-weight: 700;
                color: #000;
            }}
            
            ul {{
                padding-left: 1.5rem;
                margin-bottom: 1.5rem;
            }}
            
            li {{
                margin-bottom: 0.5rem;
                position: relative;
            }}

            /* 6. COMPONENTS */
            
            /* Intro */
            .intro-section {{ margin-bottom: 60px; }}
            .meta-tag {{
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 2px;
                color: var(--accent);
                margin-bottom: 20px;
            }}
            .report-title {{
                font-size: 48px;
                line-height: 1.1;
                margin: 0 0 20px 0;
            }}
            .report-subtitle {{
                font-size: 20px;
                color: var(--text-muted);
                font-weight: 300;
                margin-bottom: 40px;
            }}

            /* Executive Summary */
            .executive-summary {{
                background: #f8f9fa;
                padding: 30px;
                border-left: 4px solid var(--accent);
            }}
            .summary-label {{
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 1px;
                color: var(--text-muted);
                display: block;
                margin-bottom: 10px;
            }}
            .executive-summary p {{
                font-size: 16px;
                margin: 0;
                font-weight: 500;
            }}

            /* Charts */
            .chart-wrapper {{
                margin: 40px -40px; /* Breakout */
                text-align: center;
            }}
            .chart-wrapper img {{
                max-width: 100%;
                height: auto;
                border: 1px solid rgba(0,0,0,0.05);
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }}
            figcaption {{
                font-size: 12px;
                color: #888;
                margin-top: 10px;
                font-family: var(--font-main);
            }}

            /* Quotes */
            blockquote {{
                font-size: 20px;
                font-weight: 300;
                font-style: italic;
                text-align: center;
                margin: 40px 0;
                padding: 20px;
                border-top: 1px solid var(--border);
                border-bottom: 1px solid var(--border);
            }}

            /* Divider */
            .divider {{
                border: 0;
                height: 1px;
                background: var(--border);
                margin: 60px 0;
            }}

            /* Footer */
            .footer {{
                margin-top: 100px;
                padding-top: 40px;
                border-top: 1px solid var(--border);
                text-align: center;
                font-size: 12px;
                color: #aaa;
            }}

            @media (max-width: 768px) {{
                .container {{ padding: 40px 20px; }}
                .chart-wrapper {{ margin: 30px 0; }}
                .report-title {{ font-size: 36px; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {full_content}
            
            <div class="footer">
                <p>GEMINI AI RESEARCH | 2025</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully Generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_report()
