# http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
def find_sum_hash(arr, x):
	match = {}
	found = 0
	for i in xrange(len(arr)):
		if x-arr[i] in match.keys():
			for t in match[x-arr[i]]:
				found += 1
				print '%d, [%d]= %d, [%d]= %d' % (found, t, arr[t], i, arr[i])
		if arr[i] in match.keys():
			match[arr[i]].append(i)
		else:
			match[arr[i]] = [i]
	return found

arr=[6,3,643,54,63,43,66,74,26,4,56,64]
arr = [6,-4,7,8,9,4,6]

x=10
print find_sum_hash(arr, x)
