#Making use of the 'break' statement to abort a 
# for/while loop, and move to the code after the loop block .	
def break_statement(num):
    for i in range(num):
        if i==int(num/2):
            break
        print(i)
a=int(input("enter the number: "))
break_statement(a)