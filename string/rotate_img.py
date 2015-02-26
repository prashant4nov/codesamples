# http://www.geeksforgeeks.org/turn-an-image-by-90-degree/
def rotate_img(img, m, n):
	img_new = [x[:]for x in img]
	for i in xrange(0, m):
		for j in xrange(0, n):
			img_new[j][m-i-1] = img[i][j]
	
	print img_new


img = [[1,2],[3,4]]

rotate_img(img, 2, 2)