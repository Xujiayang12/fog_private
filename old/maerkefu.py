import pandas as pd
import numpy as np
from prettytable import PrettyTable as PT

#################参数设置###############
type = 'o3'
feed = 15

########################################


air = pd.read_csv('fog.csv').head(feed)
data = air[type]
average = data.mean()
std = data.std()
std_square = data.var()
print('平均值为：' + str(average) + ' ，标准差为：' + str(std) + ' ，方差为：' + str(std_square) + "\n")

E1 = 'E1:( -∞ , ' + str(average - 1.0 * std) + " )"
E2 = 'E2:( ' + str(average - 1.0 * std) + ' , ' + str(average - 0.5 * std) + " )"
E3 = 'E3:( ' + str(average - 0.5 * std) + ' , ' + str(average + 0.5 * std) + " )"
E4 = 'E4:( ' + str(average + 0.5 * std) + ' , ' + str(average + 1.0 * std) + " )"
E5 = 'E5:( ' + str(average + 1.0 * std) + ' , ' + "+∞" + " )"

E_list = [E1, E2, E3, E4, E5]

print('E1:( -∞ , ' + str(average - 1.0 * std) + " )")
print('E2:( ' + str(average - 1.0 * std) + ' , ' + str(average - 0.5 * std) + " )")
print('E3:( ' + str(average - 0.5 * std) + ' , ' + str(average + 0.5 * std) + " )")
print('E4:( ' + str(average + 0.5 * std) + ' , ' + str(average + 1.0 * std) + " )")
print('E5:( ' + str(average + 1.0 * std) + ' , ' + "+∞" + " )\n")

##############################算概率矩阵部分#############################

d1 = average - 1.0 * std
d2 = average - 0.5 * std
d3 = average + 0.5 * std
d4 = average + 1.0 * std

state_list = []
for index, row in air.iterrows():  # 划分转态转化成列表
    i = row[type]
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
p_M2 = p_M.dot(p_M)
p_M3 = p_M2.dot(p_M)
p_M4 = p_M3.dot(p_M)
p_M5 = p_M4.dot(p_M)
p_M_list = [p_M, p_M2, p_M3, p_M4, p_M5]
print("p_M1:")
print(p_M)
print("\n")
####################################################################

##############################算自相关系数部分######################

list_data = []
for index, row in air.iterrows():
    list_data.append(row[type])

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
# print(w1, w2, w3, w4, w5)
print("\n")

##########################################################


##########################################################
last_5_low = air.tail(5)
state_list.reverse()
slist_5 = state_list[0:5]
slist_5.reverse()
state_list.reverse()


# print(state_list)
# print(slist_5)

def get_p(s_in_sl_5, s2):
    s1 = slist_5[s_in_sl_5]
    pm = 5 - s_in_sl_5
    pM = p_M_list[pm - 1]
    P = pM[s1 - 1][s2 - 1]
    return P


table = PT(["初始日期", "初始状态", "滞时", "权重", "状态1", "状态2", "状态3", "状态4", "状态5", "对应的概率矩阵"])
table.add_row(
    [last_5_low.iloc[4,]['date'], slist_5[4], 1, w1, get_p(4, 1), get_p(4, 2), get_p(4, 3), get_p(4, 4), get_p(4, 5),
     "P1"])
table.add_row(
    [last_5_low.iloc[3,]['date'], slist_5[3], 2, w2, get_p(3, 1), get_p(3, 2), get_p(3, 3), get_p(3, 4), get_p(3, 5),
     "P2"])
table.add_row(
    [last_5_low.iloc[2,]['date'], slist_5[2], 3, w3, get_p(2, 1), get_p(2, 2), get_p(2, 3), get_p(2, 4), get_p(2, 5),
     "P3"])
table.add_row(
    [last_5_low.iloc[1,]['date'], slist_5[1], 4, w4, get_p(1, 1), get_p(1, 2), get_p(1, 3), get_p(1, 4), get_p(1, 5),
     "P4"])
table.add_row(
    [last_5_low.iloc[0,]['date'], slist_5[0], 5, w5, get_p(0, 1), get_p(0, 2), get_p(0, 3), get_p(0, 4), get_p(0, 5),
     "P5"])
# table.add_row([last_5_low[]])
print(table)


# print(last_5_low)
# print(last_5_low.iloc[4,])

def get_pre_p(state_code):
    P = w1 * get_p(4, state_code) + w2 * get_p(3, state_code) + w3 * get_p(2, state_code) + w4 * get_p(1,
                                                                                                       state_code) + w5 * get_p(
        0, state_code)
    return P


p_table = PT(["p1", "p2", "p3", "p4", "p5"])
p_pre_list = [get_pre_p(1), get_pre_p(2), get_pre_p(3), get_pre_p(4), get_pre_p(5)]
p_table.add_row(p_pre_list)
print(p_table)
p_max_index = p_pre_list.index(max(p_pre_list))
print("\n" + "预测后一天的状态为" + E_list[p_max_index])
air_all = pd.read_csv('fog.csv')
p_date = last_5_low.iloc[4,]['date']
real_data_index = int(air_all[air_all['date'].isin([p_date])].index.values)
real_data = air_all.iloc[real_data_index + 1,][type]
print("而真实值为" + str(real_data))
