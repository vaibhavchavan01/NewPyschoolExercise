import re
print(re.findall('\d', '1a2b3c'))#matches any decimal number

print(re.findall('\D', '1a2b3c'))#matches non decimal number

print(re.findall('.?\d\D', '1a2b3c'))