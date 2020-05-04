### Release Notes on Updates
# Last Updated By: Emad Bin Abid on January 17, 2018

## History
# Updated By: Saman Gaziani on January 16, 2018
# Updated By: Emad Bin Abid on January 14, 2018

###

class SSet:
    def __init__(self):
        '''Initializes member variables.
        '''

        self.ssetList = list()

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''

        return "'{}'".format(self.usetList)

    def add(self, key, val):
        '''Adds the pair (key, val) to the SSet if no pair with key
        already exists in the SSet, and returns True. Returns False if a
        pair with key already exists in the SSet.
        '''

        for keys in range(0, len(self.ssetList)):
            if (self.ssetList[keys][0] == key):
                return False
        self.ssetList.append((key, val))
        return True

    def remove(self, key):
        '''Removes the pair with key from the SSet and returns it.
        Returns None if no such pair exsits.

        '''

        for keys in range(0, len(self.ssetList)):
            if (self.ssetList[keys][0] == key):
                return self.ssetList.pop(keys)

        return None

    def find(self, key):
        '''Returns the pair from the SSet that contains key. If no such
        pair exists, returns the pair from the SSet that contains the
        successor of key. Returns None if no such pair exists.
        '''

        listOfMax = list()
        for keys in range (0, len(self.ssetList)):
            if(self.ssetList[keys][0] == key):
                return self.ssetList[keys]

            if(self.ssetList[keys][0] > key):
                listOfMax.append(self.ssetList[keys][0])

        if(listOfMax == []):
            return None
        else:
            return self.find(min(listOfMax))


    def size(self):
        '''Returns the number of pairs currently in the SSet.
        '''

        return len(self.ssetList)

    def keys(self):
        '''Returns a list of keys in the SSet.
        '''

        keyList = list()
        for keys in range(0, len(self.ssetList)):
            keyList.append(self.ssetList[keys][0])

        return keyList
