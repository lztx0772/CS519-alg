def max_wis(a):
    return opt(len(a)-1, a)

def opt(n, a, route = None, cache = None):
    if cache is None:
        cache = {}
    if route is None:
        route = {}
        
    if n == -2 or n == -1:
        cache[n+2] = 0
        route[n+2] = []
    if n+2 in cache:
        return cache[n+2], route[n+2]

    tmp1, r1 = opt(n-2, a, route, cache)
    tmp2, r2 = opt(n-1, a, route, cache)

    if  tmp1 + a[n] > tmp2:
        cache[n+2] = tmp1 + a[n]
        route[n+2] = route[n]+[a[n]]
        
    else:
        cache[n+2] = tmp2
        route[n+2] = route[n+1]

    return cache[n+2], route[n+2]

def max_wis2(a):
    opt = {}
    route = {}
    opt[0] = opt[1] = 0
    route[0] = route[1] = []
    for i in range(len(a)):
        tmp1 = opt[i] + a[i]
        tmp2 = opt[i+1]
        if tmp1 > tmp2:
            opt[i+2] = tmp1
            route[i+2] = route[i]+[a[i]]
        else:
            opt[i+2] = tmp2

    return opt[len(a)+1], route[len(a)+1]
 
