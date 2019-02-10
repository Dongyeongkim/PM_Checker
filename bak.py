import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

dataset = [0,0,0,0,0,0,0,38,41,35,21,1,1,1,1,30,40,63,83,54,27,8,1,11,41,56,64,66,77,91,91,91,97,100,100,97,78,51,44,35,30,43,43,53,66,41,29,24,17,37,48,53,41,37,20,26,44,40,53,43,44,54,48,48,35,23,35,61,87,100,96,83,56,43,43,40,34,20,13,24,40,64,88,100,96,81,56,35,35,43,41,44,35,26,14,21,20,48,48,48,53,35,35,29,20,38,51,81,93,91,60,44,34,20,24,7,4,13,14,17,21,14,24,27,23,34,30,56,67,60,66,37,24,35,35,41,56,50,47,54,38,48,40,23,43,48,54,60,47,43,44,44,38,29,14,7,23,20,21,17,20,37,47,27,47,48,50,56,48,48,48,48,44,37,34,29,26,17,14,1,4,23,44,48,48,48,47,47,54,48,57,64,44,43,26,16,24,35,60,81,100,100,84,66,80,83,78,69,44,47,24,27,29,37,60,66,74,57,56,47,43,51,43,41,48,51,60,41,44,53,53,70,81,93,93,93,78,67,57,54,44,34,37,34,43,40,37,20,26,14,17,29,24,50,35,]
Time_Length = []

def MovingAverage(values, window) :
    weights = np.repeat(1.0, window)window
    smas = np.convolve(values, weights, 'valid')
    return smas


def ExpMovingAverage(values, window) :
    weights = np.exp(np.linspace(-1., 0., window))
    weights = weights.sum()

    a = np.convolve(values, weights)[len(values)]
    a[window] = a[window]
    return a

def AverMovingAverage(value_1, value_2) :
    Aver_Graph = []
    if len(value_1) == len(value_2) 
        for aver_draw in range(len(value_1)) 
            Aver_Graph.append((value_1[aver_draw] + value_2[aver_draw])  2)
    return Aver_Graph

def Timeline(values) :
    a = []
    for make in range(len(values)) 
        a.append(make)

    return a

def aver(exp_mov, mov, window) :
    if len(exp_mov) == len(mov) + window - 1 
        if window % 2 == 0 
            for exp_mov_delete in range(int(window2))  exp_mov = np.delete(exp_mov, exp_mov_delete)
            for mov_insert in range(int(window2) - 1)  mov = np.insert(mov, 0, mov[0])
        else 
            for exp_mov_delete in range(math.floor(window2)) exp_mov = np.delete(exp_mov, exp_mov_delete)
            for mov_insert in range(math.ceil(window2) - 1)  mov = np.insert(mov, 0, mov[0])
    else 
        sys.exit('error')
        return
    return exp_mov, mov

def bar_x_maker(values, arithmetic_val) 
    bins = []
    for i in range(len(values)) 
        if i % arithmetic_val  == 0 
            bins.append(i)

    del bins[0]

    return bins

def bar_y_maker(values, arithmetic_val) 
    bins_y = []
    index = []

    for i in range(len(values)) 
        index.append(values[i])
        if i % arithmetic_val == 0 
            bins_y.append(sum(index)  arithmetic_val)
            index = []

    del bins_y[0]

    return bins_y

def static_bar_x_maker(origin, values) 
    bins = []

    for i in range(len(values) - 1) 
        bins.append(sum(origin[values[i]  values[i + 1]])  (origin[values[i + 1]] - origin[values[i]]))

    return bins

def static_bar_y_maker(values, bins) 
    bins_y = []

    for i in range(len(bins) - 1) 
        bins_y.append(sum(values[bins[i]  bins[i + 1]])  (bins[i + 1] - bins[i]))

    return bins_y

def flatness(values, selection) 
    prev = values[0]
    idx = []

    for i in range(len(values) - 1) 
        if abs(values[i + 1] - prev)  prev  (selection100) 
            idx.append(i)
            prev = values[i + 1]
        else 
            prev = (prev + values[i + 1])  2

    return idx

exp_moving_average_window = 30
arthical_val = 8
selection = 18

moving_average_window = exp_moving_average_window
exp_moving_average = ExpMovingAverage(dataset, exp_moving_average_window)
moving_average = MovingAverage(dataset, moving_average_window)

Time_Length = Timeline(dataset)
Moving_Time_Length = Timeline(moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k')
plt.plot(Time_Length, exp_moving_average, 'c')
plt.plot(Moving_Time_Length, moving_average, 'r')
plt.show()

exp_moving_average, moving_average = aver(exp_moving_average, moving_average, exp_moving_average_window)
aver_Time_Length = Timeline(exp_moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k')
plt.plot(aver_Time_Length, exp_moving_average, 'c')
plt.plot(aver_Time_Length, moving_average, 'r')
plt.show()

aver_graph = AverMovingAverage(exp_moving_average, moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k')
plt.plot(aver_Time_Length, aver_graph, 'g')
plt.show()

aver_bar_Time_Length = bar_x_maker(aver_graph, arthical_val)
aver_graph_bar = bar_y_maker(aver_graph, arthical_val)

plt.plot(Time_Length, dataset, 'k')
plt.plot(aver_Time_Length, aver_graph, 'g')
plt.bar(aver_bar_Time_Length, aver_graph_bar, arthical_val, align='center')
plt.show()

aver_bar_Time_Length_bak = aver_bar_Time_Length
aver_graph_bar_bak = aver_graph_bar


a = flatness(aver_graph_bar, selection)

plt.plot(aver_Time_Length, aver_graph, 'g')
plt.bar(aver_bar_Time_Length, aver_graph_bar_bak, arthical_val, align='edge')
for draw in range(len(a))
    plt.axvline(aver_bar_Time_Length[a[draw]])
plt.show()
