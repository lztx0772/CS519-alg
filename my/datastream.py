from heapq import heappush, heappop
#
#  Find the k smallest numbers in a data stream of length n (k<<n),
#  using only O(k) space (the stream itself might be too big to fit in memory).

#   >>> ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
#  [2, 3, 5, 7]
#   >>> ksmallest(3, xrange(1000000, 0, -1))
#  [1, 2, 3]
#

def ksmallest(k, nums):
    res = []
    for i in nums:
        heappush(res, i*(-1))
        if len(res) > k:
            heappop(res)
    return sorted(map(lambda x:x*(-1),res))
    
if __name__ == "__main__":
    print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
    print ksmallest(3, xrange(1000000, 0, -1))


#complexity: O(nlogk) build heap O(klogk) and bubble-up travsal O(nlogk)
    #so it is o(nlogk)


