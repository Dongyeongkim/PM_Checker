import librosa;import numpy as np

filename = "Test_Music/"+input("Input the File name")
y, sr = librosa.load(filename);onset_env = librosa.onset.onset_strength(y,sr=sr)
dtempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None)


tg = librosa.feature.tempogram(onset_envelope=onset_env,sr=sr)
import librosa.display;librosa.display.specshow(tg, x_axis='time',
                                                y_axis='tempo')

import matplotlib.pyplot as plt;plt.plot(librosa.frames_to_time(
    np.arange(len(dtempo))), dtempo,color='w', linewidth=1.5,
                                          label='Tempo estimate')
plt.title('Dynamic Tempo Estimation');plt.show()
