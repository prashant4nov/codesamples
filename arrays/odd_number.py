# http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
arr = [3,4,4,5,6,4,2,4,2,4,6,3,5,5]

def odd_number(arr):
	group = {}
	for i in xrange(len(arr)):
		if arr[i] in group.keys():
			group[arr[i]] += 1
		else:
			group[arr[i]] = 1

	for i in group.keys():
		if group[i] % 2 != 0:
			print i


odd_number(arr)
