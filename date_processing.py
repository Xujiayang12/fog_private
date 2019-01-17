import datetime
import time
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def date_str_to_dict(text):
    texts = text.split('-')
    out = {}
    out['year'] = texts[0]
    out['month'] = texts[1]
    out['day'] = texts[2]
    return out


def get_before(year, month, day, num):
    '''
    推算这一天前几天的日期
    '''
    now = datetime.datetime.strptime(str(year) + '-' + str(month) + '-' + str(day), '%Y-%m-%d')
    delta = datetime.timedelta(days=num)
    before = now - delta
    out = str(before).replace(' 00:00:00', '')
    return out


def get_before_dict(date_dict, num):
    now = datetime.datetime.strptime(
        str(date_dict['year']) + '-' + str(date_dict['month']) + '-' + str(date_dict['day']), '%Y-%m-%d')
    delta = datetime.timedelta(days=num)
    before = now - delta
    out = str(before).replace(' 00:00:00', '')
    return out


def get_before_str(text, num):
    return get_before_dict(date_str_to_dict(text), num)


def get_after(year, month, day, num):
    '''
    推算这一天后几天的日期
    '''
    now = datetime.datetime.strptime(str(year) + '-' + str(month) + '-' + str(day), '%Y-%m-%d')
    delta = datetime.timedelta(days=num)
    after = now + delta
    out = str(after).replace(' 00:00:00', '')
    return out


def get_after_dict(date_dict, num):
    now = datetime.datetime.strptime(
        str(date_dict['year']) + '-' + str(date_dict['month']) + '-' + str(date_dict['day']), '%Y-%m-%d')
    delta = datetime.timedelta(days=num)
    after = now + delta
    out = str(after).replace(' 00:00:00', '')
    return out


def get_after_str(text, num):
    return get_after_dict(date_str_to_dict(text), num)


def tolist_to_reallist(a_list):
    out_list = []
    for i in a_list.tolist():
        out_list.append(i[0])
    return out_list

def to_reallist(a_list):
    out_list = []
    for i in a_list:
        out_list.append(i[0])
    return out_list


if __name__ == '__main__':
    print(get_after(2017, 1, 1, 3))
