import csv
filename= 'newfile.csv'
with open(filename, "w") as f:
    f.write('Date'+'\t\t'+'Month'+'\t\t'+'year')
    f.write('\n'+'07/12/2021'+'\t'+'december'+'\t'+'2021')
    f.write('\n'+'IP address'+'\t\t'+'Host')
    f.write('\n'+'127.0.0.1'+'\t\t'+'localhost')