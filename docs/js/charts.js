// web_report/js/charts.js

// Institutional Theme Configuration
const THEME = {
    text: '#1a202c',
    subtext: '#64748b',
    grid: '#f1f5f9',
    red: '#991b1b', // Signal Crimson
    blue: '#0f172a', // Institutional Blue
    gold: '#b45309', // Bronze
    white: '#ffffff',
    gray: '#cbd5e1',
    midGray: '#adb5bd' // New: for CTA safe zone track
};

const commonConfig = {
    backgroundColor: 'transparent',
    textStyle: { fontFamily: "'Inter', sans-serif" },
    grid: { top: 70, right: 30, bottom: 50, left: 60, containLabel: true },
    tooltip: {
        trigger: 'axis',
        backgroundColor: 'rgba(255,255,255,0.95)',
        borderColor: THEME.grid,
        borderWidth: 1,
        textStyle: { color: THEME.text, fontSize: 13, fontFamily: "'Inter', sans-serif" },
        padding: [12, 16],
        extraCssText: 'box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); border-radius: 6px;'
    }
};

// 1. Intraday Reversal (Smoothed)
function initChartIntraday() {
    const chart = echarts.init(document.getElementById('chart-intraday'));
    const option = {
        ...commonConfig,
        title: { 
            text: '标普500 vs 英伟达: 日内反转走势', 
            subtext: '11月21日 | 标准化涨跌幅',
            left: '0%',
            textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue }
        },
        legend: { bottom: 0, icon: 'rect', data: ['NVDA (英伟达)', 'S&P 500 (标普)'] },
        xAxis: {
            type: 'category',
            data: ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '14:00', '15:00', '16:00'],
            boundaryGap: false,
            axisLine: { show: false },
            axisTick: { show: false },
            axisLabel: { color: THEME.subtext }
        },
        yAxis: { 
            type: 'value', 
            axisLabel: { formatter: '{value}%', color: THEME.subtext },
            splitLine: { lineStyle: { color: THEME.grid } }
        },
        series: [
            {
                name: 'NVDA (英伟达)',
                type: 'line',
                smooth: 0.3, // Smoother curve
                symbol: 'none',
                lineStyle: { width: 3, color: THEME.blue },
                data: [4.5, 4.9, 3.8, 2.1, 1.2, 0.5, -0.8, -1.5, -2.8, -3.2],
                markLine: {
                    symbol: 'none',
                    label: { formatter: '反转开始', position: 'insideEndTop' },
                    lineStyle: { color: THEME.red, type: 'dashed' },
                    data: [{ xAxis: '10:00' }]
                }
            },
            {
                name: 'S&P 500 (标普)',
                type: 'line',
                smooth: 0.3,
                symbol: 'none',
                lineStyle: { width: 2, color: THEME.gold, type: 'solid' },
                areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: 'rgba(180, 83, 9, 0.1)' },
                        { offset: 1, color: 'rgba(180, 83, 9, 0)' }
                    ])
                },
                data: [1.2, 1.4, 1.1, 0.6, 0.1, -0.4, -0.9, -1.2, -1.4, -1.6]
            }
        ]
    };
    chart.setOption(option);
}

// 2. Liquidity Depth Analysis
function initChartLiquidity() {
    const chart = echarts.init(document.getElementById('chart-liquidity'));
    const option = {
        ...commonConfig,
        title: { text: '市场深度: 标普500期货 (盘口)', left: '0%', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { left: '22%', top: 60, bottom: 40 }, /* Increased left padding */
        xAxis: { show: false },
        yAxis: { 
            type: 'category', 
            data: ['2025年均值', '11.21 事件日'], 
            axisLine: { show: false }, 
            axisTick: { show: false },
            axisLabel: { fontSize: 14, fontWeight: 600, color: THEME.text }
        },
        series: [{
            type: 'bar',
            barWidth: 25, /* Further adjusted bar width */
            label: { show: true, position: 'right', formatter: '${c}M', fontWeight: 'bold', fontSize: 14 },
            itemStyle: { borderRadius: 2 },
            data: [
                { value: 11, itemStyle: { color: THEME.gray }, label: { color: THEME.subtext } },
                { value: 5, itemStyle: { color: THEME.red }, label: { color: THEME.red, formatter: '${c}M (极度枯竭)' } }
            ]
        }]
    };
    chart.setOption(option);
}

// 3. Bitcoin vs Nasdaq Correlation
function initChartBTC() {
    const chart = echarts.init(document.getElementById('chart-btc'));
    const option = {
        ...commonConfig,
        title: { text: '流动性代理: 比特币 vs 纳斯达克100', left: '0%', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        legend: { bottom: 0, data: ['比特币', '纳斯达克100'] },
        tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } },
        xAxis: { type: 'category', data: ['11月17', '11月18', '11月19', '11月20', '11月21'], boundaryGap: false, axisLine: { show: false }, axisLabel: { color: THEME.subtext } },
        yAxis: [
            { type: 'value', name: '比特币 ($)', min: 85000, axisLine: { show: false }, splitLine: { show: true, lineStyle: { color: THEME.grid } }, axisLabel: { color: THEME.subtext } },
            { type: 'value', name: '纳斯达克100', min: 19500, axisLine: { show: false }, splitLine: { show: false }, axisLabel: { color: THEME.subtext } }
        ],
        series: [
            {
                name: '比特币',
                type: 'line',
                data: [91500, 92000, 90500, 89000, 86300],
                lineStyle: { color: THEME.gold, width: 3 },
                itemStyle: { color: THEME.gold },
                yAxisIndex: 0
            },
            {
                name: '纳斯达克100',
                type: 'line',
                data: [20500, 20600, 20450, 20100, 19800],
                lineStyle: { color: THEME.blue, width: 2, type: 'dashed' },
                itemStyle: { color: THEME.blue },
                yAxisIndex: 1
            }
        ]
    };
    chart.setOption(option);
}

// 4. Historical Returns
function initChartHistory() {
    const chart = echarts.init(document.getElementById('chart-history'));
    const option = {
        ...commonConfig,
        title: { text: '标普500 "高开低走" 后表现', subtext: '基于1957年以来的8次历史事件', left: 'center', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { bottom: 60 }, /* Added space for x-axis labels */
        xAxis: { type: 'category', data: ['T+1 日', 'T+1 周', 'T+1 月'], axisLine: { show: false }, axisTick: { show: false }, axisLabel: { color: THEME.subtext, fontSize: 12 } },
        yAxis: { show: false },
        series: [{
            type: 'bar',
            barWidth: '35%',
            data: [
                { value: 2.33, itemStyle: { color: THEME.gray }, label: { show: true, position: 'top', formatter: '+{c}%', fontWeight: 'bold', fontSize: 14 } },
                { value: 2.88, itemStyle: { color: THEME.gray }, label: { show: true, position: 'top', formatter: '+{c}%', fontWeight: 'bold', fontSize: 14 } },
                { value: 4.72, itemStyle: { color: THEME.blue }, label: { show: true, position: 'top', formatter: '+{c}%', fontWeight: 'bold', fontSize: 18, color: THEME.blue } }
            ]
        }]
    };
    chart.setOption(option);
}

// 5. CTA Threshold Model
function initChartCTA() {
    const chart = echarts.init(document.getElementById('chart-cta'));
    const option = {
        ...commonConfig,
        title: { text: 'CTA 策略卖出触发点', left: 'center', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { top: 80, bottom: 60, left: 40, right: 40 },
        xAxis: { min: 6200, max: 6800, axisLabel: { show: true, color: THEME.subtext, fontSize: 12 }, axisLine: { show: false }, splitLine: { show: false } },
        yAxis: { show: false, min: -1, max: 1 },
        series: [{
            type: 'custom',
            renderItem: function (params, api) {
                const y = api.coord([0, 0])[1];
                const start = api.coord([6200, 0])[0]; // Updated min
                const end = api.coord([6800, 0])[0];   // Updated max
                const threshold = api.coord([6456, 0])[0];
                const current = api.coord([6538, 0])[0];
                
                return {
                    type: 'group',
                    children: [
                        // 1. Full Track (Neutral/Safe Zone part background)
                        { type: 'rect', shape: { x: start, y: y - 2, width: end - start, height: 4 }, style: { fill: THEME.midGray } }, // Use midGray
                        // 2. Danger Zone (Red Highlight, overlaying the full track)
                        { type: 'rect', shape: { x: start, y: y - 2, width: threshold - start, height: 4 }, style: { fill: 'rgba(220, 38, 38, 0.4)' } }, // Slightly more opaque red
                        
                        // 3. Threshold: Vertical Line + Label BELOW
                        { type: 'line', shape: { x1: threshold, y1: y - 25, x2: threshold, y2: y + 25 }, style: { stroke: THEME.red, lineWidth: 3 } },
                        {
                            type: 'text', 
                            style: { 
                                text: '6456\n(触发线)', 
                                x: threshold, 
                                y: y + 35, 
                                textAlign: 'center', 
                                fill: THEME.red, 
                                font: 'bold 14px Inter',
                                textVerticalAlign: 'top'
                            } 
                        },

                        // 4. Current Price: Arrow (Triangle) + Label ABOVE
                        {
                            type: 'polygon', 
                            shape: { points: [[current, y], [current - 8, y - 15], [current + 8, y - 15]] }, 
                            style: { fill: THEME.blue } 
                        },
                        {
                            type: 'text', 
                            style: {
                                text: '6538\n(当前)', 
                                x: current, 
                                y: y - 25, 
                                textAlign: 'center', 
                                fill: THEME.blue, 
                                font: 'bold 14px Inter',
                                textVerticalAlign: 'bottom'
                            } 
                        }
                    ]
                };
            },
            data: [0]
        }]
    };
    chart.setOption(option);
}

// 6. Rate Cut Probabilities
function initChartRates() {
    const chart = echarts.init(document.getElementById('chart-rates'));
    const option = {
        ...commonConfig,
        title: { text: '12月降息隐含概率', left: '0%', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { bottom: 60 }, /* Increased bottom padding */
        xAxis: { type: 'category', data: ['1月前', '1周前', '11.20 (前)', '11.21 (后)'], axisLine: { show: false }, axisLabel: { color: THEME.subtext, fontSize: 12 } },
        yAxis: { show: false },
        series: [{
            type: 'line',
            smooth: true,
            data: [98, 60, 50, 30],
            lineStyle: { color: THEME.red, width: 4 },
            symbol: 'circle',
            symbolSize: 10,
            itemStyle: { color: THEME.white, borderColor: THEME.red, borderWidth: 3 },
            label: { show: true, position: 'top', formatter: '{c}%', fontWeight: 'bold', fontSize: 14, color: THEME.text },
            areaStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: 'rgba(153, 27, 27, 0.1)' },
                    { offset: 1, color: 'rgba(153, 27, 27, 0)' }
                ])
            }
        }]
    };
    chart.setOption(option);
}

// 7. Volatility Surface (VIX)
function initChartVix() {
    const chart = echarts.init(document.getElementById('chart-vix'));
    const option = {
        ...commonConfig,
        title: { text: 'VIX 期限结构飙升', left: '0%', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { bottom: 60 }, /* Increased bottom padding */
        xAxis: { type: 'category', data: ['11月10', '11月14', '11月18', '11月21'], axisLine: { show: false }, axisLabel: { color: THEME.subtext, fontSize: 12 } },
        yAxis: { min: 12, max: 30, splitLine: { show: false } },
        series: [{
            type: 'bar',
            barWidth: '35%', /* Adjusted bar width */
            data: [14.5, 15.2, 16.8, { value: 26.05, itemStyle: { color: THEME.red } }],
            itemStyle: { color: THEME.blue, borderRadius: [4, 4, 0, 0] },
            label: { show: true, position: 'top', color: THEME.text, fontWeight: 'bold', fontSize: 14 }
        }]
    };
    chart.setOption(option);
}

// 8. Sector Rotation - REMOVED from HTML, function kept for reference but not called
// function initChartSectors() {
//     const chart = echarts.init(document.getElementById('chart-sectors'));
//     const option = {
//         ...commonConfig,
//         title: { text: '板块表现: 防御性轮动', left: '0%' },
//         grid: { left: 80 }, // More space for labels
//         xAxis: { type: 'value', show: false },
//         yAxis: { type: 'category', data: ['科技', '非必需消费', '金融', '必需消费'], axisLine: { show: false }, axisTick: { show: false }, axisLabel: { fontSize: 13, fontWeight: 600 } },
//         series: [{
//             type: 'bar',
//             data: [
//                 { value: -2.4, itemStyle: { color: THEME.red }, label: { show: true, position: 'left', formatter: '{c}%', fontWeight: 'bold' } },
//                 { value: -1.8, itemStyle: { color: THEME.red }, label: { show: true, position: 'left', formatter: '{c}%', fontWeight: 'bold' } },
//                 { value: -0.6, itemStyle: { color: THEME.gray }, label: { show: true, position: 'left', formatter: '{c}%', fontWeight: 'bold' } },
//                 { value: 0.8, itemStyle: { color: '#166534' }, label: { show: true, position: 'right', formatter: '+{c}%', fontWeight: 'bold' } }
//             ]
//         }]
//     };
//     chart.setOption(option);
// }

// 9. Gamma Exposure Profile
function initChartGamma() {
    const chart = echarts.init(document.getElementById('chart-gamma'));
    const option = {
        ...commonConfig,
        title: { text: '做市商 Gamma 敞口: "负翻转"', left: 'center', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        grid: { top: 80, bottom: 80, left: '15%', right: '15%' }, /* Increased top and bottom padding */
        xAxis: {
            type: 'category', 
            data: ['6800', '6725 (翻转)', '6600', '6538 (现价)', '6400'], 
            axisLine: { onZero: false, lineStyle: { color: THEME.subtext } }, // Axis at bottom
            axisLabel: { interval: 0, fontSize: 12, color: THEME.text, fontWeight: 'bold', margin: 15 } 
        },
                yAxis: { 
                    name: '伽马值 ($B)', 
                    min: -10, /* Adjusted min value */
                    max: 10,  /* Adjusted max value */
                    splitLine: { show: false }, 
                    axisLine: { show: false },
                    axisLabel: { color: THEME.subtext } 
                },        series: [{
            type: 'bar',
            barWidth: '40%',
            data: [
                { value: 5, itemStyle: { color: '#166534' }, label: { show: true, position: 'top', formatter: '正 Gamma', fontWeight: 'bold', fontSize: 13, color: THEME.text } },
                { value: 0.5, itemStyle: { color: THEME.gray }, label: { show: true, position: 'top', formatter: '中性', fontWeight: 'bold', fontSize: 13, color: THEME.text } },
                { value: -2, itemStyle: { color: THEME.red }, label: { show: true, position: 'bottom', formatter: '{c} $B', fontWeight: 'bold', fontSize: 13, color: THEME.text } },
                { value: -4.5, itemStyle: { color: THEME.red }, label: { show: true, position: 'bottom', formatter: '{c} $B (加速)', fontWeight: 'bold', fontSize: 13, color: THEME.text } },
                { value: -6, itemStyle: { color: THEME.red }, label: { show: true, position: 'bottom', formatter: '{c} $B', fontWeight: 'bold', fontSize: 13, color: THEME.text } }
            ],
            markLine: {
                symbol: 'none',
                lineStyle: { color: THEME.text, width: 1, type: 'solid' },
                label: { show: false },
                data: [{ yAxis: 0 }]
            }
        }]
    };
    chart.setOption(option);
}

// 10. Fund Flow Divergence
function initChartFlows() {
    const chart = echarts.init(document.getElementById('chart-flows'));
    const option = {
        ...commonConfig,
        title: { text: '资金流向: 科技 vs 必需消费', left: '0%', textStyle: { fontSize: 16, fontWeight: 700, color: THEME.blue } },
        legend: { bottom: 0, data: ['科技 (XLK)', '必需消费 (XLP)'] },
        grid: { bottom: 60, left: 80 }, /* Increased bottom and left padding */
        xAxis: { type: 'category', data: ['周一', '周二', '周三', '周四', '周五'], axisLabel: { color: THEME.subtext } },
        yAxis: { name: '净流入 ($M)', splitLine: { show: false }, axisLabel: { color: THEME.subtext } },
        series: [
            { name: '科技 (XLK)', type: 'bar', stack: 'total', barWidth: '40%', data: [120, 80, -50, -200, -450], itemStyle: { color: THEME.blue } },
            { name: '必需消费 (XLP)', type: 'bar', stack: 'total', barWidth: '40%', data: [-20, -10, 30, 150, 280], itemStyle: { color: THEME.gold } }
        ]
    };
    chart.setOption(option);
}


document.addEventListener('DOMContentLoaded', () => {
    initChartIntraday();
    initChartLiquidity();
    initChartBTC();
    initChartHistory();
    initChartCTA();
    initChartRates();
    initChartVix();
    // initChartSectors(); // REMOVED as per user request
    initChartGamma();
    initChartFlows();
    
    window.addEventListener('resize', () => {
        const charts = document.querySelectorAll('.chart-container');
        charts.forEach(c => {
            const instance = echarts.getInstanceByDom(c);
            if (instance) instance.resize();
        });
    });
});