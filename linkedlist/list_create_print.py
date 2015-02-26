
class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)



def print_list(list):
	print 'print the list'
	while list:
		print list.cargo,
		list = list.next


#create 3 nodes.
node1 = Node('test1')
node2 = Node('test2')
node3 = Node('test3')


# linking the nodes to create the list.
node1.next = node2
node2.next = node3


# print the nodes
list = node1




print_list(list)