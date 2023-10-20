#stb -> service time begin
#ste -> service time end
#qt -> queue time
#wt wait time

import time
import pandas as pd
import numpy as np
from os import system, name
import matplotlib.pyplot as plt

def get_begin_service_time(a,b):
    tem = []
    tem.append(a[0])
    for i in range(1,len(a)):
        tem.append(max(a[i] , tem[-1]+b[i-1]))
    return tem
def get_end_service_time(a,b):
    tem = []
    for i in range(0,len(a)):
        tem.append(a[i]+b[i])
    return tem
def get_queue_time(a,b):
    tem = []
    for i in range(0,len(a)):
        tem.append(b[i] - a[i])
    return tem
def get_wait_time(a,b):
    tem = []
    for i in range(0,len(a)):
        tem.append(b[i] - a[i])
    return tem
n = int(input('Number of person: '))
arival_time = sorted(np.random.randint(1, 10, n))
service_time = np.random.randint(1, 10, n)
stb = get_begin_service_time(arival_time , service_time)
ste = get_end_service_time(stb , service_time)
qt = get_queue_time(arival_time , stb)
wt = get_wait_time(arival_time , ste)

def take(x):
    lst = [x,arival_time[x-1] , service_time[x-1] , stb[x-1] , ste[x-1] , qt[x-1]]
    return  lst
def make():
    p = []
    for i in range(1,n+1):
        p.append(take(i))
    return p
person = make()
df = pd.DataFrame(np.array(person),
                  columns=['Person','Arrival time' , 'Service Time' , 'Service Time Begin','Service time End','Queue Time'])
def get_arival(x):
    arived = []
    for i in range(0,n):
        # print(person[i][1] , x)
        if person[i][1]==x:
            arived.append(i+1)
    return arived

#main service
que = []
last_person_ste = 0
idol = 0
sf = []
info = [0,0,0,0,0]
running = 0
obs_time = []
q_length = []
def operation():
    global idol,last_person_ste,que,sf,running,info
    for i in range(0, ste[-1] + 1):
        obs_time.append(i+1)
        print('At Time: {}'.format(i))
        for j in get_arival(i):
            que.append(j)
        # print(last_person_ste , i,que,info)
        if last_person_ste > i:
            pass
        elif last_person_ste == i:
            if len(que) == 0:
                print("System is Idol")
                idol += 1
                que = que[1:]
                if info[0] > 0:
                    sf.append(info[0])
            else:
                if last_person_ste != 0:
                    if info[0]>0 :
                        sf.append(info[0])
                info = person[que[0] - 1]
                last_person_ste = info[4]
                running = info[0]
                que = que[1:]
        else:
            if len(que) == 0:
                print("System is Idol")
                idol += 1
                running = None
            else:
                info = person[que[0] - 1]
                last_person_ste = info[4]
                running = info[0]
                que = que[1:]

        # print('\x1b[6;30;42m'+f'Service running: {running}'+'\x1b[0m')
        print("Service Finished: ", sf)
        print("Waiting list:", que)
        time.sleep(0.5)
        # system('cls')
        q_length.append(len(que))
        print()


        # time.sleep(1)

operation()
print(df)
print("Avarage Sarvice Time: ",sum(service_time) / n)
print("Avarage Queue Time: ",sum(qt) / n)




#graph show...
plt.hist(wt)
plt.xlabel('Waiting time (min)')
plt.ylabel('Number of customers')
plt.show()

plt.step(np.array(obs_time) , np.array(q_length) ,where='post')
plt.xlabel('Time(min)')
plt.ylabel('Queue lenght')
plt.show()