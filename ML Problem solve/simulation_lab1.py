import threading
import time
import pandas as pd
import numpy as np
from os import system
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

def get_list_of_arival(n):
    numbers = np.random.randint(0, 10, n)
    numbers = sorted(numbers)
    return list(numbers)
def get_list_of_service(n):
    numbers =  np.random.randint(1, 10, n)
    return list(numbers)

n = int(input('Number of Person: '))
arival_time = get_list_of_arival(n)
service_time = get_list_of_service(n)
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
def showw():
    print('\x1b[6;30;44m' + f"\t\t\t\tArival Time: {arival_time}" + '\x1b[0m')
    print('\x1b[6;30;44m' + f"\t\t\t\tService Time: {service_time}" + '\x1b[0m')

que = []
last_person_ste = 0
idol = 0
sf = []
info = [0,0,0,0,0]
running = 0
obs_time = []
q_length = []
start = '$'

def operation(st):
    global idol,last_person_ste,que,sf,running,info,start
    for i in range(0, ste[-1] + 1):
        obs_time.append(i+1)
        showw()
        if start == '$':
            start = input('Press 1 for start: ')
        print('\t\t\t\tAt Time: {}'.format(i))
        for j in get_arival(i):
            que.append(j)
        # print(last_person_ste , i,que,info)
        if last_person_ste > i:
            pass
        elif last_person_ste == i:
            if len(que) == 0:
                print('\x1b[6;30;42m' + '\t\t\t\tSystem is Idol' + '\x1b[0m')
                idol += 1
                que = que[1:]
                if info[0] > 0:
                    sf.append(info[0])
            else:
                if last_person_ste != 0:
                    if info[0]>0:
                        sf.append(info[0])
                info = person[que[0] - 1]
                last_person_ste = info[4]
                running = info[0]
                que = que[1:]
        else:
            if len(que) == 0:
                print('\x1b[6;30;42m' + '\t\t\t\tSystem is Idol' + '\x1b[0m')
                idol += 1
                running = None
            else:
                info = person[que[0] - 1]
                last_person_ste = info[4]
                running = info[0]
                que = que[1:]
        print('\x1b[6;30;42m'+f'\t\t\t\tService running: '+'\x1b[0m',running)
        print('\x1b[6;30;42m'+"\t\t\t\tService in Queue:"+'\x1b[0m', que)
        print('\x1b[6;30;42m' + "\t\t\t\tService Finished: " + '\x1b[0m', sf)
        time.sleep(st)
        if i != ste[-1]:
            system('cls')
        q_length.append(len(que))
        print()

def plot_his1():
    plt.hist(wt)
    plt.xlabel('Waiting time (min)')
    plt.ylabel('Number of customers')
    plt.show()
def plot_his2():
    plt.step(np.array(obs_time), np.array(q_length), where='post')
    plt.xlabel('Time(min)')
    plt.ylabel('Queue lenght')
    plt.show()

def run_thread(n,st):
    operation(st)
    print('\x1b[5;30;45m' + f'{df}' + '\x1b[0m')
    print('\x1b[5;30;45m' + f'Avarage Service time: {sum(service_time) / n} Second' + '\x1b[0m')
    print('\x1b[5;30;45m' + f'Avarage Queue Time: {sum(qt) / n} Second' + '\x1b[0m')
    print('\x1b[5;30;45m' + f'System Idol: {idol} Second' + '\x1b[0m')
    plot_his1()
    plot_his2()


# Create thread instances
t1 = threading.Thread(target=run_thread(n,st=0.5))

# Start the threads
t1.start()

# Wait for both threads to finish
t1.join()
