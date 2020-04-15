from uset import USet

def test_add():
    uset = USet()
    assert uset.add(1, 10) == True
    assert uset.add(2, 20) == True
    assert uset.add(1, 10) == False

def test_remove():
    uset = USet()
    uset.add(1, 10)
    uset.add(2, 20)
    assert uset.remove(1) == (1,10)
    assert uset.remove(1) == None
    assert uset.remove(2) == (2,20)
    
def test_size():
    uset = USet()
    assert uset.size() == 0
    uset.add(1, 10)
    assert uset.size() == 1
    uset.add(2, 20)
    assert uset.size() == 2
    uset.add(2, 20)
    assert uset.size() == 2
    uset.remove(10)
    assert uset.size() == 2

def test_keys():
    uset = USet()
    assert uset.keys() == []
    uset.add(1, 10)
    assert uset.keys() == [1]
    uset.add(2, 20)
    assert uset.keys() == [1,2]
    uset.remove(2)
    assert uset.keys() == [1]
    uset.remove(1)
    assert uset.keys() == []

def test_find():
    uset = USet()
    uset.add(1, 10)
    uset.add(2, 20)
    assert uset.find(1) == (1,10)
    assert uset.size() == 2
    assert uset.find(1) == (1,10)
    assert uset.size() == 2
    assert uset.find(2) == (2,20)
    assert uset.size() == 2
    assert uset.find(10) == None
    assert uset.size() == 2
    
    
    
