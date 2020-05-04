class MinDeque:
    '''As described in Exercise 3.16.'''

    def __init__(self):
        self.dequeList = list()
        self.Size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return "'{}'".format(self.dequeList)

    def add_first(self, x):
        '''Adds x at the front.
        '''
        if self.Size == 0: 
            self.dequeList.insert(0, (x,x))
        elif self.dequeList[0][1] > x :
            self.dequeList.insert(0, (x,x))
        else:
            self.dequeList.insert(0, (x,self.dequeList[0][1]))
        self.Size = self.Size + 1

    def add_last(self, x):
        '''Adds x at the back.
        '''
        if self.Size == 0: 
            self.dequeList.append((x,x))
        elif self.dequeList[-1][1] > x :
            self.dequeList.append((x,x))
        else:
            self.dequeList.append((x,self.dequeList[0][1]))
        self.Size = self.Size + 1

    def remove_first(self):
        '''Removes the element at the front and returns it. Returns None
        if dq is empty.
        '''
        if len(self.dequeList) == 0:
            return None
        else:
            self.Size = self.Size - 1
            return self.dequeList.pop(0)[0]
            

    def remove_last(self):
        '''Removes the element at the back and returns it. Returns None 
        if dq is empty.
        '''
        if len(self.dequeList) == 0:
            return None
        else:
            self.Size = self.Size - 1
            return self.dequeList.pop()[0]
            

    def size(self):
        '''Returns the number of elements currently in the dq.
        '''
        return self.Size

    def min(self):
        '''Returns the smallest element currently in the dq.
        '''
        if self.dequeList[-1][1] < self.dequeList[0][1]:
            return self.dequeList[-1][1]
        else:
            return self.dequeList[0][1]


