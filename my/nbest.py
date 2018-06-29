from random import randint
import time

def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return []
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x[0]+x[1] < pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1]<pivot[1])]
        right = [x for x in a[1:] if x[0]+x[1] > pivot[0]+pivot[1] or (x[0]+x[1]==pivot[0]+pivot[1] and x[1]>pivot[1])]
        lleft = len(left)
        return left+[pivot] if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            left+[pivot]+qselect(k-lleft-1, right)

def nbesta(a, b):
    if not len(a)==len(b):
        return "n is different"
    lst, n= [], len(a)
    for i in a:
        for j in b:
            lst.append((i, j))
    lst.sort(key=lambda x:(x[0]+x[1], x[1]))
    return lst[0:n]

def nbestb(a, b):
    if not len(a)==len(b):
        return "n is different"
    lst, n= [], len(a)
    for i in a:
        for j in b:
            lst.append((i, j))
    lst = qselect(n, lst)
    return sorted(lst, key=lambda x:(x[0]+x[1], x[1]))


def nbestc(a, b):
    x = a.sort()
    y = b.sort()
    

if __name__ == "__main__":
    a, b = [4, 1, 5, 3], [2, 6, 3, 4]
    print nbesta(a, b)
    print nbestb(a, b)

   # a = b = range(2000)
   # s = time.time()
   # nbesta(a, b)
   # print time.time()-s
   # print "--------"
   # s = time.time()
    #nbestb(a, b)
    #print time.time()-s
