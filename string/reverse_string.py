def reverse(txt):
	n = len(txt)
	for i in xrange(0, n/2):
		txt[i], txt[-(i+1)] = txt[-(i+1)], txt[i]
	print ''.join(txt)

txt='abcd'

reverse(list(txt))