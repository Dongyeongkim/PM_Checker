from NeuroPy import NeuroPy
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
    
neuropy = NeuroPy("COM3")
neuropy.start()
    
fig = plt.figure()
t = 0

meditation = []

x_time = []

print("=============================")

def animate(i) :
    global t
    
    if t ==  300:
        
        more = raw_input("more or save ? (M : more, S : save) : ")
        
        if more == 'S' :
            with open('waves.txt', 'w') as w :
                w.write('[meditation] \n')
                w.write(str(meditation))
                w.write('\n')

                w.close()

            neuropy.stop()
            return 0
        
        elif more == 'M' :
            t = 0
            return 1
            
    print("meditation: ", neuropy.meditation)
    print("")
    print("RawValue: " , neuropy.rawValue)
    print("PoorSignal: " , neuropy.poorSignal)
    
    print("=============================")

    x_time.append(i)

    meditation.append(neuropy.meditation)

    plt.ylabel('Med.')
    plt.xlabel('Time')

    plt.plot(x_time, meditation, 'm')
    plt.axis([i - 30, i, 0, max(meditation)])

    t += 1

while True :
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    
    if ani == 0 :
        print('exit')
        break


