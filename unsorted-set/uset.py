### Release Notes on Updates
# Last Updated By: Emad Bin Abid on January 17, 2018

## History
# Updated By: Saman Gaziani on January 16, 2018
# Updated By: Emad Bin Abid on January 14, 2018

###
class USet:
    def __init__(self):
        '''Initializes member variables.
        '''
        self.usetList = list()

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''

        return "'{}'".format(self.usetList)

    def add(self, key, val):
        '''Adds the pair (key, val) to the USet if no pair with key
        already exists in the USet, and returns True. Returns False if a
        pair with key already exists in the USet.
        '''

        for keys in range(0, len(self.usetList)):
            if(self.usetList[keys][0] == key):
                return False

        self.usetList.append((key, val))
        return True


    def remove(self, key):
        '''Removes the pair with key from the USet and returns it.
        Returns None if no such pair exsits.
        '''

        for keys in range (0, len(self.usetList)):
            if(self.usetList[keys][0] == key):
                return self.usetList.pop(keys)

        return None


    def find(self, key):
        '''Returns the pair from the USet that contains key; None if no
        such pair exists.
        '''

        for keys in range (0, len(self.usetList)):
            if(self.usetList[keys][0] == key):
                return self.usetList[keys]

        return None

    def size(self):
        '''Returns the number of pairs currently in the USet.
        '''

        return len(self.usetList)

    def keys(self):
        '''Returns a list of keys in the USet.
        '''

        keyList = list()
        for keys in range (0, len(self.usetList)):
            keyList.append(self.usetList[keys][0])

        return keyList
