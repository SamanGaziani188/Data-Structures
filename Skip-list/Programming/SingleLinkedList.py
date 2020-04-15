### Release Notes on Updates
# Last Updated By: Emad Bin Abid on February 5, 2018

## History: 
# Updated By: Emad Bin Abid on February 4, 2018

## Creation: 
# Created by: Emad Bin Abid on Feb 05, 2018
###

# Python libraries


# Custom libraries


class Node:
    def __init__(self, data):
        self.data = data
        self.front = None

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return str(self.data)

class SingleLinkedList:
    def __init__(self, data, height):
        self.head = self.tail = None
        self.size = height

        ## Altered linked list starts...
        headNode = Node(data)
        self.head = headNode
        headNode.front = None

        temp = self.head
        for i in range(0, height-1):
            temp.front = Node(data)
            temp = temp.front
            temp.front = None

        self.tail = temp
        ## Altered linked list ends...

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        strReturn = "["
        temp = self.head
        while(temp != None):
            strReturn = strReturn + str(temp) + ", "
            temp = temp.front

        strReturn = strReturn[0:len(strReturn)-2]
        strReturn = strReturn + "]"
        return strReturn

    def get(self, i):
        '''SL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if(i > self.size - 1):
            return None
        temp = self.head
        for index in range(0, i):
            temp = temp.front
        return temp.data

    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if(i > self.size - 1):
            return False
        temp = self.head
        for index in range(0, i):
            temp = temp.front
        temp.data = x
        return True


##    def add(self, i, x):
##        '''SL.add(int, value) -> bool
##
##        Inserts x at index, i, and returns True.
##        Returns False if i \notin {0, ..., n}.
##
##        Runs in O(1+i) time.
##        '''
##        if(i > self.size):
##            return False
##
##        if(i == 0):
##            newNode = Node(x)
##            newNode.front = self.head
##            self.head = newNode
##        elif(i == self.size):
##            newNode = Node(x)
##            temp = self.head
##            for index in range(self.size - 1):
##                temp = temp.front
##            temp.front = newNode
##            self.tail = newNode
##            newNode.front = None
##        else:
##            newNode = Node(x)
##            temp = self.head
##            for index in range(i - 1):
##                temp = temp.front
##            newNode.front = temp.front
##            temp.front = newNode
##
##        self.size += 1
##        return True
##
##
##    def remove(self, i):
##        '''SL.remove(int) -> value
##
##        Removes the element at index, i, and returns it.
##        Returns None if i \notin {0, ..., n-1}.
##
##        Runs in O(1+i) time.
##        '''
##        if(i >= self.size):
##            return None
##
##        if(i == 0):
##            temp = self.head
##            self.head = self.head.front
##            temp.front = None
##            return temp.data
##        elif(i == self.size - 1):
##            temp = self.head
##            for index in range(0, self.size - 2):
##                temp = temp.front
##            value = temp.front.data
##            self.tail = temp
##            temp.front = None
##            return value
##        else:
##            temp = self.head
##            for index in range(0, i - 2):
##                temp = temp.front
##            value = temp.front.data
##            temp.front = temp.front.front
##            return value
##
##    def length(self):
##        return self.size

## Commented out because this linked list will be used as an underlying structure for a Skiplist which doesnot need these functions for its interface.
    
