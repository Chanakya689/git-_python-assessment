#default values in dictionary

from collections import defaultdict
d = defaultdict(int)
print(d["name"])

d = {"name":"lee","age":24}

print(d.get("name","Unknown"))
print(d.get("city","None"))
a = d.get("occupation","None")
print(a)