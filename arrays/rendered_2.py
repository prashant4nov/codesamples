def rendered(arr):
	sin_ele = []
	dbl_ele = []
	for i, ele in enumerate(arr[:-1], 1):
		print '[' + str(i)+ ']',
		#print ele,
		print arr[i-2],
		print ele,
		#print arr[i-1],
		print arr[i]
		dbl_ele.append(ele) if ele == arr[i] or ele == arr[i-2] else sin_ele.append(ele)
	ele = arr[-1]
	dbl_ele.append(ele) if ele == dbl_ele[-1] else sin_ele.append(ele)
	sin_ele.extend(dbl_ele)
	return sin_ele


arr = [1,2,3,3,3,4,5,6,7,7,7,7,8,8,8,9]

#output arr = [1,2,4,5,6,9,3,3,3,7,7,7,7,8,8,8]

print rendered(arr)