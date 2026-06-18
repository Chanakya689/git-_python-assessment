#printing nested dictionary

d = {"Student":{"name":"Lee","age":24,"Roll":{"Lee":1,"chan":{"History":1971}}}}
print(d["Student"]["age"])
print(d["Student"]["Roll"]["Lee"])
print(d["Student"]["Roll"]["chan"]["History"])

