# A mxn matrix, m rows and n columns, can be represented using nested lists.
# Write a function that returns the diminensions of a matrix.
def matrixDimensions(m):
    i = j = 0
    l=len(m[0])
    for i in range(0,len(m)):
        if l != len(m[i]):
            return "This is not a valid matrix."
        for j in range(0,len(m[i])):
            continue
    return "This is a "+str(i+1)+"x"+str(j+1)+" matrix." 
a = [[1, 3,5],[-5,8,4],[2, 4,2]]
print(matrixDimensions(a))