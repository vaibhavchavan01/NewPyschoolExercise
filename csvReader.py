import csv
def csvReader(filename):
    records = []
    for line in open(filename):
        line = line.rstrip()  # strip '\n'
        if line=='':
            continue
               # ignore empty line
    records.append(line)
    return records 
f1='newfile.csv'
csvReader(f1)