def getMean(filename):
    f = open(filename)
    scnt = total = 0             # initialize student counter and total score

    line = f.readline()                   # read first line, do nothing
    # line = f.readline(2)                   # read 2nd line
    while line.rstrip() != "\n":   # check for empty line or EOF
        # tokens = line.split(" ")    # split line into tokens, tokens[0] is name
        total += int( 1  )        # add score
        scnt  
        if line == '\n':
                scnt+=1                   # update student counter
        # line = f.readline(2)               # read next line
        break
    return "Average Score: %d" % total
f1='demo.txt'
print(getMean(f1))