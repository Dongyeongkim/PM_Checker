import matplotlib.pyplot as plt
import numpy as np; import wave
import sys;import math;import librosa

class B_Music_Elements():

       def __init__(self):
              self.Music_Name = input("Please input the Music Name without the extensions");
              spf = wave.open('Test_Music/'+self.Music_Name+'.wav','r');signal = spf.readframes(-1)
              self.signal = np.fromstring(signal, 'Int16');self.Fs = spf.getframerate();
       def Tempo(self):
              Time=np.linspace(0, len(self.signal)/self.Fs, num=len(self.signal))
              y, sr = librosa.load("Test_Music/"+self.Music_Name+'.wav')
              tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
              return tempo
       def FrQ(self):
              Time=np.linspace(0, len(self.signal)/self.Fs, num=len(self.signal))
              n=len(self.signal);NFFT=n;k=np.arange(NFFT);f0=k*self.Fs/NFFT
              f0=f0[range(math.trunc(NFFT/2))];return f0
       def Amp(self):
              Time=np.linspace(0, len(self.signal)/self.Fs, num=len(self.signal))
              n=len(self.signal);NFFT=n;k=np.arange(NFFT);
              f0=k*self.Fs/NFFT;f0=f0[range(math.trunc(NFFT/2))];
              Y=np.fft.fft(self.signal)/NFFT;Y=Y[range(math.trunc(NFFT/2))];
              amplitude_Hz = 2*abs(Y);return amplitude_Hz
       def Pha(signal):
              Time=np.linspace(0, len(self.signal)/Fs, num=len(self.signal))
              n=len(self.signal);NFFT=n;k=np.arange(NFFT);
              f0=k*Fs/NFFT;f0=f0[range(math.trunc(NFFT/2))];
              Y=np.fft.fft(self.signal)/NFFT;Y=Y[range(math.trunc(NFFT/2))];
              phase_ang = np.angle(Y)*180/np.pi;return phase_ang




    
