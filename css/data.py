import csv
from pathlib import Path

# Read 

file = open(Path.home() / Path('D:','csv','employees_1.csv'))
read = csv.reader(file)   # => this is object
# shall pass all values to list

# data = list(read)
# print(data)
# print(data[1][0])
# print(data[1][1])
# print(data[1][2])

for row in read:
    print('Row #' + str(read.line_num )+ ''+ str(row))   # => to print the number of the line use  =>> reader.line_num



# =============================================================================================================
#  Write ----------------------------------------------
my_file = open(Path.home() / Path('D:','csv','employ_1.csv'),'a' ,newline='') # => to not leave empty line
writer = csv.writer(my_file)  # => this is object
"""mode => a  =append to list yet,, mode w delete the old value and write new one"""
# add data
# writer.writerow(['Ahmed',1000,'10/05/2022'])
# my_file.close()

# =============================================================================================================
#  TO write multi line  ----------------------------------------------
header = ['name','salary','date']
data = [
    ['mu',500,'20/01/2022'],
    ['ramy',1400,'17/02/2022'],
    ['frid',400,'10/03/2022'],
    ['jmi',1700,'20/12/2022']
    ]
writer.writerow(header)
writer.writerows(data)
my_file.close()

#=============================================================

#delimiter     ,,lineterminator
# my_file = open(Path.home() / Path('D:','csv','employees_1.csv'),'a' ,newline='') # => to not leave empty line
# writer = csv.writer(my_file ,delimiter='\t',lineterminator='\n-----------------\n')
# writer.writerow(['Ahmed',1000,'10/05/2022'])
# my_file.close()


