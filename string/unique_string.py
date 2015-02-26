def unique(txt):
	match = {}
	unique = True
	for i in xrange(0, len(txt)):
		if txt[i] in match.keys():
			unique = False
			break
		else:
			match[txt[i]] = i
	return unique

txt = 'abcdefg'

print unique(txt)
