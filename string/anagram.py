# print all the permutations of the string.
def perm(a, k, n):
	if k == n: print a
	else:
		for i in xrange(k, n):
			t = txt[i]
			txt = txt[:i] + txt[k] + txt[i+1:]
			txt = txt[:k] + t + txt[k+1:]
			#a[i], a[k] = a[k], a[i]
			perm(a, k+1, n)
			#a[i], a[k] = a[k], a[i]

			t = txt[i]
			txt = txt[:i] + txt[k] + txt[i+1:]
			txt = txt[:k] + t + txt[k+1:]

a = '123'

perm(a, 0, len(a))

# print all the permutations of the string.
def perml(a, k, n):
	if k == n: print ''.join(a)
	else:
		for i in xrange(k, n):
			a[i], a[k] = a[k], a[i]
			perml(a, k+1, n)
			a[i], a[k] = a[k], a[i]

a = '123'

perml(list(a), 0, len(a))