from scipy.io.wavfile import read
f = open("Test_Acapella/Acapella.txt",'r')
Acapella = f.read();Acapella1 = read("Test_Acapella/"+Acapella+".wav")
Acapella1 = numpy.array(a[0], dtype = float)
for i in range(len(Acapella)):
    if(Acapella[i] ==0):
        f = open("Test_Acapella/"+Acapella+".txt",'a')
        f.close()
    else:
        continue



