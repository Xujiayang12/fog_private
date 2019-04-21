from BP import *
from data_getter import *
from Morkov import *
from bp_morkov import *
import warnings

warnings.filterwarnings("ignore")

pm25 = BP_Morkov(11, 'tanh', 16000,
          get_by_time_delta_list('2015-1-1', 1100, ['pm25'], ['pm25_1', 'pm25_2', 'pm25_3', 'pm25_4', 'pm25_5']),
          ['pm25_1', 'pm25_2', 'pm25_3', 'pm25_4', 'pm25_5'], ['pm25'], 100, 20)
o3 = Morkov('2014-1-1','o3',100,5)

pm25_now = BP(11, 'tanh', 160000,
          get_by_time_delta_list('2015-1-1', 1100, ['pm25'], ['o3', 'pm10', 'so2', 'co', 'no2']),
          ['o3', 'pm10', 'so2', 'co', 'no2'], ['pm25'], 1000, 20)

if __name__ == '__main__':
    o3.run_Morkov_by_plotly()
    # pm25_now.run_BP_by_plotly()
