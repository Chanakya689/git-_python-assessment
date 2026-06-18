l=[[1,2,3],[4,5,6],[7,8,9]]

print("The original nested list is:", l)
for i in range(len(l)):
    print("The elements of the nested list at index", i, "are:", l[i])

for i in range(len(l)):
    for j in range(len(l[i])):
        print("The element at index", i, "and", j, "is:", l[i][j])
    print() 
         

