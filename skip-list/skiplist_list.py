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
        if i >= self.size or i<0:
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
#the following code has been implemented on the given pseodocode in the reference book
    def remove(self, i):
        '''Removes the element at valid index i, shifting subsequent
        elements to the left, and returns the remove elements. Returns 
        None if i is invalid.

        i \in [0,n-1]
        '''
        if i >= self.size or i <0:
            return None
        pointer = self.sentinel
        height = self.Height-1
        counter = -1
        while height>= 0:
            while pointer.front[height] != None and counter + pointer.front[height][1] < i:
                counter = counter + pointer.front[height][1]
                pointer = pointer.front[height][0]
            if pointer.front[height] != None and counter+pointer.front[height][1] >= i: 
                pointer.front[height][1] = pointer.front[height][1] - 1
            if pointer.front[height] != None and counter + pointer.front[height][1] + 1 == i :
                Answer = pointer.front[height][0].Data
                if pointer.front[height][0].front[height] != None:
                    pointer.front[height][1] =  pointer.front[height][1] + pointer.front[height][0].front[height][1]
                    pointer.front[height][0] = pointer.front[height][0].front[height][0]
                else:
                    pointer.front[height] = None
            if pointer == self.sentinel and pointer.front[height] == None:
                self.Height = self.Height - 1
            
            height = height - 1
        self.size = self.size - 1
        return Answer
    

    def truncate(self, i):
        # As described in Exercise 4.11
        pointer = self.sentinel
        counter = -1
        height = self.Height-1
        returnSkipList = SkiplistList()
        while height >= 0:
            while pointer.front[height] != None and counter + pointer.front[height][1] <= i:
                #print("Next Node: ", pointer.front[height][0].Data)
                counter = counter + pointer.front[height][1]
                pointer = pointer.front[height][0]
            if pointer.front[height] != None:
                if returnSkipList.Height == 1:
                    returnSkipList.sentinel.add_levels(height)
                    returnSkipList.Height = height
                returnSkipList.sentinel.front[height] = [pointer.front[height][0],1]
                pointer.front[height] = None
            if pointer == self.sentinel and pointer.front[height] == None:
                self.Height = self.Height - 1
            height = height - 1
        returnSkipList.size = self.size - i
        self.size = i
        
        return returnSkipList
            
                
                
            

    def absorb(self, l2):
        # As described in Exercise 4.12
        pointer = self.sentinel
        if l2.Height > self.Height:
            self.sentinel.add_levels(l2.Height-self.Height)
            self.Height = len(self.sentinel.front)
            height = self.Height-1
        else:
            height = l2.Height - 1
        counter = 0
        #if l2 height is higher
        while height>= 0:
            #print("Height: " , height)
            while pointer.front[height] != None:
                counter = counter + pointer.front[height][1]
                pointer = pointer.front[height][0]
            pointer.front[height] = [l2.sentinel.front[height][0],(self.size - counter)+ l2.sentinel.front[height][1]]
            height = height-1
        self.size = self.size+l2.size
        return True
        
            
            

skiplist1 = SkiplistList(10)
print(skiplist1.add(0,1))
print(skiplist1.add(1,2))
print(skiplist1.add(2,3))
print(skiplist1.add(0,4))
print(skiplist1.add(2,5))
print(skiplist1)
print(skiplist1.remove(0))
print(skiplist1.remove(1))
print(skiplist1.remove(0))
print(skiplist1.remove(6))
print(skiplist1)
##skiplist2 = SkiplistList(13)
##print(skiplist2.add(0,7))
##print(skiplist2.add(1,4))
##print(skiplist2.add(2,19))
##print(skiplist2.add(0,35))
##print(skiplist2.add(2,56))
##print(skiplist2)
##print(skiplist1.absorb(skiplist2))
##print(skiplist1)

#print(skiplist1.truncate(2))
#print(skiplist1)


