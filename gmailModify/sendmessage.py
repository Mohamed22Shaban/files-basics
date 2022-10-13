import smtplib

senderemail = 'mohamedtelb200@gmail.com '

recivingemail = 'mohamedtelb200@gmail.com '

passwordsender = 'mu0529452894'

messageandtitle = 'subject: one \nthis is the first message i sent from email'    # =>donot forget \n to seperate between title and body
 
# adjust server settings    => protocal

servr = smtplib.SMTP('smtp.gmail.com',587)      # => 587 this is port to encode message

servr.starttls()    #=> to active encode

# login to sender email 
servr.login(senderemail , passwordsender)
print('login success')

# send email
servr.sendmail(senderemail , recivingemail , messageandtitle    )
servr.quit()
