mf = open(r'C:\Users\احمد شعبان\Desktop\acadmy test\project\excercises\file.txt','r')

print(mf.name)
print(mf.mode)

lines = mf.readlines()
count =0
for line in lines:
    print(line)
    count += 1
    if count == 5:
        break
mf.close()

#=================================================================================
# ------------  to copy fies -------------------------
from pathlib import Path
import shutil
import os

# 1) copy Files **
# shutil.copy(r'C:\Users\احمد شعبان\Desktop\acadmy test\project\excercises\file.txt',r'C:\Users\احمد شعبان\Desktop\asas\folder')

# 2) copy Files**
# shutil.copytree(Path.home() / Path(r'D:','Pictures','mu'),Path.home() / Path(r'C:','Users','mu'))

# 3) move Files **
# shutil.move(Path.home() / Path('C:','Users','احمد شعبان','Desktop','acadmy',' test','project','excercises','muu.txt'),Path.home() / Path('D:','Pictures','haaa'))
# shutil.move(r'C:\Users\احمد شعبان\Desktop\acadmy test\project\excercises\muu.txt','D:\Pictures\haaa')

# 4) delet files **

# os.unlink(r'D:\Pictures\haaa\muu.txt')

# 5) delete empty folder **
# os.rmdir(r'D:\Pictures\haaa\kk')

# 6) delete full folder **
# shutil.rmtree(r'D:\New folder')


import zipfile
import re

# # compress File
# new = zipfile.ZipFile('compact.zip' , 'w')
# new.write(r'C:\Users\احمد شعبان\Desktop\asas\aa.txt')

# compress folder
# shutil.make_archive('CompressFile','zip',r'C:\New folder')

# extract folder
# new.extractall()

# to new file's name in this folder   => to change name of file

format = '^(.*?)-((0|1)?\d)-((19|20)\d\d)(.*?)$'
for i in os.listdir(Path.home() / Path('C:','Users','احمد شعبان','Desktop','happy')):
    searsh = re.search(format , i)
    if searsh == None:
        continue
    before = searsh.group(1)
    day = searsh.group(2)
    month = searsh.group(3)
    year = searsh.group(4)
    after = searsh.group(5)

    emerge = before + day + '-'+ month + '-'+ year + after 
    print(f'rename "{i} " to "{emerge}"')

    oldName = Path.home() / Path('C:','Users','احمد شعبان','Desktop','happy')/i
    newName = Path.home() / Path('C:','Users','احمد شعبان','Desktop','happy')/emerge
    shutil.move(oldName , newName)
