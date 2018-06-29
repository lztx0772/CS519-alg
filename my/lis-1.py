###############
#CS519
#Xiao Tan
#HW 8 - 1
###############
def lis(arr):
	n = len(arr)
	m = [0]*n
	for x in range(n-2,-1,-1):
		for y in range(n-1,x,-1):
			if arr[x] < arr[y] and m[x] <= m[y]:
				m[x] += 1
		max_value = max(m)
		result = ""
		for i in range(n):
			if m[i] == max_value:
				result += arr[i]
				max_value -= 1
	return result


if __name__ == "__main__":
        print lis("aebbcg") 
        print lis("zyx")
        print lis("fdfadfasfasdfa")
        print lis("hjafjoajfoiajlang")
