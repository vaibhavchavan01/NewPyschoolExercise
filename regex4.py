import re
a="abbcccd1234ABCD"
print(re.findall('0-9',a))

print(re.findall('a-z',a))

print(re.findall('A-Z',a))
