arr = [1,2]
for i, ele in enumerate(arr):
	print i,
	print ele

print '-------'
for i, ele in enumerate(arr[:-1]):
	print i,
	print ele

print '-----'
for i, ele in enumerate(arr[:-1], 1):
	print i,
	print ele