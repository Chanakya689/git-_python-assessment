#Comparing Tuples

t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(t1 == t2)   # False
print(t1 < t2)    # True
print(t1 > t2)    # False

#Removing Duplicates from Tuple

t = (1, 2, 2, 3, 4, 4)

new_t = tuple(set(t))
print(new_t)

#Filter Tuples

t = (10, 15, 20, 25, 30)

# keep only even numbers
new_t = tuple(x for x in t if x % 2 == 0)
print(new_t)

#Map Tuples

t = (1, 2, 3, 4)
new_t = tuple(x * 2 for x in t)
print(new_t)

#Modify Tuple

t = (1, 2, 3)

temp = list(t)
temp[1] = 20
t = tuple(temp)

print(t)


#Sort a Tuple of Tuples by 2nd Item

t = ((1, 3), (2, 1), (4, 2))

# sort based on second element
sorted_t = tuple(sorted(t, key=lambda x: x[1]))

print(sorted_t)

#Count Elements

t = (1, 2, 3, 2, 4, 2)

print(t.count(2))


#Check if all items are the same

t = (5, 5, 5, 5)

print(all(x == t[0] for x in t))