from random import randint
def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
       # print pindex
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return left+[pivot] if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            left+[pivot]+qselect(k-lleft-1, right)
       
def mklist(a,v):
    res = []
    for i in range(len(a)):
        res.append((abs(a[i]-v),i))
    return res

def find(a, v, k):
    ls = mklist(a,v)
    tp = qselect(k, ls)
    #print tp
    idx, res = [], []
    for i in range(len(tp)):
        idx.append(tp[i][1])
    idx = sorted(idx)
    #print idx
    for j in idx:
       # print j
        res.append(a[j])
    return res
