from BP import *
from data_getter import *
import warnings

warnings.filterwarnings("ignore")

pm25 = BP(11, 'tanh', 160000,
          get_by_time_delta_list('2015-1-1', 1100, ['pm25'], ['pm25_1', 'pm25_2', 'pm25_3', 'pm25_4', 'pm25_5']),
          ['pm25_1', 'pm25_2', 'pm25_3', 'pm25_4', 'pm25_5'], ['pm25'], 1000, 20)
if __name__ == '__main__':
    pm25.run_BP_by_plotly()
    # pm25.run_BP_by_echart()
