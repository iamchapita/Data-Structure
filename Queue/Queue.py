# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

from Node import Node

class Queue:
    
    def __init__(self):
        self.first = None

    def push(self,value):
        
        if not self.first:
            self.first = Node(value)
            return True #None, True y False, inicial en mayuscula

        current = self.first
        while current.next:
            current = current.next
        current.next = Node(Value)
        return True

    def pop(self):
        pass

    def length(self):
        pass

    def print(self):
        pass

    