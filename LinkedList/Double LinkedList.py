# -*- coding: utf-8 -*-

class Node:
    
    def __init__(self, value):
        
        self.value = value 
        self.next = None
        self.prev = None

class Double_LinkedList:

    def __init__(self):
        self.first = None

    def push(self, value, position = 0):

        if(not isinstance(position, int) or position < 0 or position > self.length()):
            return False

        if(not self.first):
            self.first = Node(value)
            return True
        
        if(position == 0):
            current = self.first
            self.first = Node(value)
            self.first.next = current
            self.first.next.prev = self.first    
            return True
        
        before = self.first
        current = self.first.next
        count = 1
        
        while (before):
            
            if(count == position):

                before.next = Node(value)
                before.next.prev = before    
                before.next.next = current
                return True

            count += 1
            before = before.next
            current =  current.next

        current = Node(value)
        return True

    def print(self, order = "up"):

        if(order == "up"):
            current = self.first
            string = ""

            while(current):

                string += (("%s <=> ")%(current.value))
                current = current.next
            
            string += "null"
            print(string)

        elif(order == "down"):

            current = self.first
            string = ""

            while(current):

                if(current.next == None):
                    break

                current = current.next

            while (current):

                string += (("%s <=> ")%(current.value))
                current = current.prev
                
            string += "null"
            print(string)

    def delete(self, position):
        
        if(not isinstance(position, int) or position < 0 or position > self.length()):
            return False

        if(position == 0):
            self.first = self.first.next
            self.first.prev = None
            return True
        
        count = 1
        before = self.first
        current = self.first.next

        while (current):

            if(count == position):
                
                before.next = before.next.next
                before.next.prev = current.prev
                return True
            
            count += 1
            before = before.next
            current =  current.next
        
        return False

    def search(self, value):

        current = self.first

        while (current):
            
            if(value == current.value):
                print(True)
                return True

            current =  current.next
        
        print(False)
        return False

    def length(self):
        
        current = self.first
        count = 0

        while (current):

            count += 1    
            current = current.next
        
        return count

    
d_ll = Double_LinkedList()
d_ll.push(1,0)
d_ll.push(2,1)
d_ll.push(3,2)
d_ll.push(4,3)
d_ll.push(5,4)
d_ll.push(6,5)
d_ll.push(7,6)
d_ll.push(8,7)
d_ll.push(9,8)

d_ll.delete(4)

d_ll.print("up")
d_ll.print("down")



