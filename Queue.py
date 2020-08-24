# -*- coding:utf-8 -*-


class Node:
    #constructor
    def __init__(self,value): #en todas las funciones el primer parametro tiene que ser un self
        self.value = value #self -> this
        self.next = None

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

    