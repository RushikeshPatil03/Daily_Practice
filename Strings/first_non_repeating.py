from collections import Counter
def first_non_repeating(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None
s=str(input())
print(first_non_repeating(s))
