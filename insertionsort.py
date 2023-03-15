import time

st = time.time()


def insertionsort(l):

    for s in range(1, len(l)):
        key = l[s]
        j = s - 1
            
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        
        l[j + 1] = key

import random
dataset=[]
for i in range(8000):
    #x=random.randrange(0, 500000339783)
    dataset.append(i)

insertionsort(dataset)
print(dataset)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')