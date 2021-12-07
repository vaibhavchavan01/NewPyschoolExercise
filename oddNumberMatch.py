import re
print(re.findall('([13579])([a-z])', '1a2b3c'))#match odd number and tuples with only character

print(re.findall('([0-9])\\1', '1233455'))

print(re.findall(r'([a-z,0-9])\1', 'a1bb222c3dd444'))

