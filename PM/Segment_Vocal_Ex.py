from scipy.io.wavfile import read
f = open("Test_Acapella/Acapella.txt",'r')
Acapella = f.read();Music = Acapella.replace("_acapella","");
Acapella1 = read("Test_Acapella/"+Acapella+".wav");Music1 = read("Test_Music/"+Music)
Acapella1 = numpy.array(a[0], dtype = float); Music1 = numpy.array(a[0], dtype = float)
for i in range(len(Music1)):
    if(Music1 == 0):
        continue
    else:
       Vocal_Percentage = (Acapella1/Music1)*100
       print(Vocal_Percentage)
        




