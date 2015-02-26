'''
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# kadanes algorithm
'''

def max(x, y):
	return y if y > x else x

def largest_sub_sum(arr):
	curr_max = arr[0]
	max_so_far = arr[0]
	for i in xrange(1, len(arr)):
		curr_max = max(arr[i], curr_max+arr[i])
		max_so_far = max(max_so_far, curr_max)

	print max_so_far

arr = [3,4,45,6,3,2,-1,-45,-6,10]
largest_sub_sum(arr)
arr = [-5,-1,-2,-3,-4]
largest_sub_sum(arr)