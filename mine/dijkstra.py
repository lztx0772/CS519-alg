#
#CS519 HW 9
#Xiao Tan - 3
#

from heapdict import *

def shortest(n, paths):
      #  v = range(n)
    hd = heapdict()
    back = [0]
    
    res = [float("inf")]*n
    for i in range(n):
        hd[i] = float("inf")

    idx = 0
    value = 0
    dflag = 0
    count = 0
    while count != n - 1:
        #print idx
        for j in range(len(paths)):
            #print j
            if idx == paths[j][0]:
                tmp = value + paths[j][2]
                #print tmp
                if hd[paths[j][1]] > tmp:
                    hd[paths[j][1]] = tmp
                paths[j] = (-1,-1,-1)#mark used as (-1,-1,-1)
                dflag = 1
                #print paths

        if  dflag:
            #print paths
            p_tmp = set(paths)
            p_tmp.remove((-1,-1,-1))
            paths[:]=list(p_tmp)
            dflag = 0
            
        idx, value = hd.popitem()
        #print idx, value
        res[idx] = value
        back.append(idx)
        count += 1
    return res[n-1], back

if __name__ == "__main__":
    print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
    print shortest(6, [(0,1,7),(0,5,14),(0,2,9),(1,2,10),(1,4,15),(2,5,2),(2,3,11),(3,4,6),(4,5,9)])
