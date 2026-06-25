t=()
n = int(input("Enter the size of the tuple:-"))
for i in range(n):
    ele = int(input("Enter the element {}:-".format(i)))
    t+=(ele,)
print(t)

#Reversing tuple
print(t[::-1])

#nested tuple

t=(1,2,(3,4),(5,6,(7,8)))
print(t[3][2][1])

t = ("a", ("b", "c"), ("d", ("e", "f")))

print(t[1][0])  
print(t[2][1][1]) 


t = (1, (2, (3, (4, 5))))
print(t[1][1][1][0])

