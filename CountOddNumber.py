#Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.
def countOddNumber(list1):
    count=0
    for i in range(1,len(list1),3):
        if(i%2!=0):
            count+=1
    print(count)
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
countOddNumber(list1)
