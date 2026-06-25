l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is:", l)

def comprehension_of_num(lst):
    return [x**3 for x in lst if x%2!=0]

print("The list after applying list comprehension is:", comprehension_of_num(l))