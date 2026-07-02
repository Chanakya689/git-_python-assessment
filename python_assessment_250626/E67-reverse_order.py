#Create a script where number will be printed in reverse order using recursive method

def print_reverse(n):
    if n < 1:
        return
    print(n,end= " ")
    print_reverse(n - 1)

print_reverse(5)