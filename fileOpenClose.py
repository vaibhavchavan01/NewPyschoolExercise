def addEmail(filename, name, email):
    with open(filename, "w") as f:# replace the mode
    
    # Append name and email, each record should end with '\n'.

    # close file
        f.write(name +"\n"+ email)
        
        f.close()
        return f # do not remove this line 
f1 = 'demo.txt'
f2 = "Amazatic"
f3 = "amazatic@gmail.com"
print(addEmail(f1, f2, f3))
