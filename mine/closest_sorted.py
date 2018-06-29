import bisect

def find(l, num, count):
    if l == []:
        return []
    pos = bisect.bisect(l, num)
    left, right = pos-1, pos
    while count != 0:
        if right == len(l) or abs(num-l[left]) <= abs(l[right]-num):
            left = left - 1
        elif left < 0 or abs(num-l[left]) > abs(l[right]-num):
            right = right + 1
        count = count -1
        
    return l[left+1:right]        

if __name__ == "__main__":
    print find([1,2,3,4,4,7], 5.2, 2) #returns   [4,4]
    print find([1,2,3,4,4,7], 6.5, 3) #returns   [4,4,7]
    print find([1,2,3,4,4,6,6], 5, 3) #returns   [4,4,6]
    print find([1,2,3,4,4,5,6], 4, 5) #returns   [2,3,4,4,5]
