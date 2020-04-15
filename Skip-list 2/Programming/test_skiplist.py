from skiplist import Skiplist

def test_add():
    sklist = Skiplist()
    assert sklist.add(10) == True
    assert sklist.add(20) == True
    assert sklist.add(10) == False

def test_remove():
    sklist = Skiplist()
    sklist.add(1)
    sklist.add(2)
    assert sklist.remove(1) == True
    assert sklist.remove(1) == False
    assert sklist.remove(2) == True
    
def test_find():
    sklist = Skiplist()
    sklist.add(1)
    sklist.add(2)
    sklist.add(3)
    assert sklist.find(1) == 1
    assert sklist.find(0) == 1
    assert sklist.find(2) == 2
    assert sklist.find(10) == None
    assert sklist.find(1.5) == 2
    assert sklist.find(3) == 3
    
def test_find_predecessor():
    sklist = Skiplist()
    sklist.add(1)
    sklist.add(2)
    sklist.add(3)
    sklist.add(4)
    sklist.add(5)
    assert sklist.find_predecessor(6)[0].data == 5
    assert sklist.find_predecessor(4.5)[0].data == 4
    assert sklist.find_predecessor(2.9)[0].data == 2
    assert sklist.find_predecessor(1.1)[0].data == 1
    assert sklist.find_predecessor(0.9)[0].data == None
    
    


    
    
    
