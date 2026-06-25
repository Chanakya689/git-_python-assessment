d = {"Chanlee":900,"lee":800,"Brucelee":1000,"Jay":777}

value = int(input("Enter the value you want to check in dictionary:"))

#Membership operators {"in","not in"}
if value in d.values():
    print("Value is present in dict")
else:
    print("Value is not in")