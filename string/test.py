def prefix_table(pat):
	pat_len = 0
	lps = [0]
	i = 1
	while i < len(pat):
		if pat[pat_len] == pat[i]:
			i = i + 1
			pat_len = pat_len + 1
			lps.append(pat_len)
		else:
			if pat_len != 0:
				pat_len = lps[pat_len-1]
			else:
				i = i+1
				lps.append(0)

	return lps


def find(pat, a):
	lps = prefix_table(pat)
	i = 0
	j = 0

    
	while i < len(a):
	  if pat[j] == a[i]:
	    i = i+1
	    j = j+1
	  if j == len(lps)-1:
	     print 'pattern found at %s' % (i-j)
	     j = lps[j-1]
	  elif:
	    if j != 0:
	      j = lps[j-1]
	    else:
	      i = i+1 
