word1 = "listen"
word2 = "silent" 

#Expected Output: Is "listen" an anagram of "silent"? True

def anagram_check(w1,w2):
    s1 = sorted(w1)
    s2 = sorted(w2)
    if s1==s2:
        print("{} an anagram of {} True ...!!!".format(w1,w2))
    else:
        print("Not an angarm {} and {}".format(w1,w2))  

anagram_check(word1,word2)          