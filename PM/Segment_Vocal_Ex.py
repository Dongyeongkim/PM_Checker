from scipy.io.wavfile import read; import numpy
f = open("Test_Acapella/Acapella.txt",'r')
Acapella = f.read();Music = Acapella.replace("_acapella","");
Acapella1 = read("Test_Acapella/"+Acapella+".wav");Music1 = read("Test_Music/"+Music)
Acapella1 = numpy.array(Acapella1, dtype = int16); Music1 = numpy.array(Music1, dtype = int16)
for i in range(len(Music1)):
    if(Music1 == 0):
        continue
    else:
       Vocal_Percentage = (Acapella1/Music1)*100
       print(Vocal_Percentage+"%")
        




