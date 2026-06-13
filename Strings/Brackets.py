s='([[{}]])'
def is_valid(s):
    S=[]
    pairs={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in s:
        if char in '({[':
            S.append(char)
        else:
            if not S:
                return False
                
            top=S.pop()
            if top != pairs[char]:
                return False
                
    return len(S)==0
print(is_valid(s))
