import re
a = re.search('.com', 'abc@gmai.com')
print(a.group())

b = re.search('(d+)c(d+)', 'a1b22c333d4444')
print(b)