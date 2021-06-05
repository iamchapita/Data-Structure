# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

from Node import Node

class Tree:

    def __init__(self):

        self.root = Node("raíz")

    def add_Child(self, value, Node_str = "raíz"):
        
        current = self.root

        if(Node_str == "raíz" ):
            current.children.push(value)
            return True

        if(isinstance(Node_str, str)):
            tree_aux =  Tree()
            tree_aux.root = current
            current = tree_aux.search(Node_str)
            current.children.push(value)
            return True
        
        return False

    def search(self, value, current = None):

        if(current == None):
            current = self.root

        if(current.value == value):
            return current

        if(current.next):
            
            current_aux = current.next

            while (current_aux):

                if(current_aux.value == value):
                    return current_aux
                
                current_aux = current_aux.next

        while (current):
            
            if(current.children.first):
                result = self.search(value, current.children.first)

                if(isinstance(result, Node)):
                    if(result.value == value):
                        return result

                if(result == False):
                    current = current.next
            else:
                current = current.next
        
        return False

    def print(self, current = None, tab = ""):
    
        if(not current):
            current = self.root

        while (current):
            
            if(current.children.first):

                if(current.children.first):
                    print("%s"%(tab)+current.value+":")

                else:
                    print("%s"%(tab)+current.value)

                self.print(current.children.first, "%s\t"%(tab))
            
            else:
                print("%s"%(tab)+current.value)

            current = current.next

tree = Tree()

"""
tree.add_Child("Hijo1")
tree.add_Child("Hijo2")
tree.add_Child("Hijo3")
tree.add_Child("Hijo121")
tree.add_Child("Hijo211")
tree.add_Child("Hijo333")
tree.add_Child("Hijo334")
tree.add_Child("Hijo335")
tree.add_Child("Hijo336")
tree.add_Child("Hijo337")
tree.add_Child("Hijo338")
tree.add_Child("Hijo339")
tree.add_Child("Hijo3310")

tree.add_Child("Hijo70", "Hijo1")
tree.add_Child("Hijo80", "Hijo1")
tree.add_Child("Hijo99", "Hijo1")

tree.add_Child("Hijo1000", "Hijo70")
tree.add_Child("Hijo1001", "Hijo70")
tree.add_Child("Hijo1002", "Hijo70")
tree.add_Child("Hijo1003", "Hijo70")
tree.add_Child("Hijo100212", "Hijo70")
tree.add_Child("Hijo10050", "Hijo70")

tree.add_Child("Hijo1000001", "Hijo1000")

tree.add_Child("Hijo701", "Hijo2")
tree.add_Child("Hijo801", "Hijo2")
tree.add_Child("Hijo991", "Hijo2")

tree.add_Child("Hijo7", "Hijo3")
tree.add_Child("Hijo8", "Hijo3")
tree.add_Child("Hijo9", "Hijo3")

tree.add_Child("Hijo10", "Hijo8")
tree.add_Child("Hijo11", "Hijo8")
tree.add_Child("Hijo12", "Hijo9")

tree.add_Child("Hijo13", "Hijo12")
tree.add_Child("Hijo14", "Hijo12")
tree.add_Child("Hijo15", "Hijo12")
tree.add_Child("Hijo16", "Hijo12")
tree.add_Child("Hijo17", "Hijo12")

tree.add_Child("Hijo18", "Hijo17")
tree.add_Child("Hijo19", "Hijo17")
tree.add_Child("Hijo20", "Hijo17")

tree.add_Child("Hijo200")
tree.add_Child("Hijo230")
tree.add_Child("Hijo918")

"""
tree.add_Child("Hijo1")
tree.add_Child("Hijo2")
tree.add_Child("Hijo3")
tree.add_Child("Hijo122")
tree.add_Child("Hijo222")
tree.add_Child("Hijo333")

tree.add_Child("Hijo4", "Hijo1")
tree.add_Child("Hijo5", "Hijo1")
tree.add_Child("Hijo6", "Hijo1")
tree.add_Child("Hijo15", "Hijo4")

tree.add_Child("Hijo22", "Hijo15")


tree.add_Child("Hijo14", "Hijo2")


tree.add_Child("Hijo7", "Hijo3")
tree.add_Child("Hijo8", "Hijo3")
tree.add_Child("Hijo9", "Hijo3")

tree.add_Child("Hijo20", "Hijo7")
tree.add_Child("Hijo10", "Hijo9")
tree.add_Child("Hijo11", "Hijo9")
tree.add_Child("Hijo12", "Hijo9")

tree.add_Child("Hijo13", "Hijo12")
tree.add_Child("Hijo19", "Hijo13")
tree.add_Child("Hijo17", "Hijo14")
tree.add_Child("Hijo18", "Hijo14")

tree.print()


