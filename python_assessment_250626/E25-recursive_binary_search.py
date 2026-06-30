l = [10, 20, 30, 40, 50, 60]
Target = 50 
#Expected Output: Target found at index: 4

def binary_search(l,low,high,target):
    
    if low>high:
        return -1
        
    mid = (low+high)//2

    if l[mid] == target:
        return mid
    
    if target<l[mid]:
        return binary_search(l,low,mid,target)
    else:
        return binary_search(l,mid+1,high,target)
    


result = binary_search(l,0,len(l)-1,Target) 
if result != -1:
    print("Result of targted inedx:-",result) 
else:
    print("Element not in the list")    
  