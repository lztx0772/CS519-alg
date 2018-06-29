#
#CS519 HW 9
#Xiao Tan - 2
#
from collections import defaultdict
def longest(n, edges):    
    def order(num, edges): #do Topological Sort
        v = range(num) #generate vertex list
        def check_indegree(v, edges):
            if v == []:
                return None
            tmp = v[:]
            for i in edges:
                if i[1] in tmp:
                    tmp.remove(i[1])
            if tmp == []:
                return -1 #check if a circle
            #delete elements in v and edges
            for t in tmp:  
                for i in range(len(edges)):  
                    if t in edges[i]:  
                        edges[i] = (-1, -1)
            if edges:  
               e_tmp = set(edges)
               e_tmp.remove((-1, -1))
               edges[:]=list(e_tmp)  
            if v:  
                for t in tmp:  
                    v.remove(t)  
            return tmp
        result=[]  
        while True:  
            nodes = check_indegree(v,edges)  
            if nodes == None:  
                break  
            if nodes == -1:  
                return None  
            result.extend(nodes)  
        return result

    torder = order(n, edges[:]) #get topological order
    #print torder
    if torder is None:
        return None
    back = [(0, -1)]*n # init
   # print back
    
    for i in torder:
        #print i
        for j in edges:
            if i == j[0]:
                tmp = back[i][0] + 1
                if tmp > back[j[1]][0]:
                    back[j[1]] = tmp, i

    def backtrack(l, d):
        max_l, max_i = 0, 0
        result = []
        for i in range(l):
            if max_l < d[i][0]:
                max_l = d[i][0]
                max_i = i
        for j in range(max_l+1):
        #while d[max_i][1] != -1:
            result.append(max_i)
            max_i = d[max_i][1]
        result.reverse()
        return max_l, result

    return backtrack(n, back)  


if __name__ == "__main__":
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   #(5, [0, 2, 3, 4, 5, 6])

    print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
   #(5, [0, 2, 4, 3, 5, 6])

    print longest(4, [(0,1), (1,2), (2,1), (2,3)])
    #None
