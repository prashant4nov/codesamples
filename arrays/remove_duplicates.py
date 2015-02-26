def remove_duplicates(arr):
	arr = sorted(arr)
	print arr
	prev = 0
	for i in xrange(1, len(arr)-1):
		print 'i-1:%d' % arr[i-1]
		print 'i:%d' % arr[i]
		print 'i+1:%d' % arr[i+1]

		if arr[i] == arr[prev]:
			arr[prev] = arr[prev]

	return arr


arr = [12,12,23,12,21,2,12,23,23,22]

print remove_duplicates(arr)