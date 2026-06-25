dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

new_dict={}

def merge_dict(d1,d2):
   
    for k1,v1 in d1.items():
       if k1 in d2:
           new_dict[k1] = v1+d2[k1]
       else:
           new_dict[k1] = v1

    for k2,v2 in d2.items():
        if k2 not in new_dict:
            new_dict[k2] = v2

    return new_dict        
              
d = merge_dict(dict_a,dict_b)
print(d)


