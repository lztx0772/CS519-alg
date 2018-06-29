##best(3, [(2, 4, 2), (3, 5, 3)])

def best(maxweight, items, cache = None):
    result = [0 for i in range(len(items))]
    if cache is None:
        cache = {}
        
    def best_helper(i, m):
        if i == 0:
            return 0
        if (i,m) in cache:
            return cache[i, m]
        
        weight, value, num = items[i - 1]
        if weight > m:
            cache[i, m, pre] = best_helper(i - 1, m)
            return cache[i, m]
        else:
            op1 = best_helper(i - 1, m)
            op2 = best_helper(i, m - weight) + value
            print op1, op2, i
            if op1 >= op2:
                cache[i, m] = op1
            else:
                cache[i, m] = op2
            return cache[i, m]
        
    return best_helper(len(items),maxweight), result


