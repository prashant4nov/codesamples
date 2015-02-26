''' quick sort'''
def quicksort(arr, size):
	partition(arr, size)

def partition(arr, size):
	if size <= 1:
		return

	left = 0
	right = size - 1
	pivot = arr[size/2]

	while left < right:
		while arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right -= 1

		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp

	partition(arr, left)
	partition(arr[left:], len(arr[left:])


arr = [1,2,3,4,5,45,3,5,4,6]
quicksort(arr, len(arr))
