
'''to print from the terminal'''


import sys
if len(sys.argv) == 1:
    l =open('file.txt','r')
    p =l.readlines()
    count =0
    for i in p:
        count +=1
        if count == 5:
            break
        else:
            print(i)
        
else:
    print('wrong')

