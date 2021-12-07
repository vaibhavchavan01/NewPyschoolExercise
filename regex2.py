import re
a="abcde"
print(re.findall('.',a))

print(re.findall('^a',a))

print(re.findall('.$',a))