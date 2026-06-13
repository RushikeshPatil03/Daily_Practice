#Reverse the order of words in string
s=input()
words=s.split()
result=''
for word in words[::-1]:
    result+=word+' '
print(result.strip())
