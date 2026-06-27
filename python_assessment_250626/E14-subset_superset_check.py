A={1, 2, 3}
B={1, 2, 3, 4, 5} 
#Expected Output: Set A is a subset of Set B.

#list->set->check

l1=[]
n=int(input("Enter the size of the list-1:"))
for i in range(n):
    ele = int(input(f"Element {i+1}:-"))
    l1.append(ele)
print(l1)    

l2=[]
n=int(input("Enter the size of the list-2:"))
for i in range(n):
    ele = int(input(f"Element {i+1}:-"))
    l2.append(ele)
print(l2)   

s1 = set(l1)
s2 = set(l2)

print(s1,"\n",s2,sep="")

def subset(s1,s2):
    if s1.issubset(s2):
        print(f"{s1} is subset of {s2}")
    else:
        print(f"{s1} is not a subset of {s2}")

def superset(s1,s2):
    if s1.issuperset(s2):
        print(f"{s1} is superset of {s2}")
    else:
        print(f"{s1} is not superset of {s2}")            

subset(s1,s2)
superset(s1,s2)


