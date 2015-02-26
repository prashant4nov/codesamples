'''
http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
'''

def odd_no(arr):
	result = 0
	for i in xrange(0, len(arr)):
		result = result ^ arr[i]

	return result

print odd_no(arr=[1,90,2,3,4,5,6,7,90,1,2,3,4,5,6,7,8,8,90])