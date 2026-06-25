l=[1,1,2,3,4,1,2,3,4]
#output l = [1,2,3,4]

def remove_dups(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    print(new)        

remove_dups(l)        
        