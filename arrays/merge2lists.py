'''
http://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/
'''
def merge(l1, l2):
	i = 0
	j = 0
	done = False
	res = []
	median = 0
	while not done:
		if l1[i] < l2[j]:
			res.append(l1[i])
			if i == len(l1)-1:
				res = res + l2[j:]
				done = True
			i += 1
		else:
			res.append(l2[j])
			if j == len(l2)-1:
				res = res + l1[i:]
				done = True
			j += 1

	return res


l1 = [1,3,5]
l2 = [4,6,8]

print merge(l1, l2)



