nums = [1, 2, 3, 4, 5, 6] 
#Expected Output: [4, 16, 36]


def even_squares(l):
    result = list(map(lambda x:x**2,filter(lambda x:x%2==0,l)))
    print(result)

even_squares(nums)