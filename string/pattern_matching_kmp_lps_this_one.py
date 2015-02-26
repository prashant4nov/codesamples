'''
http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
Preprocessing Algorithm:
In the preprocessing part, we calculate values in lps[]. 
To do that, we keep track of the length of the longest prefix 
suffix value (we use len variable for this purpose) for the 
previous index. We initialize lps[0] and len as 0. If pat[len] 
and pat[i] match, we increment len by 1 and assign the incremented 
value to lps[i]. If pat[i] and pat[len] do not match and len is not 
0, we update len to lps[len-1]. See computeLPSArray () in the below 
code for details.
'''
def prefix_table(pat):
	i = 1
	pat_len = 0 # is the length
	lps = [0]
	
	while i < len(pat):
		if pat[pat_len] == pat[i]:
			pat_len += 1
			lps.append(pat_len)
			i += 1
		else:
			if pat_len != 0:
				pat_len = lps[pat_len-1] # this is tricky.
			else:
				lps.append(0)
				i += 1

	return lps


def find_match(pat, txt):
	m = len(pat)
	lps = prefix_table(pat)
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
		# mismatch after j matches.	
		elif i < n and txt[i] != pat[j]: #Do not match lps[0..lps[j-1]] characters, they will match anyway.
			if j > 0:
				j = lps[j-1]
			else:
				i += 1


txt = 'this is a test text'
pat = 'is'

find_match(pat, txt)

txt = '1223453 is a t467678est t12ext'
pat = '12'

find_match(pat, txt)


