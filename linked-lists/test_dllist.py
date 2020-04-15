from dl_list import DLList

def test_add_get():
    dllist = DLList()
    assert dllist.add(0, 10) == True
    assert dllist.add(1, 20) == True
    assert dllist.add(1, 15) == True
    assert dllist.add(4, 40) == False
    assert dllist.add(-1, 40) == True
    assert dllist.add(-5, 40) == False
    assert dllist.get(0) == 10
    assert dllist.get(1) == 15
    assert dllist.get(2) == 20
    assert dllist.get(-1) == 40

def test_add_front_back():
    dllist = DLList()
    assert dllist.add(0, 100) == True
    assert dllist.add(1, 200) == True
    assert dllist.add(2, 150) == True

    assert dllist.dummy.front.data == 100
    assert dllist.dummy.back.data == 150
    assert dllist.add(1, 333) == True
    x=dllist.dummy.front.front
    assert x.back.data == 100
    assert x.front.data == 200

    
def test_add_head_tail():
    dllist = DLList()
    assert dllist.add(0, 100) == True
    assert dllist.size == 1
    assert dllist.add(1, 200) == True
    assert dllist.add(2, 150) == True
    assert dllist.dummy.front.data == 100
    assert dllist.add(0, 250) == True
    assert dllist.dummy.front.data == 250
    assert dllist.dummy.back.data == 150
    assert dllist.size == 4
    assert dllist.get(0) == 250
    assert dllist.get(1) == 100

def test_set():
    dllist= DLList()
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 10)
    dllist.add(3, 40)
    assert dllist.add(-1, 40) == True
    assert dllist.set(0, 11) == True
    assert dllist.get(0) == 11
    assert dllist.set(2, 22) == True
    assert dllist.get(2)== 22
    assert dllist.set(3, 44) == True
    assert dllist.get(3)== 44
    assert dllist.set(-2, 25) == True
    assert dllist.get(-2) == 25
    assert dllist.dummy.back.data == 40
    
def test_remove():
    dllist= DLList()
    assert dllist.remove(0) == None
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 100)
    dllist.add(3, 40)
    assert dllist.remove(1) ==20
    assert dllist.size == 3
    assert dllist.dummy.front.data == 10
    assert dllist.remove(0) ==10
    assert dllist.dummy.front.data == 100
    assert dllist.size == 2
    assert dllist.remove(1) ==40
    assert dllist.dummy.back.data == 100
    assert dllist.size == 1

def test_remove_front_back():
    dllist = DLList()
    dllist.add(0, 100)
    dllist.remove(0) == 100
    dllist.remove(1) == None
    dllist.add(0, 200)
    dllist.add(1, 150)
    dllist.add(2, 300)
    
    assert dllist.remove(0) == 200
    x = dllist.dummy.front.front
    assert x.back.data == 150
    assert x.data == 300

    
def test_remove_head_tail():
    dllist = DLList()
    dllist.add(0, 10)
    dllist.add(1, 20)
    dllist.add(2, 100)
    dllist.add(3, 40)

    assert dllist.remove(0) == 10
    assert dllist.dummy.front.data == 20
    assert dllist.dummy.back.data == 40
    assert dllist.size == 3
    assert dllist.get(0) == 20
    assert dllist.get(1) == 100

def test_is_palindrome():
    dllist = DLList()
    a=["madam","discrete","())("]
    for i,x in enumerate(a[0]):
        dllist.add(i,x)
    assert dllist.is_palindrome()== True
    dllist = DLList()
    for i,x in enumerate(a[1]):
        dllist.add(i,x)
    assert dllist.is_palindrome()== False
    dllist = DLList()
    for i,x in enumerate(a[2]):
        dllist.add(i,x)
    assert dllist.is_palindrome()== True
    
def test_truncate():
    dllist = DLList()
    a=["abcdefghi","ct is awesome"]
    for i,x in enumerate(a[0]):
        dllist.add(i,x)
    dllist.truncate(5)
    assert dllist.get(0) == 'a'
    assert dllist.get(-1) == 'e'
    for i in range(5):
        dllist.get(i) == a[0][i]
    dllist = DLList()
    for i,x in enumerate(a[1]):
        dllist.add(i,x)
    dllist.truncate(7)
    assert dllist.get(0) == 'c'
    assert dllist.get(-1) == 'a'
    for i in range(7):
        dllist.get(i) == a[1][i]
    assert dllist.dummy.back.data == 'a'

def test_absorb():
    dllist = DLList()
    dllist2 = DLList()
    dllist3 = DLList()
    a=["Alice","Bob","Eve"]
    for i,x in enumerate(a[0]):
        dllist.add(i,x)
    for i,x in enumerate(a[1]):
        dllist2.add(i,x)
    for i,x in enumerate(a[2]):
        dllist3.add(i,x)
    dllist2.absorb(dllist3)
    x=a[1]+a[2]
    for i in range(len(x)):
        assert dllist2.get(i) == x[i]
    assert dllist2.dummy.back.data == 'e'
    y=a[0]+x
    dllist.absorb(dllist2)
    for i in range(len(y)):
        assert dllist.get(i) == y[i]
    assert dllist.get(-2) == 'v'
    

def test_reverse():
    dllist = DLList()
    a=["abcdefghi","programming is fun"]
    for i,x in enumerate(a[0]):
        dllist.add(i,x)
    dllist.reverse()
    assert dllist.get(1) == 'h'
    assert dllist.get(-2) == 'b'
    for i in range(len(a[0])):
        assert dllist.get(i) == a[0][-i-1]
    dllist = DLList()
    for i,x in enumerate(a[1]):
        dllist.add(i,x)
    dllist.reverse()
    assert dllist.get(0) == 'n'
    assert dllist.get(-1) == 'p'
    for i in range(len(a[1])):
        assert dllist.get(i) == a[1][-i-1]
