# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.parent = None
        self.children = LinkedList()


# Versión Especial de Lista Enlazada para contener los múltiples hijos del árbol
class LinkedList:

    def __init__(self):
        self.first = None

    def push(self, value):

        if(not self.first):
            self.first = Node(value)
            return True

        current = self.first

        while (current):

            if(not current.next):
                
                current.next = Node(value)
                return True

            current = current.next

        return False

    def print(self):

        current = self.first
        string = ""
        while(current):
            if(current.next):

                string += (("%s<=>") % (current.value))

            if(not current.next):
                string += (current.value)

            current = current.next

        print(string)

    def delete(self, value):

        if(not self.first):
            return False

        current = self.first

        while (current):

            if(current.value == value):
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, value):

        current = self.first
        while(current):

            if(current.value == value):
                
                return current

            current = current.next

        return False

    def length(self):

        current = self.first
        count = 0

        while(current):

            count += 1
            current = current.next

        return count
