import random
def partition(qlist):
    p = random.randint(0,len(qlist)-1)
    pivot = qlist[p]
    left=[x for x in qlist if x < pivot]
    right=[x for x in qlist[:p] if x>=pivot]+[x for x in qlist[p+1:] if x>=pivot]  
    return left, pivot, right

def qselect(p, qlist):
    left, pivot, right = partition(qlist)
    
    if len(left) == p-1:
        result = pivot
    elif len(left) >= p-1:
        result = qselect(p,left)
    else:
        result = qselect(p-1-len(left),right)
    return result

