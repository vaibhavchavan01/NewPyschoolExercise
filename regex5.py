import re
print(re.findall('abc|123|efg', '123abcefg')) #check either abc either 123 either efg

print(re.findall('1|2','123'))   

print(re.findall('abc|123','a1b2c3'))  #check whether continuous char