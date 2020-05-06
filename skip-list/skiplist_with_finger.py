from skiplist import Skiplist

# As defined in Exercise 4.10
class SkiplistWithFinger(Skiplist):
    def __init__(self, limit=100):
        Skiplist.__init__(self, limit)
        self.stack = list()             # a list of tuples

    def find(self,x):
        searchStack = self.stack
        if len(searchStack) != 0: 
            (Node,Height) = searchStack.pop()
            if Node.data != None and Node.data >= x:
                while Node.data != None and Node.data >= x and len(searchStack) != 0:
                    (Node,Height) = searchStack.pop()
            if Node.data != None and Node.data < x :
                if (Node.data == searchStack[-1][0].data):
                    searchStack.pop()
                searchStack.append((Node,len(Node.front)-1))
        Answer = self.find_predfinger(searchStack,x)
        if Answer[0].front[0] != None:
            self.stack = Answer[1]
            return Answer[0].front[0].data
        else:
            return None
                
                
    def find_predfinger(self,searchStack,x):
        
            stack = searchStack
            if len(stack) == 0:
                u = self.sentinel
                height = self.Height
                stack.append((u,height))
            else:
                (u,height) = searchStack.pop()
            for i in range(height):
                #print(u.front[self.Height-1-i].Data)
                while(u.front[height-1-i]== None or u.front[height-1-i].data < x ):
                    if u.front[height-1-i] == None:
                        ans = u
                        stack.append((ans,height-1-i))
                        break
                    else:
                        u = u.front[height-i-1]
                if u.front[height-1-i]!= None and u.front[height-1-i].data >= x :
                    ans = u
                    stack.append((ans,height-1-i))                
            return (ans,stack)

f_sklist = SkiplistWithFinger()
f_sklist.add(1)
f_sklist.add(2)
f_sklist.add(3)
print(f_sklist.find(1))
print(f_sklist.find(0))
print(f_sklist.find(2))
print(f_sklist.find(10))
print(f_sklist.find(1.5))
