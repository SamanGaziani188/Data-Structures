from min_dq import MinDeque

def test_remove_first():
    dq = MinDeque()
    dq.add_first(10)
    dq.add_first(30)
    dq.add_first(40)
    assert dq.remove_first() == 40
    assert dq.remove_first() == 30
    assert dq.remove_first() == 10
    assert dq.remove_first() == None



def test_add_first():
    dq = MinDeque()
    dq.add_first(10)
    assert dq.remove_first() == 10
    dq.add_first(10)
    dq.add_first(30)
    dq.add_first(40)
    assert dq.remove_first() == 40
    assert dq.remove_first() == 30
    assert dq.remove_first() == 10
    assert dq.remove_first() == None

def test_add_remove():
    dq = MinDeque()
    dq.add_first(10)
    dq.add_last(20)
    dq.add_first(30)
    dq.add_last(60)
    dq.add_first(70)
    assert dq.remove_last() == 60
    assert dq.remove_last() == 20
    dq.add_last(50)
    assert dq.remove_first() == 70
    assert dq.remove_last() == 50
    assert dq.remove_first() == 30
    assert dq.remove_last() == 10
    assert dq.remove_first() == None
    assert dq.remove_last() == None

def test_size():
    dq = MinDeque()
    assert dq.size() == 0
    dq.add_first(10)
    assert dq.size() == 1
    dq.remove_first()
    assert dq.size() == 0
    dq.remove_last()
    assert dq.size() == 0
    dq.add_last(20)
    dq.add_first(30)
    assert dq.size() == 2
    dq.add_last(60)
    dq.add_first(70)
    assert dq.size() == 4
    dq.remove_last()
    assert dq.size() == 3
    dq.remove_first()
    assert dq.size() == 2
    dq.remove_first()
    assert dq.size() == 1
    dq.remove_first()
    assert dq.size() == 0
    dq.remove_first()
    dq.remove_last()
    assert dq.size() == 0

def test_min():
    dq = MinDeque()
    dq.add_first(50)
    assert dq.min() == 50
    dq.add_last(20)
    assert dq.min() == 20
    dq.add_first(40)
    assert dq.min() == 20
    dq.add_last(10)
    dq.add_first(30)
    assert dq.min() == 10
    dq.remove_last()
    assert dq.min() == 20
    dq.remove_last()
    assert dq.min() == 30
    dq.remove_first()
    assert dq.min() == 40
    dq.remove_first()
    assert dq.min() == 50