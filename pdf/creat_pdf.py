import PyPDF2
from PyPDF2 import PdfFileWriter as w

# creat object
pdf = w()
file = open(r'C:\Users\احمد شعبان\Desktop\Work Folders\acadmy test\project\pdf\inastance.pdf' , 'wb')

for i in range(5):          # identify number of pages
    pdf.addBlankPage(219,297)  #= add dimantion
    pdf.write(file)


# copy 
# identify coping file
open_file = open(r'C:\Users\احمد شعبان\Desktop\Work Folders\file1.pdf' , 'rb')

read_file = PyPDF2.PdfFileReader(open_file)

for i in range(read_file.numPages):
    ff = read_file.getPage(i)
    pdf.addPage(ff)

pdf.write(file)
file.close()
