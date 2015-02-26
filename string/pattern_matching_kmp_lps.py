def prefix_table(pat):
	i = 1
	j = 0
	lps = {}
	lps[0] = 0
	m = len(pat)
	while i < m:
		if pat[i] == pat[i]:
			lps[i] = j+1
			i += 1
			j += 1
		else:
			if j > 0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i += 1

	return lps


def find_match(pat, txt):
	lps = prefix_table(pat)
	m = len(pat)
	n = len(txt)
	i = 0
	j = 0
	while i < n:
		if txt[i] == pat[j]:
			i += 1
			j += 1
		if j == m-1:
			print 'pattern found at %d' % (i-j)
			j = lps[j-1]
		elif i < n and txt[i] != pat[j]:
			if j > 0:
				j = lps[j-1]
			else:
				i += 1


txt = 'this is a test text'
pat = 'is'

find_match(pat, txt)


