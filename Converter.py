f = open('Data/meditation_2.csv','r')
Raw_Data = f.read();print(Raw_Data);
Data = Raw_Data.split(','); f.close()
for i in range(len(Data)):
    f = open('Data/Data2.csv','a')
    f.write(Data[i]+'\n')
    f.close
    
