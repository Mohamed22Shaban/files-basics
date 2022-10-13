import csv
from pathlib import Path
import os

# file = open(Path.home() / Path('D:','csv','employees_1.csv'))
# read_by_dict = csv.DictReader(file)    #= > it consider the first line is the header

# for row in read_by_dict:
#     print(row['Name'],row['Salary'] ,row['Date'])

# file.close()
# ================================================================================
# werite from dict 

# file = open(Path.home() / Path('D:','csv','text.csv'),'a',newline='')
# read_by_dict = csv.DictWriter(file,['Name','Salary','Date'])    #= > it consider the first line is the header

# read_by_dict.writeheader()
# p ={
#     'Name':'aza','Salary':1000,'Date':'10/10/2022'
# }
# read_by_dict.writerow(p)
# file.close()



#        =================================================================

#        to delete the first line in the file
l = []
for f in os.listdir(Path.home() / Path('D:','csv')):
    if f .endswith('csv'):
        l.append(f)

for j in l:
    file = open(Path.home() / Path('D:','csv',j))
    read_by_dict = csv.reader(file)
    for k in read_by_dict:
        if read_by_dict.line_num == 1:
            continue
        print('Row #' + str(read_by_dict.line_num )+ ''+ str(k))
