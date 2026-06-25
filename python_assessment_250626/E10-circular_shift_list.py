l = [1, 2, 3, 4, 5]
shift=2
dir = "left" 
#Expected Output: [4, 5, 1, 2, 3]

def circular_rotation(l,shift,dir):
    for i in range(shift):
       
        if dir == "right":
            a = l[-1]  
            for j in range(len(l)-1,-1,-1):
                l[j] = l[j-1]

            l[0] = a
                
        elif dir == "left":
            a = l[0]
            for j in range(0,len(l)-1,1):
                l[j] = l[j+1]        
            
            l[-1] = a
        
    print(l)

circular_rotation(l,shift,dir)            
            


        

