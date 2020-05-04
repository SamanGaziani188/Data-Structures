class DLNode:
    def __init__(self, data):
        self.data = data
        self.front = self.back = None

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return "'{}'".format(self.data) 

class DLList:
    def __init__(self):
        '''Initializes the dummy node and size.'''
        node = DLNode(None)
        self.dummy = node
        self.size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        strReturn = "["
        if self.size != 0:
            temp = self.dummy.front
            while(temp != self.dummy):
                strReturn = strReturn + str(temp) + ", "
                temp = temp.front

            strReturn = strReturn[0:len(strReturn)-2]
        strReturn = strReturn + "]"
        return strReturn

    def get(self, i):
        '''DL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i < -self.size or i>self.size:
            return None
        if i <0:
            if self.size+i > -i:
                node = self.dummy
                for j in range(-i):
                    node = node.back
                return node.data
            else:
                node = self.dummy.front
                for j in range(self.size+i):
                    node = node.front
                return node.data
        else:
            if self.size-i > i:
                node = self.dummy.front
                for j in range(i):
                    node = node.front
                return node.data
            else:
                node = self.dummy
                for j in range(self.size - i):
                    node = node.back
                return node.data
            

    def set(self, i, x):
        '''DL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i<-self.size or i>=self.size:
            return False
        if i <0:
            if self.size+i > -i:
                node = self.dummy
                for j in range(-i):
                    node = node.back
                node.data = x
                return True
            else:
                node = self.dummy.front
                for j in range(self.size+i):
                    node = node.front
                node.data = x
                return True
        else:
            if self.size-i > i:
                node = self.dummy.front
                for j in range(i):
                    node = node.front
                node.data = x
                return True
            else:
                node = self.dummy
                for j in range(self.size - i):
                    node = node.back
                node.data = x
                return True

    def add(self, i, x):
        '''DL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {-n, ... , n}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i<-self.size or i>self.size:
            return False
        if self.size == 0:
            node = DLNode(x)
            node.front = self.dummy
            node.back = self.dummy
            self.dummy.front = node
            self.dummy.back = node
            self.size = self.size+1
            return True
        if i <0:
            if self.size+i > -i:
                pointer = self.dummy.back
                for j in range(-i-1):
                    pointer = pointer.back
                node = DLNode(x)
                node.front = pointer.front
                node.back = pointer
                pointer.front = node
                node.front.back = node
                self.size = self.size + 1
                return True
            else:
                pointer = self.dummy.front
                for j in range(self.size+i):
                    pointer = pointer.front
                node = DLNode(x)
                node.front = pointer.front
                node.back = pointer
                pointer.front = node
                node.front.back = node
                self.size = self.size + 1
                return True
        else:
            if self.size-i > i:
                pointer = self.dummy
                for j in range(i):
                    pointer = pointer.front
                node = DLNode(x)
                node.front = pointer.front
                node.back = pointer
                pointer.front = node
                node.front.back = node
                self.size = self.size + 1
                return True
            else:
                pointer = self.dummy.back
                for j in range(self.size - i):
                    pointer = pointer.back
                node = DLNode(x)
                node.front = pointer.front
                node.back = pointer
                pointer.front = node
                node.front.back = node
                self.size = self.size+1
                return True
        

    def remove(self, i):
        '''DL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returs None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i<-self.size or i+1>self.size:
            return None
        if self.size == 1 and i == 1:
            answer = self.dummy.front.data
            self.dummy.front.back = None
            self.dummy.front.front = None
            self.dummy.front = None
            self.dummy.back = None
            self.size = self.size-1
            return answer
        if i <0:
            if self.size+i > -i:
                pointer = self.dummy
                for j in range(-i):
                    pointer = pointer.back
                pointer.front.back = pointer.back
                pointer.back.front = pointer.front
                pointer.back = None
                pointer.front = None
                self.size = self.size - 1
                return pointer.data
            else:
                pointer = self.dummy.front
                for j in range(self.size+i):
                    pointer = pointer.front
                pointer.back.front = pointer.front
                pointer.front.back = pointer.back
                pointer.front = None
                pointer.back = None
                self.size = self.size - 1
                return pointer.data
        else:
            if self.size-i > i:
                pointer = self.dummy
                for j in range(i+1):
                    pointer = pointer.front
                pointer.back.front = pointer.front
                pointer.front.back = pointer.back
                pointer.front = None
                pointer.back = None
                self.size = self.size - 1
                return pointer.data
            else:
                pointer = self.dummy
                for j in range(self.size - i):
                    pointer = pointer.back
                pointer.back.front = pointer.front
                pointer.front.back = pointer.back
                pointer.front = None
                pointer.back = None
                self.size = self.size - 1
                return pointer.data
            
    '''The next few methods involve performing manipulations on
    DLLists. You should complete them without allocating any new nodes
    or temporary arrays. They can all be done only by changing the
    value of front and back in existing nodes.
    '''
    
    def is_palindrome(self):
        '''As described in Exercise 3.7.
        '''
        pointer1 = self.dummy.back
        pointer2 = self.dummy.front
        if pointer1 != pointer2 or pointer1.back != pointer2 : 
            if pointer1.data != pointer2.data:
                return False
            else:
                pointer1 = pointer1.back
                pointer2 = pointer2.front
        return True
    
    def truncate(self,i):
        '''As described in Exercise 3.9.
        '''
        dllist = DLList()
        pointer = self.dummy
        if i == self.size:
            return dllist
        if self.size-i < i:
            dllist.dummy.back = self.dummy.back
            self.dummy.back.front = dllist.dummy
            for j in range(self.size-i):
                pointer = pointer.back
            dllist.dummy.front = pointer
            pointer.back.front = self.dummy
            self.dummy.back = pointer.back
            pointer.back = dllist.dummy    
        else:
            dllist.dummy.back = self.dummy.back
            self.dummy.back.front = dllist.dummy
            for j in range(i):
                pointer = pointer.front
            dllist.dummy.front = pointer.front
            pointer.front.back = dllist.dummy
            self.dummy.back = pointer
            pointer.front = self.dummy
        return dllist
            
    
    def absorb(self,dllist):
        '''As described in Exercise 3.10.
        '''
        self.dummy.back.front = dllist.dummy.front
        dllist.dummy.front.back = self.dummy.back
        self.dummy.back = dllist.dummy.back
        dllist.dummy.back.front = self.dummy
        dllist.dummy.front = None
        dllist.dummy.back = None
        self.size = self.size+dllist.size
        dllist.size = 0
        return self
        
    
    def reverse(self):
        '''As described in Exercise 3.12.

        Your code should run in O(n) time.
        '''
        pointer = self.dummy
        for i in range(self.size+1):
            print(pointer.data)
            (pointer.back, pointer.front) = (pointer.front, pointer.back)
            pointer = pointer.back
        return self
        
        

##dllist = DLList()
##dllist2 = DLList()
##dllist3 = DLList()
##a=["Alice","Bob","Eve"]
##for i,x in enumerate(a[0]):
##    dllist.add(i,x)
##for i,x in enumerate(a[1]):
##    dllist2.add(i,x)
##for i,x in enumerate(a[2]):
##    dllist3.add(i,x)
##
##dllist2.absorb(dllist3)
##
##print(dllist.get(-3))
##print(dllist2.get(-3))
##print(dllist3.get(-3))




##dllist1 = DLList()
##print(dllist1)
##print(dllist1.add(0,32))
##print(dllist1.add(1,23))
##print(dllist1.add(1,11))
##print(dllist1.add(3,42))
##print(dllist1.add(3,23))
##print(dllist1.add(-3,86))
##print(dllist1.size)
##print(dllist1)
##print(dllist1.reverse())
#print(dllist1.remove(-3))
#print(dllist1.remove(2))
#print(dllist1)
#print(dllist1.size)
#print(dllist1.is_palindrome())
#print(dllist1.truncate(5))

##dllist2 = DLList()
##print(dllist2)
##print(dllist2.add(0,13))
##print(dllist2.add(1,47))
##print(dllist2.add(1,53))
##print(dllist2.add(3,7))
##print(dllist2.add(3,48))
##print(dllist2.add(-3,8))
##print(dllist2.size)
##print(dllist2)
##
###print(dllist1.dummy.back)
##print(dllist1.absorb(dllist2))

##dllist = DLList()
##print(dllist.remove(0))
##dllist.add(0, 10)
##dllist.add(1, 20)
##dllist.add(2, 100)
##dllist.add(3, 40)
##print(dllist.remove(1))

##dllist= DLList()
##print(dllist.remove(0))
##dllist.add(0, 10)
##dllist.add(1, 20)
##dllist.add(2, 100)
##dllist.add(3, 40)
##print(dllist.remove(1))
##print(dllist.size)
##print(dllist.dummy.front.data)
##print(dllist.remove(0))
##print(dllist.dummy.front.data)
##print(dllist.size)
##print(dllist.remove(1))
