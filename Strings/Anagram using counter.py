from collections import Counter

s1 = "listen"
s2 = "silent"

if Counter(s1) == Counter(s2):
    print("Anagram")
else:
    print("Not Anagram")
