t=()
n = int(input("Enter the size of the tuple:-"))
for i in range(n):
    ele = int(input("Enter the element {}:-".format(i)))
    t+=(ele,)
print(t)

#slicing of tuple
#printing elements from 2nd index to last
print(t[2::])

#printing elements from  Zero to before 3rd index 
print(t[:3:])

#Printing elements alternative from start (Based upon step size)
print(t[::2])

#printing elements reverse alternative from last (Based upon step size)
print(t[::-2])

#Within Range
t = t[2:4:1]
print(t)

#Adding two ranges
t = t[2:4:1]+t[1:3:1]
print(t)