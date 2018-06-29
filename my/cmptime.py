from heapq import *
import random
import time

if __name__ == "__main__":

    #lst = [x for x in range(100000)]
    #lst = [random.randint(0, 100) for __ in range(100000)]
    lst = [x for x in range(100000,0,-1)]
    
    start = time.time()
    hp1 = []
    for i in lst:
        heappush(hp1, i)
    end = time.time()
    print "heappush:", end-start


    start = time.time()
    heapify(lst)
    end = time.time()
    print "heapify:", end-start
   
