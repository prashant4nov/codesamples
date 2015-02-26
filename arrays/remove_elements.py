#http://n00tc0d3r.blogspot.com/2013/05/remove-element-from-arraylist.html

#http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

#http://souravgarg.blogspot.com/p/facebook-intern.html
# http://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

def remove_all(a, el):
	s = 0
	e = len(a) -1 
	while s <= e:
		if a[s] == el:
			a[s], a[e] = a[e], a[s]
			#a[s] = a[e]
			e = e - 1
		else:
			s = s + 1
	return s,a

a=[1,2,3,4,5,6,3]

print remove_all(a,3)
