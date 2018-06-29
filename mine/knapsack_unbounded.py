##   >>> best(3, [(2, 4), (3, 5)])
##   (5, [0, 1])

def best(maxweight, items, cache = None):
    result = [0 for i in range(len(items))]
    if cache is None:
        cache = {}
        
    def best_helper(i, m):
        if i == 0:
            return 0
        if (i,m) in cache:
            return cache[i, m]
        
        weight, value = items[i - 1]
        if weight > m:
            cache[i, m] = best_helper(i - 1, m)
            return cache[i, m]
        else:
            op1 = best_helper(i - 1, m)
            op2 = best_helper(i, m - weight) + value
            print op1, op2, i
            if op1 >= op2:
               #result[i-1] = result[i]
                cache[i, m] = op1
            else:
                #result[i-1] += 1
                cache[i, m] = op2
            return cache[i, m]
              
            #return max(best_helper(i - 1, m), best_helper(i, m-weight) + value)

        
##    result, weight = [0 for i in range(len(items))], maxweight
##    for i in xrange(len(items), 0, -1):
##        if best_helper(i, weight) != best_helper(i-1, weight):
##            result[i - 1] += tmp / items[i - 1][1]
##            weight-=items[i - 1][0]
    return best_helper(len(items),maxweight), result


