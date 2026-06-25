d = {1:"lee",2:"chan",3:"jay"}

new_d = d.fromkeys(d.keys(),0)
print(d)
print(new_d)

#Another version

for key in d:
    new_d[key]=0
print(new_d)