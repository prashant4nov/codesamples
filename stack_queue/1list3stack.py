class Stack:
	stack = []
	p = [0,1,2]
	def push(self, stack_no, value):
		self.stack.insert(self.p[stack_no-1], value)
		for x in xrange(stack_no-1, 3):
			self.p[stack_no-1] += 1

	def pop(self, stack_no):
		if self.p[stack_no-1] < 0:
			print 'stack empty!'
		else: 
			del self.stack[self.p[stack_no-1]]
			for x in xrange(stack_no-1, 3):
				self.p[stack_no-1] -= 1

	def print_stack(self):
		print self.stack
		print self.p


stack = Stack()

stack.push(1,1)
stack.push(2,2)
stack.push(2,2)

stack.print_stack()

stack.push(1,1)
stack.push(2,2)
stack.push(2,2)

stack.print_stack()

stack.pop(1)
stack.pop(2)
stack.pop(2)





