d = {"Name":"Chanlee", "Age": 25, "City": "New York"}

#print keys
print("The keys of the dictionary are:", d.keys())

#print values
print("The values of the dictionary are:", d.values())

#print items
print("The items of the dictionary are:", d.items())

#Add a new key-value pair to the dictionary
d["Occupation"] = "Validation Engineer"
print("The updated dictionary is:", d)

#Remove a key-value pair from the dictionary
del d["City"]
print("The updated dictionary after removing the key 'City' is:", d)

#Check if a key exists in the dictionary
if "Age" in d:
    print("The key 'Age' exists in the dictionary.")
    print("The value of the key 'Age' is:", d["Age"])
else:
    print("The key 'Age' does not exist in the dictionary.")   

#dict copy
d_copy = d.copy()
print("The copy of the dictionary is:", d_copy) 
