#
#CS519 RNA
#Xiao Tan
#

from collections import defaultdict
def _match(a, b):
    if (a == 'A' and b == 'U') or (b == 'A' and a == 'U'):
        return True
    if (a == 'G' and b == 'C') or (b == 'G' and a == 'C'):
        return True
    if (a == 'G' and b == 'U') or (b == 'G' and a == 'U'):
        return True
    return False

def _printer(l, back):
    tmp = ['.']*l
    result = ''
    for i in back:
        tmp[i[0]] = '('
        tmp[i[1]-1] = ')'
    for j in tmp:
        result += j
    return result

def best(rna):
    cache = defaultdict(int)
    back = defaultdict(lambda:[])
    
    def _best(i, j):
        if (i, j) in cache:
            return cache[i, j]
        if i == j:
            return cache[i, j]
        if i+1 == j:
            return cache[i, j-1]
        tmp = -1
        if _match(rna[i],rna[j-1]):
            tmp = _best(i+1, j-1) + 1
            back[i, j] = back[i+1, j-1] + [(i,j)]
        for k in range(i+1, j):
            if tmp < _best(i, k) + _best(k, j):
                tmp = _best(i, k) + _best(k, j)
                back[i, j] = back[i, k] + back[k, j]
        cache[i, j] = tmp
        return cache[i, j]
    i, j = 0, len(rna)
    res = _best(i, j)

    print back
    return res, _printer(j, back[i, j])

def total(rna):
    tot = defaultdict(lambda: 1)
    def _tot(i, j):
        if (i, j) in tot:
            return tot[i, j]
        if i == j:
            return tot[i, j]
        if i+1 == j :
            return tot[i, j]
        
        _sum = 0
        for k in range(i+1, j+1):
            
            if _match(rna[i], rna[k-1]) :
                _sum = _sum +_tot(i+1, k-1)*_tot(k, j)
            else:
                tot[i, j] = _tot(i+1, j)
        tot[i, j] = _tot(i+1, j) + _sum
        return tot[i, j] 
    i, j = 0, len(rna)
    return _tot(i,j)

    
def kbest(rna, n):



    return []

    


if __name__ == "__main__":
    r1=["ACAGU",
    "AC",
    "GUAC",
    "GCACG",
    "CCGG",
    "CCCGGG",
    "UUCAGGA",
    "AUAACCUA",
    "UUGGACUUG",
    "UUUGGCACUA",
    "GAUGCCGUGUAGUCCAAAGACUUC",
    "AGGCAUCAAACCCUGCAUGGGAGCG"]


    
    #for r in r1:
        #print r
        #print best(r)
        #print total(r)

        

    
