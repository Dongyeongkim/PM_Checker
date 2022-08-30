import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.io.wavfile as wav
import scipy.fftpack
import scipy

fig = plt.figure()

def fft_freq(aud_data, rate, start_dur, end_dur) :
    
    aud_data = np.array(aud_data)
    if rate / CHUNK == 0 :
        magnification = rate / CHUNK
    else :
        magnification = round(rate / CHUNK, 1)
    
    N = len(aud_data[start_dur : start_dur + CHUNK])

    aver_x_stack = []
    aver_stack = []
    
    if (end_dur - start_dur) % CHUNK != 0 :
        for draw in range(int((end_dur - start_dur) / CHUNK) + 1) :
            
            fourier = np.fft.fft(aud_data[start_dur : start_dur + CHUNK])
            freqs = scipy.fftpack.fftfreq(N, t[1] - t[0])
            
            start_dur = start_dur + CHUNK
            if start_dur > end_dur :
                N = len(aud_data[start_dur - CHUNK : end_dur])
                fourier = np.fft.fft(aud_data[start_dur - CHUNK : end_dur])
                freqs = scipy.fftpack.fftfreq(N, t[1] - t[0])

            freqs = abs(freqs[0: int(len(freqs) / 2)])
            fourier = abs(fourier[0: int(len(fourier) / 2)])

            arithmetic_val = 100
                
            aver_x = bar_x_maker(freqs, arithmetic_val)
            aver_y = bar_y_maker(fourier, arithmetic_val, aver_x)
            del aver_x[-1]

            aver_x_stack.append(aver_x)
            aver_stack.append(aver_y)
            
            for i in range(len(aver_x)) :
                aver_x[i] = aver_x[i] * magnification
            
        return aver_x_stack, aver_stack

    else :
        for draw in range(int((end_dur - start_dur) / CHUNK)) :
            fourier = np.fft.fft(aud_data[start_dur : start_dur + CHUNK])
            freqs = scipy.fftpack.fftfreq(N, t[1] - t[0])
            start_dur = start_dur + CHUNK

            freqs = abs(freqs[0: int(len(freqs) / 2)])
            fourier = abs(fourier[0: int(len(fourier) / 2)])

            aver_x_stack.append(freqs)
            aver_stack.append(fourier)
            
        return aver_x_stack, aver_stack, magnification

def bar_x_maker(values, arithmetic_val) :
    bins_x = [values[0]]
    
    for i in range(len(values)) :
        if (i + 1) % arithmetic_val == 0 :
                bins_x.append(i + 1)
    
    return bins_x

def bar_y_maker(values, arithmetic_val, x_val) :
    bins_y = []
    index = []

    for i in range(len(x_val) - 1) :
        bins_y.append(sum(values[int(x_val[i]) : int(x_val[i+1])]) / arithmetic_val)
    
    return bins_y
    
CHUNK = 1
arithmetic_val = 1

rate, aud_data = wav.read('havana.wav')
aver_frequency = []
aver_std = []

start_dur = 0
end_dur = 100

#N = len(aud_data)
#secs = N / float(rate)
#Ts = 1.0 / rate
#t = scipy.arange(0, secs, Ts)

segment_x, segment_y, magnification = fft_freq(aud_data, rate, (start_dur * rate), (end_dur * rate))

segment_x = np.array(segment_x)
segment_y = np.array(segment_y)

print(segment_y)
for make_frequency in range(len(segment_y[0])) :
    aver_frequency.append(sum(segment_y[:, make_frequency]) / len(segment_y))
    aver_std.append(np.std(segment_y[:, make_frequency]))

aver_x = bar_x_maker(segment_x[0], arithmetic_val)
aver_y = bar_y_maker(aver_frequency, arithmetic_val, aver_x)
del aver_x[-1]

for i in range(len(aver_x)) :
    aver_x[i] = aver_x[i] * magnification
            
plt.plot(segment_x[0], aver_frequency)
plt.show()

plt.bar(aver_x, aver_y, (arithmetic_val - 30) * magnification, align='edge')
plt.show()
