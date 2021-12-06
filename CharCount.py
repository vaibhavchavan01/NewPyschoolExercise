def countX(s,i, count):
    if i == len(s)-1:
        return count
   
    elif s[i] == 'X':
        i = i+1
        count+=1
        return countX(s, i, count)

    else:
        i+=1
        return countX(s, i, count)
s="aaXaXaax"
count=0
i=0
print(countX(s,i,count))