import datetime
import time
import pandas as pd
import numpy as np
from scipy import stats
import math
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


# ------------------------------------------- M o r k o v ----------------------------------------

def get_std_and_var(pd_data, type_name):
    data = pd_data[type_name]
    out = {}
    out['average'] = data.mean()
    out['std'] = data.std()
    out['std_square'] = data.var()
    out['len'] = len(data)

    return out


def morkov_get_status_list(out_data):
    average = out_data['average']
    std = out_data['std']
    len = out_data['len']

    # d1 = average - 1.0 * std
    # d2 = average - 0.5 * std
    # d3 = average + 0.5 * std
    # d4 = average + 1.0 * std
    t_25 = stats.t.interval(0.025, len - 1, average, std)
    a = (t_25[0] + t_25[1])/2
    d1 = average - 2*a
    d2 = t_25[0]
    d3 = t_25[1]
    d4 = average + 2*a
    d_list = [d1, d2, d3, d4]
    return d_list


def morkov_get_state_list(pd_data, type_name, d_list):
    state_list = []
    d1 = d_list[0]
    d2 = d_list[1]
    d3 = d_list[2]
    d4 = d_list[3]
    for index, row in pd_data.iterrows():  # 划分转态转化成列表
        i = row[type_name]
        if i < d1:
            state_list.append(1)
        elif i >= d1 and i < d2:
            state_list.append(2)
        elif i >= d2 and i < d3:
            state_list.append(3)
        elif i >= d3 and i < d4:
            state_list.append(4)
        elif i >= d4:
            state_list.append(5)
    return state_list


def morkov_get_transfer_matrix(state_list):
    e11 = 0
    e12 = 0
    e13 = 0
    e14 = 0
    e15 = 0
    e21 = 0
    e22 = 0
    e23 = 0
    e24 = 0
    e25 = 0
    e31 = 0
    e32 = 0
    e33 = 0
    e34 = 0
    e35 = 0
    e41 = 0
    e42 = 0
    e43 = 0
    e44 = 0
    e45 = 0
    e51 = 0
    e52 = 0
    e53 = 0
    e54 = 0
    e55 = 0

    for i in range(len(state_list) - 1):  # 记录各个状态转移的数量
        if state_list[i] == 1:
            if state_list[i + 1] == 1:
                e11 += 1
            elif state_list[i + 1] == 2:
                e12 += 1
            elif state_list[i + 1] == 3:
                e13 += 1
            elif state_list[i + 1] == 4:
                e14 += 1
            elif state_list[i + 1] == 5:
                e15 += 1
        if state_list[i] == 2:
            if state_list[i + 1] == 1:
                e21 += 1
            elif state_list[i + 1] == 2:
                e22 += 1
            elif state_list[i + 1] == 3:
                e23 += 1
            elif state_list[i + 1] == 4:
                e24 += 1
            elif state_list[i + 1] == 5:
                e25 += 1
        if state_list[i] == 3:
            if state_list[i + 1] == 1:
                e31 += 1
            elif state_list[i + 1] == 2:
                e32 += 1
            elif state_list[i + 1] == 3:
                e33 += 1
            elif state_list[i + 1] == 4:
                e34 += 1
            elif state_list[i + 1] == 5:
                e35 += 1
        if state_list[i] == 4:
            if state_list[i + 1] == 1:
                e41 += 1
            elif state_list[i + 1] == 2:
                e42 += 1
            elif state_list[i + 1] == 3:
                e43 += 1
            elif state_list[i + 1] == 4:
                e44 += 1
            elif state_list[i + 1] == 5:
                e45 += 1
        if state_list[i] == 5:
            if state_list[i + 1] == 1:
                e51 += 1
            elif state_list[i + 1] == 2:
                e52 += 1
            elif state_list[i + 1] == 3:
                e53 += 1
            elif state_list[i + 1] == 4:
                e54 += 1
            elif state_list[i + 1] == 5:
                e55 += 1

    e1_all = e11 + e12 + e13 + e14 + e15
    e2_all = e21 + e22 + e23 + e24 + e25
    e3_all = e31 + e32 + e33 + e34 + e35
    e4_all = e41 + e42 + e43 + e44 + e45
    e5_all = e51 + e52 + e53 + e54 + e55

    if e1_all == 0: e1_all = 0.1
    if e2_all == 0: e2_all = 0.1
    if e3_all == 0: e3_all = 0.1
    if e4_all == 0: e4_all = 0.1
    if e5_all == 0: e5_all = 0.1

    p_M = np.array([[e11 / e1_all, e12 / e1_all, e13 / e1_all, e14 / e1_all, e15 / e1_all],
                    [e21 / e2_all, e22 / e2_all, e23 / e2_all, e24 / e2_all, e25 / e2_all],
                    [e31 / e3_all, e32 / e3_all, e33 / e3_all, e34 / e3_all, e35 / e3_all],
                    [e41 / e4_all, e42 / e4_all, e43 / e4_all, e44 / e4_all, e45 / e4_all],
                    [e51 / e5_all, e52 / e5_all, e53 / e5_all, e54 / e5_all, e55 / e5_all]])

    return p_M


def morkov_get_matrix_n(p_M, day):
    p_Mn = p_M
    if day == 1:
        return p_M
    elif day >= 2:
        for i in range(day - 1):
            p_Mn = p_Mn.dot(p_M)
        return p_Mn


def morkov_get_w_list(pd_data, type_name, std_dict):
    average = std_dict['average']
    list_data = []
    for index, row in pd_data.iterrows():
        list_data.append(row[type_name])

    x3 = 0
    for i in list_data:
        x3 += (i - average) * (i - average)

    def zixiangguan(n):
        r = 0
        for i in range(len(list_data) - 1 - n):
            x1 = list_data[i] - average
            x2 = list_data[i + n] - average
            y = x1 * x2 / x3
            r += y
        return r

    r1 = zixiangguan(1)
    r2 = zixiangguan(2)
    r3 = zixiangguan(3)
    r4 = zixiangguan(4)
    r5 = zixiangguan(5)
    # print(r1, r2, r3, r4, r5)

    # 规范化
    rk_all = abs(r1) + abs(r2) + abs(r3) + abs(r4) + abs(r5)
    w1 = abs(r1) / rk_all
    w2 = abs(r2) / rk_all
    w3 = abs(r3) / rk_all
    w4 = abs(r4) / rk_all
    w5 = abs(r5) / rk_all
    w_list = [w1, w2, w3, w4, w5]

    return w_list


def morkov_final(w_list, state_list, p_M, d_list):
    w1 = w_list[0]
    w2 = w_list[1]
    w3 = w_list[2]
    w4 = w_list[3]
    w5 = w_list[4]

    state_list.reverse()
    slist_5 = state_list[0:5]
    slist_5.reverse()
    state_list.reverse()

    p_M_list = [morkov_get_matrix_n(p_M, 1), morkov_get_matrix_n(p_M, 2), morkov_get_matrix_n(p_M, 3),
                morkov_get_matrix_n(p_M, 4), morkov_get_matrix_n(p_M, 5)]

    def get_p(s_in_sl_5, s2):
        s1 = slist_5[s_in_sl_5]
        pm = 5 - s_in_sl_5
        pM = p_M_list[pm - 1]
        P = pM[s1 - 1][s2 - 1]
        return P

    def get_pre_p(state_code):
        P = w1 * get_p(4, state_code) + w2 * get_p(3, state_code) + w3 * get_p(2, state_code) + w4 * get_p(1,
                                                                                                           state_code) + w5 * get_p(
            0, state_code)
        return P

    p_pre_list = [get_pre_p(1), get_pre_p(2), get_pre_p(3), get_pre_p(4), get_pre_p(5)]
    p_max_index = p_pre_list.index(max(p_pre_list))
    d1 = d_list[0]
    d2 = d_list[1]
    d3 = d_list[2]
    d4 = d_list[3]
    E_list = [[0, d1], [d1, d2], [d2, d3], [d3, d4], [d4, 400]]  # 表示无穷大无无穷小尚待解决
    print("\n" + "预测后一天的状态为" + str(E_list[p_max_index]))
    return E_list[p_max_index]


# -------------------------------------K - Means ----------------------------
def get_error_list(reallist, prelist):
    real_list = pd.DataFrame(reallist)
    pre_list = pd.DataFrame(prelist)
    error_list = (pre_list - real_list) / pre_list
    return error_list[0].tolist()


if __name__ == '__main__':
 pass