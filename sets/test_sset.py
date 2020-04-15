from sset import SSet

def test_add():
    sset = SSet()
    assert sset.add(1, 10) == True
    assert sset.add(2, 20) == True
    assert sset.add(1, 10) == False

def test_remove():
    sset = SSet()
    sset.add(1, 10)
    sset.add(2, 20)
    assert sset.remove(1) == (1,10)
    assert sset.remove(1) == None
    assert sset.remove(2) == (2,20)
    
def test_size():
    sset = SSet()
    assert sset.size() == 0
    sset.add(1, 10)
    assert sset.size() == 1
    sset.add(2, 20)
    assert sset.size() == 2
    sset.add(2, 20)
    assert sset.size() == 2
    sset.remove(10)
    assert sset.size() == 2

def test_keys():
    sset = SSet()
    assert sset.keys() == []
    sset.add(1, 10)
    assert sset.keys() == [1]
    sset.add(2, 20)
    assert sset.keys() == [1,2]
    sset.remove(2)
    assert sset.keys() == [1]
    sset.remove(1)
    assert sset.keys() == []

def test_find():
    sset = SSet()
    sset.add(1, 10)
    sset.add(2, 20)
    assert sset.find(1) == (1,10)
    assert sset.size() == 2
    assert sset.find(1) == (1,10)
    assert sset.size() == 2
    assert sset.find(2) == (2,20)
    assert sset.size() == 2
    assert sset.find(10) == None
    assert sset.size() == 2
    assert sset.find(1.5) == (2,20)
    assert sset.size() == 2
    
    
    
