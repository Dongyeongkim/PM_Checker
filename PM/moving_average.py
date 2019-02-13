import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import pandas as pd

dataset = pd.read_csv('BrainWave/BrainWave.csv'); Time_Length = []

def MovingAverage(values, window) :
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def ExpMovingAverage(values, window) :
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()

    a = np.convolve(values, weights)[:len(values)]
    a[:window] = a[window]
    return a

def AverMovingAverage(value_1, value_2) :
    Aver_Graph = []
    if len(value_1) == len(value_2) :
        for aver_draw in range(len(value_1)) :
            Aver_Graph.append((value_1[aver_draw] + value_2[aver_draw]) / 2)
    return Aver_Graph

def Timeline(values) :
    a = []
    for make in range(len(values)) :
        a.append(make)

    return a

def aver(exp_mov, mov, window) :
    if len(exp_mov) == len(mov) + window - 1 :
        if window % 2 == 0 :
            for exp_mov_delete in range(int(window/2)) : exp_mov = np.delete(exp_mov, exp_mov_delete)
            for mov_insert in range(int(window/2) - 1) : mov = np.insert(mov, 0, mov[0])
        else :
            for exp_mov_delete in range(math.floor(window/2)): exp_mov = np.delete(exp_mov, exp_mov_delete)
            for mov_insert in range(math.ceil(window/2) - 1) : mov = np.insert(mov, 0, mov[0])
    else :
        sys.exit('error')
        return
    return exp_mov, mov

def bar_x_maker(values, arithmetic_val) :
    bins = []
    for i in range(len(values)) :
        if i % arithmetic_val  == 0 :
            bins.append(i)

    del bins[0]

    return bins

def bar_y_maker(values, arithmetic_val) :
    bins_y = []
    index = []

    for i in range(len(values)) :
        index.append(values[i])
        if i % arithmetic_val == 0 :
            bins_y.append(sum(index) / arithmetic_val)
            index = []

    del bins_y[0]

    return bins_y

def static_bar_x_maker(origin, values) :
    bins = []

    for i in range(len(values) - 1) :
        bins.append(sum(origin[values[i] : values[i + 1]]) / (origin[values[i + 1]] - origin[values[i]]))

    return bins

def static_bar_y_maker(values, bins) :
    bins_y = []

    for i in range(len(bins) - 1) :
        bins_y.append(sum(values[bins[i] : bins[i + 1]]) / (bins[i + 1] - bins[i]))

    return bins_y

def flatness(values) :
    prev = values[0]
    idx = []

    for i in range(len(values) - 1) :
        if abs(values[i + 1] - prev) > prev * 0.23 :
            idx.append(i)
            prev = values[i + 1]
        else :
            prev = (prev + values[i + 1]) / 2

    return idx


exp_moving_average_window = 20
moving_average_window = 20

exp_moving_average = ExpMovingAverage(dataset, exp_moving_average_window)
moving_average = MovingAverage(dataset, moving_average_window)

Time_Length = Timeline(dataset)
Moving_Time_Length = Timeline(moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k', label='meditation')
plt.plot(Time_Length, exp_moving_average, 'c', label='ExpMovingAver')
plt.plot(Moving_Time_Length, moving_average, 'r', label='MovingAver')
plt.legend(loc='upper right')
plt.show()

exp_moving_average, moving_average = aver(exp_moving_average, moving_average, exp_moving_average_window)
aver_Time_Length = Timeline(exp_moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k', label='meditation')
plt.plot(aver_Time_Length, exp_moving_average, 'c', label='ExpMovingAver')
plt.plot(aver_Time_Length, moving_average, 'r', label='MovingAver')
plt.legend(loc='upper right')
plt.show()

aver_graph = AverMovingAverage(exp_moving_average, moving_average)

plt.grid()
plt.plot(Time_Length, dataset, 'k', label='meditation')
plt.plot(aver_Time_Length, aver_graph, 'g', label='OptimalMovingAver')
plt.legend(loc='upper right')
plt.show()

arthical_val = 5

aver_bar_Time_Length = bar_x_maker(aver_graph, arthical_val)
aver_graph_bar = bar_y_maker(aver_graph, arthical_val)

plt.grid()
plt.plot(Time_Length, dataset, 'k', label='meditation')
plt.plot(aver_Time_Length, aver_graph, 'g', label='OptimalMovingAver')
plt.bar(aver_bar_Time_Length, aver_graph_bar, arthical_val, align='center', label='Sampling')
plt.legend(loc='upper right')
plt.show()

aver_bar_Time_Length_bak = aver_bar_Time_Length
aver_graph_bar_bak = aver_graph_bar


a = flatness(aver_graph_bar)
print(a, len(a))
print(aver_graph_bar)
print(aver_bar_Time_Length)
print('')

plt.grid()
plt.plot(aver_Time_Length, aver_graph, 'g', label='OptimalMovingAver')
plt.bar(aver_bar_Time_Length, aver_graph_bar_bak, arthical_val, align='center', label='Sampling')
for draw in range(len(a)):
    plt.axvline(aver_bar_Time_Length[a[draw]])
plt.axvline(aver_bar_Time_Length[a[0]], label='TurningPoint')
plt.legend(loc='upper right')
plt.show()

plt.grid()
plt.plot(Time_Length, dataset, 'k', label='meditation')
for draw in range(len(a)):
    plt.axvline(aver_bar_Time_Length[a[draw]])
plt.axvline(aver_bar_Time_Length[a[0]], label='TurningPoint')
plt.legend(loc='upper right')
plt.show()

with open('points.csv', 'w') as  W :
    W.write('points')
    W.write('\n')
    for save in range(len(a)) :
        W.write(str(aver_bar_Time_Length[a[save]]))
        W.write('\n')
    W.close()
