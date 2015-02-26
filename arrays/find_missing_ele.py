'''
http://www.geeksforgeeks.org/find-the-missing-number/
'''
# about xor : http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/BitOp/xor.html

def missing_ele(arr):
	x1 = 0
	x2 = 0
	for i in xrange(0, len(arr)):
		x1 = x1 ^ arr[i]
	for i in xrange(1, len(arr)+2):
		x2 = x2 ^ i

	print (x1 ^ x2)

arr = [1,2,3,4,5,7]

missing_ele(arr)
