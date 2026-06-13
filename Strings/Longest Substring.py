s=input()
d={}
d[0]=[]
for i in range(len(s)+1):
    res=[]
    for j in range(i,len(s)):
        if s[j] not in res:
            res.append(s[j])
        else:
            d[len(res)]=res
            break
    d[len(res)]=res
print(max(d.keys()))
