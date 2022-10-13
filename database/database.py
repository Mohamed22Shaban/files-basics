
from importlib.resources import path
import sqlite3
con =sqlite3.connect('data.db')
cur =con.cursor()
cur. execute('create table if not exists students(FirstName varchar(20),LastName varchar(20),age integer)')

# add data to table 
cur.execute('insert into students values("muhammed" ,"shaban" ,31)')



#        ===================================================
# bring data from database 
cur.execute('select FirstName,age from students')  # or = >'select * from students
# print(cur.fetchall())          #return list   all element
# print(cur.fetchone())          #return tubles one element 
print(cur.fetchmany(2))          #determin count of lines 


con.commit()    #should save changes
con.close()     #should close data after finish


# ======================================================================
#  ----- Update  data---------

cur.execute('update students set age = 30 where id =2')
con.commit()


# ======================================================================
# -------- Delete date------------

cur.execute('delete from students  where id =2')
con.commit()



# ======================================================================

# adding data from csv file

from pathlib import Path
import csv
# # add data to table 
# my_file = open(Path.home() / Path('D:','csv','employ_1.csv'))
# read_by_dict = csv.reader(my_file)
# # print(read_by_dict)
# cur.executemany('insert into employe values(?,?,?)',read_by_dict)       # => Notice executemany
# con.commit()    #should save changes
# con.close()     #should close data after finish
 

#================================================================================

# add data to Excel file

import openpyxl
cur.execute('select FirstName,age from students')
dat = cur.fetchall()
# con.commit()    #should save changes
p =openpyxl.Workbook()
sheet = p.active

i = 0
for row in dat:
  i += 1
  j = 1
  for col in row:
    cell = sheet.cell(row = i, column = j)
    cell.value = col
    j += 1
p.save(filename=r'C:\Users\احمد شعبان\Desktop\Work Folders\war.xlsx')
con.close()     #should close data after finish

print('data added')



