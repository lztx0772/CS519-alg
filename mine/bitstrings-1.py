##3. Number of bit strings of length n that has
##   1) no two consecutive 0s.
##   2) two consecutive 0s.
##1.  1+a[n-1]
##2.  01+a[n-2]   
##3.  00+all      2^(n-2)

def num_yes( n ):
    return fib2(n)

def num_no( n ):
    #print num_yes(n)
    #print 2**n
    return 2**n - num_yes(n)

def fib2(n, cache=None):
                if cache is None:
                    cache = {}
                if n in cache:
                    return cache[n]
                cache[n] = 0 if n==0 or n==1 else fib2(n-1, cache)+fib2(n-2, cache) + 2**(n-2)
                return cache[n]
