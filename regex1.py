import re
a="abcde"
print(re.findall('.*',a))

print(re.findall('.+',a))

print(re.findall('.?',a))