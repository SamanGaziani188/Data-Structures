from skiplist_list import SkiplistList

def test_add():
    skiplist = SkiplistList()
    assert skiplist.add(0, 10) == True
    assert skiplist.add(1, 20) == True
    assert skiplist.add(1, 15) == True
    assert skiplist.add(4, 40) == False
    assert skiplist.add(5, 40) == False

def test_get():
    skiplist = SkiplistList()
    assert skiplist.add(0, 10) == True
    assert skiplist.add(1, 20) == True
    assert skiplist.add(1, 15) == True
    assert skiplist.add(4, 40) == False
    assert skiplist.add(5, 40) == False
    
    assert skiplist.get(0) == 10
    assert skiplist.get(1) == 15
    assert skiplist.get(2) == 20
    assert skiplist.get(4) == None

    

def test_set():
    skiplist= SkiplistList()
    assert skiplist.add(0, 10) == True
    assert skiplist.add(1, 20) == True
    assert skiplist.add(2, 10) == True
    assert skiplist.add(3, 40) == True
    assert skiplist.add(1, 40) == True
    
    assert skiplist.set(0, 11) == 10
    assert skiplist.get(0) == 11
    assert skiplist.set(2, 22) == 20
    assert skiplist.get(2)== 22
    assert skiplist.set(3, 44) == 10
    assert skiplist.get(3)== 44
    assert skiplist.set(2, 25) == 22
    assert skiplist.get(2) == 25
    
def test_remove():
    skiplist= SkiplistList()
    assert skiplist.remove(0) == None
    skiplist.add(0, 10)
    skiplist.add(1, 20)
    skiplist.add(2, 100)
    skiplist.add(3, 40)
    
    assert skiplist.remove(1)==20
    assert skiplist.remove(0)==10
    assert skiplist.remove(1)==40
    
def test_truncate():
    skiplist = SkiplistList()
    a=["abcdefghi","ct is awesome"]
    for i,x in enumerate(a[0]):
        skiplist.add(i,x)
    skiplist.truncate(5)
    assert skiplist.get(0) == 'a'
    assert skiplist.get(4) == 'e'
    for i in range(5):
        skiplist.get(i) == a[0][i]
    skiplist = SkiplistList()
    for i,x in enumerate(a[1]):
        skiplist.add(i,x)
    skiplist.truncate(7)
    assert skiplist.get(0) == 'c'
    assert skiplist.get(6) == 'a'
    for i in range(7):
        skiplist.get(i) == a[1][i]

def test_absorb():
    skiplist = SkiplistList()
    skiplist2 = SkiplistList()
    skiplist3 = SkiplistList()
    a=["Alice","Bob","Eve"]
    for i,x in enumerate(a[0]):
        skiplist.add(i,x)
    for i,x in enumerate(a[1]):
        skiplist2.add(i,x)
    for i,x in enumerate(a[2]):
        skiplist3.add(i,x)
    skiplist2.absorb(skiplist3)
    x=a[1]+a[2]
    for i in range(len(x)):
        assert skiplist2.get(i) == x[i]
    y=a[0]+x
    skiplist.absorb(skiplist2)
    for i in range(len(y)):
        assert skiplist.get(i) == y[i]
    assert skiplist.get(len(y)-2) == 'v'
