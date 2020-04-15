### Release Notes on Updates
# Last Updated By:Saman Gaziani on February 17, 2018 

## History:
# Updated By:Saman Gaziani on February 6, 2018 
# Updated By: Emad Bin Abid on February 5, 2018
# Updated By: Emad Bin Abid on February 4, 2018

## Creation:
# Created by: Waqar Saleem, Syed Shariq Ali & Syeda Naeema Hasan on January 29, 2018
###


# Python libraries
from random import randint

# Custom libraries

class Skipnode:
    def __init__(self, data, height):
        '''Initializes node with data and (height+1) front pointers.
        '''
        self.Data = data
        self.front = list()
        for i in range(height+1):
            self.front.append(None)
        self.Height = height
    
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return "'{}'".format(self.Data)
        
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
    
    def height(self):
        '''Returns the height of this node.
        '''
        return self.Height

    def add_levels(self, n):
        '''Adds n front pointers.
        '''
        for i in range(n):
            self.front.append(None)
        self.Height= self.Height+n

class Skiplist:
    def __init__(self, limit=100):
        '''Initializes sentinel, height limit, and size.
        '''
        self.sentinel = Skipnode(None,0)
        self.heightlimit = limit
        self.size = 0
        self.Height = 0
        
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        string = ""
        reference = self.sentinel.front[0]
        #print(reference)
        while(reference != None):
            #print (aaa)
            string = string + str(reference.Data) + " "
            reference = reference.front[0]
        return string

##        String = '['
##        u = self.sentinel.front[0]
##        for i in range(self.size):
##            String = String + u.Data + ', '
##        String = String + ']'
##        return String
                
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
        
    def height(self):
        '''Returns the height of the skiplist.
        '''
        return self.Height
        
    def find_predecessor(self, x):
        '''Returns (predecessor_node, stack).
        '''
        u=self.sentinel
        ans = self.sentinel 
        stack = list()
        for i in range(self.Height):
            #print(u.front[self.Height-1-i].Data)
            while(u.front[self.Height-1-i]== None or u.front[self.Height-1-i].Data < x ):
                if u.front[self.Height-1-i] == None:
                    ans = u
                    #print("Ans1: ", ans)
                    stack.append((ans,self.Height-1-i))
                    break
                else:
                    #print("aaa")
                    u = u.front[self.Height-i-1]
                    #print(u.frontData)
            if u.front[self.Height-1-i]!= None and u.front[self.Height-1-i].Data >= x :
                ans = u
                #print(x,'aaa')
                #print(u.front[self.Height-1-i].Data)
                #print("x: " ,x)
                #print("Ans2: ", ans)
                stack.append((ans,self.Height-1-i))
##        print(ans,stack)                
        return (ans,stack)
    
    def find(self, x):
        '''Returns x, its successor, or None, in that order.
        '''
        Node = self.find_predecessor(x)[0]
        if Node.front[0] == None:
            return None
        return int(Node.front[0].Data)

    def add(self, x):
        '''Adds x to the skiplist and returns True; does not add and
        returns False if x is already an element.
        '''
        randnum = randint( 0, self.heightlimit)
        NewNode = Skipnode(x,randnum)
        #print("node: " ,(x,randnum))
        if self.size == 0:
            self.sentinel.add_levels(randnum+1)
            for i in range(randnum+1):
                self.sentinel.front[i] = NewNode
                #print(i)
            self.size = self.size + 1
            self.Height = randnum+1
            #print("size: " , self.size)
            #print("height: " , self.Height)
            return True                     #base case is correct and working
        Answer = self.find_predecessor(x)
        Node = Answer[0]
        Stack = Answer[1]
        #print("Stack: ", Stack)
        #print("Node: " , Node)
        if Node.front[0] != None and Node.front[0].Data == x:
            return False
        if randnum > self.Height:
            self.sentinel.add_levels(randnum-self.Height+1)
            for i in range(randnum-self.Height):
                self.sentinel.front[randnum-i] = NewNode
        count = 0
        while (len(Stack) != 0 and randnum+1 > count ):
                pointer = Stack.pop()
                NewNode.front[pointer[1]] = pointer[0].front[pointer[1]]
                pointer[0].front[pointer[1]] = NewNode
                #print()
                count=count+1
        self.size = self.size+1
        if randnum>= self.Height:
            self.Height = randnum+1
    
        #print("size: " ,self.size)
        #print("Height: ", self.Height)
        return True
 
    def remove(self, x):
        '''Removes x from the skiplist and returns True; does not remove
        and returns False if x is not an element.
        '''
        Answer = self.find_predecessor(x)
        Node = Answer[0]
        Stack = Answer[1]
        #print(Stack)
        #print(Node.height())
        if Node.front[0] == None or Node.front[0].Data != x:
            return False
        for i in range(len(Stack)-Node.height()):
            Stack.pop(0)
        #print (Stack)
        for i in range (len(Stack)):
            temp = Stack[len(Stack)-i-1][0]
            height = Stack[len(Stack)-i-1][1]
            if temp.front[height]== None:
                break
            #print(temp.front[height])
            temp.front[height] = temp.front[height].front[height]
        return True

##skiplist = Skiplist(10)
##print(skiplist)
##print(skiplist.add(5))
##print(skiplist.add(3))
##print(skiplist.add(4))
##print(skiplist.add(4))
##print(skiplist.add(4))
##print(skiplist.add(70))
##print(skiplist)
##print(skiplist.remove(55))
##print(skiplist.add(0.5))
###print(skiplist.remove(5))
##print(skiplist)
##print(skiplist.remove(65))
##print(skiplist)
####sklist = Skiplist()
####sklist.add(1)
####sklist.add(2)
####sklist.add(3)
####print(sklist)
####sklist.remove(2)
####print(sklist)
