import numpy as np
import matplotlib.pyplot as plt

def delay(n, k):
    n1 = []
    for i in range(0,len(n)):
        n1.append(n[i]+k)
    return n1
def advence(n, k):
    n1 = []
    for i in range(0,len(n)):
        n1.append(n[i]-k)
    return n1

def sceling(n , k):
    n1 = []
    for i in range(0,len(n)):
        n1.append(n[i]*k)
    return n1

x1 = []
x2 = []
x = []
for i in range(-10,11):
    x.append(i)
    x1.append(0.5*np.cos(np.pi*i))
    x2.append(2*np.sin(np.pi*i))
print(x1)
print(x2)

#delay by three x1.. 
new_x1 = delay(x1 , 3)
new_x11 = sceling(new_x1 , 0.5)
print(new_x11)

#delay by three x2.. 
new_x111 = sceling(x1 , 0.5)
print(new_x111)


#add x1 and x2..
y1 = []
for i in range(0,len(x1)):
    y1.append(new_x11[i]+new_x111[i])

new_x2 = advence(x2 , 3)
new_x22 = advence(x2 , 1)

#add new_x2 , new_x22
y2 = []
for i in range(0 , len(x2)):
    y2.append(new_x2[i] + new_x22[i])
print(y2)

y = []
for i in range(0 , len(y1)):
    y.append(y1[i]+y2[i])
print(y)

#plot y1 , y2 , y signal
plt.subplot(3,1,1)
plt.stem(x,x1)
plt.subplot(3,1,2)
plt.stem(x,x2)
plt.subplot(3,1,3)
plt.stem(x,y)