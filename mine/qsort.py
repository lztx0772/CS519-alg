#sorted(t): returns the sorted order (infix traversal)
#search(t, x): returns whether x is in t
#insert(t, x): inserts x into t (in-place) if it is missing, otherwise does nothing.
def sorted(t):
        if t == []:
                return []
        return sorted(t[0])+[t[1]]+sorted (t[2])

def _search(tree, x):
        if tree == []:
                return tree
        if tree[1] == x:
                return tree
        elif tree[1] > x:
                return _search(tree[0], x)
        else:
                return _search(tree[2], x)

def search(t, x):
        if _search(t, x) == []:
                return False
        else:
                return True    

def insert(t, x):
        if not search(t, x):
                _search(t, x).extend([[],x,[]])

def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot ]
		right = [x for x in a[1:] if x >= pivot]
		return [sort(left)] + [pivot] + [sort(right)]
