employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)] 
#Expected Output: [('Bob', 25, 75000), ('Charlie', 35, 60000), ('Alice', 30, 50000)]

def sorting(l):
    return sorted(l,key = lambda x:x[1],reverse=False)
        

print(sorting(employees))    