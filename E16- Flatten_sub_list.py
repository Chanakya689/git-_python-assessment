l=[[1,2],[3,4],[5,6]]

print("The original nested list is:", l)
flattened_list = [item for sublist in l for item in sublist]
print("The flattened list is:", flattened_list)