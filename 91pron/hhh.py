import random


iplist = []
hhhhh = []

for i in range(20000):
    randomIP = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
        random.randint(0, 255)) + '.' + str(random.randint(0, 255))
    iplist.append(randomIP)
    iplist = list(set(iplist))
print(len((iplist)))