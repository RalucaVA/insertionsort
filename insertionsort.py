import time

st = time.time()


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
            
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key

import random
dataset=[]
for i in range(490293032):
    x=random.randrange(0, 500000339783)
    dataset.append(i)

insertionSort(dataset)
print(dataset)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')