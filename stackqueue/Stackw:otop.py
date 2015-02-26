class Stack:
	def __init__(self):
		self.s = []

	def push(self, value):
		self.s.append(value)

	def pop(self):
		if not self.isEmpty():
			return self.s.pop()
		else:
			return 'Stack empty!'

	def isEmpty(self):
		return self.s == []

	def peek(self):
		return self.s[-1]
		