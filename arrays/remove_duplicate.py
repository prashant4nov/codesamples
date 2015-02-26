def remove_duplicate(a):
	n = len(a)
	for i in xrange(0, n):
		j = i+1
		while j < n:
			if a[j] == a[i]:
				for k in xrange(j, n-1):
					a[k] = a[k+1]
				n = n-1
			else:
				j = j+1

	print a[:n]

a = [1,2,3,1,2,3,3,3,3,4,5,4,5,4,4,5]

remove_duplicate(a)