# -*- coding=utf-8 -*-

from Node import *

class Stack:

    def __init__(self):
        self.first = None


    def push(self, value):
        
        #Si no existe un First
        if(not self.first):
            self.first = Node(value)
            return True
        
        #Si existe un First
        current = self.first

        while(current.next):
            current = current.next

        current.next = Node(value)
        return True

    def pop(self):

        if(not self.first):
            return False

        before = self.first
        current = self.first.next

        while(current.next):
            current = current.next
            before = before.next
        
        before.next = None

        return True
    def print(self):

        current = self.first
        empty = ""

        while(current):
            empty += "%s=>" %(current.value)
            current = current.next
        
        empty += "Null"
        return empty
            
    def lenght(self):

        current = self.first
        count = 0

        while(current):
            count += 1
            current = current.next
        return count

s = Stack()
s.push(0)
s.push(1)
s.push(2)
s.push(3)


