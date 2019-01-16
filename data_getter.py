import pandas as pd
import numpy as np
from date_processing import *
from database_model import *
import time


def get_data_one_dict(date_dict, type_name):
    '''
    得到某一天某一种类的数据
    :param date_dict: 包含日期的字典
    '''
    data = Air.select().where(Air.year == date_dict['year'], Air.month == date_dict['month'],
                              Air.day == date_dict['day'])[0]
    if type_name == 'pm25':
        return data.pm25
    elif type_name == 'aqi':
        return data.aqi
    elif type_name == 'rank':
        return data.rank
    elif type_name == 'pm10':
        return data.pm10
    elif type_name == 'so2':
        return data.so2
    elif type_name == 'co':
        return data.co
    elif type_name == 'o3':
        return data.o3
    elif type_name == 'date':
        return data.date
    elif type_name == 'no2':
        return data.no2


def get_data_one_str(text, type_name):
    return get_data_one_dict(date_str_to_dict(text), type_name)


def get_by_time_delta(date_text, time_dalta, type_name):
    date_all = []
    for i in range(time_dalta):
        try:
            one_data = {}
            one_data['date'] = get_data_one_str(get_after_str(date_text, i), 'date')
            one_data[type_name] = get_data_one_str(get_after_str(date_text, i), type_name)
            one_data['timestamp'] = int(time.mktime(time.strptime(one_data['date'], '%Y-%m-%d')))
            date_all.append(one_data)
        except:
            continue
    pd_data = pd.DataFrame(date_all)
    return pd_data


def get_by_time_delta_list(date_text, time_dalta, type_name_list, type_befor_list):
    date_all = []
    for i in range(time_dalta):
        try:
            one_data = {}
            one_data['date'] = get_data_one_str(get_after_str(date_text, i), 'date')
            for j in type_name_list:
                one_data[j] = get_data_one_str(get_after_str(date_text, i), j)
            for k in type_befor_list:
                type_dict = type_before(k)
                one_data[k] = get_data_one_str(get_after_str(date_text, i - 1), type_dict[0])
            one_data['timestamp'] = int(time.mktime(time.strptime(one_data['date'], '%Y-%m-%d')))
            date_all.append(one_data)
        except:
            continue
    pd_data = pd.DataFrame(date_all)
    return pd_data


def type_before(text):
    texts = text.split('_')
    return texts


if __name__ == '__main__':
    print(get_by_time_delta_list('2014-1-1', 1000, ['pm25', 'o3', 'no2'], ['pm25_1','o3_1']))
