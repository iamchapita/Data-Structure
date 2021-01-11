# -*- coding: utf-8 -*-

class Node:
    
    def __init__(self, value):
        
        self.value = value 
        self.next = None

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


cll = CircularLinkedList()

cll.push(0)
cll.push(1,1)
cll.push(2,2)
cll.push(3,3)
cll.push(4,4)
cll.push(5,5)
cll.push(6,6)
cll.push(7,7)
cll.push(-1)
cll.push(-2,0)

cll.print()

print("El valor se encuentra en la lista:", cll.search(0))
print("La longitud de la lista circular enlazada es:" , cll.length())

print("El primer valor(nodo) de la lista enlazada circular es: ", cll.first.value)
print("El último valor(nodo) de la lista enlazada circular es: ", cll.last.value)
print("El valor(nodo) que está despues del último valor(nodo) es: ", cll.last.next.value)
