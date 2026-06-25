l= ["apple", "education", "ice", "ocean", "python", "umbrella"] 
#Expected Output: ['education', 'umbrella']

def vowel_list(l):
    new=[]
    for word in l:
        if word[0] in "aeiouAEIOU":
            if len(word)>5:
                new.append(word)

    return new

my_list = vowel_list(l)
print(my_list)            
