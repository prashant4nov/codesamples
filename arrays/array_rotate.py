'''
http://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
'''

def rotate(arr, d):
	i = 1
	done = False
	while i <= d:
		arr.append(arr[0])
		arr.remove(arr[0])
		i += 1


#def reversal_rotate()
arr = [1,2,3,4,5]

rotate(arr, 2)

print arr