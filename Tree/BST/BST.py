# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

from LinkedList import LinkedList
from Node import Node

class BST:

    def __init__(self):
        self.root =  None

    def add(self, value) -> None:
        current = self.root
        self.__add(value, current)
    
    # Se utiliza "__" al principio para definir el método como privado
    def __add(self, value, current: Node) -> bool:

        # Si el valor que se intenta ingresar, ya está en el árbol
        """ if self.search(value):
            return None """

        # Si no hay raíz
        if(current == None):
            self.root = Node(value)
            return True

        # Si la raíz es del tipo Nodo
        if(isinstance(current, Node)):
            
            # Si el valor que se intenta ingresar(value) es mayor al valor del nodo(current.value)
            if value > current.value:
                
                # Si no existe nodo a la derecha del nodo comprobado(current.value) 
                if(not current.right):
                    
                    # Se inserta un nodo y se establece con el valor que se intenta ingresar
                    current.right = Node(value)
                    return True
                
                # Si hay nodo a la derecha del nodo comprobado
                else: return self.__add(value, current.right)

            # Si el valor que se intenta ingresar(value) es menor al valor del nodo(current.value)
            else:
                
                # Si no hay nodo a la izquierda del nodo comprobado
                if(not current.left):

                    # Se inserta un nodo y se establece con el valor que se intenta ingresar
                    current.left = Node(value)
                    return True

                # Si hay nodo a la izquierda del nodo comprobado
                else: return self.__add(value, current.left)
    
    # Se convierte una lista enlazada a un árbol binario de búsqueda (BST)
    # Se debe ejecutar en un instancia de árbol vacía
    def convert(self, linkedlist: LinkedList) -> bool:
        
        # Se comprueba que linkedlist sea el tipo LinkedList
        if(not isinstance(linkedlist, LinkedList)): return False
        
        # Se establece el current
        current = linkedlist.first

        # Se recorre la lista enlazada
        while (current):    

            # Se agrega el valor al árbol
            self.add(current.value)
            current = current.next
        
        return True

    def search(self, value) -> Node:
        # Se instancia la raíz del árbol
        current = self.root
        # Si no hay raíz
        if(not current): 
            return False
        # Si el valor de la raíz es el valor buscado
        if(current.value == value):
            print(current.value)
        # Se llama el método que buscara en los hijos de la raíz, y en los hijos de los hijos
        else:
            # Se llama con return puesto que la función se utiliza múltiples veces(recursivo)
            # Retorna el valor al llamado de instanciabst.search(valor)
            return self.__search(value, current)

    def __search(self, value, current) -> Node:
        
        if(current.value == value):
            # Retorna el *nodo* al llamado de __search
            return current

        elif value > current.value and current.right is not None:
            return self.__search(value, current.right)

        elif value < current.value and current.left is not None:
            return self.__search(value, current.left)
    
    def deleteNode(self, value) -> Node:
        # Se borra el nodo retornado por el método de búsqueda
        return self.__deleteNode(self.search(value))
    
    def __deleteNode(self, node:Node):

        if not node:
            print("Nodo no encontrado")
            return None

        # Incompleto, necesito estudiar para hacerlo JAJA
        
    def print(self):
        current = self.root
        self.__print(current)

    def __print(self, current, space = 0) : 

        if (current == None): 
            return False
        
        space += 7

        self.__print(current.right, space)  
        print()  
        
        for i in range(space): 
            print(end = " ")  

        print(current.value)  
  
        self.__print(current.left, space)  

bst = BST()

bst.add(1)
bst.add(10)
bst.add(11)
bst.add(12)
bst.add(-4)
bst.add(-3)
bst.add(8)
bst.add(-7)
bst.add(-1)
bst.add(4)
bst.add(7)
bst.add(5)

# Se imprime dirección de memoria del nodo encontrado
#print(bst.search(-7))
# Imprime el valor del  nodos encontrado
#print(bst.search(-7).value)

bst.print()

#======================================================================================#

ll = LinkedList()
ll.push(10,0)
ll.push(15,1)
ll.push(29,2)
ll.push(33,3)
ll.push(49,4)
ll.push(46,5)
ll.push(60,6)
ll.push(38,7)
ll.push(110,8)
ll.push(66,6)
ll.push(9,9)
ll.push(5,10)
ll.push(3,11)
ll.push(4,12)
ll.push(7,13)
ll.push(11,14)
ll.push(1,15)

bst1 = BST()

bst1.convert(ll)

#bst1.print()





