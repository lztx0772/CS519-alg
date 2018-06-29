import math

def kmergesort(lst, k):
    if len(lst) <= 1:
        return lst
    n = int(math.ceil(len(lst)/float(k)))
    lst = [kmergesort(lst[i:i+n], k) for i in range(0, len(lst), n)]
    return merge(lst)

def merge(allst):
    sorted_lst = []
    while allst:
        minum,index = allst[0][0],0
        for lst in allst:
            if lst[0]<minum:
                minum = lst[0]
                index = allst.index(lst)

        sorted_lst.append(minum)
        allst[index].pop(0)
        if allst[index] == []:
            allst.remove(allst[index])     
    return sorted_lst

#if __name__ == "__main__":
#    print kmergesort([4,1,5,2,6,3,7,0], 3) 

