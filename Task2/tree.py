myTree = ['a',
            ['b',
            ['d', [], []],
            ['d', [], []]],
            ['c',
            ['f', [], []],
            []]
            ]

def Binarytree(r):
    return [r, [], []]

def  iserteft (root, newBranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def inertRight(root, newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]
def setRootVal(root, newVal):
    root[0] = newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree!= None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
