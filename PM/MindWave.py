from NeuroPy import NeuroPy
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
    
neuropy = NeuroPy("COM3") # Specify COM Port
neuropy.start()
    
fig = plt.figure()
t = 0

meditation = []

x_time = []

print("=============================")

def animate(i):
    global t
    global meditation
    
    if t == 300: # preset: 300(sec)
        
        con = raw_input("Continue (Y/N)? ")
        
        if con == 'N':
            with open('BrainWave/BrainWave.csv', 'w') as w:
                meditation = str(meditation);meditation = meditation.split()
                for i in range(len(meditation)):
                    w.write(meditation[i]+'\n')
                w.close()
                print 'The previous data is saved.'

            neuropy.stop()
            return 0
        
        elif con == 'Y':
            t = 0
            
    print 'meditation: {}'.format(neuropy.meditation)
    print ''
    print 'RawValue: {}'.format(neuropy.rawValue)
    print 'PoorSignal: {}'.format(neuropy.poorSignal)
    
    print("=============================")

    x_time.append(i)

    meditation.append(neuropy.meditation)

    plt.ylabel('Med.')
    plt.xlabel('Time')

    plt.plot(x_time, meditation, 'm')
    plt.axis([i - 30, i, 0, max(meditation)])

    t += 1

while True:
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    
    if ani == 0:
        print 'exit'
        break
