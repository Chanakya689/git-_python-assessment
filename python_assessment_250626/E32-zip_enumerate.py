names = ["Alice", "Bob", "Charlie"] 
scores = [85, 92, 78]
#Output: 
# Rank 1: Bob scored 92 
# Rank 2: Alice scored 85 
# Rank 3: Charlie scored 78

def zip_enumerate(l1,l2):
    #reverse=false by default-->ascending order(optional)
    #reverse=true manually done-->descending order

    data = sorted(zip(l1,l2),key=lambda x:x[1],reverse=True)

    for index,(name,score) in enumerate(data,start=1):
        print(f"Rank {index}:{name} scored {score}")
      
zip_enumerate(names,scores)        