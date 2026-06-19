#changing values in nested dict

d={"student":{"Name":"Chanlee","Age":{"Chanlee":1,"lee":24}}}
print(d)
d["student"]["Age"]["Chanlee"]=100
print(d)

