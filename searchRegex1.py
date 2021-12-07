import re
a = re.search('(\d+)/(\d+)', 'Using pi=22/7, compute ...')
print(a.groups())

b = re.search('\.+', '++++.......+++') 
print(b.start())