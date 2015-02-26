# http://www.geeksforgeeks.org/factorial-large-number/.
def factorial(n):
	result = [1]
	for i in xrange(2, n+1):
		result = multiply(i, result)

	return result
		
def multiply(i, result):
	carry = 0
	for j in xrange(0, len(result)):
		prod = i*result[j] + carry
		carry = int(prod/10)
		result[j] = prod % 10

	while carry:
		r = carry % 10
		result = result + [r]
		carry = carry/10
	return result

result = factorial(1000)
for i in xrange(1, len(result)+1):
	print result[-i]

