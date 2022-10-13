import  PyPDF2

open_file = open(r'C:\Users\احمد شعبان\Desktop\Work Folders\file1.pdf' , 'rb')

read_file = PyPDF2.PdfFileReader(open_file)

# know number of its pages
print(read_file.numPages)

#read the cointain page
read_first_page = read_file.getPage(2)
print(read_first_page.extractText())
open_file.close()                       #=> should close the file