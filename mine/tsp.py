#V=[[0,1,2,4]
#   [1,0,3,4]
#   [2,4,0,5]
#   [3,4,5,0]] martix
from collections import defaultdict

def tsp( V ):
    L = len(V[0])
    visit = tuple([1]*L)
    result = defaultdict(int)
    min_tmp = 100000000
    
    def d(i, Visit):
        if (i,Visit) in result:
            return result[i, Visit]
        if sum(Visit) == 1:
            result[i, Visit] = V[i][0]
           # print V[i][0]
            return result[i, Visit]

        
        
        for k in range( 1, L ):
            if Visit[k] == 1 and V[i][k]!= 0:
                #print i, Visit
                v_tmp = Visit
                v_tmp = list(v_tmp)
                v_tmp[k] = 0
                v_tmp = tuple(v_tmp)

                min_tmp = V[i][k] + d(k, v_tmp)
                #print "Vik",V[i][k]
                #print "min",min_tmp
                if result[i, Visit]==0 or min_tmp < result[i, Visit]:
                    result[i, Visit] = min_tmp
        return result[i, Visit]
                             
    return d(0, visit)

if __name__ == "__main__":

    v1 = [[0, 1, 2, 4], [1, 0, 3, 4], [2, 4, 0, 5], [3, 4, 5, 0]]
    v2 = [[0,3,6,7],[5,0,2,3],[6,4,0,2],[3,7,5,0]]
    v3 = [[0,3,6],[5,0,2],[6,4,0]]
    print tsp(v1)
    print tsp(v2)
    print tsp(v3)
