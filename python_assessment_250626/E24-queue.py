class Queue:
    def __init__(self):
        self.rear = []
       
    def enqueue(self,data):
        self.rear.append(data)

    def dequeue(self):
        if not self.empty():
            return self.rear.pop(0)
        else:
            print("Queue is empty")

    def empty(self):
        return len(self.rear)==0  

    def display(self):
        print(self.rear) 

q =  Queue()

q.enqueue("Customer-A")
q.enqueue("Customer-B")
q.enqueue("Customer-C")

q.display()

print("dequeue:-",q.dequeue())
q.display()
