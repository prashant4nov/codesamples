class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)


def print_list(list):
	while list:
		print list.cargo,
		list = list.next
	print'______'

def del_all_occurances(key, list):

	if list.cargo == key:
		list = list.next 
		list.next = None

	head = list
	tail = list.next
	while tail.next != None and tail.cargo != key:
		head = tail
		tail = tail.next

	head.next = tail.next
	tail.next = None



# create Nodes.

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)
node7 = Node(7)


# create list.

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

import sys

print_list(node1)

del_all_occurances(2, node1)

print_list(node1)

