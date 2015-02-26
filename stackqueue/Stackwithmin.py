import sys

class Stack(object):
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
        return self.s == []



class StackMin(Stack):

    def __init__(self):
        super(StackMin, self).__init__()
        self.s2 = Stack()

    def push(self, value):
        if value <= self.min():
            self.s2.push(value)

        super(StackMin, self).push(value)

    def pop(self):
        value = super(StackMin, self).pop()
        if value == self.min():
            self.s2.pop()

        return value

    def min(self):
        if self.s2.isEmpty():
            return sys.maxint
        else:
            return self.s2.peek()


def main():
 s = StackMin()
 n = [2,34,452,23,64,33,53,6,1]
 for i in xrange(0,len(n)):
     s.push(n[i])
 print s.min()
 s.pop()
 print s.min()
 s.pop()
 print s.min()
 

if __name__ == '__main__':
    main()
