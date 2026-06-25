d = {"Name":"Chanlee","Hobby":"Table Tennis","City":"Banglore"}

print("Sorted by Keys:")
print(dict(sorted(d.items())))
print()

print("Sorted by values:")
print(dict(sorted(d.items(),key=lambda x:x[1])))