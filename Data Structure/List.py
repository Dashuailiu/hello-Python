# -*- coding:utf-8 -*-
import copy
class Node(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def reverse(self) -> object:
        lNode = None
        cNode = copy.deepcopy(self)
        rNode = cNode.next
        while rNode != None:
            cNode.next = lNode
            lNode = cNode
            cNode = rNode
            rNode = cNode.next
        cNode.next = lNode
        return cNode

    def show(self):
        cNode = self
        while cNode != None:
            print(cNode.value)
            cNode = cNode.next

class LinkedList(object):
    class LinkedNode(object):
        def __init__(self,value,next=None):
            self._value = value
            self._next = next

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self,value):
            self._value = value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self,next):
            self._next = next

    def __init__(self):
        self._head = None

    def initlist(self):
        try:
            val = input()
            self._head = self.LinkedNode(val)
            p = self._head
            while True:
                val = input()
                if val == 'end':
                    break
                tmp = self.LinkedNode(val)
                p.next = tmp
                p = tmp
        except ValueError:
            print('Wrong value!')
        finally:
            print('Input ended!')
            
    def show(self):
        cLinkedNode = self._head
        while cLinkedNode != None:
            print(cLinkedNode.value)
            cLinkedNode = cLinkedNode.next

    def reverse(self):
        clnode = self._head
        rlnode = clnode.next
        llnode = None

        while rlnode != None:
            clnode.next = llnode
            llnode = clnode
            clnode = rlnode
            rlnode = clnode.next
        clnode.next = llnode
        self._head = clnode






if __name__ == '__main__':
    L = Node('a',Node('b',Node('c',Node('d'))))
    L.show()
    L2 = L.reverse()
    L2.show()

    print("LinkedList: ")
    LList = LinkedList()
    LList.initlist()
    LList.show()
    LList.reverse()
    LList.show()
    