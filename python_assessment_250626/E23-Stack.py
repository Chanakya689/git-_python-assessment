#Push="google.com", "pynative.com"
#Pop expected output:

#Current Top: pynative.com 
#Popped: pynative.com 
#New Top: google.com
'''
l=[]
n = int(input("Enter the size of the list:"))
for i in range(n):
    st = input("Enter the .com format into the list:")
    l.append(st)

print(l)   

l.pop()
print(l)

'''
#-------------------------------------------------------------------||

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
       # print(self.stack,"\n",sep="")   

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("Stack is Empty\n")

    def peek(self):
        if not self.empty():
            print(self.stack[-1])
            return self.stack[-1]
        else:
            print("Stack is empty\n")


    def empty(self):
        return len(self.stack)==0               

    def display(self):
        print(self.stack,end=" ")

obj = Stack()

obj.push("googly.com")
obj.push("Yahoo.com")
obj.push("Lee.com")
obj.display()
print()
print("peek:-",obj.peek())

print("pop:-",obj.pop())
print("After poped:-",obj.display())
