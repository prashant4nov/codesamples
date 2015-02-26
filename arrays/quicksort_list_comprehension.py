'''
quick sort using list comprehension.
http://en.literateprograms.org/Quicksort_%28Python%29
'''

def quicksort(arr):
	if arr == []:
		return []
	else:
		pivot = arr[0]
		lesser = quicksort([x for x in arr[1:] if x < pivot])
		greater = quicksort([x for x in arr[1:] if x >= pivot])
		return lesser + [pivot] + greater


arr = [4,243,56,1,435,84,23,67]
print quicksort(arr)

