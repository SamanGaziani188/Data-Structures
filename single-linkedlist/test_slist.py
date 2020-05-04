from sl_list import SLList

def test_get():
    sllist = SLList()
    assert sllist.add(0, 10) == True
    assert sllist.add(1, 20) == True
    assert sllist.add(1, 15) == True
    assert sllist.get(0) == 10
    assert sllist.get(1) == 15
    assert sllist.get(2) == 20
    assert sllist.get(3) == None
    
def test_add():
    sllist = SLList()
    assert sllist.add(0, 100) == True
    assert sllist.add(1, 200) == True
    assert sllist.add(2, 150) == True
    assert sllist.head.data == 100
    assert sllist.add(0, 250) == True
    assert sllist.add(6, 300) == False
    assert sllist.head.data == 250
    assert sllist.tail.data == 150
    assert sllist.size == 4
    assert sllist.get(0) == 250
    assert sllist.get(1) == 100

def test_set():
    sllist= SLList()
    sllist.add(0, 10)
    sllist.add(1, 20)
    sllist.add(2, 10)
    sllist.add(3, 40)
    assert sllist.set(0, 11) == True
    assert sllist.get(0)==11
    assert sllist.set(2, 22) == True
    assert sllist.get(2)== 22
    assert sllist.set(3, 44) == True
    assert sllist.get(3)== 44
    
def test_remove():
    sllist= SLList()
    sllist.add(0, 10)
    sllist.add(1, 20)
    sllist.add(2, 100)
    sllist.add(3, 40)
    assert sllist.remove(1) == 20
    assert sllist.head.data == 10
    assert sllist.remove(0) == 10
    assert sllist.head.data == 100
    assert sllist.remove(1) == 40
    assert sllist.tail.data == 100
    
