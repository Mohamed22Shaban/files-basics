



import bs4
import requests
from pathlib import Path
import csv




my_link = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
sel = bs4.BeautifulSoup(my_link.text,'html.parser')

table_soup = sel.find_all('table')
fiier_table = [table for table in table_soup if table.caption is not None]  # caption => title of the table
# print(fiier_table)
empty = None                    # => make none to take the value that i need   => taable
for element in fiier_table:
    if str(element.caption.text).strip() == 'Top languages by population per Nationalencyklopedin':
        empty =element      # => now empty take the define table 
        break
# print(requr)

rows = empty.find_all('tr')
headers = [head.text.replace('\n','') for head in rows[0].find_all('th')]
print(headers)

l = []
for row in rows :
    value = row.find_all('td')
    value_text = [mm.text.strip() for mm in value]


    l.append(value_text) # => should add to list in order to add to csv file




my_file = open(Path.home() / Path('D:','csv','employees_1.csv'),'a' ,newline='') 
writer = csv.writer(my_file) 

writer.writerows(l)
my_file.close()



##  Notice 
l = ['mu','kamel','jmi']
g = [ i for i in l if len(l) == 3]
print(g)