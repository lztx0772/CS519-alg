def find(l):
    l.sort() #sort list first
    res = []
    for pos in range(len(l)):
        left, right = 0, len(l)-1

        while left < right:
            if left == pos:
                left += 1
            elif right == pos:
                right -= 1
            elif l[left]+l[right] == l[pos]:
                res.append((l[left],l[right],l[pos]))
                left += 1
                right -= 1
            elif l[left]+l[right] > l[pos]:
                right -= 1
            elif l[left]+l[right] < l[pos]:
                left += 1
        
    return res
   
