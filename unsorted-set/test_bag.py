from bag import Bag

def test_find_all():
    bag = Bag()
    bag.add(1, 10)
    bag.add(2, 20)
    bag.add(1, 10)
    bag.add(1, 20)
    pairs = bag.find_all(1)
    assert (1,10) in pairs
    assert pairs.count((1,10)) == 2
    assert bag.find_all(10) == []
    assert bag.find_all(2) == [(2,20)]

def test_find():
    bag = Bag()
    bag.add(1, 10)
    bag.add(2, 20)
    bag.add(1, 10)
    bag.add(1, 20)
    assert bag.find(1) in bag.find_all(1)
    assert bag.find(2) == (2, 20)
    assert bag.find(10) == None
    
def test_remove():
    bag = Bag()
    bag.add(1, 10)
    bag.add(2, 20)
    bag.add(1, 10)
    bag.add(1, 20)
    pairs = bag.find_all(1)
    assert bag.remove(1) in pairs
    assert len(bag.find_all(1)) == len(pairs) - 1
    assert bag.remove(2) == (2, 20)
    assert bag.remove(2) == None
    
def test_size():
    bag = Bag()
    assert bag.size() == 0
    bag.add(1, 10)
    assert bag.size() == 1
    bag.add(2, 20)
    assert bag.size() == 2
    bag.add(2, 20)
    assert bag.size() == 3
    bag.remove(10)
    assert bag.size() == 3
    bag.remove(1)
    assert bag.size() == 2

def test_keys():
    bag = Bag()
    assert bag.keys() == []
    bag.add(1, 10)
    assert bag.keys() == [1]
    bag.add(2, 20)
    assert bag.keys() == [1, 2]
    bag.add(1, 10)
    assert bag.keys() == [1, 2]
    bag.remove(1)
    assert bag.keys() == [1, 2]
    bag.remove(2)
    assert bag.keys() == [1]
    
    
    
