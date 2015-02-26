class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.cargo)


tree = Tree(1, Tree(2, Tree(4)), Tree(3))

def total(tree):
	if tree is None: return 0
	return total(tree.left) + total(tree.right) + tree.cargo


print 'total: %d' % total(tree)