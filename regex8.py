import re
print(re.findall('\w', '1a2b3c^'))#matching only some specific character


print(re.findall('\W', '1a2b3c!@#$%^&*'))
