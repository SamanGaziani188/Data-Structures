class SLNode:
    def __init__(self, data):
        self.data = data
        self.front = None # can't use "next" - used by python.

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return "'{}'".format(self.data)

class SLList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

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
        if self.size > i:
            this = self.head
            for j in range(i):
                this = this.front
            return this.data
        else:
            return None

    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if self.size > i:
            this = self.head
            for j in range(i):
                this = this.front
            this.data = x
            return True
        else:
            return False
        

    def add(self, i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ..., n}.

        Runs in O(1+i) time.
        '''
        if self.size > i or self.size == i:
            if i == 0:
                node = SLNode(x)
                node.front = self.head
                self.head = node
                self.size = self.size+1
                if self.size == 0:
                    self.tail = node
                return True
            this = self.head
            for j in range(i-1):
                this = this.front
            node = SLNode(x)
            node.front = this.front
            this.front = node
            if node.front == None:
                self.tail = node
            self.size = self.size+1
            return True
        else:
            return False

    def remove(self, i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''
        if self.size > i or self.size == i:
            if i == 0:
                answer = self.head.data
                self.head= self.head.front
                self.size = self.size-1
                if self.size == 0:
                    self.tail = None
                return answer
            this = self.head
            for j in range(i-1):
                this = this.front
            answer = this.front.data
            this.front=this.front.front
            if this.front == None:
                self.tail = this
            self.size = self.size-1
            return answer
        else:
            return None
        

##linkedlist = SLList()
##print(linkedlist.add(0,5))
##print(linkedlist.add(1,4))
##print(linkedlist.add(1,3))
##print(linkedlist.add(0,7))
##print(linkedlist.add(1,89))
##print(linkedlist.add(5,56))
##print(linkedlist)
##print(linkedlist.set(3,123))
##print(linkedlist)
##print(linkedlist.get(9))
##print(linkedlist.remove(4))
##print(linkedlist)










