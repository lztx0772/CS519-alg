#
#CS519 HW 9
#Xiao Tan - 1
#

def order(num, edges):
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

if __name__ == "__main__":
   print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   #[0, 1, 2, 3, 4, 5, 6, 7]

   print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
   #[0, 1, 2, 4, 3, 5, 6, 7]
   
   print order(4, [(0,1), (1,2), (2,1), (2,3)])
   #None
