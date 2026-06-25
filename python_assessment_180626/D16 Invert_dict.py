#invert dict
#key becomes value
#value becomes key

di = {"Name":"lee","Age":24,"City":24}
i={}
for k,v in di.items():
    i.setdefault(v,[]).append(k)
print(i)

#or

from collections import defaultdict

fd = defaultdict(list)
for k,v in di.items():
   #fd[v]=k overrides the previous data
   #Adds the data to the same key and values in the list
   fd[v].append(k)

print(dict(fd))   
