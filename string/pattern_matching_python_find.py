import re

print [m.start() for m in re.finditer('test', 'test test test test')]


def find_all(pat, txt):
	start = 0
	while True:
		start = txt.find(pat, start       )
		if start == -1:
			return
		yield start
		start += len(pat)


txt = 'test test test test'
pat = 'test'
print list(find_all(pat, txt))
