'''
http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
'''
def binary_search_rotated(arr, start, end, ele):
	if start > end:
		return -1
	else:
		mid = (start + end)/2
		if arr[mid] == ele:
			return mid
		elif arr[start] <= arr[mid]: # start half is in sorted order.
			if ele >= arr[start] and ele < arr[mid]:
				return binary_search_rotated(arr, start, mid-1, ele)
			else:
				return binary_search_rotated(arr, mid+1, end, ele)
		else: # end half is in sorted order.
			if ele > arr[mid] and ele <= arr[end]:
				return binary_search_rotated(arr, mid+1, end, ele)
			else:
				return binary_search_rotated(arr, start, mid-1, ele)


def search(arr, ele):
	return binary_search_rotated(arr, 0, len(arr)-1, ele)


arr = [3,4,5,6,1,2]
print search(arr, 2)
