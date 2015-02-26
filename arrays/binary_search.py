def binary_search(arr, ele):
	left = 0
	right = len(arr)-1

	while left <= right:
		mid = (left+right)/2
		if ele > arr[mid]:
			left = mid + 1
		elif ele < arr[mid]:
			right = mid - 1
		else:
			return mid
	return -1

arr = [1,2,3,4,5,6,7,8,9]
print binary_search(arr, 8)


