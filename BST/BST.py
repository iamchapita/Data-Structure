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
                    current.right.parent = current
                    return True
                
                # Si hay nodo a la derecha del nodo comprobado
                else: return self.__add(value, current.right)

            # Si el valor que se intenta ingresar(value) es menor al valor del nodo(current.value)
            elif value < current.value:
                
                # Si no hay nodo a la izquierda del nodo comprobado
                if(not current.left):

                    # Se inserta un nodo y se establece con el valor que se intenta ingresar
                    current.left = Node(value)
                    current.left.parent = current
                    return True

                # Si hay nodo a la izquierda del nodo comprobado
                else: return self.__add(value, current.left)

            else: 
                print("El valo ya existe en el Árbol")
    
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
            return current
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

    # Encuentra la altura del árbol
    # Encuentra la rama mas larga o alta del árbol y devuelve el número de niveles
    def height(self):
        # Comprobando si hay raíz 
        current = self.root
        if current:
            return self.__height(current)

    def __height(self, node, heigh=0):
        # Si no hay nodo
        if not node:
            return heigh
        # Calculando la altura por el lado izquierdo de todos los nodos
        leftHeigh = self.__height(node.left, heigh+1)
        # Calculando la altura por el lado derecho de todos los nodos
        rightHeigh = self.__height(node.right, heigh+1)
        # retorna el valor mas alto de ambas variables
        return max(leftHeigh, rightHeigh)

    # Borra un nodo del árbol
    def deleteNode(self, value) -> Node:
        # Se borra el nodo retornado por el método de búsqueda
        return self.__deleteNode(self.search(value))
    
    def __deleteNode(self, node:Node):
        
        if not node:
            print("Nodo no encontrado")
            return None

        # División por casos:
        # 1. El nodo no tiene hijos
        # 2. El nodo tiene un hijo
        # 3. El nodo tiene dos hijos

        # Obtenemos el padre del nodo
        parent = node.parent

        # CASO 1: Si el nodo no tiene hijos
        if self.numChildren(node) == 0:
            
            if parent:

                if parent.left == node:
                    parent.left = None
                
                else:
                    parent.right = None
                
            else:
                self.root = None

        # CASO 2: El nodo tiene un hijo
        if self.numChildren(node) == 1:
            
            # Obteniendo el hijo del lado izquierdo (si existe)
            if node.left:
                child = node.left

            # Obteniendo el hijo del lado derecho (si existe)
            else:
                child = node.right

            # Si existe un padre
            if parent:
                
                # Si el padre contiene el nodo a eliminar en el lado izquierdo
                if parent.left == node:
                    parent.left = child

                # Si el padre contiene el nodo a eliminar en el lado derecho
                else:
                    parent.right = child

            # No existe un padre
            else:
                self.root=child
            
            child.parent = parent

        # CASO 3: El nodo tiene dos hijos
        if self.numChildren(node) == 2:

            successor = self.minValue(node.right)
            node.value = successor.value
            self.__deleteNode(successor)

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

    # Obtiene el valor más pequeño de un nodo
    def minValue(self, current):
        while current.left:
            current = current.left
        return current
    
    # Obtiene el número de hijos del nodo
    def numChildren(self, current):
        count = 0
        if current.left:
            count += 1
        if current.right:
            count += 1
        return count

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
# print(bst.search(-7))
# Imprime el valor del  nodos encontrado
# print(bst.search(-7).value)

bst.print()
bst.deleteNode(1)
bst.deleteNode(-7)
bst.deleteNode(12)
print("=======================================================================================")
bst.print()
