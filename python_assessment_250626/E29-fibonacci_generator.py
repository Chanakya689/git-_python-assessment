#Create a generator function that yields Fibonacci numbers up to N. 
#Instead of returning a full list, it should yield values one by one. 
# Given Input: n = 8
#Expected Output: First 8 Fibonacci numbers: 0 1 1 2 3 5 8 13

def fibonacci_gen(n:int):

    a,b=0,1
    while n>0:
        yield a
        a,b=b,a+b
        n-=1
        



value = fibonacci_gen(8)
for i in value:
    print(i,end=" ")    