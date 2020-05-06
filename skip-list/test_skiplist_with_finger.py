from skiplist_with_finger import SkiplistWithFinger

def test_find():
    f_sklist = SkiplistWithFinger()
    f_sklist.add(1)
    f_sklist.add(2)
    f_sklist.add(3)
    assert f_sklist.find(1) == 1
    assert f_sklist.find(0) == 1
    assert f_sklist.find(2) == 2
    assert f_sklist.find(10) == None
    assert f_sklist.find(1.5) == 2
    assert f_sklist.find(3) == 3
    
