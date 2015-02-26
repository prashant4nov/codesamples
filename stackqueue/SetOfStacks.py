class Stack:
    def __init__(self):
        self.s = []
        self.top = -1
    
    def __str__(self):
    	return str(self.s)

    def push(self, n):
        self.s = self.s + [n]
        self.top += 1
  
    def pop(self):
        if self.top > -1:
            self.top -= 1
            return self.s.pop()
        else:
            return 'stack is empty!'
  
    def peek(self):
        return self.s[self.top]
  
    def isEmpty(self):
        return self.top == -1

    def items(self):
    	return self.top


class SetOfStacks:
	def __init__(self, capacity=3):
		if capacity < 1:
			raise Error('Stack of this capacity not possible!')
		else:
			self.capacity = capacity
			self.s = []

	def __str__(self):
		return str(self.s)

	def push(self, el):
		if self.s == [] or self.s[-1].items() == self.capacity-1:
			s1 = Stack()
			s1.push(el)
			self.s.append(s1)
		else:
			self.s[-1].push(el)

	def pop(self):
		if self.s == []:
			raise Error('Stack empty!')
		else:
			el = self.s[-1].peek()
			if self.s[-1].items() == 0:
				self.s.pop()
			else:
				self.s[-1].pop()
			return el

def main():
 s = SetOfStacks()
 n = [2,34,452,23,64,33,53,6,1,90]
 for i in xrange(0,len(n)):
 	s.push(n[i])

 print s
 print s.pop()
 print s
 print s.pop()
 print s
 print s.pop()
 print s
 print s.pop()
 print s
 s.push(100)
 print s


if __name__ == '__main__':
    main()

