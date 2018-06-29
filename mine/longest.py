def longest(t):

    return merge(t)[0]

def merge(t):
    if len(t) < 3: return [0 ,0]

    left = merge(t[0])
    right = merge(t[2])

    lg, dep = left[0], left[1]+1
    if left[1] < right[1]: dep = right[1]+1
    if left [0] < right [0]: lg = right[0]
    if left[1]+right[1] > lg: lg = left[1]+right[1]

    return [lg, dep]
    
