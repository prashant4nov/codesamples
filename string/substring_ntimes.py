'''
http://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/
'''
def find_substring(txt):
	n = len(txt)
	lps_len = get_lps_len(txt)

	if lps_len > 0 and n % (n-lps_len) == 0:
		print True
		print 'substring is %s' % txt[0:n-lps_len]
		print 'repeated %s times.' % str(n/(n-lps_len))
	else:
		print False


def get_lps_len(txt):
	m = len(txt)
	i = 1
	j = 0
	lps = [0]
	while i < m:
		if txt[i] == txt[j]:
			lps.append(j+1)
			i += 1
			j += 1
		else:
			if j == 0:
				lps.append(0)
				i += 1
			else:
				j = lps[j-1]

	return lps[m-1]


txt = ['abcabc', 'ababab', 'abcdabcd', 'geeksforgeeks', 'geekgeek', 'aaaacaaaac', 'abcdabc']

for t in txt:
	find_substring(t)