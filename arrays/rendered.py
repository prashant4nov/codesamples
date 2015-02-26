def rendered(arr):
	single_elements = []
	double_elements = []
	for i in xrange(len(arr)-1):
		if arr[i] == arr[i+1] or arr[i] == arr[i-1]:
			double_elements.append(arr[i])
		else:
			single_elements.append(arr[i])
    
	if arr[-1] == double_elements[-1]:
		double_elements.append(arr[-1])
	else: 
		single_elements.append(arr[-1])

	return single_elements+double_elements


arr = [1,2,3,3,3,4,5,6,7,7,7,7,8,8,8,9]

#output arr = [1,2,4,5,6,9,3,3,3,7,7,7,7,8,8,8]

print rendered(arr)