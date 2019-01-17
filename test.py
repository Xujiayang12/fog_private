import numpy as np
import plotly
import plotly.graph_objs as go

'''创建仿真数据'''
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

'''构造trace0'''
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)

'''构造trace1'''
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)

'''构造trace2'''
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

'''将所有trace保存在列表中'''
data = [trace0, trace1, trace2]

'''启动绘图'''
# plotly.offline.init_notebook_mode()
# plotly.offline.plot(data, filename='output/scatter-mode.html')
print(random_x.tolist())