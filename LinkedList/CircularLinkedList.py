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
    

ll = CircularLinkedList()

ll.push(0)
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.push(110)

ll.print()
print(ll.search(0))
print(ll.length())

print("El primer valor(nodo) de la lista enlazada circular es: ", ll.first.value)
print("El último valor(nodo) de la lista enlazada circular es: ", ll.last.value)
print("El valor(nodo) que está despues del último valor(nodo) es: ", ll.last.next.value)
