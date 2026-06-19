d = {"a":"lee","b":"chan","c":"jay","d":"git"}
l=["a","d"]

for key in l:
    #del d[key]
    d.pop(key,"NONE")
print(d)    