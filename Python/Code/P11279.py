# https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
# https://www.acmicpc.net/problem/11279

import sys
import heapq

# initialize list
q = []
# convert to heap
heapq.heapify(q)

# Test case
for _ in range(int(input())):
    elem = -int(sys.stdin.readline())
    # add elem to heap
    heapq.heappush(q, elem)
    if elem == 0:
        # Remove smallest element from the heap
        temp = -heapq.heappop(q)
        print(temp)
