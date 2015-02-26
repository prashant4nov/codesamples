'''
http://www.geeksforgeeks.org/write-a-program-to-reverse-an-array/
'''
def reverse(arr):
	for i in xrange(0, len(arr)/2):
		print 'arr[i]',
		print arr[i]
		print 'arr[-(i+1)]',
		print arr[-(i+1)]
		temp = arr[i]
		arr[i] = arr[-(i+1)]
		arr[-(i+1)] = temp
	print arr


arr = [1,2,3,4,5,6,7]

reverse(arr[:])
print arr