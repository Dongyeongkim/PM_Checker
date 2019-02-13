from analyzer_formula import *
import pandas as pd

dataset = pd.read_csv('BrainWave\BrainWave.csv'); Time_Length = []
dataset = dataset.values; dataset = dataset.ravel();print(dataset)
exp_moving_average_window = 20 # preset: 20
moving_average_window = 20 # preset: 20

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

arthical_val = 5 # preset: 5

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
