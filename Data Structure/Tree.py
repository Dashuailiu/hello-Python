# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self,value=None,left=None,right=None):
        self._value = value
        self._left =  left
        self._right = right

class Trees:
    def __init__(self,root):
        self._root = root

    def perTraverse(self,treeNode):
        if treeNode == None:
            return
        print(treeNode._value)
        self.perTraverse(treeNode._left)
        self.perTraverse(treeNode._right)


    def inTraverse(self, treeNode):
        if treeNode == None:
            return
        self.perTraverse(treeNode._left)
        print(treeNode._value)
        self.perTraverse(treeNode._right)


    def postTraverse(self, treeNode):
        if treeNode == None:
            return
        self.perTraverse(treeNode._left)
        print(treeNode._value)
        self.perTraverse(treeNode._right)

if __name__ == '__main__':
    tnode = TreeNode('1',
                         TreeNode('2',
                                  TreeNode('3'),TreeNode('4')
                                  ),
                         TreeNode('5',
                                  TreeNode('6'),TreeNode('7')
                                  )
                         )
    tree = Trees(tnode)
    print('pertraverse:')
    tree.perTraverse(tree._root)
    print('intraverse:')
    tree.inTraverse(tree._root)
    print('posttraverse:')
    tree.postTraverse(tree._root)