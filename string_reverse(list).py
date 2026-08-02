def reverse_string(s):
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)
s = input("Enter the string: ")
print(reverse_string(s))
