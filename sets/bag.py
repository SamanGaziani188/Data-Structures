### Release Notes on Updates
# Last Updated By: Emad Bin Abid on January 18, 2018

## History
# Updated By: Saman Gaziani on January 17, 2018
# Updated By: Saman Gaziani on January 16, 2018
# Updated By: Emad Bin Abid on January 14, 2018

###

from uset import USet

# Adapted from Exercise 1.5 in the book.

class Bag:
    def __init__(self):
        '''Initializes member variables.
        '''

        self.uset = USet()  # this is the underlying data structure.

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''

        return str(self.uset)

    def add(self, key, val):
        '''Adds the pair (key, val) to the Bag.
        '''

        if(self.uset.find(key) == None):
            self.uset.add(key, [val])
        else:
            valList = self.uset.find(key)[1]
            valList.append(val)
            self.uset.remove(key)
            self.uset.add(key, valList)

    def remove(self, key):
        '''Removes a pair with key from the Bag and returns it.
        Returns None if no such pair exsits.
        '''

        if(self.uset.find(key) == None):
            return None

        valList = self.uset.find(key)[1]

        if(valList != []):
            returningTuple = (key, valList.pop())
            if(valList == []):
                self.uset.remove(key)
            return returningTuple
        else:
            self.uset.remove(key)


    def find(self, key):
        '''Returns a pair from the Bag that contains key; None if no
        such pair exists.
        '''

        if (self.uset.find(key) == None):
            return None

        valList = self.uset.find(key)[1]
        returningTuple = (key, valList[0])
        self.uset.add(key, valList)
        return returningTuple

    def find_all(self, key):
        '''Returns all pairs from the Bag that contains key; None if no
        such pair exists.
        '''

        if (self.uset.find(key) == None):
            return []

        listOfTuples = list()
        valList = self.uset.find(key)[1]

        for val in valList:
            listOfTuples.append((key, val))
        return listOfTuples

    def size(self):
        '''Returns the number of pairs currently in the Bag.
        '''

        keyList = self.uset.keys()
        usetSize = 0
        for key in keyList:
            usetSize = usetSize + len(self.uset.find(key)[1])

        return usetSize

    def keys(self):
        '''Returns a list of keys in the Bag.
        '''

        return sorted(self.uset.keys())


