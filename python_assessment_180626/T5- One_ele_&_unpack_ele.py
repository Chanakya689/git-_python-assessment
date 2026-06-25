#Taking one element

t = (9,)
print(t)

#or
t = tuple([9])
print(t)
print(type(t))

#Unpack_of_tupel

t = (1,2,3,4)
a,b,c,d=t
print("a:{},b:{},c:{},d:{}".format(a,b,c,d))

t = (6,7,8,9,10)
a,*b=t
print(f"a:{a},b:{tuple(b)}")