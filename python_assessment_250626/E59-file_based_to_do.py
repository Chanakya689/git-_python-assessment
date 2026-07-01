class To_Do:
    filename = "to_do18.txt" 
    def add(self,task):
        with open(self.filename,"a") as f:
            f.write(task+"\n")
        
    def check(self):
        try:
            with open(self.filename,"r") as f:
                lines = f.readlines()
                if len(lines) == 0:
                    print("File is Empty")
                    return   
                                                         
                print("||---------To-Do--------||")
                for index, value in enumerate(lines, start=1):
                    print(f"{index}:{value.strip()}")

        except FileNotFoundError:
            '''File is not existed or created yet, so we are handling the exception'''
            print("File not found. Please add a task first.")            
                    
                    
    def clear(self):
        with open(self.filename,"w") as f:
            #f.write("")
            pass
        print("File data cleared")

obj = To_Do()             
while True:
    print("Options:->1:add(),2:check(),3:clear()")
    choice = int(input("Enter the option:"))
    
    if choice==1:
        task = input("Enter the task to add:")
        obj.add(task)
    
    elif choice==2:
        obj.check()
    
    elif choice==3:
        obj.clear()
    
    else:
        print("Invalid option and Exiting the program")
        break