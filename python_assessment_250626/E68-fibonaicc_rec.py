def fibonaicc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaicc(n-1) + fibonaicc(n-2)
    
for i in range(9):
    print(fibonaicc(i), end=" ")    
