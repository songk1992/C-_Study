# https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
# https://docs.python.org/3/library/heapq.html
# https://www.acmicpc.net/problem/11279
# https://www.acmicpc.net/problem/1927

import sys
import heapq

# initialize list
q = []
# convert to heap
heapq.heapify(q)

# Test case
for _ in range(int(input())):
    elem = int(sys.stdin.readline())
    if elem != 0:
        # add elem to heap
        heapq.heappush(q, elem)

    else:
        try:
            # Remove smallest element from the heap
            print(heapq.heappop(q))
        except:
            print(0)

