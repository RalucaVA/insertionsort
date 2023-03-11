import time

# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# wait for 3 seconds
time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

data=[]
for k in range(5000000,0,-1):
    data.append(k)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)