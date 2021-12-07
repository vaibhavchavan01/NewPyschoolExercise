def readFile(filename):
    #f = open(filename)
    with open(filename, "rb") as f:
        count = 0
        count2 = 0
        while True:
            byte = f.read(1)
            if not byte:
                break
            count+=1
            if byte == '\n':
                count2+=1
        print(count)
        print(count2)
        return (count, count2)
n1='demo.txt'
print(readFile(n1))