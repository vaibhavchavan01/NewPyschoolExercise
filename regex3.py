import re
a="abbcccd"
print(re.findall('.{1,3}',a))# make 3 character group

print(re.findall('.d$',a))# '.' denotes character before the d char.

print(re.findall('.+',a))# all string