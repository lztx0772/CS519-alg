###############
#CS519
#Xiao Tan
#HW 7 - 2
###############
from collections import defaultdict

def best(amount, value):
    opt = defaultdict(lambda : -1)
    types = -1
    res = [0]*len(value)
    
    def _best(i, x):
        if i < 0 or x < 0 :
            return 0
        if x == 0:
            opt[i, x] = 1
            return opt[i, x]
        if (i, x) in opt:
            return opt[i, x]
        op1 = _best(i-1, x)
        op2 = _best(i, x - value[i])
        opt[i, x] = op1 or op2
        return opt[i, x]
    
    def trace(i):
        t, m, n = 0, 0, i
        flag = 1
        tmp = [0]*len(value)
        while m < amount:
            if opt[n, m + value[n]]==1:
                tmp[n] += 1
                m += value[n]
                if flag ==1:
                    t += 1
                    flag = 0
            else:
                n += 1
                flag = 1
        return t,tmp 

    _best(len(value)-1, amount)
    #print opt
    if  opt[len(value)-1, amount]== 0:
        return None
    else:
        for i in range(len(value)):
            if opt[i, 0] == 1:
               a, b = trace(i)
               if types == -1 or types > a:
                   types = a
                   res = b
                   
    return types, res

if __name__ == "__main__":
    
   print best(47, [6, 10, 15])
  # (3, [2, 2, 1])

   print best(59, [6, 10, 15])
  # (3, [4, 2, 1])	

   print best(37, [4, 6, 15])
  # (3, [4, 1, 1])
 
   print best(27, [4, 6, 15])
   #(2, [3, 0, 1])

   print best(75, [4, 6, 15])
   #(1, [0, 0, 5])

   print best(17, [2, 4, 6])
   #None
