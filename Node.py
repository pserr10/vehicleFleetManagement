# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:24:04 2019

@author: Diogo Soares
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.l_child = None
        self.r_child = None

    def binary_insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.l_child is None:
                    root.l_child = node
                else:
                    self.binary_insert(root.l_child, node)
            else:
                if root.r_child is None:
                    root.r_child = node
                else:
                    self.binary_insert(root.r_child, node)

    def in_order_print(self, root):
        if not root:
            return
        self.in_order_print(root.l_child)
        print(root.data)
        self.in_order_print(root.r_child)

    def pre_order_print(self, root):
        if not root:
            return        
        print(root.data)
        self.pre_order_print(root.l_child)
        self.pre_order_print(root.r_child)
        
    def findvalue(self, root, value):
        if value < root.data:
            if root.l_child is None:
                return False
            return root.l_child.findvalue(root.l_child, value)
        elif value > root.data:
            if root.r_child is None:
                return False
            return root.r_child.findvalue(root.r_child, value)
        else:
            return True

if __name__ == "__main__":
    r = Node(3)
    r.binary_insert(r, Node(7))
    r.binary_insert(r, Node(1))
    r.binary_insert(r, Node(5))
    print("in order:")
    r.in_order_print(r)
    
    print("pre order")
    r.pre_order_print(r)
    print(r.findvalue(r, 5))
    print(r.findvalue(r, 6))