import sys


for item in sys.argv:
  print item


name = raw_input('what is your name?')

print 'your name is %s' % name

for i in name:
	print i
