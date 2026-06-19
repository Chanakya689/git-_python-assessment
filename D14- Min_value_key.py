d = {"Chan":9,"DP":6,"Trivikram":4}

def min_value_key(**kwargs):
    print(kwargs)
    return (min(kwargs.values()))

value = min_value_key(**d)  

for k,v in d.items():
    if v == value:
        print(k)

#Other version
#key → special keyword argument (fixed name)

min_key = min(d,key = d.get)
print(min_key)