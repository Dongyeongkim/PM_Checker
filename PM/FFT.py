import matplotlib.pyplot as plt
from matplotlib import animation,rc
import numpy as np; import wave
import sys;import math
import time


spf = wave.open('Test_Music/DNA.wav','r');signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16');Fs = spf.getframerate();
Time=np.linspace(0, len(signal)/Fs, num=len(signal))

def FrQ(signal):
       Time=np.linspace(0, len(signal)/Fs, num=len(signal))
       n=len(signal);NFFT=n;k=np.arange(NFFT);f0=k*Fs/NFFT
       f0=f0[range(math.trunc(NFFT/2))];return f0
       
def Amp(signal):
    Time=np.linspace(0, len(signal)/Fs, num=len(signal))
    n=len(signal);NFFT=n;k=np.arange(NFFT);
    f0=k*Fs/NFFT;f0=f0[range(math.trunc(NFFT/2))];
    Y=np.fft.fft(signal)/NFFT;Y=Y[range(math.trunc(NFFT/2))];
    amplitude_Hz = 2*abs(Y);return amplitude_Hz
    
def Pha(signal):
    Time=np.linspace(0, len(signal)/Fs, num=len(signal))
    n=len(signal);NFFT=n;k=np.arange(NFFT);
    f0=k*Fs/NFFT;f0=f0[range(math.trunc(NFFT/2))];
    Y=np.fft.fft(signal)/NFFT;Y=Y[range(math.trunc(NFFT/2))];
    phase_ang = np.angle(Y)*180/np.pi;return phase_ang



    
