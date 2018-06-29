def mergesort(mlist, c):
    if len(mlist) < 2:
        return mlist
    
    result = []
    mid = int(len(mlist)/2)
    left = mergesort(mlist[:mid], c)
    right = mergesort(mlist[mid:], c)
    
    while(len(left) > 0 ) and (len(right) > 0):
        if left[0] > right[0]:
            c[0] += len(left)
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left+right)
    return result

def num_inversions(a):
    count = [0]
    mergesort(a, count)

    return count[0]
