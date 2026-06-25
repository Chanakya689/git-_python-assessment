d = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}

print("The original nested dictionary is:", d)
def access_nested_dict(nested_dict, key1, key2):
    if key1 in nested_dict and key2 in nested_dict[key1]:
        return nested_dict[key1][key2]
    else:
        return None

# Example usage:
name = access_nested_dict(d, "person1", "name")
age = access_nested_dict(d, "person2", "age")

print("Name of person1:", name)
print("Age of person2:", age)   