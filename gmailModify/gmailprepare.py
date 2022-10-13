import os ,ezgmail

# should transform credential.json file to the same path and change the path in python look down 

os.chdir(r'C:\Users\احمد شعبان\Desktop\Work Folders\acadmy test\project\gmailModify')

ezgmail.init()

#     if you forget the email name 
print(ezgmail.EMAIL_ADDRESS)        #  =>  mohamedtelb200@gmail.com 


#       ======   send message  (email name  , title , body ,[ more than picture and should be exist in the same path] , )
ezgmail.send('mohamedtelb200@gmail.com ' , 'title test' , 'the body of the test')



#=  ========================================================================================
#  ====================== Read  unread messages    => to know messages that you dont read write in your gmai   is:unread
unreadMmessage = ezgmail.unread()
# print(ezgmail.summary(unreadMmessage))    # => will return maximum 25 messages

print(len(unreadMmessage))
print(unreadMmessage[0])


# =======================================
#-----------------------------------------   bring the leatest 25 messages weather it read or not      ----

leatest = ezgmail.recent()
# print(ezgmail.summary(leatest)) 
print(len(leatest))

#=====================================
#    to incease count of maxmium
leatest = ezgmail.recent(maxResults=50)
print(len(leatest))


#=====================================
#    to search in gmail
searshresult = ezgmail.search('test')
print(len(searshresult))
# print(ezgmail.summary(searshresult))