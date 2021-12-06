#code no-08
def addDashes(str1, s, i):
    if i==len(s)-1:
        str1+=s[i]
        return str1
    else:
        str1+=s[i]+'-'
        i+=1
        return addDashes(str1, s, i)
str1=""
s="google"
i=0
print(addDashes(str1, s, i))
#outputis - g-o-o-g-l-e 