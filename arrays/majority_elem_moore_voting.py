'''
http://www.geeksforgeeks.org/majority-element/
'''
def find_candidate(arr):
	index = 0
	count = 1
	for i in xrange(1, len(arr)):
		if arr[i] == arr[index]:
			count += 1
		else:
			count -= 1

		if count == 0:
			index = i
			count = 1

	return arr[index]


def majority(arr):
	count = 0
	element = find_candidate(arr)
	for i in xrange(0, len(arr)):
		if element == arr[i]:
			count += 1
		if count > len(arr)/2:
			return element


arr = [4,4,4,4,2,5,4,5,7]
print majority(arr)
