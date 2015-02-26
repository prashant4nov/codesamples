def quicksort(arr):
	partition(arr, 0, len(arr)-1)

def partition(arr, start, stop):
	print 'partition called'
	if stop - start < 1:
		return
	else:
		left = start
		right = stop
		pivot = arr[start + ((stop-start)/2)]
		while left <= right:
			while arr[left] < pivot:
				left += 1
			while arr[right] > pivot:
				right -= 1
			if left <= right:
				arr[left], arr[right] = arr[right], arr[left]
				left += 1
				right -= 1

		partition(arr, start, right)
		partition(arr, left, stop)


arr = [34,63,23,3,2,54,23,5,2]

quicksort(arr)
print arr
