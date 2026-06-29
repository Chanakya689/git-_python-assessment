class power_of_two:
    def __init__(self,max_expo):
        self.max_expo = max_expo
        self.current = 0
        
    def __iter__(self):
        return self 

    def __next__(self):
        if self.current > self.max_expo:
            raise StopIteration
        result = 2**self.current
        self.current+=1

        return result

obj = power_of_two(3)
for value in obj:
    print(value,end=" ")       