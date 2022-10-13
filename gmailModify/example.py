import imp
import smtplib ,openpyxl
from turtle import stamp
from pathlib import Path

#define  excel file
file = openpyxl.load_workbook(Path.home() / Path()) 
# define all papers 
sheets = file.sheetnames
# define paper i need 
sheet = file['Sheet1']
#define last column
lastcolumn = sheet.max_column
# define the cell 
lastcell = sheet.cell(row=1 ,column=lastcolumn).value
# creat emty dict to pass data to it
myclient = {}
# creat for start from the second row 
for i in range(2,sheet.max_row +1):
    pyment = sheet.cell(row=i ,column=lastcolumn).value
    if pyment != 'paid':
        name =sheet.cell(row=i,column=1).value
        email =sheet.cell(row=i,column=2).value
        #add to dict
        myclient[name]=email


# send email 
#define protocol
stmobj = smtplib.SMTP('smtp.gmail.com' ,587)
stmobj.starttls()

# define sender 
seder = 'mohamedtelb200@gmai.com'
password = 'mu0529452894'
stmobj.login(seder ,password)

#define reciver
for name ,email in myclient.items():
    body = 'subject:%s dues unpaid. \n dear %s, \n please send %s to complete participation '%(lastcell ,name ,lastcell)

    send = stmobj.sendmail(seder ,email ,body)

stmobj.quit()



