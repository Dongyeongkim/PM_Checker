import librosa;import sys;import matplotlib.pyplot as plt

try:
    filename = input("Input your File Name")
    y, sr = librosa.load("Test_Music/"+filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y,sr=sr)
    print('{:.2f}BPM'.format(tempo))
    beat_times = librosa.frames_to_time(beat_frames, sr=sr);
    print(beat_times);plt.plot(beat_times);
    plt.axhline(y=tempo, color='r', linewidth=1);plt.show()

except FileNotFoundError:
    print("File is not Founded, please type correctly")
    sys.exit(0)
    
