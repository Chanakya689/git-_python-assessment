words = ["apple", "bat", "cherry", "dog", "elderberry"]
new_list=[]

def remove_shorter_str(l):
    
    for word in l:
        if len(word)>4:
            word = word.upper()
            new_list.append(word)

remove_shorter_str(words)
print(new_list)
