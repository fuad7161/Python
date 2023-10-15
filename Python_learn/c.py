import simpy
import numpy as np
import matplotlib.pyplot as plt

def warehouse_run(env , order_cutoff,order_target):
    global inventory , balance , num_ordered

    inventory = order_target
    balance = 0.0
    num_ordered = 0

    while True:
        interarrival = generate_interarrival()
        yield  env.timeout(interarrival)
        balance -= inventory*2*interarrival
        demand = generate_demand()
        if demand < inventory:
            balance += 100*demand
            inventory -= demand
            print(f'{env.now:.2f} sold {demand}')
        else:
            balance += 100*inventory
            inventory = 0
            print(f'{env.now:.2f} sold {inventory} Out of stok')
        if inventory< order_cutoff and num_ordered == 0:
            env.process(handle_order(env , order_target))
def handle_order(env , order_target):
    global inventory , balance , num_ordered
    print(f'{env.now:.2f} placed order for {num_ordered}')
    num_ordered = order_target - inventory
    balance -= 50*num_ordered
    yield env.timeout(2.0)
    inventory += num_ordered
    num_ordered = 0
    print(f'{env.now:.2f} received order, {inventory} in inentory')

def generate_interarrival():
    return  np.random.exponential(1./5)
def generate_demand():
    return np.random.randint(1,5)
obs_time = []
inventory_level = []

def observe(env):
    global inventory
    while True:
        obs_time.append(env.now)
        inventory_level.append(inventory)
        yield env.timeout(0.1)

np.random.seed(0)
env = simpy.Environment()
env.process(warehouse_run(env , 10 , 30))
env.process(observe(env))
env.run(until=10.0)

print(inventory_level)
print(obs_time)
obs_time.append(10)
ans = 0
for i in range(0,len(inventory_level)):
    ans += (inventory_level[i]*(obs_time[i+1] - obs_time[i]))
print(ans)
obs_time.pop()
plt.figure()
plt.step(obs_time , inventory_level , where='post')
plt.xlabel('Simulation time (days)')
plt.ylabel('Inventory level')
plt.show()