def robin_karp(txt, pat, q):
	n = len(txt)
	m = len(pat)
	d = 256
	h = pow(d, m-1) % q
	p = 0
	t = 0
	j = 0
	i = 0
	for i in xrange(m):
		p = (d * p + int(pat[i])) % q
		t = (d * t + int(txt[i])) % q

	for i in xrange(0, n-m+1):
		print 'i = %d' % i
		if p == t:
			for j in xrange(0, m):
				if txt[i+j] != pat[j]:
					break
			if j == m-1:
				print 'pattern found at %d' % i

		if i < n-m:
			t = (d * (t - int(txt[i]) * h) + int(txt[i+m])) % q

		if t < 0:
			t = t + q


txt = '1234545674545'
pat = '45'
q = 11

robin_karp(txt, pat, q)


txt = 'this is test'
pat = 'is'
q = 11

robin_karp(txt, pat, q)

