def replace_space(t):
	li = ''
	for i in xrange(0, len(t)):
		if t[i] == ' ':
			li = li + '%20'
		else:
			li = li + t[i]
	print ''.join(li)


replace_space('hi how are you?')
