s = "A man, a plan, a canal: Panama" 
#Expected Output: True

#words = s.split()
def palindrome_check(s):
    sentance = ""
    for i in s:
        if i.isalpha():
            sentance+=i.lower()
            
    if sentance == sentance[::-1]:
        return True
    else:
        return False    
  

if (palindrome_check(s)):
    print("palindrome")
else:
    print("Not")    
    
