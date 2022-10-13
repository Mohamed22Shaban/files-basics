
''' must input file name and the number which need during the terminal so use =>   sys  '''

import openpyxl , sys
from openpyxl.styles import Font

# to know how many inputs the user enter 
if len(sys.argv) == 2:
    #to make sure user input is int
    try:
        number = int(sys.argv[1])           #=> this is the number that i input in the terminal  => 5
    
    except Exception as e:
        print(e)
    
    excel_file = openpyxl.Workbook()
    sheet = excel_file.active

    # we need tow loops one for rows and the second for columns
    for row in range(number + 1):
        for column in range(number + 1):

            header =False

            if column == 0 and row == 0:      # if the first cell is empty 
                header = True
                n = ''

            elif column == 0 :
                header = True
                n = row

            elif row == 0 :
                header = True
                n = column
            
            else:
                n =column * row

            # identify the cell 
            cell = sheet.cell(row= row+1 , column= column +1)

            # to make the first cells bold 

            if header:
                cell.font = Font(bold= True)

            # add the value of n to the cell

            cell.value = n
    saved_file = str(r'C:\Users\احمد شعبان\Desktop\Work Folders\multiplication_table') + str(number) + '.xlsx'
    excel_file.save(saved_file)

    print( ' to run the program write in terminal "python multiplicationTable.py 5"')    #=<< name of the page



else:
    print('Too Many Value')


