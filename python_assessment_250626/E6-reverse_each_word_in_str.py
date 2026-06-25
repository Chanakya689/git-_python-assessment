s = "Python is awesome" 
#Expected Output: "nohtyP si emosewa"

new = []

def reverse_str(s):
    
    for word in s.split():
        w = word[::-1]
        new.append(w)

    return " ".join(new)

print(reverse_str(s))

        
