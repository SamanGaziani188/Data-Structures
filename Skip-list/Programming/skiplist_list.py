### Release Notes on Updates
# Last Updated By: Emad Bin Abid on February 5, 2018

## History:
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
        self.Height = height+1
    
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
        
class SkiplistList:
    def __init__(self, limit=100):
        '''Initializes sentinel, height limit, and size.
        '''
        self.heightlimit = limit
        self.sentinel = Skipnode(None,0)
        self.size = 0
        self.Height = 1
        
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        string = []
        for i in range (self.Height):
            Level = []
            reference = self.sentinel
            #print(reference.front)
            while reference.front[i] != None:
                Level.append((reference.Data,reference.front[i][1]))
                reference = reference.front[i][0]
            Level.append((reference.Data,None))
            string.append(Level)
        return str(string)
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
        
    def height(self):
        '''Returns the height of the skiplist.
        '''
        return self.Height()
        
    def get(self, i):
        '''Returns the element at index i; None if i is inavlid.

        i \in [0,n-1]
        '''
        if i > self.size-1 or i<0:
            return None
        pointer = self.sentinel
        currentLevel = self.Height-1
        index = i+1
        while index > 0:
            if pointer.front[currentLevel] != None:
                if pointer.front[currentLevel][1] <= index:
                    index = index - pointer.front[currentLevel][1] 
                    pointer=pointer.front[currentLevel][0]
                else:
                    currentLevel = currentLevel - 1
            else:
                currentLevel = currentLevel - 1
        return pointer.Data
    
    def set(self, i, x):
        '''Sets the element at valid index i to x and returns the old
        element. Returns None if i is inavlid.

        i \in [0,n-1]
        '''
        if i > self.size-1 or i<0:
            return None
        pointer = self.sentinel
        currentLevel = self.Height-1
        index = i+1
        while index > 0:
            if pointer.front[currentLevel] != None:
                if pointer.front[currentLevel][1] <= index:
                    index = index - pointer.front[currentLevel][1] 
                    pointer=pointer.front[currentLevel][0]
                else:
                    currentLevel = currentLevel - 1
            else:
                currentLevel = currentLevel - 1
        old = pointer.Data
        pointer.Data = x
        return old
    
    def add(self, i, x):
        '''Adds x at valid index i, shifting subsequent elements to the
        right, and returns True. Returns False if i is invalid.

        i \in [0,n]
        '''
        if i > self.size or i <0:
            return False
        randnum = randint(0,self.heightlimit)
        newNode = Skipnode(x,randnum)
        if i ==0 and self.size == 0:
            self.sentinel.add_levels(randnum)
            self.Height = self.Height+randnum
            for j in range (randnum+1):
                self.sentinel.front[j] = [newNode,1]
            self.size = self.size+1
            return True
        if randnum >= self.Height:
            self.sentinel.add_levels(randnum-self.Height+1)
            for k in range(randnum-self.Height+1):
                self.sentinel.front[randnum-k] = [newNode,i+1]
        pointer = self.sentinel
        index = i
        for k in range (self.Height):
            Nodeadded = False
            currentLevel = self.Height-k-1
            while pointer.front[currentLevel] != None and pointer.front[currentLevel][1] <= index and index != 0:
                index = index - pointer.front[currentLevel][1]
                pointer = pointer.front[currentLevel][0]
            if currentLevel <= randnum:
                newNode.front[currentLevel] = pointer.front[currentLevel]
                pointer.front[currentLevel] = [newNode, index+1] 
                Nodeadded = True
                if newNode.front[currentLevel] != None:
                    newNode.front[currentLevel][1] = newNode.front[currentLevel][1] - index  
            if pointer.front[currentLevel] != None and Nodeadded == False:
                pointer.front[currentLevel][1] += 1    
        self.size = self.size +1
        if randnum>= self.Height:
            self.Height = len(self.sentinel.front)
        return True
    
    def remove(self, i):
        '''Removes the element at valid index i, shifting subsequent
        elements to the left, and returns the remove elements. Returns 
        None if i is invalid.

        i \in [0,n-1]
        '''
        if i > self.size or i <0:
            return False
        pointer = self.sentinel
        index = i
        for k in range (self.Height):
            currentLevel = self.Height-k-1
            while pointer.front[currentLevel] != None and pointer.front[currentLevel][1] <= index:
                index = index - pointer.front[currentLevel][1]
                pointer = pointer.front[currentLevel][0]
            if pointer.front[currentLevel] != None and pointer.front[currentLevel][1] == 1:
                pointer1 = pointer.front[currentLevel][0]
                pointer1.front[currentLevel] = None
                if pointer1.front[currentLevel] != None:
                    pointer.front[currentLevel][1] = pointer.front[currentLevel][1] + pointer1.front[currentLevel][1] - 1
                    pointer.front[currentLevel][0] = pointer1.front[currentLevel][0]
            if pointer.front[currentLevel] != None and pointer.front[currentLevel][1] > 1:
                pointer.front[currentLevel][1] = pointer.front[currentLevel][1] - 1
        self.size = self.size - 1
        return pointer1.Data

##            while pointer.front[currentLevel] != None and pointer.front[currentLevel][1] <= index:
##                index = index - pointer.front[currentLevel][1]
##                pointer = pointer.front[currentLevel][0]
##            if pointer.front[currentLevel] != None:
##                if pointer.front[currentLevel][1] == index:
##                    Answer = pointer.front[currentLevel][0].Data
##                    if pointer.front[currentLevel][0].front[currentLevel] != None:
##                        pointer.front[currentLevel][1] = pointer.front[currentLevel][1]+ pointer.front[currentLevel][0].front[currentLevel][1]-1
##                    else:
##                        pointer.front[currentLevel][1] = None
##                    pointer.front[currentLevel][0] = pointer.front[currentLevel][0].front[currentLevel][0]
##                else:
##                    pointer.front[currentLevel][1] = pointer.front[currentLevel][1] - 1
##        pointer = self.sentinel
##        while self.sentinel.front[self.Height-1] == None:
##            self.sentinel.front.pop()
##            self.Height = self.Height - 1
##        return Answer
##                
                
##            if currentLevel <= randnum:
##                newNode.front[currentLevel] = pointer.front[currentLevel]
##                pointer.front[currentLevel] = [newNode, index+1] 
##                if newNode.front[currentLevel] != None:
##                    newNode.front[currentLevel][1] = newNode.front[currentLevel][1] - index  
##            if pointer.front[currentLevel] != None and Nodeadded == False:
##                pointer.front[currentLevel][1] += 1
        

    def truncate(self, i):
        # As described in Exercise 4.11
        pass

    def absorb(self, l2):
        # As described in Exercise 4.12
        pass

skiplist = SkiplistList(10)
print(skiplist.add(0,1))
print(skiplist.add(1,2))
print(skiplist.add(2,3))
print(skiplist.add(0,4))
print(skiplist.add(2,5))
print(skiplist.get(2))
print(skiplist.set(2,78))
print(skiplist.get(2))
print(skiplist)
print(skiplist.remove(0))
print(skiplist)
