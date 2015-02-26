from itertools import groupby
arr = [1,2,3,3,3,4,5,6,7,7,7,8,8,8,8,8,9]
a, b = [], []
for i, g in groupby(arr):
	group = list(g)
	(a if len(group) > 2 else b).extend(group)

print a + b
