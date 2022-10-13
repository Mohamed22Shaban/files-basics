import os
import PyPDF2
from PyPDF2 import PdfFileWriter as w
from pathlib import Path


l = []

#create for to pass on files in the folder---
for file_name in os.listdir(Path.home() / Path('D:','paperwork')):
    if file_name.endswith('pdf'):
        l.append(file_name)

l.sort(key=str.lower)
pdf = w()

# open all files
for file_name in l:
    open_file = open(Path.home() / Path('D:','paperwork',file_name), 'rb')

    #read files
    read = PyPDF2.PdfFileReader(open_file)

    for pagnum in range(1 , read.numPages):
        ff = read.getPage(pagnum)
        pdf.addPage(ff)

# result file
pdfoutput = open(Path.home() / Path('D:','paperwork','article.pdf'), 'wb')
pdf.write(pdfoutput)
pdfoutput.close()






