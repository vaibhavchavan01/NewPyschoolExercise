import re 
print(re.findall('.com','abc@gmail.com'))

print(re.findall('[aeiou]','pyschool'))#matching set of character

print(re.findall('[3-6]', '12345678'))# match element from 3 to 6

print(re.findall('[^3-6]', '12345678'))#[^] meaning of this is neglecting number 
