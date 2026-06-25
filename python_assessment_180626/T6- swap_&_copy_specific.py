t1=(1,2,3)
t2=(6,8,9)

print("Before swap:",t1,"\n",t2)
t1,t2 = t2,t1
print("After swap:",t1,"\n",t2)

t = (10, 20, 30, 40, 50)

# copy only values > 25
new_t=()
for x in t: 
    if x > 25:
        new_t+=(x,)        

print(new_t)

#Using Indexing 
t = (10, 20, 30, 40, 50)
new_t = (t[0], t[2], t[4])
print(new_t)