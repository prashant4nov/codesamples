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
            #el = self.s[top]
            #self.s.pop()
            self.top -= 1
            return self.s.pop()
        else:
            return 'stack is empty!'
  
    def peek(self):
        return self.s[self.top]
   
    def isEmpty(self):
        return self.s == []
   

def sort(s):
    r = Stack()
    while not s.isEmpty():
         tmp = s.pop()
         while not r.isEmpty() and r.peek() > tmp:
                s.push(r.pop())
         r.push(tmp)

    print s
    print r


def main():
 s = Stack()
 n = [34,452,23,64,33,53,6,1]
 for i in xrange(0,len(n)):
     s.push(n[i])
 sort(s)

if __name__ == '__main__':
    main()
