import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts import Bar, Grid, Line
import pylab
from date_processing import *
import plotly
import plotly.graph_objs as go
import warnings

warnings.filterwarnings("ignore")

pylab.rcParams['figure.figsize'] = (15.0, 8.0)  # 显示大小


# from pylab import mpl
#
# mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class BP():
    def __init__(self, hidden_num, act_fun, train_time, data, feature_list, label_list, sample, test_set):
        '''

        :param hidden_num: 隐藏神经源的个数
        :param act_fun: 激励函数
        :param train_time: 训练次数
        :param data: 所有训练数据 = sample + test_set
        :param feature_list: 输入神经元的type_name
        :param label_list: 标签type_name
        :param sample: 训练集个数
        :param test_set: 测试集个数
        '''
        self.h = hidden_num
        self.act_fun = act_fun
        self.train_time = train_time
        self.data = data
        self.feature = feature_list
        self.label = label_list
        self.data_train = data.head(sample)
        self.data_test = data[sample:sample + test_set]
        self.x_train = self.data_train[self.feature].values  # 特征数据
        self.y_train = self.data_train[self.label].values  # 标签数据
        self.x_test = self.data_test[self.feature].values  # 特征数据
        self.y_test = self.data_test[self.label].values  # 标签数据
        self.time = data['timestamp'].head(sample).values[:, np.newaxis]
        self.time_pre = data['timestamp'][sample:sample + test_set].values[:, np.newaxis]
        self.test_loss = 0
        self.y_pre = 0
        self.y_test_pre = 0
        self.train_line = 0
        self.test_line = 0

    def run_BP_by_plt(self):
        # 建模
        model = Sequential()  # 层次模型
        model.add(Dense(len(self.feature),  # 此处为output_dim
                        input_dim=len(self.feature)))  # 输入层，Dense表示BP层
        model.add(Activation(self.act_fun))  # 添加激活函数
        model.add(Dense(1, input_dim=self.h))  # 输出层
        adam = Adam(lr=0.001)
        model.compile(loss='mean_squared_error',
                      optimizer=adam)  # 编译模型 交叉熵categorical_crossentropy 均方差mean_squared_error

        # 开始训练
        for step in range(self.train_time):
            cost = model.train_on_batch(self.x_train, self.y_train)
            if step % 2000 == 0: print("loss:", cost)

        # 测试
        self.test_loss = model.evaluate(self.x_test, self.y_test)
        self.y_pre = model.predict(self.x_train)
        self.y_test_pre = model.predict(self.x_test)
        print("test_loss:", self.test_loss)

        # matplotlib展示
        plt.plot(self.time, self.y_train)
        plt.plot(self.time, self.y_pre, '-r')
        plt.title('Result of Sample')
        plt.xlabel('Time')
        plt.ylabel(self.label[0])
        plt.show()
        plt.plot(self.time_pre, self.y_test)
        plt.plot(self.time_pre, self.y_test_pre, 'r-')
        plt.title('Result of Test')
        plt.xlabel('Time')
        plt.ylabel(self.label[0])
        plt.show()

    def run_BP_by_echart(self):
        # 建模
        model = Sequential()  # 层次模型
        model.add(Dense(len(self.feature),  # 此处为output_dim
                        input_dim=len(self.feature)))  # 输入层，Dense表示BP层
        model.add(Activation(self.act_fun))  # 添加激活函数
        model.add(Dense(1, input_dim=self.h))  # 输出层
        adam = Adam(lr=0.001)
        model.compile(loss='mean_squared_error',
                      optimizer=adam)  # 编译模型 交叉熵categorical_crossentropy 均方差mean_squared_error

        # 开始训练
        for step in range(self.train_time):
            cost = model.train_on_batch(self.x_train, self.y_train)
            if step % 2000 == 0: print("loss:", cost)

        # 测试
        self.test_loss = model.evaluate(self.x_test, self.y_test)
        self.y_pre = model.predict(self.x_train)
        self.y_test_pre = model.predict(self.x_test)
        print("test_loss:", self.test_loss)

        # echart

        self.train_line = Line(self.label[0] + '训练集拟合效果图')
        self.train_line.add('真实数值', to_reallist(self.time), tolist_to_reallist(self.y_train), mark_point=["max", "min"],
                            mark_line=["average"])
        self.train_line.add('拟合数值', to_reallist(self.time), tolist_to_reallist(self.y_pre))
        self.train_line.render('output/train_line.html')

        self.test_line = Line(self.label[0] + '测试集拟合效果图')
        self.test_line.add('真实数值', to_reallist(self.time_pre), tolist_to_reallist(self.y_test), mark_point=["max", "min"],
                           mark_line=["average"])
        self.test_line.add('预测数值', to_reallist(self.time_pre), tolist_to_reallist(self.y_test_pre))
        self.test_line.render('output/test_line.html')
        print(self.time)

    def run_BP_by_plotly(self):
        # 建模
        model = Sequential()  # 层次模型
        model.add(Dense(len(self.feature),  # 此处为output_dim
                        input_dim=len(self.feature)))  # 输入层，Dense表示BP层
        model.add(Activation(self.act_fun))  # 添加激活函数
        model.add(Dense(1, input_dim=self.h))  # 输出层
        adam = Adam(lr=0.001)
        model.compile(loss='mean_squared_error',
                      optimizer=adam)  # 编译模型 交叉熵categorical_crossentropy 均方差mean_squared_error

        # 开始训练
        for step in range(self.train_time):
            cost = model.train_on_batch(self.x_train, self.y_train)
            if step % 2000 == 0: print("loss:", cost)

        # 测试
        self.test_loss = model.evaluate(self.x_test, self.y_test)
        self.y_pre = model.predict(self.x_train)
        self.y_test_pre = model.predict(self.x_test)
        print("test_loss:", self.test_loss)

        # plotly

        trace0 = go.Scatter(x=to_reallist(self.time), y=tolist_to_reallist(self.y_train), mode='lines+markers',
                            name='真实数值')
        trace1 = go.Scatter(x=to_reallist(self.time), y=tolist_to_reallist(self.y_pre), mode='lines+markers',
                            name='拟合数值')
        data1 = [trace0, trace1]
        plotly.offline.plot(data1, filename='output/train_line.html')

        trace2 = go.Scatter(x=to_reallist(self.time_pre), y=tolist_to_reallist(self.y_test), mode='lines+markers',
                            name='真实数值')
        trace3 = go.Scatter(x=to_reallist(self.time_pre), y=tolist_to_reallist(self.y_test_pre), mode='lines+markers',
                            name='预测数值')
        data2 = [trace2, trace3]
        plotly.offline.plot(data2, filename='output/test_line.html')
