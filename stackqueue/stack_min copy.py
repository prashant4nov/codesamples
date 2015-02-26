class Stack():
	def __init__(self):
		self.top = -1
		self.stack = []

	def push(self, value):
		self.stack.append(value)
		self.top += 1

	def pop(self):
		if self.top > -1:
			self.stack.pop()
			self.top -= 1

	def print_it(self):
		print 'print_it'
		for n in self.stack:
			print n


class StackMin(Stack):
	def push(self, value):
		min_value = self.min(value)
		node = Node(value, min_value)
		#super(Stack, self).push(node)
		Stack.push(self, node)

	def min(self, value):
		min_value = value
		if self.top > -1 and value > self.stack[self.top].min:
			print 'min. value changed'
			min_value = self.stack[self.top].min
		print 'min. value not changed'
		return min_value


class Node:
	def __init__(self, value, min_value):
		self.min = min_value
		self.value = value

	def __str__(self):
		return str([self.value, self.min])


def main():
	done = False
	stack = StackMin()
	while not done:
		push = 'push'
		pop = 'pop'
		print_it = 'print'
		yes = 'yes'
		no = 'no'
		print 'push or pop or print?'
		value = input()
		value = value
		
		if value == push:
			print 'Enter element to push'
			value = input('enter value:')
			stack.push(value)
		elif value == pop:
			stack.pop()
		elif value == print_it:
			stack_it.print_it()

		stack.print_it()
		print 'done? yes/no :'
		value = input()
		if str(value) == yes:
			done = True
		elif str(value) == no:
			done = False



if __name__ == '__main__':
	main()

