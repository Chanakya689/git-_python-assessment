d = {"Name":"Chan","Age":24,"Location":"Banglore"}

d["N"] = d["Name"]
del d["Name"]

print(d)

#Another version pop()
#if old key doesn't exist use pop()

d["City"] = d.pop("Locations","None")
print(d)