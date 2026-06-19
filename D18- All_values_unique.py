d = {"N":1,"S":1,"U":1}

for i in d.values():
    flag=0
    for j in d.values():
        if i!=j:
            flag=1
            break

if flag==0:
    print("All are same values..!!!")
else:
    print("Not Same values...!!!")    