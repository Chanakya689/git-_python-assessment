#For Node inside [data|next]->
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class Implementing_SLL:
    
    def __init__(self):
        self.head = None
    
    def appending(self,data):
        #Node Creation
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        #For Traversing the list
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
            
            
sll = Implementing_SLL()  

sll.appending(10)
sll.appending(20)
sll.appending(30)

sll.display()
