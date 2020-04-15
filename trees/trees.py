### Release Notes on Updates
## History
# Updated By: Emad Bin Abid on January 23, 2018
# Created By: Waqar Saleem on March 23, 2018

import random



########## Nodes.
# Nodes to be used in trees.

class TreeNode:
    '''A node in a binary tree.'''
    def __init__(self, n):
        self.data = n
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    def num_children(self):
        '''N.num_children() -> int

        Returns the number of children of N that are not None.
        '''
        return sum([1 for child in [self.left, self.right] if child])

class TreapNode(TreeNode):
    '''A node in a treap.'''
    def __init__(self, data, priority):
        super().__init__(data)  # Parent constructor.
        self.priority = priority

    def __str__(self):
        return "({}, {})".format(self.data, self.priority)
        
class AvlNode(TreeNode):
    '''A node in an AVL tree.'''
    def __init__(self, data):
        super().__init__(data)  # Parent constructor.
        self.height = 0

    def __str__(self):
        return "({}, {})".format(self.data, self.height)

########## Trees. ##########
# Trees utilizing above nodes. Use helper functions defined outside
# the class to achieve functionality.

class Bst:
    '''A BST. Does not contain duplicates. Nodes are of type TreeNode.'''
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return tree_string(self.root)
    
    def __repr__(self):
        return self.__str__()
        
    def add(self, n):
        self.root, added = bst_add(self.root, n)
        if added:
            self.size += 1
        return added
    
    def find(self, n):
        return bst_find(self.root, n)
    
    def remove(self, n):
        self.root, removed = bst_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed

    def clear(self):
        self.__init__()
        
class Treap(Bst):
    '''A treap. Does not contain duplicates. Nodes are of type TreapNode.'''
    max_priority = 1 << 10
    def __init__(self):
        super().__init__()
        self.priorities = set()
        
    def add(self, n):
        priority = random.randint(0, Treap.max_priority)
        print(n,priority)
        while priority in self.priorities:
            priority = random.randint(0, Treap.max_priority)
        self.root, added = treap_add(self.root, n, priority)
        if added:
            self.size += 1
            self.priorities.add(priority)
        return added

    def remove(self, n):
        self.root, removed = treap_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed

class AvlTree(Bst):
    '''An AVL tree. Does not contain duplicates. Nodes are of type AvlNode.'''
    def __init__(self):
        super().__init__()
        
    def add(self, n):
        self.root, added = avl_add(self.root, n)
        if added:
            self.size += 1
        return added

    def remove(self, n):
        pass
        self.root, removed = avl_remove(self.root, n)
        if removed:
            self.size -= 1
        return removed
    
########## Tree helper functions. ##########
# Work for any type of node above.
    
def tree_string(node, level = 0):
    '''tree_string(node) -> str

    Returns a string representation of the subtree rooted at node.

    credit: https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    '''
    if not node:
        return '\n'
    prefix = '   '*level
    str = repr(node) + '\n'
    if node.num_children():
        str += prefix + '|_ ' + tree_string(node.left, level+1)
        str += prefix + '|_ ' + tree_string(node.right, level+1)
    return str
    
def tree_size(node):
    '''tree_size(node) -> int

    Returns a string representation of the subtree rooted at node.
    '''
    if node.left == None and node.right == None:
        return 1
    if node.left == None:
        return 1+tree_size(node.right)
    if node.right == None:
        return 1+tree_size(node.left)
    else:
        1+tree_size(node.left)+tree_size(node.right)

def tree_height(node):
    '''tree_height(node) -> int

    Returns the height of the subtree rooted at node. Returns -1 if
    node is None.

    A node's height is the value of its height attribute, if it
    exists. Otherwise it has to be computed.

    See
    - EAFP at https://docs.python.org/3.4/glossary.html
    - https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
    '''

    #code citation: stackoverflow
    if hasattr(node,'height'):
        return node.height
    if node == None:
        return -1
    Rheight = tree_height(node.right)
    Lheight = tree_height(node.left)
    if (Lheight > Rheight):
        return Lheight + 1
    else:
        return Rheight + 1
    

def inorder(n):
    '''inorder(node) -> [node content]

    Returns an inorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    if n != None:
        return inorder(n.left)+[str(n)]+inorder(n.right)
    else:
        return[]

def preorder(n):
    '''preorder(node) -> [node content]

    Returns an preorder traversal of the subtree rooted at node; empty
    list if n is None.
    '''
    if n != None:
        return [str(n)]+preorder(n.left)+preorder(n.right)
    else:
        return[]

def postorder(n):
    '''postorder(node) -> [node content]

    Returns an postorder traversal of the subtree rooted at node;
    empty list if0 n is None.
    '''
    if n != None:
        return postorder(n.left)+postorder(n.right)+[str(n)]
    else:
        return[]

def update_height(node):
    '''update_height(node) -> None

    Updates the value of node's height attribute using the height of
    its children.

    Assumes that node has a height attribute.
    '''
    node.height = 1 + max(tree_height(node.left),tree_height(node.right))
##    if node.right == None and node.left == None:
##        node.height = 0
##    elif node.right == None and node.left != None:
##        update_height(node.left)
##        node.height = 1+node.left.height
##    elif node.left == None and node.right != None:
##        update_height(node.right)
##        node.height = 1+node.right.height
##    else:
##        update_height(node.right)
##        update_height(node.left)
##        node.height = 1 + max(node.right.height,node.left.height)

def rotate_left(node):
    '''rotate_left(node) -> node

    Returns the root of the tree obtained by rotating node to the
    left. Updates the height attribute of nodes where necessary and if
    the attribute is present.
    '''

    if node.left == None:
        return node
    if node.left.right == None:
        (node,node.left) = (node.right,node)
        if hasattr(node,'height'):
            update_height(node)
        return node
    else:
        (node,node.left,node.left.right) = (node.right,node,node.right.left)
        if hasattr(node,'height'):
            update_height(node)
        return node

def rotate_right(node):
    '''rotate_right(node) -> node

    Returns the root of the tree obtained by rotating node to the
    right. Updates the height attribute of nodes where necessary and if
    the attribute is present.
    '''

    if node.right == None:
        return node
    if node.right.left == None:
        (node,node.right) = (node.left,node)
        if hasattr(node,'height'):
            update_height(node)
        return node
    else:
        (node,node.right,node.right.left) = (node.left,node,node.left.right)
        if hasattr(node,'height'):
            update_height(node)
        return node
    

########## BST helper functions. ##########

def bst_find(node, n):
    '''bst_find(node, int) -> bool

    Returns whether n is contained in the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.
    '''
    pointer = node
    if pointer == None:
        return False
    while((pointer.left != None or pointer.right != None) and pointer.data != n): 
        if n > pointer.data:
            if pointer.right == None:
                return False
            pointer = pointer.right
        elif n < pointer.data:
            if pointer.left == None:
                return False
            pointer = pointer.left
    if pointer.data != n:
        return False
    return True 

def bst_find_min(node):
    '''bst_find_min(node) -> int

    Returns the smallest value stored in the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.
    '''
    pointer = node
    while pointer.left != None:
        pointer = pointer.left
    return pointer.data

def bst_add(node, n):
    '''bst_add(node, int) -> (node, bool)

    Returns the result of adding n to the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the root of the tree obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.
    '''
    if node == None:
        root = TreeNode(n)
        return (root,True)
    pointer = node
    root = node
    while(pointer != None): 
        if n > pointer.data:
            if pointer.right == None:
                pointer.right = TreeNode(n)
                return (root,True)
            else:
                pointer = pointer.right
        elif n < pointer.data:
            if pointer.left == None:
                pointer.left = TreeNode(n)
                return (root,True)
            else:
                pointer = pointer.left
        else:
            return (root,False)
        

def bst_remove(node, n):
    '''bst_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree rooted at
    node. Assumes the subtree to be a BST with no duplicates.

    The first returned value is the root of the tree obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    '''
    if bst_find(node,n) == False:
        return (node,False)
    pointer = node
    prev = None
    root = node
    while(pointer.data != n): 
        if n > pointer.data:
            if pointer.right == None:
                return (root,False)
            prev = pointer
            pointer = pointer.right
        elif n < pointer.data:
            if pointer.left == None:
                return (root,False)
            prev = pointer
            pointer = pointer.left
    if pointer.data != n:
        return (root,False) 
    if pointer.right == None and pointer.left == None:
        if prev == None:
            root = None
        elif prev.right == pointer:
            prev.right = None
        else:
            prev.left = None
        return (root,True)
    if pointer.right != None and pointer.left == None:
        if prev == None:
            root = pointer.right
        elif prev.right == pointer:
            prev.right = pointer.right
        else:
            prev.left = pointer.right
        return (root,True)
    if pointer.right == None and pointer.left != None:
        if prev == None:
            root = pointer.left
        elif prev.right == pointer:
            prev.right = pointer.left
        else:
            prev.left = pointer.left
        return (root,True)
    else:
        a = bst_find_min(pointer.right)
        bst_remove(root,a)
        pointer.data = a
        return (root,True)
         

########## BST helper functions. ##########

def treap_add(node, n, p):
    '''treap_add(node, int, int) -> (node, bool)

    Returns the result of adding n with priority, p, to the subtree
    rooted at node. Assumes the subtree to be a treap with no
    duplicate values.

    The first returned value is the root of the treap obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.
    '''
    if bst_find(node,n) == True:
        return (node,False)
    if node == None:
        return (TreapNode(n,p),True)
    if (n <= node.data):
        node.left = treap_add(node.left,n,p)[0]
        if (node.left.priority < node.priority):
            node = rotate_right(node)
    else:
        node.right = treap_add(node.right,n,p)[0]
        if (node.right.priority < node.priority):
            node = rotate_left(node)
    return (node,True)

def treap_remove(node, n):
    '''treap_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree rooted at
    node. Assumes the subtree to be a treap with no duplicate values.

    The first returned value is the root of the treap obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    '''
    if bst_find(node,n) == False:
        return (node,False)
    pointer = node
    prev = None
    root = node
    while(pointer.data != n): 
        if n > pointer.data:
            if pointer.right == None:
                return (root,False)
            prev = pointer
            pointer = pointer.right
        elif n < pointer.data:
            if pointer.left == None:
                return (root,False)
            prev = pointer
            pointer = pointer.left
    if pointer.data != n:
        return (root,False) 
    if pointer.right == None and pointer.left == None:
        if prev == None:
            root = None
        elif prev.right == pointer:
            prev.right = None
        else:
            prev.left = None
        return (root,True)
    if pointer.right != None and pointer.left == None:
        if prev == None:
            root = pointer.right
        elif prev.right == pointer:
            prev.right = pointer.right
        else:
            prev.left = pointer.right
        return (root,True)
    if pointer.right == None and pointer.left != None:
        if prev == None:
            root = pointer.left
        elif prev.right == pointer:
            prev.right = pointer.left
        else:
            prev.left = pointer.left
        return (root,True)
    else:
        a = bst_find_min(pointer.right)
        treap_remove(root,a)
        pointer.data = a
        return (root,True)

########## AVL helper functions. ##########
        
def avl_balanced(node):
    '''avl_balanced(node) -> bool

    Returns whether the AVL property is satisfied at node. Should work
    for any of the nodes defined above.
    '''
    if (tree_height(node.right)-tree_height(node.left)) > 1 or tree_height(node.right)-tree_height(node.left) < -1:
        return False
    return True

def avl_left_left(node):
    '''avl_left_left(node) -> node
    
    Returns the root of the tree obtained by resolving a left-left
    case at node.
    '''
    node = rotate_right(node)
    return node

def avl_right_right(node):
    '''avl_right_right(node) -> node
    
    Returns the root of the tree obtained by resolving a right_right
    case at node.
    '''
    node = rotate_left(node)
    return node

def avl_left_right(node):
    '''avl_left_right(node) -> node
    
    Returns the root of the tree obtained by resolving a left_right
    case at node.
    '''
    node = rotate_left(node)
    node = rotate_right(node)
    return node

def avl_right_left(node):
    '''avl_right_left(node) -> node
    
    Returns the root of the tree obtained by resolving a right_left
    case at node.
    '''
    node = rotate_right(node)
    node = rotate_left(node)
    return node

def avl_add(node, n):
    '''avl_add(node, int) -> (node, bool)

    Returns the result of adding n to the subtree rooted at
    node. Assumes the subtree to be a valid AVL tree with no
    duplicates.

    The first returned value is the root of the AVL tree obtained as a
    result of the addition. The second value indicates whether
    addition succeeded. Addition fails if n is already present in the
    subtree.
    '''
    bool = True
    if node == None:
        node = AvlNode(n)
        print('xx')
        return (node,True)
    if node.data == n:
        update_height(node)
        print('yyy')
        return (node,False)
    elif n < node.data:
        (node.left, bool) = avl_add(node.left, n)
    else:
        (node.right, bool) = avl_add(node.right, n)
    if bool == True:
        balance = tree_height(node.left)-tree_height(node.right)
        if balance > 1 and n < node.left.data:
            node = avl_left_left(node)
        if balance < -1 and n > node.right.data:
            node = avl_right_right(node)
            #return (avl_right_right(node),True)
        if balance > 1 and n > node.left.data:
            node = avl_left_right(node)
            #return (avl_left_right(node),True)
        if balance < -1 and n < node.right.data:
            node = avl_right_left(node)
            #return (avl_right_left(node),True)
        update_height(node)   
    return (node,bool)

def avl_remove(node, n):
    '''avl_remove(node, int) -> (node, bool)

    Returns the result of removing n from the subtree rooted at
    node. Assumes the subtree to be a valid AVL tree with no
    duplicates.

    The first returned value is the root of the AVL tree obtained as a
    result of the removal. The second value indicates whether removal
    succeeded. Removal fails if n is not present in the subtree.
    '''
    if bst_find(node,n) == False:
        return (node,False)
    pointer = node
    prev = None
    root = node
    while(pointer.data != n): 
        if n > pointer.data:
            if pointer.right == None:
                update_height(root)
                return (root,False)
            prev = pointer
            pointer = pointer.right
        elif n < pointer.data:
            if pointer.left == None:
                update_height(root)
                return (root,False)
            prev = pointer
            pointer = pointer.left
    if pointer.data != n:
        update_height(root)
        return (root,False) 
    if pointer.right == None and pointer.left == None:
        if prev == None:
            root = None
        elif prev.right == pointer:
            prev.right = None
        else:
            prev.left = None
        update_height(root)
        return (root,True)
    if pointer.right != None and pointer.left == None:
        if prev == None:
            root = pointer.right
        elif prev.right == pointer:
            prev.right = pointer.right
        else:
            prev.left = pointer.right
        update_height(root)
        return (root,True)
    if pointer.right == None and pointer.left != None:
        if prev == None:
            root = pointer.left
        elif prev.right == pointer:
            prev.right = pointer.left
        else:
            prev.left = pointer.left
        update_height(root)
        return (root,True)
    else:
        a = bst_find_min(pointer.right)
        treap_remove(root,a)
        pointer.data = a
        update_height(root)
        return (root,True)


import timeit

def tree_find_time(tree, x):
    start_time = timeit.default_timer()
    if not tree.find(x):
        pass
    return (timeit.default_timer() - start_time)

def list_find_time(lst, x):
    start_time = timeit.default_timer()
    try:
        lst.index(x)
    except:
        pass
    return (timeit.default_timer() - start_time)

def get_trees(lst):
    trees = [Bst(), Treap(), AvlTree()]
    for x in lst:
        for t in trees:
            t.add(x)
    return trees

def compare_find(n=1000, repeat=3, number=1000):
    lst_times = []
    tree_times = [[], [], []]
    limit = 1<<30
    # Perform several repetitions. 
    for _ in range(repeat):
        # Generate structures.
        lst = random.sample(range(limit), n)
        trees = get_trees(lst)
        lst_time = 0
        tree_time = [0]*len(trees)
        # Accumulate total find time for each structure over a number of iterations.
        for _ in range(number):
            x = random.randint(0,limit)
            lst_time += list_find_time(lst, x)
            for i,t in enumerate(trees):
                tree_time[i] += tree_find_time(t, x)
        # Save the total time for each structure from this repetition.
        lst_times.append(lst_time)
        for i,times in enumerate(tree_times):
            times.append(tree_time[i])
    # Output the minimum time from all repetitions, as per best practice.
    times = [n,min(lst_times)] + [min(times) for times in tree_times]
    times = [str(num) for num in times]
    print('\t'.join(times))

import matplotlib.pyplot as plt
def plot_times(fname='times.txt'):
    n = []
    times = [[], [], [], []]
    for line in open(fname):
        nums = line.split()
        n.append(int(nums[0]))
        for i,t in enumerate(nums[1:]):
            times[i].append(float(t))
    labels = ['List', 'BST', 'Treap', 'AVL']
    colors = ['-r', '-b', '-g', '-y']
    fig, (a0,a1) = plt.subplots(2,1)
    for i,t in enumerate(times):
        a0.plot(n, t, colors[i], label=labels[i])
    for i,t in enumerate(times[1:]):
        a1.plot(n, t, colors[i+1], label=labels[i+1])
    for ax in (a0,a1):
        ax.set(xlabel='n',ylabel='Time (s)')
        ax.legend(loc='best')
        ax.grid()
    a0.set_title("Time for 1000 find()'s in structures of size n")
    a1.set_title('Above figure without list')
    fig.subplots_adjust(hspace=.5)
    fig.savefig(fname[:-3]+'png')
    plt.show()


##Test Cases##
def test_add():
    tree=Bst()
    assert tree.add(10)
    assert tree.root.data==10
    assert not tree.add(10)
    assert tree.add(20)
    assert tree.add(5)
    assert tree.add(30)
    assert tree.add(25)
    assert tree.add(55)
    assert tree.add(2)
    assert tree.add(1)
    assert tree.add(3)
    assert tree.add(15)
    assert tree.root.data==10
    assert tree.root.left.data==5
    assert tree.root.left.left.data==2
    assert tree.root.left.left.left.data==1
    assert tree.root.left.left.right.data==3
    assert tree.root.right.data==20
    assert tree.root.right.right.data==30
    assert tree.root.right.left.data==15
    assert tree.root.right.right.left.data==25
    assert tree.root.right.right.right.data==55

def test_find():
    a=Bst()
    a.add(20)
    a.add(5)
    a.add(30)
    a.add(25)
    a.add(55)
    a.add(2)
    a.add(15)
    assert a.find(15)
    assert a.find(2)
    assert a.find(55)
    assert not a.find(0)

def test_remove():
    a=Bst()
    a.add(10)
    a.add(20)
    a.add(5)
    a.add(2)
    a.add(1)
    a.add(3)
    a.add(15)
    assert a.remove(3)
    assert a.remove(1)
    assert not a.find(3)
    assert not a.find(1)
    assert a.find(15)
    assert a.remove(15)
    assert not a.remove(15)
    assert not a.find(15)
    a.add(7)
    assert a.remove(5)
    assert not a.remove(5)
    assert not a.find(5)

def test_tree_size():
    a=Bst()
    for i in range(1,99):
        a.add(i)
        assert tree_size(a.root)==i
    from random import randint
    for i in range(randint(5,tree_size(a.root))):
        a.remove(randint(0,50))
        assert a.size==tree_size(a.root)

def test_tree_height():
    a=Bst()
    from random import randint
    for i in range(21):
        a.add(i)
    assert tree_height(a.root)==20
    a.remove(2)
    a.remove(10)
    a.remove(12)
    assert tree_height(a.root)==17
    for i in range(-100,-50,1):
        a.add(i)
    assert tree_height(a.root)==50

def test_pre_in_post_order():
    a=Bst()
    for i in range(10):
        a.add(i)
    assert [i for i in range(10)]==preorder(a.root)
    assert [i for i in range(10)]==inorder(a.root)
    assert [i for i in range(9,-1,-1)]==postorder(a.root)
    a.clear()
    a.add(10)
    a.add(10)
    a.add(20)
    a.add(5)
    a.add(30)
    a.add(25)
    a.add(55)
    a.add(2)
    a.add(1)
    a.add(3)
    a.add(15)
    assert preorder(a.root)==[10, 5, 2, 1, 3, 20, 15, 30, 25, 55]
    assert inorder(a.root)==[1, 2, 3, 5, 10, 15, 20, 25, 30, 55]
    assert postorder(a.root)==[1, 3, 2, 5, 15, 25, 55, 30, 20, 10]
    

##Test Cases for treap##
def test_treap_remove():
    tree=Treap()
    tree.add(5)
    tree.add(15)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(13)
    tree.add(17)
    assert tree.remove(7)
    assert not tree.remove(7)
    assert not tree.remove(12)
    assert tree.remove(13)
    assert tree.remove(5)
    
    
def test_treap_add():
    tree=Treap()
    from random import randint
    while tree.size!=5:
        ran=randint(1,50)
        if not tree.find(ran):
            assert tree.add(ran)
        else:
            assert not tree.add(ran)
    #print(tree)
    if tree.root.left:
        assert tree.root.data>tree.root.left.data
        assert tree.root.priority<tree.root.left.priority
        if tree.root.left.left:
            assert tree.root.left.data>tree.root.left.left.data
            assert tree.root.left.priority<tree.root.left.left.priority
        if tree.root.left.right:
            assert tree.root.data>tree.root.left.data
            assert tree.root.priority<tree.root.left.priority
            
    if tree.root.right:
        assert tree.root.data<tree.root.right.data
        assert tree.root.priority<tree.root.right.priority
        if tree.root.right.right:
            assert tree.root.right.data<tree.root.right.right.data
            assert tree.root.right.priority<tree.root.right.right.priority
        if tree.root.right.left:
            assert tree.root.data<tree.root.right.data
            assert tree.root.priority<tree.root.right.priority

def test_rotate_left():
    tree=Bst()
    tree.add(10)
    tree.add(35)
    tree.add(23)
    tree.add(13)
    tree.add(27)
    tree.add(5)
    tree.add(17)
    tree.add(1)
    tree.root=rotate_left(tree.root)
    assert tree.root.data==35
    assert tree.root.left.data==10
    assert tree.root.left.left.data==5
    assert tree.root.left.left.left.data==1
    assert tree.root.right is None
    assert tree.root.left.right.data==23
    assert tree.root.left.right.right.data==27
    assert tree.root.left.right.left.data==13
    assert tree.root.left.right.left.right.data==17
    assert tree.root.left.right.left.right.left is None
    assert tree.root.left.right.left.right.right is None
    tree.root.left.right=rotate_left(tree.root.left.right)
    assert tree.root.data==35
    assert tree.root.left.data==10
    assert tree.root.left.left.data==5
    assert tree.root.left.left.left.data==1
    assert tree.root.right is None
    assert tree.root.left.right.data==27
    assert tree.root.left.right.left.data==23
    assert tree.root.left.right.left.left.data==13
    assert tree.root.left.right.left.left.right.data==17

def test_rotate_right():
    tree=Bst()
    tree.add(34)
    tree.add(14)
    tree.add(2)
    tree.add(19)
    tree.add(26)
    tree.add(20)
    tree.add(7)
    tree.add(40)
    tree.add(45)
    tree.root=rotate_right(tree.root)
    assert tree.root.data==14
    assert tree.root.left.data==2
    assert tree.root.left.right.data==7
    assert tree.root.right.data==34
    assert tree.root.right.right.data==40
    assert tree.root.right.right.right.data==45
    assert tree.root.right.right.right.right is None
    assert tree.root.right.left.data==19
    assert tree.root.right.left.right.data==26
    assert tree.root.right.left.right.left.data==20
    tree.root.right.left.right=rotate_right(tree.root.right.left.right)
    assert tree.root.data==14
    assert tree.root.left.data==2
    assert tree.root.left.right.data==7
    assert tree.root.right.data==34
    assert tree.root.right.right.data==40
    assert tree.root.right.right.right.data==45
    assert tree.root.right.right.right.right is None
    assert tree.root.right.left.data==19
    assert tree.root.right.left.right.data==20
    assert tree.root.right.left.right.right.data==26

def test_add():
    tree=Bst()
    assert tree.add(10)
    assert tree.root.data==10
    assert not tree.add(10)
    assert tree.add(20)
    assert tree.add(5)
    assert tree.add(30)
    assert tree.add(25)
    assert tree.add(55)
    assert tree.add(2)
    assert tree.add(1)
    assert tree.add(3)
    assert tree.add(15)
    assert tree.root.data==10
    assert tree.root.left.data==5
    assert tree.root.left.left.data==2
    assert tree.root.left.left.left.data==1
    assert tree.root.left.left.right.data==3
    assert tree.root.right.data==20
    assert tree.root.right.right.data==30
    assert tree.root.right.left.data==15
    assert tree.root.right.right.left.data==25
    assert tree.root.right.right.right.data==55

def test_find():
    a=Bst()
    a.add(20)
    a.add(5)
    a.add(30)
    a.add(25)
    a.add(55)
    a.add(2)
    a.add(15)
    assert a.find(15)
    assert a.find(2)
    assert a.find(55)
    assert not a.find(0)

def test_remove():
    a=Bst()
    a.add(10)
    a.add(20)
    a.add(5)
    a.add(2)
    a.add(1)
    a.add(3)
    a.add(15)
    assert a.remove(3)
    assert a.remove(1)
    assert not a.find(3)
    assert not a.find(1)
    assert a.find(15)
    assert a.remove(15)
    assert not a.remove(15)
    assert not a.find(15)
    a.add(7)
    assert a.remove(5)
    assert not a.remove(5)
    assert not a.find(5)

def test_tree_size():
    a=Bst()
    for i in range(1,99):
        a.add(i)
        assert tree_size(a.root)==i
    from random import randint
    for i in range(randint(5,tree_size(a.root))):
        a.remove(randint(0,50))
        assert a.size==tree_size(a.root)

def test_tree_height():
    a=Bst()
    from random import randint
    for i in range(21):
        a.add(i)
    assert tree_height(a.root)==20
    a.remove(2)
    a.remove(10)
    a.remove(12)
    assert tree_height(a.root)==17
    for i in range(-100,-50,1):
        a.add(i)
    assert tree_height(a.root)==50

def test_pre_in_post_order():
    a=Bst()
    for i in range(10):
        a.add(i)
    assert [i for i in range(10)]==preorder(a.root)
    assert [i for i in range(10)]==inorder(a.root)
    assert [i for i in range(9,-1,-1)]==postorder(a.root)
    a.clear()
    a.add(10)
    a.add(10)
    a.add(20)
    a.add(5)
    a.add(30)
    a.add(25)
    a.add(55)
    a.add(2)
    a.add(1)
    a.add(3)
    a.add(15)
    assert preorder(a.root)==[10, 5, 2, 1, 3, 20, 15, 30, 25, 55]
    assert inorder(a.root)==[1, 2, 3, 5, 10, 15, 20, 25, 30, 55]
    assert postorder(a.root)==[1, 3, 2, 5, 15, 25, 55, 30, 20, 10]
    
