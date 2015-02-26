arr = [3,4,4,5,6,4,2,4,4]


def maj_dict(a):
	match = {}
	output = []
	for i in xrange(0, len(a)):
		if a[i] in match.keys():
			match[a[i]] += 1
		else:
			match[a[i]] = 1

	for x in match.keys():
		if match[x] > len(a)/2:
			output.append(x)

	print output




def majorit_ele(arr):
	group = {}
	output = []
	for i in xrange(len(arr)):
		if arr[i] in group.keys():
			group[arr[i]].append(arr[i])
		else:
			group[arr[i]] = [arr[i]]

	for i in group.keys():
		if len(group[i]) > len(arr)/2:
			output.extend(group[i])
	print output


#majorit_ele(arr)
maj_dict(arr)
