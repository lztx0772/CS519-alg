#f(n)=f(n-1)+f(n-2)*f(1)+f(n-3)f(2)+...+f(n-3)f(2)+f(n-2)f(1)

def bsts(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    if n == 0 or n == 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    else:
        cache[n] = 0
        for i in range(n):
            cache[n] += bsts(n-(i+1), cache)*bsts(i, cache)
    return cache[n]
