class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.cargo)


tree = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3))

def inorder(tree):
	if tree is None: return
	inorder(tree.left)
	print '%d, ' % tree.cargo,
	inorder(tree.right)

def preorder(tree):
	if tree is None: return 
	print '%d, ' % tree.cargo,
	preorder(tree.left)
	preorder(tree.right)


def postorder(tree):
	if tree is None: return
	postorder(tree.left)
	postorder(tree.right)
	print '%d, ' % tree.cargo,


print 'inorder: ',
inorder(tree)

print '_'
print 'preorder: ',
preorder(tree)
print '_'

print 'postorder: ',
postorder(tree)