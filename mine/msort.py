def mergesort(mlist):
    if len(mlist) < 2:
        return mlist
    
    result = []
    mid = int(len(mlist)/2)
    left = mergesort(mlist[:mid])
    right = mergesort(mlist[mid:])
    
    while(len(left) > 0 ) and (len(right) > 0):
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left+right)
    return result
