import imapclient

# reciving gmail
imapobj = imapclient.IMAPClient('imap.gmail.com', ssl=True)     #encode => ssl

# login to gmail that i need to bring messagesfrom it 

rec_email ='judimuhammed512@gmail.com'
password = 'rheem2022'

imapobj.login(rec_email ,password)

# define the box that bring messages from it

# toprint all boxes

import pprint
pprint.pprint(imapobj.list_folders())

# select folder
imapobj.select_folder('inpox' ,readonly= True)

# searsh     = > will give unique id  and the should pass to the method "fech"
ps = imapobj.search(['all'])     #  ,,    impamobj.search(['on 05-jul-2020'])    ,,  impamobj.search(['since 01-2-1990'])
print(ps)


# first install setuptools-54.1.1  then installed pyzmail36

import pyzmail
message = pyzmail.PYZMessage.factory(ps[number][b'body[]'])    #=> b = its binary numbery

print(message.get_address)
 
# to get body of message
print(message.test_part.get_payload().decode(message.text_part.charser))