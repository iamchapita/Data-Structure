# -*- coding: utf-8 -*-

class Node:
    
    def __init__(self, value):
        
        self.value = value 
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, value):
        
        newNode = Node(value)

        if(not self.first):
            self.first = newNode
            self.last = newNode
            newNode.next = self.first
            return True

        else:
            self.last.next = newNode
            self.last = newNode
            self.last.next = self.first
            return True

    def print(self):

        current = self.first
        str = ""
        str += ("%s=>")%(current.value)

        while (current.next != self.first):
            
            current = current.next
            str += ("%s=>")%(current.value)
            if(current.next == self.first):
                str += ("...")
        
        print(str)

    def search(self, value):

        current = self.first
    
        if(value == current.value):
            return value

        while(current.next != self.first):
            current = current.next
            if(current.value == value):
                return current.value

        return False

    def length(self):
    
        current = self.first
        count = 1

        while(current.next != self.first):

            count += 1
            current = current.next
            
        return count
    

cll = CircularLinkedList()

cll.push(0)
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)
cll.push(5)
cll.push(6)
cll.push(7)
cll.push(110)

cll.print()
print(cll.search(0))
print(cll.length())

print("El primer valor(nodo) de la lista enlazada circular es: ", cll.first.value)
print("El último valor(nodo) de la lista enlazada circular es: ", cll.last.value)
print("El valor(nodo) que está despues del último valor(nodo) es: ", cll.last.next.value)
