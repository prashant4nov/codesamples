class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)



def middle_element(list):
	head = list
	count = 0
	while list:
		count = count + 1
		if count%2 != 0 and count >= 3:
			head = head.next
		list = list.next
	print head


# create Nodes.

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)


# create list.

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7




# middle element is:
middle_element(node1)

