l = [1, 2, 3] 
#Expected Output: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]


def power_set(l):
    result = [[]]
    
    for elem in l:
        print("------->",elem)
        new_subsets = []
        for subset in result:
            print("subset:-",subset)
            new_subsets.append(subset + [elem])
            print("new_subsets:-",new_subsets)
        result.extend(new_subsets)
        print("result:--->",result)
    
    return [tuple(x) for x in result]

l = [1, 2, 3]
print(power_set(l))
