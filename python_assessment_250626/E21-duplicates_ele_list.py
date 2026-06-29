numbers = [1, 1, 2, 3, 2, 4, 5, 1, 6] 
#Expected Output: Duplicates found: {1, 2}

def dups_founding(l:list):
    result=[]
    for i in l:
        count=0
        for j in l:
            if i==j:
                count+=1
        if count>1:
            result.append(i)   

    return result

print(set(dups_founding(numbers)))             





seen = set()
duplicates = set()

for i in numbers:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)        

    