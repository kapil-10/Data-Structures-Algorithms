# Heap and priority queue ( both are same , names are used interchangeably )
# Heap is a perticular case of binary_tree

# min-heap parent node is always smaller or equeal to its child node
# time : O(n) , space O(1)

import heapq
from  collections import Counter

#build heap from scarch , Time 0(n log n)
c = [-5,4,2,1,7,0,3]
c_len = len(c)
heap = []
for i in range(c_len):
    heapq.heappush(heap,c[i])
    print('Heap from scarch :',heap,c_len)

a = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9]
heapq.heapify(a)
print('Heapfied min-heap :', a)

# push , time O(logn)
heapq.heappush(a,4) 
print('Push to min-heap :',a)

#pop , time O(logn)
min = heapq.heappop(a)
print('Pop from min-heap :',a , min)

# peek, Tikme O(1)
print('peek_min_heap (minimum) :',a[0])

# heapsort O(n log n), space O(n)

def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minimum = heapq.heappop(arr)
        new_list[i] = minimum

    return new_list

print ('heap_sort :',heap_sort([1,3,5,7,9,2,4,6,8,0]) )

# max - heap

b = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9]
n = len(b)
for i in range(n):
    b[i] = -b[i] # multiply each value -ve 
heapq.heapify(b)
print(b)

# push
heapq.heappush(b,-7) # this inserts positive 7 into max heap

#pop
maximum = -heapq.heappop(b)
print('POP from Max-heap',maximum)

#peek
print('peek max-heap :',b[0])

# find the count in a list using counter from collections library
d = [5, 4, 3, 5, 4, 3, 5, 5, 4]
counter = Counter(d)
print('dublicates in list_count :',counter)






