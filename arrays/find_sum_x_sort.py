'''
http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
'''

def find_sum(arr, n):
	left = 0
	right = len(arr) - 1

	while left < right:
		sum = arr[left] + arr[right]
		if n == sum:
			return True, left, arr[left], arr[right]
		else:
			if sum < n:
				left += 1
			else:
				right -= 1

		return False



n = 11
arr = [1,2,3,4,5,6,7,8,9]
print find_sum(arr, n)