t=()
n = int(input("Enter the size of the tuple"))
for i in range(n):
    ele = int(input("Enter the element {}:-".format(i)))
    t+=(ele,)
print(t)

#Repetation of tuple

c = int(input("Enter the Repetation times:"))
t = t*c
print(t)