nested = [1, [2, 3], [4, [5, 6]], 7] 
#Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]
new_list=[]

def flattened_list(l):
    
    for i in l:
        if isinstance(i,list):
            #recursive function
            flattened_list(i)
        else:
            new_list.append(i)
    return new_list        

new = flattened_list(nested)
print(new)