def find_hash_sum(arr, x):
	match = {}
	found = 0
	for i in xrange(len(arr)):
		if x-arr[i] in match.keys():
			for j in match[x-arr[i]]:
				found += 1
				print '%d, [%d]:, %d, [%d]:, %d' % (found, j, arr[j], i, arr[i])
		if arr[i] in match.keys():
			match[arr[i]].append(i)
		else:
			match[arr[i]] = [i]



arr = [6,4,7,8,42,61,34,6,4]

arr = [6,4,7,8,9,4,6]

find_hash_sum(arr, 10)