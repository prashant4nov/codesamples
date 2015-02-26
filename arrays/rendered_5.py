arr = [1,2,3,3,3,4,5,6,7,7,7,8,8,8,8,8,9]

group = {}
a, b = [], []
for i in xrange(len(arr)):
	if arr[i] in group.keys():
		group[arr[i]].append(arr[i])
	else:
		group[arr[i]] = [arr[i]]

for i in group.keys():
	print i,
	print group[i]
	(a if len(group[i]) > 2 else b).extend(group[i])

print a
print b