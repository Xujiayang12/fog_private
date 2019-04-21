from date_processing import *
from data_getter import *
from database_model import *
import plotly
import plotly.graph_objs as go
import warnings

warnings.filterwarnings("ignore")


class Morkov:
    def __init__(self, begin, type_name, period, num):
        self.num = num
        self.period = period
        self.type_name = type_name
        self.data = get_by_time_delta(begin, period * num, type_name)

    def run_Morkov_by_plotly(self):
        max = []
        min = []
        real = []
        time = []
        for i in range(self.num):
            one_data = self.data[0 + i * self.period:self.period + i * self.period - 1]
            std_out = get_std_and_var(one_data, self.type_name)
            # print(std_out)
            d_list = morkov_get_status_list(std_out)
            state_list = morkov_get_state_list(one_data, self.type_name, d_list)
            # print(state_list)
            print(d_list)
            matrix = morkov_get_transfer_matrix(state_list)
            # print(matrix)
            w_list = morkov_get_w_list(one_data, self.type_name, std_out)
            # print(w_list)
            pre_num = morkov_final(w_list, state_list, matrix, d_list)
            real_num = self.data.iloc[self.period + i * self.period - 1][self.type_name]
            min.append(float(pre_num[0]))
            max.append(float(pre_num[1]))
            real.append(float(real_num))
            time.append(self.data.iloc[self.period + i * self.period - 1]['timestamp'])
        trace0 = go.Scatter(x=time, y=max, mode='lines+markers',
                            name='预测最大值')
        trace1 = go.Scatter(x=time, y=min, mode='lines+markers',
                            name='预测最小值')
        trace2 = go.Scatter(x=time, y=real, mode='lines+markers',
                            name='真实值')
        data2 = [trace0, trace1, trace2]
        plotly.offline.plot(data2, filename='output/morkov.html')
