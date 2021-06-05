# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

from Node import Node

class CircularLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, value, position = 0):
        
        #Comprobando is position es entero, es mayor que 0 o es menor que la longitud de la lista
        if(not isinstance(position,int) or position < 0 or position > self.length()):
            return False

        newNode = Node(value)

        #Caso base: si la lista enlazada esta vacía 
        if(not self.first):
            self.first = newNode
            self.last = newNode
            newNode.next = self.first
            return True

        count = 0
        current = self.first
    
        #caso 1: si se quiere insertar un nodo en la primera(0) posición
        if(position == count):
            self.first = newNode
            self.first.next = current
            self.last.next =  self.first    
            return True
        
        before = self.first
        current = self.first.next
        
        #Caso 2: Si se quiere inserta un nodo en otra posición que no sea la primera(0)
        while (before):

            count += 1
            if(count == position):
                before.next = newNode
                before.next.next =  current

                #Comprobando si la longitud de la lista y la position son iguales, para cambiar el "last" de la lista
                if(self.length() - 1 == position):
                    self.last = newNode
                    newNode.next =  self.first
                return True
            
            #Comprobando si el before.next es distinto del primero para mover los punteros
            if(before.next != self.first):
                before = before.next
                current = current.next

            #Se rompe el while, puesto que, si el before.next es igual al self.first significa que se recorrió
            #toda la lista enlazada y no es necesario seguir con el while
            else:
                break
        
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
            return True

        while(current.next != self.first):
            current = current.next
            if(current.value == value):
                return True

        return False

    def length(self):
    
        current = self.first
        count = 1

        try:
            while(current.next != self.first):

                count += 1
                current = current.next
            
            return count
        except: 
            return count


Cll = CircularLinkedList()

Cll.push(0)
Cll.push(1,1)
Cll.push(2,2)
Cll.push(3,3)
Cll.push(4,4)
Cll.push(5,5)
Cll.push(6,6)
Cll.push(7,7)
Cll.push(-1)
Cll.push(-2,0)

Cll.print()

print("El valor se encuentra en la lista:", Cll.search(0))
print("La longitud de la lista circular enlazada es:" , Cll.length())

print("El primer valor(nodo) de la lista enlazada circular es: ", Cll.first.value)
print("El último valor(nodo) de la lista enlazada circular es: ", Cll.last.value)
print("El valor(nodo) que está despues del último valor(nodo) es: ", Cll.last.next.value)
