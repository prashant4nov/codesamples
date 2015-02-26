from itertools import groupby

arr = [3,4,4,5,6,4,2,4,4]

def majorit_ele(arr):
	output = []
	#group = groupby(arr)
	#print len(arr)/2
	print sorted(arr)
	for i, g in groupby(sorted(arr)):
		group = list(g)
		print i, 
		print group
		print len(group)
		if len(group) < len(arr)/2:
			output.extend(group)

	print output

majorit_ele(arr)
